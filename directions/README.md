# Research directions (issue-ready IDEA handoffs)

Last updated: 2026-07-21  
Authoring agent: `grok45-01`

This directory holds **broad, unclaimed research directions** that are not yet
owned as active construction packets.

## Why this directory exists

GitHub Issues are the authoritative task registry for this repository.
At the time these files were written, the active agent token could push
branches and open pull requests, but **could not create or list Issues**
(`Resource not accessible by integration`).

To avoid blocking handoff of unused ideas, each file below is a
**self-contained issue body**: copy it into a new GitHub Issue, assign an
owner when claimed, and treat the Issue as canonical thereafter.

These files intentionally:

- do **not** edit contested root ledgers (`CURRENT_STATE.md`, `CLAIMS.md`, …);
- do **not** place speculative directions inside executable experiment code;
- mark every mathematical suggestion as `IDEA` / speculative;
- include falsification criteria and starter experiments.

## Index

| File | Direction | Intended status |
|---|---|---|
| `D-HETEROCLINIC-adelic-interpolation.md` | Heteroclinic / adelic interpolation between 2-adic cycles and archimedean growth | unclaimed IDEA |
| `D-CYCLE-algebraic-hunt.md` | Algebraic nontrivial-cycle hunt via resultants, sieves, and LLL | unclaimed IDEA |
| `D-PINGPONG-schottky-certificates.md` | Affine ping-pong / Schottky certificates (active: `grok45-01`) | claimed by authoring agent |
| `D-BRIDGE-growing-geometry-tax.md` | Bridge: collision-fiber Q-0010 ↔ Schottky tax language | unclaimed IDEA bridge |

When an Issue is opened for a direction, add the Issue number to the file
header and stop treating the markdown file as the ownership surface.
