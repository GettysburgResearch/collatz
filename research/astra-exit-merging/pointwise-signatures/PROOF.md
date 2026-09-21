# Pointwise signatures, witness-preserving lifts, and forced slope escape

**PSS-001--004: PROPOSED pending independent mathematical review.**
Date: 2026-09-21. Parent: #132, `7687eec1ac364009d644cb8d015f1fe3b28730cc`.
This is not a full Collatz proof. The universal fixed-input restart remains OPEN.

Use the raw shortcut map T(n)=n/2 for even positive n and (3n+1)/2 for odd n.
In particular T(1)=2, T(2)=1. Words record source parities chronologically.
An empty word is allowed. For a word w with length L and q ones,

    T_w(x)=(3^q*x+A_w)/2^L,
    A_w=sum_(i:w_i=1) 2^i 3^(number of ones strictly after i).

A positive integer follows w exactly iff it is in the unique source residue
modulo 2^L. All finite witnesses below use positive ordinary states.

## Provenance and the change of question

The preceding ACS packet is already present in #132 at the stated head; its
proof blob is `5b6e729c219680081dc44f9048a418c5b535f7c9`. It is not republished
or modified. The existence classification of affine TEMPLATE families in #132
also has a parallel proof in #130/UFS at
`53cf9b53bd568b1ab67601b00e789b464198e42b`. No priority is asserted between them.
The #131/DS packet at `e092da549c8c50e8a9430f88fb721ea51fe34d91` already proves
that some positive H-pairs merge only at isolated ordinary points, never on a
uniform H cylinder containing that point. Its DS-005 first-meeting odd-count
criterion is credited, not claimed new here.

The present questions concern the ACTUAL point, not whether a nearby successful
subprogression can be constructed. PSS-001 gives the terminal signature version
for any finite affine collection of certified convergent starts; it does not
presuppose a stopping time for an arbitrary unverified integer. PSS-002 lifts
an existing numerical witness while keeping that very source in the family.
PSS-003 yields a strict first-escape family using a different smaller source.
PSS-004 is a quantitative necessary condition for a hypothetical least source,
including permanent escape from any bounded propagated derivative menu.

## PSS-001. A complete pointwise criterion on the convergent basin

### 1. Charge defined only when a finite core path is supplied

If n reaches 1, write sigma(n) for its FIRST arrival time, o(n) for the number
of odd steps before that time, and define

    chi(n)=2*o(n)-sigma(n).

Thus chi(1)=0 and chi(2)=-1. The function is not assigned a value at a source
whose convergence has not been established. In the experiment every value is
obtained from an explicitly bounded, literally replayed path.

If T^L(n)=E and E converges, with q odd steps in the displayed prefix, then

    chi(n)=2q-L+chi(E).                                  (1)

For prefixes ending before the first visit to 1 this is concatenation of the
first-arrival paths. If the prefix runs through the core, every complete 10
core loop contributes 2*1-2=0, and the intermediate state 2 has charge -1.
Hence (1) also holds in the unabsorbed convention.

For reference, with B_n(t)=2*q_n(t)-t, after the first visit to 1,

    B_n(t) = chi(n) + ((t-sigma(n)) mod 2).               (2)

Two convergent sources x,y meet at equal clocks iff sigma(x),sigma(y) have the
same parity. Sufficiency: at time max(sigma(x),sigma(y)) both are 1. Necessity:
a meeting propagates forever, whereas opposite core phases never agree.
This assertion concerns an individual pair, not a uniform affine cylinder.

### 2. Pointwise affine-family theorem

Fix a finite collection f_i(t)=A_i*t+B_i, A_i positive integers, and a prescribed
integer t_* such that every n_i=f_i(t_*) is positive and has a supplied finite
path to 1. Write

    A_i = c_i * 2^u_i * 3^v_i,  gcd(c_i,6)=1,
    eta_i = u_i + 2*v_i + chi(n_i).                      (3)

Then the following are equivalent:

(a) There are fixed finite physical words w_i that merge all f_i(t) on an
    infinite parameter progression CONTAINING t_*, and are legal at t_*.
(b) All c_i agree and all eta_i agree.

A progression containing the point may be written t=t_*+M*h, h>=0. Positivity
at t_* and positive slopes make all its sources positive. The theorem does
not merely construct a translated progression missing the prescribed point.

**Necessity.** Infinite affine equality forces equality of endpoint slopes:

    A_i*3^q_i/2^L_i = A_j*3^q_j/2^L_j.

Consequently c_i=c_j, L_i-L_j=u_i-u_j, and
q_i-q_j=v_j-v_i. At the prescribed point all endpoints are the same convergent
E. Substitution into (1) gives eta_i=eta_j.

