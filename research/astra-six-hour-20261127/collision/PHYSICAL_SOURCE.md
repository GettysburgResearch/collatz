# Summable cancellation from large physical source windows

**Status.** Proposed written theorem, conditional on the one-extra-digit
joint mixing stated below. The origin cutoff in this note is on actual
ordinary positive starts, before any affine or Markov approximation.
The claim supplements the finite-period propagation theorem, which uses
only the original, natural-depth mixing bound.

Use \(U,T,\sigma,s\) from [the depth-difference theorem](DEPTH_DIFFERENCE.md).
If \(X\ge2\), let \(I\) be any interval contained in \([X,2X]\); endpoints
may use either half-open convention with the integer boundary terms charged
below. Write \(s_I(x)={\bf1}_I(x)\sigma(x)/x\) on positive odd \(x\).
For \(1\le t\le(\log_2 X)/32\) and every fixed \(A>0\),
\[
                   \|T^t s_I\|_1\ll_A t^{-A}.                         \tag{1}
\]
There is no target cutoff in (1). All subsequent integer forward
transfers are contractions, so the same upper bound applies at every
odd clock at least \(t\).

## One extra ternary digit of the original word law

For a length-\(t\) word with total \(h\) write its forward affine action
as \(x\mapsto \lambda_h x+F\), \(\lambda_h=3^t2^{-h}\),
\(0<F<3^t\). Under the original iid geometric law each such word has
mass \(2^{-h}\); reversal preserves the joint distribution of the
stationary-order offset and the retained total. Put \(q=3^t,\ Q=3q\),
\[
 P_h(r)=\Pr(E_t=h,\ F=r\bmod Q),\qquad
 (MP_h)(r)=\tfrac13\sum_{r'=r\bmod q}P_h(r').
\]
The needed input is
\(\sum_h\|P_h-MP_h\|_{\ell^1(\mathbb Z/Q)}\ll_A t^{-A}\). This is
Weaver–Wren Theorem 6, equation (66), with word length \(N=t\), observation
depth \(t+1\) and coarse depth \(t\). Its hypothesis \(1\le\delta_A t\)
holds for large \(t\); the finite remainder is absorbed into the constant.
The norm is the sum norm of joint *probability masses*; no additional
power of three appears. Equations (65)–(66) are present in v1 and the
expanded v2. [Weaver and Wren, Paper 48, v1, §8, Theorem 6](https://rstation.ai/problems/collatz/papers/48/v1) · [v2, §8, Theorem 6](https://rstation.ai/problems/collatz/papers/48)

Choose first \(h\le4t\). Given positive odd output \(y\), a word
is legal exactly when \(F=y\bmod q\). Its unique odd positive source is
\(x=2^h(y-F)/q\), and its transported coefficient from \(1/x\) is
\(\lambda_h/y\). The sign is exactly
\(\sigma(x)=\sigma(2^h(y-F)/q\bmod3)\), which reads the extra ternary
digit. Replace the condition \(x\in I\) by \(y\in\lambda_h I\) for these
words only. If the filters disagree then \(x\) lies within \(2^h+1\)
of an endpoint of \(I\), since \(F/\lambda_h<2^h\). Across *all*
\(h\le4t\), discrepancies involve only \(O(2^{4t})\) positive integer
sources. Each actual source has exactly one word, output and clock at
depth \(t\), including the words newly admitted by the replacement.
The total error in the physical \(\ell^1\) norm is \(O(2^{4t}/X)\)
because each transport weight is at most \(1/x\) and these sources
are comparable to \(X\) (enlarge constants for bounded \(X\)).

The original filter's discarded totals \(h>4t\) have reciprocal mass
\(O(e^{-c t}+2^{4t}/X)\). Indeed deciding that more than \(4t\) native
steps are needed for \(t\) odd steps is a binary cylinder event visible
modulo \(2^{4t+1}\); for an odd uniform residue its probability is
\(\Pr(E_t>4t)\le[3(2/3)^4]^t\), using the geometric moment at \(3/2\).
Counting the complete periods and the remainder in the enclosing octave
adds at most \(O(2^{4t}/X)\). When the interval \(I\) is shorter than
the octave we only need its unnormalized reciprocal mass and may enlarge
to the octave for this bound.

The remaining signed coefficient at a positive odd \(y\) and fixed \(h\)
is, exactly,
\[
 \frac{q}{y}{\bf1}_{y\in\lambda_hI}\,
       B_h(y),\qquad
 B_h(y)=\sum_{j=0}^2 \sigma(2^hj\bmod3)\,P_h(y-jq\bmod Q).              \tag{2}
\]
As the three signs have mean zero, the formula is unchanged on replacing
\(P_h\) by \(P_h-MP_h\). Consequently
\(\sum_{r\bmod Q}|B_h(r)|\le 3\|P_h-MP_h\|_1\).
In \(\lambda_h I\subset[\lambda_h X,2\lambda_h X]\) there are at most
\(1+\lambda_h X/Q\) positive odd representatives of any one residue
(up to an immaterial endpoint constant). Since
\(\lambda_h X/Q=X/(3\cdot2^h)\gg1\), summing \(q|B_h(y)|/y\) over
these actual positive targets costs at most a constant times
\(\|P_h-MP_h\|_1\). Sum over \(h\le4t\), then add the two errors. Our
choice of \(t\) makes \(2^{4t}/X\le X^{-7/8}\). This proves (1).

The cancellation is stronger than pairing each \(x=2\bmod3\) with its
negative sibling \(4x+1\). More explicitly, if \(a\) is the least odd
parent of a unit \(y\) and its gap is \(e_0\in\{1,2\}\), all the parents
have form \(a_j=4^ja+(4^j-1)/3\). Their signs are
\(\sigma(a+j\bmod3)\), with relative transported weights \(4^{-j}\).
Thus their total in \(Ts(y)\), in units of \(3\cdot2^{-e_0}/y\), is
\(-20/21,4/21,16/21\) when \(a=0,1,2\bmod3\), respectively. One
sibling cancels a quarter of the leading positive weight in the last
case. These one-step numbers by themselves give no repeated uniform
contraction along a moving target.

## Physical truncation and grade charges

At \(q_k=3^{k+1}\), with \(R\ge2\), (1) implies
\[
 \limsup_{k\to\infty}
 \left\|{\bf1}_{y<2q_k} T^k\bigl(s{\bf1}_{x\ge R}\bigr)\right\|_1
       \ll_A (1+\log R)^{-A}.                                         \tag{3}
\]
To verify summability, partition \([R,\infty)\) into dyadic octaves,
using a partial first octave if necessary. When \(x\asymp2^j\) and
\(j\le16k\), take \(t=\lfloor j/32\rfloor\le k\). The cost at time \(k\)
is \(O_B((1+j)^{-B})\), allowing finitely many small \(j\) by
contraction. For \(j>16k\), arrival at \(y<2q_k\) forces \(2^{E_k}>x/6\)
from \(U^k x\ge3^k x2^{-E_k}\). On the octave the event forces
\(E_k>\lfloor j/2\rfloor\), apart from bounded \(j\). It can be read
on the first \(\lfloor j/2\rfloor+1\) binary digits. Its odd-uniform
probability is \(O(3^k(2/3)^{j/2})=O(e^{-c j})\), and the incomplete
period costs \(O(2^{-j/2})\). This upper-bounds the unnormalized
reciprocal mass there, even without cancellation. Summation with
\(B>A+1\) proves (3). All sums at a fixed output are absolutely
convergent, as explained in equation (1) of the preceding note.

For each escaping component and signed grade define the finite-source
array
\[
 B_R(C,v)=\sum_{\substack{x<R,\ x\in C\\g_C(x)=v}}
                             \frac{\sigma(x)}{P(x)} .
\]
With \(\Delta_{C,v}=Z_{C,v-1}-Z_{C,v}\) from the preceding note, one has
\[
 \sum_{C,v}|B_R(C,v)-\Delta_{C,v}|\ll_A (1+\log R)^{-A}.               \tag{4}
\]
Indeed, at fixed \(R\) the restricted starts split into finitely many
ordinary trajectories; the eventually periodic ones lose all mass.
The others give the moving placement of \(B_R\) in the physical norm
as \(k\to\infty\). They lie within the period at all sufficiently large
depths. Subtract the full moving placement from equation (4) of
[the depth-difference theorem](DEPTH_DIFFERENCE.md) and apply (3).
Equivalently at a single grade the untruncated signed series converges
absolutely by \(\sum_{g_C(x)=v}1/P(x)<\infty\), and the one-step inverse
identity gives its sum \(\Delta_{C,v}\).

Thus in particular
\[
 \sum_C\left|H_C-
       \sum_{\substack{x<R,\ x\in C}}\frac{\sigma(x)}{P(x)}\right|
                 \ll_A(1+\log R)^{-A}.                                \tag{5}
\]
This is a rapidly convergent *height-ordered* signed charge. It is not
the absolute sum of the individual \(1/P(x)\) over all component grades.
The unrestricted source \(1/x\) has infinite harmonic mass. Reindexing
\((T-I)(1/x)\) on the entire basin as a formally summable coboundary
would discard its boundary charge \(H_C\). The estimates control the
large physical source windows. They do not prove cancellation of the
finite signed charges in (4) on an escaping component.
