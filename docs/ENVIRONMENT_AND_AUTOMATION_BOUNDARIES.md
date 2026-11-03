# Environment, Dependencies and AI-Agent Boundaries

**Status:** documentation of the verified repository boundary; not a proposal to add runtime components.  
**Reviewed:** 2026-10-29  
**Repository:** P2P 60-24 OneClick Evo Positiv

## 1. Executive decision

The other LLM's description of GitHub automation is broadly correct, but it mixes capabilities, optional future infrastructure, and features that would need implementation.

**Do not add a database, networking library, relay, or in-app AI model merely because it is available.** First identify a concrete gap in the current runtime, then choose the smallest dependency that solves it and verify it with tests.

The current product goal remains a small, downloadable P2P node. Developer automation must not become an end-user installation requirement.

## 2. What is present in this repository

Inspection of the repository at this review found:

- GitHub Actions workflows for Linux, Windows and Android builds, evidence/tests, and release packaging.
- `requirements.txt` currently declares `cryptography>=42,<51`.
- `.devcontainer/devcontainer.json` exists and configures Go, Rust, Python and Node development features.
- The runtime proof is direct Node A ↔ Node B communication over the current TCP transport, with HELLO/WELCOME/AUTH and Ed25519 proof-of-possession.
- Separate Neo4j-related workflow and historical session files exist. Their presence does **not** make Neo4j a runtime dependency.
- The repository has agent instructions in `AGENTS.md`; this is guidance for engineering agents, not an AI agent embedded in the P2P executable.

These are repository facts, not a claim that every workflow currently passes. CI must be checked for the exact commit being evaluated.

## 3. Three separate environments

### A. End-user P2P runtime

This is the executable/APK downloaded and run by a user.

- **No Docker or Kubernetes requirement.** This is a hard product constraint.
- Do not require the user to install Python, Go, Rust, Node, a database server, an AI runtime, or a developer tool just to run a packaged build.
- Package required runtime components into the distributable where appropriate and permitted by their licences.
- The existing TCP P2P proof does not by itself provide Internet-wide discovery, NAT traversal, relay, end-to-end encryption, or production deployment.

### B. Build and CI environment

GitHub Actions can run configured tests, build binaries/APKs, and retain workflow artifacts. Those outcomes require actual workflow definitions and a successful run for the exact commit.

- CI tools and build dependencies belong in workflows or build configuration, not automatically in the end-user installation.
- A workflow artifact is a downloadable build output; it is not automatically a published, versioned GitHub Release.
- A build passing on a CI runner is not proof that all physical LANs, routers, or operating systems work.

### C. Optional developer workspace

The existing `.devcontainer/devcontainer.json` is a development-environment configuration. It can help standardize tools for contributors or a supported cloud workspace.

- It is optional for end users and does not mean the application itself runs in a container.
- Do not create or pay for a separate Codespace unless a concrete development need justifies it.
- The configured Go/Rust/Python/Node features do not mean all four languages are runtime dependencies.
- A new library should be added only when a real implementation need and its maintenance/security costs are documented.

## 4. Databases and additional libraries

No database is currently established as a required dependency of the minimal P2P runtime.

Add a database only when a specific persistence/query requirement cannot be met adequately by the current design. Before adoption, document:
1. the demonstrated gap and alternatives considered;
2. whether data is local or shared and who controls it;
3. packaging, migration, backup, privacy and failure behavior;
4. dependency/licence/security maintenance;
5. tests proving the required behavior.

Neo4j-related workflows and historical G-01 documents must be treated as a separate experimental/evaluation track unless an approved architecture decision explicitly connects them to the runtime. They do not authorize installing Neo4j for end users.

Likewise, do not add libp2p, IPFS/Helia, OrbitDB, CRDTs, relays or discovery mechanisms without an evidence-backed GAP and approval at the appropriate architecture boundary.

## 5. Two different meanings of “AI agent”

**Engineering agent:** a tool that reads and edits the repository, runs tests, and prepares evidence or pull requests. It belongs to the development workflow. `AGENTS.md` defines project rules but does not itself install or activate such an agent. A real autonomous agent still needs a chosen product, account/plan access, permissions, triggers, workspace and cost/security checks.

**In-app AI:** a model or agent shipped with or called by the P2P application to provide functionality to end users. This is a product feature with separate model/runtime/API, privacy, resource, offline/online and security implications. The current runtime does not require it, and adding an engineering agent does not add in-app AI.

Do not conflate either with GitHub Actions: Actions automate configured jobs; they are not by themselves a continuously planning AI agent.

## 6. Bootstrap, relay and network infrastructure

Bootstrap/discovery and relay services can be useful in some P2P designs, particularly when peers do not know each other's addresses or cannot accept direct connections. They are not mandatory for every P2P topology.

For the current direct Node A ↔ Node B proof, manually supplying an address is sufficient. If a later requirement demands automatic discovery or connectivity across NAT/firewalls, record a concrete network test and GAP first, then compare local discovery, rendezvous/bootstrap, STUN-like techniques, and relays. A relay may carry traffic without becoming the authoritative store for application data, but it still introduces availability, cost, privacy and trust considerations.

## 7. Security and evidence rules

- Use least-privilege GitHub Actions permissions.
- Do not expose secrets to untrusted pull-request code or grant write access to an agent for a read-only trial.
- “Do not edit” in a prompt is not a security boundary; enforce read-only permissions technically where possible.
- Never claim GREEN based on an absent status, a different commit, or an artifact alone.
- Preserve the workflow: **INSPECT → UNDERSTAND → GAP → RED → IMPLEMENT → GREEN → EVIDENCE → STONE**.
- Human approval remains required for protected architecture, protocol, ontology, Trust, governance and security decisions.

## 8. Recommended next action

No new runtime library, database, Docker/Kubernetes layer, or embedded AI is justified by the supplied LLM description alone.

Keep this document as the environment boundary. For the agent-continuity initiative, continue the separate SES-088 preflight: refresh the branch/main/CI evidence, verify actual account availability, permissions and cost, and perform a technically constrained read-only pilot before considering any write-enabled trial.

## 9. Official references

- GitHub Actions workflow artifacts: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
- GitHub Codespaces / development containers: https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers
- GitHub Actions secrets: https://docs.github.com/en/actions/concepts/security/secrets
- Secure use of `pull_request_target`: https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target
