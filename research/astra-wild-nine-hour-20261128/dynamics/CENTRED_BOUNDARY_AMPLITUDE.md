# The centred height at the positive cycle and its complete ordinary range

**PROPOSED written theorem.** Let \(T\) be the positive shortcut map. Write \(q_t(n)\) for the number of odd departures up to physical date \(t\), and define
\[
       W_t(n)=\frac{2^{t-2q_t(n)}T^t(n)}n .
\]
The limit \(W(n)\) exists for every positive integer. It is positive exactly when \(n\) reaches 1. The positive values at odd ternary units form a countable set \(V\subset(0,1]\). Its closure in the real line has the exact disjoint decomposition
\[
   K=\overline V=\{0\}\ \sqcup\ \bigsqcup_{h=0}^\infty (3/4)^h V.       \tag{1}
\]
For every nonnegative integer \(j\), its \(j\)-th Cantor–Bendixson derivative, obtained by repeatedly retaining only real accumulation points, is
\[
    K^{(j)}=\{0\}\ \sqcup\ \bigsqcup_{h\ge j}(3/4)^h V .
                                                                         \tag{2}
\]
The intersection of these derivatives is \(\{0\}\), whose derivative is empty. Every point of positive real value in \(K\) is rational. Its exact derivative rank is the exponent of 3 in its reduced rational value. Every nonzero value of \(W\) at an odd ternary unit is isolated in \(K\). Its reduced denominator has odd part equal to the entire starting unit.

For a fixed physical source cylinder \(n\equiv r\bmod 2^k\) with \(q=q_k(r)\ge1\), the set of all real limits of \(W(n_i)\) for \(n_i\to\infty\) in the cylinder is exactly \(K^{(q)}\). The limsup there is \((3/4)^q\). The positive limits arise from genuine trajectories to 1, even if there are additional positive components. Zero is a limit of genuine positive amplitudes too.

## The positive boundary and a uniform approximation

One even departure leaves \(W_t\) unchanged. At an odd departure \(x=T^t n\) its multiplier is \((3x+1)/(4x)\), equal to one at 1 and at most \(5/6\) at every odd \(x\ge3\). The sequence is decreasing and nonnegative. A positive integer trajectory has infinitely many odd departures, because a run of even divisions from any fixed positive integer is finite. On a path missing 1 the limit is therefore zero. If the path first hits 1 at date \(t\), the later departures in the cycle preserve the value and
\[
                         W(n)=2^{t-2q_t(n)}/n.                         \tag{3}
\]
In particular \(W(1)=1\). Stopping after \(p\) odd departures approximates \(W(n)\) with absolute error at most \((5/6)^p\), uniformly in the positive source. If it has already hit 1 the error is zero; otherwise both the limit and the current product are between zero and the displayed upper bound. For odd \(n\) with a positive amplitude, reducing the dyadic rational factor in (3) cannot cancel any odd factor of \(n\). Thus the odd part of the denominator is exactly \(n\), and \(v_3(W(n))=0\) on the unit sources. This arithmetic fact proves disjointness of the positive layers in (1).

Previous fixed-source reciprocal traces normalize by \(3^p2^{-S_p}\) along odd clocks, where \(S_p\) is total divisions. Their product can survive on escaping trajectories and vanishes on positive cycles. The present factor \(2^{S_p-2p}\) uses the mean-two cycle at the specified ordinary root 1. This is the source of both the uniform contraction before that hit and the dyadic numerator in (3). The mean-two continuation on this cycle is also used in PR218's harmonic first-exit calendar. [PR215, fixed-source product conventions](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/escape/phase8/TILTED_ORDINARY_REPRESENTATIVE.md) · [PR218, first-hit calendar](https://github.com/GettysburgResearch/collatz/blob/5b2a3fab71fc5c4116839240495e2ba49765b8c3/research/astra-full-proof-20261128/mass/RECORD_FLUX.md)

## Positive accumulation points of the actual odd-unit values

Write \(U(x)=(3x+1)/2^{v_2(3x+1)}\) at odd positive \(x\). Every output of \(U\) is a ternary unit. If \(a_i\) are odd units with distinct positive values \(W(a_i)\) tending to \(w>0\), their first-hit odd depths are bounded by the contraction estimate. After taking a subsequence the depth is a fixed \(p\), and \(a_i\to\infty\). At each of the finitely many indices \(0\le j\le p\), take a further subsequence on which \(U^j(a_i)\) either tends to infinity or is a fixed integer. Once a state is fixed its entire future is fixed. At index \(p\) the state is 1. Hence for some \(1\le h\le p\) the first \(h\) odd states tend to infinity and the next is a fixed odd unit \(a\) reaching 1. Their multiplier product tends to \((3/4)^h\), so \(w=(3/4)^hW(a)\).

