
# P2P 60-24 OneClick Evo Positiv — Project Overview for Humans

> **Purpose:** explain the project from its beginning to the current state in plain language, without requiring programming knowledge.
>
> This document complements the technical README. The README explains **how to run the current program**. This document explains **why the project exists, how it evolved, what has actually been built, how it is verified, and where we are now**.

---

# 1. Why was the project created?

The starting idea was simple:

> **People should be able to connect and cooperate directly through their own devices, without giving a central operator control over their communication and relationships.**

The project was therefore intended to be more than an ordinary messenger.

The original direction included:

- direct device-to-device communication,
- as little dependence on central servers as possible,
- local/LAN operation,
- minimal data,
- future offline and mesh possibilities,
- user control,
- security,
- trust between real people,
- no dependence on cryptocurrency, tokens, or speculation.

The broader social goal was to use technology as infrastructure that supports people rather than creating another central intermediary between them.

---

# 2. The original idea was much larger

At the beginning the project had a much broader vision.

One major concept was a **System Builder**: a system that could understand what a person wants and then:

**understand → design → build → test → deliver a working system.**

P2P 60-24 OneClick Evo was one concrete system that could eventually be built within that larger vision.

This led to a substantial conceptual architecture:

- system constitution,
- microkernel architecture,
- events,
- contracts,
- state,
- capabilities,
- trust,
- authorization,
- execution,
- results,
- effects.

One especially important architectural distinction became:

**communication ≠ trust ≠ authorization ≠ execution ≠ effect**

This prevents the system from treating a network connection, a trusted relationship, permission to act, an attempted action, and its result as if they were the same thing.

---

# 3. The project deliberately became smaller before becoming bigger

There was an important risk: a project can have a very large architecture, documentation, and vision while still lacking a simple program that really works.

So the scope was deliberately reduced.

Instead of trying to build the whole future ecosystem at once, the project chose a concrete foundation:

> **First build a real, downloadable P2P program: Node A ↔ Node B.**

That means two independent program processes should be able to:

**Node A → Node B**

and back:

**Node B → Node A**

Only after this foundation works reliably should larger layers be added.

This decision is one of the most important in the history of the project.

---

# 4. Early stages — building the foundations

The first stages established the internal rules needed to move from an idea toward a real system.

The project tested such things as:

- how a user intention is represented,
- how an execution request is represented,
- how approval is separated from execution,
- how a result is represented,
- how an effect is produced.

Important milestones included:

- **SES-007** — Intent Envelope,
- **SES-009** — specification and CI,
- **SES-013** — GREEN,
- **SES-014** — approval boundary,
- **SES-015**,
- **SES-017** — execution request,
- **SES-021** — result → effect verification.

For a non-programmer, the important meaning is:

> the system was being forced to make its actions explicit: what was requested, whether it was allowed, what was attempted, and what the result was.

---

# 5. From concepts to two real nodes

The next stage moved from internal models toward real P2P communication.

Two independent nodes were introduced.

The question changed from:

> “Does this internal function work?”

to:

> “Can two separate programs really find each other, connect, and exchange information?”

**SES-043** produced an important two-node proof.

Further sessions strengthened this foundation.

---

# 6. SES-047 — reproducible evidence became central

SES-047 reached **GREEN / CLOSED**.

At this point an increasingly important rule became explicit:

> **It is not enough to say that something works. There must be evidence that it works.**

Evidence can be:

- a test,
- a CI result,
- a log,
- an artifact,
- a commit,
- a session document.

This creates a history that can be checked later instead of relying on memory.

---

# 7. The System Builder chain was also demonstrated

SES-052 demonstrated a working System Builder chain.

The important flow was:

**intention → specification → execution → result → effect**

and it was verified through CI.

This showed that the earlier conceptual work was connected to executable behavior.

It did **not** mean that the complete future System Builder was finished.

That distinction remains important.

---

# 8. SES-053 — a stable checkpoint

SES-053 ended as:

**GREEN / CLOSED / STONE**

This established a stable point from which later work could continue.

A session closure therefore means:

> a defined scope has been completed and documented,

not:

> the entire project is finished.

---

# 9. A real identity problem was discovered

As the P2P runtime became more concrete, a problem appeared.

The two nodes could communicate, but identity visibility was not sufficiently symmetric.

**SES-055** identified:

**GAP-055-01 — asymmetric identity observability.**

The problem was fixed with a minimal change.

This became an important example of the project's working method:

> even when the main function works, deeper inspection can reveal a real problem.

Finding such problems is not failure. Finding and correcting them is part of building the system correctly.

---

# 10. SES-056 — focus moved to the real downloadable P2P program

