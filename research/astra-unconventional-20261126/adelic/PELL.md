# Pell units, their fields and the Bloch boundary

**PROPOSED written mathematics.** Here `x` is a positive ordinary odd state, `2^a y=3x+1` is its exact odd transition, and `q=3/2^a`. Use positive real square roots in the displayed real identities. Write

$$U_x=\sqrt{3x+1}+\sqrt{3x},\quad E_x=U_x^2,\quad F_x=\mathbb Q(\sqrt{3x(3x+1)}),\quad X_x=E_x^{-1}.$$

`U_x` is an algebraic-integer unit because its inverse is `√(3x+1)−√(3x)`. The field `F_x` is real quadratic since `3x(3x+1)` lies strictly between consecutive integer squares. Its nontrivial automorphism exchanges `E_x` and `E_x^{-1}`. In particular `E_x` is a totally positive norm-one unit with integral trace `t_x=12x+2`. The global unit property uses the literal additive constant one.

## P1. Honest units and a punctured-line equation on every edge

Put `k=√q` and `θ=k U_x/U_y`. One directly has

$$U_y-U_y^{-1}=k(U_x+U_x^{-1}),\qquad
(1-\theta)(1+kU_xU_y)=1+q.$$

For the second identity multiply out and use `U_x²+1=(U_x+U_x^{-1})U_x`. Both `θ` and `1−θ` have zero valuation at every finite prime outside the primes dividing `6(2^a+3)` in a multiquadratic field. Indeed `θ` is a `{2,3}`-unit, and both factors of the second identity are integral outside `{2,3}` while their product is a unit outside the indicated finite set. In the distinguished real embedding `0<θ<1`, since `√(3y+1)>k√(3x)`.

The four formal signed values are `kU_x/U_y`, `k/(U_xU_y)`, `−kU_xU_y`, `−kU_y/U_x`. The product of their complements is `(1+q)²`. These are the four conjugates when the two quadratic Pell fields are distinct, and a formal product with multiplicities in degenerate cases. To check the field statement, set `A=√(3x+1)`, `B=√(3x)`, `D=√(3y)=kA`, `C=√(3y+1)`. Expanding `θ=k(A+B)(C−D)` shows all terms lie in `F_x F_y`: `kAC=DC`, `kAD=D²`, `kBD=qAB`, and `kBC=(AB)(DC)/A²`. The two field involutions independently change the signs of `AB` and `DC` when the fields are distinct, giving the stated list.

Multiplying the physical `θ_i` on any interval of `m` odd transitions with total clock `A` gives `√(3^m/2^A) U_start/U_end`. This has degree bounded independently of `m`, because only the two endpoint radical expressions and the square root of a rational remain. It decreases as the endpoint time increases because all factors lie between zero and one. It is also the normalized divided difference of a square root: with `z_i=2^{A_i}x_i/3^i=n+t_i`, one has `1/(√z_i+√z_{i+1})=√(3^{i+1}/2^{A_i})/U_i`.

Classical fixed-number-field unit-equation finiteness does not apply uniformly to this family. Already at `a=1`, every positive `x≡3 (mod 4)` supplies such an edge with the same allowed prime set `{2,3,5}`. Its `θ` tends to one from below as `x→∞`, by the displayed identity and growth of the two `U`'s. Thus there are infinitely many distinct edge solutions in the varying multiquadratic fields before any cycle condition is imposed.

## P2. Effective no-return of Pell fields at a fixed source

Let an actual shortcut segment of length `H≥1` carry an odd state `x` to an odd state `y`. With `m` odd departures, `d=2^H`, `g=3^m` and `0<C≤3^H−2^H`, the exact equation is `d y=g x+C`. If `F_x=F_y`, then

$$x\le4\cdot36^H.$$

Indeed `R=E_y/E_x` is a norm-one unit in their common quadratic field and `T=R+1/R` is an integer. The rational `g/d+d/g` is not an integer: its reduced-grid numerator `g²+d²` is odd whereas `dg` is even. Consequently their difference has modulus at least `1/(dg)≥6^{-H}`.

On the other hand `E_v=12v+e_v` with `1<e_v<2`, by its trace relation and `E_v>1`. Hence `|dE_y−gE_x|≤12C+2d+2g≤16·3^H`. Using `E_x>12x`, `E_y>12y` and `y≥x/d`, we obtain

$$|R-g/d|+|R^{-1}-d/g|\le 4\cdot 6^H/x.$$

This proves the bound. An exact alternative certificate for one word is the Fricke identity `t_x²+t_y²−T t_x t_y+T²−4=0`. On substituting `d t_y = g t_x + (12C+2d−2g)` the leading coefficient of the quadratic in `t_x` is `d²+g²−dgT`, an odd nonzero integer. For each `T` at most two sources remain, and the segment bounds `R` and its inverse in terms of `H`.

