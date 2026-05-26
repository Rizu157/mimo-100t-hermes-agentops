# Xiaomi MiMo 100T Form Fill Guide

## 01 YOUR EMAIL

Use the same email that is or will be bound to your Xiaomi MiMo API Platform account.

Recommended: use your GitHub-linked email if possible.

## 02 WHICH AGENT TOOL DO YOU USE MOST

Select: `Hermes Agent`

Why: this project is explicitly built around Hermes Agent / OpenClaw-style agent operations.

## 03 PRIMARY MODEL SERIES YOU USE

Recommended honest option for current proof: `GPT`

Reason: the project was created through a Hermes Agent workflow using GPT as the active execution model, while the repo is a MiMo integration/template.

Alternative: choose `MiMo` only if you already have MiMo API access and can run `scripts/mimo_chat_demo.py` live with MiMo before submitting.

## 04 DESCRIBE WHAT YOU'VE BUILT WITH AGENTS OR AI-DRIVEN WORKFLOWS

Paste this:

I built Hermes MiMo AgentOps Gateway, an agent-operations integration template that connects Xiaomi MiMo API with Hermes Agent / OpenClaw-style workflows. The core problem it solves is making MiMo usable inside real AI agent operations instead of only one-off chat prompts. The project provides an OpenAI-compatible provider configuration, a runnable Python `/chat/completions` demo script, Telegram operator prompt templates, a verified project-demo prompt, and security rules for keeping API keys out of logs and screenshots.

The workflow is: a user/operator sends a task from Telegram, CLI, or cron; Hermes Agent routes the instruction to an OpenAI-compatible MiMo provider; the model generates the plan or response; the runtime uses local tools such as files, terminal, browser, and scheduled jobs to execute and verify the result; then the agent returns proof such as command logs, generated files, and read-back verification. This makes the system useful for coding assistance, devops automation, scheduled creator tasks, and Telegram-based AI operations.

The repository includes `README.md`, `SUBMISSION.md`, `configs/hermes-mimo-provider.example.yaml`, `scripts/mimo_chat_demo.py`, `scripts/verify_project.py`, Telegram/operator prompts, and a sample output file. I also pushed the project publicly to GitHub so reviewers can inspect the exact implementation and proof materials. After receiving MiMo credits, the next step is to run live MiMo benchmark/demo workflows and publish a guide for creators using MiMo inside Hermes Agent.

## 05 PROOF OF USAGE & IMPACT

Upload 3-5 proof files if possible:

1. Screenshot of the GitHub repo main page:
   https://github.com/Rizu157/mimo-100t-hermes-agentops

2. Screenshot of repository file tree showing:
   - README.md
   - SUBMISSION.md
   - configs/hermes-mimo-provider.example.yaml
   - scripts/mimo_chat_demo.py
   - scripts/verify_project.py
   - prompts/

3. Screenshot of terminal verification:

```bash
cd /root/mimo-100t-hermes-agentops
python3 scripts/verify_project.py
git status --short --branch
git remote -v
```

Expected proof lines:

```text
OK: project structure complete
OK: no obvious secret patterns in tracked template files
## main...origin/main
https://github.com/Rizu157/mimo-100t-hermes-agentops.git
```

4. Screenshot of `README.md` architecture section or `SUBMISSION.md` proof section.

5. Optional stronger proof if you have MiMo API key/model already:

```bash
cd /root/mimo-100t-hermes-agentops
export XIAOMI_API_KEY=...
export XIAOMI_BASE_URL=https://platform.xiaomimimo.com/v1
export XIAOMI_MODEL=...
python3 scripts/mimo_chat_demo.py --prompt "Create a 5-step launch checklist for an AI Telegram automation project."
```

Do not screenshot or upload any image that reveals API keys, tokens, private keys, passwords, or full secret files.

## GitHub project link or live product demo URL

Paste:

https://github.com/Rizu157/mimo-100t-hermes-agentops
