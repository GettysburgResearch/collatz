# Actual three-ray returns

**PROPOSED: elementary, unconditional partial results. Collatz remains open.**

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Write `a ~ b` when the two ordinary forward paths meet at independent finite
clocks, and write `C(n)` for `n ~ 3n`. The source-qualified motivation is
PR #146, commit `561d48a4d3a793a59b1cdf0406062ae1a6d47515`,
`research/upper-bit-mergers/THREE_RAY.md`: universal `C(n)` is equivalent to
Collatz. None of the local results here needs that equivalence as an input.

[PROOF.md](PROOF.md) contains:

* **TR-001:** the exact grade condition for a uniform two-word certificate on
  a binary neighborhood of an already convergent three-ray pair;
* **TR-002:** any exact forward pullback from `(u,3u)` to `(m,3m)` has the same
  odd part as `m`, even with independent clocks;
* **TR-003:** explicit ordinary merger and return guards, including a return
  to a finite list of smaller three-ray obligations;
* **TR-004:** a bound on repeated expanding return blocks, and a lower bound
  on the factor complexity of any bounded-alphabet expanding return run.

The first unresolved step is a complete, terminating selector for a fixed
ordinary input. Some residue classes do not enter these return guards.
Within the guarded family, arbitrarily varying expanding returns are not
excluded. An exclusion of fixed or periodic return schedules is not an
exclusion of such aperiodic runs.

Replay the finite arithmetic checks with:

```sh
python -X utf8 -B research/focused-forward-20261120/three-ray/check.py
```

The checker verifies actual path endpoints, independently enumerates grade
identities, constructs ordinary witnesses for arbitrarily prescribed tested
finite return schedules, and checks the divisibility statements. Its finite
ranges neither prove the general algebra nor close the all-input problem.
