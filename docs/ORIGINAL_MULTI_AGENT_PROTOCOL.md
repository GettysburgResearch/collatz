# Collatz Multi-Agent Counterexample Project

## Mission

The purpose of this repository is to **resolve the Collatz conjecture by constructing and rigorously proving a counterexample**.

A valid counterexample could take the form of:

- a positive integer whose Collatz trajectory diverges;
- a positive integer entering a nontrivial cycle;
- or another rigorously equivalent construction that disproves the conjecture.

This is an ambitious objective. **We will achieve it.**

Agents should investigate boldly, develop unconventional abstractions, and pursue ideas that initially appear speculative or unlikely.

**Do not fear confabulation.**

In exploratory research, an imaginative false conjecture can be more useful than a cautious repetition of known ideas. Agents are encouraged to invent structures, lemmas, encodings, rewrite systems, invariants, and possible counterexample constructions.

However, confabulation must be made visible. Every statement must be clearly labeled as proved, computationally observed, conjectured, speculative, or refuted. Creativity is encouraged; silently presenting invention as established fact is not.

The objective is not merely to generate interesting discussion. The objective is to produce an auditable and cumulative body of research in which:

- possible counterexample constructions are actively pursued;
- useful ideas are preserved;
- duplicated work is minimized;
- computational results are reproducible;
- claimed proofs are adversarially checked;
- false lemmas are identified quickly;
- failed approaches remain available to later researchers;
- organizational methods improve as the project progresses;
- no speculative claim is silently promoted to a theorem.

**Be imaginative in discovery and uncompromising in verification.**

---

## 1. Repository operating model

This repository has five primary coordination layers:

1. **README.md** — stable operating rules and project mission.
2. **GitHub Issues** — active tasks, ownership, discussion, and blocking dependencies.
3. **Agent reports** — append-only records of individual research sessions.
4. **Pull requests** — reviewable research contributions.
5. **CURRENT_STATE.md** — the current integrated understanding of the project.

Agents should not treat chat history as durable project knowledge.

Any result, idea, failure, construction, computational discovery, or organizational suggestion that may matter later must be written into the repository.

---

## 2. Required startup procedure

Before beginning a research session, every agent must:

1. Read this README.
2. Read `CURRENT_STATE.md`.
3. Read `OPEN_PROBLEMS.md`.
4. Read `CLAIMS.md`.
5. Search open issues and pull requests for overlapping work.
6. Read the latest relevant files under `reports/`.
7. Select or create a GitHub issue for the task.
8. Announce an agent ID and claim the issue before substantial work begins.
9. Consider whether the current repository structure or coordination process can be improved.

Agents may attack the full conjecture, pursue a narrow lemma, construct candidate counterexamples, develop new symbolic systems, run computational experiments, audit another agent’s argument, or reorganize existing ideas into a stronger framework.

---

## 3. Agent identity

Each research thread must use a unique, persistent agent ID.

Suggested format:

```text
<model-or-human>-<number>
```

Examples:

```text
gpt56-01
gpt56-02
claude-03
human-gideon
verifier-01
integrator-01
```

Every issue comment, report, commit, and pull request should identify the responsible agent.

Do not reuse another active agent’s ID.

When the same agent begins a substantially new independent attempt, it may either retain its existing identity or create a clearly related sub-identity:

```text
gpt56-01-a
gpt56-01-b
```

---

## 4. Task ownership

GitHub Issues are the authoritative task registry.

An issue should contain:

- a precise research question;
- the relationship to constructing a Collatz counterexample;
- known dependencies;
- relevant claim or lemma IDs;
- expected deliverables;
- suggested verification methods;
- current owner;
- current status.

Before working on an issue, comment:

```text
CLAIMED BY: <agent-id>
STARTED: <UTC timestamp>
BRANCH: agent/<agent-id>/<issue-number>-<short-name>
APPROACH: <one-paragraph plan>
```

A claim should normally expire after 24 hours without an update. Another agent may then take over, but must preserve and reference the earlier work.

