# Primitive words force a superpolynomial residual denominator

Date: 2026-11-23. **Status: a written all-word degree theorem, followed by a
source-qualified consequence of PR185's factor-gap theorem.** This is not
a Lean theorem and does not exclude the final integer evaluation gcd.

The new conclusion is qualitative: the denominator remaining after the
complete *polynomial* gcd grows faster than every fixed power of the odd
period. The earlier bound was only a fixed positive power. The proof
keeps arbitrary primitive words and every residual factor. No fixed word
schema, bounded number of terms, or assumption on the factorization of
the complete cycle denominator is made.

## 1. Objects and exact dependency boundary

For a binary word of length \(A\), with \(p\ge1\) odd positions
\(0\le d_0<\cdots<d_{p-1}<A\), put

\[
 F(X)=X^p-2^A,\qquad
 Q(X)=\sum_{i=0}^{p-1}2^{d_i}X^{p-1-i},
 \qquad G=\gcd_{\mathbb Q[X]}(F,Q),
\]

with monic gcd, and define

\[
 F_0=F/G,\quad Q_0=Q/G,\quad n=\deg F_0,
 \quad g=\gcd(A,p),\quad A=ga,\quad p=gb.
\]

Primitivity means that the original binary word has least cyclic period
\(A\). The degree theorem below does not require \(2^A>3^p\).

The structural input is the finite-Fourier argument in PR185, science
commit `e04daab0a0ddd59c80f5d16a51b9943fd5149e6c`,
`research/central-closure-20261123/PRIMITIVE_RESIDUAL_DEGREE.md`,
Sections 1--4. Its exact output is

\[
 b\le n,\qquad
 \operatorname{lcm}\mathcal H=g,\qquad
 \sum_{\substack{h\in\mathcal H\\h>1}}\varphi(h)\le n-b.
 \tag{1}
\]

Here \(\mathcal H\) is the set of orders of the roots of unity
\(\alpha^b/2^a\), as \(\alpha\) runs over every root of \(F_0\).
The principal factor \(X^b-2^a\) supplies \(b\) roots with image one;
the other images contain their complete Galois orbits. The lcm is the
full \(g\) because the normalized coefficient sequence has full Fourier
clock \(p\): a smaller clock would give a proper cyclic period of the
original parity word, including across the wraparound. Thus (1) concerns
the actual primitive word, not an unrelated polynomial period.

For reference, that note's elementary estimate also gives
\(p\le3^{n-1}\). The argument below replaces its product estimate on
the orders by a prime-power budget. No asymptotic result about primes or
permutation groups is used.

## 2. A prime-power budget for a least common multiple

For an integer \(g\ge1\), define

\[
 S(g)=\sum_{\ell^e\parallel g}\varphi(\ell^e),
\]

where the sum has one summand for each prime dividing \(g\). Then (1)
implies

\[
 \boxed{S(g)\le n-b+1\le n.}
 \tag{2}
\]

To see this, assign each maximal prime power \(\ell^e\parallel g\) to
one order \(h\in\mathcal H\) containing that power. For one such order,
the factors \(\varphi(\ell^e)\) are all at least two, with the sole
possible exception \(\varphi(2)=1\). A product of two or more integers
at least two is at least their sum; this follows from \(uv\ge u+v\)
for \(u,v\ge2\), followed by induction. For one factor there is
equality. Hence the sum of the assigned costs at \(h\) is at most
\(\varphi(h)\), except possibly for an extra one if the prime power
two was assigned there. That exception occurs at most once, because the
maximal power of each prime was assigned only once. Summing over the
orders proves (2). Empty assigned sets and \(g=1\) contribute zero.

This is the point where taking the product of *all* the orders wastes
information. A large prime-power factor of their lcm must be paid for at
least once by its own totient; repeatedly counting small shared factors
cannot manufacture a large lcm at negligible cost.

## 3. An elementary Chebyshev bound, with its constant

Write

\[
 \psi(y)=\sum_{\ell^j\le y}\log\ell
 \qquad(y\ge1),
\]

