# Extension to primitive binary nonuniform substitutions (MPS-5)

2026-11-24. **PROPOSED written extension.** This strengthens MPS-1 from uniform substitutions to **every primitive binary substitution**, including nonuniform substitutions such as Fibonacci. Full Collatz remains OPEN. The existing finite Lean identities already allow arbitrary substitution image lengths; the analytic extension is written mathematics, not Lean verified.

Use the same two rational physical inverse affine maps with different fixed points and positive binary multiplier valuations, and the same non-eventually-periodic one-sided fixed word s of a substitution σ. Assume now only that σ(0),σ(1) are nonempty and that the 2-by-2 incidence matrix M (row a counts zeros and ones in σ(a)) is primitive. Then the unique physical completion is transcendental over Q. Together with MPS-1 this covers all uniform binary substitutions (even nonprimitive ones covered there) and all primitive binary substitutions of arbitrary image lengths.

## 1. Regularity for unequal image lengths, including a proper prefix

The substitution Mahler equation (3) of README.md holds unchanged:

    G_1(X,Y) = P_0/(1-X') + D/(1-X') G_1(X',Y'),
    D=(1-X')P_1-(1-Y')P_0,

where X',Y' are the prefix products of the full images σ(0),σ(1). The previous earliest differing finite-position proof needs repair if one image is a proper prefix of the other.

For any two different infinite binary words, their G_1 evaluations at the same x,y with positive 2-adic valuations differ. At their first differing symbol, the common prefix product is the unique lowest-valuation contribution to the difference; all later terms on both sides have strictly higher valuations. For a nonempty word u with multiplier x_u and prefix-one sum P_u, the evaluation for its periodic repetition is P_u/(1-x_u). Consequently D=0 if and only if the two infinite periodic words σ(0)^∞ and σ(1)^∞ are identical. If identical, every infinite concatenation of the two images is that same periodic word: each image length is a period of their common repetition, and the images are its initial segments. A nonperiodic fixed point cannot occur in this case. Thus D is nonzero at every physical iterate, also for unequal lengths. This uses exact 2-adic positivity, not a generic determinant hypothesis.

## 2. Matrix growth replaces the uniform clock

Let λ>1 be the Perron eigenvalue of M, μ the other eigenvalue, and w a positive right Perron eigenvector. Primitivity implies |μ|<λ and λ is simple. (Some power of M has positive integer entries, so λ>1.) Define the monomial iteration z_n=(x_n,y_n) by the incidence matrix. With v_n=(v2(x_n),v2(y_n))^T and v_0 strictly positive, Perron-Frobenius gives

    v_n = M^n v_0 = C λ^n w + O(|μ|^n),    C>0,

with the error identically zero after the first step when μ=0. In particular min(v_n) is bounded below by c λ^n for sufficiently large n, for some c>0.

The heights h(x_n),h(y_n) are O(λ^n), directly from the nonnegative exponents in M^n. If B_0=G_1(x_0,y_0) is algebraic, the nonzero coefficient in the Mahler equation gives B_n=G_1(x_n,y_n) in one fixed number field K and

    h(B_{n+1}) <= h(B_n)+O(λ^n),    h(B_n)=O(λ^n).

Thus, for a fixed integer auxiliary polynomial R of individual degree <=m in its variables,

    h(R(x_n,y_n,B_n)) <= C' m λ^n + O_R(1).

The same bound holds for a one-variable rational parameter of height O(λ^n) in place of x_n,y_n. The lower bound for nonzero η in K remains v2(η) log 2 <= [K:Q] h(η). The only new issue is nonvanishing of the auxiliary series along this nonuniform moving orbit.

## 3. Nonvanishing when the Perron weight ratio is irrational

By README Section 4, G_1(X,Y) is transcendental over Q(X,Y). Choose an integer auxiliary polynomial R with individual degrees <=m and vanishing all total-degree coefficients below d=floor(m^(3/2)) after substitution W=G_1. This is possible by the same linear dimension count. The resulting nonzero integral formal series F has total order >=d.

If w_0/w_1 is irrational, the weights w_0 i+w_1 j of distinct integer exponent pairs are distinct. A nonzero F has a unique term of least weight, since positive weights leave finitely many monomials below any fixed bound. Its valuation at (x_n,y_n) is asymptotic to C λ^n times that weight. Every other term of any fixed finite truncation has larger valuation for large n. The infinite tail is also larger: choose a sufficiently large total degree cutoff L so that (C/2) min(w_0,w_1)(L+1) exceeds the leading asymptotic weight C(w_0 i+w_1 j), and use min(v_n)>=(C/2)min(w)λ^n. Coefficients are integers. Therefore the least term dominates and F(x_n,y_n) != 0 eventually.

All terms have valuation at least d min(v_n)>=c d λ^n. The height bound and product formula contradict this for m large since d/m tends to infinity. This covers, for example, the genuine nonuniform Fibonacci substitution 0->01, 1->0, whose incidence matrix [[1,1],[1,0]] is primitive and whose Perron ratio is irrational. Its fixed word is aperiodic (its limiting letter frequencies are irrational, obtained from the normalized incidence matrix powers, whereas eventual periodicity gives rational frequencies).

## 4. Rational Perron weight: exact transverse monomial

If the Perron ratio is rational, normalize w=(p,q) with coprime positive integers p,q. Then λ is an integer: both λp and λq are integers, and Bézout applies. Also μ=trace(M)-λ is an integer. The row vector (-q,p) annihilates w and is a left eigenvector for μ. Consequently the exact rational transverse ratio is

    r_n=y_n^p / x_n^q = r_0^(μ^n).

