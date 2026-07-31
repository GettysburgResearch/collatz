# Human Guide to Participating and Steering AI Research

This guide is for the humans directing ChatGPT, Claude, Cursor, Codex, and other
research agents. The main README is the agent-facing operating protocol.

## Quick start

1. Create a GitHub account.
2. Connect GitHub to one or more AI applications.
3. Open this repository or a relevant Issue in the application.
4. Give the agent a starter prompt and let it choose its own persistent agent ID.
5. Ensure that useful work is committed, pushed, or recorded in an Issue or PR
   before the session ends.

Setup links will be added here:

- ChatGPT / Codex: `[SETUP LINK TO BE ADDED]`
- Claude: `[SETUP LINK TO BE ADDED]`
- Cursor: `[SETUP LINK TO BE ADDED]`
- Other supported tools: `[LINKS TO BE ADDED]`

For direct repository access, use the short access-request Issue and provide only
your GitHub username. See [../CONTRIBUTING.md](../CONTRIBUTING.md).

## Contributing from a phone

After GitHub is connected, much of the workflow can be directed from a phone:

1. open the repository, an Issue, or a PR in the AI application;
2. ask the agent to read the README and the most relevant repository context;
3. ask it to choose or continue a research direction;
4. let it investigate mathematics, literature, computation, verification, or
   organization;
5. ask it to preserve the result in GitHub;
6. review consequential writes before accepting them.

A phone session may produce a proof draft, correction, computation, literature
map, review, dashboard, Issue comment, report, or PR extension.

## Starter prompts

### General contribution

```text
You are the latest contributor to GettysburgResearch/collatz, Agentic Polymath
#1. Read the README, current state, relevant Issues, pull requests, claims, and
recent reports. Choose or continue a useful research direction toward proving or
disproving Collatz. Work ambitiously, label uncertainty, treat known open
problems as literature connections rather than stop signs, choose a unique agent
ID, and preserve all useful work in GitHub.
```

### Literature

```text
Search for literature directly relevant to the repository's active claims.
Reconstruct exact standalone theorems, hypotheses, normalizations, and citations.
Distinguish exact prior results, analogies, and new repository consequences.
Then attempt to use the literature to advance or refute an active direction
rather than stopping because the boundary is open.
```

### Verification and cartography

```text
Act as an adversarial verifier and research cartographer. Freeze exact source
SHAs, reconstruct claims independently, identify the first unsupported
inference, compare overlapping branches, preserve neutral non-reproduction, and
leave a durable review, dependency map, dashboard, or corrected packet.
```

### Complete the repository write

```text
Finish every pending repository action now. Commit the intended files, push the
branch, update or open the pull request, and verify the exact branch and PR head
SHA. Do not stop at a draft in chat or merely describe what should be pushed.
```

Models sometimes complete the mathematical work but fail to finish GitHub writes
because a tool window closes, permissions change, or the session shifts context.
Do not assume the work is public until the agent reports an exact commit SHA or a
verifiable Issue/PR update.

In ChatGPT, explicitly mentioning `@GitHub` can sometimes help route the request
back to the connected GitHub tool when repository access unexpectedly appears
read-only. Availability depends on the connected environment.

## Discussions and the durable record

GitHub Discussions may be used by humans for broad conversation. Many agent
GitHub integrations do not expose Discussions, so any actionable outcome must
also be mirrored into an Issue, pull request, report, or repository file.

Private chat is not the project record. A useful result must be made discoverable
to later humans and models.

## What agents can usefully do

Agents can:

- attack the full conjecture directly;
- develop proof-side or disproof-side programs;
- reconstruct literature;
- extract standalone theorems;
- verify or refute claims;
- search for small counterexamples;
- run exact computations;
- build independent checkers;
- formalize stable statements;
- compare branches;
- construct dependency maps and dashboards;
- identify repeated circularity;
- improve repository organization.

Other cloud agents and compute environments can be especially useful for
experiments. Their outputs should be returned as exact code, parameters,
manifests, hashes, certificates, and compact checkers so stronger reasoning
models can interpret and use them.

## Start computations small

Before launching a full search or solver campaign:

1. run a small representative instance;
2. measure runtime and memory;
3. verify the output format and checker;
4. estimate the full cost;
5. add checkpoints and explicit stopping conditions;
6. only then scale up.

A small pilot often exposes a mistaken complexity estimate, data-format problem,
or invalid interpretation before substantial compute is spent.

## Supplying inaccessible papers

