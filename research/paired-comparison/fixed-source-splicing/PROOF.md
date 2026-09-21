# Fixed-source splicing: whole valuation strata and original-root escape tests

**FSS-001--005: PROPOSED pending independent mathematical review.**
Date: 2026-09-21. These are guarded, pointwise lower-source results, not a
complete Collatz proof. No external priority claim is made. FSS-006 records
the finite experiment and the unsupported global step.

## Conventions, sources, and the change of question

Use the unabsorbed shortcut map T(x)=x/2 for even x and (3x+1)/2 for odd x.
Words give source parities chronologically. Every certificate uses positive
ordinary sources and independently specified clocks. The root N is immutable.
A witness smaller than a later inflated state is not automatically below N.
Write H(C)=9C+2 and v2 for the exact positive-integer two-adic valuation.

Previous packet #130 is present, still draft, at
`53cf9b53bd568b1ab67601b00e789b464198e42b`, tree
`895792dbe4a467309384c23820e3f850b7bed6cd`. All six local source/artifact blob
identities were matched to live directory readback. This is an additive child
packet; neither main nor any older proof/status is changed.

Dependencies and credits:

- #125, `081dd4fb8af75b3b237a5eb4cef28b84bb5329be`,
  `research/paired-comparison/valuation-ladder/PROOF.md`: first-odd-run
  H entrance, valuation-return machinery and original-source inequalities.
- #127, `f5e7ec9a23fa691d71a5a9f518cbff5529a5ea00`,
  `research/paired-comparison/escape-gaps/PROOF.md`: the 4-adic type
  normalization. The repeated 01 transition used below is already there.
- #130, same head above,
  `research/paired-comparison/universal-finite-synchronization/PROOF.md`:
  all-type gate construction and persistent original-companion budgets.
  Its selector supplies the frozen finite baseline, not a premise establishing
  correctness of the new formulas. Every retained success is replayed.
- Parallel #131, `e092da549c8c50e8a9430f88fb721ea51fe34d91`,
  `research/paired-comparison/delayed-shadow-compiler/PROOF.md`: successful
  subcells need not contain a fixed ordinary source, even one that merges.
- Parallel #132, `7687eec1ac364009d644cb8d015f1fe3b28730cc`, supplies another
  affine classification and finite-escape analysis. Its PR description was
  inspected; this packet does not claim a proof-body review of all its claims.

The project's existing inverse-fan work already supplies the general idea of
looking backwards from an actual endpoint. FSS-001 is an elementary exact
specialization, not a claim to have invented inverse search. The good odd-exit
identity used in FSS-005 is also credited prior work, not a new lemma. The
contribution here is a gate-free **whole odd-valuation identity**, its exact
ORIGINAL-root acceptance region, and an unbounded no-descent construction.

The earlier affine compilers choose additional source digits. This packet
instead evaluates a formula on the unchanged source. Its inequality can fail;
when it fails, it is not silently replaced by a favorable translated source.

## FSS-001. Complete one-step inverse test at a fixed actual endpoint

Let N>1 and y=T^A(N) with A>=1. If y>=N, a positive m<N with T(m)=y exists
if and only if

    y=2 mod3, and 2y-1<3N.                              (1)

When it exists it is unique and m=(2y-1)/3, which is odd. Thus the exact
root-relative band is

    N <= y < (3N+1)/2, y=2 mod3.                        (2)

Proof: the even inverse 2y is not below N. The only possible odd inverse is
(2y-1)/3; integrality is equivalent to y=2 mod3, its parity is then odd,
and its order is precisely (1). Positivity follows from y>=N>1.

If the whole original prefix stays at least N, the terminal step of such a
certificate cannot be odd: its unique odd inverse would be the previous
actual state, which is at least N. This observation prevents mistaking a
literal reversal of the original edge for a new smaller witness.

In particular EVERY hypothetical least nonconvergent N must avoid (2) at
EVERY positive actual time. This is a necessary orbit restriction, not a
proof that every orbit enters the band. The implementation requires strict
no-descent, y_i>N throughout, for its general BAND search. The closed formulas
below also retain successful certificates whose original arms descend.

## FSS-002. Every odd valuation of C has a gate-free one-step companion

For EVERY k>=0 and positive odd v, set

    C=2^(2k+1)v,
    M=3^(k+1)v,
    E=(3^(k+2)v+1)/2.

Then

    T^(2k+2)(H(C)) = T(M) = E,                          (3)
    upper word (01)^k00; lower word 1.

There is no further residue guard on v.

Proof: each old 01 transition sends H(C) to H(3C/4) when 4 divides C.
After k such transitions the upper value is 18*3^k*v+2. This is divisible
by four since v is odd. Its two halvings give E. Since M is odd, T(M)=E.
All intermediate parities and positive values have therefore been supplied.

Consequently, at ANY actual checkpoint T^a(N)=H(C), with odd v2(C), (3)
is a lower-original-source certificate precisely when

    3^((v2(C)+1)/2) * oddpart(C) < N.                   (4)

The original arm must be the H coordinate. An orientation swap does not
license applying (4) with the wrong root or to a different arm. Nothing
requires the former companion to be retained: the new M is justified by its
actual path and comparison with N. This is not an invocation of a clock
budget after a reset.

