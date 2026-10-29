# GitHub Cloud Development Model — Shared Interpretation

**Status:** engineering guidance; not a change to the P2P protocol or product architecture.  
**Scope:** how humans and AI agents develop, test, build, and publish this repository.  
**User-facing constraint:** the finished P2P program must not require the end user to install Docker, Kubernetes, a database server, or a development environment.

## 1. Decision in brief

**Development can be performed online through GitHub, without keeping a working copy on the user's personal computer.** That does not mean every action happens inside the GitHub website itself, nor that GitHub replaces all runtime dependencies or external services.

The recommended model is:

1. GitHub repository is the source of truth.
2. A cloud development workspace (GitHub Codespaces, when needed) provides a terminal and editable working tree in the cloud.
3. GitHub Copilot coding agent can take a bounded issue/task, work in its hosted environment, and propose changes as a pull request when enabled and configured.
4. GitHub Actions runs repeatable tests/builds on hosted runners and stores artifacts.
5. A human reviews evidence and approves protected decisions and merges.

Use the simplest surface that fits the task: GitHub web UI for small edits/reviews; Copilot coding agent for bounded code tasks; Codespaces for interactive development/debugging; Actions for reproducible CI. These are complementary, not interchangeable.

## 2. What “no local files” actually means

“Local” has two meanings and must not be confused:

- **On the user's computer:** a clone, editor, compiler, SDK, database, or command-line tools installed on their personal device. This is not inherently required for repository development.
- **Inside a workspace:** code and temporary files must exist somewhere while a build or test runs. That place can be a cloud Codespace or a hosted Actions runner instead of the user's computer.

The GitHub website can edit many text files and manage pull requests, but it is not a full interactive operating system or a universal compiler. Some tasks need a terminal, SDKs, dependencies, debugging, or several running processes. Those can often be provided by Codespaces or Actions. A cloud workspace still uses files; they are simply hosted remotely.

Actions runners are generally job-scoped environments. Do not treat a runner's working directory as permanent storage. Preserve required outputs as workflow artifacts, commits, releases, or another explicitly configured store. A Codespace is a workspace with its own lifecycle and storage rules; it is not the repository itself and should not be the only place where important work exists.

## 3. Separate the development environment from the delivered product

These are different environments with different requirements:

| Layer | Purpose | May use development tooling? | Must the end user install it? |
|---|---|---|---|
| GitHub repository | Source, decisions, tests, documentation | N/A | No |
| Codespaces / agent environment | Edit, inspect, debug, run commands | Yes, as justified | No |
| GitHub Actions runner | Automated checks and builds | Yes, as justified | No |
| Build-time libraries / SDKs | Compile and test source | Yes; pin and document them | Usually no, if bundled or not needed at runtime |
| Runtime libraries | Required while the application runs | Depends on packaging | Avoid extra manual installs for the intended OneClick experience |
| External infrastructure | Optional bootstrap, relay, update service, hosted database, etc. | Only if architecture requires it | May create ongoing operating, privacy, security and availability obligations |

The standing product constraint is **no Docker/Kubernetes or other development-environment installation required from the end user**. This does not automatically forbid every development tool in a cloud CI job, but repository decisions also record a specific unresolved conflict: `.github/workflows/g01-neo4j-gs01.yml` and `.github/workflows/g01-neo4j-gs02.yml` use Docker/Neo4j. Do not manually run or trigger these workflows until that conflict has been explicitly resolved. Do not infer that “cloud-only” makes the conflict disappear.

## 4. Libraries, databases, and workspace: add only when evidence requires them

### Libraries and SDKs
A project needs the language runtime/compiler and libraries required by its code and tests. In CI, declare them in the repository (for example, dependency manifests and lockfiles where supported) and install them reproducibly in the workflow. Prefer pinned or bounded versions, minimal dependencies, and automated security/update review. A library used only to build/test is not necessarily a dependency the final user must install.

### Databases
A database is **not automatically required** for P2P. Add one only when an approved feature has a real persistence/query need that cannot be met more simply with the existing design. First identify what data is stored, who owns it, retention, migration, backup, privacy, and failure behavior. A local embedded store and a remote database have very different consequences. A central database must not silently become a mandatory central authority for a decentralized design.

Neo4j is not a prerequisite for the current P2P runtime. Existing G-01/Neo4j evaluation workflows are separate historical/evaluation work and are currently constrained by the recorded Docker conflict.

### Cloud workspace
A Codespace is useful when work needs a terminal, an IDE, interactive tests, or multiple processes. Configure only the tools actually needed by the current task. Do not add a workspace configuration, service, database, or container just because the platform supports it.

### Secrets
Never commit credentials, private keys, access tokens, or production secrets. Use GitHub Actions secrets/variables only where needed, least-privilege permissions, and explicit environment/review gates for sensitive deployment. Treat pull-request code and AI-generated changes as untrusted until reviewed and tested.

