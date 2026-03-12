#!/usr/bin/env python3
"""
交互式 MD → JSON 字符串转换

运行后循环：粘贴 MD → 输入 --- 回车 → 输出 JSON → 继续
输入 q 或 exit 回车退出
"""
import json
import sys

SENTINEL = "---"   # 输入此行表示「转换」
QUIT_CMDS = ("q", "exit", "quit")


def main():
    print("MD → JSON 字符串转换（交互模式）", file=sys.stderr)
    print("粘贴 MD 内容，输入 --- 回车 输出 JSON；输入 q 回车 退出", file=sys.stderr)
    print("-" * 50, file=sys.stderr)

    while True:
        lines = []
        try:
            while True:
                line = sys.stdin.readline()
                if not line:
                    return
                line = line.rstrip("\n\r")
                if line.strip().lower() in QUIT_CMDS:
                    return
                if line.strip() == SENTINEL:
                    break
                lines.append(line)
        except (KeyboardInterrupt, EOFError):
            return

        if not lines:
            continue

        text = "\n".join(lines)
        escaped = json.dumps(text, ensure_ascii=False)
        print(escaped)
        print("\n" + "=" * 60 + "\n", file=sys.stderr)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
