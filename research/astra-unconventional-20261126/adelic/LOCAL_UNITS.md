# Local logarithms and the edge's third quadratic field

**PROPOSED written mathematics.** Use the notation from [PELL.md](PELL.md). At each indicated finite place use the additive valuation normalized by `v_p(p)=1`. The state `x` is an odd positive integer prime to three and `d=2^a` with `d y=3x+1` and `y` odd.

## U1. Two exact valuations of one global unit

At every place above 2 or 3, respectively,

$$v_2(\log_2 E_x)=1+a/2,\qquad
v_3(\log_3 E_x)=1/2+v_3(4x+1).$$

The logarithm on local units is the usual homomorphism extending the series at one and killing roots of unity. From `E_x+E_x^{-1}=12x+2`,

$$(E_x+1)^2/E_x=4(3x+1),\qquad (E_x-1)^2/E_x=12x.$$

Thus `v₂(−E_x−1)=1+a/2>1`. The first Taylor term of `log₂(−E_x)` has strictly smaller valuation than all later terms. For the ternary place `v₃(E_x−1)=1/2` lies exactly at the boundary of that first-term argument. Instead use

$$E_x^3-1=(E_x-1)E_x(12x+3).$$

It has valuation `3/2+v₃(4x+1)>1/2`. Apply the same first-term calculation to `log₃(E_x³)=3log₃(E_x)`. In general `v_p(u)>1/(p−1)` suffices since `v_p(j)≤(j−1)/(p−1)` for `j≥2`. The value is independent of the choice of local embedding, since conjugation inverts the unit.

The ternary quantity has an ordinary dynamical meaning: the distinct inverse sibling `4x+1` has the **same ordinary odd successor** as `x`, with clock `a+2`. Thus the two local logarithms of the same global unit distinguish the outgoing clock and the ternary order of that sibling. They use the integer-unit property, but supply no rational linear relation among the different states' logarithms.

## U2. Asymmetric relative norms

On a single edge write `q=3/d`, `Y=E_y^{-1}`, `v=√q/(U_xU_y)` and `θ=√q U_x/U_y`. Then `θ+v=1−Y`, `θv=qY`, hence

$$(1-\theta)(1-v)=(1+q)Y.$$

When `F_x,F_y` are distinct the left side is the norm to `F_y`; P1 shows that the norm to `F_x` is `1+q`. Dividing the complements in the physical embedding yields

$$\beta=\frac{1-v}{1-\theta}>1,\qquad
\beta+\beta^{-1}=\frac{(1+Y)^2}{(1+q)Y}-2
=2+\frac{36x}{d+3}.$$

Both individual quadratic involutions invert `β`, making it an element of the third quadratic subfield. An explicit formula valid also when field labels coincide is

$$\beta=\frac{(\sqrt{9x+d+3}+\sqrt{9x})^2}{d+3}.$$

The squareclass of its radical is `[x(9x+d+3)]=[F_x]+[F_y]`, where a trivial label means a rational number. The real number `β` and its inverse are algebraic integers exactly when `d+3` divides `x`. This follows from the displayed trace and `gcd(36,d+3)=1`. In the rational degeneracy, algebraic integrality of both inverses would require `β=1`, which the positive formula excludes. If a rational prime `p` has `j=v_p(d+3)−v_p(x)>0`, the trace has valuation `−j`. The roots of the monic quadratic `B²−tr(β)B+1` then have valuations `±j` and lie in `Q_p`: Newton's polygon gives opposite integral slopes of horizontal length one, equivalently the quadratic discriminant is a square in `Q_p` since `p≥5` and `1−4/tr(β)²≡1 mod p`.

## U3. All intervals compose by a rational square root

For `h≥1` successive odd edges from `u` to `w` let `D=2^{A_{i,h}}`, `G=3^h`, `C=Dw−Gu>0`. The interval unit expression is

$$B_{i,h}=\frac{(\sqrt{Dw}+\sqrt{Gu})^2}{C},
\qquad W_{i,h}=\frac{B_{i,h}+1}{B_{i,h}-1}=\sqrt{\frac{Dw}{Gu}}.$$

At length one `B=E_u` and at length two `B=β`. More generally `tr=B+B^{-1}=2+4Gu/C`. The values `W` multiply on concatenating intervals by cancellation of their common intermediate state. On a complete cycle of length `m` and total clock `A`,

$$B_{i,m}=\frac{(2^{A/2}+3^{m/2})^2}{2^A-3^m},\qquad
\prod_{i=0}^{m-1} W_{i,h}=(2^A/3^m)^{h/2}.$$

The identical top expression belongs to the fixed field `Q(√2,√3)` in every rotation. In the actual global multiplicative relation, every `p∤6` records precisely `v_p(W_{i,h})=(v_p(x_{i+h})−v_p(x_i))/2`. In particular primes at which a two-edge `β` has the nonzero valuations in U2 contribute zero to the valuation of its Cayley transform `W`. Locally `W` approaches one of `±1` to that same order: `W−1=2/(β−1)` if `v_p(β)<0`, and `W+1=2β/(β−1)` if `v_p(β)>0`. A prime occurring at just one `β` does not contradict the product. Its possible residual information concerns oriented congruences rather than that product's valuation.

