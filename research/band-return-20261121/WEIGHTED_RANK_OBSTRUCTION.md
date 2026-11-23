# An odd-count weighted rank cannot support the unrestricted mixed rules

**Status: paper-level argument, not an additional Lean formalization.** This
note tests a specific proposed repair of the simultaneous induction. It does
not claim that every possible rank or mixed proof architecture is impossible.

Let `T` be the ordinary shortcut map, and consider fixed positive real weights
`lambda, mu` in the supplied-certificate rank

\[
R_{\lambda,\mu}(n,d,p)=(n+1)\lambda^d\mu^p.
\]

Here `T^d(n)=1` is an actual finite certificate and `p` counts its odd inputs.
The proposed rule set requires strict rank descent both when advancing an
ordinary source certificate and when applying the particular frozen reverse
template specified below. These two unrestricted requirements are incompatible.
The counterinstances are an explicit unbounded family of positive ordinary
integers with actual certificates on both sides.

## 1. Necessary strict inequalities from forward steps

For an odd source, `T(n)+1=3*(n+1)/2`. Consuming one clock and one odd step
therefore gives the exact ratio

\[
\frac{R(T(n),d-1,p-1)}{R(n,d,p)}
=\frac{3}{2\lambda\mu}.
\]

Strict decrease requires

\[
\boxed{\lambda\mu>3/2}.
\]

This requirement already follows from the certified step `3 -> 5`; it does
not use convergence of an arbitrary source. Equality would preserve the
rank on every odd forward step and is therefore inadmissible.

For a positive even source, the corresponding ratio is

\[
\frac{n+2}{2(n+1)\lambda}.
\]

Thus any admitted even forward-step comparison that strictly decreases this
rank requires `lambda>1/2`. Requiring all such comparisons includes the
certificate `2 -> 1` and gives the stronger inequality `lambda>2/3`.
Only the weaker necessary inequality is used below. In particular, treating
`2 -> 1` as a terminal case does not remove the obstruction if the rule set
still requires a strict even forward-step comparison elsewhere.

## 2. The precise frozen reverse row and its transport contract

