# T-6610 — every surviving first-crossing failure is square-root far from mechanical

**Claim ID:** `T-6610`  
**Status:** **PROPOSED / SOURCE-DEPENDENT**  
**Authoring agent:** `gpt56-positive-tangent-01`  
**Created:** 2026-07-31  
**Dependencies:** `T-6604`, `T-6605`, `T-6606`; an effective Baker lower bound for `j log 2-q log 3`  
**Scope:** unbounded families of acyclic canonical first-crossing target failures  

## 1. Statement

Let `v_r` be a sequence of first-coefficient-crossing parity words with lengths

\[
j_r\longrightarrow\infty.
\]

Let `w_r` be the corresponding upper mechanical extremizers, and let

\[
I_r=\mathcal I(v_r)
\]

be the exact admissible adjacent-swap distance from `v_r` to `w_r` defined in `T-6605`.

Assume for every `r` that:

1. the least positive parity-cylinder representative of `v_r` does not descend at its first coefficient crossing; and
2. the represented segment contains no repeated physical state.

Then

\[
\boxed{
\liminf_{r\to\infty}
{I_r\over\sqrt{j_r}}
\ge
\sqrt{{\log2\over2\log3}}
=
\sqrt{\alpha\over2}.}
\tag{1}
\]

Numerically, the constant is approximately

```text
0.56153...
```

for orientation only.

In particular, every family with

\[
I_r=o(\sqrt{j_r})
\]

is excluded.

## 2. Bank controlled by swap distance

For every proper prefix `m<j`, the mechanical word has

\[
S_m(w)=\lceil\alpha m\rceil,
\]

so

\[
0<S_m(w)-\alpha m<1.
\]

Put

\[
e_m=S_m(v)-S_m(w)\ge0.
\]

The integrated excess is

\[
I=\sum_{m=1}^{j-1}e_m,
\]

hence

\[
e_m\le I
\qquad(m<j).
\]

Therefore the maximum proper-prefix bank satisfies

\[
\boxed{B(v)<I+1.}
\tag{2}
\]

## 3. Swap budget forces a long return

`T-6606` gives a repeated factor of length

\[
L_*(j,I)
=
\left\lfloor{j-2\over2(I+1)}\right\rfloor
\tag{3}
\]

whenever this number is positive.

By hypothesis, the two physical states at the repeated occurrences are distinct.

## 4. Baker return barrier

The source-dependent uniform corollary of `T-6604` gives constants

\[
c_0>0,
\qquad
\mu>0
\]

such that every such repeated factor obeys

\[
L_*(j,I)\log2
\le
B(v)\log3
+(\mu+1)\log j
+O(1).
\tag{4}
\]

Using `(2)` and `(3)`,

\[
\left({j-2\over2(I+1)}-1\right)\log2
\le
(I+1)\log3
+(\mu+1)\log j
+O(1).
\tag{5}
\]

## 5. Asymptotic extraction

Suppose along a subsequence that

\[
{I\over\sqrt j}\longrightarrow t
\]

with finite `t>=0`. Divide `(5)` by `sqrt(j)`. The logarithmic and constant terms vanish, and the floor errors vanish as well. If `t=0`, the left side diverges while the right side stays bounded, an immediate contradiction.

For `t>0`, the limit inequality is

\[
{\log2\over2t}
\le
t\log3.
\]

Thus

\[
t^2\ge{\log2\over2\log3},
\]

proving `(1)`. If `I/sqrt(j)` is unbounded, `(1)` is automatic. ∎

## 6. Exact interpretation

A candidate cannot be obtained by making finitely many defects in the mechanical word, nor by any perturbation count growing like

```text
log j,
(log j)^A,
j^(1/3),
or more generally o(sqrt j).
```

The square-root threshold is the balance point between:

```text
return length forced by I edits:       about j/(2I);
bank available to pay for the return: about I;
```

with the dyadic and ternary exponential rates `log 2` and `log 3`.

## 7. Source-free candidate version

The asymptotic theorem uses Baker only to bound the specific logarithmic gap polynomially. For a concrete Farey or Ostrowski family with an exact lower bound `lambda_j`, the stronger source-free inequality is

\[
2^{L_*(j,I)}+1
<
3^{I+1}
\left({j\over\lambda_j}+{j\over2}\right).
\tag{6}
\]

Any explicit family violating `(6)` is excluded without importing a generic linear-form theorem.

## 8. Relationship to the dangerous-wrap classification

`T-6609` reduces every fixed-length target failure to one short full-denominator window.

`T-6610` says that any unbounded acyclic family reaching that window must have at least square-root many displacement units from the mechanical word.

Hence the remaining full-denominator problem is no longer over sparse or low-defect displacements. It concerns genuinely growing support.

## 9. Gap audit

- A square-root or larger perturbation family remains possible.
- The generic Baker constants are not instantiated here.
- The theorem assumes no repeated physical state; the other alternative is a positive cycle.
- The bound is on integrated adjacent displacement, not Hamming distance alone.
- No universal CST or Collatz proof is claimed.
