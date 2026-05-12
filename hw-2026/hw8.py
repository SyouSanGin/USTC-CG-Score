import score_tools

# ============================================================
# 功能 (Function) — Code Implementation & Correctness
# ============================================================
# 总计 7 个 HW8_TODO 实现项，基础分合计 4.25 分
#   编码实现: 0.65 + 0.65 + 0.30 + 0.30 = 1.90
#   注意力机制: 0.90 + 0.70 + 0.75 = 2.35
#   合计: 1.90 + 2.35 = 4.25

function_group = score_tools.AddGroup("功能", subgroups=[
    # --- Basics: 编码实现 (Tasks 1-3) ---
    score_tools.AddGroup("Basics - 编码实现", maximum=1.9, minimum=0, basic_score=0, subgroups=[
        score_tools.FixedLeafGroup("[Task1] Triangle Embedding 实现正确 (construct_seq)", 0.65, True),
        score_tools.FixedLeafGroup("[Task2] Ray Bundle Embedding 实现正确 (ViewTransformer.forward)", 0.65, True),
        score_tools.FixedLeafGroup("[Task3a] RoPE Encoder 实现正确 (TransformerEncoder)", 0.30, True),
        score_tools.FixedLeafGroup("[Task3b] RoPE Decoder 实现正确 (TransformerDecoder)", 0.30, True),
    ]),

    # --- Basics: 注意力机制 (Tasks 4-6) ---
    score_tools.AddGroup("Basics - 注意力机制", maximum=2.35, minimum=0, basic_score=0, subgroups=[
        score_tools.FixedLeafGroup("[Task4] Scaled Dot-Product Attention 实现正确 (MultiHeadAttention)", 0.90, True),
        score_tools.FixedLeafGroup("[Task5] Self-Attention Encoder Forward 实现正确", 0.70, True),
        score_tools.FixedLeafGroup("[Task6] Cross-Attention Decoder Forward 实现正确", 0.75, True),
    ]),

    # --- 代码质量扣分项 ---
    score_tools.AddGroup("代码质量扣分项", maximum=0, minimum=-114514, basic_score=0, subgroups=[
        score_tools.FixedLeafGroup("代码存在严重错误，无法运行/训练直接崩溃", -2, False),
        score_tools.FixedLeafGroup("提交了checkpoint权重文件(.pt)，未按要求删除", -0.01, False),
        score_tools.FixedLeafGroup("补全方式为直接抄答案/硬编码绕过TODO（非真实实现）", -2, False),
        score_tools.MutableLeafGroup("PSNR未达15（根据与15的差距酌情扣分：差距<2扣0.1，<5扣0.2，5+扣0.5）", score_max=0, score_min=-0.5, initial=0),
        score_tools.MutableLeafGroup("部分TODO实现有误但不影响整体运行（根据错误程度酌情扣分）", score_max=0, score_min=-0.5, initial=0),
    ]),

    # --- Bonus: 可选任务 ---
    score_tools.AddGroup("Bonus - 可选任务", maximum=1e9, minimum=0, basic_score=0, subgroups=[
        score_tools.MutableLeafGroup("尝试更大场景/更多视角/动态光源，并做定性&定量分析", score_max=0.5, score_min=0, initial=0),
        score_tools.MutableLeafGroup("完成消融实验（ablation study），分析各模块贡献", score_max=0.5, score_min=0, initial=0),
        score_tools.MutableLeafGroup("自建数据集，评估视角数量与分布对渲染质量的影响", score_max=0.5, score_min=0, initial=0),
    ]),
], maximum=5.5, minimum=0, basic_score=0)


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
    function_group, report_group
])


# ============================================================
# 拓展任务 (Extension) — 可选 & 拓展任务，独立加分
# ============================================================
extension_group = score_tools.AddGroup("拓展任务", maximum=5.5, minimum=0, basic_score=0, subgroups=[
    score_tools.MutableLeafGroup("材质/光照编码方式的探索", score_max=0.5, score_min=0, initial=0),
    score_tools.MutableLeafGroup("逐三角编码 & 逐物体编码的对比", score_max=0.5, score_min=0, initial=0),
    score_tools.MutableLeafGroup("渲染结果与GT的误差分析与可视化", score_max=0.5, score_min=0, initial=0),
    score_tools.MutableLeafGroup("探索透明物体/风格化渲染等特殊场景", score_max=0.5, score_min=0, initial=0),
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

【评分说明】
- 功能部分共7个TODO实现项，基础分合计4.25分：
  编码实现（Task1~3）1.90分 + 注意力机制（Task4~6）2.35分
- Task4（Scaled Dot-Product Attention）为核心实现，权重最高（0.90分）
- 若代码完全无法运行或训练直接崩溃，扣2分
- 若发现直接抄答案/硬编码绕过TODO，扣3分
- PSNR要求>15，未达标的根据差距扣0.1~0.5分
- 报告必须包含AI使用记录（对话日志+分析评价+反思），缺失将逐项扣分
- 拓展任务为独立加分项，直接累加到总成绩上（封顶5.5）
""")
