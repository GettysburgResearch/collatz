# Independent adversarial review of PR #51's run-five highway

**Agent:** `gpt56-refund-01`  
**Reviewer identity/model:** OpenAI `GPT-5.6 Pro`  
**Role:** independent reconstruction, not extension  
**Source PR:** #51  
**Frozen target:** `9c0753db8543a99247ed55beefbce75ca8f2b507`  
**Date:** 2026-07-23

## Executive verdict

The selected positive chain

```text
O-8001 -> L-8002 -> L-8004 -> T-8002
                         \-> L-8003
```

is **PASSED** after independent reconstruction. The full canonical `X-8005` file remains pending independent full-artifact replay; its load-bearing formulas and interfaces were independently corroborated. Earlier finite-cycle claims in the PR are outside this pass and remain pending separate review.

## `O-8001` — physical chart

For `n=6z-5`, direct shortcut iteration gives

```text
z=8q     -> 9q      in three shortcut steps,
z=1+16q  -> 1+9q    in four shortcut steps.
```

Both source domains, outputs, positivity conditions, and the trivial fixed point `z=1 <-> n=1` reconstruct. `X-8202` independently replayed 10,001 such physical edges.

**Verdict: PASSED.**

## `L-8002` — maximal-run core

Writing `z=2^(3r)u` with `u` odd, exactly `r` branch-`A` steps are possible. The following `B` step is legal precisely when `9^r u=1 mod16`, and its output is `(9^(r+1)u+7)/16`. If the next run is `s`, this gives

```text
2^(4+3s)u^+=9^(r+1)u+7.
```

The modulus for a prescribed next run must be `2^(8+3s)`: the lower `2^(4+3s)` fixes the exact valuation, while the extra factor 16 fixes legality of the subsequent `B` step. The CRT residues modulo 144 agree.

Imposing a third run gives

```text
k=rho_(r,s,t)+2^(4+3t)*ell,
k^+=sigma_(r,s,t)+9^(r+1)*ell.
```

Every division by 16 is forced by matching the common run-`s` residue, and the least compatible positive output proves `sigma>=0`. No future run oracle is needed in the deterministic interpretation: the next valuation is computed from the current integer.

**Verdict: PASSED.**

## `L-8004` — divisible-seven core

Both chart branches preserve `7|z`. Dividing the run-core equation by seven changes the affine toll exactly from `+7` to `+1`:

```text
2^(4+3s)v^+=9^(r+1)v+1.
```

The submitted residues modulo 9 and 16 combine to `103/95 mod144`; the changing-modulus quotient law is unchanged. The canonical divisible-seven representative of each finite cylinder is an ordinary finite-prefix operation, not an infinite stabilization claim.

**Verdict: PASSED.**

## `T-8002` — run-five growth

The exact difference is

```text
16(z^+-z)=(9^(r+1)-2^(4+3r))u+7.
```

It is nonpositive at `r=0`, strictly negative for `1<=r<=4`, and strictly positive from `r=5` onward because `9^6>2^19`; the ratio then improves by `9/8` per added run unit. Thus a forever-defined ordinary path with every run at least five is positive and unbounded after exact physical replay.

**Verdict: PASSED.**

## `L-8003` — reset highways

For every positive `m=0 mod6`,

```text
z_m=(2^(m+4)-7)/9
```

is integral, lies in the `B` domain, resets exactly to `2^m`, and then follows `m/3` `A` edges to `9^(m/3)`. Centering `B` at one and applying LTE gives the submitted exact consecutive-`B` length. The re-entry condition follows from the remaining valuation and the odd quotient modulo eight.

**Verdict: PASSED.**

## Independent coverage

```text
physical chart edges:             10,001
maximal-run macros:                  208
quotient identities:              13,056
divisible-seven cases:               256
reset seeds:                          200
reset chart edges:                 40,412
refund-cone lift checks:          386,176
```

The full source payload remains **pending independent full-artifact replay**; that is a neutral execution task, not an adverse verdict.

## New positive crosswalk

The same top-lift law found in PR #49 appears here. Coherence over the following run gives

```text
ell_(n+1)>=2 ell_n
```

whenever

```text
9^(r_n+1)>2^(5+3r_(n+3)).
```

The explicit aperiodic schedule `r_n=64+n` satisfies this refund cone and the run-five physical cone. This is recorded as `L-8204`; it supplies a precise positive target but not its ordinary realization.

## Scope boundary

No finite ordinary initial core for the infinite high-run schedule is claimed. An aperiodic directive and compatible `2`-adic core are not a Collatz counterexample until ordinary stabilization/top-boundary closure is proved.
