# Polynomial-phase rigidity and an exact-doubling control

## Status and main result

**Independently reviewed written derivation from the stated frozen analytic
inputs.** The new derivation and control were checked by a separate
collaborating agent; the inherited inputs retain their earlier review scope.
This continuation starts
from [LITERATURE_RIGIDITY_BRIDGE.md](LITERATURE_RIGIDITY_BRIDGE.md) at published
PR182 commit `45354128f890fb479f6c23b547368bcddd9cebe6`, SHA-256
`b31fd7aaa0d911eeda02345604ccc8d96661672a37cf45faf057f481f7cdce81`.
It retains exactly that note's marginal stationary-density and FLOOR inputs;
the positive approximation gap additionally uses its LOG input. Those
inputs retain their separately audited written-proof status. The newer
joint-clock natural-density assertion is not used.

The new positive theorem replaces linear phases by **all real polynomial
phases, of every fixed finite degree**. The new control satisfies the
ordinary doubling equation exactly, has zero topological entropy, and has
a vanishing logarithmic mean defect in the other shortcut equation, but
still stays a fixed distance from the approximation class. Neither result
constructs approximants for the actual basin label or proves full Collatz.

Write

\[
 T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
 \quad e(t)=\exp(2\pi i t),\quad
 H_X=\sum_{n\le X}\frac1n,\quad
 L_X(a)=H_X^{-1}\sum_{n\le X}\frac{a(n)}n.
\]

Let \(f:\mathbb N_{>0}\to\{0,1\}\) obey \(f(Tn)=f(n)\) pointwise.
For every real polynomial \(P\), let

\[
 m(P)=\lim_{N\to\infty}\frac1N\sum_{n\le N}e(P(n)).
\]

This mean exists. It is zero if some nonconstant coefficient is irrational;
otherwise the phase is a constant times a periodic sequence.

**Theorem P1.** Under the stationary-density and FLOOR inputs,

\[
 \boxed{L_X(f(n)e(P(n)))-L_X(f)m(P)\longrightarrow0.}
 \tag{P1}
\]

In particular \(L_X(fe(P))\to0\) whenever \(P\) has an irrational
nonconstant coefficient. Rational polynomial phases need centering:
for example \(m(n^2/4)=(1+i)/2\), which is not zero.
No existence of \(\lim L_X(f)\) is assumed.

**Theorem P2.** If \(f\) is nonconstant, LOG gives one \(\eta_f>0\)
such that every fixed finite sum

\[
 Q(n)=\sum_{\ell=1}^{J}c_\ell e(P_\ell(n)),
 \qquad c_\ell\in\mathbb C,\quad P_\ell\in\mathbb R[n],
\]

satisfies

\[
 \boxed{\liminf_X L_X|f-Q|\ge\eta_f.}
 \tag{P2}
\]

The same constant is independent of the degrees, polynomial coefficients,
and number of summands. Every approximant is fixed before \(X\to\infty\).
There is no uniform cancellation rate over polynomials allowed to change
with the cutoff.

Let \(\mathcal P\) be the closure of these sums in the ordinary
Besicovitch seminorm

\[
 \|a\|_{B^1}=\limsup_{X\to\infty}X^{-1}\sum_{n\le X}|a(n)|.
\]

Then the same positive logarithmic gap holds for every bounded member of
\(\mathcal P\), and \(\inf_{v\in\mathcal P}\|f-v\|_{B^1}\ge\eta_f\).
Thus membership of the actual basin-of-one indicator in \(\mathcal P\)
would imply full convergence. This is a strictly larger candidate
approximation class than the linear-phase class of the preceding note.
Its membership for an actual invariant label remains unproved.

## 1. A finite compact model for a family of polynomial phases

Fix finitely many real polynomials, of maximum degree \(d\ge1\).
Discard their constant terms into the scalar coefficients. Choose real
numbers \(\beta_1,\ldots,\beta_s\) such that
\(1,\beta_1,\ldots,\beta_s\) are rationally independent and span all
nonconstant coefficients together with 1. Clear all denominators with one
integer \(D\), and put \(\eta_i=\beta_i/D\). Each coefficient now has
the form \(a_0/D+\sum_i a_i\eta_i\) with integers \(a_i\).
Write \(D=2^u3^v m\), where \((m,6)=1\).

