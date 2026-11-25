# What the Subspace Theorem says about a critical record limit

**PROPOSED written corollary and a source-pinned review.** The p-adic
Subspace Theorem gives a substantive arithmetic restriction on repetitive
critical scripts. It does not force the limit of records of an ordinary
integer orbit to be algebraic. An explicit balanced script below has a
transcendental ternary coordinate under the reconstructed theorem. Every
finite prefix is realized by positive ordinary integers. These are changing
finite realizations, not an escaping orbit from one fixed integer.

The reviewed source is PR210 at
`592328fecf8ea2cf41736294856d95f890a1ba98`, specifically
[README, R1 and R2](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/README.md)
and [SUBSPACE, S1--S3](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/SUBSPACE.md).
The source and this corollary concern backwards odd-gap scripts. They do
not identify these scripts with ordinary ternary digit expansions.

## The retained arithmetic

Let the positive gaps be `e_j`, their cumulative clocks be `S_j`, and assume
`2^S_j < 3^j` at every nonempty prefix. Set

$$
 A_j=2^{S_j}/3^j,\qquad
 \beta_j=\sum_{i=1}^j3^{i-1}2^{-S_i},\qquad
 z=\lim_j\beta_j\quad\hbox{in }\mathbb Z_3.
$$

In this paragraph `\beta_j` is simultaneously a rational real number and a
ternary residue; the limit is only taken in the ternary metric. The exact
backwards affine identity is

$$ y_j=A_j(z-\beta_j). $$

R1 classifies rational points on this tree by negative rational cycles,
with an eventual periodic tail after the finite normalization needed for
an even denominator. The odd-numerator, odd-denominator case is a negative
cycle phase with a purely periodic backwards script. The even-denominator
qualification matters: a positive rational coordinate can have a finite
prefix into a negative cycle. The source gives `49/32` as an example.

The finite shadow proof uses a signed path occupation bound. On a simple
path for `2^e u_next=3u +/- d`, the number of distinct magnitudes at most
`X` is `O_d(X^(39/40))`. Its reciprocal tail bounds the correction product
along a negative backwards shadow with prefix multiplier at most a fixed
`H`. That shadow is bounded. A repeated vertex lies on a signed forward
cycle; forward determinism and repetition applied at every tail make the
whole infinite shadow periodic. The sign of the complete cyclic carry
excludes a positive cycle in a critical backwards script. This argument
uses the full carry and rational denominator, not just reduction at a
single prime.

R2 then rules out a nonrepeating ordinary ray whose strict multiplier
records have both uniformly bounded index gaps and a finite set of
rational odd-numerator, odd-denominator accumulation points. A long
backwards word is forced to follow one of the negative cycles, and bounded
record gaps extend that agreement along the actual source. Equal physical
parities for a positive integer `x` and a negative numerator `a` on
denominator `d` imply

$$ 2^h\mid dx-a. $$

No fixed positive `dx-a` is divisible by arbitrarily large powers of two.
Neither finite rational confinement nor bounded record gaps has been
proved for a hypothetical escaping ordinary ray.

## Where the heavy theorem enters

Suppose the actual script agrees with `U V V ...` for `r+w p-O(1)` gaps,
where `r=|U|`, `p=|V|` tends to infinity, and `r<=L p`. Write `s=S(U)`
and `A=S(V)`. For the integer carry `C_W=2^S(W) beta_W`, the periodic
approximation has the exact form

$$
 z_i=\frac{N}{X-Y},\qquad
 X=2^{s+A},\quad Y=2^s3^p,\quad
 N=C_U(2^A-3^p)+3^r C_V.
$$

At infinity and at 2 use the coordinate linear forms. At 3 use
`X, Y, z(X-Y)-N`. Under the hypothesis that `z` is algebraic these are
fixed algebraic forms, independent at each place. Their product is at most

$$ |N|3^{-m},\qquad m\ge r+w p-O(1). $$

Both large clock monomials cancel between the archimedean and finite
absolute values. The common divisor of `(X,Y,N)` is a power of two; passing
to primitive coordinates preserves this product and leaves height at
least `3^p`. Criticality gives height at most `3(9/2)^(r+p)`. If the
deficit `j log 3-S_j log 2` is `o(j)`, the sharper bound is
`3^(r+p) exp(o(r+p))`. Thus the three-place Subspace Theorem applies when

$$
 w>\log_3(9/2)+(\log_3(9/2)-1)L,
$$

or, under the balanced deficit condition, for any fixed `w>1`.
An infinite subsequence satisfies a rational linear relation
`uX+vY+tN=0`. Dividing by `X` and taking the ternary limit gives `u+tz=0`;
`t=0` would make all three coefficients zero. Hence an algebraic `z` must
be rational. R1 supplies eventual periodicity of its script.

