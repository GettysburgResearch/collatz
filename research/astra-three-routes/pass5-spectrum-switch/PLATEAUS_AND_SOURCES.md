# Equal-rank orientation and complete lower-witness lists

**Status: PROPOSED pending independent review.** This is the source-separation
attack of pass 5 and a new termination interface. Full lower-witness coverage
is OPEN. A bounded search labelled unresolved is not a counterexample.

Use A and R from pass 4. A(n) is the maximal repeated word w_a=1^a0, with
a=0 for an even n and a=v2(n+1) otherwise. The numerical map contracts for
a=0,1 and expands for a>=2, when n>1.

## 1. T-A3-1051: an equal-rank step must increase the ordinary number

For n>1,

    R(A(n))=R(n) implies A(n)>n.                       (1)

This does not claim that 3->4 is the only equal-rank step at all heights. That
is the only one in the present finite census. The universal assertion is its
direction, which suffices to rule out equal-rank cycles.

### Rank-fiber coordinates

Let the common rank be m>0, e=v3(m), and Z=sqrt(m*3^e). This is an integer.
Every positive source of rank m belongs to

    Z, Z+1, Z-5,
    n_i=(Z-c_i)/d_i, 3<=i<=e,
    d_i=3^i-2^(i+1), c_i=3^i-2^i.                     (2)

Nonintegral, nonpositive and nonminimizing entries are discarded. For i>=3,
any retained n_i has h(n_i)=i and n_i<Z-5, since z_i(x)>z_2(x)=x+5 on x>0.
All non-first entries have parity opposite to Z. These are properties of the
complete parent fiber list, not assumptions that its candidates all occur.

It suffices to exclude equal rank when the active mode is 0 or 1.

### Case a=0: maximal halving

Write y=A(n)=n/2^k, k>=1, with y odd. If n is a non-first entry of (2), its
evenness makes Z odd. Every non-first possible endpoint is then even, so y
would have to be Z. But n<=Z+1 and n/2<Z for Z>1. The remaining Z=1 case is
n=2->1, where rank is not equal.

If n=Z, then v3(n)=e and v3(y)=e. An endpoint with moving index i>=3 is
impossible: e>=i would make y divisible by 3, whereas h(y)=i requires y=1
modulo 3. If e=0 such an index is already forbidden by i<=e. The fixed target
Z+1 is larger than n and Z itself gives no strict halving. Only Z-5 remains.
Its equation is

    (2^k-1)Z=5*2^k.

Coprimality implies 2^k-1 divides 5, so k=1, Z=10 is the only possibility.
But the proposed component ranks are not the actual envelope ranks:
R(10)=9, R(5)=16. Thus no contracting equal-rank step occurs in mode zero.

### Case a=1: repeated 10

Here y=1+(3/4)^k(n-1), k>=1, and y<n. A moving target index i>=3 is impossible.
Indeed, if e=0 the fiber condition already forbids it. If e>0, each possible
source in (2) has n+1 a ternary unit: n=Z is 0 modulo 3, the fixed other
entries are 1 modulo 3, and every moving entry has h(n)>=3. Each repeated 10
therefore leaves h(y)=1, also forbidding a moving target. Thus y is one of
the three fixed entries Z,Z+1,Z-5.

If the source is Z-5 or a smaller moving entry, no smaller target remains.
For n=Z, only y=Z-5 is possible, giving

    (4^k-3^k)(Z-1)=5*4^k.

As gcd(4^k-3^k,4)=1, its denominator divides 5. For k>=2 it is at least 7
and increasing, so k=1,Z=21. But R(21)=147 and R(16)=75, not equal.

For n=Z+1 the two smaller targets give respectively

    (4^k-3^k)Z=4^k,
    (4^k-3^k)Z=6*4^k.

Again k=1 is the only possibility. They yield n=5,y=4 and n=25,y=19.
Their actual ranks are (16,3) and (192,36), not equal. This exhausts all
contracting modes. Every a>=2 expands, proving (1). QED.