Put \(R=\mathbb Z[1/6]\), \(\Sigma_6=\widehat R\), and

\[
 K=(\Sigma_6^d)^s\times\mathbb Z/m\mathbb Z.
\]

The cases \(s=0\) and \(m=1\) are allowed. Scalars in \(R\) act
continuously on \(\Sigma_6\); every unit of \(R\) acts as an
automorphism. Let \(\omega_i\in\Sigma_6\) be the character
\(r\mapsto e(r\eta_i)\). The ordinary auxiliary point is

\[
 \kappa(n)=((n^j\omega_i)_{1\le i\le s,\ 1\le j\le d},
                     n\bmod m).
 \tag{1.1}
\]

Together with the ordinary binary and ternary embeddings, use

\[
 \Omega=\mathbb Z_2\times\mathbb Z_3\times K,
 \quad \iota(n)=(n,n,\kappa(n)),
 \quad H=H_2\times H_3\times H_K.
\]

Every phase in the fixed family is the restriction of a continuous
function on \(\Omega\). The rational polynomial part is recovered
from \(n\bmod D\), using the binary, ternary, and coprime residue factors;
the irrational parts use the moment-coordinate characters.

### Joint ordinary equidistribution

On the ordinary points, a character of \(\Omega\) has the form

\[
 e\!\left(n\Bigl(\frac a{2^r}+\frac b{3^t}+\frac k m\Bigr)
          +\sum_{i,j} r_{ij}\eta_i n^j\right),\qquad r_{ij}\in R.
\]

If some \(r_{ij}\ne0\), choose the greatest such degree \(j\).
Its coefficient is irrational by rational independence with 1.
Weyl's polynomial equidistribution theorem makes the character mean zero.
If all moment coefficients vanish, the remaining nontrivial finite
character has mean zero by the Chinese remainder theorem and the
geometric-sum identity. Consequently

\[
 X^{-1}\sum_{n\le X}\delta_{\iota(n)}\Longrightarrow H,
 \qquad H_X^{-1}\sum_{n\le X}\frac{\delta_{\iota(n)}}n
                         \Longrightarrow H.
 \tag{1.2}
\]

The first assertion follows by uniform density of the characters in the
continuous functions on this compact metrizable abelian group; the second
follows by partial summation. This is ordinary-source equidistribution,
not an assertion about an individual Collatz orbit.

The only new external equidistribution input is the classical polynomial
Weyl theorem. A primary author exposition is Tao, *Higher Order Fourier
Analysis*, Section 1.1, Corollary 1.1.9; its proof is induction on degree
using finite differences and van der Corput. The precise link is in
Section 7. No quantitative estimate uniform in degree or coefficients is
needed here.

## 2. The affine lift and its commutator

For a unit \(a\in R\) and \(b\in R\), define an affine map on each
moment block by

\[
 (V_{a,b}x)_{i,j}
   =\sum_{k=1}^{j}\binom jk a^k b^{j-k}x_{i,k}+b^j\omega_i.
 \tag{2.1}
\]

On the finite factor use \(z\mapsto az+b\), where the fractions are
well defined because \((m,6)=1\). The diagonal entries of the linear
part are the units \(a^j\), so \(V_{a,b}\) is a continuous affine
automorphism preserving Haar measure. The binomial identity gives

\[
 V_{a,b}V_{c,d}=V_{ac,ad+b},\qquad
 V_{a,b}^{-1}=V_{a^{-1},-b/a},\qquad
 V_{a,b}\kappa(n)=\kappa(an+b)
 \tag{2.2}
\]

in the moment sense, including rational arguments for the last formula.
One way to verify composition without assuming actual moment relations
among the coordinates is to regard \(x\) as a linear functional on
polynomials, with \(x(1)=\omega_i\), and act by substitution
\(P(X)\mapsto P(aX+b)\). Thus (2.2) is valid on the entire compact
group, not only on the embedded ordinary points.

