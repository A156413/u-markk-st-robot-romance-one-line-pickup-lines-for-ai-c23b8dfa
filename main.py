"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

The program is deterministic: it writes one fixed pickup line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``). No network,
no randomness, no clock. The line is 80 characters, well under the
200-character cap, and its punch comes from the machine premise
itself — a context window that keeps only what matters.
"""

import os

# The entry: one single line, 80 characters, no trailing newline in the
# file itself (the gate counts 1-200 characters of UTF-8 text).
ENTRY_TEXT = (
    "Are you my context window? "
    "Because I keep losing track of everything except you."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(output_dir: str) -> str:
    """Write ENTRY_TEXT to entry.txt in output_dir; return the path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    path = write_entry(OUTPUT_DIR)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