## U4. An integral obstruction to using only the multiplicative balance

The two **actual ordinary paths**

$$25\longmapsto19\longmapsto29\longmapsto11,\qquad
55\longmapsto83\longmapsto125$$

have respective clock lists `(2,1,3)` and `(1,1)`. Their endpoint products agree because `25·55=11·125`. Thus all five source and successor states satisfy the multiplicative balance of a complete cycle, including `∏(1+1/(3x))=2^8/3^5`. All inputs and outputs are ordinary positive integers coprime to 6, yet the endpoint multisets differ. In particular every completely additive real function on the positive integers has total change zero on these five edges. Even arbitrary real prime weights therefore cannot give a strict one-step decrease on all nontrivial states. This is a finite obstruction to the multiplicative-only projection, independent of any conjectural orbit.

The original Pell units retain the discarded information. The endpoint products of their `E_x` differ: for `u>0`, the ratio `E_{5u}/E_u` is strictly increasing, since `log E_u=2 asinh √(3u)` has logarithmic derivative `u(d/du)log E_u=√(3u/(3u+1))`, an increasing function. Thus `E_{125}E_{11}>E_{25}E_{55}`. This distinction does not yet force an ordinary descent.

An opposite five-edge swap has the same total clock eight:

$$7\longmapsto11,\qquad
143\longmapsto215\longmapsto323\longmapsto485\longmapsto91.$$

Here `143=13·11` and `91=13·7`. Consequently no function `H(n)=F(n)+g(log n)` with completely additive `F` and globally convex **or** globally concave `g` can decrease strictly along every nontrivial ordinary edge. For convex `g` the increment `g(t+log 5)−g(t)` is nondecreasing in `t`: the first swap has nonnegative total change. For concave `g` the increment `g(t+log 13)−g(t)` is nonincreasing: the second swap has nonnegative total change. Both conclusions allow all real prime weights, equality, and arbitrary slopes of the correction. They include either sign of a `log E_n` correction.

## U5. A norm-symmetrized Bloch boundary and its exact real regulator

Use additive square-bracket notation in `K*⊗Q` as in P4. For a single edge abbreviate `Q=[q]`, `P=[1+q]`, `E=[E_x]`, `Y=[E_y^{-1}]`, `B=[β]`. The norm identities above give

$$2[\theta]=Q+Y+E,\quad 2[v]=Q+Y-E,\quad
2[1-\theta]=P+Y-B,\quad 2[1-v]=P+Y+B.$$

It follows that

$$\partial\{\theta\}+\partial\{v\}
=\tfrac12\big((Q+Y)\wedge(P+Y)-E\wedge B\big).$$

Flipping the two `y`-radicals interchanges `θ,v` with `−q/v,−q/θ` and sends `Y,B` to `−Y,−B`. Thus the four formal boundary terms sum to `Q∧P=∂{−q}`. These algebraic substitutions for the four arguments and complements hold also at a specialized edge with coincident labels: the norm-symmetrized formula requires no independent involutions after specialization. This gives a genuine Bloch-group element with a rational clock correction. Its real Rogers regulator with the convention of P5 is exactly

$$L(\theta)+L(v)+L(-q/v)+L(-q/\theta)=L(-q).$$

For verification fix any positive real `q`, set `s=v/q` and `θ=(1−v)/(1+s)`, and vary `0<v<1`. The boundary identity in the real rational function field gives a zero derivative for the difference of the two sides, using the differential of P5 (negative signs have zero logarithm after real absolute value). As `v→0`, `θ→1` and `−q/v→−∞`. Their Rogers values cancel at the limit since `L(1)=π²/6` and `L(−∞)=−π²/6`. This proves the identity on every physical edge.

The unprojected half has one invariant clock term and a nontrivial target-field component. Indeed the non-invariant part of twice the half boundary is `(Q−P)∧Y−E∧B`. Full symmetrization removes the latter component on each individual edge. At a rational prime `p≥5` the `(v₃∧v_p)` coordinate of the residual `∂{−q}` is `v_p(d+3)`. These coordinates are nonnegative and at least one is positive on **every** edge, since `d+3>1` is coprime to 6. Consequently a positive sum of the rational clock symbols alone cannot be in the Bloch group, even on a complete cycle. The equality above uses all four signs, and does not furnish a small positive clock-only torsion sum.

## U6. The small positive whole-cycle correction has a nonzero ternary boundary

