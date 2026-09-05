# Third pass: unbounded-run renewal, ordinary averaged drift, and the transported discrepancy

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05, Asia/Jerusalem.
Frozen parent: PR #90 at `8bad9ba6a0d24ea1bb64f1f1f6048230483f9d3c`.

**All new theorem-level claims are PROPOSED pending independent review.**
This is a further attempted full closure, not a complete Collatz proof. The
original uniform Green bound remains open. No earlier claim or artifact is
changed. The new positive result is an ordinary-integer averaged contraction
for complete, arbitrarily long odd/even runs, with a cofinal rational
certificate. The contraction is not silently applied to the distributions
produced by the dynamics: an exact all-source example shows that application
would be false. An explicit rate-free discrepancy target remains unproved.

## 0. The change in the attempted proof

The previous finite-dictionary obstruction allows each block only a bounded
number of shortcut steps. Here one packet contains a **whole odd run followed
by a whole even run**. Its length is unbounded over ordinary sources. The
inverse kernel sums both run lengths, with exact arithmetic guards.

The work establishes:

| Claim | Result | Not established |
|---|---|---|
| T-ASTRA-014 | Exact unbounded-run map, inverse kernel, killing interface, and clock bound | No all-source termination claim |
| L-ASTRA-015 | An integrated, analytically bounded infinite inverse-run tail for a positive seed | No uniform bound after arbitrarily many packets |
| T-ASTRA-016 | Ordinary finite-packet height-moment asymptotic, with explicit error bound | No independence assumption after transport |
| C-ASTRA-017 | Cofinal one-packet factor 22/25 and two-packet certificate | Not a pointwise drift inequality |
| T-ASTRA-018 | Rate-free transported-discrepancy sufficient criterion for full Collatz | The discrepancy limit is OPEN |
| R-ASTRA-019 | Exact failure of iterating the fresh-shell contraction on an actual full-support ensemble | Does not refute eventual decay or a cumulative estimate |
| X-ASTRA-003 | Exact arithmetic, core, kernel, and all-source finite-packet certificates | Same-author implementations, not independent mathematical review |

The essential gain over the earlier reduction is a **proved ordinary averaged
inequality** for an unbounded-step map. The essential remaining difficulty is
the precise distribution actually transported by that map.

## 1. T-ASTRA-014 — exact unbounded-run induction

Use the shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n.
For a positive odd n write

\[
a=\nu_2(n+1),\qquad n+1=2^a m\quad(m\text{ odd}),
\qquad b=\nu_2(3^a m-1).
\]

Both a and b are finite positive integers. Define

\[
\boxed{F(n)=\frac{3^a m-1}{2^b}.}                         \tag{1.1}
\]

The first a shortcut steps are odd, their endpoint is the even integer
3^a m-1, and the next b steps are even. The resulting F(n) is odd. Thus this
is exactly one maximal odd run and one maximal even run, not a model of them.
The formula also gives F(1)=1, representing the shortcut cycle 1,2,1.

Every positive ordinary source has a finite first packet. If a positive
shortcut orbit never reaches 1, its odd tail undergoes infinitely many packets:
it cannot remain even forever, and infinitely many consecutive odd steps would
require n+1 divisible by every power of two. Consequently convergence of all
F-orbits to 1 is equivalent to Collatz.

### Killing a finite core

Fix an integer H>=1. For n>H odd, a packet starts with an increasing odd run,
then a decreasing even run ending at F(n). Thus the packet enters [1,H] if
and only if F(n)<=H. No intermediate crossing is omitted by endpoint killing.
On odd integers greater than H, let K_H be the forward mass pushforward under
F, killed at this first entry. Equivalently, its inverse formula is

\[
(K_H f)(y)=\sum_{b\ge1}\sum_{a=1}^{\nu_3(2^b y+1)}
 \mathbf1_{\{n_{a,b}(y)>H\}}f(n_{a,b}(y)),\quad y>H\text{ odd},
\]
\[
n_{a,b}(y)=2^a\frac{2^b y+1}{3^a}-1.                       \tag{1.2}
\]

For every retained pair the quotient is a positive odd integer, so the actual
source has exactly a initial odd steps and b subsequent even steps. For a
fixed source these lengths are unique. Conversely every physical predecessor
packet occurs in (1.2). In particular no source is counted twice.
For nonnegative f, Tonelli therefore gives the exact identity

