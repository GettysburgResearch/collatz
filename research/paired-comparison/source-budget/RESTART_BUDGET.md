# Root safety under valuation-compressed H restarts

**RSB-001--005: PROPOSED, with a separate in-session mathematical reconstruction;
not accepted project mathematics or a complete Collatz proof.**
Date: 2026-10-18 (Asia/Jerusalem).

These statements concern actual ordinary inputs for the unabsorbed shortcut
map `T(n)=n/2` for even `n`, `(3n+1)/2` for odd `n`. The original source `N`
is immutable. Write `H(C)=9C+2`, and let `v2` denote the exact positive-integer
two-adic valuation. A new companion is usable by least-source induction
only if it is strictly below `N`.

The credited starting point is PR #135, head
`40c59116ba9a3f94565d9782e4ffe3c97cc0ce71`,
`research/paired-comparison/fixed-source-splicing/PROOF.md`, FSS-002--005.
The normalization `(01)^k` is older: #125 and #127, respectively heads
`081dd4fb8af75b3b237a5eb4cef28b84bb5329be` and
`f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00`.
PR #136, head `fc55ecf265f23b263983fb7eebd95a4c4b0f0787`, motivates retaining
one common rank or ledger; its rank `D-2` is not asserted for these returns.

The new contributions below are a common contracting original-companion
rank for an unbounded valuation-guarded language, its exact companion-height
ledger, a sharp power law for the loss of original-root order, and arbitrary finite
expanding runs whose only initially usable canonical companion is the first.
The even-valuation complement itself is included for proof completeness,
without an external priority claim. No convergence theorem follows.

## RSB-001. The exact complete canonical restart

Suppose `T^a(N)=H(C)`, and write

    C=2^(2k+epsilon)v,  v odd, k>=0, epsilon in {0,1},
    M(C)=3^(k+1)v.

If `epsilon=1`, the credited FSS-002 identity is

    T^(2k+2)(H(C))=T(M(C)),

with upper word `(01)^k00`. Its original-root order test is precisely
`M(C)<N`.

If `epsilon=0`, put `M=M(C)`, `s=v2(M+1)>=1`,
`u=(M+1)/2^s`, and `Q=3^s u`. Then the upper word `(01)^k` first gives

    T^(2k)(H(C))=3M+2.

The next `s+2` steps give the following exhaustive alternatives:

| Guard | Upper word after compression | Lower word from M | Endpoint |
|---|---|---|---|
| Q=3 mod4 | `1^s00` | `1^s01` | common `(3Q-1)/4` |
| Q=1 mod4 | `1^s01` | `1^s00` | `(H(D),D)`, D=(Q-1)/4 |

Every path and its times are actual. Positivity and the parity guards hold
for all positive inputs. In the hard case `D>0`: `Q` is a positive
multiple of three, and `Q=1 mod4` therefore implies `Q>=9`. The new
original companion is admissible exactly if `M<N`.

**Proof.** Each credited `01` step sends `H(C)` to `H(3C/4)` while `4|C`.
After `k` repetitions this is `9*3^k v+2=3M+2`. Since
`M=2^s u-1` and `3M+2=2^s(3u)-1`, the first `s` parities on both arms
are odd. They reach `Q-1` and `3Q-1`, respectively, both even. A further
halving reaches `(Q-1)/2` and `(3Q-1)/2`. If `Q=3 mod4`, the former is
odd and the latter even; their next states coincide. If `Q=1 mod4`, the
former is even and the latter odd, giving `D` and `9D+2`.

## RSB-002. One common exact companion-height ledger

Consider any nonempty finite sequence of hard returns from RSB-001. Write its H
parameters as `C_0,...,C_L`. The inputs `C_0,...,C_(L-1)` have even two-adic
valuation. Write

    C_j=2^(2k_j+epsilon_j)v_j, M_j=3^(k_j+1)v_j,

where `epsilon_j=0` for `j<L`; `epsilon_L` may be zero or one. Let `s_j`
be the odd-run length used in the hard return from `M_j`.

