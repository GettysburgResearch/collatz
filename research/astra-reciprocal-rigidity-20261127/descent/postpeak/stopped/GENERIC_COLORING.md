# A comparison for component cuts of positive density

There is a binary coloring \(c\) of the positive integers with both colors of natural density \(1/2\) such that
\[
 c(2n)=c(3n)=c(n)\quad(n\ge1),\qquad
 \#\{n\le X:c(n+1)\ne c(n)\}=o(X).
\]
Hence \(c(3n+2)=c(2n+1)\) also holds outside a set of ordinary density zero. These density and scaling properties alone cannot force a constant color. An actual Collatz component indicator has the exact affine identity \(c(2n+1)=c(3n+2)\) at every input. The construction proves zero **natural density** of the boundary; it supplies no upper-Banach-density assertion and does not exhibit distinct positive Collatz components. Compare the earlier essential-norm result for local operators on actual orbit components. [Local operator algebra](../../../rigidity/phase2/LOCAL_OPERATOR_ALGEBRA.md)

Konieczny previously constructed a binary sequence invariant under the adjacent shift almost everywhere and sign-reversing under both dilations almost everywhere, in his counterexample for asymptotic automaticity. The comparison here uses exact same-color dilation identities and gives equal natural color densities. [Konieczny, *An asymptotic version of Cobham’s theorem*, §4, Lemma 4.2](https://arxiv.org/abs/2209.09588)

## Balanced waves on logarithmic shells

Write \(\alpha=\log_2 3\), \(\mathbb T=\mathbb R/\mathbb Z\), and let \(\lambda\) denote normalized circle length. Take increasing integers \(q_k\to\infty\) so that \(q_{k+1}/q_k\) is odd and \(\|q_k\alpha\|\to0\), where \(\|\cdot\|\) is distance to an integer. Given \(q_k\), the odd multiples of \(q_k\alpha\) are dense on the circle, by irrationality; choose a larger such multiple sufficiently close to zero. Choose increasing integer stage starts \(J_k\), with \(J_1\ge4\), such that
\(J_{k+1}-J_k\to\infty\) and \(q_{k+1}/2^{J_k}\to0\), possible after choosing the frequencies.

Put \(f_q(u)=\mathbf1_{\{\{qu\}<1/2\}}\). At an integer shell index \(J_k\le j<J_{k+1}\), let \(s=(j-J_k)/(J_{k+1}-J_k)\) and define \(F_j(u)\) to be \(f_{q_{k+1}}(u)\) if \(\{2q_ku\}<s\), and \(f_{q_k}(u)\) otherwise. The finitely many earlier indices use \(f_1\). In the final six-free-core coloring below, this ensures \(c(7)=0\) and \(c(11)=1\): both numbers are six-free, \(7^2>2^5\), and \(11^2<2^7\). Since \(T(7)=11\), the exact affine Collatz identity fails at this explicit input.

1. Each mixed wave has period \(1/q_k\), with mean \(1/2\) on that period. Shifting by \(1/(2q_k)\) preserves the gate and reverses both binary waves, because the frequency ratio is odd.
2. It has \(O(q_{k+1})\) discontinuities. A shift by \(\alpha\) changes its value on circle measure
   \(O(\|q_k\alpha\|+\|q_{k+1}\alpha\|)=o(1)\). Mismatches can occur only when the gate or one of the two component waves changes; for an interval indicator evaluated at frequency \(q\), this has measure at most \(2\|q\alpha\|\), and the gate frequency is \(2q_k\).
3. Moving from \(j\) to \(j+1\) changes the wave on measure at most \(1/(J_{k+1}-J_k)\). Within the stage this is the interval of gate thresholds crossed in the move. At the final index compare with the same mixture at threshold one, which is exactly the next stage's initial wave. Thus any fixed bounded shift of shell indices costs \(o(1)\) in circle measure, including across stage transitions.

## Sampling the waves at integer points

For \(j=\lfloor\log_2 n\rfloor\), put \(d(n)=F_j(\{\log_2 n\})\). In a partial shell \(2^j\le n<2^{j+z}\), \(0\le z\le1\), the number of ones equals
\[
 2^j\int_0^z F_j(u)(\log2)\,2^u\,du+O(q_{k+1}).
\]
This follows by replacing each of the \(O(q_{k+1})\) constituent intervals by its length in the real \(n\)-coordinate, with at most a constant rounding error each. The primitive of \(F_j-1/2\) has magnitude \(O(1/q_k)\) by period balance. Integration by parts against the fixed smooth weight \((\log2)2^u\) therefore bounds the error from replacing \(F_j\) by \(1/2\) by \(O(1/q_k)\) inside the integral, uniformly in the partial endpoint \(z\). Each partial shell count differs from half its population by \(o(2^j)\). Summing completed shells geometrically and adding the final partial shell proves natural density \(1/2\). Within each shell, adjacent sampling points can switch color only across one of \(O(q_{k+1})\) discontinuities, plus a shell endpoint. Hence the adjacent boundary of \(d\) has natural density zero.

## Enforcing exact invariance under two and three

Write \(n=2^a3^b u\), \(\gcd(u,6)=1\), and put \(c(n)=d(u)\). Both multiplicative identities are exact.

We show \(c=d\) outside a set of density zero. Fix \(M\) and restrict first to \(a,b\le M\). In shell \(j\), the core's angle is the angle of \(n\) minus \(b\alpha\) on the circle. Its shell index is \(j-h\), with \(0\le h\le M+\lceil M\alpha\rceil\). For each possible \(b,h\), the mismatch set
\[
       \{v:F_j(v)\ne F_{j-h}(v-b\alpha)\}
\]
has \(\lambda\)-measure \(o_M(1)\) by the bounded number of rotations and shell shifts above. Its number of component intervals is \(O_M(q_{k+1})\), since the earlier shell has no larger frequencies. In the actual shell, ignoring the divisibility conditions only enlarges this union of possible mismatch sets. The same integer sampling estimate, with bounded smooth weight, gives \(o_M(2^j)+O_M(q_{k+1})=o_M(2^j)\) exceptions, also on partial shells. The unrestricted exceptional upper density is thus at most \(2^{-M}+3^{-M}\), by the tails of the two valuations. Let \(M\to\infty\).

Ordinary density and its adjacent zero-boundary conclusion now pass from \(d\) to \(c\): a shift by one of a density-zero exceptional set still has density zero. Finally, taking an affine subsequence \(an+b\) with fixed \(a>0\) preserves zero upper natural density of the exceptional inputs, by counting them in \([1,aX+|b|]\). Thus \(c(3n+2)\) agrees with \(c(3n)=c(n)\) for almost all \(n\), and \(c(2n+1)\) agrees with \(c(2n)=c(n)\) for almost all \(n\). The proof leaves the exact pointwise odd-branch identity as a separate arithmetic requirement.
