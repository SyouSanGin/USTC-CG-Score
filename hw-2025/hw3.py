import score_tools
# 功能性（基本要求：矩形的Poisson和实时拖动）：
# - 混合梯度（bonus，较为容易的）
# - 多边形扫描线（bonus，需区分是否维护了扫描线算法的特殊数据结构）
# - 实时拖动（1）
# - 矩形区域的融合（4）
#   - 系数矩阵的构造（1）
#   - 右侧向量的构造（1）
#   - 调用正确的求解器（1）
#   - 得到正确结果（1）

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.AddGroup("Basics",maximum=5,minimum=0, basic_score=0,subgroups=[
            score_tools.FixedLeafGroup("实时拖动", 1, True),
            score_tools.AddGroup(
                "形区域的融合", maximum=4, minimum=0, basic_score=0, subgroups=[
                    score_tools.FixedLeafGroup("系数矩阵的构造", 1, True),
                    score_tools.FixedLeafGroup("右侧向量的构造", 1, True),
                    score_tools.FixedLeafGroup("调用正确的求解器", 1, True),
                    score_tools.FixedLeafGroup("得到正确结果", 1, True),
                ]
            )
        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("混合梯度", score_max=0.2, score_min=0, initial=0),
            score_tools.MutableLeafGroup("多边形扫描线（需区分是否维护了扫描线算法的特殊数据结构）",score_max=0.5,score_min=0,initial=0),
            score_tools.MutableLeafGroup("Seamless Tiling",score_max=0.5,score_min=0,initial=0),
            score_tools.MutableLeafGroup("Texture Flattening",score_max=0.5,score_min=0,initial=0),
        ])
    ],maximum=5.5, minimum=0, basic_score=0)

# 程序鲁棒性和规范性：
# - 合理的类型封装，例如将不同的梯度计算设计为多个类 (bonus)
# - 没有处理区域移动到背景图像之外的情况（-2）
# - 程序效率不高（-0~-2）
#   - 没有使用稀疏矩阵（-2）
#   - 其他影响效率的冗余操作（酌情）
# - 其他不规范写法（酌情）
prog_group = score_tools.AddGroup("程序", maximum=5.5,minimum=0,basic_score=0,subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
        score_tools.FixedLeafGroup("没有处理区域移动到背景图像之外的情况", score=-2, status=False),
        score_tools.AddGroup(
            '程序效率不高',maximum=0, minimum=-2,basic_score=0,
            subgroups=[
                score_tools.FixedLeafGroup("没有使用稀疏矩阵", -2,False),
                score_tools.MutableLeafGroup("其他影响效率的冗余操作", score_max=0, score_min=-2, initial=0),
                score_tools.MercifulLeafGroup("其他影响效率的冗余操作(不作扣分)")
            ]
        ),
        score_tools.MutableLeafGroup("其他不规范写法", score_max=0, score_min=-2, initial=0),
        score_tools.MercifulLeafGroup("其他不规范写法(不作扣分)"),
        score_tools.FixedLeafGroup("程序发生崩溃",score=-2, status=False),
        score_tools.FixedLeafGroup("发生偶发性求解异常",score=-1, status=False)
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
        score_tools.MutableLeafGroup("合理的类型封装，例如将不同的梯度计算设计为多个类",score_max=0.5, score_min=0, initial=0)    
    ])
])

# 实验报告（功能说明、算法原理、结果呈现）：
#   - 详细完整，且有更丰富且合理的例子（bonus）
#   - 详细完整，且有针对变量的实验和分析（bonus）
#   - 不直观的交互没有说明（-1）
#   - 没有结果展示（-2）
#   - 没有原理说明（-0~-2）

report_group = score_tools.AddGroup("报告",maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.AddGroup("Basics", maximum=5, minimum=0, basic_score=5, subgroups=[
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