If the starting shortcut value of an `H`-window is `n>4·72^H`, every odd departure value in the window exceeds `4·36^H` since each step reduces by at most a factor two. Hence all its odd departure Pell fields are pairwise distinct. This is a window of length proportional to `log n`, with no conjectural input.

For a whole positive cycle with `f` distinct Pell fields let `H=2f+2`. At least `H/2=f+1` odd departures occur in the `H` steps preceding the cycle maximum `M`, because every odd step has multiplier at most two and every even one multiplier one-half. The start is at least `M/2^H`. Therefore

$$M\le4\cdot144^{2f+2}.$$

On a finite segment from a positive `n₀` replace the right side by `max(2^H n₀,4·144^H)` to cover an early maximum. These bounds give `Ω(log M)` distinct real quadratic Pell fields up to a large record on any fixed escaping path. They require no uniform restriction on the prime generators of the fields. They do not bound how many such fields a fixed seed can generate.

## P3. Whole-cycle unit rank and the telescoping relation

In any finite multiquadratic compositum the logs `σ↦log|σ(E_x)|` are a scalar multiple of the nontrivial quadratic character corresponding to `F_x`. Distinct quadratic fields give orthogonal sign functions on its Galois group. In a given real quadratic field every totally positive norm-one unit is an integer power of its fundamental generator for that subgroup. Write `E_{x_i}=η_{F_i}^{u_i}` with `η_F>1` and `u_i>0`. The rank of the subgroup generated by the `E_{x_i}` is precisely the number `f` of their distinct fields.

For a simple cycle, the subgroup generated by the **normalized edge units** `θ_i²/q_i=E_{x_i}/E_{x_{i+1}}` has rank `f−1` when every field occurs once and rank `f` when a field occurs at two different states. Over `Q` its span consists of the differences of the points `u_i e_{F_i}` in the coordinate space with basis indexed by fields. In the first case these `f` points are affinely independent. In the second, two distinct exponents on one coordinate give that coordinate direction; subtracting the remaining points recovers every other direction. Distinct states have distinct `E_x`, by the trace. The required relation `∏_i θ_i²/q_i=1` always holds: each state appears once in each position. It does not impose an extra relation between the distinct field unit directions.

## P4. Two positive dilogarithm candidates have a nonzero exterior boundary

Use `[v]` here for the additive vector of `v` in `K^*⊗Q` and `∂{z}=[z]∧[1−z]` for the rationalized pre-Bloch boundary. A Rogers-dilogarithm torsion argument that puts a sum in the Bloch group first needs its exterior boundary to vanish. The Steinberg relation kills its image in Milnor `K₂`, a different quotient. The following computations take place before that quotient.

* On an ordinary cycle put `z_i=1/(3x_i+1)`. Every odd cycle state is prime to 3. For each rational prime `p≥5`, the `(v₃∧v_p)` coordinate of `∂{z_i}` is `v_p(x_{i+1})`. In fact `v₃(z_i)=0`, `v₃(1−z_i)=1` and `v_p(z_i)=−v_p(x_{i+1})`. Therefore a positively weighted sum over the cycle cannot have zero boundary if it weights any successor greater than one. Corrections whose arguments **and complements** are `{2,3}`-units have zero in all these coordinates. With signed weights, vanishing in all these coordinates requires `∏x_{i+1}^{w_i}=1` after clearing rational denominators of weights.
* The candidate `{X_{x_i}²}` has argument of order `x_i^{-2}`, so its positive real dilogarithms would be summably small on a high simple cycle. Its boundary has an exact obstruction. The identities `(1−X_x)²/X_x=12x` and `(1+X_x)²/X_x=4(3x+1)` give

  $$\partial\{X_x^2\}=[X_x]\wedge[48x(3x+1)].$$

  Normalize any valuation over 3 by `v(3)=1`. It kills the global unit `X_x`; on an odd cycle it takes the value one on `48x(3x+1)`. Thus contraction of the positive weighted boundary with this valuation equals `±∑w_i[X_{x_i}]`. This vector is nonzero since the product of positive powers of the chosen `0<X_x<1` is strictly less than one. It cannot be canceled by arbitrary rational-symbol corrections either: in the Galois decomposition the `X_x` directions belong to nontrivial quadratic characters, whereas rational vectors are invariant. Repeated fields have positive powers in the same oriented unit direction and do not cancel for positive weights.

The compact adjacent identity `θ_i=(1−X_{x_{i+1}})/(1+X_{x_i})` resembles relations in dilogarithm systems. Its cyclic product equals the slope square root already computed in P1. It supplies neither of the required exterior cancellations above. These are precise obstructions to two proposed positive cycle sums; a different correction using actual nonrational unit directions and odd-prime data remains possible. [Rogers functions and the Bloch boundary](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/fulltext.pdf).

