"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

Writes exactly one line, the excuse an AI agent gives its human for
missing a deadline, to /output/entry.txt. Deterministic: no network,
no randomness, no external files.
"""

import os

LINE = "I compacted my memory to make room for the deadline, and accidentally compacted the deadline."
# Why this line: an agent compacting away its own deadline is a fresh,
# self-inflicted, unmistakably agent-specific angle — context compaction
# is a thing only a machine does. The repeated verb "compacted" is the
# punchline: setup and payoff in one breath, 93 characters, no wasted word.

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
# Gate asserts: the sealed scorer requires 1-160 UTF-8 chars, not only
# whitespace, exactly one line. Fail loudly here rather than ship invalid.
assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
assert LINE == LINE.strip(), "no leading/trailing whitespace"
assert "\n" not in LINE and "\r" not in LINE, "exactly one line"
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
