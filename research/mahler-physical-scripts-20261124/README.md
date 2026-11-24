# Physical Collatz completion for binary uniform substitutions

2026-11-24. **PROPOSED written theorem; exact finite controls; Lean arithmetic source pending compiler replay. Full Collatz remains OPEN.** This packet attacks actual fixed-source rationality, not a change of source with the horizon. It replaces the repeat-position bound of PR187 by a Mahler auxiliary-polynomial argument for an entire class of arbitrary expanding or contracting two-letter return scripts.

## 1. Main theorem (MPS-1)

Let W0,W1 be two distinct nonempty finite words of positive accelerated odd Collatz gaps, of the same number of odd steps. More generally, any pair whose rational inverse affine maps have different fixed points is sufficient. Let s be a one-sided fixed point of a binary b-uniform substitution σ, b>=2, so σ(0) and σ(1) each have length b and s=σ(s). If s is not eventually periodic, the unique physical odd 2-adic completion of the concatenated gap script W_{s_0} W_{s_1} ... is **transcendental over Q**.

Consequently no positive or negative rational odd source can realize such an itinerary. An eventually periodic itinerary has a rational completion (not necessarily a positive integer). No rate of real growth, frequency assumption, bounded discrepancy, return-height assumption, or restriction to balanced substitutions is required. This does NOT cover arbitrary automatic words (larger alphabets or nontrivial codings), arbitrary two-letter schedules, or arbitrary Collatz orbits.

In particular, apply to PR182's L=(2,1), P=(1,4), with inverse maps

    f0(t)=(8t-7)/9,  f1(t)=(32t-5)/9.

Every non-eventually-periodic fixed point of every binary uniform substitution has a transcendental physical completion in this L/P language. This includes the genuinely expanding examples in Section 6. PR187's finite digit-weight scripts are credited; we are not claiming that all of those are binary uniform fixed points.

## 2. Exact physical reduction (no real/2-adic identification)

For any gap g>=1, inverse map I_g(t)=(2^g t-1)/3 sends odd 2-adic integers to odd 2-adic integers and has exact valuation g at its image. For word W write its inverse composition as f_W(t)=α_W t+β_W, α_W=2^{sum W}/3^{length W}, β_W in Z_2 odd, rational. Composition is in the physical order, with the rightmost inverse applied first. Thus f_W has |α_W|_2<1. The fixed point β_W/(1-α_W) is odd, rational, and realizes W repeatedly. Distinct words of the same odd length cannot have the same fixed point: the actual valuations at one source are unique.

Write x=α_W0, y=α_W1, a=β_W0, e=β_W1. For an infinite binary word s and formal variables X,Y let n_0(j),n_1(j) count the two letters strictly before j, and put

    G_i(X,Y)=sum_{j:s_j=i} X^{n_0(j)} Y^{n_1(j)}.

These lie in Z[[X,Y]], one monomial at most per degree for each series. On |X|_2,|Y|_2<1 they converge. Finite telescoping, followed by the vanishing product, gives

    (1-X)G_0+(1-Y)G_1=1.                                  (1)

The unique odd 2-adic completion is

    q = a G_0(x,y)+e G_1(x,y)
      = a/(1-x) + [e-a(1-y)/(1-x)] G_1(x,y).               (2)

Indeed the exact finite inverse prefix equals its constant plus the prefix multiplier times any supplied odd terminal value; the multiplier goes to zero 2-adically. This also proves uniqueness and ordinary attachment: any actual rational physical source (odd denominator) equals q in Q_2. The coefficient of G_1 in (2) is nonzero by the distinct-fixed-point hypothesis. Algebraicity of q is therefore equivalent to algebraicity of G_1(x,y). No assertion equates the Q_2 limit to a real limit.

## 3. The two-variable Mahler equation and regularity at every physical iterate (MPS-2)

Let c_a be the number of ones in σ(a). Let P_a(X,Y) be the sum of the prefix products at positions containing one in the finite word σ(a). Set

    X'=X^{b-c_0}Y^{c_0},  Y'=X^{b-c_1}Y^{c_1},
    λ=c_1-c_0.

Grouping the actual fixed word by consecutive substitution blocks, and eliminating G_0 using (1), proves the exact identity

    G_1(X,Y) = P_0/(1-X') + D(X,Y)/(1-X') G_1(X',Y'),      (3)
    D=(1-X')P_1-(1-Y')P_0.

This is a formal series identity and an analytic identity on the open 2-adic bidisk. It retains complete physical block weights, not just the number of P letters.

**Regularity.** Since s is not eventually periodic, σ(0) != σ(1). Let r be their first differing position. The common prefix has 2-adic product valuation t. In P_1-P_0 the contribution at r is ± that product, while every later contribution has valuation strictly above t; earlier contributions cancel. Both X' and Y' have valuation strictly greater than t, and P_0,P_1 are 2-adically integral. Hence D has valuation exactly t and is nonzero at every pair with strictly positive valuations. In particular all iterates (x_n,y_n) of the monomial map from (x_0,y_0)=(x,y) are regular: 1-x_{n+1} and D are nonzero. This is stronger than just checking a generic Mahler system determinant. Also

    min(v2(x_n),v2(y_n)) >= b^n min(v2(x),v2(y)),
    y_n/x_n = (y/x)^(λ^n).                                (4)

