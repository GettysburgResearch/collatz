# A computable inverse horizon from exact finite mixing certificates

**Status:** new finite written theorem and eight Lean-checked algebraic
statements. The asymptotic size of the calibrated horizon uses Tao's
marginal mixing theorem. The infinite-depth canonical-potential bound and
full Collatz remain **OPEN**.

This continuation replaces the constants hidden in the previous
polylogarithmic horizon with an exactly computable rational error. It
produces **one computable horizon growing faster than every fixed power of
the logarithm of the predecessor floor**, while keeping all ordinary
sources and all valuation clocks. For each particular finite certificate,
its density bound uses only finite rational data and the ordinary counting
argument; it does not require a numerical mixing constant.

The small matrices checked here validate the computation. They do not
produce a useful numerical Collatz cutoff: the three displayed calibrated
horizons are all one.

## 1. Inputs and ordinary domain

Use the accelerated odd map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers, and call an integer a unit when it is not
divisible by three. The actual inverse operator is

\[
Pf(q)=\sum_{\substack{e\ge1\\2^eq\equiv1\pmod3}}
\frac3{2^e}f\!\left(\frac{2^eq-1}{3}\right),
\qquad D_s=P^s1.
\tag{J1}
\]

Every displayed parent is a positive odd ordinary integer. The functions
\(D_s\) are periodic modulo \(3^s\). For \(s\ge1\), they vanish
on multiples of three. Since \(P1\) takes values \(0,1,2\), positivity
gives the elementary uniform bound

\[
0\le D_s(q)\le2^s.
\tag{J2}
\]

Fix a positive odd unit target \(q\), a real floor \(b\ge1\), and a
finite horizon \(K\). The only predecessor-floor premise needed is

\[
U^j(n)=q,\quad j\le K,\quad n>0\text{ odd unit}
\quad\Longrightarrow\quad n\ge b.
\tag{J3}
\]

This includes \(q\ge b\), from depth zero. A least ordinary unit in a
whole merger component supplies this floor at every target of that
component. A minimum of a later forward suffix generally does not.

### Exact source pins

