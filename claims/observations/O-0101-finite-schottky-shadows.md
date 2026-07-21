# O-0101 — Finite Schottky shadows exist; infinite mild walks not found

Claim ID: `O-0101`  
Title: Finite expanding block shadows and empirical death of mild greedy walks  
Status: `EMPIRICAL`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`, `D-0102`, `L-0104`  
Scope: computational searches in `X-0101`–`X-0107`  
Related counterexample candidates: none

## Statement

The following were observed with exact integer arithmetic:

1. **Affine census (`X-0101`, \(L\le14\)):** \(32766\) words, \(6333\) supercritical,
   \(2434\) mild with \(\mu\le 3/2\). Smallest \(\log\mu\) among supercritical words
   occurs at the \(7/11\) convergent class \(\mu=2187/2048\).

2. **Positive-interval real Schottky (`X-0102`):** \(0\) hits; matches `L-0101`.

3. **Infinity-chart Schottky (`X-0104`):** \(0\) hits; matches `L-0102`.

4. **Concrete finite alternators (`X-0105`):** seeds such as
   \(n_0=4095\) with block schedule \((1,11)\) grow for a few rounds then fail
   residue compatibility (failure at round \(8\) when extended).

5. **Mild greedy walks (library \(L\le8\), \(\mu\in(1,3/2]\), \(n_0\le3000\)):**
   - depth \(5\): \(316/3000\) survivors,
   - depth \(10\): \(35/3000\),
   - depth \(15\): \(8/3000\) (all die by depth \(20\)),
   - depth \(20+\): \(0/3000\).

6. **Symbolic expanding block cycle (`X-0106`):**
   \(w_1=1111010\), \(w_2=1101110\), product \(\mu=59049/16384>1\), with a
   modular handshake \(47\to91\to175\). Exact lifting shows at most \(2\)
   concatenated periods on tested seeds; explained by `L-0104`.

7. **Syracuse modular ping-pong (`X-0107`, mod \(27\)):** \(0\) disjoint
   expanding-valuation residue sets; expanding Syracuse cycles found
   symbolically but \(0\) odd-integer lifts of periodic \(k\)-schedules in the
   searched range.

## Motivation

Separates useful finite phenomena from infinite certificates. Prevents later
agents from rediscovering the same finite shadows as purported counterexamples.

## Proof or construction

Computational; scripts and digests under `experiments/X-0101-…` through
`X-0107-…`.

## Dependency audit

- Scripts cited above.
- Interpretive link to `L-0104` for item 6.

## Gap audit

- Bounds are finite; not a nonexistence proof for all Schottky automata.
- Mild library and depth bounds are parameters, not intrinsic constants.

## Adversarial tests

Re-run each `run.py`. All use only the Python standard library.

## Remaining uncertainty

Whether a larger block library, mixed subcritical repairs with a Lyapunov
window, or complementary-domain Möbius ping-pong can escape these deaths.

## Suggested next attack

Prove a general precision-drain lemma (`C-0102`) and/or build an automaton
that sometimes uses subcritical bridges while keeping a global height
Lyapunov function unbounded on an aperiodic language.
