# Anchored returns, two R-bridges, and compressed original companions

**AR-001--006: PROPOSED pending independent mathematical review.**
This publishes the preceding in-chat pass, with freshly reconstructed exact checks.
No complete Collatz proof, independent acceptance, or external priority claim.
Date: 2026-09-20. Map: unabsorbed shortcut T(n)=n/2 for even n and
T(n)=(3n+1)/2 for odd n, on positive ordinary integers. Thus 1 <-> 2.
Words record actual source parities chronologically. All original clocks are
retained; comparison-stage increments below are synchronous, but original
source prefixes need not have the same lengths.

## Provenance, dependencies, and publication scope

The chat inspected #124 at `1d4dfc103055648def3db73860778a383a91ea3c`,
#125 at `081dd4fb8af75b3b237a5eb4cef28b84bb5329be`, and #126 at
`7e996feb24cc5d8579d75b39e0b909ffc03b3bcb`. This packet is additive and
stacked on the frozen #125 head. Its proof is at
`research/paired-comparison/valuation-ladder/PROOF.md` (VL-001--008).
The Q repeats, completion of (D,3D+2), forced H entrance and old ladder
are credited there; adjacent exits and gap-four comparisons are also in
#124/#126 under `research/astra-exit-merging/`.

At publication #127 was read at `f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00`
and #128 was recorded at `edd48df6e9c678fa4a65b4ed8f41421dfc92518b`.
In particular the 1024t+735 cylinder below independently appears in #127,
EG-004. Do not claim priority over that publication or count its individual
cylinder as new relative to #127. The benchmark here compares ONLY the
exact #125 two-bridge language, not every rule in the live repository.
The reusable R entrance, two-countdown guard and anchored-return argument
are the organizing content of this packet.
Main was `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
All dependencies retain their proposed statuses. No analytic, density,
rank-transport, or external formalization theorem is a premise.

## AR-001. Fixed-anchor arm-swapping returns cannot be infinite

Let n be a hypothetical least positive integer not reaching 1, and fix a
positive original source m<n. Consider physical stages

    (T^a_j(n), T^b_j(m)) = (H(C_j),C_j) or (C_j,H(C_j)),
    H(C)=9C+2, C_j>=1.

Suppose each nonterminal return advances both actual clocks and swaps the
orientation. There cannot be infinitely many such returns.

Proof. Minimality gives that m reaches 1; its unabsorbed orbit is eventually
in {1,2}. Clock b_j tends to infinity. Infinitely many alternate stages would
put this fixed m-arm at H(C_j)>=11, a contradiction. No monotonicity of C_j
or peak height is used. In particular growing return parameters alone are
not a reason to demand a decreasing parameter rank.

This is a conditional least-counterexample lemma, NOT an unconditional
assertion that an arbitrary H parameter cannot return forever. A finite
OUTSIDE outcome is still possible. Administrative arm relabeling, clock
resets, or changing the original companion without further control does not
meet the hypotheses. VL-003/004 and AR-003/004 returns meet them.
The remaining target is escape-complete root-compatible comparison rules;
this packet does not establish that target.

## AR-002. A complete finite classification of the R entrance

Put R(D)=(3D-4,D), Q(E)=(3E-1,E), K(E)=(9E-10,E).
For every v>=1, C=8v-1 satisfies the actual three-step identity

    (H(C),C) --101 / 111--> R(27v-1).

Indeed its endpoint is (81v-7,27v-1). For EVERY integer D>=2,
two steps on each arm give exactly one of these rows:

| Guard | Endpoint | Upper/lower words |
| --- | --- | --- |
| D=0 mod4 | Q(D/4) | 00 / 00 |
| D=2 mod4 | R((3D+2)/4) | 01 / 01 |
| D=3 mod4 | (Y-5,Y-1), Y=9(D+1)/4 | 10 / 11 |
| D=1 mod4 | K((3D+1)/4) | 11 / 10 |

These follow by substitution into T twice. Every displayed endpoint is
positive. In the repeated row D'-2=3(D-2)/4. If D>2, each repetition
consumes exactly two units of v2(D-2), so the repeat cannot be infinite.
D=2 is already the merger (2,2). Consequently every C=7 mod8 has a finite
physical route to Q, a gap-four pair, or K. This is exhaustive type entry
for that entire class, not successful termination of all the resulting types.

## AR-003. Bridge A: consecutive R and Q valuation countdowns

Assume C=8v-1 and v2(9v-1)=2k+1 with k>=0. Set

    b=(9v-1)/2^(2k+1), E=(3^(k+1)b+1)/2.

The AR-002 entrance followed by k R repeats and the even exit reaches Q(E)
in 2k+5 steps. To see the count, D_0-2=3(9v-1); after k repeats
D_k-2=2*3^(k+1)b, so D_k=0 mod4 and D_k/4=E.
Now suppose E>1 and v2(E-1)=2ell+1, ell>=0. Put

    c=(E-1)/2^(2ell+1), F=(3^(ell+1)c+1)/2.

The Q rule E=1 mod4 -> (3E+1)/4 subtracts one according to
E'-1=3(E-1)/4. After ell repeats the Q parameter is 3 mod4;
its exit reaches (F,3F+2). Its words are 00/11 and the preceding
Q-repeat words are 01/10. Total time so far: 2k+2ell+7.
This Q rule and the following completion are inherited from VL-002/004.

Write F+1=2^s q with q odd, s>=0, and z=3^s q. After s common odd steps
and two final steps the endpoint is

    z=3 mod4: ((3z-1)/4,(3z-1)/4),
    z=1 mod4: (C',H(C')), C'=(z-1)/4>0.

The final words are 1^s01 / 1^s00 in the first case and reversed final
two bits in the second. Thus Bridge A merges or swaps the H orientation
in exactly 2k+2ell+s+9 steps on each arm. All countdowns are read from the
actual input. Admitted C are 7 mod16, hence v2(3C-1)=2: these are outside
both VL-003 admission guards.

### Whole cylinder A

For every integer t>=0,

    C=512t+439,
    T^9(H(C))=T^9(C)=243t+209,
    words 101000001 / 111001100.

Uniform parity and affine substitution prove the identity on the entire
progression. It is only one subcase of the reusable two-countdown bridge.
For example T^9(3953)=T^9(439)=209.

## AR-004. Bridge B: the R exit to gap four and adjacent returns

For every v>=1, C=32v-1 and Y=243v satisfy

    (H(C),C) --10110 / 11111--> (Y-5,Y-1).

This is AR-002 with D=108v-1=3 mod4, using its gap-four row.
Assume Y=1 mod4. Two more halvings yield (q,q+1), q=(Y-5)/4>0.
If q is odd, impose q>1 and v2(q-1)=2s>0. Then exactly s repeats

    (q,q+1) --10 / 01--> ((3q+1)/4,(3q+1)/4+1)

reach an even parameter: q'-1=3(q-1)/4, with its exact 2-adic countdown.
If q is already even, no repeat is needed. Write the resulting even
parameter as q again. Its finite exits are as follows.

* v2(q)=2: after two steps reach (e,3e+1), e=q/4 odd, and one further
  step merges at (3e+1)/2.
* v2(q)>=3: the same two-step endpoint has e even, and one further step
  reaches (q/8,H(q/8)), a swapped H return.
* v2(q)=1: two steps reach (D,3D+2), D=(3q+2)/4. Apply the finite
  completion in AR-003 (including its s=0 case).

These adjacent exits are inherited from #124--126; the new connection is
the exact R entrance from the residual H pair, with its original roots intact.
Bridge B therefore merges or returns with swapped orientation, on an input
class C=31 mod32 disjoint from Bridge A and the VL-003 guards.

### Whole cylinder B

For every t>=0,

    C=1024t+735,
    T^10(H(C))=T^10(C)=729t+524,
    words 1011000001 / 1111100100.

For example T^10(6617)=T^10(735)=524. This identity is also present in
parallel PR #127; the benchmark does not count it as novel over that PR.

## AR-005. Compressed original-source ladder

VL-001 gives that a hypothetical least counterexample has n=2^r u-1,
r>=2, u positive odd, and the hard first-exit condition 3^r u=3 mod4.
For every 1<=h<=floor(r/2), define

    mhat_h=(n+1)/4^h-1=2^(r-2h)u-1,
    C_h=(3^(r-2h+1)u-1)/4.

Then all quantities are positive ordinary integers, and

    0 < 4^h*mhat_h < n,
    T^(r+2)(n)=H^h(C_h),
    T^(r-2h+2)(mhat_h)=C_h.

Proof. Put p=r-2h. Since 3^p u=3 mod4, the p initial odd steps from
2^p u-1 followed by 01 reach (3^(p+1)u-1)/4. This includes p=0,
where the odd block is empty; its congruence ensures mhat_h>0 even then.
Also H^h(C)=9^h C+(9^h-1)/4. Substitution proves the first arm's identity.
Finally 4^h*mhat_h=n+1-4^h<n.

The original companion is below n/4^h rather than approximately n/2.
The first rung is (n-3)/4 and the second is (n-15)/16. This improves the
source factor and clocks, but alone does not enlarge the successful C set.
The ladder has only floor(r/2) rungs for each fixed n; no extra rung is assumed.

For the prior VL-006 example,

    T^18(236031)=T^16(59007)=478505, 4*59007<236031.

For the prior skipped-rung example,

    T^34(20530069503)=T^30(1283129343)=37500596075,
    16*1283129343<20530069503.

The original arm is unchanged, so a previously proved no-descent property
of that arm is retained. Under minimality every original ladder source
converges, not merely a newly introduced intermediate comparison state.

## AR-006. Unbounded original-source exclusion families

For every r>=2, choose positive odd u and integer t>=0 with

    3^(r-1)u=2048t+1757, n=2^r u-1.

The hard first exit and AR-005 h=1 give (H(C),C) with C=512t+439.
Append cylinder A:

    T^(r+11)(n)=T^(r+9)((n-3)/4)=243t+209.

For every fixed r, odd multiplication modulo 2048 produces infinitely
many such u. For r>=9 every displayed positive-time state on the n-arm
exceeds n. Its odd prefix increases. The minimum of the subsequent H tail
is 162t+139=(3^(r+3)u+19)/1024. Since 3^(r+3)>2^(r+10) at r>=9,
this exceeds n. The two intervening exit states also exceed n.

Similarly, for every r>=2 use

    3^(r-1)u=4096t+2941, n=2^r u-1.

Cylinder B gives

    T^(r+12)(n)=T^(r+10)((n-3)/4)=729t+524.

For r>=8 the minimum of the H tail is
486t+349=(3^(r+4)u+89)/2048>n, because 3^(r+4)>2^(r+11).
Again the earlier states exceed n. Both are actual families with the
companion below n/4, not just successes for independent abstract parameters.

CRT independently imposes 2^r u=1 mod3. Thus 3|n and no smaller pure
ancestor of n exists at any depth: the odd predecessor equation would be
(2n-1)/3, not integral; iterated even predecessors are only 2^j n.
For each fixed sufficiently large r, infinitely many original sources satisfy
all these conditions simultaneously.

Example (family B):

    n=333567, m=83391<n/4,
    T^20(n)=T^18(m)=507179,
    min_(1<=j<=20)T^j(n)=338119>n, 3|n.

The n=7 mod8 family is outside #126's original n=8^k u-5 seed domain,
which is 3 mod8. Its relationship to that packet is reuse of its local
comparison rule rather than reentry into its original seed family.

## Exact bounded evidence and limitations

Run from repository root:

    python -S -B experiments/paired-comparison/anchored-returns/run.py --full /tmp/ar.jsonl --summary /tmp/ar.json
    python -S -B experiments/paired-comparison/anchored-returns/verify.py /tmp/ar.jsonl --summary /tmp/ar.json

The generator reconstructs VL-003/004 from their formulas; each admitted
stage is separately replayed by literal T, and every final merger is replayed
from the ORIGINAL pair (9C+2,C). The standalone verifier imports no generator
or repository module and checks merger parities/endpoints independently.
It authenticates the full corpus and checks range uniqueness; it does NOT
independently certify the mathematical meaning of OUTSIDE labels.

On exactly C=1..65536:

| Outcome | #125 language | Extended language |
| --- | ---: | ---: |
| Initially admitted | 8191 | 9440 |
| Finite mergers | 4366 | 5082 |
| Merger sources C=2 mod3 | 1464 | 1704 |
| OUTSIDE | 61170 | 60454 |
| Budget exhausted | 0 | 0 |

There are 716 additional successes and no lost baseline successes, including
240 additions in the necessary first-entry congruence C=2 mod3. These are
selected certificate-language outcomes, NOT a convergence census or a
percentage of hypothetical counterexamples. Most C still leave the language.

Fresh additional tests: all 65535 R rows for 2<=D<=65536; 13600 compressed
ladder instances; two whole-cylinder symbolic checks; 192 CRT-prescribed
Bridge A cases including k=63, ell=64; 40 long Bridge B countdowns; 40 lifted
CRT no-descent cases; the explicit example and two smaller-ladder examples.
The earlier chat mentioned a differently sized unpersisted ladder/lift grid;
only the fresh counts here are supported by this publication's executable.

Generator passes with -S normally and under -O, with identical summaries.
Standalone merger verifier passes with -S normally and under -OO, rejects
five direct semantic mutations in each mode, and replays 9448 merger rows
across the two modes. Same-author implementation diversity is not peer review.
Full 131072-row SHA-256:
`a45838ee24f9c05ddd81a27b8a749f7c1055ec4512a4542b8fa51d203f1c8d04`.
No complete-checkout root validation, remote CI, Lean build or independent
mathematical review was performed. Direct Git transport failed DNS; API
publication and local packet execution do not substitute for those events.

## Remaining target and retained controls

AR-002 makes K(E)=(9E-10,E) an explicit next escape type. The other major
family is VL's C=4^s d -> (3^(s+2)d+2,d), whose exponent is unbounded.
Parallel #127 gives every such type a nonempty gate; this still does not
force the ACTUAL parameter into a gate. A complete comparison procedure
must handle finite escapes, preserve root/clock compatibility, and explain
why any infinite continuation forces the forbidden anchor behavior.

It cannot demand universal equal-clock merging of each fixed H pair:
(20,2) reaches (2,1) after five common steps and then keeps opposite phases.
An earlier equality would persist, so no synchronous merger is possible.
Parameters 17 and 71 still leave the selected language. Their failure is
retained, not converted into either convergence or divergence evidence.
The anchor lemma removes a needless decreasing-C demand for its exact
return architecture; it does not prove an escape-complete architecture exists.
