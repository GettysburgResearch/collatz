# Ordinary two-arm sections: exact least-failure guards and an all-horizon obstruction

**Status: PROPOSED.** The algebraic statements and all-horizon family below have written elementary proofs and an exact standard-library replay. They do not prove Collatz. In particular, no all-source termination theorem for the guarded process is asserted.

We use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

For positive integers, write `f(x)=f(y)` when their forward orbits meet at possibly different clocks. This is an equivalence relation. Put

\[
P(n): f(n)=f(3n),\qquad
Q(a): f(a)=f(3a-1)=f(2a-1).
\]

The last two values have the same component because `T(2a−1)=3a−1`.

## Source boundary and objective

The comparison target `P` and the smaller-comparison program are inherited from **PR146**, frozen at
`7d04c4dd756cfe495eb3eee78eba35a99085cd2a`, specifically
`research/upper-bit-mergers/THREE_RAY.md` and `THREE_RAY_SMALLER.md`.
That head already proves that all parameters `n≡7 (mod 8)` reduce to smaller tripling comparisons, that a nonempty finite set of odd tripling failures is impossible, and a stronger quantitative failure lower bound. Those are source results, not discoveries of this note. In particular the older finite-defect obstruction at head `561d48a4d3a793a59b1cdf0406062ae1a6d47515` is superseded.

The present attempt asks whether actual, variable-duration ordinary two-arm motion supplies a complete least-counterexample descent. It supplies an exact guard interface, two additional smaller-tripling implications, and a family escaping every fixed clock budget. It does not repeat the local-cylinder grading result of PR150 (`ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`).

All logical claims below are proved directly; no external density or conjectural equidistribution input is used. The finite replay is evidence for the implementation, not a substitute for these proofs.

## QG1. The least failure and its physical orientation

If Collatz fails, let `m` be the least positive nonconvergent integer. Then

\[
m=2a-1,\qquad a\ge2\text{ is even}.
\]

Every positive integer below `m` reaches 1. Thus `a` is in the component of 1, while `3a−1=T(m)` is not. Moreover `a` is exactly the least parameter for which `Q(a)` fails.

**Proof.** A least nonconverger is odd. An odd `m>1` congruent to 1 modulo 4 has `T²(m)=(3m+1)/4<m`, so `m≡3 (mod 4)` and `a=(m+1)/2` is even. For `b<a`, both `b` and `2b−1` are below `m`, so `Q(b)` holds. At `a`, the left source converges and the right source does not. Conversely, if all `Q(a)` hold, strong induction proves convergence: an even number halves, and an odd number `2a−1>1` has the same component as the smaller number `a`. This also identifies the least two failures. ∎

Fix this hypothetical `a` and retain it throughout the process. At synchronous clock `h`, define the **physical** arms

\[
X_h=T^h(a),\qquad Y_h=T^h(3a-1).
\]

`X` always belongs to the convergent component; `Y` always belongs to the nonconvergent component. The following guards contradict the assumed least failure:

1. Some physical `Y_h<m`, or more generally `oddpart(Y_h)<m`.
2. A meeting `X_i=Y_j` at any finite independent clocks.
3. A numerical section `Y_h=3X_h−1` with `X_h<a`. Its positive odd preimage `2X_h−1<m` belongs to the bad component.
4. A numerical reversed section `X_h=3Y_h−1` with `oddpart(Y_h)<m`. Here the section parameter itself is in the bad component; this guard is already contained in guard 1.

The source `a`, its floor `m`, and which physical arm is bad never change. Resetting a canonical coordinate does not reset this floor or license a new favorable lift.

## QG2. An exact synchronized affine transducer

Represent the current physical pair, possibly with its order exchanged, as

\[
(B,3^sB+D),\qquad s\ge0,\quad D\in\mathbb Z.
\]

An orientation bit `ε` records whether `B=X` (`ε=0`) or `B=Y` (`ε=1`). Initially `(s,D,ε)=(1,−1,0)` and `B=a`. Let `b=B mod 2`.

