# Demo Output Sample

Command:

```bash
python3 scripts/mimo_chat_demo.py --prompt "Create a 5-step launch checklist for an AI Telegram automation project."
```

Expected response style:

```text
1. Confirm provider configuration and API key are loaded from environment variables.
2. Verify Telegram gateway connectivity and allowed chat/thread settings.
3. Run a small model smoke test before enabling long-running workflows.
4. Execute one file-writing task and verify the output with a read-back check.
5. Monitor logs, keep rollback steps ready, and avoid printing secrets in status reports.
```

Verification command:

```bash
python3 scripts/verify_project.py
```

Expected verification:

```text
OK: project structure complete
OK: no obvious secret patterns in tracked template files
Project root: /path/to/mimo-100t-hermes-agentops
```
