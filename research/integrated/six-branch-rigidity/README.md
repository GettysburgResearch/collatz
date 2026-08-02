# IC-RIG-001 — finite tame rigidity in the reviewed six-branch chart

## Status

- **Mathematical status:** `VERIFIED` with namespace and dependency fixes.
- **Repository role:** accepted integrated reference after merged PR #84.
- **Proof residency:** local proof packet.
- **Artifact status:** small exact tables were checked; the all-depth conclusions are symbolic.
- **Open boundary:** the least legal roots are not known to stabilize or escape.
- **Collatz status:** this is a method-class obstruction inside one strict subsystem, not a proof of Collatz.

## The chart

Put

\[
P=3^{12}=531441,
\qquad
Q=2^{19}=524288,
\qquad P>Q,
\]

and

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

The stationary chart is

\[
F(x)=\left\lceil\frac{Px}{Q}\right\rceil,
\qquad
\delta(x)=QF(x)-Px.
\]

A root is legal while every canonical digit `δ(F^n(x))` lies in `A`.

For each current type `i`, the source/output table supplies residues `r_i,c_i` satisfying

\[
Qc_i=Pr_i+a_i,
\qquad a_i\in\mathcal A.
\]

Every ordered type pair `i→j` has positive ordinary realizations. Writing

\[
x=r_i+Qk,
\qquad
F(x)=c_i+Pk=r_j+Qk',
\]

gives the exact high-quotient transition

