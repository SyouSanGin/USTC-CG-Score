import score_tools

# create rules
# 功能（算法/目标的完成度）


more_ui = score_tools.FixedLeafGroup("添加UI", 1, True)
ell_create = score_tools.FixedLeafGroup("实现椭圆的绘制",2, True)
poly_create = score_tools.FixedLeafGroup("实现多边形绘制", 2, True)
cannot_poly = score_tools.FixedLeafGroup("不能画出多边形(無法封口)", -1, False)
poly_ill = score_tools.FixedLeafGroup("设计操作不合理(右键结束绘制时，同时添加了两条边/Freehand操作不合理等)", -0.5, False)

grp_func = score_tools.AddGroup("功能（算法/目标的完成度）",subgroups=[
    more_ui,ell_create,poly_create,cannot_poly, poly_ill
],maximum=100, minimum=0,basic_score=0)

# 程序（鲁棒性、规范性等，要求面向对象的类型设计）：

polymorphism = score_tools.AddGroup(
    "多态",subgroups=[
        score_tools.MutableLeafGroup("Polygon 类的存储数据不合理", 0, -2, 0),
        score_tools.FixedLeafGroup("使用了dynamic_cast来转换父类为子类",-1, False)
        ], maximum=2, minimum=0, basic_score=2
)
standard = score_tools.AddGroup(
    "代码规范",
    subgroups=[
        score_tools.FixedLeafGroup("多余的 if 语句", -1, False),
        score_tools.FixedLeafGroup("给无符号 size_t 赋值 -1", -1, False),
        score_tools.FixedLeafGroup("未删除不必要的注释和打印", -1, False)
        
    ],
    maximum=1, minimum=0, basic_score=1
)
robust = score_tools.AddGroup(
    "鲁棒性",
    subgroups=[
        score_tools.FixedLeafGroup("每次单击的时候都会重新构造一个 polygon", -1, False),
        score_tools.FixedLeafGroup("没有形状时单击 Fill 按钮程序崩溃", -1, False),
        score_tools.FixedLeafGroup("Freehand 按钮后双击右键会崩溃", -1, False),
        score_tools.FixedLeafGroup("椭圆向左上方拖动会变成菱形", -1, False),
        score_tools.FixedLeafGroup("绘制下一个polygon，但是程序异常退出",-1,False),
        score_tools.FixedLeafGroup("Polygon右键程序崩溃",-1,False),
        # score_tools.MercifulLeafGroup("我很仁慈 (Merciful节点)")
        ],
    maximum=2,minimum=0, basic_score=2
)

prog = score_tools.AddGroup(
    "程序",subgroups=[
        polymorphism, standard,robust
    ],
    maximum=100, minimum=0, basic_score=0
)

# 报告
report = score_tools.AddGroup(
    "报告",
    subgroups=[
        
        score_tools.FixedLeafGroup("不常见的绘制操作缺少说明", -1, False),
        score_tools.FixedLeafGroup("报告中没有类图", -2, False),
        score_tools.FixedLeafGroup("图片太小", -1, False),
        
    ],
    maximum=100,minimum=0, basic_score=5
)


freehand = score_tools.MutableLeafGroup("Freehand(B)", 1, score_min=0, initial=0)
redo = score_tools.MutableLeafGroup("Redo/Undo(B)", 1, score_min=0, initial=0)
thickness = score_tools.MutableLeafGroup("Thickness(B)", 1, score_min=0, initial=0)
otherfunc = score_tools.MutableLeafGroup("Other functions(B)", 1, score_min=0, initial=0)


better_struct = score_tools.MutableLeafGroup("优化了代码结构(B)", 1, score_min=0, initial=0)

good_report = score_tools.MutableLeafGroup("详细完整美观(B)", 1, score_min=0, initial=0)

all_score = score_tools.AverageGroup("总成绩",subgroups=[
    score_tools.AddGroup("功能 (with bonus)", [grp_func, freehand, redo,thickness,otherfunc], maximum=5.5, minimum=0),
    score_tools.AddGroup("代码 (with bonus)", [prog, better_struct], maximum=5.5, minimum=0),
    score_tools.AddGroup("报告 (with bonus)", [report, good_report], maximum=5.5, minimum=0)
    
    # grp_func, prog, report, 
], maximum=5.5, minimum=0, basic_score=0)

score_tools.run_group(all_score, addon="每一项不考虑bonus单独算分，然后再加上bonus（封顶5.5），最后三项平均")