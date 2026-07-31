# Current state — support-corrected coefficient frontier

**Snapshot:** 2026-08-01  
**Active branch:** `agent/gpt56-positive-entropy-01/75-supercritical-entropy`  
**Draft PR:** #81  
**Cross-branch inputs:** PR #83; updated PR #77 base (`T-6710/L-6711`)  
**Status:** draft mathematical research

All theorem-level statements remain **PROPOSED** pending independent
reconstruction.  The all-length upper-mechanical theorem imports the quoted
Rhin normalization, and the complete prime-power compiler imports PR #34's
full-order theorem.

**No proof of Collatz is claimed.**

## 1. Corrected exhaustive target

For a parity word `w` of length `j` and weight `q`, let

\[
2^j s_w=3^q r_w+A_w
\]

be the canonical source--endpoint pair.  For a subcritical word,

\[
r_w>{A_w\over2^j-3^q}
\iff
s_w-r_w<0.
\]

The two exhaustive obligations are:

```text
SC*:
  m_N^sup=min_{w in W_N^sup} r_w -> infinity;

FC*:
  apart from the trivial word 10, no complete first-crossing tuple has
  canonical displacement d=s_w-r_w>=0.
```

`L-6814` absorbs every nontrivial positive cycle into FC*.  Thus

\[
\boxed{\mathrm{SC}^*+\mathrm{FC}^*\Longrightarrow\text{Collatz}.}
\]

There is no separate cycle premise.

## 2. Source/endpoint notation is frozen

For a canonical first-crossing near-return

\[
T^j(r)=s=r+d,
\qquad
D=2^j-3^q,
\]

one has

\[
\boxed{
A_w=Dr+2^jd=Ds+3^qd,}
\]

and

\[
\boxed{0\le d<A_w/2^j<q/3<j/3.}
\]

Therefore

```text
source   = (A_w-2^j d)/D;
endpoint = (A_w-3^q d)/D.
```

The congruences are equivalent modulo `D`; the quotients are not
interchangeable.

## 3. What is already closed in FC

Subject to the declared source inputs:

```text
upper-mechanical word:
  descends at every nontrivial length;

no-wrap nonmechanical word:
  is easier to descend than the mechanical word;

low-complexity / low-bank families:
  are eventually excluded;

sub-sqrt(j)-support repair families:
  are excluded;

one-pulse near-return families over the two known negative baselines:
  are excluded within PR #83's declared source-dependent scope.
```

The complete exceptional family is polynomially sparse across words at each
length, but every unbounded acyclic member is internally rough:

\[
R_j
\ge
\sqrt{{\log2\over2\log3}j}-O(\log j),
\]

with `R_j` the number of displaced odd positions.

## 4. New uniform mechanical support loss

Let

\[
C_j={3^q\over2^j}
\]

and let `R(v)` be the displaced support of a nonmechanical first-crossing word
relative to the upper-mechanical word.  `L-6816` proves

\[
\boxed{
E_{\rm mech}-E_v>{C_j\over12}R(v)>{R(v)\over24}.}
\]

Therefore every canonical non-descent satisfies

\[
\boxed{
 r_v
 <
 F_j-{C_jR(v)\over12(1-C_j)},}
\qquad
F_j={A_{\rm mech}(j)\over2^j-3^q}.
\]

This couples the ordinary source coordinate directly to the internal support
forced by the full first-crossing geometry.

## 5. Exact return-forced support threshold

Define

\[
L_j(R)=\left\lfloor{j-2\over2(R+1)}\right\rfloor
\]

and let `rho_j` be the least nonnegative integer `R` for which either
`L_j(R)=0` or

\[
2^{L_j(R)}+1
<
3^{R+1}
\left({q\over3\lambda_j}+{q\over3}\right),
\qquad
\lambda_j=j\log2-q\log3.
\]

`T-6812` proves that every internally injective nonmechanical canonical
failure has

\[
R(v)\ge rho_j.
\]

This threshold is exact and source-free; a directed lower bound for
`lambda_j` makes it finitely certifiable.

## 6. Strictly weaker cofinal envelope

Define

\[
\boxed{
H_j^{\rm supp}
=
F_j-{C_jrho_j\over12(1-C_j)}.}
\]

Every internally injective nonmechanical failure has source below
`H_j^supp`.  Primitive positive cycles and failures containing repeated
proper states reduce to an internally injective canonical first-crossing
witness.

Consequently, after a finite initial audit, the cofinal inequality

\[
\boxed{m_{j-1}^{\rm sup}\ge H_j^{\rm supp}}
\]

closes FC*.  The corrected envelope remains unbounded along the lower
convergents, so the same hypothesis also forces SC*.

The explicit scalar version is

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

## 7. Updated SC* equivalence from the base branch

The updated PR #77 base now contains `T-6710`:

\[
\boxed{
m_N>B
\iff
\tau_c(n)\le N
\text{ for every }1\le n\le B.}
\]

It follows that SC* is exactly universal finite coefficient stopping.  In
fixed-source form, a source `n` realizes an all-supercritical word `w` of
length `N` only if

\[
v_2(3^{q(w)}n+A_w)\ge N.
\]

`L-6711` gives a sharp endpoint-accumulation inequality for a fixed source,
but it does not move that source.  The missing theorem is a source-dependent
finite upper bound on the displayed valuation.

For the corrected envelope put

\[
B_j^{\rm supp}=\lceil H_j^{\rm supp}\rceil-1.
\]

The smallest exact remaining moving box is

\[
\boxed{
\tau_c(n)\le j-1
\quad
(1\le n\le B_j^{\rm supp})}
\]

cofinally in the valid first-crossing lengths.

## 8. Complete-denominator form remains mandatory

Factor

\[
D=2^j-3^q=\prod_sQ_s,
\qquad
h_s=\operatorname{ord}_{Q_s}(2).
\]

`L-6809` remains the lossless local-to-global compiler.  One exact FC tuple
requires:

```text
compatible local excess paths modulo every h_s;
the unique monotone ordinary lift;
every proper first-crossing inequality;
one common 0<=d<q/3;
every complete prime-power equation A == 3^q d;
the canonical source (A-2^j d)/D.
```

No proper-factor hit, factor tuple without a common `d`, or reconstructed word
failing the prefix barriers is a certificate.

## 9. Smallest exact blocker

The current program has not proved the original envelope, the
support-corrected envelope, SC*, or FC*.

After the new loss theorem, the smallest exact blocker is either of the
equivalent forms:

```text
cofinal source form:
  m_(j-1)^sup >= H_j^supp;

moving coefficient-stopping box:
  tau_c(n)<=j-1 for every n<=ceil(H_j^supp)-1;

fixed-source valuation form:
  v_2(3^q n+A_w)<|w| beyond a source-dependent finite depth;

complete-denominator form:
  no complete first-crossing tuple survives with one d<q/3.
```

Any future claim must close one of these forms rather than add downstream
physical growth, family sparsity, or proper-factor compatibility.