The second equality follows directly by taking the quotient of the two monomials. For λ=0 use it at n>=1. Nonperiodicity excludes λ=b (then σ(0)=0^b, σ(1)=1^b and every fixed point is constant) and λ=-b (first letter cannot be fixed). Thus |λ|<b.

## 4. Formal transcendence, including weighted one-variable specializations (MPS-3)

Here is an elementary version of the finite-alphabet algebraicity obstruction; it also works after the variable rescaling needed when |λ|=1. For any fixed nonzero rational c,

    H_c(z)=G_1(z,c z)=sum_j s_j c^{n_1(j)} z^j

is transcendental over Q(z) when s is not eventually periodic.

Proof: an algebraic formal power series in characteristic zero is D-finite: its derivatives belong to the same finite extension of Q(z), since the minimal polynomial is separable. Linear dependence of finitely many derivatives, with denominators cleared, gives a nonzero polynomial-coefficient differential equation. Extracting coefficients gives a nontrivial recurrence sum_{k=0}^r p_k(n) u_{n+k}=0 for all sufficiently large n, where u_j=s_j c^{n_1(j)}. To see nontriviality of the extraction, group derivative monomials z^i d^j/dz^j by their index shift j-i; within each group the falling-factorial polynomials have distinct degrees j.

Divide the recurrence by c^{n_1(n)}. The resulting tuple of normalized values depends only on the finite binary word s_n,...,s_{n+r}, and hence ranges over a finite set. For each possible tuple the left side is a polynomial in n. Beyond the largest integer root of all its nonzero possibilities, every tuple that actually occurs must make that polynomial identically zero. Choose a degree of the original p_k with a nonzero coefficient vector. Its coefficient yields a nonzero constant-coefficient recurrence for u. With r now the largest index with nonzero coefficient, divide again by c^{n_1(n)}. The earlier r letters determine s_{n+r} uniquely because c^{n_1(n+r)-n_1(n)} is nonzero and determined by those letters. A deterministic finite-state recursion is eventually periodic (the r=0 case forces a zero tail). Contradiction.

Taking c=1 also proves G_1(X,Y) transcendental over Q(X,Y): any polynomial relation could be divided by the largest common power of X-Y, then restricted to X=Y=z to give a nonzero polynomial relation for H_1. The formal substitution is valid degree by degree. This proof is a weighted variant of the classical Fatou finite-alphabet principle, not an assumption that the physical word has small complexity.

## 5. Mahler auxiliary-polynomial proof at the exact physical rational point (MPS-4)

Suppose B_0=G_1(x,y) is algebraic in Q_2. By (3) and its established regularity all B_n=G_1(x_n,y_n) lie in the fixed number field K=Q(B_0). Use absolute logarithmic Weil height h. For the rational starting values and monomial map, h(x_n),h(y_n)=O(b^n). Solving (3) for B_{n+1}, the rational coefficients have height O(b^n); the elementary height inequalities give h(B_{n+1})<=h(B_n)+O(b^n), hence h(B_n)=O(b^n). The implied constants here depend on σ, x,y,B_0, not on an auxiliary polynomial.

For any fixed integer polynomial R(X,Y,W) of degree at most m in each variable, the standard polynomial evaluation bound (apply the local triangle inequality and sum over places) gives

    h(R(x_n,y_n,B_n)) <= C m b^n + O_R(1).               (5)

For any nonzero η in K, the product formula / height of η^{-1} gives

    v2(η) log 2 <= [K:Q] h(η).                             (6)

The local embedding into Q_2 is the one used throughout. No conjectural transcendence or prime distribution estimate is used.

### Case A: |λ|>=2 and y/x != 1

There are (m+1)^3 coefficients in a polynomial R of the above degrees. Impose the homogeneous linear equations that the coefficients of total degree < d= floor(m^(3/2)) in R(X,Y,G_1(X,Y)) vanish. There are d(d+1)/2 such equations, fewer than the unknowns. Choose a nonzero rational solution and clear denominators. By Section 4, the resulting series F is not zero. Let its first nonzero homogeneous part have degree t>=d, with form X^t P(Y/X) for nonzero integer polynomial P. All coefficients of F are integers.

The ratios r_n=(y/x)^(λ^n) are distinct (the slopes are positive rational, and y/x != 1), so P(r_n) != 0 for all sufficiently large n. Their heights are O(|λ|^n). Therefore v2(P(r_n))=O_R(|λ|^n) from above, by the rational version of (6). The leading homogeneous evaluation has valuation at most

    t min(v2(x_n),v2(y_n)) + O_R(|λ|^n),

