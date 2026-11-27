# A pointwise deficit from maximal Syracuse growth

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers. For the first \(d\) odd departures from \(x=x_0\), write \(x_i=U^i(x)\), \(e_i=v_2(3x_{i-1}+1)\), and \(J_d=\#\{1\le i\le d:e_i\ge2\}\). All constants below are independent of the ordinary source and the depth once their displayed parameters are fixed. For every \(M>0\) there is \(C_M\) such that
\[
 2^{-J_d}\le C_M\left(1+\frac d{\log_2(x+1)}\right)^{-M}. \tag{1}
\]
In particular \(J_d/\log d\to\infty\) along **every** fixed positive odd source. The same result gives
\[
 U^d(x)+1\le C_M (x+1)(3/2)^d
              \left(1+\frac d{\log_2(x+1)}\right)^{-M}. \tag{2}
\]
Weaver's earlier rise-group theorem gives the stronger \(J_d\gg\log(d/H)\log\log(d/H)\) when \(H=\log_2(x+1)\) and \(d/H\) is large, by splitting at \(J_d=d/2\). The fixed-number-of-rises concentration in the same paper also yields the coefficient-one height budget below. We give a shorter proof of the weaker all-powers conclusion to isolate the positive-coordinate input in the tilted height estimate. [Weaver, Paper 174, Theorems 1–2](https://rstation.ai/problems/collatz/papers/174/v1) · [Tilted height application](TILTED_HEIGHT.md).

The estimates use Evertse's ineffective \(S\)-adic sum inequality in fixed dimension. They allow growth exponential in \(d\), and provide no positive lower bound on \(J_d/d\).

## A fixed number of complete ascent blocks

At a positive odd block start write \(x_i+1=2^{a_i}u_i\), where \(u_i\) is odd and \(a_i\ge1\). Indices in this section enumerate blocks, starting at 1, independently of the individual-step indices above. The first \(a_i-1\) odd departures have valuation one. Their completed endpoint plus one equals \(2\cdot3^{a_i-1}u_i\). The next odd departure has valuation \(b_i+1\), where \(b_i=v_2(3^{a_i}u_i-1)\ge1\). Thus the block has \(a_i\) odd departures, and the next block satisfies
\[
 x_{i+1}=\frac{3^{a_i}u_i-1}{2^{b_i}},\qquad
 2^{a_{i+1}+b_i}u_{i+1}=3^{a_i}u_i+(2^{b_i}-1). \tag{3}
\]
These are the usual valuation-one run identities. In particular \(b_i\) is the **extra** valuation at its exit. [Steiner's circuits and their run formula](https://wildducktheories.github.io/collatz/papers/33-architecture/33-architecture.pdf).

For every fixed integer \(h\ge1\) and \(\eta>0\),
\[
 \sum_{i=1}^h a_i\le (1+\eta)\log_2(x_1+1)+C_{h,\eta}. \tag{4}
\]
For \(h=1\) this follows directly from \(2^{a_1}\mid x_1+1\). For \(h\ge2\), put \(A_{r:s}=\sum_{i=r}^{s}a_i\), with empty sums zero, \(D_j=\sum_{i=1}^j(a_{i+1}+b_i)\), \(D_0=0\), and \(B=\sum_{i<h}b_i\). Iterating the positive identity (3) gives
\[
 2^{D_{h-1}}u_h=V_0+\cdots+V_{h-1},\quad
 V_0=3^{A_{1:h-1}}u_1,\quad
 V_j=3^{A_{j+1:h-1}}2^{D_{j-1}}(2^{b_j}-1)\quad(1\le j<h). \tag{5}
\]
Every summand is a positive integer, and \(V_0\) is odd. In particular every nonempty subsum is nonzero.

We use Evertse's Theorem 2 for \(K=\mathbb Q\), \(S=\{\infty,2,3\}\) and \(T=\{2\}\). In this normalization, for an integer vector \(V\) of fixed length \(h\) with all nonempty subsums nonzero, and any \(\epsilon>0\),
\[
 \left(\prod_{j<h}|V_j|_\infty |V_j|_2 |V_j|_3\right)
   \left|\sum_{j<h}V_j\right|_2
 \ \ge c_{h,\epsilon}\max_j|V_j|_2\,\|V\|_\infty^{-\epsilon}. \tag{6}
\]
This theorem applies to arbitrary integral coordinates. It does not require the \(u_i\) or the \(2^{b_i}-1\) to be \(S\)-units. [J.-H. Evertse, *On sums of S-units and linear recurrences*, Compositio Math. 53 (1984), Theorem 2, p. 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf).

Here \(|n|_\infty|n|_2|n|_3\) is the factor of \(n>0\) left after stripping all factors of two and three. Its product over the \(V_j\)'s is at most \(u_1\prod_{j<h,\ j\ge1}(2^{b_j}-1)\le u_1 2^B\). Also \(\max_j|V_j|_2=1\) and, by (5), the two-adic absolute value of the sum is exactly \(2^{-D_{h-1}}=2^{-A_{2:h}-B}\). Consequently
\[
 2^{A_{2:h}}\le c_{h,\epsilon}^{-1}u_1\|V\|_\infty^\epsilon. \tag{7}
\]
In particular the size of a large exit valuation has canceled from the valuation product.

For the archimedean bound, every positive odd step satisfies \(U(v)+1\le(3/2)(v+1)\). Hence \(x_{i+1}+1\le(x_i+1)^L\), \(L=\log_2 3\), since \(a_i\le\log_2(x_i+1)\). Also \(b_i\le\log_2(3^{a_i}u_i)\le L\log_2(x_i+1)\). Thus for each fixed \(h\) every exponent in (5) is \(O_h(\log(x_1+1))\), giving \(\|V\|_\infty\le(x_1+1)^{C_h}\). Choose \(\epsilon\) so that \(C_h\epsilon\le\eta\), multiply (7) by \(2^{a_1}\), and use \(2^{a_1}u_1=x_1+1\). This proves (4).

## From a finite block bound to every positive source

Fix \(h\) and use (4) with, for instance, \(\eta=1\), including all block counts \(1,\ldots,h\) by taking the maximum of their constants. Partition a prefix of \(d\) odd departures into groups of \(h\) complete blocks and a final group. If the last block is unfinished, count its remaining observed run as at most its full \(a_i\). Equation (4) for this last group uses only the intervening exits and is valid even if the last exit is outside the prefix. Empty groups may be omitted. The number \(q\) of groups is at most \(J_d/h+1\). If \(t\) denotes the number of odd departures elapsed before one group, then \(\log_2(x_t+1)\le\log_2(x+1)+t\log_2(3/2)\). Therefore successive group endpoints satisfy
\[
 t_{\rm next}\le L_* t +2\log_2(x+1)+C_h,\qquad
 L_*=1+2\log_2(3/2)>1 .
\]
Since \(\log_2(x+1)\ge1\), iterating from zero yields
\[
 1+d/\log_2(x+1)\le K_h L_*^{J_d/h}.
\]
For prescribed \(M\), choose \(h\) so that \(M\log L_*/h\le\log2\); the preceding inequality gives (1). The dimensions and constants depend on \(M\). The proof does not let \(h\) grow inside a single instance of (6).

At a valuation-one departure \(U(v)+1=(3/2)(v+1)\). At every departure with valuation at least two,
\[
 (U(v)+1)/[(3/2)(v+1)]\le (3v+5)/(6(v+1))\le2/3 .
\]
Thus \(U^d(x)+1\le(x+1)(3/2)^d(2/3)^{J_d}\). Taking a larger \(M\) in (1) yields (2), including repeated or periodic orbits. The exact affine multiplier \(\omega_d=3^d2^{-\sum e_i}\) also obeys
\[
 \omega_d\le C_M(3/2)^d(1+d/\log_2(x+1))^{-M}, \tag{8}
\]
since \(\sum e_i-d\ge J_d\). No assumption on the minimum state, predecessor densities or convergence is used.

The finite ascent-block and summand identities are arithmetic. The pointwise asymptotic and its constants rely on the external theorem (6); they are not a Lean reconstruction of Evertse's theorem.
