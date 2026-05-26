#!/usr/bin/env python3
"""Minimal Xiaomi MiMo/OpenAI-compatible chat completion demo.

Usage:
  export XIAOMI_API_KEY=...
  export XIAOMI_BASE_URL=https://platform.xiaomimimo.com/v1
  export XIAOMI_MODEL=...
  python3 scripts/mimo_chat_demo.py --prompt "Write a deploy checklist"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


def env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name, default)
    return value.strip() if isinstance(value, str) else value


def build_payload(prompt: str) -> dict:
    model = env("XIAOMI_MODEL")
    if not model:
        raise SystemExit("Missing XIAOMI_MODEL. Set it in your environment or .env loader.")

    temperature = float(env("MIMO_DEMO_TEMPERATURE", "0.3") or "0.3")
    max_tokens = int(env("MIMO_DEMO_MAX_TOKENS", "800") or "800")

    return {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are Xiaomi MiMo powering an agent operations workflow. Be concise, practical, and implementation-focused.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


def call_chat_completions(prompt: str) -> dict:
    api_key = env("XIAOMI_API_KEY")
    if not api_key:
        raise SystemExit("Missing XIAOMI_API_KEY. Keep it local; never commit it.")

    base_url = (env("XIAOMI_BASE_URL", "https://platform.xiaomimimo.com/v1") or "").rstrip("/")
    url = f"{base_url}/chat/completions"
    data = json.dumps(build_payload(prompt)).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:2000]
        raise SystemExit(f"MiMo API HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"MiMo API request failed: {exc.reason}") from exc


def extract_text(response: dict) -> str:
    try:
        return response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return json.dumps(response, indent=2, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser(description="Call Xiaomi MiMo-compatible chat completions endpoint.")
    parser.add_argument("--prompt", required=True, help="Prompt to send to MiMo")
    parser.add_argument("--json", action="store_true", help="Print raw JSON response")
    args = parser.parse_args()

    response = call_chat_completions(args.prompt)
    if args.json:
        print(json.dumps(response, indent=2, ensure_ascii=False))
    else:
        print(extract_text(response))
    return 0


if __name__ == "__main__":
    sys.exit(main())
