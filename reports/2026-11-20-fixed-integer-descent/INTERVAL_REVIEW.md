# Independent review of the translated recursive occupancy theorem

**Verdict: VERIFIED at the local claim level stated below.** This is a mathematical reconstruction and an independently implemented integer replay by a separate research agent. It is not proof-assistant verification, external peer review, a priority assessment, or a review of all surrounding research. No scientific file was edited by this reviewer.

## Frozen scope

The baseline is main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The present additions were reviewed by exact content hash before publication; the verdict applies to these bytes, not automatically to a later revision.

| Path | SHA-256 |
|---|---|
| `research/fixed-integer-descent/drift.md` | `d73a93d8a803996bde7b15f33e307d28385c8ffe2f9b99f449dfea35140c3338` |
| `experiments/fixed_integer_interval_bootstrap.py` | `2dc95673f0bc3689f06586740ddbe451fdc59fb31de54e3caefc2ca3a22d3fec` |
| `reports/2026-11-20-fixed-integer-descent/interval-bootstrap-report.json` | `1eafa6e36274d249978559b8835051362e3a7783dcbad762c48226b2b8c358d7` |

The reviewed mathematical target is **FID-DRIFT-005**, including its finite-simple-path input from FID-DRIFT-001, the strong-induction estimate for every exponent strictly above `H_2(log_3 2)`, and the conditional record-exponent substitutions. I inspected the record argument and the resident `research/astra-three-routes/pass3/FINITE_RECORDS.md` to check what hypotheses those substitutions retain. This report does not promote the resident packet's status or certify universal coefficient stopping.

## Reconstruction of the universal finite-path argument

The domain is one finite path of positive ordinary integers, with every listed state distinct. Removing its final `k` states leaves internal `k`-step images, and those images are distinct because the entire path is simple. If fewer than `k` states exist, the terminal cost alone is sufficient. No injectivity of `T^k` on all ordinary integers or on a predecessor basin is being asserted.

For a word with `q` odd inputs, exchanging the affine letters `10` for `01` increases the nonnegative remainder. Sorting the odd letters to the end gives the valid uniform bound

`0 <= E_w <= (3/2)^q - 1`.

This comparison is algebraic; the rearranged word need not be the physical word of the original source. It is used only to bound the affine constant. The high-odd-count contribution is a literal count of parity residue classes modulo `2^k`, each contributing at most `ceil(X/2^k)` points to an arbitrary translated integer interval.

For the low-odd-count images, let their real interval be `[A,B)`. Its length is

`D = 3^q X/2^k + (3/2)^q - 1`.

The printed integer width is exactly `L_q = ceil(D)`, including the case where `D` is an integer. The integer points of `[A,B)` range from `ceil(A)` through `ceil(B)-1`; the inequality

`ceil(B) - ceil(A) <= ceil(B-A)`

puts all of them in `[ceil(A), ceil(A)+L_q)`. Because `A>0`, the translated lower endpoint remains an integer at least one. There is no missing alignment unit. Replacing the ceiling by a floor is false already for `[1,3/2)`, which contains one integer although its width has floor zero.

All low-count images are states of the original simple path. Therefore an occupancy bound for that same path applies to their image interval. Different odd counts may produce overlapping image intervals; adding their upper bounds is still valid. The lengths are positive and nondecreasing with `q`, so `L_h<X` ensures that every recursive argument is strictly smaller than `X`.

This proves the strong-induction recurrence for `F`. The trivial fallback `X` handles every small width and every empty eligible menu. The menu `k=0,h=0` has child `X` itself, so it is correctly ineligible. The code omits `k=0` for precisely this harmless reason. The domination `F<=Bhat` is also valid: any one-pass menu whose value beats `X` already has `L_h<X`, and replacing its `L_q` summands by `F(L_q)<=L_q` cannot increase it.

## Reconstruction of the exponent bootstrap

For `H_2(log_3 2)<alpha<1`, continuity and monotonicity allow a choice

`1/2 < theta < log_3 2`, `H=H_2(theta)<alpha`, `u=theta log_2 3<1`.

At `k=floor(log_2 X)`, `h=floor(theta k)`, the high-count term is at most `2 X^H`, while `1<=L_q<=3*3^q`. The latter estimate includes the ceiling correctly, because the `-1` in the image width cancels the possible unit from taking its ceiling.

