# Vanishing gated harmonic mass for long pieces with small signed rational witnesses

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) at positive odd integers. At a signed odd rational of odd reduced denominator the same formula is defined provided its numerator \(3x+1\) is nonzero. A piece of a finite exponent word is witnessed at height \(H\) when it is an exact consecutive prefix from some \(-p/q<0\), with \(p,q\) positive odd and at most \(H\). The witness may change at every cut and may itself be nonperiodic. Only the start of the witness must be negative.

Take the all-prefix gate \(4A_j\le7j\), where \(A_j\) is the cumulative division cost. For each admitted word \(w\) of \(n\) odd steps, let \(m(w)\) be the least positive ordinary seed in its exact dyadic cylinder. The original centered harmonic gate sums \(1/m(w)\). Its union \(D\) of all admitted least seeds satisfies
\[
         \#(D\cap[1,X])\ll X^d,\qquad d=H_2(4/7)<1.                 \tag{1}
\]
This is the stopped binary count in the [global prefix trace](GLOBAL_PREFIX_TRACE.md), with its harmless endpoint factor absorbed in the constant.

**Written selective estimate.** Fix \(\theta\ge0\) and \(c>0\) with \(\theta<\nu:=1-c\log(\log_2 3)\), using the natural logarithm outside the indicated base. At depth \(n\) restrict to words decomposable into at most \(c\log n\) witnessed pieces of heights at most \(H_n\le2^{n^\theta}\). Then their contribution to the actual harmonic gate is
\[
                   \sum_{w\ {\rm restricted}}\frac1{m(w)}
                        \ll \exp(-c_1 n^\nu)                         \tag{2}
\]
for large \(n\), with \(c_1>0\). Thus this part of the finite mass has zero limit without assuming Collatz or any conjectural mixing. The pieces are a restriction on the full prefix. The unrestricted gate mass has no such bound here.

Let a piece of \(t\) odd steps and division cost \(a\) start at the actual state \(x\). The cleared affine difference of the two matched trajectories gives
\[
               2^a \mid 3^t(qx+p),\qquad 2^a\le qx+p\le H(x+1).
                                                                         \tag{3}
\]
The first division is taken in ordinary integers, since the terminal rational denominator divides the original odd \(q\). The second uses coprimality and \(qx+p>0\). If \(R\) of the preceding true exponents are one, then \(x+1\le(3/2)^R(m+1)\), \(m=m(w)\): exponent one gives equality for shifted heights, while every exponent at least two makes the shifted height nonincreasing. Therefore, with \(\gamma=\log_2(3/2)\) and \(L=\log_2[H(m+1)]\), the cost \(a_i\) of piece \(i\) satisfies
\[
            a_i\le L+\gamma R_{i-1}.
\]
Putting \(S_i=\sum_{j\le i}a_j\), one has \(R_{i-1}\le S_{i-1}\) and hence \(S_i\le(1+\gamma)S_{i-1}+L\). With \(k\) pieces this forces
\[
        n\le S_k\le L\,\frac{(\log_2 3)^k-1}{\log_2(3/2)}.         \tag{4}
\]
Under the stated budgets \((\log_2 3)^k\le n^{1-\nu}\), so \(\log_2(m+1)\ge\gamma n^\nu-n^\theta\). At fixed depth the least seeds are distinct. Summing (1) over height octaves gives \(\sum_{m\in D,\ m>M}1/m\ll M^{d-1}\), proving (2). The full posterior or path weights are never changed to a probability on the witnesses.

A weighted version does not charge a piece's total cost equally in its height growth. Let \(r_i\) be its number of exponent-one steps and \(\lambda_i=r_i/a_i\). Then
\[
 S_k\le L\sum_{j=1}^k\prod_{i<j}(1+\gamma\lambda_i).                 \tag{5}
\]
Indeed \(L+\gamma R_i\le(1+\gamma\lambda_i)(L+\gamma R_{i-1})\). The same proof of (2) applies if the sum in (5) is \(O(n^{1-\nu})\), with \(\theta<\nu\). One long piece alone starting after \(R\) previous one-exponents already forces \(\log_2(m+1)\ge a-\gamma R-\log_2 H\). This gives selective decay without a complete partition if that lower bound tends to infinity sufficiently fast.

