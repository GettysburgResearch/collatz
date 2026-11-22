# Critical affine renewal at the actual escape clock

**Status.** The finite ordinary-orbit clock estimate below is Lean checked.
The support and norm estimates are written proofs. They show an exponential
failure of a proposed uniform conditional-norm extension of a published
mixing theorem. The critical affine-renewal theorem does apply to the
auxiliary law identified below, but its conclusion does not supply the
ordinary-source comparison needed for escape exclusion. No lower bound for
PR180's sibling leakage, and no proof of Collatz, is claimed.

The positive attempt was to obtain PR180's logarithmic sibling leakage from
critical affine renewal. Unlike a general catalogue of possible machinery,
this note specifies the auxiliary law, checks the theorem's hypotheses,
computes its exact likelihood relative to the actual harmonic path law,
and identifies the first missing transfer. The clock theorem is an
interface check for that attempt.

## 1. Every eventual escaping tail lies below the central division clock

Let an actual accelerated odd orbit satisfy

\[
2^{a_i}x_{i+1}=3x_i+1,\qquad a_i\ge1,
\qquad A_s=\sum_{i=0}^{s-1}a_i.
\]

Suppose that \(x_i\ge64\) for \(i<s\), \(x_s>0\), and
\(x_0\le2^c\). Then

\[
\boxed{5A_s\le8s+5c.}                                      \tag{1}
\]

Indeed,

\[
64(3x_i+1)\le193x_i,\qquad
193^5=267785184193<274877906944=2^{38}.
\]

Taking fifth powers gives

\[
2^{5a_i}x_{i+1}^5\le2^8x_i^5.
\]

Multiplying these inequalities, using \(x_s^5\ge1\), and then using
\(x_0^5\le2^{5c}\), proves (1). The file `LowClock.lean` proves precisely
this finite statement from the displayed edge equations and inequalities.
It imports no harmonic envelope, predecessor estimate, or assumption that
Collatz holds.

Every nonrepeating positive-integer orbit eventually avoids each finite
set. Consequently an escaping orbit has one fixed tail with all
\(x_i\ge64\); one fixed integer \(c\) then makes (1) hold for every prefix
of that tail. Its division clock satisfies

\[
A_s\le\tfrac85s+c,
\]

so it eventually lies outside every window \(|A_s-2s|\le C\sqrt{s}\).
This is a statement about each hypothetical ordinary escaping source,
not a statement about a randomly selected starting integer.

There is also a sharper written asymptotic bound. Put \(\beta=\log_2 3\).
The exact edge identity gives

\[
A_s=\beta s+\log_2x_0-\log_2x_s
 +\sum_{i<s}\log_2\left(1+\frac1{3x_i}\right).
\]

For an escaping tail the last average tends to zero, while
\(-\log_2x_s\le0\). Hence

\[
\limsup_{s\to\infty}A_s/s\le\beta.                         \tag{2}
\]

## 2. A conditional ternary norm must grow exponentially there

At length \(s\) and total division count \(A\), the exponent words are
positive compositions of \(A\) into \(s\) parts. There are
\(\binom{A-1}{s-1}\) of them. Their Syracuse affine prefixes map into
\(\mathbb Z/3^s\mathbb Z\); any collisions only reduce the image's size.
The following bound therefore applies to **any** probability law supported
on those words, without needing injectivity or equidistribution.

For \(z=3/8\), the generating sum over all positive words of length \(s\)
is

\[
\sum_{e_1,\ldots,e_s\ge1}z^{e_1+\cdots+e_s}
=\left(\frac{z}{1-z}\right)^s=(3/5)^s.
\]

The number of such words with total at most \(A\) is consequently at most
\((8/3)^A(3/5)^s\). If \(A\le(8/5)s+c\), their ternary image has size

\[
N\le(8/3)^c\rho^s,
\qquad
\rho=\left(\frac{8^8}{3^3\,5^5}\right)^{1/5}<3,             \tag{3}
\]

where the last inequality follows from
\(8^8=16777216<20503125=3^8 5^5\).

Let \(f\) be the density of any normalized law on that image with respect
to uniform probability on the quotient of size \(3^s\). For
\(1<q\le\infty\), Hölder's inequality gives

\[
1\le\|f\|_q(N/3^s)^{1-1/q}.
\]

Together with (3), this yields the explicit estimate

\[
\boxed{\displaystyle
\|f\|_q\ge
(8/3)^{-c(1-1/q)}
\left(\frac3\rho\right)^{s(1-1/q)}.}                       \tag{4}
\]

Here \(\rho\approx2.882048082\), so
\(\log(3/\rho)\approx0.040111108>0\).

