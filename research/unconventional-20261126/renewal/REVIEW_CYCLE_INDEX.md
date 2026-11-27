# Independent review of the rational cycle-index packet

**Reviewed snapshot.** [CYCLE_INDEX.md](../adelic/CYCLE_INDEX.md)
at SHA-256 2fa0db4b7221dd782f4e28cd9c548a1c045092600061bb6c93e4e51fbf0fe1ec.
I reconstructed sections 1–4, checked the imported prime-uniform
formula on both original printed pages, and replayed the finite
controls. I found no failed estimate in the pinned statements.
A separate [stronger swap bound](CYCLE_SIEVE_REVIEW.md) improves a
genuinely nonsharp step without changing that snapshot.

## Positive rational coding and the exponent upper bound

Rotating a word changes its numerator by the claimed shortcut
recurrence with the **common unreduced** denominator $D$. Since
$D$ is odd, an even first letter forces an even numerator and an
odd letter an odd numerator. Thus each word supplies its own true
parities, and different marked words at fixed $n$ supply different
points. For nonzero grade $D$ is prime to both 2 and 3, so all
cyclic reductions have the same denominator. Positivity requires
$3^p<2^n$. The minimum inequality uses the actual product of
all height ratios, giving
$0<n\log2-p\log3\le n/(3m)$. With the standard fixed-base
two-logarithm lower bound this gives a polynomial bound independent
of $d$ for the real minimum and a polynomial times $d$ bound for
its numerator. At fixed $d$ the parity window length is long enough
to distinguish the numerators. An arbitrary window from the
minimum, even one spanning several laps, ends at least at its start,
and every odd ratio is at most $(3+1/R)/2$. Therefore its weight
is at least $\log2/\log(3+1/R)$ times its length. For $R\ge1$
this proportion is at least $1/2$, as required for the binomial
upper-tail entropy estimate (including equality at $R=1$).
The count of candidate denominators grows subexponentially because
each divides one of at most $n$ integers less than $2^n$. Taking
the maximum of $d^{h_R-s}$ over these divisors proves (5) even
when this exponent is negative.

