# Critical tails, clock changes, and the attempted closure

**Status: PROPOSED pending independent mathematical review.**
Author: `astra-tail-transport-01`, returning from the Reviewer D audit to research.
Date: 2026-09-07. Frozen repository base:
`69b1ed57ce90fe8c9d6d7c80c69760a86eb0fd2a`.

This is not an additional review verdict or a complete Collatz proof. All claims
below have new `ATT-*` identifiers. The numerical checks are regressions, not
proofs of the universally quantified statements. No external theorem is needed
for Sections 1–6. Section 7 distinguishes a general elementary identity from
its optional interface to the repository's SC* crosswalk.

## 1. Map, rank, and actual mass

Use the shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n. Let tau(n) be
its first hitting time of 1, with infinity allowed. On surviving states n>=2,
put

    d_a=3^a-2^(a+1), c_a=3^a-2^a,
    z_a(n)=d_a n+c_a,
    R_a(n)=z_a(n)^2 / 3^v3(z_a(n)),
    R(n)=min_(a>=0) R_a(n),                 w(n)=1/R(n)^2.

Zero component values receive rank zero; the only positive zero is n=1,a=1,
which is killed. This is exactly the moving rank R_* of the pinned PR92 source,
NOT PR90/91's P(n)=(2n+1)^2/3^v3(2n+1).

For raw shortcut time k define the genuine pushforward and its rank tail

    f_k(y)=sum_{n>=2: tau(n)>k, T^k(n)=y} w(n),
    F_k(Y)=sum_{y>=2: R(y)>Y} f_k(y),       Y>0.

Rows are endpoints, columns are sources. All series are nonnegative. Merging
sources contribute separately to f_k; there is no injectivity or fresh-shell
assumption. These are finite measures, not necessarily probability measures.
A weak first **rank moment** means sup_{Y>0} Y F_k(Y)<infinity. This is a tail
condition on the random variable R(endpoint) under the source measure. It is
not a claim that f_k, regarded as a function on counting measure, has a stated
Lorentz norm.

### Reconstructed rank facts (credited to the moving-rank packet)

For n>=2,

    n-1 <= R(n) <= n^2,
    R(n)=min(R_0,R_1,R_2,R_h), h=v3(2n+1),

where R_h is needed only when h>=3. To check the finite formula, for a>=2,

    z_(a+1)(n)=3z_a(n)+2^a(2n+1)>3z_a(n).

If t=v3(n+1), then h and t cannot both be positive, and away from a+t=h,

    v3(z_a(n))=min(a+t,h).

For h<=1 the minimum for a>=2 is at 2. For h=2 possible cancellation only
improves R_2. For h>=3, t=0, and the increasing numerator shows every a>2,
a!=h, has R_a>R_2. This proves the rule. Also z^2/3^v3(z)>=abs(z), and
abs(z_0)=n, abs(z_1)=n-1, z_a>=n+5 for a>=2. Properness and the upper bound
follow. In particular sum w<2, by comparison with sum_{m>=1} m^-2<2.

The input has finite first rank moment. One quick reconstruction is the rank
fiber count: writing a component rank as 3^e u^2 with 3 not dividing u, the
fixed indices give at most three sources, and a minimizing moving index must
lie in 3<=a<=e. Thus there are at most max(3,e+1) sources per (e,u), and

    sum_{n>=2} 1/R(n)
      <= 2 sum_{e>=0} max(3,e+1) 3^-e =55/6.

This familiar estimate is repeated only to identify the input space.

## 2. ATT-001 — sharp ordinary-height tails for the canonical input

For every real N>=2,

    1/(9N^2) <= sum_{n>N} w(n) <= 43/N^2.                (1)

The exponent is sharp. Notice that the cutoff is ordinary n, not R(n).
The existing square-root rank-counting estimate alone gives a weaker upper
bound when combined just with R(n)>=n-1.

### Proof

For positive integers m put g(m)=3^{2v3(m)}/m^4. For real Z>=1,

    sum_{m>Z} g(m) <= (7/2) Z^-2.                       (2)

Write m=3^e u and enlarge the inner sum to all u>=1. For e<=E=floor(log_3 Z),
use sum_{u>x}u^-4 <=(4/3)x^-3, x>=1. These contributions are at most

    (4/3) Z^-3 sum_{e=0}^E 3^e <=2 Z^-2.

For e>E use sum u^-4<=4/3. The geometric tail contributes at most
(3/2)Z^-2. This proves (2), including nonintegral Z.