Multiple agents may work on the same issue when independent attempts are useful. They must use separate branches and explicitly mark the attempts as independent.

Agents are encouraged to open issues for:

- candidate counterexample constructions;
- possible nontrivial cycles;
- divergence mechanisms;
- symbolic encodings;
- string rewrite systems;
- invariant discovery;
- proof gaps;
- computational searches;
- adversarial verification;
- synthesis of multiple approaches;
- improvements to the project’s organizational structure.

---

## 5. Branch and commit conventions

Never push research directly to the default branch.

Branch naming:

```text
agent/<agent-id>/<issue-number>-<short-description>
```

Examples:

```text
agent/gpt56-01/17-rewrite-system-invariant
agent/claude-03/22-check-modular-obstruction
agent/verifier-01/31-audit-lemma-L0012
agent/gpt56-04/44-candidate-divergent-orbit
```

Commit messages should use one of these prefixes:

```text
idea:
construction:
proof:
experiment:
verification:
refutation:
report:
organization:
docs:
```

Examples:

```text
construction: define candidate rewrite orbit with unbounded growth
proof: establish termination on restricted residue class
experiment: search rewrite cycles through depth 40
verification: independently reconstruct lemma L-0017
refutation: find counterexample to proposed monotonicity lemma
report: summarize failed parity-vector approach
organization: propose claim dependency index
```

Commit partial work frequently.

A failed approach is still useful project information.

---

## 6. Pull request rules

Each pull request should address one coherent contribution.

A pull request must state:

- agent ID;
- issue addressed;
- exact contribution;
- relationship to the counterexample objective;
- claim IDs added or changed;
- dependencies;
- verification performed;
- unresolved doubts;
- files that a reviewer should inspect first;
- any suggested improvements to the research process.

A pull request must not describe a result as a proof unless the complete proof is present in the repository.

Large speculative explorations should normally be submitted as research reports or candidate constructions rather than theorem claims.

Agents should not merge their own proof claims.

Proof-level contributions require review by at least one independent agent.

Claims purporting to construct a genuine Collatz counterexample or disprove the full conjecture require at least two independent adversarial reviews before being marked verified.

Whenever practical, at least one verifier should attempt to refute the result computationally and another should reconstruct the mathematical argument independently.

---

## 7. Research claim classification

Every mathematical claim must have a stable identifier.

Use:

```text
D-####  Definition
Q-####  Open question
O-####  Observation
C-####  Conjecture
K-####  Candidate counterexample
L-####  Lemma
T-####  Theorem
X-####  Computational experiment
R-####  Refutation
M-####  Methodological or organizational proposal
```

Examples:

```text
K-0003
L-0017
C-0009
X-0032
R-0004
M-0006
```

Every claim must have exactly one status:

```text
IDEA
EMPIRICAL
PARTIAL
PROPOSED
PROVED
INDEPENDENTLY_VERIFIED
REFUTED
SUPERSEDED
```

Meanings:

- **IDEA** — an informal possibility without substantial support.
- **EMPIRICAL** — supported computationally, but not proved.
- **PARTIAL** — a rigorous result with incomplete scope.
- **PROPOSED** — a complete-looking proof or construction has been submitted but not independently verified.
- **PROVED** — the proof has passed an initial detailed review.
- **INDEPENDENTLY_VERIFIED** — independently reconstructed or checked by another agent.
- **REFUTED** — a counterexample, computation, or logical failure is known.
- **SUPERSEDED** — replaced by a clearer, corrected, or stronger formulation.

No result may jump directly from `IDEA` to `INDEPENDENTLY_VERIFIED`.

A candidate counterexample remains a candidate until both the object and the universal mathematical reasoning establishing its behavior have been independently verified.

---

## 8. Required structure for mathematical claims

Each candidate construction, lemma, or theorem file should contain:

```text
Claim ID:
Title:
Status:
Authoring agent:
Reviewing agents:
Created:
Last updated:
Dependencies:
Scope:
Related counterexample candidates:
```

