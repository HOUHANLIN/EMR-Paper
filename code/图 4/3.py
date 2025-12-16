from graphviz import Digraph

def build_detailed_flowchart(out_name="口腔语音电子病历系统流程图_细化版", fmt="png"):
    g = Digraph(name="EMR_System_Detailed", format=fmt)

    # ===== 全局布局设置 =====
    # compound='true' 允许在簇(cluster)之间连线
    g.attr(compound='true', rankdir="TB", splines="ortho", nodesep="0.4", ranksep="0.5", fontname="Microsoft YaHei")
    g.attr("node", shape="box", style="filled", fontname="Microsoft YaHei", fontsize="12", margin="0.2,0.1")
    g.attr("edge", color="#cc6666", penwidth="1.2", arrowsize="0.8", fontname="Microsoft YaHei", fontsize="10")

    # 定义通用样式
    style_title = {"fillcolor": "#e9a2a2", "fontsize": "18", "width": "8", "height": "0.8"}
    style_stage_header = {"fillcolor": "#f4c7c7", "fontsize": "14", "width": "7", "height": "0.5"}
    style_process = {"fillcolor": "#ffffff", "fontsize": "11", "width": "6", "color": "#555555"}

    # ===== 0. 总标题 =====
    g.node("MAIN_TITLE", "基于 ASR 专科优化与 LLM 槽位提取的\n口腔医疗语音电子病历生成系统研发", **style_title)

    # ==================== 阶段一：数据集构建 ====================
    with g.subgraph(name="cluster_stage1") as c:
        c.attr(label="", style="dashed", color="#dddddd")  # 簇的边框设置
        
        # 阶段标题
        c.node("S1_Title", "（1）数据集构建与标准化处理", **style_stage_header)
        
        # 细分步骤
        c.node("S1_1", "① 数据来源\n(虚拟病例420例 + 真实病例2000+例)", **style_process)
        c.node("S1_2", "② 语音-文本配对\n(专家撰写金标准 + 问诊录音复刻)", **style_process)
        c.node("S1_3", "③ 预处理与标准化\n(降噪/静音切分 + 术语映射/纠错)", **style_process)
        c.node("S1_4", "④ 数据集划分\n(训练集 / 验证集 / 测试集)", **style_process)

        # 内部连接
        c.edge("S1_Title", "S1_1", style="invis") # 隐形线辅助布局
        c.edge("S1_1", "S1_2")
        c.edge("S1_2", "S1_3")
        c.edge("S1_3", "S1_4")

    # ==================== 阶段二：模型研发 ====================
    with g.subgraph(name="cluster_stage2") as c:
        c.attr(label="", style="dashed", color="#dddddd")
        
        c.node("S2_Title", "（2）ASR-LLM 协同模型与模板化生成", **style_stage_header)
        
        # 并行步骤：ASR优化 和 模板定义
        c.node("S2_1", "① ASR 专科优化\n(引入种植科热词库，降低WER)", **style_process)
        c.node("S2_2", "② 种植科模板库构建\n(7大类场景，18个核心槽位定义)", **style_process)
        
        # 汇聚步骤
        c.node("S2_3", "③ LLM 槽位信息提取\n(禁止自由生成，严格映射JSON)", **style_process)
        c.node("S2_4", "④ 协同训练与微调\n(ASR与LLM端到端联合优化)", **style_process)

        # 内部连接
        c.edge("S2_Title", "S2_1", style="invis")
        c.edge("S2_Title", "S2_2", style="invis")
        # 简单的分支结构
        c.edge("S2_1", "S2_3")
        c.edge("S2_2", "S2_3")
        c.edge("S2_3", "S2_4")

    # ==================== 阶段三：系统集成与验证 ====================
    with g.subgraph(name="cluster_stage3") as c:
        c.attr(label="", style="dashed", color="#dddddd")
        
        c.node("S3_Title", "（3）系统集成与临床验证体系", **style_stage_header)
        
        c.node("S3_1", "① 全流程系统集成\n(前端采集交互 + 后端模型推理)", **style_process)
        c.node("S3_2", "② 建立双重测试体系\n(回顾性测试 + 前瞻性临床对照)", **style_process)

        c.edge("S3_Title", "S3_1", style="invis")
        c.edge("S3_1", "S3_2")

    # ==================== 阶段四：评估与消融 ====================
    with g.subgraph(name="cluster_stage4") as c:
        c.attr(label="", style="dashed", color="#dddddd")
        
        c.node("S4_Title", "（4）多维度评估与消融实验", **style_stage_header)
        
        c.node("S4_1", "① 客观指标评估\n(F1值、覆盖率、术语规范率)", **style_process)
        c.node("S4_2", "② 医生主观盲评\n(5级Likert量表：准确性/完整性)", **style_process)
        c.node("S4_3", "③ 幻觉与效率分析\n(幻觉率统计 + 耗时/修改次数)", **style_process)
        c.node("S4_4", "④ 消融实验验证\n(验证“模板约束”对抑制幻觉的作用)", **style_process)

        c.edge("S4_Title", "S4_1", style="invis")
        c.edge("S4_1", "S4_2")
        c.edge("S4_2", "S4_3")
        c.edge("S4_3", "S4_4")

    # ==================== 阶段五：迭代优化 ====================
    with g.subgraph(name="cluster_stage5") as c:
        c.attr(label="", style="dashed", color="#dddddd")
        
        c.node("S5_Title", "（5）闭环迭代优化", **style_stage_header)
        
        c.node("S5_1", "① 收集临床反馈数据\n(错误案例与医生修改记录)", **style_process)
        c.node("S5_2", "② 系统策略更新\n(热词库更新、模板微调、模型重训)", **style_process)

        c.edge("S5_Title", "S5_1", style="invis")
        c.edge("S5_1", "S5_2")

    # ==================== 阶段间的主干连接 ====================
    # 注意：连接 cluster 内部的具体节点，使用 ltail/lhead 属性（需要 compound=true）
    # 但为了布局简单，直接连节点通常效果最好
    
    g.edge("MAIN_TITLE", "S1_Title")
    
    g.edge("S1_4", "S2_Title", minlen="2")
    g.edge("S2_4", "S3_Title", minlen="2")
    g.edge("S3_2", "S4_Title", minlen="2")
    g.edge("S4_4", "S5_Title", minlen="2")

    # ==================== 循环回流 (关键) ====================
    # 从 S5_2 (更新策略) 回流到 S1_3 (预处理/术语库) 和 S2_1 (ASR/模板)
    
    g.edge("S5_2", "S1_3", label=" 更新术语/错词库", style="dashed", color="#888888", constraint="false")
    g.edge("S5_2", "S2_1", label=" 迭代模型参数", style="dashed", color="#888888", constraint="false")

    # 生成图片
    g.render(out_name, cleanup=True)
    print(f"已生成细化版流程图：{out_name}.{fmt}")

if __name__ == "__main__":
    build_detailed_flowchart()