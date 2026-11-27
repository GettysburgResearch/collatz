# Macroscopic mixing and quantitative finite-state prediction rigidity

**PROPOSED written proof, conditional on the explicitly pinned written estimates P of PR146; all-source closure consequence also uses M.** The theorem below strengthens PR200 AUTOMATA.md from a sparse-error obstruction to a decorrelation statement valid for every fixed automaton and a growing-state class. No conjecture is assumed in deriving the decorrelation.

Let f:N+ -> {0,1} be ANY invariant ordinary label, f(Tn)=f(n). In particular f can be the indicator of the basin of 1. Put c_X=X^(-1) sum_(1<=n<=X) f(n) for integer X.

Input P (PR146, f431078244e868dc699fad011044f0d5e7f76437): THREE_RAY_UPPER.md gives O(X/sqrt(log X)) actual tripling discrepancies on intervals, and TRIPLING_VARIATION.md bounds adjacent label changes in any fixed-ratio interval by O of the corresponding odd tripling defects in a larger fixed-ratio interval. The estimates apply to invariant labels since different labels imply nonmeeting. These are source-qualified, not independently rebuilt here.

## 1. Uniform macroscopic discrepancy

Write theta=log_2 3 (modulo 1), epsilon_R=(log R)^(-1/2), and use the logarithmic circle representation

    g_R(t)=f(floor(R 2^t)), 0<=t<1,
    a_R=integral_0^1 g_R(t) dt.

For arbitrary real R>=large, P and exact doubling invariance give

    ||g_R(t+theta)-g_R(t)||_1 <= C epsilon_R,
    ||g_(2R)-g_R||_1 <= C epsilon_R.                (1)

Reconstruct the rounding: theta rotates x=R2^t to 3x/2^j in the same shell, j=1 or 2. The integer 3floor x differs from 2^j floor(3x/2^j) by at most four, so a discrepancy costs either a tripling defect or a nearby adjacent change. Each adjacent change is charged by O(1) n; each failed odd part has O(1) doublings in the shell. Each n has logarithmic measure O(1/R). For doubling, floor(2x) is 2floor x or one more; a difference requires an adjacent change. This is the same rounding geometry as PR146 but used here in weak rather than strong convergence.

Fix a Diophantine exponent kappa>=1 and c>0 with ||h theta||>=c h^(-kappa) for h>=1. Such effective kappa follows from the classical two-logarithm lower bound (Baker–Wüstholz; see source pins). Let p/q be a reduced Dirichlet approximation chosen with q<=L and |q theta-p|<=1/L. Then q>=c' L^(1/kappa), and |theta-p/q|<=1/q^2. The q rotation points have discrepancy O(1/q) for EVERY circle interval, by comparison to the translated rational grid with error at most 1/q.

For G_R=g_R-a_R, average the test 1_I over these q rotations. Its pointwise deviation from |I| is O(1/q), and replacing the original integral by the rotated average incurs O(q epsilon_R) by (1). Since integral G_R=0,

    sup_I |integral_I G_R| <= C (q epsilon_R + 1/q).
    
Choose L comparable to epsilon_R^(-kappa/(kappa+1)). We obtain a uniform primitive bound delta_R=O(epsilon_R^(1/(kappa+1)))=O((log R)^(-a)), a=1/[2(kappa+1)].

Change variables x=R2^t. Multiplying by the bounded-variation weight (log 2)2^t costs only a constant factor in the primitive bound (integration by parts). Counting whole integer cells differs from the resulting real integral by O(1) at endpoints. Thus any interval inside [R,2R] has discrepancy from density a_R at most C R delta_R.

For arbitrary [A,B] in [1,X], split into shells R_j=X/2^j, j>=1. Discard the portion below sqrt X at cost O(sqrt X). For the remaining shells delta_R=O(delta_X), and |a_R-a_X|<=C j epsilon_(sqrt X) by (1). Summing shell lengths times these errors uses sum_j j2^(-j)<infinity. Applying the same bound to [1,X] itself replaces a_X by c_X. We get the uniform all-subinterval estimate

    sup_(1<=A<=B<=X) |sum_(A<=n<=B)(f(n)-c_X)|
       <= C X (log X)^(-a).                     (2)

Also P summed over dyadic shells gives total adjacent variation O(X/sqrt(log X)) below X. Constants here depend on the pinned estimates and theta but NOT on the later automaton.

## 2. A quantitative automaton averaging lemma

Fix an integer digit base B>=2. A deterministic finite automaton with output in [0,1] reads the canonical most-significant-first expansion (no leading zeros); its initial state is fixed. Let it have S states and transition matrix P_B under a uniform next digit. If n ranges over an aligned interval [p B^k,(p+1)B^k) with p>=1, the average output is EXACTLY (P_B^k o)(q_p), where q_p is the state reached after reading p. The suffix includes arbitrary leading zero digits of length k. This is finite enumeration, not an assumption about integer dynamics.

The following two uniform mixing estimates are useful.

