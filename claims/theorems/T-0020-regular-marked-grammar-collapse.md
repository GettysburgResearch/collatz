# T-0020 — Finite-phase regular marked grammars collapse to regular sanctuaries

Claim ID: `T-0020`  
Title: Regular finite-phase Collatz block systems and marked-grammar collapse  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0015`, `L-0014`, `T-0018`  
External infrastructure: PR #13 `LIT-KTHM-0019`–`0022`; PR #12 exact sanctuary verifier  
Scope: regular finite-phase systems of fixed finite Collatz blocks  
Related counterexample candidates: none

## Statement

Let

\[
\mathcal C=\{w\in\{0,1\}^*:w\ne\epsilon,\ w\text{ ends in }1\}
\]

be the canonical positive LSD-first binary language.

Let \(V\) be a finite phase set. For each phase \(i\in V\), let

\[
L_i\subseteq\mathcal C
\]

be regular. For each \(i\), let \(E_i\) be a finite set of outgoing edges.
Every edge \(e\in E_i\) has:

- a target phase \(\tau(e)\in V\);
- a fixed positive block length \(b_e\ge1\);
- a regular domain \(D_e\subseteq L_i\).

Assume:

### Coverage

\[
\boxed{
L_i\subseteq\bigcup_{e\in E_i}D_e
}
\tag{1}
\]

for every phase \(i\).

The domains may be made disjoint when a deterministic selector is desired, but
disjointness is not needed for the theorem.

### Exact block closure

\[
\boxed{
T^{b_e}(D_e)\subseteq L_{\tau(e)}
}
\tag{2}
\]

for every edge.

### Terminal-cycle exclusion

\[
\boxed{
L_i\cap\{1,2\}=\varnothing
}
\tag{3}
\]

for every phase.

### Nonemptiness

At least one \(L_i\) is nonempty.

Then the language

\[
\boxed{
K
=
\bigcup_{e}
\ \bigcup_{k=0}^{b_e-1}
T^k(D_e)
}
\tag{4}
\]

is a nonempty regular shortcut-Collatz sanctuary:

\[
\boxed{
T(K)\subseteq K,
\qquad
K\cap\{1,2\}=\varnothing.
}
\tag{5}
\]

Conversely, every regular shortcut-Collatz sanctuary is a one-phase system of
this form with one edge of length one.

Therefore:

\[
\boxed{
\text{finite phases + regular domains + fixed finite blocks}
\iff
\text{one-step regular sanctuary}
}
\tag{6}
\]

at the level of existence.

## Marked-grammar corollary

Suppose instead that phase \(i\) carries a regular language \(G_i\) of finite
marked configurations—for example:

- finite endpoint intervals \([v,q)\);
- finite ordered populations with one marked rank;
- finite carry words with one ordinary boundary marker.

Assume:

1. the marker's canonical positive rank language is obtained from \(G_i\) by a
   rational finite-state projection;
2. each regular edge domain \(G_e\subseteq G_i\) rewrites by a fixed finite
   sequence of exact local rules;
3. the rewrite sends the marker rank \(n\) to \(T^{b_e}(n)\);
4. the target configuration lies in \(G_{\tau(e)}\);
5. no phase language contains a marker of rank \(1\) or \(2\).

Then the projected marker languages satisfy the hypotheses above, and the
grammar compiles effectively to an ordinary regular sanctuary.

In particular:

> A regular finite-state two-layer marked interval or marked-particle
> certificate is not more expressive than the regular-sanctuary program of
> PR #12.

## Proof

### Regularity

The shortcut map on canonical LSD-first words is a deterministic subsequential
transduction. Therefore every fixed iterate \(T^k\) maps regular languages to
regular languages. Each \(T^k(D_e)\) in (4) is regular, and the union is finite.
Hence \(K\) is regular.

### Nonemptiness

Choose a nonempty phase language \(L_i\). By coverage, every member of \(L_i\)
belongs to some edge domain \(D_e\). Since \(D_e\) occurs in (4) at \(k=0\),
the language \(K\) is nonempty.

### Forward closure

Take

\[
x\in T^k(D_e),
\qquad
0\le k<b_e.
\]

If \(k+1<b_e\), then

\[
T(x)\in T^{k+1}(D_e)\subseteq K.
\]

If \(k=b_e-1\), then exact block closure gives

\[
T(x)\in T^{b_e}(D_e)\subseteq L_{\tau(e)}.
\]

Coverage at the target phase places this endpoint in at least one outgoing
domain \(D_f\subseteq K\). Thus \(T(K)\subseteq K\).

### Exclusion of the terminal cycle

Suppose for contradiction that

\[
x=T^k(n)\in\{1,2\}
\]

for some \(n\in D_e\) and \(0\le k<b_e\). The shortcut map permutes the set
\(\{1,2\}\). Therefore

\[
T^{b_e}(n)\in\{1,2\}.
\]

But exact block closure puts this value in \(L_{\tau(e)}\), contradicting (3).
Hence \(K\cap\{1,2\}=\varnothing\).

### Converse

Given a regular sanctuary \(K\), use one phase, one domain \(D=K\), one
self-edge, and block length \(b=1\).

### Marked configurations

By `L-0015`, or more generally closure under rational transductions, the marker
projection of each regular configuration language and edge domain is regular.
Exact marker replay supplies (2), and the preceding proof applies. ∎

## Fixed-block and finite-graph consequences

### Fixed macro-blocks do not enlarge the class

A regular checkpoint language satisfying

\[
T^B(L)\subseteq L
\]

for one fixed \(B\) produces the sanctuary

\[
L\cup T(L)\cup\cdots\cup T^{B-1}(L).
\]

### Finite phase covers do not enlarge the class

Finite negative-target graphs, finite carry-phase systems, and finite collections
of fixed macro-tiles remain in the regular-sanctuary class whenever their
selected marker domains are regular.

### Finite-state marked populations do not remove the ordinary-boundary problem

The unmarked population layer of `T-0018` may carry useful pressure and
combinatorics. If the accepted finite configurations and marker extraction are
regular, however, their accepted ordinary marker ranks form a regular
sanctuary. The marker problem has not been bypassed; it has been compiled.

## Effective interoperability with PR #12

The proof is constructive:

1. project regular configuration domains to regular marker domains;
2. construct each fixed iterate image;
3. take the finite union (4);
4. determinize/minimize if desired;
5. submit the resulting LSD-first DFA to PR #12's unchanged exact checker.

PR #12 then supplies:

- exact one-step closure;
- a concrete counterexample word if closure fails;
- the maximal safe accepting-state kernel for the compiled skeleton;
- a short canonical witness bound when the language is nonempty.

Thus the literature and neighboring branch convert a large class of proposed
marked grammars into proof-carrying finite certificates immediately.

## Strategic consequence

The theorem sharply separates worthwhile next directions.

A marked rewrite construction can exceed regular sanctuaries only by using at
least one genuinely unbounded or nonregular ingredient, such as:

1. a pushdown stack;
2. an unbounded cycle-padding or valuation counter;
3. a nonregular arithmetic survivor language;
4. variable block lengths not reducible to finitely many phases;
5. a marker/configuration coupling whose projection is not rational.

This validates the current negative-cycle padding route while ruling out a
large amount of redundant finite-state grammar search.

The next central object should be a **counter- or stack-augmented marked
sanctuary**, with a finite ordinary marker present from the start and a
proof-carrying update rule for the unbounded memory.

## Literature audit incorporated

The literature-review branch contributes the exact boundary:

- `LIT-KTHM-0019`: subsequential images preserve regularity;
- `LIT-KTHM-0020`: fixed-DFA closure is decidable;
- `LIT-KTHM-0021`: a fixed finite relation has a greatest safe kernel;
- `LIT-KTHM-0022`: a nonempty \(q\)-state canonical DFA has a short witness.

Its live review also advises treating graph expansion as solved infrastructure
and focusing on arithmetic selectors and ordinary witnesses. The present
theorem applies that advice to the marked-particle route.

## Gap audit

- The theorem does not rule out regular sanctuaries; it identifies the exact
  existing search program for them.
- It does not apply when reachable configurations form a nonregular language.
- A finite rule alphabet can still generate a pushdown or more powerful
  language; “finite rewrite rules” must not be confused with “regular
  certificate language.”
- Unbounded counters introduce their own finite-versus-adic and reachability
  obligations.
- No counterexample or sanctuary is constructed here.

## Adversarial tests

`X-0011` independently implements:

- exact regular projection from endpoint-pair languages to interval lengths;
- canonical high-zero removal by right quotient;
- the exact shortcut subsequential transducer;
- exact closure witnesses;
- the maximal safe-state kernel;
- finite-block normalization controls.

The implementation is deliberately small and standard-library-only. PR #12
remains the comprehensive certificate checker.

## Recommended next attack

Use the negative eleven-cycle padding counter from `T-0015` as the first
unbounded memory symbol. Define a pushdown marked-particle grammar whose finite
control is a negative phase, whose stack height records synchronized cycle
padding, and whose distinguished marker follows the ordinary child of
`T-0018`.

The next theorem should prove an exact stack update

\[
(i,t,\text{marker})
\longmapsto
(j,t+\Delta_e,\text{new marker})
\]

on a regular family of low-order marker residues, with:

- stack nonnegativity;
- closure of the residue obligation;
- positive cycle growth above an explicit threshold;
- one finite initial marked configuration.
