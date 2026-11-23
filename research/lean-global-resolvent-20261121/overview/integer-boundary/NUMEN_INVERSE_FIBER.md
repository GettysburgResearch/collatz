# A concrete obstruction to the proposed non-Archimedean closing step

Date: 2026-11-23. Written proof and exact finite controls; no global Collatz closure and no new Lean claim.

## Why this was tested

The new full-denominator theorem of PR185 leaves numerical evaluation cancellation open. A suggested high-variance import was the non-Archimedean Tauberian framework in Maxwell Charles Siegel, *$(p,q)$-adic Analysis and the Collatz Conjecture*, arXiv:2412.02902v1. We inspected its definitions and Theorems 2.7, 3.38, and 4.6, rather than relying on the abstract. The elementary construction below prevents using absence of arbitrary 3-adic numen roots as the cycle-closing condition.

The construction uses the inverse branching already proved in PR175's `risk23/InverseBranching.lean`; no priority is claimed for that lemma. The consequence for the numen fibers and the particular converse in the cited thesis is the new calculation here.

## 1. The exact series, and an ordinary inverse ray

Use the shortcut branches

\[
H_0(x)=x/2,\qquad H_1(x)=(3x+1)/2.
\]

For a binary 2-adic integer with infinitely many ones, at positions
$0\le d_1<d_2<\cdots$, define the 3-adically convergent series

\[
\chi(z)=\sum_{i\ge1}\frac{3^{i-1}}{2^{d_i+1}}.                 \tag{1}
\]

This normalization gives $\chi(2z)=\chi(z)/2$ and
$\chi(2z+1)=(3\chi(z)+1)/2$, and $\chi(2)=1/4$ for a finite input.
It is the $\chi_3$ normalization in the cited thesis.

Fix a positive odd integer $q_0$ not divisible by three. At any positive odd unit $q$, there are exactly two exponents in the interval $3\le e\le8$ for which

\[
q'=(2^e q-1)/3
\]

is again an odd integer not divisible by three. They are:

| $q\pmod9$ | The two exponents |
|---:|---:|
| 1 | 4, 8 |
| 2 | 3, 7 |
| 4 | 6, 8 |
| 5 | 3, 5 |
| 7 | 4, 6 |
| 8 | 5, 7 |

Indeed the unit-output condition is $2^e q=4$ or $7\pmod9$, and powers of two over six consecutive exponents run through all six units. The numerator is odd; exact division by three leaves it odd. Moreover $q'>q$, since $2^e\ge8$ and $q\ge1$.

Choose either exponent at every stage, producing $q_{i+1}>q_i$ with

\[
3q_{i+1}+1=2^{e_{i+1}}q_i.                                 \tag{2}
\]

These are genuine ordinary inverse edges: $U(q_{i+1})=q_i$ with exact odd-step valuation $e_{i+1}$. Put

\[
A_i=e_1+\cdots+e_i,\qquad
z=\sum_{i\ge1}2^{A_i-1},\qquad
S_k=\sum_{i=1}^k\frac{3^{i-1}}{2^{A_i}}.
\]

Iterating (2) gives the exact rational identity

\[
\boxed{q_0-S_k=\frac{3^kq_k}{2^{A_k}}.}                    \tag{3}
\]

Since $q_k$ is a 3-adic unit, the right side has exactly 3-adic valuation $k$. Therefore

\[
\boxed{\chi(z)=q_0\quad\hbox{in }\mathbb Q_3.}              \tag{4}
\]

This is an infinite exact construction, not a finite-prefix extrapolation.

## 2. Every constructed input is irrational

Suppose the binary code were eventually periodic. Its gaps between ones would then eventually repeat a block with total bit length $L$ and positive number of ones $P$. At a sufficiently late one-boundary, one repeated inverse block has the form

\[
q_{k+P}=(2^Lq_k-C)/3^P
\]

for a fixed integer $C$. Its unique fixed point is

\[
v=C/(2^L-3^P)\in\mathbb Z_3,
\]

because the displayed denominator is not divisible by three. Repeating the block gives, for every $j\ge1$,

\[
q_k-v=(3^P/2^L)^j(q_{k+jP}-v).
\]

All terms $q_{k+jP}-v$ belong to $\mathbb Z_3$. Hence the fixed rational number $q_k-v$ has 3-adic valuation at least $jP$ for every $j$, and must vanish. The recurrence then makes $q_{k+P}=q_k$, contrary to strict growth.