## FSS-003. Exact first-entry acceptance, with whole-stratum exclusions

Write N=2^r*u-1, r>=2, u positive odd. At the hard first odd exit,
3^r*u=3 mod4, the credited exact prefix is

    T^(r+2)(N)=H(C), C=(3^(r-1)u-1)/4=2 mod3,
    original word 1^r01.                              (5)

The good first exit already has the old smaller-source certificate and is
not counted as a new result here. If

    v2(3^(r-1)u-1)=2k+3,
    v=(3^(r-1)u-1)/2^(2k+3),                           (6)

then v is positive odd, C=2^(2k+1)v, and (3) gives

    T^(r+2k+4)(N)=T(M)=E,
    M=3^(k+1)v, E=(3^(k+2)v+1)/2,
    original word 1^r(01)^(k+1)00.                    (7)

The necessary and sufficient original-root order test is

    [2^(r+2k+3)-3^(r+k)]v > 3^(r-1)-2^r.              (8)

Indeed multiplication of N-M by 3^(r-1) gives the left side of (8) minus
its right side. All endpoints are ordinary positive integers before this
order test is imposed.

For EVERY r in {2,3,4,5}, EVERY k>=0, and EVERY positive odd u satisfying
(6), (8) is AUTOMATIC. No further dyadic gate is required. To see this, use

    M=(3/4)^k(3^r*u-3)/8 <= (3^r*u-3)/8 < 2^r*u-1.

The strict inequality follows from (8*2^r-3^r)u>5, valid for these four r.
Some of these certificates also descend on the original arm; do not label
all of them as genuinely no-forward-descent mergers.

Thus EVERY hypothetical least counterexample with an odd-valuation first
H parameter must have r>=6 and must satisfy the complement of (8). This is
an actual all-source exclusion within a specified stratum, rather than an
existence statement about one favorable subclass at each valuation.

Dropping (8) is false: N=191 has r=6,u=3,k=0 and the true identity

    T^10(191)=T(273)=410.

But 273>191, so it is NOT a smaller-original-source certificate. The verifier
retains this countercontrol. Positivity and physical legality do not repair
an order failure.

## FSS-004. Unbounded first runs and valuations, with no displayed descent

For every r>=5, choose the least integer k>=0 such that

    lambda = 3^(r+k)/2^(r+2k+3) < 1.                  (9)

It exists because increasing k multiplies lambda by 3/4. For r=5 it is
k=0, lambda=243/256. For r>=6, minimality and k>=1 give

    3/4 <= lambda < 1.                               (10)

Both r and these chosen k are unbounded as r increases. Define

    beta=3^(k+1)/2^(2k+3), 0<beta<=3/8.

On every compatible source in (6),

    M=lambda*(N+1)-beta,
    E=(3lambda/2)N+(3lambda-3beta+1)/2.                (11)

Equation (10) implies E>N. Since lambda<1, all sufficiently large compatible
N also have M<N. A computable exact threshold is supplied by (8), whose
coefficient of v is positive under (9).

There are infinitely many compatible N, and we may simultaneously require
3 divides N. In detail, put Q=2^(2k+4), select

    3^(r-1)u=1+Q/2 modQ,
    2^r*u=1 mod3.                                    (12)

The first class is odd; Q and 3 are coprime, so CRT gives one class modulo
3Q. Taking a sufficiently positive tail enforces (8). This does not choose
the future of a fixed N: it proves the stated infinite-family theorem,
separate from the pointwise use of (8).

For every member of that positive tail, EVERY positive-time state on the
entire original arm of (7) is above N. In fact its exact minimum is E.
The first r odd steps increase, and their first value T(N) exceeds T(M)=E
because M<N and both are odd. The next state (3^r*u-1)/2 is
12*4^k*v+1>E. In the remaining H tail all valleys are above the final E:
a valley during the j-th 01 block is 9*4^(k-j)*3^j*v+1 for 0<=j<k;
the last two halvings descend from 18*3^k*v+2 to E. These comparisons are
strict. This proves the whole-arm assertion, not just the final inequality.

If 3 divides N, its only positive depth-b pure ancestor is 2^b*N: an odd
inverse into any multiple of three is impossible, and the even inverse
preserves divisibility by three. Therefore the family has no smaller pure
ancestor at any depth either.

### Small whole-cylinder instance

For EVERY integer t>=0:

    N=1536t+1311, M=1458t+1245, E=2187t+1868,
    T^9(N)=T(M)=E, original word 111110100,
    0<M<N<E=min_(1<=j<=9) T^j(N), and 3 divides N.      (13)

At t=0 the previous #130 selector is OUTSIDE at C=830. The new certificate
uses M=1245, not the old prescribed companion. We do not claim the parent
selector fails on every t of (13). This family trades companion compression
for a much shorter companion clock and whole-stratum coverage: M is not
below N/2. The older compressed-companion results keep their own advantage.

## FSS-005. Consecutive actual comparison types and a root-safe restart

