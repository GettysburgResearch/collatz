# Closing attempts: one ordinary pressure maximum, full cycle cancellation, and pressure loss

**23 November 2026. Full Collatz remains open.** Three parallel attacks pursued
the remaining global steps after the updated unrestricted witness optimizer,
full-denominator cycle work, and ordinary atomic pressure construction.
This checkpoint adds a common-root reduction with no path-length cap, exact
numerical cancellation transport, and an original-source pressure-loss identity.
It does not prove that the two-sided root restrictions are inconsistent,
exclude all nontrivial cycles, or eliminate the retained escaping measure.

This continues PR182 from `aa12c13601cacec2c8496f1349b4947457dc1b45`.
The [source ledger](SOURCES.json) freezes the refreshed PR175, PR176, PR177,
PR178, PR180 and PR185 heads and the individual files actually used. The
[previous checkpoint](../high-variance-20261123/README.md) remains available.

## 1. One fixed ordinary root controls both directions

Let `E` be a hypothetical escaping component of positive odd integers prime
to three. Write `U(n)=(3n+1)/2^a(n)` for the accelerated odd map. The pinned
elementary orbit-count estimate gives a positive product

`Lambda(n) = product_(j>=0) 3U^j(n)/(3U^j(n)+1)`.

Put `r(n)=Lambda(n)/n`. Since `0<r(n)<=1/n`, this weight attains a maximum
at an actual ordinary root `m in E`. The same root maximizes every pressure
atom `r(n)^s`, independently of `s>1`.

The exact edge equation is `2^a(n) r(n)=3r(U(n))`. It yields opposite strict
coefficient inequalities at that **same root**, simultaneously:

| Actual path | Complete coefficient inequality |
|---|---|
| Every nonempty forward odd prefix from `m`, with `h` steps and total gap `A` | `2^A < 3^h` |
| Every nonempty positive odd unit inverse prefix ending at `m` | `3^h < 2^A` |

There is no depth cap, finite exponent alphabet, or changing choice of root.
Every positive odd-clock future state of `m` is strictly larger than `m`.
Its local residues satisfy `m mod36 in {7,19,23,31}`. The class `23` is
retained: its apparent incoming gap-one source is divisible by three and
does not belong to the stated unit domain.

If `m_0=min E`, the written orbit-count estimate sharpens the location to

`m_0 <= m <= m_0 exp((160/3) m_0^(-1/40))`.

Thus the bound on `m/m_0` tends to one as the component floor grows. This
does not identify `m` with the least global counterexample or decide
membership in `E`.

[SOURCE_CLOSURE.md](SOURCE_CLOSURE.md) proves the written application and
records the direct finite-graph attack. [TwoSidedPressure.lean](TwoSidedPressure.lean)
proves maximum attainment, the exact path telescope, and the common-root
conclusion from explicit positive-weight, `n*r(n)<=1`, and edge-balance
hypotheses. Its `GapPath` retains positive odd unit vertices and the physical
integer equation at every edge. The infinite-product construction and the
quantitative floor bound remain written proofs.

The attempted final inference failed at a concrete place. The pressure
operator preserves ordinary components. A test supported on the finite
graph of already known convergent orbits, or its inverse enlargement, is
zero on the escaping component and gives `0=0` there. An arithmetic
construction contradicting one of the two path inequalities is still needed.

## 2. Cancellation transport at the complete numerical denominator

For a chronological shortcut word `w` of length `A` and positive weight `p`,
keep its complete carry `C(w)` and positive denominator `D=2^A-3^p`.
For complete words `w=u 0^h 1 v` and `w'=u 1 0^h v`,

`C(w)-C(w') = 2^|u| 3^|v|_1 (2^h-1)`.

If `D` divides `C(w)`, then exactly

`gcd(D,C(w')) = gcd(D,2^h-1)`.

An adjacent exchange therefore gives a neighbor whose reduced denominator
is the full `D`. All numerical prime powers are retained. When `D=1`, the
neighbor remains integral; that exception is explicit.

