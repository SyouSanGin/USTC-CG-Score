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
        score_tools.FixedLeafGroup("没有结果", -2, False),
        score_tools.FixedLeafGroup("缺少对AI辅助的相关分析(如果使用的话)", -0.1, False),
        score_tools.MutableLeafGroup("缺少算法原理说明", score_max=0,score_min=-2, initial=0),
        score_tools.FixedLeafGroup("没有交PDF格式", -0.5, False),
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("详细完整，且有更丰富且合理的例子", 0.5,0,0),
            score_tools.MutableLeafGroup("详细完整，且有针对参数的实验和分析", 0.5,0,0),
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

