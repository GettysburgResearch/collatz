# Physical Mahler script audit and the reducible binary case

**Pinned source.** PR190, ba58227c5a047ff3859a148a5fdaac4fd1451e4c, research/mahler-physical-scripts-20261124/README.md (MPS-1 to MPS-4, SHA256 cf21b34f190cc2c1bf7891577079a1d09eeadcd31aca9e7fb7ee2427fed7600e) and PRIMITIVE_MORPHISMS.md (MPS-5 to MPS-6, SHA256 af537c75df871e454308268bf3b30aae5655923a26faecc1e925a35602f4a837). The mathematical audit below is of the written proofs. The new reducible theorem is PROPOSED written mathematics.

## Source claims

| ID | Verdict | Reason |
|---|---|---|
| MPS-1 | VERIFIED at its stated script scope | The two physical affine inverse maps have positive rational slopes of positive 2-adic valuation and distinct fixed points. Their common itinerary has one odd 2-adic completion. Its expression in $G_1(x,y)$ is affine with a nonzero rational linear coefficient. |
| MPS-2 | VERIFIED | Substitution-block grouping is exact. At every strictly 2-adically contracting rational point, the first differing binary symbol separates two infinite word evaluations in $G_1$. Applied to the two periodic substitution images this also handles a proper-prefix relation in MPS-5. If their periodic repetitions agree, all concatenations of the two images are periodic. |
| MPS-3 | VERIFIED | A nonzero polynomial relation for $G_1$ can be cleared of the common factor $X-Y$ before diagonal specialization. The one-clock weighted D-finite argument genuinely recovers the original word from the normalized finite coefficient tuple. |
| MPS-4 | VERIFIED | A fixed candidate algebraic value and the exact affine Mahler equation keep all forward iterates inside one embedded number field. Heights grow on the substitution clock. The univariate and bivariate nonvanishing cases separately establish a nonzero auxiliary value, so the product formula applies to that value. |
| MPS-5 | VERIFIED | With primitive binary incidence, Perron growth is simple and the two nonleading error coordinates have scale $O(|\mu|^n)$. An irrational weight ratio distinguishes all monomials. For rational weights, the exact transverse power ratio resolves all collisions except the constant-ratio cases, which MPS-6 resolves. |
| MPS-6 | VERIFIED | Normalize the size-$r+1$ recurrence window at the last pre-window symbol boundary. Each nonzero entry is a product of boundedly many fixed factors. After polynomial recurrence extraction, coefficient comparison beyond finitely many roots leaves a nonzero constant recurrence. At an actual boundary its last coefficient recovers the next letter, and updating by the letter's clock length and weight gives a deterministic finite boundary state. |

For MPS-3/6, algebraicity in characteristic zero makes coefficient derivatives linearly dependent over the rational-function field. On coefficient extraction, group terms $z^iD^j$ by the shift $j-i$. The factors from different $j$ in a shift have different polynomial degrees, so the resulting recurrence is nonzero. The normalized tuples are finite even when $a,b$ are not units of the rational integers or have negative real sign. At clock boundaries the current coefficient is either zero or its known nonzero prefix weight, and both types have a deterministic next state. This proves formal transcendence before using any algebraic specialization of the physical point. The rational parameters in MPS-5's fixed-ratio case exist by Bézout with the two relatively prime positive Perron coordinates. Their 2-adic sizes tend to zero. A leading univariate coefficient therefore dominates even when the coefficient denominators grow exponentially with degree.

For the irrational Perron ratio, the first nonzero weight in a nonzero integral auxiliary series is attained exactly once. Discarding all terms above a sufficiently large *fixed* total degree ahead of the large-$n$ argument leaves a strictly positive valuation separation on the remaining finite set. The discarded tail is controlled uniformly by the minimum coordinate valuation and integrality. For rational coprime weight coordinates $(p,q)$, exponents on a common weight line differ by multiples of $(-q,p)$. Their evaluation is a monomial times $P(y_n^p/x_n^q)$ for a nonzero one-variable polynomial. Unless the ratios cycle, their distinct positive rational values eventually avoid the finite root set and their heights grow only as $O(|\mu|^n)$. These conditions control both exact cancellation and excess 2-adic valuation. The constants in the height upper bounds multiplying auxiliary degree do not depend on the selected polynomial. Its fixed coefficient heights can then be absorbed by taking $n$ large after choosing the degree.