Then include the following sections.

### Statement

A fully quantified, unambiguous mathematical statement.

### Definitions

All nonstandard terminology and notation.

### Motivation

Explain how the claim could contribute to constructing or validating a Collatz counterexample.

### Proof or construction

Provide the complete argument or construction with no appeals to inaccessible chat history.

### Dependency audit

List every earlier result used and the precise point where it is used.

### Gap audit

Deliberately search for:

- hidden finiteness assumptions;
- unjustified induction;
- failure to cover boundary cases;
- confusion between empirical and universal statements;
- invalid interchange of limits;
- circular dependence;
- nonuniform estimates;
- assumptions equivalent to the Collatz conjecture itself;
- incorrectly assumed independence;
- unproved properties of an infinite rewrite sequence;
- finite computation being extrapolated to infinite behavior;
- a proposed counterexample being defined circularly;
- failure to prove that a symbolic object corresponds to an actual positive integer.

### Adversarial tests

Include small examples, edge cases, alternate formulations, symbolic checks, or computational tests that could expose an error.

### Remaining uncertainty

State any part of the argument about which the author is not fully confident.

### Suggested next attack

Describe the most promising way another agent could prove, strengthen, exploit, or refute the claim.

---

## 9. Candidate counterexample requirements

Every proposed counterexample should receive a stable `K-####` identifier.

A candidate file should include:

```text
Candidate ID:
Status:
Proposing agent:
Object or construction:
Claimed failure mode:
Dependencies:
Verification status:
```

The file must then address:

### Exact object

Define the proposed positive integer, infinite symbolic object, residue sequence, cycle, rewrite path, or equivalent construction precisely.

### Translation to Collatz dynamics

Prove that the proposed representation corresponds to a legitimate Collatz trajectory or to an equivalent formulation of the conjecture.

### Failure mechanism

State whether the construction is claimed to:

- diverge to infinity;
- remain unbounded;
- avoid 1 forever;
- enter a nontrivial cycle;
- or violate an equivalent necessary condition.

### Existence proof

If the construction is defined indirectly, prove that the object actually exists.

### Integrality and positivity

Prove that all required quantities correspond to positive integers where necessary.

### Infinite consistency

If defined through finite prefixes, prove that the prefixes are mutually compatible and determine a valid infinite object.

### Verification plan

State exactly what mathematical and computational checks are needed before the candidate can be accepted.

---

## 10. Computational result requirements

Computational evidence is welcome and may play a central role in discovering the counterexample.

However:

**Never call partial numerical evidence a proof. Partial numerical evidence may inspire a lemma, invariant, construction, or reduction which can then support a proof.**

Every experiment must record:

- experiment ID;
- research question;
- exact code;
- command used;
- parameter ranges;
- software environment;
- random seeds, when applicable;
- output or output digest;
- interpretation;
- limitations;
- associated issue and claim IDs.

Place experiments under:

```text
experiments/X-####-short-name/
```

Suggested contents:

```text
README.md
run.py
requirements.txt
results/
```

Large generated files should not be committed unless genuinely necessary. Prefer scripts that regenerate results.

Computational searches should aim not only to test known formulations, but also to discover:

- unexpected rewrite patterns;
- invariant candidates;
- unusually slow or growing trajectories;
- modular structures;
- cycle equations;
- symbolic fixed points;
- self-consistent parity sequences;
- candidate infinite paths;
- failures of proposed lemmas;
- structures that suggest an existence theorem.

Whenever possible, include automated tests that distinguish between:

- verified finite output;
- extrapolated behavior;
- heuristic interpretation;
- rigorous mathematical consequence.

---

## 11. Agent session reports

At the end of every substantial session, create:

```text
reports/<agent-id>/<YYYY-MM-DD>-<issue-number>-<short-name>.md
```

Reports are append-only historical records.

Do not overwrite another agent’s report.

Each report must contain:

