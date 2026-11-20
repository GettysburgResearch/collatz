# A full box survives the current descending-square comparisons

**VERIFIED finite algebraic obstruction.** This is an obstruction to
coverage by specified necessary inequalities. It is not a positive
ordinary Collatz cycle, and does not show that any point in this box is
ordinarily realizable.

The cubic-descent argument in [PROOF.md](PROOF.md) does not extend to a
descending square by tightening its rational constants. For three rising
squares followed by a descending square, consider the closed box

\[
\mathcal B=\left\{g\in\mathbb R^3:
\left\|g-(1/2,1/2,1)\right\|_\infty\le1/100\right\}.
\]

Every point of this box is strictly inside the corresponding necessary
height domain, but fails each of the 12 charged comparison tests used in
the cubic packet, six additional comparisons retaining both descending
monomials, and the usual full-displacement charge inequality. The
failure has a strictly positive margin throughout the box, for the
actual constant `c=log_2 3`.

## The precise finite model

Put `gamma=c-1`, `h_0=1`, and

\[
h_i=h_{i-1}+2g_i,\qquad
u_i=h_{i-1}-\frac{2-c}{\gamma}g_i,
\qquad D=(h_3-1)/2,\qquad
u_P=D+1-\frac c\gamma.
\]

The necessary height domain is

\[
g_i\ge0,\qquad u_i\ge0,\qquad
h_3\ge F_2:=\frac{2c}{\gamma}-1.
\tag{1}
\]

The last inequality is equivalent to `u_P>=0`. Each `u_i` is an
upper bound for the corresponding rising multiplier logarithm; `u_P`
is the descending multiplier bound. The cone method must work even
at these upper bounds unless another arithmetic argument improves them.
The present assertion evaluates the charged tests at those upper bounds.

For rising squares `i<j` and `k=1,2`, the available comparison requires

\[
\min(kg_i,g_j,h_i/c)>k u_i+u_j.
\tag{2}
\]

For a rising square i and `k,ell in {1,2}`, transporting the first k
source terms to the first ell descending terms has the guaranteed
error saving and charge

\[
\min(kg_i,\ell D,h_i/c)>k u_i+\ell u_P.
\tag{3}
\]

The `ell=1` tests are those in the cubic packet, with the appropriate
descending-square divisor. The `ell=2` tests retain both descending
terms. Omitting the starting state then gives relative saving `2D`.
All of these tests fail at the charge inequality, so further conditions
needed for exact-relation or divisibility arguments cannot rescue them.

The full-displacement charge test would require

\[
h_3>2u_1+2u_2+2u_3+2u_P.
\tag{4}
\]

It fails on the entire box as well. We do not claim these are all
possible Subspace-Theorem comparisons, or that the actual multiplier
logarithms must attain their stated upper bounds.

## Exact box certificate and dependence on the logarithm

The checker uses

\[
\frac{1054}{665}<\log_2 3<\frac{485}{306},
\]

certified by the integer inequalities `2^1054<3^665` and
`3^306<2^485`. It performs the box calculations at the **lower**
endpoint `c_0=1054/665`.

This endpoint gives a rigorous obstruction for the true logarithm:

* The coefficient `(2-c)/(c-1)` decreases with c. Thus `u_i` increases
  with c at every positive `g_i`, and the domain conditions get weaker.
* `F_2=2c/(c-1)-1` decreases, so its domain condition also gets weaker.
* `u_P` increases with c, whereas `h_i/c` decreases. Hence each charged
  margin in (2) and (3) is nonincreasing with c. The full margin (4)
  is nonincreasing as well.

For an affine form `a_0+a dot g`, its exact extrema over this box are
its value at the center plus or minus `(1/100) sum |a_i|`. The checker
verifies every domain minimum is positive. For each of the 18 tests,
it identifies one of the three constituent cost margins whose maximum
over the whole box is negative. This suffices to reject that test
everywhere in the box, with no floating-point calculation.

## Actual execution receipt

Command run from the repository root on 20 November 2026:

```sh
python -X utf8 -B research/independent-attack-20261120/check_square_obstruction.py
```

Exit status: `0`.

```text
logarithm interval: 1054/665 < log2(3) < 485/306
center: ('1/2', '1/2', '1') radius: 1/100
strict domain margin: 49/100
failed charge comparisons: 18
weakest certified charge-failure gap: 3974/9725
full displacement maximum margin: -45096/9725
negative controls: oversized box rejected; zero-charge mutation rejected
PASS: whole rational box survives all stated square-descent comparisons
```

The oversized-box control crosses a domain face and must fail domain
verification. The zero-charge control removes the very multiplier
costs responsible for the obstruction; the checker must then refuse
to certify the mutated comparison as a failure.

## What a stronger argument needs

This is a region of positive volume, not a near-equality caused by an
imprecise logarithm bound. At its center the multiplier charges already
exceed the guaranteed approximation savings substantially. Further
progress needs information absent from this cone model: sharper
multiplier costs, additional relations between multipliers, use of the
minimum's location inside a root, or a different comparison. An
ordinary realization of the cone point has not been constructed.
