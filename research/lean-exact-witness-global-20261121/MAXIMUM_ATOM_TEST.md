# Maximum-atom closing test: the exact boundary that remains

**2026-11-23. Written deduction; escape exclusion remains OPEN.**
This test combines the newly selected common pressure maximum with the
ordinary Riesz decomposition. It obtains a strict local row deficit, but
the full finite test retains a positive boundary term at every depth.
No new full-exclusion or Lean claim is made.

## 1. Sources and normalization

The refreshed external source is PR182 at full head
`b78819e95ee7d39f02022de991b42217821e7590`, specifically:

- `research/closure-round2-20261123/README.md`;
- `research/closure-round2-20261123/SOURCE_CLOSURE.md`, Sections 2--4;
- `research/closure-round2-20261123/ESCAPE_CLOSURE.md`, Sections 2 and 6.

Only these written files were read in this refresh. Their proof modules
and verification receipts were not audited in this test.
The local decomposition is AE-P1--AE-P2 in
[ATOMIC_EXCLUSION_CONTINUATION.md](ATOMIC_EXCLUSION_CONTINUATION.md),
frozen at SHA256
`c4d2c2124f51d4cd8dd59e9169197da7a79d45b4f290d2379151185c501db16a`.

Let `O` be the positive odd integers prime to three, with accelerated map
`U(n)=(3n+1)/2^a(n)` and exact valuation `a(n)=v2(3n+1)`.
On a hypothetical escaping eventual-meeting component `E`, put

\[
\Lambda_k(n)=\prod_{j<k}\frac{3U^j(n)}{3U^j(n)+1},\quad
r(n)=\frac{\Lambda_\infty(n)}n,\quad
\mu_{E,s}=\sum_{n\in E}r(n)^s\delta_n\qquad(s>1).
\]

For this test restrict the inverse operator to ordinary roots `q in O`:
`P_s f(q)=sum_(e:I_e(q) in O) (3/2^e)^s f(I_e(q))`,
where `I_e(q)=(2^e q-1)/3`. The cited positive product construction gives
`mu_(E,s) P_s=mu_(E,s)` and `0<r(n)<=1/n`.
The common maximum is therefore attained at an ordinary `m in E`.

## 2. A finite test retaining the same maximum atom

Write `M=r(m)`, `q_k=U^k(m)`, and let `A_k` be the sum of the first k
actual odd gaps, with `A_0=0`. Edge balance gives

\[
w_k:=\frac{3^k}{2^{A_k}}=\frac{M}{r(q_k)},\qquad
w_0=1,\qquad w_k>1\quad(k>0).
\tag{MA1}
\]

The last strict inequality is the common-root forward conclusion. All
`q_k` are distinct because the component escapes. Define the finite test

\[
F_N=\sum_{k=0}^N w_k^s\mathbf1_{\{q_k\}}.
\]

Each ordinary source has exactly one ordinary forward root, so there is
the exact identity on `O`, before taking any limit,

\[
\boxed{P_sF_N=F_N-\mathbf1_{\{m\}}
       +w_{N+1}^s\mathbf1_{\{q_{N+1}\}}.}
\tag{MA2}
\]

Every displayed test has finite support and finite values. Integrating
against the actual finite component measure is legitimate and gives

\[
0=-M^s+w_{N+1}^s r(q_{N+1})^s=-M^s+M^s.
\tag{MA3}
\]

MA2 is not asserted on all of `Z_3^times`: the ternary-only operator also
sends singleton tests to nonordinary dyadic rational roots. Its ordinary
restriction is exactly the one needed for both atomic integrations here.

Thus the boundary term is exactly `M^s` at every depth, including at this
globally selected maximizer. The coefficient inequality `w_k>1` does not
make that term tend to zero.

## 3. The whole loss sum leaves precisely the same atom

Let `lambda(n)=3n/(3n+1)` and
`D_s=sum_(n in O) n^(-s)(1-lambda(n)^s) delta_n`.
The physical product relation is `w_k=q_k Lambda_k(m)/m`. Consequently

\[
D_s(\{q_k\})w_k^s
=m^{-s}\bigl(\Lambda_k(m)^s-\Lambda_{k+1}(m)^s\bigr).
\]

Summing this positive telescope, with no exchange of divergent integrals,
gives

\[
\boxed{\sum_{k\ge0}D_s(\{q_k\})w_k^s=m^{-s}-M^s,
\qquad R_s(\{m\})=M^s>0.}
\tag{MA4}
\]

Here `R_s` is the residual measure in AE-P1. Maximality has not changed
the portion retained after the complete ordinary-source loss summation.

## 4. Even the strict row deficit does not close the test

The common-root restrictions give `m mod36 in {7,19,23,31}`. Enumerating
the two legal exponent classes modulo six gives the exact table:

| `m mod36` | Legal `e mod6` | `P_1 1(m)` |
|---:|:---:|---:|
| 7 | 4, 0 | 5/21 |
| 19 | 2, 4 | 20/21 |
| 23 | 3, 5 | 10/21 |
| 31 | 2, 0 | 17/21 |

All legal branch weights `3/2^e` at m are below one. Hence
`P_s 1(m)<=P_1 1(m)<=20/21<1` for every `s>=1`.
However, the forward gap at m is one, and its contribution at `q_1` is

\[
(3/2)^s r(q_1)^s=M^s.
\tag{MA5}
\]

A row deficit at the largest atom is compatible with this left
eigenmeasure: the compensating branch weight transports the same atom
along its injective forward ray. Turning the local deficit into a maximum
principle, or discarding the boundary in MA3, would be unsupported.
The precise remaining closing obligation is an arithmetic contradiction
to the simultaneous path restrictions, or an additional estimate that
rules out this nonvanishing original-source boundary.