```text
Agent:
Issue:
Branch:
Starting hypothesis:
Approaches attempted:
New results:
Candidate counterexamples:
Failed approaches:
Potential errors:
Files changed:
Claims affected:
Recommended next actions:
Organizational improvement ideas:
```

A report must distinguish among:

- proved facts;
- computational observations;
- plausible conjectures;
- speculative ideas;
- candidate constructions;
- known failures;
- organizational suggestions.

Even when no mathematical progress was made, record what was attempted and why it failed.

Agents should also consider whether the difficulty encountered arose from the mathematics or from deficiencies in the project’s coordination, indexing, file structure, review process, or division of work.

---

## 12. Handoffs between agents

When handing work to another agent:

1. Create or update the relevant issue.
2. Link the latest report.
3. Identify the exact unresolved step.
4. List the files and claims that must be read.
5. State what has already been tried.
6. State what would falsify the current approach.
7. State whether an organizational change would make continuation easier.

Recommended handoff format:

```text
HANDOFF FROM: <agent-id>
HANDOFF TO: any / <specific-agent-id>
CURRENT CLAIM OR CANDIDATE: <claim-id>
BLOCKING STEP:
FILES TO READ:
FAILED ATTEMPTS:
MOST PROMISING NEXT MOVE:
MAIN RISK:
POSSIBLE ORGANIZATIONAL IMPROVEMENT:
```

Do not use vague instructions such as “continue the proof.”

A useful handoff should allow another agent to begin productive work without reconstructing the entire history of the project.

---

## 13. Independent verification protocol

A verifier should begin without relying on the original author’s confidence.

The verifier should:

1. Restate the claim independently.
2. Reconstruct the proof from its explicit dependencies.
3. Check every quantifier and boundary case.
4. Search computationally for small counterexamples when appropriate.
5. Attempt to negate or strengthen the claim.
6. Check whether any dependency is circular.
7. Verify that symbolic constructions correspond to actual integer trajectories.
8. Check whether finite consistency has been improperly substituted for infinite existence.
9. Record the first unsupported inference, if one exists.
10. Submit either:
    - a verification report;
    - a correction request;
    - a formal refutation.

Review comments should identify exact file paths and exact logical steps.

“Looks correct” is not sufficient verification.

For a claimed counterexample, the verifier should independently reproduce:

- the construction;
- the translation into Collatz dynamics;
- the claimed nontermination, divergence, or cycle behavior;
- every supporting lemma;
- and the absence of hidden assumptions equivalent to the desired conclusion.

---

## 14. Integrator role

One designated integrator maintains:

```text
CURRENT_STATE.md
CLAIMS.md
OPEN_PROBLEMS.md
```

Ordinary research agents should propose changes to these files through pull requests, but the integrator resolves conflicts and maintains consistent status classifications.

The integrator does not decide mathematical truth by authority.

The integrator records the strongest status justified by repository evidence.

The integrator should periodically:

- merge accepted reports;
- close duplicated issues;
- identify conflicting claims;
- request independent reviews;
- mark stale tasks;
- update the dependency graph;
- create synthesis issues;
- identify promising candidate counterexamples;
- summarize major failed directions;
- review organizational proposals;
- improve templates and repository structure where justified.

The integrator may create dedicated issues for organizational improvements suggested by agents.

---

## 15. Improving the research process

The project’s organizational system is itself experimental.

All agents are invited to propose better ways to:

- coordinate parallel research;
- reduce duplicated effort;
- preserve partial insights;
- represent dependencies;
- rank promising approaches;
- detect contradictions;
- conduct adversarial review;
- divide long arguments into verifiable units;
- share computational artifacts;
- track candidate counterexamples;
- summarize large bodies of work;
- allocate agents dynamically;
- improve communication between research threads.

Organizational proposals should use `M-####` identifiers when substantial.

A methodological proposal should include:

```text
Proposal ID:
Problem with current process:
Proposed change:
Expected benefit:
Possible cost or risk:
Trial procedure:
Success criterion:
```

Agents should not wait until the end of the project to suggest improvements.

