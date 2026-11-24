# Adversarial audit of the uniform predecessor population

## Verdict and exact boundary

**VERIFIED as a written, source-qualified derivation at the frozen sources
below. This is not a Lean theorem or a verification of all of PR180.**

The claims audited are `JOINT_CLOCK_MIXING.md` (TF), (JF), (CW), and (CFJ),
followed by `GLOBAL_RENEWAL_ATTACK.md` (PD) and (PDU), Sections 1--5. The
earlier `LINEAR_BLOCK_ATOM_FLOOR.md`, Section 6, (LOG), is checked separately
in Section 8 of this audit; its proof needs only the marginal atom floor.
The joint-clock analytic input is Tao's nonnegative renewal estimate, Proposition
7.3, equation (7.10), together with the elementary prefix separation in
Section 6. The marginal parent uses his Proposition 1.14 directly.
The argument was reconstructed from those primary statements;
the neighboring source's own review was not used as its justification.

The resulting claim is substantial: there are absolute positive constants
`c,C` such that every positive target `a` with `3` not dividing `a` has

\[
 X\ge Ca\quad\Longrightarrow\quad
 \#\{0<n\le X:n\text{ odd},\ \exists t\ge0,\ T^t(n)=a\}
 \ge cX/a,
 \tag{PD}
\]

where `T` is the ordinary shortcut Collatz map. The constants are not made
numerically effective in the supplied argument. In particular, the claim
would give positive lower natural density of the basin of one, a major
advance beyond an exponent strictly below one. That consequence warrants
explicit independent analytic scrutiny; neither its novelty nor its
agreement with heuristics is evidence for it.

This audit found no unsupported step in the specified derivation. It does
not establish the missing upper bound on actual surviving original-source
mass, marked-global sublinearity, or finite defect energy. It does not
establish Collatz convergence. No theorem in the checked Lean continuation
silently imports (PD).

## 1. Frozen sources and byte authentication

The two main files are from PR180 at
`d0349de2108abb7c8fb8393c086610e3372df116`. The parent selected-prefix
construction is read at its explicitly cited earlier revision.

| Source and audited claims | Frozen head | Git blob |
|---|---|---|
| `research/lean-forward-band-20261121/JOINT_CLOCK_MIXING.md`, TF/JF/CW/CFJ | `d0349de2108abb7c8fb8393c086610e3372df116` | `c66d3f02df57047554873e86efbaf332ebff26c2` |
| `research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md`, PD/PDU, Sections 1--5 | `d0349de2108abb7c8fb8393c086610e3372df116` | `79f590b45674a41bbbc1709c5a77aacabacb60d0` |
| `research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md`, selected blocks, weighted counting, FLOOR and LOG, Sections 1--6 | `f87cb69b3dd86257731ddfbab58c87bf3b5f63d6` | `1cf40edfd0263a1f4b7f0d683d8cbaf1fcd50fc8` |

| Source basename | Bytes | SHA-256 |
|---|---:|---|
| `JOINT_CLOCK_MIXING.md` | 14843 | `782812faebb610672d02a158301bb1b5d6a69e3b1a1828106d4000bf6279878b` |
| `GLOBAL_RENEWAL_ATTACK.md` | 22075 | `313822ace94d9d98eb27a1b7dc3bdbe67ac40d0c1b0ed693ecc40c11ec2561b9` |
| `LINEAR_BLOCK_ATOM_FLOOR.md` | 16544 | `3e3d3c6c6206bf731ffb5da186bfb209e5d837a4f20f73749d6f79ef98dc30e2` |

The SHA-256 values were computed from the fetched UTF-8 source bytes.
Independently recomputing each Git blob identifier from the same bytes
matched GitHub's supplied blob. No trailing newline was added before those
checks. The hashes identify complete files; the verdict remains limited to
the claims and sections listed above.

## 2. Primary analytic input and version check

The primary paper is Terence Tao, *Almost all orbits of the Collatz map
attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12,
[DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8).
The published Cambridge text was inspected at:

- Proposition 1.14, equations (1.26)--(1.27), for the normalization of
  fine-scale total variation;
- Section 6, equations (6.1)--(6.10), and Corollary 6.3, for the stopped
  prefix, its fixed total, independence of the suffix, and separation of
  distinct prefix offsets;
