# A three-odd upper certificate and its remaining Mersenne exponent

For \(m\ge0\), set \(a=98+162m\) and
\[
 z=(2^{a+9}-527)/81,\qquad M_j=2^j-1.
\]
The congruences \(2^{103}\equiv119\pmod {243}\) and
\(2^{162}\equiv1\pmod {243}\) give \(z\equiv17\pmod {48}\).
Both are direct finite modular calculations. After the first two odd moves,
the triple is at \(2^7(2^a-1)/3\). Seven halvings and one odd move send
it to \(2^{a-1}\). Thus its upper certificate uses three odd moves.

The signed rational trace starting at \(-527/81\) is
\[
 -527/81,-250/27,-125/27,-58/9,-29/9,-13/3,-6,-3,-4,-2,-1 .
\]
The difference from the positive start is \(2^{a+9}/81\), so the same ten
parities apply. Each odd move multiplies the difference by \(3/2\), and
each even move halves it. Five odd moves give the positive endpoint
\(3\cdot2^{a-1}-1=T(M_a)\). These are identities between ordinary
positive orbit values. In particular, \(z\) is in the basin exactly when
\(M_a\) is in it. PR146's earlier forward binary rank-three result gives a
separate transfer for Mersenne numbers in `RANK_THREE_MERSENNE.md` at
`f431078244e868dc699fad011044f0d5e7f76437`.

Suppose this \(z\) is the globally least reverse defect, and take the least
\(j\le a\) with \(M_j\) outside the basin. The quantitative directed return
of `RANK_TWO_DESCENT.md` rules out \(j\le a-43\), because a witness then has
height at most \(2^{40}M_j<z\). Thus \(r=a-j\) is one of 0 through 42.
Every earlier positive Mersenne number is in the basin. In particular,
\(3M_j\) is also in it. Three steps reach \(9\cdot2^{j-3}-1\), and
\(j-3\) further odd moves reach \(3^{j-1}-1=T^{j-1}(M_{j-1})\).

## Forty direct returns below the hypothetical minimum

The literal paths in `MersenneReturnPaths.json` work on complete ordinary
source progressions \(x=ut+v\) containing \(M_j\). In each case, \(u\)
is a power of two times 243, \(x\equiv-1\) modulo the binary factor, and
\(x+1\equiv2^{98-r}\pmod {243}\). Every edge is an ordinary shortcut,
an ordinary inverse edge, or the directed comparison \(w\longrightarrow3w\)
at \(w\equiv17\pmod {48}\). The word letters `h,d,s,i,q` mean halving,
doubling, odd shortcut, odd inverse and directed comparison.

At each query row \(w=ct+d\) the verifier checks
\[
 81c\le512\cdot2^r u,\qquad
 81d<512\cdot2^r(v+1)-527.
\]
These two comparisons guarantee \(w<z\) at the actual source, including its
affine constants. The endpoints are \(3M_j\) or an earlier \(M_{j-i}\).
Consequently each such path would pass from nonbasin to basin at a reverse
defect strictly below \(z\). The 40 complete offsets cover every \(r\)
except 0, 1 and 2. They contain 80 directed query positions in total.
`check_mersenne_returns.py` replays positivity, divisibility, edge direction,
endpoint identity and query heights. The kernel theorem
`MersenneReturnKernel.forty_returns` consumes the original directed
`runSound` theorem. It checks all 40 source progressions, the induction that
places every original Mersenne exponent in its progression, the literal
expanded words, each strict height bound and all resulting endpoints.

## Two further offsets fall by ordinary merger alone

For even \(j\ge2\) set \(u=(3^{j-1}-1)/2\), which is odd. The point
\(M_{j-1}\) reaches \(3^{j-1}-1\), then \(u\), then \((3u+1)/2\).
The point \(M_j\) reaches \(3^j-1=2(3u+1)\); two halvings reach
the same \((3u+1)/2\). Thus a first bad Mersenne exponent is odd.
Because \(a\) is even, this excludes \(r=0,2\).

These arguments leave only \(j=a-1=97+162m\). On this residual class,
the ordinary word `didddidi` from \(M_j\) reaches the admissible smaller
query \(w=(256\cdot2^j-341)/27\). The upper ray from \(3w\) reaches
\(27\cdot2^{j-1}-17\) in nine native steps. A full 11-step turn in the
signed cycle through \(-17\) has multiplier \(3^7/2^{11}>1\).
The ordinary source construction, its complete three-odd certificate and
its lower basin equivalence are kernel-checked in `RankThreeFamily.lean`.
The actual-basin corollary `CollatzMersenneFirstBad.exact_first_bad` in
`MersenneFirstBad.lean` consumes the 40 paths and the independent ordinary
even-exponent merger from `MersenneParity.lean`. Its bound on return from
an arbitrary nonbasin endpoint is explicit in the statement.
This finite calculation does not classify all possible returns at that
offset. It also does not cover all sources with three upper odd steps.
