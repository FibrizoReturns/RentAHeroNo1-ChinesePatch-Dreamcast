#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compare_track03.py — 两个 track03.bin 的逐字节差异定位工具

用途：拿到别的汉化版（如韩文版）补丁后，和本版（或日文原版）比对，
      看清谁改了哪些区域、改了多大，用来判断"某一页/某一块"对方有没有动。

用法：
    python compare_track03.py A.bin B.bin [--min-gap 64] [--top 40] [--dump 报告.txt]

输出：
    1) 两文件大小与 MD5
    2) 差异区间（按偏移聚簇，间隔小于 --min-gap 字节的差异合并成一个区间）
    3) 每个区间：起始/结束偏移、长度、差异字节数、差异率
    4) 可选 --dump 把完整报告写成文本

只看结论，不做任何写入——本工具绝不改文件。
"""

import sys
import hashlib
import argparse


def md5_of(path, chunk=1 << 20):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest().upper()


def load(path):
    with open(path, "rb") as f:
        return f.read()


def precise(a, b, n, min_gap, step):
    clusters = []
    cur_start = None
    cur_end = None
    cur_cnt = 0
    i = 0
    while i < n:
        end = min(i + step, n)
        if a[i:end] == b[i:end]:
            # 相同块：若当前簇存在且间隔过大，则收尾
            if cur_start is not None and i - cur_end >= min_gap:
                clusters.append((cur_start, cur_end, cur_cnt))
                cur_start = None
                cur_end = None
                cur_cnt = 0
            i = end
            continue
        for j in range(i, end):
            if a[j] != b[j]:
                if cur_start is None:
                    cur_start = j
                cur_end = j + 1
                cur_cnt += 1
        i = end
    if cur_start is not None:
        clusters.append((cur_start, cur_end, cur_cnt))
    return clusters


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--min-gap", type=int, default=64,
                    help="两处差异间隔小于该值则合并为一个区间（默认 64）")
    ap.add_argument("--top", type=int, default=40,
                    help="只打印差异字节数最多的前 N 个区间，0=全部")
    ap.add_argument("--dump", default=None, help="完整报告写入该文本文件")
    args = ap.parse_args()

    a = load(args.a)
    b = load(args.b)
    lines = []
    p = lines.append

    p("=" * 78)
    p("A: %s" % args.a)
    p("    size=%d  md5=%s" % (len(a), md5_of(args.a)))
    p("B: %s" % args.b)
    p("    size=%d  md5=%s" % (len(b), md5_of(args.b)))
    if len(a) != len(b):
        p("!! 大小不同，仅比对前 %d 字节" % min(len(a), len(b)))
    p("=" * 78)

    if a == b:
        p("两个文件完全相同。")
        emit(lines, args.dump)
        return

    clusters = precise(a, b, min(len(a), len(b)), args.min_gap, 64)
    total_diff = sum(c[2] for c in clusters)
    p("差异区间数=%d  差异字节合计=%d  占比较小文件 %.2f%%"
      % (len(clusters), total_diff, 100.0 * total_diff / max(1, min(len(a), len(b)))))
    p("-" * 78)
    p("%-10s %-10s %-9s %-9s %6s" % ("start", "end", "len", "diff", "rate"))
    show = clusters
    if args.top and args.top > 0:
        show = sorted(clusters, key=lambda c: -c[2])[:args.top]
        p("（按差异字节数排序，只列前 %d 个）" % args.top)
    for (s, e, cnt) in show:
        p("%08X   %08X   %-9d %-9d %5.1f%%"
          % (s, e, e - s, cnt, 100.0 * cnt / max(1, e - s)))
    emit(lines, args.dump)


def emit(lines, dump):
    text = "\n".join(lines)
    print(text)
    if dump:
        with open(dump, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print("\n报告已写入 %s" % dump)


if __name__ == "__main__":
    main()