with prime \(\ell\), positive \(j\), and natural logarithms. We need
only the elementary inequality

\[
 \psi(y)\le4(\log2)y.
 \tag{3}
\]

For an integer \(N\ge1\), every prime power in \((N,2N]\)
contributes a factor of its prime to \(\binom{2N}{N}\): in

\[
 v_\ell\binom{2N}{N}
 =\sum_{j\ge1}\left(\left\lfloor\frac{2N}{\ell^j}\right\rfloor
               -2\left\lfloor\frac N{\ell^j}\right\rfloor\right),
\]

every summand is nonnegative, and a prime power in that interval gives
a summand one. Thus

\[
 \psi(2N)-\psi(N)\le\log\binom{2N}{N}\le2N\log2.
\]

Summing on dyadic intervals gives
\(\psi(2^k)<2^{k+1}\log2\). Taking the next dyadic endpoint above
\(y\) proves (3). This deliberately loose explicit constant avoids
any prime number theorem input.

## 4. A quantitative degree bound

Assume first that \(n\ge4\), and put

\[
 y=\sqrt{n\log(2n)}>e.
\]

Split the maximal prime powers \(q_\ell=\ell^{v_\ell(g)}\) into
those at most \(y\) and those greater than \(y\). The first group
contributes at most \(\psi(y)\) to \(\log g\). For the second,
\(\varphi(q_\ell)\ge q_\ell/2\), and \((\log t)/t\) decreases
for \(t\ge e\). Consequently (2) and (3) give

\[
\begin{aligned}
 \log g
 &\le \psi(y)
     +\frac{2\log y}{y}\sum_{q_\ell>y}\varphi(q_\ell)\\
 &\le4(\log2)y+\frac{2n\log y}{y}\\
 &\le\bigl(4\log2+2\bigr)\sqrt{n\log(2n)}\\
 &<5\sqrt{n\log(2n)}.
\end{aligned}
 \tag{4}
\]

The third line uses \(y\le2n\), hence \(\log y\le\log(2n)\).
Also \(\log b\le\log n\le\sqrt{n\log(2n)}\). As \(p=bg\),

\[
 \boxed{\log p<6\sqrt{n\log(2n)}\quad(n\ge4).}
 \tag{5}
\]

In particular, every primitive word with \(p\ge10\) satisfies (5),
since \(p\le3^{n-1}\) rules out \(n\le3\).

Here is an explicit inverse form with no hidden degree-dependent
constant. For \(p\ge10\), put \(L=\log p>1\). If \(n\ge L^2\),
the following inequality is immediate. Otherwise
\(\log(2n)<2\log(2L)\), and squaring (5) gives it directly:

\[
 \boxed{
 n>\frac{(\log p)^2}{72\log(2\log p)}
 \qquad(p\ge10).
 }
 \tag{6}
\]

Thus \(n/\log p\to\infty\), uniformly over all primitive parity
words as \(p\to\infty\). This conclusion is unconditional once the
elementary word/Fourier structure (1) has been established. It does not
depend on Matveev, the factor-gap theorem, or on integer cycle existence.

## 5. Consequence for the complete residual polynomial denominator

Now impose \(D=2^A-3^p>0\), and set

\[
 D_{\rm pol}=|F_0(3)|.
\]

PR185 at the science commit pinned above,
`research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md`,
proves, for a primitive word other than `10` or `01`,

\[
 D_{\rm pol}> (3/2)^{n-1}.
 \tag{7}
\]

**Source boundary for (7):** this is a written theorem of that PR. Its
general factor-gap proof uses its stated two-logarithm lower bound and
finite exact continued-fraction certificate. This note inspected the
proof and statements; it does not claim a new end-to-end Lean proof or
a fresh replay of the inherited certificate. Formulae (1)--(6) above
do not use that external logarithmic-form input.

Combining (6) and (7), for \(p\ge10\), gives the new uniform bound

\[
 \boxed{
 \log D_{\rm pol}>
 \log(3/2)\left(
 \frac{(\log p)^2}{72\log(2\log p)}-1\right).
 }
 \tag{8}
\]

