import score_tools

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.AddGroup("Basics",maximum=4.25,minimum=0, basic_score=0,subgroups=[
            score_tools.AddGroup(
                "ARAP的局部迭代的正确性", maximum=2, minimum=0, basic_score=0, subgroups=[
                    score_tools.FixedLeafGroup("二阶矩阵的 SVD 分解", 1, True),
                    score_tools.FixedLeafGroup("计算当前参数化 Jacobian的局部正交逼近", 1, True),
                ]
            ),
            score_tools.FixedLeafGroup("ARAP的全局迭代的正确性", 1.25, True),
            score_tools.FixedLeafGroup("使用测试纹理和网格检验实验结果", 1, True),
            score_tools.MutableLeafGroup("结果与正确结果之间差距过大（酌情扣分）", score_max=0, score_min=-1, initial=0),        
        ]),
        score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
            score_tools.MutableLeafGroup("ASAP参数化算法", score_max=0.5, score_min=0, initial=0),
            score_tools.MutableLeafGroup("Hybrid参数化算法", score_max=0.5, score_min=0, initial=0)
        ])
    ],maximum=5.5, minimum=0, basic_score=0)


prog_group = score_tools.AddGroup("程序", maximum=5.5,minimum=0,basic_score=0,subgroups=[
    score_tools.AddGroup("Basics", maximum=4.25, minimum=0, basic_score=5, subgroups=[
        score_tools.FixedLeafGroup("处理大型方程时没有使用稀疏矩阵（在处理大规模网络时计算效率&内存效率低下）", -0.5,False),
        score_tools.FixedLeafGroup("野指针满天飞（建议使用智能指针）", -1,False),
        score_tools.FixedLeafGroup("运行出错，导致程序崩溃", -1,False),
    ]),
    score_tools.AddGroup("Bonus", maximum=1e9, minimum=0, basic_score=0, subgroups=[
        score_tools.MutableLeafGroup("合理的类型/功能封装",score_max=0.3, score_min=0, initial=0)    
    ])
])


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
    function_group, prog_group,report_group
])


thinking = score_tools.AddGroup("思考题", maximum=5.5,minimum=0, basic_score=0, subgroups=[
    score_tools.MutableLeafGroup("对于算法中不同参数设定的分析(0.05)，给出相应的实验定性(0.05)与定量结果(0.05)",score_max=0.5,score_min=0,initial=0),
    score_tools.MutableLeafGroup("ARAP 算法对初始参数化的敏感性验证，呈现定性(0.1)与定量结果(0.1)",score_max=0.5,score_min=0,initial=0),
    score_tools.MutableLeafGroup("ARAP 局部阶段的并行化加速 (OpenMP/<thread>/CPU-Based 0.1, GPGPU 0.2)",score_max=0.5,score_min=0,initial=0),
    score_tools.MutableLeafGroup("探索更多可能的约束（硬约束、软约束），分析算法在不同约束下的效果，呈现定性(0.1)&定量结果(0.1)",score_max=0.5,score_min=0,initial=0),
    score_tools.MutableLeafGroup("探究 ARAP 参数化中三角形翻转的成因,实现后处理方法(0.1),定性(0.05)&定量(0.05)分析",score_max=0.5,score_min=0,initial=0),
    score_tools.MutableLeafGroup("其他合理创新，酌情给分",score_max=1,score_min=0,initial=0),
])

with_thinking_grp = score_tools.AddGroup("总成绩（含思考题）",maximum=5.5,minimum=0,basic_score=0,subgroups=[
    all_score,thinking
])

score_tools.run_group(with_thinking_grp, addon="""每一项不考虑bonus单独算分，然后再加上bous（封顶5.5），最后三项平均
每一项无论得分多寡，最终都会限制到[0, 5.5]中！
>5无论多少都只算5+
""")

