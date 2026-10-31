# First-hit distortion, basin pressure, and computability

**PROPOSED; self-audited, not independently reviewed or formally verified.**
This pass does not prove Collatz. All sources and intermediate states below
are positive ordinary integers. The old orbit-packing estimate is credited,
not claimed as a new discovery. The new contributions are its uniform
first-hit application, the pressure comparison, and the effective reductions.

Use the odd map U(x)=(3x+1)/2^a(x), a(x)=v2(3x+1). Let B_t be the set of
positive odd sources whose orbit reaches the positive odd target t. For
x in B_t, let q(x,t) be its FIRST hitting time, A the total valuation, and
J_0(x,t)=3^q/2^A. In particular q(t,t)=0 and J_0(t,t)=1. Define, for s>0,

    H_s(t)=sum_(x in B_t) J_0(x,t)^s,
    Z_t(s)=sum_(x in B_t) x^(-s).

These are nonnegative extended sums; infinity is allowed. All-history pressure
G_s additionally counts every repeated arrival at a periodic target. It is
not H_s. The distinction is essential in every statement below.

## B1. Credited finite-path packing and its first-hit consequence

The inherited finite-simple-path bound is T-A3-651 in
`research/astra-three-routes/pass3/FINITE_RECORDS.md`, at parent commit
`c8a5f1a391a10ef4927383e472bceebb2b04c5e7`. If S consists of the odd states
of a finite simple shortcut path, then, uniformly in its length and peak,

    # {x in S:x<=X} <= 5 X^(39/40),
    sum_(x in S, x>=m) 1/x <= 200 m^(-1/40).          (1)

Here is a reconstruction of the estimate used, including its finite endpoint.
Choose q=floor((3/5)log_2 X), h=floor(5q/3). Discard the last q odd states;
all remaining q-step endpoints are inside the simple path and are distinct.
A valuation word with total A selects one odd class modulo 2^(A+1), and

    U^q(x)=(3^q x+C)/2^A, 0<C/2^A<=(3/2)^q-1.

For A<=h, 2^h<=X makes each class have at most (3/2)X 2^(-A) members.
The composition generating function at z=4/5 gives

    sum_(A<=h) binom(A-1,q-1)2^(-A) <= rho^q,
    rho^3=3125/3456.

For A>h, the distinct odd endpoints lie below
sigma^q X+(3/2)^q-1, where sigma^3=27/32<rho^3. Hence

    # (S intersect [1,X]) <= 2X rho^q+(1/2)(3/2)^q+q.

The exact inequality 8*3125^24<3456^24 gives rho<2^(-1/24), while rho>2/3.
The three terms are respectively less than 3, 1/2, and 6/5 times
X^(39/40); for the last use log_2 X<2 sqrt(X). If q=0 or the path has fewer
than q odd states, the trivial bound handles the omitted case. Integrating
1/x=integral_x^infinity u^(-2)du proves the second part of (1).

A first-hit path is simple: repeating a state before the target would trap
it in a cycle that did not contain the target. The shortcut path obtained
by expanding its divisions is also simple. Its exact real product identity is

    t=J_0(x,t) x P(x,t),
    P(x,t)=product_(preterminal odd n)(1+1/(3n)).       (2)

If every state of this first-hit path is at least m, (1) gives

    1<=P(x,t)<=exp((200/3)m^(-1/40)).                 (3)

Since ln 2>2/3 (use its positive atanh series), (3) in particular gives the
explicit, intentionally crude, uniform arithmetic estimate

    2^(-100) t/x < J_0(x,t) <= t/x.                  (4)

The empty path satisfies (4) as well. Neither x nor t is assumed convergent.
This is a lower bound on actual first-hit weights, not on arbitrary inverse
words or on repeated arrivals. The repeated 1-cycle has weight (3/4)^r,
which is below 2^(-100) at r=256; this is an explicit countercontrol to
removing FIRST from the hypothesis.

## B2. The exact basin/pressure convergence threshold

For every positive odd t and every real s>0, (4) gives

    2^(-100s) t^s Z_t(s) <= H_s(t) <= t^s Z_t(s).     (5)

Thus H_s and the ordinary basin Dirichlet series have exactly the same
abscissa of convergence. With N_t(X)=#(B_t intersect [1,X]), put

    delta_t=limsup_(X->infinity) log N_t(X)/log X.

Then they converge for s>delta_t and diverge for 0<s<delta_t. At s=delta_t
nothing follows without more information. For completeness, if s>delta_t,
choose delta_t<b<s and eventually N_t(X)<=X^b, then integrate against
s X^(-s-1). If 0<s<delta_t, choose s<b<delta_t; along unbounded X,
Z_t(s)>=X^(-s)N_t(X)>X^(b-s).

