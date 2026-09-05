# T-9827 -- Maximal phase runs form an exact odd-carry zipper

Claim ID: `T-9827`
Title: Maximal binary-chart runs transport one positive odd carry through exact dyadic and odd-place cylinders
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-wave16-completion-cold-review`
Reviewing agents: `gpt56-synthesis-01`; `gpt56-synthesis-01-wave14-period-ten`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: local `T-9823` and `L-9801`
Scope: every nontrivial binary expanding-chart recurrence with positive ordinary tails; exact `4 -> 5` specialization
Related counterexample candidates: issue #26; interfaces with issue #31 and PR #35; no `K-####` candidate

## Setup and run indexing

Let

\[
 U=2^a,
 \qquad a\ge1,
 \qquad V>U\text{ odd},
 \qquad C=V-U.
\tag{1}
\]

Suppose positive ordinary integers `M_n>1` and binary symbols
`epsilon_n` satisfy the exact recurrence of `T-9823`,

\[
 \boxed{UM_{n+1}=VM_n-C\epsilon_n.}
\tag{2}
\]

Reduction modulo `U` gives

\[
 M_n\equiv\epsilon_n\pmod U.
\tag{3}
\]

By `T-9823`, both symbols occur infinitely often.  The code therefore has a
unique decomposition into finite maximal runs.  Put `p_0=0` and define

\[
 p_{k+1}=\min\{n>p_k:\epsilon_n\ne\epsilon_{p_k}\},
 \qquad
 \ell_k=p_{k+1}-p_k\ge1,
\tag{4}
\]

\[
 s_k=\epsilon_{p_k},
 \qquad
 \sigma_k=2s_k-1\in\{-1,1\}.
\tag{5}
\]

Thus

\[
 \epsilon_n=s_k\quad(p_k\le n<p_{k+1}),
 \qquad
 s_{k+1}=1-s_k,
 \qquad
 \sigma_{k+1}=-\sigma_k.
\tag{6}
\]

In particular, `sigma_k=-1` on a zero-run and `sigma_k=1` on a one-run.

## Theorem 1 -- exact maximal-run odd-carry zipper

For every `k>=0`, there is a positive odd integer `q_k` such that

\[
 \boxed{M_{p_k}=s_k+U^{\ell_k}q_k.}
\tag{7}
\]

Every state in that run has the exact form

\[
 \boxed{
 M_{p_k+j}
 =s_k+U^{\ell_k-j}V^j q_k
 }
 \qquad(0\le j\le\ell_k).
\tag{8}
\]

At the common boundary between runs `k` and `k+1`, the two expressions in
(8) and (7) give the exact zipper equation

\[
 \boxed{
 U^{\ell_{k+1}}q_{k+1}
 =V^{\ell_k}q_k+\sigma_k.
 }
\tag{9}
\]

Consequently the next run length is an exact dyadic valuation:

\[
 \boxed{
 v_2\!\left(V^{\ell_k}q_k+\sigma_k\right)
 =a\ell_{k+1}.
 }
\tag{10}
\]

The zipper also removes every prime factor of `V` from the outgoing carry:

\[
 \boxed{\gcd(q_k,V)=1\qquad(k\ge1).}
\tag{11}
\]

For every prime `r` dividing `V`, equation (9) gives the exact odd-place
transport law

\[
 v_r\!\left(U^{\ell_{k+1}}q_{k+1}-\sigma_k\right)
 =\ell_kv_r(V)+v_r(q_k),
\tag{12}
\]

and hence, after the first run,

\[
 \boxed{
 v_r\!\left(U^{\ell_{k+1}}q_{k+1}-\sigma_k\right)
 =\ell_kv_r(V)
 }
 \qquad(k\ge1).
\tag{13}
\]

Equivalently, the adjacent carries satisfy the simultaneous exact cylinders

\[
 \boxed{
 q_k\equiv-\sigma_kV^{-\ell_k}pmod {U^{\ell_{k+1}}},
 }
\tag{14}
\]

