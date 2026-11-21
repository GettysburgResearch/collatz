# A uniform ordinary predecessor population, and the remaining renewal step

## Status and exact dependence

This continuation proves a stronger ordinary population consequence of the
new joint clock argument in [`JOINT_CLOCK_MIXING.md`](JOINT_CLOCK_MIXING.md).
It also records an independent check of that argument at its critical
interfaces. These are **written analytic results**, not Lean declarations.
The imported non-elementary input is Tao's published nonnegative renewal
estimate, as specified in the companion note. The finite-word arithmetic
and the population argument below are elementary.

For the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\]

write \(n\to a\) for an actual finite ordinary trajectory ending at \(a\).
The result is that there are **absolute** constants \(c,C>0\) such that,
for every positive integer \(a\) with \(3\nmid a\),

\[
\boxed{X\ge Ca\quad\Longrightarrow\quad
 \#\{n\le X:n>0,\ n\text{ odd},\ n\to a\}\ge cX/a.}       \tag{PD}
\]

After changing the two absolute constants, the counted sources may also be
required to satisfy \(3\nmid n\). Thus the conclusion is a uniform
finite-scale statement, not only a target-dependent asymptotic density.
No constants are claimed numerically effective from the existing analytic
proof. In particular, this note does not provide a numerical convergence
cutoff or prove that every orbit reaches one.

The target restriction is essential. If \(3\mid a\), its direct ordinary
predecessors may be only its doubling ancestors. An arbitrary ordinary
component nevertheless contains a ternary unit, so every component has
positive lower natural density as a consequence of (PD).

## 1. Independent check of the new clock argument

The review was performed against the complete companion proof, not by
inferring a joint theorem from its older marginal fine-scale statement.
The primary source is Terence Tao, *Almost all orbits of the Collatz map
attain almost bounded values*,
[DOI 10.1017/fmp.2022.8](https://doi.org/10.1017/fmp.2022.8), Section 6,
equations (7.4)--(7.5), Lemma 7.2, and Proposition 7.3, equation (7.10).
The following are the points checked independently.

1. **The whole clock is measurable after the pairing.** Conditional on
   every pair sum \(b_j=a_{2j-1}+a_{2j}\), and also the last unpaired
   letter in odd length, the exponent total is fixed. Multiplication by
   any bounded complex function of that total leaves the same
   nonnegative product-of-moduli envelope. The renewal bound therefore
   controls the \(\ell^1\) norm of the sliced Fourier coefficients, by
   duality. It is not merely a bound for their possibly cancelling sum.

2. **A shorter conductor retains the extra clock.** A character of
   conductor \(3^h\) sees only the first \(h\) offset letters. The
   remaining letters contribute an independent sum to the total, so
   their contribution is convolution by a probability mass function.
   This contracts the sliced \(\ell^1\) bound and does not discard those
   clock letters.

3. **The prefix entropy estimate is unaffected.** At fixed prefix length
   and fixed prefix total, the source separation argument bounds the
   largest prefix atom by \(2^{-\ell}\). The suffix is independent of
   all these prefix conditions. Summing the squared suffix Fourier
   coefficients over its total costs at most the square of their
   \(\ell^1\) norm. After a total-clock cutoff of \(6n\), the passage
   to joint total variation has only a polynomial loss. The arbitrarily
   high polynomial renewal bound absorbs that loss.

4. **Projection keeps the final total.** The projection from level
   \(n\) to level \(m\) is exactly the joint law at \(m\), convolved
   in its clock by the negative-binomial law for \(n-m\) letters.
   It is not the law of the shorter total. Lifting and this clock
   convolution are contractions in the stated mixed norm, so the
   geometric telescoping step is valid.

5. **The selected-prefix estimate has the necessary mixed norm.** Its
   bound is \(\sup_r\sum_u|H(u,r)|\). One first sums absolute values
   over the shifted clocks, then applies the same fixed-total spatial
   counting bound. No unjustified interchange to
   \(\sum_u\sup_r|H(u,r)|\) is required.

6. **The local clock lower bound survives all errors.** At a fixed
   positive residue of one finite initial selected density, a finite
   collection of clocks carries positive mass. Their fixed shifts
   satisfy the negative-binomial local lower bound at all sufficiently
   large final depths; one can use the Gaussian constant for a slightly
   wider window to include its endpoints. For early telescoping errors,
   the remaining clock kernel has maximum atom \(O(N^{-1})\); for
   late errors the summed loss, after multiplication by \(N\), is
   \(O(N^{4-K})\). Choosing \(K>5\) makes both estimates adequate.
   The same telescope can end at every intervening final depth.

7. **The real offset remains bounded.** The unconditioned terminal
   suffix has length \(O(N)\), even though its clock is unbounded.
   Its real offset is less than \(2^{O(N)}\), while the selected
   prefix multiplier is at most \((7/8)^{\Theta(N^2)}\). Therefore
   fixing one final total does not introduce a large real offset.
   Spreading the positive cylinder uses a uniformly bounded initial
   exponent and only shifts the central clock window by a fixed amount.

No gap was found at these interfaces. This review does not amount to a
formalization of Tao's theorem or of the analytic argument. It licenses
the following precise written input, not an unrestricted independence
claim for the total and the residue.

## 2. The fixed-total input

Put

\[
\alpha=\log_2 3,\qquad \delta=2-\alpha>0.
\]

There are absolute \(B,c_0>0\) and \(s_0\) such that, for every
integer \(s\ge s_0\), every unit residue \(r\pmod{3^s}\), and every
integer \(A\) with \(|A-2s|\le\sqrt s\), the retained length-\(s\)
words have

\[
 A(w)=A,\quad 0\le\beta_w\le B,\quad
 \beta_w\equiv r\pmod{3^s},\qquad
 \sum_w3^s2^{-A}\ge\frac{c_0}{\sqrt s}.              \tag{F}
\]

Each fixed-total word family is finite. In particular its cardinality is
at least

\[
                 \frac{c_0}{\sqrt s}\frac{2^A}{3^s}. \tag{2.1}
\]

This is the input called (CFJ) in the companion note. No separate local
limit assumption conditional on a particular residue is added here.

## 3. A nonperiodic unit parent of controlled size

Choose once and for all an integer \(e_0\ge1\) with
\(2^{e_0}>6B+1\). For a supplied positive unit \(a\), consider

\[
             b_e=\frac{2^e a-1}{3},\qquad
             e_0\le e\le e_0+5.
\]

The powers of two modulo nine run through all six units. Exactly two of
these six exponents have \(2^e a\equiv4\) or \(7\pmod9\); for them
\(b_e\) is a positive odd ternary unit. They satisfy

\[
                 2B<b_e\le K_Ba,\qquad
                 K_B=2^{e_0+5}/3.                    \tag{3.1}
\]

Both are actual ordinary predecessors of \(a\): the identity
\(3b_e+1=2^e a\) gives \(T^e(b_e)=a\). This remains true when
\(a\) is even. In that case the next accelerated odd value is the odd
part of \(a\), not necessarily \(a\) itself.

At most one of the two candidates is periodic under the accelerated odd
map \(U\). Indeed, a periodic candidate hitting \(a\) puts \(a\) on
the same ordinary cycle. The next odd value of either candidate is the
odd part of \(a\). A cycle has only one preceding odd member for that
odd member, so two different candidates cannot both be periodic.
Choose a nonperiodic candidate and denote it by \(b\).

The word ``nonperiodic'' here permits eventual entry into a cycle. Its
required consequence is only that no ordinary source can hit \(b\) at
two distinct accelerated depths. Two such hits would make \(b\) itself
periodic.

## 4. Linear many actual predecessors

Fix a real \(X>b\), and set

\[
 L=\log_2(X/b),\qquad S=L/\delta,\qquad
 \kappa=\frac1{4\delta}.
\]

Take all integers \(s\) in

\[
                  |s-S|\le\kappa\sqrt S,             \tag{4.1}
\]

and put

\[
                  A_s=\lfloor L+\alpha s\rfloor.
\]

For every sufficiently large \(S\), with an absolute threshold,
all these depths satisfy

\[
 s\ge s_0,\quad S/2\le s\le2S,\quad
 |A_s-2s|\le\delta|S-s|+1
                 \le\sqrt S/4+1\le\sqrt s.           \tag{4.2}
\]

There are at least \(\kappa\sqrt S\) such integers after increasing
that absolute threshold. The floor defining \(A_s\) gives

\[
       X/2< b\,2^{A_s}/3^s\le X.                    \tag{4.3}
\]

Apply (F) to the actual residue of \(b\pmod{3^s}\), with total
\(A_s\). Every retained word gives the integer

\[
             n_w=\frac{2^{A_s}}{3^s}(b-\beta_w).
\]

The congruence in (F) makes each inverse step integral. Positivity of the
odd target and positivity of every exponent make each inverse parent
positive and odd. Thus these are genuine length-\(s\) accelerated
predecessors of \(b\), with ordinary shortcut clock exactly \(A_s\).
Using \(b>2B\) and (4.3),

\[
                       X/4<n_w\le X.                \tag{4.4}
\]

At a fixed depth, different admissible words give different sources:
their deterministic accelerated forward trajectories recover all their
exponents. The number at that depth is consequently at least

\[
 \frac{c_0}{\sqrt s}\frac{2^{A_s}}{3^s}
                >\frac{c_0X}{2b\sqrt s}.             \tag{4.5}
\]

Sources at different depths in (4.1) are also distinct, by the
nonperiodicity of \(b\). Summing (4.5), and using \(s\le2S\), gives

\[
 \#\{n\in(X/4,X]:n\text{ odd},\ n\to b\}
       \ge\frac{c_0\kappa}{2\sqrt2}\frac Xb.         \tag{4.6}
\]

If needed, decrease the positive coefficient in this inequality. The
threshold used throughout is merely \(S\ge S_*\), for one absolute
\(S_*\). Equivalently, it is

\[
                          X\ge2^{\delta S_*}b.
\]

Finally \(b\le K_Ba\) and \(b\to a\). Taking

\[
 C=2^{\delta S_*}K_B,\qquad
 c=\frac{c_0\kappa}{2\sqrt2K_B}
\]

proves (PD), and in fact proves its stronger interval version with sources
in \((X/4,X]\). All constants are independent of the supplied target.
The clock \(A_s+e\) to \(a\) is allowed to depend on the depth;
no common clock across the entire union in (4.6) is asserted.

The argument uses every integer depth in (4.1). There is no shrinking
rotation-window assumption or unproved equidistribution rate in this
counting step.

## 5. Unit sources without an additional mixing hypothesis

For an odd source \(n\to a\), with \(3\nmid a\), define

\[
 F(n)=\begin{cases}n,&3\nmid n,\\4n+1,&3\mid n.\end{cases}
\]

The output is always odd and a ternary unit. In the second case
\(n\ne a\), so its actual hitting path has at least one shortcut step.
The exact identity

\[
                     T^3(4n+1)=T(n)                 \tag{5.1}
\]

therefore implies \(F(n)\to a\). This argument also preserves hits to
even targets; it does not replace the target by its odd part.

Every output has at most two preimages under \(F\): one possible source
from each branch of its definition. The image of sources at most \(Y\)
lies at most \(4Y+1\). Thus (PD) gives

\[
 \#\{m\le4Y+1:m>0,\ m\text{ odd},\ 3\nmid m,\ m\to a\}
                   \ge\frac{cY}{2a}\qquad(Y\ge Ca).
\]

Substitute \(Y=(X-1)/4\) and enlarge the absolute onset constant.
Since \(Y\ge X/8\) for \(X\ge2\), one obtains absolute
\(c_{\rm u},C_{\rm u}>0\) with

\[
 X\ge C_{\rm u}a\quad\Longrightarrow\quad
 \#\{m\le X:m>0,\ m\text{ odd},\ 3\nmid m,\ m\to a\}
                         \ge c_{\rm u}X/a.           \tag{PDU}
\]

No extra cap on a terminal exponent and no conditional unit-source local
limit theorem are needed for this consequence.

## 6. Applying the uniform population to actual renewal

The improved onset removes a real quantifier obstruction in simultaneous
counting. For a finite set \(\mathcal A\) of unit targets whose full
predecessor sets are pairwise disjoint, (PD) now holds simultaneously at
every \(X\ge C\max\mathcal A\). Consequently

\[
              c\sum_{a\in\mathcal A}\frac1a\le1.   \tag{6.1}
\]

Unlike a lower-limit argument, this is a finite-scale inequality with one
explicit form of cutoff. It still bounds a reciprocal sum; it does not
give a positive constant contribution for every target regardless of its
height.

In particular, choose one off-orbit unit parent \(b_i<22q_i\) for each
member \(q_i\) of an injective odd orbit, as in
[`DIVERGENT_ORBIT_PHASES.md`](DIVERGENT_ORBIT_PHASES.md). Their predecessor
sets are pairwise disjoint. Formula (6.1) reproves a bounded reciprocal
occupation sum, now from a uniform finite-scale population. It does not
force that sum to diverge. Counting several nested ancestor levels as
disjoint would be incorrect.

The marked survivor mass still has to decrease under its **actual**
ordinary return transport. A positive predecessor population is not a
loss term in that mass balance. The new theorem also does not bound the
five-defect energy of an ordinary invariant label. It discharges the
stronger positive-natural-density premise, but the incoming charge and
renewal inequalities remain separate obligations.

## 7. A tested spectral route and its first unsupported step

One global attempt was to use the inverse pressure at an exponent
\(1<s<2\). For a leading inverse operator on ternary-unit densities,
an inverse letter \(e\) has multiplier \((3/2^e)^s\). Change of variables
in ternary Haar measure contributes \(1/3\), giving the total Haar mass
factor

\[
                \lambda(s)=\frac{3^{s-1}}{2^s-1}<1
                    \qquad(1<s<2).                  \tag{7.1}
\]

The strict inequality follows from the strict concavity of
\(s\mapsto\log(2^s-1)-(s-1)\log3\), which vanishes at both
endpoints. This scalar contraction suggests a finite incoming-weight
estimate, but does not establish one on individual ordinary targets.

There is an exact obstruction to upgrading it to a bounded positive
ternary eigenfunction without real-state control. The ternary integer
\(-1\) is fixed by the inverse letter \(e=1\), whose contribution is
\((3/2)^s\). An eigenfunction positive at that point cannot have
eigenvalue \(\lambda(s)<1\). Ordinary positive integers arbitrarily
close to \(-1\) in the ternary metric also realize arbitrarily long
finite chains of this expanding branch. Thus a residue-only bounded
comparison cannot supply the missing ordinary contraction.

For a positive ordinary target \(q\), legal inverse words instead satisfy
the real condition \(\beta_w<q\). Retaining this condition yields the
correct positive-real/ternary transfer problem. A global incoming-weight
bound for that killed transfer has not been established here. Dropping
the real condition, or replacing the scalar Haar factor in (7.1) by a
pointwise ordinary estimate, would be the first unsupported step.

## Conclusion of this attack

The new clock estimate supports a uniform linear population of ordinary
predecessors at every sufficiently large scale relative to the supplied
target, including unit sources. That statement improves the earlier
logarithmic-density result and has a full written proof above.

Neither survivor absorption nor finite-energy closure follows from the
population lower bound alone. The full Collatz conclusion remains open
in this checkpoint; none of these analytic statements is inserted into
Lean as an axiom.
