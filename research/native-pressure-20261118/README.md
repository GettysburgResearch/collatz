# Power-saving descent to every fixed source power

**PROPOSED, pending independent mathematical review.** Let T(n)=n/2 for
even n and (3n+1)/2 for odd n. The clock in this note counts these shortcut
steps on positive ordinary integers. Put k(x)=⌊log₂ x⌋ and define S(x) by taking exactly k(x) shortcut steps
from x. In particular S(1)=1.

For every fixed 0<θ<1 and every fixed log₂3/2<ρ<1 there is η=η(θ,ρ)>0
such that, apart from O_(θ,ρ)(X^(1−η)) sources x≤X, an actual shortcut
iterate T^j(x)≤x^θ occurs at a clock

    j ≤ log₂(x)/(1−ρ).                                             (1)

The exponent is not uniform as θ tends to zero. The threshold x^θ grows
with the source. No fixed-floor result, exclusion of cycles, or resolution
of Collatz follows. The proof uses a finite energy bound for collisions at the actual
ordinary endpoints. All analytic steps are given below.

## 1. Exact arithmetic for a physical native block

A length-k shortcut parity word of weight p has affine form
2^k T^k(x)=3^p x+C, with C≥0. Its residue class modulo 2^k contains exactly
one source in [2^k,2^(k+1)). This follows by lifting one bit at a time:
the two lifts at depth i give T^i values differing by an odd power of 3.
If the odd positions are j₁<⋯<j_p (zero indexed), then
C=∑_(i=1)^p 3^(p−i)2^jᵢ. Since jᵢ≤k−1−(p−i),

    C/2^k ≤ (3/2)^p−1,
    3^p ≤ S(x) < 2·3^p+(3/2)^p ≤ 3^(p+1).                       (2)

For p=0 we have S(x)=1. Thus p is recovered from the *ordinary* endpoint
as ⌊log₃ S(x)⌋. Each endpoint residue modulo 3^p has at most two lifts in
the range (2).

Decompose the word into ℓ initial even steps and p groups, each group
beginning with one odd step followed by aᵢ−1 even steps. Here aᵢ≥1 and
k=ℓ+∑aᵢ. The last state can be even: the final group stops at the
specified physical clock k. With F_a(z)=(3z+1)/2^a in Z₃,

    S(x) ≡ F_(a_p) ∘ ⋯ ∘ F_(a_1)(0)   (mod 3^p).                 (3)

Indeed the omitted initial argument contributes a multiple of 3^p;
all powers of two are ternary units. Every ℓ and positive a-vector gives
exactly one word, hence one ordinary input in its corresponding shell.

Let μ_p be the distribution modulo 3^p of the right side of (3) for
independent exponents with P(a=b)=2^(−b), b≥1. Then for each r,

    ∑_{x: ⌊log₃ S(x)⌋=p, S(x)≡r mod 3^p} 2^(−k(x)) = 2 μ_p(r).       (4)

To check the identity sum (3) over ℓ, using ∑2^(−ℓ)=2, and then over
the exponent vectors. The shell-weight measure has infinite total mass
but (4) is finite for every p. We never assume that the exponents of a
fixed integer are independent. Equation (4) is the exact law *after*
summing actual ordinary source shells with these displayed weights.

## 2. A finite energy inequality for the actual pushed population

Write m_(p,y) for the number of ordinary sources in the input shell
[2^k,2^(k+1)) with odd count p and endpoint y. The following bound
also holds for any interval of 2^k consecutive positive starts, if p is
retained separately instead of being recovered from y:

    ∑_(p,y) 3^p (m_(p,y)/2^k)² ≤ 1+k/2.                           (5)

Fix p,y. The numbers C_w=2^k y−3^p x are distinct nonnegative integers
as x varies over this fiber, and are congruent modulo 3^p. If the fiber
has size m, their sum is at least 3^p m(m−1)/2. Add 3^p m to twice
this inequality and sum the resulting bound on 3^p m² over the fibers.

Every k-bit word occurs once. With x uniform on this entire initial
interval, E[3^p]=2^k. The real affine offset f=C_w/2^k starts at zero
and evolves by f↦f/2 or f↦(3f+1)/2 with the next fair bit. Thus its
expected increment is exactly 1/4 and E[f]=k/4. Dividing the fiber sum
by 4^k now gives (5). The fair bits are used only on the one complete
ordinary input interval; the estimate itself concerns its transported
endpoints, including every collision. For an arbitrary source subset A
the same argument before this final averaging gives the localized bound

    ∑_(p,y) 3^p (m_(p,y;A)/2^k)²
      ≤ 2^(−k)∑_(x∈A) (3^p/2^k + 2C_w/2^k).                       (6)

## 3. The inverse image under S of a power-sparse set is power-sparse

Call B⊂N power-sparse if #(B∩[1,Y])≤C Y^(1−u) for all Y≥1 with u>0.
Enlarge C if needed and take 0<u≤1. For x in [2^k,2^(k+1)), the proportion
with p<k/4 is at most 2^(−(1−h₂(1/4))k) by the binomial exponential bound.
Here h₂ is binary entropy. In the remaining range Cauchy–Schwarz and (5)
bound the proportion with S(x)∈B by

    √(1+k/2) · [∑_(p≥⌈k/4⌉) 3^(−p)
                   #(B∩[3^p,3^(p+1))))]^(1/2)
      ≤ √(3C(1+k/2)/(1−3^(−u))) · 3^(−uk/8).                    (7)

The sum in brackets uses the physical endpoint range (2). Every fixed

    0 < η < min(1−h₂(1/4), u log₂(3)/8)

therefore gives #(S⁻¹(B)∩[1,X])=O_B(X^(1−η)) by summing dyadic shells.
The loss of exponent is explicit and only linear in u. The inequality is
uniform over target subsets with the given counting envelope. It does not
assert a positive gain on top of the uniform pullback of *all* subsets.

## 4. Repeated native descent

Fix log₂3/2<ρ<1 and let B_ρ={y:S(y)>y^ρ}. By (2), this requires
3^(p+1)>2^(ρk), hence p>ρk/log₂3−1. Since ρ/log₂3>1/2, a binomial
upper-tail bound on each input shell, with any fixed cut between 1/2
and ρ/log₂3 for all large k, makes B_ρ power-sparse.

Take a fixed M with ρ^M≤θ. By (7) each S^(−i)(B_ρ), for 0≤i<M, is
power-sparse, and so is their finite union. Outside it the *same*
source satisfies S^i(x)≤x^(ρ^i) for 0≤i≤M. The physical shortcut
clock for these M blocks is at most
∑_(i<M) ρ^i log₂ x≤log₂ x/(1−ρ). This proves (1). In particular X^θ
is also attained in the same time for the retained sources x≤X.

The argument does not keep a positive uniform η as M grows. Knowing
every fixed iterate preserves the class of power-sparse sets does not
make a countably infinite union power-sparse. A target H independent
of x, or the stronger survivor-specific exponent for comparison with
a predecessor lower bound, remains an open obligation.

[Repository fixed-floor obligation and prior transport qualifications](../integrated/exceptional-mass/README.md).


[Exact finite checks and a separate ternary collision estimate](COLLISIONS.md).

Inselmann's Theorem 2.18 previously established power-saving descent to
every fixed source power, with control of intermediate orbit values.
The contribution here is the exact shell collision inequality and its
independent derivation of the pullback estimate. The fixed-target
predecessor input has also been discussed in the repository.

[Inselmann, arXiv:2402.03276](https://arxiv.org/abs/2402.03276).
[Existing fixed-height discussion](../external/mazur-2026/fixed-height-power-saving-attack.md).