A minor formulation detail is that the choice of a particular binary substitution word, followed by block encoding, is essential. An arbitrary finite alphabet with a binary coding need not give a fixed point of a binary substitution. The adjective “substitutive” in the conclusion is read with the precise fixed-point hypotheses in MPS-5's statement.

## Extension to all nonidentity, non-erasing binary substitutions

**Theorem (proposed).** Take two nonempty physical gap blocks whose rational inverse affine maps have different fixed points. Let the binary schedule be a non-eventually-periodic one-sided fixed point of a non-erasing binary substitution other than the identity. Its unique physical completion is transcendental over $\mathbb Q$. No nonprimitive nonuniform spectral hypothesis is required. The conclusion also applies after a finite shift of the itinerary.

We use the functions, iterates and height estimates of MPS-1–6. With the physical inverse slopes $x,y$ one has $x,y\in\mathbb Q_{>0}$ and $v_2(x),v_2(y)>0$. Prefix generating series are $G_i(X,Y)=\sum_{j:s_j=i}X^{n_0(j)}Y^{n_1(j)}$. They obey $(1-X)G_0+(1-Y)G_1=1$. For this nonperiodic fixed word its affine substitution equation is regular at all the iterates of the physical point, by MPS-5 §1. If $B_0=G_1(x,y)$ were algebraic over $\mathbb Q$, all $B_n=G_1(x_n,y_n)$ would lie in one number field embedded in $\mathbb Q_2$ and satisfy $h(B_{n+1})\le h(B_n)+O(h(x_n)+h(y_n)+1)$. The constants depend on the fixed substitution and physical maps. Absolute logarithmic Weil height satisfies $v_2(\xi)\log2\le[K:\mathbb Q]h(\xi)$ for nonzero $\xi$ in this field.

Primitive substitutions are covered by MPS-5. An irreducible imprimitive two-letter substitution interchanges the first letter of every word and cannot have a one-sided fixed point. A diagonal incidence matrix gives images $0^a,1^d$. If the first symbol expands, its fixed word is constant. If it is fixed as a letter while the other expands, either the word is constant or the tail from the first expanding symbol is constant. When both symbols are fixed the substitution is the identity, excluded in the statement. The remaining reducible matrices, after renaming letters, have the form
$$
M=\begin{pmatrix}a&b\\0&d\end{pmatrix},\qquad b\ge1,\ d\ge1,
$$
where $\sigma(1)=1^d$ and $\sigma(0)$ contains $a$ zeros and $b$ ones. A non-eventually-periodic binary word has infinitely many zeros and ones. If $a=0$ a fixed word contains no zero. The different possible triangular growth rates are treated below.

### 1. The pure image grows faster, $d>a$

Here $d\ge2$, the Perron eigenvalue is $d$ with positive right eigenvector $(b/(d-a),1)$. Both coordinate valuations equal a positive constant times the corresponding Perron coordinate times $d^n$, with errors $O(a^n)$. This follows directly from
$$
y_n=y^{d^n},\qquad x_n=x^{a^n}y^{b(d^n-a^n)/(d-a)} .
$$
Thus all the rational-weight parts of MPS-5 §§2,4–6 hold with $\lambda=d$ and $\mu=a$. For coprime integer Perron coordinates $p,q$, the transverse ratio is precisely $(y^p/x^q)^{a^n}$. Moving-ratio dominance when $a\ge2$ and the constant-ratio weighted specialization otherwise are exactly the verified arguments above. Primitivity supplied the two positive asymptotic coordinates in the source proof; here the explicit triangular formula supplies them.

For example $\sigma(0)=001,\sigma(1)=1111$ is a nonuniform reducible substitution prolongable on zero. Its $\sigma^n(0)$ prefixes have $2^n$ zeros and length of order $4^n$. An eventually periodic word with infinitely many zeros has positive limiting zero density, so this fixed word is aperiodic.

