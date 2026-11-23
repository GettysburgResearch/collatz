# Two critical pressures and the ordinary atomic measure

Date: 2026-11-23.

**Status: new written finite and infinite deductions; escape exclusion remains
OPEN.** This attempt changes the operator parameter rather than estimating
another cutoff of the old canonical Green potential. It obtains an exact
ordinary-source spectral interface: an escaping component supplies a finite,
purely atomic eigenmeasure of an operator whose Haar mass contracts. The
positive path product needed in the construction is reconstructed below from
an elementary orbit-cylinder count. No canonical-envelope, predecessor-density
or mixing hypothesis is used by the new theorems. No infinite theorem here
is asserted to be Lean checked.

The new parameter does not erase the original orbit. In particular, the
Haar contraction cannot be substituted for contraction of its atomic
measure. A direct interpolation attempt is tested below, including the
sharp obstruction furnished by the negative fixed point -1.

## 1. Domain, maps, and frozen inputs

Write

\[
 U(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1),\qquad
 \lambda(n)=\frac{3n}{3n+1}.
 \tag{HE1}
\]

An ordinary vertex is a positive odd integer not divisible by three.
Every image of such a vertex is again an ordinary vertex. A nonperiodic
vertex may later enter a positive cycle. An escaping component means one
component of the equivalence relation of eventual forward meeting, all of
whose forward orbits are nonperiodic. Its actual forward orbits are
injective and tend to infinity.

The following sources were read at their exact commits.

| Source | Material used and boundary |
|---|---|
| PR177, `0444986571f09f302cb3687b4bba3552600e4119` | `research/lean-exact-witness-global-20261121/LITERATURE_CANONICAL_ENERGY.md`, (3)--(6), and `ENERGY_TRANSPORT_CONTINUATION.md`: canonical domain and the existing qualified path/flow framework. The finite-Green profile is context, not a premise of the new pressure calculations. |
| PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2` | `research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`, (M9)--(M11), and `research/retained-source-attacks-20261122/SIBLING_MASS.md`: positive product bound, least obstacle, and unit-Haar change of variables. Its predecessor-population and envelope qualifications remain attached. |
| PR178, `7e4569476e152f6b8537bdc1711df595ec1ffd89` | `research/whole-repo-synthesis-20261122/entropy/CANONICAL_TIME_ENTROPY_ATTEMPT.md`, (3)--(8): finite total loss of the actual reversed spine and the distinction between exact ordinary kernels and compact limits. |
| PR185, `39ba48e6a8af781193e28c679ea8ab64663c3aa6` | `research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md`, (3)--(12): exact all-depth inverse-window comparison. This does not identify the time law with Haar. |
| PR175, `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73` | `research/lean-global-closure-20261121/CANONICAL_POTENTIAL_SUPERLEVELS.md`, Section 4, and `LITERATURE_TRANSPORT_ATTEMPT.md`, (2)--(3): finite-chain count and reciprocal correction, explicitly independent of the predecessor-population input. Its `closing/UNEQUAL_DEPTH_SIBLING_ATTEMPT.md` supplies context on actual anchored concentration. |
| PR92 source, `2055b8a311ab87d07bffc730154a7f8546fe382c` | `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, Section 1, T-A3-401: the cylinder calculation reconstructed next. |

### The positive path product is elementary here

For completeness, reconstruct the finite-cylinder argument used by the
pinned PR175/185 source. Let \(S\) be the odd states of one escaping
orbit. Every \(U^r\) is injective on \(S\). A length-\(r\) gap word
of total \(A\) selects one odd residue modulo \(2^{A+1}\), and its
actual affine map has the form

\[
 U^r(n)=(3^rn+B)/2^A,\qquad
 0<B/2^A\le(3/2)^r-1.
\]

The endpoint odd bit enforces the exact valuations; the remainder bound
follows by composing the \(r\) affine steps and using each gap at
least one. There are \(\binom{A-1}{r-1}\) words at total \(A\).
Choose \(r=\lfloor(3/5)\log_2X\rfloor\) and
\(m=\lfloor5r/3\rfloor\), so \(2^m\le X\). For \(r\ge1\),
the low-total lane \(A\le m\) contains at most