## 2. T-A3-1052: turn all nonincreasing rank steps into strict descent

Define the explicit nonnegative integer refinement

    Phi(n)=R(n)^2+R(n)+1-n.                            (3)

Phi(1)=0 and Phi(n)>=R(n)^2>0 for n>=2, by R(n)>=n-1. If R drops, the
intervals of possible Phi for successive rank values are disjoint and ordered:
for rank r the lower endpoint is r^2; at rank r-1 the upper endpoint is less
than r^2. If R stays equal, (1) makes the last term -n strictly decrease.
Therefore

    n>1, R(A(n))<=R(n) implies Phi(A(n))<Phi(n).        (4)

This proves more than checking flat edges up to a numerical floor. It orients
all flat edges at arbitrary heights. It does not orient the rank-increasing
edges, which genuinely exist.

Let G={n>1:R(A(n))<=R(n)}. Iteration while the current source is in G is total:
Phi strictly decreases and no source repeats. All its nonabsorbed sources
lie in the initial sublevel R<=R(n). The rank-spectrum theorem now yields

    number of A steps before reaching 1 or leaving G <= 9 sqrt(R(n)).     (5)

Each step costs at most 3 log_2(R(n)+6) shortcut steps, so its shortcut clock
is at most 27 sqrt(R(n)) log_2(R(n)+6). Integer upper bounds can replace the
real quantities in an implementation. This expands the parent quarter-drop
region; its universal clock is correspondingly weaker, not logarithmic.

## 3. T-A3-1053: complete spatial search, without pretending clocks are bounded

For a given n>=2 let M=R(n). Every x with Phi(x)<Phi(n) belongs to

    {1} union {x>=2:R(x)<=M},                          (6)

and within rank M it must have x>n. By the complete spectrum enumerator,
(6) is a finite list with at most 1+9 sqrt(M) entries. It is a complete list
of possible smaller-refined-rank witnesses, not merely a set of convenient
congruence classes. Every member is an ordinary integer.

For a specified finite clock cap J, inspect T^r(n)=T^s(x), 0<=r,s<=J,
for all candidates. This exactly decides all lower-Phi merging diagrams with
both clocks within that cap. Empty words and the trivial cycle are included.
Do not bound intermediate vertices by M: only the candidate source is bounded.
Temporary growth can occur on either leg.

A successful diagram preserves convergence status and strictly lowers Phi.
Thus a deterministic procedure that takes any certified diagram and repeats
is well founded. It can halt at 1 OR at an explicitly unresolved source when
no tested diagram exists. A proof that every unresolved source has a diagram
selected by a PROVED TOTAL rule would finish Collatz, including cycles.
That complete temporal cover is not supplied.

This is a spatial improvement, not a concealed halting theorem. Increasing J
until a meeting occurs without proving that it occurs is not a complete
algorithm. The conditional minimum-rank implication was already present in
pass 4 and the neighboring PR #90; it is not claimed new here.

## 4. Exact bounded evidence and what it refutes

At n=2,...,16384, 13459 sources lie in G, versus 10505 in the old quarter-drop
region. The only sampled equal-rank edge is 3->4. Iterating G alone sends 294
inputs to 1 and 16089 to a labelled unsafe source. Its largest sampled length
is ten A modules; the proof of (5), not that maximum, is universal.

The complete J=6 merging test is performed at ten named sources. The generator
enumerates all lower-Phi sources using (6) and follows them forward. The
independent verifier instead builds the full inverse trees at each endpoint
of the n leg. Their complete diagram counts agree. Sources 9,27,703,2223
remain unresolved at these particular clock caps. All are labelled unresolved,
not exceptional. These are NOT claims of unrestricted minimal diagram depths.

The mass route can remove every finite G excursion using the analytic bound
in [INDUCED_MASS.md](INDUCED_MASS.md). The constructive route supplies new
certified transitions across some rank increases in
[SWITCH_REPAYMENT.md](SWITCH_REPAYMENT.md). Neither result establishes coverage
of the remaining unsafe process.
