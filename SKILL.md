# 中文去味写作

## 先分层诊断

- 动手前先判断这篇稿子的问题出在哪一层，顺序是材料层、结构层、句式层、词汇层

- 材料层先查三件事，作者有没有一个真实判断，判断有没有具体材料托住，说话的人站在什么位置

- 前两层是空的就先停下改词，词改得再干净也只是把机器稿擦亮，读者照样闻得出味

- 结构层查段落是否同构，推进是否靠材料和因果，结尾有没有临时升华到正文没处理过的尺度

- 句式层和词汇层最后处理，细目查 [references/patterns.md](references/patterns.md)

## 写之前先备材料

- 写长稿前在内部列出至少五件具体材料，动作、数字、时间、地点、原话、失败、代价和后来结果优先

- 每件材料要能说出来路，用户给的、可核验的公开来源、用户亲历都算，说不出来路的精确细节是假细节

- 假细节越具体，AI 味越重，没有来源的精确时间、神态、天气、摆设和对白不要写进非虚构稿

- 材料不够时只有三条路，先查公开材料，依赖用户亲历时一次问完最多三个问题，或者缩小题目写短答

- 找不到说话位置就先别写，先回答谁在说、他凭什么知道、哪一点他判断明确、哪一块他还拿不准

- 虚构创作按人物目标、动作和变化托住场景，细节跟着人物视角走，不给虚构细节伪造现实来源

## 按顺序改稿

- 第一遍只看推进，每段必须带一件新东西，新事实、新动作、新例子、新区别或新后果，换个说法重复上一段的不算推进

- 第二遍拆表演，假深刻、假具体、假口语、抽象名词抒情和比喻换场逐处拆掉，保护已经写活的段落

- 第三遍顺中文，主语和动作先出现，再接时间、原因和例子，动作已经把感情写出来时停住，不追在后面解释

- 第四遍清硬禁令，命中即改，清单在下一节

- 第五遍核事实，数字、日期、引文和确定程度与原稿逐项对齐，原稿的可能不要改成确定

- 最后一遍查结尾，删掉最后一段试读，正文没处理过的尺度不许只在结尾出现，写到事情讲完就停

- 长稿改完跑 `scripts/check_deai.py` 扫一遍硬禁令，脚本只报告不改稿，清零才交

## 硬禁令

- 不写翻案腔，先立一个没人主张的误解再推翻它给下文抬价，判断直接从正面下

- 不写三项以上的同构排比，两项为限，第三项换说法或删掉

- 不给抽象名词配具体动词抒情，不把动词名词化，完成了对流程的优化要写成把流程改顺了

- 不用破折号串联一切，不用提示性冒号引出结论，一句话总结和核心是这类写法直接删

- 不用洞察路标词领句，值得注意的是、真正的问题、更深一层、从某种意义上说都算

- 不用商业黑话和空大词抬价，赋能、闭环、重塑、开启新篇章出现时落回谁做了什么、花了多少、结果如何

- 不用借喻包装抽象概念，仓库、钥匙、底座、浪潮这类比喻不拿来装抽象名词，真写这些东西时除外

- 开头不用在当今什么时代铺垫，结尾不用让我们一起号召，不在末段把全文重新摘要一遍

## 短帖模式

- 帖子在一百到三百字时跳过长稿全流程，只跑六查，一分钟内完成

- 第一查具体细节，全帖有没有一个数字、时间、原话或动作，没有就补一件或改发事实帖

- 第二查翻案句，命中就直说后半句

- 第三查结尾，最后一句是升华、格言或号召就删掉，停在最后一个具体事实上

- 第四查黑话，赋能、闭环、重塑这类词换成谁做了什么

- 第五查同构，三句以上同句式连排拆掉至少一句的骨架

- 第六查朗读，全帖出声读一遍，一口说不完的句子拆开，不像本人平时说话的词换掉

- 短帖不跑量化指标，句长变异系数和词汇多样性在几句话的样本上没有统计意义，硬凑长短句只会显得刻意

- 短帖可以贴两三条本人过去的真人短帖作样本校准声线，比套长篇作者声音档案准

## 交付边界

- 去味的目标是给人读，不是过检测器，任何一派方法都不保证过检测，不要对用户许诺检测分数

- 改稿守事实锁，原文的事实、数字、日期、引文、链接和结论不动，需要补的事实先问或先查，不编

- 只处理成簇出现的痕迹，单个词或单个句式偶尔出现不算 AI 证据，看密度不看单点

- 同义词替换是最弱的去味，检测实测里换词不动分数，句式和段落节奏一起重组才有效

- 交稿时说明改了哪几层，材料层动过要说清补了什么材料，事实层拿不准的地方单独标出

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [blader/humanizer](https://github.com/blader/humanizer) for the original 26 pattern checklist built on the Wikipedia guide to signs of AI writing, strongest five tells first.

- [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) for the material first method, speaking position checks and the revision rules this skill compresses.

- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) for the most widely used Chinese adaptation, fact preservation and certainty preservation checks.

- [larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) for the paired corpus measurements behind the rhythm rules, sentence length variation and lexical diversity findings.
