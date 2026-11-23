# Complete denominator rigidity and the surviving low cosets

23 November 2026. Parent PR182 head:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Status: PROPOSED elementary written theorems with exact finite controls;
one explicitly qualified finite-field estimate. Collatz remains OPEN.**

The previous prime-power exclusions extend to arbitrary complete
denominators. A surviving rational scalar has an explicit bound on
every prime exponent, determined only by its prime support. This gives
finitely many possible denominators for each fixed support. A second
identity excludes all odd denominators on which a power of three equals
two. The remaining low cosets are substantial: an explicit infinite
family survives every ordinary-floor phase test, satisfies all the
forward pressure-clock inequalities, and is approached by actual
positive ordinary sources. Its later integer carries remain the
unresolved arithmetic issue.

## 1. The actual scalar and the review boundary

Throughout, q is a positive odd ordinary integer,

\[
q_i=U^i(q),\quad g_i=v_2(3q_i+1),\quad
2^{g_i}q_{i+1}=3q_i+1,\quad
h(q)=\sum_{i\ge0}\frac{g_i}{3^{i+1}}.
\]

The parent proves

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g_0.                                      \tag{1}
\]

Its exact source is PR182 at the full parent head above,
`research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`, R8-G1--R8-G4,
blob `540110f09cf68e3309fd83fea9c7ae497536ded4`.
The finite phase theorem and pressure maximum are in the same head,
`research/repo-synthesis-round8-20261123/PRESSURE_CONSTRUCTION.md`,
R8-P1--R8-P5, blob `7ef222d23f59a2dffd936dbfa93765df064db166`.
Their independent review blobs are
`934b34035a35debc78a806557380b474cb21ff95` and
`392a9e764020bd8ade2455b1fce875a8354cf686` for the pressure note.

Write a rational scalar in lowest terms as `a/(3^r d)`, `(d,3)=1`.
After r odd steps its fractional parts lie on one coset C of
`<3>` in `(Z/dZ)^*`. For `0<=f<1`, put

\[
m(f)=\begin{cases}f+1,&f\le1/2,\\f,&f>1/2.\end{cases}
\qquad
\mu_d(C)=\frac1{|C|}\sum_{a\in C}m(a/d),\quad
\nu_d(C)=\frac1{|C|}\sum_{a\in C}a/d.                  \tag{2}
\]

Actual values in this tail are `m(f_i)+k_i`, with integer `k_i>=0`.
The closed upper endpoint is deliberate: `m(1/2)=3/2` because the
actual lower bound in (1) is strict.

R8-P1 proves that every phase with mean at least 7/8 is impossible
at a nontriadic actual scalar. Its explicitly verified ordinary floor
`q<=31` strengthens this sufficient mean to 4/5. More generally a
phase of period L and lift sum S is excluded if

\[
(3+1/(Q+2))^L<2^{2S},                                  \tag{3}
\]

where all odd sources at most the odd floor Q have been verified to
reach one. We retain exactly that actual-source theorem and its
finite-floor hypothesis. Denominator statements below concern the
whole reduced residual d, not just one of its factors.

## 2. Full fibers inside a composite denominator

**R9-P1 (complete fiber theorem).** Suppose `d=MD`, `D>1`, `(d,3)=1`,
D and d have the same prime support, and

\[
\operatorname{ord}_{d}(3)=M\operatorname{ord}_{D}(3).    \tag{4}
\]

Every tripling coset modulo d contains all M lifts above every residue
of its projected coset `C_D` modulo D. Its exact lift mean is

\[
\boxed{
\mu_d(C)=
\begin{cases}
1+(\mu_D(C_D)-1)/M,&M\text{ odd},\\
1+(\nu_D(C_D)-1/2)/M,&M\text{ even}.
\end{cases}}                                           \tag{5}
\]

In either case `mu_d(C)>1-1/(2M)`. In particular if M>=4, the complete
denominator d is excluded by the parent phase theorem.

