# Exact controls and the rational cancellation fixture

23 November 2026. These controls check finite identities and coverage;
they do not establish an arbitrary-source arithmetic germ or prove Collatz.

## A written all-order identity for the fixture

For the positive rational cycle `110000`, put

\[
J(t)=\frac{5+t}{9-(2+t)^6}=\sum_{j\ge0}c_jt^j,
\qquad q(t)=9-(2+t)^6=\sum_{i=0}^6q_it^i.
\]

Here `q_0=-55` has five-adic valuation one and `q_1=-192` is a five-adic
unit. Direct calculation gives `c_0=-1/11` and `c_1=181/605`, with
valuations zero and minus one respectively. For `j>=2`, the numerator
has no coefficient at that order, so

\[
q_0c_j=-\sum_{i=1}^{\min(6,j)}q_ic_{j-i}.
\]

Assume inductively `v_5(c_k)=-k` for `1<=k<j`. The `i=1` term has
valuation `-(j-1)`. Every other nonzero term has valuation at least
`-(j-2)`: its integer multiplier has nonnegative valuation, and the
`c_0` endpoint also has valuation zero. Thus the first term is the
unique term with smallest valuation. The sum has that valuation;
division by `q_0` gives `v_5(c_j)=-j`. Hence

\[
v_5(\operatorname{den}(c_j))=j\qquad(j\ge1).
\]

This elementary induction is a written proof for this one rational
fixture. It is not a new ordinary integer cycle and is not included
among the 17 Lean declarations. The replay separately checks orders
1 through 31 using exact rational coefficients.

## Reproducible finite execution

From the repository root:

```sh
python -X utf8 -B research/profound-round6-20261123/exact_replay.py
python -O -X utf8 -B research/profound-round6-20261123/exact_replay.py
```

No optional Python package is required. Every guard explicitly raises
an exception on failure, and both output objects bind the science and
executable input hashes. Normal and optimized outputs are byte-identical.

The cycle census keeps every chronological affine carry, the full
numerical denominator and its gcd, literal rational parity, complete
state return, and Taylor transport around the cycle. It enumerates
primitive words of length at most ten with at least one odd bit and
positive `2^A-3^p`; rotations are counted as separate words. The
nonzero remainder modulo `z^u-3^v` is calculated exactly. Observing all
1,269 reduced-prime instances in the first 12 coefficients is a finite
observation, not a claim of a universal 12-coefficient detection bound.

The ordinary-source controls follow the literal shortcut map to the
first hit of one, with a 10,000-step cap. They compare 32 coefficients
from reverse shortcut recurrences with direct translation of the full
prefix polynomial and the standard tail. The 131 distinct sources are
1 through 128 together with 6171, 77031, and 837799. Each tested
denominator divides the one common prefix power `3^s`.

Collision controls keep the complete ordered-pair list and independently
compare it with squared bucket counts. They check the full quotient
injection, all ordinary diagonal pairs, off-diagonal pairs, and exact
diagonal equality beyond the maximum source height. Rational finite
comparison vectors exercise the total-variation inequality with radicals
eliminated by exact squaring. These reference vectors are not asserted
to be stationary laws of the orbit.

The exact outputs and execution commands are in the
[round-six report](../../reports/2026-11-23-profound-round6/README.md).
