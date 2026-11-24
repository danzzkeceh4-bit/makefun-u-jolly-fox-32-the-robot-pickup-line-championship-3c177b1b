#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun entry.

Writes a single-line pickup line a robot would use to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

LINE = (
    "Are you a firmware update? Because every time you're near, "
    "I reboot a little - and somehow I keep coming back better."
)


def main() -> int:
    text = LINE
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    assert 1 <= len(back) <= 200, f"read-back length {len(back)} out of range"
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