**Proof.** The reduced coset has length `ord_D(3)`. Equation (4)
makes each projected residue occur M times in the original coset;
there are only M residue lifts, so every one occurs. Equal prime
supports ensure that all those lifts are units.

For a base fraction f the lifted fractions are `(b+f)/M`, `0<=b<M`.
Their average is `1/2+(f-1/2)/M`. When M is odd, exactly `(M+1)/2`
need the added one in (2) if `f<=1/2`, and exactly `(M-1)/2` otherwise.
This gives the first line of (5), including its half endpoint. When M
is even and `0<f<1`, exactly M/2 need the added one; this gives the
second line. The strict bound follows from `m(f)>1/2` and `f>0`.
No independence of local prime factors is assumed.

## 3. Explicit exponent caps for every fixed prime support

Write

\[
d=2^a\prod_{p\in P}p^{k_p},\qquad P\subset\{5,7,11,\ldots\}.
\]

For each odd prime in P define the finite exact numbers

\[
t_p=\operatorname{ord}_p(3),\quad w_p=v_p(3^{t_p}-1),\quad
\ell_p=\max_{q\in P\setminus\{p\}}v_p(t_q),\quad
\ell_2=\max_{q\in P}v_2(t_q),                           \tag{6}
\]

where an empty maximum is zero.

**R9-P2 (complete support caps).** If d is the residual denominator
of an actual rational scalar, then

\[
\boxed{k_p\le w_p+\ell_p\quad(p\in P),\qquad
a\le\ell_2+3.}                                         \tag{7}
\]

Thus, for this fixed P, d divides the explicit integer

\[
\mathcal D(P)=2^{\ell_2+3}\prod_{p\in P}p^{w_p+\ell_p}. \tag{8}
\]

This is a finiteness theorem for fixed prime support, not an assertion
that all divisors of (8) can occur.

### Odd exponents

The elementary binomial lifting proof from R8-P4 gives

\[
\operatorname{ord}_{p^k}(3)=t_p p^{\max(k-w_p,0)}.
\]

Orders for coprime moduli combine by their least common multiple.
For `m=d/p^k`, the p-adic valuation of `ord_m(3)` is precisely ell_p:
lifting at any other odd prime q adds powers of q, not of p, and the
binary factor adds only powers of two. Also `p` does not divide t_p,
since t_p divides p-1. Therefore, if `k>w_p+ell_p`, lowering k by one
lowers the complete order by exactly p. R9-P1 applies with `M=p>=5`
and excludes d. This proves the odd-prime part of (7).

Only primes q>p contribute to ell_p, since t_q divides q-1. In
particular the largest odd prime factor p of a surviving d has
exponent at most w_p. The other caps depend on the prime support,
not on any still-unknown exponents at the other primes.

### The binary exponent, including its boundary case

For `a>=3`, `ord_(2^a)(3)=2^(a-2)`. If
`a>=max(5,ell_2+4)`, reducing a by two lowers the complete order by
exactly four. R9-P1 with M=4 excludes d. The only remaining case
needed for (7) is `ell_2=0`, `a=4`.

Write then `d=16m`, m odd. The tripling order modulo m is odd, so
the order-four binary orbit and the orbit modulo m are independent
in the precise Chinese-remainder sense: each pair of local residues
occurs. The two binary orbits are `{1,3,9,11}` and `{5,7,13,15}`.
Fix a residue `c mod m`, represented by `0<=c<m`, and put `f=c/m`.
Its four CRT lifts have fractions `(b+f)/16`, where the b-values are

`r,s,r+8,s+8`, with `0<=r,s<8` and `r-s=2 or 6 mod 8`.

There are two lower-half and two upper-half values, except that a
possible exact half only increases the mean under (2). Their lift
mean is at least

\[
1+\frac{(r+s)/2+f-4}{16}\ge\frac{13}{16}>\frac45,       \tag{9}
\]