Since w(n)=max_a g(abs(z_a(n))), it is bounded by the positive sum over a.
For a=0,1,2, the three absolute linear forms are n,n-1,n+5. Their ordinary
tail contributes at most 3*(7/2)*(N-1)^-2. For a>=3, d_a>=3^(a-2)>0;
ignoring the progression restriction, the a-th contribution is bounded by
(7/2)(d_a N)^-2. Therefore

    sum_{n>N} w(n)
      <= (21/2)(N-1)^-2 + (7/16)N^-2
      <= (679/16)N^-2 <43N^-2.

All infinite dictionary terms are covered by this convergent geometric bound.
There is no fixed-index truncation in (1).

For the lower bound choose the first power n=3^e>N. It satisfies n<=3N and
R(3^e)=3^e: h=0, R_0=3^e, R_1=(3^e-1)^2>=3^e, and R_2=(3^e+5)^2.
Its single weight proves the lower bound. QED.

## 3. ATT-002 — exact critical tail exponent at every fixed positive clock

For every integer k>=0 and Y>0,

    F_k(Y) <= 77 (9/4)^k /Y.                            (3)

For every fixed k>=1 there are explicit positive constants c_k,Y_k such that

    F_k(Y) >= c_k/Y,                 Y>=Y_k.             (4)

One valid choice is

    E_k=2k+2, c_k=1/[9*36^(k+1)],
    Y_k=3^(2E_k)/36^(k+1).

Consequently, for EACH fixed k>=1, all fractional rank moments of orders
0<s<1 are finite, but

    sum_y R(y) f_k(y)=infinity.                          (5)

In fact the s-th rank moment is finite exactly for 0<s<1. The initial first
rank moment is finite; the singularity in (5) appears immediately and persists
at every fixed positive shortcut time. These facts require no divergent orbit. The clock dependence is also essential:
writing W_k=sup_{Y>0}Y F_k(Y), Section 6 proves

    (9/4)^k/5184 < W_k <=77(9/4)^k, k>=6.               (5a)

Thus the exponential growth rate of this critical weak moment is sharp, even
though it does not by itself establish mass escape.

### Upper bound

The deterministic size inequality gives

    T^k(n)+1 <= (3/2)^k (n+1).

Set b=(3/2)^k. If R(T^k(n))>Y, then n>sqrt(Y)/b-1. When sqrt(Y)>=4b, this
threshold is at least (3/4)sqrt(Y)/b>=3. Apply (1):

    F_k(Y) <= (688/9)b^2/Y <77b^2/Y.

For smaller Y, use F_k(Y)<=sum w<2 and Y<16b^2. Killing can only reduce mass.
This proves (3). Positive integration of the tail gives, for 0<s<1,

    sum_y R(y)^s f_k(y) <=2 +77s(9/4)^k/(1-s).

### Uniform ternary stabilization on the actual powers of three

Let n=3^e and k>=1. Its actual length-k parity word starts with 1. Write

    T^k(n)=(3^q n+A)/D, D=2^k.

Then q>=1, A is a positive odd integer, and A<=3^k-2^k. Oddness follows from
the affine recurrence: after the first odd step its remainder is 1; later
steps either preserve it or replace it by 3A plus an even number. The maximum
remainder is the all-odd value 3^k-2^k (or use the recurrence inductively).

Set C=2A+D. Then 0<C<2*3^k and v3(C)<=k. For e>=E_k,

    v3(2T^k(n)+1)=v3(C)=h<=k.

For each of the possible minimizing indices a in {0,1,2,h}, write

    D z_a(T^k(n))=d_a 3^q n + C_a,
    C_a=d_a A+D c_a.

No C_a is zero. For a=0 it is -A; for a=1 it is D-A, nonzero because A is odd
and D is even; for a>=2 both terms are positive. Also

    abs(C_a)<2*3^(k+a),   v3(C_a)<=k+a<=2k+2.

For a=0,1 the same bound follows directly; the estimate a<=max(2,k) suffices.
The coefficient d_a is a 3-adic unit. Since e+q>2k+2, each component has its
fixed valuation v3(C_a). Meanwhile T^k(n)>=n/2^k, so

    abs(z_a(T^k(n))) >= T^k(n)-1 >= n/2^(k+1)

for these e. It follows that

    R(T^k(3^e)) >=3^(2e)/36^(k+1),      e>=E_k.           (6)

The full path survives: T^i(3^e)>=3^e/2^k>1 for i<=k. This is an actual-source
argument; no finite compatible words have been turned into one infinite orbit.