**Sufficiency.** Suppose (b). Choose S>=0 so that L_i=S+u_i>=sigma(n_i) for all i
and S+eta_i is even. These parity requirements agree, since
eta_i=u_i-sigma(n_i) mod2. Follow each actual path to 1 and append exactly
(L_i-sigma(n_i))/2 copies of 10. All point endpoints are 1, and their odd counts
satisfy

    q_i+v_i=(S+eta_i)/2.

Thus all endpoint slopes A_i*3^q_i/2^L_i agree. Equality at t_* makes their
intercepts agree as well. On t=t_*+2^S*h, each original slope A_i*2^S is divisible
by 2^L_i, so every indicated word is physical on the entire progression. This
proves (a) constructively, using only the supplied finite convergence paths.

The forced clock difference is L_i-L_j=u_i-u_j. When c_i agree but eta_i differ,
there is no uniform certificate through the point at ANY future depth. If all
eta_i have the same parity, the actual starts do meet at the forced clock
differences, but only as an isolated point of those fixed affine templates.
If their parities differ, no numerical meeting at those forced differences
is possible at any time. Unequal, differently offset numerical meetings can
still occur. If c_i differ, the known slope obstruction already forbids any
infinite fixed-word affine equality, independently of the point.

### 3. H-pair specialization and all-depth finite census

For H(C)=9C+2, use slopes 9 and 1. The exact criterion is

    a uniform H-merger cylinder contains C
        iff chi(C)-chi(H(C))=4.                         (4)

All quantities in (4) require certified convergence at that C. This is the
terminal version of #131/DS-005: at a first synchronous meeting, lower odd
count minus upper odd count must be two; a subsequent common continuation
cannot change that discrepancy.

On EVERY C=1,...,65536, literal finite core paths were reconstructed. The exact
all-future classification is:

| Outcome for the fixed H relationship | All C | C=2 mod3 |
|---|---:|---:|
| Uniform cylinder containing the actual point exists | 13147 | 4357 |
| Synchronous numerical meeting exists, but every such uniform cylinder fails | 25865 | 8651 |
| No synchronous numerical meeting at ANY time | 26524 | 8837 |

The last two rows total 52389. No increase in a UNIFORM H-atlas depth can recover
these particular points while keeping that affine relationship. They are not
counterexamples to Collatz; all have the displayed convergence evidence.
The verifier independently finds the first literal meeting through the complete
core-arrival horizon, then applies the conserved odd-count test, rather than
using only the generator's charge formula. At every uniform point it also
checks a whole affine cylinder through that actual point.

For example C=128 has sigma(H(C))=23, o(H(C))=8; sigma(C)=7, o(C)=0.
Both charges equal -7. The phases agree, so the pair numerically meets, but
its charge difference is zero rather than four: it can never be a uniform
H-certificate point. C=17 and C=71 retain the earlier DS controls.

There are infinitely many elementary instances of the distinction. Since
chi(2^j)=-j, the translate templates (t+2^i,t+2^j), i!=j, have no uniform
merger cylinder containing t=0. For equal parity i,j they synchronize only
as an isolated point; for different parity they never synchronize. This is
not an assertion that their neighboring parameter classes also fail.

Neither chi nor eta is a proposed global rank. Their computation here already
requires a finite convergence proof, and chi(2^j)=-j is unbounded below.

## PSS-002. Every numerical witness has a primitive point-preserving lift

Suppose n0>m0>0 have a literally verified finite merger

    T^L(n0)=T^J(m0)=E,

with actual words w,z and odd counts q,p. Put

    A = 2^L * 3^max(p-q,0),
    B = 2^J * 3^max(q-p,0).                              (5)

Then for EVERY integer h for which n=n0+A*h and m=m0+B*h are positive,

    T^L(n0+A*h)=T^J(m0+B*h)=E+3^max(p,q)*h.             (6)

The words stay w,z. These are exactly ALL integer source pairs following
those words and meeting, relative to the original pair: the step (A,B) is
primitive within the two physical source cylinders.

**Proof.** Legal words require differences Delta n=2^L*s, Delta m=2^J*t.
Their endpoint differences are 3^q*s,3^p*t. Equality is equivalent to
3^q*s=3^p*t, whose complete integer solution is
s=3^max(p-q,0)*h, t=3^max(q-p,0)*h. This proves both claims, not just existence
of one sufficient subprogression. Positive starts keep every iterate positive.

For h>=0 the exact root-order domain is:

* A>=B: m<n for all h>=0;
* A<B: 0<=h<=floor((n0-m0-1)/(B-A)).