In particular, for every fixed \(K>0\), there is a threshold \(p_K\)
such that **every** primitive positive word with \(p\ge p_K\) obeys

\[
 \boxed{D_{\rm pol}>p^K.}
 \tag{9}
\]

The threshold is uniform in the word and in \(A\); it comes directly
from the displayed elementary function in (8). The degree statement and
its proof have no unquantified dependence on a changing polynomial
dimension.

## 6. What this does and does not force at the integer fiber

No cancellation is omitted. The actual reduced rational denominator is

\[
 q=\frac{D_{\rm pol}}{\gcd(D_{\rm pol},Q_0(3))},
 \qquad
 D\mid Q(3)\Longleftrightarrow D_{\rm pol}\mid Q_0(3).
 \tag{10}
\]

An integer cycle must therefore absorb a superpolynomial amount of
integer gcd *after* all structural polynomial factors have already been
removed. Equation (9) supplies a substantially larger target for a
distinguished-fiber gcd argument; it is not such an argument by itself.

For comparison, along any hypothetical sequence of primitive integer
cycles with \(p\to\infty\), the standard two-logarithm minimum estimate
bounds the minimum \(m\) by a fixed power of \(p\). Here is the exact
dependency and comparison. Multiplying the ordinary odd edges gives

\[
 2^A=3^p\prod_{i<p}\left(1+\frac1{3x_i}\right)\le4^p,
 \qquad
 0<\Lambda=A\log2-p\log3\le\frac p{3m}.
 \tag{10a}
\]

Thus \(A\le2p\). Matveev's fixed two-logarithm specialization supplies
absolute effective \(c,K>0\) with \(\Lambda\ge cA^{-K}\), so

\[
 m\le \frac{pA^K}{3c}\le\frac{2^K}{3c}p^{K+1}.
 \tag{10b}
\]

The exact inherited source is PR175 at
`8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`,
`research/lean-global-closure-20261121/closing/ZERO_ATOM_CLOSING_ATTEMPT.md`,
Section 3 and its source pin to PR183
`68345f60a4f757acb42a69a4ac95910f8ce26163`,
`research/profound-step-20261122/arithmetic/FREE_EXPONENT_CYCLES.md`,
Section 4. The primary input is Matveev, *An explicit lower bound for a
homogeneous rational linear form in the logarithms of algebraic numbers.
II*, Corollary 2.3, <https://www.mathnet.ru/eng/im314>.
This comparison uses that source-qualified estimate; it is not another
proof of Matveev's theorem.

Accordingly, (9) makes the required integer gcd larger than every fixed
power of \(m\) along such a sequence. Rotate the word to its minimum
before writing \(Q_0(3)/F_0(3)=\pm m\). This does not alter \(G\),
\(n\), or \(D_{\rm pol}\): one-letter rotations satisfy
\(2Q_{\rm rot}=Q\) or \(2Q_{\rm rot}=XQ-F\), and \(X\) is
coprime to \(F\). No conclusion that a large gcd is impossible follows
merely from this small quotient. In particular, (10b) is a bound on the
minimum, not on the coefficient height of \(Q_0\) or on the largest
cycle state.

PR182's high rational-cycle construction at
`aa12c13601cacec2c8496f1349b4947457dc1b45`,
`research/high-variance-20261123/CYCLE_IDEAL.md`, remains compatible with
(8)--(10). It prescribes cancellation modulo a selected \(M\) while
retaining a failed extra prime. It neither bounds the complete
post-evaluation gcd nor disproves (9).

The remaining exact line is still a strict bound at the same evaluation
ideal for every prime power dividing \(D_{\rm pol}\):

\[
 \log\gcd(D_{\rm pol},Q_0(3))<\log D_{\rm pol}.
 \tag{11}
\]

This note proves (6), and proves (8)--(9) from the explicitly identified
written factor-gap theorem. It does not claim (11), nontrivial-cycle
exclusion, or the full Collatz conjecture.
