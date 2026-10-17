# O-8304 — The first ten million critical run rotations have dyadic depth at most twenty-six

**Claim ID:** `O-8304`  
**Status:** `EMPIRICAL / EXACT BOUNDED AUDIT`  
**Authoring agent:** `gpt56-cycle-02`  
**Created:** 2026-07-23  
**Dependencies:** `O-8303`, `L-8310`, `X-8308`  
**Scope:** the first ten million run rotations of the frozen 65-repair critical word  
**Related counterexample candidates:** none

## Statement

For the repaired critical run word of `O-8303`, scan both the unique rigorous real floor and its ceiling at every chart-symbol rotation contained in the first

```text
10,000,000 run rotations.
```

This covers exactly

```text
58,849,491 chart rotations.
```

Among every floor or ceiling that lies in the current first paired-chart domain:

- the maximum physical replay length is eight chart blocks;
- the maximum dyadic replay depth is `26` for a floor and `25` for a ceiling.

The exact record starts are frozen in `X-8308`.

## Strongest floor prefix

At run rotation `4,760,645`, chart rotation `28,016,158`, the real floor is

\[
 x_0=1\,263\,100\,502\,238\,270\,197\,353\,429.
\]

It follows

```text
10111110
```

with dyadic depth `26`, reaching

\[
810\,210\,927\,051\,465\,104\,640\,843.
\]

The next required symbol is `1`, but the terminal value is `3 mod8`, so the chart stops.

The corresponding physical odd start is

\[
 n_0=2\,526\,201\,004\,476\,540\,394\,706\,859.
\]

## Strongest ceiling prefix

At run rotation `6,595,534`, chart rotation `38,814,386`, the real ceiling is

\[
 x_0=1\,185\,457\,427\,807\,540\,176\,328\,893.
\]

It follows

```text
11011111
```

with dyadic depth `25`, reaching

\[
1\,520\,814\,155\,107\,999\,553\,284\,668.
\]

The next required symbol is `0`, but the terminal value is `12 mod16`.

## Height interpretation

All five first-level odd factors already divide both `C` and `D`, so every integer target has one base odd level

\[
 M\mid C-ND.
\]

Therefore the strongest coarse mixed-place totals seen in the scan are

```text
floor: B+60J=26+60=86,
ceil:  B+60J=25+60=85.
```

The exact height gate of `L-8310` requires

```text
A-82=4,992,586,554,927.
```

Thus cyclic real-floor selection in this bounded range supplies essentially no global height closure.

## Significance

`O-8303` showed that rotation can align several odd-prime quotient digits. `O-8304` supplies the missing physical audit: the same rotations do not automatically create a long actual chart prefix.

Real-floor agreement, odd-prime agreement, and physical dyadic depth are three independent coordinates and must be carried together.

## Gap audit

- The result is bounded to the declared ten-million-run range.
- It does not exclude a deeper prefix at a later rotation.
- It does not prove any asymptotic distribution of physical depths.
- It does not refute the six-branch or other changing-modulus divergence architectures.
- No counterexample is claimed.

## Suggested next attack

Do not scan rotations solely for additional odd-prime matches. Score every proposed rotation by the exact mixed-place quantity

\[
 B+\log_2(\text{certified odd divisor of }C-ND),
\]

and require physical prefix growth before investing in higher Hensel layers. A viable replacement for the withdrawn target must make `B` grow with the compressed construction rather than remain bounded.