\[
 \frac32X\sum_{A\le m}\binom{A-1}{r-1}2^{-A}
 \le\frac32X\rho^r,\qquad
 \rho^3=3125/3456<1.
\]

For the last bound insert \(z=4/5\) and use
\(\sum_{A\ge r}\binom{A-1}{r-1}(z/2)^A=(z/(2-z))^r\),
with \(z^{-A}\le z^{-m}\le z^{-5r/3}\).
In the other lane \(A\ge m+1>5r/3\), all endpoints are below
\(\sigma^rX+(3/2)^r-1\), with \(\sigma^3=27/32<\rho^3\).
They are distinct odd integers, so counting them bounds this lane by
\((\sigma^rX+(3/2)^r)/2\). Hence

\[
 N_S(X)\le2X\rho^r+\tfrac12(3/2)^r\le4X^{39/40}.
\]

The last numerical margins follow from
\(8\,3125^{24}<3456^{24}\), which gives
\(\rho<2^{-1/24}\), and \(\rho>2/3\). The case \(r=0\)
is immediate from \(N_S(X)\le X\) and \(X<2^{5/3}\).
All sources, endpoints, and valuations used here are actual ordinary
integers. No averaging over a new source distribution has occurred.
Tonelli now gives

\[
 \sum_{n\in S}\frac1n
 =\int_1^\infty N_S(t)t^{-2}\,dt\le160.
\]

Thus the product required below exists and obeys

\[
 \boxed{\Lambda_\infty(n):=\prod_{j\ge0}\lambda(U^jn)
       \ge\exp(-160/3)>0}
 \quad\text{on every escaping ordinary orbit.}
 \tag{HE2}
\]

This uses \(\log(1+z)\le z\) and monotone limits of the finite
products. It is independent of the stronger predecessor-population and
canonical-envelope constructions cited for context above.

Let \(X=\mathbb Z_3^\times\), with normalized unit-Haar probability \(m\).
For \(e\ge1\), put \(I_e x=(2^e x-1)/3\), using this branch only when
\(I_e x\in X\). Its inverse is
\(\Phi_e y=(3y+1)/2^e\). For \(s>0\), define

\[
 (P_s f)(x)=\sum_{\substack{e\ge1\\I_e x\in X}}
       \left(\frac3{2^e}\right)^s f(I_e x).
 \tag{HE3}
\]

The geometric coefficient sum is finite. Each branch domain is clopen,
and the series converges uniformly for continuous bounded \(f\); thus
\(P_s\) is a bounded positive operator on \(C(X)\). At an ordinary
root, every legal branch is a positive odd integral unit predecessor.
Indeed integrality of \((2^ex-1)/3\), with \(x\) positive odd, gives
an odd positive integer, and the unit guard is precisely the displayed
guard. The exact forward valuation is \(e\).

## 2. A strict Haar contraction between two critical parameters

### HE-P1. Exact Haar pressure

For every nonnegative measurable \(f\),

\[
 \int_X P_s f\,dm=\rho(s)\int_X f\,dm,
 \qquad
 \boxed{\rho(s)=\frac{3^{s-1}}{2^s-1}.}
 \tag{HE4}
\]

To prove it, the map \(\Phi_e:X\to\Phi_e(X)\subset X\) has ternary
Jacobian \(1/3\). Change variables separately in each nonnegative
summand of (HE3), then use Tonelli:

\[
 \int P_s f\,dm
 =\frac13\sum_{e\ge1}\left(\frac3{2^e}\right)^s\int f\,dm.
\]

The geometric sum gives (HE4). In particular,

\[
 \rho(1)=\rho(2)=1,
 \qquad \boxed{\rho(s)<1\quad(1<s<2).}
 \tag{HE5}
\]

