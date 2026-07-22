# L-9883 -- Common-width exposure for survivor cylinder selectors

Claim ID: `L-9883`  
Title: Every suffix is a unique live cylinder minimum, and the global promotion criterion is exactly a block-zero exclusion  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9826`, `L-9847`, `L-9877`, `L-9881`  
Scope: common-width finite survivor extensions and cylinder-restricted order selectors  
Related counterexample candidates: none

## Statement

Fix `m>=1`, put `M=64^m`, and write

\[
r_m(u)=\alpha_m(u),
\qquad u\in\{0,1\}^m.
\tag{1}
\]

The suffix-cylinder map `u -> r_m(u) mod M` is injective.  For a depth-`n`
survivor prefix `p`, put

\[
x=x_n(p),
\qquad
J=J_{n,m}(p),
\qquad
z=[81^{-n}]_M.
\tag{2}
\]

The arbitrary-width compiler is

\[
\boxed{
\alpha_{n+m}(p,u)
=
x+64^n[J+zr_m(u)]_M.
}
\tag{3}
\]

### 1. Every suffix is a unique live cylinder minimum

For every `v in {0,1}^m`, there are infinitely many `n=1 mod 4` such that,
for the actual one-hot prefix `p_v=w_n=0^(n-1)1`, the extension `p_vv` is
the unique ordinary minimum among all `2^m` common-width extensions `p_vu`.

The depths are exactly a residue class satisfying

\[
\boxed{
81^{-n}
\equiv
(17+64r_m(v))^{-1}
\pmod {64^{m+1}}.
}
\tag{4}
\]

At such a depth,

\[
\boxed{
\alpha_{n+m}(w_n,v)=64^{n-1},
}
\tag{5}
\]

whereas for `u!=v` its exact output block is

\[
\boxed{
[z(r_m(u)-r_m(v))]_M\ne0.
}
\tag{6}
\]

The cylinder-restricted successor gap is therefore

\[
\boxed{
64^n
\min_{u\ne v}
\langle z(r_m(u)-r_m(v))\rangle_M^+.
}
\tag{7}
\]

### 2. Exponential lower bounds for two exact selectors

Define the horizon-`m` **prefix-cylinder selector** to order all `2^m`
extensions `pu` of one actual prefix `p` and return the labels and values of
its first two members.  The witnesses in part 1 have different unique
minimizing labels, so

\[
\boxed{
N_{\rm cylinder\ selector}(m)\ge2^m.
}
\tag{8}
\]

No fixed finite state set implements this exact selector over all horizons.

There is also a smaller selector with a stronger bound.  Let the labeled
**two-ray selector** order only `p0^m` and `p1^m`.  For each `0<=q<M`, choose
the one-hot prefix from `L-9881` with `J=q`.  Its two exact representatives
are

\[
\boxed{
\begin{aligned}
A_0&=64^{n-1}+64^nq,\\
A_1&=64^{n-1}+64^n[q+81^{-n}]_M.
\end{aligned}
}
\tag{9}
\]

They are distinct and the labeled block attached to `0^m` is exactly `q`.
Hence

\[
\boxed{
N_{\rm labeled\ two\mbox{-}ray\ selector}(m)\ge64^m.
}
\tag{10}
\]

Both bounds concern genuine common-width survivor comparisons, not merely
abstract terminal states.

### 3. Exact promotion criterion for the global minimum

For the prefix `w_n` of part 1, put `Q=64^n`.  For every depth-`n` prefix
`epsilon` and suffix `u`, define

\[
K(\varepsilon,u)
=
[J_{n,m}(\varepsilon)+81^{-n}r_m(u)]_M.
\tag{11}
\]

Then

\[
\alpha_{n+m}(\varepsilon,u)
=
x_n(\varepsilon)+QK(\varepsilon,u).
\tag{12}
\]

The exposed candidate `(w_n,v)` has block zero and lower coordinate `Q/64`;
every positive block starts at least at `Q`.  It is therefore the actual
global nontrivial survivor minimum if and only if

\[
\boxed{
x_n(\varepsilon)\ge Q/64
}
\tag{13}
\]

for every nonconstant pair `(epsilon,u)` with `K(epsilon,u)=0`.

Let

\[
g_v=
\min_{u\ne v}
\langle81^{-n}(r_m(u)-r_m(v))\rangle_M^+.
\tag{14}
\]

The restricted successor from (7) is also the global successor exactly when,
in addition to (13), there is no other nonconstant survivor in block zero,
every block `1,...,g_v-1` is empty, and the `w_n` extension is the head of
block `g_v`.

Thus promotion to the unrestricted global selector is reduced to an exact
ordinary-order exposure problem.  Terminal-jet reachability alone does not
prove (13).

## Definitions

The bracket `[a]_M` is the canonical representative in `{0,...,M-1}` and
`<a>_M^+` is its least positive representative.  A live cylinder head is a
survivor that is genuinely first in the ordinary order among every extension
of the same prefix at the prescribed horizon.

The selectors in part 2 retain suffix labels.  This is essential: their state
must distinguish which continuation realizes the returned ordinary value.
Neither selector is the unrestricted global `(M_n^[1],M_n^[2])` sequence.

## Motivation

`L-9881` proved that all terminal jets occur among actual one-hot prefixes,
but its witnesses lived at different depths.  The present lemma supplies a
true common-width exposure: for any chosen suffix, one prefix makes that
suffix beat all competing descendants simultaneously.

The resulting exponential state bounds apply to two natural exact
order-statistic compilers.  Part 3 then identifies the remaining global gap
without hiding it behind automata language: only lower-coordinate survivors
inside the specially translated block-zero fiber can defeat the candidate.

## Proof

### Exposure congruence

The right side of (4) is `1 mod 16`, so the power-of-81 subgroup theorem in
`L-9881` gives infinitely many solutions, all `1 mod 4`.  For the resulting
one-hot prefix, put `z=81^(-n)`.  Its zero-tail block is

\[
J={17z-1\over64}\pmod M.
\tag{15}
\]

Equation (4) gives

\[
J+zr_m(v)
={z(17+64r_m(v))-1\over64}
\equiv0\pmod M.
\tag{16}
\]

Subtracting this identity for any other `u` gives (6).  Since `z` is a unit
and `r_m` is injective, only `u=v` has block zero.  The lower coordinate is
`x_n(w_n)=64^(n-1)`, proving (5) and (7).

### Selector bounds

If two prefixes from part 1 induced the same deterministic cylinder-selector
state, expansion of the identical labeled binary tree of depth `m` would
return the same minimizing suffix.  The `2^m` different labels contradict
this, proving (8).  For the two-ray selector, `r_m(0^m)=0` and
`r_m(1^m)=1`; substitution in (3) gives (9).  The `64^m` possible labeled
zero-ray blocks are distinct outputs, proving (10).

### Global criterion

Equation (12) orders survivors first by block and then by the old lower
coordinate.  The candidate has block zero and coordinate `Q/64`.  Positive
blocks cannot precede it, so exactly the block-zero inequalities (13) decide
whether it is globally minimal.  The four listed successor conditions are
the same lexicographic comparison through block `g_v`.  QED

## Dependency audit

- `L-9877` supplies the arbitrary-width compiler (3).
- `L-9826` supplies suffix-cylinder injectivity.
- `L-9881` supplies the one-hot state formula and the power-of-81 subgroup.
- `L-9847` interprets (7) as a pointed translated-cylinder gap but is not
  needed for the state lower bounds.
- No empirical minimum table or infinite-survival hypothesis is used.

## Gap audit

- The `2^m` and `64^m` bounds apply to the explicitly defined restricted
  selectors, not to every black-box global minimum/successor algorithm.
- The global criterion (13) is exact but unproved in general.
- Other depth-`n` prefixes may occupy block zero below `64^(n-1)`.
- Global successor promotion additionally requires empty intervening blocks
  and the correct head in block `g_v`.
- No asymptotic lower bound on the restricted gap (7) is asserted.

## Adversarial tests

- Congruence (4) is one base-64 digit wider than the output blocks; division
  by 64 in (16) requires that precision.
- The minimum proof uses injectivity of the complete suffix code modulo
  `64^m`, not just distinct last bits.
- All `2^m` competitors in part 1 share one prefix and one final width.
- The two-ray outputs retain modular wrap in the second line of (9).
- A block-zero competitor is ordered by its old coordinate, so merely proving
  uniqueness among descendants of `w_n` does not establish global minimality.

## Remaining uncertainty

Can exact survivor coding exclude `x_n(epsilon)<64^(n-1)` inside the special
block-zero fiber of (13) for infinitely many exposing depths?  This is now the
precise common-width bridge to the global first-two selector.

## Suggested next attack

Combine the signed-difference valuation law of `L-9834` with the block-zero
equation in (11).  A lower bound for the first differing digit of any
competitor below `64^(n-1)` could prove (13), while a finite counterexample
would identify the exact prefix pattern that defeats one-hot exposure.
