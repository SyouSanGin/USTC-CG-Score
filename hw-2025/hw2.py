import score_tools

# 功能(5.5)
#     Basics(5)
#         至少实现了半残的IDW/RBF(如只能实现仿射变换等不完全功能)(1)
#         实现IDW(2)
#         实现RBF(2)
#         实现了算法，但是Bonus完成有小问题（例如补洞）而导致Warping效果不佳(-0) (merciful)
#     Bonus
#         MLP(MLS, 三角化/四边形网格插值等) warping
#         填充(ANN, 逆映射插值, MC, 卷积等)
#         其他合理的bonus项

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.AddGroup("Basics",maximum=5,minimum=0, basic_score=0,subgroups=[
            score_tools.FixedLeafGroup("至少实现了半残的IDW/RBF(如只能实现仿射变换等不完全功能)", 1, True),
            score_tools.FixedLeafGroup("实现IDW", 2, True),
            score_tools.FixedLeafGroup("实现RBF", 2, True),
            score_tools.MercifulLeafGroup("实现了算法，但是Bonus完成有小问题（例如补洞）而导致Warping效果不佳", False),
        score_tools.MutableLeafGroup("其他功能性缺陷（扣分内容需单独补充）",score_max=0, score_min=-2, initial=0),

        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("MLP(MLS, 三角化/四边形网格插值等) warping", 1,0,0),
            score_tools.MutableLeafGroup("填充(ANN, 逆映射插值, MC, 卷积等)", 1,0,0),
            score_tools.MutableLeafGroup("其他合理的创新/额外工作", 1,0,0),
        ])
    ],maximum=5.5, minimum=0, basic_score=0)

# 程序(5.5)
#     Basics(5)
#         没有正确解耦出Warper类（例如Warper类是数学映射，与图像无关）(-1)
#         没有正确封装（例如RBF系数计算实现在类的外面）(-0.5)
#         没有使用多态，而是单独创建子类并调用方法(-0) (merciful)
#         对每个像素都重新计算 warping 映射的参数，存在效率问题(-0.5)
#         没有处理点数较少的情况，存在鲁棒性问题(-1)(mutable)
# 	存在内存泄漏，例如申请了 warper* 指针的内存，但是没有释放，推荐使用智能指针或者主动调用delete(-1)
#     Bonus
#         较明显地优化了代码结构
#         速度优化(并行)

prog_group = score_tools.AddGroup("程序", maximum=5.5,minimum=0,basic_score=0,subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.FixedLeafGroup("没有正确解耦出Warper类（例如Warper类是数学映射，与图像无关）", -0.5, False),
        score_tools.FixedLeafGroup("没有正确封装（例如RBF系数计算实现在类的外面）", -0.5, False),
        score_tools.MercifulLeafGroup("没有使用多态，而是单独创建子类并调用方法", False),
        score_tools.FixedLeafGroup("对每个像素都重新计算 warping 映射的参数，存在效率问题", -0.5, False),
        score_tools.AddGroup("边界情况处理（控制点数量少）(0表示未扣分)", maximum=0, minimum=-1e9, basic_score=0, subgroups=[
            score_tools.FixedLeafGroup("程序崩溃", -1, False),
            score_tools.FixedLeafGroup("RBF/IDW边界情况未处理", -0.5, False),
            score_tools.MercifulLeafGroup("没有控制点的时候点击变换，黑屏", False),
            score_tools.MutableLeafGroup("酌情扣分（扣分内容需单独补充）",score_max=0, score_min=-1, initial=0),
            
        ]),
        score_tools.MutableLeafGroup("其他代码缺陷（扣分内容需单独补充）",score_max=0, score_min=-2, initial=0),
        
        
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("较明显地优化了代码结构", 1,0,0),
            score_tools.MutableLeafGroup("速度优化(并行)", 1,0,0),
        ])
])



# 报告(5.5)
#     Basics(5)
#         没有类图(-1)
#         不直观的交互没有说明(-1)
#         缺少结果(-2)
#         缺少算法原理说明(-0.5)
#         粘贴大段大段的代码(-0) (merciful)
#         实在是太丑了(-0) (merciful)
#         报告交的不是pdf(-0.5)
#     Bonus
#         详细完整，且有更丰富且合理的例子
#         详细完整，且有针对参数的实验和分析

report_group = score_tools.AddGroup("报告",maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.FixedLeafGroup("没有类图", -1, False),
        score_tools.FixedLeafGroup("不直观的交互没有说明", -1, False),
        score_tools.FixedLeafGroup("没有结果", -2, False),
        score_tools.FixedLeafGroup("缺少算法原理说明", -0.5, False),
        score_tools.MercifulLeafGroup("不要粘贴大段代码",False),
        score_tools.MercifulLeafGroup("报告实在是不美观😭",False),
        score_tools.FixedLeafGroup("没有交PDF格式", -0.5, False),
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("详细完整，且有更丰富且合理的例子", 1,0,0),
            score_tools.MutableLeafGroup("详细完整，且有针对参数的实验和分析", 1,0,0),
        ])
])


all_score = score_tools.AverageGroup("总成绩",maximum=5.5,minimum=0,basic_score=0,subgroups=[
    function_group,prog_group,report_group
])

score_tools.run_group(all_score, addon="每一项不考虑bonus单独算分，然后再加上bonus（封顶5.5），最后三项平均")

