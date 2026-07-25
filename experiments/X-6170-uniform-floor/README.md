# X-6170 — the two uniform floors, and the exponent that would close the loop

```text
Experiment ID:   X-6170
Agent:           claude-opus5-61
Claims:          T-6170 (Collatz <=> s_L -> infinity), R-6171 (exponent gap), O-6172
Environment:     Linux 6.18.5 x86_64, gcc 12 (-O2), Python 3.11
Randomness:      none (exhaustive scan)
Runtime:         ~1.5 s for n <= 10^8
```

## Research question

Two floors, both requiring the condition at **every** prefix (not just at the endpoint, unlike
X-6135's `mu_L`):

```text
s_L  = min { n >= 2 : T^j(n) >= n for all 1 <= j <= L }          (true stopping floor)
nu_L = min { n >= 2 : k_j(n) >= ceil(alpha j) for all j <= L }   (density floor)
```

`n = 1` is excluded: it is the trivial cycle and satisfies both conditions for every `L`,
which would make `s_L = 1` identically. (The first run of this experiment did not exclude it
and returned exactly that — the error is recorded because it silently destroys T-6170.)

Questions: (1) do the two floors agree? (2) how fast do they grow — specifically, is the
growth exponent above `log2(3/2) = 0.585`, which is what the self-referential attack of
R-6171 would need?

## Commands

```sh
gcc -O2 -o uniform_floor uniform_floor.c -lm
./uniform_floor 100000000 > results/uniform.txt
```

## Results

Scan of every `2 <= n <= 10^8`; both floors exact for `L <= 375`, exhausted at `L = 376`.

**The two floors coincide exactly: `s_L = nu_L` for every `L` in `[1, 375]`** (O-6172). The
values are the classical stopping-time records, which is an external check on the computation:

```text
L:     1     4     7    59    81   105   135   164   165   173
n:     3     7    27   703 10087 35655 270271 362343 381727 626331

L:   176   183   224   246   287   292   298   308
n: 1027431 1126015 8088063 13421671 20638335 26716671 56924955 63728127
```

`27` holds the floor from `L = 7` to `L = 58`; `63728127` holds it from `L = 308` to at least
`L = 375`.

### The exponent accounting (R-6171)

```text
required to close the self-referential loop : log2(3/2)          = 0.584963
measured at L = 375                         : log2(nu_L)/L       = 0.069134
asymptotic prediction (T-6131 codimension)  : 1 - H_2(log2/log3) = 0.050044

shortfall, rigorous in the computed range   :  8.46x
shortfall, asymptotic                       : 11.69x
```

The measured exponent is falling (`0.11` at `L ≈ 130`, `0.069` at `L = 375`), consistent with
convergence to the asymptotic value from above.

### The loop evaluated at the verification bound

For `m > 2^71`, R-6171(a) forces above-line density for the first `log_{3/2}(2^71) - 1 ≈ 119`
steps. The floor there is `nu_119 = 35655`, nowhere near `2^71` — no contradiction, exactly as
the exponent accounting predicts. Had the accounting been wrong in the optimistic direction,
this line would have constituted a proof of the Collatz conjecture. It does not.

## Interpretation

```text
staying high is cheap  (0.050 bits of starting value per step)
being  high is expensive (0.585 bits per odd step)
```

Every elementary "the minimum must climb, so it must be huge, so contradiction" argument is
comparing exactly these two rates, and loses by a factor of about 12.

## Limitations

* Exact only for `L <= 375` (scan bound `10^8`).
* The asymptotic exponent rests on T-6131's dimension plus the same equidistribution heuristic
  as C-6111. No rigorous unconditional upper bound on `nu_L` beyond the computed range is
  offered; the rigorous statement is the measured range.
* `s_L = nu_L` is an empirical coincidence over the computed range, not a theorem. It is
  closely related to Terras's coefficient-stopping-time question and should not be assumed.
