from graphviz import Digraph

def build_straight_flowchart(out_name="口腔语音EMR流程图_垂直校正版", fmt="png"):
    g = Digraph(name="EMR_System_Straight", format=fmt)

    # ===== 1. 全局配置：关键在于 newrank 和 splines =====
    g.attr(
        compound='true',       # 允许跨簇连线
        rankdir="TB",          # 从上到下
        splines="ortho",       # 折线风格
        nodesep="0.5",         # 节点左右间距
        ranksep="0.5",         # 节点上下层级间距
        fontname="Microsoft YaHei",
        newrank="true"         # 【关键】使用新排版引擎，对子图对齐更友好
    )

    # 节点默认样式
    g.attr("node", shape="box", style="filled", fontname="Microsoft YaHei", 
           fontsize="12", margin="0.25,0.1", color="#444444", fillcolor="#ffffff")
    
    # 线条默认样式
    g.attr("edge", color="#b05555", penwidth="1.2", arrowsize="0.8", fontname="Microsoft YaHei", fontsize="10")

    # === 样式定义 ===
    # 标题样式
    STYLE_TITLE = {"fillcolor": "#e9a2a2", "fontsize": "18", "width": "8", "height": "0.8", "penwidth":"0"}
    # 阶段标签（无框文字）
    STYLE_LABEL = {"shape": "plaintext", "fontsize": "13", "fontcolor": "#8b3a3a", "style": ""}
    # 步骤节点样式 (统一宽度，保证对齐)
    STYLE_STEP = {"fillcolor": "#ffffff", "fontsize": "11", "width": "6.0", "height":"0.6"}
    # 簇的样式 (背景色)
    ATTR_CLUSTER = {"style": "filled,rounded", "color": "#eecbc4", "fillcolor": "#fff9f9", "labeljust":"c"}

    # ================= 核心：定义节点 =================
    # 【重点】所有主干节点都加上 group='main'，强制它们在一条直线上

    # 0. 总标题
    g.node("MAIN_TITLE", "基于 ASR 专科优化与 LLM 槽位提取的\n口腔医疗语音电子病历生成系统研发", 
           **STYLE_TITLE, group="main")

    # 1. 阶段一
    with g.subgraph(name="cluster_stage1") as c:
        c.attr(**ATTR_CLUSTER)
        c.node("S1_Label", "阶段一：数据集构建与标准化", **STYLE_LABEL, group="main")
        c.node("S1_1", "① 数据采集：虚拟(420例) + 真实(2000+例)", **STYLE_STEP, group="main")
        c.node("S1_2", "② 语音-文本强制对齐 (Alignment)", **STYLE_STEP, group="main")
        c.node("S1_3", "③ 预处理：降噪、切分、术语库映射", **STYLE_STEP, group="main")
        
        # 簇内连接 (加大权重 weight=2 保证垂直优先)
        c.edge("S1_Label", "S1_1", style="invis", weight="10")
        c.edge("S1_1", "S1_2", weight="10")
        c.edge("S1_2", "S1_3", weight="10")

    # 2. 阶段二
    with g.subgraph(name="cluster_stage2") as c:
        c.attr(**ATTR_CLUSTER)
        c.node("S2_Label", "阶段二：ASR-LLM 协同模型开发", **STYLE_LABEL, group="main")
        
        # 此时遇到分叉。为了保持直，我们把“LLM槽位抽取”作为主干，其他的放在两侧或并行
        # 这里为了视觉垂直，我们将“ASR优化”放在左，“模板定义”放在右，或者让他们都拥有 group='main' 依次排列
        # 为了最直观的“垂直流”，建议设计成：ASR 和 模板 是前置条件，然后汇入主干
        
        # 技巧：用一个隐形的点或者其中一个步骤作为主轴。
        # 这里我们将 S2_3 (汇聚点) 设为主轴 group='main'
        
        c.node("S2_1", "① ASR 专科声学模型微调", **STYLE_STEP) # 不加 group，让它自动排
        c.node("S2_2", "② 种植科结构化模板定义 (JSON)", **STYLE_STEP) # 不加 group
        c.node("S2_3", "③ LLM 槽位抽取与约束生成", **STYLE_STEP, group="main") # 主干回归
        
        c.edge("S2_Label", "S2_1", style="invis")
        c.edge("S2_Label", "S2_2", style="invis")
        
        # 连接
        c.edge("S2_1", "S2_3")
        c.edge("S2_2", "S2_3")

    # 3. 阶段三
    with g.subgraph(name="cluster_stage3") as c:
        c.attr(**ATTR_CLUSTER)
        c.node("S3_Label", "阶段三：系统集成与临床验证", **STYLE_LABEL, group="main")
        c.node("S3_1", "① 前后端集成 (Web/App)", **STYLE_STEP, group="main")
        c.node("S3_2", "② 双重测试：回顾性验证 + 前瞻性试用", **STYLE_STEP, group="main")
        
        c.edge("S3_Label", "S3_1", style="invis", weight="10")
        c.edge("S3_1", "S3_2", weight="10")

    # 4. 阶段四
    with g.subgraph(name="cluster_stage4") as c:
        c.attr(**ATTR_CLUSTER)
        c.node("S4_Label", "阶段四：多维度评估与消融实验", **STYLE_LABEL, group="main")
        c.node("S4_1", "① 客观指标 (WER, F1, 覆盖率)", **STYLE_STEP, group="main")
        c.node("S4_2", "② 主观盲评 (准确性, 完整性, 逻辑性)", **STYLE_STEP, group="main")
        
        c.edge("S4_Label", "S4_1", style="invis", weight="10")
        c.edge("S4_1", "S4_2", weight="10")

    # 5. 阶段五
    with g.subgraph(name="cluster_stage5") as c:
        c.attr(**ATTR_CLUSTER)
        c.node("S5_Label", "阶段五：反馈与迭代优化", **STYLE_LABEL, group="main")
        c.node("S5_1", "① 收集修改记录与错误样本", **STYLE_STEP, group="main")
        c.node("S5_2", "② 策略更新：热词/模板/模型参数", **STYLE_STEP, group="main")
        
        c.edge("S5_Label", "S5_1", style="invis", weight="10")
        c.edge("S5_1", "S5_2", weight="10")

    # ================= 连接主流程 =================
    # 使用 high weight 确保它们垂直紧密连接
    g.edge("MAIN_TITLE", "S1_Label", style="invis", weight="10")
    g.edge("MAIN_TITLE", "S1_1", weight="10") 
    
    g.edge("S1_3", "S2_Label", style="invis", weight="10")
    # 这里有点特殊，S1_3 下来要分叉去 S2_1 和 S2_2
    # 我们画一条隐形的主线维持垂直度
    g.edge("S1_3", "S2_3", style="invis", weight="10") 
    
    # 实际的物理连接线
    g.edge("S1_3", "S2_1", constraint="true")
    g.edge("S1_3", "S2_2", constraint="true")

    g.edge("S2_3", "S3_Label", style="invis", weight="10")
    g.edge("S2_3", "S3_1", weight="10")

    g.edge("S3_2", "S4_Label", style="invis", weight="10")
    g.edge("S3_2", "S4_1", weight="10")

    g.edge("S4_2", "S5_Label", style="invis", weight="10")
    g.edge("S4_2", "S5_1", weight="10")

    # ================= 右侧循环回流 (防止歪斜的关键设置) =================
    
    # 设置1：constraint="false" -> 告诉布局算法这条线不参与层级计算，随意画，不要挤歪主干
    # 设置2：tailport="e" / headport="e" -> 强制从右边出入
    # 设置3：color="#888888" -> 灰色虚线

    edge_attr_loop = {
        "color": "#888888", 
        "style": "dashed", 
        "penwidth": "1.5", 
        "constraint": "false",
        "fontsize": "10",
        "fontcolor": "#555555"
    }

    # 回流线 A: 到数据处理
    g.edge("S5_2", "S1_3", 
           label="  反馈回流：更新术语库与错词库", 
           tailport="e", headport="e", 
           **edge_attr_loop)

    # 回流线 B: 到模型优化 (连到 S2_3 比较顺，或者连到 S2_1/S2_2)
    # 为了美观，连到 S2_3 (LLM部分) 的右侧，或者 S2 Cluster 的右侧
    g.edge("S5_2", "S2_3", 
           label="  反馈回流：迭代ASR与模板定义", 
           tailport="e", headport="e", 
           **edge_attr_loop)

    g.render(out_name, cleanup=True)
    print(f"已生成垂直校正版流程图：{out_name}.{fmt}")

if __name__ == "__main__":
    build_straight_flowchart()