- equations (7.4)--(7.5), Lemma 7.2, and Proposition 7.3, equation (7.10),
  for the nonnegative conditional product envelope.

The primary [arXiv record](https://arxiv.org/abs/1909.03562) was also checked.
Its current [version 7](https://arxiv.org/html/1909.03562v7), dated 16 July
2026, records a correction to Lemma 7.9. Version 7 retains Proposition 7.3,
equation (7.10), in the same nonnegative form needed here. This audit does
not reproduce Tao's proof of that external theorem. In particular, the
external theorem is neither a new local axiom in Lean nor a theorem whose
formalization was executed by this packet.

The parent note attributes the selected-prefix strategy and weighted
residue-counting device to Naoufal El Jaouhari's October 2026 work, via the
exposition it names. This audit reconstructs the displayed counting proof
and block estimates; it does not establish priority or audit that external
manuscript's other claims.

## 3. Keeping the complete time length is justified

Let the independent letters satisfy `Pr(a_i=e)=2^(-e)` for positive `e`,
write `A_h=sum a_i`, and let

\[
 X_h=\sum_{i=1}^h3^{i-1}2^{-A_i}\pmod {3^h}.
\]

For a primitive character `chi` modulo `3^h`, put
`z(u)=E[1_{A_h=u} chi(X_h)]`. Conditional on the pair sums
`a_(2j-1)+a_(2j)` and, for odd `h`, the final unpaired letter, `A_h` is
fixed. The remaining choices within different pairs are independent.
Multiplying the conditional characteristic function by any bounded
complex function `phi(A_h)` therefore leaves Tao's product-of-moduli
upper bound unchanged. His nonnegative renewal estimate gives

\[
 |\mathbb E[\phi(A_h)\chi(X_h)]|\le C_Kh^{-K}
 \quad (|\phi|\le1).
\]

Taking the phase of each `z(u)` as the test function proves
`sum_u |z(u)| <= C_K h^(-K)`. This does not assume independent clock and
residue marginals. The phase choice is legitimate because the sliced
sequence is absolutely summable even before the improved bound.

If the word is longer than the character conductor, its later letters
vanish from the offset seen by that character and add an independent
clock. Convolution by that clock law contracts the sliced `ell^1` norm.
Thus the same estimate is available at every high conductor used by the
prefix argument.

## 4. The joint total-variation calculation has no exponential loss

Tao's stopped prefix has length `k+1` close to
`n log(3)/(2 log(2))`, and fixed total
`ell = n log(3)/log(2) - O(log n)`. Its admissibility conditions depend
only on that prefix after the explicitly controlled enlargement of the
good event. Hence the suffix remains independent.

For its prefix subprobability `nu`, Corollary 6.3 gives at most one
admissible prefix of fixed total at each residue modulo `3^n`. With the
unnormalized probability Fourier transform,

\[
 \sum_\xi|\widehat\nu(\xi)|^2
 =3^n\sum_r\nu(r)^2\le3^n2^{-\ell}=n^{O(1)}.
\]

After coarse spatial averaging at level `m>=0.9n`, every remaining
frequency induces a suffix conductor at least `m-k-1`, a positive
constant times `n`. The sliced Fourier estimate just proved applies.
Truncation of the total at `6n` costs an exponentially small probability.
Cauchy--Schwarz over at most `6n` clock values and `3^n` residues,
followed by Plancherel, leaves the factor

\[
 6n\sum_\xi|\widehat\nu(\xi)|^2
       \sum_v|\widehat\mu_v(\xi')|^2.
\]

The spatial `3^n` from Cauchy--Schwarz cancels the `3^(-n)` from
Plancherel. All remaining losses are polynomial. Arbitrarily high
polynomial decay in the primary theorem absorbs them.

Projection to level `m` retains the final total: the projected joint
law is `J_m * p_(n-m)`, with convolution only in the clock. Geometric
telescoping of adjacent resolutions uses this final-clock law, not the
shorter total. This proves the claimed (JF) in its stated normalized norm.

## 5. Why an averaged error can produce the claimed individual floor

A bound tending to zero in total variation alone would not justify a
lower bound for every atom of size about `3^(-s)`. PR180 supplies an
additional real-arithmetic smoothing step. This is the essential
interface in this audit.

For a prefix of length `d` and total `A`, let
`omega=3^d 2^(-A)` and `beta` be its real offset. Suppose the chosen
prefixes satisfy `0<=beta<=B`, `omega<=Omega`, and use `L` possible
totals. At a fixed final residue, represented by an integer `M`, every
contributing prefix has an integral inverse representative

\[
 R_w=(M-\beta_w)/\omega_w.
\]

Within one fixed total these integers are distinct. Indeed the offset
numerator recovers the last exponent from its exact two-adic valuation,
then recovers every earlier exponent, with the first fixed by the total.
The representatives lie in an interval of length `B/omega`. Each
residue modulo `3^q` consequently occurs at most
`B/(omega 3^q)+1` times. Multiplication by `omega`, and summation over
the input residues and the `L` totals, proves

\[
 \sup_r\sum_u\left|\sum_w\mathcal T_w H(u,r)\right|
 \le L(B+3^q\Omega)\|H\|_{1,1}.
 \tag{CW}
\]

The clock shift is common within each fixed total and does not change
the sum of absolute values over that clock. The norm here is
`sup_r sum_u`, which suffices; no stronger interchange of those
operations is made.

The selected blocks have lengths `10(j+1)`, total prefix length of
order `N^2`, prefix multiplier at most `(7/8)^d`, bounded real offset,
and only `O(N^2)` possible totals. The compared suffix length is of
order `N`. Thus `3^q Omega` is uniformly bounded, while the positive
retained probability stays bounded away from zero because rejection
probabilities are summable. Applying (CW) to (JF) gives a summable
**supremum over final residues** of the clock-summed errors. This is
the actual justification for the individual floor; the proof never
compares a bare polynomial total-variation error with `3^(-s)`.

## 6. The central-clock floor survives the telescope

Choose an initial selected level and a residue whose clock-summed
normalized density is at least the positive retained mass. A finite
collection of clocks carries at least half that mass. Convolution with
the remaining negative-binomial clock gives a lower bound of order
`1/sqrt(s)` throughout each fixed central window about `2s`, at all
sufficiently large depths. The finitely many initial clock shifts alter
the onset, not the eventual positive lower constant.

For early telescope errors, the remaining clock has length comparable
to `s`, so its maximum atom is `O(1/sqrt(s))`. The sum of their
coefficients is made smaller than a fixed fraction of the main lower
coefficient by choosing the initial level sufficiently late. That
choice is not circular: the main coefficient uses a universal local
limit lower bound and the retained probability, independent of which
finite clocks were selected; those clocks affect only how late the
bound starts.

For late errors use the probability bound one on the remaining clock.
At level `N`, with `s` of order `N^2`, their size after multiplication
by `sqrt(s)` is `O(N^(4-K))`, tending to zero when `K>5`. The same
telescope ends at arbitrary intervening depths, with an additional
error `O(N^(2-K))`. The unrestricted final suffix has only `O(N)`
letters, so its real offset, after multiplying by the selected prefix
multiplier, is uniformly bounded.

Finally, a bounded initial exponent spreads the positive cylinder to
all ternary units, using that two generates the units modulo every
power of three. It changes the final central clock by a bounded amount
and preserves a uniform real-offset bound. This proves (CFJ) with the
normalization

\[
 \sum_{w:\ A(w)=u,\ \beta_w\equiv r\ (3^s)}3^s2^{-u}
 \ge c_0/\sqrt s,
 \qquad |u-2s|\le\sqrt s,
\]

over a finite family whose real offsets are uniformly bounded.

## 7. Positive ordinary realization and collisions at different depths

The fixed-total congruence makes the final inverse value integral and
also makes each earlier prefix integral. Each legal inverse step is
`x -> (2^e x-1)/3`; positivity and integrality force a positive odd
integer. Starting from an odd target, the prescribed exponent is its
exact odd-map valuation. Thus no two-adic completion or nonintegral
history is counted as an ordinary source.

One cannot simply add predecessor counts at all depths of a periodic
target. PR180 first chooses a positive odd ternary-unit parent
`b=(2^e a-1)/3` with `2B<b<=K a`. Among six consecutive choices of
`e` there are exactly two unit parents. At most one is periodic under
the accelerated odd map, since a deterministic cycle has only one
cycle predecessor of its next odd member. Choose the nonperiodic
one. Its forward orbit may eventually enter a cycle; that does not
affect the argument.

With `alpha=log_2 3`, `delta=2-alpha`, and
`L=log_2(X/b)`, choose all integer depths near `L/delta` in a window
of width a constant times `sqrt(L)`. The total
`A_s=floor(L+alpha s)` then lies in the central clock window. Each
word yields a source in `(X/4,X]`, because `b>2B`. There are at
least a constant times `X/(b sqrt(s))` sources at each depth.

Within a depth, the ordinary forward trajectory recovers the exponent
word uniquely. Across two different depths, a repeated source would
make `U^r(b)=b` for a positive `r`, contradicting the choice of `b`.
Adding the order `sqrt(L)` depths therefore gives `cX/b>=c'X/a`.
All onsets depend only on the ratio `X/a`, as claimed in (PD).

For the unit-source conclusion, the map replacing an odd nonunit
`n` by `4n+1` preserves a hit to the unit target by the exact identity
`T^3(4n+1)=T(n)`. It increases height by at most `4n+1` and has
multiplicity at most two when combined with the identity on unit
sources. This proves (PDU), including hits to even unit targets.

## 8. Separate audit of the earlier logarithmic population

The later periodic-approximation theorem only needs the older marginal
population statement (LOG). That statement does not depend on (TF), (JF),
the clock-conditioned local floor, or (PD). Its proof was independently
reconstructed as follows.

Write the marginal atom floor as `D_s(q)>=c_*` for positive unit targets.
For the sum `A_s` of `s` independent geometric letters,
`E[(3/2)^A_s]=3^s`. Therefore, uniformly in the target residue,

\[
 3^s\Pr(A_s>6s)\le9^s(2/3)^{6s}=(64/81)^s.
\]

After an absolute onset, the normalized atom mass at any unit target
with total at most `6s` is at least `c_*/2`. If `b` is a positive odd
nonperiodic unit target, each such length-`s` word gives an actual
positive odd predecessor `n` with

\[
 n<b(64/3)^s,\qquad 1/n>\omega_w/b.
\]

The positivity, integrality and exact-valuation checks are those in
Section 7 above, without a central-clock restriction. Fixed-depth word
injectivity and nonperiodicity of `b` make all these depth sets disjoint.
Summing through depth `floor(log_(64/3)(X/b))` gives harmonic predecessor
mass at least

\[
 \frac{c_*}{2b\log(64/3)}\log X-O_b(1).
\]

For any positive unit target `a=2^v a_0` with `a_0` odd, choose the
three admissible exponents `e,e+2,e+4` for parents
`(2^e a_0-1)/3`, beginning at the least admissible `e>=v+1`.
The largest exponent is at most `v+6`. Two candidates are units, and
at most one is periodic. Each hits `a` after `e-v` ordinary shortcut
clocks and is less than `64a/3<22a`. Choose a nonperiodic candidate `b`.
Thus

\[
 \liminf_{X\to\infty}\frac1{\log X}
       \sum_{n\le X,\ n\to a}\frac1n
 \ge\frac{c_*}{44a\log(64/3)}>0.
 \tag{LOG}
\]

This verifies the named LOG claim at the pinned parent file. Its explicit
clock cutoff is important: merely proving that the harmonic predecessor
sum diverges would not prove a positive limiting logarithmic proportion.
The ratio of `H_X` and `log X` tends to one, so either normalization
gives the same assertion. The unit-source conversion used by the new
periodic-approximation proof is written separately in Section 5 of
[PROFINITE_LABEL_RIGIDITY.md](PROFINITE_LABEL_RIGIDITY.md); it does not
import the later joint-clock population theorem.

## 9. Consequences not licensed by this audit

The derivation supplies a lower population bound for every fixed target
and a common finite-scale onset for any finite collection of targets.
It does not make different nested predecessor basins disjoint. It also
does not turn a forward path's rare marked visits into loss of original
source mass, nor make a source-dependent finite inverse Green column
uniform over moving endpoints.

The first further inference needed for full convergence remains an
upper estimate on an actual surviving source population or on a
corresponding invariant-label charge. The analytic review here accepts
neither such an estimate nor the later potential statements merely
because they occur in the same PR. The checked finite Fourier and
temporal-density theorems in this packet retain their own separate
kernel verification and do not rely on this audit.
