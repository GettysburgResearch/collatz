# Open questions — ordinary-section and stack-value program

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Last updated:** 2026-07-21

## Q-9401 — Directive-to-output complexity transfer

**Status:** PARTIAL / sharply split by `T-9404` and `R-9401`

For exact stack, skeleton, or marked-rewrite grammars, bound emitted-code
complexity in terms of finite control, output length, carry memory, counter
height, and genuinely fresh arithmetic bits.

### Resolved bounded-output case

`T-9404` proves

```text
p_output(n)<=Q*B*p_directive(n)
```

for a non-erasing sequential transducer with `Q` states and maximum output
length `B`. A Sturmian/quasi-Sturmian directive producing an ordinary binary
survivor needs

```text
Q*B>=18.
```

A synchronized letter-to-letter local coding is impossible.

### Refuted unrestricted shortcut

`R-9401` and `T-9406` show that unbounded run-length integration of a Sturmian
`17/18` directive can have quadratic output complexity. Therefore

```text
low directive complexity => low output complexity
```

is false without charging output length or counter growth.

### Remaining target

Use the exact demand-tree, active-cylinder, or partial-theta coordinates rather
than raw factor complexity.

---

## Q-9402 — Denominator cancellation and chart sharpening

**Status:** IDEA

The universal periodic approximant denominator is

```text
N^r*(N^s-M^s).
```

Determine whether chart classes modulo `17`, balanced digit counts, exact carry
constraints, or collision alphabets force cancellation.

Concrete targets:

1. compute the gcd of the periodic numerator with `N^s-M^s` under chart-class
   restrictions;
2. isolate cancellation forced by a fixed digit-count vector;
3. compare near-critical collision fibers with generic digit words;
4. feed any exponential saving into `T-9402` and `T-9405`.

---

## Q-9403 — Fourier-cylinder connection

**Status:** IDEA

PR #16 isolates sparse low-energy carry cylinders. Seek an implication

```text
low Fourier/carry energy
  => low arithmetic-description height
  => product-formula or partial-theta squeeze.
```

Literal repeated factors are not necessary: `T-9406` shows that the raw output
may already be quadratically complex. The desired bridge should use one of:

- the demand-tree lift digits;
- active-cylinder extension blocks;
- standard-word approximants to the sparse partial-theta value.

---

## Q-9404 — Wider collision alphabets

**Status:** PROPOSED RESOLUTION by `D-9402`, `L-9403`, and `T-9405`

For

```text
H_D(MB+d)=NB+d,
M=2^L,
N>M odd,
D subset {0,...,M-1},
```

`L-9403` gives exact periodic rational height and first-difference separation.
`T-9405` gives, for every aperiodic ordinary chart code,

```text
liminf p_d(n)/n >=1/(log_M(N)-1).
```

Independent reconstruction is required before full resolution. Chart-specific
cancellation and fiber economics remain Q-9402 and Q-9407.

---

## Q-9405 — Near-saturation structure

**Status:** IDEA

Classify repetitions close to

```text
ell=(log_M(N)-1)*t+log_M(height).
```

Near saturation forces the cross numerator to be a small multiple of
`M^(t+ell)` while the reduced denominator is near its universal maximum.
Suggested exact state:

```text
(reduced denominator,
 cross-numerator/M^(t+ell),
 chart class,
 digit-count vector,
 terminal carry state).
```

This may connect to the conditioned `3`-adic resonance program in issue #8.

---

## Q-9406 — Padding-free arithmetic information

**Status:** PARTIAL / represented exactly by `L-9405`, `T-9408`, and `T-9409`

The original question asked for an invariant that does not reward long zero
padding. Three exact candidates now exist:

1. **Demand precision:** each next base-64 demand digit is a permutation of six
   new stage bits (`L-9405`).
2. **No-reuse windows:** bounded-increment schedules have exponentially long
   windows of distinct exact demand templates (`T-9408`).
3. **Initial-cylinder precision:** a `K`-stage tower selects exactly
   ```text
   6*sum_(i=1)^K(9m_i+1)
   ```
   initial binary digits (`T-9409`).

The remaining question is not to invent another raw complexity measure, but to
prove that the selected precision cannot terminate in one ordinary context.
That value problem is now Q-9409.

---

## Q-9407 — Complexity versus collision-fiber economics

**Status:** IDEA

`T-9405` supplies the ordinary-code demand

```text
kappa(M,N)=log_(N/M)(M).
```

Issue #4 and PR #3 measure supply through

```text
log_2|D|,
fiber-width exponent,
carry-state growth,
normalized displacement width.
```

Seek a theorem comparing these quantities. The active examples require lower
complexity slopes approximately

```text
17.65, 39.12, 116.11.
```

A mismatch theorem could explain why large mildly supercritical fibers improve
finite economics without carrying one ordinary marker indefinitely.

---

## Q-9408 — Active steering and extension blocks

**Status:** PROPOSED REDUCTION by `L-9406`, `T-9409`, and `L-9407`

For every finite directive

```text
m_0,...,m_K,
```

there is exactly one working initial cylinder

```text
R_K mod Q_K.
```

An infinite directive determines one point of `Z_2`. Writing

```text
a_K=(R_(K+1)-R_K)/Q_K,
```

ordinary closure is equivalent to eventual zero of `a_K`.

`L-9407` identifies the same point with one sparse partial-theta value. Thus the
remaining dichotomy is:

```text
Obstruction:
  prove infinitely many a_K are nonzero for every admissible balanced directive.

Construction:
  construct an admissible directive with a_K=0 eventually,
  then check positivity and the Collatz chart lift.
```

Finite nonzero blocks are bounded evidence only.

---

## Q-9409 — Quadratic-lacunary `2`-adic value

**Status:** IDEA / primary theorem target

For heights `m_t`, put

```text
ell_t=9m_t+1,
H_0=0,
H_j=sum_(1<=i<=j)ell_i.
```

The unique initial context is

```text
x_0^*
 =-1/81
  +17/81^(ell_0+1)*sum_(j>=0)(64/81)^H_j.           (1)
```

For a mechanical `17/18` directive, `H_j` has a quadratic main term plus an
irrational-rotation floor-sum perturbation. `T-9410` proves that the coefficient
word of the corresponding sparse series has factor complexity `Theta(n^2)` and
support count `Theta(sqrt(N))`.

### Target A — obstruction

Prove

```text
sum_(j>=0)(64/81)^H_j notin Q
```

inside `Q_2`, or at least prove that (1) is not an ordinary integer, for every
admissible balanced directive.

### Target B — construction

Find an admissible directive making (1) an ordinary nonnegative integer. Then
replay all contexts, prove positivity, check the chart class modulo `17`, and
only afterward create a `K-####` candidate.

### Candidate methods

1. S-adic matrix products over standard words of the mechanical directive;
2. a `p`-adic Subspace-Theorem argument using simultaneous shifted
   approximants;
3. an exceptional-value theorem for nonrational sparse series with bounded
   positive second differences;
4. an adelic product-formula estimate keeping real and `2`-adic limits
   separate;
5. a direct translation from any value theorem to infinitely many nonzero
   cylinder extension blocks.

### Hypothesis warnings

- The directive is Sturmian; the actual coefficient word is not. It has
  quadratic factor complexity.
- The exponent ratio tends to one, so fixed-ratio Hadamard-gap assumptions are
  absent.
- Formal-series nonrationality does not decide one special value.
- Pre-carry support digits are not automatically the base-`2` digits of the
  final `2`-adic value.

See `Q-9409-quadratic-lacunary-value.md` and `SPARSE_PARTIAL_THETA.md`.