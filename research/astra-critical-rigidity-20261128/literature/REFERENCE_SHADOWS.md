# Physical rational references for arbitrary affine arcs

**Status: PROPOSED.** A length-$L$ parity word with an affine reference of endpoint heights at most $H$ agrees, except possibly on its final $\lfloor\log_2 H\rfloor$ letters, with the actual shortcut trajectory of its reference source. Over a path, $K$ such separated affine pieces can be replaced by at most $K+1$ separated, physically realized **signed rational** pieces, at endpoint height at most $4H^{1+\log_2 3}$. On a circle, $K$ suffice. The extra open-path piece is necessary in general, even if the allowed physical height is any fixed polynomial in the original height. For a sufficiently long individual word there is at most one low-height affine reference source, which can be recovered or ruled out by continued fractions.

Write $F_0(x)=x/2$, $F_1(x)=(3x+1)/2$ and $H(a/b)=\max(|a|,b)$ in lowest terms with $b>0$. Rational physical parity is defined on the rationals with odd reduced denominator, by reduction modulo two. An affine reference applies the specified branches irrespective of that parity. Separation means its source differs from the actual source of the arc being studied. The native path can be positive while its reference is signed.

## The exact length of the uncontrolled suffix

For a nonzero rational input of negative $2$-adic valuation, either prescribed branch reduces that valuation by one, since the term $3x$ dominates $1$ at two. From a $2$-integral input the correct parity branch remains integral at two; the other branch gives valuation exactly $-1$. Consequently:

* If the reference source has $2$-part $2^a>1$ in its reduced denominator, its terminal denominator has $2$-part exactly $2^{a+L}$.
* If it starts integral at two and first uses the wrong parity at time $j<L$, the terminal denominator has $2$-part exactly $2^{L-j}$.
* If both endpoints are integral at two, **every** applied parity is physical. Otherwise any unverified suffix occupies at most $B=\lfloor\log_2 H\rfloor$ letters when the terminal height is at most $H$.

Zero uses its usual even parity and stays integral under the even branch. The physical ring here permits reduced denominators divisible by three. Such a factor may disappear at an odd departure.

## Changing the cuts

For the $i$th affine word write $P_i S_i$, where $P_i$ is the maximal initial physical segment of its specific reference and $S_i$ is the residual, of length at most $B$. Set $P_i$ empty if the source is not integral at two. Each nonempty $P_i$ starts at a $2$-integral rational of height at most $H$. Its end $\zeta$ has height at most $2H^2$. To see this when $S_i$ has positive length $e$, write $\eta$ for its terminal reference, $g$ for its grade, and $C$ for its carry. The terminal reduced denominator has exact dyadic part $2^e$, so $2^e|\eta|\le H$. The odd-departure formula gives

$$
 C/3^g=\sum_{j\ {\rm odd\ departure}}\frac{2^j}{3^{1+g_j}}<2^e ,
 \qquad \zeta=(2^e\eta-C)/3^g ,
$$

where $g_j$ counts odd departures strictly before $j$. Thus $|\zeta|\le H+2^e\le2H$. Its odd denominator is at most the denominator of the reference source along the physical segment, hence at most $H$. If $S_i$ is empty, the endpoint already has height at most $H$.

Use the new pieces

$$
      P_1,\quad S_1P_2,\quad S_2P_3,\quad\ldots,\quad S_{K-1}P_K,\quad S_K .
$$

Omit empty pieces. If $P_i$ is nonempty, force any preceding suffix $S_{i-1}$ backwards from its known source $\xi=a/b$ using $y\mapsto2y$ or $y\mapsto(2y-1)/3$ in the reversed order. The resulting start is integral at two because the odd denominator $b$ gains at most powers of three. The prescribed branches return it to $\xi$; since both endpoints are integral at two, all the forced branches are physical by the valuation argument. More explicitly its unreduced numerator and denominator are $2^e a-C b$ and $3^g b$. The carry of an $e$-bit word is at most $3^e$ (the unrestricted maximum is $3^e-2^e$, attained by all ones). Both coordinates are at most $2H\,3^e\le2H^{1+\log_2 3}$ in absolute value. Separation at $\xi$ implies separation at the new beginning since the preceding affine map has nonzero slope. The terminal point is the physical end of $P_i$.