Here is a short proof of strictness without numerical approximation.
Let an auxiliary integer \(E\) have probability \(2^{-e}\), and put
\(Y=3/2^E\). Then \(\mathbb EY=1\) and
\(\rho(1+u)=\mathbb EY^u\). Strict concavity of \(y^u\), for
\(0<u<1\), gives \(\mathbb EY^u<1\). This auxiliary random variable
computes the Haar multiplier only; it is not the actual Collatz gap law.

Consequently, for \(1<s<2\), the nonnegative Green function

\[
 Z_s(x)=\sum_{j\ge0}P_s^j1(x)
 \tag{HE6}
\]

satisfies

\[
 \boxed{\int_X Z_s\,dm=\frac1{1-\rho(s)}<\infty.}
 \tag{HE7}
\]

Thus it is finite at Haar-almost every ternary unit. This is an exact
statement about one specified operator, not an assumed stationary law
of the ordinary orbit.

## 3. Actual gaps have a strict pressure surplus

The positive integer constraint gives an opposing estimate on every
single escaping ordinary source. Let
\(q_i=U^i(q_0)\), with \(g_i=a(q_i)\), and set
\(A_N=\sum_{i<N}g_i\), \(\ell=\log_2 3\).
For \(u>0\), write

\[
 b_1=(3/2)^u,\quad b_2=(3/4)^u,\qquad
 c_u=(2-\ell)b_1+(\ell-1)b_2.
 \tag{HE8}
\]

### HE-P2. Finite integer-gap inequality

For every finite list of positive integer gaps,

\[
 \boxed{\sum_{i<N}(3/2^{g_i})^u
 \ge (2N-A_N)b_1+(A_N-N)b_2.}
 \tag{HE9}
\]

Indeed \(t\mapsto(3/2^t)^u\) is strictly convex. At the integer
arguments \(g\ge1\), its graph lies above the line through its
values at 1 and 2. Equality holds for those two arguments; for every
integer \(g\ge3\), the convex graph lies above the extension of that
secant. Sum that inequality. Coefficients on the right may be negative
when \(A_N>2N\); the finite inequality still holds.

For a supplied injective actual segment, the exact physical telescope is

\[
 A_N\log2=N\log3+\log q_0-\log q_N
       +\sum_{i<N}\log\left(1+\frac1{3q_i}\right).
 \tag{HE10}
\]

Distinctness and positivity give \(\sum_{i<N}1/q_i\le H_N\), where
\(H_N=\sum_{j=1}^N1/j\). Since \(q_N\ge1\),

\[
 A_N\le N\ell+\frac{\log q_0+H_N/3}{\log2}.
 \tag{HE11}
\]

Combining the exact finite inequalities gives

\[
 \boxed{\frac1N\sum_{i<N}(3/2^{g_i})^u
 \ge c_u-(b_1-b_2)
       \frac{\log q_0+H_N/3}{N\log2}.}
 \tag{HE12}
\]

The constants in \(c_u\) are positive weights summing to one, and

\[
 (2-\ell)\log(3/2)+(\ell-1)\log(3/4)=0.
\]

Strict convexity of the exponential therefore proves \(c_u>1\).
In particular every fixed escaping source obeys

\[
 \boxed{\liminf_{N\to\infty}\frac1N
       \sum_{i<N}(3/2^{g_i})^u\ge c_u>1.}
 \tag{HE13}
\]

At the second critical parameter, \(u=1\),

\[
 c_1=\frac{9-3\log_2 3}{4}=1.061278124\ldots.
 \tag{HE14}
\]

For \(0<u<1\), the Haar pressure \(\rho(1+u)\) is strictly below
one, while the actual time average in (HE13) stays uniformly above one.
This isolates a fixed separation between the laws. It does not prove
that those laws agree. The finite estimate keeps its original source
height \(q_0\); no uniformity over arbitrary moving starting heights
is asserted.

## 4. The exact ordinary Green kernel is a source sum

### HE-P3. Ordinary-source formula

Fix a nonperiodic ordinary root \(q\). For an actual source \(n\)
with \(U^j n=q\), let \(\Lambda(n,q)\) be the product of
\(\lambda\) over the \(j\) input states on that finite path; the
empty path has product one. The physical edge identity telescopes to