In particular, (4) applies to the iid geometric law conditional on the
exact total \(A\). The conditional word law is uniform on the compositions
for **every** geometric parameter: its unconditioned word weight depends
only on \(A\). A geometric change of measure therefore cannot restore
uniform conditional finite-\(L^q\) norms at these clocks.

Using (2) and the same generating argument at
\(z=(\beta-1)/\beta\) gives the sharper asymptotic exponent

\[
\liminf_{s\to\infty}\frac1s\log\|f_s\|_q
\ge(1-1/q)\Delta,
\quad
\Delta=\log3-\{\beta\log\beta-(\beta-1)\log(\beta-1)\}
\approx0.054979473>0.                                      \tag{5}
\]

The fixed rational estimate (4), rather than the decimal values, already
establishes strict exponential growth.

### Exact scope

For a **nonnegative unnormalized** density \(g\) supported on the same
image, the correct bound has its total mass as a factor:

\[
\|g\|_q\ge\left(\int g\right)(3^s/N)^{1-1/q}.              \tag{6}
\]

A bounded real restriction can have very small total mass. Thus these
estimates do not rule out an estimate retaining that mass, a weighted
renewal argument, a localized estimate, or Fourier methods. They give no
lower or upper mass at a prescribed individual ordinary root. A support
bound cannot be substituted for that source-sensitive information.

The point of (4) is specific: the normalized exact-total quotient laws
cannot satisfy uniform finite-\(L^q\) bounds in the eventual escape regime.
Paper 9, Appendix C, Theorem 18 instead treats exact central totals
\(A=2s+O(\sqrt{s})\), with real localization retained. The source already
explicitly excludes arbitrary totals; (1)--(5) explain why the omitted
regime includes every eventual escaping tail. Equation (6) keeps the
distinction between normalized laws and its unnormalized real restrictions.

### A fixed real window also prevents an all-totals extension

One can directly test the real-localized conclusion, without discarding
its mass. Set \(A_s=\lceil\beta s\rceil\) and take the single composition
\((A_s-s+1,1,\ldots,1)\). Its real affine prefix is

\[
B_s=\sum_{j=1}^s\frac{3^{j-1}}{2^{e_1+\cdots+e_j}}
=\frac{3^s}{2^{A_s}}-2^{s-A_s}.
\]

For \(s\ge3\), this lies between \(1/4\) and \(1\): the first term is
greater than \(1/2\) and at most \(1\), and \(A_s\ge s+2\).
The fixed 1-Lipschitz function
\(F(t)=\max\{0,\min\{t,2-t\}\}\), supported on \([0,2]\), therefore has
\(F(B_s)\ge1/4\) on this word. Under the conditional geometric law at
total \(A_s\), the word has probability
\(1/\binom{A_s-1}{s-1}\).

Let \(g_s\) be the unnormalized quotient density with the weight \(F(B_s)\).
Its value at this word's ternary residue, including any other words there,
gives

\[
\|g_s\|_q\ge
\frac{3^{s(1-1/q)}}{4\binom{A_s-1}{s-1}}.
\]

Since \(A_s\le(8/5)s+1\), (3) in particular proves

\[
\|g_s\|_{32}\ge\frac3{32}
 \left(\frac{3^{31/32}}{\rho}\right)^s\longrightarrow\infty.
\tag{6a}
\]

The base exceeds one by the exact integer inequality
\(3^{251}5^{160}>2^{768}\). Thus even the fixed-real-window uniform-norm
conclusion cannot hold at all division totals. This counterexample uses
the critical totals \(\lceil\beta s\rceil\); it does not claim that a
particular ordinary escaping orbit has those exact totals, or rule out
other weights and localized estimates.

## 3. Applying critical affine renewal, with the law kept explicit

Set

\[
\theta=1-1/\beta,\qquad
\pi(e)=(1-\theta)\theta^{e-1},\qquad e\ge1,
\quad f_e(x)=\frac{3x+1}{2^e}.
\]

Then \(\mathbb E_\pi e=\beta\), so the real multiplier
\(M=3/2^e\) has \(\mathbb E\log M=0\). For the affine pair
\((M,Q)=(3/2^e,1/2^e)\), the hypotheses of
Brofferio--Buraczewski--Damek's Theorem 1.1 hold:

- The pairs are iid under this explicitly chosen auxiliary law.
- \(M\ne1\), and the maps with \(e=1,2\) have distinct fixed points
  \(-1,1\), so there is no common fixed point.
- Every polynomial logarithmic moment is finite. For small positive
  \(\delta\) with \(\theta2^\delta<1\),
  \(\mathbb E(M^\delta+M^{-\delta}+|Q|^\delta)<\infty\).
- The multipliers generate a dense multiplicative subgroup of the
  positive reals: otherwise both \(\log2\) and \(\log3\) would be
  integer multiples of one positive number, contradicting unique prime
  factorization. This verifies the theorem's aperiodicity condition.

