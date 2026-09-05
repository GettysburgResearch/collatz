# Route 2 — use the first crossing's forced continuation

**Status:** **PROPOSED pending independent review**. Elementary proofs supplied.
The all-word exclusion and SC* remain **OPEN**. This does not establish FC*.

## 1. Why look beyond the crossing?

The older coefficient program attempts to exclude non-descent exactly when the
multiplicative coefficient first falls below one. For a least counterexample,
that is stronger than necessary: a forced descent immediately *after* that
crossing is just as contradictory. The useful data is the ordinary displacement
between the starting state and the crossing endpoint.

We use the exact parity difference isometry, already part of the repository's
finite-cylinder toolkit, and apply it to this ordinary return displacement.
The new output is a valuation-stratified displacement sieve retaining the same
source, word, and complete denominator. It is not an independent-factor sieve.

## 2. T-A3-201 — first-disagreement return echo

Let n,d be positive integers, t=v_2(d), and

\[
x_i=T^i(n),\qquad
C_i=3^{q_i}/2^i,\qquad x_i=C_i n+E_i,
\quad E_i=A_i/2^i.
\]

The trajectories from n and n+d have identical parity through positions
0,...,t-1, and opposite parity at position t. Moreover,

\[
T^i(n+d)=x_i+C_i d\quad(0\le i\le t).                 \tag{1}
\]

If x_t is odd, the next iterate of the shifted source is

\[
T^{t+1}(n+d)=\frac{x_t+C_t d}{2}.
\]

Therefore it lies strictly below n exactly when

\[
\boxed{(2-C_t)n>C_t d+E_t,\qquad x_t\text{ odd}.}      \tag{2}
\]

If x_t is even, the next shifted iterate is instead
(3(x_t+C_t d)+1)/2.

### Proof

As long as the parities agree, a difference is multiplied by either 1/2 or 3/2.
Its 2-adic valuation drops by exactly one at each such step, regardless of the
odd multiplier. Starting at valuation t, the difference is even until time t,
when it becomes odd. This proves both the exact first-disagreement time and
(1), by induction. At time t, odd x_t means that the shifted state is even;
apply its even branch. Rearrangement gives (2). The other parity case follows
by the odd branch. QED.

The same algebra is valid for positive rationals with odd denominator, using
parity in Z_2. Such rationals are useful formal test objects, but are not
ordinary Collatz counterexamples.

## 3. L-A3-202 — a source-free shifted displacement threshold

Suppose w is a first coefficient-crossing word of length j and odd count q>=1.
Set

\[
P=2^j,\quad Q=3^q,\quad D=P-Q>0,
\qquad T^j(r)=r+d,
\qquad A=Dr+Pd.
\]

Every proper coefficient prefix is at least one. If the odd positions are e_i,
numbered with i=1,...,q, then

\[
E_j=\frac AP=\frac QP\sum_{i=1}^q\frac{2^{e_i}}{3^i}
\le\frac QP\frac q3<\frac q3.                         \tag{3}
\]

Here 2^(e_i)<=3^(i-1) follows from supercriticality before that odd step.
The case q=0 is the one-step even descent and cannot be an obstruction.

For a non-descending positive realization,

\[
0\le d<A/P<q/3.                                      \tag{4}
\]

For d>0, put t=v_2(d). Then t<j. Let

\[
P_t=2^t,\quad Q_t=3^{q_t},\quad E_t=A_t/P_t,
\quad v_t\in\{0,1\}
\]

be the prefix data before bit t. If v_t=1 and Q_t<2P_t, define

\[
B_t=(2P_t-Q_t)A-DA_t,\qquad
C_t^{\rm den}=2P_tP-QQ_t>0.
\]

A necessary condition for the crossing's forced continuation not to descend
below r at its first disagreement is

\[
\boxed{C_t^{\rm den}d\ge B_t.}                        \tag{5}
\]

Thus the allowed integer displacement stratum is narrowed to

\[
\{d:\ v_2(d)=t,\quad 0<d<A/P,\quad
 d\ge\lceil B_t/C_t^{\rm den}\rceil\}.                 \tag{6}
\]

If the lower endpoint exceeds that stratum's upper endpoint, the entire
valuation class is excluded. Negative lower endpoints are harmless.

### Proof

Substitute r=(A-Pd)/D into (2), multiply by P_t D, and collect d:

\[
(2P_t-Q_t)(A-Pd)>D(Q_t d+A_t)
\iff
(2P_t-Q_t)A-DA_t>(2P_tP-QQ_t)d.
\]

