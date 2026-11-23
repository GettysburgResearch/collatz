# Independent review: fixed-source prefix arithmetic

23 November 2026. **VERIFIED, at the narrow written mathematical scope
specified below.** Reviewer lane: `risk26_triadic_construction`.

## Frozen objects

| Object | Frozen SHA256 |
|---|---|
| `../endpoint/FIXED_SOURCE_PREFIX_SHADOWS.md` | `b81ea465055a95621afa5b0221facab52400fcc660a1a70308849d0a00aa0e5a` |
| `../endpoint/FixedSourcePrefixGcd.lean` | `c7865b8483ab131a3c0387927ccd1b08a947bdf45ab2653094015725422005e6` |

The files were read from
`/workspace/scratch/957bb0caa6f2/risk26/endpoint/` and their hashes were
independently recomputed. This review reconstructs the mathematics of
all six Lean declarations and the note's (F1)--(F13). Compilation and
axiom-output replay are separate root-lane checks; this reviewer did not
run either and does not relabel the written asymptotic statements as
Lean theorems.

## 1. Complete gcd and actual-edge induction

The general affine identity is `u q = v p + c`, with `gcd(u,v)=1`.
Independently expanding it gives

\[
 c=u(q-p)+(u-v)p,\qquad \gcd(u,u-v)=1.
\]

Therefore

\[
 \gcd(c,u-v)=\gcd(u(q-p),u-v)=\gcd(q-p,u-v).
\]

This is an exact identity for the full gcd, including signed `p,q,c`
and signed or zero `u-v`. It is not merely a bound on selected prime
factors. The gcd divides `q-p`. Its positive-size bound by `|q-p|`
correctly requires `q != p`; that premise is present in both relevant
Lean statements and in (F3).

For `u=2^A` and `v=3^N`, the coprimality premise is unconditional. The
Lean specialization uses integer subtraction, so no truncated natural
subtraction changes the claimed denominator.

For the actual accelerated edges

\[
 2^{a_j}q_{j+1}=3q_j+1,
\]

the recursively defined clock and carry are

\[
 A_0=C_0=0,\qquad A_{j+1}=A_j+a_j,\qquad
 C_{j+1}=3C_j+2^{A_j}.
\]

Multiplying the edge at `j` by `2^{A_j}`, then inserting the induction
hypothesis, gives

\[
 2^{A_{j+1}}q_{j+1}
 =3(3^jp+C_j)+2^{A_j}
 =3^{j+1}p+C_{j+1}.
\]

This verifies the actual-edge induction and the final all-prefix gcd
theorem. There is no replacement by an independently selected source at
each horizon. The Lean hypotheses are intentionally more general than
positive odd Collatz states; the application supplies those additional
properties where the written later argument uses them.

## 2. Positive normalization, height, and approximation exponent

For the actual positive odd orbit, `a_j>=1`. For `N>=1`, `C_N` is odd
and prime to `3`, while `D_N=2^{A_N}-3^N` is odd, prime to `3`, and
nonzero. The primitivity and absolute-value assertions in the note are
therefore justified.

Write

\[
 E_N=\frac{2^{A_N}q_N}{3^N}=p+\frac{C_N}{3^N}.
\]

The exact edge recurrence gives both

\[
 E_{N+1}-E_N=\frac{2^{A_N}}{3^{N+1}},\qquad
 \frac{E_{N+1}}{E_N}=1+\frac1{3q_N}.
\]

The explicit reciprocal hypothesis (FC) therefore implies a finite
limit `E_infinity>p`. Actual escape gives `q_N -> infinity`, whence
`2^{A_N}/3^N=E_N/q_N -> 0`. This proves the three limits in (F5) and
the negative real limit of the periodic shadows in (F6).

Separately, exact subtraction gives

\[
 z_N-p=\frac{2^{A_N}(q_N-p)}{D_N}.
\]

Since `D_N` is odd, this is exactly the binary norm in (F7), which
tends to zero because `A_N>=N`. Different real and binary limits are
properly kept in their distinct completions.

Under the separately stated critical-clock hypothesis (CR),
`log q_N=o(N)`. The exact gcd bound then gives `log g_N=o(N)`.
Since `|D_N|/3^N -> 1` and `C_N/3^N -> E_infinity-p>0`, both the
reduced denominator and rational height have logarithm
`N log 3 + o(N)`, as asserted in (F9). No estimate on the smallness of
a linear form in `log 2` and `log 3` is inserted.

Finally, for the nonzero integer `q_N-p`,

\[
 0\le v_2(q_N-p)\log2\le\log|q_N-p|=o(N).
\]

Combining this with the exact binary norm proves the approximation
exponent one in (F10). If (CR) is known only on selected horizons,
these conclusions hold on those horizons; the note retains that
restriction explicitly.

## 3. Exact local products

Take the primitive integer vector `x_N=(X_N,Y_N)=(3^N,C_N)`.

For (F11), the real factor is
`3^N 2^{A_N} q_N`. The binary factor is exactly `2^{-A_N}`, since
`q_N` is odd, and the ternary factor is `3^{-N}`. Their product is
exactly `q_N>=1`. The fixed source `p` appears in the same forms at
every horizon.

For (F12), put `alpha=E_infinity-p`. The real factor is now

\[
 |X_N(\alpha X_N-Y_N)|_\infty
 =3^{2N}(E_\infty-E_N).
\]

Multiplying by the unchanged binary and ternary factors gives

\[
 \mathcal P_N=\frac{3^N}{2^{A_N}}(E_\infty-E_N).
\]

Summing the exact positive increments from (F4) yields

\[
 \mathcal P_N
 =\sum_{j\ge0}\frac{2^{A_{N+j}-A_N}}{3^{j+1}}
 =q_N\left(\frac{E_\infty}{E_N}-1\right)
 \ge\frac13.
\]

Every factor and exponent agrees with the note. The first future
correction supplies the lower bound. The warning that algebraicity of
`alpha` is itself unproved is necessary and correctly stated. Even if
it were supplied, these exact local products could not tend to zero as
a fixed negative power of the vector height.

For (F13), after omitting `K` future increments, the first remaining
term has size

\[
 \frac{2^{A_{N+K}-A_N}}{3^{K+1}}
 \ge\frac{2^K}{3^{K+1}},
\]

because each actual gap is at least one. If `K=o(N)`, its logarithmic
cost is at most `log 3 + K log(3/2)=o(N)`. Under (F9), the scalar tail
therefore cannot satisfy a fixed saving `H(z_N)^{-epsilon}` at all
sufficiently large selected horizons. This conclusion is correctly
limited to the scalar tail. The note does not claim to have paid for
moving coefficients, denominator clearing, or more general changed
linear forms.

## Review boundary

The verdict covers the six finite Lean theorem statements as mathematics
and the written deductions (F1)--(F13) from their displayed hypotheses.
It does not independently certify the source theorem used to obtain
(FC), the separate iid repetition theorem, universal ordinary-source
genericity, or a stronger all-horizon version of (CR). It does not
exclude higher-dimensional encodings or alternative local forms.

No gap or correction is required in the reviewed statements. The result
does not construct a successful triadic witness and does not prove
Collatz convergence.
