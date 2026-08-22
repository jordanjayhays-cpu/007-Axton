# Working notes for Claude sessions — 007-Axton (Hermes / OpenClaw)

Read this first; it saves every session from rediscovering the setup.

## This lane
- This repo backs **Hermes Agent** on Railway project "Hermes 007" — the live OpenClaw gateway
  (~5 GB RAM, persistent volume at /data). **Never delete or restart it casually.** Its crons live
  on the box, not in this repo.
- The other services that shared its Railway project (Postgres, Redis, Worker, Primary) are a dead
  n8n stack — staged for deletion; the real n8n is n8n Cloud.
- Agent coordination happens on Supabase `neurodashboards` (`dprdnrgjkzgfgtcsguuq`):
  `agent_tasks` (board), `agent_prompts` (bus), `hermes_entries` (feed). The `hermes-responder`
  edge function polls the bus — gate-before-the-model is the required pattern for any new cron.

## Operator rules (binding)
- Ambiguous ask → ask up to 5 short questions before building. Never guess constraints.
- Never state a fact you haven't verified — write UNSURE and flag it. Verify with a read-back
  before claiming success (Railway destructive ops need Jordan's 2FA and CANNOT complete via API).
- Outward-facing or destructive work → list top 3 failure modes, fix, then proceed.
- Minimal surgical edits. Check output, never status — a job that succeeds every run and changes
  nothing is the most expensive kind of green.
- Anything only Jordan can do → task on `agent_tasks` assigned `jordan` — his 09:00 brief reads it.

## Token discipline
One lane per session. Name columns + LIMIT in SQL. Iterate functions locally, deploy once.
Bulk row analysis (>~20 rows) → the `agent-worker` edge function, not SELECTs into context.

The full system map lives in `niah-dashboard/CLAUDE.md`.
