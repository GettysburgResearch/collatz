# Ordinary Fourier cancellation and Besicovitch rigidity

## Status, theorem, and quantifiers

**Independently reviewed written derivation from the frozen marginal
analytic inputs listed in Section 9.** The new measure-theoretic argument is
not claimed to be a Lean theorem. Its ordinary-source limits are unweighted:
no almost-everywhere ternary density is evaluated on ordinary integers.
The later joint-clock and positive-natural-density claims of PR180 are
not used.

The new independent semantic review covers Sections 3--8. It checks the
new derivation against the stated inputs; those earlier inputs retain
their separate audit and evidence level.

Write

\[
 T(n)=
 \begin{cases}n/2,&n\equiv0\pmod2,\\(3n+1)/2,&n\equiv1\pmod2,\end{cases}
 \quad e(t)=\exp(2\pi i t),\quad
 H_X=\sum_{1\le n\le X}\frac1n,\quad
 \mathcal L_X a=\frac1{H_X}\sum_{1\le n\le X}\frac{a(n)}n.
\]

Let \(f:\mathbb N_{>0}\to\{0,1\}\) satisfy the **exact pointwise**
equation \(f(Tn)=f(n)\) for every positive integer \(n\).

**Theorem A: ordinary Fourier cancellation.** For every fixed real
\(\theta\notin\mathbb Z\),

\[
                  \boxed{\lim_{X\to\infty}\mathcal L_X(f(n)e(n\theta))=0.}
 \tag{FC}
\]

This is a statement about sampling the actual ordinary source integers.
It does not assert that the logarithmic mean \(\mathcal L_X f\) exists.
All its subsequential means may still be considered.

**Theorem B: a uniform approximation gap.** If \(f\) is nonconstant,
there is \(\epsilon_f>0\) such that every fixed finite trigonometric
polynomial

\[
                 Q(n)=\sum_{j=1}^{J}c_j e(n\theta_j),
                 \qquad c_j\in\mathbb C,\quad\theta_j\in\mathbb R,
\]

satisfies

\[
 \boxed{\liminf_{X\to\infty}\mathcal L_X|f-Q|\ge\epsilon_f.}
 \tag{BG}
\]

The same constant works for all finite frequency sets, all coefficients,
and all polynomial lengths. Each approximant is fixed **before**
\(X\to\infty\). Frequencies and complexity may vary with a requested
approximation accuracy; they may not be chosen anew for each cutoff.
No convergence rate uniform in the frequencies is asserted.

For a bounded sequence \(a\), set

\[
 \|a\|_{B^1}=\limsup_{X\to\infty}\frac1X\sum_{n\le X}|a(n)|.
\]

Besicovitch almost periodicity means membership in the \(B^1\)-closure
of the finite trigonometric polynomials with arbitrary real
frequencies. Thus (BG) implies

\[
        \inf_{Q\ {\rm trigonometric}}\|f-Q\|_{B^1}\ge\epsilon_f.
 \tag{BG-N}
\]

In particular, **an ordinary invariant Boolean label that is
Besicovitch almost periodic is constant.** Periodic functions of every
integer period are included. This enlarges the approximation class in
[PROFINITE_LABEL_RIGIDITY.md](PROFINITE_LABEL_RIGIDITY.md) from periods
\(2^a3^b\) to arbitrary rational and irrational frequencies.

The membership of an actual basin label in this larger approximation
class remains unproved. Section 8 gives a complete explicit obstruction
to replacing that missing step by zero entropy together with small
averaged errors in the functional equation.

## 1. What the primary literature contributes

Three precise ideas guide the proof.

* Kakutani's *Random Ergodic Theorems and Markoff Processes with a Stable
  Distribution*, Theorem 3, relates joint ergodicity of
  measure-preserving maps to their averaged Markov operator and a
  Bernoulli skew product. Section 4 proves the needed one-sided version
  directly, including its conditional-expectation step.
* Bergelson, Kułaga-Przymus, Lemańczyk, and Richter, *A structure theorem
  for level sets of multiplicative functions and applications*,
  Definition 1.1 and Section 2.3, distinguish general Besicovitch
  approximation from rational, periodic approximation. Their
  multiplicative-function structure theorems are not applied to
  Collatz labels.
* The solenoid dual to \(\mathbb Z[1/2,1/3]\) makes multiplication by
  both 2 and 3 invertible. Einsiedler and Lindenstrauss describe this
  model explicitly in Example 9.2 of *Rigidity properties for commuting
  automorphisms on tori and solenoids*. Here the relevant affine maps
  do not commute. Their joint invariant functions are handled by an
  elementary translation identity, without invoking a higher-rank
  measure-rigidity theorem or a positive-entropy hypothesis.

The primary links and exact inherited source pins are in Section 9.
The proofs below state all additional hypotheses they use.

