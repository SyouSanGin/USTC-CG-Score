import score_tools

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.AddGroup("Basics",maximum=5,minimum=0, basic_score=0,subgroups=[
            score_tools.FixedLeafGroup("完成矩形光源（相交计算，采样计算，Irradiance计算）", 1, True),
            score_tools.FixedLeafGroup("直接光照积分器下结果正常", 1, True),
            score_tools.FixedLeafGroup("完成PT（递归进行光线传播），但是效果稀碎", 1, True),
            score_tools.FixedLeafGroup("完成PT（递归进行光线传播），效果还行", 1, True),
            score_tools.FixedLeafGroup("Russian Roulette", 1, True),
        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("做了其他的材质模型（有文章支撑）并进行MIS", score_max=0.25, score_min=0, initial=0),
            score_tools.MutableLeafGroup("添加了透明支持", score_max=0.25, score_min=0, initial=0),
        ])
    ],maximum=5.5, minimum=0, basic_score=0)


prog_group = score_tools.AddGroup("程序", maximum=5.5,minimum=0,basic_score=0,subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.MutableLeafGroup("程序无法编译", score_max=0, score_min=-2, initial=0),
        score_tools.MutableLeafGroup("程序严重不完整，导致无法进行批改", score_max=0, score_min=-2, initial=0),
        score_tools.MutableLeafGroup("有较大的使用LLM写的嫌疑", score_max=0, score_min=-2, initial=0),
        
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
    ])
])



report_group = score_tools.AddGroup("报告",maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.MutableLeafGroup("提交不完整（比如代码文件夹没有整个打包，没有提交报告等）", score_max=0,score_min=-2, initial=0),
        score_tools.FixedLeafGroup("没有前述功能任务点相应内容的展示（主要是矩形光源效果&PT效果）", -1, False),
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