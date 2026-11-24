# Punctured sides of a dyadic center have recurring common futures

**PROPOSED written theorem.** Fix a positive ordinary integer $b$. Every nonconstant arithmetic progression of nonnegative exponents admits an infinite arithmetic subprogression of $k\ge1$ on which the following three positive ordinary integers have one common future:
$$
             2^k b-1,\qquad 2^{2k}b+1,\qquad 2^{2k+1}b+1.
$$
The center $b$ keeps its original value throughout the construction. Its own future need not meet the other three under this argument.

After exactly $k$ odd shortcuts the first start reaches $u_k=3^k b-1$. For every $z\ge1$, the odd shortcut from $4z+1$ reaches $6z+2$, and the next halving reaches $3z+1$. Induction on $k$ gives
$$
 T^{2k}(4^k z+1)=3^k z+1.
$$
For the second and third starts this gives $u_k+2$ and $2u_k+3$, respectively. The latter can be compared to $2u_k$, which halves to $u_k$.

Given any exponent progression, restrict further to $k=a+Mh$ with $M>0$ even and $a\ge1$. The values $u_k$ hit every congruence refining the class $u_a\bmod 2^{v_2(b)+v_2(3^M-1)}$. Indeed $3^M$ generates the subgroup $1\bmod 2^{v_2(3^M-1)}$ modulo each finer power of two, as shown by successive squaring in [PERIODIC_BOUNDARIES.md](PERIODIC_BOUNDARIES.md). A prescribed reachable congruence is attained on an entire arithmetic subprogression of exponents by periodicity modulo its modulus.

The deterministic merger-cylinder lemma in section 1 of the same note supplies a refining class for $u_k,u_k+2$. Restrict $k$ to the subprogression realizing it. On this restricted progression the values $2u_k$ again cover a whole binary ball, now with the extra factor of two accounted for in the depth. Apply the lemma there to $2u_k,2u_k+3$ and restrict once more. The first merger still holds. Both new futures intersect the future of $u_k$, and determinism gives a common future of all three. A single selected exponent uses the same ordinary integer $b$ on every arm. This uses the elementary exponential-parameter mechanism of [PR146, f431078244e868dc699fad011044f0d5e7f76437, GROWING_ADDITIVE_GAPS.md](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md).

For any ordinary component coloring $f$, the punctured right neighbors $f(2^j b+1)$ being eventually constant $R$ implies that $f(2^k b-1)=R$ on a subprogression of every exponent progression. In particular an eventual left punctured color different from an eventual right punctured color at the same center is impossible. The geometric center itself can still have $f(b)\ne R$. The argument does not exclude the single terminal boundary which compares the center to one punctured side.

For one direct finite check take $b=5$ and $k=51$ in $k=3\bmod4$. The pair $u_k,u_k+2$ meets at nine additional equal clocks with equal odd counts. The pair $2u_k,2u_k+3$ meets at 22 additional equal clocks with equal odd counts. The arithmetic-progression assertion above is proved by the residue argument, independently of this example.
