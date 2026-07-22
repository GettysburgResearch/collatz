# T-8803 — Parameterized ordinary-section repetition rigidity

Claim ID: T-8803  
Title: Repetition and factor-complexity obstruction for every binary expanding chart  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801  
Scope: all `U=2^m`, odd `V>U`, and binary directives whose completion is a positive ordinary integer  
Related counterexample candidates: issue #26; independent reconstruction of the mechanism neighboring PR #20

## Statement

Let

```text
U=2^m,  m>=1,
V>U,    V odd,
C=V-U,
Phi(eps)=(C/V)*sum_(j>=0) eps_j*(U/V)^j in Z_2.
```

Let `eps in {0,1}^N` and suppose

```text
M=Phi(eps)
```

is a positive ordinary integer. If two length-`ell` factors agree at starting
positions `0<=r<t`, then either

```text
M=1 and eps=111...,
```

or

```text
U^(t+ell) < M*V^t,
```

and hence

```text
ell < (log_U(V)-1)*t + log_U(M).
```

Let `p_eps(ell)` denote the number of distinct length-`ell` factors. For every
nontrivial ordinary completion,

```text
p_eps(ell)
  > (ell-log_U(M))/(log_U(V)-1),
```

so

```text
liminf_(ell->infinity) p_eps(ell)/ell
  >= 1/(log_U(V)-1).
```

### `5x+1` specialization

For a positive ordinary integer `A` whose orbit remains forever in the chart of
T-8802, put `M=A+2`. Then

```text
U=4,
V=5,
M=Phi_(4,5)(eps)>=3.
```

The exceptional all-one case is impossible, and every repeated factor obeys

```text
4^(t+ell) < (A+2)*5^t,
ell < (log_4(5)-1)*t + log_4(A+2).
```

Moreover,

```text
liminf p_eps(ell)/ell
  >= 1/(log_4(5)-1)
  = 6.212567439010779752... .
```

Thus no such positive ordinary `5x+1` chart survivor has Sturmian,
quasi-Sturmian, or any lower factor-complexity slope below that constant.

## Definitions

The logarithms are real logarithms. The series defining a generic nonperiodic
`eps` is used only in `Z_2`. Real estimates are applied solely to rational,
eventually periodic approximants.

## Motivation

PR #20 obtains a strong repetition obstruction for its `64 -> 81` chart. This
theorem reconstructs the mechanism from first principles and exposes the exact
portable parameter

```text
delta(U,V)=log_U(V)-1.
```

Its survival at the genuine positive-drift `4 -> 5` control chart is a hidden
connection: low-complexity exclusion is not, by itself, evidence of negative
Collatz drift. It is an ordinary-section completion-height phenomenon whose
strength becomes extreme near the critical boundary `V=U`.

## Proof or construction

### Step 1: exact common-prefix valuation and injectivity

If two directives first differ at position `j`, factor their difference as

```text
Phi(eps)-Phi(eta)
 = (C/V)*(U/V)^j
   * [plus_or_minus 1 + (U/V)Z],
```

where `Z in Z_2`. The bracket is odd because `U/V` is divisible by `2` in
`Z_2`, and `C/V` is also odd. Therefore

```text
v_2(Phi(eps)-Phi(eta)) = m*j.
```

In particular, `Phi` is injective, and agreement through position `N-1`
implies the difference is divisible by `U^N`.

### Step 2: construct an eventually periodic approximant

Set `s=t-r`. Retain the first `r` digits of `eps` and repeat the block
`eps[r:t]` forever:

```text
eta = eps[0:r] (eps[r:t])^infinity.
```

The equality of the two length-`ell` factors makes the interval
`eps[r:t+ell]` `s`-periodic. Repeatedly subtracting `s` from an index shows that
`eta` and `eps` agree at every position below `t+ell`, including when the
repeated factors overlap.

Put

```text
Y=Phi(eta).
```

The geometric series is rational. Writing `Y=p/q` in lowest terms with `q>0`,
its denominator divides

```text
V^r*(V^s-U^s).
```

This number is odd, and

```text
q < V^(r+s)=V^t.
```

In the real embedding, the same eventually periodic rational satisfies

```text
0<=Y<=1,
```

because its digits are binary and the all-one sum is exactly `1`.

### Step 3: combine `2`-adic closeness with archimedean height

The common prefix gives

```text
M-Y in U^(t+ell) Z_2.
```

Since `q` is odd,

```text
z=qM-p=q(M-Y)
```

is an ordinary integer divisible by `U^(t+ell)`.

If `z!=0`, then

```text
U^(t+ell) <= |z|.
```

Because `M>=1` and `0<=Y<=1`,

```text
|z|=q|M-Y|<=qM<MV^t.
```

This proves

```text
U^(t+ell)<MV^t
```

and the logarithmic repetition bound.

If `z=0`, then `M=Y` lies in `[0,1]`; positive integrality forces `M=1`.
Injectivity and `Phi(111...)=1` force `eps=111...`.

### Step 4: factor complexity

Fix `ell` and write `p=p_eps(ell)`. Among the `p+1` factors starting at
positions `0,1,...,p`, two agree. Choose starts `r<t`; then `t<=p`. The
repetition inequality gives

```text
ell < (log_U(V)-1)*p + log_U(M).
```

Rearrangement proves the finite complexity bound. Divide by `ell` and take
`liminf` for the asymptotic result.

### Step 5: specialize to `5x+1`

T-8802 gives `M=A+2=Phi_(4,5)(eps)`. Since `A>0`, `M>=3`, so the zero-numerator
exception cannot occur. Substitute `U=4,V=5` in the general bounds. **QED**

## Dependency audit

Only the chart completion definition in D-8801 and elementary geometric-series,
valuation, and pigeonhole arguments are used. The proof is independent of the
unreviewed status of neighboring PR #20 claims.

T-8802 is needed only to translate the generic theorem to the physical `5x+1`
chart.

## Gap audit

- The theorem is conditional on the completion being an ordinary positive
  integer. Generic `2`-adic directives are not constrained by the archimedean
  height argument.
- The arbitrary nonperiodic directive is never interpreted via a real infinite
  sum. Only its eventually periodic approximant is evaluated in both places.
- Repeated factors may overlap; the common-prefix argument explicitly covers
  this case.
- The theorem gives a large linear complexity lower bound, not positive entropy.
- A low-complexity input directive can be transformed into a higher-complexity
  physical code by an unbounded or nonuniform transducer. The theorem constrains
  the code to which `Phi` is applied.
- No transfer theorem says that a `3x+1` counterexample must resemble a `5x+1`
  chart survivor.

## Adversarial tests

X-8801 independently computes the constants

```text
1/(log_64(81)-1)=17.654847577085155652...,
1/(log_4(5)-1)=6.212567439010779752...,
```

and verifies the exact chart identities used in the specialization. The proof,
not the decimal calculation, establishes the theorem.

## Remaining uncertainty

The proof appears complete but awaits independent reconstruction. The main
strategic uncertainty is whether a finite connector grammar for T-8802 forces
its **output** phase code below the stated complexity threshold.

## Suggested next attack

Prove a complexity-transfer and fuel-balance theorem for finite connector
families on the two phases. This would turn the control theorem into either a
constructive certificate or a complete format-level no-go result.
