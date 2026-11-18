# Almost-sure mean of the raw translated cone

For Lebesgue-almost every phase u simultaneously for 0<θ<1,

    lim_(N→∞) N^(−1) Σ_(q=1)^N S_q^u([θ,1]) = (1/2) log(1/θ).

The result concerns a fixed u through all depths. Its inputs are the
raw odd-grid translation formula and the known L^p ternary offset
density for every 1≤p<2. The averaging uses the natural extension
of tripling. Exceptional specified phases are allowed.

[Finite-depth raw grid and band estimates](TRIADIC_OFFSET.md)
· [Stationary Syracuse density moments](https://rstation.ai/problems/collatz/papers/9/v2).

## A common probability space for all depths

Let the iid positive exponents have probabilities 2^(−a). Write
F_q=Σ_(i=1)^q 3^(i−1)2^(−S_i) in the reals and let Z be the limiting
series in Z₃. Thus F_q represents Z modulo 3^q, and F_q↑F with
0<F<∞ almost surely. In particular E√F<∞ by summing the half moments
using E√(3/2^a)<1. Write λ for ternary Haar probability. For any
code event A let d_A be the density of P(Z∈dz,A) relative to λ;
it exists and is bounded above by the unrestricted stationary density.
With E_q denoting ternary Haar conditional expectation at precision q,

    (E_q d_A)(y)=3^q P(Z≡y mod 3^q,A).

Work on λ(dz)dv for z∈Z₃, 0≤v<1. Put
T(z,v)=(3z+⌊3v⌋,{3v}), z_q=3^q z+⌊3^q v⌋.
This map preserves the product and is ergodic: the independent ternary
digits of z (least significant first) and v (most significant first)
form a two-sided iid ternary sequence, and T shifts its cut by one.
Real ternary expansions with alternate endpoints can be discarded.

For j≥0 set t_j=2j+2{v+1/2} and y_j=2j+1−2z−2 1_{v≥1/2}.
Off the null real endpoint v=1/2 define

    H_q(z,v)= Σ_(0≤j<3^q) (E_q d_{θt_j≤F_q≤t_j})(y_j)/t_j.

Then H_q(T^q(z,u))=S_q^u([θ,1]) off the countable grid-boundary phases,
for every initial z. Indeed shifting the odd representatives by 2·3^q u
moves them by 2⌊3^q u⌋ plus 2{3^q u}; relabeling the least positive
one gives exactly the displayed carry. The ternary component of T^q
reduces to ⌊3^q u⌋ modulo 3^q. The marked mass in that cylinder is the
word slope-sum because J_w=3^q P(w).

## Pointwise limit and an integrable common envelope

For fixed j and almost every v the two positive endpoints θt_j,t_j
are nonatoms of the real F law, since they vary with nonzero slope on
each of two intervals. For any such endpoint b, monotonicity squeezes
the marked Haar averages for F_q≤b between those for F≤b and F_m≤b
when q≥m. The latter fixed-event Haar martingales converge as q→∞;
then let m→∞, using d_{F_m≤b}↓d_{F≤b} almost everywhere by measure
continuity. The same reasoning with strict endpoints works off atoms.
Thus the displayed j summand tends almost everywhere to
d_{θt_j≤F≤t_j}(y_j)/t_j. One may choose these jointly measurable
versions using disintegration of the real coordinate given Z. For fixed
v, y_j is Haar distributed under z since −2 is a ternary unit.
Fubini and countable intersection justify the assertion for every j.

Here a single integrable random bound controls the full sum as q and
the grid size vary. Fix 1<p<p₀<2. For dyadic B≥1 use the majorant
M_B=sup_q E_q d_{F≥B}. The dominated density has L¹ norm
O(B^(−1/2)) and bounded L^(p₀) norm. Interpolation and Doob give
||M_B||_p≤C B^(−δ) for some δ>0. For dyadic B<1 use instead
M_B=sup_q E_q d_{2^(−a₁)<2B}. Conditional on a₁=a the infinite
ternary law is the pushforward of Z by z↦2^(−a)(1+3z), of L^p norm
3^(1−1/p)||d_Ω||_p. The total probability of the eligible a is O(B),
hence ||M_B||_p≤CB by Doob. These majorize every depth-q density with
F_q∈[B,2B), because F_q≤F and 2^(−a₁)≤F_q.

For any depth the portion in band B is bounded by
G_B=B^(−1) Σ_{j≥0:B≤t_j≤2B/θ} M_B(y_j).
For B≥1 only O_θ(B) indices enter, and each term before division by B
has norm at most ||M_B||_p. For B<θ/2 only j=0 can enter, on a real
set of length O_θ(B). Conditional on any such v the y₀-coordinate
is Haar, so ||G_B||_p≤C_θ B^(1/p−1)||M_B||_p=O_θ(B^(1/p)).
The intermediate dyadic bands are finite. Consequently Σ_B G_B∈L^p,
and its tails vanish almost everywhere. This controls the index tail
j→∞ as well, since an eligible large j requires B≥θ t_j/2. Therefore
H_q→H almost everywhere, where H is the same infinite sum over j
with the limiting marked densities. The H_q and H share an L^p envelope.

## The ergodic average

For fixed m the function sup_(k≥m)|H_k−H| is integrable and its
mean tends to zero as m→∞ by dominated convergence. Birkhoff bounds
the limsup of the absolute average error on the diagonal H_q∘T^q
by this mean: ignore q<m, then bound each error by that one function
at T^q. Apply Birkhoff also to H and then let m→∞. This proves almost
sure convergence of the diagonal averages to the integral of H.

For fixed v each y_j is Haar; averaging the marked density gives
P(θt_j≤F≤t_j). As v ranges uniformly, t_j is uniform in [2j,2j+2).
Tonelli gives

    ∫H = (1/2) ∫₀^∞ P(θt≤F≤t) dt/t = (1/2) log(1/θ),

using 0<F<∞ almost surely. The diagonal average depends only on u,
so the full-product result gives the asserted phase statement by
Fubini. First intersect over rational θ and extend to all 0<θ<1
by monotonicity and continuity of the limiting expression.
