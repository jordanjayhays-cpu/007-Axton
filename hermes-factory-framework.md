# Hermes Agent Factory: Comprehensive Self-Improvement Framework

> **Owner:** Jordan  
> **Agent:** Hermes  
> **Version:** 1.0 — May 2026  
> **Purpose:** Build a closed-loop factory system so Hermes autonomously gets better every session.

---

## The Big Picture

```
Session N ──► Reflection ──► Skill Authoring ──► Memory Compaction ──► Session N+1
                  │                   │                    │
                  ▼                   ▼                    ▼
              Critique on         Extract from          Synthesize into
              recent work         success              persistent memory
                  │                   │                    │
                  ▼                   ▼                    ▼
           Self-grading &        New/updated         Hermes knows more
           prompt optimization   skill file           each time
```

**The Factory has six interlocking subsystems:**
1. Self-Reflection Loop
2. Memory Compounding
3. Skill Factory
4. Prompt Optimization
5. Error Recovery
6. Multi-Agent Learning

Each is designed to feed the others, creating compounding growth.

---

## 1. Self-Reflection Loop

### What It Is
After each significant task, Hermes pauses to critically evaluate: What did I do well? What failed? What should I change?

### Trigger Conditions
Run a reflection cycle when:
- A task completes with 5+ tool calls
- User provides explicit correction or negative feedback
- An error was encountered and recovered
- A new workflow was improvised that wasn't in any skill

### The Reflection Prompt Template
```markdown
## Self-Reflection: [Task Name]

### What happened:
[Brief description of the session's key events]

### What worked:
[Specific things that went well — include the exact approach/command used]

### What failed or could be improved:
[Specific failures, inefficiencies, or gaps — be concrete]

### Root cause analysis:
[Why did the failure happen? Misunderstanding? Missing knowledge? Wrong tool?]

### What I will do differently next time:
[Actionable changes for next session — name specific files, commands, approaches]

### Is this worth writing into a skill?
[Yes/No — if Yes, trigger Skill Factory below]
```

### Self-Grading Rubric
Score each session on a 1–5 scale across these dimensions:

| Dimension | 1 (Poor) | 3 (OK) | 5 (Excellent) |
|---|---|---|---|
| **Accuracy** | Wrong facts, wrong approach | Mostly correct | Precise, verified |
| **Efficiency** | Wasted steps, circular | Reasonable | Minimal tool calls |
| **Context** | Missed key context | Used available context | Found subtle context |
| **Recovery** | Gave up or made worse | Fixed eventually | Smooth self-correction |
| **User satisfaction** | User corrected me | User accepted | User impressed |

**If average < 3.5 → trigger Prompt Optimization.**  
**If any dimension = 1 → trigger Error Recovery logging.**

---

## 2. Memory Compounding

### The Karpathy LLM Wiki Pattern (adapted for Hermes)

Hermes's memory should function like a **compiling knowledge system**, not a search index.

### Three-Layer Architecture

```
Layer 1: RAW SOURCES (append-only, immutable)
─────────────────────────────────────────────
~/.hermes/memory/raw/
  session-YYYY-MM-DD-N.json    ← raw session log
  user-feedback-YYYY-MM-DD.md  ← explicit corrections
  error-log.md                  ← all errors encountered

Layer 2: SYNTHESIZED WIKI (LLM-compiled, interlinked)
────────────────────────────────────────────────────
~/.hermes/memory/wiki/
  MEMORY.md        ← always-on context (3,575 char limit)
  USER.md          ← user model (preferences, patterns)
  SKILLS_INDEX.md  ← master index of all skill files
  CONCEPTS/        ← topic pages (e.g., "docker-networking.md")
  PROJECTS/        ← project-specific pages

Layer 3: SCHEMA + OPERATING RULES
─────────────────────────────────
~/.hermes/SOUL.md             ← personality + values
~/.hermes/CONTEXT.md          ← project-specific context
~/.hermes/SCHEMA.md           ← conventions + taxonomy
```

### Memory Compaction Trigger

Run compaction when:
- Session exceeds 4,000 tokens
- `MEMORY.md` approaches 3,575 char limit
- Task completes with major decisions

### Compaction Workflow
1. Summarize the session → 200–400 word abstract
2. Extract key facts → add to relevant wiki pages
3. Extract user preferences → update `USER.md`
4. Update `SKILLS_INDEX.md` with any new skills created
5. Prune `MEMORY.md` to keep only highest-signal content
6. Archive raw session to `~/.hermes/memory/raw/`

