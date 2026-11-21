# 中文去味写作（chinese-deai-writing）

一个 Agent Skill：把中文稿从机器拼装感改成真人写作。适用于中文帖子、长帖、文案的写作与改稿。

## 它做什么

- 先分层诊断：材料层、结构层、句式层、词汇层，顺序不能反。只修句式会修出表演出来的人味。
- 写之前先备材料：五件具体材料、假细节禁令、先找到说话位置。
- 改稿五遍：推进、拆表演、顺中文、清硬禁令、核事实，最后查结尾。
- 硬禁令清单：翻案腔、三项以上同构排比、提示性冒号、洞察路标词、商业黑话抬价、结尾升华等，命中即改。
- 短帖模式：100 到 300 字的帖子只跑六查（具体细节、翻案句、升华尾、黑话、同构、朗读），不跑量化指标。
- 自带检查脚本 `scripts/check_deai.py`：纯本地正则扫描硬禁令，只报告不改稿。
- 完整标记清单在 `references/patterns.md`（词汇、句式、结构、节奏、标点五层）。

## 方法来源

综合自公开方法与实测研究：blader/humanizer（Wikipedia 的 AI 写作特征指南）、数字生命卡兹克的 human-writing（活人感写作）、op7418/Humanizer-zh 的事实保真路线、lieflat-less-ai-tone 的配对量化实测，以及腾讯朱雀等检测器的第三方实测结论。本技能为独立蒸馏与再创作，不含上述项目的原文与脚本。

边界：去味的目标是给人读，不保证过任何 AI 检测器。

## 安装

```bash
npx skills add jessica-mrsmiley2/chinese-deai-writing
```

或把本仓库文件夹放进你的 agent 的 skills 目录。

## 结构

```
chinese-deai-writing/
├── SKILL.md            技能本体
├── skill.yaml          技能描述
├── references/
│   └── patterns.md     五层标记清单
└── scripts/
    └── check_deai.py   硬禁令扫描脚本（Python 3，无依赖）
```

## 检查脚本用法

```bash
python3 scripts/check_deai.py <稿件文件>
```

命中硬禁令退出码 1，其余 0。句长 CV 只在全文 350 字以上时给出。
