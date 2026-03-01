import score_tools

"""
评分准则
功能（算法/目标的完成度）：
- part 1: 实现数组的内存分配（new/delete）（1.0）
- part 2: 实现数组空间的预分配和动态调整 Reserve(int size) （1.0）
- part 3: 实现模板数组类（1.0）
- part 4: 用 STL list实现多项式（0.5），生成动态库（0.5）
- part 5: 用 STL map 实现多项式（0.5），生成静态库（0.5）

程序（鲁棒性、规范性等）：
- 重复编译，比如没有 #pragma once 或者 #ifndef （-1）
- 析构函数、构造函数编写有误（-1）
- 内存泄露（-1）
- 空指针（-1）

"""

function_group = score_tools.AddGroup("功能", subgroups=[
        score_tools.FixedLeafGroup("实现数组的内存分配", 1, True),
        score_tools.FixedLeafGroup("实现数组空间的预分配和动态调整 ", 1, True),
        score_tools.FixedLeafGroup("实现模板数组类 ", 1, True),
        score_tools.AddGroup("List 多项式",maximum=1,subgroups=[
            score_tools.FixedLeafGroup("实现多项式类", 0.5, True),
            score_tools.FixedLeafGroup("生成动态库", 0.5, True)
            ]),
        score_tools.AddGroup("Map 多项式",maximum=1,subgroups=[
            score_tools.FixedLeafGroup("实现多项式类", 0.5, True),
            score_tools.FixedLeafGroup("生成静态库", 0.5, True)
            ])
    ],maximum=5.5, minimum=0, basic_score=0)

prog_group = score_tools.AddGroup("程序", maximum=5,minimum=0,basic_score=5,subgroups=[
    score_tools.FixedLeafGroup("重复编译", -1, False),
    score_tools.FixedLeafGroup("析构函数、构造函数编写有误", -1, False),
    score_tools.FixedLeafGroup("内存泄露", -1, False),
    score_tools.FixedLeafGroup("空指针", -1, False)
])

all_score = score_tools.AverageGroup("总分", maximum=5, minimum=0, basic_score=0, subgroups=[
    function_group,
    prog_group
])  

if __name__ == "__main__":
    score_tools.run_group(all_score,addon="""每一项不考虑bonus单独算分，然后再加上bonus（封顶5.5），最后三项平均
每一项无论得分多寡，最终都会限制到[0, 5.5]中！
>5无论多少都只算5+
""")