For `0<=j<L` define the positive rational numbers

    a_j = 3^(s_j+1+k_(j+1)) /
          2^(s_j+2+2k_(j+1)+epsilon_(j+1)),
    b_j = 1 - 3^(k_(j+1)+1) /
              2^(2k_(j+1)+epsilon_(j+1)+2).

Then `1/4 <= b_j < 1` and the single exact recurrence is

    M_(j+1)+1 = a_j*(M_j+1)+b_j.                  (1)

Put `P_0=1`, `P_j=product_(0<=i<j) a_i`. Its exact solution is

    M_j+1 = P_j * [M_0+1 + sum_(0<=i<j) b_i/P_(i+1)].    (2)

Consequently the canonical companion at that actual checkpoint is below
the fixed root `N` if and only if the right side of (2) is at most `N`.
The normalized quantity `(M_j+1)/P_j` is strictly increasing. Separate
valuation countdowns are not being combined as though they were one rank.

**Proof.** The hard-return formula is

    C_(j+1) = [3^s_j*(M_j+1)/2^s_j - 1]/4.

Also `M_(j+1)=gamma_(j+1)*C_(j+1)`, where

    gamma_(j+1)=3^(k_(j+1)+1)/2^(2k_(j+1)+epsilon_(j+1)).

Multiplication gives (1), with `a_j=gamma_(j+1)*3^s_j/2^(s_j+2)`
and `b_j=1-gamma_(j+1)/4`. Since `0<gamma_(j+1)<=3`, the stated bounds
on `b_j` follow. Divide (1) by `P_(j+1)` and telescope to obtain (2).
Finally `M_j` is an integer, so `M_j<N` is equivalent to `M_j+1<=N`.

### A whole valuation-guarded language with a common contracting rank

For one actual hard return, write `M=M_j`, `s=s_j`, and normalize its
output as `D=2^(2k+epsilon)v`, `M'=3^(k+1)v`. If the actual integers obey

    3^(s+k) <= 2^(s+2k+epsilon),                     (G)

then

    0 <= M'-3 < (3/4)*(M-3),   M'<M.                (6a)

Thus a canonical companion already below the fixed original `N` stays
below `N` under every admitted restart, irrespective of how the valuation
types switch. This is a single ordinary integer rank, `M-3`, for the whole
guarded language; it is not a mixture of separate ranks.

**Proof.** Set `beta=(3/4)^k/2^epsilon` and
`delta=(3/2)^s*beta`. Guard (G) is exactly `delta<=1`. The exact hard-return
formula gives

    M' = (3/4)*delta*(M+1) - (3/4)*beta
       < (3/4)*(M+1).

Both canonical companions are positive multiples of three, so `M'>=3`.
Subtracting three gives (6a). In particular (G) cannot hold when `M=3`,
and it gives strict decrease for every admissible input.

The corresponding deterministic normalizer starts from an actual H
checkpoint with `M_0<N`. If its current canonical companion is `M=3`,
then necessarily `C=1` or `C=2`. It returns the explicit core merger

    T^6(H(1))=T(3)=5, upper word 110100, lower word 1;
    T^2(H(2))=T(3)=5, upper word 00, lower word 1.

Otherwise it applies RSB-001; an odd valuation or a good
exit returns MERGE. At a hard exit it continues precisely if (G) holds
for the actual output valuation, otherwise returning that actual checkpoint
with label FAILED_DEBT_GUARD. It keeps `N` fixed throughout. Any admitted odd-valuation
output supplies a merger at the next pass. For `M_0>3`, if `J` is the least
nonnegative integer such that `3^J*(M_0-3)<4^J`, there can be at most `J`
admitted hard restarts: by then the nonnegative integer rank is zero, and
another admitted restart is impossible. For `M_0=3` there are none.

For an exact upper clock bound, define

    K_0=max {k>=0 : 3^(k+1)<=M_0},
    S_0=max {s>=1 : 2^s<=M_0+1},
    B_0=max(6,2K_0+S_0+2),