Conversely, fix \(a\) as above and \(h\ge1\). There are arbitrarily large positive exponents \(e\) for which \(x=(2^ea-1)/3\) is an odd ternary unit. In fact the powers of two cycle through all six units modulo nine; choose \(2^ea\equiv4\) or \(7\bmod9\). From each such \(x\) attach a further \(h-1\) unit inverse odd edges, using exponents in \([3,8]\) and the same modulo-nine fact at each step. All these heights tend to infinity with \(e\), and their true forward words reach \(a\). The distinct starting odd units can be chosen increasing; (3) ensures their amplitudes are distinct. The \(h\) new multipliers tend to \(3/4\), realizing \((3/4)^hW(a)\) as a limit of \(V\). Finally there is an infinite unit inverse ray growing from 1 using exponents in \([3,8]\) and avoiding its self-loop. Every edge increases its parent, and its amplitudes at depth \(j\) are at most \((5/6)^j\). They tend to zero. These facts give \(V'=\{0\}\cup\bigcup_{h\ge1}(3/4)^h V\).

To take the next derivative of any of the unions in (2), a positive limiting point can involve only boundedly many indices \(h\), since every layer lies below \((3/4)^h\). Pass to a subsequence of constant \(h\), then use the just-proved description of \(V'\) and scale it by \((3/4)^h\). Conversely each point of the next positive layer is a limit from the preceding layer. Zero remains a limit at every finite index, already using \((3/4)^hW(1)\to0\). This proves (1) and (2), including the rank of zero.

## Complete cluster set on a prescribed binary cylinder

For fixed \(r,k\) and \(n_i\to\infty\) in its cylinder, all true states through physical time \(k\) tend to infinity, since \(T^j n_i\ge n_i2^{-j}\). The first \(q\) odd multipliers therefore contribute a factor tending to \((3/4)^q\). If \(q\ge1\), the odd part of the state at date \(k\) is a ternary unit. Its amplitude is zero or belongs to \(V\), because even divisions preserve amplitude. Thus every limit belongs to \((3/4)^q K=K^{(q)}\).

For the reverse inclusion choose \(h\ge q\) and append \(h-q\) odd bits to the original physical prefix. Each extra bit is possible on one lifted binary cylinder, by the odd affine slope after the previous prefix. Denote the new length by \(t\), its least nonnegative compatible input by \(r'\), and its true endpoint by \(v\). The standard prefix identity is
\[
                    T^t(r'+2^t b)=v+3^h b\quad (b\ge0).               \tag{4}
\]
Here \(v\) is a ternary unit because at least one odd step has occurred. For any positive odd unit \(a\) reaching 1, choose arbitrarily large \(e\) such that \(2^e a\equiv v\bmod3^h\). Two generates the unit group modulo \(3^h\): its order modulo three is two, and \(v_3(4^{3^j}-1)=j+1\) by induction by cubing. Take \(b=(2^ea-v)/3^h\) and then the original input given by (4). Every state in the fixed prefix tends to infinity, while the terminal value undergoes pure even divisions to \(a\). The limit is exactly \((3/4)^hW(a)\). Zero follows by a diagonal choice with \(h\to\infty\). This proof also gives the limsup, since one may take \(h=q,a=1\) and no amplitude exceeds one. The elementary powers-of-two routing and native affine prefix identity are previous arithmetic inputs. [PR215, pointwise congruence](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/POINTWISE_CONGRUENCE.md) · [PR215, native counted cylinder lifting](https://github.com/GettysburgResearch/collatz/blob/4f33ecc2de6f0ccf605a68c28da5abea0348e47b/research/astra-nine-hour-20261128/machinery/phase2/COUNTED_BLOCKS_AND_PROGRESSIONS.md)

## Effective positive-rational membership and detection of finite paths

Membership of any **specified positive rational** \(u\) in \(K\) is decidable unconditionally. Calculate \(h=v_3(u)\) and reject a negative rank. Reduce \(v=(4/3)^h u\). Its numerator must be a power of two, its odd denominator part \(a\) must be a ternary unit, and \(v\le1\). Choose \(P\) so \((5/6)^P<v\) and run the true odd path of \(a\) for at most \(P\) departures. If it has still missed 1, its amplitude is below \(v\), even if the path later succeeds. Otherwise calculate (3) exactly and compare. By the rank and reduced denominator classification this is a decision for the entire infinite compact set. It does not decide whether *some* dyadic numerator occurs at a specified denominator as those candidate values decrease to zero.

The range even detects prescribed ordinary paths near each positive higher-rank value. For fixed \(a\) an odd unit with \(W(a)>0\), and \(h\ge1\), there is an open interval about \((3/4)^h W(a)\) such that every positive-amplitude odd unit \(x\) with value in that interval has \(U^h x=a\). To see this, a contrary sequence must have distinct unbounded sources; its limit has positive rank and cannot equal any one source amplitude. Apply the bounded-depth subsequence argument. The number of initial odd states tending to infinity is exactly \(h\) by the ternary valuation of the limit, and the next fixed state is exactly \(a\) by the reduced odd denominator. This contradicts failure of the claimed finite path. In particular, approximating a positive-rank point by genuine predecessors of 1 at sufficiently fine resolution already supplies a path through the ordinary denominator being tested.

## The ordinary denominator problem

For an odd unit \(a\) outside the basin of 1, its own value would be zero while the odd denominator \(a\) would be absent from *every positive layer* of \(K\). Multiplication by \((3/4)^h\) preserves the unit odd denominator. Conversely its appearance at any positive rank forces membership of that very integer in the basin by (3) and uniqueness of the reduced odd denominator. This identifies exactly what information a proof through the full range must supply. The derivative theorem determines every rank and the actual maximum in every nontrivial binary cylinder. Zero is nevertheless a genuine accumulation point of convergent odd units, even if all positive integers converge. The question which unit denominators occur among the isolated values remains open.
