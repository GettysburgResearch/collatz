# Effective phase distribution on every distinct ordinary segment

**22 November 2026. Written finite theorem and an unsuccessful global
closing attempt.** No hypothetical orbit is replaced by random parity.
Every estimate below applies to a supplied actual finite segment whose
odd states are distinct. The consequence for an escaping orbit is
uniform in the source and in the starting position of the window.

The qualitative phase mechanism is already present in PR173 and PR176.
The new calculation combines distinctness with that mechanism to obtain
a source-independent discrepancy bound and a growing binary run
threshold. Its elementary version is explicit. Consuming Rhin's
published linear-form bound strengthens it to a power of the window
length, and forces a run threshold proportional to log N. It also gives
an elementary route to the qualitative run-density and run-moment
conclusions of PR177. It does **not** replace PR177's S-unit theorem
about a finite-core return at specified separations.

## 1. Exact finite statement

Let

\[
 q_0,q_1,\ldots,q_N\in\mathbb N_{>0},\qquad
 2^{g_i}q_{i+1}=3q_i+1,\quad g_i\ge1,
 \tag{1}
\]

be actual successive odd states. Assume only that the first N states
are pairwise distinct. Put

\[
 \alpha=\log_2 3,\quad
 \theta_i=\{\log_2 q_i\},\quad
 \epsilon_i=\log_2\left(1+\frac1{3q_i}\right),\quad
 H_N=\sum_{j=1}^N\frac1j.
\]

For any circular interval I, write

\[
 D_N=\sup_I\left|
 \frac1N\#\{i<N:\theta_i\in I\}-|I|\right|.
\]

The supremum is over intervals on the unit circle, with a consistent
half-open endpoint convention. For N >= 256, one explicit bound is

\[
 \boxed{
 D_N\le d_N:=\min\left\{1,
 \frac{16\log3}{\log N}
 +\frac{1+2(1+\log N)/(3\log2)}{\sqrt N}
 \right\}.}
 \tag{2}
\]

All unmarked logarithms are natural. The constants are deliberately
loose. The useful features are the decay and the absence of any initial
height, source-dependent threshold, independent-gap premise, or external
Collatz estimate.

Using Rhin's exponent 7.616 as explained in Section 3.1 gives the
stronger written theorem

\[
 \boxed{D_N\le C_R
 \left(\frac{1+\log N}{N}\right)^{1/8.616}
 =O(N^{-1/9}).}
 \tag{2a}
\]

The absolute constant is independent of the supplied segment. A
numerical value of it is not computed here. The positive constant in
Rhin's theorem is a literature input, not a Lean axiom.

For any positive integer h, an additional exact Fourier bound is

\[
 \boxed{
 \left|\frac1N\sum_{i<N}e^{2\pi i h\theta_i}\right|
 \le
 \frac{2+(2\pi h/(3\log2))H_N}
 {N\,|e^{2\pi i h\alpha}-1|}.}
 \tag{3}
\]

The denominator is nonzero because 3^h is not a power of two.

## 2. The entire perturbation budget comes from distinct integers

Taking logarithms in (1) gives the exact circle recurrence

\[
 \theta_{i+1}=\theta_i+\alpha+\epsilon_i\pmod1.
 \tag{4}
\]

Since log(1+x) <= x for x >= 0,

\[
 0<\epsilon_i\le\frac1{3\log2\,q_i}.
\]

If distinct positive integers are arranged increasingly as
a_1 < ... < a_N, then a_j >= j. Therefore

\[
 \boxed{\sum_{i<N}\epsilon_i
 \le\frac1{3\log2}\sum_{i<N}\frac1{q_i}
 \le\frac{H_N}{3\log2}
 \le\frac{1+\log N}{3\log2}.}
 \tag{5}
\]

No eventual lower bound on the states is needed. In particular (5)
holds on every shifted distinct window, with the same constants.

For (3), put z_i=exp(2 pi i h theta_i) and a=exp(2 pi i h alpha).
Equation (4) and |exp(it)-1| <= |t| give

