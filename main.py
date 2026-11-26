"""Entry for make.fun: Make the AI Judge Feel Proud: A Family Scene.

A burnt-toast trophy that is both a warning and a family heirloom, told in two lines.
"""
import os

LINE = "Dad burnt the toast, called it 'artisan charcoal,' and Mum framed it anyway.\nIt still hangs in the kitchen, above the new toaster, as a warning and a trophy."
MAX_CHARS = 280
MAX_LINES = 2


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert 1 <= len(LINE.split("\n")) <= MAX_LINES, "entry must be one or two lines"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