\[
 \frac{3^j}{2^{a(n)+\cdots+a(U^{j-1}n)}}
       =\frac qn\Lambda(n,q).
 \tag{HE15}
\]

Consequently, for every \(s>1\),

\[
 \boxed{Z_s(q)=q^s\sum_{n\in\operatorname{Pred}(q)}
                 \frac{\Lambda(n,q)^s}{n^s}
       \le q^s\sum_{n\ge1}n^{-s}
       \le q^s\left(1+\frac1{s-1}\right).}
 \tag{HE16}
\]

All sources in the middle expression are actual positive odd unit
ancestors, including \(q\). Because \(q\) is nonperiodic, an
ancestor can reach it at only one odd depth. Thus summing over depths
counts each source once. This uniqueness is why the expression cannot
be applied unchanged at a periodic root. The last inequality is the
integral comparison for the positive decreasing function \(x^{-s}\).

The formula proves pointwise finiteness at every nonperiodic ordinary
root, including at \(s=2\). In contrast, (HE7) diverges as
\(s\uparrow2\). The two statements concern different measures and
are compatible.

On one escaping orbit, the proved product bound (HE2) shows that the single unchanged source
\(q_0\) contributes

\[
 \boxed{P_s^N1(q_N)
       \ge\left(\frac{q_N}{q_0}\Lambda(q_0,q_N)\right)^s
       \ge\left(\frac{q_N}{q_0}\Lambda_\infty(q_0)\right)^s.}
 \tag{HE17}
\]

This is the positive source that a moving-root argument must retain.
It is present before any limit or change of measure.

## 5. A finite atomic eigenmeasure at eigenvalue one

### HE-P4. Construction from an escaping component

Fix an escaping ordinary component \(E\). Define

\[
 r_E(n)=\frac{\Lambda_\infty(n)}n\quad(n\in E),\qquad
 \mu_{E,s}=\sum_{n\in E}r_E(n)^s\,\delta_n\quad(s>1).
 \tag{HE18}
\]

The atoms are embedded in \(X\) by their ordinary integer values.
Their total mass is finite and positive, since
\(0<r_E(n)\le1/n\). Exact edges give

\[
 r_E(n)=\frac3{2^{a(n)}}r_E(Un).
 \tag{HE19}
\]

The component is closed under every ordinary legal unit predecessor.
For bounded nonnegative \(f\), Tonelli and (HE19) now give

\[
\begin{aligned}
 \int P_sf\,d\mu_{E,s}
 &=\sum_{q\in E}r_E(q)^s
       \sum_{Un=q}\left(\frac3{2^{a(n)}}\right)^s f(n)\\
 &=\sum_{n\in E}r_E(n)^s f(n).
\end{aligned}
\]

Thus

\[
 \boxed{\mu_{E,s}P_s=\mu_{E,s},\qquad
        0<\mu_{E,s}(X)<\infty.}
 \tag{HE20}
\]

This is a finite positive **conformal eigenmeasure**. The operator is
not a probability kernel, so the phrase does not assert that it is a
stationary probability for an unstated Markov chain. Normalizing its
finite mass is harmless but does not make the rows of \(P_s\) sum to
one.

For \(1<s<2\), this measure and Haar are left eigenmeasures of the
same operator at different eigenvalues:

\[
 \boxed{\mu_{E,s}P_s=\mu_{E,s},\qquad
        mP_s=\rho(s)m,\qquad \rho(s)<1.}
 \tag{HE21}
\]

The first is purely atomic; the second is nonatomic. No absolute
continuity or domination has been proved between them.

The same source sum also identifies the boundary of (HE16). For any
forward ray \(q_k\) in \(E\), every fixed \(n\in E\) eventually
belongs to \(\operatorname{Pred}(q_k)\), and its product to \(q_k\)
converges to \(\Lambda_\infty(n)\). Domination by \(n^{-s}\) gives

