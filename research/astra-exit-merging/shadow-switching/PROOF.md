# Shadow switching: remove the missing seed and compress the companion

**Status: PROPOSED pending independent mathematical review.**
Date: 2026-09-20. Programme: issue #121. Parent: PR #124 at
`1d4dfc103055648def3db73860778a383a91ea3c`.
New statements AES-001--006 have no inherited mathematical acceptance.
No complete Collatz proof or external priority claim is made.

Use raw shortcut T(n)=n/2 for even integers and (3n+1)/2 for odd integers.
Positive paths stay positive. Raw T continues through 1 -> 2 -> 1; absorption
is a separate convention, not a way to manufacture equal-clock meetings.
A word records actual parities in chronological order, with an empty word
allowed when a certificate's smaller source already is its endpoint.

## 1. AES-001: compare different periodic centres, not only different slopes

Let a physical negative periodic word w return -c to itself, with c>1,
length L and q odd steps. For integers k,u>=1 suppose

    n=2^(Lk)u-c > 0,    m=2^(qk)u-1 > 0,    m<n.

Then both following prefixes are physical and

    T^(Lk)(n)=3^(qk)u-c,
    T^(qk)(m)=3^(qk)u-1.                              (1)

The repeated word on n is w^k; the word on m is 1^(qk). Moreover

    m=(n+c)/2^((L-q)k)-1.                             (2)

In particular, if 2^((L-q)k)>c, then m<n/2^((L-q)k).
This is a comparison of prefixes, NOT yet a merger or a convergence result.

**Proof.** Along the known negative path, a positive start differing from
-c by 2^(Lk)u differs at time j by 3^(q_j)2^(Lk-j)u. For j<Lk this is even,
so its next parity agrees with the negative path. Induction proves the
entire positive word and the first identity. Positivity also follows from
ordinary forward iteration from n>0. For m, after j<qk odd steps the value
is 3^j2^(qk-j)u-1, which is odd and positive. This proves the other identity.
Equation (2) and its inequality are algebra. No ordinary infinite negative
or positive realization is inferred from a compatible finite word.

### The 110 case

The physical negative cycle is -5 -> -7 -> -10 -> -5, with word 110.
Thus for n=8^k u-5, compare the new **odd-spine** companion

    m=4^k u-1,     T^(3k)(n)=9^k u-5,
                  T^(2k)(m)=9^k u-1.                 (3)

For odd u>=1 the only failure of m<n is k=u=1, when both are 3. This input
has the separate certificate T^5(3)=1. Every other input in this family
has a smaller m; for k>=3 it satisfies m<n/2^k. For k=1,2 that last stronger
inequality is NOT asserted: the exact formula is m=(n+5)/2^k-1.

The sources now follow DIFFERENT repeating words and DIFFERENT clocks.
The old same-centre ansatz m=a*8^(k-1)u-5 could not supply this compression.

## 2. AES-002: a direct merger for dyadic gaps, including another period

Assume AES-001 and c-1=2^d. Put Y=3^(qk)u and impose the exact guard

    Y = c+2^(d+2) mod 2^(d+3).                       (4)

Then Q=(Y-c)/2^d is a positive integer congruent to 4 modulo 8. After d
halvings, the pair in (1) is (Q,Q+1). Write Q=4b with b odd positive. The
physical tails 001 from Q and 100 from Q+1 meet at (3b+1)/2. Hence

    T^(Lk+d+3)(n)=T^(qk+d+3)(m)
      =[3(Y-c)+2^(d+2)]/2^(d+3).                    (5)

The words are w^k 0^d 001 and 1^(qk) 0^d 100. This proves every asserted
parity, the independent clocks, positivity and the original-source order.

If every nonempty prefix of w has coefficient 3^(q_j)/2^j>1, and

    3^(qk) >= 2^(d+2) 2^(Lk),                       (6)

then EVERY positive-time state on the entire n-arm of (5) is above n.
Indeed all prefixes of w^k have coefficient greater than one and nonnegative
affine correction. On the remaining arm the minimum is (Y-c)/2^(d+2).
Subtracting n from that value gives

    [(3^(qk)-2^(Lk+d+2))u+c(2^(d+2)-1)]/2^(d+2)>0.

The prefix hypothesis matters; it is not asserted for every negative cycle.

