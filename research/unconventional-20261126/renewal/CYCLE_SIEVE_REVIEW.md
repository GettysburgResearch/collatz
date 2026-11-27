# A shorter congruence patch for high-minimum rational cycles

**Status — PROPOSED extension following independent review.**
This strengthens the swap argument in
[the cycle-index packet](../adelic/CYCLE_INDEX.md), initially reviewed
at SHA-256 2fa0db4b7221dd782f4e28cd9c548a1c045092600061bb6c93e4e51fbf0fe1ec.
That version obtains a patch of $O_K((\log(2Y))^2)$ blocks and
growing-prime cutoff $n^a$ for $a<1/4$. Below all residues occur
with $O_K(\log(2Y)\log\log(3Y))$ complete blocks. The exponent range
in its high-minimum theorem (7) and its least-period construction
therefore extends to **every $0<a<1/2$**.

## A uniform Fourier estimate

Let $K\ge2$, $Y\ge2$, $\gcd(Y,6)=1$ and let $t_j$ be units
modulo $Y$ obeying $3^{q_j}t_{j+1}=2^K t_j\bmod Y$ for some
$1\le q_j\le K$ on consecutive indices. Define

$$
 H=1+\lceil\log_3Y\rceil,\quad M=3^K+2^K,\quad
 \eta=1/(2M),\quad \rho=\cos(\pi\eta)<1.
$$

Take $t$ to be any positive integer large enough that
$2MH\rho^{t/2}\le1/4$. For example one may take the ceiling of
$2\log(8MH)/(-\log\rho)$, increased to one if necessary. Over
$t(H+1)$ consecutive indices the subset sums of the $t_j$ cover
**every** residue modulo $Y$; in fact fair independent switches
give each residue probability at least $1/(2Y)$.

At a character $u\bmod Y$, the Fourier magnitude of each switch
is $|\cos(\pi y_j/Y)|$ where $y_j$ is the centered integer
representative of $u t_j$ modulo $Y$ in $(-Y/2,Y/2]$. Work first
on a window of $H+1$ successive indices with $H$ transitions.
Encode it by the integer vector

$$
        z_j=(3^{q_j}y_{j+1}-2^K y_j)/Y,\qquad |z_j|\le M.
$$

For two characters having the same vector, subtraction gives
$3^{\sum q_j}(y_H-y'_H)=2^{KH}(y_0-y'_0)$ in local window
indices. Coprimality forces $3^{\sum q_j}\mid(y_0-y'_0)$.
The modulus exceeds $Y$, and the absolute difference is smaller
than $Y$, so the first centered representatives coincide.
The first $t_j$ of this window is a unit modulo $Y$, hence the
characters themselves coincide. In particular only the zero
character can have the all-zero vector.

A nonzero $z_j$ requires $|y_j|\ge\eta Y$ or
$|y_{j+1}|\ge\eta Y$, since otherwise its numerator has absolute
value less than $Y/2$. Each index can account for at most two such
transitions. If $r$ entries of the vector are nonzero, at least
$r/2$ Fourier factors are bounded by $\rho$. The map to vectors
is injective, and at most $\binom Hr(2M)^r$ vectors have support
of size $r$. For the product $P(u)$ of Fourier magnitudes on
this window we obtain

$$
 \sum_{u\ne0} P(u)^t
 \le (1+2M\rho^{t/2})^H-1
 \le e^{1/4}-1 < 1/2.                                             \tag{C1}
$$

Now partition the whole patch into $t$ disjoint windows of $H+1$
factors each. Ignore their connecting transitions in the vector
encoding. Each window separately satisfies (C1), with its actual
starting unit and its own variable grades. Hölder's inequality
on the **same** nonzero characters gives

$$
 \sum_{u\ne0}\prod_{i=1}^t P_i(u)
   \le\prod_{i=1}^t\bigg(\sum_{u\ne0}P_i(u)^t\bigg)^{1/t}<1/2.
$$

The zero Fourier mode is one. Inversion gives every residue the
claimed probability, regardless of a fixed additive contribution
from the unpatched part. The patch length is
$O_K(\log(2Y)\log\log(3Y))$. For $Y=1$ no switches are needed.

## The growing sieve

In the cycle-index construction $Y$ is the full part of
$D=2^n-3^p$ supported at the tested primes (excluding its trivial
2- and 3-parts), and $K$ is fixed before $n\to\infty$.
Yu's prime-uniform bound at degree one gives
$\log(2Y)\ll_S n^{2a}(\log(2n))^{O(1)}$ for the primes at most
$n^a$ together with a fixed finite set $S$. Thus for every
$a<1/2$ the new patch uses $o(n)$ bits. Block grades, minimum
height, real spacing and least period are preserved. The entropy
count discards only $o(n)$ free positions at fixed $K$. To retain
the zero lower rate for high denominator weights at repeated
periods, use an intermediate $a<b<1/2$ and the same multiple
$L=\lfloor n_0^{(b/a-1)/2}\rfloor$ as in the original proof.

A logarithmic endpoint variant follows directly from the displayed
formula on printed pages 241–242 of Yu. At degree one set both
height parameters to $C(1+\log\ell)$ for the rational bases
$2,3$ at primes $\ell\ge5$. The product of these parameters
cancels the denominator $(\log\ell)^2$ up to an absolute bound,
and the last maximum in the constant is $O(1+\log\ell)$. It gives

$$
 v_\ell(2^n-3^p)\ll \ell(1+\log\ell)\log(2n).
$$

Using the elementary Chebyshev estimate
$\sum_{\ell\le X,\ \ell\ {\rm prime}}\log\ell\ll X$, we get
$\log(2Y)\ll_S X^2\log(2X)\log(2n)$ for primes up to $X$.
For every fixed $\varepsilon>0$, taking
$X=\sqrt n/(\log(2n))^{3/2+\varepsilon}$ still makes the patch
$o(n)$, so the same nearcritical least-period construction
satisfies this stronger cutoff. For the repeated-period
zero-exponent lower rate with this cutoff, construct first with
$\varepsilon/2$ in place of $\varepsilon$ at period $n_0$,
and take $L=\lfloor(\log n_0)^{\varepsilon/2}\rfloor$.
Then $\sqrt{Ln_0}/(\log(2Ln_0))^{3/2+\varepsilon}$ is eventually
below the stronger cutoff at period $n_0$, while $s/L\to0$.
All constants may depend on the chosen exponent tolerance and $K$.
[Yu, section 0.1](https://www.numdam.org/article/CM_1994__91_3_241_0.pdf)

The proof controls divisors with $\log(2Y)\log\log(3Y)=o(n)$.
The full positive nearcritical determinant has $\log D$ comparable
to $n$, so this does not provide the missing ordinary cycle condition
$D\mid A(w)$.