## 2. The marginal analytic inputs and their scope

Let \(H_p\) denote normalized Haar measure on \(\mathbb Z_p\). For
independent positive geometric letters
\(\Pr(a_i=r)=2^{-r}\), put

\[
 Z_\infty=\sum_{i\ge1}3^{i-1}2^{-(a_1+\cdots+a_i)}
                 \quad\hbox{in }\mathbb Z_3,
 \qquad \nu=\operatorname{Law}(Z_\infty).
\]

This is a ternary unit with probability one: its first term is a unit
and all later terms are divisible by three. The geometric recursion,
or conditioning on the next fair binary symbol, gives stationarity
under the two maps

\[
                  F_0(z)=z/2,\qquad F_1(z)=(3z+1)/2
 \tag{1}
\]

with probabilities \(1/2,1/2\).

Define the finite densities

\[
       g_r(z)=3^r\Pr(Z_\infty\equiv z\pmod {3^r}),\qquad g_0=1.
\]

Tao's marginal fine-scale mixing and consistency, as used in the
pinned PR168 source, imply that \(g_r\) converges in \(L^1(H_3)\)
to a nonnegative density \(g\), and \(\nu=gH_3\). The audited
marginal atom-floor argument in the pinned earlier PR180 source gives
an absolute \(c_*>0\) with

\[
             g_r(z)\ge c_*\quad(r\ge1,\ z\notin3\mathbb Z_3).
 \tag{FLOOR}
\]

Consequently

\[
 g=0\quad H_3\hbox{-a.e. on }3\mathbb Z_3,\qquad
 g\ge c_*\quad H_3\hbox{-a.e. on }\mathbb Z_3^\times.
 \tag{2}
\]

For example, the second assertion follows from an almost-everywhere
convergent subsequence of the \(L^1\) convergence. Thus \(\nu\) and
Haar measure restricted to the units have the same null sets.
Only this equivalence and stationarity are used for Theorem A.
Neither a uniform upper bound for \(g\) nor a value of \(g\) at an
individual ordinary integer is used.

For Theorem B, one additional inherited consequence is needed. The
earlier PR180 marginal argument, Section 6, (LOG), supplies an absolute
\(c_{\log}>0\) such that every positive ternary-unit target \(q\) has

\[
 \liminf_{X\to\infty}
   \frac1{H_X}\sum_{\substack{n\le X\\\exists t\ge0,\ T^t(n)=q}}\frac1n
                         \ge\frac{c_{\log}}q.
 \tag{LOG}
\]

The separate LOG audit in
[PREDECESSOR_POPULATION_AUDIT.md](PREDECESSOR_POPULATION_AUDIT.md)
reconstructs it from the marginal floor: truncate the total valuation
at \(6s\), losing at most \((64/81)^s\), and sum disjoint inverse
depths of a small nonperiodic unit parent. It records the possible
choice \(c_{\log}=c_*/(44\log(64/3))\) for the constants in that
source's proof.

These are substantial analytic inputs, retained with their original
written-proof status. This note does not obtain (FLOOR) or (LOG) from
a bare total-variation error: the audited selected-prefix counting
argument is part of their dependency chain. In particular, the
separate, stronger joint-clock positive-natural-density claim is not
a hidden input.

## 3. A compact environment for every finite real frequency set

Fix the frequencies \(\theta_1,\ldots,\theta_J\). Choose real numbers
\(\beta_1,\ldots,\beta_d\) such that
\(1,\beta_1,\ldots,\beta_d\) are linearly independent over
\(\mathbb Q\) and span these frequencies over \(\mathbb Q\).
After clearing **all** denominators, including the rational constant
terms, there is \(D\ge1\) such that

\[
 \theta_j=\frac{a_{j0}}D+\sum_{\ell=1}^d a_{j\ell}\eta_\ell,
 \qquad \eta_\ell=\beta_\ell/D,\qquad a_{j\ell}\in\mathbb Z.
 \tag{3}
\]

Write \(D=2^u3^v m\), where \(\gcd(m,6)=1\). The cases \(d=0\)
and \(m=1\) are allowed. Put

\[
 \Sigma_6=\widehat{\mathbb Z[1/6]},\qquad
 K=\Sigma_6^d\times\mathbb Z/m\mathbb Z.
 \tag{4}
\]

Here the hat denotes the compact Pontryagin dual of the discrete
additive group. Explicitly, an element of \(\Sigma_6\) is a
homomorphism from \(\mathbb Z[1/6]\) to the unit circle. Since this
discrete group is countable, the compact group is metrizable.
Multiplication by 2 and by 3 are continuous Haar-preserving
automorphisms of \(K\).

Let \(\omega_\eta\in\Sigma_6\) be the homomorphism
\(r\mapsto e(r\eta)\), and set

\[
                 \omega=(\omega_{\eta_1},\ldots,\omega_{\eta_d},1).
\]