### Two explicit, unbounded instances

* c=5, w=110, d=2: if 9^k u=21 mod32, then

      T^(3k+5)(8^k u-5)=T^(2k+5)(4^k u-1)=(3*9^k u+1)/32.

  All prefixes satisfy the coefficient hypothesis, and (6) holds for k>=24.
  In the parent's seed variable v=9^(k-1)u, the guard is **v=13 mod32**.
  The parent assigned this class to an H return; this is a direct merger
  for the WHOLE class, whether that return would have succeeded or failed.

* c=17, w=11110111000, d=4: direct negative replay is

      -17,-25,-37,-55,-82,-41,-61,-91,-136,-68,-34,-17.

  Here L=11,q=7. If 3^(7k)u=81 mod128, then

      T^(11k+7)(2^(11k)u-17)
        =T^(7k+7)(2^(7k)u-1)=(3*3^(7k)u+13)/128.

  The prefix inequalities again hold, and (6) holds for k>=64. The companion
  is below n/2^(4k) for k>=2. At k=64 the supplied example is a 712-bit
  source and a 456-bit companion, meeting at clocks 711/455 while the whole
  original arm stays above its source. This is a second application of the
  same conditional algebra, not a classification of negative cycles.

For either instance and each k, the dyadic guard is one odd residue for u.
It can be combined by CRT with 2^(Lk)u=c mod3. Thus infinitely many sources
are divisible by three. At such a source the only depth-j positive ancestor
is 2^j n: the odd inverse (2n-1)/3 fails integrality and every even inverse
preserves divisibility by three. Consequently these two-sided certificates
can coexist with no smaller pure ancestor at any depth and no forward
descent anywhere on the certified arm. Later forward descent is not excluded.

## 3. AES-003: a contracting adjacent comparison, with its fixed-point exception

For q=4b+1, b>=1, the pair (q+1,q) has physical words

    upper: 01,    lower: 10,