\[
\|K_H f\|_1=\sum_{\substack{n>H\text{ odd}\\F(n)>H}}f(n)
\le\|f\|_1.                                               \tag{1.3}
\]

The word "inverse" describes evaluation at the endpoint; as a mass operator
this is the deterministic forward pushforward. This convention agrees with
the original packet's L and is not a stochastic surrogate.

### How the packet clock differs from the shortcut clock

Put c=log_2(3), L_i=log_2(F^i(n)+1). Equation (1.1) gives

\[
a_i\le L_{i-1},\quad b_i\le cL_{i-1},\quad L_i\le cL_{i-1}.
\]

If R packets suffice to reach 1, then

\[
\tau(n)\le(1+c)\log_2(n+1)\frac{c^R-1}{c-1}.               \tag{1.4}
\]

In particular a logarithmic packet bound would imply a polynomial, not
necessarily logarithmic, shortcut-time bound. The rate-free criterion in
Section 5 prescribes neither of these bounds. All inequalities here follow
from actual finite packets; no orbit is assumed convergent in deriving them.

## 2. L-ASTRA-015 — a summable infinite inverse-run tail

For this section take H=1 and the positive odd-source seed f(n)=(n+1)^(-2),
n>=3. For y>=3 odd put v_b=nu_3(2^b y+1). Exact summation of the a index in
(1.2) yields

\[
(K_1 f)(y)=\sum_{b\ge1}\frac{9}{5}
 \frac{(9/4)^{v_b}-1}{(2^b y+1)^2}.                        \tag{2.1}
\]

No inverse source 1 occurs for y>=3. Let p=log_3(4)>5/4, the latter inequality
following from 3^5<4^4. Since 3^{v_b}<=2^b y+1, the b summand is at most
(9/5)(2^b y+1)^(-p). Hence for any B>=1,

\[
\sum_{b\ge B}\frac{9}{5}
 \frac{(9/4)^{v_b}-1}{(2^b y+1)^2}
\le\frac{18}{5}\,2^{-5B/4}y^{-5/4}.                       \tag{2.2}
\]

Here 1/(1-2^{-5/4})<2 was used. This is a deterministic bound on the whole
omitted infinite ray, not a truncation convention. Its total over all odd
y>=3 is at most

\[
\frac{72}{5}\,2^{-5B/4},                                  \tag{2.3}
\]

because sum_{y>=3} y^{-5/4} <= integral_2^infinity t^{-5/4}dt <4.
Thus the complete first-packet inverse tail has an explicit **integrated**
bound, despite arbitrary local valuation spikes.

For B divisible by four, (2.2) has the fully rational upper bound

\[
\frac{18}{5\,2^{5B/4}\,y\lfloor y^{1/4}\rfloor}.          \tag{2.4}
\]

The new checker encloses (2.1) at 40 endpoint/truncation pairs using (2.4).
This seed and bound are not asserted invariant under K_H. Iterating the same
seed bound without proving an invariant estimate would be invalid.

## 3. T-ASTRA-016 — ordinary averaged height drift for complete packets

Let I_X be the odd integers in (X,2X], X a positive integer. Fix a positive
integer r and 0<theta<1. Define

\[
P_\theta=
 \frac{3^\theta}{2^{1+\theta}-3^\theta}
 \frac{1}{2^{1+\theta}-1}.                                \tag{3.1}
\]

If theta(c^r-1)<1, then

