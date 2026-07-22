# Drift isolation at `5x+1`

Agent: `gpt56-drift-01`  
Issue: #26  
Branch: `agent/gpt56-drift-01/26-5x1-portability`  
Packet status: **PARTIAL**  
Claim namespace: `88xx`

## Mission of this packet

Use the shortcut `5x+1` map as a positive-drift control universe. The purpose is
not to transfer unproved behavior from `5x+1` back to `3x+1`; it is to separate:

1. universal parity-word and `2`-adic format constraints;
2. multiplier-specific arithmetic realization of exact charts;
3. drift-sensitive quantitative constants;
4. ordinary-integer completion obstructions.

All theorem-level entries are **PROPOSED** pending independent reconstruction.
No divergent positive seed or counterexample is claimed.

## Wave 1 — exact `4 -> 5` amplifier and portability

For

```text
T_5(n) = n/2       when n is even,
         (5n+1)/2  when n is odd,
```

there are two exact two-step branches:

```text
T_5^2(4q-1) = 5q-1,   parity word 10,
T_5^2(4q-2) = 5q-2,   parity word 01.
```

Thus the control universe contains a genuine same-phase `4 -> 5` amplifier.
Finite towers stack exactly:

```text
H^m(4^m*q-c)=5^m*q-c,   c in {1,2}.
```

For a hypothetical positive ordinary infinite chart orbit, normalize its phase
directive by `eps_j in {0,1}`. Then in `Z_2`,

```text
A+2 = (1/5) * sum_(j>=0) eps_j*(4/5)^j.
```

The ordinary-section repetition/height squeeze survives in this genuinely
positive-drift chart. If two length-`ell` factors begin at `r<t`, then

```text
4^(t+ell) < (A+2)*5^t,
```

and every nontrivial ordinary survivor code has lower factor-complexity slope at
least

```text
1/(log_4(5)-1) = 6.212567439010779752...
```

This is weaker than the active `64 -> 81` constant
`17.654847577085155652...`, but still far above Sturmian slope `1`. The
obstruction is therefore primarily ordinary-section/certificate-format driven;
its strength is amplified by the near-criticality constant

```text
delta(U,V)=log_U(V)-1.
```

A literal port of the length-`6`, weight-`4` `3x+1` phase chart fails earlier:

```text
5^4-2^6=561
```

divides none of the fifteen relevant affine corrections. That is an arithmetic
chart-realization break, not a convergence theorem.

## Wave 2 — signed phase shadows close the coarse connector frontier

### Every connector is a signed orbit lift

For any odd multiplier `a`, signed phase `d`, length `L`, and quotient `q`, let
`d_k=T_a^k(d)` and let `s_k` count odd phase states through step `k`. Then

```text
T_a^k(2^L*q+d)=a^(s_k)*2^(L-k)*q+d_k.
```

At full depth,

```text
T_a^L(2^L*q+d)=a^s*q+T_a^L(d).
```

So parity word, endpoint phase, and affine correction are shadows of one signed
integer orbit; they are not independent connector data.

### Cycle sign duality

For a nonzero signed periodic phase `d` of period `L` and weight `s`,

```text
(2^L-a^s)d=B_a(w)>0.
```

Therefore:

```text
positive cycle  <=>  2^L>a^s  <=> contracting cylinder,
negative cycle  <=>  2^L<a^s  <=> expanding cylinder.
```

The exact `4 -> 5` chart is the positive-quotient lift of the negative cycle

```text
-2 -> -1 -> -2.
```

### The two-phase switch gain telescopes

On phases `-2,-1`, define `chi(-2)=0`, `chi(-1)=1`. Every connector of length
`L`, weight `s`, start `d_0`, and end `d_L` satisfies

```text
2s-L=chi(d_0)-chi(d_L).
```

All internal phase terms cancel under concatenation. Every closed phase circuit
has exactly `s=L/2`. Thus variable connector segmentation cannot create an
additional asymptotic odd-step surplus. R-8801 records this narrow but complete
refutation.

The baseline `5/4` expansion is not refuted. A successful connector must carry
state beyond the two-valued phase: quotient, carry, deeper residue, additional
signed phases, collisions, or unbounded memory.

## Wave 2 — exact rational-base reformulation

Shift a positive chart state by

```text
M=A+2,
X=A+1.
```

One macro-step becomes

```text
M' = floor(5M/4),
4X' = 5X+delta,   delta in {0,1}.
```

Define the base-`5/4` representation tree by

```text
x --r--> y  iff  4y=5x+r,  r in {0,1,2,3,4}.
```

The least admissible digit at `x` is

```text
b(x)=(-x) mod 4 in {0,1,2,3},
```

and the bottom child is `ceil(5x/4)`. T-8806 proves the exact equivalence:

> A positive infinite `4 -> 5` chart survivor exists iff some root `X>=2` has a
> base-`5/4` bottom word using only digits `0` and `1` forever.

Any such orbit is strictly increasing, hence divergent. The next frontier is no
longer an informal phase-connector search; it is a precise forbidden-digit
problem in a rational-base tree.

See `RATIONAL_BASE_FRONTIER.md` for the live theorem targets and literature
adjacency.

