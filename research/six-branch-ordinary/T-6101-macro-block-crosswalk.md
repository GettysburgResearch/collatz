```text
Claim ID:            T-6101
Title:               The six-branch rational-base chart is an exact shortcut-Collatz macro-block subsystem
Status:              PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        classical Terras/Everett parity-vector bijection (stated as L-6100 below)
Scope:               the fixed chart P=3^12, Q=2^19, A={7*3^(2i)*2^(15-3i)}; no claim about other charts
Related counterexample candidates: none produced
```

## Statement

Let

```text
P = 3^12 = 531441,   Q = 2^19 = 524288,
a_i = 7 * 3^(2i) * 2^(15-3i)  for i = 0..5,
A   = {a_0,...,a_5} = {229376, 258048, 290304, 326592, 367416, 413343}.
```

For `x` in `Z` define the chart step

```text
x' = ceil(P x / Q),      d(x) = Q x' - P x  in  [0, Q),
```

and call the step **legal** when `d(x) in A`. Let `T` be the shortcut Collatz map,
`T(n) = (3n+1)/2` for odd `n` and `T(n) = n/2` for even `n`, and let

```text
phi(x) = 6x - 5.
```

**Theorem.** For every `x` in `Z` with `d(x) = a_i`:

1. `T^19( phi(x) ) = phi(x')` with `x' = (P x + a_i)/Q`;
2. the parity word of `phi(x)` over those 19 steps is exactly

   ```text
   W_i = (110)^(5-i) . 1010 . (110)^i,
   ```

   which has exactly 12 odd steps and 7 even steps;
3. the number of leading `110` blocks before the unique `1010` defect equals `v_2(x)/3`
   (this is T-6102).

**Corollary A (subsystem).** If `x_0 > 0` is legal for `N` chart steps then the real
Collatz trajectory of `n_0 = 6x_0 - 5` executes `19N` shortcut steps containing exactly
`12N` odd steps, and `n_k = 6 x_k - 5` for every `k <= N`.

**Corollary B (automatic divergence).** If `x_0 > 0` is legal for every `n >= 0` then
`x_{n+1} >= P x_n / Q`, hence `x_n >= (P/Q)^n x_0 -> infinity` and
`n_k = 6 x_k - 5 -> infinity`. Such an `x_0` is therefore a genuine divergent Collatz
trajectory, i.e. a counterexample to the Collatz conjecture.

**Scope warning.** The converse is false. The chart is a *strict* subsystem: it forces the
orbit to repeat one of only six of the `C(18,11) = 31824` parity words of length 19 with
12 odd steps, forever. Emptiness of the chart excludes nothing outside it.

## Definitions

* `v_2` is the 2-adic valuation.
* The *parity word* of `n` of length `L` is `w_1...w_L` with `w_j = n_{j-1} mod 2`,
  `n_j = T(n_{j-1})`, `n_0 = n`.
* *Legal for N steps* means `d(x_k) in A` for `k = 0..N-1` where `x_{k+1} = ceil(P x_k / Q)`.

## Motivation

Every positive-construction lane in this project eventually needs a bridge from a symbolic
or residue-level architecture to an actual integer Collatz orbit. This theorem supplies that
bridge for the six-branch chart with no residual gap: legality for `N` chart steps is
*equivalent* to a fully specified real Collatz orbit segment of length `19N`, and all-time
legality is *equivalent* to a divergent orbit. It therefore reduces the entire counterexample
question for this architecture to a pure existence question, which is exactly Q-7601 /
issue #58.

## Proof

### L-6100 (classical; Terras 1976, Everett 1977)

For every `L >= 1` the map sending `n mod 2^L` to the parity word of `n` of length `L` is a
bijection from `Z/2^L Z` onto `{0,1}^L`. Moreover, if `w` has `k` ones then on the unique
class `r_w mod 2^L` realising `w` one has

```text
T^L(n) = ( 3^k n + kappa_w ) / 2^L
```

for an integer `kappa_w` depending only on `w`, computable by the recursion

```text
(alpha, beta, t) := (1, 0, 0)
for each letter b of w:
    if b = 1:  (alpha, beta) := (3 alpha, 3 beta + 2^t)
    t := t + 1
```

ending with `alpha = 3^k`, `beta = kappa_w`, `t = L`; and `r_w` is obtained by solving, at
each letter, `alpha n + beta = b * 2^t (mod 2^(t+1))`, which is uniquely solvable because
`alpha` is odd.

### Step 1: the six words are affine with the right constant

Each `W_i` has length 19 and 12 ones, so `L-6100` gives
`T^19(n) = (3^12 n + kappa_i)/2^19` on one class `r_i mod 2^19`. Running the recursion:

| `i` | `W_i` | `kappa_i` | `35765 + 6 a_i` | `r_i mod 2^19` |
|---|---|---|---|---|
| 0 | `1101101101101101010` | 1412021 | 1412021 | 196603 |
| 1 | `1101101101101010110` | 1584053 | 1584053 | 417787 |
| 2 | `1101101101010110110` | 1777589 | 1777589 | 11259  |
| 3 | `1101101010110110110` | 1995317 | 1995317 | 209275 |
| 4 | `1101010110110110110` | 2240261 | 2240261 | 38827  |
| 5 | `1010110110110110110` | 2515823 | 2515823 | 174753 |

(reproduced by `experiments/X-6110-six-branch-least-root/crosswalk_proof.py`).