## 5. What Copilot coding agent does — and does not do

When available and enabled for the repository/account, GitHub Copilot coding agent can be assigned a bounded task, work in a hosted environment, use configured tools, and submit a pull request for review. Repository instructions such as `AGENTS.md` help establish project rules.

It is not a guarantee of unrestricted, uninterrupted, indefinitely autonomous work. Availability, permissions, supported operations, usage limits, costs, network access, and tool access depend on GitHub's current product configuration and the account/organization policy. Verify these before relying on the agent. Keep tasks small, require test evidence, and review its diff. Do not grant broad write/deployment secrets merely to make the agent appear autonomous.

**Continuity belongs in repository artifacts**, not in an assumed permanent agent memory: task/issue, branch, commits, session handoff, tests, evidence, and next action. An agent should resume by inspecting these artifacts and the current repository state.

## 6. P2P architecture: what the analogy does and does not imply

The target is a peer-to-peer application, not a blockchain. “Client” and “server” can be roles played by processes on a device: a node may listen for inbound connections and also initiate outbound connections. During development, two processes on one computer can test the protocol over loopback; that proves local process communication, not communication between physical devices.

The current repository proves a narrower foundation: Node A can connect to Node B over TCP, perform HELLO/WELCOME/AUTH with Ed25519 proof of possession, exchange a message and response, and exercise framing/error handling. The current transport is TCP. This is not yet an Internet-wide network.

Skype and Bitcoin are not interchangeable technical blueprints:
- Skype is a communication product whose historical and current architectures should not be assumed identical; voice/video introduces latency, media, NAT, availability and privacy requirements.
- Bitcoin is a peer-to-peer transaction network whose consensus and blockchain are core to its design. This project explicitly does **not** use a blockchain and should not import Bitcoin consensus, mining, or token assumptions by analogy.

P2P does not mean “no servers under any circumstances.” Discovery/bootstrap, relays, updates, or rendezvous may be useful in some designs, but each is an architectural choice with costs and trust/privacy implications. None should be added without a demonstrated GAP and an approved design. NAT traversal and relay support are not currently implemented.

Also distinguish **two roles on one device** from **a useful multi-device P2P network**. A loopback test is an early protocol test; LAN and Internet tests require separate evidence. CI success does not prove real-world connectivity through every router, firewall, carrier-grade NAT, or mobile network.

## 7. Recommended engineering workflow

Follow the repository's existing method:

**INSPECT → UNDERSTAND → IDENTIFY REAL GAP → RED (when meaningful) → MINIMAL IMPLEMENTATION → GREEN → EVIDENCE → DOCUMENT → STONE**

For each bounded task:
1. Inspect the current branch, authoritative docs, code, tests, and existing workflows.
2. State the expected outcome and allowed scope.
3. Reuse the current language, dependency system, architecture, and test patterns.
4. Add a regression test for a demonstrated defect or a test before implementation where a clear specification exists. Do not manufacture a failing test when there is no meaningful test case.
5. Run relevant tests locally in the cloud workspace or in Actions. Distinguish “not run,” “passed in CI,” “passed locally,” and “verified on physical devices.”
6. Review the diff, permissions, dependency changes, and generated artifacts.
7. Open a pull request with evidence. Do not silently merge architectural, protocol, ontology, or security-governance decisions that require human approval.
8. Record the commit, checks, known limitations, and next step in repository documentation/session notes.

## 8. Current scope and evidence boundary

As recorded in `docs/CURRENT_STATE.md` and `README.md`, the current implementation has Linux/Windows build paths and an Android APK build path, with CI artifacts. An artifact is not necessarily a permanent public release, and a successful workflow proves only the checks actually executed for that commit.

Current limitations include automatic peer discovery, NAT traversal, relay infrastructure, end-to-end encryption, advanced authorization, GUI, automatic installation, and production-grade Internet deployment. These are limitations, not automatic requirements. Do not claim that a complete Skype-like product exists today.

## 9. Final shared interpretation

- **The user need not program on or install a development environment on their personal computer.**
- **Code still exists in a repository or cloud workspace while it is edited, compiled, and tested.**
- **GitHub web editing, Codespaces, Copilot coding agent, and Actions have distinct roles.**
- **Extra libraries are added when required and declared reproducibly; a database is not presumed necessary.**
- **The end-user OneClick requirement is a product constraint, not a ban on all cloud-side development tooling.**
- **No Docker-based G-01/Neo4j workflow may be run until its recorded conflict is resolved.**
- **This project is P2P without blockchain.** A local client/server test is not proof of a robust multi-device or Internet-wide P2P network.
- **The repository and test evidence are the source of truth.** Agent claims, plans, artifacts, and chat summaries are not substitutes for verified code and checks.

## References

- [GitHub Codespaces documentation](https://docs.github.com/en/codespaces)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub Copilot coding agent documentation](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
- [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
