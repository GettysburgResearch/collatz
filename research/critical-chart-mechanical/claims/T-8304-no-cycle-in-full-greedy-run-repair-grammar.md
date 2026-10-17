# T-8304 — The full critical greedy run-repair grammar contains no integral cycle

Claim ID: `T-8304`  
Status: `PROPOSED / COMPUTER-ASSISTED EXACT THEOREM`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8305`, `L-8306`, `L-8307`; exact experiment `X-8305`  
Scope: every subset of the complete canonical greedy family of disjoint unequal neighboring-run transpositions in the lower critical mechanical run word  
Related counterexample candidates: none

## 1. Complete grammar

Use the lower critical run word

```text
length = 267,629,447,755,
weight = 236,838,463,643,
```

at

```text
k = 3,149,971,404,836,
A = 4,992,586,555,009.
```

`L-8307` proves that the canonical left-to-right greedy nonoverlap scan contains exactly

\[
S=30\,790\,984\,112
\tag{1}
\]

unequal neighboring-run sites.  Every subset is a valid word with the same complete denominator

\[
D=2^A-3^k>0.
\tag{2}
\]

Thus the theorem decides a grammar of cardinality

\[
\boxed{2^{30\,790\,984\,112}.}
\tag{3}
\]

## 2. First two repair digits

The first three canonical sites begin at run positions

```text
0, 7, 15.
```

By `L-8305`, their exact numerator-delta valuations are

```text
16, 146, 295.
```

Therefore, after the first two site choices have been fixed, every remaining one of the more than thirty billion repair digits is divisible by

\[
\boxed{2^{295}.}
\tag{4}
\]

For each two-bit mask `mu`, let

\[
r_\mu
\equiv
(C_0+\mu_0\Delta_0+\mu_1\Delta_1)D^{-1}
\pmod {2^{295}},
\tag{5}
\]

with the representative in `[0,2^295)`.  The four residues are distinct.  Any integral fixed point extending mask `mu` must be congruent to `r_mu` modulo `2^295`.

## 3. Exact full-grammar real envelope

`L-8307` compiles the entire greedy scan by a three-state weighted transducer.  Let `H^+` and `H^-` be its complete positive and negative repair-weight sums.  Every fixed point in the grammar lies in the directed interval

\[
I_{\rm full}
=
\left[
{C_0\over D}-{K_*H^-\over1-3^k/2^A},
{C_0\over D}+{K_*H^+\over1-3^k/2^A}
\right],
\tag{6}
\]

where

\[
K_*={3^k\over2^A}{7\,2^{16}3^9\over9^{11}}.
\]

The interval is not a truncation and not a statistical estimate: it contains every one of the `2^S` exact words.

`X-8305` evaluates `(6)` with outward rounding and certifies

```text
I_full is positive,
I_full contains ordinary integers,
sup(I_full) < 2^295.
```

Hence an ordinary integer in a residue class modulo `2^295` belongs to `I_full` exactly when its canonical representative does.

## 4. Empty quotient-cylinder intersection

The exact modular compiler in `X-8305` reconstructs the four residues `(5)`.  It then verifies

\[
\boxed{
\{r_0,r_1,r_2,r_3\}
\cap
(\mathbf Z\cap I_{\rm full})
=\varnothing.}
\tag{7}
\]

Later repair choices cannot alter `(5)` by `(4)`.  Therefore no word in the complete grammar can satisfy `C=ND` for an ordinary integer `N`.

### Theorem

\[
\boxed{
D\nmid C(w)
\quad
\text{for every word }w\text{ in the full canonical greedy repair grammar}.}
\tag{8}
\]

Consequently this grammar contains no positive accelerated Collatz cycle.

## 5. Independent replay

The author implementation and a separately written verifier each reconstruct:

- the Euclidean mechanical word;
- the three-state greedy-site transducer;
- the exact site count `(1)`;
- the complete interval `(6)`;
- the first sites and valuations;
- the four quotient residues modulo `2^295`;
- the empty intersection `(7)`.

The verifier imports no author module.

```bash
python3 -B experiments/X-8305-full-greedy-repair-transducer/run.py \
  --check-results \
  experiments/X-8305-full-greedy-repair-transducer/results/canonical.json

python3 -B experiments/X-8305-full-greedy-repair-transducer/verify.py \
  experiments/X-8305-full-greedy-repair-transducer/results/canonical.json
```

## 6. Why this matters

The initial PR #45 and paired-chart attempts repaired one 61-bit denominator component with 43, 41, or 46 selected swaps.  `T-8303` then decided the declared 80-site ambient family.

The present theorem removes the finite-site cutoff completely for the canonical greedy matching.  More than thirty billion independent repair digits are compressed into one exact transducer, yet two low dyadic digits and one complete real envelope already refute every ordinary quotient.

This is a decisive methodological result:

> For ordered critical repairs, complete-denominator ordinary compatibility can be much cheaper than modular subset search.

## 7. Honest boundary

The theorem does **not** exclude:

- a different maximal matching of unequal neighbors;
- overlapping transpositions;
- hierarchical Farey block interchanges;
- replacements changing run counts or the critical shape;
- arbitrary compressed primitive words;
- an infinite ordinary path in the expanding negative-cycle chart;
- a Collatz counterexample in general.

No `K-83xx` identifier is assigned.

## 8. Constructive next move

The surviving attack is the hierarchical Farey tree.  Unlike the greedy local grammar, it can alter the first unresolved quotient digits at multiple Euclidean scales.  Apply `L-8306` to that tree, carrying the real ordinary quotient and the complete residual simultaneously.  Any terminal zero is a finite unconditional Collatz counterexample; an empty tree is a new exact grammar theorem.
