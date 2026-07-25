# X-6150 — exact cycle-length floor from the verification bound

```text
Experiment ID:   X-6150
Agent:           claude-opus5-61
Issue:           #58 (follow-on); cycle-lane counterpart of X-6110, predicted by T-6140
Claims:          T-6141 (the floor), T-6140 (the lane dichotomy it demonstrates)
Environment:     Linux 6.18.5 x86_64, Python 3.11 (decimal + fractions only)
Randomness:      none
Runtime:         ~2 minutes
```

## Research question

A positive Collatz cycle with `k` odd elements, `q` total shortcut steps and minimum element
`m` satisfies the exact identity `prod (3 + 1/n_i) = 2^q`, hence

```text
m  <=  k * 2^q / ( 3 * (2^q - 3^k) )                       (T-6141b, pure integers)
| q/k - log3/log2 |  <=  1 / (3 m log 2)                   (T-6141c)
```

Given a verification bound `B` (every `n < B` reaches 1, so `m >= B`), which `(q,k)` survive?

## Method

1. Enumerate candidates. By Legendre's theorem `q/k` must be a continued-fraction convergent
   of `log_2(3)` whenever `k^2 < 3 B ln2 / 2`, so the convergents are the only candidates in
   that range. The continued fraction is produced with 200-digit decimals and its leading 18
   terms are asserted equal to the classical value `[1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3]`.
   **This step only enumerates; no conclusion rests on it.**
2. Decide each candidate exactly.
   * `q <= 60000`: compute `2^q` and `3^k` as exact big integers and apply the bound directly.
     Fully certified, no floating point.
   * `q > 60000`: bound `delta = q ln2 - k ln3` by certified rational intervals around `ln 2`
     and `ln 3` (decimal `ln` is correctly rounded; the interval is widened by 10 ulp), and use
     `m <= k/(3 delta_lo)`.
3. A candidate is excluded if `2^q < 3^k` (impossible by the identity) or if its bound on `m`
   is at most `B`.

## Commands

```sh
python3 cycle_convergents.py 40 71 > results/convergents_B71.txt   # B = 2^71
python3 cycle_convergents.py 40 68 > results/convergents_B68.txt   # B = 2^68
```

Arguments: number of continued-fraction terms, and `log2(B)`.

## Results

Every convergent with `k < 4.95 * 10^10` is excluded. The first surviving one is

```text
q = 217976794617 halvings,  k = 137528045312 odd steps,  bound on m ~ 5.10 * 10^22.
```

Certified conclusions, as a function of the verification bound:

| `B` | unconditional `k >=` | unconditional `q >=` |
|---|---:|---:|
| `2^68` | `1.7518 * 10^10` | `2.7765 * 10^10` |
| `2^71` | `4.9548 * 10^10` | `7.8531 * 10^10` |

and, *if* `q/k` is a convergent, `k >= 137528045312`.

## Validation

* **The trivial cycle is exactly on the bound.** `1 -> 2 -> 1` has `q = 2`, `k = 1`,
  `2^q - 3^k = 1`, and the bound gives `m <= 4/3`, i.e. `m <= 1`, attained by `m = 1`. This
  checks the derivation *and* the orientation of `q` versus `k`, which is the easy error.
* Convergents alternate between `2^q > 3^k` and `2^q < 3^k`, as they must; both cases are
  printed and the impossible ones are discarded by the identity rather than skipped.
* The exact-integer and certified-interval routes overlap in range and agree.

## Limitations

* `B` is an **input**. The exhaustive-verification record cannot be checked from inside this
  repository, so results are published as a function of `B` and the floor scales as `sqrt(B)`.
* This is a floor, not an exclusion: it does not show that no cycle exists.
* The method is classical (Crandall 1978, Steiner 1977). The contribution here is an exact,
  parameterised, reproducible computation — not a new idea. Deeper results (Eliahou;
  Simons-de Weger on the number of circuits) are neither reproduced nor superseded.
* The Legendre gap between `sqrt(3B ln2/2)` and the first surviving convergent is not closable
  by this argument; see T-6141's suggested next attack.

## Why this sits next to X-6110

T-6140 predicts the two lanes behave differently under finite computation. Here it is,
measured: in the cycle lane two minutes of exact arithmetic excludes an infinite family of
`(q,k)` and yields an unconditional floor. In the divergence lane (X-6110) 94 billion nodes of
search bought exactly one inequality and excluded nothing. That asymmetry is T-6140(C), not a
difference in effort.
