# EMR-Paper 团队协作指南

> 保留所有版权

本仓库是团队共同撰写与维护题为「生成式病历论文结构稿」的 LaTeX 项目，面向口腔科等专科场景，聚焦语音识别与大语言模型结合的电子病历生成。本文档说明团队成员如何高效协作、提交修改并生成 PDF。

## 协作流程

1. **获取最新代码**：在开始前执行 `git pull` 保持本地与远端同步。
2. **创建分支**：按功能创建分支，推荐命名为 `feature/<内容>`、`fix/<内容>` 或 `refine/<章节>`。
3. **编辑内容**：
   - 章节内容位于 `sections/` 下，对应 `abstract.tex`、`methods.tex`、`results.tex`、`discussion.tex` 等文件。
   - 如需新增章节，在 `sections/` 中创建 `xxx.tex`，并在 `main.tex` 中通过 `\input{sections/xxx}` 引入。
4. **自动编译与自测**：分支合并后 GitHub Actions 会自动编译 PDF，可在仓库的 **Actions** 页面查看生成记录与产物。必要时可在本地按下文命令自测，避免合并后失败。
5. **提交与推送**：遵循提交信息规范（见下节），完成本地测试后推送分支并发起合并请求。
6. **评审与归档**：
   - 评审人关注格式、引用、术语一致性以及图片/表格编号。
   - 重要版本请将生成的 `tmp/main.pdf` 及变更说明复制到 `archive/<日期>/` 目录。

## 提交信息规范

- 标题使用祈使句，说明改动目标，例如：`Update methods section with new dataset description`。
- 如涉及多个模块，可在正文列出要点：章节、图表编号、引用变化等。
- 大范围结构调整或版面修改需在提交正文中注明，以便评审关注。

## 仓库结构

```text
.
├── main.tex              # 主文档入口（ctexart）
├── archive/              # 历史版本与关键版本归档
├── sections/             # 各章节内容（可新增文件并在 main.tex 引用）
│   ├── abstract.tex      # 摘要与介绍
│   ├── methods.tex       # 材料与方法 / 实验设计
│   ├── results.tex       # 结果
│   ├── discussion.tex    # 讨论
│   ├── methods_refs.tex  # 方法部分参考文献
│   └── discussion_refs.tex # 讨论部分参考文献
├── docs/                 # 协作教程（Markdown、LaTeX、GitHub 使用说明）
├── media/                # 图像资源（示意图等）
│   └── image1.jpeg
├── tmp/                  # 编译生成的中间文件与 PDF
└── README.md
```

> 说明：`tmp/` 目录中可存放本地编译产物（如 `main.pdf`）。主分支合并成功后会由 GitHub Actions 自动编译，可在 **Actions** 页面下载最新 PDF；若需提前验证，可按下文命令在本地生成。

## 编译环境与命令

- **TeX 发行版**：推荐 TeX Live / MacTeX 2020 及以上版本。
- **编译引擎**：`xelatex`（默认）或 `lualatex`，UTF-8 编码，`ctexart` 文类。
- **主要宏包**：`ctex`、`graphicx`、`amsmath`、`amssymb`、`hyperref`、`geometry`（完整发行版一般包含）。

### 自动编译

- 分支合并进入默认分支后，GitHub Actions 会自动运行编译流程并上传 PDF 产物。
- 在仓库页面点击 **Actions** → 对应工作流运行记录，即可查看日志并下载 PDF（通常在 Artifacts 部分）。

### 本地快速验证（可选）

在项目根目录执行以下命令生成 PDF：

- 使用 `latexmk`（推荐）：
  ```bash
  latexmk -xelatex -output-directory=tmp main.tex
  ```
- 或使用原生 `xelatex`：
  ```bash
  xelatex -output-directory=tmp main.tex
  xelatex -output-directory=tmp main.tex
  ```

成功后 PDF 位于 `tmp/main.pdf`。

## 常见协作约定

- 图片与表格：
  - 图片统一放置在 `media/`，命名简洁（如 `pipeline-overview.pdf`）。
  - 在正文引用时使用 `\label{fig:...}`，保持编号连续。
- 引用与参考文献：
  - 方法与讨论部分的参考文献分别维护在 `sections/methods_refs.tex` 与 `sections/discussion_refs.tex`。
  - 新增引用请保证 BibTeX/LaTeX 语法正确，避免重复键值。
- 语言与术语：
  - 专业术语保持一致，重要缩写在首次出现时注明全称。
  - 对于口腔科专用词汇，如有新增热词或术语，请同步更新文中描述。
- 安全与隐私：
  - 仓库仅包含论文与示意图，不包含真实医疗数据或生产代码。
  - 若需添加实验数据或代码，请先与团队确认目录结构和脱敏要求。