| State condition | `b` | New `(s,D)` | New base | Orientation |
|---|---:|---|---|---|
| `D` even | 0 | `(s,D/2)` | `B/2` | unchanged |
| `D` even | 1 | `(s,(3D+1−3^s)/2)` | `(3B+1)/2` | unchanged |
| `D` odd, `s>0` | 0 | `(s+1,(3D+1)/2)` | `B/2` | unchanged |
| `D` odd, `s>0` | 1 | `(s−1,(D−3^(s−1))/2)` | `(3B+1)/2` | unchanged |
| `D` odd, `s=0` | 0 | `(1,(3D+1)/2)` | `B/2` | unchanged |
| `D` odd, `s=0` | 1 | `(1,(1−3D)/2)` | `(B+D)/2` | exchanged |

**Proof.** Apply the actual map to each physical arm. If `D` is even, the two parities agree. If `D` is odd, they differ. The final row is the only one in which the arm with the smaller power-of-three slope changes, so the new canonical base is the old other arm after its even step. Each displayed numerator has the indicated integrality. This proves the invariant inductively, without assigning random fresh bits. ∎

A canonical return is `(s,D)=(1,−1)`. It preserves `Q`, possibly exchanging its two component labels. At such a return with base `b`, the correct least-failure thresholds are:

- unchanged orientation: `b<a` is a contradiction;
- exchanged orientation: `oddpart(b)<2a−1` is a contradiction.

A canonical state describes an affine identity on a binary class. A numerical specialization can meet or become a section even when that affine identity does not hold on the whole class. Therefore the physical guards in QG1 must be checked as well as canonical returns.

### Exact return constants

For a word `w` of length `h` with `q_w` odd inputs, use the standard affine numerator

\[
T_w(x)=\frac{3^{q_w}x+C_w}{2^h},\qquad C_w\ge0.
\]

Let `w,v` be the actual words on the original physical `X,Y` arms. An unchanged canonical return requires

\[
q_w=q_v=q,\qquad C_v-3C_w=3^q-2^h.
\]

An exchanged canonical return requires

\[
q_w=q_v+2,\qquad 3C_v-C_w=3^{q_v+1}+2^h.
\]

These follow by comparing both coefficients and constants in `Y_h=3X_h−1` or `X_h=3Y_h−1`, using initial `Y_0=3a−1`.

Every nonempty return has a base map

\[
b=\frac{3^q a+C}{2^h},\qquad C>0.
\]

In the unchanged case `C=C_w`. Equality `C_w=0` would mean both physical words have no odd inputs, impossible since the initial arm parities differ. In the exchanged case `C=C_v−3^{q_v}` and the return equation gives `3C=C_w+2^h>0`.

Consequently an expanding return has a negative real affine fixed point. This excludes a positive ordinary fixed point for that one affine map; it does not exclude an arbitrary sequence of different return words.

## QG3. Concrete return identities and smaller comparisons

The following are exact canonical return words; the digits are successive canonical-base parities, not necessarily the parity word of one fixed physical arm after an exchange.

| Word | Source class for `a` | Returned base | Orientation |
|---|---|---|---|
| `10` | `a≡1 (mod 4)` | `(3a+1)/4` | unchanged |
| `010` | `a≡2 (mod 8)` | `(3a+2)/8` | unchanged |
| `01100` | `a≡6 (mod 32)` | `(9a+10)/32` | unchanged |
| `001100` | `a≡12 (mod 64)` | `(9a+20)/64` | unchanged |
| `110001` | `a≡11 (mod 64)` | `(9a+29)/64` | exchanged |

They are obtained by applying QG2, or by literal affine replay of both ordinary arms. For odd `n`, the first step on each arm of `(n,3n)` gives the Q pair with `a=(3n+1)/2`. The third and fourth rows therefore imply, for every integer `u≥0`,

\[
\boxed{P(25+64u)\iff P(7+18u)},
\qquad
\boxed{P(93+128u)\iff P(13+18u)}.
\]

Both right parameters are strictly smaller. Thus a least tripling failure cannot lie in either of these two classes. They add the explicit subprogressions `25 (mod 64)` and `93 (mod 128)`, contained respectively in `1 (mod 8)` and `5 (mod 8)`, to the explicit smaller-comparison theorem at the frozen PR146 head; they do not cover every member of either modulo-8 class or all remaining classes.

### Why the physical orientation matters

The first return word `01111011011101110` has

