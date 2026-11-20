# Exact positive circulation and one-sided Dirichlet coercivity

**Status: PROPOSED.** These are ordinary positive-integer statements with written
proofs and bounded independent arithmetic replays. They do not prove Collatz.

The contribution is an exact positive weighting of tripling edges for which
inward and outward boundary fluxes agree, and its extension to arbitrary real
invariant labels. This is stronger data than a comparison of two counting
functions, but it does not make either boundary vanish.

## 1. Sources, map, and what is added

Use the shortcut map

\[
 T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.
 \end{cases}
\]

The first input is PR146 at
`6863d298187af8b2619efbf78cc4b0aa8e627393`,
`research/upper-bit-mergers/DIRECTED_TRIPLING.md`, especially its bounded
ordinary return paths and finite affine source list. That source already proves
comparability of inward and outward counting functions and strong connectivity
of the augmented directed graph. Neither is claimed new here.

The analytic input is PR155 at
`92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
`research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`,
claims OD1--OD4, and its `ENDPOINT_BOUNDARY.md`. Those supply the dyadic
variation estimate, weighted coercivity modulo constants, and endpoint limit.

The addition is the common positive weight, its exact signed flux identity,
its extension to general moderate weights and real invariant labels, and the
resulting one-sided functional estimates. Equality of the directed abscissae
is also an immediate consequence of the source's counting comparisons; it is
recorded as a consequence, not a priority claim.

## 2. A canonical cycle at every odd source

An ordinary edge may be traversed in either direction; an added tripling edge
is traversed only as `x -> 3x`, with `x` positive and odd. Fix once and for all
the following deterministic choices in the source's return construction:
choose the smallest allowed exponents at each step and use the neighbor
cylinders in the order listed below.

For every odd positive `x`, this specifies a return path `R_x` from `3x` to
`x`. Adding `x -> 3x` gives a finite directed cycle. Write `S_x` for the
**multiset** of odd sources of the tripling edges in `R_x`.

Here are explicit, deliberately crude uniform bounds. Set

\[
 A=31110,\quad L=3A+120=93450,\quad H=3^{L+1},
 \quad M=90A+22=2799922.                                    \tag{1}
\]

The return has at most `L` edges, every `y in S_x` satisfies

\[
 x/H\le y\le Hx,                                           \tag{2}
\]

and every occurrence of a source is represented by one of at most `M`
fixed positive-slope rational affine functions of `x`, each occurring at most
once in the chosen source list for one return. A fixed affine function is
injective on its applicable ordinary inputs.

### Reconstruction of these bounds

If `x=3^5 v`, with `v` any positive odd integer, choose
`b in {2,3,4,5}` and `a in {6,7,8,9}` such that `3^b v` and `3^a v` are
`3` or `5` modulo `16`. Tripling to the upper exponent, crossing the ordinary
neighbor merger, descending between exponents, crossing back, and tripling to
`x` gives the return. A single exponent descent uses at most eleven edges;
there are at most seven such descents. The total is at most `99`.
Its tripling sources belong to

\[
 3^i v\quad(0\le i\le9),\qquad
 8\,3^i v-1\quad(0\le i\le6).                              \tag{3}
\]

Otherwise write `x=3^j u`, where `0 <= j <= 4` and `u` is positive odd and
prime to three. The smallest `a_0 in [j+1,j+486]` satisfying
`2^{a_0}u = 1 (mod 729)` exists because `2` generates the units modulo `729`.
Among `a=a_0+486r`, `0 <= r < 64`, choose the first giving one of

\[
 3^a u\equiv369\pmod{512},\quad3\pmod{16},\quad
 5\pmod8,\quad23\pmod{32}.                                \tag{4}
\]

The multiplier `3^486` generates each fixed odd residue class modulo `8`
inside the units modulo `512`, so one exists, and `j<a<=A`.
The four neighbor meetings take at most nine steps on each arm.
Set `z=(2^a u-1)/3`; it is positive odd and divisible by `3^5`.

The return consists of: triplings from `3x` to `3^a u`; an ordinary connection
to `3^a u-1`; `a` ordinary exchanges to `2^a u-1=3z`; the high-case return
from `3z` to `z`; `a` ordinary steps from `z` to `u`; and `j` final triplings.
Its length is at most `3a+116`, hence below `L`.

The low-case source list consists of `3^i u`, `0<=i<=A`, and the seventeen
forms (3) with

\[
 v=\frac{2^a u-1}{729},\qquad1\le a\le A.
\]

Substitute `u=x/3^j` for each of five possible `j`. Together with the
seventeen high-case forms this gives
`17+5(A+1)+5A*17=M` listed forms. Each has positive slope. A form may have a
negative intercept; only its legal positive domain is used. The displayed
lists retain multiplicity between different forms.

Every elementary edge changes the positive vertex by a factor between `1/3`
and `3`. Starting at `3x`, the length bound implies (2). These estimates are
not intended as practical routing bounds.

## 3. The exact circulation theorem

Let `omega` be a strictly positive weight on odd positive integers. Suppose
that for some finite `K_omega`,

\[
 H^{-1}x\le y\le Hx\quad\Longrightarrow\quad
 \omega(x)\le K_\omega\omega(y).                           \tag{5}
\]

Examples are

\[
 \omega(n)=n^{-s}(\log(en))^\alpha,
 \qquad s,\alpha\in\mathbb R,
\]

with `K_omega=H^{|s|}(1+log H)^{|alpha|}` sufficient.
Define, for positive odd `y`,

\[
 \pi_\omega(y)=\omega(y)+
       \sum_{x\text{ odd}>0}\omega(x)\,\#\{y\text{ in }S_x\}.\tag{6}
\]

**Theorem DC1.** The sum in (6) has at most `M` terms when source occurrences
are counted by their affine labels. In particular it is a finite, exactly
defined ordinary quantity and

\[
 \omega(y)\le\pi_\omega(y)
       \le(1+M K_\omega)\omega(y).                         \tag{7}
\]

For every real ordinary invariant labeling `f`, put

\[
 g(x)=f(3x)-f(x),\quad g_+(x)=\max(g(x),0),\quad
 g_-(x)=\max(-g(x),0).
\]

If either `sum omega(x) g_+(x)` or `sum omega(x) g_-(x)` is finite, then both
are finite and

\[
 \boxed{\sum_{x\text{ odd}>0}\pi_\omega(x)g_+(x)
      =\sum_{x\text{ odd}>0}\pi_\omega(x)g_-(x).}            \tag{8}
\]

The unweighted-by-`pi` one-sided moments satisfy

\[
 \sum\omega(x)g_-(x)\le M K_\omega\sum\omega(x)g_+(x),
 \qquad
 \sum\omega(x)g_+(x)\le M K_\omega\sum\omega(x)g_-(x),       \tag{9}
\]

as extended nonnegative inequalities without any summability assumption.

**Proof.** For a fixed `y`, each of the at most `M` affine source labels has at
most one preimage `x`. Equations (2) and (5) prove (7).

Ordinary edges have no label change. Telescoping the finite directed cycle
at `x` gives the exact identity

\[
 g(x)+\sum_{y\in S_x}g(y)=0.                                \tag{10}
\]

In particular `g_-(x) <= sum_{y in S_x} g_+(y)` and conversely with signs
reversed. Multiply by `omega(x)` and apply Tonelli. The finite source
multiplicity and (5) give (9). Thus finiteness of either side implies
absolute summability of the full defect. Moreover

\[
 \sum_x\omega(x)\sum_{y\in S_x}|g(y)|
 \le M K_\omega\sum_y\omega(y)|g(y)|<\infty.
\]

It is now legitimate to sum and reorder (10), giving
`sum pi_omega(y) g(y)=0`. Separating positive and negative parts gives (8).
No subtraction of two infinite fluxes is used. QED.

For a complex invariant labeling, the same exact vector identity
`sum pi_omega g=0` holds when `sum omega |g|<infinity`. Apply the real result
to any fixed real projection when an oriented scalar estimate is desired.

For `omega(n)=n^{-s}`, `s>0`, write `pi_s=pi_omega` and `B_s=M H^s`.
The common weight is independent of `f` and of the choice of a component cut.
It is obtained from the fixed routing algorithm, not fitted to a proposed
counterexample.

## 4. Functional and component consequences

Write `N_s(f)=sum_{n>=1}|f(n)|n^{-s}`. For a real invariant label define

\[
 E_s^\pm(f)=\sum_{x\text{ odd}>0}(\pm(f(3x)-f(x)))_+x^{-s}.
\]

The doubling identity gives

\[
 N_s(g)=\frac{E_s^+(f)+E_s^-(f)}{1-2^{-s}}.                 \tag{11}
\]

**Corollary DC2.** For `0<s<1`, the following hold.

1. If `f` is real and `N_s(f)<infinity`, then

   \[
   N_s(f)\le\frac{K_s(1+B_s)}{1-2^{-s}} E_s^+(f),\qquad
   N_s(f)\le\frac{K_s(1+B_s)}{1-2^{-s}} E_s^-(f).           \tag{12}
   \]

2. If `f` is bounded real and either oriented moment is finite, there is a
   unique constant `c` for which both estimates (12) hold with `f-c` on the
   left. When `f` is Boolean, `c` is `0` or `1`.

Here `K_s=C(2C')^s/[2(1-2^{s-1})]` is exactly the constant in PR155 OD2/OD3.
The proof is (9), (11), followed by the corresponding source theorem. No
smallness or divergence of the oriented critical moment is assumed.

For any ordinary invariant set `K`, let

\[
 E_{\rm out}=\{x\text{ odd}:x\in K, 3x\notin K\},\quad
 E_{\rm in}=\{x\text{ odd}:x\notin K, 3x\in K\}.
\]

These are `g_-` and `g_+` for `f=1_K`. At every `s>0`, their Dirichlet moments
are comparable by (9). Thus their nonnegative convergence abscissae agree,
and at every prescribed positive exponent their moments are finite together
or infinite together. If `sigma_K<1`, PR155 OD4 further gives

\[
 \sigma_K=\sigma_{E_{\rm in}}=\sigma_{E_{\rm out}}
          =\sigma_{\partial_3K}=\sigma_{\partial_5K}.       \tag{13}
\]

At a positive common abscissa below one, convergence or divergence of all five
critical moments agrees. This includes the case of convergence at the
abscissa. It is not an every-scale counting theorem.

### A one-sided Liouville consequence, including unbounded labels

Suppose an exponent `0<beta<1` has the following predecessor input: every
ordinary component `C` has

\[
 \sum_{n\in C}n^{-\beta}=\infty.                            \tag{14}
\]

**Corollary DC3.** Every real-valued ordinary invariant `f` satisfying either
`E_beta^+(f)<infinity` or `E_beta^-(f)<infinity` is constant. No boundedness
assumption on `f` is needed.

For bounded `f`, DC2 gives `N_beta(f-c)<infinity`. If `f(n)!=c` at any
integer, the whole component of that integer contributes the fixed positive
factor `|f(n)-c|` times the divergent series (14), a contradiction.
For an unbounded `f`, apply this bounded conclusion to each clipped function
`min(b,max(a,f))`. Clipping is monotone and 1-Lipschitz, so it does not
increase either oriented defect. If two values of `f` differed, clipping
between them would preserve that difference and contradict constancy.

The component counting lower bound `#(C intersect [1,X]) >= c_C X^beta`
for every sufficiently large `X` implies (14) by partial summation. PR146's
`THREE_RAY_DENSITY.md` pins the published Krasikov--Lagarias predecessor
input with `beta=0.84`, and also recalls a smaller self-contained elementary
exponent. Thus DC3 at `beta=0.84` is conditional only on that explicitly
imported predecessor theorem, not on convergence of Collatz. The predecessor
theorem is not independently reproved here. The binary critical-moment
obstruction already occurs in PR146; the extension here is the one-sided
functional statement for every real invariant, including unbounded ones.

This is a sufficient arithmetic test for constancy. It does not establish
finite oriented defect moment for the indicator of a hypothetical separating
component; DC3 says such finiteness cannot hold for a nonconstant invariant.

## 5. What actually survives at the endpoint

If a bounded real invariant `f` has `E_1^+(f)<infinity` **or**
`E_1^-(f)<infinity`, (9) makes its full harmonic tripling defect finite.
The endpoint theorem of PR155 then proves convergence of its dyadic
logarithmic profiles in `L^1` to a constant. A Boolean limit is `0` or `1`.
This gives a directed form of that theorem.

If instead the available finite oriented moment is

\[
 \sum_{x\text{ odd}>0}\frac{\log(ex)}x\,g_+(x)
 \quad\text{or}\quad
 \sum_{x\text{ odd}>0}\frac{\log(ex)}x\,g_-(x),             \tag{15}
\]

use the moderate weight `omega(x)=log(ex)/x` in DC1. Both orientations then
have finite logarithmically weighted moments, so PR155's endpoint estimate
also gives `N_1(f-c)<infinity`.

This does **not** remove the logarithmic cost of controlling the centered
harmonic mass. Nor does it prove an exceptional sparse component empty.

The permanent-failure upper estimate in PR146 is
`D(X)=O(X/sqrt(log(2X)))`, uniformly over intervals. At the origin it implies,
for `0<epsilon<=1`, only

\[
 \sum_{x\text{ odd}>0}\frac{|g(x)|}{x^{1+\epsilon}}
       =O_f(\epsilon^{-1/2}),                              \tag{16}
\]

for bounded invariant `f`. To verify the consequence, bound `|g|` by
`2||f||_infinity` on the permanent-failure set and apply partial summation;
the tail is bounded by a constant times
`integral_1^infinity exp(-epsilon u)u^{-1/2} du`.
The estimate diverges as `epsilon` tends to zero. Multiplication by
`epsilon` makes it vanish, but that normalization does not prove the
unweighted harmonic defect finite or the ordinary boundary empty.

A finite two-vertex directed cycle already shows why the balance (8) alone
cannot eliminate a cut: one edge leaves either color and one enters, with
equal positive weight. This is a counterexample to the inference from
positive circulation to a single component, not a Collatz counterexample.

## 6. Verification and remaining proof target

`check_directed_circulation.py` reconstructs actual positive return paths from
scratch, using the elementary map rather than the source checker. It checks
all unit residues modulo `729`, all four binary cosets modulo `512`, the
high-case exponent choices, and a deterministic family of literal paths.
It then collapses only the explicitly traversed ordinary edges and verifies
zero divergence of three exact rational cycle superpositions on that finite
quotient. It does not assume the visited numbers reach 1, or identify an
unvisited ordinary component with any other.

The finite report records 218 distinct sources, 24,039 literal edges, 4,447
return-tripling edges, and three balanced quotient flows (weights `1`, `1/x`,
and `1/x^2`) on 2,196 quotient vertices. The largest tested return has 1,457
edges; the universal bound is the symbolic `L`, not that sample maximum.
Three deliberately damaged paths are rejected. The script uses explicit
exceptions and runs under ordinary and optimized Python.

The exact circulation is a positive global structure on all ordinary sources.
To close Collatz with this route still requires an arithmetic upper bound
that eliminates a separating cut, or a successful ordinary argument making
all its tripling currents zero. The current source upper bounds, coercivity,
and circulation do not provide that inference. **Collatz remains unresolved.**