When |μ|>=2 and r_0 != 1, the ratios are distinct positive rationals and h(r_n)=O(|μ|^n). Take the same two-variable auxiliary F as above. Let d0 be its least occupied weighted degree p i+q j. The first weighted homogeneous piece is a monomial times a nonzero polynomial P(r), because two exponent pairs of the same weight differ by an integer multiple of (-q,p). Its evaluation is nonzero for all large n since P has finitely many roots and r_n are distinct. By the rational height bound its valuation is at most

    C d0 λ^n + O_F(|μ|^n).

All terms of higher weighted degree have valuation at least (C-ε)(d0+1) λ^n for large n, by the componentwise asymptotic bound on v_n; take ε>0 so that (C-ε)(d0+1)>C d0. Thus the first homogeneous piece dominates. As before the total order >=d gives the incompatible lower valuation c d λ^n. This is a full moving-point check including the secondary eigenvalue.

The remaining cases (|μ|<=1 or r_0=1) have an infinite subsequence with constant ratio y_n^p/x_n^q. Fix one point (a,b) on that subsequence. Every point on it can be written

    x_n=a z_n^p,  y_n=b z_n^q,

with rational z_n: the ratios A=x_n/a,B=y_n/b satisfy B^p=A^q, and z_n=A^u B^v for integers u,v with up+vq=1. In particular h(z_n)=O(λ^n), v2(z_n)~C λ^n. We need the weighted specialization lemma below to ensure a nonzero univariate auxiliary series; mere nonalgebraicity on the diagonal would not suffice.

## 5. Weighted clock specialization is transcendental (MPS-6)

For ANY non-eventually-periodic binary word s, positive integer p,q, and nonzero rational a,b, the formal series

    H(z)=G_1(a z^p,b z^q)

is transcendental over Q(z).

Define N(j)=p n_0(j)+q n_1(j), W(j)=a^{n_0(j)}b^{n_1(j)}. Its coefficients u_t are s_j W(j) at t=N(j), and zero otherwise. Because p,q>=1, the boundary indices strictly increase, so coefficients are unambiguous.

Suppose H is algebraic. The same D-finite coefficient extraction as in README Section 4 produces a nonzero polynomial recurrence sum_{k=0}^r p_k(t)u_{t+k}=0. For each t let j(t) be the last boundary index with N(j(t))<=t. Divide by W(j(t)), never zero. Each normalized u_{t+k}/W(j(t)) belongs to a finite set (zero or products of boundedly many a,b), since a fixed clock interval crosses at most r+1 boundaries. Thus only finitely many normalized tuples occur. As before, for sufficiently large t the polynomial associated to any occurring tuple must vanish identically; selecting a nonzero coefficient vector gives a nonzero constant-coefficient recurrence for u. Let r be its largest nonzero index (r=0 forces a zero tail).

Now work at a symbol boundary N(j), storing the last r clock coefficients normalized by W(j). This is a finite state: each nonzero entry is a product of at most r inverse factors a^-1,b^-1, because at most r symbols have occurred in the preceding r clock positions. The constant recurrence determines u_{N(j)}/W(j)=s_j from that state, since the leading coefficient is nonzero. The following p-1 or q-1 clock coefficients are zero. Append this letter coefficient and those zeros, keep the most recent r entries, and divide all by a if s_j=0 or b if s_j=1. This gives exactly the next boundary state. Therefore the boundary state is a deterministic recursion on a finite set and s must be eventually periodic. Contradiction.

This also proves convergence of H near zero: coefficients have p-adic valuation bounded below by a negative constant times their clock index. No positivity of real coefficients, D-finite regularity at a specialization, or bounded weighted coefficients is assumed.

## 6. Finish the constant-ratio case and theorem

On the subsequence above B_n=H(z_n). Choose nonzero R(Z,W) of individual degrees <=m, killing the first (m+1)^2-1 coefficients of R(z,H(z)). By MPS-6 it is a nonzero convergent p-adic series. Leading-term dominance near zero gives v2(R(z_n,B_n))>=((m+1)^2-1) v2(z_n)+O_R(1) for all sufficiently large n on the subsequence. Its height is <=C' m λ^n+O_R(1), so the fixed-field product formula contradicts the quadratic auxiliary order as m grows.

This completes the primitive-binary extension. It uses no relation between real orbit growth and clock growth: λ here is the incidence-matrix growth, not the actual Collatz height exponent. In particular all nonperiodic binary primitive substitutive scripts over physical Collatz gap blocks are excluded from rational ordinary realization.

## 7. Remaining gap

This does not imply arbitrary actual Collatz schedules have substitution structure. The arbitrary-schedule scalar-phase problem in PR182, the all-reset cocycle of PR188 and the stationary critical collision deficit of PR189 remain open. In particular neither a finite rational phase nor a bounded empirical entropy forces a primitive substitution coding. The advance is a broad arithmetic exclusion theorem on exactly realized sources, not a universal convergence claim.

The multivariate method suggests a precise generalization: find enough independent auxiliary functions and prove nonvanishing along positive rational monomial orbits for larger substitution alphabets, without assuming matrix regularity or a generic orbit. The weighted specialization mechanism here handles every two-dimensional degeneration, but not arbitrary higher-dimensional subtori.

Proof status: written, proposed; Sections 1–2 use the same finite algebra identities as MahlerCore.lean. The latter is still pending compiler replay. Exact extra regularity and ratio controls are in primitive_controls.js and PRIMITIVE_CHECKS.md. No imported Collatz conjectural statement is used.