SES-056 made the direction explicit:

> move from architecture auditing toward a real Node A ↔ Node B program.

The project deliberately did **not** try to implement all future features at once.

The immediate goal was:

> **a program that can actually be run on two devices.**

---

# 11. SES-057 — the real Node A ↔ Node B proof

SES-057 was one of the major milestones.

Two independent nodes could:

**Node A**

↓ connection

**Node B**

and then:

**HELLO**

↓

**WELCOME**

↓

peer identification

↓

message exchange

↓

response.

The CI proof was recorded in run:

**35508861137**

with the corresponding artifact.

This marked an important transition:

> **the project no longer had only a P2P concept; it had a working P2P foundation.**

---

# 12. Usability became part of the engineering work

Once basic P2P communication worked, the project was examined from the perspective of an ordinary user.

It was not enough for:

> “a developer knows how to make it work.”

The intended path should be:

1. download the program,
2. start Node B,
3. start Node A,
4. provide the address,
5. see the connection,
6. exchange a message.

Therefore error handling and documentation became part of the project rather than an afterthought.

---

# 13. SES-059/060 — real user errors were tested

An external audit identified a usability problem.

When a bad --connect address was supplied, the program could expose a low-level parser error instead of a useful short message.

This was a real usability GAP.

The solution was to turn this into a controlled CLI error boundary.

The same principle was then applied to malformed peer handshakes.

This illustrates another important distinction:

> **“technically works” and “is usable by a person” are different requirements.**

---

# 14. SES-061 — a real executable became available

SES-061 reached:

**GREEN / CLOSED / STONE**

Workflow:

**P2P Linux executable**

Run:

**35688822581**

A real executable was produced.

The project therefore moved from:

> “the program exists in the repository”

to:

> **“a user can download a built program.”**

---

# 15. SES-062 — a stable Node A ↔ Node B foundation

SES-062 started from a working foundation:

**download → Node B → Node A → TCP → HELLO/WELCOME → identification → message → response**

At this point the project had a real basic P2P runtime.

It was still a foundation, not the completed system from the original vision.

---

# 16. SES-063 — the independent-user path was documented

The README was expanded so an independent user could follow the full path:

1. download the GitHub Actions artifact,
2. extract it,
3. start Node B,
4. start Node A,
5. establish the connection,
6. exchange messages.

The documented expected results include:

**pong-from-B**

and:

**node B received from A: hello-from-A**

The important change is that the project no longer says only:

> “it should work.”

It specifies:

> **what the user does and what the user should see.**

---

# 17. SES-064 — cryptographic identity

The next major step was real cryptographic identity.

Each node received an Ed25519 identity.

In simple terms:

> each node has a cryptographic proof that it possesses a particular private key.

The communication handshake became:

**HELLO**

↓

**WELCOME + cryptographic challenge/signature**

↓

client proves possession of its private key

↓

peer verifies the signature

↓

authenticated communication.

This is much stronger than simply trusting a text label such as “Node B”.

---

# 18. Authentication was kept separate from trust

This is an important architectural boundary.

The cryptographic handshake answers:

> **“Can this peer prove possession of this key?”**

It does not automatically answer:

> “Do I trust this person?”

and it does not automatically grant authorization.

Therefore the project deliberately keeps:

**identity → authentication → trust → authorization**

as separate concepts.

---

# 19. SES-065 — identity survives restart

The next problem was persistence.

If a node created a new cryptographic identity every time it started, it would not have a stable identity.

SES-065 verified persistent Ed25519 identity.

The local identity store allows the same public key and NodeID to survive process restarts.

A corrupted identity store is rejected rather than silently replaced.

The private key remains local.

No global identity service or PKI was introduced.

---

# 20. SES-066 — stop and inspect the whole project

The current session deliberately changed the rhythm.

Instead of automatically creating another feature, the project performed a whole-repository inspection.

The process is:

**INSPECT**

↓

**UNDERSTAND**

↓

**IDENTIFY GAP**

↓

**RED TEST**

↓

**IMPLEMENT**

↓

**GREEN**

↓

**VERIFY**

↓

**DOCUMENT**

↓

**COMMIT**

↓

**CONTINUE**

The principle is:

> **Do not move to the next feature simply because the previous session ended. First verify the current state of the whole system.**

---

# 21. GAP-066 — what it means

The current inspection found a candidate real problem in the TCP receive path.

The program reads incoming data until it sees the end-of-message marker.

The current implementation does not enforce a maximum frame/message size.

In simple terms, imagine a peer that connects and keeps sending:

**AAAAAAAAAAAAAAAAAAAAAAAA...**

without ever sending the expected end of the message.