## P5. A five-term identity for complete cycles and ordinary escaping rays

There is a real five-term identity which does survive across the whole orbit. On a single edge abbreviate `X=U_x^{-2}`, `Y=U_y^{-2}`, `v=k/(U_xU_y)` and `s=1/(kU_xU_y)=v/q`. All four quantities belong to `(0,1)`. Indeed `v=θX<X`, while `kU_x>√(3y)` and `U_y>√(3y)` give `s<1/(3y)`. The edge identity gives

$$XY=vs,\qquad (1+X)(1-v)=(1-Y)(1+s)=1+XY.$$

For example `1−Y=θ(1+X)`, `θ=X^{-1}v=Y/s`, and multiplying by `1+s` gives the second equality. Let `L(t)=Li₂(t)+½log|t|log(1−t)` for real `t<1`, with `L(0)=0`. Abel's five-term identity with arguments `Y,−X` gives

$$L(Y)+L(-X)=L(-XY)-L(-s)-L(v).$$

In detail, the remaining two generic arguments are `Y(1+X)/(1+XY)=s/(1+s)` and `−X(1−Y)/(1+XY)=−v/(1−v)`. Apply `L(t/(t−1))=−L(t)`. The mixed-sign branch carries no constant: differentiation of the five-term difference using `2dL(t)=log|t|dlog(1−t)−log(1−t)dlog|t|` gives zero, and the limit as the negative input tends to zero gives zero. The same derivative and limit give `L(t)+L(−t)=½L(t²)`. Consequently the following **positive correction** is exact:

$$L(s_i)-L(v_i)=L(X_{i+1})-L(X_i)+B_i,\qquad
B_i=\tfrac12 L(X_i^2)+\tfrac12 L(s_i^2)-L(-X_iX_{i+1})>0.$$

The endpoint terms telescope over a complete cycle. On an ordinary injective escaping ray the series of corrections converges absolutely. Indeed `X_i<1/(12x_i)`, `s_i<1/(3x_{i+1})`, `0<−L(−t)≤L(t)` for `0<t<1`, and `L(t)=O(t(1+|log t|))` near zero. Bound `L(X_i X_{i+1})` by the sum of the two endpoint-square values using monotonicity. Since the ordinary states are distinct, all corrections on edges with both endpoints at least `N` sum to `O(log(2N)/N)` with an absolute constant. Thus the series of signed clock terms `Σ(L(v_i/q_i)−L(v_i))` converges in time order along *each* escaping ordinary ray, with sum `−L(X_0)+ΣB_i`. On any simple positive integral cycle the signed sum is positive and obeys the same bound with `N` its minimum.

The sign alone also follows from `v_i=θ_iX_i<X_i` and `s_i=X_{i+1}/θ_i>X_{i+1}`. No arithmetic discreteness theorem for the signed clock sum is known here. It varies with the edge units. The identity does not itself put its positive right side in the Bloch torsion group. [Zagier's account of the Rogers function and its functional equations](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/fulltext.pdf).

## P6. An explicit test of the need for integrality

Positive rational cycles with their **exact dyadic clocks** can have every state large and even their full reciprocal sum arbitrarily small. Choose `m→∞` with `δ=ceil(m log₂3)−m log₂3→0`, using irrational rotation. Put `A=ceil(m log₂3)` and `A_i=floor(iA/m)`, extended periodically by `A_{i+m}=A_i+A`. Consecutive differences `a_i=A_{i+1}−A_i` belong to `{1,2}` for all sufficiently large `m`. The composition of the rational maps `z↦(3z+1)/2^{a_i}` is affine, with positive constant term and slope `3^m/2^A=2^{-δ}<1`, so it has a unique positive rational periodic point.

For any cyclic interval of `j≤m` steps starting at `i`, the discrepancy `A_{i+j}−A_i−jA/m` has modulus less than one. Its multiplicative slope `3^j/2^{A_{i+j}−A_i}` therefore lies between `1/4` and `2`. The constant term of each complete rotation is a sum of `m` positive terms, one per step, each bounded above and below by positive absolute constants since the single-step translations are `1/2` or `1/4`. Every periodic state is consequently bounded above and below by constant multiples of `m/δ`. In particular the sum of reciprocals over the full displayed period is `O(δ)`. Each cyclic numerator is odd over the odd denominator `2^A−3^m`, because the explicit affine-composition numerator has an odd first term and all later terms even. This verifies exact valuations `v₂(3x_i+1)=a_i` in the ring of rationals with odd denominator. The estimates remain true if the displayed period repeats a shorter one.

These rational solutions obey the real Pell and five-term identities and all their real smallness estimates. The ordinary-state hypothesis gives genuine algebraic-integer *units*, integral traces and the prime-valuation identities in P1–P4. An exclusion of positive integral cycles through P5 would need a further arithmetic implication of those facts for its signed correction.