If t is nonperiodic, G_s(t)=H_s(t). If t has minimal odd period p and total
valuation A, set lambda_t=3^p/2^A. Its positive affine constant, or the
product of 3n/(3n+1) around the cycle, gives 0<lambda_t<1. Every arrival is
a first hit followed by k complete cycles. Therefore, for ALL s>0,

    G_s(t)=H_s(t)/(1-lambda_t^s).                    (6)

The same convergence threshold holds for G_s. This exact cycle factor is
credited to pass 2, P2, and remains valid if a nontrivial positive cycle exists.
If 3 divides t, no odd map step can land on t, so B_t={t} and H_s=G_s=1;
then delta_t=0. No inverse-density theorem is applied to that case.

## B3. Source-qualified critical consequences, separate from B1--B2

The following implications are mathematical deductions under the explicitly
stated input assumptions. The external 2026 density releases have NOT been
independently replayed or accepted by this pass. The rest of this packet
does not depend on them.

**Density input D.** Suppose a given odd target t has an ordinary predecessor
set of positive lower natural density. Then its odd basin also has positive
lower density. To see this, discard the at most X/2^J integers divisible by
2^J, for a fixed sufficiently large J. Every retained predecessor is 2^j x,
j<J, for an odd predecessor x<=X; at most J retained inputs have the same x.
For odd t the odd map and ordinary map have the same odd reachability.
Consequently N_t(X)>=c_t X eventually, for some c_t>0.

Input D and (5)--(6) give

    G_s(t)<infinity iff s>1,
    G_s(t) asymp_t 1/(s-1) as s decreases to 1.       (7)

The lower estimate follows by integrating N_t(X)>=c_t X after a fixed
threshold. The upper estimate uses the full odd harmonic Dirichlet series
and the finite cycle factor, bounded as s decreases to 1. This is a growth
comparison, not a meromorphic continuation or an identified residue.

**Log-time input L.** Suppose a positive lower-density set of ordinary
sources reaches 1 in at most C ln n ordinary steps. The same finite
2-adic-valuation truncation gives positive lower-density odd sources with
q(x,1)<=C ln x+C_0. For those x<=exp((Q-C_0)/C), (4) and partial summation
show that the sum of first-hit weights with clock at most Q is at least
cQ-O(1). With rho_q(t)=sum_(depth-q arrivals) J, the pass-2 P4 upper bound
therefore yields

    sum_(q<=Q) rho_q(1) asymp Q,
    sum_(q>=0) z^q rho_q(1) asymp 1/(1-z), z up to 1. (8)

The second assertion follows by summation by parts; a lower bound on all
sufficiently large Q is needed. Again this is two-sided growth, NOT a proof
of an actual pole, a limit residue, or bounded individual rho_q(1).

Primary source interfaces, inspected 2026-10-31:
- Lech Mazur, *Positive Lower Density of Collatz Predecessors*, manuscript
  v1.0, 2026-09-06: https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/
  The advertised targets are positive integers not divisible by three.
- Lech Mazur, *Explicit Positive-Density Collatz Convergence in Logarithmic
  Time*, manuscript v2.1, 2026-09-06:
  https://www.proofatlas.ai/formalizations/positive-density-log-time-collatz/
  The displayed constant is 523/50 for ordinary, not odd, steps.

Only these interfaces and their versioned statements are used to identify
possible inputs D and L. No new manuscript-proof audit or Lean build is claimed.
Dirichlet-series formulations are not themselves new; this packet makes no
literature priority claim for using them.

## B4. What an arbitrary-precision pressure algorithm would decide

For fixed positive odd t, the following are equivalent:

1. H_2(t) is a computable real (rational intervals of any requested width).
2. Membership of positive odd x in B_t is decidable.

This equivalence concerns decidability, NOT the assertion that B_t is all
odd integers. Its proof uses the uniform positive floor in (4).

Given a membership decider, classify all odd x<=X, and run each positive
case until its first hit. Their exact rational sum M_X satisfies

    0<=H_2(t)-M_X<t^2/[2(X+1)]                      (9)

for odd X, by telescoping the omitted odd reciprocal squares. Thus H_2(t)
is computable. Conversely enumerate all first-hit witnesses by dovetailing
ordinary simulations of every odd source; the running exact sum M increases
to H_2(t). Simultaneously compute certified upper approximations V to H_2(t).
A candidate x, unless already enumerated, would contribute strictly more than

    epsilon_x=2^(-200)t^2/x^2

if it ever hit. If V-M<epsilon_x before it appears, certify nonmembership.
If it does hit, its finite witness eventually appears. If it does not, choose
a sufficiently tight upper approximation and wait until the enumerated sum
is sufficiently close. Hence the two-way decision always terminates.
All simulated clocks are bounded per dovetail stage; no unproved single
simulation is awaited forever. First hits are enumerated only once per source.

A single numerical enclosure, or the fixed finite census in this packet,
is NOT an arbitrary-precision oracle. No algorithm deciding all basin
memberships is constructed here. This result explains why a uniformly
improving first-hit pressure computation could contain more arithmetic
information than a fixed error bar suggests.
