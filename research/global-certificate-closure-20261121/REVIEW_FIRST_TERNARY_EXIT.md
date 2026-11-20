# Independent review of the first ternary exit

**Verdict: PASS for the scoped first-exit lemma and the displayed c=3
embedding.** No claim that an actual counterexample exists, or that a
different adaptive construction must fail, is certified here.

## Frozen inputs

| Input | SHA-256 |
|---|---|
| `FIRST_TERNARY_EXIT.md` | `1fda081599f16e94f6c3c2692fea949864ca4a9b0aa91a01b42b1860112ffe06` |
| `check_first_ternary_exit.py` | `26790b8c8250b3cc97352090e649ea3d4c5a0f2970552fb696af0647c548cf06` |

No source files were modified. PR169's two bypass domains were also read
directly at `6cb9bfdc828f91576066b0e4a099d47d8144e915`,
`research/certificate-renewal-20261121/C5_CERTIFIED_BYPASSES.md`.

## Infinite exponent classes

For every fixed \(h\ge0\), put \(\eta=h+5\). The identity
\(\nu_3(2^{162}-1)=5\), and its elementary lifting by successive
cubing, show that \(2^{162}\) has exact order \(3^{h+2}\) modulo
\(3^{\eta+2}\). Its powers therefore exhaust the subgroup congruent to
1 modulo \(3^5\). Multiplying by \(2^{119}\) exhausts exactly the
required coset.

The prescribed value
\((11+3^\eta d)/4\), with \(d=2\cdot4^{-h}\pmod9\), lies in that
coset. Hence it determines one exponent class of period
\(162\cdot3^{h+2}=2\cdot3^{\eta+1}\). Its nonzero ternary digit
forces the valuation to be exactly \(\eta\), not just at least
\(\eta\). Every positive representative is an actual ordinary power of
two and yields the stated positive odd unit \(D\). This proves infinitely
many actual sources at every prescribed depth. The example
\(e=767\pmod{13122}\) has exactly \(\eta=7\) and \(D=8\pmod9\).

## Witness provenance, height, and domains

The original source has the exact first-hit word
\((2,2,2,5,e-1)\). Prepending \(h\) exponent-two inverses gives a
complete first-hit witness for \(A_h\), with rank \(h+5\), while the
paired lower remains in the same Mersenne component. These are actual
positive odd operations.

The first lower \(I_1\) exit is legal exactly when \(D=2\pmod3\),
and it satisfies \(Z=A_h/3\) and \(U(Z)=B_h\). The repayment identity

\[
3((2Z-1)-X)=256D(2\cdot4^h-3^{h+1})-4
\]

is exact. Its sign is negative for \(h=0,1\) and positive for every
\(h\ge2\); the recurrence in the source proves the entire latter
range. Independently of height, \(Z=171\pmod{256}\) misses all three
eligible lower residues. The known source certificate belongs to
\(A_h=3Z\), and cannot be reassigned to \(2Z-1\).

Under the prescribed digit condition, \(9\mid A_h\), so \(3\mid Z\).
Thus \(2^aZ-1=-1\pmod3\) for every \(a\ge1\), proving the claimed
absence of every odd inverse. This does not exclude other earlier
branches or ordinary forward excursions.

The two cited PR169 integrality guards both require the original index
\(k=1\pmod3\); on \(k=2\cdot3^hD\), that requires \(h=0\).
After all \(h\ge1\) inverse expansions, the new standard-pair index is
divisible by eight and misses the bypasses' binary class
\(14\pmod{32}\). These are necessary-domain obstructions, not claims
that \(h=0\) alone is sufficient for either bypass.

## Source-specific c=3 embedding

The value \(r_0=(2^{e+1}-1)/9\) has the stated provenance in both
physical-five phases. Its ordinary path reaches \(2^{e-1}+1\), then
\(3^{(e-1)/2}+1<X/176106\). Its certification therefore retains the
same least-failure premise and pinned H2 dependency.

For \(\eta\ge6\), the exact congruence is \(r_0=41\pmod{81}\),
and

\[
\widehat X=(X+2)/3<X,\qquad \widehat k=k/3.
\]

The new index is positive and eligible. Its internal block is exactly
\((a,e_{\rm block})=(3,1)\). A direct ordinary merger checks this solved
case: the words \((1,1,2,2)\) from \(r_0\) and \((1,1,1,4)\) from
\(2r_0+1\) have the same endpoint. The bad Mersenne predecessor instead
is \(4r_0-1\), with word \((1,2)\) to \(2^e-1\). Those are different
targets. The source correctly makes no smaller-failure claim from the
solved c=3 comparison. At \(\eta=5\), the displayed c=3 source is not
integral, so the guard cannot be removed.

## Independent executable evidence

`review_first_ternary_exit.py` reads only files alongside itself and
prints complete deterministic JSON. It imports no author checker
functions. It uses unique ternary-digit lifting, rather than the author's
linear search, and reconstructs the complete upper certificates backwards
from 1. It checks 31 modular depth classes and 12 actual certified sources,
including two representatives in each of six classes and both physical-five
provenance phases. It also checks the c=3 guard rejection at depth zero
and the explicit direct merger at positive depths.

Normal and `-OO` executions agree byte for byte with
`first_ternary_exit_independent_expected.json`, whose SHA-256 is

```text
b3dd5627d48fc00423bc87d43c826d61c5ebee6bb9b6693f335040ba2f9cd3ad
```

The independent checker SHA-256 is

```text
ded2de6dec39d7e328d16882d9ed92f9fb2dfc0c9e5f44c5d235a0f461d9068e
```

The author's checker was independently run in normal and `-OO` modes;
both passed with identical output. Infinite claims rest on the order,
congruence, affine, and sign arguments above. Neither replay establishes
nonconvergence of a target or excludes an unbounded adaptive construction.
