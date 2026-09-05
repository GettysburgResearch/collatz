# Fixed-height forward power saving: exact partial theorem, entropy wall, and the missing killed-transfer gain

> **Overall target status: GAP/BLOCKED.** This note does **not** prove the fixed-height estimate `FWD(beta)` and does not prove Collatz. It proves an essentially sharp one-horizon power-saving theorem, identifies why the obvious repeated-descent argument loses every fixed exponent, rules out an overstrong all-subset anti-concentration premise by mass conservation, and gives an exact killed-set decorrelation criterion that would imply the desired fixed-height theorem. All new claims below are **PROPOSED pending independent review**.

## 1. Target and source boundary

Use the one-division shortcut map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
\]

and, on odd positive integers, the odd-to-odd Syracuse map

\[
\operatorname{Syr}(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}.
\]

For fixed `H` and `C>0`, distinguish

\[
\mathcal B_H^{T}(X;C)=
\{n\le X:T^m(n)>H
\text{ for every }0\le m\le C\log n\},
\]

and

\[
\mathcal B_H^{\rm Syr}(X;C)=
\{n\le X:n\text{ odd and }\operatorname{Syr}^m(n)>H
\text{ for every }0\le m\le C\log n\}.
\]

Either estimate

\[
\#\mathcal B_H^{G}(X;C)=O_H(X^\beta),
\qquad G\in\{T,\operatorname{Syr}\},
\qquad\beta<0.901,
\tag{FH}
\]

is enough for the least-counterexample exponent race: every odd core reaching the least nonconvergent orbit stays above the fixed floor forever under both normalizations. The fixed-height target must therefore be treated as a proof-level Collatz obligation, not as a routine strengthening of natural density.

The imported forward paper proves instead, for every fixed `0<d<5/143`,

\[
\#\mathcal B_H^{\rm Syr}(X;C_{\rm Syr})
\le C_d X(\log H)^{-d}.
\tag{1}
\]

For fixed `H`, equation (1) still has endpoint exponent one. Its separate scheduled no-hit term has a genuine negative power of the *moving passage scale*, but the fixed-target telescope is eventually dominated by the bottom scale. Nothing in the paper states the power saving `(FH)`. All new parity-cylinder arguments below use the one-division map `T`; no clock conversion is hidden.

## 2. New exact theorem: a one-horizon `X^(19/20)` bound

For an integer `X>=2`, set

\[
N_X=\lfloor\log_2X\rfloor
\]

and define the no-descent kernel

\[
\mathcal N(X)=
\{1\le n\le X:T^k(n)\ge n
\text{ for every }0\le k\le N_X\}.
\]

### `MZ-FH-001` — exact finite no-descent power saving

For every integer `X>=2`,

\[
\boxed{
\#\mathcal N(X)\le6499+2X^{19/20}.
}
\tag{2}
\]

This is a genuine forward power saving for failure to descend below the **starting value** during one native parity horizon. It is not fixed-height power saving.

### Proof

Write

\[
v_i(n)\equiv T^i(n)\pmod2,
\qquad
q_k(n)=\sum_{i=0}^{k-1}v_i(n).
\]

Take `n in N(X)` with `n>=6500`. Every state before time `N_X` is at least `n`. At an even step the ratio is `1/2`; at an odd step from a state `x>=n`,

\[
\frac{T(x)}x
=\frac{3+1/x}{2}
\le\frac{3+1/n}{2}
\le\frac{3+1/6500}{2}.
\]

Consequently,

\[
1\le\frac{T^{N_X}(n)}n
\le
\frac{(3+1/6500)^{q_{N_X}(n)}}{2^{N_X}}.
\tag{3}
\]

The exact integer inequality

\[
19501^{6309}<2^{10000}6500^{6309}
\tag{4}
\]

is equivalent to

\[
(3+1/6500)^{6309}<2^{10000}.
\]

