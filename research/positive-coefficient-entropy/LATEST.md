# Latest state — support-corrected coefficient closure

**Snapshot:** 2026-08-01  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Draft PR:** #81  
**Status:** draft mathematical research

All theorem-level statements remain **PROPOSED** pending independent
reconstruction. Claims using the quoted Rhin normalization or PR #34's
full-order theorem are explicitly source-qualified.

**No proof of Collatz is claimed.**

## 1. Exactly two global targets

For a parity word `w` of length `j` and weight `q`, let

\[
2^j s_w=3^q r_w+A_w
\]

be its canonical source--endpoint pair.  When `2^j>3^q`,

\[
r_w>{A_w\over2^j-3^q}
\iff
s_w-r_w<0.
\]

The exhaustive obligations are:

### SC*

\[
\boxed{
m_N^{\rm sup}
=
\min_{w\in\mathcal W_N^{\rm sup}}r_w
\longrightarrow\infty.}
\]

### FC*

Apart from the trivial word `10`, no complete first-crossing tuple has
canonical displacement

\[
d=s_w-r_w\ge0.
\]

`L-6814` proves that every nontrivial positive cycle generates a canonical
first-crossing failure. Hence FC* already contains cycle exclusion and

\[
\boxed{\mathrm{SC}^*+\mathrm{FC}^*\Longrightarrow\text{Collatz}.}
\]

## 2. Coordinate-safe near-return equation

For a canonical near-return

\[
T^j(r)=s=r+d,
\qquad
D=2^j-3^q,
\]

`L-6812` proves

\[
\boxed{
A_w=Dr+2^jd=Ds+3^qd,}
\]

with

\[
\boxed{0\le d<A_w/2^j<q/3<j/3.}
\]

Thus

```text
source   = (A_w-2^j d)/D;
endpoint = (A_w-3^q d)/D.
```

The complete prime-power congruence may use `A_w == 3^q d`, but the source
quotient must retain `2^j d`.

## 3. What is already closed in FC

Subject to the declared source inputs:

```text
upper-mechanical canonical word:
  descends at every nontrivial length;

no-wrap nonmechanical word:
  is easier to descend than the mechanical word;

bounded-bank / low-complexity families:
  are eventually excluded;

sub-sqrt(j)-support repair families:
  are excluded;

one-pulse near-return families over the known negative baselines:
  are excluded within PR #83's stated scope.
```

The complete exceptional family is polynomially sparse across words at each
length, while every unbounded acyclic member is internally rough:

\[
R_j
\ge
\sqrt{{\log2\over2\log3}j}-O(\log j).
\]

It also has `Omega(j^(2/3))` integrated displacement and leaves both the
mechanical prefix and its own post-return tail within logarithmic depth.

## 4. New theorem — uniform support loss

Let

\[
C_j={3^q\over2^j}
\]

and let `R(v)` be the number of odd positions displaced from the
upper-mechanical word.  `L-6816` proves

\[
\boxed{
E_{\rm mech}-E_v
>{C_j\over12}R(v)
>{R(v)\over24}.}
\]

For a canonical non-descent this becomes the direct source inequality

\[
\boxed{
 r_v
 <
 F_j-{C_jR(v)\over12(1-C_j)},}
\qquad
F_j={A_{\rm mech}(j)\over2^j-3^q}.
\]

Every distinct displaced odd position therefore subtracts a fixed amount
from the same mechanical envelope that the source must approach.

## 5. Exact return-forced support threshold

Define

\[
L_j(R)=\left\lfloor{j-2\over2(R+1)}\right\rfloor
\]

and let `rho_j` be the least nonnegative integer `R` such that either
`L_j(R)=0` or

\[
2^{L_j(R)}+1
<
3^{R+1}
\left({q\over3\lambda_j}+{q\over3}\right),
\qquad
\lambda_j=j\log2-q\log3.
\]

`T-6812` proves, using `L-6811/L-6815`, that every internally injective
nonmechanical canonical failure satisfies

\[
R(v)\ge rho_j.
\]

This definition is source-free and exact.  A candidate-specific directed
lower bound for `lambda_j` evaluates it without importing a generic exponent.