because `r+s>=2`. This includes m=1. The verified floor Q=31 in
R8-P1 excludes the remaining case and completes (7).

For example, P={5,11} gives `d|96800`. For P={7,13}, the sharp
support bound is `d|1456`. Section 5 exhibits a low coset at 1456
itself; the support theorem does not remove it.

## 4. The phase defect is an exact doubling difference

**R9-P3.** For odd `d>1`,

\[
\boxed{\mu_d(C)=1+\nu_d(2C)-\nu_d(C).}                  \tag{10}
\]

For even `d>2`, with D=d/2 and the projected coset `C_D`,

\[
\boxed{\mu_d(C)=1+\nu_D(C_D)-\nu_d(C).}                 \tag{11}
\]

Indeed, for a unit fraction f other than one half,

`m(f)-1 = ({2f}-1/2)-(f-1/2)`.

Average this identity. For odd d, doubling permutes the unit cosets;
for even d, its fractional values are the equally repeated projected
orbit modulo D. This proves both formulas with their actual domains.

In particular every odd complete residual denominator with
`2 in <3> mod d` is excluded: then (10) gives mean one in every coset.
Equivalently, this includes every divisor d>1 of any integer `3^j-2`.
This adds cases not explained by complementary pairing; for example
`ord_23(3)=11` is odd, but `3^7=2 mod23`.

Summing (10) around a doubling orbit of cosets makes the defects
telescope. It does not make an individual coset balanced. More
importantly, it does not move an actual ordinary source into a different
coset. The residual denominator and its tripling coset are invariant
on an ordinary forward-meeting component: the exact recurrence changes
only powers of three and integer terms. Multiplying the ordinary
source by two adds one to the full scalar H; it does not double this
coset label. A transport from C to 2C is therefore not supplied by
(10).

## 5. Low phases survive the structural caps and the forward clock

There are infinitely many finite cosets for which even the limiting
version of (3), with `3^L` in place of its left side, fails. These are
not positive ordinary counterexamples. They identify the exact
arithmetic part that the phase argument still needs to control.

### A first low family, including the denominator-eight phase

For N>=2, set

\[
u_N=\frac12+\frac1{3^N-1}.
\]

Its tripling phase has canonical charges `1^(N-1),2`, period N, and
mean `(N+1)/(2N)`. Its reduced residual denominator is `3^N-1` for
even N and `(3^N-1)/2` for odd N. To verify these assertions, its
successive minimum lifts are

\[
\frac12+\frac{3^i}{3^N-1},\qquad 0\le i<N.
\]

They lie strictly between one half and one. Their recurrence has the
stated charges, and summing those charges gives the stated mean.
The values are distinct. At N=2 this is exactly `5/8,7/8`; at N=3
it gives the low phase modulo 13; at N=5 it gives the phase of mean
3/5 modulo 121.

Every cumulative canonical clock is
`A_j=j+floor(j/N)<=j+floor(j/2)<j log_2 3`.
Thus these complete periodic words satisfy every forward coefficient
inequality at the previously selected pressure maximum. They do not
supply the actual escaping product, a maximum, or its inverse-path
inequalities.

### A sharp binary-support family

**R9-P4.** For N>=6, put

\[
D=3^N-1,\qquad d=2D,\qquad c_N=\frac{3^N}{2(3^N-1)}.
\]

The coset `<3>` modulo d has period 2N and lift mean

\[
\boxed{\mu=\frac34+\frac1{4N}\le\frac{19}{24}
<\log_4 3.}                                            \tag{12}
\]

The canonical word starting at c_N is
`1^N,2^(N-1),3`, with total clock `3N+1`. Every one of its cumulative
clocks is strictly below `j log_2 3`.