If `10000 q_(N_X)<=6309 N_X`, raise (3) to the power `10000` and use (4); its right-hand side becomes strictly less than one. Therefore

\[
10000q_{N_X}(n)>6309N_X.
\tag{5}
\]

Every length-`N_X` parity word is realized by exactly one residue class modulo `2^(N_X)`. Since

\[
2^{N_X}\le X<2^{N_X+1},
\]

each parity word has at most two representatives in `[1,X]`.

Put `z=6309/3691>1`. The number of binary words satisfying (5) is bounded by

\[
\begin{aligned}
\sum_{10000q>6309N_X}\binom{N_X}{q}
&\le z^{-6309N_X/10000}(1+z)^{N_X}\\
&=
\left[
\frac{10000}{3691}
\left(\frac{3691}{6309}\right)^{6309/10000}
\right]^{N_X}.
\end{aligned}
\tag{6}
\]

The exact integer inequality

\[
10000^{10000}<2^{9500}3691^{3691}6309^{6309}
\tag{7}
\]

says that the bracket in (6) is strictly smaller than `2^(19/20)`. Hence the `n>=6500` part of `N(X)` has size at most

\[
2\,2^{(19/20)N_X}
\le2X^{19/20}.
\]

Adding the at most 6499 smaller positive integers proves (2). `□`

## 3. The exponent is essentially the one-horizon entropy limit

Put

\[
\alpha=\frac{\log2}{\log3}
\]

and let

\[
h_2(t)=-t\log_2t-(1-t)\log_2(1-t)
\]

be binary entropy. Numerically,

\[
h_2(\alpha)=0.9499555271\ldots.
\]

For `N>=1`, define

\[
\mathcal N_N=
\{1\le n<2^N:T^k(n)\ge n\text{ for }0\le k\le N\}.
\]

### `MZ-FH-002` — one-horizon entropy wall

\[
\boxed{
\lim_{N\to\infty}\frac1N\log_2\#\mathcal N_N
=h_2(\alpha).
}
\tag{8}
\]

Thus a proof that simply discards the one-horizon no-descent kernel as an exceptional set cannot obtain an endpoint saving larger than

\[
1-h_2(\alpha)=0.0500444728\ldots.
\tag{9}
\]

The exponent-race target needs a saving greater than `0.099`. Better constants in the same one-horizon binomial tail cannot cross that gap.

### Proof of the lower bound in (8)

Call a word `v in {0,1}^N` coefficient-supercritical when, for every prefix length `k`,

\[
3^{q_k(v)}\ge2^k.
\tag{10}
\]

Its canonical positive residue `r_v` modulo `2^N` satisfies the exact affine identity

\[
T^k(r_v)=\frac{3^{q_k(v)}}{2^k}r_v+E_k,
\qquad E_k\ge0.
\]

Equation (10) therefore implies `T^k(r_v)>=r_v` for all `k<=N`; hence every such word contributes a distinct member of `N_N`.

Let `q_N=floor(alpha N)+1`. Every word of weight `q_N` has positive total surplus

\[
q_N\log3-N\log2>0.
\]

For the cyclic sequence of increments `v_i log 3-log 2`, rotate immediately after a global minimum of its cyclic partial sums. Every partial sum of that rotation is nonnegative, including wrapped prefixes because the total sum is positive. The rotation therefore satisfies (10). Each cyclic class has at most `N` words, so the number of coefficient-supercritical words is at least

\[
\frac1N\binom N{q_N}.
\]

Stirling's formula and `q_N/N -> alpha` give the lower exponential rate `h_2(alpha)`.

### Proof of the upper bound in (8)

For `n in N_N`, the same product estimate as (3) gives

\[
2^N\le(3+1/n)^{q_N(n)}.
\tag{11}
\]

Fix `epsilon>0`. The integers

\[
n<2^{(h_2(\alpha)+\epsilon)N}
\]

contribute at most that many points. On the complementary range, put

