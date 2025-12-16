from graphviz import Digraph

# ========= 全局黑白灰样式（只用黑/白/灰） =========
def apply_bw_theme(g: Digraph):
    # 图级别
    g.attr(
        splines="ortho",
        fontname="Microsoft YaHei",
        fontsize="12",
        color="#000000",
        bgcolor="#FFFFFF"
    )
    # 节点默认：白底黑边
    g.attr(
        "node",
        shape="box",
        style="rounded,filled",
        fillcolor="#FFFFFF",
        color="#000000",
        fontname="Microsoft YaHei",
        fontsize="12"
    )
    # 边默认：黑色
    g.attr(
        "edge",
        color="#000000",
        penwidth="1.2",
        arrowsize="0.8",
        fontname="Microsoft YaHei",
        fontsize="10"
    )


# ========= 图 X：数据集构建流程图（虚拟/真实两路径 + 共性主干 + 回流） =========
def build_fig_x(out_base="figX_dataset", fmt="png"):
    g = Digraph("FigX", format=fmt)
    apply_bw_theme(g)
    g.attr(rankdir="TB")

    # --- 起点：两种数据来源（只用灰度区别路径） ---
    # 虚拟病例：浅灰；真实病例：中灰（仍在黑白灰范围）
    g.node("src_virtual", "虚拟病例（420例）", fillcolor="#F2F2F2")
    g.node("src_real", "真实病例（2000例，脱敏处理）", fillcolor="#D9D9D9")

    # --- 共性流程主干（白底） ---
    g.node("n1", "信息校验")
    g.node("n2", "伦理审核")
    g.node("n3", "语音采集")
    g.node("n4", "语音预处理（语音工具）")
    g.node("n5", "文本标准化（术语库/错词库）")
    g.node("n6", "质量校验")

    # --- 输出（与来源一致灰度） ---
    g.node("out_train", "训练集 / 验证集", fillcolor="#F2F2F2")
    g.node("out_test", "测试集", fillcolor="#D9D9D9")

    # --- 连接：两路汇入主干第一节点 ---
    # 用线型区分路径（仍是黑白灰）：虚拟=实线；真实=点划线
    g.edge("src_virtual", "n1", style="solid")
    g.edge("src_real", "n1", style="dashed")

    # 主干串联
    g.edge("n1", "n2")
    g.edge("n2", "n3")
    g.edge("n3", "n4")
    g.edge("n4", "n5")
    g.edge("n5", "n6")

    # 质量不达标回流（虚线回到“语音采集”，不加文字说明）
    g.edge("n6", "n3", style="dashed", color="#7F7F7F")

    # 输出：从质量校验分叉到两类输出（沿用路径线型）
    g.edge("n6", "out_train", style="solid")
    g.edge("n6", "out_test", style="dashed")

    g.render(out_base, cleanup=True)
    print(f"Saved: {out_base}.{fmt}")


# ========= 图 Y：ASR-LLM 协同模型工作架构图（横向流水线） =========
def build_fig_y(out_base="figY_asr_llm", fmt="png"):
    g = Digraph("FigY", format=fmt)
    apply_bw_theme(g)
    g.attr(rankdir="LR")  # 横向

    # 输入/输出略深灰强调边界（仍是灰度）
    g.node("in_audio", "输入：语音数据", fillcolor="#F2F2F2")

    # 模块层
    # 仅用灰度强调关键模块（LLM）：中灰
    g.node("asr", "ASR（专科优化）", fillcolor="#FFFFFF")
    g.node("norm", "文本标准化", fillcolor="#FFFFFF")
    g.node("llm", "LLM（信息提取，降低幻觉）", fillcolor="#D9D9D9")
    g.node("tmpl", "模板填充", fillcolor="#FFFFFF")

    g.node("out_emr", "输出：结构化病历", fillcolor="#F2F2F2")

    # 串联
    g.edge("in_audio", "asr")
    g.edge("asr", "norm")
    g.edge("norm", "llm")
    g.edge("llm", "tmpl")
    g.edge("tmpl", "out_emr")

    g.render(out_base, cleanup=True)
    print(f"Saved: {out_base}.{fmt}")


# ========= 图 Z（右图）：系统功能流程图（实线正向 + 虚线回流，末端导出/HIS分支） =========
def build_fig_z(out_base="figZ_system_flow", fmt="png"):
    g = Digraph("FigZ", format=fmt)
    apply_bw_theme(g)
    g.attr(rankdir="TB")

    # 主流程节点
    g.node("z1", "语音输入", fillcolor="#F2F2F2")  # 起点浅灰
    g.node("z2", "转写")
    g.node("z3", "标准化")
    g.node("z4", "填充")
    g.node("z5", "审核", fillcolor="#D9D9D9")     # 审核强调中灰

    # 末端分支
    g.node("z6a", "导出", fillcolor="#F2F2F2")
    g.node("z6b", "对接 HIS", fillcolor="#F2F2F2")

    # 正向主流程：实线
    g.edge("z1", "z2", style="solid")
    g.edge("z2", "z3", style="solid")
    g.edge("z3", "z4", style="solid")
    g.edge("z4", "z5", style="solid")

    # 审核后分支：实线
    g.edge("z5", "z6a", style="solid")
    g.edge("z5", "z6b", style="solid")

    # 回流：虚线（不加产出物标注）
    # 你可以只保留一条回流；这里给两条典型回流
    g.edge("z5", "z4", style="dashed", color="#7F7F7F")  # 回到填充
    g.edge("z5", "z3", style="dashed", color="#7F7F7F")  # 回到标准化

    g.render(out_base, cleanup=True)
    print(f"Saved: {out_base}.{fmt}")


if __name__ == "__main__":
    # 生成 PNG
    build_fig_x(fmt="png")
    build_fig_y(fmt="png")
    build_fig_z(fmt="png")

    # 如需 SVG（论文排版更推荐），取消下面注释：
    # build_fig_x(out_base="figX_dataset", fmt="svg")
    # build_fig_y(out_base="figY_asr_llm", fmt="svg")
    # build_fig_z(out_base="figZ_system_flow", fmt="svg")