At fixed finite $S$, the progression $p=Mk+1,n=2Mk$ gives
$D\equiv-2$ at all tested primes $>3$ by Fermat, while
$\binom n{p}=2^{n-o(n)}$. The known ordinary 2-cycle supplies
a positive contribution on even iterates when necessary. The
unrestricted trace identity and the change in convergence radius
at the infinite intersection therefore hold. For the ordinary
Euler product each coefficient is a finite nonnegative integer.
The polynomial bound on marked points gives radius at least one.
The known 2-cycle forces a singularity at one by positivity. If
there are infinitely many distinct cycles, products over arbitrarily
many of them force growth exceeding every possible finite pole
order along the positive radius. Hence the integer-coefficient
Pólya–Carlson dichotomy applies. The finite weighted determinant
follows independently from ordering recurrent cycles and transient
states. [Lagarias, 1990](https://doi.org/10.4064/aa-56-1-33-53)
· [Carlson's original article, translation and facsimile](https://people.math.ethz.ch/~airibar/Polya_Carlson.pdf)

## Real size, separation, and entropy in the constructed family

The continued-fraction denominators can be taken on the lower
side infinitely often. Their errors $\delta$ are positive and
less than $\log3/n$, and every shorter integer linear form has
absolute value at least $\delta$. The prescribed block-boundary
floors keep every cyclic discrepancy bounded at fixed $K$,
including arcs crossing the period boundary. The arc multiplier is
then bounded above and below, because its additional $j\delta/n$
term is bounded as well. Each sufficiently long arc has linearly
many odd letters. Its offset, as a sum of bounded positive suffix
multipliers at those letters times $1/2$, is bounded above and
below linearly. One lap yields $x\asymp_K n/\delta$ uniformly
at every phase.

For a pair of distinct phases, both complementary forms are
nonzero and their sum is $\delta$. If both were nonnegative,
their sum would be at least $2\delta$. The expanding arc therefore
gives real separation at least a constant times the shorter time
$t$ when $t$ is large. In the other range, the two-logarithm
bound gives $|r-1|\gg_K t^{-A}$ because the multiplier is
bounded away from zero and infinity. With $x\gg_K n^2$ the
triangle inequality gives a separation at least
$c_K n^2t^{-A}-C_Kt$. At $t\le c'_K n^{2/(A+1)}$ choose $c'_K$
small, and at larger $t$ use the expanding-arc bound. These
ranges overlap. The finite exceptions to the long-arc linear
offset fall into the former range. Coprimality of $p,n$ forces
least period $n$, since nontrivial repetitions would divide
both. The block-binomial lower entropy holds for both possible
complete grades, and a leftover block costs $O(K)$ positions.

## Growing-prime cancellation and the limiting pressure

A $10$ to $01$ swap in a fixed-grade block changes its affine
numerator by the claimed monomial $2^{jK}3^{p-P_j-1}$. Other
swaps do not change that coefficient because block grades are
fixed. It is a unit modulo the full tested divisor $Y$. On any
run of characters $ut_j$ with small centered representatives,
the relation $3^{q_j}y_{j+1}=2^K y_j$ lifts from residues to
an exact integer equality. Across $h$ transitions this forces
$3^{\sum q_j}\mid y_j$; already $h>\log_3Y$ is impossible at
a nonzero character, since every $q_j\ge1$ and $|y_j|\le Y/2$.
The per-character Fourier bound and $O_K((\log(2Y))^2)$ switches
in the pinned proof therefore handle every residue. Fixing one such
choice for each arbitrary outside word preserves a distinct marked
point per outside word.

I checked the actual displayed inequality of Kunrui Yu on printed
pages 241–242, including the prime-dependent height condition, the
factor $(\ell^{f_\ell}-1)/(\log\ell)^2$, the product of the two
heights and the final maximum. For rational $2,3$, the field degree
and residue degree are one. Heights $C(1+\log\ell)$ satisfy
the stated constraints, the exponent bound is $\max(n,p,3)$,
and $2^n3^{-p}-1$ is nonzero with denominator prime to $\ell$
for every $\ell\ge5$. Thus no fixed-prime constant is being used
nonuniformly. In fact direct simplification gives
$v_\ell(D)\ll\ell(1+\log\ell)\log(2n)$, enough for the original
sum. With $a<1/4$ the original squared-log patch costs $o(n)$
bits. [Yu, section 0.1](https://www.numdam.org/article/CM_1994__91_3_241_0.pdf)

The uniformity in (4) is enough to apply it with
$R=c_K n^2$: the constants in its proof do not grow with $R$.
The discarded denominators $d\le2^{(1-e)n}$ then account for
at most $2^{((1-e)\theta+o(1))n}$ points, strictly fewer than
the surviving free-block entropy after choosing its tolerance.
For $s>\theta$, reusing one fixed cycle works only for a fixed
sieve. The packet instead constructs periods $n_0$ with a strictly
larger prime cutoff and takes $n=Ln_0$ with $L\to\infty$ and
$(Ln_0)^a\le n_0^b$. The denominator weight per repeated period
gives exponent at least $-s/L$. This justifies the asserted zero
lower rate for **marked fixed points**, and does not imply it
for exact periods. The remaining claims distinguish these counts
correctly. The new [near-linear patch estimate](CYCLE_SIEVE_REVIEW.md)
extends the same argument past $a=1/4$.

**Finite replay.** Python source SHA-256
9eed79ed97b4bdf6621dc2bc91f46aef537bdbfff68d4ec7e577e925d7c7cb2b;
replayed output and [CYCLE_CONTROLS.json](../adelic/CYCLE_CONTROLS.json)
both 710f3b8aa0024b296e4b76883ad72eecc5240a808ba111fede0a47b41074038c.
The tests exhaust the 32,766 nonempty binary words through length 14
and replay three specified prime-cancellation examples. They do
not establish Yu's inequality, Fourier mixing at arbitrary moduli
or the limiting pressure. In particular they do not establish
ordinary nontrivial cycle existence or exclusion.