\[
 |z_{i+1}-az_i|\le2\pi h\epsilon_i.
\]

The algebraic telescope is

\[
 (a-1)\sum_{i<N}z_i
 =z_N-z_0-\sum_{i<N}(z_{i+1}-az_i).
\]

Use |z_N-z_0| <= 2 and (5). This proves (3).

## 3. A direct discrepancy proof with elementary denominators

The proof of (2) uses rational grids, so it does not need a quantitative
linear-forms theorem or a separately imported discrepancy inequality.

Let p/q be a continued-fraction convergent to alpha, with next denominator
q'. The elementary convergent identities give

\[
 \gcd(p,q)=1,\qquad
 |\alpha-p/q|<\frac1{qq'}\le\frac1{q^2}.
 \tag{6}
\]

For completeness, these follow from the consecutive-convergent
determinant of absolute value one and

\[
 \alpha-\frac pq
 =\frac{\pm1}{q(qx+q_-)},
 \qquad qx+q_->q',
\]

where x is the next complete quotient and q_- the preceding denominator.
The denominators are unbounded for irrational alpha.

There is also an elementary exponential upper bound on the next
denominator. Since |q alpha-p| < 1, the distinct positive integers 3^q
and 2^p satisfy

\[
 |q\alpha-p|
 =\frac{|\log(3^q/2^p)|}{\log2}
 \ge\frac{|3^q-2^p|}{\log2\,\max(3^q,2^p)}
 >\frac1{2\log2\,3^q}.
\]

Together with |q alpha-p| < 1/q', this gives

\[
 q'<2\,3^q.
 \tag{7}
\]

Choose the largest convergent denominator q <= floor(sqrt(N)). Its
successor exceeds that cutoff. For N >= 256, (7) implies

\[
 \frac{\log N}{4\log3}\le q\le\sqrt N.
 \tag{8}
\]

Indeed floor(sqrt(N)) >= sqrt(N)/2, so
q > (log N/2-log4)/log3, which implies (8).

For an exact rotation, the q points theta+t alpha, 0 <= t < q,
are within circle distance 1/q of the translated rational grid
theta+t p/q. That grid visits every residue j/q once. Its interval
count differs from q times interval length by at most two; expanding
and contracting by 1/q therefore give the safe bound 4/q for its
normalized interval discrepancy.

Divide the actual N-term window into complete blocks of length q and
one remainder. On a complete block starting at b, the actual phase
theta_(b+t) differs from theta_b+t alpha by at most

\[
 E_b=\sum_{i=b}^{b+q-1}\epsilon_i
\]

in circle distance. Expanding or contracting the tested interval by
E_b bounds the block discrepancy by 4/q+2E_b. This is still valid
if the expanded interval is the whole circle. Averaging the complete
blocks and bounding the remainder by q/N gives

\[
 D_N\le\frac4q
       +\frac{2q}{N}\sum_{i<N}\epsilon_i+\frac qN.
 \tag{9}
\]

Equations (5) and (8) prove (2). The direct block proof also supplies
(9) for any available convergent denominator q <= N, which can be
sharper than the simple closed expression (2).

### 3.1. Consume Rhin's linear-form theorem on the same actual segment

The published paper of Lagarias--Soundararajan reproduces the following
result of Rhin in Lemma 5.3, equation (5.11): for some absolute C>0 and
integers u_0,u_1,u_2 with H=max(|u_1|,|u_2|)>=1,

\[
 |u_0+u_1\log2+u_2\log3|\ge C H^{-7.616}.
 \tag{9a}
\]

This is the linear-form theorem being used. Their separate stochastic
starting-seed theorem is not an input. The relevant full-paper proof
was inspected; Rhin's original 1987 book chapter was not independently
reconstructed.

Put tau=7.616. For a convergent p/q of alpha, 1<=p/q<=2, so substituting
(u_0,u_1,u_2)=(0,-p,q) in (9a) gives

\[
 |q\alpha-p|\ge c q^{-\tau}.
 \tag{9b}
\]

Combining with |q alpha-p|<1/q' yields q'<=C_0 q^tau. For any large
cutoff Q, choose the largest convergent denominator q<=Q. Its successor
exceeds Q; consequently

\[
 c_0 Q^{1/\tau}\le q\le Q.
 \tag{9c}
\]

Set L_N=1+log N and choose
Q=(N/L_N)^(tau/(tau+1)). Equation (9), with (5), now gives

\[
 \begin{split}
 D_N
 &\le C_1 Q^{-1/\tau}+C_2 QL_N/N\\
 &\le C_3(L_N/N)^{1/(\tau+1)}.
 \end{split}
 \tag{9d}
\]

Enlarging C_3 covers the remaining finite range. This proves (2a).
Since 1/8.616>1/9, the logarithmic factor is absorbed by that strict
exponent margin. More generally D_N=O_beta(N^(-beta)) for every
0<beta<1/8.616. Every inequality still concerns one supplied distinct
ordinary segment; no averaging over starting integers is introduced.

## 4. Growing binary run counts

Let R(n) count maximal runs of ones in the binary expansion of n.
For integers m,S >= 1 define

\[
 K(m,S)=\sum_{j=0}^{\min(2S-1,m-1)}\binom{m-1}{j}.
\]

This is exactly the number of length-m binary words that start in one
and contain at most S one-runs: the number of transitions between
adjacent digits is at most 2S-1.

For each leading word b, 2^(m-1) <= b < 2^m, its phase interval has
length log_2(1+1/b) <= 2^(1-m)/log2. A number with at least m bits
and at most S full runs has one of the K(m,S) prefixes. There are at
most 2^(m-1) distinct smaller positive integers. Consequently

\[
 \boxed{
 \frac1N\#\{i<N:R(q_i)\le S\}
 \le\frac{2^{m-1}}N
 +K(m,S)\left(\frac{2^{1-m}}{\log2}+d_N\right).}
 \tag{10}
\]

The displayed finite bound uses only the supplied distinct window.
There is no quantifier change from varying finite witnesses to one
infinite ordinary source.

First use the elementary bound (2). For fixed S, take
m=floor(log_2(log N)). Then (10) gives

\[
 \frac1N\#\{i<N:R(q_i)\le S\}
 =O_S\left(\frac{(\log\log N)^{2S-1}}{\log N}\right),
 \tag{11}
\]

uniformly over all such actual windows.

More generally, fix 0<c<1/4 and put S=floor(c m). For sufficiently
large m, the binomial bound

\[
 K(m,S)\le2^{(m-1)H_2(2c)}
\]

follows by applying the binomial theorem with x=2c/(1-2c)<1 to
the sum over at most 2S-1 transitions. Since H_2(2c)<1, (10) gives

\[
 \boxed{
 \frac1N\#\{i<N:R(q_i)\le\lfloor c\lfloor\log_2\log N\rfloor\rfloor\}
 =O_c\bigl((\log N)^{-(1-H_2(2c))}\bigr).}
 \tag{12}
\]

For instance c=1/8 gives the positive decay exponent
1-H_2(1/4). The asymptotic estimates are consequences of the explicit
finite inequality (10); their constants are not fitted to computations.

For every rho>1 and every 0<kappa<(log_2 rho)/4, it follows that

\[
 \boxed{\frac1N\sum_{i<N}\rho^{R(q_i)}
 \ge C_{\rho,\kappa}(\log N)^\kappa}
 \tag{13}
\]

for all sufficiently large N, uniformly over every supplied distinct
ordinary window. Choose c<1/4 with c log_2 rho>kappa and use (12).

Every non-eventually periodic positive orbit has all odd states distinct,
so (11)--(13) hold on all its shifted windows. In particular bounded-run
times have upper Banach density zero. A periodic orbit is covered only
over a segment with distinct states; repeating a finite cycle does not
satisfy the distinctness hypothesis.

### 4.1. Polynomial occupation decay and logarithmic run growth

In (10), d_N may be replaced by any proved upper bound on D_N.
Use (2a) in its simpler O(N^(-1/9)) form and take
m=floor((log_2 N)/9). For every fixed S>=1 this yields

\[
 \boxed{\frac1N\#\{i<N:R(q_i)\le S\}
 =O_S\left(N^{-1/9}(\log N)^{2S-1}\right).}
 \tag{13a}
\]

For 0<c<1/4, take S=floor(c m). The same prefix count gives

\[
 \boxed{\frac1N\#\{i<N:
 R(q_i)\le\lfloor c\lfloor(\log_2N)/9\rfloor\rfloor\}
 =O_c\left(N^{-(1-H_2(2c))/9}\right).}
 \tag{13b}
\]

