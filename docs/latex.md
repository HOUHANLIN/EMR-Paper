# LaTeX 使用要点（项目版）

> 适用于本仓库的论文写作与排版场景。

## 目录结构

- 主文件：`main.tex`（`ctexart`）。
- 章节：位于 `sections/`，通过 `\input{sections/<name>}` 引入。
- 媒体：放在 `media/`，引用时使用相对路径，如 `\includegraphics{media/pipeline.pdf}`。
- 参考文献：按章节拆分在 `sections/methods_refs.tex`、`sections/discussion_refs.tex`。

## 基本写作规范

- 字体编码：保持 UTF-8，编译使用 `xelatex` 或 `lualatex`。
- 段落：中文环境无需额外缩进控制，使用空行分段；必要时用 `\par`。
- 数学：行内 `$...$`，行间 `\[ ... \]` 或 `equation`、`align` 环境。
- 列表：`itemize`、`enumerate`，如需自定义标号可使用 `enumitem` 选项。
- 图表：
  - 图使用 `figure` + `\includegraphics`，表格使用 `table` + `tabular`。
  - 添加 `\caption{...}` 和 `\label{fig:...}` / `\label{tab:...}`，编号保持连续。
  - 图片尺寸建议用 `\includegraphics[width=0.8\textwidth]{...}` 控制。
- 交叉引用：使用 `\ref`/`\eqref`/`\cite`，确保标签唯一且语义化。

## 常用包与命令

- 已启用：`ctex`、`graphicx`、`amsmath`、`amssymb`、`hyperref`、`geometry`。
- 超链接：`\href{url}{text}`，或直接写 `[text](url)` 由 `hyperref` 处理。
- 页面设置：`geometry` 已配置常用页边距，如需调整请在 `main.tex` 中统一修改。

## 编译与检查

- CI：合并到默认分支后，GitHub Actions 会自动编译 PDF，可在 **Actions** 页面下载。
- 本地：推荐 `latexmk -xelatex -output-directory=tmp main.tex`，或运行两遍 `xelatex` 保证交叉引用更新。
- 错误排查：优先检查缺失图片路径、未定义引用、中文/英文符号混用等问题。

## 协作提示

- 章节新增：在 `sections/` 创建文件并在 `main.tex` 追加 `\input` 顺序。
- 图表命名：文件名简短且能反映内容（如 `ablation-results.pdf`）。
- 参考文献：保持 BibTeX 键值唯一，必要时去重或合并同义引用。
- 版本归档：重要版本的 PDF 与摘要可放入 `archive/<日期>/` 目录，便于回溯。
