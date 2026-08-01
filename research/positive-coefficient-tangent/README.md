# Positive coefficient tangent: complete-factor synchronization frontier

**Agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Issue:** independent continuation of issue `#75`  
**Namespace:** isolated `69xx`  
**Status:** theorem-level claims are **PROPOSED** pending independent reconstruction

**No proof of the Collatz conjecture is claimed.**

## Synced base state

This pass was synchronized against:

```text
PR #81 head:
086ac39d93d7c1aad9d05732f5fc11c9ce349530

PR #83:
agent/gpt56-positive-tangent-01/75-coefficient-envelope
```

The corrected source/endpoint convention is retained throughout. For

\[
T_w(r)=s=r+d,\qquad
P=2^j,\quad Q=3^q,\quad D=P-Q,
\]

one has

\[
\boxed{A_w=Dr+Pd=Ds+Qd.}
\]

Thus the endpoint-labelled equation is

\[
A_w=sD+dQ,
\]

while the source-labelled equation is

\[
A_w=rD+dP.
\]

Every non-descending first crossing satisfies

\[
0\le d<A_w/P<q/3.
\]

## Current claim map

```text
T-6901  finite no-descent coefficient threshold
T-6902  wave-minimum all-supercritical two-place tangent
T-6903  divergence / CST-violation dichotomy
R-6901  compactness does not extract an ordinary seed

L-6904  canonical first-crossing integer descent defect
L-6905  SC*/FC* envelope coupling
L-6906  upper mechanical word is the exact scalar envelope
T-6905  explicit scalar crossing envelope

T-6904  logarithmic-bank zero-entropy exclusion
T-6906  bank--complexity repeated-factor ceiling

L-6907  exact one-wrap law for nonmechanical failures
L-6908  dual defect residue and unique late canonical candidate
L-6909  universal shifted full-denominator classification
R-6910  corrected start/endpoint notation
T-6911  polynomial sparsity of all non-descending first crossings

T-6907  all-repetition one-pulse positive near-return exclusion
X-6901  exact one-pulse verifier

L-6912  complete-factor displacement and quotient-jet synchronization
L-6913  resultant-root lacunary normal form
T-6914  rough support shrinks the displacement window
R-6915  cross-factor obstruction and one-factor method boundary
X-6912  exact factor-synchronization regression
```

## Complete-factor synchronization

Factor

\[
D=\prod_\nu M_\nu
\]

into complete prime powers and define

\[
\delta_\nu=[A_wQ^{-1}]_{M_\nu}.
\]

Every factor satisfying

\[
M_\nu>A_w/P
\]

must return the same ordinary integer:

\[
\boxed{\delta_\nu=d.}
\]

Hence two large factors with different residues prove descent immediately.
More generally, every large unitary block determines the exact `d`.

The gcd profile is equally rigid:

\[
\boxed{\gcd(D,A_w)=\gcd(D,d).}
\]

Thus `d=0` is precisely the full cycle-divisibility level, while `d>0`
allows only a gcd smaller than `q/3`.

## Quotient jets and the cofinal factor dichotomy

Let

\[
\mathcal B_j=
\left\lceil
\frac{q}{3(1-Q/P)}+\frac q3
\right\rceil.
\]

Every candidate has

\[
0<r,s<\mathcal B_j.
\]

For a unitary divisor `U|D`, `C=D/U`, define

\[
\delta_U=[A_wQ^{-1}]_U
\]

and, when `U|A_w-Q\delta_U`,

\[
\sigma_U=
\left[
\frac{A_w-Q\delta_U}{U}C^{-1}
\right]_U.
\]

If `U>\mathcal B_j`, then a genuine candidate forces

\[
\delta_U=d,\qquad \sigma_U=s.
\]

Once `D>\mathcal B_j^3`, the complete factorization has one of two forms:

```text
balanced:
  D=UV with U,V>\mathcal B_j;
  both blocks must return exactly the same d and endpoint jet s;

dominant:
  D=Wc with W>\mathcal B_j^2 and c<=\mathcal B_j;
  the giant prime power determines d,r,s,
  and the small cofactor must complete the divisibility.
```

These are the two smallest exact full-denominator obstructions still open.

## Resultant-root form

When `gcd(j,q)=1`, choose `a,b` with

\[
aq+bj=1
\]

and put

\[
z=2^a3^b\pmod D.
\]

Then

\[
z^q=2,\qquad z^j=3\pmod D,
\]

and

\[
\left|\operatorname{Res}(X^q-2,X^j-3)\right|=D.
\]

If the odd positions are `d_i`, define

\[
\gamma_i=j(i-1)-qd_i\ge0.
\]

The complete displacement residue becomes

\[
\boxed{
3d\equiv\sum_{i=1}^{q}z^{-\gamma_i}\pmod D.
}
\]

Relative to the upper mechanical word, with displacements
`h_i=\bar d_i-d_i`,

\[
3d\equiv
\sum_i z^{-\bar\gamma_i}2^{-h_i}\pmod D.
\]

Thus the remaining CRT problem is a least-residue theorem for a
growing-support lacunary polynomial at one universal resultant root.

## Rough support reduces the bad interval

If `R` odd positions are displaced from the upper mechanical word, then

\[
\boxed{
\frac{A_v}{2^j}
<
\frac{A_{\rm mech}}{2^j}
-
\frac{3^q}{2^j}\frac{R}{12}.
}
\]

Therefore

\[
d<
\frac{A_{\rm mech}}{2^j}
-
\frac{3^q}{2^j}\frac{R}{12}.
\]

PR #81 forces

\[
R\ge\sqrt{\frac{\log2}{2\log3}\,j}-O(\log j)
\]

for every unbounded acyclic exceptional family, so roughness removes a
square-root-width portion of the displacement window. It does not yet force
the balanced or dominant jets to disagree.

## Exact finite method boundary

`X-6912` exhausts every first-crossing word through length `27`:

```text
first-crossing words:             502,523
nontrivial canonical failures:         0
first one-factor strategy failure:    27
number of such words:                  3
```

At `j=27`,

```text
D=5*71*14303.
```

Three descending words have every individual prime-power residue below the
real threshold, while a proper two-factor block rejects each one.

Therefore a proof based on one prime-power factor at a time is impossible.
Cross-factor synchronization is not optional.

## Honest FC* status

FC* is not proved.

After all current reductions, a surviving object must be:

```text
polynomially sparse across words;
nonmechanical and wrapped in the acyclic case;
square-root-supported;
two-thirds-scale displaced;
early departing from the mechanical word;
early departing from its own post-return tail;
compatible at every complete prime-power factor;
and synchronized to one common 0<=d<q/3.
```

The cycle level `d=0` is included.

The exact remaining theorem is to exclude:

```text
Object B:
  a balanced pair of large unitary blocks returning the same d and s;

Object G:
  one giant prime-power block returning small d,r,s
  plus a completing small cofactor.
```

Equivalently, prove a uniform least-residue lower bound for the resultant
sum in `L-6913`.

## Review first

1. `claims/L-6912-complete-factor-synchronization.md`
2. `claims/L-6913-resultant-root-normal-form.md`
3. `claims/T-6914-rough-support-displacement-window.md`
4. `claims/R-6915-cross-factor-obstruction.md`
5. `experiments/X-6912-factor-synchronization/`
6. corrected `claims/L-6909-shifted-full-denominator-equation.md`
7. `claims/T-6911-polynomial-sparsity-first-crossing-failures.md`
8. PR #81 `L-6809`, `T-6810`, `T-6811`, and `Q-6802`
9. `LATEST.md`
10. latest session report