For any leftover suffix of length $e>0$ with no following physical prefix, choose a positive ordinary representative of its binary source cylinder differing from the actual source at that cut. Two representatives in $[1,\,2^{e+1}]$ are always available. Its size plus one grows by at most $3/2$ per step, so its terminal height is at most $3\cdot3^e$. This also handles an originally nonintegral reference source. For a circle, prepend the last residual to the first physical prefix, or treat it as the corresponding leftover when that prefix is empty. All pieces now number at most $K$, without modifying the underlying cyclic order. The converse inclusion follows by using each physical reference as an affine one. Thus for bounded numbers of pieces, a sublinear logarithmic height budget is equivalent in the two models. On an open path their sharp number of pieces can differ.

## The extra open piece is necessary

Take $W=(0^L1)^K$. Each of its $K$ displayed words has the affine reference $0\to1/2$ of height two. Every positive ordinary representative of its full cylinder is separated from these references. To guarantee a simple underlying path of duration $D=K(L+1)$, take a representative greater than $2^{3D}$. Every physical state in the window exceeds $2^{2D}$ by the one-step halving lower bound, whereas a positive cycle of duration at most $D$ has minimum at most $D2^D/3$ by the [cycle product estimate](BEFORE_CROSSING.md).

Let a signed physical reference start with height at most $H$ on an arbitrary subword of $W$. Its odd denominator stays at most $H$. No two consecutive letters are odd. Any two-step affine map on this word has slope at most $3/4$ and additive carry at most $1/2$, by inspecting $00,01,10$. Iterating on pairs gives magnitude at most $\max(H,2)$ at the even-indexed cuts, and therefore at most $3(H+1)$ at every cut. A physical reference containing a whole $0^L1$ would have a nonzero state at its beginning with numerator divisible by $2^L$. This is impossible if $2^L>3H(H+1)$. Every one of the $K$ disjoint blocks then needs a strictly interior cut, so at least $K+1$ pieces are required. They suffice here even at fixed height: take reference $0$ on the initial zero run, $-1/3$ on each $1\,0^L$ (the first odd step sends it to zero), and $-1/3$ on the last single odd letter. All are separated from the positive physical source.

Signed rationality matters separately. The all-odd word has the height-one fixed reference $-1$. A positive physical rational realizing $L$ initial odds obeys $v_2(x+1)\ge L$. If $x=a/b>0$ is reduced, $a+b\ge2^L$, so $H(x)\ge2^{L-1}$.

## Recovering the unique small candidate

Put $B=\lfloor\log_2H\rfloor$. For any fixed length $L$ there are at most $3H^3$ words with an affine reference of endpoint heights at most $H$. If $L>B$, each source is integral at two, so its actual first $L-B$ letters are forced and only $B$ terminal letters are free. If $L\le B$ there are at most $2^B$ words altogether. In either case there are at most $3H^2$ rational starting descriptions. In the [ordinary pre-crossing count](BEFORE_CROSSING.md), this gives the stronger bound $K[3(D+1)H^3]^K$.

For a given word with $M=2^{L-B}>2H^2$, its first $L-B$ letters determine one residue $R\bmod M$, chosen in $[0,M)$. Compute it from the carry and grade of the prefix, or read it off the actual source. Any low-height candidate $a/b$ must satisfy $a\equiv bR\bmod M$ with odd $b$. Two such fractions have cross-difference divisible by $M$ and of magnitude at most $2H^2$, so they coincide. Moreover $k=(bR-a)/M$ gives a reduced fraction $k/b$ and

$$
       |R/M-k/b|=|a|/(Mb)<1/(2b^2).
$$

The standard Legendre criterion for continued fractions makes $k/b$ a convergent of $R/M$. Enumerate its finite continued-fraction convergents, test $a=bR-kM$, $|a|,b\le H$, $\gcd(a,b)=1$ and odd $b$, then evaluate the **whole** word on $a/b$. Keep a candidate exactly if its terminal height is at most $H$ and, when required, its source is separated. This is a decision algorithm polynomial in the bit lengths of the word data. Uniqueness by itself only tests the initial congruence. The full word evaluation is needed for the terminal height.

The rational-approximation criterion is proved as Real.exists_rat_eq_convergent in [Mathlib at d13f23b723b8a846827a245b89c10fc7d3f11612](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/NumberTheory/DiophantineApproximation/Basic.lean). This test applies to each sufficiently long actual arc. The existence of arbitrarily long small-reference covers on any specified nonperiodic positive source is a separate dynamical requirement.

The [exact checker](check_reference_shadows.py) tests 9,906 valuation histories and compares continued-fraction reconstruction against full rational enumeration on 1,416 binary words. Exactly 98 admit a reference at the tested heights. Dynamic programming on $(0^{14}1)^K$, for $1\le K\le6$, returns optimal costs $K$ for height-two affine references and $K+1$ for height-three physical ones. These checks use signed rational endpoints and exact integer arithmetic.