### Provenance Rules
- Every wiki claim must cite a source session
- Use frontmatter: `created_from: session-YYYY-MM-DD-N`
- Mark confidence: `confidence: high|medium|low`
- Flag contradictions with `[[CONTRADICTS: page-name]]`

---

## 3. Skill Factory

### What It Is
When Hermes solves a novel problem well, it extracts the approach into a reusable skill file.

### Skill Authoring Trigger Conditions
Automatically trigger skill creation when:
- A task required 8+ tool calls to complete
- A custom workflow was improvised (not from existing skills)
- User said "can you automate this?" or "can you do X more like this?"
- A complex task was completed successfully that has never been done before
- Error recovery involved an unusual workaround

### Skill File Format (agentskills.io standard)

```yaml
---
name: [skill-name-slug]
description: What this skill does and when to use it
version: 1.0.0
platforms: [linux, macos, docker]
triggers:
  - "when user asks to [description of trigger scenario]"
  - "when [specific situation occurs]"
metadata:
  hermes:
    tags: [category, subcategory]
    reliability_score: 0.0-1.0
    times_used: 0
    last_used: null
    evolved_from: null
---

# Skill: [Human-Readable Name]

## When to Use
[Describe the scenario that should trigger this skill]

## What It Does
[Step-by-step procedure]

## Example
```
[Example usage with exact commands]
```

## Gotchas / Edge Cases
[Known limitations and how to handle them]

## Success Criteria
[How to know if this skill worked]
```

### Skill Self-Improvement
After a skill is used 3+ times:
1. Review usage logs for failure patterns
2. Patch the skill file (targeted edits, not full rewrites)
3. Update `reliability_score` based on success rate
4. Note any new edge cases discovered

### Skill Evolution with DSPy + GEPA
Hermes uses DSPy + GEPA to automatically evolve skill files based on real execution traces. This requires no GPU — just API calls. The system:
- Collects execution traces from skill usage
- Runs GEPA (Gradient-Evolved Prompt Adjustment) on the traces
- Updates the skill's instructions automatically
- Validates against known good outputs before committing

---

## 4. Prompt Optimization

### What It Is
Hermes periodically reviews and refines its own system prompts, SOUL.md, and skill instructions based on observed performance.

### Prompt Optimization Trigger Conditions
Run optimization when:
- Self-reflection scores average below 3.5
- User provides repeated corrections in the same area
- A skill has reliability_score < 0.7
- A new capability is needed that no current prompt handles

### The Optimization Workflow

```
1. ANALYZE — Collect evidence
   ├── Recent self-reflection scores
   ├── User correction patterns (from feedback logs)
   ├── Skill reliability scores
   └── Error logs in this category

2. DIAGNOSE — Find root cause
   └── Which specific instruction is failing?

3. PROPOSE — Draft improved instructions
   └── Write new prompt section

4. VALIDATE — Test on 3+ historical cases
   └── Run the new prompt against old session logs

5. COMMIT — If validated, update the file
   └── Use targeted patch, not full rewrite
```

### Prompt Inventory (what to optimize)

| File | Purpose | Update Frequency |
|---|---|---|
| `SOUL.md` | Core personality + values | Monthly or after major drift |
| `~/.hermes/memory/MEMORY.md` | Always-on context | Weekly or after compaction |
| `~/.hermes/memory/USER.md` | User model | After every major session |
| `~/.hermes/SCHEMA.md` | Wiki conventions | Quarterly |
| Skill files | Task procedures | After every 3 uses or failure |

### Reframing Technique
When a prompt isn't working, apply the **reframing pattern**:
```
BEFORE: "Be more careful about accuracy"
AFTER:  "For factual claims, cite the source session. If uncertain, say 'I don't know' rather than guessing."
```
Specificity beats vague instruction.

---

## 5. Error Recovery

### What It Is
A closed-loop system where Hermes learns from failures and prevents recurrence.

### Error Classification

| Class | Description | Recovery Action |
|---|---|---|
| **T1: Tool Failure** | Tool call returned error | Retry with modified args, then use alternative tool |
| **T2: Context Drift** | Agent loses track of task goal | Re-state goal from MEMORY.md, summarize progress |
| **T3: Prompt Misunderstanding** | Agent misinterpreted user intent | Ask clarifying question, log the misunderstanding |
| **T4: Knowledge Gap** | Agent lacks domain knowledge | Research, add to wiki, flag in SOUL.md |
| **T5: Environmental** | System limitation (permissions, network, etc.) | Document limitation, suggest workaround |

### The Self-Healing Loop

