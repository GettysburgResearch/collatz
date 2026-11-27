# Three-term truncation law for the record-alphabet dimension

**Status — PROPOSED.** Let $\alpha=\log_2 3$, $H=\alpha\log\alpha-
(\alpha-1)\log(\alpha-1)$, $\theta=H/\log3$, $u=1-1/\alpha$,
$h=-\log u$ and $\sigma^2=\alpha(\alpha-1)$. With $N_m$ the number
of first-ladder words of odd length $m$, the bounded-alphabet
dimension $d_J$ is given by $\sum_{m\le J}N_m3^{-md_J}=1$.

**Theorem P.** As $J\to\infty$,

$$
 (\theta-d_J)J\log3
 =\tfrac12\log J+\log\log J+\log(h\sigma\sqrt{\pi/2})+o(1).        \tag{P1}
$$

The additive constant is approximately $0.1847310092$.
PR201 obtained the leading term from a classical ladder tail. The
proof here uses an exact first-maximum factorization, Stirling's
formula and uniform irrational-rotation averages. All calculations
concern the universal word alphabet.

## Positive and negative factors of the unrestricted word series

Use formal variables $z,y$ marking length and native clock
respectively. Give gap $e\ge1$ the monomial $zy^e$. Give a monomial
$z^n y^s$ the displacement $\alpha n-s$. Every nonconstant
monomial occurring in the following series has nonzero displacement.
Let $L$ count first-ladder words, so that nonempty proper prefix
displacements are negative and the final one is positive.
Let $Q$ count all words whose nonempty partial displacements are
negative, including the empty word. Let $P$ count the empty word
and all words whose endpoint is their strict maximum including the
initial point. The successive first records decompose such words
uniquely, so $P=(1-L)^{-1}$.

Split any unrestricted word at the unique largest partial displacement,
including the empty and terminal prefixes. The first piece ends at
its strict maximum, and every nonempty prefix of the second has
negative displacement. This is a bijective factorization, hence in
the commutative formal power series ring over $\mathbb Q$,

$$
 (1-z\sum_{e\ge1}y^e)^{-1}=P Q.
$$

Every nonconstant monomial in $\log P$ has positive displacement,
as sums of positive displacements remain positive. The monomials
in $\log Q$ are negative by the same reasoning. Taking formal
logarithms and retaining positive displacements on the left gives
$\log P$ exactly. At fixed $n$ this selected series has only
finitely many clocks $s<\alpha n$, so specialize $y=1$ there.
There are $\binom{s-1}{n-1}$ unrestricted positive compositions.
Their sum through $\lfloor\alpha n\rfloor$ is
$\binom{\lfloor\alpha n\rfloor}{n}$. We obtain

$$
 -\log(1-\sum_{n\ge1}N_n z^n)
      =\sum_{n\ge1}\frac1n\binom{\lfloor\alpha n\rfloor}{n}z^n.     \tag{P2}
$$

This is the word-count form of the ascending ladder
Spitzer–Baxter factorization. The two-variable proof avoids a
probabilistic input. It also gives the exact integer recurrence
$n N_n=B_n-\sum_{k=1}^{n-1}N_kB_{n-k}$ where
$B_i=\binom{\lfloor\alpha i\rfloor}{i}$.

## A local coefficient profile

Set $a_n=e^{-Hn}N_n$, $b_n=e^{-Hn}B_n/n$, and use $A,B$ for
their generating functions in this paragraph and the rest of the
proof. Equation (P2) becomes $1-A=\exp(-B)$. Stirling's formula
with the bounded floor displacement gives uniformly as $n\to\infty$

$$
 n^{3/2}b_n=k(\{\alpha n\})+O(1/n),\qquad
 k(t)=\sqrt{\frac{\alpha}{2\pi(\alpha-1)}}u^t,\quad 0\le t<1.     \tag{P3}
$$

Indeed the entropy exponent at total $\alpha n-t$ is
$Hn-t\log(\alpha/(\alpha-1))+O(1/n)$, and the Stirling
prefactor contributes $\sqrt{\alpha/(2\pi(\alpha-1)n)}(1+O(1/n))$.

Differentiate $1-A=\exp(-B)$ coefficientwise to get

$$
        n a_n=n b_n-\sum_{k=1}^{n-1}a_k(n-k)b_{n-k}.               \tag{P4}
$$

Positivity shows $0\le a_n\le b_n\ll(n+1)^{-3/2}$. In particular
$A(1)$ and $B(1)$ are finite and $D_0=1-A(1)=e^{-B(1)}>0$.
Define the one-periodic function

$$
 \Phi(t)=k(\{t\})-\sum_{j\ge1}a_j k(\{t-\alpha j\}).               \tag{P5}
$$

