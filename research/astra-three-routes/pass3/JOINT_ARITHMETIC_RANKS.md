# Route 3: arbitrary joint finite arithmetic features meet one ordinary shadow

**Status:** T-A3-701--703 are **PROPOSED pending independent review**. No global
ranking function, total contracting cover, or Collatz proof is supplied.
This argument is independent of the coefficient-transport proof in pass 2.
It closes the previously unexcluded *finite joint-feature* repair, and gives
a quantitative memory requirement. It does not eliminate all rank methods.

## 1. Exact class: joint, nonlinear, and polynomial features allowed

Fix a finite collection of pairs (p_i,F_i), where p_i is prime and F_i is a
nonzero polynomial in Z[X], and a positive integer modulus m_0. Write

    V(n)=(v_(p_i)(F_i(n)))_i,
    R(n)=s log n+Phi(V(n), n mod m_0)+h(n),
    s>0, h(n)=o(log n).                                  (1)

Phi is an ARBITRARY real function finite on every finite input tuple. It may
couple every feature; no separability, monotonicity, growth, or regularity is
assumed. Enlarge a finite floor to exclude the finitely many positive integer
zeros of the polynomials. Rational affine-valuation features are included by
clearing their denominators and absorbing fixed valuation shifts into Phi.
The same is true of finite rational-polynomial observations away from zeros
and poles after listing the relevant numerator/denominator polynomials.

**T-A3-701.** For every ell>=1, (1) cannot be nonincreasing under T^ell on every
sufficiently large positive integer.

**T-A3-702.** Let F be the whole-odd-run/whole-even-run macro from pass 1. For
any fixed B>=1, (1) cannot be nonincreasing under ANY total selector

    n -> F^(b(n))(n),  1<=b(n)<=B,

on all sufficiently large odd integers. The selector can inspect the entire
ordinary n, not merely V(n). In particular this includes F itself and every
fixed finite iterate of F. These are bounded numbers of unbounded-length
macros, not merely bounded shortcut words.

## 2. Choose a rational fixed point outside the whole finite dictionary

Let P contain 2,3, every observed prime, and every prime dividing m_0. Choose
a>=2 divisible by p-1 for every p in P other than 2,3. Put

    D_a=2^(a+1)-3^a <0,
    alpha_a=(3^a-2^a)/D_a,
    rho_a=3^a/2^(a+1)>1.                                (2)

D_a is a unit at 2 and 3, and at any other p in P it is 2-1=1 modulo p.
Thus alpha_a is p-integral for every p in P. Moreover

    alpha_a=-1-1/((3/2)^a-2)

is strictly increasing for a>=2 and tends to -1. Each nonzero polynomial has
only finitely many roots, so among the infinitely many permitted a's choose
one for which F_i(alpha_a)!=0 for EVERY i. This is a finite exclusion, not an
assumption about unknown positive Collatz behavior.

The shortcut word w_a=1^a 0 has affine map

    g_a(x)=(3^a x+3^a-2^a)/2^(a+1)
          =alpha_a+rho_a(x-alpha_a).                     (3)

It fixes alpha_a. Since v_2(alpha_a+1)=a and its state after those a odd steps
is 2 alpha_a with valuation 1, this word is exactly one maximal-run macro at
the rational fixed point. This is only a convenient algebraic center. The
witnesses below are positive ordinary integers, not the negative rational.

For each p choose M_p>=1 strictly greater than every v_p(F_i(alpha_a))
observed at p, and at least v_p(m_0). If z=alpha_a modulo p^M_p, then

    v_p(F_i(z))=v_p(F_i(alpha_a))                         (4)

for the observations at that prime. Polynomial coefficients and alpha_a are
p-integral, so F_i(z)-F_i(alpha_a) is divisible by z-alpha_a; the strict
precision choice proves (4), even for repeated roots or nonlinear F_i.

## 3. T-A3-703: arbitrarily long ordinary paths with identical joint profiles

For each K>=1 set

    N_K=2^((a+1)K+M_2) * product_(p in P, p odd) p^M_p.

The denominator of alpha_a is coprime to N_K. Let r_K be its canonical residue
modulo N_K and choose

    n_K=N_K+r_K, so N_K<=n_K<2N_K.                       (5)