The receiving program can continue accumulating the data.

That means the receive buffer can grow without a defined upper limit.

This creates a potential resource-exhaustion problem.

---

# 22. Why GAP-066 is not fixed blindly

At the current point, GAP-066 is:

> **confirmed in the code as a missing protection, but not yet closed as a project GAP.**

The next correct step is a **RED test**.

The test should demonstrate the required behavior:

> a message/frame exceeding the allowed maximum must be rejected instead of being accumulated without limit.

Only after that should the smallest effective implementation change be made.

Then:

**RED → minimal fix → GREEN → regression → executable verification → documentation**

This is intentional.

---

# 23. Why tests and evidence matter as much as code

Code says:

> “this is how we implemented it.”

A test says:

> “we checked that the behavior is what we expect.”

CI evidence says:

> “the check can be repeated in a controlled environment.”

Therefore the project treats three things as one engineering chain:

### Code
What the program does.

### Test
What we verify.

### Evidence
The recorded result proving the verification happened.

This is why the repository contains not only source code, but also session documents, CI runs, artifacts, and verification history.

---

# 24. Why GitHub Actions is important

The public repository uses GitHub Actions as a reproducible execution environment for testing and building.

The chain is:

**code → build/test → result → artifact**

This is stronger than:

> “it works on my computer.”

The executable can be built and the relevant behavior can be checked repeatedly.

---

# 25. What GREEN / CLOSED / STONE mean

Within this project:

### GREEN
The defined verification passes.

### CLOSED
The defined scope of the session has been completed.

### STONE
A stable checkpoint has been created that can serve as a known foundation for later work.

These labels describe a specific project stage. They do not mean the whole project is finished.

---

# 26. What has actually been built?

Today this is no longer only documentation.

There is a real P2P runtime in which two independent nodes can:

- start,
- connect,
- perform a TCP handshake,
- identify the peer,
- perform cryptographic authentication,
- exchange application messages,
- receive a response,
- retain their cryptographic identity across restarts.

There is also:

- a downloadable executable,
- a GitHub Actions build,
- automated verification,
- artifacts,
- user documentation,
- session history,
- recorded evidence of previous milestones.

---

# 27. What has NOT been built yet?

The project does not claim that the entire original vision is complete.

The current runtime is not yet:

- a complete decentralized social network,
- a complete Web-of-Trust,
- the full LocalTrust/RealBond system,
- the complete Proof of Meeting system,
- a large mesh network,
- the complete System Builder,
- a production-ready Internet-wide P2P product.

The current work is deliberately focused on the foundation.

That is a feature of the development method, not a failure.

---

# 28. The most important lesson

The biggest achievement is not one particular programming technique.

It is the development method.

The project moved from:

**large vision**

to:

**architecture**

to:

**small executable foundation**

to:

**real two-node communication**

to:

**cryptographic identity**

to:

**persistent identity**

to:

**whole-system inspection**

to:

**finding the next real weakness.**

The current rule is:

> **Do not assume that working means finished. Check it.**

If a real problem is found:

> **prove it, fix it minimally, and verify the whole system again.**

If no real problem is found:

> **do not invent one just to create another session.**

---

# 29. What do we have today?

The simplest answer is:

> **We have a working, downloadable foundation of a real P2P system in which two independent nodes can connect, identify each other, authenticate cryptographically, exchange messages, and preserve their identities across restarts.**

This is no longer only an idea.

It is no longer only documentation.

It is no longer only an internal prototype.

**It is a real working and testable P2P foundation.**

At the same time, it is not yet the complete system from the original vision.

The current phase is:

**working foundation → rigorous inspection → real GAP removal → further layers**

---

# 30. How far are we from the goal?

A simple analogy is building a house.

### Step 1 — idea
We had the vision of the whole house.

### Step 2 — design
We created architecture and rules.

### Step 3 — foundation
We built the basic execution and communication mechanisms.

### Step 4 — two connected rooms
We created two real nodes and connected them.

### Step 5 — identity and security foundation
We added cryptographic identity and authentication.

### Step 6 — persistence
The identity survives a restart.

### Step 7 — current stage
We are checking the foundation again before adding another floor.

That is where the project stands today.

---

# Final answer in one sentence

> **We started with a broad vision of a decentralized human-centered system; today we have a real, downloadable and testable Node A ↔ Node B P2P foundation, and we are now strengthening that foundation systematically — one real GAP at a time — before building the next layers.**

## Working principle

> **Maksymalizacja przez minimalizację.**
>
> Build no more than necessary.  
> Verify every important step.  
> Fix real problems.  
> Do not create artificial problems.  
> Keep the evidence.  
> Continue only from a verified state.
