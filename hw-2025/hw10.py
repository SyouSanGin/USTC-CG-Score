import score_tools

function_group = score_tools.AddGroup("功能性", subgroups=[
        score_tools.AddGroup("Basics",maximum=5,minimum=0, basic_score=0,subgroups=[
            score_tools.FixedLeafGroup("正确的关节变换", 2.5, True),
            score_tools.FixedLeafGroup("正确的蒙皮顶点计算", 2.5, True),
            score_tools.MutableLeafGroup("结果不合理根据情况扣分", score_max=0, score_min=-1, initial=0),
        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            
        ])
    ],maximum=5.5, minimum=0, basic_score=0)


prog_group = score_tools.AddGroup("程序鲁棒性和规范性", maximum=5.5,minimum=0,basic_score=0,subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.MutableLeafGroup("程序鲁棒性问题（如边界处理不合理）", score_max=0, score_min=-1, initial=0),
        score_tools.MutableLeafGroup("代码规范性问题（如冗余操作）", score_max=0, score_min=-1, initial=0),
        score_tools.MutableLeafGroup("程序严重不完整，导致无法进行批改", score_max=0, score_min=-2, initial=0),
        score_tools.MutableLeafGroup("有较大的使用LLM写的嫌疑", score_max=0, score_min=-2, initial=0),
        
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
    ])
])



report_group = score_tools.AddGroup("报告",maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=3, subgroups=[
        score_tools.FixedLeafGroup("arm.usda", 1, True),
        score_tools.FixedLeafGroup("belly_dance_girl.usda", 1, True),
        score_tools.FixedLeafGroup("没有结果展示", -2, False),
        score_tools.MutableLeafGroup("原理说明不透彻", score_max=0,score_min=-2, initial=0),
        score_tools.FixedLeafGroup("录制的视角太随意", -1, False),
        
        
        score_tools.MercifulLeafGroup("不要粘贴大段代码",False),
        score_tools.MercifulLeafGroup("报告实在是不美观😭",False),
        score_tools.FixedLeafGroup("没有交PDF格式", -0.5, False),
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("详细完整，且有更丰富且合理的例子", 0.25,0,0),
            score_tools.MutableLeafGroup("详细完整，且有针对参数的实验和分析", 0.25,0,0),
            score_tools.MutableLeafGroup("有布料+简单碰撞的结果（bonus 0.5）", 0.5,0,0),
        ])
])


all_score = score_tools.AverageGroup("总成绩",maximum=5.5,minimum=0,basic_score=0,subgroups=[
    function_group,prog_group,report_group
])

score_tools.run_group(all_score, addon="""每一项不考虑bonus单独算分，然后再加上bonus（封顶5.5），最后三项平均
每一项无论得分多寡，最终都会限制到[0, 5.5]中！
>5无论多少都只算5+
""")