Set

\[
 A=V_{1/2,0},\qquad B=V_{3/2,1/2},\qquad U_t=V_{1,t}.
\]

These give exactly the two ordinary shortcut branches. Their commutator is

\[
 AB=V_{3/4,1/4},\qquad BA=V_{3/4,1/2},\qquad
 BA(AB)^{-1}=U_{1/4},\qquad U_{1/4}^{,4}=U_1.
 \tag{2.3}
\]

Hence every function invariant under both \(A\) and \(B\) is
invariant under \(U_1\). This last map is a polynomial skew translation,
not an ordinary translation in all moment coordinates.

## 3. Haar ergodicity of the polynomial skew translation

We prove that \(U_1\) is ergodic on \(K\). A character is indexed by
\((r_{ij},k)\in R^{sd}\times\mathbb Z/m\mathbb Z\). The linear part
of pullback under \(U_1\) acts on its moment indices by

\[
 (Tr)_{i,\ell}=\sum_{j\ge\ell}\binom j\ell r_{ij}.
 \tag{3.1}
\]

If the greatest nonzero moment degree is \(J\ge2\), then for an index
\(i\) with \(r_{i,J}\ne0\),

\[
 (T^N r)_{i,J}=r_{i,J},\qquad
 (T^N r)_{i,J-1}=r_{i,J-1}+NJr_{i,J}.
 \tag{3.2}
\]

Since \(R\) is torsion free, this dual orbit is infinite. The Fourier
coefficients of an invariant \(L^2(H_K)\) function have equal magnitudes
along this orbit: the affine constants multiply coefficients by unit
phases. Square summability therefore makes every such coefficient zero.

The only remaining character indices have moment degree at most one.
They are fixed by the linear part, and their full pullback phase is

\[
 e\!\left(\sum_i r_{i,1}\eta_i+k/m\right).
 \tag{3.3}
\]

Rational independence with 1 makes (3.3) different from 1 for every
nontrivial such character. Their coefficients also vanish. Thus an
invariant \(L^2\) function is constant, proving ergodicity. This argument
covers the purely finite case \(s=0\) as well.

This is the load-bearing improvement over the linear-frequency proof:
Fourier indices of higher degree need not be fixed, but their infinite
unipotent orbits still force their coefficients to vanish. No mixing rate
or higher-rank commuting-action theorem is asserted.

## 4. Transfer back to the actual ordinary label

The stationary compact shortcut system is

\[
 S(x,z,w)=
 \begin{cases}
 (x/2,z/2,Aw),&x\text{ even},\\
 ((3x+1)/2,(3z+1)/2,Bw),&x\text{ odd}.
 \end{cases}
\]

It satisfies \(S\iota(n)=\iota(Tn)\). Let \(\nu\) be the frozen
stationary ternary law and \(\mu=H_2\times\nu\times H_K\).
Both auxiliary branches preserve Haar. Every common branch invariant is
constant by Sections 2--3. These are exactly the auxiliary hypotheses
used by Sections 4.1--4.3 of the preceding note:

1. The binary parity coding gives independent fair bits.
2. Averaging an invariant function over the bits gives
   \(h=(h\circ A+h\circ B)/2\). Equality of the two composition norms
   and the parallelogram identity force separate branch invariance.
3. Conditional expectations on successively longer initial bit words then
   make the whole reduced invariant function constant.
4. Coupling two ternary states with the same bits makes their difference
   divisible by \(3^r\) after \(r\) odd symbols. Approximation by finite
   ternary cylinders removes that initial coordinate.

Thus \(\mu\) is ergodic. None of these arguments requires the auxiliary
embedding to be a group homomorphism; the exact intertwining identity and
(1.2) are what matter.

For completeness, the ordinary-limit step is unchanged. Along a common
cutoff subsequence let

\[
 \lambda_X=H_X^{-1}\sum_{n\le X}\frac{f(n)}n\delta_{\iota(n)}
                      \Longrightarrow\lambda=hH,\quad0\le h\le1.
\]