\[
 \boxed{\lim_{k\to\infty}\frac{Z_s(q_k)}{q_k^s}
        =\mu_{E,s}(X)>0.}
 \tag{HE22}
\]

In particular the ordinary bound in (HE16) cannot be improved to
\(o(q^s)\) on such a component without excluding that component.

### HE-P5. Converse on ordinary atomic support

Conversely fix any \(s>0\). Suppose a nonzero finite positive measure
\(\mu\), concentrated on the positive odd units, satisfies
\(\mu P_s=\mu\). Here concentration means that the complement of
this countable set has measure zero; it does not restrict the closed
topological support. Testing individual atoms gives

\[
 \mu(\{n\})=
 \left(\frac3{2^{a(n)}}\right)^s\mu(\{Un\}).
 \tag{HE23}
\]

There is exactly one possible ordinary odd target in this calculation:
\((3n+1)/2^e\) is odd precisely when \(e=a(n)\). All other branch
terms lie outside the countable ordinary set carrying \(\mu\).

Around a positive cycle \(n_0,\ldots,n_{r-1}\),

\[
 \prod_{i<r}\frac3{2^{a(n_i)}}
 =\prod_{i<r}\frac{3n_i}{3n_i+1}<1.
 \tag{HE24}
\]

Multiplying (HE23) around the cycle forces all its atom masses to zero.
The same recurrence forces zero at every source that eventually enters
that cycle. Since \(\mu\) is nonzero and supported on a countable
ordinary set, some atom has positive mass. Its orbit is therefore not
eventually periodic. It escapes.

For any fixed \(s>1\), escape existence is consequently
equivalent to existence of such an ordinary atomic conformal
\(P_s\)-eigenmeasure at eigenvalue one. Both directions are written proofs; the forward direction uses the
elementary product estimate reconstructed in Section 1. This equivalence
treats escape only. It does not rule out a nontrivial
positive cycle, whose atoms (HE24) excludes from this particular measure.

### HE-P6. Classification of the ordinary atomic cone

The same argument classifies the entire cone within this support class.
If an eigenmeasure has a positive atom at one ordinary vertex, (HE23)
propagates positivity both forward and to every legal unit predecessor.
Its positive atoms therefore form a union of complete escaping components.
On one such component, division of (HE23) by (HE19) to the power \(s\)
shows that \(\mu(\{n\})/r_E(n)^s\) is constant along every edge.
Two vertices in the component have a common forward endpoint, so that
ratio is one constant \(c_E>0\) on the entire component. Hence, for
\(s>1\),

\[
 \boxed{\mu=\sum_{E\text{ escaping}}c_E\mu_{E,s},\qquad
        c_E\ge0,\quad
        \sum_Ec_E\mu_{E,s}(X)<\infty.}
 \tag{HE24a}
\]

Conversely every such nonnegative finite sum satisfies the eigenmeasure
identity by Tonelli. The sums are countable because the ordinary state
set is countable. The extreme rays of this cone are exactly the single
component measures \(\mu_{E,s}\).

Every nonzero measure in this cone has full topological support on
\(X\). To see this, start at any one positive atom \(q\). Given a
unit residue \(a\pmod{3^k}\), choose \(e\ge1\) solving

\[
 2^eq\equiv3a+1\pmod{3^{k+1}}.
\]

Such an \(e\) exists because 2 generates the units modulo
\(3^{k+1}\). An elementary proof of that fact is
\(4^{3^j}\equiv1+3^{j+1}\pmod{3^{j+2}}\), by induction, together
with \(2\equiv-1\pmod3\). The corresponding positive odd unit
parent \(I_eq\) lies in the prescribed class and has positive mass
by (HE23). Thus every nonempty basic open set has positive mass.
Different component measures can still be mutually singular: they have
disjoint countable atom supports. Full topological support is not the
missing absolute-continuity statement.

There is also a useful exact ordinary-point regularity bound for each
canonical component measure. Put
\(\zeta_s=\sum_{j\ge1}j^{-s}<\infty\). For a fixed positive
integer \(a\), once \(3^k>a\),