Since Q<P and Q_t<2P_t, the denominator in (5) is positive. The strict
inequality is exactly the certificate of later descent; its complement is
(5). For the first-crossing context, v_t=0 cannot produce a descent at this
first disagreement because C_t>=1 and E_t>=0. The v_t=1, C_t>=2 sector also
cannot satisfy (2). QED.

### Complete denominator retained

For each word, the remaining candidates must still obey

\[
D\mid A-Pd,
\qquad r=(A-Pd)/D\in\mathbb N_{>0},                    \tag{7}
\]

as well as every proper-prefix and least-source condition. Formula (5) is an
additional exact ordinary inequality on that **same d**, not a substitute for
(7). Endpoint (A-Qd)/D and source (A-Pd)/D are not interchanged.

### A uniform near-return corollary

If n>1 is a least positive counterexample, then n=3 modulo 4. An even n already
descends, and an odd n=1 modulo 4 satisfies T^2(n)=(3n+1)/4<n.

For an endpoint n+d of such an orbit:

* odd d<n is impossible, since (n+d)/2<n;
* d=2 modulo 4 with 3d+1<n is impossible, by t=1 in (2).

Consequently a first crossing with n>q+1 must have

\[
\boxed{d\equiv0\pmod4.}                              \tag{8}
\]

Indeed d<q/3 makes both sufficient inequalities hold. The d=0 cycle case is
retained. This corollary is conditional on the displayed size comparison;
no claim is made that n>q+1 holds for every later crossing.

## 4. T-A3-203 — a weaker end-to-end exclusion objective

Call an ordinary first-crossing pair (r,w,d) **echo-safe** when d>=0 and either

a) d=0; or
b) d>0 and the test (2), at t=v_2(d), does not certify a descent.

The word must be physically realized from the same positive integer r; r=1
with the trivial crossing word 10 is excluded from the target.

Assume:

1. SC*: every positive integer has a finite first coefficient crossing;
2. no echo-safe ordinary first-crossing tuple with source r>1 survives all
   necessary least-counterexample conditions (including no iterate below r).

Then Collatz holds.

### Proof

Take a least positive counterexample n. Every iterate is at least n: any smaller
one would converge by minimality. By SC*, it has a finite first coefficient
crossing. Negative displacement is already a contradiction. Positive
non-echo-safe displacement forces descent within t+1 further steps, also a
contradiction. Hence its tuple is echo-safe, contrary to hypothesis 2. The case
d=0 is retained in the echo-safe target and is not assumed away. QED.

The elementary proof does not depend on the repository's still-proposed
cross-PR SC*/FC* synthesis. Hypothesis 2 has not been established. The gain is
that one need no longer insist on descent at the crossing itself: the forced
continuation is part of the arithmetic obstruction.

## 5. Exact experiment and its limited scope

The independent checker tests the first-disagreement identity on 32,768 ordinary
pairs 1<=n<=256, 1<=d<=128. The odd-first-disagreement criterion certifies descent
in 11,495 cases. These are test inputs, not claimed counterexample-orbit returns.

The separate symbolic compiler enumerates every first-crossing word through
length 21. There are 12,449 words. For each word it enumerates every positive
integer d<A/P and forms the **rational** source (A-Pd)/D. This produces 9,779
formal positive-displacement pairs. Formula (5), or equivalently the exact
rational continuation, rejects 6,431 of them. None of the 9,779 sources is an
integer. These counts therefore measure a structural prefilter, not new
ordinary counterexample exclusions beyond an integer census.

One exact example is

\[
w=11011010,\quad (P,Q,D,A)=(256,243,13,319),
\quad d=1,\quad r=63/13.
\]

The crossing endpoint is 76/13. Its parity is even in Z_2, and the next step is
38/13<63/13. This is a positive rational illustration of the sieve, **not** a
positive integer counterexample or its refutation.

The verifier enumerates words by combinations of odd positions rather than the
generator's prefix tree, and uses actual rational parity iteration rather than
the generator's affine test. It never imports the generator.

## 6. Next obstruction

The residual tuples have d=0 or a positive displacement whose valuation falls
in an echo-safe stratum. Large coefficient bank at the disagreement can pay for
the extra even step, so the present argument does not exclude every stratum.
SC* is also still open. The next mathematical target is to combine the common-d
sieve with support-loss and complete-denominator constraints, rather than merely
increase the finite word depth or count proper-factor hits.