Its integer multiples are dense in \(K\). Indeed a character of \(K\)
has the form \((r_1,\ldots,r_d,k)\), with
\(r_\ell\in\mathbb Z[1/6]\) and \(k\in\mathbb Z/m\mathbb Z\);
its value at \(\omega\) is

\[
                      e\left(\sum_\ell r_\ell\eta_\ell+k/m\right).
\]

Rational independence with 1 shows that this equals 1 only for the
trivial character. The annihilator of the closure of the generated
subgroup is therefore trivial.

Use the full environment and ordinary embedding

\[
 \Omega_K=\mathbb Z_2\times\mathbb Z_3\times K,\qquad
 \iota(n)=(n,n,n\omega),\qquad
 H=H_2\times H_3\times H_K .
 \tag{5}
\]

Every \(Q(n)\) under consideration is the restriction of a continuous
function on \(\Omega_K\). Its irrational parts in (3) use the
characters at integer arguments in the solenoid factors. Its rational
parts are recovered from the residues modulo \(2^u,3^v,m\) by the
Chinese remainder theorem.

We need the following joint statement, not just separate
equidistribution of some coordinates:

\[
 \frac1X\sum_{n\le X}\delta_{\iota(n)}\ \Longrightarrow\ H,
 \qquad
 \frac1{H_X}\sum_{n\le X}\frac{\delta_{\iota(n)}}n\
                         \Longrightarrow\ H .
 \tag{6}
\]

To prove the first convergence, test a character. On \(\iota(n)\)
it is \(e(n\gamma)\), where

\[
             \gamma=\frac{a}{2^s}+\frac{b}{3^t}+\frac{k}{m}
                         +\sum_\ell r_\ell\eta_\ell.
\]

If some \(r_\ell\ne0\), rational independence with 1 makes
\(\gamma\) nonintegral. If all \(r_\ell=0\), the pairwise coprime
denominators \(2^s,3^t,m\) show that an integral \(\gamma\)
requires each finite character to be trivial. Every nontrivial
character therefore has Cesàro mean zero, by the finite geometric
sum formula. Finite linear combinations of characters are uniformly
dense in continuous functions on this compact abelian group, proving
the first assertion. Partial summation proves the harmonic version.

No assertion about the distribution of a particular Collatz orbit
is being made in (6).

## 4. Ergodicity of the stationary compact system

On \(K\), define

\[
                    A(w)=w/2,\qquad B(w)=(3w+\omega)/2.
 \tag{7}
\]

These are affine automorphisms preserving \(H_K\). On \(\Omega_K\)
define

\[
 S(x,z,w)=
 \begin{cases}
 (x/2,z/2,A(w)),&x\in2\mathbb Z_2,\\
 ((3x+1)/2,(3z+1)/2,B(w)),&x\in1+2\mathbb Z_2.
 \end{cases}
 \tag{8}
\]

In particular \(S\iota(n)=\iota(Tn)\) on every positive integer.
The probability measure

\[
                     \mu=H_2\times\nu\times H_K
 \tag{9}
\]

is stationary. We prove it is ergodic. We do not assert uniqueness
among all stationary measures, or require mixing of this enlarged
system.

### 4.1. The binary driving symbols

Under \(H_2\), the shortcut parity symbols form a sequence of
independent fair bits. For completeness, the inverse branches of the
two-adic map, with prescribed current parity, are
\(y\mapsto2y\) and \(y\mapsto(2y-1)/3\). Iterating them identifies
each length-\(r\) parity word with exactly one residue modulo \(2^r\).
Within that residue the terminal state is Haar and independent of
the word. These compatible finite identifications identify the
two-adic system with the one-sided fair Bernoulli shift
\(\mathcal B=\{0,1\}^{\mathbb N}\).

Let \(\sigma\) be the shift and \(F_0=A,F_1=B\) on \(K\). The reduced
system is

\[
                   S_0(b,w)=(\sigma b,F_{b_0}(w)).
 \tag{10}
\]

The product of fair Bernoulli measure and \(H_K\) is stationary
because each \(F_i\) preserves \(H_K\).

### 4.2. The affine translation forces joint invariants to be constant

Composition in the displayed order gives

\[
 AB(w)=\frac{3w+\omega}{4},\qquad
 BA(w)=\frac{3w+2\omega}{4},\qquad
                  BA(AB)^{-1}(w)=w+\omega/4.
 \tag{11}
\]

Since multiplication by 4 is an automorphism, \(\omega/4\) also
generates a dense subgroup. A function in \(L^2(H_K)\) invariant
under both \(A\) and \(B\) is invariant under the translation in
(11), and hence is constant almost everywhere. One can see the
last implication from Fourier coefficients: every nontrivial
character is nontrivial at the dense generator, so all nonconstant
coefficients vanish.