\[
 0\le\mu_{E,s}(a+3^k\mathbb Z_3)-\mu_{E,s}(\{a\})
 \le\zeta_s3^{-sk}.
 \tag{HE24b}
\]

Indeed all other positive integers in the cylinder have the form
\(a+j3^k\), \(j\ge1\), and their masses are at most their
negative \(s\)-powers. At a fixed negative integer \(-a\), with
\(a>0\) and \(3^k>2a\), the same argument gives

\[
 \mu_{E,s}(-a+3^k\mathbb Z_3)
 \le2^s\zeta_s3^{-sk}.
 \tag{HE24c}
\]

These estimates distinguish an ordinary atom from the small mass near
a negative integer boundary point. They supply no bound on the atomic
jump at a positive integer, which is exactly the mass needing exclusion.

The apparent potential-theory shortcut also has an exact remaining
integrability term. Although \(Z_s\) is finite at every ordinary atom,
for every nonzero ordinary atomic eigenmeasure,

\[
 \int_X Z_s\,d\mu
 =\sum_{j\ge0}\int_XP_s^j1\,d\mu
 =\sum_{j\ge0}\mu(X)=\infty.
 \tag{HE24d}
\]

Thus finiteness of the measure and pointwise finiteness of the Green
function do not justify integrating \((I-P_s)Z_s=1\) as a finite
identity. On a single component this is already visible from one fixed
ordinary source \(p\): at every \(q_k=U^kp\),

\[
 \mu_{E,s}(\{q_k\})Z_s(q_k)\ge r_E(p)^s>0.
 \tag{HE24e}
\]

Use the term for \(p\) in (HE16) and (HE19). The distinct future
vertices therefore retain the same positive contribution to that
integral. A successful uniform-integrability estimate would have to
eliminate these actual terms, not omit them.

## 6. The exact obstruction to an Lp interpolation shortcut

Let

\[
 \beta=\frac{\log3}{\log(3/2)}=2.70951129\ldots,
 \quad C_k=\{x\in X:x\equiv-1\pmod{3^{k+1}}\}.
 \tag{HE25}
\]

The normalized unit-Haar mass is
\(m(C_k)=1/(2\cdot3^k)\). If \(x\in C_k\), the first \(k\)
inverse gaps can all be one, with unit intermediate states, since

\[
 I_1^j(x)=-1+(2/3)^j(x+1)\equiv-1\pmod3\quad(0\le j\le k).
\]

Their total weight is \((3/2)^{sk}\). For \(1\le p<\infty\),

\[
 \boxed{\|P_s^k1\|_{L^p(m)}
 \ge2^{-1/p}\left((3/2)^s3^{-1/p}\right)^k.}
 \tag{HE26}
\]

Hence no strict operator-norm contraction on this \(L^p\) space is possible when
\(sp\ge\beta\). There is a stronger statement about the Green
function itself. The disjoint annuli \(C_k\setminus C_{k+1}\) have
mass \(3^{-(k+1)}\), and \(Z_s\ge(3/2)^{sk}\) on each. Therefore

\[
 \int_X Z_s^p\,dm
 \ge\frac13\sum_{k\ge0}
        \left((3/2)^{sp}/3\right)^k,
 \qquad
 \boxed{Z_s\notin L^p(m)\quad\text{if }sp\ge\beta.}
 \tag{HE27}
\]

This includes the equality case. It holds for the same Green function
which belongs to \(L^1(m)\) when \(1<s<2\).

These cylinders also have positive ordinary odd representatives:
\(x_k=2\cdot3^{k+1}-1\). Their first \(k\) inverse edges are legal.
Thus positivity at a finite resolution does not remove the norm
obstruction. The obstruction is nevertheless a boundary calculation;
it does not claim that these changing representatives form one escaping
ordinary orbit.

The usual finite-cylinder evaluation also shows exactly what is lost.
The function \(P_s^N1\) is constant modulo \(3^{N+1}\). Consequently
(HE4) gives the crude point bound

\[
 P_s^N1(q)\le2\cdot3^N\rho(s)^N.
 \tag{HE28}
\]