**Proof.** Modulo D the powers `1,3,...,3^(N-1)` form the full orbit
of length N, and their fractional mean is `1/(2N)`. Modulo 2D the
order is exactly 2N: `3^N=D+1` has order two there. The full two-fiber
formula (5) gives (12). Equivalently, its minimum lifts starting at
c_N are

`1/2+3^i/(2D)` for `0<=i<N`, followed by
`1+3^i/(2D)` for `0<=i<N`.

Their exact recurrence gives the claimed word. Within its first N
steps the mean clock is one; during the next N-1 it increases toward
the full-period mean, and the final charge three makes that mean
`(3N+1)/(2N)`. Every partial mean is no larger. Finally
`3^12=531441>524288=2^19` proves the strict comparison for N=6;
larger N only lower the displayed mean. Repeated complete periods
preserve every strict prefix inequality.

For even N>=6, let b=v_2(N). Then `v_2(d)=b+3`. The odd part of D
has tripling order with binary valuation b: the odd part of
`3^(N/2)+1` is nontrivial, and any prime dividing it has an order
whose binary valuation is exactly b. Thus this family attains the
binary cap `a=ell_2+3` in (7). At N=6 it is d=1456 with starting
phase `729/1456`, period 12, and clock 19.

The same maximum-root scalar ceiling from R8-P5 is also compatible
with the starting values: `u_N<=5/8<H*` and `c_N<5/8` for N>=6.
No powers of three are being cleared in these statements: these
displayed starting candidates already have residual denominator d.
This checks the actual location at which that ceiling would apply;
it does not reselect or move a pressure maximum.

## 6. Positive ordinary compatibility and the first required carry

**R9-P5 (finite ordinary realization).** Each fixed starting phase
u_N or c_N above is a limit of actual scalar values h(q_K) at positive
ordinary sources q_K that realize arbitrarily long complete repeats
of its displayed canonical word. Every finite prefix clock used
above is then a literal ordinary clock. This construction does not
produce one fixed source realizing the infinite word.

For completeness, let the chosen word have length L and total gap A.
Its full affine numerator is

\[
C=\sum_{i=0}^{L-1}3^{L-1-i}2^{A_i}>0,
\qquad q_*=-\frac{C}{3^L-2^A}.                         \tag{13}
\]

Both numerator and denominator are odd. The periodic cyclic shifts
give odd rational intermediate states with exactly the prescribed
binary valuations; they are negative in the ordinary real embedding.
For K word steps, choose the unique positive odd residue q_K below
`2^(A_K+1)` congruent to q_* modulo that power of two. The complete
affine equations show at every earlier step that the difference from
the rational periodic state has binary valuation at least
`A_K+1-A_i`. Hence every prescribed valuation through K is retained.
The orbit from q_K is an actual positive ordinary orbit.

Take K through multiples of L. The ordinary source bound and
`q_(i+1)<=2q_i` give `bl(q_K's K-th state)<=4K+1`, since every
canonical gap is at most three. The exact discounted-tail identity
from (1) therefore gives the concrete error estimate

\[
\boxed{|h(q_K)-u|\le\frac{4K+4}{3^{K+1}},}              \tag{14}
\]

where u is the chosen starting phase (which is below one). The
residue representatives are compatible as K increases and cannot
remain bounded, since their 2-adic limit q_* is a negative rational
number. Thus the positive ordinary sources tend to infinity. This is
a genuine same-word finite source construction, not identification of
an infinite positive source with its negative rational limit.

### A necessary ordinary valuation gate at exact equality

For the first family define the positive odd integers

\[
B_N=3^N-2^{N+1},\qquad C_N=3^N-2^N,
\qquad q_*=-C_N/B_N.
\]

If a positive ordinary q satisfies exactly `h(q)=u_N`, then

\[
\boxed{v_2(B_Nq+C_N)=N\pmod{N+1}.}                     \tag{15}
\]

