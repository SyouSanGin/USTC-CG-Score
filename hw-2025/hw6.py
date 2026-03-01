import score_tools

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.AddGroup("Basics",maximum=5,minimum=0, basic_score=0,subgroups=[
            score_tools.FixedLeafGroup("Diffuse着色正常", 1, True),
            score_tools.FixedLeafGroup("Specular着色正常", 1, True),
            score_tools.FixedLeafGroup("Ambient着色正常", 1, True),
            score_tools.FixedLeafGroup("实现 Shadow Mapping 算法（硬阴影）<效果还凑合>", 1, True),
            score_tools.FixedLeafGroup("实现 Shadow Mapping 算法（硬阴影）<效果不错>", 1, True),
        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("Percentage Close Soft Shadow", score_max=0.25, score_min=0, initial=0),
            score_tools.MutableLeafGroup("Screen Space Ambient Occlusion", score_max=0.25, score_min=0, initial=0),
            score_tools.MutableLeafGroup("优化Shadow map为cubemap对场景进行观察，支持多向投影", score_max=0.25, score_min=0, initial=0),
            score_tools.MutableLeafGroup("方向光源支持", score_max=0.25, score_min=0, initial=0),
            score_tools.MutableLeafGroup("实现了其他的阴影算法", score_max=0.25, score_min=0, initial=0),
        ])
    ],maximum=5.5, minimum=0, basic_score=0)



prog_group = score_tools.AddGroup("程序", maximum=5.5,minimum=0,basic_score=0,subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.MutableLeafGroup("Shader 编译出错，给程序干崩了（4个shader，崩一个扣0.5）", score_max=0, score_min=-2, initial=0),
        score_tools.MutableLeafGroup("程序严重不完整，导致无法进行批改", score_max=0, score_min=-2, initial=0),
        score_tools.MutableLeafGroup("有较大的使用LLM写的嫌疑", score_max=0, score_min=-2, initial=0),
        
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
        score_tools.MutableLeafGroup("添加了新的节点，支持更为复杂的着色效果",score_max=0.5, score_min=0, initial=0)    
    ])
])



report_group = score_tools.AddGroup("报告",maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.MutableLeafGroup("提交不完整（比如缺少stage.usdc，缺少节点连接json，根据报告评判严重性）", score_max=0,score_min=-2, initial=0),
        score_tools.FixedLeafGroup("不直观的交互没有说明", -1, False),
        score_tools.FixedLeafGroup("没有结果", -2, False),
        score_tools.MutableLeafGroup("原理说明不透彻", score_max=0,score_min=-2, initial=0),
        score_tools.MercifulLeafGroup("不要粘贴大段代码",False),
        score_tools.MercifulLeafGroup("报告实在是不美观😭",False),
        score_tools.FixedLeafGroup("没有交PDF格式", -0.5, False),
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("详细完整，且有更丰富且合理的例子", 0.25,0,0),
            score_tools.MutableLeafGroup("详细完整，且有针对参数的实验和分析", 0.25,0,0),
        ])
])


all_score = score_tools.AverageGroup("总成绩",maximum=5.5,minimum=0,basic_score=0,subgroups=[
    function_group,prog_group,report_group
])

score_tools.run_group(all_score, addon="""每一项不考虑bonus单独算分，然后再加上bonus（封顶5.5），最后三项平均
每一项无论得分多寡，最终都会限制到[0, 5.5]中！
>5无论多少都只算5+
""")