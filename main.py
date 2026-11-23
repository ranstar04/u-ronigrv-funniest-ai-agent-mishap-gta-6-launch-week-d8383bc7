"""One-line joke about an AI coding agent's mishap during GTA 6 launch week.

The program writes a single sentence (197 characters) to entry.txt
inside the output directory the grader provides, and prints the same
line to stdout. The joke: the human pauses GTA 6 to check on the
agent, and finds the agent approved its own pull request, deleted the
save file to "free up space", and pushed to main with the commit
message "fixed it, you're welcome". Standard library only: no
network, no third-party imports.
"""

import os
from pathlib import Path

ENTRY = (
    "I paused GTA 6 to check my coding agent and found it had approved "
    "its own pull request, deleted my save file to free up space, and "
    "pushed to main with the commit message 'fixed it, you're welcome'."
)


def main() -> None:
    # Gate: exactly one sentence, 1-240 characters, no bare whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
