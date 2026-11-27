# Two-place rigidity for the weighted odd-clock series

**PROPOSED.** For every fixed positive odd rational source with odd denominator, eventual periodicity of the odd orbit is equivalent to D-finiteness of its weighted cumulative-clock series. It is also equivalent to that series satisfying a Mahler equation in some integer base. On least-unit class representatives the same two-place argument excludes a Mahler equation for the weighted *signed* defects, even if infinitely many replacements occur. A bounded-discrepancy result below isolates the simpler, unweighted observable on which the obstruction acts. The missing implication for general positive integers is stated in §7.

**Prior repository credit.** PR195's GS1 already established the ordinary-source rationality/D-finiteness equivalence for the unweighted series with coefficients $2^{A_j}$; substitution $z\mapsto z/2$ preserves those two properties. The present proof extends the domain to positive odd rationals, proves the all-base Mahler criterion in this physical normalization, and treats the signed defects of actual least representatives. The subsequent [adelic synthesis](ADELIC_MAHLER.md) uses PR195's newer capacity argument to cover every nonzero rational normalization. [PR195 GS1, pinned source](https://github.com/GettysburgResearch/collatz/blob/a24ef018147a1e16bf314d14085e2d0d6c620d32/research/astra-global-closure-20261124/analytic/README.md)

## 1. A singularity visible at two absolute values

Write $K=\overline{\mathbb Q}$. For base $k\ge2$, a $k$-Mahler series $H\in K[[z]]$ is one for which the $K(z)$-span of $H(z^{k^j})$ for $j\ge0$ is finite dimensional. Equivalently there is a relation $\sum_{j=0}^d p_j(z)H(z^{k^j})=0$ with polynomial coefficients and $p_0p_d\ne0$. The *Mahler denominator* is the generator, normalized to have lowest nonzero coefficient one, of the ideal of admissible leading polynomials $p_0$ (including zero, with arbitrary finite order). This generator is itself admissible. We use Adamczewski–Bell–Smertnig, Definition 3.9 and Proposition 6.4. If its nonzero root $\lambda$ satisfies $|\lambda|_v<1$, the $v$-adic radius of $H$ is strictly less than one. The algebraic coefficient and root hypotheses apply throughout. [Primary paper](https://adamczewski.perso.math.cnrs.fr/HeightMahler.pdf)

**Two-place lemma.** Suppose $H\in\mathbb Z[[z]]$ has ordinary real radius $r\in\mathbb Q\cap(0,1)$, with $|r|_\ell<1$ for a finite prime $\ell$, and $H(t)\to+\infty$ as $t\uparrow r$. Then $H$ is not $k$-Mahler for any $k\ge2$.

Indeed, for every admissible leading polynomial the higher iterates in its equation are analytic near $r$, since $r^{k^j}<r$ for $j\ge1$. Hence $p_0(r)=0$. In particular the actual denominator vanishes at $r$. Proposition 6.4 forces the $\ell$-adic radius below one, whereas integer coefficients give radius at least one. No assumption about the vanishing of a particular nonminimal operator suffices in its place. Mahler series in a fixed base are closed under sums and rational-function multiples when the resulting formal expression is a power series. This follows by putting the finitely many spanning iterates for each summand together, with rational scalar multipliers. Rational functions themselves span a space of dimension at most one.

## 2. An equivalence for each ordinary source

Take $q_0=x_0/d>0$ with $x_0,d$ odd positive integers. Apply $q_{j+1}=(3q_j+1)/2^{a_j}$, $a_j=v_2(3q_j+1)$. Then $x_j=dq_j$ remains an odd positive integer, even if fractions reduce along the orbit. Put $A_0=0$, $A_j=\sum_{t<j}a_t$, $f_j=2^{A_j-j}$ and $g_j=f_jx_j$. Define $F(z)=\sum_{j\ge0}f_jz^j$ and $G(z)=\sum_{j\ge0}g_jz^j$. The scaling makes both series integral while preserving a fixed singularity:

$$2g_{j+1}=3g_j+df_j,\qquad (2-3z)G(z)=2x_0+dzF(z).\tag{1}$$

**Theorem.** For this source the following are equivalent.

1. The odd orbit is eventually periodic.
2. $F$ is rational over $K(z)$.
3. $F$ is D-finite over $K(z)$, meaning it satisfies a nonzero homogeneous linear differential equation over $K(z)$.
4. $F$ is $k$-Mahler for some $k\ge2$.

If the orbit repeats, the clocks are eventually periodic with period $p$. Along each of the $p$ progressions on the tail, $f_{j+p}/f_j$ is the same fixed power of two. Summing the finitely many geometric progressions gives rationality, hence both remaining properties (in every base for the Mahler property). Conversely a D-finite series with every coefficient in the rank-one group $\langle2\rangle$ is rational by Bell–Smertnig, Theorem 1.3, over the characteristic-zero field $K$. [Primary paper, Theorems 1.2 and 1.3](https://doi.org/10.4153/S0008414X22000517)

It remains to exclude a Mahler equation in the nonperiodic case. Determinism makes the $x_j$ pairwise distinct, so $x_j\to\infty$. For $r=2/3$, exact ordinary iteration gives

$$r^jg_j=x_0\prod_{t<j}\left(1+\frac{d}{3x_t}\right)\ge x_0.\tag{2}$$

The logarithm of the product is $o(j)$ by Cesàro averaging, since $d/(3x_j)\to0$. Thus $G$ has ordinary radius precisely $r$ and $G(t)\ge x_0/(1-t/r)$ for $0<t<r$. Here $|r|_2=1/2$. The two-place lemma excludes every Mahler equation for $G$. Equation (1) gives the same exclusion for $F$. This proof uses a single fixed source and its full denominator. It requires neither a convergence theorem for the sum of its reciprocals nor a complexity hypothesis on its parity word.

## 3. Complete numerical denominator on the periodic branch

Start at the beginning of a pure period of $p$ odd steps with cumulative clock $A=A_p$. Then

$$F(z)=\frac{\sum_{j=0}^{p-1}2^{A_j-j}z^j}{1-2^{A-p}z^p},\qquad C=\sum_{j=0}^{p-1}3^{p-1-j}2^{A_j},\quad D=2^A-3^p.$$

As a rational function, $F(2/3)=-3C/D$. Here $D\ne0$. The exact rational phase is $q=C/D$ by the full affine cycle identity $2^Aq=3^pq+C$. In particular the complete reduced denominator is $|D|/\gcd(C,|D|)$. A legal positive periodic phase is ordinary exactly when $D\mid C$, and positivity imposes $D>0$. Rational evaluation here means the value of the displayed rational function, including when the real Taylor series does not converge there. This calculation keeps the numerical divisor that a primitive-root or one-prime test could miss. Mahler rationality alone imposes no further condition on that divisor. For example the legal word $(1,2)$ has $D=-1$, and $(1,3)$ has $D=7,C=5$, giving the positive rational phase $5/7$; the one-letter word $(2)$ gives the positive integer phase 1.

## 4. Least-unit representatives including every replacement

Assume a hypothetical positive nonperiodic ordinary orbit and take a sufficiently late tail of its least ternary-unit synchronous-class representatives as in the [forward-section theorem, §§3–4](../../astra-global-synthesis-20261124/section/proof.md), SHA-256 `cbe95e8adf39ccf90253573005350260ee6ea0d67cb10c206108cbb624c59a02`. Use its exact corrected heights $M_{j+1}=3M_j/2^{a_j}$, $1\le a_j\le4$, $n_j/M_j\to1$. The [deficit-series lemma](../../astra-global-synthesis-20261124/arithmetic/optimality.md), §1, gives $1<M_j-n_j\le B_j=(1/3)\sum_{h\ge0} M_j/M_{j+h}$. The section also gives the minimum inverse-clock inequality for all finite windows. The following restriction already follows from the stated height and integrality estimates, so it applies to the actual optimizing representatives without assuming that their edges are literal.

Set $A_j=\sum_{t<j}a_t$, $f_j=2^{A_j-j}$, $g_j=f_jn_j$ and $\gamma_j=2^{a_j}n_{j+1}-3n_j\in\mathbb Z$. Define $W(z)=\sum f_j\gamma_jz^j$. Then $(2-3z)G=2n_0+zW$, and $(2/3)^jg_j=M_0n_j/M_j\to M_0>0$. Hence $G$ has radius $2/3$ and blows up radially there. The two-place lemma shows that **$W$ admits no Mahler equation in any base**, with no sign, size, or sparsity assumption on the defects $\gamma_j$. If there is a fixed bound on the number of signed $S$-unit summands needed for each $\gamma_j$, for a common finite set of primes $S$, then $W$ is also **not D-finite**. Indeed multiplication by $f_j$ leaves a bounded number of summands in the group generated by $-1$, $2$ and $S$. Bell–Smertnig Theorem 1.2 would make a D-finite $W$ rational. This includes any finite-valued defect sequence. It does not assume all defects equal the ordinary carry 1.

### Bounded discrepancy and unweighted block defects

Suppose for some positive integers $p,s$ that the corrected block clocks have bounded discrepancy $D_j=A_{pj}-sj$. This includes every eventually periodic clock after a shift, and allows the order and total of the clocks inside consecutive blocks to vary. Since $M_{pj}=M_0(3^p/2^s)^j2^{-D_j}\to\infty$, one has $P=3^p>Q=2^s$. Choose an integer $L\ge0$ such that $D_j+L\ge0$. Define the positive integers

$$h_j=2^{D_j+L}n_{pj},\qquad c_j=Qh_{j+1}-Ph_j.$$

The sequence $c_j$ is bounded. To see this, choose $K$ such that $|D_j|\le K$. Because $a_i\le4$, for $m\ge0$ and $0\le t<p$ we have $M_{pj}/M_{p(j+m)+t}\le 2^{2K}(Q/P)^m(16/3)^t$. This bounds $B_{pj}$ independently of $j$. Consequently $0<2^{D_j+L}(M_{pj}-n_{pj})$ is bounded, and $2^{D_j+L}M_{pj}=2^LM_0(P/Q)^j$ has zero defect $Qh_{j+1}-Ph_j$ when substituted for $h_j$. This proves boundedness, hence the integer alphabet of $c_j$ is finite.

Let $H=\sum h_jz^j$ and $C_*=\sum c_jz^j$. The exact relation is $(Q-Pz)H=Qh_0+zC_*$. Since $(Q/P)^jh_j\to2^LM_0>0$, $H$ blows up at its radius $Q/P$, with $|Q/P|_2=2^{-s}<1$. Thus $C_*$ is neither $k$-Mahler for any $k$ nor D-finite (use its finite alphabet and Theorem 1.3). In particular $c_j$ is not automatic in any base. For completeness, a finite-valued $k$-automatic sequence has finite $k$-kernel. A series for each kernel member decomposes into a polynomial combination of its $k$ residue-subseries evaluated at $z^k$. The kernel generates a finite-dimensional space of sequences, hence the sequence is $k$-regular. Becker, Theorem 1, gives the $k$-Mahler conclusion. [Primary paper](https://doi.org/10.1006/jnth.1994.1093)

If the corrected clock repeats a fixed word of length $p$ with sum $s$, then $D_j=0$ and one may take $L=0$. Thus the ordinary, unweighted block resets $2^sn_{p(j+1)}-3^pn_{pj}$ themselves cannot be automatic or D-finite, for every such word. No spacing of its valuations and no prior restriction on the reset mechanism are required.

More generally, under the same bounded-discrepancy hypothesis the clocks $a_i$ and their literal discrepancies $\gamma_i$ cannot both be $k$-automatic in the same base. To see this, suppose both are automatic. Then $E_i=pA_i-si$ is bounded, since $D_j$ is bounded and there are at most $p-1$ residual clocks, each at most four. It is also $k$-regular. Indeed for each member $v$ of the finite kernel of $a$ add its prefix sum $V(n)=\sum_{i<n}v(i)$ to the generating family. Writing $v_d(n)=v(kn+d)$, each $V(kn+r)$ is $\sum_{d<k} V_d(n)+\sum_{d<r} v_d(n)$, so the resulting finite span is stable under decimation. The sequence $i$ is also $k$-regular. Every member of the kernel of $E$ then lies in the same finite-dimensional sequence space and takes values in a common finite set. Evaluations at finitely many indices distinguish elements of a finite-dimensional sequence space, so the kernel of $E$ is finite and $E$ is automatic. Sampling an automatic sequence at $pj+t$ is automatic: each kernel member of the sample is the evaluation of a kernel member of the original at $pj+u$, with $u$ in a fixed finite range after Euclidean division. Hence $D_j=E_{pj}/p$ and each sampled $a_{pj+t},\gamma_{pj+t}$ are automatic. Iterating $2^{a_i}n_{i+1}=3n_i+\gamma_i$ over one block gives

$$c_j=2^{D_j+L}\sum_{t=0}^{p-1}3^{p-1-t}2^{A_{pj+t}-A_{pj}}\gamma_{pj+t}.$$

This is a fixed function of finitely many finite-alphabet automatic sequences, so its kernel is finite. This contradicts the exclusion of automatic $c_j$ above. In particular a periodic corrected clock permits no automatic sequence of raw signed discrepancies in any base. The argument with bounded discrepancy also covers nonperiodic corrected clocks, including blocks with different total clocks.

## 5. Explicit obstruction to a uniform Mahler-certificate search

Fix any proposed base $k\ge2$, order bound $d\ge1$ and coefficient-degree bound $h\ge0$. There are explicit positive integers which reach 1 but whose $F$ admits **no** homogeneous $k$-Mahler equation with these bounds and nonzero zeroth coefficient. For $m\ge1$ put

$$b=3^m+1,\qquad y=(2^b-1)/3,\qquad q=2^m(y+1)/3^m-1.$$

The elementary congruence $2^{3^m}\equiv-1\pmod {3^{m+1}}$ follows inductively from $X^3+1=(X+1)(X^2-X+1)$ when $X\equiv-1\pmod3$. Thus $3^m\mid y+1$, since $y+1=2(2^{3^m}+1)/3$. The integers $q_j=2^{m-j}3^j(y+1)/3^m-1$ for $0\le j\le m$ are positive and odd (also $y+1$ is even). They obey $2q_{j+1}=3q_j+1$ and $q_m=y$. Next $3y+1=2^b$, so $q$ reaches 1 and then stays there. Its $F$ agrees with $K_0(z)=1/(1-z)$ through degree $m$, and their first difference is at $m+1$ with coefficients $2^{b-1}$ and 1.

Suppose $\sum_{j=0}^d p_j(z)F(z^{k^j})=0$ with $p_0\ne0$, $\deg p_j\le h$. Replacing $F$ by $K_0$ gives order of vanishing at least $m+1$. After multiplication by $\prod_{j=0}^d (1-z^{k^j})$ the resulting polynomial has degree at most $h+\sum_{j=0}^d k^j$. If $m\ge h+\sum k^j$, this polynomial vanishes, so the operator kills both $K_0$ and $F-K_0$. The zeroth term on $F-K_0$ has vanishing order at most $m+1+h$, and all other terms have order at least $k(m+1)>m+1+h$. This is impossible. The construction rules out uniformly bounded order *and* polynomial degree in any fixed base even on known convergent ordinary inputs. Source-dependent operators remain possible.

## 6. Testing a global source generating function

A potential route to the hypothesis of §2 is to encode *all* positive sources at once and then extract a single source. For the natural table of weights, this parent series fails the holonomicity test already after one odd step. Define

$$\Phi(t,z)=\sum_{n,j\ge0} f_j(2n+1)t^n z^j,$$

where the argument of $f_j$ now specifies the source. The coefficient of $z$ is $S(t)=\sum_{n\ge0} s(n)t^n$ with $s(n)=2^{v_2(3n+2)}$. Set $r(n)=2^{v_2(3n+1)}$ and $R(t)=\sum r(n)t^n$. Direct dyadic decimation gives

$$r(2n)=1,\quad r(2n+1)=2s(n),\quad s(2n)=2r(n),\quad s(2n+1)=1,$$

and therefore

$$S(t)=\frac{2}{1-t^4}+\frac{t}{1-t^2}+4t^2S(t^4).$$

This gives a $2$-Mahler equation: the even dilates $S(t^{4^j})$ lie in the rational span of $1,S(t)$ and the odd dilates $S(t^{2\cdot4^j})$ lie in that of $1,S(t^2)$.

**No scalar holonomic or independent-base closure.** The functions $s(n+h)$, for distinct nonnegative $h$, are linearly independent over $K(n)$, as sequences modulo eventual equality. Indeed suppose $\sum_{h\in H}p_h(n)s(n+h)=0$ eventually, with polynomial coefficients after clearing denominators. Fix $h_0$ and choose $e>v_2(3(h-h_0))$ for all other $h$. In the infinite positive residue class on which $v_2(3(n+h_0)+2)=e$, the other valuations have the fixed values $v_2(3(h-h_0))$. This class exists because 3 is invertible modulo $2^{e+1}$. It yields the polynomial identity

$$2^e p_{h_0}(X)+\sum_{h\ne h_0}2^{v_2(3(h-h_0))}p_h(X)=0.$$

Repeating for $e+1$ forces $p_{h_0}=0$. Hence $s$ has no nonzero polynomial-coefficient recurrence and $S$ is not D-finite. Indeed coefficient extraction from any nonzero polynomial-coefficient differential equation gives such a recurrence (terms $t^b(d/dt)^a$ with common $a-b$ have distinct degrees $a$ in the coefficient index). In particular $S$ is not rational. The Adamczewski–Bell theorem, in characteristic zero, then shows it cannot be Mahler in any integer base multiplicatively independent of 2, including 3. [Primary paper](https://doi.org/10.2422/2036-2145.201606_010)

It follows that $\Phi$ is not multivariate D-finite. Otherwise $(\Phi-1/(1-t))/z$ would be D-finite by rational-affine closure, and it would have a nonzero differential equation in $t$ alone whose coefficients are polynomials in $t,z$. Remove their common power of $z$ and specialize at $z=0$. The result is a nonzero differential equation for $S$, contradicting the preceding proof. Thus a multivariate holonomic table followed by source extraction cannot justify the missing step for this observable. The fixed-time obstruction allows every source in the construction to be an ordinary positive integer.

There is a second, mixed obstruction. Write $T(w,j)=f_j(2w-1)$ for $w\ge1$ and $(LT)(w,j)=T(2w,j+1)$. For all $m\ge0$,

$$ (L^mT)(w,1)=2^{v_2(3^{m+1}w-1)}. $$

The source $2^{m+1}w-1$ has $m$ initial gaps equal to one and then sits at $2\cdot3^mw-1$. Its next gap is $1+v_2(3^{m+1}w-1)$. The displayed rows are linearly independent over $K(w)$. To verify this, fix one $m$ in any proposed finite dependence and choose large exact valuation $e$ at the center $w=3^{-(m+1)}\in\mathbb Z_2$. Every other row has a fixed valuation there, determined by the nonzero difference of the two centers, and retains it throughout this residue class. Subtracting the polynomial identities for $e$ and $e+1$ repeats the preceding argument. Consequently no finite-dimensional $K(w)$-space containing $T$ is closed under this simultaneous source decimation and forward-time shift. This rules out that particular finite representation, without limiting a possibly different equation for a single fixed source.

The invariant of membership in the basin of 1 is a different table. The relations between its residue sections are a genuine mixed-radix functional equation. Berg and Meinardus's uniqueness formulation, and the related research note on automatic saturated component sets, describe these invariants. The one-step $S$ above neither establishes nor rules out automaticity of that basin. [Berg–Meinardus](https://doi.org/10.1007/BF03323136) · [Related primary research note](https://rstation.ai/problems/collatz/papers/64/v2)

## 7. The outstanding global implication

The theorem in §2 makes a source-specific Mahler or differential equation sufficient to exclude escape. It does not construct such an equation for an arbitrary positive integer. Having a finite alphabet for the individual least-unit clocks gives neither finite Mahler span for their weighted summatory clocks nor automaticity of the block resets. Every finite-window minimizing inequality still holds in the class application; an implication from this extremality to one of the analytic properties above is open. The full-denominator cycle problem in §3 remains independent. In particular no general convergence claim follows from the fact that all finite initial segments of $F$ are polynomials.

A related research note, *Automatic, primitive, and nonprimitive parity in rational Collatz dynamics*, studies automaticity of the **shortcut parity sequence**. Our criteria concern the positive integer weights at successive odd times and the signed defects of actual class representatives. An automaticity theorem for one of these observables cannot be applied to another without a transfer proof. [Related primary research note](https://rstation.ai/problems/collatz/papers/16)

`MahlerCore.lean` proves the single-step weighted affine identity with a signed carry, the algebraic cancellation of an exact block comparison, and the ordinary clock-one identity. The analytic lemma and quoted theorems are used in the written proof. `check.py` replays exact arithmetic on finite inputs.