[CycleCancellation.lean](CycleCancellation.lean) derives coprimality with two
and three from the word's own denominator and proves the complete transport
consumer. It imports the unchanged chronological carry definitions from
the previous checkpoint.

The [written cycle attack](CYCLE_CANCELLATION.md) then attempts two global
injections. Under `D>2*3^floor(A/2)`, the closed adjacent-exchange neighborhoods
of all zero-residue words are disjoint. Under `D>3^h`, each zero-residue word
is determined by the bits outside any fixed cyclic window of length `h`.
These deductions include the entire zero fibre. Their resulting bounds
remain too large to force `N_0(A,p)<A`, the cycle-exclusion target.

The full-quotient defect-polynomial calculation also keeps PR178's balanced
unit at the distinguished evaluation. The attempted application of
moving-target gcd theorems does not meet their fixed-dimension, fixed-degree
and coefficient-height requirements. No transcendence theorem is silently
assumed to remove numerical cancellation.

For the exact prior comparison, see PR175's
[zero-atom census at its frozen source](https://github.com/GettysburgResearch/collatz/blob/8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73/research/lean-global-closure-20261121/closing/ZERO_ATOM_CLOSING_ATTEMPT.md)
and PR176's
[full-denominator identity-atom target](https://github.com/GettysburgResearch/collatz/blob/ff3e068fa44eb85bb918580b2e10e18c027a18e6/research/lean-global-resolvent-20261121/overview/longshot/cycles/IDENTITY_ATOM_ATTEMPT.md).

## 3. An exact budget for the complete propagated pole family

Let `P_s` be the actual unit inverse pressure operator with branch weight
`(3/2^e)^s`, and let `lambda(n)=3n/(3n+1)`. For `s>1`, the ordinary reference
measure and its positive loss are

`sigma_s = sum_(n in O) n^(-s) delta_n`,

`d_s = sum_(n in O) n^(-s)(1-lambda(n)^s) delta_n`.

Their exact identity is `sigma_s P_s = sigma_s-d_s`. Its iterates decrease
to the sum `mu_infinity,s` of all canonical escaping-component measures.
For every nonnegative seed integrable against `sigma_s`,

`sum_(k>=0) d_s(P_s^k f) = sigma_s(f)-mu_infinity,s(f)`.

This evaluates the entire time sum while retaining the original source.
For rational ternary poles of order `beta<s-1`, the proof gives an explicit
height-weighted countable-family budget. The associated Green function is
finite at every ordinary root, including periodic roots with their geometric
return factor. It is integrable against both `d_s` and, for `1<s<2`, Haar.

The proposed escape contradiction still fails under the retained measure:
on any escaping component, the same Green function has infinite integral
against `mu_(E,s)`. One unchanged source leaves the same positive contribution
at each later endpoint. The finite loss budget does not remove those terms.

[ESCAPE_CLOSURE.md](ESCAPE_CLOSURE.md) contains the complete calculation,
including the nonempty local-pole parameter window `log_2(3)<s<2` and its
precise distinction from the earlier low-exponent Haar obstruction.
These infinite measure statements are written mathematics, not Lean claims.

## 4. Verification and remaining work

The two new proof modules compile from their final bytes with Lean 4.34.1
and the pinned mathlib revision. The fresh audit covers all **18 new public
statements** and reports only `propext`, `Classical.choice`, and `Quot.sound`.
No admitted theorem or custom Collatz axiom is used. That statement does not
extend the formalization boundary to the written infinite-product or measure
arguments.

Both exact Python programs pass normally and under `-O`. Controls include
31,865 complete moving-letter identities through word length 12, cyclic
window placements, exact pressure accounting with endpoint collisions and
periodic repetitions retained, and rejection of a forged full denominator.
They are bounded implementation and scope controls, not a proof of universal
cycle absence or escape exclusion.

The [verification report](../../reports/2026-11-23-closure-round2/README.md)
contains commands, source hashes, axiom output, independent semantic reviews,
and repository-integrity receipts. The remaining closing obligations are
the contradiction at the common ordinary root, unrestricted full-denominator
cycle exclusion, and an estimate against the actual retained escape law.
