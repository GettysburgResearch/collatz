# X-ASTRA3-005: rank spectrum, induced mass, and switch repayment

**Finite exact support for proposed theorems; no complete Collatz proof.**
Read [the fifth-pass index](../../research/astra-three-routes/pass5/README.md).

Run from a checkout or from the unpacked packet root:

```bash
python -B experiments/X-ASTRA3-005-spectrum-switch/run.py \
  --check experiments/X-ASTRA3-005-spectrum-switch/results/canonical.json
python -O -B experiments/X-ASTRA3-005-spectrum-switch/verify.py \
  experiments/X-ASTRA3-005-spectrum-switch/results/canonical.json --self-test
```

The generator evaluates the four-entry rank formula, compiles rank sublevels
by ternary exponent and reduced numerator, evaluates A by affine arithmetic,
and searches all candidate witnesses forward. The verifier imports neither
the generator nor repository modules. It evaluates the whole increasing
dictionary until its numerator excludes every later entry, scans full source
ranges using the proved properness cap, executes literal shortcut steps, lifts
parities bit by bit, and reverses full finite trees for the merging comparison.

Both programs use the standard library and explicit exceptions, so disabling
Python assertions does not disable their validation. An optional `--output`
argument writes the reconstructed report. Both outputs are byte-identical.
The same author wrote both implementations: this is not independent review.

## Coverage and exact boundaries

- Nine complete rank sublevels M=4^j, 0<=j<=8. The largest contains 635 sources.
- All 16383 inputs 2<=n<=16384 for the A/rank/enlarged-safe interfaces.
  There are 13459 initially safe sources versus 10505 quarter-safe ones.
  Safe iteration sends 294 inputs to 1 and 16089 to an explicitly unsafe state.
- Six all-source mass intervals, r=0,1,2,4,8,16. Ordinary sources above 16384
  are enclosed by the proved 3/524288 tail, not declared convergent.
- Thirteen exact induced-weight obstruction cases, e=4,20,...,196.
- Forty-four ordinary sharp-family lifts, t=3,...,24 and two CRT lifts each.
- Twenty-eight general (a,b,k,t,ell) repayment cases with distinct modes.
- The exact n=103 wrong-next-mode counterexample.
- Ten complete bounded-clock merging tests, both shortcut clocks <=6.
  The lower-Phi candidate lists contain 2370 entries in total, with 109 merging
  diagrams across the specified tests. No cap-free completeness is claimed.
- Eight altered, resealed reports rejected: inflated scope, missing rank level,
  safe count, flat edge, analytic tail, spike endpoint, repayment rank and clock cap.

The finite checks validate implementations of the arithmetic interfaces.
All-parameter results and all-residence bounds are the written mathematical
arguments. A sampled zero survivor count does not remove its analytic tail.

Semantic report SHA-256:

    45888e331821905d73141de70258b9cbfc03df94ec58208a94b5d66f9d687aee

No external large computation, workflow, or publication action belongs to
these programs. The parent source files and previous certificates are untouched.