In U5 the positive half-symbol `{1−θ}+{v}` has boundary `½((Q+Y)∧B−E∧(P+Y))` and contraction `B/2` at any place over three: all of `E,Y,B,P` are ternary units, while `v₃(q)=1`. Its positive sum over a cycle is nonzero since every distinguished real `β>1`. The nontrivial quadratic components cannot be canceled by rational-symbol corrections. At any growth edge the third-field label is nontrivial: equality of the endpoint field labels would force identical squareclasses of the first and third odd states and even sum of the two clocks, contradicted by the coprimality argument at the start of [A6](GROWTH.md).

There is also a direct test of P5's *specific* positive quadratic-order correction, which superficially has exactly the real size wanted for a torsion-gap proof. Let

$$C_i=\tfrac12\{X_i^2\}+\tfrac12\{s_i^2\}-\{-X_iY_i\},\qquad s_i^2=X_iY_i/q_i.$$

Normalize the valuation over three as above and use the contraction convention `ι(a∧b)=v(a)[b]−v(b)[a]`. The facts `v₃(1−X_i²)=1/2`, `v₃(s_i²)=v₃(1−s_i²)=−1` and `v₃(1+X_iY_i)=0` yield

$$2\iota_3\partial C_i=[E_{x_i}]+[s_i^2/(1-s_i^2)]
=[Y_i/(q_i(1-s_i^2))].$$

Here `E_{x_i}s_i²=Y_i/q_i`. If the cycle minimum is `N≥1`, then `Y_i<1/(12N)`, `s_i<1/(3N)`, and the full product of slopes satisfies `∏q_i=∏3x_i/(3x_i+1)≥(3/4)^m`. The product of these real factors is strictly less than `(8N)^{−m}`. Thus the positive correction of P5 has nonzero rationalized exterior boundary on **every** complete ordinary cycle, even though its real regulator tends uniformly to zero with the cycle minimum.

## U7. A uniform regulator grid for actual integral Bloch classes

Let `K` be any finite real multiquadratic field. In the convention of Frenkel and Szenes its Bloch group `B(K)` is cyclic of order dividing **60**. Indeed their Proposition 5.4 gives order `½∏_p p^{m_p}`, where `m_p` is the largest `m` for which `Q(ζ_{p^m})⁺⊂K`. Every quotient of the elementary abelian 2-group `Gal(K/Q)` has exponent at most two. For an odd prime the real prime-power cyclotomic Galois group is cyclic of order `φ(p^m)/2`, permitting only `3,5` among the nontrivial prime powers. At two its order is `2^{m−2}` for `m≥2` and it is cyclic, permitting `2^m≤8`. Thus the product divides `8·3·5=120`. The factor one-half gives 60. Equivalently the group of indecomposable `K₃` has order dividing 240; the totally real Suslin kernel has order four. This keeps the two-primary cases distinct. [Frenkel–Szenes, Prop. 5.4 proof and Cor. 5.5](https://arxiv.org/pdf/hep-th/9304118), [Cisneros-Molina, §5, Prop. 5.7](https://smm.org.mx/boletin_anterior/v10/ne.pdf).

For an **integral** combination `D=Σ n_j{t_j}` of real symbols with zero boundary only in the *rationalized* exterior square, a uniformly safe raw Rogers grid is

$$\sum_j n_jL(t_j)\in(\pi^2/120)\mathbb Z.$$

Here use the usual real extension of the Rogers function when necessary. To justify the factor two, the signed tensor target of the integral Bloch boundary is `(K*⊗K*)/⟨a⊗b+b⊗a⟩`. Its torsion is killed by two: `K*\cong\{±1\}⊕F` with a free abelian `F`, since principal fractional ideals form a free abelian group and its unit kernel is a finitely generated free group modulo `±1`. In a basis of `F` the remaining diagonal tensors are two-torsion, and every tensor with a torsion factor is killed by two. Thus `2D` gives an integral Bloch class. The normalized Rogers homomorphism sends `{t}` to `L(t)−π²/6` modulo `π²`. Its value on `2D` has order dividing 60, giving the displayed grid for the unshifted sum. Rational symbol coefficients with common denominator `b` give denominator `120b`. This is an absolute gap **conditional on the boundary vanishing**, not a boundary-vanishing theorem. U6 shows precisely why P5 cannot invoke it.

For clarity about the scope of real estimates, the rational cycles of P6 can also have pairwise gaps tending to infinity. Choose coprime upper continued-fraction convergents `A/m` of `log₂3` with `δ=A−m log₂3→0`. The phase `r=iA mod m` visits `0,…,m−1`, and the state's numerator over `D=2^A−3^m` is `Σ_j 3^{m−1−j}2^{floor((jA+r)/m)}`, with `0≤j<m`. When `r` increases by one before the wrap, exactly one exponent increases; the numerator increases by at least `3^{m−1}/2`. Therefore successive states in *size order* are separated by at least `1/(6(2^δ−1))→∞` while their full reciprocal sum goes to zero. These positive rational trajectories obey the real closed-cycle identities, the exact dyadic clocks, and more than unit real spacing. Certifying a new positive Bloch element would require a use of integrality that those trajectories do not share.
