import score_tools

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.AddGroup("Basics",maximum=4.25,minimum=0, basic_score=0,subgroups=[
            score_tools.FixedLeafGroup("正确的前向加噪", 1, True),
            score_tools.FixedLeafGroup("正确的训练迭代过程", 1.5, True),
            score_tools.FixedLeafGroup("正确的逆向去噪过程", 1.75, True),
            
        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("文生图",score_max=0.5,score_min=0,initial=0),
            score_tools.MutableLeafGroup("图像Inpainting",score_max=0.5,score_min=0,initial=0),
            score_tools.MutableLeafGroup("有多图泛化性",score_max=0.2,score_min=0,initial=0),
            score_tools.MutableLeafGroup("其他创新(酌情)",score_max=0.5,score_min=0,initial=0),
        ])
    ],maximum=5.5, minimum=0, basic_score=0)



report_group = score_tools.AddGroup("报告",maximum=5.5,minimum=0, basic_score=0, subgroups=[
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
            score_tools.MutableLeafGroup("缺少算法原理说明（至少需要对基础内容算法进行公式化说明）", score_max=0,score_min=-1, initial=0),
            score_tools.MutableLeafGroup("缺少实验结果展示（至少需要对基础内容进行展示）", score_max=0,score_min=-1, initial=0),
            score_tools.MutableLeafGroup("缺少实验结果分析与结论（至少需要对基础内容进行分析总结）", score_max=0,score_min=-1, initial=0),
        ]),
        
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("对方法的原理有充分的解析，并有自己的理解", 0.5,0,0),
            score_tools.MutableLeafGroup("将方法应用于更多数据上，并展示算法结果", 0.3,0,0),
            score_tools.MutableLeafGroup("对方法中不同模块/参数进行充分消融实验，展示并分析结果", 0.5,0,0),
            score_tools.MutableLeafGroup("对不同方法进行对比实验（包括但不限于作业中提及的不同方法），展示并分析结果", 0.5,0,0),
            score_tools.MutableLeafGroup("报告赏心悦目，排版精美", 0.3,0,0),
        ])
])


all_score = score_tools.AverageGroup("总成绩",maximum=5.5,minimum=0,basic_score=0,subgroups=[
    function_group,report_group
])


thinking = score_tools.AddGroup("思考题", maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.MutableLeafGroup("alpha&beta 选取分析",score_max=0.2,score_min=0,initial=0),
    score_tools.MutableLeafGroup("时间步 选取分析",score_max=0.2,score_min=0,initial=0),
    score_tools.MutableLeafGroup("噪声类型对结果的影响",score_max=0.5,score_min=0,initial=0),
    score_tools.MutableLeafGroup("Flow Matching",score_max=1,score_min=0,initial=0),
    score_tools.MutableLeafGroup("其他创新尝试（酌情）",score_max=2,score_min=0,initial=0),
])

with_thinking_grp = score_tools.AddGroup("总成绩（含思考题）",maximum=5.5,minimum=0,basic_score=0,subgroups=[
    all_score,thinking
])

score_tools.run_group(with_thinking_grp, addon="""每一项不考虑bonus单独算分，然后再加上bous（封顶5.5），最后三项平均
每一项无论得分多寡，最终都会限制到[0, 5.5]中！
>5无论多少都只算5+
""")

