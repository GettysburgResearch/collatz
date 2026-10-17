# Ordinary-section rigidity for the `64 -> 81` stack

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Branch:** `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
**Status:** independent `94xx` theory program; all theorem-level claims are
`PROPOSED` pending adversarial review

## Mission

Issue #4 isolates one direct counterexample route: find a positive ordinary
integer in the binary `64 -> 81` survivor attractor. Existing work supplies
exact finite amplifiers and rules out periodic, automatic, fixed-substitution,
and finite cyclic exponential-polynomial certificate formats, while leaving a
Sturmian/Ostrowski/nonstationary S-adic stack frontier.

This packet studies that frontier from the ordinary-integer section. It now has
five layers:

1. repetition and rational-height rigidity for one ordinary survivor code;
2. complexity transfer and near-critical chart information demand;
3. exact stack-demand trees and stationary ghost stages;
4. active one-cylinder fuel conservation;
5. a sparse `2`-adic partial-theta normal form for the unique infinite context.

No result here constructs a Collatz counterexample or proves that none exists.

---

## Packet 1 — repetition rigidity

For `eps in {0,1}^N`, define

```text
Phi(eps)
 =(17/81)*sum_(n>=0)eps_n*(64/81)^n
 in Z_2.
```

`L-9401` and `L-9402` prove:

- an eventually periodic code with preperiod `r` and period `s` has an odd
  reduced denominator `<81^(r+s)` and real value in `[0,1]`;
- if two codes first differ at position `m`, then
  ```text
  v_2(Phi(eps)-Phi(eta))=6m.
  ```

If `A=Phi(eps)>1` is an ordinary integer and equal length-`ell` factors begin at
`r<t`, `T-9401` gives

```text
ell < (log_64(81)-1)*t + log_64(A).                 (1)
```

Consequently `T-9402` proves

```text
liminf p_eps(ell)/ell
 >=1/(log_64(81)-1)
 =17.654847577085... .                              (2)
```

Thus a nontrivial ordinary survivor cannot have a Sturmian, quasi-Sturmian, or
other output code below that lower linear-complexity slope.

### Local copy-overlap

Every shifted code tail represents the exact later ordinary state. If a tail at
state `A_r` begins with a word `U` followed by a copied prefix of length `b`,
`T-9403` gives

```text
b < (log_64(81)-1)*|U| + log_64(A_r).               (3)
```

This is a stage-local adversarial test for marked or copied regeneration.

---

## Packet 2 — complexity transfer and criticality

### Bounded finite-state output

For a deterministic non-erasing sequential transducer with `Q` states and
maximum emitted block length `B`, `T-9404` proves

```text
p_output(n)<=Q*B*p_directive(n).                    (4)
```

A Sturmian or quasi-Sturmian directive can emit an ordinary binary survivor
only if

```text
Q*B>=18.                                            (5)
```

A fixed-radius letter-to-letter coding is impossible.

### General expanding digit charts

For

```text
H_D(MB+d)=NB+d,
M=2^L,
N>M odd,
D subset {0,...,M-1},
```

`T-9405` proves that every aperiodic ordinary chart code satisfies

```text
liminf p_d(n)/n
 >=1/(log_M(N)-1)
 =log_(N/M)(M).                                     (6)
```

Illustrative required slopes:

| chart ratio | lower slope |
|---|---:|
| `64 -> 81` | `17.654847577085...` |
| `512 -> 729` | `17.654847577085...` |
| `2^17 -> 3^11` | `39.117553288328...` |
| `2^22 -> 3^14` | `116.110298602604...` |
| `2^44 -> 3^28` | `116.110298602604...` |

This is the **complexity-criticality law**: multiplier ratios closer to one may
improve finite collision economics while demanding much more information from
one ordinary aperiodic code.

### Negative result: padding inflates raw complexity

`T-9406` proves that

```text
y=1 0^(g_0) 1 0^(g_1) 1 0^(g_2) ...
```

with strictly increasing gaps and bounded positive gap increments has

```text
p_y(n)=Omega(n^2).
```

The idealized `17/18` stack has gap increments `{153,162}`. Therefore a
Sturmian directive can generate quadratically complex raw output merely through
long padding. `R-9401` records the failure of the unrestricted
“low-complexity directive => low-complexity output” shortcut.

---

## Packet 3 — demand tree and stationary ghosts

The exact same-stage stack demand is

```text
D(m)=17*81^(-(9m+2))-81^(-1).                       (7)
```

### Demand isometry

`L-9405` proves

```text
v_2(D(n)-D(m))=4+v_2(n-m).                          (8)
```

Hence

```text
D/16:Z_2 -> Z_2
```

is a bijective isometry. At base-`64` depth `j`,

```text
m mod 2^(6j-4)
  <->
