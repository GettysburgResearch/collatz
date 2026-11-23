# Independent review of primitive residual-denominator growth

Date: 2026-11-23. Reviewer lane: `nov23_surgery`.

**Verdict: PASS as a written theorem with a qualified analytic input and
an exact finite certificate.** This is not a claim of an end-to-end Lean
proof or full cycle exclusion.

## Frozen reviewed inputs

| File | SHA256 |
|---|---|
| `nov23_cycle/PRIMITIVE_DENOMINATOR_GROWTH.md` | `e0921fe30a77472cc6c17477f8e6b9edbc042c5d80ce37b09840310a969b0430` |
| `nov23_cycle/check_factor_growth_gap.py` | `ce0461731035a067b03b1a1e155aa8c07d0b29ac46c2fc5790cb3cd898238d43` |
| `nov23_cycle/factor-growth-gap-certificate.json` | `4e6f116d47c09806265b19b353d3d488cd57a4c3f04b9fa7b04fe49e7680e554` |
| `nov23_surgery/PRIMITIVE_RESIDUAL_DEGREE.md` | `ef823ecb00302060890f0858e1713ac967c11cbfd31723a8fe47f43402ab5b7b` |

The reviewer co-developed the last structural degree theorem. The
independent scope here is the cycle lane's value-growth proof, its
analytic specialization, its finite/infinite coverage, and its coupling
to the explicitly stated degree conclusion. The root agent and cycle
lane separately reviewed the degree theorem.

## 1. Root support and the correct norm exponent

For a monic integer factor $P$ of $X^p-2^A$, all roots have modulus
$r=2^{a/b}$. The constant coefficient forces $b\mid\deg P$. Root
conjugation gives

\[
X^dP(r^2/X)=P(0)P(X).
\]

Comparing nonzero symmetric coefficients forces $b\mid2i$.
Therefore, for $e=\gcd(b,2)$, the factor has the form
$P(X)=H(X^{b/e})$. The roots of $H$ have modulus $2^{a/e}$,
and there are exactly $ed/b$ of them with multiplicity. Thus the
reverse-triangle bound has the stated exponent $ed/b$.

This reconstruction does not use irreducibility of a homogenized
cyclotomic substitution. In particular the possible partial splitting
when $b$ is even has been retained correctly.

## 2. Uniform gap: complete coverage

Assuming failure of the claimed gap and $b\ge14$ gives
$a<2b$ from $3^q+(3/2)^q<4^q$, with $q=b/e\ge7$.
The nonzero quantity is $\varepsilon=2^a3^{-b}-1$.

I checked the real-field formula in Bugeaud--Mignotte--Siksek,
Theorem 9.4, against the primary Annals PDF, including its height
definition on the preceding page. With $n=2,D=1$, heights $1,2$,
and maximum exponent at most $2b$, the chosen constant $10^{10}$
dominates the theorem's numerical prefactor. No GRH or Collatz
assumption is used in this specialization.

Primary source:
<https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf>.
This validates the application of the published theorem, not a new proof
of Matveev's bound.

The assumed gap gives
$\log\varepsilon<2-b/3$. At $K=10^{12}$ the exact inequality
$K/3-2>31\cdot10^{10}$ holds. The function comparing the two sides
is increasing above $K$, since its derivative is
$1/3-10^{10}/b>0$. The certified bound $\log(2K)<30$ then excludes
the full infinite tail.

For $14\le b<K$, the approximation error is strictly below
$3/(b2^{b/2})<1/(2b^2)$. The two parity base cases $b=14,15$ and
the induction by two cover every integer in this range. Coprimality
of $a,b$ makes Legendre's criterion applicable.

The rational logarithm enclosure has the correct first omitted term
$2z^{257}/257$ and its geometric tail bound. The common continued
fraction is continued beyond the cutoff, to denominator
$5409303924479$. Consequently the twelve reported upper convergents
are a complete list below the cutoff. Among them, denominator 41
is checked by the exact integer gap inequality. The other nine
denominators at least 14 are all at least 306, so their putative
gap would force $\tau<2^{-152}$, contradicting the rational lower
bound $\tau>2^{-100}$.

For each $1\le b\le13$, the code finds and checks the least admissible
exponent after removing the explicit pair $(2,1)$. Monotonicity in
$a$ covers every larger admissible exponent. The square-root comparison
for even $b$ is squared only after both sides are known positive.
No negative or unsearched exponent range is omitted.

## 3. The integer slope has been handled separately

When $A=2p$, rational scaling preserves the irreducibility of each
ordinary cyclotomic polynomial. The residual factor is therefore a
product of entire factors
$P_h(X)=4^{\varphi(h)}\Phi_h(X/4)$, and principal survival includes
$P_1=X-4$ exactly once.

For $h>1$, $P_h(3)>0$: nonreal roots pair by conjugation and the only
additional real root is negative. The primitive-root logarithm series
is absolutely convergent at $3/4$. The prime-power Ramanujan formula
and multiplicativity give
$|c_h(k)|\le\gcd(h,k)\le k$, so

\[
\log|\Phi_h(3/4)|\ge-\sum_{k\ge1}(3/4)^k=-3.
\]

This bound retains all conjugates. It implies
$P_h(3)\ge4^{\varphi(h)}e^{-3}>(3/2)^{\varphi(h)}$ for
$\varphi(h)\ge4$, using $(8/3)^4>27>e^3$.
The smaller totients give exactly $h=2,3,4,6$, with the displayed
values $7,37,25,13$. These all satisfy the desired strict inequality.

The principal factor has absolute value one. If it were the only
remaining factor, the already reviewed exact repetition theorem would
force an alternating parity word. Primitivity reduces that possibility
to the two explicitly excluded length-two words. Every permitted word
in the integer-slope case therefore has a further factor and the
strict product bound $D_{\rm pol}>(3/2)^{n-1}$ follows.

## 4. Combination, execution, and limits

Away from the integer slope, the deflated root-gap estimate gives the
stronger $D_{\rm pol}>(3/2)^n$. In either case, combining with
$p\le3^{n-1}$ gives

\[
D_{\rm pol}>p^{\log_3(3/2)}.
\]

I independently ran the exact checker normally and under `python -O`.
Both returned **PASS** and byte-identical JSON. The run reproduced the
cutoff denominator, all nine large candidates, seven malformed-input
rejections, and log-interval hash
`11fb143a539564862da316b1d331374b0c438cb9733ac013be8f444ff63b6ce3`.

No mathematical issue was found in the reviewed proof or certificate.
The proven lower bound concerns the residual **polynomial** denominator.
It gives no lower bound for
$D_{\rm pol}/\gcd(D_{\rm pol},Q_0(3))$. Its final integer evaluation
gcd remains the actual unrestricted cycle problem in this route.
