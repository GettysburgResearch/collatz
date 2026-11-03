# Finite-clock energy, uniform tail certificates, and a collision target

**PROPOSED; self-audited only.** This is an additive continuation of PR140,
not a proof that its pressure vanishes. In particular the moment upper bound
in PF-008 remains OPEN. The first-hit discount used below retains the parent
proof/review status specified in [SOURCES.md](SOURCES.md).

Use U and F from [PROOF.md](PROOF.md). A clock q is a number of odd-to-odd
steps. Unlike F, the following fixed-depth quantities RETAIN cycle visits.
For every positive odd source x set

    t_q(x)=U^q(x),
    J_q(x)=3^q/2^(a(x)+...+a(U^(q-1)(x))),
    P_q(x)=product_(j<q)(1+1/(3U^j(x))).

The empty products are one. The identity t_q=x J_q P_q holds even when
states repeat. Define the nonnegative exact-depth population

    Z_q(t)=sum_(x odd: U^q(x)=t) J_q(x)^2.

A source is counted once at each fixed clock. At different clocks it may be
counted repeatedly. Z_q is NOT first-hit pressure and NOT the original
first-power geometric Syracuse density.

## PF-006. A decreasing, computable all-source energy

Define

    E_q=sum_(t odd) Z_q(t)/t^2
       =sum_(x odd) 1/[x^2 P_q(x)^2].                       (1)

Then E_0=pi^2/8, the sequence E_q is strictly decreasing, and

    E_q-E_(q+1)
      =sum_(t odd) Z_q(t) (6t+1)/[t^2(3t+1)^2].           (2)

Moreover, with the nonperiodic component masses Lambda_C of PR140 Q2,

    lim_q E_q = sum_C Lambda_C.                            (3)

Consequently E_q tends to zero if and only if F tends to zero at ordinary
odd infinity. Neither vanishing assertion is proved here.

### Proof

Tonelli and the product identity give (1). For a source currently at t,
its normalized squared coefficient is multiplied in the next odd step by
c(t)^2, where c(t)=3t/(3t+1)<1. The difference of the two normalized
coefficients is J_q(x)^2[1/t^2-9/(3t+1)^2]. Summing gives (2).
Every source has strictly positive loss; the sums are finite since each
term in (1) is at most x^-2. This proves strict decrease without asserting
any positive lower bound on the loss.

If a source is eventually periodic, each circuit of its positive cycle
multiplies 1/P_q by a number less than one, so its limit contribution is
zero. If it is nonperiodic, 1/P_q tends to the parent's r(x)>0. Dominated
convergence with the envelope x^-2 gives (3), grouping the nonperiodic
sources by their disjoint merger components. The sum is at most pi^2/8.
There are only countably many components. A nonempty component has positive
Lambda_C. This and PR140 Q4 prove the stated equivalence.

### A finite clock differs from an all-time basin oracle

For any positive odd cutoff X let

    E_(q,X)=sum_(x<=X, odd) [J_q(x)/U^q(x)]^2.

Then for EVERY q, including clocks beyond visits to the cycle,

    0 <= E_q-E_(q,X) < 1/[2(X+1)].                         (4)

The omitted odd reciprocal-square tail telescopes. Computing E_(q,X)
requires exactly q odd steps for each source, not a test of whether that
source eventually converges. Thus E_q is uniformly computable in q to
arbitrary absolute precision. This does not decide its limit, and does
not contradict PR140 B4, which concerns all-time pressure at a fixed target.

## PF-007. A finite-prefix certificate for every sufficiently large target

Let

    M_(q,X)=max{U^j(x): x<=X odd, 0<=j<=q},
    Theta_(q,X)=E_(q,X)+1/[2(X+1)].

Then the following is an INFINITE-TARGET statement:

    F(t) < Theta_(q,X) for EVERY odd t > M_(q,X).           (5)

No eventual classification of any of the sources through X is required.

To prove (5), a small source first hitting such a t does so strictly after
clock q. Its normalized first-hit weight is 1/[x P_hit] <= 1/[x P_q].
Sum this inequality squared over the small sources that do hit; retain all
small sources in the upper bound. The unclassified x>X sources contribute
less than the same reciprocal-square tail as in (4).

For fixed X, Theta_(q,X) strictly decreases with q. For fixed q it also
strictly decreases under X -> X+2: the added term is at most 1/(X+2)^2,
whereas the displayed tail allowance drops by

    1/[2(X+1)]-1/[2(X+3)]=1/[(X+1)(X+3)]>1/(X+2)^2.

By (4), Theta_(q,X) tends to sum_C Lambda_C along ANY choice of q and X
both tending to infinity. This identifies the exact possible residual; it
does not prove the residual zero. The threshold M_(q,X) may be enormous.

This extends the parent complete-bank certificate to unfinished finite
prefixes. It is not a uniformly successful algorithm for finding a desired
accuracy: if the energy limit were positive, arbitrarily small requested
bounds could not be attained this way.

## PF-008. An explicit finite-clock moment sufficient to force zero energy

Set

    S_q=sum_(t odd) Z_q(t)^2/t^2.                          (6)

This is a collision quantity for the SQUARED-derivative depth-q population.
It is not the forward occupation collision statistic of PR140 E5.

### Finiteness and effective truncation

Let A be the operator in PF-002, let C multiply coordinate x by
c(x)=3x/(3x+1), and put B=A* C. For h in l2(O),

    (B h)(t)=sum_(Ux=t) [3/2^a(x)] c(x) h(x)
            =sum_(Ux=t) [3/2^a(x)]^2 (x/t) h(x).