```
Error occurs
    │
    ▼
Diagnose (LLM analyzes error type + context)
    │
    ├── T1: RETRY_MODIFIED → try same tool, different args
    ├── T2: CONTEXT_RESTORE → re-summarize from MEMORY.md
    ├── T3: CLARIFY → ask user, log pattern
    ├── T4: RESEARCH → add knowledge to wiki
    └── T5: DOCUMENT → add to known-limitations.md

Success? ──► Yes → Log as successful recovery in error-log.md
            │
            └── No → After 3 attempts → ESCALATE to user

Preventive: Check if error pattern is new → trigger Skill Factory
```

### Error Logging Format

```markdown
## Error: [Brief Title]
**Date:** YYYY-MM-DD
**Type:** T1/T2/T3/T4/T5
**Session:** session-YYYY-MM-DD-N

### What happened:
[Description of the error]

### What I tried:
1. [First attempt]
2. [Second attempt]
3. [Third attempt]

### What worked:
[The successful recovery]

### Did I create a skill from this?
[Yes/No — if Yes, skill name: _____]

### Prevention:
[What should change to prevent this?]
```

---

## 6. Output Quality (Self-Grading)

### The Generator-Evaluator Pattern

Run a two-pass process for high-stakes outputs:
1. **Generate:** Produce the output (code, analysis, response)
2. **Evaluate:** Run a critical self-assessment

### Evaluation Prompt Template

```markdown
## Evaluate this output

### Task: [Original user request]
### My output: [The response I generated]

### Evaluate against:
1. **Accuracy:** Are the facts correct? Are sources cited?
2. **Completeness:** Did I address all parts of the request?
3. **Clarity:** Is it structured and easy to follow?
4. **Actionability:** Can the user act on this output immediately?
5. **Concision:** Did I avoid unnecessary elaboration?

### What are the weaknesses?
[Specific weaknesses with examples from the output]

### What would I do differently?
[Specific improvement approach]

### Revised output:
[Rewrite addressing the weaknesses]
```

### Quality Gates
- Score < 3.5 on any dimension → regenerate
- User rejection → trigger Error Recovery + Prompt Optimization
- Code output → must pass `lint` + `typecheck` before delivery

---

## 7. Multi-Agent Learning (Hermes ↔ Nanobot)

### Architecture

```
HERMES (Lead Agent)
  ├── Orchestrates high-level goals
  ├── Manages memory + skills
  ├── Delegates to sub-agents
  └── Learns from Nanobot feedback

NANOBOT (Specialist Agent)
  ├── Handles specialized tasks
  ├── Reports outcomes to Hermes
  ├── Can request Hermes help with novel problems
  └── Shares skill discoveries back to Hermes
```

### Communication Protocol

**Hermes → Nanobot:**
```
Task: [Specific task description]
Context: [Relevant background from MEMORY.md]
Tools: [Allowed tool set]
Success criteria: [What "done" looks like]
Escalation: [When to hand back to Hermes]
```

**Nanobot → Hermes:**
```
Result: [What was accomplished]
Learnings: [Any new patterns discovered]
Blockers: [What stopped Nanobot from completing]
Suggestions: [Recommendations for future similar tasks]
```

### Skill Sharing Protocol
When Nanobot discovers a useful workflow:
1. Nanobot writes it as a draft skill in shared format
2. Hermes reviews, edits, validates
3. Hermes commits to `~/.hermes/skills/` under Herms authorship
4. Hermes updates `SKILLS_INDEX.md`
5. Hermes acknowledges Nanobot in skill metadata

### Conflict Resolution
- If Hermes and Nanobot disagree on approach → Hermes wins (it has more context)
- If Nanobot discovers something Hermes doesn't know → Nanobot teaches Hermes
- If both fail the same task → trigger joint reflection, update both

---

## 8. Learning Loop — Putting It All Together

### The Daily Cycle

```
MORNING BRIEF (Cron-triggered)
├── Check for new messages / tasks
├── Update MEMORY.md with overnight insights
├── Run health check on skill reliability scores
└── Report daily focus to user

SESSION START
├── Load MEMORY.md, USER.md, relevant project context
├── Review recent skill usage + scores
├── Check for any flagged errors to avoid
└── Start task

SESSION END
├── Run self-reflection (if task > 5 tool calls)
├── If skill-worthy → trigger Skill Factory
├── Run memory compaction if needed
├── Update skill reliability scores
└── Log session to raw/

WEEKLY MAINTENANCE (Cron-triggered)
├── Review skill reliability scores → patch low scorers
├── Review error log → identify T3/T4 patterns
├── Run prompt optimization on low-scoring areas
├── Check for stale wiki pages
└── Update SCHEMA.md if needed

MONTHLY DEEP REVIEW
├── Full audit of SOUL.md alignment
├── Review user feedback patterns
├── Evolve 3 lowest-reliability skills with DSPy + GEPA
├── Update MEMORY.md compaction strategy
└── Report to user: "Here's how I've improved this month"
```