The series converges uniformly. Each term has at most one
discontinuity per period, so $\Phi$ is Riemann integrable, by
uniform approximation. Substituting (P3) into (P4) gives

$$
 n^{3/2}a_n=\Phi(\{\alpha n\})+o(1),\qquad
 \overline\Phi=\int_0^1\Phi(t)\,dt=D_0\,\overline k,\quad
 \overline k=\frac{1}{\sigma h\sqrt{2\pi}}.                        \tag{P6}
$$

For completeness split (P4), after multiplication by $\sqrt n$,
at $j=M$ and $j=n/2$. The finitely many terms $j\le M$ can replace
$\sqrt{n/(n-j)}$ by one with vanishing error, retaining their exact
rotation arguments in (P3). For $M<j\le n/2$ the contribution is
$O(\sum_{j>M}a_j)$ uniformly. For $n/2<j<n$ it is at most
$C\sqrt n\,n^{-3/2}\sum_{\ell\le n/2}\ell^{-1/2}=O(n^{-1/2})$.
Let $M\to\infty$. Translation invariance of the integral and
$\int_0^1u^t\,dt=(1-u)/h$ give the displayed mean.

Separately the exact support is simple. For $m\ge2$, feasibility
is equivalent to $\{\alpha m\}<\alpha-1$. The last gap is one,
so the preceding $m-1$ gaps must have total
$s'=\lfloor\alpha m\rfloor-1>\alpha(m-1)$; this is that inequality.
Conversely rotate any composition of $s'$ into $m-1$ positive gaps
after the minimum of $S_j-\alpha j$ for $0\le j<m-1$.
All new proper prefix sums are strictly positive, including after
wraparound by positivity of the full sum. Append gap one to obtain
a first-ladder word. Thus at every feasible length
$N_m\ge\binom{s'-1}{m-2}/(m-1)\gg e^{Hm}m^{-3/2}$ by Stirling,
matching the uniform upper bound from (P4). The exceptional $m=1$
has one word. Irrational rotation makes the feasible lengths syndetic.

## The moving truncation window

For fixed real $C$ write
$t=(\frac12\log J+\log\log J+C)/J$. The finite pressure evaluated
here is $S_J(t)=\sum_{n\le J}a_n e^{tn}$. For
$n\le J/(\log J)^2$ the weight tends to one uniformly and the
sum tends to $A(1)$. For $J/(\log J)^2<n\le J/2$, the total is
$O(e^{tJ/2}(\log J)/\sqrt J)=o(1)$.

On the top half, (P6) gives

$$
 \sum_{J/2<n\le J} a_n e^{tn}
       =(\overline\Phi+o(1))\,\frac{e^{tJ}J^{-3/2}}{t}.             \tag{P7}
$$

Here is the averaging detail. Set $\ell=J-n$ and divide by
$e^{tJ}J^{-3/2}/t$. The error $o(1)$ in (P6) is uniform over
$n>J/2$, and the factor $(1-\ell/J)^{-3/2}$ is bounded there.
For fixed $W>0$ terms with $\ell>W/t$ have normalized contribution
$O(e^{-W})$. For $\ell\le W/t$ the factor tends to one uniformly
because $tJ\to\infty$. Irrational rotation gives
$L^{-1}\sum_{j=0}^{L-1}\Phi(x-\alpha j)\to\overline\Phi$ uniformly
in $x$: the claim follows for trigonometric polynomials by geometric
sums, for continuous functions by uniform approximation, and for
Riemann-integrable functions by bounding with continuous upper and
lower functions with integrals arbitrarily close. Thus
$t\sum_{\ell\ge0}e^{-t\ell}\Phi(\alpha J-\alpha\ell)\to\overline\Phi$
uniformly in the starting phase as $t\downarrow0$, by summation by
parts of the bounded partial-sum errors (or split into fixed-length
blocks and then increase their length). Letting $W\to\infty$ proves
(P7). The Riemann-integrable averaging includes exact encounters
with the countable set of jump points.

Since $e^{tJ}J^{-3/2}/t\to 2e^C$, altogether
$S_J(t)\to A(1)+2e^C D_0\overline k$. This is one exactly when
$C=-\log(2\overline k)=\log(h\sigma\sqrt{\pi/2})$. Applying
monotonicity at that constant plus and minus any fixed positive
$\varepsilon$ brackets the actual root to $o(1)$ in the numerator.
Its value is $t=(\theta-d_J)\log3$, proving (P1).

**Classical source.** The factorization behind (P2) is the
ascending ladder transform, also called the Spitzer–Baxter identity.
The local profile, its moving-window average and the particular
dimension expansion above have been derived from (P2).
[Bingham, *Random Walks and Fluctuation Theory*, section 2](https://www.ma.imperial.ac.uk/~bin06/Papers/RWFT.pdf)