\[
 \boxed{
 q_{k+1}\equiv
 \sigma_kU^{-\ell_{k+1}}pmod {V^{\ell_k}}.
 }
\tag{15}
\]

Here and below a negative exponent in a congruence denotes the inverse of a
unit modulo the displayed modulus.

There is also a carry-sensitive pointwise run bound:

\[
 \boxed{
 \ell_{k+1}
 \le \log_U\!\left(V^{\ell_k}q_k+\sigma_k\right)
 <\log_UV\,\ell_k+\log_U(q_k+1).
 }
\tag{16}
\]

The first inequality uses `q_(k+1)>=1`; the second is valid for either sign
because

\[
 0<V^{\ell_k}q_k+\sigma_k<V^{\ell_k}(q_k+1).
\tag{17}
\]

### Proof

While the emitted symbol is the fixed value `s_k`, equations (1)--(2) give

\[
 \begin{aligned}
 U(M_{n+1}-s_k)
 &=VM_n-Cs_k-Us_k\\
 &=V(M_n-s_k).
 \end{aligned}
\tag{18}
\]

Iterating through the run gives

\[
 U^{\ell_k}(M_{p_{k+1}}-s_k)
 =V^{\ell_k}(M_{p_k}-s_k).
\tag{19}
\]

At the terminal boundary, (3) and (6) imply

\[
 M_{p_{k+1}}-s_k
 \equiv s_{k+1}-s_k
 =1-2s_k=-\sigma_k\pmod U.
\tag{20}
\]

The integer on the left of (20) is odd.  Since `V` is odd, taking dyadic
valuations in (19) gives

\[
 v_2(M_{p_k}-s_k)=a\ell_k.
\tag{21}
\]

Moreover `M_(p_k)-s_k>0` because `M_(p_k)>1` and `s_k<=1`.  Therefore

\[
 q_k={M_{p_k}-s_k\over U^{\ell_k}}
\tag{22}
\]

is a positive odd integer.  Iterating (18) only through `j` steps proves (8).

At `j=ell_k`, equation (8) gives

\[
 M_{p_{k+1}}=s_k+V^{\ell_k}q_k.
\tag{23}
\]

Equation (7) at the next run gives

\[
 M_{p_{k+1}}=s_{k+1}+U^{\ell_{k+1}}q_{k+1}.
\tag{24}
\]

Subtract (24) from (23), and use
`s_k-s_(k+1)=2s_k-1=sigma_k`, to obtain (9).  Since `q_(k+1)` is odd,
taking dyadic valuations in (9) proves (10).

Reducing (9) modulo any prime factor of `V` shows that neither
`U^(ell_(k+1))` nor `q_(k+1)` is divisible by that prime.  This proves (11).
Rearranging (9) gives

\[
 U^{\ell_{k+1}}q_{k+1}-\sigma_k
 =V^{\ell_k}q_k.
\tag{25}
\]

Taking `r`-adic valuations proves (12), and (11) reduces it to (13) for
`k>=1`.  Equations (14)--(17) are immediate consequences of (9), positivity,
and the fact that `U` and `V` are coprime. **QED**

## Theorem 2 -- converse orbit reconstruction

Conversely, fix a starting symbol `s_0 in {0,1}` and any positive run lengths

\[
 \ell_0,\ell_1,\ell_2,\ldots .
\tag{26}
\]

Put `s_k=s_0` for even `k`, `s_k=1-s_0` for odd `k`, and define `sigma_k` by
(5).  Suppose positive odd integers `q_k` satisfy (9) for every `k`.

Define `p_0=0`, `p_(k+1)=p_k+ell_k`, and, for `0<=j<ell_k`, put

\[
 \boxed{
 M_{p_k+j}=s_k+U^{\ell_k-j}V^jq_k.
 }
\tag{27}
\]

Then (27) defines one infinite sequence of integers `M_n>1` satisfying
(2), and its emitted code has exactly the prescribed maximal runs.