and put `J=0` if `M_0=3`. Every even-valuation iteration has at most
`B_0` upper steps, and every terminating odd-valuation iteration has at
most `2K_0+2<=B_0` upper steps. The explicit `M=3` core merger uses at
most six upper steps, also at most `B_0`. There are at most `J` admitted hard
iterations and one final iteration. Thus the total upper clock advance,
starting at the given actual H checkpoint `T^a(N)=H(C_0)`, is at most

    (J+1)*B_0.                                      (6b)

Thus its upper clock from the original root is at most `a+(J+1)*B_0`;
the bound does not include the earlier work needed to reach that checkpoint.

This follows from `3^(k_j+1)<=M_j<=M_0` and
`2^s_j<=M_j+1<=M_0+1`. In particular the bounds are `O(log M_0)` admitted
stages and `O((log M_0)^2)` upper shortcut steps. These are physical step
bounds for this partial language, not bit-complexity or universal convergence
bounds. No theorem forces guard (G) at a failed checkpoint.

### Arbitrarily large valuation types are actually admitted

For every `s>=1` and `epsilon in {0,1}`, choose any positive `u` satisfying

    3^s*u = 1+2^(4s+epsilon+2) mod 2^(4s+epsilon+3),
    2^s*u = 7 mod9.                                 (6c)

Both inverses exist, and the moduli are coprime, so CRT gives one nonempty
positive residue class. The first congruence makes `u` odd. Define

    M=2^s*u-1, C=M/3, N=(16C+1)/3,
    D=(3^s*u-1)/4.

The second congruence makes `C` an odd positive integer with `C=2 mod3`.
Thus `N` is a positive ordinary first-run-2 root, with

    T^4(N)=H(C), M<N,
    T^(s+6)(N)=H(D), T^(s+2)(M)=D.

The exact output valuation is `v2(D)=4s+epsilon`, hence its normalization
has `k=2s`. Guard (G) reads `27^s<=32^s*2^epsilon`, which is strict.
Therefore the next actual canonical companion is strictly below `M<N`.
This establishes genuinely unbounded `s` and `k` inside the guarded
language. If `epsilon=1`, the next odd-valuation identity supplies a merger
with this smaller companion after a total of `5s+8` upper steps from `N`.

For each prescribed `s,epsilon`, all sufficiently positive representatives
of (6c) give these statements. Constructing such a family does not select
new digits for a source that was already fixed, and it does not claim
that every fixed source eventually satisfies (G).

### A necessary accumulated valuation balance

Suppose `L>=1`, every output also has even two-adic valuation, and set
`S=sum_(j<L) s_j`, `K=sum_(1<=j<=L) k_j`. If `M_L<N`, positivity in
(2) forces

    S*log(3/2) - (L+K)*log(4/3) < log(N/(M_0+1)).       (3)

In particular, since `S>=L`, indefinitely keeping these canonical
companions below one fixed `N` would require compression valuations with

    K > [log(9/8)/log(4/3)]*L
        - log(N/(M_0+1))/log(4/3).                     (4)

This is a necessary condition, not a sufficient contraction or a frequency
law for actual orbits. The positive correction sum in (2) also has to be
paid. If the last valuation is odd, subtract an additional `log(2)` from
the left side of (3), exactly as prescribed by `a_(L-1)`.

### The odd-parameter corridor loses root safety in boundedly many stages

If `C_j` and `C_(j+1)` are odd, then

    C_(j+1)+1 >= (9/8)*(C_j+1),                      (5)

because `s_j>=1`, and the hard-return expression is increasing with `s_j`.
Equality holds for `s_j=1`.

At the first hard H entry of an original root with first odd-run length
`r=2`, the exact relation is `N=(16C_0+1)/3`. Thus if the first six H
parameters `C_0,...,C_5` are odd and all five transitions are hard,

    M_5=3C_5 >= 3*(9/8)^5*(C_0+1)-3 > N.

For first odd-run length `r=3`, `N=(32C_0-1)/9`, and two such hard
transitions already imply `M_2>N`. These statements concern loss of the
canonical root-order test; they do not declare the original orbit divergent
or preclude another smaller-original companion.

