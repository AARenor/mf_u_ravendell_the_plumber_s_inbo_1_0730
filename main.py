#!/usr/bin/env python3
"""Write the one-line make.fun entry to the requested output directory."""

import os
import sys
from pathlib import Path

ENTRY_TEXT = (
    "Subject: No software\n"
    "You don't need another app. You're up at six, out on a leak, and keying "
    "invoices at ten. I'll match bank lines to jobs, file receipts, list who "
    "owes you. £190/month. Don't send the whole file; send the unpaid jobs "
    "first. Nick"
)


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 280
    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output"))
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY_TEXT.encode("utf-8"))
    print(len(ENTRY_TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
