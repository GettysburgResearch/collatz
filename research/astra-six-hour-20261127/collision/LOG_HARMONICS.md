# Cancellation of growing logarithmic harmonics in the original clipped energy

Use the same odd map, representatives and first-hit conventions as in
[the source occupation bound](SOURCE_OCCUPATION.md). Put
\(\chi_m(y)=\exp(2\pi i m\log_2 y)\) for an integer \(m\),
\(\alpha=\log_2 3\), \(\lambda_m=\exp(2\pi i m\alpha)\), and
\(s=H_2(\log_3 2)-\gamma\), with the interval-compression saving
\(\gamma>0\). Write \(\|t\|\) for distance to the nearest integer.

**Proposed, source-qualified theorem.** There are an absolute \(K\) and
a sequence \(\epsilon_k\to0\), independent of the frequency, such that
for every nonzero integer \(m\),
\[
 \left|\frac1k\sum_{\substack{0<y<2\cdot3^k\\y\ {\rm odd}}}
       \Phi(u_k(y))\,\chi_m(y)\right|
 \le \epsilon_k+
 K\left(\sum_{C\ {\rm escaping}}\Phi(H_C)\right)
 \min\!\left(1,\frac{1+|m|^s}{k\,\|m\alpha\|}\right).                  \tag{1}
\]
In particular there is genuine cancellation at every fixed nonzero
frequency and along every sequence with
\((1+|m_k|^s)/(k\|m_k\alpha\|)\to0\). The ordinary clipped law of
\(\log_2 y\bmod1\), with weights \(\Phi(u_k(y))/k\), tends weakly to
Haar measure times \(\sum_C\Phi(H_C)\), even allowing ordinary escape.
The frequency window includes nonresonant modes growing proportionally
to \(k\), since \(s<1\).

## Uniform orbit estimate

At each odd step the integer exponent drops out of the logarithmic
character:
\[
 \chi_m(Ux)=\lambda_m\chi_m(x)
          \exp\!\left(2\pi i m\log_2(1+1/(3x))\right).
\]
Consequently the one-step defect has magnitude
\(O(\min(1,|m|/x))\). On any simple finite odd-path segment
\(x_0,\ldots,x_{n-1}\), the translated-interval counting argument in
(2) of [the occupation theorem](SOURCE_OCCUPATION.md) gives, uniformly
in the segment,
\[
 \sum_{i<n}\min(1,|m|/x_i)\ll 1+|m|^s.
\]
There are \(O(1+|m|^s)\) sites through \(|m|\). In the dyadic shell
\(2^j|m|<x_i\le2^{j+1}|m|\), the contribution is
\(O(2^{-j} (2^j|m|)^s)\). This is summable because \(s<1\).
For an arbitrary complex sequence,
\[
 (1-\lambda)\sum_{i<n}z_i=z_0-z_n+\sum_{i<n}(z_{i+1}-\lambda z_i).
\]
Take \(z_i=\chi_m(x_i)\), with \(x_n=Ux_{n-1}\) if \(n>0\). The
orbit sum is therefore \(O((1+|m|^s)/\|m\alpha\|)\), as well as at most
\(n\); \(\lambda_m\ne1\) by irrationality of \(\alpha\).
The same bounds hold after multiplying by a nonincreasing sequence
of survival factors in \([0,1]\), by summation by parts on prefix
sums. Earlier finite-block phase discrepancy and qualitative leading-word
occupation results use the same rotation at fixed ordinary sources.
Here the truncated size of the phase defect gives a power saving in
the *growing frequency* before applying the original clipped trace.
[Round twelve, earlier phase-discrepancy estimates and references](../../astra-global-closure-20261124/round12/trace/README.md)

## Uniformity of the transfer to the clipped law

Choose one odd ray \(a_{C,n}\) in each escaping component, with start at a
positive ternary unit. The proof of the original clipped energy limit gives
the following total-variation comparison on the countable odd labels:
\[
 \left\|\frac1k\sum_{0<y<2\cdot3^k,\ y\ {\rm odd}}\Phi(u_k(y))\delta_y
       -\sum_C\frac{\Phi(H_C)}k\sum_{n<k}\delta_{a_{C,n}}\right\|_1
 \longrightarrow0.                                                     \tag{2}
\]
For precision, exhaust by the trajectories through a fixed \(M\).
Outside them the first-hit clip costs \(O(M^{-\eta})\) after division
by \(k\), by the complementary first-hit cap and the harmonic first
moment. Among the finitely many remaining escaping tails, the uniform
grade profile and its two tails permit replacing the weights on the
first \(k\) sites by \(\Phi(H_C)\) with *sum of absolute errors* \(o_M(k)\).
The future beyond \(k\) costs \(o_M(k)\) by the positive-lag profile
and the harmonic bound. The first \(k\) sites lie below the representative
cutoff for large \(k\) by \(a_{n}+1\le(3/2)^n(a_0+1)\).
Finite heads, finite cycles, and the initial segments needed to align
different choices of rays cost \(o_M(k)\). The entire lap correction
costs \(o(k)\), and \(\sum_C\Phi(H_C)<\infty\). Increasing \(M\)
proves (2). Thus the same \(\epsilon_k\) works for *all* test functions
of sup norm at most one. Apply the finite orbit bound to the second
measure in (2). This proves (1). Trigonometric polynomial approximation
gives the stated weak limit. [PR 193, original two-copy profile, equations (3), (8)–(11)](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/COLLISION_ENERGY.md)

## Resolution of the dyadic residue witness

On odd sites the signed test from the preceding paper has the exact
expansion
\[
 W(y)=-\tfrac34\cos(2\pi(y-1)/4)+\tfrac12\cos(2\pi(y-1)/8).
\]
Fix either frequency \(\beta=1/4,1/8\). On \(R\le y\le R+L\), take
an integer \(m=\beta R\log2+O(1)\). A phase factor of modulus one aligns
\(\chi_m(R)\) with \(\exp(2\pi i\beta R)\), and Taylor's formula gives
\[
 \sup_{R\le y\le R+L}
   |\exp(2\pi i\beta y)-c_R\chi_m(y)|
       \ll (L+L^2)/R\qquad(1\le L\le R/2).                              \tag{3}
\]
One of the two consecutive choices of \(m\) has
\(\|m\alpha\|\ge\|\alpha\|/2\). Thus a small divisor can be avoided in
this local approximation. The requisite mode is still of order \(R\).

Equation (1) controls a global character. Multiplying it by a sharp
height-window indicator creates another error in the orbit telescope,
the total variation of that indicator along the actual orbit.
For \(R\) large and \(L=o(R)\), no two consecutive odd iterates can
belong to \([R,R+L]\). At an exponent-one step the ratio is at least
\(3/2\), and at an exponent of at least two it is at most
\(3/4+1/(4R)\). The variation on a simple path is therefore twice its
number of visits up to endpoint errors. The present bound on this term
has the order of the mass being estimated. Packing already disposes
of one window of cost \(o(k)\) by the occupation theorem. It gives no
sublinear total cost for windows scattered along an escaping ray.
This is the unresolved part of transfer from (1) to the actual modulus-eight
test, even when the choices of frequencies in (3) are nonresonant.
