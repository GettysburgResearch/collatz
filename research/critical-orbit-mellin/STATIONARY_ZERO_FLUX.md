# The generation increment at the specified zero cylinder

Fix a continuously differentiable test f on the nonnegative real line
with compact support in (0,∞). Write G_x for the unnormalized real
fibre measure at an odd positive integer x; it has mass H(x)=lim g_q(x)
and vanishes at nonunits. The normalization is that of g_q, with Haar
mean one. For the stationary joint affine law (F,Z) define a ternary
observable

    K_f(z)=Σ_(t odd positive) t^(−1) d_{f(F/t)}(t−2z),

where d is the ternary Haar density of the corresponding marked law.
Define A_q(f)=(E_q K_f)(0), using Haar conditional expectation on the
zero cylinder modulo 3^q. It belongs to the stationary arithmetic
family; freezing the auxiliary real displacement at zero is legitimate
here since the test is smooth and all denominators are at least one.

The individual generation increments have a limit, explicitly

    lim [A_(q+1)(f)−A_q(f)] =
    Σ_(x odd positive) ∫ [ f((B+1/3)/(x+1/3))/(x+1/3)
                           − f(B/x)/x ] G_x(dB).                        (1)

The displayed series is absolutely convergent. It equals ∫f dμ for
the escape distortion measure μ in the finite arithmetic cone theorem,
extended by zero outside [0,1]. Thus the question at zero is an
actual consecutive-increment cancellation. A change in a single
generation can persist under escape; mere Cesàro synchronization of
neighboring ordinary sources does not give this cancellation.

[Arithmetic zero-cylinder criterion](STATIONARY_ARITHMETIC_CONE.md)
· [Limiting escape measure and normalization](HARMONIC_OFFSET_CONE.md)
· [Signed harmonic correction and domination](../unsafe-return-weights/SIGNED_MASS.md)
· [Ordinary real fibre convergence](../native-pressure-20261118/REAL-FIBRES.md).

## Exact generator

The dyadic band and Doob bounds of the solenoid theorem give K_f in
every L^p for 1≤p<2. Here t starts at one; on a fixed dyadic real
band B one has t comparable to B, and only O_f(B) terms occur. Directly

    A_q(f)=Σ_(t odd positive) 3^q E[ t^(−1) f(F/t) 1_{Z≡t mod 3^q} ].

All rearrangements at fixed q are absolutely permissible: for any
0<s<1 the summands in absolute value are bounded by
C_f 3^q t^(−1−s) E F^s. Peel the newest outer exponent a, recalling
F=(3F'+1)/2^a and the analogous ternary identity. Legal positive odd
t and a are in bijection with positive odd x=(2^a t−1)/3, where
a=v₂(3x+1) and t=U(x). The ratio becomes (F'+1/3)/(x+1/3).
The normalized factor 3·2^(−a)/t is exactly 1/(x+1/3). Subtract the
q-th expression. The difference is the right side of (1) with G_x
replaced by its finite cylinder measure 3^q P(F∈dB,Z≡x mod 3^q).
The bracket is bounded uniformly in B by C_f/x²: differentiate
(x+u)^(−1)f((B+u)/(x+u)) with respect to u∈[0,1/3], using boundedness
of f(r) and (1−r)f'(r). At every fixed x the finite measures converge
weakly to G_x. The known g_q(x)≤C H(x) for q≥1 and
Σ_x H(x)/[x(3x+1)]≤δ=(1/2)log(4/3) justify dominated convergence,
proving (1).

For comparison to the physical cone, a compatible q-word from x to t
has F=F_w+J_w F' under the stationary cylinder mixture. Replacing this
by F_w costs at most C_f E(F')^s Σ_x x^(−1−s) in A_q, since
J_w/t≤1/x and f is bounded Lipschitz. For fixed f supported away
from zero, the resulting positive-target sum has no t>2·3^q for
large q by the maximum prefix offset (3/2)^q−1. Its q-normalized
limit is ∫f dμ by the arithmetic cone law, including either convention
on t=1 since its mass is bounded. A convergent increment has that same
Cesàro limit. This proves the claimed identification without interchanging
a spatial sum of two individually divergent root fluxes.

## A positive family of Stieltjes sum rules

For c≥0 set

    L(c)=∫_(0,1] (1+cr)^(−1) μ(dr).

Then one has the exact identity

    δ−L(c) = Σ_(x odd positive) ∫ (1+c)/3
             ·[(x+cB)(x+cB+(1+c)/3)]^(−1) G_x(dB).                    (2)

In particular the right side increases to δ as c tends to infinity,
and 0≤L(c)≤L(0). It is *not* enough to prove L(c)→0 to exclude
escape: this holds for every finite μ carried off zero. The stronger
condition c L(c)→0, even along a subsequence, is equivalent to no
escape, since c/(1+cr) increases to 1/r>0 on its support.

To prove (2) put f_c(r)=(1+cr)^(−1)−1. The proof of the generator
continues to apply: f_c=O_c(min(r,1)), so fixed-q absolute
convergence follows from a positive subcritical real moment, and its
derivative obeys the same bound. Its physical sum on targets beyond
the first period costs O(c 2^(−q)): the outside summands are bounded
by c(3/2)^q g_q(t)/t² and g_q has mean one on each odd period.
On the finite period use its weak limiting distortion law on [0,1];
f_c(0)=0 removes the atom at zero. Thus the increment limit equals
L(c)−L(0). Subtracting the two resolvents in the generator gives
Σ_x H(x)/[x(3x+1)] minus the right side of (2). The signed harmonic
identity is δ−L(0)=Σ_x H(x)/[x(3x+1)]. This proves (2).

In the continuum bulk comparison, replacing the positive odd target
coordinate by density-one-half Lebesgue measure on x>0 and the real
fibre by the stationary marginal gives an elementary comparison after the substitution x=cu.
The continuum integral equals
(1/2) E log(1+(1+c)/(3cF)). It tends to δ because
E log(1+1/(3F))=log(4/3) by real stationarity. Indeed 2^(−a₁)≤F
gives integrable negative log and a positive subcritical moment gives
integrable positive log. Thus a first-order continuum approximation
is consistent with every escape mass. A bound on the error at scale
o(1/c) in (2) relative to δ would decide the question.