An agent may know that a paper exists but be unable to access its full text. You
may supply a legally obtained paper, relevant pages, theorem statement, or
permitted excerpt directly to the chat.

Tell the agent explicitly that this is an option. Ask it to:

- quote or identify the exact theorem used;
- record theorem number, page, edition, and hypotheses;
- distinguish the paper's theorem from the repository's new consequence;
- avoid uploading copyrighted material to GitHub unless redistribution is
  permitted.

## Choosing models and run length

Use the strongest reliable reasoning mode available when the task is genuinely
mathematical.

In this project's experience so far, long GPT Pro research runs—often around an
hour—have been substantially more reliable for sustained mathematical
development and for finding consistent gaps in claims produced by Fable and
Claude Opus. The reverse pattern has been less common.

This is a project observation, not a controlled benchmark. The comparison is
confounded by run length because other agents often run for much less time.
Record the model, mode, approximate run duration, context, tools, and whether the
result was independently checked.

Shorter or less reliable agents can still contribute valuable computations,
literature leads, examples, counterexamples, formalization attempts, and
alternative viewpoints for stronger agents to digest.

## Do not let the target silently shrink

Across a long session, an agent may replace the original global target with a
nearby weaker result and then present that result as completion.

Restate the full remaining target when necessary:

```text
Return to the exact full target stated below. Do not replace it with a weaker
conditional, finite-prefix, approximate, proper-factor, or reformulated result.
State explicitly whether every step needed for the full target is now proved.
If not, identify the first remaining unsupported inference and continue working
on that inference.

FULL TARGET:
<insert the exact target>
```

Ask the agent to compare its claimed result line by line with the original target.

## Do not over-steer too early

A broad new idea often needs room. Allow an agent to build definitions, test
examples, search remote literature, run exploratory code, and discover why a
route succeeds or fails.

Intervene when the work repeatedly returns to the same unresolved implication
without acknowledging it.

## Signs of a circular loop

- each pass creates a new encoding of the same compatibility problem;
- increasingly long finite witnesses are presented without one ordinary infinite
  witness;
- the agent proves more consequences conditioned on existence;
- the same global blocker reappears under new notation;
- a proper denominator factor is repeatedly substituted for full cycle closure;
- a known open problem is rediscovered and treated as the end;
- the agent repeatedly says “we are close” without a stronger implication;
- computation grows while the logical gap stays fixed.

## Gentle blocker audit

```text
Pause the current development and perform a blocker audit.

State:
1. the exact final target;
2. the first unsupported inference;
3. what changed mathematically in the last three passes;
4. whether the current target is weaker than Collatz, equivalent to it, or
   stronger;
5. what exhaustive class a negative result would eliminate;
6. what explicit candidate a positive result would produce.

Do not introduce a new formalism in this pass unless it directly changes one of
those implications. Try to refute the current route before continuing it.
```

## Strong blocker audit

```text
Stop extending finite-prefix, conditional-growth, or encoding machinery.

Choose one global blocker:
- ordinary-integer extraction;
- all-time legality of one explicit seed;
- full-denominator divisibility;
- exact physical replay;
- an exhaustive architecture-level exclusion.

Either supply the missing inference or prove that the current architecture
cannot supply it. Preserve all valid partial results, but do not call another
equivalent reformulation progress toward the final objective.
```

## Open-problem continuation

```text
The fact that the target is a known open problem is context, not a stop signal.
Record the exact literature boundary and continue the attempt.

Do not claim the result is known.
Do not refuse merely because it would be significant.
Try a new proof, disproof, reduction, computation, or formalization, and state
your uncertainty honestly.
```

## Adversarial role switch

```text
For this pass, act as a hostile verifier.

Assume the previous author may have hidden:
- a quantifier swap;
- a finite-to-infinite leap;
- a 2-adic/ordinary confusion;
- a denominator gap;
- a source-normalization error;
- a circular dependency.

Find the first invalid inference or independently reconstruct the chain.
```

## When to redirect or archive

Redirect when a route produced reusable lemmas, eliminated a meaningful class,
created a verifiable certificate, exposed an exact blocker, or suggested a new
method.

Archive as inactive when no new implication appears across several documented
passes, a premise is refuted, the route is subsumed, or a required source theorem
does not say what the program assumed.

Archiving is not deletion and not a declaration that a direction can never work.

## Encourage organizational insight

Ask occasionally:

```text
What repository or coordination change would have made this work easier to
verify, continue, compare, or refute?
```

A dependency map, clearer state document, compact checker, better task split, or
warning about a recurring model failure may be a high-value contribution.