**The binary harmonic criterion.** Apply the same estimate directly to the [binary prefix criterion](../BINARY_PREFIX_CRITERION.md). Its true least positive residues \(m<2^N\) satisfy the all-prefix odd-count gates \(5j\le8g_j\), and their union over depths has harmonic tail \(O(M^{H_2(5/8)-1})\) for \(m>M\). A binary witness starts at a negative rational \(-p/q\), where \(q\) is odd and the numerator can have either parity. Its ordinary shortcut branches use the indicated parity. For a piece of length \(a\) with \(t\) odd departures, subtraction of the two binary affine iterations gives (3) verbatim. An even branch decreases the shifted height, and an odd branch multiplies it by \(3/2\). Thus (4) holds with \(S_k=N\) and \(R\) the number of earlier odd departures. Formula (5) also holds with \(r_i\) the number of odd departures in piece \(i\). Under either of the corresponding budgets the contribution of these actual retained residues to the root's finite sum \(H_N\) is \(O(\exp(-c_2 N^\nu))\). Positive ordinary witnesses matching themselves would invalidate the strict lower bound in (3). Signed witnesses enforce that strict bound. No bound on the mass of the complementary ordinary residues follows.

**A second source-qualified range for periodic dictionaries.** Weaver's adaptive-dictionary theorem charges the sum \(B\) of the full exponent totals of the dictionary words, each of which contains an exponent at least two. Strings of ones and arbitrary phases are handled by its prescribed piece-cost convention. It proves \(t+1\le \exp[K_*(k+1)/\log(k+2)](\log H(m/1)+B+1)\) up to the first step starting at 1 or on a represented rational cycle. Restrict the dictionary to one whose cycles contain no positive ordinary integer except possibly 1, as happens for growing periodic scripts with negative fixed points. In a gated prefix reaching 1 after \(h\le n\) odd steps, every subsequent exponent is two. Hence \(h+2(n-h)\le A_n\le7n/4\), so \(h\ge n/4\). Truncation to the first hit can only decrease the piece budget; a path not reaching 1 uses the original \(n\) steps. For each \(0\le\theta<1\), choose \(c>0\) small enough in terms of \(K_*,\theta\). Uniformly over adaptive dictionaries with \(B\le n^\theta\) and cost \(k\le c\log n\log\log n\), the source theorem gives \(\log(m+1)\gg n^{\nu'}\) with some \(\nu'>\theta\). Equation (1) again yields a stretched-exponential bound for this specified part of the finite harmonic mass. For instance choose \(v\) strictly between \(\theta\) and 1, then choose \(c\) so that the exponential in the theorem is at most \(n^{1-v}\) for sufficiently large \(n\). This application is distinct from the elementary unrestricted-anchor bound (2). Neither supplies a short description for an arbitrary ordinary survivor. [Weaver, Paper 15/v2, Theorem 9](https://rstation.ai/problems/collatz/papers/15/v2)

PR193's tilted Green comparison already uses divisibility of a signed affine gap when forward exponent words agree. Our power saving combines that arithmetic with the actual least-positive-seed tail (1). The [kernel interfaces](SignedPieceHeight.lean) check the cleared divisibility, shifted-height steps for both clocks, segment height bound and the lower cost before entering 1. The growth recurrence, population sum and use of the published dictionary theorem are written arguments. [PR193, tilted Green comparison](https://github.com/GettysburgResearch/collatz/blob/b69d47f7fc0a8c6c3f227b0afcaf69b28cc92845/research/astra-six-hour-20261127/global/TILTED_GREEN.md)