At the hard entry (5), let

    z=T^(r+1)(N)=(3^r*u-1)/2=6C+1,
    s=v2(z+1)>=1, v=(z+1)/2^s.

If 3^s*v=1 mod4, the credited good-exit identity at z gives

    T^(r+s+3)(N)=T^(s+1)(3C),                         (14)
    upper word 1^r 0 1^s 00,
    lower word 1^(s-1)01.

For EVERY r in {2,3} the source 3C=(3^r*u-3)/4 is positive and below
N=2^r*u-1. Thus ALL actual second-good-exit cases in these two first-run
classes are covered, with no bound on s. This is an original-root-safe
application of the old good-exit lemma, not priority for the lemma itself.
For r>=4 the displayed companion need not be below the original N; the
unqualified extension is not asserted.

Example: T^9(411)=T^5(231)=587, with actual words 110111100/11101 and
minimum positive-time original state 463>411. The parent selected H
language is OUTSIDE at its C=77. This handles an odd C, complementary to
FSS-002's even C of odd valuation.

### The complementary exit is an actual next H comparison

For ANY r>=2, not just r=2,3, if instead 3^s*v=3 mod4, set

    D=(3^(s-1)*v-1)/4 > 0.

The two actual arms satisfy

    T^(r+s+3)(N)=H(D), T^(s+1)(3C)=D.                 (15)

Thus for r=2,3 the restart is a TOTAL finite merge-or-H rule with another
smaller ORIGINAL companion, irrespective of the second exit. It is not a
total successful rule. For larger r, (15) remains a true identity without
an automatic smaller-source claim for 3C.

Now if v2(D)=2h+1, write D=2^(2h+1)w, w positive odd. For EVERY such actual
input, FSS-002 immediately supplies

    T^(r+s+2h+5)(N)=T(M'), M'=3^(h+1)w,               (16)
    original word 1^r 0 1^s (01)^(h+1)00.

Accept exactly when M'<N. This last criterion is valid even for r>=4:
there is no need to pretend the intermediate source 3C was smaller.
The entire composition is physical and keeps N fixed. The experiment
includes this SECOND_VALUATION rule before the bounded BAND scan. Repeated
compositions are possible, but no proof forces a successful order test
at some later comparison.

## FSS-006. Finite pointwise experiment, and what still fails

The deterministic original-source grid is EVERY N=2..65536, not the earlier
C=1..65536 grid. The baseline uses immediate even/mod4 descent, the credited
good first exit, and the exact hash-pinned #130 selector after hard entry.
Every old success retains exactly its original companion, words and clocks.
On a baseline failure the extension tries (7) with (8), then (14), then (16) with its order test, then
FSS-001 on the next at most 64 actual steps from the immutable N. The last
search stops at first y<=N and does NOT count such a descent as a new splice.
No new source digits are selected by this procedure.

On the SAME 65,535 original inputs:

| Outcome | Frozen baseline | Extension |
|---|---:|---:|
| Merger certificates | 58,157 | 62,978 |
| No certificate in this specified language | 7,378 | 2,557 |

There are 4,821 additions: 2,135 VALUATION, 1,345 RESTART, 442 SECOND_VALUATION, 899 BAND.
Exactly 1,648 additions have strict no-forward-descent on the entire displayed
original arm. Among the 2,557 remaining outcomes, 2,498 reach a descent or
return before the BAND rule succeeds; 59 exhaust its 64-step horizon.
These are certificate-language results, NOT a convergence census or a
fraction of hypothetical least counterexamples eliminated. No comparison
against the union of every other project rule is claimed.

The full corpus has 66,112 rows: these 65,535 source cases and 577 WHOLE
positive affine families (81 templates, 260 short-run strata, 76 unbounded
no-descent CRT families, 160 second-run restart families). The symbolic
checker validates all parameters t>=0, not only sampled members. Bounded
family indices do not prove the unbounded theorems; the proofs above do.

The standalone verifier imports neither the generator nor a repository
module. It rebuilds actual paths, full affine numerators and denominators,
all-state minima, all new selector decisions including OUTSIDE outcomes,
and exact finite inventory. The parent OUTSIDE decisions are hash-
authenticated against the frozen generator run, NOT independently
reclassified. Old positive certificates are independently replayed.
Normal/optimized generator and normal/-O/-OO verifier results are documented
in the execution receipt. Semantic/type controls are direct row mutations,
not separately resealed full-corpus mutations or mathematical peer review.

### Remaining global gap and a retained pointwise failure

The next missing theorem is still actual entry into an original-root-safe
splice or a valid companion restart. FSS-003 removes entire specified strata;
it does not cover odd C in general, even v2(C), or failed original-root
inequalities. A permanent escape through those complementary regimes is not
excluded. The clock budgets in #130 do not automatically apply to arbitrary
new companions, nor force the actual trajectory to revisit certified charts.

N=27 remains OUTSIDE in this experiment: its first smaller actual state is
23 at time59, with no earlier one-step band hit. This is not a counterexample
to Collatz; it is a countercontrol to the claim that the new one-step splice
must precede ordinary descent on every input. Exhausting 64 steps is likewise
not evidence of a permanent escape. No universal termination, no density-one
statement and no complete resolution is claimed.
