# T-7401 — Ordinary extraction is exactly Archimedean tightness

**Claim ID:** `T-7401`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none  
**Created:** 2026-07-25  
**Issue:** #55  
**Dependencies:** elementary integer finiteness and nested-set logic  
**Scope:** arbitrary prefix-closed positive-integer architectures and compatible mixed-radix cylinder chains  
**Related counterexample candidates:** none

## Statement A — nested survivor sets

Let

\[
S_0\supseteq S_1\supseteq S_2\supseteq\cdots
\]

be nonempty subsets of `Z_{>0}`. Put

\[
m_n=\min S_n.
\]

The following are equivalent.

1. One positive ordinary integer survives every depth:
   \[
   \bigcap_{n\ge0}S_n\ne\varnothing.
   \]
2. There is a finite Archimedean bound `B` such that
   \[
   S_n\cap[1,B]\ne\varnothing
   \qquad\text{for every }n.
   \]
3. The least-root sequence `(m_n)` is bounded.
4. The sequence `(m_n)` is eventually constant.

If these conditions fail, then

\[
m_n\longrightarrow\infty.
\]

### Proof

The sets are nested, so `(m_n)` is nondecreasing.

If `x` lies in every `S_n`, then `m_n<=x` for every `n`; this gives conditions 2 and 3.

Condition 2 implies condition 3 because `m_n<=B`. A bounded nondecreasing integer sequence is eventually constant, so condition 3 implies condition 4.

Suppose `m_n=m` for every `n>=n_0`. Then `m in S_n` for every `n>=n_0`. For `j<n_0`, choose `n>=n_0`; nesting gives

\[
m\in S_n\subseteq S_j.
\]

Thus `m` lies in every survivor set. This proves condition 4 implies condition 1.

If the equivalent conditions fail, an unbounded nondecreasing sequence of positive integers tends to infinity. ∎

## Statement B — one compatible cylinder chain

Let

\[
1=M_0\mid M_1\mid M_2\mid\cdots,
\qquad M_n\to\infty,
\]

and let

\[
0\le r_n<M_n,
\qquad
r_{n+1}\equiv r_n\pmod{M_n}.
\]

Then the unique inverse-limit point selected by the chain is a nonnegative ordinary integer if and only if `(r_n)` is bounded, if and only if `(r_n)` is eventually constant.

It is a negative ordinary integer `-c`, with `c>0`, if and only if

\[
M_n-r_n=c
\]

for every sufficiently large `n`.

### Proof

Compatibility of canonical representatives gives

\[
r_{n+1}=r_n+a_nM_n
\]

for some integer `a_n>=0`, so `(r_n)` is nondecreasing.

If an ordinary `x>=0` realizes every cylinder, then once `M_n>x`, its canonical residue modulo `M_n` is exactly `x`; hence `r_n=x` eventually. Conversely, eventual constancy plainly realizes that integer at every depth by compatibility.

For `x=-c<0`, once `M_n>c`, its canonical residue is `M_n-c`. The converse again follows from compatibility. ∎

## Two-place interpretation

Finite-prefix compatibility supplies compactness only at the finite place: it produces a point in `Z_2` or in the relevant mixed-radix inverse limit.

Ordinary extraction requires an additional Archimedean tightness statement:

```text
finite-place compatibility
+ one uniform ordinary-size bound
= one ordinary integer.
```

Without the uniform bound, the finite witnesses may escape to infinity while converging perfectly at the finite place.

This is the exact missing quantifier correction:

```text
for every n there exists x_n in S_n
```

does not imply

```text
there exists x in every S_n;
```

whereas

```text
there exists B such that for every n
there exists x_n in S_n with x_n<=B
```

does imply one common survivor.

## Relationship to a `K-####` candidate

Assume a separately verified physical theorem says that every member of the infinite intersection is a nontrivial Collatz cycle or an orbit avoiding `1` forever.

- If `(m_n)` is bounded, its eventual value is one explicit ordinary seed. Exact physical replay then produces a `K-####` candidate.
- If `m_n->infinity`, the complete fixed architecture has no positive ordinary survivor and is eliminated.

For a finite union of fixed architectures, take the minimum of their least-root sequences. Boundedness produces a survivor in at least one member; divergence eliminates the whole finite union.

## Logical strength

This distinction is important.

- Proving `m_n->infinity` for one strict subsystem is genuinely weaker than proving the Collatz conjecture; it eliminates only that subsystem.
- Proving boundedness for one strict subsystem is **not** logically weaker than “Collatz is false.” It is a stronger, more structured sufficient condition whose payoff is an explicit counterexample.
- The equivalence in this file is an exact decision interface, but by itself it is not an architecture-specific breakthrough. It becomes progress only when an independent theorem actually bounds or forces escape of `(m_n)`.

## Dependency audit

No unmerged repository theorem is used. The result independently reconstructs the mathematical core of draft PR #56 `T-7801` and draft PR #57 `T-7601`.

## Gap audit

- This theorem does not decide any current least-root sequence.
- Replacing `m_n` by arbitrary noncanonical representatives destroys monotonicity and is not a valid extraction criterion.
- A `2`-adic, real, entropy, or growth estimate matters only if it supplies the required ordinary bound or proves escape.
- The theorem must not be advertised as solving the ordinary-root problem; it identifies it exactly.

## Suggested next attack

For each live strict architecture, define its canonical `S_n` and attack only one of:

```text
sup_n m_n < infinity,
```

or

```text
m_n -> infinity.
```

Do not replace this with a new prescribed directive, a longer prefix, or another conditional growth statement.