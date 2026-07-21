# T-9406 — Quadratic complexity from bounded-increment growing gaps

Claim ID: T-9406  
Title: Unbounded run-length integration can turn a low-complexity directive into quadratic output complexity  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: binary words with strictly increasing, bounded-increment zero gaps  
Related counterexample candidates: issue #4 stack/S-adic frontier; no `K-####` candidate

## Statement

Let

```text
y = 1 0^(g_0) 1 0^(g_1) 1 0^(g_2) ...
```

where the integer gaps satisfy

```text
0 <= g_0 < g_1 < g_2 < ...,
1 <= g_(j+1)-g_j <= C
```

for one fixed `C>=1`.  Then for every sufficiently large integer `n`,

```text
p_y(n)
 >= (floor(n/(10C))-1) * (floor(2n/5)-1).    (1)
```

In particular,

```text
p_y(n) = Omega(n^2),
lim_(n->infinity) p_y(n)/n = infinity.        (2)
```

## Proof

Fix a sufficiently large `n`, with at least

```text
n > 2g_0,
n >= 20C.
```

Consider indices satisfying

```text
n/2 <= g_j <= 3n/5.                          (3)
```

### Step 1 — many eligible gaps

Let `j_0` be the first index with `g_(j_0)>=n/2`.  Since `n>2g_0`, we have
`j_0>=1`, and bounded increments give

```text
g_(j_0) < n/2 + C.
```

For

```text
0 <= k <= floor(n/(10C))-2,
```

we have

```text
g_(j_0+k)
 <= g_(j_0)+kC
 < n/2 + C + kC
 <= 3n/5.
```

Thus at least

```text
floor(n/(10C))-1                            (4)
```

indices satisfy (3).

### Step 2 — many factors from each eligible gap

Let `P_j` be the position of the `1` immediately before the gap `g_j`.
For an eligible `j`, and every integer

```text
0 <= a <= floor(2n/5)-2,                    (5)
```

take the length-`n` factor beginning at position `P_j-a`.

The previous `1` lies outside the factor because

```text
g_(j-1) >= g_j-C >= n/2-C >= 2n/5 >= a.
```

The factor contains the two consecutive `1`s at relative positions

```text
a,
a+g_j+1.
```

The second lies inside because, using `g_j<=3n/5`,

```text
a <= 2n/5-2 <= n-g_j-2.
```

The following `1` lies outside because

```text
g_(j+1)>g_j>=n/2,
```

so its relative position is

```text
a+g_j+1+g_(j+1)+1 > n.
```

Hence the factor has exactly two `1`s, separated by exactly `g_j` zeros.

For fixed `j`, different values of `a` put the first `1` in different
positions.  For different `j`, strict increase of the gaps gives different
separations.  Therefore all pairs `(j,a)` produce distinct length-`n` factors.

There are at least the product of (4) and

```text
floor(2n/5)-1
```

choices from (5), proving (1).  The right side is asymptotic to

```text
n^2/(25C),
```

which proves (2).  **QED**

## Application to the issue-#4 stack shape

The exact stack amplifier emits a stage prefix of the form

```text
1 0^(9m).
```

The surviving balanced schedule discussed on issue #4 uses height increments

```text
m_(j+1)-m_j in {17,18}.
```

For the concatenated idealized stage output, the zero gaps therefore have
increments

```text
g_(j+1)-g_j in {153,162}.
```

Taking `C=162`, the theorem gives

```text
p_y(n) >= (floor(n/1620)-1)*(floor(2n/5)-1)
       = Omega(n^2),
```

with asymptotic lower coefficient at least `1/4050`.

Thus a Sturmian `17/18` **directive** can emit an output whose factor complexity
is far above the linear threshold in T-9402.  Raw factor complexity alone does
not close the unbounded stack route.

## Dependency audit

The theorem is elementary combinatorics on words and has no mathematical
dependency on another branch.  The final application uses only the reported
stage-word and `17/18` height-increment shape as a branch-qualified interface;
it does not assume that an infinite ordinary stack tower exists.

## Gap audit

- Strictly increasing gaps are essential for distinguishing different `j` by
  the separation of the two `1`s.
- The upper increment bound is essential for obtaining linearly many eligible
  gaps in `[n/2,3n/5]`.
- The theorem is a complexity statement, not an ordinary-integer existence
  statement.
- Quadratic output complexity may be generated largely by zero padding and
  absolute gap lengths.  It need not represent genuinely fresh arithmetic
  carry information.
- The idealized concatenated stage word is a necessary output-shape model for
  the stack schedule, not a proof that all regeneration congruences close.

## Adversarial tests

`X-9402` generates gaps with increments `153` and `162` from a frozen Fibonacci
directive.  At four finite scales it reconstructs the exact two-one factors,
checks the previous/next-one exclusion inequalities, and verifies the uniform
lower bound (1).  The finite checks are not the universal proof.

## Remaining uncertainty

Independent reconstruction is pending.  The strategic conclusion—not the
combinatorial proof—is that a stronger invariant must distinguish padding
complexity from arithmetic information.

## Suggested next attack

Replace raw factor complexity by a height-normalized or run-collapsed
complexity that charges only new gap/carry data.  Any candidate invariant must
remain compatible with the product-formula height squeeze of T-9401 and
T-9405.