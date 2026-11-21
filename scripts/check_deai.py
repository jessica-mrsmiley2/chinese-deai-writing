#!/usr/bin/env python3
"""中文去味硬禁令扫描（自研，纯本地正则，无联网）。

用法: python3 check_deai.py <稿件文件>
只报告不改稿。命中硬禁令（翻案腔/提示性冒号/路标领句）退出码 1，其余 0。
句长 CV 仅在全文 >= 350 字时给出，短文本不计算（无统计意义）。
"""
import re
import statistics
import sys

HARD_PATTERNS = [
    ("翻案腔", re.compile(r"不是[^。！？\n]{1,30}而是|并非[^。！？\n]{1,30}而是|不只是[^。！？\n]{1,30}更是|与其说[^。！？\n]{1,30}不如说|你以为[^。！？\n]{0,30}其实")),
    ("翻案腔", re.compile(r"说到底|答案恰恰相反|不重要[，,]重要的是")),
    ("提示性冒号", re.compile(r"(一句话总结|核心是|答案是|残酷的现实是|本质上是)\s*[：:]")),
    ("路标领句", re.compile(r"(值得注意的是|需要指出的是|值得一提的是|不难发现|综上所述|总而言之|由此可见|从某种意义上说|更深一层|真正的问题是)")),
    ("时代铺垫", re.compile(r"在当今[^。！？\n]{0,20}时代|随着[^。！？\n]{0,20}的不断发展")),
    ("号召结尾", re.compile(r"让我们(一起)?[^。！？\n]{0,20}[吧！!]")),
]

SOFT_WORDS = [
    "赋能", "抓手", "闭环", "重塑", "颠覆", "开启新篇章", "里程碑",
    "说白了", "说穿了", "先说结论", "进行", "实现", "助力", "致力于",
    "研究表明", "专家指出", "数据显示", "对于", "基于", "围绕",
]
TRANSLATIONESE = re.compile(r"对于[^。！？\n]{1,20}来说|围绕[^。！？\n]{1,20}展开|使得[^。！？\n]{1,20}得以")


def split_sentences(text):
    parts = re.split(r"[。！？\n]+", text)
    return [p.strip() for p in parts if p.strip()]


def main():
    if len(sys.argv) != 2:
        print("用法: python3 check_deai.py <稿件文件>")
        return 2
    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read()

    hard_hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for name, pat in HARD_PATTERNS:
            for m in pat.finditer(line):
                hard_hits.append((lineno, name, m.group(0)))

    soft_hits = []
    for word in SOFT_WORDS:
        n = text.count(word)
        if n:
            soft_hits.append((word, n))
    trans_hits = TRANSLATIONESE.findall(text)

    sentences = split_sentences(text)
    # 三连同构: 三句相邻句子以相同两字开头
    iso = 0
    for i in range(len(sentences) - 2):
        heads = [s[:2] for s in sentences[i:i + 3] if len(s) >= 2]
        if len(heads) == 3 and len(set(heads)) == 1:
            iso += 1

    print(f"字数 {len(text)}，句子 {len(sentences)}")
    print(f"[硬禁令] {len(hard_hits)} 处")
    for lineno, name, frag in hard_hits:
        print(f"  L{lineno} {name}: {frag}")
    print(f"[软词/黑话] {sum(n for _, n in soft_hits)} 处: " +
          ", ".join(f"{w}x{n}" for w, n in soft_hits))
    print(f"[翻译腔结构] {len(trans_hits)} 处")
    print(f"[三连同构] {iso} 组")
    dash = text.count("——") + text.count("—")
    print(f"[破折号] {dash} 处（分模型看待，仅提示）")

    if len(text) >= 350 and len(sentences) >= 8:
        lengths = [len(s) for s in sentences]
        mean = statistics.mean(lengths)
        cv = statistics.pstdev(lengths) / mean if mean else 0
        print(f"[句长CV] {cv:.2f}（长稿参考，人类配对中位约 0.54，明显低于 0.50 警惕节奏太匀）")
    else:
        print("[句长CV] 跳过（短文本无统计意义）")

    return 1 if hard_hits else 0


if __name__ == "__main__":
    sys.exit(main())