\[
\alpha_N=
\frac{\log2}{\log(3+2^{-(h_2(\alpha)+\epsilon)N})}.
\]

Then `alpha_N -> alpha`, and (11) forces `q_N(n)>=alpha_N N`. Parity-cylinder injectivity bounds the remaining points by

\[
\sum_{q\ge\alpha_NN}\binom Nq
\le(N+1)2^{Nh_2(\alpha_N)}
=2^{(h_2(\alpha)+o(1))N}.
\]

Thus the limsup is at most `h_2(alpha)+epsilon`. Letting `epsilon` tend to zero proves the upper bound. `□`

## 4. Consequence for actual counterexample roots

Every positive orbit has an attained global minimum because its value set is a nonempty subset of the positive integers. If an orbit never enters `[1,H]`, its global minimum `a>H` satisfies

\[
T^k(a)\ge a\qquad(k\ge0).
\]

Hence the set of possible global minima below `X` obeys the same `X^(19/20)` upper bound from `MZ-FH-001`.

This does **not** bound all starts whose orbit has that minimum. A single minimum may have a large predecessor basin. The imported inverse theorem guarantees at least `X^0.901` predecessors for every eligible fixed target, so replacing starts by their minima is exactly the forbidden quantifier collapse.

The fixed-height problem is therefore not the problem of counting root minima. It is the problem of controlling the pullback of a sparse set through long, highly nonuniform predecessor fibers.

## 5. Why the obvious repeated power-descent proof loses the exponent

The power-descent trajectory methods discussed in the imported forward paper give power-sparse exceptional sets for descent to a fixed power of the source, and finite iteration can be organized by pullback. They do not state a fixed-height power saving.

The loss can be seen abstractly. Suppose one descent stage sends the good part of `[1,X]` into `[1,X^r]`, where `0<r<1`. Assume only the generic fiber estimate

\[
\#F_X^{-1}(A)\ll X^{1-r}\#A.
\tag{12}
\]

If a lower-scale exceptional set has size

\[
O((X^r)^{1-D}),
\]

its pullback under (12) has size

\[
O(X^{1-r}X^{r(1-D)})
=O(X^{1-rD}).
\tag{13}
\]

Thus the density exponent transforms as

\[
D\longmapsto rD.
\tag{14}
\]

After `J` scale descents it is `r^J D`. Reaching one fixed floor requires

\[
X^{r^J}=O_H(1),
\qquad
r^J\asymp_H\frac1{\log X}.
\]

The last pullback term therefore has the form

\[
X^{1-Dr^J}=X\exp(-Dr^J\log X)=\Theta_H(X),
\tag{15}
\]

up to the accumulated polylogarithmic constants. This reproduces a fixed-height density coefficient, not `X^beta` with fixed `beta<1`.

### `MZ-FH-003` — exponent-collapse verdict

A repeated power-descent argument using only the generic scale fiber `X^(1-r)` cannot establish fixed-height power saving. It needs an additional gain correlated with the lower-scale survivor set.

This is a method-boundary theorem, not a statement that every refinement of a power-descent architecture must fail.

## 6. Why uniform all-subset anti-concentration is impossible

A tempting repair of (12) is to demand, for some `delta>0`,

\[
\#F_X^{-1}(A)\ll X^{1-r-\delta}\#A
\tag{16}
\]

for every subset `A` of the endpoint range. This cannot hold for a descent map defined on `X-o(X)` sources and taking at most `O(X^r)` endpoint values.

Indeed, take `A` to be the complete image. Then the left side is `X-o(X)`, while the right side is `O(X^(1-delta))`. Equivalently, the average fiber already has order `X^(1-r)`, so some singleton fiber is at least that large.

### `MZ-FH-004` — mass-conservation obstruction

Any power gain beyond the generic fiber scale must be specific to the **killed survivor set**, or must be expressed as cancellation in a signed/weighted operator. It cannot be a positive counting inequality uniform over all endpoint subsets.

