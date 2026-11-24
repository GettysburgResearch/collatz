# Source-weighted projection on a late physical clock

The incidence step in [forward re-exposure](FORWARD_SOURCE_REEXPOSURE.md) applies at an arbitrary deterministic physical clock $t$, including $2^t>N$. It requires upper bounds on the two **actual** scalar intercepts on the selected sources. The scalar early-clock consequence in the previous note is one way of supplying those bounds. The head passage estimates give another.

Use all notation of the forward note, including $\rho=3^{g_H-g_L}$, $F=2^t/3^{g_H}$ and $V=N3^{g_L}/2^t$, where $H,L$ as subscripts refer to slope order. Let $E\ge1$ bound the two scalar intercepts on a chosen subset of original sources. For each count vector, allow a grade-dependent event with ordinary count at most $\delta V$ on its incoming lower-source interval
$$
 I_p=[3^{g_L}N_0/2^t+c_L,\ 3^{g_L}(N_0+N)/2^t+c_L+E].
$$
Impose this only for offsets in $[c_H-\rho c_L-\rho E,c_H-\rho c_L+E]$. Then for **any** admissible count-vector menu $\mathcal G$,
$$
 \Pr(\text{selected source, }p\in\mathcal G,\ B_{p,D}(z))
 \le 3\sum_{p\in\mathcal G} E(E+1/F_p)\,\delta.                 \tag{1}
$$
The conclusion is a bound on the original mass, with no conditional normalizer. Indeed the offset count is at most $3\rho E$, per-exact-output original multiplicity is at most $1+EF_p$, and $\rho F_p V=N$. This proves (1) directly without any probability law at clock $t$. One can use a separate $\delta_p$ under the sum.

For a purely $k$-bit future test from the new state whose fair fraction is at most $\delta_0$ for every incoming profile, a covering by at most $(V+E)/2^k+2$ **complete periods** bounds the ordinary count by $\delta_0(V+E+2^{k+1})$. The dyadic congruence test is defined on every residue, regardless of whether the corresponding pair on an extended period is positive. If the underlying event itself is only defined on positive pairs, dominate it there by this periodic test. Thus $\delta\le4\delta_0$ when $E\le V$ and $2^k\le V$. Similarly for an initial $t$-clock scalar word test with $2^t\le N$, cover by full periods including the partial final one to the right. Its original mass is at most twice the complete-grid probability. These coverings sharpen the endpoint additive errors in the previous note.

For a head row with $N=R/81$ parent parameters and $N_0=7R/81$, the original offsets are $0,r$, $0\le r<81$. Conditional on its count vector, the exact lower equation gives
$$
   z=V\left(n/N+ b_L/(3^{a_L}N)\right)+e_L
     \in [7V, (8+1/N)V+E].
$$
The high equation similarly gives $1/F=3^{g_H}/2^t\le Y_H/(7N)$. In particular if $z\ge M/2$ with $M\gg E$, then $V\gg M$, and if $Y_H\le R d^C$ then $1/F\ll d^C$, with $d=\log_2R$. All constants are uniform in the assigned upper/lower labels. The true scalar sliding tests in [HIGH_GRADE_SHADOW.md](HIGH_GRADE_SHADOW.md) and [HEAD_INCIDENCE.md](HEAD_INCIDENCE.md) supply a common original-source exception $O_A(Rd^{-A})$ such that the two scalar intercepts up to the first of the two polylogarithmic entrances are $\le d^{C_A}$, and both endpoint heights are $\le R d^{C_A}$. The latter follows by partitioning a scalar prefix into full contracting sliding blocks and one $O_A(\log d)$ remainder; the relative odd-step corrections before the floor contribute at most $\exp(O(d/M))$. The scalar first entrances occur by $O_A(d)$ clocks outside the same type of exception. Take $M=d^D$ with $D$ above the fixed intercept exponent.

Consequently, summing (1) over each possible $t\le C_A d$ and its at most $(t+1)^2$ count vectors costs only $d^{O_A(1)}$ on original mass for any uniform one-profile word test whose length satisfies $2^k\ll M$ with sufficiently small absolute implicit constant. This applies jointly to original high-grade states even when the offset range has exponentially many integer members. For clocks after the smaller arm has lost its linear source scale, $V$ can be too small to support a fresh word of the prescribed length. The improvement removes an exponential-in-grade census cost while the two true scalar profiles are controlled. It does not give an unlimited fair continuation after either orbit has reached a fixed small cycle.
