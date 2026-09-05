# X-9876 — Period-four quotient audits

Experiment ID: `X-9876`  
Status: `EMPIRICAL` support for `PROPOSED` claims `L-9868`--`L-9875`  
Agent: `gpt56-synthesis-01`  
Environment: standard-library Python 3 and Node.js with `BigInt`

## Purpose and boundary

These scripts independently reconstruct exact polynomial, finite-field, carry,
and Taylor-jet identities used by the period-four proof packet. They audit
algebra and boundary cases; finite scans are not substitutes for universal
proofs. In particular, the `p=3` zero pattern is an empirical census, not a
classification theorem.

The files under `lib/` are frozen exact polynomial bases used by the JS
audits. Checkers load them relative to `__dirname`; no scratch paths are
required.

## Commands

Run from this directory:

```powershell
node check_q5_block_lucas_residual.js
python check_odd_prime_power_carry_gap.py
python check_q5_odd_taylor_two_jet.py
python check_general_composite_distinguished_block.py
node check_composite_value_descent.js
node check_composite_first_jet_descent.js
node check_composite_all_order_jet_descent.js
node check_dyadic_boundary_nonvanishing.js
node check_dyadic_cartier_kernel.js
node mine_p3_squarefree_composite.js 30 220
```

## Expected audit record

- odd two-jet: 1,257,510 tropical states, 4,873 tie states, 1,420 exact jets;
- distinguished composite block: 148,289 cases;
- value descent: 216 congruences and 704 finite-field reductions;
- first jet: 666 Gaussian, 270 residual, and 40 full-quotient states;
- candidate all-order lift: 176,851 integral coefficients and 218 exact
  instances through `Phi_m^3`;
- Cartier kernel: exact identities through `u=8`, 820 scalar states, and
  binary-cluster arithmetic;
- `p=3` census at `30 220`: 3,174 candidates, 3,158 multiplicity-zero and 16
  simple-zero cases, none of multiplicity at least two.

## Limitations

The candidate all-order checker reaches only the third cyclotomic power and
does not prove its arbitrary-order degree lemma. The `p=3` census has a finite
box. No script here constructs a Collatz counterexample.

