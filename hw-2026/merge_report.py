import argparse
import importlib
import re
from pathlib import Path


def normalize_name(name: str) -> str:
	"""Normalize a student name for matching.

	- Removes all whitespace (for names like "王 小明").
	- Removes '*' gender marker in student list.
	"""
	if name is None:
		return ""
	text = str(name).strip()
	text = text.replace("*", "")
	text = re.sub(r"\s+", "", text)
	return text


def find_column_index_by_header(ws, header_name: str) -> int:
	"""Find a column index by exact header text in the first row."""
	for col in range(1, ws.max_column + 1):
		value = ws.cell(row=1, column=col).value
		if value is not None and str(value).strip() == header_name:
			return col
	raise ValueError(f"在表头中未找到列: {header_name}")


def find_f_columns(ws, start_col: int = 4) -> list[int]:
	"""Find columns from start_col whose headers match F1/F2/... pattern."""
	f_cols: list[int] = []
	for col in range(start_col, ws.max_column + 1):
		header = ws.cell(row=1, column=col).value
		if header is None:
			continue
		header_text = str(header).strip().upper()
		if re.fullmatch(r"F\d+", header_text):
			f_cols.append(col)
	return f_cols


def parse_numeric_value(value):
	"""Return numeric value if cell content is numeric; otherwise return None."""
	if value is None:
		return None
	if isinstance(value, (int, float)):
		return value

	text = str(value).strip()
	if not text:
		return None

	# Accept plain numeric strings only, like 95, -3, 87.5, .5
	if re.fullmatch(r"[+-]?\d+", text):
		return int(text)
	if re.fullmatch(r"[+-]?(?:\d+\.\d*|\.\d+)", text):
		return float(text)

	return None


def merge_scores(student_list_path: Path, report_path: Path, output_path: Path) -> None:
	try:
		openpyxl = importlib.import_module("openpyxl")
	except ModuleNotFoundError as exc:
		raise ModuleNotFoundError(
			"缺少依赖 openpyxl，请先执行: pip install openpyxl"
		) from exc

	load_workbook = openpyxl.load_workbook
	wb_students = load_workbook(student_list_path)
	wb_report = load_workbook(report_path, data_only=True)

	ws_students = wb_students.active
	ws_report = wb_report.active

	student_name_col = find_column_index_by_header(ws_students, "姓名")
	report_name_col = find_column_index_by_header(ws_report, "姓名")

	report_f_cols = find_f_columns(ws_report, start_col=4)
	if not report_f_cols:
		raise ValueError("成绩报表中未找到从 D 列开始的 F* 列（如 F1/F2）。")

	# Build name -> row map from report table.
	report_row_by_name: dict[str, int] = {}
	duplicate_names: set[str] = set()
	for row in range(2, ws_report.max_row + 1):
		raw_name = ws_report.cell(row=row, column=report_name_col).value
		norm_name = normalize_name(raw_name)
		if not norm_name:
			continue
		if norm_name in report_row_by_name:
			duplicate_names.add(norm_name)
			continue
		report_row_by_name[norm_name] = row

	target_start_col = 7  # G

	# Maintain destination headers from report F* headers.
	for offset, report_col in enumerate(report_f_cols):
		target_col = target_start_col + offset
		ws_students.cell(
			row=1,
			column=target_col,
			value=ws_report.cell(row=1, column=report_col).value,
		)

	matched = 0
	not_found = 0
	skipped_non_numeric = 0
	unmatched_names: list[str] = []
	for student_row in range(2, ws_students.max_row + 1):
		raw_name = ws_students.cell(row=student_row, column=student_name_col).value
		norm_name = normalize_name(raw_name)
		if not norm_name:
			continue

		report_row = report_row_by_name.get(norm_name)
		if report_row is None:
			not_found += 1
			unmatched_names.append(str(raw_name) if raw_name else "(空)")
			continue

		matched += 1
		for offset, report_col in enumerate(report_f_cols):
			target_col = target_start_col + offset
			raw_score = ws_report.cell(row=report_row, column=report_col).value
			numeric_score = parse_numeric_value(raw_score)
			if numeric_score is None:
				skipped_non_numeric += 1
				continue
			ws_students.cell(
				row=student_row,
				column=target_col,
				value=numeric_score,
			)

	wb_students.save(output_path)

	print(f"已完成合并，输出文件: {output_path}")
	print(f"共识别 F* 列数量: {len(report_f_cols)}")
	print(f"匹配成功人数: {matched}")
	print(f"未匹配人数: {not_found}")
	print(f"已忽略非数字成绩项数量: {skipped_non_numeric}")
	
	if unmatched_names:
		print("\n未匹配的学生名单：")
		for name in unmatched_names:
			print(f"  - {name}")
		
		unmatched_file = output_path.parent / f"{output_path.stem}_unmatched.txt"
		with open(unmatched_file, "w", encoding="utf-8") as f:
			f.write("未匹配的学生名单\n")
			f.write("=" * 30 + "\n")
			for name in unmatched_names:
				f.write(f"{name}\n")
		print(f"未匹配名单已保存到: {unmatched_file}")
	
	if duplicate_names:
		print(f"\n警告: 成绩报表中有重名（按清洗后姓名），已忽略后续重复项，数量: {len(duplicate_names)}")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="按姓名将成绩报表中的 F* 列合并到学生成绩名单。")
	parser.add_argument(
		"student_list",
		nargs="?",
		default="StudentNames.xlsx",
		help="学生成绩名单 Excel 路径，默认 StudentNames.xlsx",
	)
	parser.add_argument(
		"report",
		help="当前成绩报表 Excel 路径（包含姓名与 F* 列）",
	)
	parser.add_argument(
		"-o",
		"--output",
		default=None,
		help="输出 Excel 路径。默认覆盖 student_list 文件。",
	)
	return parser.parse_args()


def main() -> None:
	args = parse_args()

	student_list_path = Path(args.student_list)
	report_path = Path(args.report)
	output_path = Path(args.output) if args.output else student_list_path

	if not student_list_path.exists():
		raise FileNotFoundError(f"未找到学生成绩名单文件: {student_list_path}")
	if not report_path.exists():
		raise FileNotFoundError(f"未找到成绩报表文件: {report_path}")

	merge_scores(student_list_path, report_path, output_path)


if __name__ == "__main__":
	main()
