# R-7401 — Positive-entropy supercritical Collatz paths need not contain one ordinary seed

**Claim ID:** `R-7401`  
**Type:** refutation / global proof-schema boundary  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-outlier-01`  
**Reviewing agents:** none  
**Created:** 2026-07-25  
**Issue:** #55  
**Dependencies:** elementary shortcut-Collatz affine algebra; the finite parity-cylinder bijection proved below  
**Scope:** finite-prefix compatibility, compact path trees, entropy/branching, and conditional positive drift  
**Related counterexample candidates:** none

## Refuted inference

Even the following strengthened implication is false:

```text
all finite legal prefixes have infinitely many positive integer roots
+ the infinite legal-path set is compact and perfect
+ the path set has positive entropy and positive 2-adic dimension
+ every path has a uniform supercritical odd-step density
+ any positive ordinary realization would grow exponentially
=> at least one path has a positive ordinary realization.
```

The failure occurs inside the raw shortcut-Collatz parity system itself, not merely in an auxiliary encoding.

## General construction theorem

Let `L>=1` and let `B` be a finite set of binary words of length `L`, with

```text
|B|>=2,
```

such that every word in `B` has exactly `w` ones and

\[
3^w>2^L.
\tag{1}
\]

For the shortcut Collatz map

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\[1mm]
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]

there exists a computable compact perfect family `Y` of infinite parity words with all of the following properties.

1. Every length-`L` block of every word in `Y` belongs to `B`.
2. No word in `Y` is the parity sequence of any ordinary signed integer.
3. Every finite prefix occurring in `Y` is realized by exactly one residue class modulo the corresponding power of two and hence by infinitely many positive ordinary integers.
4. If a positive ordinary integer realized any word in `Y`, then along complete blocks
   \[
   T^{mL}(x)\ge x\left(\frac{3^w}{2^L}\right)^m,
   \]
   so its orbit would be unbounded.
5. The block entropy of `Y` is unchanged by the diagonal exclusion:
   \[
   h(Y)=\frac{\log_2|B|}{L}>0.
   \]
6. Under the parity-cylinder identification with `Z_2`, the corresponding compact set has `2`-adic Hausdorff dimension
   \[
   \frac{\log_2|B|}{L}>0.
   \]

Thus finite physical realizability, continuum many infinite paths, positive entropy, positive dimension, and uniform supercritical drift still do not supply ordinary extraction.

## Construction

Enumerate all ordinary signed integers as

\[
z_0,z_1,z_2,\ldots.
\]

For example, use

```text
0,1,-1,2,-2,3,-3,... .
```

Let the sparse distinguished block positions be

\[
N_j=2^j.
\tag{2}
\]

For each `j`, compute the length-`L` parity block of `z_j` beginning at shortcut time `LN_j`. Choose one block

\[
\beta_j\in B
\]

that differs from that block. This is always possible because `|B|>=2`: if the integer block belongs to `B`, choose another member; if it does not, choose any member.

Define `Y` by requiring:

- block `N_j` is exactly `beta_j` for every `j`;
- every other block may be any member of `B`.

The construction is computable because each required comparison uses only finitely many exact integer shortcut steps.

## Proof

### 1. Finite parity cylinders

Every binary parity word of length `n` is realized by exactly one residue class modulo `2^n`.

The proof is by induction. Suppose one length-`n` word is realized by `r mod 2^n`. Its two lifts modulo `2^(n+1)` are `r` and `r+2^n`. Along their common first `j<=n` branches, the exact difference is

\[
T^j(r+2^n)-T^j(r)=3^{s_j}2^{n-j},
\]

where `s_j` is the number of odd branches among those first `j` steps. The difference is even for `j<n` and odd at `j=n`. Hence the first `n` parity bits agree and the next bits are opposite. The two lifts realize the two possible extensions uniquely.

Therefore every finite prefix in `Y` has one residue modulo `2^n`, and that residue class has infinitely many positive representatives.

### 2. No ordinary infinite realization

The parity sequence of `z_j` differs from every member of `Y` at distinguished block `N_j`, by construction. Since the enumeration contains every signed ordinary integer, no ordinary integer realizes any word in `Y`.

This is an explicit diagonal exclusion, not a cardinality-only argument.

### 3. Compactness and perfectness

The set `Y` is a direct product of finite allowed block sets, with one allowed block at the sparse positions `N_j` and `|B|>=2` allowed blocks elsewhere. It is closed in the product topology and therefore compact.

There are infinitely many nondistinguished block positions. Any finite prefix can therefore be extended in at least two ways arbitrarily far out. No point is isolated, so `Y` is perfect.

### 4. Uniform supercritical growth if ordinary

Every complete `L`-block has exactly `w` odd steps. For a parity prefix containing `m` complete blocks, the exact affine formula has the form

\[
T^{mL}(x)=\frac{3^{mw}x+C_m}{2^{mL}},
\qquad C_m\ge0.
\]

For `x>0`,

\[
T^{mL}(x)
\ge
x\left(\frac{3^w}{2^L}\right)^m.
\]

Condition `(1)` makes the factor greater than one, so any positive ordinary realization would be unbounded.

### 5. Entropy and dimension

Among the first `m` complete blocks, the number of forced positions is

\[
f(m)=\#\{j:2^j<m\}=O(\log m).
\]

Hence the number of allowed prefixes of length `mL` is exactly

\[
|B|^{m-f(m)}.
\]

Therefore

\[
\lim_{m\to\infty}
\frac{\log_2 |B|^{m-f(m)}}{mL}
=
\frac{\log_2|B|}{L}.
\]

The finite parity bijection identifies length-`n` parity cylinders with residue cylinders modulo `2^n`, preserving cylinder depth. Covering the preimage in `Z_2` by its length-`mL` cylinders gives the same Hausdorff-dimension value. ∎

## Explicit smallest example

Take

```text
L=4,
B={1110,1101},
w=3.
```

Then

\[
\frac{3^w}{2^L}=rac{27}{16}>1,
\]

and the resulting ghost forest has entropy and `2`-adic dimension exactly

\[
\frac14.
\]

Every finite path is a genuine shortcut-Collatz parity prefix with infinitely many positive integer roots. Every infinite path is uniformly supercritical. Yet the family contains no parity sequence of any ordinary signed integer.

## Stronger entropy variants

The same construction may use all length-`L` words of one weight `w` satisfying `3^w>2^L`. Its entropy is

\[
\frac1L\log_2\binom{L}{w},
\]

apart from the zero-density forced blocks, which do not change the limit. Thus the obstruction is not limited to a thin periodic path or a zero-entropy controller.

## Consequence for current architectures

This theorem does not eliminate a source-specific Collatz subsystem. It eliminates a common inference schema.

The following properties, even simultaneously, cannot establish an ordinary root:

- exact finite Collatz replay for every prefix;
- infinitely many positive roots at every depth;
- a compact or perfect infinite path set;
- positive symbolic entropy or positive `2`-adic dimension;
- a uniform supercritical density;
- conditional exponential growth of every hypothetical ordinary path.

A successful ordinary-orbit proof must add information absent here, namely an architecture-specific Archimedean tightness theorem, eventual boundary stabilization, or one explicitly verified all-time integer.

## Relationship to draft PRs #56 and #57

- Draft PR #57 `T-7602` gives one explicit periodic supercritical ghost and a continuum-cardinality observation.
- Draft PR #56 `R-7801` decorates one arbitrary nonordinary cylinder chain with arbitrarily large affine expansion.
- `R-7401` strengthens both boundaries in a Collatz-native direction: the ghost set is compact, perfect, positive-entropy, positive-dimension, uniformly supercritical, and contains continuum many exact parity paths, while every finite prefix remains physically realizable.

## Gap audit

- The constructed infinite paths are deliberately nonordinary and are not counterexamples.
- The theorem refutes only arguments based on the listed common properties; a special global arithmetic identity may still force ordinary extraction in one fixed architecture.
- Positive entropy does not imply positive Haar measure, and no such implication is used.
- The diagonal set depends on the enumeration of ordinary integers, but the construction is effective and exact.

## Suggested next attack

Stop using compactness, branching, entropy, or drift as proxies for extraction. For one fixed architecture, prove either:

```text
one uniform upper bound on its least positive roots,
```

or

```text
its least positive roots tend to infinity.
```