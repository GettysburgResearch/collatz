# Uniform averaged pressure decay, summable drops, and an exact rank obstruction

**PROPOSED; self-audited.** This develops the FIRST-HIT pressure of pass 3,
not the all-history pressure G_2. Keep the source and both clocks fixed.
For positive odd x,t, let J_0(x,t) be the derivative 3^q/2^A at x's first
arrival at t, including the zero-step arrival x=t. Set

    F(t)=sum_(odd x first hitting t) (J_0(x,t)/t)^2.

The exact affine identity gives J_0(x,t)/t<=1/x, without any convergence
assumption. Hence 0<F(t)<5/4. Extend F by zero to even integers.

## P4-1. Uniform spatial averaged vanishing is now unconditional

For EVERY integer a>=1 and K>=1,

    sum_(a<=t<a+K) F(t) <= 20 K^(19/20).             (1)

In particular

    sup_(a>=1) K^-1 sum_(a<=t<a+K) F(t)
                         <=20 K^(-1/20) ->0.        (2)

Proof. For a fixed positive odd x, its distinct forward values in any finite
window form a subset of a sufficiently long simple prefix. If x eventually
cycles, stop before the first repeated value; if not, use a finite prefix
containing the finitely many window values. W2 therefore bounds their number
by 16K^(19/20), uniformly in x and a. Tonelli and J_0/t<=1/x give

    sum_(t in window) F(t)
      <=sum_(odd x) x^-2 #({odd targets first hit by x} in window)
      <=16 K^(19/20) sum_(odd x)x^-2 <20 K^(19/20).

The strict rational bound sum_odd x^-2<5/4 follows from
x^-2 < (1/2)((x-1)^-1-(x+1)^-1) for odd x>=3, plus x=1.
This is an assertion about ALL ordinary targets and the infinite source
sum, not a finite-bank average. No property of unknown large source orbits
is assumed.

For every epsilon>0 the set {t:F(t)>=epsilon} consequently satisfies

    #({F>=epsilon} intersect [a,a+K))
                        <=20 epsilon^-1 K^(19/20). (3)

Thus every fixed positive superlevel has upper Banach density zero.
This does NOT show that such a superlevel is finite. The earlier pointwise
vanishing criterion remains OPEN.

## P4-2. The full pressure really decreases on actual Collatz edges

The following statements include ALL positive odd predecessor sources:

    F(263)-F(395) > 1/3000000,
    F(251)-F(377) > 1/1500000,                       (4)
    U(263)=395, U(251)=377.

A finite certificate proves them. Reconstruct first hits from every odd
source x<=65535 and put A(t)=sum_(x<=65535) (J_0(x,t)/t)^2. Every inspected
source is literally followed to 1, with explicit failure on a clock cap.
No behavior of larger sources is assumed. The reciprocal-square tail gives

    A(t)<=F(t)<A(t)+1/131072                         (5)

for every odd t. The saved exact rational numbers satisfy
A(263)-A(395)-1/131072>1/3000000 and the corresponding second inequality.
The verifier reconstructs these four numbers using raw shortcut steps,
not the producer's accelerated clocks. This repairs the evidentiary weakness
of merely observing a drop in a partial profile: a partial drop by itself
need not survive the unknown tail.

Thus F is not a globally nondecreasing quantity along forward trajectories.
Nor is its reciprocal automatically a decreasing termination rank.

## P4-3. Nevertheless, drops along a nonperiodic orbit are summable

Let t_j=U^j(n) be nonperiodic and let m=min_j t_j. Put
w_j=3t_j/(3t_j+1). Old first-hit sources of t_j remain old sources of t_(j+1),
and their normalized weights are multiplied by w_j. New sources form a
nonnegative, disjoint cohort. Thus

    F(t_(j+1)) = w_j^2 F(t_j)+b_j, b_j>=0.           (6)

Nonperiodicity is needed: on a cycle a first arrival can precede the chosen
edge and the same formula is not a first-hit decomposition.
Since 1-w_j^2<=2/(3t_j), W3 and F<5/4 give

    sum_j (F(t_j)-F(t_(j+1)))_+ <=(800/3)m^(-1/20),
    sum_j |F(t_(j+1))-F(t_j)|
                         <=5/4+(1600/3)m^(-1/20).  (7)

The second estimate follows by telescoping positive and negative variations.
For any finite i<k the retained old sources also give

    F(t_k)>=F(t_i) product_(j=i)^(k-1) w_j^2.        (8)

These are source-persistent variation bounds, not a well-founded rank. They
are compatible with the positive component limits of pass 3.

## P4-4. An ordinary countermodel to an averaged-to-pointwise shortcut

For contrast take V(n)=3n on the positive odd integers, with the same
first-hit normalization by derivative and endpoint. If t=3^r m with 3 not
dividing m, its pressure is

    F_V(t)=m^-2 sum_(j=0)^r 9^-j.

Along the actual ordinary orbit t=3^r, F_V(t) increases to 9/8, so it does
NOT vanish at ordinary infinity. Yet a geometric orbit has at most
1+log_3 K points in any interval of K integers. The same Tonelli argument
therefore gives

    sup_a K^-1 sum_(a<=t<a+K) F_V(t)
                 <=(5/4)(1+log_3 K)/K ->0.

It also has summable pressure variation along each orbit. This is a fully
ordinary positive dynamics example, not a 2-adic completion. It refutes the
inference that uniform spatial averaged vanishing plus bounded variation
along orbits must imply pointwise vanishing. It is NOT a Collatz
counterexample and does not refute a new argument exploiting 3n+1 arithmetic.

## What the pressure route still needs

Pass 3 identifies nonzero pointwise cluster limits with nonperiodic ordinary
components. Equations (1)--(3) now constrain those possible limits to spatially
sparse spikes. No theorem here prevents one fixed ordinary orbit from
following those spikes forever. The required arithmetic anti-concentration
or regularity bridge is still absent, and nontrivial cycles remain separate.