* From any state, a closed recurrent class can be reached in <=S steps, since the finite directed graph has terminal strongly connected components. A chosen path has probability >=B^(-S). Therefore after L-1 random digits, the probability to remain transient is at most exp(-floor((L-1)/S) B^(-S)).
* Within a recurrent class, its cyclic phase advances deterministically by one modulo its period d. For any two states in the same cyclic phase, there are equal-length paths to a common state. Indeed closed walk lengths at one chosen vertex have gcd d; a finite subset already has this gcd. Nonnegative integer combinations of finitely many positive integers with gcd d contain all sufficiently large multiples of d: divide by d, then use residues modulo one generator and append copies of it. Two initial paths to that vertex have lengths congruent modulo d, so append suitable closed walks to equalize. Now the directed product graph of ordered pairs has at most S^2 vertices. A shortest path from this pair to the diagonal therefore has length <=S^2. At clock S^2 both digit-walk distributions share at least B^(-S^2) of the same tail distribution: use the two chosen words to a common state, then the same distribution of remaining digits. Their total variation distance is at most 1-B^(-S^2). The usual elementary coupling of finite probability distributions (match their common mass) and iteration gives contraction on any given phase over blocks of S^2 clocks.

The unique stationary probability on an irreducible finite class, normalized on each cyclic phase, is transported by P_B to the next phase. It follows that for any recurrent starting state q, the average P_B^k o(q) is within

    exp(-floor(k/S^2) B^(-S^2))

of the conditional stationary output mean in its FINAL phase. This is uniform in the starting state, the entire transition table and the output in [0,1]. The product-graph bound avoids needing to synchronize a deterministic word across different phase classes; the two paths may use different digits.

## 3. Decorrelation, even for slowly growing automata

For a fixed base B allow an automaton A_X to depend on X with state count S_X satisfying

    S_X^2 = o(log log log X).                      (3)

Write g_X(n) for its output. Choose k=L=floor(gamma log_B log X) with fixed 0<gamma<min(a,1/2). For large X both k and L tend to infinity.

Partition the positive integers into aligned B^k blocks. Discard the partial boundaries and the part n<X/(log X)^2; their total relative cost is o(1). On a whole block having no adjacent f change, f-c_X is constant. Replacing g_X by its average within each block therefore leaves its correlation with f-c_X unchanged there. The number of bad blocks is at most the total variation of f, and their error contribution is O(B^k X/sqrt(log X)) before normalization. This is o(X). All remaining digit lengths exceed L+k for large X.

Look at the state reached after the first L digits. Among all length-ell canonical strings with ell>=L, the fraction whose L-prefix state is transient is at most the first bound of Section 2 (first nonzero digit is fixed or averaged, later digits uniform). Bounding a possibly truncated last length by its full length interval changes counts by at most a factor B. The total discarded proportion is o(1) by (3).

On each other aligned block the state after truncating the last k digits is in a recurrent class. Section 2 replaces its block average by the conditional stationary output mean in the phase determined solely by the class and phase of the first L-prefix and by the TOTAL digit length ell. No later digit can change that class or alter the phase advancement. The uniform replacement error tends to zero by (3): indeed B^(S^2)=(log log X)^(o(1)), and k/S^2 grows faster than this. The transient error has the same property.

The resulting bounded function is constant on each interval determined by the first L digits and the total digit length. Above X/(log X)^2 there are O_B(log log X) possible lengths and O(B^L) prefixes per length. Its correlation with f-c_X is at most their number times the discrepancy in (2), which is o(X) because gamma<a. Combining all errors proves

    (1/X) sum_(n<=X) (f(n)-c_X) g_X(n) -> 0.       (AUT)

In particular for every fixed automaton in every integer base, (AUT) holds. The assertion is uniform over all automata of a fixed base satisfying the stated state bound; no fixed transition table is assumed in (3). If B varies with X the above counting and growth estimates require modification; no such assertion is made.

## 4. Consequences for full convergence

For binary g_X, write d_X=(1/X)sum g_X(n), and Err_X for the fraction of differing binary labels. The exact identity is

    Err_X = c_X+d_X-2 (1/X)sum f(n)g_X(n)
          = c_X+d_X-2c_X d_X+o(1)
          >= min(c_X,1-c_X)+o(1).

Thus every fixed digit automaton, and even the growing-state class (3), is asymptotically no more accurate than the best constant prediction at each cutoff, up to o(1). This also extends to any bounded sequence in the Besicovitch L1 closure of fixed automatic sequences: approximate it by a fixed automaton with arbitrarily small limsup mean error, and use |f-c_X|<=1.

Now use external source-qualified input M: every fixed positive ternary-unit target has positive LOWER natural predecessor density (reported by Mazur, 6 Sep 2026; see PR199 and PR201 pins; not independently rebuilt here). If Collatz is false, choose a positive nonconverging odd unit b by taking an odd step and stripping twos. Every predecessor of b is nonconverging, while every predecessor of 1 converges. M therefore gives min(c_X,1-c_X)>=eta>0 for all sufficiently large X. The same eta works for ALL fixed digit automata and the growing-state family, irrespective of their state transitions. Consequently, conditional on M and P:

    Collatz holds iff its basin indicator admits o(1) mean error
    along unbounded cutoffs by automata of one fixed base with (3).

The forward implication uses the one-state constant-1 classifier. The reverse uses the positive lower densities and (AUT). A sequence of arbitrary large finite lookup tables does not meet the state restriction. This is a stronger criterion than PR200's earlier fixed-automaton sparse-error obstruction, but no construction of such a classifier is proved. Without M, (AUT) alone does not exclude a zero-density nontrivial basin.

Finite controls exhaust all 810 binary automata with up to three states and ternary automata with two states (including reducible and periodic cases), checking 2113 reachable product-graph pairs and 140 aligned-block averages. They test the elementary averaging kernel only, not the analytic theorem.