This correction is load-bearing: a global anti-concentration premise of the form (16) would make a conditional bootstrap formally true but its hypothesis impossible.

## 7. Exact sufficient criterion: killed-set decorrelation

The mass-conservation obstruction identifies the right kind of missing theorem. The endpoint gain must exploit the fact that the endpoint is itself required to remain above the fixed floor for the rest of the clock.

Fix constants

\[
0<r<1,
\qquad D>0,
\qquad\delta>0,
\qquad c>0.
\]

Fix `G=T`; the identical abstract proof applies to `Syr` after restricting source and endpoint counts to odd integers. For each sufficiently large `X`, suppose there is a partial descent map `F_X`, defined outside a local exceptional set `E_X`, such that:

1. **physical descent:** `F_X(n)=G^(t_X(n))(n)` for some `0<=t_X(n)<=c log X`;
2. **scale reduction:** `F_X(n)<=X^r`;
3. **local exceptional saving:** for one fixed `K`,
   \[
   \#E_X\le KX^{1-D}.
   \tag{17}
   \]

For a fixed `H`, define an integer recursive horizon by

\[
L_H(X)=0
\quad(X\le X_H),
\]

and, above the base scale,

\[
L_H(X)=\lceil c\log X\rceil+L_H(\lfloor X^r\rfloor).
\tag{18}
\]

Let

\[
S_H(X)=
\{1\le n\le X:G^j(n)>H\text{ for every }0\le j\le L_H(X)\}.
\]

Assume the following **killed-set decorrelation** for some `K_H` and all sufficiently large `X`:

\[
\#\{n\le X:n\notin E_X,
F_X(n)\in S_H(\lfloor X^r\rfloor)\}
\le
K_HX^{1-r-\delta}
\#S_H(\lfloor X^r\rfloor).
\tag{19}
\]

Unlike (16), equation (19) concerns one dynamically defined sparse set and does not contradict mass conservation.

### `MZ-FH-005` — killed-transfer bootstrap

Under (17) and (19), for every fixed `H` and every

\[
\beta>
\max\left\{
1-D,
1-\frac\delta{1-r}
\right\},
\tag{20}
\]

one has

\[
\#S_H(X)=O_H(X^\beta).
\tag{21}
\]

Moreover,

\[
L_H(X)\le\frac{c}{1-r}\log X+O_H(\log\log X),
\tag{22}
\]

so, after dyadic shelling and a harmless enlargement of the clock constant, (21) implies the pointwise fixed-height estimate

\[
\#\mathcal B_H^{T}(X;C)=O_H(X^\beta)
\]

for every fixed `C>c/(1-r)`.

### Proof

The geometric logarithm sum in (18), with one ceiling at each of `O_H(log log X)` levels, gives (22).

Write `B_H(X)=#S_H(X)`. A source in `S_H(X)` either lies in `E_X`, or its physical endpoint remains above `H` for the lower recursive horizon and hence belongs to `S_H(floor(X^r))`. Equations (17) and (19) give

\[
B_H(X)
\le KX^{1-D}
+K_HX^{1-r-\delta}B_H(\lfloor X^r\rfloor).
\tag{23}
\]

Choose `beta` as in (20). Then

\[
\eta_1=\beta-(1-D)>0,
\]

and

\[
\eta_2
=\beta-(1-r-\delta+r\beta)
=\delta-(1-r)(1-\beta)>0.
\]

Assuming inductively that `B_H(Y)<=C_HY^beta` below `X`, equation (23) gives

\[
B_H(X)
\le KX^{\beta-\eta_1}
+K_HC_HX^{\beta-\eta_2}.
\]

For sufficiently large `X`, both power losses absorb the fixed constants. Enlarging `C_H` over the finite base range closes strong induction and proves (21).

