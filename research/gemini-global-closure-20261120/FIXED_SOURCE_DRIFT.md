# The explicit source measure does not retain its initial negative drift

**Status: PROPOSED exact whole-source sign certificate and source-tail reduction.** This continues the actual unsafe-transport proof at scientific commit `a882b449ca7da4a1e7ec42392e0a436611befe9b`. It attempts the source-persistent occupation estimate directly, using one fixed ordinary atomic input. The initial drift is negative, but actual transport reverses its sign at a specified later return. This defeats the proposed reuse of that initial drift; it does not refute the desired long-time occupation estimate, bounded correctors, or Collatz.

## 1. One fixed full-support input

Use exactly A,R,G,U,B,H from `ACTUAL_TRANSPORT.md`, with the quarter-safe region `G={n>1:4R(A(n))<=R(n)}`. The map B applies A once from U, then follows safe states to its first subsequent U state or the absorbing 1. H is the deterministic source-to-endpoint pushforward killed at 1.

Fix

\[
 f_0(u)=\frac{\mathbf 1_U(u)}{u(u+1)},\qquad
 f_j=H^jf_0,\qquad
 \psi(u)=1+\log\log(R(u)+6).
 \tag{1}
\]

This input is positive at every unsafe ordinary source, and its total mass m_0 is at most 1/2. Define

\[
 E_j=\sum_{u\in U}\psi(u)f_j(u),\qquad D_j=E_{j+1}-E_j.
 \tag{2}
\]

Absorbed mass contributes zero. The proved pointwise inequality `psi(Bu)<=psi(u)+log6` and the tail calculation below make every displayed finite-horizon sum finite. No fresh parity bit or replacement input is introduced.

## 2. Complete-source tail for this input

Let M>=1, m=M+1, and put

\[
 g(x)=1+\log\log(x^2+6),\qquad
 S(M)=\frac{g(m)}m+\frac1{m\log m}.
 \tag{3}
\]

The initial mass and psi-moment omitted by restricting sources to u<=M satisfy

\[
 \|f_{0,>M}\|_1\le\frac1m,\qquad
 \|f_{0,>M}\|_\psi\le S(M).
 \tag{4}
\]

**Proof.** The mass bound is the telescoping identity `1/[u(u+1)]=1/u-1/(u+1)`, with the U restriction only reducing the sum. Since R(u)<=u^2, psi(u)<=g(u). Summation by parts gives

\[
 \sum_{n=m}^{\infty}\frac{g(n)}{n(n+1)}
 =\frac{g(m)}m+\sum_{n=m+1}^{\infty}\frac{g(n)-g(n-1)}n.
\]

For x>1,

\[
 0<g'(x)=\frac{2x}{(x^2+6)\log(x^2+6)}
 \le\frac1{x\log x}.
\]

On `[n-1,n]` one has 1/n<=1/x. Thus the second sum is at most

\[
 \int_m^{\infty}\frac{dx}{x^2\log x}
 \le\frac1{m\log m}.
\]

The boundary term at infinity vanishes. This proves (4). QED.

The omitted contribution to the signed drift at time j lies in the asymmetric interval

\[
 \boxed{
 -S(M)-\frac{j\log6}{m}
 \ \le D_j(f_{0,>M})\le\frac{\log6}{m}.}
 \tag{5}
\]

The lower bound uses `D_j>=-||H^j f_tail||_psi`, followed by the actual j-return additive bound. The upper bound uses the pointwise upward increment at most log6 and mass loss at absorption. A killed return has negative drift, so it cannot invalidate the upper bound.

## 3. Exact sign reversal after transport

**Claim FD-001.** The fixed input (1), including every unsafe ordinary source, satisfies

\[
 -0.209006853156\le D_0\le-0.188077839702<0,
 \tag{6}
\]

but

\[
 0<0.000132428698\le D_9\le0.000217170924.
 \tag{7}
\]

The bounds are outward-rounded rational enclosures; their signs do not depend on floating-point computations.

For (6), the checker propagates sources through 256 for one actual B return and applies (5) with j=0. For (7), it propagates all 94,081 unsafe sources u<=262144 through nine actual returns, sums their next signed drift over 4,401 retained endpoints, and applies (5) with j=9. The finite part alone lies in

\[
 [0.000210335930,\ 0.000210335931].
\]

All original sources above 262144 remain included through the analytic bound (5). These are whole-source statements at two particular return times, not a finite-source trend promoted to an all-time claim.

### A visible cause of the reversal

The source 27 follows the exact unsafe-return path

\[
 27\to31\to121\to91\to103\to175\to445\to334\to167
 \to319\to1822.
\]

At the last displayed edge,

\[
 R(319)=1296,\qquad R(1822)=370881.
\]

Different original sources have already merged at 319. The certificate proves

\[
 \frac{f_9(319)}{f_0(319)}>179.503567796332.
 \tag{8}
\]

That ratio uses the transported weights of their original atoms; it is not obtained by reinitializing the seed at 319. The path is finite ordinary arithmetic and is not a nonconvergence witness.

## 4. The exact correlation term omitted by a fresh-source argument

Let

