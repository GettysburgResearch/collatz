# Tao side-branch and sharp record-bank report

## Objective

Continue the all-time coefficient-supercritical Collatz lane after the
Tao/logarithmic-sparsity result, synchronize with PRs #77, #80, #81, and #83,
recheck the source import, and seek an actual contradiction through inverse
basins, least-root escape, or a supercritical derived `2`-adic approximation.

No contradiction closing Lane A was obtained.  The pass produced a stronger
architecture-free bridge and isolates the smallest inverse-basin inequality
that would close the lane.

## Frozen heads reviewed

```text
PR #77  1c8ed3c7edbb190d59490d2f92a3c342c2f856eb
PR #80  fbc178758314d5e908f28aedf7b356938935b256
PR #81  5609d8b76f8b0b1e2b9a3b3e9e1122b67732e648
PR #83  674f36cb6f2bb620e6fab21da2838c7c52a5072d
```

## Tao audit

The current primary statement of Tao's Theorem 1.3 says that for every function
`f(N)->infinity`, the inequality

```text
Col_min(N) < f(N)
```

holds outside a set of logarithmic density zero.  The theorem imposes no
monotonicity or effectiveness requirement on `f`.  The orbit-dependent
construction is valid because the hypothetical orbit is fixed first and then
one fixed function is defined from it.

For any unbounded family `B` with

```text
Col_min(b) -> infinity  as b -> infinity in B,
```

define

```text
f_B(N) = (1/2) min { Col_min(b) : b in B, b >= N }.
```

Then `f_B(N)->infinity` and every `b in B` is Tao-exceptional.  Hence `B` is
logarithmically null.

The shortcut/unshortened minimum equivalence is exact: an odd shortcut omits
only `3x+1`, which is larger than the following `(3x+1)/2` state.

## Main new bridge

For every odd source time of a divergent shortcut orbit put

```text
b_i = 3*x_i + 1 = 2*x_(i+1).
```

The complete orbit minimum of `b_i` is the future minimum from `x_(i+1)`, which
tends to infinity.  Therefore the side-branch set `{b_i}` is logarithmically
null.

The exact affine correction product is

```text
P_k = product_(odd i<k) (1 + 1/(3*x_i)).
```

Since

```text
1/(3*x_i+1)
 <= log(1+1/(3*x_i))
 <= (4/3)/(3*x_i+1),
```

`log P_k` is equivalent, up to the fixed factor `4/3`, to the side-branch
harmonic mass.

At a physical record time `r`, every earlier side branch is at most `3*x_r+1`.
Tao therefore gives

```text
log P_r = o(log x_r).
```

Using

```text
x_r = n * 3^(D_r) * P_r,
```

we obtain

```text
D_r = (1-o(1))*log_3(x_r).
```

Because the first `K+1` states are distinct and bounded by the physical maximum
`X_K`,

```text
max_(k<=K) D_k >= (1-o(1))*log_3(K),
max_(k<=K) 3^(D_k) >= K^(1-o(1)).
```

This sharpens the elementary `8/9` record exponent in PR #80 to coefficient
`1`, source-dependently on Tao.

## Exact raw-approximation firewall

For the parity-prefix rational

```text
rho_k = -A_k / 3^(q_k),
e_k = v_2(x_k),
```

one has

```text
v_2(n-rho_k) = k+e_k,
q_k*log_2(3) - (k+e_k) = D_(k+e_k)/alpha > 0.
```

Thus every raw parity approximant has exponent strictly below one.  Its exact
deficiency is the surplus after stripping the current even run.  A successful
derived-approximation proof must overcome this deficiency and additionally
produce a uniform positive height margin.

## Inverse-basin audit

A fixed-root inverse tree cannot contradict Tao because all of its members may
have one fixed bounded future minimum.  The moving-root object is the high
first-hit basin of the increasing tail-minimum ladder.

A sufficient closing theorem is to construct finite cohorts `G_j` in those
moving high basins with

```text
sum_(j<=J) sum_(m in G_j) 1/m
 >= c * log(max_(j<=J,m in G_j) m)
```

along an unbounded sequence, while `min G_j -> infinity`.  The union would have
positive upper logarithmic density and orbit minima tending to infinity,
contradicting Tao.

No present inverse-tree theorem, power-of-two preimage family, or repository
counting result proves this diagonal harmonic-mass inequality.

## Status

Lane A remains open.  The strongest new proved bridge is:

```text
Tao spine/side-branch sparsity
  -> correction product negligible at physical records
  -> coefficient surplus pays asymptotically all record height
  -> record coefficient max >= K^(1-o(1)).
```

The smallest precise inverse-basin gap is the diagonal high-first-hit harmonic
mass inequality above.  The alternative exact gates remain PR #81 `SC*`
least-source escape and a derived rational approximation crossing exponent one.

Full details are in:

```text
research/h-frontier/claims/ITERATION_15.md
```
