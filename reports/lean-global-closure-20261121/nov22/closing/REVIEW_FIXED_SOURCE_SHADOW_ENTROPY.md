# Scoped independent review: fixed-source periodic shadows

Reviewer: `/root/arithmetic_closure22`.
Date: 2026-11-22. **Outcome: PASS within the scope below.**

Reviewed file:
`stepback22/entropy/FIXED_SOURCE_SHADOW_ENTROPY.md`.

Frozen SHA256:
`b61ec8fc7b1de66b58ca2355b604d1e9fb43387e251e1e0d42e2158dfba6f2db`.

The review independently reconstructed Sections 1–2, with particular focus
on equations (3)–(7). It did not independently audit the external papers,
the symbolic construction in Section 4, or a Lean formalization.

For the actual source prefix `uv`, substitution gives exactly

\[
Dx_0-Z=(2^b-3^q)(3^px_0+C(u))-2^aC(v)
      =2^{a+b}(x_a-x_{a+b}).
\]

The original ordinary integer \(x_0\) remains fixed. The denominator
\(D=3^p(2^b-3^q)\) is odd and nonzero because \(b>0\); this includes
the all-zero period case \(q=0\). Hence matching \(L\) parity bits
gives the claimed integer divisibility. Non-eventual periodicity makes
\(x_a-x_{a+b}\ne0\), so its absolute value is at least
\(2^{L-(a+b)}\). No positivity of the rational shadow is required.

Both sign cases of \(2^b-3^q\) give \(|Z|\le3^{a+b}\) from the
displayed correction bound; also \(|D|\le3^{a+b}\). Therefore
\(2^L\le(x_0+1)3^{a+b}\) follows with the actual original source
factor retained.

Finally, \(|x_a-x_N|\le H_N\) gives the height-dependent inequality.
The elementary bound \(x_{j+1}+1\le(3/2)(x_j+1)\) yields the stated
universal height envelope. For shadow scales \(N\to\infty\), division
by \(N\) and the definition of the height limsup give equation (7).

No mathematical correction was requested in this reviewed scope. The
absence of an entropy-to-repetition bridge is correctly retained as an
unproved closing step, rather than inferred from these inequalities.
