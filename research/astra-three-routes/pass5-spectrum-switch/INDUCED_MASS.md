# Route 1: full safe-excursion control, then an actual induced-kernel obstruction

**Status: PROPOSED pending independent review.** The natural rank-weight
attempt is pursued to its end-to-end criterion and explicitly refuted as a
global pointwise supersolution. A different weight or an aggregate estimate
may still work. Collatz and the earlier fixed-floor survivor bound remain open.

## 1. The process that really remains after safe states are removed

Use R and A from pass 4 and the enlarged region

    G={n>1:R(A(n))<=R(n)}, U={n>1:R(A(n))>R(n)}.

The equal-rank theorem in [PLATEAUS_AND_SOURCES.md](PLATEAUS_AND_SOURCES.md)
makes every G excursion finite, without an unproved stopping-time oracle.
For u in U, apply A once, then keep applying A only while the current state
is in G. Define J(u) to be the resulting member of U, or the absorbing 1.
This is a total, exact induced map. It can consume an unbounded number of
shortcut steps, but every individual evaluation is proved finite.

Every exceptional positive orbit reaches U and returns there infinitely often.
Otherwise its final G excursion would be infinite, contradicting the finite
rank-sublevel bound. Hence convergence of all J orbits to 1 would establish
Collatz, including the exclusion of nontrivial cycles. Conversely Collatz
would make all these induced orbits converge. This is the exact end-to-end
interface; it does not by itself prove any J-orbit convergent.

## 2. T-A3-1003: a complete, polynomial safe-resolvent tail

Let K_G push a nonnegative mass forward along A, killed on first arrival at 1
or outside G. Take f supported on G with

    0<=f(n)<=C R(n)^(-p), p>1/2.

A source that survives r steps has r+1 distinct states in its initial rank
sublevel. The spectrum bound gives R(n)>=(r/9)^2. For r>=9, therefore,

    ||K_G^r f||_1
       <= [9p/(p-1/2)] C (r/9)^(1-2p).                 (1)

No mass is reinitialized after transport; this bound is obtained by pulling
the surviving sources back to their original weights. The exact deterministic
pushforward has no source multiplicity in that accounting.

At p=2,

    ||K_G^r f||_1 <= 8748 C/r^3, r>=9,
    sum_(r>=L) ||K_G^r f||_1 <= 4374 C/(L-1)^2, L>=10. (2)

These are all-source AND all-residence bounds for G, with an explicit entire
omitted tail. The second follows by integral comparison of sum r^(-3).
They are not bounds on residence in the unsafe process U. For 1/2<p<=1 the
estimate (1) is not summable in r; that says this particular upper bound does
not certify a finite resolvent, not that the actual resolvent diverges.

The earlier quarter-drop result had an exponential tail on a smaller region.
Here ALL nonincreasing steps, including flat-rank steps, are retained. A
polynomial clock and tail are the price of this strictly larger safe region.

## 3. The global candidate and the exact sufficient criterion

For a positive weight w on U, define the killed induced inverse operator

    (L_J w)(y)=sum_(u in U, J(u)=y) w(u), y in U.

If sum_U w<infinity and L_J w(y)<w(y) for every y in U, then Collatz follows.
Indeed the exceptional part E_U, if nonempty, is forward and backward
invariant under J. Nonnegative summation and finite total mass give

    sum_(y in E_U) L_J w(y)=sum_(u in E_U) w(u),

contradicting strict inequality at every member of a nonempty E_U. This is
the standard positive-mass criterion already used in PR #90 and earlier
passes, specialized to the newly well-defined induced map. No claim of
novelty is made for the abstract criterion.

The rank spectrum now makes

    w_p(n)=R(n)^(-p), p>1/2                            (3)

a concrete positive summable candidate on U, with certified tails. It is
natural to hope that removing every nonincreasing excursion repairs its
remaining pointwise drift. The following theorem disproves that hope for
the entire family (3), not just one finite choice of p.

## 4. R-A3-1004: reciprocal-rank weights fail even AFTER inducing

For every p>1/2,

    sup_(y in U, y>H) (L_J w_p)(y)/w_p(y)=infinity     (4)

for every fixed finite floor H. The same lower bound survives killing on
that floor along the actual physical path used below.

### Ordinary family and exact unsafe return

Take e=4 modulo 16, e>=4, and put

    x=3^e, y=(9x+7)/16.

The parent all-height power family gives A(x)=y with exact word (10)^2 and

    R(x)=x, R(y)=9(x-1)^2/256=(y-1)^2/9.               (5)

These identities can also be checked directly. For e=4 mod16, 3^e=17 mod64,
so y=2 mod4 and A(y)=y/2. Further y=1 mod3, so y/2=2 mod3. On that last
class h=0 and all three fixed valuation numerators are ternary units;
consequently

    R(A(y))=(y/2-1)^2.

For y>=46, 3(y-2)>2(y-1), so R(A(y))>R(y). Equation (5) also gives
R(y)>R(x) for x>=81. Thus BOTH x and y lie in U, and

    J(x)=y                                             (6)

with no hidden safe interior. The four physical shortcut steps stay at least
y, so every fixed floor is avoided for sufficiently large e.

The inverse operator at y includes the ordinary source x. Hence

    (L_J w_p)(y)/w_p(y)
      >= [R(y)/R(x)]^p
      = [9(x-1)^2/(256x)]^p -> infinity.

This proves (4). It is stronger than showing that one raw A edge fails: the
newly induced unsafe operator itself still fails for the whole pure-power
rank-weight family. Increasing a fixed floor does not repair it. No assertion
is made here about every fixed iterate of J or about more general weights.

## 5. Why the obstruction is not a Collatz disproof or an all-method no-go

The sources of the obstruction are summable:

    sum_(j>=0) R(3^(4+16j))^(-p)
       = 3^(-4p)/(1-3^(-16p)) < infinity.

So arbitrarily large pointwise ratios need not destroy an integrated estimate.
A compensating weight concentrated at the images is not ruled out; it must
pay for its later transport too. Simply replacing w by an unexplained
invariant envelope would assume the missing theorem.

The attempted full proof stops precisely here: (2) controls every safe
excursion, but (3) does NOT control the induced unsafe returns. The source
spectrum and the repayment theorem give explicit data for a different
construction. They do not certify its all-depth closure.

## 6. Complete-source finite enclosures

The experiment sums R(n)^(-2) for the actual G survivors among n<=16384,
rounding each term outward at precision 10^(-24). Every omitted n is covered
by the analytic source tail 12/(16384)^(3/2)=3/524288. It reports r=0,1,2,4,8,16.
Thus every displayed interval covers all positive sources at that finite r.
At r=16 no enumerated source remains, but the upper bound still contains the
nonzero omitted-source tail. That row is not a zero all-source theorem.
The uniform all-r estimate is the proof of (1)-(2), not a finite trend.

The checker also verifies thirteen exact witnesses in (4), up to e=196.
The proof covers every e=4 mod16 and every p>1/2. No expensive parent inverse
cone or external computation is replayed by this test.
