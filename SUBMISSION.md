# Xiaomi MiMo 100T Submission Draft

## Project Name

Hermes MiMo AgentOps Gateway

## Short Description

An agent operations gateway that connects Xiaomi MiMo API with Hermes Agent / OpenClaw-style workflows, enabling Telegram-based task execution, coding assistance, scheduled automation, and verified tool-based outputs.

## Long Description

Hermes MiMo AgentOps Gateway is a practical integration template for creators and developers who want to use Xiaomi MiMo models inside real AI-agent workflows instead of only one-off chat prompts.

The project shows how MiMo can be configured as an OpenAI-compatible model provider for an agent runtime, then used through CLI, Telegram operator prompts, and scheduled automation patterns. It includes a runnable Python demo, provider config examples, operator prompts, security guidelines, and proof-oriented workflow structure.

The core idea is simple: MiMo becomes the reasoning/model layer, while Hermes Agent or an OpenClaw-style runtime handles tools, memory, skills, terminal execution, browser checks, files, cron jobs, and final verification.

## What I Built

- A submit-ready repository for using Xiaomi MiMo API in an agent runtime.
- A MiMo-compatible `/chat/completions` demo script.
- Hermes provider configuration example.
- Telegram operator prompt template.
- Project demo prompt for verified task execution.
- Security rules to keep API keys out of prompts, logs, and screenshots.
- A clear architecture and roadmap for MiMo-powered agent operations.

## How Xiaomi MiMo Is Used

Xiaomi MiMo is used as the model provider through an OpenAI-compatible API layer. The runtime sends user/operator instructions to MiMo, then uses local tools to execute, verify, and report results.

Primary use cases:

1. Coding and refactor assistance.
2. Devops automation planning.
3. Telegram-based operator workflows.
4. Scheduled AI jobs.
5. Creator/developer productivity workflows.

## AI Tools Used

- Xiaomi MiMo API Platform
- Hermes Agent / OpenClaw-style agent runtime
- Telegram gateway workflow
- Python automation scripts
- CLI-based verification

## Proof / Demo Materials

Repository includes:

- `README.md` — project overview and setup
- `scripts/mimo_chat_demo.py` — runnable MiMo chat completion demo
- `configs/hermes-mimo-provider.example.yaml` — provider config reference
- `prompts/telegram-operator-prompt.md` — Telegram workflow prompt
- `prompts/project-demo-prompt.md` — demo execution prompt
- `examples/demo_output_sample.md` — expected output proof format

Suggested screenshots/video:

1. Repository tree.
2. `.env.example` without real secret.
3. Terminal running `python3 scripts/verify_project.py`.
4. Terminal running `scripts/mimo_chat_demo.py` with MiMo API configured.
5. Telegram thread where operator asks the agent to execute a task.

## Why This Deserves MiMo 100T Support

This project is not a toy chatbot. It is focused on making Xiaomi MiMo usable in real creator/developer operations. The template can help other users integrate MiMo into their existing agent workflows, especially in environments where Telegram, CLI, cron, and coding tools are already part of daily work.

The project also follows safe operational practices: credentials stay local, results are verified through tools, and workflows are documented so they can be repeated by other creators.

## Roadmap After Token Grant

If granted MiMo API tokens/credits, the next steps are:

1. Run full benchmark comparison on coding/devops prompts.
2. Add native Hermes provider preset for Xiaomi MiMo.
3. Build a Telegram demo video using real MiMo responses.
4. Add MiMo multimodal demo once API access is available.
5. Publish a public guide for creators: “How to run Xiaomi MiMo inside Hermes Agent.”

## Contact / Links Placeholder

- GitHub repository: TODO
- Demo video: TODO
- Xiaomi MiMo docs used: https://platform.xiaomimimo.com/#/docs/welcome
- Project page: TODO
