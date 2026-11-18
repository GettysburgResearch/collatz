# Every-depth convergence of the finite Syracuse densities

Use Haar probability λ on Z₃, the Syracuse-offset limit μ, the
probability-normalized densities g_q=3^q μ_q, and ρ_q=(2/3)g_q. Write

    h(z)=lim_(m→∞) essinf_(u≡z mod 3^m) (2/3)(dμ/dλ)(u).

Then, with +∞ permitted,

    lim_(q→∞) ρ_q(z)=h(z)  for every z in Z₃.                         (1)

At ordinary positive integers this gives convergence to the finite
canonical trace at every depth. A sequence of moving positive targets
is not covered by the quantifier in (1).

The inputs are the oversampled joint atom floor in Lemma 7 of
*Hierarchical Syracuse renewal and linear valuation budgets for modular
routing*, and the established existence of the stationary density and
its lower representative. We use the mass inequality of Lemma 7,
which is stronger than the mere existence of modular routes in its
Theorem 8.

[Oversampled fixed-total floor, Lemma 7 and (76)](https://rstation.ai/problems/collatz/papers/48/v2).
[Stationary lower representative and transfer conventions](MINORIZATION.md).
[Prior ordinary Cesàro identification](https://doi.org/10.5281/zenodo.23025885).

## 1. A lower bound for arbitrary nonnegative local terminal functions

A word w of n iid positive geometric exponents has inverse-order offset
β_w, exponent total s, and probability 2^(−s). Its forward affine
map is z↦3^n 2^(−s)z+β_w. Its contribution to the transfer L^n f
at t is 3^n 2^(−s) f(2^s(t−β_w)/3^n) if the argument belongs to
Z₃, and zero otherwise. The transfer preserves Haar integrals,
L^n1=g_n, and L^n of a ternary local function of precision k is local
of precision at most n+k. This last claim holds for the entire
infinite sum because each summand depends only on the same finite
quotient. The one-step density g_1 takes values 0,1,2 at residues
0,1,2 modulo 3, respectively.

Let π_n(s)=P(S_n=s) for the iid geometric sum. The cited Lemma 7
supplies one fixed unit cylinder y modulo 3^u, positive constants
d,c, and an onset, such that for n beyond the onset, 0≤k≤dn,
|s−2n|≤2 sqrt(n) and every β-residue z modulo 3^(n+k) above that
cylinder,

    3^(n+k) P(β_w≡z mod 3^(n+k), S_n=s) ≥ c π_n(s).                (2)

The source gives two further restrictions inside the event; dropping
them is legitimate for this lower bound. The affine numerator and
the orientation agree with the inverse routing formula (83) there.

The bounded-prefix spreading in the proof of its Theorem 8 also
retains mass. For clarity fix an arbitrary unit β-residue z modulo
3^(n+k) and choose 1≤v≤2·3^u with 2^v z≡1+3y mod 3^(u+1).
This uses the fact that 2 generates the unit group. Prepending v in
inverse order transforms β' to 2^(−v)(1+3β'). Thus at length n−1
specify β'=(2^vz−1)/3 modulo 3^(n−1+k) and total s−v; its class lies
in the fixed cylinder. For |s−2n|≤sqrt(n), n sufficiently large and
k≤d(n−1), (2) applies. Prepending v costs probability 2^(−v), so

    3^(n+k) P(β_w≡z, S_n=s) ≥ 3·2^(−v)c π_(n−1)(s−v)
                                ≥ c₁ π_n(s)                           (3)

uniformly in z,s. The last comparison follows, for instance, from
π_n(s)=binom(s−1,n−1)2^(−s) and the local central limit theorem for
a geometric sum in this window, with bounded v. Constants can be
fixed before selecting the terminal precision or residue.

For a unit target t and any terminal residue r modulo 3^k, impose
z=t−3^n2^(−s)r modulo 3^(n+k), a unit. Every contributing word has
a compatible terminal state equal to r modulo 3^k. Conversely this
is exactly the condition for that total s. Multiplying probabilities
by 3^n and summing (3) over the central window therefore gives

    L^n 1_(r mod 3^k)(t) ≥ c₂·3^(−k),                                (4)

since the unconditional window probability is bounded away from zero
by the central limit theorem (variance 2n). This works also for
nonunit r. By linearity, for every nonnegative local f there is a
finite N(f) such that for every n≥N(f)

    L^n f ≥ ε λ(f) g_1    pointwise on Z₃,                            (5)

with ε>0 absolute. Use g_1≤2 on units and g_1=0 elsewhere; decrease
ε if necessary so ε<1.

## 2. Successive removal of a fixed fraction of the integral

Put a(t)=liminf_Q g_Q(t). For every nonnegative local f,

    liminf_Q L^Q f(t) ≥ a(t) λ(f).                                   (6)

When λ(f)=0 the local f vanishes identically. Otherwise start with
r₀=f and b₀=0. At step i choose a fixed n_i for which (5) holds
for the current nonnegative local r_(i−1). Define

    b_i=b_(i−1)+n_i,
    r_i=L^(n_i)r_(i−1)−ε λ(r_(i−1))g_1.

The residual is nonnegative and local. Since λ(g_1)=1 and L preserves
integrals, λ(r_i)=(1−ε)^i λ(f). For each fixed j and Q≥b_j, linearity
and positivity give

    L^Q f(t) ≥ ε λ(f) sum_(i=1)^j (1−ε)^(i−1) g_(Q−b_i+1)(t).

All shifts b_i are fixed before taking Q→∞, so each term has the same
liminf a(t). Take that liminf and then let j grow. This proves (6),
including a(t)=+∞. Approximation from below by bounded local functions
extends (6) to any nonnegative lower-semicontinuous f of finite positive
integral: on each k-cylinder use the infimum of min(f,k); these
approximants increase to f by lower semicontinuity.

## 3. Pointwise convergence

The canonical representative h is nonnegative and lower semicontinuous,
λ(h)=2/3, h≥Lh pointwise, and h is bounded below by a positive constant
on the units. It always satisfies h(t)≤liminf_q ρ_q(t), by taking
local essential infima and using the conditional averages of the
stationary density. Thus at h(t)=+∞ equation (1) already follows.

For finite h(t), apply (6) to h and use h(t)≥L^Q h(t). This gives

    h(t) ≥ (2/3)a(t) ≥ h(t).

In particular a(t) is finite and equals (3/2)h(t). Choose a fixed
δ>0 sufficiently small that h−δg_1 is nonnegative with positive
integral; this is possible by the uniform unit floor. The difference
is lower semicontinuous since g_1 is continuous and bounded. Now

    h(t) ≥ δg_(Q+1)(t)+L^Q(h−δg_1)(t).

Equation (6) bounds the liminf of the last term by
a(t)(2/3−δ) from below. Therefore δ limsup_Q g_(Q+1)(t)≤δa(t).
This proves (1) also at finite points. The same argument with h alone
shows L^q h(t) decreases to h(t), so Lh=h at every finite point.

More generally for bounded continuous f on Z₃ and finite h(t)>0,
the harmonic inverse kernel at t has its single-depth ternary law
converging weakly to μ. For 0≤f≤1, apply (6) to hf and to h(1−f).
Their transfers sum to h(t), and their lower bounds sum to h(t),
so L^q(hf)(t)/h(t)→(3/2)λ(hf)=μ(f). Ordinary roots satisfy the
required finiteness; all their inverse states are ordinary.