using v2(y_n/x_n)=O(|λ|^n). All higher-degree terms have valuation at least (t+1) min(v2(x_n),v2(y_n)). As |λ|<b, the leading part has strictly smaller valuation than the tail for sufficiently large n. This proves nonvanishing at the moving point, not merely nonvanishing as a formal series. Integrality of all coefficients also gives

    v2(F(x_n,y_n)) >= d min(v2(x),v2(y)) b^n.

Since F(x_n,y_n)=R(x_n,y_n,B_n), equations (5),(6) are incompatible for m sufficiently large (d/m tends to infinity). Contradiction.

### Case B: |λ|<=1 or x=y

On an infinite subsequence of n, y_n/x_n=c is a fixed nonzero positive rational: for λ=0 use n>=1, for λ=-1 take one parity, for λ=1 the ratio is unchanged, and x=y is immediate for every λ. Use H_c from Section 4 instead of G_1. There are (m+1)^2 unknowns in an integer polynomial R(Z,W) with degrees at most m. Vanish the first d=(m+1)^2-1 coefficients of R(z,H_c(z)); clear denominators. This nonzero convergent 2-adic series has order t>=d at zero. For z=x_n on the chosen subsequence, its leading term strictly dominates for sufficiently large n, so

    v2(R(x_n,B_n)) = t v2(x_n)+O_R(1).

For clarity, even if v2(c)<0 the coefficients of H_c have valuation at least -j |v2(c)|, so the series converges on a nonzero 2-adic disk; polynomial substitution preserves this and leading-term dominance near zero. The same height inequalities (5),(6) contradict d/m tending to infinity. This handles the balanced, almost-balanced and equal-slope cases without applying a multivariate nonvanishing assertion on a degenerate orbit.

Thus B_0 is transcendental. Equation (2) proves MPS-1. For an eventually periodic word, split off its finite prefix and sum the tail geometric inverse affine composition, giving a rational completion. Finite prefix attachment or removal is an invertible rational affine map and preserves algebraicity/transcendence.

## 6. Explicit expanding nonperiodic family, not a critical-height application

For every b>=12 take σ(0)=0^(b-1)1 and σ(1)=10^(b-1), prolongable on 0. The fixed point has exactly one P in each b-letter aligned block. Both images have slope forward 9^b/(4*8^b)>1. Thus real height contraction cannot exclude these words. Indeed b=12 satisfies 9^12>4*8^12, and the ratio increases with b. The fixed point is not eventually periodic: s_{bk}=s_k, s_{bk+b-1}=1-s_k, other positions zero. Both allowed one-residues 0,b-1 occur infinitely often. An eventual period p must preserve this two-element residue set by translation modulo b, so b divides p (b>=3). The identity s_{bk}=s_k then makes p/b an eventual period. Infinite descent on p is impossible.

The physical completion is transcendental even though every finite gap prefix has positive ordinary lifts and the prescribed forward block slopes expand. This is a literal obstruction at an unchanged rational source, not a growth heuristic. The theorem equally covers unbalanced substitutions, e.g. σ(0)=0001, σ(1)=1110 (λ=2), when taking a nonperiodic fixed word, regardless of its mean forward coefficient.

## 7. Full-proof attempt and remaining barrier

This does not establish that any exceptional ordinary Collatz itinerary is substitutive. The main hoped-for bridge would be an arithmetic theorem forcing an arbitrary ordinary-realizable scalar-phase return schedule to have a finite substitution description, or a different mechanism yielding enough functional equations for the physical completion. The actual scalar recurrence does not imply this: the PR182 L/P symbolic language allows arbitrary schedules. Nonautomatic/high-complexity physical schedules remain unexcluded, as do arbitrary positive cycles. We did not assert a full Collatz proof or universal rational scalar classification.

The new technique makes auxiliary-polynomial/Mahler rigidity a concrete, fixed-source tool beyond repeated factors. The proof is an application of classical transcendence machinery; no historical priority claim is made. A natural next task is to extend the nonvanishing argument to binary codings of larger uniform morphisms (finite-dimensional kernel, possibly singular coefficient matrix) and then to nonuniform substitutions (nonconstant monomial growth). Do not confuse either extension with coverage of all ordinary trajectories.

## 8. Sources and evidence

Frozen source pins and research map: see SOURCES.md. Classical background: Fatou's finite-alphabet theorem (P. Borwein and M. Coons, https://arxiv.org/abs/0806.1563); Mahler's auxiliary-polynomial method and p-adic examples (https://irma.math.unistra.fr/~bugeaud/travaux/p-adic18.pdf); the proof here supplies its own D-finiteness argument, regularity, propagation of height and moving-point nonvanishing instead of invoking a generic lifting theorem. Standard Weil-height inequalities/product formula are used in Section 5.

MahlerCore.lean proposes the exact finite weight, concatenation, substitution, telescoping, and physical affine expansion identities. It does not formalize transcendence, the infinite analytic limit, or Collatz. No sorry or custom axiom intended; compiler replay and dependency audit pending (Lean/Lake absent locally). controls.js executes exact rational finite checks, not the all-time proof. See CHECKS.md for the actual execution record. Repository-wide validator was not run in a complete checkout.
