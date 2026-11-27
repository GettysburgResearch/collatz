# A certified fifth moment for the full binary real-width-two layer family

Let λ=log₂3. Let θ→λ, choose an arbitrary mechanical intercept, and consider the complete binary path family of length a→∞ with fixed cut bits. Define the single-variable ordinary numerator polynomial F as in FIFTH_MOMENT_SOURCE_REDUCTION.md. With Haar measure of mass one,

$$
 \limsup\frac{1}{a}\log\int_{\mathbb T}|F|^5
 \le \tfrac43\log3-\tfrac1{7000}.
 \tag{1}
$$

The limit superior allows arbitrary choices of all these parameters. In particular the source theorem there applies with δ=1/10000 in base-three units. For a primitive sequence of positive ordinary integer cycles with binary valuations and real discrepancy W<2, it gives

$$
 \liminf\frac{\log X}{\log P}\ge\frac4{4/3-1/10000}>3.
 \tag{2}
$$

If μ(log₂3)≤3, this class contains only finitely many primitive cycles. This last consequence imports the logarithm ratio bound from arXiv:2610.28079v1, Theorem 11.1. No onset or enumeration of exceptional cycles is obtained. The local result (1) uses neither a logarithm-ratio irrationality theorem nor the Subspace Theorem. The passage (1)→(2) uses the fixed-place integral Subspace Theorem through Weaver 145 Lemma 4. The accompanying finite certificate is integer computer-assisted mathematical verification, without a Lean formalization. The distinct earlier four-state/return Lean checks do not prove this fifth-moment certificate.

## Pre-innovation three-branch transfer

Use the ordinary phase U_i=2^{M_i}3^{a-1-i}v and column V_i=(A_i,C_i) from the source-reduction note. Write e(u)=exp(2πiu), D(u)=diag(1,e(u)), S₁(A,C)=(A+C,C) and S₂(A,C)=(A,A+C). With S=3U_i mod 1 fixed by the past, the current U_i ranges uniformly over the three roots of 3u=S. The next pre-innovation state is 2^{m_i}u. This follows from the gcd of the first i integer characters of the original Haar v; for i=0 condition on S₀=3U₀. Thus the following operator propagates a five-homogeneous upper bound from after one letter to before its unknown ternary digit:

$$
 (T_m J)(S,V)=\tfrac13\sum_{3u=S}J(2^m u,S_mD(u)V).
 \tag{3}
$$

The source-reduction note writes the equivalent evolution conditioned on U_i itself. The integer certificate here verifies (3) on a different family of pre-innovation cochains.

For a nonzero column V=(A,C) use unit Bloch coordinates

$$
 x+iy=2\overline AC/\|V\|^2,\qquad z=(|A|^2-|C|^2)/\|V\|^2 .
$$

Each dyadic witness J_w is extended from this sphere by multiplying by ‖V‖⁵. On the unit sphere it is the real polynomial

$$
 J_w(S,x,y,z)=\sum_{k,s,j}c^w_{ksj} e(kS)
 (x+i\,\operatorname{sgn}(s)y)^{|s|}z^j,
 \quad |k|\le14,\quad |s|+j\le12.
 \tag{4}
$$

The convention for s=0 is that its complex power equals one. The coefficients are integer multiples of 2⁻⁴³, have total absolute mass below 3, and satisfy c_{−k,−s,j}=c_{k,s,j}. The file FIFTH_WITNESSES.txt.gz contains all 76 witnesses indexed by mechanical words of length 75, together with one dyadic scale r_e in (2,6) for each of the 77 length-76 words. Its generator is unnecessary for verification.

For each length-76 word with first letter m, let w,w' be its length-75 prefix and suffix. We verify simultaneously

