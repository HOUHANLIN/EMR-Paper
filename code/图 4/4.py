from graphviz import Digraph


def build_hybrid_flowchart(out_name="口腔语音电子病历系统流程图_综合版", fmt="png"):
    """
    综合 2.py 的“整体分阶段长文本说明”和 3.py 的
    “簇状细化步骤 + 闭环回流结构”，生成一个更加完整的图四。
    """
    g = Digraph(name="EMR_System_Hybrid", format=fmt)

    # ===== 全局布局（沿用 3.py 的簇状结构 + 2.py 的直观主链）=====
    g.attr(
        compound="true",
        rankdir="TB",
        splines="ortho",
        nodesep="0.40",
        ranksep="0.55",
        fontname="Microsoft YaHei",
    )
    g.attr("node", shape="box", style="filled", fontname="Microsoft YaHei",
           fontsize="11", margin="0.20,0.10")
    g.attr("edge", color="#cc6666", penwidth="1.2", arrowsize="0.80",
           fontname="Microsoft YaHei", fontsize="10")

    # ===== 通用样式（来自 3.py）=====
    style_title = {
        "fillcolor": "#e9a2a2",
        "fontsize": "18",
        "width": "9.5",
        "height": "0.8",
    }
    style_stage_header = {
        "fillcolor": "#f4c7c7",
        "fontsize": "13",
        "width": "8.6",
        "height": "0.45",
    }
    style_process = {
        "fillcolor": "#ffffff",
        "fontsize": "10.5",
        "width": "7.8",
        "color": "#555555",
    }
    style_stage_summary = {
        "fillcolor": "#ffffff",
        "fontsize": "10.5",
        "width": "9.0",
        "color": "#333333",
    }

    # ===== 0. 总标题（沿用 2.py 文案 + 3.py 样式）=====
    g.node(
        "MAIN_TITLE",
        "基于 ASR 专科优化与 LLM 槽位提取的\n口腔医疗语音电子病历生成系统研发",
        **style_title,
    )

    # ==================== 阶段一：数据集构建与标准化 ====================
    with g.subgraph(name="cluster_stage1") as c:
        c.attr(label="", style="dashed", color="#dddddd")

        c.node(
            "S1_Title",
            "（1）口腔种植科语音–病历配对数据集构建与标准化处理",
            **style_stage_header,
        )

        # 细化步骤（来自 3.py 的结构）
        c.node(
            "S1_1",
            "① 数据来源\n(虚拟病例420例 + 真实病例2000+例)",
            **style_process,
        )
        c.node(
            "S1_2",
            "② 语音-文本配对\n(专家撰写金标准 + 问诊录音复刻)",
            **style_process,
        )
        c.node(
            "S1_3",
            "③ 预处理与标准化\n(降噪/静音切分 + 术语映射/纠错)",
            **style_process,
        )
        c.node(
            "S1_4",
            "④ 数据集划分\n(训练集 / 验证集 / 测试集)",
            **style_process,
        )

        # 阶段总结（来自 2.py 的长文本精简版）
        c.node(
            "S1_SUM",
            "综合说明：\n"
            "· 虚拟病例 420 例（7 名种植科医生基于临床经验构建）\n"
            "· 真实病例 2000+ 例，经脱敏与伦理审批\n"
            "· 语音：降噪、静音切分、格式统一（单声道 PCM）\n"
            "· 文本：术语库映射 + 错词库纠错，形成标准化病历语料",
            **style_stage_summary,
        )

        # 内部连接：标题 → 步骤 → 总结
        c.edge("S1_Title", "S1_1", style="invis")
        c.edge("S1_1", "S1_2")
        c.edge("S1_2", "S1_3")
        c.edge("S1_3", "S1_4")
        c.edge("S1_4", "S1_SUM")

    # ==================== 阶段二：ASR–LLM 协同模型与模板化生成 ====================
    with g.subgraph(name="cluster_stage2") as c:
        c.attr(label="", style="dashed", color="#dddddd")

        c.node(
            "S2_Title",
            "（2）专科适配的 ASR–LLM 协同模型搭建与模板化生成机制开发",
            **style_stage_header,
        )

        # 并行关键子模块（来自 3.py）
        c.node(
            "S2_1",
            "① ASR 专科优化\n(引入口腔种植专科热词库，降低 WER)",
            **style_process,
        )
        c.node(
            "S2_2",
            "② 种植科模板库构建\n(覆盖初诊/复诊/术前/术后等场景)",
            **style_process,
        )

        c.node(
            "S2_3",
            "③ LLM 槽位信息提取\n(严格槽位映射 JSON，禁止自由补写)",
            **style_process,
        )
        c.node(
            "S2_4",
            "④ 协同训练与优化\n(先单独微调，再端到端协同)",
            **style_process,
        )

        # 阶段总结（吸收 2.py 中 S2C 的完整要点）
        c.node(
            "S2_SUM",
            "综合说明：\n"
            "· 基于腾讯开源 ASR，引入口腔种植专科热词库，提升低频术语识别率\n"
            "· 构建 7 大类、18 个核心槽位的种植科模板库，明确类型/必填/多值\n"
            "· LLM 输入为规范化文本 + 槽位定义，仅输出结构化槽位–文本映射（如 JSON），"
            "明确禁止补写原文中不存在信息以减轻幻觉\n"
            "· 采用“先分别微调，再端到端协同优化”的策略，兼顾识别准确率与提取精确率/召回率",
            **style_stage_summary,
        )

        c.edge("S2_Title", "S2_1", style="invis")
        c.edge("S2_Title", "S2_2", style="invis")
        c.edge("S2_1", "S2_3")
        c.edge("S2_2", "S2_3")
        c.edge("S2_3", "S2_4")
        c.edge("S2_4", "S2_SUM")

    # ==================== 阶段三：系统集成与多维度临床验证 ====================
    with g.subgraph(name="cluster_stage3") as c:
        c.attr(label="", style="dashed", color="#dddddd")

        c.node(
            "S3_Title",
            "（3）系统集成与多维度临床验证（基于双重测试体系）",
            **style_stage_header,
        )

        c.node(
            "S3_1",
            "① 系统功能集成\n(前端采集/预览/编辑 + 后端推理/存储)",
            **style_process,
        )
        c.node(
            "S3_2",
            "② 建立双重测试体系\n(回顾性测试 + 前瞻性临床对照)",
            **style_process,
        )

        # 阶段总结（结合 2.py S3C 的细节）
        c.node(
            "S3_SUM",
            "综合说明：\n"
            "· 前端：语音采集、识别结果预览、病历编辑与导出\n"
            "· 后端：ASR–LLM 协同模型 + 数据库支撑语音→结构化病历全流程\n"
            "· 回顾性：以脱敏真实病例的金标准病历为基准，评估准确度、覆盖率、相似度、"
            "术语规范率及幻觉率\n"
            "· 前瞻性：试验组（语音电子病历） vs 对照组（传统键盘录入），随访约 3 个月，"
            "观察效率（耗时/日均量）、质量（完整性/准确性/逻辑一致性）及主观满意度",
            **style_stage_summary,
        )

        c.edge("S3_Title", "S3_1", style="invis")
        c.edge("S3_1", "S3_2")
        c.edge("S3_2", "S3_SUM")

    # ==================== 阶段四：多维评估与消融实验 ====================
    with g.subgraph(name="cluster_stage4") as c:
        c.attr(label="", style="dashed", color="#dddddd")

        c.node(
            "S4_Title",
            "（4）多维度评估与消融实验",
            **style_stage_header,
        )

        c.node(
            "S4_1",
            "① 客观指标评估\n(精确率 / 召回率 / F1 等)",
            **style_process,
        )
        c.node(
            "S4_2",
            "② 医生主观盲评\n(5 级 Likert 量表：准确性/完整性/逻辑性等)",
            **style_process,
        )
        c.node(
            "S4_3",
            "③ 幻觉与效率分析\n(幻觉率 + 书写/修改耗时与次数)",
            **style_process,
        )
        c.node(
            "S4_4",
            "④ 消融实验验证\n(对比模板约束+信息提取 vs 自由生成式 LLM)",
            **style_process,
        )

        c.node(
            "S4_SUM",
            "综合说明：\n"
            "· 客观指标：精确率、召回率、F1，信息覆盖率，文本相似度，术语规范率\n"
            "· 主观评价：种植科医生基于 5 级 Likert 量表，从完整性、准确性、逻辑一致性等"
            "多个维度进行盲评\n"
            "· 幻觉与效率：统计幻觉发生率，记录书写与修改耗时及修改次数\n"
            "· 消融实验：比较“模板约束+槽位提取”与“自由生成式 LLM”的性能差异，"
            "验证前者在抑制幻觉与提升规范性中的作用",
            **style_stage_summary,
        )

        c.edge("S4_Title", "S4_1", style="invis")
        c.edge("S4_1", "S4_2")
        c.edge("S4_2", "S4_3")
        c.edge("S4_3", "S4_4")
        c.edge("S4_4", "S4_SUM")

    # ==================== 阶段五：迭代优化（闭环） ====================
    with g.subgraph(name="cluster_stage5") as c:
        c.attr(label="", style="dashed", color="#dddddd")

        c.node(
            "S5_Title",
            "（5）迭代优化（闭环）",
            **style_stage_header,
        )

        c.node(
            "S5_1",
            "① 收集临床反馈与错误案例\n(医生修改记录、失败样本)",
            **style_process,
        )
        c.node(
            "S5_2",
            "② 策略更新与模型重训\n(热词库/术语库/模板与模型迭代)",
            **style_process,
        )

        c.node(
            "S5_SUM",
            "综合说明：\n"
            "· 持续收集临床一线反馈与错误案例\n"
            "· 基于反馈更新专科热词库、错词库与术语库\n"
            "· 对模板槽位定义和 ASR–LLM 模型进行周期性微调与重训，"
            "目标是降低医生审核修改率、提升系统临床适配性",
            **style_stage_summary,
        )

        c.edge("S5_Title", "S5_1", style="invis")
        c.edge("S5_1", "S5_2")
        c.edge("S5_2", "S5_SUM")

    # ==================== 阶段间主干连接（兼顾 2.py 与 3.py） ====================
    g.edge("MAIN_TITLE", "S1_Title")
    g.edge("S1_SUM", "S2_Title", minlen="2")
    g.edge("S2_SUM", "S3_Title", minlen="2")
    g.edge("S3_SUM", "S4_Title", minlen="2")
    g.edge("S4_SUM", "S5_Title", minlen="2")

    # ==================== 闭环回流（结合 2.py 与 3.py 的优点） ====================
    # 从阶段五的更新策略回流到“数据/标准化”和“模型/模板”，
    # 同时兼顾 2.py 中“大阶段回流”的直观性。
    g.edge(
        "S5_2",
        "S1_3",
        label=" 更新术语/错词库\n反哺数据标准化流程",
        style="dashed",
        color="#888888",
        constraint="false",
    )
    g.edge(
        "S5_2",
        "S2_1",
        label=" 迭代 ASR/LLM 参数\n与模板库设计",
        style="dashed",
        color="#888888",
        constraint="false",
    )

    # 【可选】如需更直观的大阶段回流箭头，也可以保留到阶段标题的虚线：
    g.edge(
        "S5_SUM",
        "S1_Title",
        label=" 临床反馈闭环：数据与标准更新",
        style="dashed",
        color="#bbbbbb",
        constraint="false",
    )

    # 生成图片
    g.render(out_name, cleanup=True)
    print(f"已生成综合版流程图：{out_name}.{fmt}")


if __name__ == "__main__":
    build_hybrid_flowchart(fmt="png")

