# 2-adic repetition rigidity and complexity-criticality

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Branch:** `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
**Status:** independent `94xx` theory packet; all theorem-level claims are
`PROPOSED` pending adversarial review

## Purpose

Issue #4 reduces one direct counterexample route to the existence of a
positive ordinary integer in the `64 -> 81` survivor attractor. Existing work
has exact finite amplifiers and excludes periodic, automatic,
fixed-substitution, and finite cyclic exponential-polynomial certificate
formats, but leaves a Sturmian/Ostrowski/nonstationary S-adic frontier.

This packet attacks that frontier from the ordinary-integer side. It asks what
the **actual emitted digit code of one ordinary integer** must look like. The
load-bearing mechanism is an elementary product-formula squeeze:

1. replace an early repeated factor by periodic continuation;
2. obtain an odd-denominator rational with tightly bounded ordinary height;
3. use the long common prefix to obtain extreme `2`-adic closeness;
4. show a nonzero cross numerator would be both divisible by, and smaller than,
   the same large power of the source radix.

No probabilistic model, solver, orbit scan, Fourier-decay theorem, or unmerged
claim is a proof dependency.

## Binary `64 -> 81` code

For a binary sequence `eps=(eps_n)_(n>=0)`, define

```text
Phi(eps) = (17/81) * sum_(n>=0) eps_n*(64/81)^n  in Z_2.
```

The first packet proves:

- `D-9401` — binary code, indexing, and factor complexity;
- `L-9401` — exact eventually periodic rational and odd denominator
  `<81^(r+s)`;
- `L-9402` — exact first-difference valuation `v_2=6m`;
- `T-9401` — early repeated-factor obstruction;
- `T-9402` — factor-complexity barrier.

Put

```text
delta = log_64(81)-1 = 0.056641667147...,
kappa = 1/delta       = 17.654847577085... .
```

If `A=Phi(eps)>1` is an ordinary integer and equal length-`ell` factors begin
at `r<t`, then

```text
ell < delta*t + log_64(A).
```

Consequently,

```text
p_eps(ell) > (ell-log_64(A))/delta,
liminf p_eps(ell)/ell >= kappa.
```

A nontrivial M1 witness therefore cannot have a Sturmian, quasi-Sturmian, or
other output code with lower linear complexity slope below `17.654847...`.

## Second packet: local and cross-chart consequences

### Ordinary tail states and copy-overlap

`L-9404` proves that every shifted tail represents the exact next ordinary
chart state. `T-9403` therefore applies the repetition theorem locally.
If the tail at orbit time `r` begins with a word `U` followed by a copied
prefix of length `b`, then

```text
b < delta*|U| + log_64(A_r).
```

Thus any regeneration architecture that repeatedly copies more than `5.664%`
of a long block must keep the current ordinary marker height on the same scale
as the copied block. A long square prefix `UU` is impossible once `|U|`
dominates `log_64(A_r)`.

The same theorem gives a two-parameter novelty statement: if

```text
ell >= delta*T + log_64(A),
```

then all length-`ell` factors beginning at positions `0,...,T` are distinct.

### Finite-state directive-to-output transfer

`T-9404` proves that a non-erasing deterministic sequential transducer with
`Q` states and maximum emitted block length `B` satisfies

```text
p_output(n) <= Q*B*p_directive(n).
```

Therefore a Sturmian or quasi-Sturmian directive can produce an ordinary
binary survivor only if

```text
Q*B >= 18.
```

If the transducer state is determined by bounded input context, the state
factor disappears asymptotically; a fixed-radius letter-to-letter coding is
impossible outright.

### Complexity-criticality across the collision ladder

`D-9402`, `L-9403`, and `T-9405` generalize the argument to

```text
H_D(MB+d)=NB+d,
M=2^L,
N>M odd,
D subset {0,...,M-1}.
```

Every aperiodic ordinary chart code satisfies

```text
liminf p_d(ell)/ell
  >= 1/(log_M(N)-1)
  = log_(N/M)(M).
```

Illustrative required slopes:

| chart ratio | required lower slope |
|---|---:|
| `64 -> 81` | `17.654847577085...` |
| `512 -> 729` | `17.654847577085...` |
| `2^17 -> 3^11` | `39.117553288328...` |
| `2^22 -> 3^14` | `116.110298602604...` |
| `2^44 -> 3^28` | `116.110298602604...` |

This is the **complexity-criticality law**: approaching multiplier `1` may
improve collision economics, but forces a rapidly increasing information
requirement on any one ordinary aperiodic digit code.

## Important negative result: raw complexity does not close the stack route

The naive hope that a Sturmian directive automatically yields a linearly
complex output is false when output blocks have unbounded length.

`T-9406` considers

```text
y = 1 0^(g_0) 1 0^(g_1) 1 0^(g_2) ...
```

with strictly increasing gaps and bounded positive increments. It proves

```text
p_y(n) = Omega(n^2).
```

For the idealized issue-#4 stack output, `m_(j+1)-m_j in {17,18}` gives gap
increments `{153,162}` and hence an explicit quadratic lower bound. `R-9401`
records the resulting refutation:

> a low-complexity directive need not produce a low-complexity output when a
> counter is allowed to emit increasingly long runs.

Therefore T-9402 alone does **not** close the active unbounded stack route.
The surviving target is sharper: distinguish padding complexity from genuinely
fresh arithmetic carry/residue information.

## Current frontier

The packet now separates three regimes.

1. **Bounded state and bounded output:** quantitative transfer is proved;
   Sturmian implementations below the resource threshold are excluded.
2. **Exact copied regeneration:** the local overlap budget of T-9403 supplies a
   height-sensitive obstruction.
3. **Unbounded counter/run-length output:** raw factor complexity can be
   quadratic and is not enough. A new height-normalized, run-collapsed, or
   carry-information invariant is required.

Potential connections:

- **Issue #4:** compare stack height, emitted zero padding, and fresh supply
  digits against the criticality requirement.
- **PR #3:** instrument marked grammars with current marker height, copied block
  length, overlap, finite state count, and counter growth.
- **PR #16:** determine whether sparse low-energy carry cylinders imply a
  product-formula approximant with small arithmetic description, even when raw
  output complexity is large.
- **Issue #9:** apply the general height method to repeated affine summaries in
  compressed valuation words.

## Verification

Two dependency-free experiments are committed.

### X-9401

Checks the binary periodic formula, first-difference valuation, overlapping
repetition combinatorics, and illustrative factor-complexity profiles.

Canonical SHA-256:

```text
c19c075ceaf0883e989e8050028f29cfd58740e1ce507e15f380242f753d5086
```

### X-9402

Checks general chart formulas, 39,360 first-difference pairs, 128 finite-state
transducers, all 256 binary radius-one local maps, the growing-gap factor
construction, and criticality constants across five chart ratios.

Canonical SHA-256:

```text
a7903f3ea552cf7e96884832473b9bb4c86ec99be3da47e58ab4017f9e51f79b
```

Finite checks validate interfaces only. The universal results remain written
proofs awaiting independent reconstruction.

## Review priorities

1. Reconstruct the denominator exponent and first-difference valuation in
   `L-9403`.
2. Audit the `t+ell` common-prefix argument and the shifted-state use in
   `T-9403`.
3. Audit the factor-key count in `T-9404`, especially variable block offsets.
4. Audit the aperiodic zero-numerator case in `T-9405`.
5. Audit the eligible-gap count and exactly-two-one construction in `T-9406`.
6. Search for a stronger invariant that does not count long zero padding as
   free arithmetic information.