# Critical inverse poles in every finite arithmetic neighborhood

**PROPOSED, self-contained arithmetic obstruction.** This note constructs
positive noninteger rational Collatz cycles. It constructs no nontrivial
positive integer cycle and no divergent positive integer orbit. Its narrow
addition to existing rational shadow arguments is the simultaneous control
of binary and ternary precision at a supplied root, an arbitrary real lower
floor, and positive critical inverse score. No broad priority claim is made.

## 1. Map and an integer critical score

Put
\[
 I_a(x)=(2^a x-1)/3,\qquad f_a(y)=(3y+1)/2^a,\qquad
 X=\mathbb Z_3^\times.
\]
A legal inverse word keeps all its states in X. On positive odd rationals
with denominator coprime to six, the forward map uses the exact valuation
a=v_2(3y+1), as on positive odd integers. Define
\[
 W(x)=\sup_w\{8|w|-5A(w)\},\qquad E=\{W=+\infty\},
\]
including the empty word. The slope 8/5 exceeds log_2 3 since 3^5<2^8.

For w=(a_1,...,a_d), A_i=sum_{j<=i}a_j, A=A_d, write
\[
 F_w(y)=f_{a_1}\circ\cdots\circ f_{a_d}(y)
       ={3^d y+C_w\over2^A},\qquad
 C_w=\sum_{i=1}^d3^{i-1}2^{A-A_i}.                         \tag{1}
\]
This map returns the terminal inverse state to its original root.

## 2. A dense null exceptional set

**Proposition 1.** E is a dense G-delta subset of X and has normalized unit
Haar measure zero. For every integer B>=1,
\[
 h\{W\ge B\}\le(5/6)^B.                                  \tag{2}
\]

Set lambda=6/5 and assign each letter a the subprobability weight
\[
 q_a={1\over3}\lambda^{8-5a},\qquad
 \sum_{a\ge1}q_a={6^8\over3\,5^3(6^5-5^5)}
 ={1679616\over1744125}<1.
\]
Words first crossing score B at their last letter are prefix-free, so their
product weights sum to at most one. Adjoining a cemetery letter reduces
this statement to the usual probability version. The legal domain of a
d-letter word is exactly F_w(X). Every forward affine branch maps X into X,
and F_w scales additive Haar measure by 3^{-d}. Its normalized unit Haar
mass is therefore exactly 3^{-d}. Its product weight is
3^{-d}lambda^{8d-5A}, at least 3^{-d}lambda^B. Summing these original-root
domains proves (2), without independence of their overlapping cylinders.

Each fixed finite word has a clopen legal domain. A length-truncated
potential is measurable on a finite ternary quotient; the untruncated
event {W>=B} is only asserted to be open. Thus W is lower semicontinuous
and E is G-delta. The point -1 has legal inverse letter
1 forever, gaining score 3 per step. Every F_w(-1) belongs to E as well.
For any x in X and q, choose a legal q-letter word w at x, with terminal x_q.
Then
\[
 x-F_w(-1)=3^q2^{-A(w)}(x_q+1)\in3^q\mathbb Z_3 .
\]
This proves density. No digit is lost: F_w(-1) has an explicitly legal
inverse path returning to -1. Generic word-legality tests require q+1
digits, whereas this approximation assertion only claims q digits.

Every finite-depth cylinder therefore meets E. A finite union of cylinders
covering E must be all of X. No ordinary integer has positive ternary
distance from E. The countable variable-depth stopping covers in (2) do
not provide finite clopen covers of comparably small mass.

## 3. Positive noninteger rational cycles at a supplied integer

**Theorem 2.** Fix a positive odd integer n with 3 not dividing n, integers
j,q>=0, and a real floor H>0. There is a positive rational periodic orbit
with root r such that:

1. r-n belongs to both 2^j Z_2 and 3^q Z_3.
2. Every cycle state is greater than H in the real ordering.
3. Every state has the same reduced denominator D_red>1, coprime to six.
4. Every state is a unit in both Z_2 and Z_3, and every prescribed forward
   gap is its exact 2-adic valuation.
5. The mean gap is less than 8/5, so W is infinite at every cycle state.

The maximum permitted gap can be fixed after n,j,q are fixed and before H
is chosen.

### Fix both finite observations

Choose q legal inverse letters e_1,...,e_q at n, all at most four, keeping
positive ordinary unit states. Two letters of the required parity occur
among 1,...,4. If the smaller gives a parent divisible by three, the
two-larger alternative gives four times that parent plus one.

Let h_1,...,h_L be an actual forward valuation prefix of n, long enough
that h_1+...+h_L+1>=j. An empty prefix suffices when j<=1. Reserve the
inverse cycle word in the form
\[
 w=(e_1,...,e_q,\ \text{filler},\ h_L,...,h_1).             \tag{3}
\]
Let s=q+L and S be the total of these reserved letters. Put
B=max(2,e_1,...,e_q,h_1,...,h_L), ignoring empty lists.

### Choose the total cost and fill the middle

Upper continued-fraction convergents to log_2 3 supply arbitrarily large
integer pairs (d,A) with 0<A-d log_2 3 tending to zero. Then
J=3^d/2^A tends to one from below, and A/d tends to log_2 3<8/5.
For sufficiently large such pairs,
\[
 d-s<A-S<2(d-s),\quad 5A<8d,\quad
 {2^{-B}\over1-J}>H,\quad 2^A-3^d>1.                     \tag{4}
\]
The last condition is elementary: for A>=3 a positive difference
2^A-3^d cannot equal one, since 3^d is either one or three modulo eight.
Fill the middle d-s places with ones and twos totaling A-S. Strictness
supplies at least one of each; reserve adjacent positions containing (1,2).

