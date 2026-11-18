# Near-full rotation gcd on primitive positive rational cycles

**Proposed counterexample to a quantitative route, not an integer cycle.**
There exist cyclic shortcut parity words of least period L tending to infinity,
with K ones and D=2^L-3^K>0, whose unique positive rational orbits satisfy:

* The least state tends to infinity, and the total homogeneous defect
  L-K log₂3 tends to zero.
* Every state has the same reduced denominator H>1, coprime to 6, with
  log H = O(sqrt(L) (log L)^3).
* For every cyclic rotation numerator N_i, gcd(D,N_i)=D/H. In particular
  gcd(D,N_i)>=D exp(-O(sqrt(L)(log L)^3)) simultaneously at all rotations.
  Also log D is asymptotic to L log 2.

Thus an upper bound saving exp(L^alpha) from D for every such formal word
is false for every alpha>1/2, even after imposing primitivity, high minimum,
small total defect and all rotation numerators. The examples have large
gcd(L,K), and they retain explicit obstructions at primes of D. They do
not resolve whether H=1 is ever possible for a nontrivial positive word.

## Independent periodic inputs with a common affine slope

Let b/a be an upper continued-fraction convergent of c=log₂3 with a large.
Then gcd(a,b)=1 and 0<b-ac<1/a. Take the primes p_1,...,p_k starting at
5, with n their largest consecutive product <=a/log a. In particular
k tends to infinity. At each block index i modulo n encode the k bits
s_(j,i)=1 if p_j divides i, zero otherwise. Encode a bit zero as the
two shortcut letters 10, and one as 01, concatenating the k pairs in a
fixed order. Finish each block with a-k ones and then b-a-k zeros.
Both runs exceed six eventually. The block has b letters and a ones.
The centered transition from six consecutive ones to six consecutive
zeros occurs exactly once per block and always at the same offset:
among the encoding pairs a run has length at most two. Therefore every
cyclic period in letters is a multiple of b. The k component indicators
together have least period n, so L=bn and K=an.

Set A=3^a, B=2^b, lambda=A/B<1. The pair 10 acts as (3x+1)/4 and
01 acts as (3x+2)/4. Composing blocks gives the following exact rational
recurrence at block boundaries:

    B x_(i+1) = A x_i + C + sum_j v_j s_(j,i).

Here C is the integer numerator for the all-zero bit block, and every
v_j is a positive product of powers of 2 and 3: the difference in pair
numerators is one and every surrounding linear numerator or denominator
is smooth. By linearity the unique fixed value before block zero is

    x_0 = C/(B-A) + sum_j v_j A^(p_j-1)/(B^p_j-A^p_j).

Indeed a single indicator contributes its inhomogeneous term at the first
step of its own p_j-block cycle. This formula shows that H divides
(B-A) times the product of the B^p_j-A^p_j.

To see that H>1, fix any selected prime p. The geometric factor
Phi_p=(B^p-A^p)/(B-A) has a prime divisor ell not dividing B-A.
Otherwise its only possible prime divisor is p, by reducing the
geometric sum modulo a common prime. If p divides B-A the binomial
expansion at B=A modulo p shows v_p(Phi_p)=1 (p is odd and p does
not divide A). But Phi_p>p. For the resulting ell the order of B/A
modulo ell is p. Hence ell divides neither the constant denominator nor
any of the other component denominators. The numerator of the p-term
is coprime to ell. Its negative valuation cannot cancel. This also
exhibits a failing prime of the full denominator rather than relying
on the absence of previously known integer cycles.

## Size, phase changes and global positivity

At a block boundary the affine multiplier is lambda. Its additive
offset is at least lambda/3: the first of the k pairs contributes the
positive constant 1/4 or 2/4 and the remaining homogeneous multiplier
is lambda/(3/4). The least boundary value is therefore at least
lambda/(3(1-lambda)). Every proper prefix within a block has multiplier
at least min((3/4)^k/2,lambda). This is immediate for the pairs; after
the pairs the multiplier first increases along the common ones and
then decreases to lambda. All prefix offsets are nonnegative.
Since 1-lambda=O(1/a), every state is at least a exp(-O(k)), which
tends to infinity (k=O(log a/log log a)). The total homogeneous
defect n(b-ac) is at most 1/log a. The shortcut rational orbit realizes
all indicated parities: its full fixed-point denominator D is coprime
to 6, and the affine numerator at each rotation modulo 2 is the
prescribed first bit. On powers of 2 and 3 the reduced denominator
is therefore unchanged, and at every prime ell dividing D the rotation
formula 2N_(i+1)=3^(e_i)N_i+e_iD preserves the gcd with D.
This proves the simultaneous assertion at all phases.

By the prime number theorem, p_(k+1)=O(log a) and sum_(j<=k) p_j=
O((log a)^2). For example log n is the sum of log p over these
consecutive primes, asymptotic to p_k, and p_(k+1)/p_k tends to one.
Maximality gives n >= c_1 a/(log a)^2 for an absolute c_1>0. Since
b is comparable to a, b=O(sqrt(L) log L), and the explicit denominator
formula gives the claimed log H bound. Finally B^(n-1)<=B^n-A^n<B^n
(the difference is at least (B-A)B^(n-1)). This establishes the
asymptotic for log D without any effective irrationality measure.