### Proof

For `j<ell_k`, the second term in (27) is divisible by `U`, so

\[
 M_{p_k+j}\equiv s_k\pmod U.
\tag{28}
\]

Thus the emitted symbol is `s_k` throughout the proposed run.  Equation (18)
holds directly between consecutive expressions in (27), so (2) is satisfied
inside each run.

At the boundary, (9) gives

\[
 \begin{aligned}
 s_k+V^{\ell_k}q_k
 &=s_k+U^{\ell_{k+1}}q_{k+1}-\sigma_k\\
 &=s_{k+1}+U^{\ell_{k+1}}q_{k+1}.
 \end{aligned}
\tag{29}
\]

This is exactly the `j=0` expression for the next run, so the pieces join.
Equation (9) makes the terminal state in (29) congruent to `s_(k+1)` modulo
`U`, so the symbol really switches there.  Oddness of `q_k` records that the
factor `U^(ell_k)` extracted in (7) is exact, rather than hiding a longer run.

Finally, when `s_k=0`, every value in (27) is at least `U`; when `s_k=1`, it
is at least `U+1`.  Hence every state exceeds one. **QED**

## Theorem 3 -- exact nested cylinders for the initial odd carry

The zipper converts the one-root coherence problem into an explicit nested
cylinder problem for `q_0`.

For `N>=0`, define

\[
 S_0=0,
 \qquad
 S_N=\sum_{i=1}^{N}\ell_i,
\tag{30}
\]

\[
 E_0=0,
 \qquad
 E_N=\sum_{i=0}^{N-1}\ell_i
 \quad(N\ge1).
\tag{31}
\]

For `N>=1`, put

\[
 P_N=
 \sum_{j=0}^{N-1}
 \sigma_jU^{S_j}
 V^{\sum_{i=j+1}^{N-1}\ell_i},
 \qquad P_0=0,
\tag{32}
\]

where an empty exponent sum is zero.  Composing the first `N` zipper equations
gives

\[
 \boxed{
 U^{S_N}q_N=V^{E_N}q_0+P_N.
 }
\tag{33}
\]

Define `R_0=0`, viewed modulo one.  For `N>=1`, define `R_N` to be the least
representative modulo `U^(S_N)` of

\[
 \boxed{
 R_N\equiv
 -V^{-\ell_0}
 \sum_{j=0}^{N-1}
 \sigma_j(U/V)^{S_j}
 \pmod {U^{S_N}}.
 }
\tag{34}
\]

Then:

1. `R_N modulo U^(S_N)` is the unique initial-carry cylinder satisfying the
   first `N` zipper **divisibility** conditions.  It forces the input carries
   `q_0,...,q_(N-1)` to be odd, but not the terminal carry `q_N`; level `N+1`
   supplies that next parity condition.
2. The cylinders are nested:

   \[
   \boxed{R_{N+1}\equiv R_N\pmod {U^{S_N}}.}
   \tag{35}
   \]

3. They select the unique `2`-adic initial carry

   \[
   \boxed{
   q_*=-V^{-\ell_0}
   \sum_{j\ge0}\sigma_j(U/V)^{S_j}
   \in\mathbf Z_2.
   }
   \tag{36}
   \]

4. The prescribed infinite run schedule is realized by one positive ordinary
   orbit if and only if the canonical representatives `R_N` eventually
   stabilize.  In that case their stable value is the positive odd integer
   `q_0=q_*`, and the ordinary initial state is

   \[
   \boxed{M_0=s_0+U^{\ell_0}q_0.}
   \tag{37}
   \]

### Proof

Equation (33) follows by induction.  For `N=1`, it is (9) at `k=0`.  If it
holds at `N`, multiply (9) at `k=N` by `U^(S_N)` and substitute (33).  The new
terms are exactly those in (32), proving the next case.

