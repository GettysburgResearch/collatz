# Independent reconstruction of the elementary growing-popcount theorem

**Verdict: VERIFIED at the scoped written-argument level.** This is an
independent mathematical reconstruction by the merger-route agent. It is not
formal proof-assistant verification, external peer acceptance, or a Collatz
proof. The repository may retain the author's PROPOSED status pending its
normal review process.

## Frozen reviewed bytes

Reviewed `GROWING_COMPLEXITY.md` SHA-256:

`3b153bb1fe05571f782e388d104b823e7fa6902f7e01a274121ad5c166f8f571`.

Associated `check_growing_complexity.py` SHA-256:

`3ad32196e7c0d677e42c087627a8679729d8058788a19aa091acb7ea799078e1`.

The source comparisons were read at the exact Git objects:

- PR #141, `5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`,
  `research/ay-persistent-20261031/PROOF.md`, HC-2.
- PR #145, `dd245a712f985909f541590e3f6c179b7ba011e4`,
  `research/binary-run-occupancy/README.md`, Sections 1–4.

No verdict extends to subsequent edits or other results in those source PRs.
The companion S-unit theorem is outside this review's required dependency
chain: the elementary growing-popcount proof does not invoke it.

## Arithmetic reconstruction

I reconstructed the following steps from the definitions rather than relying
on the producer's checker or its agreement with earlier prose.

1. **Original-source cut.** For an adjacent set-bit gap `d>2L`, write
   `n=2^D u+v`, with `u,v` positive odd and `v<2^(D-d+1)`. Since the gap is
   integral, `d>=2L+1`. Thus `4^j v<2^D` for every `0<=j<=L`, including the
   endpoint. The shadow recurrence `P_(j+1)=3P_j+2^A_j<=4P_j` gives
   `A_j<D`. The next shadow valuation is strictly smaller than the upper
   block's available power of two, so it is the actual valuation. This
   proves the claimed exact state formula and disjoint binary blocks. The
   positive lower block consumes at least one of the S allowed bits.

2. **Residue period.** For `m>=3`, the exact order of 3 modulo `2^m` is
   `L=2^(m-2)`. Multiplication by odd u preserves the distinctness of the
   L residues. There are exactly
   `B_S(m)=sum_(i=0)^(S-2) binom(m-1,i)` odd residues with at most S-1 ones.
   A sparse full upper integer has a sparse residue. Therefore the local
   count is at most `min(L,B_S(m))`, irrespective of the lower shadow's
   detailed itinerary.

3. **Distinct-source count and windows.** An odd r-bit integer is uniquely
   specified by its r-1 positive gaps. Requiring each gap at most 2L gives
   exactly `(2L)^(r-1)` possibilities. The orbit's distinctness is needed
   precisely when turning that inventory into a count of visits. Reserved
   windows have starts at least L positions apart, hence number at most
   `ceil(N/L)`. A final short window obeys the same local bound. Every
   sparse visit belongs either to such a window or to the finite gap
   inventory. No independence or renewed probability assumption is used.

These checks establish the exact finite inequality, including S=2,
N<L, and the final truncated window. S=1 is correctly treated separately.
The shadow orbit of 1 never creates a fictitious physical continuation:
the separated full state has a positive even upper part and cannot be 1.

## Growing threshold and constant

Put `X=log_2 N`, `S=floor(c sqrt X)`, `m=floor(alpha sqrt X)` with
`2c<alpha<1/c`. The first term, divided by N, has logarithm at most

`-(1-c alpha)X+O_c(sqrt X+log X)`.

Choose `c/alpha<p<1/2`. Eventually `S-2<=p(m-1)`. The weighted binomial
argument gives `B_S(m)<=2^((m-1)H_2(p))`; its inequality direction is correct
because `p^i(1-p)^(M-i)` decreases with i when p<1/2. Since eventually
`L<=N`, the window fraction is at most

`2 B_S(m)/L <= 4*2^(-(m-1)(1-H_2(p)))`.

It follows that any fixed `0<delta_c<alpha(1-H_2(p))` works after increasing
the constant for the finite initial range. The faster exponential-in-X
term is absorbed by that stretched exponential. All constants can be
chosen as functions of c; none depends on source height or window location.
The floor in S exactly represents the real popcount threshold.

The two strict requirements on alpha are simultaneously satisfiable iff
`c<1/sqrt(2)`. I checked the prior run theorem rather than inferring its
constant from the new proof: it uses `2R-1` signed boundary gaps, an entropy
cutoff at `2R`, and the conditions `4c<alpha<1/(2c)`, yielding
`c<1/sqrt(8)`. Thus the claimed factor-two improvement is specifically to
the **popcount consequence**, not the number-of-runs theorem. A long block
of consecutive ones distinguishes these quantities, as the author states.

## Executed evidence and limits

The reviewed checker was executed independently with

`python -X utf8 -B check_growing_complexity.py`.

It exited zero. The exact reviewer output has SHA-256

`c6b3da02143e1746c5c732b0ea90fc3648fd3166ac3a6e6615f0dc687a8ed27a`.

This was a replay of the author's implementation, **not** a second independently
written checker. The proof reconstruction above is independent of it. No
repository-wide validator, external build, asymptotic numerical extrapolation,
or formal verification is claimed by this reviewer.

The final theorem concerns a uniformly small proportion of low-popcount
states in distinct odd-event windows. It supplies no upper popcount cap,
no positive lower frequency of low-popcount visits, and no global cut
replacement budget. Repeating a cycle invalidates distinctness; one
primitive tour is within scope, but arbitrary cycles are not excluded.

No correction to the frozen argument was required.