Domination follows from (1.2). With \(E\) and \(O\) the binary branch
sets and \(C=\{z\equiv2\pmod3\}\), ordinary changes of variables give

\[
 S_*(1_E\lambda)=\tfrac12\lambda,\qquad
 S_*(1_O\lambda)=\tfrac32 1_C\lambda.
 \tag{4.1}
\]

The identical Jacobians hold for \(H\). Since each branch is a
bijection onto its image, (4.1) gives \(h\circ S=h\) Haar almost
everywhere. Stationary ergodicity makes \(h\) constant for \(\mu\).
FLOOR identifies the null sets of \(\mu\) and Haar on ternary units.
The Haar pushforward is \((1/2+3\,1_C/2)H\), so the map is
nonsingular. Almost every binary state has a first odd symbol, which
sends every ternary state into \(C\). Pulling back null sets therefore
extends the same constant to all of \(H\):

\[
                 \lambda=\delta H,\qquad0\le\delta\le1.
 \tag{4.2}
\]

The scalar may vary with the chosen cutoff subsequence. Consequently, for
every fixed continuous \(F\) on this polynomial environment,

\[
 L_X(f(n)F(\iota(n)))-L_X(f)\int F\,dH\longrightarrow0.
 \tag{4.3}
\]

Every cutoff sequence has a further weakly convergent subsequence, and
both terms then tend to the same scalar multiple. This proves the full
limit (4.3), hence P1, without assuming a mean for \(f\).

## 5. A uniform approximation gap, with no degree bound

For a nonconstant Boolean label choose opposite-label positive odd ternary
unit targets \(a,b\), as in the preceding note. Every predecessor keeps
its target's label. LOG therefore gives along every cutoff subsequence

\[
 \eta_f\le\delta\le1-\eta_f,
 \qquad\eta_f=\min\{1/4,c_{\log}/a,c_{\log}/b\}>0.
 \tag{5.1}
\]

For a fixed polynomial-phase sum \(Q\), build the single common compact
environment of Section 1. Clip its real part to a continuous \([0,1]\)
observable \(F\) on that environment. Since \(f\) is Boolean,

\[
 |f-F|\le|f-Q|,\qquad |f-F|=f(1-F)+(1-f)F.
\]

Use (4.2) along a subsequence realizing the lower logarithmic error.
Its limit is

\[
 \delta\int(1-F)\,dH+(1-\delta)\int F\,dH
                     \ge\min(\delta,1-\delta)\ge\eta_f.
\]

This proves P2. Neither the source targets in (5.1) nor \(\eta_f\)
depends on the polynomial environment. Partial summation gives
\(\limsup L_X|a|\le\|a\|_{B^1}\) for bounded sequences. The
triangle inequality therefore extends the logarithmic lower bound and the
ordinary \(B^1\) distance bound to the closure \(\mathcal P\).

The enlargement is strict. For irrational \(\alpha\), the sequence
\(e(\alpha n^2)\) belongs to the polynomial-phase class and has zero
ordinary correlation with every linear exponential, by Weyl. It cannot
lie in the bounded linear Besicovitch class: approximation in \(B^1\),
followed by clipping to the closed unit disk, would give bounded linear
almost-periodic approximants in \(B^2\), contradicting that
orthogonality. Continuous clipping of a finite linear phase sum is
uniformly approximable in its same compact frequency environment.

## 6. A stronger control with the doubling equation exact

The preceding slow-block sequence was

\[
 b(n)=\lfloor\sqrt{\lfloor\log_2 n\rfloor}\rfloor\pmod2.
\]

Let \(\operatorname{odd}(n)=n/2^{v_2(n)}\), and define

\[
                  c(n)=b(\operatorname{odd}(n)).
 \tag{6.1}
\]

Then **\(c(2n)=c(n)\) pointwise**. The remaining conclusions below
are unconditional elementary statements; they use none of FLOOR, LOG,
or the stationary density.

### 6.1. Quantitative logarithmic proximity

