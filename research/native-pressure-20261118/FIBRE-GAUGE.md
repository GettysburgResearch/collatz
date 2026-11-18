# A polylogarithmic Hausdorff gauge for each ordinary real fibre

Fix a positive odd unit t, let μ_t be its canonical real affine fibre
law, and write L=log(1/r). For each ε>0 the full inverse path measure
is exhausted by countably many measurable sets E_N on which the
pushforward restriction satisfies, for sufficiently small r,

    μ_(t,E_N)(I) ≤ C_(t,N,ε) r L^(11/2+ε)       whenever |I|=r.

Consequently μ_t is absolutely continuous with respect to Hausdorff
measure with gauge r(log(1/r))^(11/2+ε). This quantitative statement
is compatible with the fibre's singularity for ordinary Lebesgue
measure. Translating or reflecting the real coordinate preserves it.

[All-depth profile bound](PROFILE-BOUND.md) · [Iterated-logarithm upper
clock](ITERATED-LOG-BOUND.md) · [Bounded real tails near each
depth](BOUNDARY-CODING.md) · [Extreme valuations](REAL-TAILS.md).

Use the reflected variable W=t−B₀. Put J_i=3^i/2^(S_i). Exact affine
telescoping gives

    W=J_i(X_i−B_i),       P_t(prefix through i)=J_i h(X_i)/h(t).

Here X_i is a positive odd unit integer, B_i≥0 and h(t)>0. Fix
0<δ<ε. By the cited results almost surely, eventually in i,

    h(X_i)≤i^(5+δ),      a_i≤C log(i+2),
    |log J_i+d i|≤C √(i log log(i+16)),      d=log(4/3).

For each sufficiently large i there also exists an m in
[i,i+(log i)³] with B_m≤K for a fixed constant K. This last conclusion
comes from the disjoint logarithmic-length bounded-tail trials and
uniform far-tail truncation in the coding proof. These statements
also hold after a finite cycle prefix at a periodic root.

For a concrete increasing exhaustion require on E_N that
h(X_i)≤N(i+2)^(5+δ), a_i≤N log(i+2) and the clock error is
≤N √((i+1)log log(i+16)) for every i≥1, and require the bounded-tail
visit property for every i≥N. These measurable sets have full union.
In particular log J_N is bounded below by a finite deterministic
constant depending on N. Taking r sufficiently small therefore ensures
that the last index with J_i>r is at least N throughout E_N.

For 0<r<1 small on a fixed restriction let n be one plus the last
index i with J_i>r. It is finite since log J_i/i→−d. Thus J_(n−1)>r
and every J_i for i≥n is at most r. Since the last step has multiplier
3/2^(a_n), J_n≥r exp(−C_N log(n+2)). The clock bound at n, together
with these two inequalities, gives

    n=L/d+O_N(√(L log log(L+16))).

Indeed it first bounds n above and below by positive constant
multiples of L, after which substitution gives the stated error.
Pick any permissible m between n and n+(log n)³ with B_m≤K. It is
unnecessary for these choices to be prefix stopping times: the
probability bound below uses a union of covering prefix cylinders.
Every one of the additional multipliers is at least
exp(−C_N log(m+2)) by the individual exponent bound. Consequently

    m=L/d+O_N(√(L log log(L+16))),
    r exp(−C_N (log(L+2))^4) ≤ J_m ≤ r.

There are O_N(√(L log log(L+16))) integer choices for m. For each,
J_m=3^m 2^(−S_m) ranges on a log lattice with spacing log 2, so
the number of possible integer totals S_m is O_N(1+(log(L+2))^4).
Given m,S_m and W∈I, the real identity places the integer X_m in
I/J_m+[0,K]. There are at most r/J_m+K+1 integers in that interval,
regardless of its endpoints. Restriction to odd integers coprime to
three only decreases the count. At fixed m each candidate X_m yields
at most one prefix since forward iteration is deterministic, including
at a periodic root. Any cylinder containing a qualifying path has
h(X_m)≤N(m+2)^(5+δ), so its entire probability is at most
N J_m (m+2)^(5+δ)/h(t). For a given m,S_m the aggregate mass is at most
N(K+2)r (m+2)^(5+δ)/h(t), using J_m≤r.

Sum over m and S_m. The factor (log(L+2))^4 √(log log(L+16)) is
absorbed into L^(ε−δ), giving the stated bound. For a gauge-null
Borel set take interval covers of arbitrarily small total gauge;
the restricted measures vanish there, hence so does μ_t. The same
argument controls every set needing completion of the fibre measure.