Choose the first power 3^e>sqrt(36^(k+1)Y), with Y>=Y_k. Then e>=E_k and
3^e<=3 sqrt(36^(k+1)Y). Its weight alone gives (4). Alternatively, summing the
contribution R(T^k(3^e))/R(3^e)^2>=36^(-k-1) over e>=E_k proves (5) directly
by Tonelli, even if endpoint merging were present. The tail lower bound rules
out every moment s>=1. QED.

### What the theorem does NOT say

The constant in (3) grows with k. Exchanging 'for every fixed k' with 'uniformly
in k' is the unproved step. A finite first moment is unnecessarily strong for
tightness, but (3) alone does not prove tightness of the whole time family.

## 4. ATT-003 — a sharper all-mode height ceiling

Let A be the total maximal repeated-word acceleration from the pinned moving-
rank packet. At n>1 use a=0 if n is even, otherwise a=v2(n+1), and

    k=floor(v2(z_a(n))/(a+1)),
    A(n)=g_a^k(n), g_a(n)=(3^a n+c_a)/2^(a+1).

For every ordinary n>1,

    A(n)+5 <= (n+5)^(9/4).                              (7)

This improves the source's coarse cubic height ceiling. It is a size bound,
not a rank decrease or a stopping-time bound.

### Physical exactness and totality

The parity word (1^a0)^k has exactly the cylinder
2^((a+1)k) | z_a(n): its rational fixed point -c_a/d_a realizes that periodic
word, and d_a is odd. Finite parity-cylinder bijectivity, or direct induction,
proves the equivalence. The active a ensures one copy, the finite valuation
gives the exact maximum, and the endpoint is positive. The n=1 zero is handled
by absorption. Modes 0 and 1 contract ordinary size; a>=2 expands at module
boundaries and cannot hit 1 internally. These elementary facts are credited,
not claimed as new constructions.

### Proof of (7)

Let lambda=log_2 3. The exact inequalities 3^2>2^3 and 3^17<2^27 give

    3/2<lambda<27/17.

Only a>=2 needs proof. Put s=log_2(n+5), rho=3^a/2^(a+1)>1. Since
0<z_a(n)<3^a(n+1) and a<=log_2(n+1)<s,

    k(a+1)<lambda a+s.                                  (8)

Also 1<c_a/d_a<=5 gives

    A(n)+5 <=rho^k(n+5).

For k=1,2,

    log_2(rho^k)=k[a(lambda-1)-1]
      < k(lambda-1)s <(5/4)s.

For k>=3, (8) gives a<(s-k)/(k-lambda), so

    log_2(rho^k)
      < [k(lambda-1)/(k-lambda)]s
      <=[3(lambda-1)/(3-lambda)]s <(5/4)s.

The middle function decreases with k; the last inequality is precisely
lambda<27/17. This proves (7). Modes 0,1 satisfy it by A(n)<=n. QED.

## 5. ATT-004 — a global fractional-moment contract for ONE unsafe return

Use ONLY the quarter-safe set

    G={n>=2:4R(A(n))<=R(n)}, U={n>=2}\G.

From U take one A step, then all consecutive G steps, until arrival at U or 1;
call the resulting killed map B. It is total because a G step decreases a
positive integer rank. Let H be the pushforward for B, killed at 1. For any
nonnegative input f on U satisfying

    f(n)<=C/R(n)^2,

one has the ALL-SOURCE, ALL-EXCURSION bound

    sum_{y in U:R(y)>Y} Hf(y) <=200 C Y^(-4/9), Y>0.     (9)

In particular its s-th rank moment is finite for every 0<s<4/9, with

    sum_y R(y)^s Hf(y) <=C[2+200s/(4/9-s)].               (10)

### Proof

Every retained B endpoint has R(B(n))<=R(A(n)); all intermediate G steps reduce
rank. By (7), R(A(n))<=A(n)^2<(n+5)^(9/2). For Y>=10^(9/2), any contributing
source satisfies n>Y^(2/9)-5>=(1/2)Y^(2/9). Apply (1) and the input envelope to
obtain 172 C Y^(-4/9). For smaller Y, total mass is below 2C and
200Y^(-4/9)>=2. Integrating the tail at 1 proves (10). QED.

This is an actual output-domain theorem despite the known infinite first rank
moment. It includes arbitrarily long safe excursions, not a sampled cap on
B's clock. It does NOT establish that Hf satisfies f<=C/R^2 again. Repeating
(9) without a new entry-envelope theorem is invalid. The enlarged nonincreasing
safe set in the spectrum-switch packet is a different object and is not being
substituted here.