## RSB-003. Sharp one-restart inflation exponent

Let `alpha=log_2(3)`. Suppose an actual hard restart has canonical companion
`M_0<N` and output parameter `D`. Normalize `D` by RSB-001, irrespective
of whether its valuation is odd or even, and call the next canonical
companion `M_1=M(D)`. Then

    M_1 <= (3/4)*(N^alpha-1).                         (6)

The exponent `alpha` cannot be replaced by any smaller exponent in a
uniform bound over actual first-entry examples. More strongly, there is
an explicit infinite family in which the initial companion is below `N`,
the next companion is above `N`, and the entire displayed original prefix
stays strictly above `N`.

**Upper-bound proof.** Put `M_0+1=2^s u` as in RSB-001. Since `u>=1`,

    3^s u = (M_0+1)^alpha / u^(alpha-1)
           <= (M_0+1)^alpha <= N^alpha.

Thus `D=(3^s u-1)/4 <= (N^alpha-1)/4`. Every canonical normalization
satisfies `M(D)<=3D`, proving (6).

**Sharpness construction.** For every `j>=1`, put `s=6j+2` and define

    N   = 13*(2^(s+4)-1)/9,
    C   = (13*2^s-1)/3,
    M_0 = 13*2^s-1 = 3C,
    D   = (13*3^s-1)/4,
    M_1 = 3D.

All are positive integers. `C` and `D` are odd, `C=2 mod3`, and
`N=(16C+1)/3` has first odd-run length exactly two and a hard first exit.
Therefore

    T^4(N)=H(C),
    T^(s+6)(N)=H(D),   T^(s+2)(M_0)=D,               (7)

with original word `1101 1^s01`, and `M_0<N<M_1`.

To check the congruences, `s=2 mod6` gives `2^s=4 mod9`, making `C=2 mod3`
and `N` integral. Since `s` is even, `13*3^s=5 mod8`; hence `D` is odd
and the return is hard. Also

    N-M_0=(91*2^s-4)/9 > 0,
    M_1-N=[(9*3^(s+1)-2^(s+6))*13+25]/36 > 0.

The second numerator is positive already for `s>=3` and therefore for
all our `s>=8`.

The first four positive states are `8C+1,12C+2,6C+1,9C+2`, all above
`N=(16C+1)/3`. The next `s` odd steps increase. Their last state is
`4M_1+2`; the final two states are `2M_1+1` and `3M_1+2`, also above `N`.
This proves the whole-prefix claim, not only an endpoint comparison.

Finally the exact identity

    M_1+3/4 = (39/4)*[(9N+13)/208]^alpha             (8)

shows `M_1` has order `N^alpha` along this unbounded family. Hence no
uniform `O(N^beta)` upper bound with `beta<alpha` is possible. In particular,
the loss of root safety cannot be repaired by a fixed multiplicative
slack allowance for the next canonical companion. No claim is made that
the original root has no other smaller companion or that recovery at a
later checkpoint is impossible.

The first family member is

    s=8, N=5915, C=1109, M_0=3327, D=21323, M_1=63969.

## RSB-004. Arbitrarily long expanding hard runs after one safe companion

The odd-parameter hard branch with `s=3` is exactly

    C=29 mod32,
    F(C)=(81C+19)/32,
    T^5(H(C))=H(F(C)),   T^5(3C)=F(C),               (9)

with words `11101` and `11100`, respectively. Moreover

    49F(C)+19 = (81/32)*(49C+19).                    (10)

For every `K>=1`, choose any positive integer `C` satisfying

    C=2 mod3,
    49C+19 = 2^(5K+1) mod 2^(5K+2).                 (11)

Such inputs form one nonempty residue class modulo `3*2^(5K+2)` by CRT.
Set `N=(16C+1)/3`, `C_j=F^j(C)`, and `M_j=3C_j`, `0<=j<=K`.
Then every `C_j` is an odd positive integer, and

    T^(4+5j)(N)=H(C_j),
    T^5(M_j)=C_(j+1)  for 0<=j<K.                   (12)

