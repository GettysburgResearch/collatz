# Uniform translated packing, with an explicit arithmetic constant

**PROPOSED; self-audited.** Use the raw shortcut map T(n)=n/2 for even n and
T(n)=(3n+1)/2 for odd n, on positive integers. Put beta=19/20.
This is a self-contained quantitative reconstruction of an established
orbit-sparsity mechanism, not a claim to have discovered uniform sparsity or
its entropy threshold. See [SOURCES.md](SOURCES.md) for the stronger related
literature found during this pass. The new consumers are the pressure and
coefficient-record statements in this directory.

## W1. A finite-path envelope that retains the interval location

A simple segment is a finite consecutive trajectory x_0,...,x_L with all
states distinct. Let M(K) be the supremum of its number of states in any
integer interval [a,a+K), over all simple segments and all integer a>=1.
It is finite, with M(K)<=K. Cycle sets, counted once, are also covered by
such segments. A nonperiodic infinite trajectory is covered by its finite
simple prefixes.

Fix an integer k>=1. Removing the last k states of a segment costs at most k
states (remove the whole segment if shorter). On the retained states T^k is
injective and its images are still in the same simple segment. This terminal
removal is essential: a convergent preperiod is not itself a globally
collision-free set at arbitrary later clocks.

A length-k parity word of weight q has the exact identity

    2^k T^k(n) = 3^q n + C_w.

Its legal sources form one residue modulo 2^k. The parity words biject with
those residues. Furthermore

    3^q-2^q <= C_w <= (3^q-2^q) 2^(k-q).             (1)

Both extrema are attained, by moving all the odd steps to the beginning or
the end, respectively. For example, swapping adjacent 10 to 01 increases
C_w by 2^i 3^r, where i is the preceding length and r the following odd count.
This proves (1), including q=0.

Consequently all q-labelled images of sources in [a,a+K) lie in ONE real
interval whose location depends on a and q, and whose number of integer
points is at most

    L(K,k,q) = 1 + floor((3^q(K-1)
                  +(3^q-2^q)(2^(k-q)-1))/2^k).      (2)

We do not replace different q-labels by one interval or reset the source.
In particular L<=3^q K/2^k+(3/2)^k+2. For any 0<=m<=k for which the children
L(K,k,q)<K, q<=m, the following complete finite inequality holds:

    M(K) <= k + ceil(K/2^k) sum_(q=m+1)^k binom(k,q)
                   + sum_(q=0)^m M(L(K,k,q)).        (3)

The high lane counts all possible source residues, including failures of
compression. The low lane uses injectivity at the SAME physical clock and
then the same universal translated-window envelope. No equidistribution or
random model occurs in (3).

## W2. An explicit universal bound

For every K>=1,

    M(K) <= 16 K^(19/20).                            (4)

Here is an all-K induction, not a fitted exponent. For K<2^32 the trivial
bound suffices, since K^(1/20)<2^(8/5)<16. Otherwise set
k=floor(log_2 K)>=32 and m=floor(log_3(2^k))-2. Then m>=0.
Write r=12/7. Two exact integer inequalities are

    3^147 < 2^233,
    19^4660 < 7^1720 3^2940 2^10307.                (5)

They give log_3 2>147/233 and
(1+r) r^(-147/233)<2^(19/20). Since m>=147k/233-3,

    sum_(q>m) binom(k,q)
      <= r^(-m)(1+r)^k <= r^3 2^(19k/20).

Each source residue appears at most twice because 2^k<=K<2^(k+1).
Thus the entire high lane is at most

    2(12/7)^3 K^beta < 11 K^beta.                    (6)

All low children are strictly smaller than K: 3^q/2^k<=1/9 and
(3/2)^k+2<K^(3/5)+2<K/2 for k>=32. Concavity gives

    sum_(q<=m) L(K,k,q)^beta / K^beta
      <= 3^(-2 beta)/(1-3^(-beta))
                   +(k+1) 2^beta K^(-2 beta/5)
      < 9/40 + 1/40 = 1/4.                         (7)

For transparency, the rational certificates behind the last line are:
3^39>2^60 implies 3^(-beta)<3/8, and hence the geometric sum is <9/40.
The inequality 3^5<2^8 gives (3/2)^k<2^(3k/5), and K^(3/5)+2<=2K^(3/5).
For k>=32,

    2(k+1)2^(-19k/50) < 1/40.

At k=32 this is certified by 2640^50<2^608. The left side decreases
thereafter, because (k+2)/(k+1)<=34/33<5/4<2^(19/50); the last comparison is
5^50<2^119. These integer checks certify the analytic induction, not merely
its first several instances.

Finally k<=2^(k/2)<=K^beta. Inserting the induction hypothesis in (3),
then (6)--(7), gives

    M(K) <= (1+11+16/4)K^beta = 16K^beta.

This proves (4). The constant is deliberately simple and not claimed optimal.
The bound can exceed K at feasible widths; it is a theorem about all widths,
not a claim that this numerical constant is already a practical census gain.

## W3. A translated reciprocal budget

For every simple segment S with all its states >=n>=1,

    sum_(x in S) 1/x <= 320 n^(-1/20).               (8)

Indeed N_S(t)<=16t^beta by (4), and Tonelli's identity gives
sum 1/x=integral_n^infinity N_S(t)t^-2 dt
<=16/(1-beta)n^(beta-1). There is no duration or maximum-height factor.
An infinite nonperiodic orbit follows by monotone limits. A cycle is counted
once; repeated laps must NOT be inserted with multiplicity.

More generally, for integer a>=0, n>=1 and s>beta,

    sum_(x in S, x>=a+n) (x-a)^(-s)
       <=16s/(s-beta) n^(beta-s).                   (9)

The translated interval hypothesis, not merely an anchored count, proves
this version. In particular any simple L-edge segment has span at least
((L+1)/16)^(20/19)-1. There is no resulting bound on its elapsed time unless
its span has independently been bounded.

## Boundaries

A predecessor basin can have many sources with the same T^k image, so (3)
does not apply to it as a set. Cycles remain allowed. The right-tail step in
(6) uses a threshold above the binomial mean: log_3 2>1/2. Substitution of
5 for 3 would put log_5 2<1/2 and destroy that step. The check suite retains
this failed 5x+1 transfer explicitly.
