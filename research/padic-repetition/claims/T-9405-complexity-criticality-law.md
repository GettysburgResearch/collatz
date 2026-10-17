# T-9405 — Complexity-criticality law for expanding digit charts

Claim ID: T-9405  
Title: Near-critical expanding charts force large ordinary-code factor complexity  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9402, L-9403  
Scope: every aperiodic ordinary chart code satisfying D-9402  
Related counterexample candidates: issue #4 collision-fiber ladder; PR #3 structured collision codes; no `K-####` candidate

## Statement

Let

```text
M=2^L,
N>M odd,
D subset {0,...,M-1},
```

and let `d in D^N` be an aperiodic ordinary chart code with

```text
A = Phi_(M,N)(d) in Z.
```

Put

```text
D_*   = max_(e in D) |e|,
beta  = log_M(N),
delta = beta-1 = log_M(N/M),
kappa = 1/delta = log_(N/M)(M).
```

### Repetition bound

If equal length-`ell` factors begin at positions `r<t`, then

```text
M^(t+ell) < (|A|+D_*)*N^t,               (1)
```

and therefore

```text
ell < delta*t + log_M(|A|+D_*).          (2)
```

### Factor-complexity bound

For every `ell>=1`,

```text
p_d(ell)
  > [ell-log_M(|A|+D_*)]/delta.          (3)
```

Consequently,

```text
liminf_(ell->infinity) p_d(ell)/ell
  >= kappa
  = log_(N/M)(M).                        (4)
```

The required lower slope diverges as the chart becomes near-critical:

```text
N/M -> 1^+    implies    kappa -> infinity.
```

This is the **complexity-criticality law**.

## Proof of the repetition bound

Let

```text
s=t-r.
```

Form the eventually periodic code

```text
eta = d[0:r] (d[r:t])^infinity.
```

The equal factors imply that `eta` and `d` agree through the first `t+ell`
digits, including the overlapping case.  By L-9403,

```text
Phi_(M,N)(d)-Phi_(M,N)(eta) in M^(t+ell) Z_2.   (5)
```

Write

```text
Y = Phi_(M,N)(eta) = p/q
```

in lowest terms.  L-9403 gives

```text
q odd,
q < N^(r+s)=N^t,
Y in [min D,max D] in the real embedding.       (6)
```

The integer

```text
z=qA-p=q(A-Y)
```

is divisible by `M^(t+ell)` by (5), because `q` is odd.

If `z=0`, then `A=Y`.  Injectivity from L-9403 forces `d=eta`, making `d`
eventually periodic, contrary to the hypothesis.  Hence `z!=0`, so

```text
M^(t+ell) <= |z|.
```

The real interval bound gives

```text
|A-Y| <= |A|+D_*.
```

Together with `q<N^t`,

```text
|z|=q|A-Y| < (|A|+D_*)*N^t.
```

This proves (1), and taking logarithms base `M` proves (2).

## Proof of the factor-complexity bound

Fix `ell` and write

```text
p=p_d(ell).
```

Among the `p+1` factors beginning at positions

```text
0,1,...,p,
```

two are equal.  Let their starts be `r<t`; then `t<=p`.  Applying (2),

```text
ell
 < delta*t + log_M(|A|+D_*)
 <= delta*p + log_M(|A|+D_*).
```

Rearranging gives (3).  Divide by `ell` and take `liminf` to obtain (4).
**QED**

## Cross-chart values

The following values are illustrative and are replayed by `X-9402`:

| chart ratio | `kappa=1/(log_M N-1)` |
|---|---:|
| `64 -> 81` (`2^6 -> 3^4`) | `17.654847577085...` |
| `512 -> 729` (`2^9 -> 3^6`) | `17.654847577085...` |
| `2^17 -> 3^11` | `39.117553288328...` |
| `2^22 -> 3^14` | `116.110298602604...` |
| `2^44 -> 3^28` | `116.110298602604...` |

Thus moving to a closer-to-critical collision chart may improve multiplier or
fiber economics while imposing a much larger symbolic information requirement
on any one ordinary aperiodic survivor.

## Finite-state corollary

If the chart code is the output of a non-erasing sequential transducer with
`Q` states and maximum output block length `B` from a directive `x`, the proof
of T-9404 gives

```text
p_d(n) <= Q*B*p_x(n).
```

Combining with (4),

```text
Q*B*liminf p_x(n)/n >= kappa.            (7)
```

For a Sturmian/quasi-Sturmian directive, the required integer resource product
is at least `ceil(kappa)`: `18`, `40`, and `117` for the chart ratios in the
table.

## Dependency audit

- D-9402 supplies the general chart code and criticality parameters.
- L-9403 supplies the periodic rational height, real interval, common-prefix
  divisibility, and injectivity.
- The transducer corollary reuses only the elementary counting argument of
  T-9404.

No finite computation or external theorem is used in the main proof.

## Gap audit

- Aperiodicity is essential.  If the cross numerator vanishes, the code is
  exactly the eventually periodic approximant; the theorem does not classify
  periodic integer chart orbits.
- The additive height `D_*` is deliberately universal.  Chart-specific real
  intervals or numerator cancellation may improve it.
- A large factor-complexity lower bound does not imply positive entropy.
- The law constrains the emitted digit code, not automatically a low-complexity
  directive.  Unbounded run-length output can create quadratic complexity;
  T-9406 records this loophole exactly.
- The table uses chart ratios only.  It does not assert that every displayed
  digit alphabet or chart has an ordinary survivor.

## Adversarial tests

`X-9402` checks the periodic formula and exact first-difference valuation on
five chart scales, and freezes the criticality constants.  The universal
inequalities are proved above rather than inferred from those finite cases.

## Remaining uncertainty

Independent reconstruction is pending.  The largest strategic uncertainty is
whether a stronger height-sensitive complexity invariant can charge unbounded
zero padding rather than counting it as free symbolic novelty.

## Suggested next attack

Compare each collision fiber's measured information supply

```text
log_2 |D|
```

and grammar-state budget against the required `kappa`.  Search for a theorem
showing that approaching criticality faster than carry information can grow
makes ordinary realization impossible.