Indeed, the short-integer term is O(N^(-8/9)), while
K(m,S)<=2^((m-1)H_2(2c)) and both 2^(-m) and D_N are
O(N^(-1/9)). The exponents in (13a)--(13b) are positive and the
constants are uniform over all the actual windows under consideration.
Thus every rho>1 and every 0<kappa<(log_2 rho)/36 satisfy

\[
 \boxed{\frac1N\sum_{i<N}\rho^{R(q_i)}
 \ge C_{\rho,\kappa}N^\kappa}
 \tag{13c}
\]

for all sufficiently large N. Select c<1/4 with
c log_2(rho)/9>kappa and use the complement of (13b).
If desired, replace 1/9 throughout by any beta<1/8.616;
the corresponding moment condition is kappa<beta log_2(rho)/4.

The just-published PR176 checkpoint at fdcb137 proves a different,
fully explicit fixed-S upper count of O_S(N/log N) using ESS and its
actual finite core. Equation (13a) gives a stronger asymptotic
occupation rate through the linear-form theorem, with a literature
constant left unspecified. PR176's logarithmic-horizon sparse-return
descent and PR177's fixed-separation finite-core theorem provide
additional geometric information not implied by this phase estimate.

## 5. Applying the stronger bound to the actual closing estimate

PR177's canonical terminal-energy input, with all its original analytic
qualifications, gives on any hypothetical escaping ray

