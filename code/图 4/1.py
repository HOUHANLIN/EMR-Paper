from graphviz import Digraph

g = Digraph(
    name="EMR_System",
    format="png",   # 改成 pdf / svg 也可以
)

# ===== 全局样式 =====
g.attr(rankdir="TB", fontname="Microsoft YaHei")
g.attr("node", shape="box", fontname="Microsoft YaHei")

# ===== 一级大标题 =====
g.node(
    "TITLE",
    "基于 ASR 专科优化与 LLM 槽位提取的\n口腔医疗语音电子病历生成系统研发",
    shape="box",
    style="filled",
    fillcolor="#e9a2a2",
    fontsize="20",
    width="10"
)

# ===== 第一阶段 =====
g.node(
    "STAGE1",
    "阶段一：数据构建与标准化处理",
    style="filled",
    fillcolor="#f4c7c7",
    fontsize="14",
    width="8"
)

g.node(
    "S1C",
    "1. 数据来源构建：\n"
    "   - 虚拟病例开发（训练/验证）\n"
    "   - 脱敏真实病历测试集\n\n"
    "2. 语音与文本生成：\n"
    "   - 金标准结构化病历\n"
    "   - 自然口语语音采集\n\n"
    "3. 数据预处理与标准化：\n"
    "   - 语音降噪、切分、格式统一\n"
    "   - 医学术语映射与错词纠正",
    style="filled",
    fillcolor="#ffffff",
    fontsize="11",
    width="8"
)

# ===== 第二阶段 =====
g.node(
    "STAGE2",
    "阶段二：ASR–LLM 协同建模与模板化生成",
    style="filled",
    fillcolor="#f4c7c7",
    fontsize="14",
    width="8"
)

g.node(
    "S2C",
    "1. ASR 专科优化：\n"
    "   - 口腔种植热词库\n"
    "   - 领域自适应微调，降低 WER\n\n"
    "2. 专科结构化模板库：\n"
    "   - 多场景模板设计\n"
    "   - 槽位字段类型与约束定义\n\n"
    "3. LLM 槽位信息提取：\n"
    "   - 非自由生成，仅限信息抽取\n"
    "   - 输出结构化电子病历",
    style="filled",
    fillcolor="#ffffff",
    fontsize="11",
    width="8"
)

# ===== 第三阶段 =====
g.node(
    "STAGE3",
    "阶段三：系统验证与临床应用评估",
    style="filled",
    fillcolor="#f4c7c7",
    fontsize="14",
    width="8"
)

g.node(
    "S3C",
    "1. 系统功能验证：\n"
    "   - 语音输入 → 自动生成病历\n\n"
    "2. 客观评估：\n"
    "   - 精确率、召回率、F1\n"
    "   - 信息覆盖率、术语规范率\n\n"
    "3. 临床应用测试：\n"
    "   - 回顾性与前瞻性对照试验\n"
    "   - 医生效率与幻觉发生率评估",
    style="filled",
    fillcolor="#ffffff",
    fontsize="11",
    width="8"
)

# ===== 连接关系 =====
g.edge("TITLE", "STAGE1")
g.edge("STAGE1", "S1C")

g.edge("S1C", "STAGE2")
g.edge("STAGE2", "S2C")

g.edge("S2C", "STAGE3")
g.edge("STAGE3", "S3C")

# ===== 输出 =====
g.render("口腔语音电子病历系统流程图", cleanup=True)
print("流程图已生成")