Then n_K is positive odd and realizes K consecutive exact maximal-run packets
w_a, with every state above n_K. At each packet boundary x_t=g_a^t(n_K),
0<=t<=K, the FULL joint vector V(x_t) and residue x_t mod m_0 equal those at
n_K.

### Proof of physical legality and stable observations

The initial dyadic agreement has precision (a+1)K+M_2. Every shortcut step
consumes exactly one bit of agreement with the rational model (its branch
multiplier has odd numerator); therefore all K words and the odd final
endpoint are legal. At packet boundaries the remaining dyadic precision is
at least M_2. At 3 it increases by a per packet; at the other observed odd
primes it is preserved. Thus (4) holds at every boundary. The residue
observations are preserved by the same congruences.

All odd steps of a positive packet increase the state, and its sole even step
ends at g_a(x)>x because rho_a>1 and the affine correction is positive. Thus
all intermediate physical values are >=n_K. They eventually exceed any
prescribed fixed floor as K increases.

At the endpoint m_K=g_a^K(n_K), exactly,

    m_K=alpha_a+rho_a^K(n_K-alpha_a)>rho_a^K n_K,
    log n_K=(a+1)K log 2+O(1),
    log m_K=aK log 3+O(1).                              (6)

In particular

    R(m_K)-R(n_K)=sK log rho_a+o(K)>0                   (7)

for sufficiently large K. The arbitrary function Phi cancels EXACTLY because
the entire observed tuple is identical. No bound on Phi is needed. The two
h terms are o(K) by the two height estimates. This is stronger than bounding
separate nonlinear corrections one prime at a time.

## 4. Complete proofs of the two obstruction theorems

For T-A3-701 let K grow through multiples of ell. Then ell divides (a+1)K.
Apply the supposed ell-step nonincrease successively along the ordinary path
in Section 3. Every input is above its required floor. It gives R(m_K)<=R(n_K),
contradicting (7).

For T-A3-702, construct a shadow of K+B packets. Starting at n_(K+B), apply
the claimed selector until the accumulated packet count first reaches K.
This is a finite process since each selection consumes at least one packet.
The total t lies between K and K+B-1, inside the constructed shadow. Its
endpoint has the same full feature tuple and increases real logarithmic
height by at least K log rho_a. Both endpoint heights are O(K), so the
sublogarithmic errors remain o(K). Successive rank nonincrease contradicts
this positive increase. This proof does not assume that b(n) is periodic,
finite-state, or determined by the observations.

It also proves failure above any enlarged floor. A pointwise inverse-weight
inequality implying nonincrease of (1) along every such selected physical
edge is therefore excluded too. Aggregate mass contraction is not excluded.

## 5. Quantitative memory demand and a constructive direction retained

A successful correction H(n) in R(n)=s log n+H(n) must compensate on these
ordinary shadows by

    H(n_K)-H(m_K) >= sK log rho_a                       (8)

whenever the claimed monotonicity covers the path. Finite polynomial-valuation
and congruence observations cannot distinguish the endpoints at all. Merely
allowing interactions, huge profile values, more finite primes, or a bounded
number of complete packets is not enough.

This does NOT cover a different leading growth law, vector/tree-valued order,
a controlled infinite dictionary, complete digit structure, or an adaptive
selector requiring an UNBOUNDED number of packets to finish. In particular,
PR #91's unbounded repayment families remain outside the theorem; they were
not merged or assumed here. The record-set architecture in FINITE_RECORDS.md
is another genuine unbounded-state alternative, but its local stopping
premise still needs proof.

A next constructive target is therefore a proved total *unbounded* repayment
rule whose correction spends the required growing amount (8), or a common
well-founded tree rank sensitive to the digit structure that the endpoints
above share only at fixed precision. Replacing the missing totality proof
by an instruction to run until a rank drop appears is not allowed.

## 6. Evidence and novelty boundary

The checker constructs actual CRT sources for several polynomial dictionaries,
including ones that already contain earlier rational shadow roots. It checks
every repeated packet, stable joint profiles, simultaneous residue agreement,
the exact positive height gain, and adaptive group sizes. The independent
verifier uses literal shortcut steps and polynomial evaluations. These finite
cases validate interfaces; the all-dictionary result is Sections 2--4.

This is a project-level strengthening of the finite-feature obstructions in
passes 1--2 and the resident completion-ghost warning. No claim of broad
external priority is made. A finite compatible positive shadow at every K
is NOT an infinite positive orbit: n_K grows exponentially with K.