The first companion is usable, `M_0<N`, while

    M_j>N  for every 1<=j<=K.                       (13)

Every positive-time original state through time `4+5K` is strictly above
`N`. This produces arbitrary finite actual runs with canonical source
order lost immediately after their first return.

**Proof.** The guard `C=29 mod32` is equivalent to `v2(49C+19)>=5`.
It also gives `v2(3C+1)=3` and a hard exit in RSB-001. Direct substitution
gives (9) and (10). Condition (11) gives

    v2(49C_j+19)=5(K-j)+1.                           (14)

Thus the first `K` guards hold, all `C_j` are odd, and the next guard fails.
Positivity follows from `F(C)>C>0`. The first hard entrance from `N`
has word `1101`, as in RSB-003. Concatenation proves (12).

The first order difference is

    M_1-N = (217C+139)/96 > 0.

Since `F(C)>C`, all subsequent differences stay positive. In each five-step
upper block the first three odd steps increase. Write `u=(3C+1)/8`; the
starting value is `24u-1`, while the fourth value is `(81u-1)/2`, which
is strictly greater than the starting value. The last step is odd and
increases. Thus every positive state in that block exceeds its input,
and the initial four states exceed `N`, proving the full-prefix claim.

### Exact fixed-source limitation

For one fixed positive ordinary `C`, the number of consecutive admitted
applications of the branch (9) is exactly

    floor(v2(49C+19)/5).                             (15)

The positive integer `49C+19` is nonzero, and (10) consumes exactly five
valuation units per application. The arbitrary length in (11) is obtained
by changing the original source with `K`. It supplies no positive ordinary
source realizing this expanding branch forever. At the first failed guard
the full canonical algorithm may use a different actual branch; (15) does
not settle that continuation.

## RSB-005. What remains open

The exact ledger (2) gives a concrete fixed-source target: prove that an
actual sequence reaches a merger with a canonical companion below `N`,
or provide a physically justified alternate companion when the displayed
budget fails. The sharp family (7) and expanding runs (12) show why a
uniform next-step root-order claim, a fixed slack factor, or a promise
that odd-parameter hard returns will themselves restore root safety is
false. The necessary valuation balance (3) is not yet an all-orbit bound.

The existing persistent-companion clock theorem cannot be invoked after
replacing a below-root companion by one of the `M_j>N` sources in (13).
Conversely, these failures do not rule out an adaptive bank of different
smaller original sources, including sources supplied by deeper inverse
splicing. No complete proof, nontrivial positive cycle, or divergent orbit
is asserted.

## Reproducible checks

`experiments/paired-comparison/source-budget/check_restarts.py` is a standalone
arithmetic/path check, run from the repository root. Its scope is reported by
the script, including all canonical inputs `C=1..20000`, exact rational
ledger checks on finite hard chains, six power-law family members, and
the least positive CRT representative for `K=1..24`. It also runs the
guarded normalizer on all `C=1..20000`, checks the exact clock bound (6b),
and verifies (6c) for `s=1..24` and both output valuation parities.

The recorded runs used Python normally and under `-OO`, with identical
JSON results. Every validation predicate uses an explicit `need` check
that raises `RuntimeError` on failure, so optimization does not disable
the checks. They passed
all 20,000 one-stage cases, 1,008 hard ledger steps from the specified 2,000
initial sources, all six power-law members, all 24 long-run members (largest
root: 124 bits), and 20,000 exact fixed-source countdown comparisons. The
old control `N=27`, `C=5 -> 20`, `15<27<45`, was retained.
The guarded normalizer on 20,000 H parameters returned 14,697 MERGE and
5,303 FAILED_DEBT_GUARD outcomes, with 1,442 total admitted stages and at
most two on this grid. These are comparison-parameter outcomes, not a
census of original roots. All exact clock bounds passed, as did all 48
unbounded-guard construction cases (largest original root: 127 bits).

The finite checks do not prove the unbounded theorems above. They do not
invoke an absorbed map, a stopping-time oracle, or a root-convergence
assumption. No repository-wide validator or formal proof build is claimed
for this isolated draft.
