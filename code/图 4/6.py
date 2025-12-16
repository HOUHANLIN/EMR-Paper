from graphviz import Digraph

def build_flowchart(out_name="口腔语音电子病历系统流程图_v3", fmt="png"):
    g = Digraph(name="EMR_System", format=fmt)

    # ===== 全局布局 =====
    g.attr(
        rankdir="TB",
        splines="ortho",
        nodesep="0.30",
        ranksep="0.45",
        fontname="Microsoft YaHei"
    )
    g.attr("node", shape="box", fontname="Microsoft YaHei", color="#333333")
    g.attr("edge", color="#cc6666", penwidth="1.2", arrowsize="0.9")

    # ===== 大标题 =====
    g.node(
        "TITLE",
        "基于 ASR 专科优化与 LLM 槽位提取的\n口腔医疗语音电子病历生成系统研发",
        style="filled",
        fillcolor="#e9a2a2",
        fontsize="20",
        width="10.5",
        height="0.8"
    )

    # ========== 阶段一 ==========
    g.node(
        "STAGE1",
        "（1）口腔种植科语音–病历配对数据集构建与标准化处理",
        style="filled",
        fillcolor="#f4c7c7",
        fontsize="14",
        width="9.6",
        height="0.45"
    )
    g.node(
        "S1C",
        "① 数据来源：\n"
        "   - 虚拟病例 420 例，7 名种植科医生基于临床经验模拟构建\n"
        "   - 真实病例 2000+ 例，经脱敏与伦理审批\n"
        "② 语音–文本配对：\n"
        "   - 虚拟病例：专家撰写金标准电子病历 + 口语化录音\n"
        "   - 真实病例：复刻问诊语音 + 对应金标准病历\n"
        "③ 预处理与标准化：\n"
        "   - 语音：降噪、静音切分、格式统一（单声道 PCM）\n"
        "   - 文本：术语库映射 + 错词库纠错\n"
        "   - 划分：虚拟→训练/验证集，真实→测试集",
        style="filled",
        fillcolor="#ffffff",
        fontsize="10.5",
        width="9.6"
    )

    # ========== 阶段二 ==========
    g.node(
        "STAGE2",
        "（2）专科适配的 ASR–LLM 协同模型搭建与模板化生成机制开发",
        style="filled",
        fillcolor="#f4c7c7",
        fontsize="14",
        width="9.6",
        height="0.45"
    )
    g.node(
        "S2C",
        "① ASR 专科优化：\n"
        "   - 基于腾讯开源 ASR，引入口腔种植专科热词库\n"
        "   - 降低 WER/SER，提升低频术语识别率\n"
        "② 种植科模板库：\n"
        "   - 覆盖初诊、复诊、术前评估、术后随访等场景\n"
        "   - 7 大类、18 个核心槽位，明确类型/必填/多值及版本更新策略\n"
        "③ LLM 槽位信息提取（非自由生成）：\n"
        "   - 输入：规范化文本 + 槽位定义；输出结构化槽位–文本映射（如 JSON）\n"
        "   - 明确禁止补写原文中不存在信息，减轻幻觉\n"
        "④ 协同训练与优化：\n"
        "   - 先分别微调 ASR 与 LLM，再进行端到端协同优化\n"
        "   - 兼顾识别准确率与提取精确率/召回率",
        style="filled",
        fillcolor="#ffffff",
        fontsize="10.5",
        width="9.6"
    )

    # ========== 阶段三（标题不变，内容合并） ==========
    g.node(
        "STAGE3",
        "（3）系统集成与多维度临床验证（基于双重测试体系）",
        style="filled",
        fillcolor="#f4c7c7",
        fontsize="14",
        width="9.6",
        height="0.45"
    )
    g.node(
        "S3C",
        "① 系统功能集成：\n"
        "   - 前端：语音采集、结果预览、病历编辑与导出\n"
        "   - 后端：ASR–LLM 协同模型 + 数据库，支持语音→结构化病历全流程\n"
        "② 双重测试体系：\n"
        "   - 回顾性：以脱敏真实病例的金标准病历为基准，评估准确度、覆盖率、相似度、术语规范率及幻觉率\n"
        "   - 前瞻性：种植科医生试验组 vs 对照组（传统键盘录入），随访约 3 个月\n"
        "   - 观察效率（耗时、日均量）、质量（完整性、准确性、逻辑一致性）及主观满意度\n"
        "③ 多维度评估指标：\n"
        "   - 客观：精确率、召回率、F1、信息覆盖率、文本相似度、术语规范率\n"
        "   - 主观：种植科医生 5 级 Likert 量表，7 维度盲评\n"
        "   - 幻觉与效率：幻觉发生率、修改耗时、修改次数\n"
        "④ 消融实验：\n"
        "   - 对比“模板约束+信息提取”与“自由生成式 LLM”\n"
        "   - 验证模板化策略在抑制幻觉与提升规范性中的作用",
        style="filled",
        fillcolor="#ffffff",
        fontsize="10.5",
        width="9.6"
    )

    # ========== 阶段五 ==========
    g.node(
        "STAGE5",
        "（4）迭代优化（闭环）",
        style="filled",
        fillcolor="#f4c7c7",
        fontsize="14",
        width="9.6",
        height="0.45"
    )
    g.node(
        "S5C",
        "基于双重测试与临床试用反馈持续优化：\n"
        "- 更新专科热词库、错词库与术语库\n"
        "- 微调模型参数与模板槽位定义\n"
        "- 降低医生审核修改率，提升系统临床适配性",
        style="filled",
        fillcolor="#ffffff",
        fontsize="10.5",
        width="9.6"
    )

    # ===== 主流程 =====
    g.edge("TITLE", "STAGE1")
    g.edge("STAGE1", "S1C")

    g.edge("S1C", "STAGE2")
    g.edge("STAGE2", "S2C")

    g.edge("S2C", "STAGE3")
    g.edge("STAGE3", "S3C")

    g.edge("S3C", "STAGE5")
    g.edge("STAGE5", "S5C")

    # ===== 闭环回流 =====
    g.edge("S5C", "STAGE1", style="dashed", color="#888888", penwidth="1.1", label=" 反馈回流：数据/标准化更新")
    g.edge("S5C", "STAGE2", style="dashed", color="#888888", penwidth="1.1", label=" 反馈回流：模型/模板迭代")

    # 输出
    g.render(out_name, cleanup=True)
    print(f"已生成：{out_name}.{fmt}")

if __name__ == "__main__":
    build_flowchart(fmt="png")  # png / svg / pdf（论文建议 svg/pdf）