Finally, on a dyadic shell `X/2<n<=X`, equation (22) is at most `C log n` for all sufficiently large `X` whenever `C>c/(1-r)`. A point that remains above `H` for `C log n` steps lies in `S_H(X)`. Summing the shell bounds preserves exponent `beta`. `□`

## 8. Numerical crossing requirement

The imported inverse theorem has

\[
\gamma=0.901.
\]

The criterion gives a complete Collatz proof if its parameters satisfy

\[
D>0.099
\qquad\text{and}\qquad
\frac\delta{1-r}>0.099.
\tag{24}
\]

Indeed one may then choose

\[
\max\{1-D,1-\delta/(1-r)\}<\beta<0.901
\]

and apply `MZ-BRIDGE-001`.

`MZ-FH-001` does **not** itself instantiate the scale-reduction hypothesis: outside its exceptional kernel one obtains some strict descent below the source, not a fixed bound `X^r`. The entropy theorem nevertheless gives a rigorous one-horizon obstruction. At dyadic scale `X=2^N`, for every fixed `r<h_2(alpha)`, all but at most `X^r` of the `X^(h_2(alpha)-o(1))` coefficient-supercritical roots lie in `(X^r,X]`; none reaches `X^r` during the first `N` shortcut steps. Therefore any `N`-step stage that demands reduction to `X^r` must have local exceptional exponent at least `h_2(alpha)-o(1)`, so its saving satisfies

\[
D\le1-h_2(\alpha)=0.0500444728\ldots
\]

for `r<h_2(alpha)`. Such a one-horizon split cannot cross `0.901`, even with arbitrarily strong killed transfer. This does not rule out a longer stage, a weaker reduction with `r>=h_2(alpha)`, or a joint operator that handles the no-descent roots rather than placing them in `E_X`. A successful proof must do at least one of the following:

- obtain a stronger local saving using more than the native parity horizon;
- handle the no-descent kernel structurally instead of discarding it;
- increase the inverse exponent toward one;
- prove a joint operator inequality in which local failure and killed transfer are not separate maxima.

## 9. Concrete next certificate

The most focused new finite or symbolic target is equation (19), together with a local split satisfying `D>0.099`. A proof-producing search should use a state carrying:

- source and endpoint residue information modulo a controlled power of three;
- a scale or logarithmic-height bin;
- first-passage status above `H`;
- enough parity history to preserve one physical source;
- a weight vector for a killed `ell^1` or weighted `ell^p` norm.

The certificate must prove contraction on the dynamically surviving endpoint family, not on every positive endpoint set. In operator language, the source-to-endpoint transfer is mass-preserving before killing; the desired gain belongs to the killed operator.

A first meaningful milestone is any rigorously certified pair `(D,delta/(1-r))` with both positive. The full imported-exponent crossing requires both to exceed `0.099` unless the recursion is sharpened.

## 10. Checks and evidence boundary

The companion checker verifies with exact integer arithmetic:

- equations (4) and (7);
- the simpler comparison `3^6309<2^10000`;
- parity-word/residue bijectivity through depth 16;
- every ballot root's actual no-descent property through depth 16;
- the cyclic-minimum rotation used in the lower entropy bound through depth 16;
- the finite inequality (2) at dyadic cutoffs through `2^16`;
- the exponent algebra in `MZ-FH-005` at one illustrative crossing-grade parameter point.

The checker does not prove the asymptotic analysis, killed-set decorrelation (19), fixed-height power saving, `SC*`, `FC*`, or Collatz. No large external certificate or Lean build was replayed in this continuation.

## 11. Status conclusion

The requested fixed-height theorem is not established by the present source results or by this attack. The strongest new proved statement is the exact `X^(19/20)` one-horizon no-descent bound, together with its essentially sharp entropy interpretation. The first unsupported inference in the hoped-for proof is now isolated exactly as the killed-set decorrelation gain (19), with mass conservation ruling out the superficially stronger all-subset version.

That is the next theorem to attack; iterating existing density statements without it cannot retain a fixed endpoint exponent.