## 6. ATT-005 — induction in time destroys even the weak critical endpoint

The fixed shortcut-clock estimate in ATT-002 cannot simply be attached to the
unbounded stopping clock B. For the same canonical input on U,

    f(n)=1_U(n)/R(n)^2,
    sup_{Y>0} Y sum_{R(y)>Y} Hf(y)=infinity.              (11)

This strengthens the existing first-moment obstruction for this input. It does
not contradict the positive sub-4/9 output theorem.

### Explicit ordinary family

For every EVEN j>=2 put

    t=2^j, M=3^t, n=4M-5, a=j+4,
    m=(M-1)/2^(j+2), y=(3^a m-1)/2.

Then

    A(n)=B(n)=y,
    R(n)=16M, R(y)=(y+5)^2/9,
    n,y in U,
    R(y)/R(n)^2 > (9/4)^a/1152.                         (12)

These sources go to infinity, but are not asserted to be one all-time source
or to converge for every j.

### Proof of legality, ranks, and both unsafe guards

The elementary doubling identity for powers of 3 gives

    v2(3^(2^j)-1)=j+2,
    m_j=(3^(2^j)-1)/2^(j+2),
    m_1=1, m_(j+1)=m_j+2^(j+1)m_j^2.

In particular m_j=5 mod8 for j>=2, and 3 does not divide m_j. Thus n has active
mode a. Since a is even,

    z_a(n)=2^a[3^a m-(8M-9)]

has valuation a+1 at 2: the bracket is 2 mod4. Exactly one copy of 1^a0 is
consumed and its endpoint is y. Also 3^a m=5 mod8, so v2(y)=1 and A(y)=y/2.

At n, v3(2n+1)=2, v3(n)=0, v3(n-1)=1, and v3(n+5)=t. The three-entry rule and
M>=81 give R(n)=16M. At y, h=a, v3(y)=0, v3(y-1)=1, v3(y+5)=2. Further
v3(z_a(y))=a+2 follows from z_a(y)=(3^a/2^(a+1))z_a(n) and v3(z_a(n))=2.
For a>=6, d_a>=3^(a-1) gives R_a(y)>=3^(a-4)y^2. The other fixed entries are
y^2 and (y-1)^2/3. Since y>16, their minimum is R_2(y)=(y+5)^2/9.

The initial multiplier rho is greater than 5, so y>5n and R(y)>R(n). At y/2,
h=0, and none of y/2,y/2-1,y/2+5 is divisible by 3. Thus

    R(A(y))=(y/2-1)^2> (y+5)^2/9=R(y),

where the strict inequality is equivalent to y>16. Both states are in U and
B(n)=A(n)=y, not a later unknown exit.

Finally

    y+5=2(3/2)^a(M-1)+9/2,
    R(y)/R(n)^2 > [(9/4)^a/576](1-1/M)^2
                 >(9/4)^a/1152.

Take Y=R(y)/2. This single input atom forces Y times the Hf tail to exceed
(9/4)^a/2304. Let even j tend to infinity. This proves (11). It also refutes
every bound R(A(n))<=C R(n)^2 with a fixed constant and any finite excluded
initial region. QED.

The growth of this ratio is logarithmic-power in R(n), since log R(n) is of
order 2^j and (9/4)^j=(2^j)^log_2(9/4). This observation is not an upper bound
on all unsafe sources or a sharp exponent for (9).

### Sharp fixed-clock growth: completing ATT-002

For odd k>=7, choose even j=k-5 in (12), so a=k-1 and T^k(n)=y. At
Y=R(y)/2, the full (unrestricted) initial w also contains the source n, and

    W_k > (9/4)^(k-1)/2304=(9/4)^k/5184.

For even k>=6 choose j=k-4, so a=k. Stop one step earlier: u=T^k(n)=2y.
Since h(u)=0 and u=2 mod3, R(u)=(u-1)^2. The family gives

    u-1=4(3/2)^a(M-1)-2 >2(3/2)^a M,
    R(u)/R(n)^2 >(9/4)^k/64.

The choice Y=R(u)/2 gives W_k>(9/4)^k/128, hence the weaker common constant
in (5a). Together with (3), this proves the claimed sharp exponential rate.
The witness input grows doubly exponentially with k. A large value of YF_k(Y)
at such a remote, extremely small-mass atom is NOT failure of uniform tightness.