\[
a=121310+131072u,
\qquad b=163957+177147u,
\qquad u\ge0,
\]

with exchanged orientation. Here `b>a`, so the raw Q parameter increases, but

\[
(2a-1)-b=78662+84997u>0.
\]

It is therefore a valid least-nonconverger descent: the bad arm itself has fallen below the original floor. This expanding scalar example is **not** a counterexample to the orientation-aware guard.

Appending `10` and restricting to `a=121310+1048576u` produces the even-to-even increasing scalar return

\[
b=122968+1062882u>a.
\]

It is handled by the same physical guard. No failure of the stronger guard follows from the expansion of this coordinate.

### An isolated physical meeting missed by the affine state

For `a=4`, the pair `(4,11)` reaches `(1,1)` at clock 10. Its canonical state there is `(s,D)=(1,−2)`, not `(0,0)`, and it has never returned to `(1,−1)` after time zero. Thereafter its canonical states alternate `(1,−4)` and `(1,−2)` while the physical arms run on `2,1`. Testing only symbolic absorption or canonical section return would miss this convergent positive source.

## QG4. An exact family avoiding every fixed clock budget

**Theorem.** Let `H≥3`, `t≥1`, and set

\[
N=2^H t,\qquad a=N-2,\qquad m=2a-1=2N-5.
\]

The actual positive arms `X_j=T^j(a)` and `Y_j=T^j(3a−1)` satisfy all of the following through clock `H`. Here “bad arm” means the designated `Y` arm of the candidate least-failure test; it does not assert that any constructed ordinary source is nonconvergent:

1. Every bad arm value is strictly above the original floor: `Y_j>m` for `0≤j≤H`.
2. There is no independent-clock meeting `X_i=Y_j` for `0≤i,j≤H`.
3. There is no numerical simultaneous Q section in either orientation at `1≤j≤H`.
4. The canonical state neither returns to `(1,−1)` after time zero nor reaches `(0,0)`.

If, in addition, `t` is odd for `H≡1 (mod 3)` and even for `H≡0,2 (mod 3)`, then `Y_H` is odd, and

\[
\operatorname{oddpart}(Y_j)>m\qquad(0\le j\le H).
\]

Thus even the immediate halving guard cannot escape the clock budget unnoticed at its endpoint. The theorem concerns the stated guards; it does not exclude arbitrary longer inverse searches or every possible component certificate.

### Literal formulas and parity legality

For `1≤i≤H`,

\[
X_i=3^{i-1}2^{H-i}t-1.
\]

For every indicated index at most `H`,

\[
\begin{aligned}
Y_{3r}&=3^{2r+1}2^{H-3r}t-7,\\
Y_{3r+1}&=3^{2r+2}2^{H-3r-1}t-10,\\
Y_{3r+2}&=3^{2r+2}2^{H-3r-2}t-5.
\end{aligned}
\]

The formulas follow by induction with the actual parities. For `i<H`, the `X_i` after time zero are odd. For `j<H`, the bad-arm parities are `odd, even, odd` as `j` runs through `0,1,2 (mod 3)`. The factors `2^(H−i)` and `2^(H−j)` are present until the final output, so no parity assumption is imposed beyond clock `H`.

The bad-arm coefficients relative to `N` are respectively

\[
3(9/8)^r,\quad (9/2)(9/8)^r,\quad (9/4)(9/8)^r.
\]

Subtracting `m=2N−5` gives lower bounds `N−2`, `(5/2)N−5`, and `N/4`, respectively. All are positive. This proves assertion 1.

The additional parity choice makes `Y_H` odd directly in the formulas. Every earlier even bad arm occurs at `j≡1 (mod 3)` and has the next output odd, unless that next output is the endpoint, which has just been made odd. Thus its odd part is a bad-arm value already checked in assertion 1.

### No independent-clock meeting

First `X_i<m` for `i=0,1,2,3`, because `N≥8`. These values cannot equal any `Y_j`.

Suppose `i≥4` and write `X_i=P_i−1`, `Y_j=R_j−c_j`, where `P_i=3^(i−1)2^(H−i)t` and `c_j` is `7,10,5` in the three residue classes. Equality would imply

\[
P_i-R_j=1-c_j\in\{-6,-9,-4\}.
\]