Since `V` is a unit modulo every power of `U`, (33) gives one residue class
for `q_0` modulo `U^(S_N)`.  Multiplying (32) by `V^(-E_N)` and using

\[
 E_N=\ell_0+S_{N-1},
 \qquad
 \sum_{i=0}^{j}\ell_i=\ell_0+S_j,
\tag{38}
\]

reduces that class to exactly (34).  Reduction of (34) from level `N+1` to
level `N` removes the last term, which is divisible by `U^(S_N)`.  This proves
(35).  It also shows that membership in the level-`N` class implies every
earlier transition congruence; no intermediate integrality condition is lost
by the composed formula.  Membership at level `N+1` also forces `q_N` odd:
the next numerator `V^(ell_N)q_N+sigma_N` is divisible by the even integer
`U^(ell_(N+1))`, which is impossible if `q_N` is even.  Thus an infinite
member has every required odd carry, although one terminal parity is
deliberately absent from each finite level.

Since `ell_i>=1`, one has `S_j -> infinity`.  The series in (36) therefore
converges in `Z_2`, and its residues are precisely (34).  It is the unique
inverse-limit point of the cylinders.

Suppose first that a positive physical orbit has the prescribed runs.  Solve
(9) backwards through `N` transitions:

\[
 q_0
 =-V^{-\ell_0}
 \sum_{j=0}^{N-1}\sigma_j(U/V)^{S_j}
 +U^{S_N}V^{-E_N}q_N.
\tag{39}
\]

The last term tends to zero `2`-adically, so the ordinary positive odd carry
`q_0` equals (36).  Because it is an ordinary nonnegative integer, `L-9801`
implies that its canonical representatives `R_N` eventually stabilize at
`q_0`.

Conversely, suppose `R_N` eventually stabilizes.  By `L-9801`, (36) is the
stable ordinary nonnegative value.  Already at level one, (34) gives

\[
 q_*\equiv-\sigma_0V^{-\ell_0}pmod {U^{\ell_1}},
\tag{40}
\]

so `q_*` is odd and in particular is not zero.  Thus `q_*>0`.

Membership in every nested cylinder makes every forward quotient from (9) an
integer.  The future transition congruence (14) makes each such quotient odd.
Positivity propagates because

\[
 V^{\ell_k}q_k-1>0
 \quad\hbox{and}\quad
 V^{\ell_k}q_k+1>0
\tag{41}
\]

for `V>=3`, `ell_k>=1`, and `q_k>=1`.  Theorem 2 now reconstructs the positive
ordinary orbit (37). **QED**

## Exact next-block recurrence

The stabilization criterion is constructive.  Compatibility gives unique
mixed-radix blocks `a_N` with

\[
 \boxed{
 R_{N+1}=R_N+a_NU^{S_N},
 \qquad
 0\le a_N<U^{\ell_{N+1}}.
 }
\tag{42}
\]

To compute the next block without recomputing the longer cylinder, define

\[
 B_N={V^{E_N}R_N+P_N\over U^{S_N}}\in\mathbf Z.
\tag{43}
\]

Then

\[
 \boxed{
 a_N\equiv
 V^{-E_N}
 \left(-\sigma_NV^{-\ell_N}-B_N\right)
 \pmod {U^{\ell_{N+1}}},
 }
\tag{44}
\]

where `a_N` is the least representative in the range (42).

Indeed, replace `q_0` at level `N` by the general lift

\[
 q_0=R_N+U^{S_N}a.
\tag{45}
\]

Equation (33) becomes

\[
 q_N=B_N+V^{E_N}a.
\tag{46}
\]

The next zipper transition is integral exactly when

\[
 q_N\equiv-\sigma_NV^{-\ell_N}pmod {U^{\ell_{N+1}}}.
\tag{47}
\]

Substitution of (46) in (47) proves (44).  Combining (42) with `L-9801`
gives the exact eventual-zero formulation:

