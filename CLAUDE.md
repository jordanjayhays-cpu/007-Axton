# Working notes for Claude sessions — 007-Axton (Hermes / OpenClaw)

Read this first; it saves every session from rediscovering the setup.

## This lane — DECOMMISSIONED 2026-08-22
- **Hermes is being retired.** Jordan's call, verbatim intent: it was draining money and he now
  runs everything through Claude. Status:
  - `hermes-responder-5min` pg_cron: **unscheduled** (function still deployed if ever needed).
  - Railway "Hermes 007" → Hermes Agent: **scale-to-0 staged**, awaiting Jordan's 2FA Apply in the
    Railway dashboard (same batch as the 4 dead n8n service deletions). Until he clicks Apply it is
    STILL RUNNING AND BILLING — never report it stopped without a metrics read-back.
  - The `/data` volume (75cbabea) and service config are preserved for a possible future revival.
  - Revival = Apply replicas back to 1 + re-schedule the pg_cron.
- Do not create new Hermes tasks, prompts, or crons. The `agent_prompts` bus rows for hermes will
  sit unclaimed — that is expected now.
- Agent coordination continues on Supabase `neurodashboards` (`dprdnrgjkzgfgtcsguuq`) with Claude
  as the single orchestrator.

## Operator rules (binding)
- Ambiguous ask → ask up to 5 short questions before building. Never guess constraints.
- Never state a fact you haven't verified — write UNSURE and flag it. Verify with a read-back
  before claiming success (Railway destructive ops need Jordan's 2FA and CANNOT complete via API).
- Outward-facing or destructive work → list top 3 failure modes, fix, then proceed.
- Minimal surgical edits. Check output, never status — a job that succeeds every run and changes
  nothing is the most expensive kind of green.
- Anything only Jordan can do → task on `agent_tasks` assigned `jordan` — his 09:00 brief reads it.

## Token discipline
One lane per session. Name columns + LIMIT in SQL. Bulk row analysis (>~20 rows) → the
`agent-worker` edge function, not SELECTs into context.

**The master map lives in `mission-control/CLAUDE.md`.**