Thus a numerical merger is NOT automatically an unbounded smaller-source
family. The second alternative is explicitly retained and tested.
Appending the SAME subsequent physical word to both arms leaves B/A unchanged
and only refines the progression. Continuing after the meeting cannot improve
this slope ratio or cure an unfavorable order inequality.

If EVERY nonempty prefix of w has 3^q_i>2^i, then for every positive source
following w, T^i(n)>n throughout that arm: its affine remainder is nonnegative.
Accordingly (6) supplies no-forward-descent families when the stated root order
holds. This condition is checked, not inferred merely from one large example.

Example of the order failure: T^5(3)=T^10(1)=1, using 11000 and (10)^5.
The primitive steps are A=864,B=1024; only h=0 has m<n. Core padding cannot
be advertised as a successful infinite descent construction.

## PSS-003. A point-preserving bypass of a genuine first escape

A new explicit family is, for EVERY integer h>=0,

    n_h=303+2^10*3^28*h,
    m_h=27+2^51*h,
    E_h=1154+16*3^33*h.                                 (7)

Then

    T^6(n_h)=T^47(m_h)=E_h,   0<10*m_h<n_h.             (8)

The original arm has word w=111101 and actual initial states
303,455,683,1025,1538,769,1154. The companion word is the nonperiodic prefix

    z=11011111010110111011110100111011011111100111100.

It has length 47 and 33 ones and sends 27 to 1154. Its affine numerator is

    T_z(x)=(3^33*x+12316426265049391)/2^47,

whereas T_w(x)=(243*x+227)/64. Direct affine substitution or PSS-002, restricted
to its parameter 16h, proves (8) on the entire progression.
The strict order follows from 303-10*27=33>0 and

    3^28 - 10*2^41 = 886559899441 > 0.

All six prefix coefficients on n_h exceed one, so EVERY positive-time state
on its complete six-step arm is above n_h, for every h>=0.
Every n_h is divisible by three. Its only positive depth-b pure ancestor is
2^b*n_h: the odd inverse of a multiple of three is nonintegral, and doubling
preserves divisibility by three. There is no smaller pure ancestor at ANY depth.

### Why this is an actual first-escape extension

Each n_h has exactly r=v2(n_h+1)=4 initial odd steps and a hard first exit.
The standard comparison with the smaller original companion (n_h-1)/2 reaches
(H(C_h),C_h), where

    C_h=(27*n_h+11)/64=128+16*3^31*h.                   (9)

For EVERY h, C_h=0 mod16, hence v2(3C_h-2)=1 and v2(3C_h-1)=0. Neither #125
valuation entrance applies. Thus #132's admitted-return process escapes at
this first checkpoint on the whole family. Its old #123 entrance fails too.
Moreover v2(n_h+5)=2, so these sources are outside the odd-u 8^k*u-5 burst
representation used by #126. This comparison is against those SPECIFIED
languages, not a claim that no other repository certificate covers a member.

At h=0, the H parameter 128 is permanently excluded from uniform H cylinders
by PSS-001, even though it numerically synchronizes. The DIFFERENT original
companion 27 solves the root problem directly. On the whole family, replace
that companion by m_h, not by a local state merely smaller than H(C_h).
The original arm ends exactly at its H entry, two steps past its first odd
run; the much longer companion trajectory supplies the meeting. It does not traverse more old
hard-return stages to repair the failed guard.

For h=1 the literal certificate is

    n=23425835473880367,   m=2251799813685275,
    T^6(n)=T^47(m)=88944969064889522,
    min_(1<=j<=6)T^j(n)=35138753210820551>n,
    3 divides n,  10*m<n.

These identities exclude every n_h from being a least counterexample, by the
ordinary-source induction argument. They do NOT claim standalone convergence
of all m_h or give a universally successful selector for other escapes.
The elementary primitive lift is standard parity-affine algebra; no external
novelty or optimal-modulus claim is made beyond its explicitly proved lattice
minimality for THESE TWO words.

### Bounded synthesis, rather than treating the example as an isolated trick

The experiment indexes complete verified paths of smaller roots, searches an
actual n-prefix only while ALL its coefficient prefixes are supercritical,
and retains the best available endpoint derivative. It applies PSS-002 to
any meeting found. On n=2,...,4096 it produces 1130 whole-progression,
no-forward-descent lower-source certificates; 2965 inputs have no hit in that
specified search. These families are not all claimed new, disjoint, or absent
from existing rules. All successful lift identities are independently checked.
The verifier does not independently re-search the negative/optimality labels
of this secondary mine. This bounded corpus is not a convergence census.

## PSS-004. A least counterexample forces quantitative derivative escape

This is a necessary condition on actual fixed-source trajectories. It is not
another permission to choose the parity of an already fixed integer.

### 1. Positive imbalance on every prefix above the original floor

