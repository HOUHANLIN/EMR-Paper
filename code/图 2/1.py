from graphviz import Digraph

def build_flowchart(out_name="flowchart", fmt="png"):
    g = Digraph("EMR_System", format=fmt)
    g.attr(rankdir="TB", splines="ortho", fontname="Microsoft YaHei")
    g.attr("node", shape="box", style="rounded", fontname="Microsoft YaHei",
           fontsize="12", color="#333333")
    g.attr("edge", color="#cc6666", penwidth="1.2")

    # ===== 顶层：系统目标 =====
    g.node("goal",
           "专科适配的语音生成电子病历智能系统\n（ASR 专科优化 + LLM 槽位提取 + 模板填充）",
           style="rounded,filled", fillcolor="#f2b6b6")

    # ===== 第二层：数据构建与标准化 =====
    with g.subgraph(name="cluster_data") as c:
        c.attr(label="（1）数据集构建与标准化处理", color="#f2b6b6", fontname="Microsoft YaHei")
        c.attr("node", style="rounded,filled", fillcolor="#ffffff")

        c.node("d1", "① 数据来源与构建\n- 虚拟病例开发（训练/验证，约 420）\n- 真实病历测试（2000+，脱敏/伦理）")
        c.node("d2", "② 语音与文本数据生成\n- 金标准结构化病历\n- 自然口语录音/转写\n- 回顾性/前瞻性采集")
        c.node("d3", "③ 预处理与标准化\n- 语音：降噪/切分/PCM\n- 文本：术语映射/错词纠正\n- 划分：训/验/测")
        c.edges([("d1", "d2"), ("d2", "d3")])

    # ===== 第三层：ASR–LLM 协同与模板化生成 =====
    with g.subgraph(name="cluster_model") as c:
        c.attr(label="（2）ASR–LLM 协同模型 + 模板化生成机制", color="#f2b6b6", fontname="Microsoft YaHei")
        c.attr("node", style="rounded,filled", fillcolor="#ffffff")

        c.node("m1", "① ASR 专科优化\n- 热词库/领域自适应微调\n- 降低 WER/SER")
        c.node("m2", "② 专科结构化模板库\n- 7 大类场景 + 18 核心槽位\n- 字段类型/必填/多值规则\n- 版本更新机制")
        c.node("m3", "③ LLM 槽位信息提取（非自由生成）\n- 输入：规范文本 + 槽位定义\n- 输出：JSON 槽位映射\n- 明确禁止补写不存在信息")
        c.node("m4", "④ 协同训练与优化\n- 先单训后协同（端到端）\n- 超参：学习率/批大小/轮数\n- 监控：TensorBoard")
        c.edges([("m1", "m2"), ("m2", "m3"), ("m3", "m4")])

    # ===== 第四层：系统集成与临床应用 =====
    with g.subgraph(name="cluster_system") as c:
        c.attr(label="（3）系统集成与临床验证（双重测试体系）", color="#f2b6b6", fontname="Microsoft YaHei")
        c.attr("node", style="rounded,filled", fillcolor="#ffffff")

        c.node("s1", "① 系统功能集成\n前端：采集/预览/编辑/导出\n后端：ASR→标准化→LLM提取→模板填充\n数据库：语音/标注/生成病历\n人机协同审核闭环")
        c.node("s2", "② 双重测试体系\n- 回顾性：以脱敏真实金标准为基准\n- 前瞻性：临床队列试用（试验组 vs 对照组，约 3 个月）")
        c.edge("s1", "s2")

    # ===== 第五层：评估与消融 =====
    with g.subgraph(name="cluster_eval") as c:
        c.attr(label="（4）多维度评估与消融实验", color="#f2b6b6", fontname="Microsoft YaHei")
        c.attr("node", style="rounded,filled", fillcolor="#ffffff")

        c.node("e1", "客观评估\n- 精确率/召回率/F1\n- 信息覆盖率（字段/内容）\n- 文本相似度（BERTScore/ROUGE-L）\n- 术语规范率")
        c.node("e2", "主观评估\n- 盲评医生\n- 5 级 Likert\n- 7 维度：完整性/准确性/一致性等")
        c.node("e3", "幻觉与效率评估\n- 幻觉发生率\n- 书写耗时/修改耗时\n- 修改次数")
        c.node("e4", "消融实验\n对比：\nA 模板约束+信息提取\nvs\nB 自由生成式 LLM")
        c.edges([("e1", "e2"), ("e2", "e3"), ("e3", "e4")])

    # ===== 迭代优化（闭环回指） =====
    g.node("iter", "迭代优化\n- 更新热词库/错词库/术语库\n- 调整模板槽位定义\n- 微调模型参数\n目标：降低医生修改率，提升适配性",
           style="rounded,filled", fillcolor="#f2b6b6")

    # 主链连接
    g.edge("goal", "d1")
    g.edge("d3", "m1")
    g.edge("m4", "s1")
    g.edge("s2", "e1")
    g.edge("e4", "iter")

    # 闭环回流：回到数据与模型
    g.edge("iter", "d1", style="dashed", color="#999999")
    g.edge("iter", "m1", style="dashed", color="#999999")

    # 输出文件
    g.render(out_name, cleanup=True)
    print(f"Saved: {out_name}.{fmt}")

if __name__ == "__main__":
    build_flowchart(out_name="flowchart", fmt="png")   # png / svg / pdf 都行