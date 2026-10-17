# L-8307 — A three-state weighted transducer compiles the full greedy repair grammar

Claim ID: `L-8307`  
Status: `PROPOSED / EXACT COMPRESSED-CIRCUIT LEMMA`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8304`, `L-8305`, `L-8306`  
Scope: the complete lower critical mechanical run word and its canonical left-to-right maximal family of pairwise-disjoint unequal neighboring-run transpositions  
Related counterexample candidates: none

## 1. Canonical full-word repair family

Let

```text
ell = 267,629,447,755,
r   = 236,838,463,643
```

and let `w=L(r,ell)` be the lower binary mechanical run word from `L-8304`.

Scan `w` from left to right.  Whenever the current and next run symbols differ and neither belongs to the previously selected pair, select that unequal pair and skip its second symbol as a possible start.  This produces the canonical maximal family of pairwise-disjoint unequal neighboring-run sites.

At every selected site we may either retain or transpose the two runs.  The choices are independent because the sites are disjoint.

The first three selected sites begin at positions

```text
0, 7, 15.
```

## 2. Prefix weight of a transposition

For a prefix of `n` run symbols, put

\[
s_n=\left\lfloor {nr\over\ell}\right\rfloor,
\tag{1}
\]

\[
E_n=16n+3s_n,
\qquad
P_n=5n+s_n.
\tag{2}
\]

`L-8305` gives the exact numerator delta at a selected site beginning at `n`:

\[
\boxed{
\Delta_n
=\operatorname{sgn}(w_n,w_{n+1})
\,\Omega\,2^{E_n}3^{k-2(P_n+11)},}
\tag{3}
\]

where

\[
\Omega=7\,2^{16}3^9
\]

and the sign is negative for `01 -> 10` and positive for `10 -> 01`.

For the normalized real fixed point, factor out the common constant

\[
K_*={3^k\over2^A}{\Omega\over9^{11}}.
\tag{4}
\]

The remaining site weight is

\[
\boxed{z_n={2^{E_n}\over9^{P_n}}.}
\tag{5}
\]

Reading one run symbol `b in {0,1}` multiplies the current prefix weight by

\[
g_b={2^{16+3b}\over9^{5+b}}.
\tag{6}
\]

## 3. Greedy-site automaton

Use three states:

```text
E   no pending free symbol,
F0  one pending free symbol 0,
F1  one pending free symbol 1.
```

When a symbol `b` is read:

- `E -> Fb`, with no selected site;
- `Fb -> Fb`, with no selected site;
- `F0 --1--> E`, selecting a negative `01` site;
- `F1 --0--> E`, selecting a positive `10` site.

The return to `E` after a selection is exactly the nonoverlap rule: the second symbol of the selected pair is consumed and cannot begin the next pair.

If the current prefix weight immediately before the newly read symbol is `z`, then a selection from `F0` contributes `z/g_0`, while a selection from `F1` contributes `z/g_1`.  Those are precisely the weights `(5)` immediately before the pending symbol.

## 4. Weighted transition monoid

A finite word `u` has the summary

\[
\mathcal S(u)=
\bigl(G_u,\tau_u,H^+_u,H^-_u,C_u\bigr),
\tag{7}
\]

where:

- `G_u` is the product of the prefix multipliers `(6)`;
- `tau_u` is the deterministic map on the three automaton states;
- `H^+_u(s)` is the total positive selected-site weight when `u` begins in state `s` with initial prefix weight one;
- `H^-_u(s)` is the corresponding absolute negative weight;
- `C_u(s)` is the number of selected sites.

For chronological concatenation `uv`, the exact composition law is

\[
G_{uv}=G_uG_v,
\tag{8}
\]

\[
\tau_{uv}(s)=\tau_v(\tau_u(s)),
\tag{9}
\]

\[
H^{\pm}_{uv}(s)
=H^{\pm}_u(s)+G_uH^{\pm}_v(\tau_u(s)),
\tag{10}
\]

\[
C_{uv}(s)=C_u(s)+C_v(\tau_u(s)).
\tag{11}
\]

These equations are associative, so the summaries form a finite-dimensional noncommutative monoid.

## 5. Euclidean mechanical compilation

Apply the lower/upper Euclidean recursion of branch-qualified `PR45/L-8403` to the two one-letter summaries.  Equations `(8)`--`(11)` evaluate the complete `ell`-symbol word in `O(log ell)` recursive levels without expanding it.

Starting in state `E`, the exact canonical site count is

\[
\boxed{30\,790\,984\,112.}
\tag{12}
\]

Hence the complete canonical disjoint repair grammar contains

\[
\boxed{2^{30\,790\,984\,112}}
\tag{13}
\]

valid critical words.

The same evaluation gives the exact directed positive and negative weight sums

\[
H^+=H^+_w(E),
\qquad
H^-=H^-_w(E).
\tag{14}
\]

If `C_0/D` is the unmodified fixed point, every word in the full grammar lies in

\[
\boxed{
\left[
{C_0\over D}-{K_*H^-\over1-3^k/2^A},
{C_0\over D}+{K_*H^+\over1-3^k/2^A}
\right].}
\tag{15}
\]

This is the complete real envelope of the grammar, not a union bound over a finite prefix of the site list.

## 6. Proof

The automaton rules are exactly the greedy left-to-right nonoverlap scan.  The prefix multiplier `(6)` follows from `(2)`: appending symbol `b` increments `(E,P)` by `(16+3b,5+b)`.  When a pair closes, division by `g_b` moves from the weight before the second symbol to the weight before the pending first symbol, giving `(5)`.

For concatenation, the second word starts with prefix weight multiplied by `G_u` and in state `tau_u(s)`.  This gives `(8)`--`(11)` directly.  Induction proves the summary for every finite word.  The Euclidean mechanical recursion is an identity in every associative monoid, so it applies to `(7)`.  Substitution of `(3)`--`(5)` gives the full envelope `(15)`. **QED**

## 7. Computational audit

`X-8305` has two independent implementations of the summary monoid.  Both reconstruct:

```text
first sites: 0,7,15;
site count: 30,790,984,112;
third delta valuation: 295;
full directed repair envelope.
```

The verifier imports no author module.

## 8. Gap audit

- The canonical family is maximal for its greedy scan, not the set of every possible matching of unequal neighbors.
- Overlapping transpositions and hierarchical Farey block replacements lie outside the grammar.
- The envelope `(15)` alone does not imply integrality or nonintegrality.
- No positive cycle or divergent orbit is asserted here.

## 9. Suggested next attack

Combine `(15)` with `L-8306`: the first two repair digits fix the quotient modulo `2^295`, while the weighted transducer bounds every possible later repair in one exact real interval.  This decides the entire grammar at the ordinary equation rather than at a sampled denominator factor.
