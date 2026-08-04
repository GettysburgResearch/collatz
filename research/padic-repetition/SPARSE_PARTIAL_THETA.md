# Sparse partial-theta normal form for the active stack

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Branch:** `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
**Status:** synthesis of `L-9407`, `T-9410`, and `Q-9409`; theorem-level claims remain `PROPOSED`

## 1. Why this coordinate is useful

The previous active-cylinder packet proved that a prescribed infinite height
directive chooses exactly one initial point of `Z_2`, and that ordinary closure
is equivalent to eventual stabilization of the least cylinder representatives.
That formulation is exact, but the selected point was still described through
a backwards tower of modular inversions.

`L-9407` gives a direct forward formula for the same point. It exposes the
remaining problem as one special-value question for a sparse `2`-adic series.

## 2. From a height directive to one binary code

Fix heights

```text
m_0,m_1,m_2,...
```

and set

```text
ell_t=9*m_t+1,
h_0=0,
h_t=sum_(i<t) ell_i.
```

Define a binary word by placing a `1` exactly at every stage boundary `h_t`.
Its blocks are

```text
1 0^(ell_0-1), 1 0^(ell_1-1), 1 0^(ell_2-1), ... .
```

Under the issue-#4 coding map,

```text
Phi(eps)=(17/81)*sum_(t>=0)(64/81)^h_t.             (1)
```

The shift identity for `Phi` shows that the tail beginning at `h_t` is exactly
the formal stage state at height `m_t`. Thus every directive produces one
formal infinite stack orbit in `Z_2` without further choices.

## 3. Context form

Remove the first stage and put

```text
H_0=0,
H_j=sum_(1<=i<=j) ell_i.
```

For the initial context `x_0`, define `Z_0=81*x_0+1`. Then

```text
Z_0
 =17/81^(ell_0)*sum_(j>=0)(64/81)^H_j,              (2)
```

or

```text
x_0
 =-1/81
  +17/81^(ell_0+1)*sum_(j>=0)(64/81)^H_j.           (3)
```

This is the sparse stack partial-theta normal form.

The finite truncations of (2) agree exactly with the backwards active cylinders
of `T-9409`. Therefore the two earlier formulations are equivalent:

```text
least cylinder representatives eventually stabilize
```

if and only if

```text
the value in (3) is one ordinary nonnegative integer.
```

Positivity of every later context and the chart-class lift remain additional
requirements.

## 4. Mechanical `17/18` directives

For a mechanical directive write

```text
m_(t+1)-m_t=17+s_t,
s_t=floor((t+1)*theta+rho)-floor(t*theta+rho),
```

with `s_t in {0,1}`. Then

```text
m_t=m_0+17*t+floor(t*theta+rho)-floor(rho),
```

and

```text
H_j
 =j*(9*m_0+1)
  +153*j*(j+1)/2
  +9*sum_(i=1)^j(floor(i*theta+rho)-floor(rho)).     (4)
```

So the remaining value is a `2`-adic partial-theta/Hecke-Mahler-type series
with a quadratic main exponent and an irrational-rotation perturbation.

## 5. Exact coefficient complexity

`T-9410` proves that the coefficient word in (1) has

```text
p(n)=Theta(n^2).                                    (5)
```

The lower bound comes from the many distinct two-one factors created by the
strictly increasing gaps. The upper bound is elementary: only `O(n)` gaps can
fit inside a length-`n` factor, and each supports at most `n` start offsets.

The support positions themselves satisfy quadratic bounds. For `17/18`
increments,

```text
j*(9*m_0+1)+153*j*(j-1)/2
 <=h_j
 <=j*(9*m_0+1)+162*j*(j-1)/2.                      (6)
```

Hence the first `N` coefficient positions contain only `Theta(sqrt(N))` ones,
even though their local factor complexity is quadratic.

## 6. What is ruled out as a shortcut

The exact hypothesis audit matters.

1. The **directive** is Sturmian/Ostrowski, but the actual coefficient word of
   the value is not. Its complexity is quadratic, not `n+O(1)`.
2. The exponent ratio satisfies
   ```text
   H_(j+1)/H_j -> 1,
   ```
   so fixed-ratio Hadamard-gap theorems do not apply directly.
3. The formal series is nonrational, but formal-function nonrationality does
   not imply irrationality of one exceptional `2`-adic value.
4. The real sum of the rational truncations cannot be identified with the
   `2`-adic limit. Any adelic argument must keep the embeddings separate.
5. A digit theorem for the base-`2` or base-`64` expansion of the final value
   cannot be applied merely to the pre-carry coefficient support.

These are failed proof shortcuts, not evidence that the value is rational.

## 7. The remaining theorem target

For every admissible balanced directive, prove

```text
sum_(j>=0)(64/81)^H_j notin Q                       (7)
```

inside `Q_2`, or at least prove that the affine value (3) is not an ordinary
integer.

A proof of (7), combined with `L-9407`, would close this exact stack
architecture. Conversely, an admissible directive making (3) an ordinary
nonnegative integer would produce one context to replay, test for positivity,
check modulo `17`, and only then promote to a candidate.

## 8. Promising interfaces

### S-adic matrix products

Standard words of the mechanical directive give long repeated directive blocks.
Track simultaneously:

```text
- exponent sums;
- sparse partial values;
- denominator heights;
- cylinder extension blocks.
```

The goal is several simultaneous rational approximants rather than one trivial
truncation.

### `p`-adic Subspace Theorem

A repeated standard word may produce linear forms involving several shifted
copies of the same sparse value. The needed estimate must beat the automatic
`2`-adic accuracy supplied by ordinary truncation.

### Exceptional-value theorem

Develop a theorem saying that a nonrational `{0,1}` series with strictly
increasing, bounded positive second differences cannot take a rational value at
`64/81` in `Q_2`.

### Block-tail translation

Express any special-value obstruction as infinitely many nonzero cylinder
extension blocks

```text
(R_(K+1)-R_K)/Q_K.
```

This keeps the theorem connected to the exact active grammar rather than only
to an abstract series.

### Adelic estimates

Use the same rational standard-word approximants in the real and `2`-adic
absolute values, but never identify their limits. A product-formula argument
would need a genuine smallness gain at enough places to overwhelm numerator
height.

## 9. Verification artifact

`X-9405` independently checks:

- the sparse-series/active-cylinder identity on every one-through-three-edge
  schedule over heights `{0,1,2,3}`;
- balanced `17/18` prefixes through twelve stages;
- the quadratic exponent envelopes through 200 stages;
- exact factor sets at lengths `512,1024,2048,4096`.

The finite experiment is an interface verifier, not a special-value theorem.

## 10. Handoff

The next researcher should read, in order:

1. `claims/L-9407-stack-partial-theta-normal-form.md`;
2. `claims/T-9410-stack-support-quadratic-complexity.md`;
3. `Q-9409-quadratic-lacunary-value.md`;
4. `experiments/X-9405-sparse-partial-theta/run.py`;
5. `claims/T-9409-finite-tower-cylinder.md`.

The first unsupported step to avoid is: “the directive is Sturmian, therefore
a Sturmian-digit transcendence theorem applies.” The object whose value matters
has a different coefficient word.