| Input | Frozen source | Scope used here |
|---|---|---|
| Full valuation-clock ordinary counting, E14 | PR180, `bfba8feaefb3d0910456cdd92d2afcf9e8785b4d`, `research/lean-wide-pass-20261122/ENERGY_SYNTHESIS.md` | Its explicit finite-resolution inequality; no unknown clock cutoff |
| Previous finite-floor telescope | PR185, `7889fc680f5ee22237732eccc172b1699ef565da`, `research/profound-closure-20261122/POLYLOGARITHMIC_INVERSE_HORIZONS.md` and `FINITE_SPIKES_FORCE_SMALL_ANCESTORS.md` | The predecessor-floor idea and exact ordinary ancestor interpretation are credited there |
| Canonical finite comparison, E2 | Same PR180 head and file | The optional extension `V_k <= kappa D_(k+1)`, with its original analytic qualifications |
| First-contact expansion | PR176, `c83a8459066d8223aefe7fc5f6b75faeea557345`, `research/lean-global-resolvent-20261121/overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md` | Section 6 only; its stopped canonical law |
| Marginal mixing | Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Prop. 1.14, (1.23), (1.26)--(1.27), [corrected author version v7](https://arxiv.org/html/1909.03562v7) | Only the superpolynomial decay of the exact errors in Section 4 |

No joint clock/offset mixing, predecessor-population lower bound, or
ordinary almost-everywhere substitution is used in the finite theorem or
its finite obstacle extension below. The optional sharper comparison using
`kappa`, and the infinite canonical contact corollary, retain their
separately identified source hypotheses.

## 2. Exact finite rational transfer matrices

Suppose the values of \(D_r\) are known on \(\mathbb Z/3^r\mathbb Z\).
Put \(N_r=2\cdot3^r\). Since
\(2^{N_r}\equiv1\pmod{3^{r+1}}\), increasing a legal exponent by
\(N_r\) preserves both its legality and its parent residue modulo
\(3^r\). Summing the full geometric exponent tail gives

\[
\boxed{
D_{r+1}(q)=\frac3{2^{N_r}-1}
\sum_{\substack{1\le e\le N_r\\2^eq\equiv1\pmod3}}
2^{N_r-e}
D_r\!\left(\frac{2^eq-1}{3}\bmod3^r\right).
}
\tag{J4}
\]

This is an exact finite rational matrix, not an exponent truncation.
The representative in the parent residue is computed modulo
\(3^{r+1}\) before dividing by three. If a common denominator for
\(D_r\) is \(A_r\), one common denominator for \(D_{r+1}\) is

\[
A_{r+1}=A_r(2^{N_r}-1),\qquad A_0=1.
\]

Starting at \(D_0=1\), formula (J4) therefore computes every finite
density using integers only. The elementary periodicity used here follows,
for example, from Euler's theorem for the modulus \(3^{r+1}\); no
Collatz convergence premise is involved.

Define the exactly computable error

\[
\epsilon_m=
\frac1{3^{2m}}\sum_{a\bmod3^{2m}}
\left|D_{2m}(a)-D_m(a\bmod3^m)\right|,
\qquad m\ge1.
\tag{J5}
\]

Both arrays in (J5) have total normalized mass one. This is finite
arithmetic: for each fixed exponent \(e\), the legal target residues
modulo \(3^{r+1}\) correspond bijectively to parent residues modulo
\(3^r\). Averaging its branch multiplies the old mean by
\(2^{-e}\); summing \(e\ge1\) preserves the mean. Starting from
\(D_0=1\) proves the assertion. Consequently
\(0\le\epsilon_m\le2\). This definition supplies an actual rational
number for each \(m\), without first choosing an asymptotic mixing
exponent or estimating its constant.

## 3. The explicit finite-horizon bound

### Theorem J1

Assume (J3), let \(m\ge1\), and suppose \(9^m\le b\). Then

\[
\boxed{
\max_{0\le s\le K}\frac{D_s(q)}q
\le\frac{4^m}{b}
 +\frac{K(5K+4)}m\epsilon_m.
}
\tag{J6}
\]

All constants in this inequality are displayed. The theorem holds for
every finite choice of parameters, whether or not \(\epsilon_m\) is
small enough to make the bound useful.

**Proof.** Retain a family of ordinary inverse words of depth \(d\),
whose coefficients are at most \(\Omega\). The source-pinned full-clock
estimate E14, for a function \(H\) periodic modulo \(3^t\), is

\[
|P^d_{\mathcal F}H(q)|\le
\left[q(L-d+1)+2\cdot3^t\Omega
       +3^t9^d(2/3)^L\right]\|H\|_{1,3^t}.
\]

Choose the integer cutoff \(L=6d+3t\). Its last coefficient is exactly

\[
3^t9^d(2/3)^{6d+3t}
=(64/81)^d(8/9)^t\le1\le q.
\]

Consequently

\[
|P^d_{\mathcal F}H(q)|\le
\left[q(5d+3t+2)+2\cdot3^t\Omega\right]\|H\|_{1,3^t}.
\tag{J7}
\]

For \(s>2m\), take \(d=s-2m\), \(t=2m\), and
\(H=D_{2m}-D_m\). This function vanishes on nonunits. Every
contributing prefix source is therefore a unit predecessor within depth
\(d\le K\). The positive ordinary affine identity and (J3) give
\(\Omega\le q/b\). The exact semigroup identity now yields

\[
\begin{aligned}
\frac{|D_s(q)-D_{s-m}(q)|}{q}
&\le(5s-4m+2+2\cdot9^m/b)\epsilon_m\\
&\le(5s+4)\epsilon_m.
\end{aligned}
\tag{J8}
\]

For \(s\le2m\), (J2) gives \(D_s(q)/q\le4^m/b\).
Subtract \(m\) repeatedly until reaching this initial range. Equivalently,
apply the following finite induction with
\(f(s)=D_s(q)/q\):

\[
f(s)\le f(s-m)+\epsilon_m(5s+4)
\quad\Longrightarrow\quad
mf(s)\le m(4^m/b)+\epsilon_m s(5s+4).
\]

The induction slack is precisely \(5\epsilon_m m(s-m)\ge0\).
This proves (J6). Every predecessor-floor use has depth at most \(K\).
\(\square\)

The cutoff identity, a more general affine-error induction, and the
quartic calibration below are checked by Lean in
[FiniteSpikeClosure.lean](lean/FiniteSpikeClosure.lean). The full ordinary
counting theorem E14 and the inverse-operator interpretation remain written
inputs, rather than hidden formal axioms.

## 4. One computable horizon exceeding every fixed polylogarithm

Set

\[
E_m=\epsilon_m+9^{-m}>0,
\qquad
H_m=\max\{H\in\mathbb N:H^4 E_m\le1\}.
\tag{J9}
\]

The positive regularizer makes this definition independent of a
nonvanishing theorem for \(\epsilon_m\): it handles a zero error
without division by zero and makes the maximization finite. The maximum is computed by exact
integer comparisons and binary search. Small \(m\) may give \(H_m=0\);
the next statement applies when \(H_m\ge1\).

### Corollary J2

If (J3) holds through \(K\le H_m\), \(9^m\le b\), and
\(H_m\ge1\), then

\[
\boxed{
\max_{0\le s\le K}\frac{D_s(q)}q
\le\frac{4^m}{b}+\frac9{mH_m^2}
\le(4/9)^m+\frac9{mH_m^2}.
}
\tag{J10}
\]

Indeed \(H_m^4\epsilon_m\le1\) and
\(H_m(5H_m+4)\le9H_m^2\), and \(K(5K+4)\le H_m(5H_m+4)\), so (J6) gives (J10).

Tao's marginal mixing theorem implies, for **every fixed** \(A>0\),
\(\epsilon_m=O_A(m^{-A})\). Thus the same is true of \(E_m\).
As \(m\to\infty\), for every fixed \(B>0\),

\[
\boxed{H_m/m^B\longrightarrow\infty.}
\tag{J11}
\]

To justify the quantifiers, choose a fixed \(A>4B\). The definition
gives \(H_m=\lfloor E_m^{-1/4}\rfloor\); hence
\(H_m\ge\tfrac12C_A^{-1/4}m^{A/4}\) for sufficiently large \(m\).
The function \(H_m\) was defined by the exact matrices *before* this
argument. No unknown \(C_A\) has been silently set to one, and no
mixing exponent has been allowed to depend on the current target.
The quantifier passage is also checked in Lean: one maximally calibrated
horizon eventually exceeds every fixed polynomial by every fixed factor,
under an explicit rapid-decay premise for its one error sequence.

In particular the right-hand side of (J10) decays faster than every fixed
inverse power of \(m\). Taking \(m=\lfloor\log_9 b\rfloor\)
provides one computable superpolylogarithmic horizon in \(b\), with
superpolylogarithmic smallness of the normalized densities. Monotonicity of
\(H_m\) in \(m\) is not asserted or needed.

### Removing the regularizer using an ordinary cylinder

The companion [CYLINDER_BUDGET.md](CYLINDER_BUDGET.md) proves the intrinsic
lower bound

\[
\epsilon_m\ge2\bigl(4^{-m}-(2/9)^m\bigr)
\ge\frac29\,4^{-m}>0.
\]

Thus one can use the larger, still exactly computable horizon

\[
H_m^*=\max\{H\in\mathbb N:H^4\epsilon_m\le1\},
\qquad
H_m\le H_m^*\le(9/2)^{1/4}2^{m/2}.
\]

All finite calibrated estimates below also hold with \(H_m^*\).
Its intrinsic ceiling pays the longer-horizon error:
\(H_m^*(4/9)^m\le(9/2)^{1/4}(4\sqrt2/9)^m\), which
still decays exponentially. The same marginal mixing theorem makes
this one intrinsic horizon superpolynomial in \(m\).
The exact certificate records both versions and checks the displayed
ordinary-cylinder floor at its three finite block sizes.


## 5. Exact ordinary ancestor certificates and the canonical extension

Let \(b\) now be an integer. If \(q\ge b\), \(s\le H_m\),
\(9^m\le b\), \(H_m\ge1\), and

\[
\frac{D_s(q)}q>
\frac{4^m}{b}+\frac9{mH_m^2},
\tag{J12}
\]

then there are a positive odd unit \(n<b\) and
\(1\le j\le s\) with \(U^j(n)=q\).
Otherwise the finite predecessor floor would hold, contradicting
Corollary J2 with \(K=s\). The strict lower bound on \(j\) follows
from \(q\ge b>n\). This is a genuine positive ordinary ancestor
conclusion, and its finite-floor logic is formalized.

For any specified finite parameters, (J4), (J5), (J9), and (J12) involve
only rational arithmetic. Obtaining the matrix can be expensive: its
length is \(3^{2m}\). The statement is an exact certificate interface,
not a claim of a fast algorithm or a completed enormous enumeration.

### A finite obstacle bound without stationary normalization

For the obstacle iterates with \(0\le g\le1\),
\(V_0=g\), \(V_{k+1}=\max(g,PV_k)\), positivity gives

\[
\boxed{V_k\le\sum_{j=0}^k D_j.}
\tag{J13}
\]

Indeed \(g\le1=D_0\). If the claim holds at depth \(k\), then
\(PV_k\le\sum_{j=1}^{k+1}D_j\), and
\(\max(g,PV_k)\le g+PV_k\le\sum_{j=0}^{k+1}D_j\).
All functions in these finite sums are nonnegative. This argument uses
no stationary-density normalization, no population bound, and no global
finite majorant. Its form for an operator that is monotone and finite-sum additive on
an explicit function domain is checked in Lean. For the ordinary operator,
take the domain of bounded real functions: its row sum is at most two,
so every finite \(D_j\), \(V_j\), and finite sum belongs to that
domain. No additive operator on all unbounded real functions is assumed.

Combining (J13) with the calibrated bound, if the finite floor holds
through \(k\), \(9^m\le b\), \(H_m\ge1\), and
\(k+1\le H_m\),

\[
\boxed{
\frac{V_k(q)}q\le H_m\frac{4^m}{b}+\frac9{mH_m}.
}
\tag{J14}
\]

This right-hand side still decays faster than every inverse power of
\(m\), since \(H_m\le9^{m/4}\) by the regularizer and
\(H_m(4/9)^m\le(4/(3\sqrt3))^m\). For \(q\ge b\), a violation of (J14) therefore
forces a positive odd unit ancestor \(n<b\) at depth \(1\le j\le k\).
The finite floor is needed only through that actual \(k\).

### Optional sharper source-qualified comparison

Retaining the original source comparison \(V_k\le\kappa D_{k+1}\)
gives the smaller numerical upper bound

\[
\frac{V_k(q)}q\le
\kappa\left(\frac{4^m}{b}+\frac9{mH_m^2}\right).
\tag{J15}
\]

Violating (J15) likewise forces an actual unit ancestor below \(b\),
at depth at most \(k+1\). The factor \(\kappa\) and its analytic
existence are not needed for either the exact rational certificate for
\(D_s\) or the finite obstacle bound (J14).

## 6. Contact delay on the same calibrated horizon

This corollary uses PR176's stopped canonical contact representation.
For contact threshold \(1+\delta\), let \(p_L(q)\) denote the
probability of contact before depth \(L\) in that exact stopped law.
Its finite expansion gives

\[
p_L(q)\le\frac{1+\delta}{V(q)}\sum_{j<L}D_j(q).
\]

If \(V(q)\ge\eta q/\log(q+2)\), applying (J10) gives

\[
\boxed{
p_{H_m}(q)\le
\frac{(1+\delta)\log(q+2)}\eta
\left[H_m\frac{4^m}{b}+\frac9{mH_m}\right].
}
\tag{J16}
\]

The regularizer in (J9) implies \(H_m\le9^{m/4}\). Under
\(b\ge9^m\), the first term in brackets is at most
\((4/(3\sqrt3))^m\), which decays exponentially. If
\(\log(q+2)=O(m^A)\) for any fixed \(A\), (J11) shows that
the entire bound decays faster than every inverse power of \(m\).

In particular this applies to the source-relative range of marked
entrances supplied by PR176's polylogarithmic forward clock, starting from
a least component unit \(b\). It is a consequence **conditional on the
displayed critical spike**. It proves long contact delay if such a spike
exists; it does not supply the needed lower contact probability or assert
that such spikes exist at those entrances.

## 7. Why the current combination still does not close the limit

The new finite statement is (J10), with \(K=H_m\) at the explicit
horizon (J9). Replacing \(\max_{s\le H_m}\) by \(\sup_{s\ge0}\) remains
unsupported. The theorem does not give a bound on the first finite
witness of \(V(q)=\sup_kV_k(q)\).

The useful component-minimum bridge is exact: a sufficiently small
ancestor below the least unit of a whole component is impossible. But a
forward suffix minimum cannot be substituted for that least unit. Also,
propagating the obstacle value one from a least source \(b\) gives a
normalized value of order \(1/b\), which need not reach the critical
scale \(1/\log q\) at its early marked entrance. No argument here
forces that critical finite spike.

Allowing the actual return depth to grow while the same component floor
stays fixed is therefore still the first unsupported step. The exact
error certificate quantifies a longer finite part of that problem; it
does not exchange those limits or erase the original small ancestor.

## 8. Execution evidence and reproduction

The Lean module contains eight public theorems: finite geometric blocks,
the complete-clock tail normalization, a finite affine-error budget,
quartic calibration, its uniform finite-horizon consumer, domination of
all fixed polynomial horizons, the finite obstacle-sum comparison, and
ordinary finite-floor extraction.
Its analytic premises remain explicit.

The integer-only generator and certificate are:

- [finite_density_certificate.py](finite_density_certificate.py)
- [finite-density-certificate.json](finite-density-certificate.json)

The committed certificate uses only \(m=1,2,3\), hence density levels
through six. It checks exact normalization, the bound \(D_r\le2^r\),
364 ternary coarsening cells, and 120 independently evaluated literal
positive-odd inverse rows with their full geometric tail. All three
regularized horizons and all three intrinsic horizons are one. The
certificate also checks each exact rare-cylinder discrepancy floor and
its intrinsic quartic ceiling. These checks verify finite arithmetic and
normalization; they are not numerical evidence for an infinite estimate.

```sh
python3 research/lean-joint-20261122/finite_density_certificate.py \
  --max-block 3 \
  --check research/lean-joint-20261122/finite-density-certificate.json
```

The generalized affine-error induction follows the finite induction pattern
of PR185's `FiniteBlockTelescope.lean`, with the affine coefficients and
the finite horizon made explicit. The new calibrated error, rational
matrix construction, cutoff normalization, and source-relative horizon
are stated separately from that credited predecessor.