### 2. Both symbols grow, the mixed clock dominates, $a\ge d\ge2$

Put $V_n=v_2(x_n)$. Direct matrix powers give $v_2(y_n)=d^n v_2(y)=o(V_n)$: for $a>d$ the first coordinate has order $a^n$, and for $a=d$ it has order $n a^n$, since the exponent of $y$ in $x_n$ is $bn a^{n-1}$. In either case $h(x_n)=O(V_n)$, $h(y_n)=O(d^n)$ and $\sum_{j\le n}V_j=O(V_n)$, so $h(B_n)=O(V_n)$. Also $y_n\to0$ in $\mathbb Q_2$.

At each fixed exponent of $X$, the coefficient of $G_1(X,Y)$ is a *polynomial* in $Y$: the finite run of ones before the next zero is the entire contribution at that zero clock. All zeros exist because the word has infinitely many zeros. We can therefore treat $G_1$ as a series in $X$ over $\mathbb Q[Y]$. In $\mathbb Q(Y)$ solve the homogeneous linear equations making the first $(m+1)^2-1$ entire $X$-coefficients of $R(X,Y,G_1)$ vanish, with $R$ of degree at most $m$ in each of $X,W$. There are $(m+1)^2$ unknown coefficients in that field. Clear their denominators to obtain a nonzero integral polynomial $R(X,Y,W)$. Its $Y$ degree $C_m$ is finite and may grow arbitrarily fast with $m$.

The substituted series is nonzero by MPS-3's bivariate formal transcendence. Write $P_t(Y)$ for its first nonzero $X$ coefficient; $t\ge(m+1)^2-1$. Since $y_n\to0$, the first nonzero monomial of $P_t$ eventually dominates, giving $v_2(P_t(y_n))=O_R(d^n)=o_R(V_n)$. All other coefficient polynomials evaluate integrally. Hence the term of $X$ degree $t$ eventually has strictly smaller valuation than the whole tail. It follows that
$$
v_2(R(x_n,y_n,B_n))\ge t V_n,\qquad R(x_n,y_n,B_n)\ne0.
$$
The height upper bound is $C mV_n+O_R(d^n+1)$, with $C$ independent of $m$; the unbounded $Y$ degree costs only $C_mh(y_n)=o_R(V_n)$. Fix $m$ large, then let $n$ grow. This contradicts the product formula.

### 3. One symbol is fixed, $d=1$

Remove the finite initial string of ones up to the first zero. It is fixed by the substitution, so the remaining word is again fixed, and finite physical prefix removal preserves algebraicity. Its first symbol is zero, forcing the image $\sigma(0)$ to start with zero. If $a=1$ then $\sigma(0)=01^b$; its iterates force a constant-one tail, contrary to hypothesis. Thus $a\ge2$. Write
$$
\sigma(0)=0\,1^{\ell_1}0\,1^{\ell_2}\cdots 0\,1^{\ell_a},\qquad
e_r=\sum_{j=1}^r\ell_j,\quad b=e_a,\quad e_0=0.
$$
Let $c(k)$ be the number of ones strictly before zero number $k$, with the first zero numbered zero. Counting complete images and the within-block prefix gives
$$
c(ak+r)=bk+c(k)+e_r,\qquad 0\le r<a .
$$
Here the physical second multiplier is a *fixed* positive rational $y$ with $v_2(y)>0$, hence $y\ne1$. Use the positive real algebraic number $\tau=y^{b/(a-1)}$ only to establish formal transcendence, with no identification of real and 2-adic limits. Set
$$
f_k=y^{c(k)}/\tau^k,\qquad d_r=y^{e_r}/\tau^r,\qquad
H(z)=\sum_{k\ge0}f_k z^k,\qquad P(z)=\sum_{r=0}^{a-1}d_r z^r .
$$
Then $f_0=d_0=1,\ f_{ak+r}=d_r f_k$ and $H(z)=P(z)H(z^a)$ formally.