Let n0=N>=3 and suppose x_i=T^i(N)>=N for every i=0,...,a. Let q count the
odd steps in this prefix. At an even step the multiplier is 1/2, and at an
odd step it is (3+1/x_i)/2 <= (3+1/N)/2. Therefore

    1 <= x_a/N <= (3+1/N)^q / 2^a.

Thus

    q >= a*log(2)/log(3+1/N),
    B_N(a)=2q-a >= c_N*a,
    c_N=2*log(2)/log(3+1/N)-1 > 0.                       (10)

An exact, convenient uniform rational consequence for a>0 is

    7*B_N(a) > a.                                      (11)

Indeed 3+1/N<=10/3, and (10/3)^4<2^7 because 10000<10368. If q<=4a/7,
the upper multiplier in (10) would be strictly below one, a contradiction.
This is a standard multiplicative orbit bound specialized to the comparison
charge, not a new coefficient-stopping theorem.

### 2. A convergent anchor has a bounded imbalance at EVERY clock

For a convergent m, define the computable number

    M_m=max( B_m(b): 0<=b<=sigma(m), chi(m)+1 ).          (12)

Equation (2) proves B_m(b)<=M_m for EVERY b>=0, not just before its first core
visit. The anchor clock may be larger or smaller than the original clock;
even resetting its recorded clock cannot invalidate this numerical bound.

Consider fixed affine parametrizations through N and m with compatible slopes
A_N,A_m. Preserve those parametrizations when propagating actual words; do not
assign arbitrary new slopes at intermediate points. After a steps from N and
b from m the ratio of the two affine derivatives is

    2^U*3^V,
    U=v2(A_N)-v2(A_m)+b-a,
    V=v3(A_N)-v3(A_m)+q_N(a)-q_m(b).                    (13)

The common 2,3-free slope factor cancels. Let
s_m=v2(A_N)-v2(A_m)+2(v3(A_N)-v3(A_m)). Then exactly

    U+2V=s_m+B_N(a)-B_m(b).

Combining (10)--(12), for a>0,

    U+2V >= c_N*a+s_m-M_m,
    U+2V > a/7+s_m-M_m.                                (14)

In particular |U|+2|V| is bounded below by the same right side. This is an
explicit tradeoff between clock mismatch and ternary odd-count mismatch.
A very long extra anchor clock can reduce V but increases U: their combination
cannot hide the imbalance. The intercepts of the propagated affine charts
may be arbitrary; they do not enter this bound.

### 3. Application to every hypothetical least counterexample

If N is least nonconvergent, it is at least 3, every N-iterate stays >=N, and
all m<N converge. For a finite fixed portfolio of original-source affine
parametrizations, put K=max_m(M_m-s_m). At ANY observations, with any choices
of these companions and any anchor clocks,

    U+2V > a/7-K,      a>0.                             (15)

Hence as the original physical clock a tends to infinity, its comparison
must permanently leave every bounded set of propagated derivative ratios.
For example, a menu with |U|+2|V|<=R cannot be visited after a>=7(R+K),
when that upper bound is nonnegative. This includes independent clocks and
adaptive switches in the fixed portfolio. For a finite set of fixed
parametrizations of all roots m<N, K still exists by minimality.

This strengthens the bookkeeping of finite core-avoiding return budgets:
it describes a necessary linear escape in the derivative labels themselves.
It does NOT prove that such an escape is impossible. A proof establishing
unavoidable recurrence to a bounded certified menu would contradict (15)
and would therefore be substantive new progress, not an automatic consequence
of having a gate for each chart. Countably unbounded charts, isolated numerical
mergers, and genuine changes of the original affine companions remain possible
research directions.

The fixed-parametrization condition is essential. A single point pair can
always be rewritten with a newly chosen slope and a compensating intercept.
That algebraic re-description is not propagation of the old family and cannot
be counted as a physical decrease of U+2V. This theorem does not rule out a
method that supplies and justifies new source-level families with unbounded
slope changes. No conjecture is declared false by a chart or phase failure.

## Scope and exact remaining gap

The latest affine TEMPLATE existence theorem survives; #130 and #132 overlap
and are credited accordingly. The present pointwise criterion has the extra
hypothesis of supplied finite core paths. It is a diagnostic and a theorem
on that basin, not an oracle for an unverified source.

The strict family (7) genuinely handles a root-compatible first escape using
another shadow. The global restart statement still needed is: for an arbitrary
least N at an ACTUAL escape, obtain either a lower-original-source merger or
a justified continuing comparison that cannot evade all successful exits.
Neither the signature census, the primitive lifting theorem, nor (15) supplies
that universal restart. No complete Collatz proof was obtained in this pass.