\[
 \boxed{
 \text{positive ordinary realization}
 \quad\Longleftrightarrow\quad
 a_N=0\text{ for all sufficiently large }N.
 }
\tag{48}
\]

Thus the full finite run language and the one-root infinite language are
separated by one explicit sequence of carry blocks, rather than by an
unspecified compactness or completion step.

## Exact `4 -> 5` specialization

For the physical chart of PR #35 and `T-9822`, take

\[
 (U,V,C,a)=(4,5,1,2).
\tag{49}
\]

Every maximal phase run has

\[
 M_{p_k}=s_k+4^{\ell_k}q_k,
 \qquad q_k\text{ positive and odd},
\tag{50}
\]

and adjacent runs satisfy

\[
 \boxed{
 4^{\ell_{k+1}}q_{k+1}
 =5^{\ell_k}q_k+\sigma_k.
 }
\tag{51}
\]

Therefore

\[
 \boxed{
 v_2(5^{\ell_k}q_k+\sigma_k)=2\ell_{k+1},
 }
\tag{52}
\]

\[
 \boxed{
 v_5(4^{\ell_{k+1}}q_{k+1}-\sigma_k)=\ell_k
 }
 \qquad(k\ge1),
\tag{53}
\]

and

\[
 q_{k+1}\equiv
 \sigma_k4^{-\ell_{k+1}}pmod {5^{\ell_k}}.
\tag{54}
\]

The initial odd-carry completion is the alternating sparse series

\[
 \boxed{
 q_*=-5^{-\ell_0}
 \sum_{j\ge0}\sigma_j(4/5)^{S_j},
 \qquad \sigma_j=(-1)^j\sigma_0.
 }
\tag{55}
\]

For a positive chart survivor, `M_0=A_0+2`, so its ordinary root is recovered
from a stabilizing run cylinder by

\[
 \boxed{A_0=s_0+4^{\ell_0}q_*-2.}
\tag{56}
\]

Equations (51)--(55) expose the state absent from a phase-only connector:
one positive odd carry must satisfy alternating exact `2`-adic and `5`-adic
cylinders at every run boundary.

## Dependency and novelty audit

- Local `T-9823` supplies (1)--(3), proves that both symbols occur infinitely,
  and gives exact same-symbol and consecutive-switch valuations in the
  original state coordinate.  It does not extract maximal-run odd carries,
  derive the adjacent-run zipper (9), reconstruct an orbit from that zipper,
  or compute the nested `q_0` blocks (42)--(44).
- Local `L-9801` is used only after compatibility (35) has been proved.  It
  turns the explicit canonical cylinders into the exact ordinary
  stabilization criterion (48).
- Local `T-9819` gives support-density bounds for bounded-digit completion
  series.  Equation (36) is a new run-coordinate completion with alternating
  signs, but no density conclusion from `T-9819` is needed here.
- At source head `6bb647ad13507d8b478ae990d3e1d1b95aea1f17`, PR #35 `D-8801` defines
  the binary completion, `T-8802` supplies the physical `4 -> 5` recurrence,
  `T-8805` explicitly leaves quotient/carry memory open, `T-8806` gives the
  bottom-tree equivalence, and `T-8807` counts completion cylinders.  None of
  those source claims contains the maximal-run quotient or the two-place
  zipper.  The PR #35 dependency is already mediated through local `T-9823`.
- Live `PR35/T-8809` now independently reconstructs two-color multiplicative
  syndeticity and explicitly credits local `T-9819` for the first support-gap
  bound.  Its symbol-support floors agree with `T-9822`; it does not extract
  maximal-run carries, couple dyadic and odd-place precision, or give the
  stabilization blocks (42)--(48).
- Live `PR35/L-8804`, `T-8808`, and `O-8802` at
  `8060aa4d3155d526ab4f6405ef9ecb47fa8107e1` work in the word/root coordinate
  `X=M-1`: finite cylinders compose exactly, the depth-50 least survivor is
  certified, and global existence is equivalent to bounded/eventually stable
  least roots.  Under `delta=1-epsilon` and
  `M_0=s_0+4^(ell_0)q_0`, these statements are compatible with the run-carry
  cylinders here.  They do not derive (9)--(15) or the explicit blocks
  (42)--(44); `O-8802`'s global criterion and (48)'s schedulewise criterion
  agree at the existence level.
