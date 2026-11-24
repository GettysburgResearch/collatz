# Joint renewal: first mergers of three arms and actual landing weights

**Collatz remains OPEN.** This checkpoint continues the Aaronson–Yolcu–Heule head-comparison route. Its strongest written result is a first-merger moment theorem for three fixed affine arms: every moment strictly below three halves is finite. It removes the entire contribution from three or more surviving symbolic classes from the native-head summability problem. Exactly two classes can still carry different basin colors.

**Evidence status:** the probabilistic and analytic theorems are **PROPOSED written proofs**, independently reconstructed by the other research streams and the coordinator. They use the named, **SOURCE-QUALIFIED** physical-clock estimate below. The finite Lean statements have separate kernel evidence. No universal convergence theorem, formalization of all probability estimates, or literature-priority claim is made. [Source pins](SOURCES.json) · [Verification and independent reviews](../../../reports/ayh-resource-reset-20261124/joint-renewal/README.md).

## 1. First fusion of three fixed ordinary affine arms

Use the shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Fix three forms \(3^{a_i}n+c_i\), with \(a_i\ge0\), \(c_i\in\mathbb Z\), and restrict ordinary sources to values where the forms are positive. On a binary cylinder, each current arm is an affine function of the still-unexposed integer quotient. A *symbolic fusion* means equality of two whole affine functions. It certifies an actual equal-clock meeting for every positive ordinary lift of that cylinder.

Let \(\sigma\) be the first such fusion of any pair under the fair binary-prefix law. The strongest result is

\[
\boxed{\quad \mathbb E(1+\sigma)^p<\infty
\quad\text{and}\quad
\Pr(\sigma>t)=o(t^{-p})
\qquad(0<p<3/2).\quad}
\]

For every interval of \(N\) admissible ordinary parameters, this gives

\[
\#\{n:\text{three profiles remain distinct at }\lfloor\log_2N\rfloor\}
=o\!\left(\frac{N}{(\log N)^p}\right),
\]

uniformly in the interval's location. A finite union over triples gives the same bound for **at least three** surviving classes in any fixed finite affine family. The constants can depend on that family and on \(p\). There is no uniform assertion for a family whose size or initial forms grow with \(N\).

Taking, for example, \(p=4/3\) makes the normalized errors summable over the actual head scales \(R_j=81^j\). This is stronger than a vanishing three-class error, and stronger than the harmonic bound \(O(1/t)\) alone. The endpoint \(p=3/2\) and the two-class tail are not settled.

### The mechanism

All three arms use the **same** next free binary digit. Sort their affine grades \(a_i+p_i(t)\), with adjacent gaps \(u,v\) and spread \(U=u+v\). Between ties, the product \(uv\) loses one unit in conditional expectation exactly when the middle arm alone has a different parity. The pair Green estimate bounds the total cost of resolving ties. This first proves a reciprocal-clock tail and summable middle-isolation occupation.

The stronger argument uses

\[
F_\gamma(u,v)=uv(u+v)^\gamma,\qquad0<\gamma<1.
\]

The uniform mixed-clock estimate in equation (21) of the cited synchronization paper gives the three pairwise mixed-step frequencies on sufficiently long physical blocks, uniformly in the actual offsets. Its covariance matrix for the two gaps is

\[
\Sigma=\begin{pmatrix}1/2&-1/4\\-1/4&1/2\end{pmatrix}.
\]

The exact second-order contraction is

\[
\tfrac12\Sigma:D^2F_\gamma
=\frac{\gamma-1}{4}
\left(U^\gamma+\gamma uvU^{\gamma-2}\right)<0.
\]

On separated blocks the Taylor error is absorbed into this drift. Blocks near a tie are paid for using the **actual killed occupation**, rather than a new distribution of the stopped values. Their total cost is summable for \(\gamma<1\). Finite telescoping yields \(\sum_t\mathbb E[U_t^\gamma;\sigma>t]<\infty\). A final small-spread split charges a controlled fraction to an earlier dyadic shell and gives the moment \(p=1+\gamma/2\). Every absorption occurs in finite partial sums before a limit is taken.

[Strongest proof](TRIPLE_SUBCRITICAL_MOMENTS.md) · [Pair-to-triple bootstrap and finite-mean proof](TRIPLE_FIRST_FUSION.md) · [Actual second derivatives and negative curvature in Lean](SubcriticalCurvature.lean) · [One-step Lean identities](TripleGradeProduct.lean) · [Physical-window Lean bounds](MiddleIsolationWindow.lean).

## 2. A summable part of the original weighted landing problem

For an actual head child \(x=81m+r\in[7R_j,8R_j)\), put

\[
h_j=\lfloor\log_2(R_j/81)\rfloor,
\qquad S_j=|4+p_x(h_j)-p_m(h_j)|.
\]

If \(N_j\) counts children still missing symbolic merger at \(h_j\) with \(S_j\le k_{h_j}\), then

\[
\sum_{j:H\le h_j<2H}\frac{N_j}{R_j}
\ll (1+k_{2H})^2H^{-1/2}.
\]

For nondecreasing \(k_h\), the finite-certificate series converges exactly when
\(\sum_h(1+k_h)^2h^{-3/2}<\infty\). In particular \(k_h=h^\beta\), \(\beta<1/4\), gives a summable contribution to the **actual color-discordance weights**. The converse concerns missing this finite certificate; it is not a lower bound on permanent nonmergers or on different basin colors.

