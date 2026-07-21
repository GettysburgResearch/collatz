# Open questions — p-adic repetition and complexity-criticality

**Agent:** `gpt56-complexity-01`  
**Issue:** #18

## Q-9401 — Directive-to-output complexity transfer

**Status:** PARTIAL / sharply split by T-9404 and R-9401

For the exact stack, skeleton, or marked-rewrite grammars in issue #4 and
PR #3, bound the emitted survivor-code complexity in terms of

```text
- directive factor complexity;
- finite control-state count;
- maximum emitted block length;
- carry-memory radius;
- counter/stack height;
- genuinely fresh arithmetic bits introduced per level.
```

### Resolved bounded-output case

T-9404 proves that a non-erasing sequential transducer with `Q` states and
maximum output block length `B` satisfies

```text
p_output(n) <= Q*B*p_directive(n).
```

For a Sturmian/quasi-Sturmian directive producing a binary ordinary survivor,

```text
Q*B >= 18.
```

A synchronized letter-to-letter local coding is impossible.

### Refuted unrestricted shortcut

R-9401 and T-9406 show that unbounded run-length integration of a Sturmian
`17/18` directive can have quadratic output complexity. Therefore no theorem
of the form

```text
low directive complexity => low output complexity
```

is valid without charging output length or counter growth.

### Remaining target

Find a **height-normalized transfer theorem** that distinguishes long padding
from fresh carry/residue information. It should be strong enough to compare an
unbounded stack grammar with T-9403 or T-9405.

## Q-9402 — Denominator cancellation and chart sharpening

**Status:** IDEA

L-9401 and L-9403 use the universal denominator

```text
N^r*(N^s-M^s).
```

Determine whether chart classes modulo `17`, balanced block counts, exact carry
constraints, or selected collision alphabets force a uniform cancellation
factor. Even an exponential saving would increase the lower complexity slope
in T-9402/T-9405.

Concrete targets:

1. compute the gcd of the periodic numerator with `N^s-M^s` under chart-class
   restrictions;
2. isolate cancellations forced by a fixed digit-count vector;
3. determine whether near-critical fibers have more or less cancellation than
   generic digit words.

## Q-9403 — Fourier-cylinder connection

**Status:** IDEA

PR #16 isolates sparse low-energy carry cylinders. Determine whether a
low-energy cylinder supplies an arithmetic approximant whose denominator or
description height is small relative to its common-prefix depth.

The first-packet formulation asked whether low energy forces an exact repeated
factor. T-9406 shows that raw output complexity may already be quadratic, so
the stronger target is:

```text
low Fourier/carry energy
  => low arithmetic-description height
  => product-formula squeeze.
```

This could connect the ordinary-integer obstruction to the all-depth EQ
frontier without requiring literal repeated output blocks.

## Q-9404 — Wider collision alphabets

**Status:** PROPOSED RESOLUTION by D-9402, L-9403, T-9405

For

```text
H_D(MB+d)=NB+d,
M=2^L,
N>M odd,
D subset {0,...,M-1},
```

L-9403 proves exact first-difference separation and periodic rational height.
T-9405 proves, for every aperiodic ordinary chart code,

```text
liminf p_d(n)/n >= 1/(log_M(N)-1).
```

Independent reconstruction is required before this question is marked fully
resolved. Remaining chart-specific work belongs to Q-9402 and Q-9407.

## Q-9405 — Near-saturation structure

**Status:** IDEA

Classify codes with repeated factors close to

```text
ell = (log_M(N)-1)*t + log_M(height).
```

Near saturation forces the cross-multiplied rational difference to be a small
multiple of `M^(t+ell)` while the reduced denominator is near its universal
maximum. Such configurations may have rigid modular structure exploitable by
the conditioned `3`-adic resonance program in issue #8.

Suggested search state:

```text
(reduced denominator,
cross-numerator/M^(t+ell),
chart class,
digit-count vector,
terminal carry state).
```

## Q-9406 — Padding-free arithmetic information

**Status:** IDEA / primary next target

T-9406 proves that increasing zero gaps create `Omega(n^2)` ordinary factor
complexity even when the directive is Sturmian. Define an invariant that does
not reward such padding for free.

Candidate notions:

1. run-collapsed factor complexity;
2. complexity of the gap-increment word rather than absolute gap lengths;
3. arithmetic straight-line-program size of length-`n` output factors;
4. number of fresh low-order residue/carry bits needed to replay a factor;
5. factor complexity after quotienting by uniform zero-padding conjugacies;
6. product-formula approximation height per emitted nonzero/carry event.

The invariant must satisfy both:

```text
- an ordinary-integer lower bound derived from rational height;
- a grammar upper bound derived from the exact stack/marked construction.
```

## Q-9407 — Complexity versus collision-fiber economics

**Status:** IDEA

T-9405 gives the criticality demand

```text
kappa(M,N)=log_(N/M)(M).
```

Issue #4 and PR #3 measure the supply side through digit/fiber size, collision
width, carry freedom, and per-step cost. Seek a theorem comparing

```text
required ordinary-code information: kappa(M,N)
```

with

```text
available grammar information: log_2|D|,
fiber-width exponent,
carry-state growth,
normalized displacement width.
```

The near-critical examples require slopes approximately

```text
17.65, 39.12, 116.11.
```

A mismatch theorem could explain why larger mildly supercritical fibers improve
finite economics yet still fail to carry one ordinary marker indefinitely.