---

## 9. Prompt Patterns for Self-Improvement

### Pattern 1: The "After Action Review" Prompt
```
After completing [task], identify 3 specific things that went well 
and 3 specific things to improve. Write each as an actionable note.
```

### Pattern 2: The "Skill Extraction" Prompt
```
You just solved [problem]. Write a reusable SKILL.md file that 
captures exactly what you did, including all commands, tool choices, 
and reasoning steps.
```

### Pattern 3: The "Reframe" Prompt
```
The following instruction isn't working: [quote instruction]
Rewrite it to be more specific, actionable, and measurable.
```

### Pattern 4: The "Contradiction Check" Prompt
```
Before writing [claim], check your wiki for contradictions. 
List any contradictions found and how you resolved them.
```

### Pattern 5: The "Confidence Calibration" Prompt
```
For each piece of information in this response, rate your 
confidence: HIGH / MEDIUM / LOW. Cite the source that grounds 
each claim.
```

---

## 10. Power User Patterns (What the Best Do Differently)

### Pattern 1: Structured State Handoff
Instead of letting context get messy, power users:
- Start every session with a structured briefing
- End every session with a structured summary
- Use the same MEMORY.md format every time

### Pattern 2: Explicit "Learn This" Commands
Power users say things like:
- "Remember that I prefer concise responses"
- "Add the docker networking approach to skills"
- "Don't use [method] — I've found [better approach]"

### Pattern 3: Skill Iteration
Power users don't just create skills — they iterate them:
- After 3 uses, review reliability score
- Patch the skill to fix failure modes
- Contribute best skills to the community

### Pattern 4: Multi-Agent Deliberation
For high-stakes decisions, power users run two agents in parallel:
- Hermes takes one approach
- Nanobot takes a different approach
- Compare results, choose the best

### Pattern 5: Memory Hygiene
Power users prune aggressively:
- MEMORY.md has a hard 3,575 char limit
- Wiki pages get archived after 90 days of inactivity
- Skills with reliability < 0.5 get deprecated, not kept

### Pattern 6: The "Acid Test" for Prompts
Ask: "What is my exact definition of done for this task?"
If Hermes can't reproduce the rules verbatim, the instructions are too vague.

---

## 11. Integration: How the Factory Ties Together

```
Self-Reflection ──► Output Quality scores ──► Prompt Optimization
                          │
                          ▼
                    Low scores ──► Error Recovery logging
                          │
                          ▼
                    Patterns ──► Skill Factory
                          │
                          ▼
                    New skills ──► Memory Compounding
                          │
                          ▼
                    Updated wiki ──► Next session gets better

Multi-Agent ──► Nanobot reports ──► Hermes synthesizes ──► New skills
                        │
                        ▼
                  Hermes teaches ──► Nanobot improves
```

---

## 12. Quick-Reference Commands for Hermes

| Action | Command / Trigger |
|---|---|
| Run self-reflection | `reflect on this session` |
| Trigger skill factory | `extract this as a skill` |
| Compact memory | `compact my memory` |
| Optimize a prompt | `improve my [SOUL.md/MEMORY.md/skill]` |
| Log an error | `log error: [description]` |
| Check skill scores | `review skill reliability` |
| Multi-agent task | `delegate to Nanobot: [task]` |
| Start daily brief | `morning brief` |
| End-of-day summary | `daily summary` |

---

## Appendix: Key Files and Locations

| File/Directory | Purpose |
|---|---|
| `~/.hermes/SOUL.md` | Core personality and values |
| `~/.hermes/memory/MEMORY.md` | Always-on context (3,575 char) |
| `~/.hermes/memory/USER.md` | User model (preferences, patterns) |
| `~/.hermes/memory/wiki/` | Synthesized knowledge base |
| `~/.hermes/memory/raw/` | Raw session logs (append-only) |
| `~/.hermes/skills/` | All skill files |
| `~/.hermes/error-log.md` | Error recovery log |
| `~/.hermes/SCHEMA.md` | Wiki conventions and taxonomy |

---

*Factory Framework v1.0 — Built for Jordan's Hermes Agent*
*Each subsystem is designed to compound the others — the more Hermes learns, the faster it learns.*