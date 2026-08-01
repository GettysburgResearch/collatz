# Compute Policy

## Purpose

Computation is central to discovery and verification.

GitHub Actions is not an open-ended distributed mathematics compute service.

## Pilot before scaling

Before launching a large search, solver campaign, or cloud job:

1. run a small representative instance;
2. measure runtime and memory;
3. validate the output format and independent checker;
4. estimate the full resource cost;
5. add checkpoints, logs, and explicit stopping conditions;
6. only then scale up.

A small pilot should be preserved when it reveals complexity, correctness, or
interpretation problems relevant to the full run.

## Allowed CI work

- schema validation;
- link and Markdown checks;
- unit tests;
- small deterministic experiment replays;
- certificate verification;
- checksum validation;
- Lean builds;
- no-`sorry` checks;
- generated-state consistency checks.

## Work that should run elsewhere

- broad candidate searches;
- large parameter sweeps;
- long solver campaigns;
- distributed residue enumeration;
- large matrix or number-theory computation;
- model inference;
- exploratory jobs with unknown termination.

These may run on contributor-controlled or explicitly funded infrastructure,
including other cloud agents and compute services.

Return:

- exact code;
- command;
- environment;
- parameters;
- seed;
- manifest;
- checksum;
- certificate;
- independent verifier;
- stated resource use.

## GitHub Actions defaults

Every workflow should use:

```yaml
permissions:
  contents: read
```

Every job should have:

```yaml
timeout-minutes: <small explicit value>
```

Expensive duplicate runs should use concurrency cancellation.

Do not permit GitHub Actions to approve pull requests.

## Public fork safety

Use ordinary `pull_request` workflows for untrusted fork code.

Do not combine privileged tokens or secrets with execution of code fetched from
a public pull request.

Treat downloaded artifacts from untrusted workflows as untrusted data.

## Resource-abuse prevention

The repository may reject or disable workflows that:

- launch open-ended searches;
- evade timeouts;
- split one large search into many CI jobs;
- use scheduled jobs for discovery compute;
- mine unrelated resources;
- execute opaque binaries;
- contact unexplained external services.

This policy limits infrastructure use, not mathematical ambition.