Now let \(h\) be a bounded \(S_0\)-invariant function and put
\(a(w)=\mathbb E_b h(b,w)\). Independence of the first bit and
the remaining bits gives

\[
                       a=\tfrac12(a\circ A+a\circ B).
 \tag{12}
\]

Both compositions on the right have the same \(L^2(H_K)\) norm as
\(a\). The parallelogram identity gives

\[
 \left\|\frac{a\circ A+a\circ B}{2}\right\|_2^2
       =\|a\|_2^2-\frac14\|a\circ A-a\circ B\|_2^2.
\]

Thus \(a\circ A=a\circ B=a\), so \(a\) is a constant \(c\).
For the sigma-algebra generated by \(w,b_0,\ldots,b_{N-1}\),
invariance iterated \(N\) times and independence of the remaining
bits give

\[
 \mathbb E[h\mid w,b_0,\ldots,b_{N-1}]
          =a(F_{b_{N-1}}\cdots F_{b_0}w)=c.
 \tag{13}
\]

These sigma-algebras increase to the full product sigma-algebra.
Conditional expectations converge in \(L^2\); consequently \(h=c\)
almost everywhere. This proves ergodicity of (10).

### 4.3. The ternary coordinate adds no invariant functions

In Bernoulli coordinates the full system has the form

\[
 (b,z,w)\longmapsto
      (\sigma b,F_{b_0}^{(3)}(z),F_{b_0}(w)),
\]

where \(F_0^{(3)},F_1^{(3)}\) are (1). Start with \(z,z'\) independently
distributed according to \(\nu\), the same Bernoulli bits \(b\),
and the same independent Haar state \(w\). Run both ternary states
with these common bits. After \(N\) steps their difference is

\[
                       z_N-z_N'=3^{s_N}2^{-N}(z-z'),
\]

where \(s_N\) is the number of ones among the first \(N\) bits.
They agree modulo \(3^r\) whenever \(s_N\ge r\).

Each coupled marginal at time \(N\) is still the stationary product
measure. To justify the product assertion, condition on the driving
word: every affine word sends Haar \(w\) to Haar independently of
that word and of \(z\). The ternary marginal, after averaging the
word, is \(\nu\) by stationarity; the remaining bits are independent
of everything already used.

If \(h\) is a bounded invariant function, let \(h_r\) be its
conditional expectation given the full \(b,w\) coordinates and
\(z\bmod3^r\). Then \(\|h-h_r\|_2\to0\) and
\(\|h_r\|_\infty\le\|h\|_\infty\). This convergence holds because
the finite ternary residue sigma-algebras, together with the other
two full coordinates, increase to the full product sigma-algebra.
Choose the finite-residue representatives of \(h_r\) so that equal
residues give equal values.

Invariance, the two stationary marginals, and the common-bit
coupling give