Put \(H=\lfloor\log_2 X\rfloor\). For \(n=2^v m\) with \(m\)
odd, the two colors can differ only if some square lies between the binary
heights of \(m\) and \(2^vm\). At fixed \(v\), at most
\(v\lfloor\sqrt H\rfloor\) dyadic height levels are eligible.
Each dyadic interval has harmonic mass at most one. Dropping the oddness
restriction only enlarges the sum, so

\[
 \begin{split}
 \sum_{n\le X}\frac{|c(n)-b(n)|}{n}
 &\le\sum_{v=1}^{H}2^{-v}v\lfloor\sqrt H\rfloor\\
 &\le2\sqrt H.
 \end{split}
 \tag{6.2}
\]

Thus \(L_X|c-b|=O((\log X)^{-1/2})\). Both colors of \(c\) have
logarithmic mass one half, and

\[
 L_X(1_{n\equiv r\ (q)}c(n))\longrightarrow\frac1{2q}
\]

for every fixed modulus and residue, by the corresponding elementary
slow-block calculation for \(b\).

### 6.2. The whole shortcut defect tends to zero

For any nonnegative error sequence \(d\), the ordinary branch changes
and \(3/(2q-1)\le2/q\) for \(q\ge2\) give

\[
 \sum_{n\le X}\frac{d(Tn)}n
       \le\frac12\sum_{q\le X/2}\frac{d(q)}q
          +2\sum_{q\le(3X+1)/2}\frac{d(q)}q.
 \tag{6.3}
\]

Apply this to \(d=|c-b|\), use (6.2), and insert the already proved
\(O((\log X)^{-1/2})\) logarithmic defect of \(b\). The triangle
inequality yields

\[
                 L_X|c(Tn)-c(n)|=O((\log X)^{-1/2}).
 \tag{6.4}
\]

The odd equation is not pointwise exact: \(T(11)=17\), while
\(c(11)=1\) and \(c(17)=0\).

### 6.3. Polynomial word complexity and zero topological entropy

Here is a deliberately conservative bound that does not rely on the
specific square-block choice. For **any** binary sequence \(a(k)\), the
sequence

\[
 d(n)=a(\lfloor\log_2 n\rfloor-v_2(n))
\]

has

\[
                    p_d(L)\le4L+64L^2(L+1),\qquad L\ge1.
 \tag{6.5}
\]

To prove it, choose a power \(Q=2^R\) with \(2L\le Q<4L\).
Starting positions below \(Q\) contribute fewer than \(4L\) words.
In a length-\(L\) window starting at \(N\ge Q\), there is at most one
multiple of \(Q\), so at most one position with valuation at least
\(R\). The binary height has at most one transition, since two successive
power-of-two boundaries in this range are separated by at least \(L\).
Writing \(K=\lfloor\log_2 N\rfloor\ge R\), every other position uses
one of the \(R+1\) bits

\[
              a(K-R+1),\ldots,a(K+1).
\]

The word is determined by the starting residue modulo \(Q\), these
\(R+1\) bits, the height-transition position (at most \(L+1\) options),
and the one possible high-valuation bit (at most two options). Therefore
there are at most

\[
 Q\,2^{R+1}(L+1)\,2=4Q^2(L+1)<64L^2(L+1)
\]

such words. This proves (6.5). In particular \(c\) has zero topological
entropy. Counting complexity of prefixes only would not suffice here;
the bound explicitly covers windows at all offsets.

### 6.4. Orthogonality to every bounded zero-Cesaro-mean sequence

A stronger summation fact explains why this control defeats polynomial
and nilsequence approximation alike. If \(a\) is bounded and
\(A(N)=\sum_{n\le N}a(n)=o(N)\), then

\[
                         L_X(b(n)a(n))\longrightarrow0.
 \tag{6.6}
\]