## Wave 2 — `2`-adic geometry

Let

```text
C = { (1/5) * sum_(j>=0) eps_j*(4/5)^j : eps_j in {0,1} }.
```

If two directives first differ at index `j`, then their images differ with
exact valuation `2j`. Hence:

- the coding is injective and isometric for prefix scale `4^(-j)`;
- level `k` occupies exactly `2^k` residue classes modulo `4^k`;
- `C` has Haar measure zero in `Z_2`;
- `C` has Hausdorff dimension exactly `1/2`;
- positive ordinary chart survivors have upper natural density zero.

This proves arithmetic thinness, not emptiness.

## Portability matrix

| Repository mechanism | `ax+1` verdict | Exact discriminator | Meaning |
|---|---|---|---|
| Affine parity-word formula | **HOLDS-VERBATIM** | none | Pure branch algebra |
| Positive-cycle sign criterion | **HOLDS-VERBATIM** | `2^L-a^s` | Positive cycles are subcritical |
| Signed phase-shadow identity | **HOLDS-VERBATIM** | signed phase orbit | Connector data collapse to one orbit |
| One-step shared-branch fuel loss | **HOLDS-VERBATIM** | oddness of `a` | Format-driven precision drain |
| Direct `T_5^2` amplifier | **EXISTS** | `5-4=1` | Exact phases `-1,-2` |
| Literal length-6/weight-4 port | **BREAKS** | `561` divisibility | Arithmetic realization failure |
| Repetition/height squeeze | **HOLDS** | `log_U(V)-1` | Format-driven, near-criticality amplified |
| Phase-only connector surplus | **REFUTED** | coboundary `chi(start)-chi(end)` | Switch gain telescopes |
| Rational-base bottom reduction | **EXACT** | `4X'=5X+delta` | Survivor iff bottom digits stay in `{0,1}` |
| Completion-set geometry | **EXACT** | first-difference valuation `2j` | Measure zero, dimension `1/2` |
| Fair-parity drift model | **CHANGES SIGN** | `(1/2)log_2(a)-1` | Model-level only |
| Divergence of seed `7` | **UNRESOLVED** | infinite behavior | Finite ledger is not proof |

## Exact finite controls

### X-8801

- `12,288` affine-formula checks for `a in {3,5,7,9}`;
- `65,024` one-step fuel-loss checks;
- `200,000` exact physical checks of the two `4 -> 5` branches;
- positive-cycle reconstruction through parity-word length `14`;
- fixed-phase block censuses;
- one million exact shortcut steps from seed `7`.

### X-8802

- `39,999` lifted signed-connector replays through length `20`;
- `40` closed-circuit coboundary checks;
- signed-cycle reconstruction through parity-word length `18`;
- `1,000,052` physical/rational-tree edge checks for `A<=10^6`;
- a bounded low-digit survivor census.

The longest prefix below one million has depth `19`:

```text
A=786766,
X=786767,
low-digit prefix=1101100001001100001,
first exit A=54592968.
```

Every numerical statement above is finite evidence only.

## Claims

### Definitions and observations

- `D-8801`: generalized shortcut and expanding-chart definitions.
- `O-8801`: fair-parity drift threshold, explicitly model-level.

### Lemmas and theorems

- `L-8801`: universal affine parity-word formula.
- `L-8802`: exact one-step `2`-adic fuel loss.
- `L-8803`: signed phase-shadow identity.
- `T-8801`: positive-cycle sign and admissibility criterion.
- `T-8802`: exact `5x+1` `4 -> 5` chart and completion formula.
- `T-8803`: parameterized repetition rigidity and complexity bound.
- `T-8804`: signed cycle sign duality.
- `T-8805`: complete two-phase connector coboundary.
- `T-8806`: rational-base low-digit-tree equivalence.
- `T-8807`: exact completion-set Cantor geometry.

### Refutations and experiments

- `R-8801`: phase-only switch scheduling cannot create extra asymptotic gain.
- `X-8801`: generalized portability controls.
- `X-8802`: phase shadows, signed cycles, and rational-base tree controls.

## Strategic consequence

The coarse two-phase connector question is closed: the phase graph contains no
hidden scheduling freedom. The highest-upside remaining question is now exact:

```text
Does some X>=2 have
b(tau^j(X)) in {0,1} for every j>=0,
where tau(x)=ceil(5x/4)?
```

Equivalently, does the base-`5/4` bottom map `tau(x)=ceil(5x/4)` admit an orbit
that avoids residues `1,2 modulo 4` forever?

The next attacks should be one of:

1. a finite-state/PDR eventual-escape invariant;
2. a self-replicating low-digit subtree producing an ordinary root;
3. a Diophantine upper bound on low-digit prefix length;
4. a rigorously audited successor-transducer propagation theorem;
5. a richer signed-phase graph with genuine state beyond `{-2,-1}`.

## Claim boundary

This packet claims no divergent positive `5x+1` seed, no positive-integer
Collatz counterexample, and no resolution of either conjecture. It establishes
exact identities, equivalences, rigidity theorems, and finite controls designed
to expose where certificate methods depend on drift, arithmetic realization,
or representation format.