all demand residues 0 mod 16 modulo 64^j.           (9)
```

Every parent has exactly `64` children realizing all next digits once. One new
demand digit is a permutation of six new binary stage bits: the **six-bit lift
law**.

### Stationary matching and ghost stages

For fixed `x=15 mod 16`, compare

```text
81^(9m)*(81x+1)
```

with `D(m)`. `T-9407` proves that their difference divided by `16` is another
`Z_2` isometry. Exactly one matching stage class exists at every finite depth,
with exact conditioned rates `1/4` for the first base-64 digit and `1/64` for
every additional digit.

The matching locus is

```text
X(m)
 =17*81^(-(18m+3))
  -81^(-(9m+2))
  -81^(-1).                                         (10)
```

It is a scaled isometry onto `15+16Z_2`, but `X(m)<0` in the real embedding for
every ordinary `m>=0`. Positive ordinary contexts therefore have arbitrarily
deep compatible stationary matches whose limit is a nonordinary **ghost
stage**, not one positive height.

### No-reuse windows

For positive stage increments bounded by `C`, `T-9408` proves that every

```text
floor((2^(6j-4)-1)/C)+1                             (11)
```

consecutive depth-`j` demand residues are distinct. With `C=18`, the window
lengths are

```text
15, 911, 58,255, ...
```

at depths `2,3,4,...`.

---

## Packet 4 — active quotient fuel and one cylinder

For height `m`, put

```text
ell_m=9m+1,
M_m=64^(ell_m),
A_m=81^(ell_m),
c_m=(M_m+17)/81.
```

### One-stage quotient conjugacy

For a transition from height `m` to height `n`, `L-9406` finds one admissible
residue `r_(m,n) mod M_n`. Writing

```text
x=r_(m,n)+M_n*y
```

gives the exact next context

```text
x'=A_m*y+k_(m,n).                                   (12)
```

Because `A_m` is odd,

```text
v_2(x'(y)-x'(z))=v_2(y-z).                          (13)
```

The unused high quotient is transported isometrically. Future obligations
select more quotient digits; they do not create several compatible classes or
refund consumed precision.

### Finite-tower cylinder

For any prescribed finite height schedule

```text
m_0,m_1,...,m_K,
```

`T-9409` proves that exactly one initial cylinder works:

```text
x_0=R_K mod Q_K,
Q_K=product_(i=1)^K 64^(9m_i+1).                   (14)
```

Every member of that cylinder realizes the schedule integrally, and no other
context does.

For an infinite directive the nested cylinders determine exactly one

```text
x_0^* in Z_2.
```

Let `R_K` be the least representative in `[0,Q_K)`. Then

```text
x_0^* is an ordinary nonnegative integer
 iff R_K eventually stabilizes.                     (15)
```

Equivalently, with

```text
a_K=(R_(K+1)-R_K)/Q_K,
```

ordinary closure is eventual zero of the new cylinder blocks.

For `17/18` increments, a `K`-stage tower fixes quadratically many initial
binary digits:

```text
54*K*m_0+459*K*(K+1)+6K
 <=log_2 Q_K
 <=54*K*m_0+486*K*(K+1)+6K.                        (16)
```

---

## Packet 5 — sparse partial-theta normal form

The cylinder inverse system has a direct forward expression.

For stage lengths

```text
ell_t=9m_t+1
```

and boundaries

```text
h_0=0,
h_t=sum_(i<t)ell_i,
```

place a binary `1` exactly at every `h_t`. `L-9407` proves that the exact formal
stack state is

```text
A_*(m)
 =(17/81)*sum_(t>=0)(64/81)^h_t
 in Z_2.                                             (17)