So `kappa_i = 35765 + 6 a_i = 5(P - Q) + 6 a_i` for all six branches, since `P - Q = 7153`
and `5 * 7153 = 35765`.

### Step 2: the affine identity is exactly the chart step

Put `n = 6x - 5`. Then

```text
( P n + kappa_i ) / Q = ( P(6x-5) + 5(P-Q) + 6 a_i ) / Q
                      = ( 6 P x - 5 Q + 6 a_i ) / Q
                      = 6 (P x + a_i)/Q - 5
                      = 6 x' - 5 = phi(x'),
```

using `Q x' = P x + a_i`. This is an identity of rationals; it is an identity of integers
exactly when `Q | (P x + a_i)`, i.e. exactly when the chart step with digit `a_i` is legal.

### Step 3: the residue classes agree (in the direction that is used)

Legality with digit `a_i` says `P x + a_i = 0 (mod 2^19)`, i.e. `x = x_i := -a_i P^{-1}
(mod 2^19)`, a single class mod `2^19`. Reducing `n = 6x - 5` shows `n = 6 x_i - 5 (mod 2^19)`,
and the last two columns of the table confirm `6 x_i - 5 = r_i (mod 2^19)`. By `L-6100`,
every such `n` has parity word `W_i` and satisfies `T^19(n) = (P n + kappa_i)/2^19`, which by
Step 2 equals `phi(x')`.

Steps 1-3 give claims 1 and 2. Claim 3 is T-6102. Corollary A follows by induction on `N`;
Corollary B from `ceil(y) >= y`. `QED`

### Remark (the converse, stated exactly)

`x -> (6x-5) mod 2^19` is **two-to-one**, so Step 3 is an inclusion, not an equality of
classes, and the naive converse "parity word `W_i` implies chart-legal" is **false**. The two
classes mapping onto `r_i` are `x = x_i` and `x = x_i + 2^18 (mod 2^19)`; only the first is
legal. The second is nevertheless harmless, for a reason that can be proved:

> If `x = x_i + 2^18 (mod 2^19)` then `m := P x + a_i` satisfies `v_2(m) = 18`, so
> `T^19(6x-5) = 6m/2^19 - 5 = 3*(m/2^18) - 5` is an **even** integer.

Since every `W_j` begins with the letter `1`, such an `n` cannot continue with a further
block. Hence:

**Converse.** If `n = 1 (mod 6)` and the parity word of `n` of length `19N` equals
`W_{i_0} ... W_{i_{N-1}}` and the `(19N+1)`-st parity letter is `1`, then `x = (n+5)/6` is
chart-legal for `N` steps with digit word `i_0...i_{N-1}`. In particular an infinite parity
word that is an infinite concatenation of blocks from `{W_0,...,W_5}` is realised only by
chart-legal `x`.

Verified numerically for all six branches (`converse.py`): the shifted class realises `W_i`
and lands on an even number in every case.

## Dependency audit

* `L-6100` is classical and is *also* re-derived from scratch inside the certificate script
  (the recursion is implemented directly, not imported), so no unverified dependency remains.
* No dependency on PR #45, PR #50, PR #57 or any other in-flight branch. The chart constants
  were taken from issue #58 and re-verified independently.

## Gap audit

* *Finite-to-infinite*: Corollary A is a statement about finite `N` only. Corollary B assumes
  all-time legality as a hypothesis and does **not** assert that such an `x_0` exists. The
  existence question is open (C-6111) and is not touched here.
* *Boundary cases*: `x <= 0` is allowed in the theorem statement (the algebra is identical);
  only Corollary B needs `x_0 > 0`. For `x_0 > 0`, `n_0 = 6x_0 - 5 >= 1` and stays positive.
* *Direction of the equivalence*: Step 3 checks class equality in both directions, so no
  hidden one-sided inclusion.
* *Hidden circularity*: none; nothing here assumes anything about Collatz.
* *Symbolic-object-to-integer*: this theorem is precisely the step that is usually missing.
  It is complete here because both sides are congruence conditions mod `2^19` that were
  computed and compared explicitly.

## Adversarial tests

Independent end-to-end replay (`experiments/.../replay.py`), performed on the exact least
roots of X-6110:

* `m_6 = 49927377479016341945330731072`, word `345415`:
  `T^114(6 m_6 - 5)` equals `6 x_6 - 5`, the realised parity word equals the predicted
  concatenation `W_3 W_4 W_5 W_4 W_1 W_5`, and the orbit contains exactly 72 odd steps with
  growth ratio `1.084703 = (3^12/2^19)^6`.
* `m_9 = 274731072270742333628800865325991165013963264`, word `252541135`:
  `T^171(6 m_9 - 5) = 6 x_9 - 5`, exactly 108 odd steps, growth ratio
  `1.129708 = (3^12/2^19)^9`, predicted parity word matches.

These are real Collatz computations, not chart computations, and they are performed on
numbers far outside any range where the chart was designed.

## Remaining uncertainty

None on the theorem itself. The one judgement call is the phrase "strict subsystem":
6 words out of 31824 possible `(12,19)` macro-blocks, i.e. the chart is a `1 : 5304`
restriction of the already-thin full `12/19` block family. That ratio is stated exactly, so
no reader can mistake the chart's negative resolution for a Collatz result.

## Suggested next attack

The crosswalk is done and can be used freely. Everything now rests on existence: C-6111 and
X-6110. Do not spend further effort re-deriving physical replay for this chart.