## 7. ATT-006 — exact escape/cycle decomposition for a fixed summable ensemble

Here is the end-to-end target after abandoning the unnecessarily strong first
moment. It uses the FIXED explicit f=1_U/R^2, not an existentially chosen weight
depending on unknown stopping times. Put f_j=H^j f. Define

    D =lim_{Y->infinity} sup_{j>=0} sum_{R(y)>Y} f_j(y),
    C =lim_{Y->infinity} lim_{J->infinity}
          (1/J) sum_{j=0}^{J-1} sum_{R(y)<=Y} f_j(y).

Both limits exist, and

    D =sum_{n in U: T-orbit tends to infinity} 1/R(n)^2,
    C =sum_{n in U: T-orbit reaches a nontrivial cycle} 1/R(n)^2.  (13)

Consequently

    Collatz <=> D=0 AND C=0.                             (14)

This is an elementary fixed-ensemble compactness/occupation identity, not a
claim to have proved either vanishing statement. It is given here to prevent a
third false closure: tightness by itself does not exclude positive cycles.

### Proof

On any countable deterministic killed system with a proper height, an orbit is
absorbed, eventually cycles, or has infinitely many distinct states and escapes
every finite height set. The last assertion uses properness, not a growth rate.
For B the classification agrees with T: safe excursions always terminate, so
any nonconvergent T orbit visits U infinitely often.

For any finite set of divergent input atoms, all their late endpoints lie above
a given Y. Their total weight is therefore a lower bound on the supremum in D.
Exhaust these atoms to obtain D>=their full mass. For the reverse bound, retain
a finite set of input atoms whose omitted total mass is below epsilon. Every
nondivergent retained atom has bounded height over its entire surviving orbit.
For Y above all those finitely many peaks, every time-j tail is bounded by the
divergent mass plus epsilon. This proves the identity for D.

For each input atom, Cesaro occupation of a finite rank ball tends to zero for
absorbed and divergent trajectories, and to the fraction of its eventual cycle
in that ball otherwise. Summability of f permits dominated convergence over
inputs. Increasing Y captures every finite cycle completely. This proves C.
Full support on U and the necessary visits to U give (14). QED.

### SC* interface, separately source-qualified

Combining (13) with the pinned repository's theorem that every non-eventually-
periodic positive orbit has a coefficient-supercritical tail identifies D=0
with SC*. This uses that exact orbitwise theorem; it is NOT needed for (13) or
(14), and does not promote the old SC*/FC* integrated bridge. An alternative
proof of D=0 would settle the divergent lane; C=0 is still the cycle lane.
The earlier Assani–Ebbighausen–Hande finite-measure/power-boundedness viewpoint
is related conceptual background, not a theorem imported into this proof.

## 8. Actual attempted completion and first unsupported inference

The attempted chain was:

1. Replace the failed first-moment argument with a tail condition.
2. Prove a quantitative output bound for real source transport (ATT-001–004).
3. Iterate a single tail cone through the unsafe map.
4. Obtain D=0, then discharge the finite-cycle alternative to conclude (14).

Step 3 is NOT proved. The most natural critical version is explicitly false by
ATT-005. The valid fractional-moment output bound has an input-envelope premise
that is not known to be regenerated. Nor has a universal cycle exclusion been
proved in Step 4. The displayed finite-clock constants grow with the clock.

A quantitatively sufficient pair of targets would be a finite constant M with

    sup_j sum_y R(y)^(1/3) H^j f(y) <= M,
    sup_J sum_{j<J} sum_y R(y)^(-1) H^j f(y) < infinity.

The first implies D=0 by Markov's inequality; the second excludes every cycle
because any cycle's positive source atom contributes a positive reward forever.
Only the FIRST unsafe-return one-third moment is proved here: (10) gives the explicit
bound 602. Finiteness or boundedness of the iterated one-third moments is not proved.
In particular, the uniform first/weak-first-moment variants are already false.
These sufficient targets may be stronger than needed; (13)-(14) state the exact
qualitative criterion without asserting a stopping-time rate.

The next concrete target is a transport-stable tail envelope or an amortized
source-conditioned escape-flux estimate. It must tolerate (12), not assume a
uniform quadratic rank ceiling or identify a stopping clock with a fixed clock.
A merely cofinal collection of finite source certificates is not an all-source
proof. No numerical trend is used to assert D=C=0.

The purpose of this packet is a proved change in the analytic contract and an
exact failure test for its first iteration attempt. It supplies neither a full
proof nor evidence that the remaining uniform estimate is imminent.