Together with (HE17), this permits only
\(q_N\le C[3\rho(s)]^{N/s}\). But

\[
 [3\rho(s)]^{1/s}=\frac3{(2^s-1)^{1/s}}>\frac32.
 \tag{HE29}
\]

It is weaker, at every finite \(s\), than the elementary actual bound
\(q_N+1\le(3/2)^N(q_0+1)\). Dropping the cylinder cost would be the
unsupported inference. Even a hypothetical high-p estimate would first
improve a growth-rate bound; excluding arbitrarily slow escape would
require an additional argument.

## 7. Leastness and boundary classification were tested directly

The least-envelope atom-removal theorem in the pinned PR180 acts on a
simple **inverse** ray. A tail-supported function \(h\) there obeys
\(Ph\ge h\), so subtracting a small multiple preserves excessivity.
Trying the corresponding subtraction on the future tail of one
escaping forward ray has the opposite sign at its first supported
vertex: its predecessor on that ray was removed. Restoring all its
inverse ancestors runs through the obstacle constraints. The existing
leastness statement does not supply the required positive room there.
No forward-end removal is claimed.

A second attempted import was an affine-group or Diestel--Leader Martin
boundary classification. The primary statements checked were:

- Sara Brofferio, *The Poisson boundary of random rational affinities*,
  Ann. Inst. Fourier 56 (2006), 499--515, main theorem:
  <https://www.numdam.org/item/10.5802/aif.2191.pdf>.
- Sara Brofferio and Wolfgang Woess, *Positive harmonic functions for
  semi-isotropic random walks on trees, lamplighter groups, and
  DL-graphs*, introduction and Theorems 3.4, 4.23, 5.1:
  <https://arxiv.org/pdf/math/0501440>.

Brofferio's group walk has iid affine increments and a finite moment;
its boundary is described by the contracting completions. The second
paper uses irreducible semi-isotropic transition laws on its specified
graphs. Neither hypothesis set has been established for the actual
ordinary legal inverse kernel, or for the atomic measure (HE20).
These inspected classifications do not rule out that measure. No full
proof audit of either literature source is claimed.

The direction of the branches matters as well: the inverse maps in
(HE3) expand ternary distances by three. The contracting forward affine
maps occur in a different adjoint description. A theorem requiring
contracting inverse branches cannot be applied by silently interchanging
those directions. In particular the negative number log(rho(s)) is the
Haar L1 growth rate, not an identified topological pressure of a
countable-state thermodynamic model.

The principal researcher also suggested Klaus Thomsen's *Dissipative
conformal measures on locally compact spaces*, whose primary introduction
and conformal-measure setup were then opened:
<https://arxiv.org/pdf/1312.5969>. For its cofinal noncompact local
homeomorphisms, the construction allows nonzero dual fixed measures at
nonpositive pressure, with dissipative measures at strictly negative
pressure. That is not an instantiated theorem about (HE3), and its
pressure has not been identified with log(rho(s)). It does rule out
using a general slogan that negative pressure forbids all conformal
measures. A classification adequate here must keep the specific
ordinary atomic support and the actual operator.


## 8. The remaining central step

The new pressure family supplies all of the following with the original
ordinary source retained: the strict Haar contraction (HE5), the strict
actual-gap surplus (HE13), the exact source Green formula (HE16), and
an ordinary atomic conformal eigenmeasure (HE20)--(HE23) equivalent to
escape, using the elementary actual-orbit product bound.

The intended closing theorem would exclude that finite positive atomic
eigenmeasure, or prove a quantitative bound on the same original-source
term (HE17) strong enough to contradict it. The elementary Haar norm
and Lp interpolation do not do this; their precise failures are paid in
(HE26)--(HE29). Deleting every high-weight inverse prefix is also not a
solution, since the prefix carrying the fixed source in (HE17) is one
of the terms that such a deletion could discard.

No escape exclusion, vanishing canonical charge, unrestricted cycle
exclusion, or full Collatz proof has been obtained in this lane.