Its norm is at most sqrt(12/5). With h_0(x)=1/x, telescoping the factors
x/t gives

    (B^q h_0)(t)=Z_q(t)/t,
    S_q=||B^q h_0||_2^2 <= (12/5)^q pi^2/8.              (7)

This exponential bound establishes finiteness but is far too weak to close
the problem. If Z_(q,X) restricts the starting sources to x<=X, and
S_(q,X)=sum_t Z_(q,X)(t)^2/t^2, then

    0 <= sqrt(S_q)-sqrt(S_(q,X))
       < (12/5)^(q/2)/sqrt(2(X+1)).                       (8)

This follows by applying B^q to the omitted l2 tail of h_0 and using the
triangle inequality. Monotonicity of the nonnegative entries supplies the
left inequality. An entirely rational weaker enclosure is

    S_(q,X) <= S_q < 2 S_(q,X)+(12/5)^q/(X+1).            (9)

So every S_q is computable to arbitrary precision at a fixed finite q.
The source cutoff needed in (8) can grow exponentially with q; omitting
that cost would give a misleading claim of numerical control.

### A sufficient upper bound, not supplied here

If one fixed odd n has a nonperiodic trajectory t_q=U^q(n), the parent's
first-hit bound applies at every q, giving J_q(n)/t_q >= 2^-100/n. Its
single contribution in Z_q(t_q) therefore implies

    S_q >= 2^-400 t_q^2/n^4.                              (10)

In particular S_q tends to infinity on the hypothesis of even ONE escaping
source. More quantitatively, the first Q states are distinct positive odd
integers, so

    sum_(q=0)^(Q-1) S_q
       >= [2^-400/(3 n^4)] Q(4Q^2-1).                    (11)

Thus EITHER of the following independently sufficient estimates would
prove F(t)->0:

    liminf_(q->infinity) S_q < infinity;                  (12)

    liminf_(Q->infinity) Q^-3 sum_(q<Q) S_q = 0.           (13)

In particular the pointwise growth estimate S_q=o(q^2) would suffice for
(13). Neither (12), (13), nor this subquadratic estimate is proved. A mere
O(q^2) bound does not contradict (11) ALONE. The stronger orbit-packing
input does, however, make an O(q^2) bound sufficient, as follows.

### PF-008b. Sparsity upgrades the target to a quadratic moment bound

Sort the Q distinct values t_0,...,t_(Q-1) increasingly as z_1<...<z_Q.
The credited uniform simple-path bound implies

    i <= 5 z_i^(39/40), hence z_i >= (i/5)^(40/39).

Using (10), and summing the increasing power by its lower integral, gives

    sum_(q<Q) S_q
      >= (2^-400/n^4) * [39/(119 * 5^(80/39))] * Q^(119/39)
      > [2^-400/(500 n^4)] Q^(119/39).                    (14)

Here 119/39 is strictly greater than 3. Therefore the explicit all-source
moment target

    S_q <= C (q+1)^2 for every q>=0, for some finite C,    (M)

would prove F(t)->0. Even O(q^2 (log(q+2))^b), for any fixed b>=0, would
suffice. More generally O(q^p) with p<80/39 is enough using the explicit
packing estimate. Applying the optimized PF-001b bound instead gives the
sufficient range p<2/h0, approximately 2.10536; its constant is not explicit.
For that assertion choose beta>h0 with p<2/beta, and repeat the sorted-value
argument with z_i >= (i/C_beta)^(1/beta).

(M) is the principal OPEN target of this continuation. No quadratic bound
for this particular squared-derivative integer-trace moment is established
by the present argument or computations. Equation (7) remains only an
exponential upper bound. In particular an external quadratic estimate for
a different Haar density is not a proof of (M).

These criteria use all depths of ONE FIXED starting integer in the
contradiction, not a new source selected at each q. They exclude escape,
not additional positive cycles.

### Exact finite control: stepwise contraction and S_q<=S_0 both fail

Starting at 27, literal odd iteration at q=32 gives

    t_32=3077,
    J_32=1853020188851841/17592186044416.

The one source alone gives S_32 >= J_32^4/3077^2 > 13, checked as an exact
rational inequality. This is an ordinary finite convergent trajectory,
not evidence of a counterexample. A genuine moment estimate must allow
these intermittent finite excursions, rather than assume stepwise l2
contraction or extrapolate a small finite-source experiment.

## Comparison with an external finite-energy programme

The source-qualified Valbuena repository inspected in this session has a
DIFFERENT finite masked cylinder-energy criterion equivalent to eventual
periodicity. Its original geometric first-power density, no-return mask,
and division by K+1 are not Z_q, E_q, or S_q above. Its reported Haar
quadratic-energy bound also cannot be substituted into (13): the underlying
law and the positive-integer trace weights differ. Its unproved
small-ancestor energy condition is explicitly retained by that source.
See [SOURCES.md](SOURCES.md). No external formal build or theorem is a
dependency of PF-006--008; no literature-priority claim is made for proposing
an energy criterion.

## What the experiments do and do not establish

The new finite-clock suite computes rigorous dyadic enclosures for E_(q,X)
and S_(q,X), literal prefix maxima, and the rational tail allowances, for
X=4095 and 0<=q<=40. It retains sources that have not yet reached 1.
A separate implementation replays shortcut steps and independently
reconstructs the endpoint collisions and arithmetic. Cycle steps after 1
are retained rather than killed. Direct semantic corruptions are rejected.
These are finite regressions of the identities and certificate interface,
NOT an upper bound on the all-time limit or a polynomial bound on the growth of S_q.
