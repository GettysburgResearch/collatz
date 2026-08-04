# O-8802 — Known-frontier identification

Claim ID: O-8802  
Title: The remaining `5/4` chart question is exactly a two-residue approximate-multiplication and rational-base minimal-word problem  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8806, T-8803  
Scope: literature positioning of the unresolved global existence question  
Related counterexample candidates: issue #26; no `K-####` candidate

## Observation

The global question left by T-8806 is not an isolated repository invention.
It is the specialization

```text
p=5,
q=4,
S={0,3}
```

of the approximate-multiplication map introduced by Dubickas and Mossinghoff:

```text
x -> ceil(p*x/q)  if x mod q is in S,
     STOP         otherwise.                         (1)
```

Their 2009 paper explicitly proposes termination for all positive starts, proves
the singleton-`S` case, and identifies the family

```text
p=q+1,
S={0,q-1}
```

as a natural first two-residue target. The exact PR #35 bottom map is the case
`q=4`:

```text
x -> ceil(5x/4) while x mod 4 is in {0,3}.            (2)
```

Independently, (2) is the minimal or bottom path from the nonempty seed `x` in
the rational-base `5/4` representation tree. Its edge labels are precisely

```text
b(tau^j(x))=(-tau^j(x)) mod 4 in {0,1,2,3}.
```

Therefore an infinite chart survivor is exactly a nonempty-seed minimal word in
base `5/4` that omits both letters `2` and `3`.

## Current literature boundary

Andrieu, Eliahou, and Vivion conjecture that every nonempty-seed minimal word in
base `p/q` is normal over `{0,...,q-1}`. In base `5/4`, that conjecture would
force every digit `0,1,2,3` to occur with frequency `1/4`; it therefore implies
that every orbit (2) eventually stops.

The full normality conjecture is much stronger than required here. The exact
weak statement needed to close PR #35 is only:

> Every nonempty-seed base-`5/4` minimal word contains at least one occurrence
> of digit `2` or `3`.

The same 2026 paper records the known complexity theorem of Dubickas:

```text
liminf p_w(ell)/ell >= log(q)/log(p/q)               (3)
```

for every rational-base minimal word. At `p/q=5/4`, the right side is

```text
log(4)/log(5/4)
  =1/(log_4(5)-1),
```

exactly the constant reconstructed independently in T-8803. Thus the
specialized complexity slope is known mathematics; the contribution of T-8803
is its self-contained ordinary-section proof, exact finite repeated-factor
inequality, and integration with the physical `5x+1` chart.

## Why this matters

The repository should not advertise the remaining step as though a routine SAT
run or one more height inequality were expected to finish it. A complete global
termination theorem for (2) would resolve a named two-residue instance of a
longstanding approximate-multiplication program and prove a nontrivial special
case of the weak digit-richness consequences anticipated by current
rational-base normality research.

Conversely, one infinite low-digit root would refute that termination instance
and provide a rigorously divergent positive `5x+1` orbit inside the exact chart.

## Source audit

### Dubickas–Mossinghoff, 2009

`Lower bounds for Z-numbers`, Mathematics of Computation 78 (2009), 1837–1851,
DOI `10.1090/S0025-5718-09-02211-X`.

Load-bearing points checked in the full text:

- definition of the approximate multiplication map (1);
- statement of the general termination question;
- identification of `p=q+1, S={0,q-1}`;
- Proposition 3.2 proving termination when `|S|=1`.

### Andrieu–Eliahou–Vivion, 2026 revision

`A Normality Conjecture on Rational Base Number Systems`, arXiv `2510.11723v2`.

Load-bearing points checked:

- definition of minimal words as paths taking the smallest available edge;
- Conjecture 1.2, normality of every nonempty-seed minimal word over
  `{0,...,q-1}`;
- attribution of the linear complexity lower bound (3);
- explicit statement that normality would imply the Dubickas–Mossinghoff
  Collatz-like termination conjecture.

### Akiyama–Marsault–Sakarovitch, 2018

`On subtrees of the representation tree in rational base numeration systems`,
DMTCS 20:1, DOI `10.23638/DMTCS-20-1-10`.

This is contextual support for bottom words, subtrees, and successor
transducers. No theorem from it is used in the proofs of T-8806 or L-8804.

## Classification boundary

This file is a literature observation, not a proof that the problem is open in
every conceivable equivalent formulation. It records that the exact target is a
special case of explicitly posed conjectural programs and that no located source
supplies the missing global theorem.

## Suggested next attack

Work below full normality. The weakest decisive theorem is eventual occurrence
of one forbidden digit. Candidate intermediate targets are:

1. unbounded richness threshold for the pair `{2,3}`;
2. a modular obstruction to an all-`{0,1}` minimal word;
3. a recursive lower bound forcing the exact minima from L-8804 to infinity;
4. a discrepancy theorem strong only for the union of residue classes `1,2 mod4`.
