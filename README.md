# Hermes MiMo AgentOps Gateway

> Submission project for Xiaomi MiMo Orbit 100T Token Creator Incentive.

## One-line Pitch

Hermes MiMo AgentOps Gateway is an OpenAI-compatible agent operations template that lets creators plug Xiaomi MiMo API into Hermes Agent, Telegram operator workflows, scheduled automation, and coding/devops task execution.

## Problem

Power users already run AI agents across Telegram, CLI, cron jobs, coding tools, and automation scripts. The hard part is not just calling a model endpoint; it is operating the model safely inside repeatable workflows:

- route tasks from chat/CLI to the right model provider,
- keep API keys out of prompts and logs,
- verify outputs with tools,
- run scheduled jobs and long-running operations,
- preserve reusable skills and memory across sessions,
- produce proof that the AI actually executed the task.

## Solution

This project provides a ready-to-use MiMo integration layer and demo workflow for Hermes Agent / OpenClaw-style operators:

1. Configure Xiaomi MiMo as an OpenAI-compatible provider.
2. Run a local CLI demo that sends tasks to MiMo-compatible chat completions.
3. Use a Telegram/operator prompt template for real task execution.
4. Capture evidence: logs, generated output, and submission-ready description.

## Why Xiaomi MiMo

Xiaomi MiMo V2.5 exposes model capabilities for text, multimodal, and voice scenarios through an API platform. This project uses MiMo as the execution brain behind agentic workflows, especially for:

- software engineering assistance,
- automation planning,
- operational reporting,
- Telegram-based AI operator workflows,
- scheduled creator/developer tasks.

## Architecture

```text
User / Operator
   |
   | Telegram, CLI, Cron, Webhook
   v
Hermes Agent / OpenClaw-style Runtime
   |
   | OpenAI-compatible provider config
   v
Xiaomi MiMo API Platform
   |
   | model response
   v
Tools + Verification Layer
   |
   | file, terminal, browser, web, cron
   v
Result + Evidence
```

## Repository Layout

```text
.
├── README.md
├── SUBMISSION.md
├── .env.example
├── configs/
│   └── hermes-mimo-provider.example.yaml
├── prompts/
│   ├── telegram-operator-prompt.md
│   └── project-demo-prompt.md
├── scripts/
│   ├── mimo_chat_demo.py
│   └── verify_project.py
└── examples/
    └── demo_output_sample.md
```

## Quick Start

### 1. Prepare credentials

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Then fill only local secrets:

```bash
XIAOMI_API_KEY=your_api_key_here
XIAOMI_BASE_URL=https://platform.xiaomimimo.com/v1
XIAOMI_MODEL=your_mimo_model_id
```

Do not commit `.env`.

### 2. Run local MiMo-compatible demo

```bash
python3 scripts/mimo_chat_demo.py \
  --prompt "Create a 5-step launch checklist for an AI Telegram automation project."
```

The script reads credentials from environment variables and calls a MiMo/OpenAI-compatible `/chat/completions` endpoint.

### 3. Configure Hermes Agent provider

Use `configs/hermes-mimo-provider.example.yaml` as a reference and map it into your Hermes `~/.hermes/config.yaml`.

Example shape:

```yaml
model:
  provider: custom
  default: ${XIAOMI_MODEL}
  base_url: ${XIAOMI_BASE_URL}
  api_key: ${XIAOMI_API_KEY}
```

Secrets must live in `.env`, not in the project README or prompt files.

### 4. Demo workflow

Use `prompts/project-demo-prompt.md` inside Hermes Agent or OpenClaw:

```text
Use Xiaomi MiMo provider to generate a devops automation plan, create a checklist file, then verify the file exists and summarize the result.
```

Expected evidence:

- terminal command log,
- generated checklist file,
- final response with verification status.

## Target Users

- AI creators submitting to MiMo 100T,
- developers using coding agents,
- Telegram/Discord community operators,
- teams needing low-friction AI automation,
- Web3/devops operators who need verified agent execution.

## Evaluation Criteria Mapping

- **AI tool usage:** Hermes Agent, Telegram gateway, CLI scripts, cron-capable workflows.
- **Model usage:** Xiaomi MiMo API as OpenAI-compatible provider.
- **Project specificity:** agent operations gateway with concrete config, scripts, prompts, and evidence.
- **Proof material:** runnable demo script, provider config, architecture, sample output.
- **Creator value:** helps other users adopt MiMo in real agent workflows.

## Roadmap

- Add native Hermes provider preset for Xiaomi MiMo.
- Add streaming response support test matrix.
- Add Telegram screenshot/video walkthrough.
- Add multi-model routing examples.
- Add MiMo multimodal and voice demo when API access is available.

## Security

- Never store API keys in git.
- `.env` is ignored by default.
- Demo script masks key presence and never prints the key.
- Submission docs reference secret paths and env variable names only.

## License

MIT for project template and examples.