\[
 d(u)=
 \begin{cases}\psi(Bu)-\psi(u),&Bu>1,\\-\psi(u),&Bu=1,
 \end{cases}
 \quad q_j(u)=\frac{f_j(u)}{f_0(u)},\quad
 m_j=\sum_Uf_j(u),\quad \bar d=\frac{D_0}{m_0}<0.
\]

Then the drift splits exactly as

\[
 D_j=\bar d\,m_j+\mathcal C_j,
 \tag{9}
\]

where

\[
 \mathcal C_j
 =\sum_U f_0(u)
 \left(q_j(u)-\frac{m_j}{m_0}\right)(d(u)-\bar d).
 \tag{10}
\]

This is an **unnormalized covariance**, equal to `m_0 Cov_(f_0/m_0)(q_j,d)`. It is well defined because the relevant actual psi-moments are finite. The constant-density replacement `q_j=m_j/m_0` would discard this term and predict negative drift whenever mass survives. Equation (7) disproves that replacement for this particular full-support input.

The same exact certificate gives the quantitative lower bound

\[
 \mathcal C_9>0.002149752028.
 \tag{11}
\]

Indeed m_0<=1/2 and (6) imply `bar d<=2*(-0.188077839702)`, while the finite contribution already gives `m_9>0.005363001119`. Combining the nonrounded interval versions of these bounds with (7) gives (11).

The genuine long-time term is now explicit. Telescoping (2) yields

\[
 \frac1N\sum_{j=0}^{N-1}E_j
 =E_0+\sum_{j=0}^{N-2}
 \left(1-\frac{j+1}{N}\right)
 \bigl(\bar d\,m_j+\mathcal C_j\bigr).
 \tag{12}
\]

To establish the `o(log log N)` occupation estimate, the signed triangular sum on the right must be controlled for this same transported atomic input. The initial negative term supplies no estimate for the accumulated correlation term. The positive value in (11) is a concrete obstruction to setting it to zero or assuming its sign. No general prohibition of amortized cancellation is asserted.

## 5. The infinite original-source tail is already affordable

At any horizon N, split f_0 at its original source M=N. Applying (4) and the actual additive return bound gives

\[
 0\le\frac1N\sum_{j<N}\|H^jf_{0,>N}\|_\psi
 \le S(N)+\frac{(N-1)\log6}{2(N+1)}=O(1).
 \tag{13}
\]

Consequently the desired `o(log log N)` estimate is equivalent to the same estimate for the finite triangular array

\[
 \frac1N\sum_{u\in U,\ u\le N}\frac1{u(u+1)}
 \sum_{\substack{0\le j<N\\B^ju\text{ retained}}}\psi(B^ju).
 \tag{14}
\]

This is a reduction of the analytic source-tail obligation, not a proof of (14). The difficult part is the arbitrarily long actual history of original atoms, including any hypothetical fixed exceptional source; increasing the cutoff does not turn those histories into independent or freshly sampled inputs.

## 6. The occupation target is also a plain ordinary-height target

Put `phi(n)=1+log(log(n+5))`. The proper-rank bounds give

\[
 n+5\le R(n)+6\le(n+5)^2,
 \qquad 0\le\psi(n)-\phi(n)\le\log2.
 \tag{15}
\]

For every actual transported Cesaro measure mu_N,

\[
 0\le\|\mu_N\|_\psi-\|\mu_N\|_\phi
 \le(\log2)\|f_0\|_1\le\tfrac12\log2.
 \tag{16}
\]

Thus the source-persistent `o(log log N)` target is equivalent with phi in place of psi. The moving rank remains useful for defining B, controlling its safe excursions, and proving the domain estimate; it does not provide an additional asymptotic saving merely by changing the occupation gauge. The positive psi-drift in (7) by itself says nothing about the sign of the phi-drift or the success of another bounded corrector.

## 7. Reproducible evidence and its limit

From the repository root, run `python -X utf8 -B research/gemini-global-closure-20261120/check_transported_drift.py`. The checker uses no third-party package and no floating-point operation. It independently reconstructs A and R, physically replays each encountered A word, checks the unsafe guards, transports rational mass inside integer intervals, and includes all omitted original sources through (5).

Every logarithm is enclosed by writing `x=2^k y`, `1<=y<2`, and using

\[
 \log y=2\sum_{r=0}^{31}\frac{z^{2r+1}}{2r+1}+\mathcal R,
 \quad z=\frac{y-1}{y+1}\in[0,1/3],
 \quad 0\le\mathcal R\le\frac9{4\cdot65\cdot3^{65}}.
\]

Integer interval arithmetic at scale 10^32 rounds every multiplication and division outwards. Nested logarithms use monotonicity and the already-enclosed inner argument. Mass intervals likewise enclose the exact rational seed and remain valid under merging. The output in [the drift receipt](../../reports/2026-11-20-gemini-closure/drift-receipt.json) records the signed whole-source intervals, cutoffs, carrier, and code hash. Normal and optimized Python must produce the same receipt; assertions are not used as verification gates.

The remaining work is a rigorous amortized bound for (12), or another pointwise closing mechanism. This pass proves that neither omitted-source mass nor ignorance of the initial drift is the obstacle: the unproved term is the correlation created by the actual successive unsafe returns. No all-time estimate has been obtained.