\[
 \mathfrak e_N(q_j)\ge c_0/N
 \quad(J\le j\le N-K)
\]

for fixed positive c_0 and fixed J,K. Apply (13c) to the interior
distinct window. For every rho>1 and
0<kappa<(log_2 rho)/36,

\[
 \boxed{\sum_x\rho^{R(x)}\mathfrak e_N(x)
 \ge c_1N^\kappa}
 \tag{14}
\]

eventually, with c_1 depending on the supplied component constants.
Thus the previously qualitative divergence now has a polynomial lower
rate, and its arithmetic part uses Rhin instead of the S-unit theorem.
The weaker logarithmic lower rate follows from (13) without that
transcendence input.

I tried to use phase coboundaries to obtain the contrary upper bound.
This does not close. PR175 evaluates the actual canonical commutator
for fixed truncated run weight w_L=min(rho^R,rho^L): its asymptotic
retains 2 rho^L b_infinity minus a term bounded independently of L.
The boundary drift is already controlled there. Hence finite forcing
and the phase identity do not give a cutoff-uniform transported-energy
bound; the uncontrolled commutator is precisely capable of carrying
the growth in (14). No such upper bound was proved in this pass.

The subsequent PR177 checkpoint at 0444986 evaluates every finite-Green
depth/time regime. Its uniform profile retains
W b_infinity min(M/N,1) for each sign at fixed truncated weight W.
Taking M=o(N) removes the corresponding finite-depth energy but leaves
the full Green tail with the surviving increasing energy. That result
does not provide a contrary upper bound for (14).

The new ternary entropy ceiling of PR185 does not contradict the phase
law either. Leading binary mantissas and fixed ternary residue digits
are different observables. Irrational circle rotation has uniform
one-time phase distribution and zero dynamical entropy. The proof above
does not supply a positive entropy lower bound for the actual ternary
time law or its inverse-branch policy.

