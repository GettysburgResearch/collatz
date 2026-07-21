# KTHM-0006 — Transcendence of `log_64 81`

**Source:** Gelfond–Schneider theorem; standard exposition in Niven. [@Niven1956]  
**Proof status:** black-box use of Gelfond–Schneider, complete corollary proof  
**Maps to:** transcendental-slope component of `CLAUDE/T-0003` and substitution-frequency discussions

## Black-box theorem

If `α` is algebraic with `α≠0,1` and `β` is algebraic irrational, then every value of `α^β` is transcendental.

## Corollary

The real number

\[
\beta=\log_{64}81
\]

is transcendental.

More generally, if `a,b,c,d∈Q`, `ad-bc≠0`, and `cβ+d≠0`, then

\[
\frac{a\beta+b}{c\beta+d}
\]

is transcendental.

## Proof

The number `β` is not rational: an equality `β=p/q` would imply `64^p=81^q`, contradicting unique factorization into powers of `2` and `3`.

If `β` were algebraic irrational, Gelfond–Schneider would make `64^β` transcendental. But `64^β=81` is algebraic. Thus `β` is transcendental.

For the second statement, suppose the displayed Möbius transform were algebraic. Solving for `β` expresses it as a rational function of that algebraic number, hence algebraic, a contradiction. ∎

## Scope limitation

The theorem proves transcendence of a numerical slope. To exclude a proposed grammar, one must separately prove that the grammar's limiting frequency is algebraic or rational and that the limit exists.