Writing `D_alpha=3^alpha/(1-3^(-alpha))`, the low-count induction terms sum geometrically to at most

`C_alpha D_alpha X^(alpha*u)`.

Choosing a finite cutoff with `3X^u<X` and `D_alpha X^(-alpha(1-u))<=1/2` makes this at most half the target `C_alpha X^alpha`. The remaining `k+2X^H` is at most `4X^alpha`, absorbed by the other half when `C_alpha>=8`. Choosing also `C_alpha>=X_0^(1-alpha)` covers every smaller width by the trivial bound. Thus the induction closes without assuming the conclusion at an equal or larger width, and without an unacknowledged logarithmic loss.

The claimed strict rational instance is correct. For `theta=200/317`, the integer inequality `3^200<2^317` gives `u<1`. Expanding the binary entropy shows that

`317^6340 < 2^6023 * 200^4000 * 117^2340`

is exactly the required `H_2(200/317)<19/20`. Both were evaluated with integer arithmetic. The resulting constant is finite and effective in principle, but it has not been computed here; the tiny strict margin does not justify a practical cutoff claim. The endpoint exponent itself is not asserted.

## Record consequences and scope limits

A strict coefficient record on a simple no-descent path has `C_i<=1` and consequently lies in the exact integer window `[n,n+floor(n(P_L-1))+1)`. Its source values are distinct, so replacing the elementary interval width by `F` is legitimate.

In the conditional finite clock, each supplied coefficient stop from a record source produces the next strict global record within the certified time. If no descent or repetition occurs, `F(W_n)+1` records contradict the occupancy bound. This uses the same all-source stopping certificate as before. It does not establish that the next crossing occurs without that certificate.

The exponent arithmetic checks exactly:

- `(39/40)*(19/20)=741/800` for the explicit source-window exponent.
- `(19/20)^2=361/400` for the qualified improved source window.

The written text keeps the inherited window inputs, unevaluated constants, coefficient-stopping premise, and repetition alternative explicit. I found no claim that this gives a basin-size bound, a universal Collatz running time, or a full proof. Those conclusions would not follow from the reviewed argument.

## Commands and independent replay

The following command was actually run from the repository root and passed against the frozen report:

```bash
python -X utf8 -B experiments/fixed_integer_interval_bootstrap.py --compare reports/2026-11-20-fixed-integer-descent/interval-bootstrap-report.json
```

The full recursive minimum is computed only for widths `1..4096`. The larger-width numbers `55681` at `100000` and `2841764210` at `10^10` are the separately identified restricted policy bounds: three selected recursive layers above the already available exact small-width table. They are not the full minima. The checker and manuscript label this distinction correctly.

I implemented the recurrence independently using `Fraction`, direct rational ceilings, and direct binomial-tail summation, without importing the author's width or recurrence functions. That reconstruction is preserved as [check_interval_independent.py](check_interval_independent.py); its execution report is [interval-review-report.json](interval-review-report.json).

The preserved command was actually run:

```bash
python -X utf8 -B reports/2026-11-20-fixed-integer-descent/check_interval_independent.py > reports/2026-11-20-fixed-integer-descent/interval-review-report.json
```

Do not repeat that redirection over the frozen report; for a further replay, run the script to stdout or redirect to a new path.

The independent run reconstructed all 4096 values and all **195322** eligible menus. Its table hash agrees byte-for-byte with the author's:

`52aaeeb4753255cc6b655a05f77c942b115ee04277487b41f7486c2e58b65dbb`.

It found **3308** widths where the recursive value strictly improves the one-pass minimum. It separately checked **114688** exact translated half-open image alignments, all positive widths and their monotonicity within the finite table, both integer exponent certificates, and both record-exponent products. Four controls preserve the omitted-ceiling, self-recursion, arbitrary-set, and repeated-cycle boundaries. The checks recover `F(128)=117` and `F(4096)=2565`.

| Independent artifact | SHA-256 |
|---|---|
| `check_interval_independent.py` | `24287a95cfd51b0090f4ea2c9afca013b504b1f2ccf730ce8806b645f8a93be1` |
| `interval-review-report.json` | `cd1f902091cb61a0c4f35d5099995735435b51cca46582e66551dd709d8d5685` |

**Required mathematical fixes:** none found in this frozen revision. The universal coverage and coefficient-stop obligations remain open exactly as stated in the source.