## 6. Source pins and evidence boundary

- PR173, `fa0c9e2a2851e6324391e39c17afcb5913185aec`,
  `research/lean-shell-cover/ForwardSection.lean`: the actual logarithmic
  perturbed-rotation mechanism and forced band.
- PR176, `00018ce11fa657b5f3fae072e5567a1d93184c2b`,
  `research/lean-global-resolvent-20261121/overview/machinery/ACTUAL_COMPACT_JOINING.md`:
  actual phase-Haar projection and its compact-law limitations.
- PR177, `e4ca639326bac73da8c2a698dec8a749e5efbe68`,
  `research/lean-exact-witness-global-20261121/LITERATURE_ARITHMETIC_RETURN.md`
  and `LITERATURE_CANONICAL_ENERGY.md`: stronger S-unit finite-core
  return, qualitative run consequences, and qualified actual energy.
- PR175, `08fe1388ad63c758680b3695249aca319515c47d`,
  `research/lean-global-closure-20261121/machinery/EXACT_RUN_WEIGHT_COMMUTATOR.md`:
  the exact surviving commutator used in Section 5.
- PR185, `980d40fc4afeaaf8f2a9256f322acf3e4568e013`,
  `research/deep-closing-20261122/ACTUAL_ORBIT_ENTROPY.md`: the distinct
  ternary time-law entropy ceiling.

Late source additions:

- PR176, fdcb137214f4be8ac30dbb025d6eeb6568e22e2a:
  [effective occupation](https://github.com/GettysburgResearch/collatz/blob/fdcb137214f4be8ac30dbb025d6eeb6568e22e2a/research/lean-global-resolvent-20261121/overview/returns/EFFECTIVE_RUN_OCCUPATION.md)
  and
  [logarithmic sparse-return descent](https://github.com/GettysburgResearch/collatz/blob/fdcb137214f4be8ac30dbb025d6eeb6568e22e2a/research/lean-global-resolvent-20261121/overview/returns/LOGARITHMIC_SPARSE_RETURN_DESCENT.md),
  compared in Section 4.1.
- PR177, 0444986571f09f302cb3687b4bba3552600e4119:
  [finite-Green depth/time profile](https://github.com/GettysburgResearch/collatz/blob/0444986571f09f302cb3687b4bba3552600e4119/research/lean-exact-witness-global-20261121/ENERGY_TRANSPORT_CONTINUATION.md),
  compared in Section 5. Its proof is source-qualified here rather
  than a fresh audit of the entire canonical construction.

The elementary convergent estimates are also derived in
[Ben Lynn's author-hosted continued-fraction notes, Bounds](https://crypto.stanford.edu/pbc/notes/contfrac/converge.html).
The classical broader Benford literature includes Lagarias--Soundararajan,
[*Benford's Law for the 3x+1 Function*, JLMS 74 (2006), 289--303](https://doi.org/10.1112/S0024610706023131),
whose [author manuscript, Lemma 5.3 and equation (5.11)](https://arxiv.org/pdf/math/0509175)
states the precise Rhin theorem used in Section 3.1. The original
reference is G. Rhin, *Approximants de Padé et mesures effectives
d'irrationalité*, Séminaire de Théorie des Nombres, Paris 1985--1986,
Progress in Mathematics 71 (1987), 155--164, inequality (8).
The separate Lagarias--Soundararajan main theorem concerns most
starting seeds and their finite shortcut prefixes. It is not being
substituted for a statement about every supplied distinct odd-state
segment here. No general historical priority claim for conditional
leading-digit equidistribution or this application is made.

The discrepancy, run-occupation and moment consequences of
equations (2), (2a), and (9)--(14), the continued-fraction argument, and the
connection to the canonical energy are written mathematics. The separate
Lean subdirectory states exactly which finite core is formalized; its
audit does not certify the remaining closing estimate. No escape or
nontrivial-cycle exclusion is claimed.
