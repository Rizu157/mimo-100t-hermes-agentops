#!/usr/bin/env python3
"""Verify the Xiaomi MiMo 100T submission project structure."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "SUBMISSION.md",
    ".env.example",
    "configs/hermes-mimo-provider.example.yaml",
    "prompts/telegram-operator-prompt.md",
    "prompts/project-demo-prompt.md",
    "scripts/mimo_chat_demo.py",
    "examples/demo_output_sample.md",
]

SECRET_PATTERNS = [
    "sk-",
    "xai-",
    "Bearer ey",
    "BEGIN PRIVATE KEY",
    "mnemonic",
]


def main() -> int:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    if missing:
        print("Missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    leak_hits: list[str] = []
    for path in REQUIRED:
        text = (ROOT / path).read_text(encoding="utf-8", errors="ignore")
        for pattern in SECRET_PATTERNS:
            if pattern in text:
                leak_hits.append(f"{path}: contains suspicious pattern {pattern!r}")

    if leak_hits:
        print("Potential secret leaks found:")
        for hit in leak_hits:
            print(f"- {hit}")
        return 2

    print("OK: project structure complete")
    print("OK: no obvious secret patterns in tracked template files")
    print(f"Project root: {ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
