import score_tools
# 功能性（ARAP网格参数化方法方法正确性）：
# - ASAP   参数化算法(bonus)
# - Hybrid 参数化算法(bonus)
# - ARAP的局部迭代的正确性（2）
#   - 二阶矩阵的 SVD 分解 (1)
#   - 计算当前参数化 Jacobian的局部正交逼近（1）
# - ARAP 的全局迭代的正确性（2）
# - 使用测试纹理和网格检验实验结果（1）

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.AddGroup("Basics",maximum=5,minimum=0, basic_score=0,subgroups=[
            score_tools.AddGroup(
                "ARAP的局部迭代的正确性", maximum=2, minimum=0, basic_score=0, subgroups=[
                    score_tools.FixedLeafGroup("二阶矩阵的 SVD 分解", 1, True),
                    score_tools.FixedLeafGroup("计算当前参数化 Jacobian的局部正交逼近", 1, True),
                ]
            ),
            score_tools.FixedLeafGroup("ARAP的全局迭代的正确性", 2, True),
            score_tools.FixedLeafGroup("使用测试纹理和网格检验实验结果", 1, True)
        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("ASAP参数化算法", score_max=0.25, score_min=0, initial=0),
            score_tools.MutableLeafGroup("Hybrid参数化算法", score_max=0.25, score_min=0, initial=0)
        ])
    ],maximum=5.5, minimum=0, basic_score=0)

# 程序鲁棒性和规范性：
# - 合理的类型封装，例如将不同的权重计算设计为多个类 (bonus)
# - 程序效率不高（-0~-2）
#   - 没有使用预处理（-2）
#   - 没有使用稀疏矩阵（-2）
# - 其他不规范写法（酌情）
# - 固定点的选取方式以及个数（酌情）
# - 程序发生崩溃（不是由框架引起的 -2）
# - 冗余操作（酌情）
#   - 连节点的时候连接了一些多余的节点（酌情）
#   - 对节点的输入输出大改并且没有说明怎么使用，还不带节点图（酌情）

prog_group = score_tools.AddGroup("程序", maximum=5.5,minimum=0,basic_score=0,subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.AddGroup(
            '程序效率不高',maximum=0, minimum=-2,basic_score=0,
            subgroups=[
                score_tools.FixedLeafGroup("没有使用预处理", -2,False),
                score_tools.FixedLeafGroup("没有使用稀疏矩阵", -2,False)
            ]
        ),
        score_tools.MutableLeafGroup("其他不规范写法", score_max=0, score_min=-2, initial=0),
        score_tools.MercifulLeafGroup("其他不规范写法(不作扣分)"),
        score_tools.MutableLeafGroup("固定点的选取方式以及个数", score_max=0, score_min=-2, initial=0),
        score_tools.MercifulLeafGroup("固定点的选取方式以及个数(不作扣分)"),
        score_tools.FixedLeafGroup("程序发生崩溃(不是由框架引起的)",score=-2, status=False),
        score_tools.AddGroup(
            '冗余操作',maximum=0, minimum=-1,basic_score=0,
            subgroups=[
                score_tools.MutableLeafGroup("连节点的时候连接了一些多余的节点", score_max=0, score_min=-0.5, initial=0),
                score_tools.MercifulLeafGroup("连节点的时候连接了一些多余的节点(不作扣分)"),
                score_tools.MutableLeafGroup("对节点的输入输出大改并且没有说明怎么使用，还不带节点图", score_max=0, score_min=-0.5, initial=0),
                score_tools.MercifulLeafGroup("对节点的输入输出大改并且没有说明怎么使用，还不带节点图(不作扣分)")
            ]
        ),
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
        score_tools.MutableLeafGroup("合理的类型封装，例如将不同的梯度计算设计为多个类",score_max=0.5, score_min=0, initial=0)    
    ])
])

# 实验报告（功能说明、算法原理、结果呈现）：
#   - 详细完整，且有更丰富且合理的例子（bonus）
#   - 详细完整，且有针对变量的实验和分析（bonus）
#   - 提交不完整（比如缺少stage.usdc，根据报告评判严重性）(-2~-0)
#   - 不直观的交互没有说明（-1）
#   - 没有结果展示（-2）
#   - 没有原理说明（-0~-2）

report_group = score_tools.AddGroup("报告",maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.MutableLeafGroup("提交不完整（比如缺少stage.usdc，根据报告评判严重性）", score_max=0,score_min=-2, initial=0),
        score_tools.FixedLeafGroup("不直观的交互没有说明", -1, False),
        score_tools.FixedLeafGroup("没有结果", -2, False),
        score_tools.MutableLeafGroup("缺少算法原理说明", score_max=0,score_min=-2, initial=0),
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