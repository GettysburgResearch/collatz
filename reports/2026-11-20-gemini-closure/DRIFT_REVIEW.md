# Narrow review: a fixed input's whole-source drift changes sign

## Frozen review boundary

The reviewed final repository files are:

| Path, relative to the repository root | SHA-256 |
|---|---|
| `research/gemini-global-closure-20261120/FIXED_SOURCE_DRIFT.md` | `64e6e22f7a32bf975107c75158b4719af8aa7ff21b12ac35c307600603f74d98` |
| `research/gemini-global-closure-20261120/check_transported_drift.py` | `2a6aac718e199a3660a9c4d5b6b3c45107a045f916688fd95b9bbd59a2fb3312` |

The final publisher receipt at
`reports/2026-11-20-gemini-closure/drift-receipt.json` has SHA-256
`42cbe571aea112d959a0aa70d450ca3b3d29882922f50c69d6759c9158aef685`.
I reproduced this complete final-root receipt, including its embedded
document and checker hashes, from the final repository files listed above.
The final document differs from the reviewed author draft only by making
the domain wording explicitly unsafe, giving the root-relative run command,
and linking the publisher's receipt.

**Verdict: VERIFIED for FD-001 and the stated source-tail, covariance, and
gauge identities**, conditional on the A/R interfaces and additive return
bound frozen in the preceding transport packet. This is a narrow
mathematical and computational review, not a proof of all-time decay,
cycle exclusion, or Collatz. The reviewer is a separate agent from the
sign-certificate author and independently reconstructed the tail analysis,
interval semantics, and selected physical trajectories.

The input under review is exactly

```
f0(u) = 1_U(u) / [u(u+1)].
```

It is not `1_U/R(u)^2`, and it is not renormalized after transport.

## 1. Every omitted original source is bounded

For `m=M+1`, the mass above source M is at most `1/m` by telescoping.
With `g(x)=1+log log(x^2+6)`, the rank upper bound gives
`psi(u)<=g(u)`. Summation by parts yields exactly

```
sum_(n>=m) g(n)/[n(n+1)]
 = g(m)/m + sum_(n>m) [g(n)-g(n-1)]/n.
```

Since `g'(x)<=1/[x log x]` and `1/n<=1/x` on `[n-1,n]`, the second
term is at most `1/[m log m]`. This verifies the source psi-tail bound
`S(M)` without a claim about fresh or stationary endpoint distributions.

For a surviving original atom u, its drift at return j is bounded above
by `log 6` and below by `-psi(B^j u)`. Killed atoms contribute zero at
later returns; an atom killed on the next return contributes the negative
of its current psi-value. Applying the actual additive return bound
therefore gives the complete signed tail interval

```
[-S(M)-j log(6)/m,  log(6)/m].
```

The two sides have the correct asymmetric signs. Using the upper
increment alone to bound the negative tail would have been invalid;
the implementation retains the full current-energy lower bound.

## 2. The integer intervals enclose the quantities actually computed

For `0<=z<=1/3`, the 32 retained terms of the positive atanh series have
remainder at most `9/[4*65*3^65]`. The code floors every positive lower
product and division and ceilings every positive upper product and
division. Binary range reduction writes a positive log argument at least
one as `2^k y`, with nonnegative k and `1<=y<2`, so combining the enclosed
`log 2` with the atanh part preserves the interval direction.

The nested logarithm uses monotonicity: its lower argument is the
enclosed inner lower endpoint, and its upper argument is the enclosed
inner upper endpoint. The inner logarithm is strictly above one on all
retained states. At absorption the code uses psi-value zero, as required
by killing, rather than applying the positive-state formula at 1.

The exact rational seed mass is enclosed at scale `10^32`. Merging adds
mass intervals without discarding correlations. For a signed drift,
the code takes the minimum and maximum of all four interval products;
it does not assume the drift is positive. Thus the interval summation
remains valid for the mixture of positive, negative, and killed terms.

I ran `python -O -B research/gemini-global-closure-20261120/check_transported_drift.py`
from the final repository root. Its entire parsed JSON output matched the
publisher receipt pinned above, including the final document hash `64e6e22f...`.
This final-root replay is distinct from an earlier author-folder replay
whose receipt contained the author draft's different document hash.
The checker's controls use explicit
exceptions, so removing Python assertions does not remove the gates.
The complete enclosures are:

```
D0 in [-0.209006853156, -0.188077839702],
D9 in [ 0.000132428698,  0.000217170924].
```

These are two whole-source signs. The calculation does not certify a
trend at unspecified times.

## 3. Independent reconstruction of contributing ordinary atoms

A separate implementation computed A by physically replaying its
maximal active words, and recomputed R from the finite envelope formula.
It then eliminated safe excursions to reconstruct B. Among the checked
original atoms were:

| Original u | Exact seed mass | B^9(u) | B^10(u) | R at the two endpoints |
|---:|---:|---:|---:|---:|
| 27 | `1/756` | 319 | 1822 | `1296, 370881` |
| 82 | `1/6806` | 319 | 1822 | `1296, 370881` |
| 55 | `1/3080` | 167 | 319 | `27556, 1296` |
| 31 | `1/992` | 1822 | 911 | `370881, 828100` |
| 63 | `1/4032` | 911 | 244 | `828100, 243` |
| 175 | `1/30800` | 23 | killed at 1 | `484, 0` |

The complete 27 path agrees with the certificate. The return
`167 -> 319` is not a single A step: `A(167)=283`,
`R(283)=9216`, and 283 is safe because
`4R(319)=5184<=9216`. Eliminating that actual safe step gives the
displayed B return. Also 1822 is unsafe: its next A endpoint is 911,
whose rank 828100 exceeds its current rank 370881. These checks verify
both a material safe-excursion boundary and the positive-drift edge.

The decimal explorations used to select these atoms were not used to
certify the sign of the full sum; that sign uses the frozen outward
interval calculation and the analytic tail above.

## 4. Covariance and long-horizon boundary

The centered term is correctly defined as

```
C_j = D_j - m_j (D0/m0)
    = m0 Cov_(f0/m0)(f_j/f0, d).
```

It is an unnormalized covariance. Integrability follows from the finite
actual psi-moments and `-psi(u)<=d(u)<=log 6`. Since `m0<=1/2` and D0
is negative, its mean satisfies `D0/m0<=2D0`. Combining the upper
negative bound for D0, the lower retained mass, and the lower bound for
D9 gives the claimed positive lower bound for C9. The sign directions
in this comparison are correct.

The triangular telescoping weights in equation (12) are
`(N-1-j)/N`, as obtained by counting the later energies containing Dj.
At the original-source split M=N, the omitted Cesaro energy is bounded
by `S(N)+(N-1)log(6)/[2(N+1)]`, which is O(1). Hence removing those
original sources preserves an `o(log log N)` target. It does not prove
the target for the remaining triangular array of actual histories.

Finally `n+5<=R(n)+6<=(n+5)^2` gives exactly
`0<=psi(n)-[1+log log(n+5)]<=log 2`. The resulting O(1) Cesaro
gauge difference is valid under killing and finite mass. It supplies
no further asymptotic saving by itself.

The certificate rigorously rejects reusing this initial negative drift
as though the transported density were unchanged. It leaves open
amortized cancellation, bounded correctors, other input measures, and
the full source-persistent occupation estimate.
