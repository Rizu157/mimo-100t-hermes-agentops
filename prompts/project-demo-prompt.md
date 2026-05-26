# Project Demo Prompt

Use Xiaomi MiMo as the model provider for this agent workflow.

## Goal

Demonstrate that MiMo can power a practical AI operations workflow, not only a single chat completion.

## Task

1. Generate a concise devops checklist for deploying a Telegram-based AI agent.
2. Save it to `output/mimo_agentops_checklist.md`.
3. Verify that the file exists.
4. Read the file back.
5. Report the result with proof.

## Acceptance Criteria

- The checklist has exactly 7 numbered steps.
- It includes secret handling, gateway health check, model provider config, and rollback plan.
- The final response includes file path and verification status.
