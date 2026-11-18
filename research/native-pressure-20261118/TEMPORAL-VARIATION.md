# A uniform temporal variation estimate on nonperiodic ordinary targets

Let g_q(t)=3^q μ_q(t mod 3^q), and g_0=1. For every Q≥1,

    sup_(t positive odd nonperiodic) (1/t) sum_(0≤q<Q) |g_(q+1)(t)−g_q(t)|
       ≤ C sqrt(Q).                                                  (1)

This uses Leen’s balanced synchronization upper bound. In particular the
average absolute temporal increment after normalization by ordinary height
is O(Q^(−1/2)) uniformly in t. Individual inherited spike times remain
uncontrolled by (1).

## Pairwise cancellation

Write L for the geometric transfer. Direct geometric summation gives
g_1(x)−1 equal to −1,0,+1 at residues 0,1,2 modulo 3, respectively.
Thus g_(q+1)−g_q=L^q(g_1−1). At ordinary odd roots we can pair the
negative initial sources x=6m+3 with the positive sources x+2=6m+5.
On any fixed inverse level, the weight of a source y with U^q y=t is
J_q(y)=3^q 2^(−A_q(y)), where A_q(y) is the number of shortcut steps
needed to finish q odd-only steps.

If two paired sources merge at a common shortcut clock with the same
odd count before one finishes q odd steps, their endpoints and total
shortcut clocks upon completing q odd steps agree. Their signed terms
cancel identically. This includes a merger landing at an even common
point: the common remaining divisions to the next odd point are identical.
The triangle inequality therefore bounds the absolute increment at t
by the sum of J_q(y) over sources y reaching t at odd depth q whose
pair has not balanced by their arrival. All sums at each level are
absolutely convergent, since their positive total is g_q(t).
Nonperiodicity makes each source contribute at most once across q.

## Counting the uncancelled sources

Let t lie in the dyadic shell with index ℓ, and y in shell k (shell k is
[2^k,2^(k+1))). Each positive shortcut step changes height by a factor
between 1/2 and 2. Hence the shortcut arrival clock is at least
|k−ℓ|−1. Set s=max(0,min(k,|k−ℓ|−2)). Every contributing pair remains
unbalanced up to shortcut clock s, except that at s=0 we simply count
the whole shell. For a Haar dyadic root z, Leen’s finite-horizon bound
on balanced merger for (z,z+2) gives a failed fraction ≤C/sqrt(1+s).
Failure is a union of complete residues modulo 2^s by his cylinder
dictionary. The shell is a whole number of such periods, as is its
translate by −2 for right partners. Thus at most C 2^k/sqrt(1+s)
contributing sources belong to shell k. Using J_q(y)/t≤1/y, their total
normalized contribution is at most

    C [(1+k)^(−1/2) + (1+|k−ℓ|)^(−1/2)].                           (2)

Leen’s fixed-offset estimate also follows here by taking the union of
the two failure events for adjacent pairs through the intermediate
integer: a common clock and count for both adjacent balanced mergers
can be chosen as the later one.

[Leen, *Exact rates in Collatz synchronization*, finite-horizon bound and exact cylinder dictionary](https://doi.org/10.5281/zenodo.23268751).

Since U(y)≤2y, no source with k<ℓ−Q occurs. Sum (2) from
max(0,ℓ−Q) to ℓ+10Q. Each inverse-square-root sum over this interval
is O(sqrt(Q)), independently of its location. For the remaining shells
y/t>2^(10Q−1), the inequality J_q(y)y≤t forces A_q(y)>10Q−1. In the
geometric word law E[(3/2)^A_q]=3^q. Discard compatibility and use
Markov’s bound to get a total normalized tail bounded by

    (3/2) sum_(q<Q) 9^q (2/3)^(10Q) / t.

This is exponentially small since 9(2/3)^10<1. Together these estimates
prove (1).

[Exact integer level identity](ORDINARY-DENSITIES.md).