If $H$ were algebraic over $\overline{\mathbb Q}(z)$, let $M(z,T)$ be its monic minimal polynomial of degree $l$ and let $C(z)\ne0$ be its constant coefficient. The monic polynomial $P(z)^l M(z^a,T/P(z))$ annihilates $H(z)$ and has the same degree as $M$. Equality of the polynomials gives $C(z)=P(z)^l C(z^a)$. Thus the Laurent series $H(z)^l/C(z)$ is invariant under $z\mapsto z^a$. Order comparison and the first nonconstant coefficient imply it is constant, so $R=H^l$ is rational and satisfies $R(z)=P(z)^lR(z^a)$. For each nonzero finite $\xi$, orders satisfy $\operatorname{ord}_\xi R\equiv \operatorname{ord}_{\xi^a}R\bmod l$ because the power map is unramified there. If any such order were nonzero modulo $l$, all the $a^j$ distinct preimages at depth $j$ would also have nonzero order, contrary to the finite divisor of $R$. At zero $R(0)=1$, and the order at infinity is consequently divisible by $l$ too. Factoring the rational function over $\overline{\mathbb Q}$ now shows $R$ is an $l$th power there. Its formal $l$th root $H$ differs from that rational root by an $l$th root of unity. Thus $H$ would be rational.

The coefficients of a rational series in characteristic zero have, eventually, a partial-fraction expression $\sum_{j} Q_j(k)\gamma_j^k$ with nonzero polynomials and distinct nonzero bases. Such expressions are unique: the generating function of each polynomial times $\gamma_j^k$ has a unique pole at $1/\gamma_j$ whose order is one more than the polynomial degree. Since $f_{ak}=f_k$, every base must occur among the $a$th powers of the same finite set. The power map is consequently a permutation on that set, which consists of roots of unity. Iterate until the permutation is the identity. Uniqueness gives $Q_j(a^h k)=Q_j(k)$, hence each $Q_j$ is constant. Thus $f_k$ has finite eventual range. For a fixed digit $r=1,\ldots,a-1$, the base-$a$ integers formed by successively repeating $r$ have values $d_r^j$. A positive real $d_r$ with finite eventual power range must equal 1. It follows that all $f_k=1$, hence $c(k)=bk/(a-1)$ for every $k$ because $y>0,\ y\ne1$. Consecutive zeros are separated by the same integer number of ones, contradicting nonperiodicity.

Therefore $G_0(X,y)=H(\tau X)$ is transcendental over $\overline{\mathbb Q}(X)$, and the formal telescope gives the same for $G_1(X,y)$. Its coefficients are rational and 2-adically integral because each is a finite sum of nonnegative powers of $y$. On the physical iterates, $y_n=y$ and $x_{n+1}=x_n^a y^b$. Thus $v_2(x_n)\asymp a^n$ and the assumed algebraicity gives $h(x_n),h(B_n)=O(a^n)$. Use an integral $R(X,W)$ of degree at most $m$ in each variable vanishing on the first $(m+1)^2-1$ coefficients after substitution of $G_1(X,y)$, obtained by rational linear algebra. The substituted one-variable series is nonzero and its first coefficient dominates at $x_n$ for all sufficiently large $n$. The same valuation-versus-height contradiction as MPS-4 proves that the physical value is transcendental. This completes the last triangular case.

## Physical scope and unresolved problem

A common fixed point of the two physical block maps, if it exists, realizes both infinite periodic repetitions. Uniqueness of the actual valuations then makes the two repetitions identical. Both blocks are initial segments of that same infinite word and each block length is a period. Arbitrary concatenations of the two blocks therefore form the same periodic gap word. In particular any non-eventually-periodic gap word obtained by a non-erasing block encoding automatically has distinct physical fixed points. Equal-length distinct blocks are the familiar special case.

The binary theorem excludes the resulting itineraries at a fixed ordinary rational source. A coded automatic word supplied by a larger substitution alphabet need not be a binary substitution fixed point, and there is no conclusion here for all automatic or all morphic itineraries. The identity substitution fixes every word and gives no functional-equation growth; it must be excluded. Nothing in this proof makes an arbitrary ordinary orbit substitutive or excludes a nontrivial positive cycle.