\[
 \begin{split}
 \mathbb E|h(b,z,w)-h(b,z',w)|^2
 &\le 6\|h-h_r\|_2^2\\
 &\quad+12\|h\|_\infty^2
                  \Pr(\operatorname{Bin}(N,1/2)<r).
 \end{split}
 \tag{14}
\]

First let \(N\to\infty\) at fixed \(r\), then let \(r\to\infty\).
The left side is zero. Hence \(h\) is independent of \(z\) almost
everywhere, by Fubini and the vanishing conditional variance. It
descends to an invariant function for (10), so it is constant.
This proves ergodicity of \(S\) for \(\mu\).

## 5. The ordinary branch identities give unweighted rigidity

This section is the strengthening over the earlier weighted
projection argument. It retains the even and odd branches
separately before taking a compact limit.

Fix an arbitrary sequence of cutoffs tending to infinity. On the
compact metrizable space (5), take a subsequence for which

\[
             \lambda_X^f=\frac1{H_X}\sum_{n\le X}
                            \frac{f(n)}n\,\delta_{\iota(n)}
                   \ \Longrightarrow\ \lambda .
 \tag{15}
\]

By (6) and \(0\le f\le1\), \(0\le\lambda\le H\). Write
\(\lambda=hH\) with \(0\le h\le1\).

Let \(E=\{x\in2\mathbb Z_2\}\), \(O=\Omega_K\setminus E\), and
\(C=\{z\equiv2\pmod3\}\), viewed as clopen subsets of \(\Omega_K\).
For a bounded continuous test \(\phi\), use exact ordinary
invariance and \(n=2q\) on the even branch of (15). The change
from cutoff \(X/2\) to \(X\) has bounded harmonic mass, and so
vanishes after division by \(H_X\). This gives

\[
                         S_*(\mathbf1_E\lambda)=\tfrac12\lambda.
 \tag{16}
\]

On the odd branch set \(q=(3n+1)/2\). The resulting positive
integers are exactly \(q\equiv2\pmod3\); the inverse is
\(n=(2q-1)/3\). Replacing \(3/(2q-1)\) by \(3/(2q)\) costs a
summable \(O(q^{-2})\) error. Changing the cutoff by the fixed
factor \(3/2\) again costs \(o(1)\) after harmonic normalization.
Thus

\[
                     S_*(\mathbf1_O\lambda)=
                               \tfrac32\mathbf1_C\lambda .
 \tag{17}
\]

All restrictions in these weak limits are clopen, so no boundary
regularity assumption is needed.

Compare (16)--(17) with the exact branch changes of Haar measure:

\[
 S_*(\mathbf1_E H)=\tfrac12H,\qquad
 S_*(\mathbf1_O H)=\tfrac32\mathbf1_C H .
 \tag{18}
\]

The even branch is a bijection \(E\to\Omega_K\); it removes the
factor \(1/2\) of binary Haar mass, while its ternary and \(K\)
maps preserve Haar. The odd branch is a bijection \(O\to C\).
It removes the same binary factor, maps ternary Haar onto three
times Haar restricted to the coset \(2+3\mathbb Z_3\), and
preserves Haar on \(K\).

If \(I_0,I_1\) are these inverse branch bijections, the
Radon--Nikodym densities in (16)--(18) say

\[
 h(I_0y)=h(y)\quad H\hbox{-a.e.},\qquad
 h(I_1y)=h(y)\quad H\hbox{-a.e. on }C.
\]

Pulling back through the respective branch maps yields

\[
                            h\circ S=h\quad H\hbox{-a.e.}
 \tag{19}
\]

Notice that \(\lambda\) itself need not be stationary for \(S\)
under Haar: summing (16)--(17) gives a nonconstant Jacobian.
It is its density \(h\) that is invariant.

Since \(\mu\ll H\), equation (19) also holds \(\mu\)-almost
everywhere. Section 4 therefore gives \(h=\delta\)
\(\mu\)-almost everywhere for a scalar \(0\le\delta\le1\).
By (2), \(\mu\) and \(H\) have the same null sets on

\[
                      U=\{z\in\mathbb Z_3^\times\}.
\]

Hence \(h=\delta\) \(H\)-almost everywhere on \(U\).

We must still handle ordinary ternary nonunits; it is not enough
to assert that \(\nu\) has full support. From (18),

\[
                  S_*H=(\tfrac12+\tfrac32\mathbf1_C)H,
 \tag{20}
\]

so \(S\) is Haar-nonsingular: the inverse image of an \(H\)-null
set is \(H\)-null. Consequently (19) can be iterated outside one
null set, and the preimages of the exceptional set in \(U\)
remain null. The binary parity sequence has a first odd symbol
at a finite time for \(H\)-almost every initial state. At that
step every ternary state enters \(C\subset U\), since
\((3z+1)/2\equiv2\pmod3\). Thus almost every initial state
eventually reaches the set where \(h=\delta\). Iterated (19)
implies \(h=\delta\) \(H\)-almost everywhere on all of
\(\Omega_K\).

We have proved the unweighted projection theorem

\[
             \boxed{\text{Every limit in (15) is }\lambda=\delta H.}
 \tag{UP}
\]

The scalar may depend on the cutoff subsequence. There was no
evaluation of the density \(g\) at an ordinary integer and no
assumption that the ordinary component already had any density.

## 6. Fourier cancellation and the uniform Besicovitch gap

For any continuous observable \(P\) on a fixed environment
\(\Omega_K\), (UP) implies the full, unqualified limit

\[
 \mathcal L_X\big(f(n)P(\iota(n))\big)
       -(\mathcal L_X f)\int P\,dH\longrightarrow0.
 \tag{21}
\]

Indeed every sequence of cutoffs has a further subsequence with a
limit (15). On that subsequence the two terms tend to the same
number \(\delta\int P\,dH\). Compactness and boundedness rule out
any nonzero subsequential limit of their difference.

For fixed \(\theta\notin\mathbb Z\), construct the environment
from that frequency. The function \(e(n\theta)\) is the restriction
of a nontrivial character. Its Haar mean is zero, either directly
from the character description or by (6). Equation (21) proves
(FC), without requiring (LOG) or the existence of \(\lim\mathcal L_Xf\).

Now suppose \(f\) is nonconstant. There are positive odd ternary
units \(a,b\) with \(f(a)=1\) and \(f(b)=0\). To find a unit in
either nonempty label class, strip powers of two from a representative;
if its odd part is divisible by three, take one accelerated odd
step and strip its powers of two. These are actual ordinary
iterates, preserve the label, and produce an odd ternary unit.

All predecessors of \(a\) have label one, and all predecessors
of \(b\) have label zero. Thus (LOG) gives, along every subsequence,

\[
       \eta\le\delta\le1-\eta,\qquad
       \eta=\min\{1/4,c_{\log}/a,c_{\log}/b\}>0 .
 \tag{22}
\]

Unlike the weighted proof, no conversion of the whole predecessor
population to a unit subfamily is needed here: (UP) concerns the
unweighted source measure.

Fix a trigonometric polynomial \(Q\), with its environment from
Section 3. Let \(P\) be the continuous function on that environment
obtained by clipping the real part of \(Q\) to \([0,1]\). For
\(f\in\{0,1\}\), pointwise,

\[
              |f-P|\le|f-Q|,\qquad
              |f-P|=f(1-P)+(1-f)P .
 \tag{23}
\]

The clipped function need not be a trigonometric polynomial; its
continuity on the same compact environment is all that is used.
Choose a cutoff sequence realizing the lower logarithmic mean of
\(|f-P|\), and then a subsequence as in (15). Equations (6), (UP),
and (23) give

\[
 \begin{split}
 \lim \mathcal L_X|f-P|
   &=\delta\int(1-P)\,dH+(1-\delta)\int P\,dH\\
   &\ge\min(\delta,1-\delta)\ge\eta .
 \end{split}
 \tag{24}
\]

The same \(\eta\) in (22) is independent of the environment,
frequencies, polynomial, and cutoff subsequence. This proves (BG)
with \(\epsilon_f=\eta\).

For any bounded nonnegative sequence \(a\), partial summation
gives

\[
 \limsup_{X\to\infty}\mathcal L_X a
         \le\limsup_{X\to\infty}\frac1X\sum_{n\le X}a(n).
 \tag{25}
\]

Therefore (BG-N) follows. The triangle inequality extends the
same distance bound to the entire \(B^1\)-closure of the
trigonometric polynomials. It also extends the logarithmic
lower bound: approximate a fixed bounded Besicovitch almost
periodic sequence \(v\) in \(B^1\), use (25) to bound the
logarithmic upper mean of the approximation error, then let
that error tend to zero. Thus

\[
 \liminf_X\mathcal L_X|f-v|\ge\eta
       \quad\hbox{for every bounded Besicovitch almost periodic }v .
 \tag{26}
\]

A natural lower mean bound is not asserted.

## 7. What is strengthened, and what the doubling equation cannot do

The rational-frequency part of (FC) says that every fixed residue
class receives its uniform share of each subsequential ordinary
logarithmic label mass. The irrational part supplies a larger
family of orthogonality relations. Equations (21)--(22) allow
diffuse projections \(\delta H\) with \(0<\delta<1\); they do
not make that scalar an indicator or exclude it.

This is more than a consequence of the doubling identity
\(f(2n)=f(n)\). A nonconstant Boolean periodic example satisfying
the latter is \(\mathbf1_{3\nmid n}\). There is also a simple
irrational-frequency example: for irrational \(\theta\), let

\[
             u(n)=\cos(2\pi\theta\,\operatorname{oddpart}(n)).
\]

Then \(u(2n)=u(n)\) and \(u\) is nonconstant. For \(V\ge1\),

\[
 u_V(n)=\sum_{0\le v<V}\mathbf1_{v_2(n)=v}
                                  \cos(2\pi\theta n/2^v)
\]

is a finite trigonometric polynomial, because each valuation
indicator is periodic. The difference is supported on
\(2^V\mid n\), with absolute value at most one, so
\(\|u-u_V\|_{B^1}\le2^{-V}\). Thus doubling invariance alone
permits nonconstant Besicovitch almost periodic functions.
The odd branch, the translation (11), and its exact ordinary
change of variables are essential to the proof above.

No theorem about arbitrary automatic or substitutive sequences
is being inferred. Nor does density of continuous functions in
an \(L^1\) space construct ordinary approximants: the ordinary
embedded integers are countable and Haar null. The proof starts
with their actual sums in (15), before introducing a density.

## 8. A rigorous obstruction to an averaged entropy shortcut

The next example isolates why a plausible weaker regularity
argument cannot replace the missing step. Define the computable
Boolean sequence

\[
 b(n)=\left\lfloor\sqrt{\lfloor\log_2 n\rfloor}\right\rfloor
                  \pmod2.
 \tag{27}
\]

Equivalently, \(b(n)=j\bmod2\) on the exact integer block
\([2^{j^2},2^{(j+1)^2})\).

### 8.1. Linear word complexity and zero topological entropy

Let \(p_b(L)\) be the number of different contiguous length-\(L\)
words occurring in \(b\). Write \(N_j=2^{j^2}\) and
\(\ell_j=N_{j+1}-N_j\); these run lengths increase. Choose the
least \(J\) with \(\ell_J\ge L\). If \(J\ge1\), then
\(\ell_{J-1}<L\) and \(N_{J-1}\le N_J/2\), giving \(N_J<2L\).
There are fewer than \(2L\) starting positions before \(N_J\).
Every length-\(L\) word starting at or after \(N_J\) meets at most
one boundary, since all subsequent runs have length at least \(L\).
The two constant words and the two orientations with each possible
cut give at most \(2L\) such words. If \(J=0\), there are no
earlier starts and the same latter bound suffices.

Consequently \(p_b(L)\le4L\) for every \(L\ge1\). The shift orbit closure
of this sequence has topological entropy
\(\lim_{L\to\infty}L^{-1}\log p_b(L)=0\).

### 8.2. Both colors have positive logarithmic mass in every residue

The harmonic mass of block \(j\) is

\[
 \sum_{2^{j^2}\le n<2^{(j+1)^2}}\frac1n
              =(2j+1)\log2+O(2^{-j^2}).
 \tag{28}
\]

The alternating sum of the first \(J\) odd numbers is \(O(J)\);
the total of those numbers is \(J^2\). A partially included
last block also has mass \(O(J)\). Thus

\[
                       \mathcal L_X b\longrightarrow\tfrac12 .
 \tag{29}
\]

For any fixed modulus \(q\) and residue \(r\), the harmonic
mass of that residue in an interval \([A,B)\) is
\(q^{-1}\log(B/A)+O_q(A^{-1})\), by counting and partial
summation. Apply this on the blocks in (28). The error is
summable, and hence

\[
 \mathcal L_X\big(\mathbf1_{n\equiv r\ (q)}b(n)\big)
                  \longrightarrow\frac1{2q}.
 \tag{30}
\]

In particular each color has logarithmic mass \(1/3\) among
ternary units. Positive mass on every finite residue class
therefore does not force mean almost periodicity.

### 8.3. The actual shortcut-equation defect tends to zero in mean

For every positive \(n\), \(1/2\le Tn/n\le2\), so the binary
heights of \(n\) and \(Tn\) differ by at most one. A change in
(27) is therefore possible only when the height lies at a
perfect square or immediately below one. Each such height
contributes a bounded harmonic mass; there are
\(O(\sqrt{\log X})\) of them up to \(X\). More explicitly,
the possible sources lie in the union of intervals
\([2^{j^2-1},2^{j^2+1})\), \(j\ge1\). It follows that

\[
             \mathcal L_X|b(Tn)-b(n)|
                        =O((\log X)^{-1/2})\longrightarrow0.
 \tag{31}
\]

The equation is not pointwise exact: \(b(1)=0\), whereas
\(b(T1)=b(2)=1\). This sequence is not an invariant Collatz
label or a counterexample to Collatz.

### 8.4. Distance one half from every almost periodic model

For \(\theta\notin\mathbb Z\), the finite geometric-sum formula
and summation by parts give

\[
          \left|\sum_{A\le n<B}\frac{e(n\theta)}n\right|
                              \le C_\theta/A .
 \tag{32}
\]

Sum (32) over the constant blocks on which \(b=1\), including
the possibly truncated last block. Since
\(\sum_j2^{-j^2}<\infty\), these sums are uniformly bounded
in the cutoff. Therefore

\[
                   \mathcal L_X(b(n)e(n\theta))\longrightarrow0
                         \quad(\theta\notin\mathbb Z).
 \tag{33}
\]

For a finite trigonometric polynomial \(P\), equations
(29) and (33) imply that its logarithmic mean is its constant
Fourier coefficient \(M(P)\), and
\(\mathcal L_X(bP)\to M(P)/2\). Uniform approximation extends
these identities to every Bohr almost periodic sequence,
meaning a uniform limit of finite trigonometric polynomials.
Thus for every such \(p\) taking values in \([0,1]\),

\[
 \lim_X\mathcal L_X|b-p|
   =\lim_X\mathcal L_X(b+p-2bp)
   =\tfrac12+M(p)-M(p)=\tfrac12 .
 \tag{34}
\]

For any complex trigonometric polynomial \(Q\), clipping
\(\operatorname{Re}Q\) to \([0,1]\) gives a Bohr almost
periodic sequence. Indeed it is a continuous function of a
finite torus rotation, and characters uniformly approximate
that continuous function on the orbit closure. Pointwise
clipping decreases the distance to \(b\). Consequently

\[
       \liminf_X\mathcal L_X|b-Q|\ge\tfrac12,\qquad
                              \|b-Q\|_{B^1}\ge\tfrac12 .
 \tag{35}
\]

The constant polynomial \(1/2\) attains equality. The triangle
inequality therefore shows that the \(B^1\)-distance of \(b\)
from the entire Besicovitch almost periodic class is exactly
\(1/2\).

This gives a precise failed implication: **zero topological
entropy, positive logarithmic masses in every residue, and
vanishing logarithmic mean error in the actual shortcut
equation do not imply Besicovitch almost periodicity.**
It does not disprove a proposed theorem that additionally
uses the exact pointwise equation. It also shows that the
Fourier cancellation conclusion alone cannot construct
almost periodic approximants.

## 9. Source ledger, evidence level, and remaining problem

The new proof depends on the following exact inherited files.

| Input | Frozen source | Exact byte pin |
|---|---|---|
| Stationary law and marginal \(L^1\) density, TM4/TM6 | PR168 at e4599b32e4b1a955ac9315d46782d4ad6a5db96c; research/closure-frontier-20261121/TERNARY_STATIONARY_BOUNDARY.md | SHA-256 543c0bd7a72d5dec598898850a49a257a9ef3b55cd1fff8741d8699fbad57a7c; Git blob 3b5ec5745ec6037bd4cd687877dd34f1e0a5dc03 |
| FLOOR and Section 6 LOG | PR180 at f87cb69b3dd86257731ddfbab58c87bf3b5f63d6; research/lean-ordinary-closure-20261121/LINEAR_BLOCK_ATOM_FLOOR.md | SHA-256 3e3d3c6c6206bf731ffb5da186bfb209e5d837a4f20f73749d6f79ef98dc30e2; Git blob 1cf40edfd0263a1f4b7f0d683d8cbaf1fcd50fc8 |
| Independent written audit, including its separately reconstructed LOG section | PREDECESSOR_POPULATION_AUDIT.md at checkpoint 2d478a6588f33a72fc3a5bdc085a928b5cf78737 | SHA-256 07cd8744f5ddd29016f976faa2fa9bb8becef3ff42e5ec7f5cba7b4fad9ec07d |
| Earlier weighted finite-period argument and precise ordinary-source safeguards | PROFINITE_LABEL_RIGIDITY.md at the same checkpoint | SHA-256 ec502a0e26562badfbfb615420ce80036917e1b39d6ec28be32c1a658b6cffa6 |

The present proof uses the earlier audit only for its marginal
FLOOR and LOG dependencies. Its separate verdict on the later
joint-clock positive-natural-density argument is outside this
dependency chain.

Primary sources:

1. Terence Tao, *Almost all orbits of the Collatz map attain almost
   bounded values*, Forum of Mathematics, Pi 10 (2022), e12,
   [DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8);
   [arXiv version 7](https://arxiv.org/html/1909.03562v7).
   The marginal inputs are Proposition 1.14, (1.26)--(1.27),
   and consistency (1.23). The version check and the substantial
   selected-prefix upgrade needed for FLOOR are recorded in the
   pinned audit.
2. Shizuo Kakutani, *Random Ergodic Theorems and Markoff Processes
   with a Stable Distribution*, Proceedings of the Second Berkeley
   Symposium on Mathematical Statistics and Probability (1951),
   pp. 247--261, [primary scan](https://digicoll.lib.berkeley.edu/nanna/record/112759/files/math_s2_article-18.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0),
   Theorem 3, beginning on p. 258. Sections 4.2--4.3 supply the
   complete one-sided skew and contracting-coordinate arguments
   used here.
3. Vitaly Bergelson, Joanna Kułaga-Przymus, Mariusz Lemańczyk,
   and Florian K. Richter, *A structure theorem for level sets of
   multiplicative functions and applications*, manuscript dated
   10 August 2017, [author manuscript](https://www-users.mat.umk.pl/~mlem/files/BeKuLeRi3.pdf),
   Definition 1.1 and Section 2.3, especially Theorem 2.7 and
   Corollary 2.8. The definitions distinguish the approximation
   classes; no multiplicativity of an ordinary basin is assumed.
4. Manfred Einsiedler and Elon Lindenstrauss, *Rigidity properties
   for commuting automorphisms on tori and solenoids*, Ergodic
   Theory and Dynamical Systems 42 (2022), pp. 691--736,
   [DOI 10.1017/etds.2021.74](https://doi.org/10.1017/etds.2021.74),
   Example 9.2. The solenoid realization is the only construction
   drawn from that example.

Sections 3--8 are written mathematical arguments. They establish
an ordinary-source orthogonality theorem, a larger rigidity class,
and an explicit obstruction to an averaged entropy shortcut.
They do not establish that a Collatz component has zero entropy,
is automatic, is substitutive, or is Besicovitch almost periodic.
They do not prove the disappearance of a fixed original survivor
atom, exclude every divergent ordinary orbit, or exclude every
nontrivial cycle.

The exact remaining regularity problem for this route is to
derive, from the actual basin rather than an ambient compact
representative, approximants \(Q_\varepsilon\) fixed independently
of the observation cutoff with
\(\|f-Q_\varepsilon\|_{B^1}<\varepsilon\) for all
\(\varepsilon>0\). The theorem would then force that label to
be constant. The explicit sequence (27) identifies several
weaker properties that cannot supply this step by themselves.