and becomes (q'+1,q'), where

    q'=(3q+1)/4=3b+1,
    q'-1=(3/4)(q-1),
    v2(q'-1)=v2(q-1)-2.                              (7)

This follows by the two paths

    4b+2 -> 2b+1 -> 3b+2,
    4b+1 -> 6b+2 -> 3b+1.

Orientation is preserved, and both arms advance two shortcut steps. If
v2(q-1)=2s, exactly s repetitions reach an EVEN adjacent parameter; before
then every required parameter is 1 mod4 and larger than one. This is a
finite procedure because it consumes a finite valuation of the GIVEN q.

At q=1 the pair is (2,1); (7) has a fixed point and its two raw trajectories
never merge synchronously. That exception is excluded, not silently absorbed.
With odd v2(q-1), the same process ends at q=3 mod4, outside this particular
lemma's useful exit. The choice in the next section prevents that endpoint.

## 4. AES-004: the entire missing odd seed class has a finite entry

Let

    n=8^k u-5,   k>=1, u positive odd,
    v=9^(k-1)u=1 mod16,   v>1,
    t=v2(v-1)>=4,   w=(v-1)/2^t positive odd.

Choose the companion according to the parity of t, not by prescribing a
future parity word for an arbitrary different source.

### Odd t: keep the same-centre companion, with a newly completed exit

Put

    m=(3n-5)/4,   s=(t-1)/2,
    q_A=(9v-7)/2=9*2^(t-1)w+1.

The physical prefixes (110)^k 0 and (110)^(k-1)10 reach (q_A+1,q_A) at
clocks 3k+1 / 3k-1. The parent's adjacent seed identity proves this; directly
substitute odd v into 8v-5 --1100--> (9v-5)/2 and
6v-5 --10--> (9v-7)/2. Since v2(q_A-1)=t-1=2s, append (01)^s and (10)^s.
The pair reaches (Q+1,Q), where

    Q=3^(s+2)w+1 is positive even.                    (8)

The clocks are 3k+1+2s and 3k-1+2s. Here 0<m<3n/4.

### Even t: switch to the odd-spine companion

Put

    m=4^k u-1,   s=(t-2)/2,
    q_B=(9v-5)/4=9*2^(t-2)w+1.

By (3), (110)^k 00 and 1^(2k)00 reach (q_B,q_B+1). Both halvings on each
arm are legal because v=1 mod16. Now v2(q_B-1)=t-2=2s. Append (10)^s to
the ORIGINAL arm and (01)^s to its companion. They reach (Q,Q+1), with
Q given by (8), at clocks 3k+2+2s and 2k+2+2s.

The orientation is reversed relative to the first case. The original source
names are not exchanged. This m is positive and smaller than n by AES-001;
when k>=3, m<n/2^k.

### Complete finite entry, not complete successful coverage

For every positive even Q, the following elementary physical exit is total:

* v2(Q)=2: words 100 / 001 from (Q+1,Q) merge.
* v2(Q)>=3: words 101 / 000 reach H(C)=(9C+2,C), C=Q/8.
* v2(Q)=1: put b=Q/2, a=v2(b+1)>=1, d=(b+1)/2^a, B=3^a d-1.
  After one step and a odd steps the pair is (3B+2,B).
  If B=2 mod4, append 00 / 01 and merge.
  If B=0 mod4, append 01 / 00 and reach H(B/4).

In the third case the complete words are 1^(a+1)00 / 0 1^a 01 for a merger,
and 1^(a+1)01 / 0 1^a 00 for a return. All clocks are finite and all states
positive. These are the credited AAC even-adjacent exits, recalled in full.
For the reversed pair (Q,Q+1), exchange the two words, not the original roots.

Thus EVERY source in the previously missing class reaches a merger OR an
explicit H pair in finite time. The remaining case v=1 is exactly k=u=1,
n=3, handled by T^5(3)=1. No source is dropped to avoid that endpoint.

Together with the parent's other seven odd seed classes, this gives a
finite merger-or-H entry for EVERY k>=1, odd u>=1. The sources outside this
representation, H states outside its next guard, and infinite hard-return
itineraries remain unresolved. Returning an H pair is NOT a successful
merger and is not counted as one.

## 5. AES-005: original-root certificates on the new seed, with an all-states bound

In AES-004, impose the additional exact guard Q=4 mod8. The terminal
adjacent exit has length three and endpoint E=(3Q+4)/8. For odd t,

    T^(3k+4+2s)(n)=T^(3k+2+2s)((3n-5)/4)=E.           (9)

For even t,

    T^(3k+5+2s)(n)=T^(2k+5+2s)(4^k u-1)=E.           (10)

Both t and k are unbounded. These identities control an expanding 110
prefix, its actual exit, an arbitrarily long contracting adjacent phase,
and the final merger, without changing the original-source comparator.

### Exact non-vacuity for every k and t

Set s as in AES-004 and choose the odd representative

    d0=3*3^(-(s+2)) mod8.

The desired v has the exact class

    v=1+2^t d0 mod2^(t+3).                            (11)

It forces v2(v-1)=t and Q=4 mod8, not merely lower bounds on those valuations.
For each k solve (11) for u through v=9^(k-1)u and also impose

    u=epsilon mod3,    epsilon=1 for odd k, 2 for even k.

CRT gives one positive odd class modulo 3*2^(t+3). Every member has n=3 mod12,
so n has no smaller pure ancestor. Varying t or k changes the prescribed
finite source family; it does not force an arbitrary source's future.

### No forward descent along the WHOLE original arm

A sufficient condition for every positive-time state on the arm in (9) or
(10) to exceed n is

    3^s 9^k >= 2^(t+2) 8^k.                          (12)

To prove it, all states during the first k expanding 110 blocks exceed n.
Thereafter every state on the original arm is at least Q/4. In the odd-t
case a 01 contraction may dip below its adjacent lower parameter, but it
stays above half that parameter, hence above Q/4. In the even-t case each
10 contraction has its minimum at its endpoint; the final 001 tail has
minimum Q/4. The initial post-burst halvings obey the same bound. Finally,

    Q/4-n = [3^s 9^k/2^(t+2)-8^k]u
            +5+(1-3^(s+2)/2^t)/4 > 0.

The coefficient is nonnegative by (12). The constant is positive: for
all t>=4 in the two cases, 3^(s+2)/2^t<=81/32. This proves the strict bound.
For t=4,5,6,7 the least sufficient k are 26,23,29,25 respectively. These
are thresholds for (12), not asserted universally optimal thresholds.

Example, k=26,u=137,t=4,s=1:

    n=41405709321801049233686523,
    m=616993148949757951,
    T^85(n)=T^59(m)=62238390386066313887370728,
    min_(1<=j<=85)T^j(n)=41492260257377542591580485 > n,
    2^26*m<n,    n=3 mod12.

The parent's selector returns OUTSIDE_SEED here. This new certificate has
no forward descent on its displayed arm and no smaller pure inverse at n.
It does not assert that m is already covered by this selector or that all
future trajectories stay in this class. It excludes n from being a least
counterexample by the usual strong-induction reasoning, not by assuming
convergence for an unbounded sequence of larger intermediate states.

## 6. AES-006: every finite hard-return pattern can also follow the new entry

For completeness, retain the exact H return: at C=2^(r+1)b-2, r>=3,
after r+3 steps on EACH arm, (9C+2,C) either merges if 3^r b=1 mod4, or
becomes (D,9D+2) if 3^r b=3 mod4, D=(3^(r-1)b-1)/4. A hard return swaps
orientation. Its words are 0000 1^(r-3)01 / 0 1^r 00 in the merging case,
and 0000 1^(r-3)00 / 0 1^r 01 in the hard case. The derivation and growth
thresholds are in the parent hard-return packet; none is strengthened here.

For every finite list r1,...,rJ>=3, hard at the first J-1 and merge at the
last, the exact H compiler gives C=c modM, M=2^sum(ri+3). A self-contained
backwards step is: at a hard label put d=2^(r+3), b0=3^(r+1) mod4,
c0=2^(r+1)b0-2, D0=(3^(r-1)b0-1)/4. If the suffix class is c modM,
replace c by c0+d*((c-D0)*3^(-(r-1)) modM) and M by dM. The final merging
class uses b0=3^r mod4. Odd multipliers make each class complete by induction.

To enter it from AES-004, impose Q=8C. Equation (8) becomes

    3^(s+2)w+1=8C,
    w=(8c-1)*3^(-(s+2)) mod8M.                        (13)

This is an odd class. Thus v=1+2^t w has a dyadic class modulo 2^t*8M.
Solve v=9^(k-1)u there and impose the same modulo-three condition as above.
This supplies infinitely many ordinary positive original sources for EVERY
k>=1, t>=4 and every finite label list, all in the newly completed v=1 mod16
seed. In particular lists (8,...,8,4) supply arbitrarily many expanding H
returns, but no infinite ordinary itinerary is extracted from finite lists.

Append the orientation-aware H words to (9)/(10)'s prefix, replacing the
final direct-merger tails by 101 / 000 (or reversed). The added clock is
R=sum(ri+3). The total clocks are those in (9) or (10) plus R on each arm.
The companion remains the SAME original m<n; for the even-t case with
k>=3 it remains below n/2^k, regardless of intermediate growth.

The all-states bound (12) is proved for the DIRECT merger in Section 5,
not automatically for these extended H itineraries. The code and claims
keep that distinction. No new repeated-return mass estimate is inferred.

## 7. What this does and does not close

The missing seed v=1 mod16 has no remaining undefined entry in this
selector. That is a structural all-parameter statement, stronger than adding
a finite table of successful inputs. A second negative periodic centre also
produces a different unbounded family through the same general gap theorem.

Nevertheless the complete method still returns OUTSIDE_RETURN or a bounded
BUDGET result for some inputs. For example:

    n=643, m=323: new even-t entry reaches (17,155)=reversed H(17);
    n=1795, m=1345: new odd-t entry reaches (641,71)=H(71).

Both have r=v2(C+2)-1<3. These are failures of THIS selected continuation,
not divergent inputs or a proof that no other certificate exists. Some such
inputs even have direct ordinary descent on the displayed arm; the bounded
selector intentionally does not claim optimality or exhaust all alternatives.

On the complete former grid, every old merger remains a merger. This is also
algebraic: old non-v=1 seed cases are unchanged except v=13 mod32, where the
new direct theorem replaces an H return with an unconditional merger in its
guard. The former missing class had no old successful outputs to lose.

The remaining all-source task is still an unavoidable ORIGINAL-ROOT-compatible
successful cover. Finite entry into H, finite residue compatibility and an
infinite collection of finite certificates do not supply it. All equations
here have finite ordinary witnesses and independently recorded arm clocks;
no statistical density or local decrease is substituted for that quantifier.