For `j≥2`, this is impossible by divisibility by 3. Specifically, for `j≡2`, both terms are divisible by 9 but the right side is `−4`; for `j≡0` with `j≥3`, both are divisible by 27 but the right side is `−6`; for `j≡1` with `j≥4`, both are divisible by 27 but the right side is `−9`.

For the remaining clocks, equality reduces to

\[
2^{H-i}t(3^{i-2}-2^i)=-2\quad(j=0),
\]

or

\[
2^{H-i}t(3^{i-3}-2^{i-1})=-1\quad(j=1).
\]

In the first equation the bracket is `−7,−5` at `i=4,5` and positive for every `i≥6`. In the second it is `−5,−7,−5` at `i=4,5,6` and positive for every `i≥7`. Neither equation is possible. This proves assertion 2.

### No specialized simultaneous section

For `j≥2`, the equation `Y_j=3X_j−1` would require

\[
R_j-3P_j=c_j-4\in\{3,6,1\},
\]

but the left side is divisible by 9. At `j=1`, the equation forces `N=2`, contrary to `N≥8`.

For `j≥3`, the equation `X_j=3Y_j−1` would require

\[
P_j-3R_j=-3c_j,
\]

whose left side is divisible by 9 while its right side has ternary valuation exactly 1. At `j=1` and `j=2`, the equations are `13N=30` and `2N=5`. These are impossible. This proves assertion 3 and distinguishes actual specializations from affine-state identities.

### Canonical state and the signed boundary

Every source `a=2^H t−2` agrees with the signed source `−2` modulo `2^H`, so the two physical parity words and the canonical state agree through clock `H`. The signed physical pair starts at `(-2,-7)`. Its first arm reaches the fixed point `−1`; its other arm follows

\[
-7\longmapsto-10\longmapsto-5\longmapsto-7.
\]

The canonical states through clock 7 are

| Clock | `(s,D)` | Orientation |
|---:|---|---|
| 0 | `(1,−1)` | unchanged |
| 1 | `(2,−1)` | unchanged |
| 2 | `(1,−2)` | unchanged |
| 3 | `(1,−4)` | unchanged |
| 4 | `(1,−7)` | unchanged |
| 5 | `(0,−4)` | unchanged |
| 6 | `(0,−6)` | unchanged |
| 7 | `(0,−9)` | unchanged |

At clocks `8+3r,9+3r,10+3r`, the orientation is exchanged, `s=r+1`, and

\[
D=5\cdot3^{r+1}-1,\quad7\cdot3^{r+1}-1,\quad10\cdot3^{r+1}-1,
\]

respectively. These are positive. The exact infinite canonical parity code is

\[
0\,1^7(110)^\infty.
\]

This proves assertion 4. It also identifies the ordinary-realization boundary: an integer satisfying `a≡−2 (mod 2^H)` for every `H` is exactly `a=−2`. The positive least representatives `2^H−2` escape to infinity. Positive ordinary witnesses at every finite depth do not produce one positive all-time source.

## The remaining global step

The finite-horizon family rules out a uniform synchronized clock bound for this whole guard interface, including independent-clock meetings within the horizon and numerical simultaneous sections. It does **not** rule out an unbounded terminating program, a well-founded rank, or a stronger ordinary merger mechanism.

The exact first-return algebra has not been turned into a theorem that every return surviving all earlier physical guards must reduce the least failure. Nor has section avoidance been excluded for one fixed positive ordinary source. The all-horizon family isolates one signed residual code; excluding this code alone does not control arbitrary positive sources that depart from it and later follow other branches.

The first unsupported global inference would be: **every fixed positive even source eventually triggers one of these guards**. No argument in this packet establishes that inference. Consequently there is no complete Collatz proof here.

## Replay scope

`check_q_section_guards.py` replays the exact return words, the scalar-expansion control with its correct physical descent, the isolated positive meeting, the signed state formulas, and the all-horizon identities on a deterministic range. It tests all independent-clock meetings using exact set intersection. It also checks the extra endpoint parity restriction and rejects corrupted affine-return artifacts. It contains no assertions whose removal changes its verification behavior.

The unbounded theorem rests on the displayed proofs, not the finite range in the report.
