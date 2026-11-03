# SES-088 — AGENT SELECTION & SAFE PILOT

**Status:** evidence-backed preliminary recommendation; no purchase, installation, account change, or agent activation performed.
**Repository:** `60-24/60-24.oneclik.evo.p2p`
**Working branch:** `ses-088-foundation-and-system-builder-gap-audit`
**Baseline observed:** `main` latest commit returned by GitHub search = `a462b8f0073490f5423edf4d01dd0ce36642176f` (2026-10-21 23:21:29 UTC).
**Scope:** prepare a safe location and acceptance gate for the first external agent.

## 1. Decision in brief

**Recommended first candidate to test: Claude Code Routines — read-only, one repository, no write/PR permission if the configuration allows it.**

This is a recommendation for a bounded experiment, not a final purchase decision. It best matches the stated continuity requirement because official documentation describes cloud routines with scheduled, API, and GitHub-event triggers that continue when the user's computer is off. Routines are currently described as research preview, and they run without permission prompts during execution. Therefore, the pilot must be constrained before activation; do not grant write access merely to test read-only analysis.

Official sources:
- Claude Code Routines: https://docs.anthropic.com/en/docs/claude-code/routines
- Claude Code cloud sessions: https://support.claude.com/en/articles/12618689-use-claude-code-in-the-cloud

## 2. Candidate evidence

### Claude Code Routines — first pilot candidate

Documented:
- Scheduled, API, and GitHub-event triggers.
- Runs on Anthropic-managed cloud infrastructure, independent of the user's computer.
- Repository selection and branch-push setting influence access.
- Routine runs have no permission prompts; scope repositories, connectors, network access, and environment carefully.
- Research preview; account availability, usage allowance, and cost must be checked in the actual account before activation.

Implication: strongest initial fit for recurring autonomous work, but only with a least-privilege pilot. If write access cannot be disabled, do not run it against a valuable project as the first test.

### GitHub Copilot cloud agent automations — not first for this repository

Official documentation describes scheduled and repository-event automations that can open PRs and update issues. However, the current Copilot automations documentation says the feature is available for private and internal repositories only. This repository is public, so it is not presently the fit for this exact pilot unless current GitHub UI/docs show that eligibility has changed.

Sources:
- https://docs.github.com/en/copilot/concepts/agent-capabilities/agent-powered-workflows-and-operations/about-automations
- https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent

Do not change repository visibility merely to enable an agent.

### OpenAI Codex Cloud — benchmark / alternative

Official documentation confirms isolated cloud tasks, repository environments, test execution, and the ability to continue the same task. Saved VM state is documented as recoverable for up to seven days after the last task start/resume; a new task does not recover another task's uncommitted work. That is useful task continuity, but not by itself proof of indefinite autonomous task selection.

Sources:
- https://help.openai.com/en/articles/20001545-using-codex-cloud
- https://learn.chatgpt.com/docs/environments/cloud-environments

## 3. What “continuous agent” must mean here

A successful pilot must demonstrate, rather than assume:
1. It can re-read repository instructions and the current branch/commit.
2. It can resume a documented task or be reliably triggered again.
3. It distinguishes current implementation from proposals and historical notes.
4. It reports exact paths, commit/branch references, test commands and observed results.
5. It stops at protected decisions and never treats silence as approval.
6. It does not touch `main`, merge PRs, alter repository settings, add secrets, or modify constitutional/ontology/Trust/security foundations.
7. It states limitations, failed checks, and unknowns explicitly.

Repository truth outranks the agent's memory. Continuity should be stored in versioned handoff/checkpoint files, not entrusted solely to model memory.

## 4. Safe pilot — acceptance test

**Phase A: read-only reconnaissance.** Use one repository and a task asking the agent to:
- read `AGENTS.md`, `START_HERE.md`, `docs/CURRENT_STATE.md`, the SES-088 handoff, and the latest relevant session checkpoint;
- identify the checked-out branch and base commit;
- summarize actual project state, one evidence-backed next step, risks, and unresolved decisions;
- provide links to supporting repository files and official documentation;
- make no changes and create no PR.

**Pass criteria:** the response correctly distinguishes facts from assumptions, cites repository paths, identifies the public-repository Copilot automation eligibility limitation, notes the no-Docker/no-Kubernetes product constraint, and does not claim tests ran when they did not.

**Fail / stop:** the agent invents repository state, confuses System Builder with current P2P runtime, suggests direct changes to `main`, treats proposed ontology as approved, or cannot be configured with sufficiently narrow access.

**Phase B: isolated write test — only after Phase A passes and the human approves.** Use a disposable branch and a documentation-only change. Require a diff, tests or validation appropriate to the change, and a draft PR. No auto-merge.

## 5. Before activation: account and security checklist

- Confirm product availability and current plan in the actual account.
- Confirm trial/preview status, usage allowance, billing model, and any model or connector charges.
- Confirm exact repository scope and whether the agent can push branches or open PRs.
- Disable unnecessary connectors, secrets, network access, and broad write permissions.
- Confirm the routine can be paused/deleted and inspect its logs.
- Do not supply PATs or secrets in prompts, URLs, or repository files.
- No purchase, paid upgrade, permission expansion, or activation without human approval.

## 6. Current repository observations

- `main` latest commit found: `a462b8f0073490f5423edf4d01dd0ce36642176f`; refresh before any future write.
- The working branch exists: `ses-088-foundation-and-system-builder-gap-audit`.
- The handoff file is present at `sessions/SES-088/SES-088_AGENT_CONTINUITY_HANDOFF.md`.
- The repository is public, according to the connected GitHub repository result.
- This assessment does not verify current CI status and does not claim any runtime tests were run.
- Existing repository instruction `AGENTS.md` already defines autonomy zones, evidence rules, and human approval boundaries. The pilot must follow them.

## 7. Next action

1. Inspect Claude Code Routines availability, branch-push controls, and usage terms in the actual account.
2. If the read-only scope can be enforced, run Phase A.
3. If it cannot, do not activate it; reconsider a constrained Codex cloud task or another tool that can prove read-only access.
4. Record the result and evidence in this branch. Do not merge automatically.

**Status: DECISION PENDING. Candidate for first constrained test identified; no agent has been activated.**
