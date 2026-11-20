# Two expanding macros reduce exactly to a restricted ceiling orbit

**PROPOSED exact normalization; no all-source termination theorem is claimed.**
Inputs are the two independently certified macros in
the neighboring `expanding_return_certificate.json`:

$$
M=2^{38}=274877906944,\quad K=3^{24}=282429536481,\quad
D=K-M=7551629537,
$$
$$
C_0=610948284866,\qquad C_1=613397164994,
$$
with maps $a\mapsto(Ka+C_i)/M$, and safe source classes
$210578993150\pmod{2M}$ and $341135408638\pmod{2M}$, respectively.
Both displayed residues are positive and less than $2M$.

## 1. An exact common congruence

Put

$$
\Delta=C_1-C_0=2448880128=2^9 3^{14},\qquad
a_*=1714077182,\qquad c=5285712575.
$$

Direct integer identities give

$$
Da_*+C_0=\Delta c,\quad
Da_*+C_1=\Delta(c+1).                                  \tag{1}
$$

Every safe source is $510\pmod{512}$, as is $a_*$. Every macro endpoint
is $C_0M^{-1}\pmod{3^{14}}$, because $3^{14}\mid K$ and
$3^{14}\mid(C_1-C_0)$. Equation (1) shows that this latter residue is
also that of $a_*$, since $D\equiv-M\pmod{3^{14}}$.

Consequently, along any infinite safe macro path,

$$
a_n\equiv a_*\pmod\Delta\qquad(n\ge1).
$$

The integers

$$
b_n=(a_n-a_*)/\Delta\qquad(n\ge1)
$$

are positive: every continuing safe source is at least 210578993150,
which exceeds $a_*$. Substitution gives the consecutive-digit recurrence

$$
\boxed{M b_{n+1}=K b_n+c+\varepsilon_n,\qquad
       \varepsilon_n\in\{0,1\}.}                     \tag{2}
$$

Conversely, any infinite positive ordinary integer solution of (2) gives a
safe macro path by $a_n=a_*+\Delta b_n$. The affine equations follow from
(1). Each $a_{n+1}$ is even, so
$Ka_n+C_{\varepsilon_n}\equiv0\pmod{2M}$. Since K is odd, this selects
exactly the corresponding certified safe source residue. Positivity and the
fact that the residue lies in $(0,2M)$ imply the nonnegative cylinder
parameter. Thus existence of an infinite positive macro path is equivalent
to existence of an infinite positive integer solution of (2).

## 2. The exact remaining arithmetic problem is a ceiling-map restriction

Both $c$ and $c+1$ belong to $[0,M-1]$. Therefore (2) is equivalent to

$$
b_{n+1}=\left\lceil\frac KM b_n\right\rceil,
\qquad
d(b_n):=M\left\lceil\frac KM b_n\right\rceil-Kb_n
        \in\{c,c+1\}.                                \tag{3}
$$

The ordinary ceiling map itself is total; the two allowed remainder values
are the restriction. The missing theorem is that **every positive integer
orbit of this exact ceiling map eventually has a remainder outside
$\{5285712575,5285712576\}$**.

Every finite prescribed binary word in (2) is realizable by a positive integer
source. Indeed, for a word of length h,

$$
M^h b_h=K^h b_0+
 \sum_{j=0}^{h-1}K^{h-1-j}M^j(c+\varepsilon_j),
$$

and the last integrality congruence selects a unique class for $b_0\pmod{M^h}$.
It gives integrality at each intermediate by reduction modulo M and induction.
Positive representatives remain positive because every affine offset is
positive. A finite forbidden-word argument alone therefore cannot establish
the missing all-source theorem.

## 3. The narrow real shadow is only a necessary condition

Reindex the normalized tail from zero, and write $\lambda=K/M$.
Along a hypothetical infinite path the real limit

$$
\beta=\lim_{n\to\infty}\lambda^{-n}b_n
      =b_0+\frac1K\sum_{j\ge0}(c+\varepsilon_j)(M/K)^j
$$

exists, and

$$
\beta\lambda^n-b_n\in
\left[\frac cD,\frac{c+1}D\right]\subset(0,1).           \tag{4}
$$

Thus the fractional parts of $\beta\lambda^n$ stay in an interval of
width $1/D$. The same digit series has a different limiting operation in
the 2-adic field: there its negative equals the ordinary integer $b_0$,
because $(M/K)^n b_n\to0$ 2-adically. The real endpoint term instead tends
to $\beta>0$. Convergence in both places does not identify the limits.
Also, condition (4) alone does not imply the two-digit recurrence; it is a
necessary condition, not an asserted equivalence.

As external context, the ceiling-map digit process is the minimal-word
process of rational-base numeration. The 2026 paper by Andrieu, Eliahou and
Vivion, [A Normality Conjecture on Rational Base Number Systems,
arXiv:2510.11723v2](https://arxiv.org/html/2510.11723v2), explicitly states as
Conjecture 1.6 that every positive integer orbit of $x\mapsto\lceil px/q\rceil$
is equidistributed modulo powers of q. That conjecture would rule out (3),
since multiplication by K permutes residues modulo M. It is not a theorem
available for use here. This does not assert that the particular numerical
instance (3) is known to be equivalent to any of the paper's general open
conjectures.

## 4. Scope in the actual least-counterexample argument

The two macros preserve the orientation and advance the physical X arm by
38 shortcut steps. In the intended least-nonconverger setup that X source is
already known to converge. Its finite hitting clock immediately rules out
infinitely many unchanged expanding macro returns: the return bases increase
strictly, whereas after the hitting clock that physical orbit is in $\{1,2\}$.

Thus even a new all-positive-source solution of (3) would not by itself close
the original argument. The remaining issue includes permanent section
avoidance after the known convergent arm has reached its eventual cycle.

No elementary or sourced theorem proving termination of (3) was obtained in
this attack. No large finite exclusion or numerical census is offered as a
replacement. `check_two_macro_normalization.py` verifies the constants and
the two directions on 126 finite prescribed digit words; those checks do not
establish an infinite-schedule exclusion.
