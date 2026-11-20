# Shifted multiplicative rank and effective cycle bounds

The [proof note](SHIFTED_RANK_COMPACTNESS.md) establishes a source-qualified
uniform bound for defect transitions whose shifted endpoints lie in a
fixed number of cosets of a bounded-rank multiplicative group. Combining
that count with an explicitly reconstructed classical cycle bound gives
a computable height ceiling for **all** positive cycles with that rank
and coset budget, without knowing the generators or their prime supports.
An elementary boundary also excludes every nontrivial positive cycle
whose shifted values have absolute multiplicative rank one.

The external inputs are Evertse--Schlickewei--Schmidt's general-rank
unit-equation theorem and Lagarias's explicit two-logarithm estimate.
The shifted equation is credited to PR161; fixed-local-minimum cycle
finiteness is classical. The note identifies the narrower addition and
the full-proof gap. There is no supplied ceiling on shifted rank for an
arbitrary fixed ordinary source; a family of explicitly certified
convergent inputs already has unbounded ranks as the source varies.

The [checker](check_shifted_rank.py) reconstructs exact algebra and
finite rank/coset tests, builds a depth-128 actual first-hit inverse
certificate, and rejects malformed or degenerate cases. Its frozen
[report](shifted-rank-report.json) records finite execution only.

```bash
python -X utf8 -B research/global-forcing-20261121/arithmetic/check_shifted_rank.py --check research/global-forcing-20261121/arithmetic/shifted-rank-report.json
python -X utf8 -OO -B research/global-forcing-20261121/arithmetic/check_shifted_rank.py --check research/global-forcing-20261121/arithmetic/shifted-rank-report.json
```

All failures use explicit exceptions and remain active with optimization.
No search through the enormous theoretical cycle ceiling was performed.
