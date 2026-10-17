# L-0039 — Complete low-bit projection is not source orientation

Claim ID: `L-0039`  
Title: A complete correction alphabet still occupies only one full source cylinder inside each low-bit cell  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-25  
Dependencies: `L-0001`, `L-0005`; applications use `T-0041`, `T-0042`  
Scope: every finite family of fixed-length shortcut-Collatz parity branches  
Related counterexample candidates: none

## Statement

Let

\[
\mathcal W=\{w_x:x\in X\}
\]

be distinct parity words of one common length `L`.  Each word determines one
source residue

\[
\rho_x\pmod {2^L}
\]

on which that exact parity block occurs.

Assume that `X` has cardinality `2^b`, with `b<=L`, and that the branch roots
have complete low-bit projection:

\[
\boxed{
\{\rho_x\bmod2^b:x\in X\}
=\mathbb Z/2^b\mathbb Z.}
\tag{1}
\]

After relabelling, write

\[
\rho_x\equiv x\pmod {2^b}.
\tag{2}
\]

Then the following hold.

### 1. Exact source coverage

The union of legal source states is

\[
\boxed{
\mathcal S
=\bigcup_{x\in\mathbb Z/2^b\mathbb Z}
(\rho_x+2^L\mathbb Z).}
\tag{3}
\]

Inside each low-bit cell

\[
x+2^b\mathbb Z,
\]

there are exactly `2^(L-b)` residue classes modulo `2^L`, and exactly one of
them is legal for the branch labelled by `x`.

Thus

\[
\boxed{
\frac{|\mathcal S\bmod2^L|}{2^L}=2^{b-L}.}
\tag{4}
\]

Complete projection does not mean complete source coverage unless `b=L` and all
`2^L` parity words occur.

### 2. Failure of a low-bit-only causal rule

Consider the apparent controller

```text
read x = n mod 2^b;
select branch w_x.
```

It is a legal Collatz action at the current integer `n` if and only if

\[
\boxed{n\equiv\rho_x\pmod {2^L}.}
\tag{5}
\]

The low `b` bits determine which candidate branch is named.  They do not prove
the remaining `L-b` source bits required by that branch.

Consequently a complete-projection collision code is a **finite branch
compiler**, not a total controller on ordinary integers.  To orient it along one
existing orbit, a construction must additionally carry or prove the full source
cylinder (5), including its most-significant finite boundary.

### 3. Iterated deficit

Suppose stage `j` offers `B_j` fixed-length parity blocks of length `L_j`.
Every length-`N` sequence of selected blocks concatenates to one parity word of
length

\[
D_N=\sum_{j=0}^{N-1}L_j.
\]

Distinct concatenated parity words have distinct source residues modulo
`2^(D_N)`.  Hence the set of starts realizing *some* first `N` stage choices
occupies at most

\[
\prod_{j=0}^{N-1}B_j
\]

residue classes modulo `2^(D_N)`, and therefore has dyadic density at most

\[
\boxed{
2^{-D_N}\prod_{j=0}^{N-1}B_j.}
\tag{6}
\]

If `B_j=2^(b_j)`, this is

\[
\boxed{
2^{-\sum_{j<N}(L_j-b_j)}.}
\tag{7}
\]

This bound does not prove emptiness: a zero-density nested family may contain an
ordinary integer.  It proves that symbolic branch count or complete low-bit
projection cannot replace the missing full-cylinder invariant.

## Proof

A length-`L` shortcut parity word determines exactly one residue modulo `2^L`;
this is the standard parity-cylinder bijection.  Distinct words therefore give
distinct residues.  Equation (1) places exactly one selected residue above every
low class modulo `2^b`, proving (3)--(4).  The current integer follows `w_x`
exactly when it belongs to that word's parity cylinder, which is (5).

For the iterated statement, concatenate the selected blocks.  There are at most
`prod B_j` concatenations, and each determines one residue modulo `2^(D_N)`.
Dividing by the total number `2^(D_N)` of residues gives (6)--(7).  ∎

## Consequence for the all-precision selector

`T-0042` proves that, for every requested `b`-bit correction, one finite
collision branch can be compiled causally.  In particular this is available at
`b=176`.

The present lemma narrows that result:

```text
proved by T-0042:
  request -> one exact candidate parity branch;

not proved:
  current ordinary refund state -> membership in that branch's full source
  cylinder.
```

The second line is the ordinary top-boundary problem.  It cannot be inferred
from complete projection, CRT anchoring of each finite prefix, or the existence
of many branches.

## Global significance

This closes one recurrent but invalid inference in the repository:

\[
\boxed{
\text{ability to represent every required low correction}
\not\Longrightarrow
\text{ability to apply the representing branch to the current integer}.}
\]

A successful selector/refund coupling must prove a full source-cylinder
identity from the current finite state, not merely compute a branch whose low
projection is desirable.

## Gap audit

- The lemma does not exclude an ordinary orbit lying in the sparse source set.
- The density bound is not an emptiness theorem.
- A one-counter or pushdown invariant may carry exactly the missing high source
  information; this lemma says that information must be proved explicitly.
- No Collatz counterexample is claimed.