## 6. Strictly weaker cofinal envelope

Put

\[
\boxed{
H_j^{\rm supp}
=
F_j-{C_jrho_j\over12(1-C_j)}.}
\]

Every internally injective nonmechanical failure has source below
`H_j^supp`.  Failures containing repeated proper states reduce to a
least-period positive cycle, whose minimum rotation and first crossing are
internally injective.  Thus, after the finite initial audit and the
source-qualified mechanical theorem, the cofinal inequality

\[
\boxed{m_{j-1}^{\rm sup}\ge H_j^{\rm supp}}
\]

closes FC*.

The corrected envelope remains unbounded along lower convergents, because

\[
F_j>{C_jq\over6(1-C_j)},
\qquad
rho_j\le\lfloor(j-2)/2\rfloor.
\]

Hence the same cofinal inequality forces SC*.

The fully explicit scalar form is

\[
\boxed{
 m_{j-1}^{\rm sup}
 \ge
 {q/3-C_jrho_j/12\over1-C_j}.}
\]

This is strictly weaker than the previous scalar target

\[
{q\over3(1-C_j)}.
\]

Neither corrected inequality is proved cofinally.

## 7. Updated SC* equivalence

The updated base branch now contains `T-6710`:

\[
\boxed{
m_N>B
\iff
\tau_c(n)\le N
\text{ for every }1\le n\le B.}
\]

Thus SC* is exactly universal finite coefficient stopping. In fixed-source
form, source `n` realizes an all-supercritical word `w` of length `N` only if

\[
v_2(3^{q(w)}n+A_w)\ge N.
\]

`L-6711` controls endpoint accumulation for one fixed source but does not move
that source.

For the corrected envelope define

\[
B_j^{\rm supp}=\lceil H_j^{\rm supp}\rceil-1.
\]

The smallest exact moving source box is now

\[
\boxed{
\tau_c(n)\le j-1
\quad
(1\le n\le B_j^{\rm supp})}
\]

cofinally at the valid first-crossing lengths.

## 8. Complete denominator remains mandatory

Factor

\[
D=2^j-3^q=\prod_sQ_s,
\qquad
h_s=\operatorname{ord}_{Q_s}(2).
\]

`L-6809` remains the lossless compiler.  One exact first-crossing
non-descent requires:

```text
compatible local excess paths modulo every h_s;
the unique monotone ordinary lift in the full-order window;
every proper first-crossing coefficient inequality;
one common 0<=d<q/3;
every complete prime-power equation A == 3^q d;
the canonical source (A-2^j d)/D.
```

An order-cover may decode a word but does not certify omitted prime powers.
A proper-factor hit is not a near-return.

## 9. Exact current blocker

The program has not proved SC*, FC*, the original cofinal envelope, or the
support-corrected envelope.

The smallest exact forms now are:

```text
cofinal source inequality:
  m_(j-1)^sup >= H_j^supp;

moving stopping box:
  tau_c(n)<=j-1 for every n<=ceil(H_j^supp)-1;

fixed-source valuation:
  v_2(3^q n+A_w)<|w| beyond a source-dependent finite depth;

complete-denominator exclusion:
  no complete first-crossing tuple with one 0<=d<q/3.
```

Another endpoint-growth theorem, family count, proper-factor sieve, or free
completion does not close these objects.

## 10. Review order

1. `CURRENT_STATE.md`
2. `claims/L-6816-uniform-support-remainder-loss.md`
3. `claims/T-6812-support-corrected-cofinal-envelope.md`
4. `claims/L-6812-bilateral-shifted-near-return.md`
5. `claims/L-6814-positive-cycles-absorb-into-first-crossing.md`
6. `claims/L-6813-sharpened-box-coupling-envelope.md`
7. `claims/T-6806-upper-mechanical-all-length-closure.md`
8. `experiments/X-6801-mechanical-cst/`
9. `claims/L-6811-support-sensitive-factor-complexity.md`
10. `claims/T-6810-square-root-displaced-support.md`
11. `claims/L-6809-near-cycle-prime-power-compiler.md`
12. `Q-6802-canonical-displacement-closure.md`
13. latest session report