The source is PR168 head
`e4599b32e4b1a955ac9315d46782d4ad6a5db96c`, file
[`research/closure-frontier-20261121/negative_template_compiler.py`](https://github.com/GettysburgResearch/collatz/blob/e4599b32e4b1a955ac9315d46782d4ad6a5db96c/research/closure-frontier-20261121/negative_template_compiler.py).
Its source SHA-256 is
`16aab6efe1294a33c88f8b2fadae9d8060e68cc242eee18425aab7cfdcdd1745`.

The row has reference `-1039/729` and parameters

\[
(a,b,c,K,\mathrm{residue})=(11,7,-1069,11,779).
\]

Its source parameter satisfies

\[
M\equiv2047\pmod{2048},\qquad
M\equiv779\pmod{2187},
\]

and the transformed parameter obeys

\[
2187M'+1069=2048M.
\]

These guards give the progression `M=761855+4478976*h`, `h>=0`, with
`M'=713433+4194304*h`, so both parameters are positive. The complete original
row guards and finite-prefix legality conditions are retained; they are not
replaced by an asymptotic height estimate.

The frozen row data and their earlier exact arithmetic review are available
in [the copied inputs](../../reports/2026-11-21-lean-global/common-rank-clock-inputs.json)
and [the source-clock review](../../reports/2026-11-21-lean-global/COMMON_RANK_CLOCK_REVIEW.md).
The source words are

```text
old: (2,2,2,1,2,4)
new: (2,2,2,1,1,2,2,2,2,1,2,4,5)
source_J = 2
```

The compiler's source splicing contract changes the clock by
`28-13-4=11` and the odd count by `13-6=7`; the `J^2` adjustment reduces
the first remaining odd exponent by four. The common binary-to-psi source
prefix has seven clocks and four odd steps, so those contributions cancel
on conjugating the contract to the actual known psi sources

\[
S=81M+2,\qquad S'=81M'+2.
\]

In these coordinates the resulting certificate law is

\[
(d,p)\longmapsto(d+11,p+7),
\]

and the exact shifted-height identity is

\[
\boxed{2187(S'+1)=2048(S+1)-86172}.
\]

The complete generic compiler splicing contract is not newly formalized in
Lean by this note. Moreover, the explicit family in section 4 has direct
ordinary certificates for both `S` and `S'`, independently corroborating the
required clock and odd-count changes. The obstruction therefore does not
depend on assuming that arbitrary guarded sources converge or on silently
padding a source witness.

## 3. The template eventually increases the proposed rank

Define

\[
K_{\lambda,\mu}
=\frac{2048}{2187}\lambda^{11}\mu^7
=(2\lambda)^4\left(\frac{2\lambda\mu}{3}\right)^7.
\]

The strict forward-step requirements imply `K_{lambda,mu}>1`. The exact
template ratio is

\[
\frac{R(S',d+11,p+7)}{R(S,d,p)}
=K_{\lambda,\mu}
 \left(1-\frac{86172}{2048(S+1)}\right).
\]

Thus the reverse-template comparison increases the rank whenever

\[
S+1>
\frac{86172K_{\lambda,\mu}}
     {2048(K_{\lambda,\mu}-1)}.
\]

The finite negative offset cannot rescue the comparison at arbitrarily large
sources. There is no unresolved asymptotic-equality case: `lambda*mu=3/2`
already violates strict odd-step descent, while the actual strict hypotheses
give `K>1`. The boundary `lambda=1/2` also fails every positive even forward
step. The argument does not substitute a non-strict inequality for either
of these required strict comparisons.

## 4. Explicit unbounded guarded sources with actual certificates

For each natural `j`, put

\[
e_j=2534744+3188646j,
\qquad
S_j=\frac{2^{e_j}-85}{27}.
\]

The exact modular computations are

\[
2^{2534744}\equiv1703812\pmod{4782969},
\qquad
2^{3188646}\equiv1\pmod{4782969},
\]

where `4782969=3^14`, `3188646=2*3^13`, and

\[
1703812=85+27(81\cdot779+2).
\]

It follows that every `S_j` is a positive integer and

\[
S_j\equiv63101\pmod{3^{11}}.
\]

Since `e_j>=11` and `27*1969+85=2048*26`, also

\[
S_j\equiv1969\pmod{2048}.
\]

Consequently `M_j=(S_j-2)/81` is integral and satisfies both row guards:
`M_j mod2187=779` and `M_j mod2048=2047`. These sources and their transformed
parameters are positive and unbounded.

The ordinary eleven-clock prefix at the canonical binary representative is

```text
1969 -> 2954 -> 1477 -> 2216 -> 1108 -> 554
     -> 277 -> 416 -> 208 -> 104 -> 52 -> 26.
```

It has three odd steps and affine intercept 85. Exact binary-cylinder lifting
therefore gives

\[
T^{11}(S_j)=\frac{27S_j+85}{2048}=2^{e_j-11}.
\]

The remaining `e_j-11` clocks are halvings. Hence every source has the actual
certificate

\[
\boxed{T^{e_j}(S_j)=1,\qquad p=3}.
\]

Its complete odd-exponent word is `(2,4,e_j-6)`. The last exponent is much
larger than four, so the frozen row's `J^2` adjustment is admissible without
padding. Removing the common seven-clock source prefix from the row's new
word gives the transformed complete odd word

```text
(1,2,2,2,2,1,2,4,5,e_j-10).
```

This has ten odd steps and total clock `e_j+11`.

### Direct independent certificate for the transformed source

There is also a direct ordinary-cylinder check of that conclusion. For
`S'_j=81M'_j+2`, the exact row identity simplifies to

\[
3^{10}S'_j=2^{e_j+11}-2504477.
\]

The canonical residue `3262123 mod2^22` has, in its actual 22-clock shortcut
prefix, odd input clocks

```text
0,1,3,5,7,9,10,12,16,21
```

and endpoint `45926`. Its affine intercept is `2504477`; in particular,

\[
3^{10}\cdot3262123+2504477=2^{22}\cdot45926.
\]

The displayed formula for `S'_j` forces precisely that residue modulo `2^22`.
Applying the actual finite-word cylinder identity yields

\[
T^{22}(S'_j)=
\frac{3^{10}S'_j+2504477}{2^{22}}
=2^{e_j-11}.
\]

Again the remaining clocks are halvings. Thus the transformed sources have
actual certificates with clock `e_j+11` and odd count ten, independently of
the generic compiler's witness-splicing implementation.

The modular congruences and the two finite prefixes are exact integer checks.
The all-`j` conclusion follows from congruence periodicity and the exact
ordinary affine-cylinder law, not from testing finitely many large sources.
Since this certified family is unbounded, it eventually exceeds the threshold
in section 3 for every fixed pair of weights satisfying the forward-step
requirements.

## 5. Consequence and limits

No rank of the stated fixed multiplicative form can strictly decrease on
both the unrestricted ordinary forward-source comparisons and all instances
of this one frozen reverse row. The obstruction occurs on actual positive
ordinary certificates, not merely on formal states or completed 2-adic inputs.

This does not contradict the earlier checked common rank
`(n+1)*(201/200)^d`: its forward moves retain an explicit growth guard and
do not include every ordinary source step. Nor does this argument rule out
guarded move selection, a different functional form, or additional phase
and history in the induction state.

For the global band-return attack, the sound ordinary-to-marked budget remains
`2^H(m)*m<n`. The new first-return bridge supplies that budget on an unbounded
explicit family. A total decreasing selector for every remaining marked
state is still required. Neither an unproved ordinary floor nor a free
conversion of semantic goal kinds provides that selector, and this note
does not claim a full Collatz proof.
