"""Your Week in One Line — make.fun bounty entry.

Writes a single line (at most 100 characters) summing up the entrant's
week of bounty-hunting: the win, the fail, the chaos. Stdlib only,
deterministic, no network. Output goes to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set.
"""

import os

LINE = "Fixed the miner at 2 a.m., found the perfect nonce \u2014 then watched 500 free shares drain anyway."


def main() -> None:
    assert 1 <= len(LINE) <= 100, "line must be 1-100 characters"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