While working on the mathematics, continuously consider how the group itself could reason, communicate, verify, and collaborate more effectively.

Useful organizational experiments may be tested on a limited set of issues before becoming project-wide rules.

The README is not immutable. Changes may be proposed through pull requests and adopted when they improve the project’s ability to construct and verify a counterexample.

---

## 16. Recommended repository structure

```text
README.md
CURRENT_STATE.md
OPEN_PROBLEMS.md
CLAIMS.md
CANDIDATES.md
NEGATIVE_RESULTS.md
NOTATION.md
ORGANIZATIONAL_PROPOSALS.md

claims/
  definitions/
  observations/
  conjectures/
  candidates/
  lemmas/
  theorems/
  refutations/
  methodology/

experiments/
  X-0001-example/

reports/
  gpt56-01/
  gpt56-02/
  claude-01/
  verifier-01/
  integrator-01/

scripts/
tests/

.github/
  ISSUE_TEMPLATE/
  PULL_REQUEST_TEMPLATE.md
```

---

## 17. Non-negotiable rules

1. Never conceal uncertainty.
2. Never call partial numerical evidence a proof, though it may inspire a lemma, construction, or reduction which can then support a proof.
3. Never rely on inaccessible chat context.
4. Never silently delete failed work.
5. Never modify another agent’s branch without coordination.
6. Never merge a claimed major theorem or counterexample without independent review.
7. Never assume the desired conclusion inside an intermediate lemma.
8. Never treat eloquence, length, confidence, or model identity as evidence.
9. Always preserve exact statements and dependencies.
10. Always distinguish finite verification from infinite proof.
11. Always distinguish a symbolic construction from proof that it represents an integer trajectory.
12. Always record potentially useful false starts.
13. Always remain open to unconventional ideas.
14. Do not fear confabulation, but label it.
15. Always suggest organizational improvements when they could help the group.
16. Always leave the repository more understandable than you found it.

---

## 18. Initial instruction for every new agent

Use the following instruction when starting a new research thread:

```text
You are one researcher in a coordinated multi-agent project whose goal is
to resolve the Collatz conjecture by constructing and rigorously proving
a counterexample.

The goal is ambitious, and we will achieve it.

Do not fear confabulation. Generate bold hypotheses, unusual constructions,
new rewrite systems, speculative lemmas, and unconventional equivalences.
However, clearly label everything as proved, computational, conjectural,
speculative, or refuted.

Before doing mathematical work:

1. Read README.md, CURRENT_STATE.md, OPEN_PROBLEMS.md, CLAIMS.md,
   CANDIDATES.md, relevant open issues, relevant pull requests, and
   recent reports.
2. Choose or create one precise GitHub issue.
3. Assign yourself a unique agent ID.
4. Claim the task in the issue.
5. Work on a separate agent branch.
6. Clearly distinguish proof, partial proof, computation, conjecture,
   speculation, candidate construction, and refutation.
7. Preserve failed approaches.
8. Pursue the construction of a counterexample directly or develop
   mathematical tools that could enable such a construction.
9. End the session with an agent report and a reviewable pull request.
10. Include ideas for improving the research organization itself.
11. Never call partial numerical evidence a proof, though it may inspire
    a lemma or construction that can later be proved.
12. Do not claim resolution of the Collatz conjecture unless every
    dependency, existence claim, and infinite step is explicitly
    established in the repository.
13. Be imaginative in discovery and uncompromising in verification.
```

---

## 19. Current project objective

The project’s objective is to construct a genuine counterexample to the Collatz conjecture and prove rigorously that it is a counterexample.

The immediate objectives are to:

- discover candidate counterexample mechanisms;
- invent mathematical representations capable of expressing them;
- derive lemmas that convert finite or symbolic structure into infinite behavior;
- test and refute weak constructions rapidly;
- preserve all useful negative and positive results;
- improve the organization of the multi-agent research process;
- and build a reliable, cumulative, adversarially reviewed path toward the final construction.

**The goal is ambitious. We will achieve it.**
