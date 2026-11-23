# Independent review of the same-maximum binary gate

23 November 2026. Reviewer: `density_free_germ8`.

**Verdict: PASS for R9-M1 with its stated source-qualified input.**
The selected pressure maximum stays fixed throughout the argument.
The gate does not exclude the denominator-eight phase or cover a
denominator with an uncleared power of three.

## Exact binding

Parent: `6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.
The following paths are under
`research/scalar-rigidity-round9-20261123/`.

| File | Git blob | SHA256 |
| --- | --- | --- |
| `MAXIMUM_GATE.md` | `2b2b2613d17c1881c05b5335738be9c33060d998` | `e5f587c59d0277f3a4cce67771a812dfd3a84dbf56597820df4a673911215ff9` |
| `MaximumGate.lean` | `d53fe8111cae3f2a4d49e8cd7432b1af87222c53` | `812cb007aec7ddc494198153721026e56a11dada5f5ad8db18e9eadd92ff54aa` |
| `CARRY_RETURN.md` | `0b0d2ff63339522689f9984aad1bae3ab63d9e08` | `6392e987c4b384a9c5992841005fa0e9dbd7840283a5f7785dc1f3e890ca6618` |

The pressure input is the parent's
`research/repo-synthesis-round8-20261123/PRESSURE_CONSTRUCTION.md`,
R8-P5, blob `7ef222d23f59a2dffd936dbfa93765df064db166`, with
the same escaping-component source qualification pinned in the note.
This review does not supply that escaping component or its product.

## Independent reconstruction

At the selected maximum, the actual scalar lies strictly between
one half and the pressure ceiling. With reduced denominator exactly
eight, the only possible value in that interval is `5/8`. Its actual
first gap must be one, since any larger positive gap would violate
the strict scalar lower bound at the next ordinary state. Thus the
same actual successor n has scalar `7/8` and satisfies
`n+7=3(m+5)/2`.

I checked the particular R9-C2--R9-C3 inputs used here. For an actual
denominator-eight tail, every high state has scalar at least `13/8`.
The potential `W=q/2^h` is bounded below by one half and contracts
by a factor smaller than one half on each transition from a high
state. This forces the first high excursion to end. On a low `7/8`
state, an unpaid `(2,1)` pair decreases `v_2(q+7)` by three. The
possible terminal exponents two and three violate the actual scalar
lower bound, whereas exponent one forces entry into a high state.
Consequently exactly t unpaid pairs occur and `v_2(n+7)=3t+1`.

For the normalized first paid excursion, both endpoint carries are
zero. Summing its complete carry equations over `2 ell` steps gives
`Gamma=3ell+2K`. If `ell=1`, the single interior carry is one.
If `ell>=2`, first-return minimality gives at least `2ell-2` positive
interior carries, including the possibility of the forced final
normalization step. Therefore `Gamma>=5ell` in every case.

The full prefix measured from m has exactly `1+2t+2ell` odd steps
and clock `1+3t+Gamma`. Applying the pressure inequality to this
prefix, without selecting a new maximum, gives the ratio in (5).
For `t<=7` and `ell>=1`, its lower bound is
`2^27/3^17=134217728/129140163>1`, contradicting that inequality.
Thus `t>=8`. The successor identity shifts the binary valuation by
one, yielding `v_2(m+5)=3t+2>=26` and `m>=2^26-5`.
Rearranging the same positive ratio gives the general relation (7).

I separately replayed the exact seven-pair rational comparison and
the stated decimal ceiling using the parent's 40-term rational tail
bound. That upper bound is
`114040910592111046952/182364981885853932015`, strictly below
`625344347433389/10^15`. The proof of the denominator choice also
works with the parent's weaker exact bound `152/243<3/4`.

## Formal scope and remaining boundary

The inspected Lean source has five public arithmetic declarations:
`coefficient_identity`, `seven_pair_obstruction`,
`rational_return_gate`, `complete_clock_gate`, and
`shifted_valuation_gate`. Their hypotheses retain the complete clock
bound and the positive excursion length. They prove exactly the
rational power comparison and the resulting natural-number gate.
Fresh compilation and dependency-audit receipts are owned by root;
this review inspected the source and does not claim a separate
compilation run.

No least scalar source is substituted for the pressure maximum.
The stronger least-source constraint in the companion return note
belongs to a different selection and is correctly kept separate.
Clearing a denominator `8*3^r` would move the ordinary source, so
the same-maximum corollary correctly requires `r=0`. Longer initial
low runs can satisfy the necessary inequality; the review does not
turn the gate into a universal contradiction.
