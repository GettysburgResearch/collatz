# Independent review of the negative-spike density obstruction

**Disposition:** DSP-001 through DSP-005, the resolvent corollary, and the
vanishing-loss mask lemma in
`NEGATIVE_SPIKE_BARRIER.md` survive independent reconstruction.
They concern the specified auxiliary residue law and one clipping/counting
mechanism. They are not upper bounds on actual positive predecessor density.
The claimed relation to source-paper normalizations was not independently
re-audited here; the local proofs below use exactly the law displayed in the
packet and do not require those source claims.

## Reference law and the first spike

For independent positive geometric exponents with P(A=a)=2^{-a}, write

\[
Y_q=\sum_{j=1}^q3^{j-1}2^{-(A_1+\cdots+A_j)}\pmod{3^q},
\qquad\rho_q(y)=3^qP(Y_q=y).
\]

The law has mean density one under uniform residues and is compatible
under reduction modulo smaller powers of three. On the event that all q
exponents equal one, its value is (3/2)^q−1, which is −1 modulo 3^q.
The event probability is 2^{-q}; hence rho_q(−1)≥(3/2)^q. No mixing
or limit-law assumption enters this argument.

## Clipping tail and the endpoint moment

For q≥k, the ball y≡−1 (mod 3^k) has uniform mass 3^{-k} and
probability at least 2^{-k}. Summing (rho_q−U)_+ over that ball gives

\[
E_q(U)\ge2^{-k}-U3^{-k}.
\]

If U≤(3/2)^k/2, this is at least 2^{-k-1}. Choosing
k=ceil(log_{3/2}(2U)) yields the stated absolute lower bound
c U^{-delta_*}, delta_*=log2/log(3/2), whenever q is sufficiently
large for this fixed U. The quantifier order is important: choose U,
then allow q≥k(U). It rules out an upper bound uniform in q with a
strictly larger polynomial tail exponent.

For the endpoint L^p argument, first k exponents equal to one followed
by exponent two has probability 2^{-k-2}. Its residue satisfies

\[
Y_Q+1\equiv5\,3^k/2^{k+2}\pmod{3^{k+1}},
\]

and therefore lies in the exact annulus v_3(y+1)=k. This annulus has
uniform mass 2·3^{-k-1}. The annuli for k=0,…,Q−1 are disjoint.
Jensen gives a contribution of at least

\[
\frac{(2^{-k-2})^p}{(2\,3^{-k-1})^{p-1}}.
\]

At p=p_*=log3/log(3/2), the relation 3^{p−1}=2^p makes this exactly
2^{1−2p}, independently of k. Summing gives the claimed lower bound
Q·2^{1−2p_*}. Thus the endpoint strong L^{p_*} norm is unbounded.
A matching weak endpoint upper bound or sharp actual tail asymptotic has
not been established. For that reason “obstruction exponent” is preferable
to an unqualified “sharp tail exponent.”

## Census mechanism and its scope

Suppose positive constants A,B,z_0, independent of the positive root R,
are used only through

\[
z_0\le Z\le A U W+B R E_q(U),
\qquad\text{density guarantee}\ge W/R.
\]

To obtain a positive lower bound for W by subtraction, the actual global
error must be smaller than z_0. The lower bound for E_q(U) then forces
U≳R^{1/delta_*}. The lower bound extracted in this manner is at most
of order R^{-1−1/delta_*}=R^{-log_2 3}. The argument is valid in
the fixed-root density limit, where U is selected before q tends to
infinity. It does not constrain a different source-conditioned error, a
stronger root-dependent marked-mass lower bound, or another counting
method. It is also not a bound on the actual W or actual density.

## Positive-source cap and transfer expansion

For a positive odd target t, repeated inverse exponent-one steps satisfy

\[
I_1^r(t)+1=(2/3)^r(t+1).
\]

Integrality is equivalent to 3^r dividing t+1. This also makes every
prefix positive and odd, because dividing the even integer t+1 by an
odd power of three leaves a positive even integer. The forward valuation
is exactly one since 3I_1(u)+1=2u with odd u. Thus the exact initial
run cap is v_3(t+1); no bounded cap is uniform over all positive targets.

The first-letter law is

\[
\rho_q(t)=
\sum_{\substack{a\ge1\\3\mid2^a t-1}}
\frac3{2^a}\rho_{q-1}\big((2^a t-1)/3\big).
\]

Expanding the a=1 branch until the first non-one exponent gives precisely
the packet's formula (14), including its terminal all-one term and the
cutoff min(v_3(t+1),q−1). The sums converge at each finite q because
rho_{q-1} is bounded on its finite residue space and the coefficients are
geometric.

The cap is only initial. Later non-one branches change the positive target
and can create a larger ternary valuation budget. The draft correctly
leaves a uniform bound on that transported budget open. Replacing those
budgets by a global supremum would restore the negative-completion spike
that the conditioning was intended to avoid.

## Fixed-positive-target bound: DSP-005 independently verified

Fix a positive **odd** ordinary target t and an exact depth q. A legal
inverse valuation word with total valuation A has weight w=3^q2^{-A}
and a positive odd source x satisfying

\[
t=wx+\beta,\qquad\beta>0.
\]

A residue fiber really does force all prefix inverse steps to be integral:
reducing the depth-q fiber modulo 3^r gives every prefix condition. Starting
from positive odd t, each integral inverse step is positive odd. Its stated
exponent is the exact forward valuation, since its next target is odd.
Thus different legal words at fixed q have different sources. The unique
forward Syracuse trajectory reconstructs their valuations, in reverse
order. Periodic targets do not invalidate fixed-depth injectivity.

At a fixed A, all these sources lie below t/w. Counting them as positive
integers gives at most t/w choices and therefore total weight at most t.
There are 5q+1≤6q integer totals in q≤A≤6q. Above 6q, dropping all
arithmetic restrictions and applying Markov with
E[(3/2)^{A_i}]=3 gives

\[
3^qP(A_1+\cdots+A_q>6q)
\le\frac{9^q}{(3/2)^{6q}}=(64/81)^q.
\]

Hence rho_q(t)≤6qt+(64/81)^q. This is an unconditional positive-source
bound, independent of convergence or a no-return property. It proves the
stated radius ≥1 for the depth generating series at every fixed positive
odd t. The negative point −1 instead has radius ≤2/3 by DSP-001.
It gives neither a finite value at z=1 nor a uniform bound as the positive
endpoint varies. The endpoint factor t must still be controlled in any
transported census.

## Vanishing-loss reference masks: verified in the stated limit order

For a subprobability selection mu_tilde_q≤mu_q with total loss epsilon_q,
the nonnegative density difference has uniform mean epsilon_q. Since
positive-part clipping is 1-Lipschitz,

\[
\widetilde E_q(U)\ge E_q(U)-\varepsilon_q.
\]

For each fixed U the lower bound from DSP-002 is positive, while
epsilon_q→0. Thus taking q sufficiently large retains the same obstruction
to any better uniform polynomial tail exponent. This does not exclude
moving heights U_q and losses of comparable order to U_q^{-delta_*}; the
draft correctly separates that possibility and its still-unpaid census cost.

The reviewed claim scope is now DSP-001--005 plus these two stated
corollaries/lemmas, not only the earlier source snapshot. No further numerical
checks were necessary for these elementary counting and tail inequalities.
