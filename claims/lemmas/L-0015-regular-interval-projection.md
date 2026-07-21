# L-0015 — Regular projection of finite marked intervals

Claim ID: `L-0015`  
Title: Effective regularity of interval lengths and marked ranks  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0014`, `T-0018`  
External infrastructure: PR #13 `LIT-KTHM-0019`–`0022`; proof below is self-contained  
Scope: finite-state encodings of ordinary interval endpoints and marked particles  
Related counterexample candidates: none

## Statement

All binary words below are least-significant digit first.

For nonnegative integers \(v,q\), not both zero, define their canonical
synchronous convolution

\[
\operatorname{conv}(v,q)
=
(v_0,q_0)(v_1,q_1)\cdots(v_{m-1},q_{m-1}),
\]

where

\[
m=\max\{\ell(v),\ell(q)\},
\]

missing high bits are zero, and the final pair is not \((0,0)\).

Let

\[
\Gamma=\{(0,0),(0,1),(1,0),(1,1)\}.
\]

Suppose \(G\subseteq\Gamma^*\) is a regular language consisting of canonical
pairs with

\[
q>v\ge1.
\]

Define its physical-length language by

\[
\operatorname{Len}(G)
=
\left\{
\operatorname{bin}_{\rm LSD}(q-v):
\operatorname{conv}(v,q)\in G
\right\}.
\]

Then:

### 1. Effective regularity of interval lengths

\[
\boxed{\operatorname{Len}(G)\text{ is regular.}}
\]

An NFA, and hence a DFA, for this language is effectively constructible from a
DFA for \(G\).

### 2. Fixed- and diagonal-gauge lifts

If \(L\) is any regular language of canonical positive binary words, then both

\[
\boxed{
G_{\rm fix}(L)
=
\{\operatorname{conv}(1,n+1):\operatorname{bin}_{\rm LSD}(n)\in L\}
}
\]

and

\[
\boxed{
G_{\rm diag}(L)
=
\{\operatorname{conv}(n+1,2n+1):\operatorname{bin}_{\rm LSD}(n)\in L\}
}
\]

are regular.

Their physical-length projections are exactly \(L\).

### 3. Marked-particle projection

Let \(H\) be a regular convolution language of finite populations and marked
ranks,

\[
\operatorname{conv}(x,j),
\qquad
1\le j\le x.
\]

Then the canonical language of marked ranks

\[
\operatorname{Mark}(H)
=
\{\operatorname{bin}_{\rm LSD}(j):\operatorname{conv}(x,j)\in H\}
\]

is regular and effectively constructible.

More generally, every marker extracted from a regular configuration language by
a finite rational transduction has a regular canonical language.

## Proof

### The binary addition relation is finite-state

Consider canonical three-track convolutions of \(v,n,q\). A two-state carry
automaton recognizes

\[
v+n=q.
\]

At bit position \(i\), with carry \(c_i\in\{0,1\}\), it accepts precisely the
triples satisfying

\[
v_i+n_i+c_i=q_i+2c_{i+1}.
\]

The initial carry is zero and the terminal carry must be zero. Track
canonicality and the requirement \(q>v\ge1\) are regular conditions. Therefore

\[
\mathcal A
=
\{
\operatorname{conv}(v,n,q):v+n=q,\ q>v\ge1
\}
\]

is a regular synchronized relation.

Intersect the \((v,q)\)-tracks with \(G\). The resulting three-track language is
regular. Projecting a regular language onto the \(n\)-track gives a regular
language: equivalently, an NFA guesses the hidden endpoint bits while it reads
the \(n\)-bits.

The synchronized word may contain high zero padding on the \(n\)-track because
\(q\) can be longer than \(n=q-v\). Removing this padding is the right quotient

\[
L_{\rm padded}/0^*,
\]

followed by intersection with the canonical positive language
\(\{0,1\}^*1\). Right quotient by a regular language and regular intersection
preserve regularity. This proves part 1 and gives an effective construction.

### Gauge lifts

The graph of

\[
n\longmapsto n+1
\]

is recognized by the ordinary one-bit binary carry automaton. Pairing the
constant track \(1\) with the output track gives \(G_{\rm fix}(L)\).

For the diagonal gauge, the maps

\[
n\longmapsto n+1,
\qquad
n\longmapsto2n+1
\]

are subsequential binary transductions. Their synchronized product with a DFA
for \(L\) is regular. The interval differences are respectively

\[
(n+1)-1=n
\]

and

\[
(2n+1)-(n+1)=n.
\]

### Marked particles

Projection from the convolution alphabet onto the marked-rank track is a
letter-to-letter homomorphism followed, if necessary, by removal of high zero
padding and canonical intersection. Hence the marked-rank language is regular.

The final statement is the standard closure of regular languages under rational
transductions. ∎

## Effective construction used in `X-0011`

The experiment implements part 1 directly:

1. take the product of the endpoint DFA with the carry state;
2. on each visible length bit, existentially choose endpoint bits satisfying
   \(v_i+n_i+c_i=q_i+2c_{i+1}\);
3. accept terminal carry zero;
4. compute the right quotient by \(0^*\) through reverse zero-reachability;
5. determinize while enforcing canonical positivity.

The result is an ordinary LSD-first binary DFA compatible with the exact
regular-sanctuary semantics of PR #12.

## Significance

`L-0014` showed that an ordinary Collatz value is the length of a finite
interval. `T-0018` placed an ordinary trajectory on a marked particle spine.
The present lemma proves that **regular finite-state endpoint or population
descriptions have regular physical-marker projections**.

Thus finite endpoint decoration can simplify a certificate, but it does not
hide a nonregular ordinary marker set inside a regular configuration language.

## Gap audit

- Regularity does not imply nonemptiness, Collatz invariance, or avoidance of
  the terminal cycle.
- Projection can cause exponential determinization blowup.
- A pushdown, counter, indexed, or otherwise nonregular configuration language
  is outside this lemma.
- A finite rewrite rule set need not have a regular reachable-configuration
  language; the claim concerns an explicitly regular certificate language.

## Adversarial tests

`X-0011`:

- compiles randomly generated finite endpoint languages and checks the exact
  projected difference set;
- handles several gauges of the same physical length without duplication;
- compiles the infinite regular fixed-gauge language
  \(\{\operatorname{conv}(1,q):q\ge2\}\) to all positive integers;
- independently replays exact shortcut closure and the maximal safe-state
  kernel on the compiled DFA.

## Remaining uncertainty

The construction is standard finite-state algebra. The important native
question is whether a useful marked grammar can be made invariant only by using
an unbounded stack/counter or a genuinely nonregular survivor condition.