This reconstructs the mechanism of S1 and S2. The repetition extraction
in S3 uses two repeated length-`n` factors among `O(n)` positions. It
allows overlap and also the case in which the distance between their
starts exceeds `n`. Enlarging a short period to a multiple comparable to
`n` gives period length tending to infinity, bounded preperiod ratio and
a repeat fraction strictly above one. Consequently a balanced,
non-eventually-periodic critical script with bounded liminf complexity
ratio has a transcendental coordinate.

The primary analytic input is Schlickewei's p-adic Subspace Theorem in
[Evertse, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf).
The combinatorial method is related to
[Adamczewski--Bugeaud, Annals 165 (2007), 547--565](https://annals.math.princeton.edu/2007/165-2/p04).
The latter paper is a precedent for the method, not a direct theorem
about these variable-clock Collatz coordinates. No growing dimension or
varying set of linear forms is smuggled into the application.

## An explicit transcendental critical point

Put `alpha=log_2 3` and

$$
 S_j=\lfloor j\alpha\rfloor,\qquad
 e_j=S_j-S_{j-1},\qquad
 z_*=\sum_{j\ge1}\frac{3^{j-1}}{2^{\lfloor j\alpha\rfloor}}
       \quad\hbox{in }\mathbb Z_3.
$$

**Corollary C1, written.** The script has letters in `{1,2}`, is critical
at every nonempty prefix, and has bounded positive deficit. Its coordinate
`z_*` is transcendental over `Q`, using S3 above.

Indeed `alpha` is irrational: a rational equality `alpha=a/b` would give
`2^a=3^b`. Therefore

$$
 \tfrac12<2^{S_j}/3^j<1,\qquad
 0<j\log3-S_j\log2<\log2.
$$

The mean of the letters tends to the irrational number `alpha`, whereas
an eventually periodic integer word has rational mean. For the complexity
bound, a length-`n` block starting at position `l+1` depends on
`t={l alpha}` through the floors `floor(t+j alpha)`, `0<=j<=n`.
The `n` distinct thresholds `{-j alpha}`, `1<=j<=n`, partition `[0,1)`
into `n+1` intervals on which the block is constant. There are at most
`n+1` factors of each length. All hypotheses of S3 are now satisfied.

This is a direct corollary of the reviewed source, not an assertion of
novelty for mechanical-word transcendence. It shows explicitly why
criticality, balance, low complexity and compactness do not themselves
force a rational limiting coordinate.

**Corollary C2, elementary written statement.** Every finite prefix of this
script is the exact backwards odd-gap word of a positive ordinary
integer, with its endpoint greater than every preceding odd site.

For a prefix of length `n`, choose a positive odd integer
`q == beta_n (mod 3^n)` with `q>2n+1`. This is an ordinary Chinese remainder
condition, since the denominators of the finite sum are powers of two.
Set `y_0=q` and `y_j=(2^e_j y_(j-1)-1)/3`. The ternary congruence and the
affine identity make each `y_j` an integer. They are odd by induction.
Also `beta_j<2j/3<q` and `0<A_j<1`, so `0<y_j<q`. The identity
`3y_j+1=2^e_j y_(j-1)` proves that `e_j` is the exact binary valuation.
Thus these are actual finite ordinary paths. This construction makes a
different source available for each length; it provides no single
ordinary source realizing all lengths coherently in forward time.

The [exact control](check.py) uses only integer bit lengths, powers and
modular inverses. It checks 4,096 mechanical gaps, finite factor counts,
and positive ordinary backwards realizations through depth 256. It does
not infer transcendence or an infinite path from finite enumeration.

The [repeated switch construction](TRANSCENDENTAL_FAMILY.md) strengthens
this example to an explicit compact subset consisting entirely of
transcendental critical coordinates. Its ternary Hausdorff dimension is
`(2-log_2 3) log 2/(2 log 3)>0`. Every finite prefix still has ordinary
realizations, with the same fixed-source qualification. The proof is a
written corollary of S2, not a Lean formalization.

## Lean scope and the final proposal

[CriticalRecordRigidity.lean](CriticalRecordRigidity.lean) recompiles the
source's finite candidate. The
[exact original](../../../../reports/astra-global-closure-20261124/round13/critical/upstream/CriticalRecordRigidity.lean.txt)
is preserved. The changes are narrow imports, three algebra tactics,
two linter fixes, and four additional axiom inventories. The theorem
statements are unchanged. Thirteen selected declarations compile under
warnings-as-errors with only the allowed standard axioms.

The kernel proves physical parity transport, divisibility and impossibility
of an infinite positive-to-negative parity match. It does not formalize
the signed occupation estimate, R1, compactness, the Subspace Theorem,
S1--S3 or C1. Its full-domain consumer explicitly assumes both
`RecordLock` and `CycleExclusion`. Those are unproved hypotheses. The
other retained universal proposal still assumes `FrontierMerger`.
Neither proposal is an unconditional proof of Collatz.
