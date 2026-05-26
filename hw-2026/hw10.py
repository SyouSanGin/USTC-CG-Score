import score_tools


# ============================================================
# 功能 (Function) — Code Implementation & Correctness
# ============================================================
function_group = score_tools.AddGroup("功能", subgroups=[
	score_tools.AddGroup("Basics", maximum=4.25, minimum=0, basic_score=0, subgroups=[
		score_tools.FixedLeafGroup("实现弱可压缩SPH流体仿真（WCSPH）的完整流程（包括密度估计、粘性力计算、压力计算、速度与位置更新）", 1.5, True),
		score_tools.FixedLeafGroup("测试不同参数和边界条件设置下的仿真效果",1.5, True),
		score_tools.FixedLeafGroup("从粒子重建表面，渲染结果 (这部分已经写好了的，但是你得连上对应节点)", 1.25, True),
	]),

	score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
		score_tools.MutableLeafGroup("实现隐式不可压缩的SPH流体仿真方法 IISPH", score_max=0.5, score_min=0, initial=0),
	]),
], maximum=5.5, minimum=0, basic_score=0)


# ============================================================
# 程序 (Program) — 代码提交与工程质量
# ============================================================
prog_group = score_tools.AddGroup("程序", maximum=5.5, minimum=0, basic_score=0, subgroups=[
	score_tools.AddGroup("Basics", maximum=4.25, minimum=0, basic_score=4.25, subgroups=[
		score_tools.FixedLeafGroup("程序运行错误或依赖缺失导致无法复现", -1, False),
		score_tools.FixedLeafGroup("存在明显内存安全问题（越界/野指针/双重释放等）", -1, False),
		score_tools.MutableLeafGroup("日志与参数说明不足导致难以复现（酌情扣分）", score_max=0, score_min=-0.5, initial=0),
		score_tools.MutableLeafGroup("代码结构与可读性（模块化、注释、说明）", score_max=0, score_min=-0.5, initial=0),
	]),
])





# ============================================================
# 报告 (Report) — 实验报告质量
# ============================================================
report_group = score_tools.AddGroup("报告", maximum=5.5, minimum=0, basic_score=0, subgroups=[
	score_tools.AddGroup("Basics", maximum=4.25, minimum=0, basic_score=4.25, subgroups=[
		score_tools.AddGroup("报告格式规范性", maximum=0, minimum=-114514, basic_score=0, subgroups=[
			score_tools.FixedLeafGroup("没有交PDF格式，但是提交了Docx格式", -0.1, False),
			score_tools.FixedLeafGroup("没有交PDF格式/Docx格式（如Markdown）", -0.2, False),
			score_tools.FixedLeafGroup("报告内容缺乏结构化组织（如无“算法原理”、“实验结果”，“思考题”等分节）", -0.1, False),
			score_tools.FixedLeafGroup("报告公式排版混乱/未使用公式语法书写&渲染（如latex/doc中公式环境）", -0.1, False),
			score_tools.FixedLeafGroup("报告图片排版极度混乱", -0.2, False),
		]),
		score_tools.AddGroup("报告内容完整性", maximum=0, minimum=-114514, basic_score=0, subgroups=[
			score_tools.FixedLeafGroup("缺少对AI辅助的相关分析/使用情况说明", -0.5, False),
			score_tools.FixedLeafGroup("若使用AI工具，缺少对AI结果的相关分析", -1, False),
			score_tools.FixedLeafGroup("报告中结果图片缺少标题/相关解释说明", -0.1, False),
			score_tools.FixedLeafGroup("报告中表格/统计图表缺少标题/相关解释说明", -0.1, False),
			score_tools.MutableLeafGroup("缺少算法原理说明（至少需要对基础内容算法进行公式化说明）", score_max=0, score_min=-1, initial=0),
			score_tools.MutableLeafGroup("缺少实验结果展示（至少需要对基础内容进行展示）", score_max=0, score_min=-1, initial=0),
			score_tools.MutableLeafGroup("缺少实验结果分析与结论（至少需要对基础内容进行分析总结）", score_max=0, score_min=-1, initial=0),
		]),
	]),
	score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
			score_tools.MutableLeafGroup("对方法的原理有充分的解析，并有自己的理解", 0.5, 0, 0),
			score_tools.MutableLeafGroup("将方法应用于更多数据上，并展示算法结果", 0.3, 0, 0),
			score_tools.MutableLeafGroup("对方法中不同模块/参数进行充分消融实验，展示并分析结果", 0.5, 0, 0),
			score_tools.MutableLeafGroup("对不同方法进行对比实验（包括但不限于作业中提及的不同方法），展示并分析结果", 0.5, 0, 0),
			score_tools.MutableLeafGroup("报告赏心悦目，排版精美", 0.3, 0, 0),
		])
])


# ============================================================
# 总成绩 — 功能与报告取平均
# ============================================================
all_score = score_tools.AverageGroup("总成绩", maximum=5.5, minimum=0, basic_score=0, subgroups=[
    function_group, prog_group, report_group
])


# ============================================================
# 拓展任务 (Extension) — 可选 & 拓展任务，独立加分
# ============================================================
extension_group = score_tools.AddGroup("拓展任务", maximum=5.5, minimum=0, basic_score=0, subgroups=[
    score_tools.MutableLeafGroup("对模拟过程进行定量分析", score_max=0.5, score_min=0, initial=0),
    score_tools.MutableLeafGroup("并行加速", score_max=0.5, score_min=0, initial=0),
    score_tools.MutableLeafGroup("DL方法", score_max=0.5, score_min=0, initial=0),
    score_tools.MutableLeafGroup("其他合理创新（酌情给分）", score_max=0.5, score_min=0, initial=0),
])

# ============================================================
# 总成绩（含拓展任务）
# ============================================================
with_extension_grp = score_tools.AddGroup("总成绩（含拓展任务）", maximum=5.5, minimum=0, basic_score=0, subgroups=[
    all_score, extension_group
])

# ============================================================
# 启动评分工具
# ============================================================
score_tools.run_group(with_extension_grp, addon="""基础成绩 = (功能 + 报告) / 2，再 + 拓展任务加分，封顶5.5
每一项无论得分多寡，最终都会限制到[0, 5.5]中！
>5无论多少都只算5+
""")