Indeed the ordinary q differs from the negative rational q_*, so a
first valuation departure occurs. Before it, the actual scalar equals
the canonical minimum lift, with zero extra integer carry. A larger
gap than the canonical gap would make the next scalar fall below its
minimum lift, violating (1). A canonical gap one cannot be replaced
by a smaller positive gap. Thus the first departure replaces one of
the terminal canonical twos by a one. If it follows j complete words,
the valuation of the original rational difference is
`j(N+1)+N`. The odd denominator B_N gives exactly (15).

For N=2 this says `v_2(q+5)=2 mod3`. Its forced gap-one successor n
has `h(n)=7/8` and `n+7=3(q+5)/2`, giving the equivalent gate
`v_2(n+7)=1 mod3` used by the companion return analysis. That analysis
retains arbitrary later integer carries. Equation (15) alone does
not remove them.

## 7. A qualified analytic route for large prime cosets

The finite-field literature applies to this finite modular source,
without identifying it with an actual forward trajectory. Kurlberg,
*Bounds on exponential sums over small multiplicative subgroups*
(2007), [arXiv:0705.4573](https://arxiv.org/abs/0705.4573), Section 1,
gives the standard complete coset estimate

`|sum_(a in C) exp(2 pi i k a/p)|<sqrt(p)` for `k not=0 mod p`.

This particular bound follows from character orthogonality and the
complete Gauss-sum magnitude; no incomplete or mixed-modulus bound
is imported. The [author's PDF](https://people.kth.se/~kurlberg/eprints/short_expsum.pdf)
was directly inspected. Its stronger small-subgroup theorem is not
needed in the following deduction.

**R9-P6 (analytic, prime-only).** For a prime p>=5 and any tripling
coset C of length t,

\[
\boxed{|\mu_p(C)-1|\le
\frac{\sqrt p}{2t}\sum_{j=1}^{(p-1)/2}\frac1j.}          \tag{16}
\]

To check the application, define the sampled centered sawtooth
`f(a)=m(a/p)-1` on nonzero residues and `f(0)=0`. Its zero Fourier
coefficient is zero. Use the unnormalized transform
`F(k)=sum_(a mod p) f(a) exp(-2 pi i k a/p)`, so inversion has the
factor `1/p`. The cyclic first difference has one unit jump,
so the nonzero F(k) have magnitude
`1/(2|sin(pi k/p)|)`. Fourier inversion, the displayed complete
coset bound, and `sin(pi k/p)>=2k/p` for `1<=k<=p/2` give (16)
after pairing k and p-k.

Consequently, if the exact rational comparison

\[
25p\left(\sum_{j=1}^{(p-1)/2}1/j\right)^2<4t^2         \tag{17}
\]

holds, every coset has mean greater than 4/5 and the verified ordinary
floor excludes residual denominator p. This sufficient large-order
condition does not handle the short cosets in Section 5, and it is
not asserted for a composite d by replacing p with d.

## 8. Validation and the remaining step

`phase_controls.py` checks complete mixed-modulus fibers and both
parities of (5), complete support-cap consequences in specified
finite domains, the binary boundary, the doubling identities, exact
low words, literal positive ordinary cylinders, and the first-departure
gate. All arithmetic checks remain active under `python -O`. Its
finite domains corroborate the written universal proofs; they do not
replace them. No full scalar-rigidity theorem is claimed as Lean
formalized by these computations.

The actual pressure-product hypothesis remains exactly the parent's
source-qualified escaping-component construction. Its forward clock
and scalar ceiling are necessary conditions, not a sufficient
realization criterion. The low families meet those numerical
conditions; their negative rational periodic realizations do not
become positive ordinary ones by a limiting argument.

**First unsupported step:** control the later integer carries of one
unchanged positive ordinary source, or construct a different arithmetic
constraint on its actual scalar that excludes the remaining complete
cosets and irrational values. Fixed-support finiteness, doubling
balance across different cosets, and arbitrarily accurate finite
ordinary realizations do not supply that control.