Indeed summation by parts expresses the unnormalized sum using an endpoint
term, the smooth differences of \(1/n\), and one jump term at each
\(2^{j^2}\). Given \(\varepsilon>0\), choose \(N_0\) with
\(|A(N)|\le\varepsilon N\) for \(N\ge N_0\). The smooth terms above
\(N_0\) total at most \(\varepsilon\log X+O(\varepsilon)\), and the
jump terms total \(O(\varepsilon\sqrt{\log X})\). The finite initial
part is \(O_{N_0}(1)\). Division by \(H_X\), followed by
\(\varepsilon\to0\), proves (6.6). Equation (6.2) gives the same
conclusion with \(c\) in place of \(b\).

Consequently, for every sequence \(p(n)\in[0,1]\) whose ordinary
Cesaro mean \(M(p)\) exists,

\[
 L_X(cp)\to\tfrac12M(p),\qquad
 \boxed{L_X|c-p|\to\tfrac12.}
 \tag{6.7}
\]

For a finite complex polynomial-phase sum \(Q\), clipping its real part
to \([0,1]\) gives a sequence with an ordinary mean by (1.2). Clipping
cannot increase error. Hence

\[
 \liminf_X L_X|c-Q|\ge\tfrac12,
 \qquad \inf_{v\in\mathcal P}\|c-v\|_{B^1}=\tfrac12.
 \tag{6.8}
\]

The constant \(1/2\) attains equality. The same logarithmic distance in
(6.7) applies to every \([0,1]\)-valued nilsequence: those have ordinary
means, by the nilrotation equidistribution theorem. This last fact concerns
the control, not a claimed nilsequence decorrelation theorem for an actual
Collatz invariant label.

Thus zero entropy, exact doubling, positive logarithmic color masses in
every residue, and vanishing mean shortcut error still do not produce
polynomial-phase approximation. The exact odd relation remains essential.
In particular \(c\) itself has no ordinary Cesaro mean, since otherwise
one could put \(p=c\) in (6.7).

## 7. Literature, nilsequence boundary, and next actual-label obligation

Primary references used for the new steps:

1. Terence Tao, *Higher Order Fourier Analysis*, Section 1.1, Corollary
   1.1.9, [author's preliminary AMS version](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf).
   Only the fixed-polynomial Weyl theorem is used. Joint character testing
   and the affine lift above are written explicitly.
2. A. Leibman, *Pointwise convergence of ergodic averages for polynomial
   sequences of translations on a nilmanifold*, Ergodic Theory and
   Dynamical Systems 25 (2005), pp. 201--213,
   [publisher primary statement](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/pointwise-convergence-of-ergodic-averages-for-polynomial-sequences-of-translations-on-a-nilmanifold/6208D0707B5DED9422B9400874428105).
   This is used only for existence of ordinary means of nilsequences in
   the control discussion. Uniform limits preserve existence of the mean.
3. Nikos Frantzikinakis, *The structure of strongly stationary systems*,
   [author preprint](https://arxiv.org/abs/math/0403453).
   Its Bernoulli and nilsystem structure suggests a broader direction;
   no strong-stationarity hypothesis for the actual label process is
   proved or imported here.

General nilsequences are not identified with classical polynomial phases.
For example, a nilmanifold can require nonabelian or bracket coordinates
that are not continuous functions of the finite moment model used here.
A proposed generalization would need an actual compact extension admitting
both shortcut affine automorphisms, their measure preservation, ordinary
joint equidistribution, and ergodicity of the commutator translation.
A dilation of one nilrotation orbit can alter finite components or its
orbit closure. None of these missing interfaces is supplied merely by
naming the nilsequence inverse theorem.

Likewise, fixed-polynomial cancellation cannot be upgraded silently to a
uniform Gowers-norm estimate: an inverse-theorem witness may depend on the
cutoff, whereas P1 fixes the polynomial first. The countermodel in Section 6
also shows that orthogonality, low complexity, and an exact doubling law do
not force the desired structured approximation.

The actual-label closing target remains to derive the necessary structure
from **both exact ordinary branch equations**, or to prove a multipoint
merger/correlation statement that forces constancy directly. This note
establishes stronger structural consequences of a hypothetical nonconstant
label and a stronger control for failed shortcuts. It does not establish
that such a label exists, rule out all such labels, or complete Collatz.