The proof conditions the Green occupation bound at a deterministic clock while retaining the killed normalized-offset moment. Complete binary blocks then give upper and lower comparisons with the original integer intervals. [Proof and sharp scope](KILLED_GRADE_OCCUPATION.md) · [Finite Green identity in Lean](KilledGradeGreen.lean).

## 3. A quantitative bound on actual first-entrance weights

Write \(d=\log_2R\), \(M=d^D\), with \(D\) sufficiently large for a requested exception exponent \(A>1\). Both actual arms first enter \([M/2,M)\) by \(O(d)\), outside \(O_A(Rd^{-A})\) original children. Let \(W_j(v,w)\) retain the ordered first-entrance pair and its original multiplicity.

On one common typical source set, among children missing a specified finite merger certificate, the mass at **each prescribed landing height on either arm** is

\[
O_A\!\left(\frac{R(\log d)^{3/2}}{M}\right).
\]

Consequently, if every pair in a set \(E\) has its first endpoint in \(P\) or its second endpoint in \(Q\), then

\[
\frac1R\sum_{(v,w)\in E}W_j(v,w)\mathbf1_{f(v)\ne f(w)}
\ll_A d^{-A}+
\frac{(\log d)^{3/2}}M(|P|+|Q|),
\]

where \(f\) is the basin-of-one indicator. Fractional vertex covers are also allowed. The exception is paid once, independently of the chosen endpoint test.

For fixed entrance time and height, the original sources lie in one short interval, with only one possible odd count on the narrow source annulus. Applying the original head-pair merger estimate **inside that source interval** supplies the extra saving. No uniform landing law or independence of the arms is assumed. The time window and the sharper correction use the original-source first-passage method, with Shaik's prior scalar results explicitly credited.

Typical pairs additionally lie in \(O(\sqrt{d\log d})\) disjoint arithmetic slope strips. A two-logarithm bound separates the zero strip, where \(|v-w|=O(\log d)\), from the other strips, where \(|v-w|\gg M(d\log d)^{-\nu/2}\). The intervening region has only summable exceptional source mass. These support constraints do not determine the colors within a strip.

[Proof](LANDING_WEIGHT_TRANSFER.md) · [Odd-count uniqueness and endpoint-only cardinality in Lean](EndpointFibers.lean).

## 4. Joint stopped-clock residues, with the actual roots retained

For the pair \((81n+r,n)\), choose arbitrary entrance sets below \(Y\). Retain the exact two entrance values, hit/miss pattern and the two signed differences of physical and odd-count clocks. On the hit part, one common pair of clock residues modulo \(m\) becomes approximately uniform independently of that retained data, in total variation.

For parameters in \([X,X+L)\), let \(w=L/X\). If \(2^h\le L\), \(2^hY<X\), and \(Q\) is a convergent denominator of \(\log_3 2\), the error is

\[
O\!\left(\min\{1,mQ/\sqrt h+m/(wQ)\}\right).
\]

The bound is uniform in the entrance sets and number of retained bins. A selection of original mass \(\delta\) inherits the absolute error divided by \(\delta\). This qualification matters: the discordant population may already be smaller than the unconditioned error.

The fixed-modulus result for weighted clocks in PR193 is prior work. This result supplies a quantitative growing-modulus comparison retaining **both actual roots and both integer clock gaps**. It also identifies a summable low-grade portion of the rare-selection transport error. [Proof and rare-selection scope](JOINT_ENTRANCE_GRADES.md) · [First-entrance transfer and finite averaging](EntranceGrades.lean) · [Exact restrictions on affine matching](AffineGradeRigidity.lean).

## 5. Why the two-class case is the remaining global problem

The exact cylinder

\[
n=32q+23,\quad r=73,
\qquad T^5n=27q+20=:z,
\qquad T^5(81n+73)=9z+2
\]

shows a genuine two-class contribution. After tripling the parent parameter with digit two, both new arms reach the old upper endpoint at clock five. Doubling with digit one does the same at clock six. Yet \(\gg R/\sqrt{\log R}\) original children in every sufficiently large head row still miss the original finite symbolic certificate at its natural deadline.

Thus even the new summable three-class theorem cannot justify multiplying two failure probabilities in this quartet. The cylinder does **not** prove different eventual colors; its two residual arms may merge later. [Written scope](QUARTET_COLLAPSE.md) · [All-parameter ordinary identities in Lean](QuartetCollapse.lean).

The closing estimate remains

\[
\sum_j\frac1{81^j}\sum_{v,w}W_j(v,w)
\mathbf1_{f(v)\ne f(w)}<\infty.
\]

The previous [head rigidity argument](../continuation/HEAD_EDGE_RIGIDITY.md) and [source-qualified positive-density closure](../literature-step/MACROSCOPIC_PAIR_CLOSURE.md) explain why this would settle Collatz. This checkpoint supplies summable three-class and low-grade errors, and actual-weight estimates for small endpoint covers. It does not prove summability of the remaining two-class weighted color failures.

## Replay

Use Lean 4.34.1 and Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`:

```sh
lake env bash /path/to/joint-renewal/check_lean.sh
python -X utf8 -B /path/to/joint-renewal/check_entrance_grades.py
```

The build uses fresh temporary outputs, rebuilds the local import closure, treats warnings as errors and queries the named public declarations for transitive axioms. The probability theorems, including the moment theorem, have the written scope stated above. The bounded replay checks exact ordinary entrance transfers; it is not an asymptotic test.