```

After removing the first stage, put

```text
H_0=0,
H_j=sum_(1<=i<=j)ell_i.
```

The unique initial context satisfies

```text
x_0^*
 =-1/81
  +17/81^(ell_0+1)*sum_(j>=0)(64/81)^H_j.           (18)
```

Finite truncations of (18) are exactly the cylinders in (14). Hence the
block-tail problem is the special-value problem:

```text
is the value in (18) one ordinary nonnegative integer?               (19)
```

### Exact coefficient class

For increasing bounded-increment heights, `T-9410` proves that the coefficient
word in (17) has

```text
p(n)=Theta(n^2),                                    (20)
```

while the support positions grow quadratically and the number of ones in the
first `N` digits is `Theta(sqrt(N))`. The corresponding formal power series is
nonrational.

For mechanical `17/18` directives, the exponents have a quadratic main term
plus an irrational-rotation floor-sum perturbation. The coefficient word is not
Sturmian, and the exponent ratio tends to one. Thus neither a linear-complexity
Sturmian-digit theorem nor a fixed-ratio Hadamard-gap theorem applies without a
new reduction.

`Q-9409` freezes the remaining value-theory target:

```text
prove sum_(j>=0)(64/81)^H_j notin Q inside Q_2,
```

or at least prove that its affine value (18) is not an ordinary integer, for
every admissible balanced directive.

See `SPARSE_PARTIAL_THETA.md` for the detailed synthesis and hypothesis audit.

---

## Verification artifacts

All experiments use the Python standard library and exact arithmetic.

### `X-9401`

Binary periodic-height, first-difference, and overlap checks.

```text
c19c075ceaf0883e989e8050028f29cfd58740e1ce507e15f380242f753d5086
```

### `X-9402`

General chart formulas, 39,360 first-difference pairs, finite-state transfer,
all radius-one binary local maps, and criticality constants.

```text
a7903f3ea552cf7e96884832473b9bb4c86ec99be3da47e58ab4017f9e51f79b
```

### `X-9403`

Demand permutations, six-bit lifts, stationary matching trees, ghost stages,
and schedule novelty.

```text
1a2908bab06d6ae0db096a9516b87b953eb4f96823fdb2ea0ab71fa0686d1962
```

### `X-9404`

Active one-cylinder recursion, quotient isometry, perturbation failures, and a
24-stage balanced prefix fixing `282,888` initial bits.

```text
73a878073e3e8e39e6e950ad0e4585c522cd7fe1794639dc5b015a3b5115be3f
```

### `X-9405`

Sparse-series/cylinder equivalence, balanced prefixes, quadratic support
bounds, and exact finite factor-complexity profiles.

```text
df2543be76c294397dcce6819c1d4551a811407a7835b7d2e1997866b0283c67
```

Finite checks validate frozen interfaces only. Universal statements rest on
the written proofs and remain `PROPOSED` pending independent reconstruction.

---

## Review order

1. `claims/L-9407-stack-partial-theta-normal-form.md`
2. `claims/T-9410-stack-support-quadratic-complexity.md`
3. `claims/L-9406-active-quotient-conjugacy.md`
4. `claims/T-9409-finite-tower-cylinder.md`
5. `claims/T-9407-stationary-matching-ghost.md`
6. `claims/L-9405-demand-tree-isometry.md`
7. `SPARSE_PARTIAL_THETA.md`
8. `Q-9409-quadratic-lacunary-value.md`
9. `experiments/X-9405-sparse-partial-theta/run.py`

## Current frontier

The exact stack route is now reduced to a special-value dichotomy.

```text
Obstruction:
  prove the sparse partial-theta context is never an ordinary integer.

Construction:
  produce an admissible directive for which it is an ordinary positive context,
  then verify every later context and the Collatz chart lift.
```

No compatible finite prefix, ghost stage, formal series, or nonzero finite
block sequence is by itself a counterexample.