$$
 J_w>9/100,\qquad T_m J_{w'}\le r_e(1+1/6000)J_w
 \tag{5}
$$

on the entire circle and unit Bloch sphere. Upper boundedness follows from (4). Iterating and sandwiching the initial and terminal cochains between constants times ‖V‖⁵ bounds the expected fifth power of either cut component by the product of these edge scales, up to a bounded factor. The last 75 letters can be assigned an arbitrary mechanical continuation; the word already comes from an infinite mechanical clock. The reference `fifth_verify.py` constructs all phase words independently by their rationally bracketed breakpoints. The exact checks give

$$
 \sum_e |I_e|\log r_e <1.464469599112,\qquad
 \sum_e|I_e|\log r_e+1/6000 < \tfrac43\log3-1/7000
 \tag{6}
$$

at α=λ−1. Uniform rotation frequencies under arbitrary intercepts and θ→λ, as proved in the source note, complete (1). The ordering of the 77 finite breakpoints is checked at both endpoints of the rational bracket 0.58496250071<α<0.58496250073. Distinct breakpoints give the left-endpoint floor word of the open cell immediately following them. For the local statistic the same arbitrary-intercept limit holds for longer rational variables converging to α, with any nonprimitive reduced denominator.

## Separating the circle Fourier coordinate

Measure the angles in radians in this paragraph. Write 2πS=3r and let ψ equal the azimuth of x+iy plus r. Let β be a polar angle, so the rotated input has coordinates (sinβ cosψ,sinβ sinψ,cosβ). The three branches rotate ψ further by 2πd/3 for d=0,1,2. At a rotated point (x,y,z), put σ=−1 for m=1 and +1 for m=2. The squared shear norm and normalized output are

$$
 g=(3+2x+σ z)/2,\quad x'=(x+1+σz)/g,\quad y'=y/g,
 \quad z'=(z-σ(1+2x))/(2g).
$$

When J_w is evaluated at the unrotated vector, its r-frequency is 3k−s. For T_mJ_{w'} the r-frequency is 2^m k. The d-th branch uses the factor exp(2πi 2^m k d/3), the azimuth shift 2πd/3 and the weight g^{5/2}. These formulas account for all signs and both cut states. Put

$$
 T_mJ_{w'}/r_e - J_w = \sum_{h=-68}^{68} R_h(β,ψ)\exp(ihr).
$$

It suffices to bound Σ_h‖R_h‖∞. Some frequencies in this full enclosing range never occur. A grid of 252 equally spaced angles in each of β and ψ includes all the branch shifts in its ψ-coordinate. Extending β around the entire circle is harmless and allows identical trigonometric sampling estimates on both axes.

## Analytic extension off the grid

At a single monomial of sphere degree l=|s|+j, the raw transformed coordinates have affine numerators and common denominator g. Its shear multiplier in front of the l-fold numerator is g^ν, ν=5/2−l. Each numerator factor has modulus ≤g. On the sphere, (3−√5)/2≤g≤(3+√5)/2<2.619. Introduce an auxiliary angle φ with

$$
 g=(5/4)(1+\rho e^{iφ})(1+\rho e^{-iφ}),\qquad \rho=1/\sqrt5<0.448.
$$

Use the first J+1 binomial terms of (1+ρ e^{iφ})^ν with J=80−l, multiply by their complex conjugate and by (5/4)^ν. The result is an ordinary polynomial of degree ≤J in cosφ and hence in g. For a majorant set t_k=|binom(ν,k)|(0.448)^k, B=Σ_{k=0}^J t_k, and

$$
 E=t_{J+1}/\left(1-0.448(1+(|ν|+1)/(J+2))\right).
$$

The denominator is positive. The binomial tails are bounded by E by the term ratio. Nonnormalized harmonic contributions of a transformed monomial are therefore approximated with uniform error at most

$$
 e_l=(2.619)^l (5/4)^{\lceilν\rceil}(2B+E)E.
$$

Indeed the conjugate product difference is at most (2B+E)E and the raw numerator product has modulus ≤g^l. The approximating result has trigonometric degrees ≤80 in each of β and ψ. Each input circle coefficient contributes to a single residual r-frequency and the three branch weights average to one in absolute mass. If all R_h are so approximated by P_h, the total remainder Σ_h‖R_h−P_h‖∞ is at most

$$
 t_e=r_e^{-1}\sum_{k,s,j}|c^{w'}_{ksj}|e_{|s|+j}.
$$

The direct J_w summand already has degree at most 12. These finite sums and all following analytic margins are checked with exact rational arithmetic.

For a complex trigonometric polynomial of degree D in one variable, its supremum is at most (1−(πD/N)²/2)⁻¹ times its grid supremum, for the stated positive denominator. At an absolute maximum take a fixed real component attaining that absolute value, then its first derivative vanishes. Taylor to the nearest grid node and the trigonometric Bernstein inequality ‖P''‖∞≤D²‖P‖∞ give the assertion. One elementary proof of Bernstein differentiates by the Riesz formula using translates by (2j−1)π/(2D), 1≤j≤2D, with coefficients (−1)^{j+1}/(4D sin²((2j−1)π/(4D))). Its value on each exponential mode is its derivative, and the sum of the absolute coefficients is D by the differentiated cotangent sum. Applying the one-axis estimate twice with D=80,N=252 and π≤22/7 gives the rational computable factor C<4. Therefore if U_e bounds Σ_h max_grid|R_h|,

$$
 \sum_h\|R_h\|_\infty \le C U_e+(C+1)t_e.
 \tag{7}
$$

For positivity, write J_w=Σ_k e(kS) J_{wk}(β,ψ) in the original azimuth. At every grid point it is bounded below by J_{w0}−Σ_{k≠0}|J_{wk}|. To extend to the whole sphere, take a global minimum with fixed S and move to a nearest grid angle on each axis. The gradient vanishes at the minimum on the torus. The angular factors in a monomial are (sinβ)^|s|(cosβ)^j exp(isψ). Their β-Fourier absolute mass is at most one, with maximal frequency l=|s|+j. The absolute second derivative along the short displacement is therefore at most (π(l+|s|)/N)². Summing with the coefficient masses and dividing by two gives the rigorous grid-to-minimum correction. Let L_e denote the corrected lower bound. The replay gives

| Certified quantity | Uniform bound over all 77 edges |
|---|---:|
| L_e | >0.094717 |
| U_e | <0.000003059480 |
| t_e | <0.000000000598312 |
| (C U_e+(C+1)t_e)/L_e | <0.000128074 |

The fourth row uses the actual bounds separately on each edge. The rational verifier also checks it directly against 1/6000. Equations (5)–(6) follow.

## Error budget for the integer grid evaluation

The C++20 verifier computes on integers at scale Q=2⁵⁰. Division of fixed-point products truncates toward zero, losing less than one unit u=1/Q; an integer square root rounds down. The Python witness decoder verifies the real coefficient symmetry and the total coefficient bound. The rational angle routine brackets π using the alternating Machin formula and evaluates the sine/cosine Taylor polynomials on one quadrant with rational remainders. Every input coordinate is within u of its true equally spaced circle value, including modular grid shifts. The two nontrivial ternary roots use integer sqrt(3Q²) and a division by two, giving error <2u.

Here are explicit absolute-error estimates on one site. They apply to the complex modulus, except where Cartesian components are named.

1. At the base point |x̃−x|,|ỹ−y|<4u and |z̃−z|≤u. The computed g differs by ≤6u and exceeds 0.38. In the normalized shear, the raw affine numerators differ by at most 5u for x, 4u for y and 9u before the final division by two for z. Since each exact normalized component has magnitude at most one, division by the perturbed g and fixed-point truncation give <64u error per component. The complex x'+iy' therefore differs by <128u.
2. For integer products of two complex fixed-point numbers the code accumulates each real or imaginary numerator before dividing by Q, producing <2u modulus error. Each monomial of total degree ≤12 is evaluated by precomputed powers of x'+iy' and z' and one final product. Each factor has modulus ≤1+128u. Telescoping at most 12 input-factor errors and at most 13 product truncations bounds the final error by (12·128+26)u(1+130u)¹³<2000u. The same bound covers the untransformed sphere and negative s by conjugation.
3. The exact multiplier is g^{5/2}<12. The computed sqrt(g) is the integer floor at scale Q, and its error from using the perturbed g is at most 6u/(2√0.38)+u. Squaring the perturbed g, truncating, and multiplying by this root gives total error <100u. Hence a g^{5/2}-weighted monomial differs in complex modulus by <25000u, including its final multiplication. The lower-degree coordinates are covered at the same budget.
4. All dot products of the dyadic coefficients and computed bases are accumulated exactly in signed 128-bit integers before truncation at scale Q. Coefficient absolute mass <3 bounds each transformed coefficient error by <75002u, and each original coefficient error by <6002u. The three unit-root products each add <80u beyond the transformed error, using total transformed coefficient magnitude <37 and root error <2u. The exact dyadic r_e>2 and the division by 3r_e reduce the transformed error by at least a factor two. Adding the original coefficient error gives <50000u<2⁻³⁰ on each of the 137 residual Fourier coefficients. The grid maximum of its square uses an exact 128-bit integer, and the final square root is rounded upward. The rational checker adds 2⁻³⁰ to every returned grid coefficient bound.
5. On the lower side, at most 29 original coefficient errors occur in J_{w0}−Σ_{k≠0}|J_{wk}|. The computed integer absolute values are rounded upward for the subtraction. The resulting lower estimate therefore needs a correction less than 29·6002u<2⁻²⁸, which is subtracted in full. The positive lower bound and comparison in (7) now hold independently of any floating-point implementation.

The stored dot products before division are bounded in magnitude by 3·13·2⁴³Q, strictly below 2¹⁰⁰. Every grid-value component after that division has magnitude <40Q, and the intermediate branch sums are <120Q. Their squared norms and all fixed-point multiplications fit within signed 128-bit integers. The true and approximate scales remain positive. The C++ verifier's Newton square root uses only integer division and comparisons. The script can replay the full grid and compare all 10,626 saved integer row entries byte for byte using `python3 fifth_verify.py --rebuild --threads 2`. A default run checks the saved finite rows and all rational analytic inequalities without recomputing the grid. The source reduction, analytical norm estimates and arithmetic error envelope are written proof.

## Denominator extension

The same source argument gives (2) with X replaced by Y=dX on a sequence of primitive positive rational binary cycles of common denominator d and log d=o(log P). The scaled recurrence is 2^{e_i}N_{i+1}=3N_i+d, all P distinct N_i are positive integers ≤Y, and the ordinary B-polynomial here is identical. The actual normalized multiplier at the segment is now ω=[−d3^{−n}]_{2^m}/2^m. In the integer-separation proof for the low-frequency sampling estimate one has 2^ma₀−3^nb₀=dk instead of k. Because Y≥P and d=Y^{o(1)}, the bound dk≤2^h exp(−c_ηK) is retained. The nonzero difference remains nonzero, so the rest of the proof is unchanged. Also X tends to infinity and the geometric θ-bound remains a bound for the rational cycle values. Under the same source-qualified μ(λ)≤3, the entire real W<2 binary class consequently satisfies d≥P^c eventually for some c>0, hence has only finitely many primitive cycles at each fixed denominator. The rational controls with exp(o(P)) denominators are compatible with this polynomial bound.
