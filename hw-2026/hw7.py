import score_tools

function_group = score_tools.AddGroup("功能", subgroups=[
		score_tools.AddGroup("Basics", maximum=4.25, minimum=0, basic_score=0, subgroups=[
			score_tools.AddGroup("Blinn-Phong 着色模型（Rast）", maximum=1.25, minimum=0, basic_score=0, subgroups=[
				score_tools.FixedLeafGroup("Diffuse 项：使用 N·L 与漫反射颜色", 0.25, True),
				score_tools.FixedLeafGroup("Specular 项：半角向量 H 与高光指数", 0.25, True),
				score_tools.FixedLeafGroup("Ambient 项：环境光/常量项", 0.25, True),
				score_tools.FixedLeafGroup("法线贴图：采样 + TBN 变换正确", 0.5, True),
			]),
			score_tools.AddGroup("Shadow Mapping（Rast）", maximum=1.0, minimum=0, basic_score=0, subgroups=[
				score_tools.FixedLeafGroup("光源视角深度图生成正确（light VP）", 0.5, True),
				score_tools.FixedLeafGroup("主渲染 pass 深度比较与偏移正确", 0.5, True),
			]),
			score_tools.AddGroup("矩形光源相关（P.T.）", maximum=1.0, minimum=0, basic_score=0, subgroups=[
				score_tools.FixedLeafGroup("光线与矩形光源相交计算正确", 0.5, True),
				score_tools.FixedLeafGroup("面积采样与 pdf 计算正确", 0.25, True),
				score_tools.FixedLeafGroup("Irradiance/几何项/可见性计算正确", 0.25, True),
			]),
			score_tools.AddGroup("路径追踪递归与 Russian Roulette（P.T.）", maximum=1.0, minimum=0, basic_score=0, subgroups=[
				score_tools.FixedLeafGroup("递归/迭代路径积分与 throughput 更新正确", 0.5, True),
				score_tools.FixedLeafGroup("Russian Roulette 概率与权重归一正确", 0.5, True),
			]),
		]),
		score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
			score_tools.AddGroup("可选任务", maximum=1e9, minimum=0, basic_score=0, subgroups=[
				score_tools.MutableLeafGroup("Percentage Close Soft Shadow (PCSS)", score_max=0.3, score_min=0, initial=0),
				score_tools.MutableLeafGroup("Screen Space Ambient Occlusion (SSAO)", score_max=0.5, score_min=0, initial=0),
				score_tools.MutableLeafGroup("Displacement Mapping", score_max=0.2, score_min=0, initial=0),
				score_tools.MutableLeafGroup("复杂 BRDF + MIS", score_max=0.7, score_min=0, initial=0),
			]),
		])
	], maximum=5.5, minimum=0, basic_score=0)


prog_group = score_tools.AddGroup("程序", maximum=5.5, minimum=0, basic_score=0, subgroups=[
	score_tools.AddGroup("Basics", maximum=4.25, minimum=0, basic_score=5, subgroups=[
		score_tools.MutableLeafGroup("Raster 部分 shader 编译出错或无法渲染（每个关键 shader -0.5，最多 -2）", score_max=0, score_min=-2, initial=0),
		score_tools.MutableLeafGroup("Path Tracing 部分运行错误/输出全黑导致无法评测", score_max=0, score_min=-2, initial=0),
		score_tools.MutableLeafGroup("程序严重不完整，导致无法进行批改", score_max=0, score_min=-2, initial=0),
	]),
	score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
		score_tools.MutableLeafGroup("合理的类型/功能封装", score_max=0.5, score_min=0, initial=0)
	])
])


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


all_score = score_tools.AverageGroup("总成绩", maximum=5.5, minimum=0, basic_score=0, subgroups=[
	function_group, prog_group, report_group
])


extension_group = score_tools.AddGroup("拓展任务", maximum=5.5, minimum=0, basic_score=0, subgroups=[
	score_tools.AddGroup("全面对比光栅 & 光追效果、时间等指标", maximum=0.5, minimum=0, basic_score=0, subgroups=[
		score_tools.MutableLeafGroup("同场景/同视角/同参数对齐对比", score_max=0.1, score_min=0, initial=0),
		score_tools.MutableLeafGroup("统计时间/采样/分辨率等设置说明", score_max=0.1, score_min=0, initial=0),
		score_tools.MutableLeafGroup("定量指标或误差图（如PSNR/SSIM/差分图）", score_max=0.15, score_min=0, initial=0),
		score_tools.MutableLeafGroup("定性对比图与文字分析", score_max=0.15, score_min=0, initial=0),
	]),
	score_tools.AddGroup("修改参数并系统对比效果（含图示/表格）", maximum=0.5, minimum=0, basic_score=0, subgroups=[
		score_tools.MutableLeafGroup("明确参数列表与取值范围", score_max=0.1, score_min=0, initial=0),
		score_tools.MutableLeafGroup("至少2-3组对照实验", score_max=0.2, score_min=0, initial=0),
		score_tools.MutableLeafGroup("图示/表格呈现对比结果", score_max=0.1, score_min=0, initial=0),
		score_tools.MutableLeafGroup("简要分析与结论", score_max=0.1, score_min=0, initial=0),
	]),
	score_tools.AddGroup("修改渲染方式实现非真实感渲染（说明方法与效果）", maximum=0.5, minimum=0, basic_score=0, subgroups=[
		score_tools.MutableLeafGroup("方法/算法说明清楚", score_max=0.15, score_min=0, initial=0),
		score_tools.MutableLeafGroup("实现结果图清晰可见", score_max=0.2, score_min=0, initial=0),
		score_tools.MutableLeafGroup("与原渲染方式对比与分析", score_max=0.15, score_min=0, initial=0),
	]),
])


with_extension_grp = score_tools.AddGroup("总成绩（含拓展任务）", maximum=5.5, minimum=0, basic_score=0, subgroups=[
	all_score, extension_group
])

score_tools.run_group(with_extension_grp, addon="""每一项不考虑bonus单独算分，然后再加上bous（封顶5.5），最后三项平均
每一项无论得分多寡，最终都会限制到[0, 5.5]中！
>5无论多少都只算5+
""")
