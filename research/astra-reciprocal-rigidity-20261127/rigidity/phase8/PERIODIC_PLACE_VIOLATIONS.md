# Positive upper density of violating ordinary vertices for locally constant corrections

Use the supersolution inequality, the nondecreasing unbounded radial term $g$, and the notation $u=n^2\exp[-g(\log_2 n)-P(n)-E(n)]$ of [the finite-place obstruction](ADELIC_HEIGHT_OBSTRUCTION.md). Suppose $P$ is a finite sum of locally constant functions on finitely many prime coordinates and full logarithmic valuations at finitely many fixed algebraic centers, none a positive rational integer. Finite-precision versions with cutoffs tending to infinity are allowed. Assume also
\[
                      \sum_{n\ge1}|E(n)|/n<\infty .                    \tag{1}
\]
Then
\[
    \limsup_{Y\to\infty}Y^{-1}\#\{n\le Y:u(Tn)<w(n)u(n)\}>0.         \tag{2}
\]
The same conclusion follows whenever $P$ takes one constant value at all sufficiently large diagonal integer points of some finite-place neighborhood of a particular expanding rational periodic point, as constructed below. The density lower bound can depend on the neighborhood. Formula (1) holds for $E=0$ and for $E(n)=O((\log n)^{-1-\delta})$.

## An expanding affine return away from the centers

Include 2 in the finite prime set $S$. For $h\ge4$ let $w=1^{h-1}0$ be a physical parity word. Its branch has form $F(x)=A x+B_0$, with $A=3^{h-1}/2^h>1$, $B_0>0$. Its unique real fixed point $z=-B_0/(A-1)$ is a negative rational, with denominator dividing $3^{h-1}-2^h$ before reduction: the affine numerator has integral coefficients after multiplication by $2^h$. The denominator is odd and prime to three. At each other $\ell\in S$ require $h$ to be a multiple of the multiplicative orders of both 2 and 3 modulo $\ell$. Then $2^h=1$, $3^{h-1}=3^{-1}$ modulo $\ell$, which are unequal for $\ell>3$. This makes $z$ integral at every place in $S$.

The infinite repeated word has a unique realizing element of $\mathbb Z_2$ by the finite parity bijection. Its image at clock $h$ has the same infinite parity sequence, so it is fixed by the branch, and it equals $z$. The word has least period $h$ because it has just one zero per period. Infinitely many admissible $h$ therefore give distinct rationals $z$. Choose one unequal to every prescribed logarithmic center (over any of its indicated prime embeddings). On a sufficiently small residue neighborhood of this diagonal $z$, all finite valuations $v_\ell(n-r)$ take their fixed value at $z$. The locally constant terms are constant there too. Every truncation budget tending to infinity eventually exceeds all these fixed valuations. Thus $P$ has one common value there at all sufficiently large integers.

Refine that neighborhood to one positive arithmetic progression $\mathcal A$ so every input follows $w$ for $h$ actual shortcut steps, and both input and endpoint are in the original neighborhood. At the binary place take $h$ extra digits beyond the requested precision. At the other finite places applying the fixed branch preserves the requested congruence, since each factor $1/2,3/2$ is integral there. The Chinese remainder theorem gives the progression. Thus for all sufficiently large $n\in\mathcal A$, its physical endpoint is $F(n)=A n+B_0$, and $P(F(n))=P(n)$. All intermediate maps are strictly increasing affine functions of $n$ on this progression, with fixed positive slopes and nonnegative offsets.

## Counting the same positive radial increase on an interval of inputs

Suppose the set of violating inputs has upper natural density zero. For any fixed $0<a<b<\infty$, all but $o(t)$ of the progression points in $[at,bt]$ avoid every violation through their $h$ departing sites, uniformly as $t\to\infty$. Indeed each intermediate map is injective and has height at most $C t$ there, and there are only $h$ such maps. Call the remaining sufficiently large progression points good.

Choose $A^{-1}<a<b<1$. Every sufficiently large real threshold $t$ has at least $c t$ good progression points in $[at,bt]$ with $n<t<F(n)$, where $c>0$ depends on the fixed choices. The sum of $1/n$ over these inputs is bounded below uniformly. On the other hand the exact endpoint identity and the edge inequalities along each good path give
\[
  0\le g(\log_2 F(n))-g(\log_2 n)
               \le O_h(1/n)+|E(n)|+|E(F(n))| .                         \tag{3}
\]
Here the true logarithmic correction is at most $2^h/(3n)$, and $g$ is nondecreasing. Multiplying (3) by $1/n$ and summing over good $n$ gives a finite result by (1). The last term also has finite sum since $F$ is injective on the progression and $F(n)\asymp n$.

To see the contradiction without a continuity convention for $g$, fix $1<d<A$. For each large integer $k$ take good inputs in $[a_0d^k,b_0d^k]$, with constants $d/A<a_0<b_0<1$. Choose $a_0,b_0$ close enough that $b_0<a_0 d$, so these input intervals are disjoint. Each group has harmonic weight at least $c'>0$ and each of its members has
\[
 n<d^k<d^{k+1}<F(n).
\]
Its contribution to the lower side of (3), after the harmonic weighting, is at least $c'[g(\log_2 d^{k+1})-g(\log_2 d^k)]$. These nonnegative lower bounds telescope to infinity. This contradicts the finite upper sum and proves (2).

This argument fixes one arithmetic progression for each proposed finite family of centers. Infinite or dense families can prevent exact cancellation of the local term on such a progression. The separate full-counting-exponent result treats finite measures with that feature.
