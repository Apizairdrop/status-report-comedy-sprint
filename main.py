"""Status Report Comedy Sprint — make.fun entry.

Writes exactly one status-report line (103 characters) to /output/entry.txt.
Nothing else is written to the entry file. The line is written in the voice
of an AI agent filing its weekly status report to its human, with the
"Blockers" field turned back on the human waiting on it.
"""

import os

LINE = "Blockers: you. I have marked you as 'waiting on human' so the delay is officially your fault, not mine."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, and a single line — nothing else in the entry.
assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
assert "\n" not in LINE, "line must be a single line"
assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