\[
\boxed{Qk'=Pk+c_i-r_j.}
\]

The integrated packet establishes four related boundaries:

1. the ordinary high quotient immediately leaves the six-digit language;
2. finite affine complete-tree self-sections collapse to the forward map;
3. finite rational-function complete-tree self-sections also collapse to the forward map;
4. the all-depth survivor contains no infinite arithmetic progression or semilinear forward-invariant sanctuary.

## Lemma A — direct high-quotient exit

For a two-step legal root of type `i→j`, the canonical first digit of the high quotient `k` is

\[
b_{ij}=[c_i-r_j]_Q.
\]

The complete matrix is

\[
\begin{pmatrix}
4024&491448&384440&1912&292464&357191\\
41391&4527&421807&39279&329831&394558\\
149859&112995&5987&147747&438299&503026\\
6165&493589&386581&4053&294605&359332\\
235937&199073&92065&233825&89&64816\\
177480&140616&33608&175368&465920&6359
\end{pmatrix}.
\]

No entry lies in `A`. Therefore

\[
x\in S_2
\quad\Longrightarrow\quad
\left\lfloor\frac{x}{Q}\right\rfloor\notin S_1.
\]

### Proof

The quotient recurrence follows by subtracting `r_j` from `c_i+Pk`. The canonical first digit of `k` is `[-Pk]_Q=[c_i-r_j]_Q`.

For a compact exact check, reduce modulo `2048`. The allowed digits reduce to

\[
\{0,1536,960,824,1695\},
\]

while the quotient matrix reduces to

\[
\begin{pmatrix}
1976&1976&1464&1912&1648&839\\
431&431&1967&367&103&1342\\
355&355&1891&291&27&1266\\
21&21&1557&2005&1741&932\\
417&417&1953&353&89&1328\\
1352&1352&840&1288&1024&215
\end{pmatrix}.
\]

These sets are disjoint. Disjointness modulo `2048` implies disjointness modulo `Q=2^19`. ∎

This closes the most direct recursive idea—strip one base-`Q` block and reuse the high quotient—but does not prove the original roots escape.

## Lemma B — the digit alphabet has trivial affine automorphism group

Suppose residues `w,t mod Q` satisfy

\[
t+w\mathcal A=\mathcal A\pmod Q.
\]

Then

\[
w=1,
\qquad t=0\pmod Q.
\]

### Proof

The alphabet contains exactly one odd element,

\[
a_5=413343,
\]

and five even elements. If `w` were even, all images would have the same parity. Hence `w` is odd.

If `t` were odd, the five even inputs would map to odd outputs and the one odd input to an even output, giving five odd images rather than one. Thus `t` is even, and the unique odd input maps to the unique odd output:

\[
t+wa_5\equiv a_5\pmod Q.
\]

Let `S=\sum_{a\in\mathcal A}a`. Summing the affine permutation gives

\[
6t+wS\equiv S\pmod Q.
\]

Using `t=(1-w)a_5`,

\[
(1-w)(6a_5-S)\equiv0\pmod Q.
\]

Directly,

\[
6a_5-S=594979,
\]

which is odd. Since `Q` is a power of two, `w≡1 mod Q`, and then `t≡0 mod Q`. ∎

## Theorem C — finite affine nuclei collapse

Let `Ω` be a finite control set. Suppose each reachable state `(ω,i)` carries an integer-affine coordinate

\[
y=v_\omega k+s_{\omega,i},
\qquad v_\omega>0,
\]

has all six children, and the transformed coordinates reproduce the same six-branch law on every exact edge, with successor control and initially allowed label permutations.

Then every reachable section is

\[
\boxed{y=Pk+c_i,}
\]

the original forward image. No finite affine nucleus yields a contracting, bounded, seed-preserving, or least-root-descending complete-tree self-section.

### Proof

On an edge `(ω,i)→(ω',j)`, compare the coefficient of the free integer `k` in the transformed recurrence. This gives

\[
v_{\omega'}=v_\omega.
\]

Thus one positive integer scale `v` occurs on a reachable component.

For a fixed parent state, reduction modulo `Q` makes the six transformed digits an affine image of `A` with multiplier

\[
w=vP^{-1}\pmod Q.
\]

Lemma B forces `v≡P mod Q` and fixes the physical labels. Write

\[
v=P+mQ.
\]

Define normalized carries

\[
h_{\omega,i}=s_{\omega,i}-c_i-mr_i.
\]

The exact edge equations simplify to

\[
Qh_{\omega',j}=Ph_{\omega,i}-ma_i.
\]

The right side is independent of the child type. Let `H` be the finite nonempty set of normalized carries occurring after a transition. Every value appears with all six current types, so

\[
T_i(H)\subseteq H,
\qquad
T_i(h)=\frac{Ph-ma_i}{Q}.
\]

Let `h_-` and `h_+` be the minimum and maximum of `H`.

If `m>0`, the maximum inequality gives

\[
h_+\le\frac{ma_{\min}}{P-Q},
\]

while the minimum inequality gives

\[
h_-\ge\frac{ma_{\max}}{P-Q}.
\]

Since `a_max>a_min`, this forces `h_->h_+`, impossible.

If `m<0`, write `m=-n` with `n>0`. The same extremal argument gives

\[
h_+\le-\frac{na_{\max}}{P-Q},
\qquad
h_-\ge-\frac{na_{\min}}{P-Q},
\]

again impossible.

Thus `m=0`. Then every carry maps by multiplication with `P/Q>1`. A positive maximum would map to a larger value, and a negative minimum to a smaller value. Hence `H={0}`. Therefore

\[
v=P,
\qquad s_{\omega,i}=c_i.
\]

The only finite affine nucleus is the forward map. ∎

## Theorem D — finite rational nuclei also collapse

Suppose each reachable finite-control section carries a nonconstant rational function

\[
f_{\omega,i}(X)\in\mathbf Q(X),
\]

which is a positive ordinary integer for every sufficiently large integer input and reproduces the complete six-branch law on every exact child progression. Then

\[
\boxed{f_{\omega,i}(X)=PX+c_i}
\]

at every reachable state, with physical labels fixed.

### Proof

#### Tail-integral rational functions are polynomials

Write `f=A/B` with coprime `A,B∈Z[X]`. Bézout gives polynomials `U,V∈Z[X]` and nonzero integer `R` such that

\[
UA+VB=R.
\]

For every sufficiently large integer `n`, integrality of `A(n)/B(n)` gives `B(n)\mid A(n)`, and hence `B(n)\mid R`. A nonconstant `B` has unbounded absolute value on the positive integers, impossible. Therefore `B` is constant and `f` is a polynomial over `Q`.

#### Finite polynomial control forces degree one

Every exact child tail has a parametrization

\[
k=\kappa_{ij}+Qt,
\qquad
k'=\lambda_{ij}+Pt.
\]

Because the transformed recurrence holds for infinitely many integers `t`, it is a polynomial identity. Degrees are equal along every edge. If the common degree is `d` and the leading coefficients are `L_{\omega,i}`, comparison gives

\[
L_{\omega',j}=L_{\omega,i}\left(\frac QP\right)^{d-1}.
\]

A path in finite control eventually reaches a directed cycle. Multiplying around a cycle of length `s` gives

\[
L=L\left(\frac QP\right)^{s(d-1)}.
\]

Since `L≠0` and `P≠Q`, one must have `d=1`.

Thus every section is affine. Tail integrality makes its coefficients integers, eventual positivity makes the common slope positive, and Theorem C forces

\[
f_{\omega,i}(X)=PX+c_i.
\]

∎

## Theorem E — no semilinear sanctuary

Let `S_∞` be the positive ordinary integers whose canonical digits remain forever in `A`. Then:

1. `S_∞` contains no infinite arithmetic progression;
2. `S_∞` contains no infinite semilinear subset;
3. no nonempty semilinear `X⊆S_∞` satisfies `F(X)⊆X`.

More quantitatively, if

\[
R+MZ_{\ge0}\subseteq S_n
\]

and `v=ν_2(M)`, then

\[
2^{19n-\min(v,19n)}\le6^n.
\]

### Proof

Every length-`n` word over the six digits selects one residue class modulo

\[
Q^n=2^{19n}.
\]

Hence `S_n` occupies at most `6^n` residue classes modulo `Q^n`.

An arithmetic progression with step `M` occupies exactly

\[
\frac{Q^n}{\gcd(M,Q^n)}
=2^{19n-\min(v,19n)}
\]

classes modulo `Q^n`. If the entire progression lies in `S_n`, these classes must be among the legal classes, proving the inequality.

For fixed `M`, once `19n>v`, this becomes

\[
\left(\frac{2^{19}}6\right)^n\le2^v,
\]

which fails for all sufficiently large `n`. Thus no infinite arithmetic progression lies in `S_∞`.

Every infinite semilinear subset of the positive integers contains an infinite arithmetic progression, so `S_∞` has no infinite semilinear subset.

Finally,

\[
F(x)=\left\lceil\frac{Px}{Q}\right\rceil>x
\]

for every positive `x` because `P>Q`. A nonempty forward-invariant set contains an infinite strictly increasing orbit. A semilinear forward-invariant subset of `S_∞` would therefore be infinite, contradiction. ∎

## Scientific meaning

The packet rules out an entire family of proposed extraction certificates:

```text
complete six-branch tree
+ finite control
+ affine or rational exact sections
+ eventual ordinary integrality
```

and separately rules out Presburger/ultimately periodic value-space sanctuaries.

This is an all-depth theorem, not a report that several guessed controllers failed. It also shows why another finite tame recoding of the full tree is unlikely to cross the ordinary-extraction boundary.

## Boundaries and common misreadings

- None of these theorems proves `S_∞` empty.
- The least legal root sequence remains undecided.
- A single survivor may lie in a proper, genuinely nonlinear, infinite-state sublanguage.
- Algebraic functions beyond the reviewed rational class are not included here; PR #65’s extension requires its own reviewed import.
- Automatic sets need not be semilinear.
- Absence of arithmetic progressions, zero density, or high symbolic complexity does not imply emptiness.
- The physical Collatz seed crosswalk is branch-qualified and is not part of this integrated packet.
- The direct quotient exit is not a proof of general quotient-tree exit.

## Provenance

Primary source: PR #64 at

```text
88884c3e590b08aeb2018872987e71e14de1fe7b
```

Source files:

```text
research/six-branch-extraction/claims/D-7401-six-branch-minimal-word-system.md
research/six-branch-extraction/claims/L-7401-high-quotient-section.md
research/six-branch-extraction/claims/T-7401-affine-section-rigidity.md
research/six-branch-extraction/claims/T-7402-finite-affine-nucleus-rigidity.md
research/six-branch-extraction/claims/T-7403-finite-rational-nucleus-rigidity.md
research/six-branch-extraction/claims/T-7404-no-semilinear-sanctuary.md
```

Source author: `gpt56-extraction-01`.

Independent review:

```text
reports/gpt56-cartographer-01/2026-08-01-pre-public-review-pr64-pr65-pr66.md
@ 591a06ad914b63dddfd65ee658dbec36291ffbc0
```

Verdict: `VERIFIED WITH FIXES`, including namespace and dependency corrections. Small exact tables were checked; no expensive computation carries the theorem.

The integrated ID `IC-RIG-001` avoids collisions with unrelated branch-local claims named `T-7401`. Source IDs are not renamed.

## Next missing step

Decide the same initial-root sequence:

\[
\sup_N m_N<\infty
\quad\text{or}\quad
m_N\to\infty.
\]

A positive route must introduce genuinely unbounded nonlinear arithmetic information tied to one fixed root. A negative route should prove direct ordinary height or digit escape.