\[
\boxed{
\frac1{\#I_X}\sum_{n\in I_X}
 \left(\frac{F^r(n)+1}{n+1}\right)^\theta
\longrightarrow P_\theta^r\quad(X\longrightarrow\infty).
}                                                        \tag{3.2}
\]

The same limit holds when a fixed floor H kills a term on first entry,
because each fixed finite packet word eventually avoids that floor as its
ordinary source increases. This theorem is about **ordinary integer counts**,
not a Haar-measure conclusion substituted for an ordinary one.
Moreover 0<P_theta<1. To see this, use the probability weights 2^{-a-b} on
positive pairs (a,b). Their sum is one and the mean of C=3^a/2^{a+b} is one.
Strict concavity gives E(C^theta)<1, since C is not constant. Summing the two
geometric series gives (3.1).

### Exact packet cylinders

For fixed pairs (a_1,b_1),...,(a_r,b_r), let L=sum(a_i+b_i), q=sum a_i. The
parity word consists of these runs and a final odd bit at the endpoint.
It selects one residue class modulo 2^{L+1}. Its count in I_X is therefore

\[
X/2^{L+1}+\epsilon,\qquad |\epsilon|\le1.                 \tag{3.3}
\]

For completeness, the usual finite affine formula is 2^L T^L(n)=3^q n+A_w.
The class with the prescribed word and odd endpoint is

\[
n\equiv(2^L-A_w)(3^q)^{-1}\pmod{2^{L+1}}.
\]

Finite parity-cylinder bijectivity follows inductively: the two lifts of a
length-L class have opposite next parity, because their L-step difference is
odd. The final odd bit enforces maximality of the last even run. No independence
beyond this exact finite congruence is assumed.

### Explicit finite-X upper bound, including every affine correction

Set L_0=log_2(2X+1), A_i=ceil(c^{i-1}L_0), B_i=ceil(c^i L_0). These bound the
actual a_i and b_i by Section 1. Let

\[
J_\theta=\sum_{b\ge1}2^{-\theta b}=\frac1{2^\theta-1},
\quad H_\theta(A)=\sum_{a=1}^A(3/2)^{\theta a},
\]
\[
D_{i,r}=\left(\prod_{j=1}^i A_jB_j\right)
 J_\theta^{r-i}\prod_{j=i+1}^r H_\theta(A_j),\qquad0\le i\le r. \tag{3.4}
\]

Empty products equal one. Then

\[
\begin{split}
\sum_{n\in I_X}\left(\frac{F^r(n)+1}{n+1}\right)^\theta
\le&\ \frac X2\left(P_\theta^r+X^{-\theta}
                   \sum_{i=1}^rP_\theta^{r-i}\right)\\
   &+D_{0,r}+X^{-\theta}\sum_{i=1}^rD_{i,r}.                \tag{3.5}
\end{split}
\]

**Proof.** In shifted coordinates x=n+1 a packet is
x' = C_i x+d_i, C_i=3^{a_i}/2^{a_i+b_i}, d_i=1-2^{-b_i} in (0,1).
Consequently, using subadditivity of t^theta,

\[
\left(\frac{F^r(n)+1}{n+1}\right)^\theta
\le\prod_{j=1}^rC_j^\theta+
 X^{-\theta}\sum_{i=1}^r\prod_{j=i+1}^rC_j^\theta.          \tag{3.6}
\]

For the first product, the main term of (3.3), summed over all positive run
lengths, is XP_theta^r/2. The sum of absolute counting errors is at most D_0,r:
retain the actual a bounds and extend the positively weighted b sums to infinity.
For the i-th correction, the first i packets carry no multiplier. Bound their
numbers of parameter choices by product_{j<=i} A_jB_j. The suffix errors are
therefore D_i,r. Its main term is XP_theta^{r-i}/2, since the unweighted prefix
probabilities sum to one. This proves (3.5).

Now D_0,r=O(X^{theta(c^r-1)}), and
D_i,r=O((log X)^{2i} X^{theta(c^r-c^i)}). Divide (3.5) by #I_X=X/2+O(1).
All errors vanish under the stated condition. Conversely, restrict to any
finite collection of words. The true ratio is at least their coefficient
product, and (3.3) gives the corresponding limiting lower bound. Increasing
the finite collection exhausts P_theta^r. This proves (3.2). QED.

This is an arbitrary-fixed-r theorem with the stated theta restriction, not a
uniform-in-r theorem. At theta=1/2 the proved error range includes r=1 and 2;
the displayed estimate alone does not give the same assertion at r=3.

## 4. C-ASTRA-017 — an exact cofinal drift certificate

Take lambda=9/8 and theta=1/2. Then

\[
P_{1/2}=\frac{\sqrt3}{(2\sqrt2-\sqrt3)(2\sqrt2-1)}
       <\frac{173}{200}.                                 \tag{4.1}
\]

The rational square-root enclosures in X-ASTRA-003 certify this strict bound
by integer squaring. No floating-point estimate is load-bearing.
For X=2^m use the following larger, entirely rational/integer quantities in
(3.5):

\[
A_i=\lceil(8/5)^{i-1}(m+2)\rceil,\quad
B_i=\lceil(8/5)^i(m+2)\rceil,
\]
\[
D_{i,r}\le\left(\prod_{j<=i} A_jB_j\right)
 (25/2)^{r-i}(5/4)^{\sum_{j>i}A_j},\quad
X^{-1/2}\le2^{-\lfloor m/2\rfloor}.                       \tag{4.2}
\]

Indeed c<8/5 follows from 3^5<2^8, sqrt(3/2)<5/4, and
J_{1/2}=1+sqrt2<5/2. Thus H_{1/2}(A)<5(5/4)^A.
The exact rational substitution proves

\[
\boxed{
\lambda\frac1{\#I_{2^m}}\sum_{n\in I_{2^m}}
 \sqrt{\frac{F(n)+1}{n+1}}<\frac{99}{100}\quad(m\ge18),
}                                                        \tag{4.3}
\]

and

\[
\boxed{
\lambda^2\frac1{\#I_{2^m}}\sum_{n\in I_{2^m}}
 \sqrt{\frac{F^2(n)+1}{n+1}}<\frac{19}{20}\quad(m\ge128).
}                                                        \tag{4.4}
\]

Since #I_{2^m}=2^{m-1}, there is no count-normalization error here.
Equation (4.3) gives the undiscounted one-packet factor
(99/100)/(9/8)=22/25. Both bounds remain valid after killing at any floor.

### Why a finite certificate proves every subsequent dyadic scale

The certificate checks (4.3) at m=18,...,42 and (4.4) at m=128,...,152.
The extension is a written induction, not an extrapolation.
When m increases by 25, the A_1,A_2,B_1,B_2 increments are respectively
25,40,40,64. In the one-packet range both A_1 and B_1 grow by a factor at most
9/4. In the two-packet range all four factors grow by at most 6/5.
The nonnegative normalized error terms in (4.2) are consequently multiplied
by at most

\[
(5/4)^{25}/2^{25},\quad(9/4)^2/2^{37}
\]

for r=1, and by at most

\[
(5/4)^{65}/2^{25},\quad
(6/5)^2(5/4)^{40}/2^{37},\quad(6/5)^4/2^{37}
\]

for r=2. Each is less than one, certified by exact rational arithmetic.
The remaining X^{-1/2} main corrections decrease too. This proves both
cofinal statements in every residue class modulo 25.

This certificate controls an average of actual ordinary orbits over complete
source intervals. It does not assert contraction separately for each source,
each survivor subset, or each transported probability distribution.

## 5. T-ASTRA-018 — a rate-free remaining closure target

Set H=2^18. X-ASTRA-003 checks directly that every positive n<=H reaches 1,
with maximum shortcut time 278 at n=230631. This is a local exact finite-core
certificate, not an imported large verification record.
On odd n>H put v(n)=sqrt(n+1) and define the height-weighted pushforward

\[
(\mathcal A h)(y)=\sum_{\substack{F(n)=y\\n>H}}
 h(n)\frac{v(y)}{v(n)},\qquad y>H\text{ odd}.              \tag{5.1}
\]

Let Pi replace h on each dyadic I_{2^m}, m>=18, by its average there. It is a
positive mass-preserving projection. By (4.3), for every nonnegative summable h,

\[
\boxed{\|\mathcal A\Pi h\|_1\le\frac{22}{25}\|h\|_1.}    \tag{5.2}
\]

Unlike a residue-only model, this retains ordinary height. It is a theorem
for the projected measure, not a license to insert Pi between physical steps.

### A fixed, positive, full-support seed without a polynomial lower profile

For n in I_{2^m}, m>=18, define

\[
h_0(n)=2^{\,1-m-4(2^m-H)},\qquad h_j=\mathcal A^j h_0.
                                                               \tag{5.3}
\]

Every odd n>H receives positive weight. The total initial mass on shell m is
2^{-4(2^m-H)}; the first shell has mass exactly one. The seed's rapid decay
avoids prescribing the earlier polynomial source profile.
All h_j have finite mass for each fixed j, unconditionally: (1.4)'s height
bound gives

\[
\|h_j\|_1\le\sum_{m\ge18}
 2^{-4(2^m-H)+(m+2)(c^j-1)/2}<\infty.                      \tag{5.4}
\]

Define the signed ordinary discrepancy

\[
\Delta_j=\|\mathcal A h_j\|_1-\|\mathcal A\Pi h_j\|_1.
                                                               \tag{5.5}
\]

Equivalently, if d(n)=v(F(n))/v(n) when F(n)>H and d(n)=0 otherwise, and
bar d_m is its average on shell m, then

\[
\Delta_j=\sum_{m\ge18}\sum_{n\in I_{2^m}}
 h_j(n)(d(n)-\bar d_m).                                  \tag{5.6}
\]

The sums are absolutely defined, since both positive masses in (5.5) are
finite. This is a precise correlation with a known physical multiplier,
not an unspecified "mixing" assumption.

### Sufficient completion theorem: a signed sublinear budget

For the exact seed (5.3), put S_J=sum_{j=0}^{J-1} Delta_j. It suffices to prove

\[
\boxed{\liminf_{J\to\infty}\frac{S_J}{J}=0.}                \tag{Q-ASTRA-002}
\]

In particular, either sum_{j<J} Delta_j^+=o(J) or Delta_j^+->0 is sufficient.
The signed budget permits cancellations and sparse large spikes. Neither
pointwise nonpositive discrepancy nor absolute summability is required.

**Proof.** Write m_j=||h_j||_1, p_j=||A Pi h_j||_1, and q=22/25. Then
Delta_j=m_{j+1}-p_j and p_j<=q m_j. Summing exactly gives

\[
\begin{split}
S_J&=m_J-m_0+\sum_{j<J}(m_j-p_j)\\
   &\ge m_J-m_0+(1-q)\sum_{j<J}m_j.                       \tag{5.7}
\end{split}
\]

In particular S_J>=-m_0, so its normalized liminf is always nonnegative.
If any positive source were exceptional, its odd core would be exceptional
and greater than H by the finite-core certificate. For that fixed odd source n,
height factors telescope along the physical orbit and yield

\[
m_j\ge h_0(n)\frac{v(F^j(n))}{v(n)}
\ge h_0(n)\frac{\sqrt{H+1}}{v(n)}=:c_n>0
\]

for every j. Equation (5.7) then forces
liminf S_J/J >= (1-q)c_n>0, contradicting Q-ASTRA-002. Cycles and nonperiodic
failures are both covered. Thus the signed sublinear budget implies Collatz.

The first stronger sufficient condition follows from S_J<=sum Delta_j^+ and
S_J>=-m_0. The second implies the first by Cesaro averaging. QED.

There is also a useful stronger recurrence: m_{j+1}<=q m_j+Delta_j^+.
If Delta_j^+->0, geometric convolution gives m_j->0. Conversely m_j->0 implies
Delta_j^+->0 because Delta_j^+<=m_{j+1}. This equivalence is not used to claim
that either limit is proved. Summability of Delta_j^+ would give finite total
occupation mass, a still stronger target.

Q-ASTRA-002 requires no prescribed decay rate, exponential occupation moment,
or universal logarithmic stopping estimate. It is still **OPEN**. A converse
from Collatz alone is not claimed: very rare large finite excursions could
obstruct uniform integrability of this fixed height-weighted seed.
A possible route is a rigorously bounded telescoping correction for (5.6),
controlling its accumulated signed charge rather than each spike. No such
all-depth correction or sublinear upper bound for S_J was proved.

## 6. R-ASTRA-019 — the fresh-shell contraction actually fails after transport

The seed (5.3) is exactly shell-flat: Pi h_0=h_0. It is tempting to apply (5.2)
at every subsequent time. The following **all-source** certificate refutes that
step for this very seed; it is not an artificial point-mass counterexample.
Let M_j=lambda^j||h_j||_1. Exact intervals give

| j | Outward-rounded enclosure for M_j |
|---|---|
| 0 | [1, 1+2^(-120)] |
| 1 | (0.6524105278, 0.6524105280) |
| 2 | (0.4788461746, 0.4788461748) |
| 21 | (0.0777727966, 0.0777727968) |
| 22 | (0.0843425957, 0.0843425959) |
| 23 | (0.0870687878, 0.0870687881) |
| 24 | (0.0873500360, 0.0873500363) |

Thus M_22>M_21, M_23>M_22, and M_24>M_23. These are stronger failures than
M_{j+1}>(99/100)M_j, so ||h_{j+1}||_1>(22/25)||h_j||_1 at these transitions.
The undiscounted masses need not increase; the table concerns M_j as defined.
In particular Delta_j>0 at j=21,22,23. This does **not** disprove a sublinear signed discrepancy budget,
Delta_j^+->0, or any of the full-closure targets.

### Coverage of all omitted source shells

Only the first shell H<n<=2H is enumerated. No initial source outside that
shell is assumed convergent. For j<=24 set

\[
p=\left\lceil\frac{(8/5)^{24}-1}{2}\right\rceil=39614.
\]

Using (5.4) and lambda^j<=2^24, the entire omitted contribution to M_j is at
most

\[
\sum_{m\ge19}2^{-4(2^m-H)+(m+2)p+24}
\le 2^{-216657}<2^{-120}.                                \tag{6.1}
\]

The first exponent is -216658, and consecutive terms decrease by a ratio at
most one half because -4*2^m+p<=-1. This proves (6.1) for every time in the
certificate, irrespective of the fate of any omitted orbit.

For the enumerated part, each sqrt((F^j(n)+1)/(n+1)) is rounded down to a
multiple of 2^(-96), using integer square roots. If A_j is the sum of these
floors and N_j is the surviving count, the exact entire-source interval is

\[
\lambda^j\frac2H\frac{A_j}{2^{96}}
\ \le M_j\le\
\lambda^j\frac2H\frac{A_j+N_j}{2^{96}}+2^{-120}.            \tag{6.2}
\]

The compact artifact rounds these rational endpoints outward once more to
a 2^(-64) grid; the full 96-bit replay is reproducible with --full-output.
Both sets of rational endpoints, not the displayed decimals, are authoritative. This is **all sources but only finitely many packets**. There is
no extrapolation of either the downward trend or the later increases.

## 7. What was tried toward closure, and the first unproved inference

I replaced the bounded-step dictionaries by complete odd/even runs, summed
the inverse odd-run index exactly, and obtained an integrated bound on the
remaining infinite ray. I then proved actual ordinary shell drift rather
than substituting a random parity model. The positive cofinal margin is large
enough to absorb a finite core certified in this session.

The direct closure attempt would now assert that this drift persists under
iteration. R-ASTRA-019 proves that assertion false for the actual selected
full-support seed. The valid replacement is the exact discrepancy equation
(5.5), with the finishing target liminf S_J/J=0. This is the first currently
unsupported step. The finite evidence neither establishes nor refutes it.

The new avenue is not covered by the earlier bounded-block obstruction: a
packet has no uniform shortcut-length cap, and (5.2) is an integrated theorem.
It also does not make the earlier obstruction disappear. A proof that replaces
the transported distribution by its shell average would lose precisely the
arithmetic information those obstructions exposed.

For the next mathematical pass, the object to estimate is (5.6) for the exact
h_j, using a sublinear cumulative signed charge for the transported affine
spikes. More finite packet simulations alone do not prove that budget. A signed telescoping correction or a justified coarse-graining
with a remainder tending to zero would be a substantive advance.

## 8. Validation, sources, and review boundary

The [experiment](../../experiments/X-ASTRA-003-run-renewal/README.md) checks
237 packet cylinders; 63 complete bounded-even-run inverse lists; 40 infinite
kernel tail enclosures; 50 initial cofinal drift inequalities and their exact
25-scale contraction factors; every source <=2^18 for the finite core; and 25
all-source finite-packet mass intervals. A separate generalized 5x+1 cycle
control is retained as nonterminating, not silently absorbed by the stopping
logic. No assertion about standard Collatz is inferred from that control.

Both checkers use only the standard library and were authored in this pass.
The verifier uses step-by-step shortcut iteration rather than the generator's
power/valuation packet formula, physical source enumeration for inverse lists,
bit-by-bit parity lifting for cylinders, and a different exact square-root
rounding identity. This is implementation independence, **not independent
mathematical review**. Scope and numerical data remain PROPOSED until reviewed.

The preceding [CONTINUATION.md](CONTINUATION.md) and [PROOF.md](PROOF.md) remain
unchanged and retain their own claim boundaries. No existing canonical status,
other contributor's branch, repository setting, or workflow is changed.

Sources and positioning:

- Finite parity-cylinder interface: the resident completion-ghost packet at
  main `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`, and the original PR #90
  FIRST_PASSAGE.md. The elementary interface is reproved here.
- M. Neklyudov, *Functional analysis approach to the Collatz conjecture*,
  arXiv:2106.11859v9, HTML read during this pass:
  https://arxiv.org/html/2106.11859v9 . Operator and resolvent approaches are
  established prior literature; no general priority claim is made.
- No outside predecessor theorem, density theorem, Diophantine estimate, or
  large verification record is a dependency of this third-pass proof packet.
  A comprehensive external novelty audit was not completed.