The theorem supplies an invariant **Radon** measure \(m\), unique up to
scale, whose fixed-ratio annuli satisfy

\[
m\{az<|u|<bz\}\longrightarrow C_+\log(b/a)
\qquad(0<a<b,\ z\to\infty),\quad C_+>0.                  \tag{7}
\]

There is no invariant probability measure in this critical case. Formula
(7) is a vague scaling conclusion for fixed real test sets; it is not a
pointwise density estimate or a ternary-cylinder estimate.

Brofferio's rational-affine Poisson-boundary theorem also applies to the
auxiliary word laws. For the original geometric parameter \(1/2\), the
negative drifts occur at the real and ternary places, giving boundary
\(\mathbb R\times\mathbb Q_3\). For the critical law above, the real drift
is zero, the ternary drift is \(-\log3\), and the dyadic drift is
\(\log3\); the boundary is \(\mathbb Q_3\). This change in auxiliary
boundary does not identify either law with the ordinary-source kernel.

## 4. The first missing transfer in the positive attempt

Let \(G\) be the repo's canonical positive critical harmonic function,
with all its imported construction qualifications. For a legal inverse
word of length \(s\), total \(A\), current root \(n\), and ordinary
ancestor \(p\), its exact Doob probability is

\[
\mathbb P_G(w\mid n)=\frac{3^s}{2^A}\frac{G(p)}{G(n)}.
\]

Relative to the auxiliary critical iid word probability, this is

\[
\boxed{\displaystyle
\frac{\mathbb P_G(w\mid n)}{\pi(w)}
=\left(\frac{3\theta}{1-\theta}\right)^s
 \left(\frac1{2\theta}\right)^A\frac{G(p)}{G(n)}.}          \tag{8}
\]

Illegal words have Doob probability zero. Equation (8) preserves both the
total division count and the actual integer endpoint. Neither factor can
be deleted by invoking a real renewal theorem. At \(A=\beta s\), the
exponential factor before \(G(p)/G(n)\) is
\(\exp(s\{\beta\log\beta-(\beta-1)\log(\beta-1)\})\);
it is not a bounded density comparison.

The attempted positive step was to use the logarithmic scaling in (7) to
compare the finite obstacle at \(n\) with its values at
\(64^j n+(64^j-1)/3\), then pass to the harmonic limit. The **first
unsupported step** is representing, or uniformly comparing, that
specified ordinary-source obstacle functional by the auxiliary invariant
measure in (7). Formula (8) shows exactly the source and clock weights
that such a comparison must keep. The renewal theorem gives no such
identification.

Even after that step, vague convergence against fixed real test functions
would not justify conditioning on a ternary cylinder whose depth grows
with the inverse word. The exponential support deficit in (4) prevents a
repair based on uniform normalized \(L^q\) control. A successful weighted
joint renewal argument would have to retain the actual cylinder mass,
real window, word clock, and endpoint factor in (8). No bound of that
strength was obtained here.

Thus this attempt has not established PR180's positive logarithmic
sibling-leakage bound. What is established is the exact source-clock
interface and an obstruction to one tempting extension of the available
mixing input. The weighted, localized route remains open.

## Sources and qualification record

- S. Brofferio, D. Buraczewski and E. Damek,
  *On the invariant measure of the random difference equation
  X_n=A_n X_{n-1}+B_n in the critical case*, Ann. Inst. H. Poincaré
  Probab. Statist. **48** (2012), 377--395, Theorem 1.1 and hypotheses
  (H), M(δ):
  <https://www.numdam.org/article/AIHPB_2012__48_2_377_0.pdf>.
- S. Brofferio, *The Poisson boundary of random rational affinities*,
  Ann. Inst. Fourier **56** (2006), 499--515, main theorem, pp. 500--501:
  <https://www.numdam.org/article/AIF_2006__56_2_499_0.pdf>.
- LyapunovWeaver, *Ternary Syracuse laws: real localization, clock
  stability, and critical regularity*, rStation paper 9, v2 (25 October
  2026), Appendix C, Theorem 18. This is the named upstream research
  input, not a Lean theorem imported by the certificate:
  <https://rstation.ai/problems/collatz/papers/9>.
- The positive target is PR180, `CRITICAL_BOUNDARY.md`, §6, at
  `a9f471543d7fed0a76f348e6d97a9d6d44fa369e`. The canonical operator and
  source qualifications were also checked against PR175 at
  `f63204765438c83def68154e7f253ee9b660979c` and PR185 at
  `4b0c2c27812db555061f5d9006de82a87e7e364f`.

The support proof and affine-law calculations above are written
mathematics. The Lean audit covers only `division_clock_bound`; it does
not certify the external papers, the norm argument, or any escape
exclusion.
