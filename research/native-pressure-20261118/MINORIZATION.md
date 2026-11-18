# Uniform Haar minorization on the ternary units

Let λ be Haar probability on Z₃, μ the projective Syracuse-offset law,
and ρ=(2/3)dμ/dλ. With the external inputs identified below, an absolute
constant c>0 satisfies

    ρ ≥ c on the ternary units, λ-almost everywhere.                  (1)

Consequently ρ_k(t)≥c for every unit residue modulo every 3^k, k≥1.
This minorizes the mass of *arbitrary* unit subsets linearly in their
Haar mass. The constant constructed here is existential. The law refers
to the geometric valuation model and to exactly identified pushforwards;
a deterministic forward trajectory is not an independent draw from it.

## Transfer and a continuous subfunction

Put F_a(z)=(3z+1)/2^a, p_a=2^(−a), J_a=3p_a for positive a. Define

    T_a f(t)= J_a f(F_a^(−1)(t)) on F_a(Z₃), and zero elsewhere.

On Haar L¹ its norm is p_a times that of f, by change of variables.
Write L=sum_a T_a and T_w for the composition in inverse-prefix order.
For a word w with valuation sum A, ||T_w f||₁=2^(−A)||f||₁.
Tao's fine-scale mixing estimate makes the finite weights ρ_k an
L¹-convergent martingale of mean 2/3. Its limit ρ satisfies Lρ=ρ
since the next geometric step is independent. For any finite prefix-free
collection W of inverse words, positivity gives

    sum_(w in W) T_w ρ ≤ ρ  almost everywhere.                       (2)

Indeed extend each prefix to a common depth d at least its length via
L^(d−|w|)ρ=ρ. The resulting disjoint subfamilies are included in L^dρ.

[Tao, Proposition 1.14](https://arxiv.org/html/1909.03562v7#S1.SS4).

Use the central histories of Mazur’s *Explicit positive-density Collatz
convergence in logarithmic time*, §§3–4 (the original central construction
suffices). Fix an allowed base b₀. At generation n these histories form
a finite prefix-free collection W_n of strings in inverse order: each
successive block ends at a prescribed first crossing, so the end of
the nth block is determined by the prefix up to that crossing. The
central-length and overshoot tests only remove strings. Whether the
sequence passes these tests is a function of the sequence. Integral
compatibility with the target is precisely the support condition of T_w.
With k_n=floor(b_n/4) tending to infinity, put

    Z_n=sum_(w in W_n) T_w ρ_(k_n).

This is a nonnegative locally constant function of the ternary root. At
every sufficiently large positive odd representative M (M≥16^b₀), it
is the central mark Z_n(M) of Mazur §3. Proposition 3.1 gives summable
bounds on ||Z_(n+1)−Z_n||∞ independent of M. For each n the difference
factors through a finite ternary quotient, whose every residue has
arbitrarily large positive odd representatives. The bounds thus hold on
all of Z₃ and Z_n converges uniformly to a continuous z≥0. Proposition
4.2 gives a representative at which z is positive. In particular there
is a unit cylinder C modulo 3^m on which z≥d for some fixed d>0.

The geometric prefix probabilities of W_n sum to at most one. Thus

    || Z_n − sum_(w in W_n) T_w ρ ||₁ ≤ ||ρ_(k_n)−ρ||₁ → 0.

By (2) and uniform convergence, z≤ρ almost everywhere, giving ρ≥d
almost everywhere on C.

[Mazur, *Explicit positive-density Collatz convergence in logarithmic time*, version 2, §§3–4](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf).

## From one cylinder to all units

For any ternary unit t choose e=1 or 2 with 2^e t≡1 mod 3. Its inverse
branches with valuations e+2j are x_j=(2^(e+2j)t−1)/3. For i≠j their
difference has ternary valuation v₃(i−j), by the lifting identity for
4^h−1 and the fact that t is a unit. The j in [0,3^m) thus cover every
residue modulo 3^m. At least one x_j belongs to C, with e+2j≤2·3^m.
Using Lρ=ρ gives ρ(t)≥3·2^(−2·3^m)d for Haar-almost every unit t;
a finite union of affine images of null exceptional sets is null.
Conditional expectation on each ternary quotient proves the finite
claim. Equivalently linear lower transport holds for every unit subset.

## A lower-semicontinuous representative

Set h(t)=lim_k essinf_(s≡t mod 3^k)ρ(s). This is lower semicontinuous,
and h≤ρ almost everywhere by differentiation. It is integrable, and
has positive integral by (1). Applying essential lower limits to Lρ=ρ
gives h≥Lh pointwise: apply the inequality first to any finite set of
branches, shrink within their clopen supports, then use monotone
convergence for the positive sum. L preserves integrals, so h=Lh almost
everywhere. The invariant probability for L is unique: after k steps
each starting distribution has the same image modulo 3^k, because
the affine starting multiplier is divisible by 3^k. Therefore h=c₀ρ
almost everywhere for a positive c₀. Essential lower regularization is
idempotent on h, since lower semicontinuity gives reg(h)≥h and h≤ρ
almost everywhere gives reg(h)≤reg(ρ)=h. Hence h=c₀h pointwise, giving
c₀=1 by its positive finite integral.

The representative can take +∞ at exceptional points. In fact g_k=3^kμ_k
tends to +∞ on a dense Gδ subset of the units. Given any unit cylinder
V modulo 3^b, choose an admissible b-word w with image V, which exists
by positivity of μ_b(V). The map F_1 fixes −1 and has weight 3/2.
For any h≥1, the cylinder F_w F_1^h(−1+3Z₃) is contained in V. By
positivity of transfer and (1), ρ is at least c J_w(3/2)^h almost
everywhere there. Choosing h large gives an open subcylinder on which
the essential lower bound exceeds any prescribed K. For each K the
union of such cylinders is open and dense in the units. On their
countable intersection, conditional means tend to infinity. Each
positive ordinary odd target has bounded conditional means by the
separate antichain argument.

[Pointwise bounds on positive ordinary odd targets](ORDINARY-DENSITIES.md).