Since J<1, each cyclic rotation has a positive rational fixed point. At the
chosen root it is
\[
 r={C_w\over D},\qquad D=2^A-3^d>0.                      \tag{5}
\]
C_w is odd and not divisible by three; D is coprime to six. The same holds
at every rotation. Thus all states are positive 2-adic and 3-adic units.
The branch identities give exact valuations because both rational
endpoints are odd 2-adic integers.

Each rotation's offset in (1) is at least 2^{-B}, from its first term.
Every fixed-point value is consequently at least 2^{-B}/(1-J)>H.
The mean gap is A/d<8/5. Repeating the inverse cycle accumulates the
positive score 8d-5A, proving W=+infinity at every state.

### Force a nontrivial denominator without factoring

Compare the interior pair (1,2) with its adjacent swap (2,1). Since
\[
 f_1\circ f_2(y)-f_2\circ f_1(y)=1/4,
\]
if the prefix preceding the pair has length l and total T, the two full
numerators differ by
\[
 C_0-C_1=3^l2^{A-T-2}.                                  \tag{6}
\]
This is coprime to D. As D>1, the two numerators cannot both be divisible
by D. Choose a version for which D does not divide C_w. Its reduced
denominator exceeds one. The relations
\[
 3N_{i+1}=2^{a_i}N_i-D
\]
preserve gcd(N_i,D), so all states have this same reduced denominator.
No factorization and no assumption excluding integer cycles are used.

### Verify both prescribed agreements

For the inverse prefix e in (3),
\[
 r-n=3^q2^{-A(e)}(r_q-n_q)\in3^q\mathbb Z_3.
\]
The reversed final block in (3) makes the first L forward gaps at r equal
to h_1,...,h_L. Therefore
\[
 3^L(r-n)=2^{h_1+\cdots+h_L}(r_L-U^L(n)).
\]
Both endpoint states are odd 2-adic integers, so the parenthesized
difference belongs to 2 Z_2. This gives binary precision at least
h_1+...+h_L+1>=j. The interior swap preserves both agreements.

## 4. Large finite scores on immediate ordinary convergers

This control separates a large certified finite-word lower bound on W
from nonconvergence. It does not establish that W(n_q) itself is finite.
For any q>=1 take the explicit positive odd integer
\[
 n_q=(2^{3^{q+1}+1}-1)/3.
\]
The elementary lifting identity
v_3(2^{3^{q+1}}+1)=q+2 gives v_3(n_q+1)=q+1 exactly. In particular
U(n_q)=1 and n_q=-1 mod 3^{q+1}. Its first q inverse letters can all be one, with every
terminal state a unit:
\[
 I_1^i(n_q)=2^i(n_q+1)/3^i-1\equiv-1\pmod3,\quad 0\le i\le q.
\]
Hence W(n_q)>=3q, though the actual forward odd map reaches one in a single
step. The extra ternary digit is necessary to guarantee the unit condition
at the last inverse state. This does not refute a logarithmic upper bound
W(n)<=5 log_2 n+C: these witnesses become very large.

## 5. Scope and the remaining arithmetic step

Theorem 2 prevents exclusion based only on fixed binary and ternary
neighborhoods, a fixed positive real floor, legal branches and infinite W.
Every such collection of conditions has a positive noninteger rational
periodic model. It does not refute a criterion using the **global**
denominator-one condition, increasing precision along one fixed ordinary
trajectory, or a proved ordinary pointwise bound on W.

Positive predecessor density concerns populations of starts. Singular
ternary empirical laws concern time averages on one supplied trajectory.
The cited density theorems do not provide an exchange of these limits or a
growing-precision estimate. PR145's compact null terminal-residue support
is a set in the real correction coordinate, distinct from E.

In particular a global ordinary estimate W(n)<=5 log_2 n+C is a sufficient
hypothesis with additional uniform cost content; equivalence to Collatz
alone is not established here. Even W(1)<infinity would uniformly bound
8q-5A over all terminating inverse histories of one, an additional
worst-case stopping-cost statement not supplied by termination alone.
The subsequent [closure boundary note](CLOSURE_BOUNDARY.md) identifies
the global closing estimates exactly with the conjunction of Collatz
and W(1)<infinity; it does not deduce the latter assertion from Collatz.

## 6. Exact provenance and verification boundary

Inspected PR145 head: dd245a712f985909f541590e3f6c179b7ba011e4.

- research/unrestricted-cycle-denominator/NEAR_FULL_GCD.md already gives
  high-minimum positive rational cycles near critical real lap multiplier
  with substantially stronger denominator-cancellation estimates.
- research/critical-orbit-mellin/ORDINARY_PHASE_AVOIDANCE.md gives high-trace
  ordinary finite paths, including prescribed subsequent destinations,
  while distinguishing them from one infinite forward orbit.
- research/terminal-residue/SUPPORT.md gives the source-qualified null
  support result in the real terminal-correction coordinate.

Inspected PR147-branch head: b74b2d466f58844a742a6ed6bcdf06844269f361.
Its research/astra-three-routes/pass3/JOINT_ARITHMETIC_RANKS.md uses negative
rational periodic pins and positive ordinary finite shadows to obstruct
finite arithmetic feature ranks.

The new claim here is the particular simultaneous binary/ternary local
density extension, positive integer critical score, and elementary
nonintegrality choice. The exact standard-library replay is
check_rational_density.py. It validates finite arithmetic interfaces; the
arbitrary-precision and arbitrary-floor theorem rests on the proof above.

The replay passed nine rational-cycle cases, comprising 1,405 inverse edges,
plus seven immediate-converger controls. It checks exact rational branch
valuations, binary/ternary congruences, positive floors, the preserved
nontrivial denominator, and positive integer score per cycle. The highest
tested binary precision was ten and the highest ternary precision was nine;
the largest tested real floor was 25.