Thus the binary code is not eventually periodic. Since rational 2-adic integers have eventually periodic binary expansions,

\[
\boxed{z\in\mathbb Z_2\setminus\mathbb Q.}                  \tag{5}
\]

The two independent choices at every stage give distinct binary codes: the first differing exponent gives a differing next one-position. Consequently **each positive odd 3-unit has continuum many irrational numen preimages**, all supplied by genuine increasing ordinary inverse rays.

In particular, choose $q_0=1$ and always take the smaller legal exponent. The first odd inverse states are

\[
1,5,13,277,1477,7877,21005,\ldots.
\]

The value 1 has the forward shortcut cycle $1\to2\to1$, while the constructed code is irrational. This alone disproves the implication that an irrational numen preimage of a positive integer forces that integer's **forward** orbit to diverge.

## 3. The two completions give different values

For this construction, $A_i\ge3i$. The same series also converges in the real numbers, but

\[
0<\sum_{i\ge1}\frac{3^{i-1}}{2^{A_i}}
\le\sum_{i\ge1}\frac{3^{i-1}}{8^i}=\frac15<q_0.             \tag{6}
\]

So the real value and the 3-adic integer value differ. Equation (3) retains the missing positive real tail; it tends to zero only in the 3-adic topology. This is exactly the distinction which must survive in a proposed simultaneous arithmetic and analytic argument.

For every $q\in\mathbb Z_3^\times$ the same residue table, without the ordinary positivity assertions, recursively constructs unit tails and a code satisfying (4). Conversely, the first nonzero term of (1) is a 3-adic unit and all later terms are divisible by three. Thus the infinite-one part of the numen has image exactly

\[
\chi(\mathbb Z_2\setminus\mathbb N_0)=\mathbb Z_3^\times.    \tag{7}
\]

Here the left domain denotes 2-adic integers with infinitely many ones. This surjectivity is a direct proof from (1), independent of the thesis's converse theorems.

## 4. Exact literature boundary

The thesis's Corollary 2.3 (printed p.73) identifies periodic **values** with integer values attained at some rational 2-adic input. In the proof of Theorem 2.7 (printed p.76), a periodic value $\chi(y)$ is used to infer that the particular input $y$ is rational. Existence of one rational preimage does not imply rationality of all preimages. The root-1 construction above is a direct counterexample to that inference and to Theorem 2.7 as printed. Theorem 4.6(ii), printed p.277, explicitly uses Theorem 2.7 in its proof.

We do not claim a review of the full dissertation or a refutation of every Tauberian theorem in it. This is one precise failed implication. Any proposed closing criterion requiring no 3-adic root of $\chi-x$ at all is already false for each positive odd unit $x$, including known terminating nonperiodic values. A useful corrected criterion must retain rational-code restrictions or an additional real-boundary condition.

Primary source: <https://arxiv.org/pdf/2412.02902> (v1; dissertation dated May 2022, uploaded December 2024). Inspected source portions: Lemma 2.4, Corollary 2.3, Theorem 2.7, Theorem 3.38, Theorem 4.6, and equations (4.185)--(4.186). No theorem about unknown positive integer cycles is imported from the disputed converse.

## 5. Return to the full denominator

For a periodic code, the geometric-series sum is rational in both completions. With the chronological word convention used by the repository it is a cyclic rotation of

\[
C_w/(2^A-3^p).
\]

Thus selecting a rational code restores the full numerator divisibility test; arbitrary numen surjectivity has not decided it. After polynomial cancellation, PR185's growing residual factor still has to be tested at its actual integer evaluation:

\[
|F_0(3)|\nmid Q_0(3).
\]

The present construction is not an integer counterexample, a cycle exclusion, or a forward escape. It prevents replacing this particular arithmetic question by a stronger no-root assertion that already fails inside the known basin of 1.

## Verification scope

`check_numen_inverse_fiber.py` checks the six residue cases, two independently selected inverse rays from roots 1 and 7, every exact prefix identity and 3-adic valuation, the initial displayed sequence, and the known forward return of 7 to 1. It also checks the literal finite numen formula independently from the affine recurrence and rejects altered prefixes. It does not prove irrationality or continuum cardinality by computation; those are the written arguments above. No existing Lean module or historical enumeration is rebuilt.