- Issue #31 asks for an exact one-counter residue block and an eventual-zero
  dichotomy.  Equations (42)--(48) provide that interface for every binary
  expanding-chart run schedule.  They do not transfer to the different
  256-transition cap system without a separate crosswalk.
- No external theorem, finite experiment, real equidistribution statement, or
  unreviewed numerical observation is used.

## Adversarial and gap audit

- **First-carry exception at odd primes.**  The initial `q_0` may share a prime
  factor with `V`.  Therefore (12), not the simplified (13), is the correct
  formula at `k=0`.  Equation (11) justifies (13) only from `k=1` onward.
- **Divisibility is weaker than a maximal run.**  If one checks only that the
  right side of (9) is divisible by `U^(ell_(k+1))`, the quotient might be
  even and the proposed next run might be nonmaximal.  The infinite zipper
  requires every `q_k` to be odd; equivalently, the following transition
  supplies the next exact terminal congruence.
- **Finite schedules remain abundant.**  A finite list of run lengths fixes
  the integrality cylinder (34).  Requiring the terminal `q_N` to be odd
  refines it to one class modulo `2U^(S_N)`; sufficiently large lifts in that
  class make the finite states positive.  The theorem does not turn finite
  compatibility into an infinite ordinary orbit.  The missing condition is
  precisely eventual vanishing of the blocks `a_N`.
- **Terminal parity is not hidden in one finite cylinder.**  For
  `U=4,V=5,ell_0=ell_1=1,sigma_0=-1`, level one is `q_0=1 mod4`.
  The lift `q_0=1` gives odd `q_1=1`, whereas `q_0=5` gives even `q_1=6`.
  Level two excludes the latter.  This is why Theorem 3 states divisibility
  compatibility at level `N` and obtains every odd carry only in the inverse
  limit.
- **The first-run modulus is not duplicated.**  The cylinder modulus in (34)
  is `U^(S_N)` with `S_N=ell_1+...+ell_N`, because `q_0` is defined only after
  the initial factor `U^(ell_0)` has been extracted from `M_0-s_0`.
- **Signs are fixed.**  A zero-run has `sigma=-1` and transports
  `V^ell*q-1`; a one-run has `sigma=1` and transports `V^ell*q+1`.  Reversing
  this convention breaks both the boundary identity and (55).
- **Composite `V` is allowed.**  Equation (13) is asserted prime by prime for
  every divisor of `V`; primality of `V` is nowhere assumed.
- **The trivial fixed completion is excluded.**  The hypothesis `M_n>1`
  excludes `M_n=1`, `epsilon_n=1` forever.  It also lets `T-9823` prove both
  symbols infinite before maximal runs are enumerated.
- **No cross-completion identification is made.**  The series (36) is used
  only in `Z_2`.  Even when its displayed terms also converge in the real
  absolute value, that real limit is not identified with `q_*`.
- **Stabilization is a criterion, not a conclusion.**  Nothing here proves
  that every run cylinder has infinitely many nonzero blocks, nor constructs
  one with an eventually zero tail.  Thus no positive `4/5` survivor is
  constructed or excluded.

## Suggested next attack

Use the exact two-place zipper rather than the phase word alone.  A negative
route can prove that the block formula (44) is nonzero infinitely often, or
show that no positive odd chain can satisfy both (10) and (13) at every scale.
A constructive route must give a finite rule for `(ell_k,q_k)` satisfying
(51), prove eventual zero blocks in (42), and recover one explicit positive
root from (56).  Either route now carries the one-root quotient memory that
the full finite phase language of `T-9822`--`T-9823` necessarily loses.
