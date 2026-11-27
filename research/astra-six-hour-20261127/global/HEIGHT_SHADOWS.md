# A target-height clock for thick and sparse shadow exclusion

Let \(a_i=U^i(a)\) escape through positive odd integers, set \(H_i=\log_2(a_i+1)\), and put \(r=\log_2(3/2)\). Fix \(\delta>0\), \(J,D\ge1\), \(K>0\) and \(0\le\gamma<1/r\). All sufficiently late starting dates \(n\) have a block of \(J\) dates finishing within \(O(H_n)\) subsequent odd steps on which both statements below hold at every date \(i\).

1. The distance from \(a_i\) to every nonzero multiple of \(3^{\lfloor\delta H_i\rfloor}\) exceeds \(2^{\eta H_i}\), for some \(\eta>0\).
2. The residue of \(a_i\) at that modulus has no representative which is a sum of at most \(D\) signed binary powers, with exponents in \([-\gamma H_i,KH_i]\).

There is a separate version which imposes statement 1 and excludes all sums of at most \(D\) **positive** terms \(2^m3^b\) with \(-\gamma H_i\le m\le KH_i\) and \(0\le b\le\kappa H_i\), for some \(\kappa>0\) depending on the other parameters. The constants may depend on the fixed source and parameters. The ternary modulus is between constant multiples of \((a_i+1)^{\delta\log_2 3}\), even for an arbitrarily slowly escaping ray. This replaces the precision proportional to the elapsed clock in [Sparse shadows](SPARSE_SHADOWS.md). The zero multiple is explicitly omitted from statement 1.

## Comparisons at consecutive near hits

Call a date marked if at least one of the two tested shadow types occurs; use the specified alternative when testing positive mixed terms. Choose one representative \(c_i\) for each mark. For a thick hit let \(c_i\) be the small integral residual, so \(a_i-c_i\ne0\). For any marked date
\[
 |a_i-c_i|\le 2^{C_0H_i}\quad\hbox{and}\quad v_2(a_i-c_i)\ge-\gamma H_i
\]
with the valuation statement interpreted as usual at zero. Choose \(C_0\ge2\) depending only on \(D,K\), for all sufficiently large \(H_i\); it can be chosen independently of \(\eta,\kappa\) when first restricting \(0<\eta,\kappa\le1\). One can use \(C_0=4+K+\log_2(D+1)\).

Consider consecutive marked dates \(i<j\) with \(j-i\le J\). We have \(H_j\le H_i+rJ\). Choose a constant \(c\in(0,1)\) below. If \(H_j\ge cH_i\), both ternary precisions are at least \(\delta cH_i-O(1)\). Let \(S_l\) be the total divisions after \(l\) steps from \(a_i\), and \(d=j-i\). Since \(2^{S_d}\le4^d a_i/a_j\), every exponent in the bridge
\[
        2^{S_d}c_j-3^dc_i-\sum_{l=0}^{d-1}3^{d-1-l}2^{S_l}                \tag{1}
\]
has binary magnitude \(O(H_i)\) after expansion. It is divisible by \(3^{\lfloor\delta c H_i\rfloor-O(1)}\). In the signed binary version the [moving-coefficient valuation estimate](SPARSE_SHADOWS.md) applied at scale \(\lceil H_i\rceil\) implies (1) is exactly zero, upon choosing the thick exponent \(\eta\) sufficiently small. In the positive mixed version choose first \(0<\kappa<\min(1,\delta c/4)\); all ternary exponents in (1) are then at most \(\delta c H_i/2\) eventually. The group-by-slope valuation argument in [Positive S-unit shadows](POSITIVE_SUNIT_SHADOWS.md) still applies with the thick coefficients of size \(2^{\eta O(H_i)}\), for a sufficiently small \(\eta\). Indeed failure for every \(\eta\) would give a sequence with coefficient logarithms \(o(H_i)\), to which the same grouping proof applies. Subtract (1) from the actual word equation to get exact homogeneous transport of the residuals. The conclusion requires both endpoints to be comparable in logarithmic height; the next argument pays for the other transitions.

## Duration and height of an exactly transported chain

Partition consecutive marks having gaps at most \(J\) into chains, ending a chain just before a step with \(H_j<cH_i\). Throughout a late chain its residuals are all zero or all nonzero. In the nonzero case telescope from the first date \(i\) through its last date \(t\) and take binary valuations. Every physical gap is at least one, so
\[
    t-i \le v_2(a_i-c_i)-v_2(a_t-c_t)
         \le C_0H_i+\gamma H_t,
    \qquad H_t\le H_i+r(t-i).
\]
The upper valuation bound on the initial nonzero dyadic rational follows from its ordinary absolute value. Consequently
\[
                    t-i \le \frac{C_0+\gamma}{1-r\gamma}H_i .              \tag{2}
\]

If all residuals are zero, thick witnesses never occur. In the signed binary case the actual mantissas then lie in the compact null signed-digit set at every mark. The irrational rotation argument in [Sparse shadows](SPARSE_SHADOWS.md) bounds the duration of such a chain by a fixed constant. In the positive mixed case, the positive subsum persistence proof in [Positive S-unit shadows](POSITIVE_SUNIT_SHADOWS.md) applies to each finite chain. Its first large subsum is \(V=2^{A_i}3^{-i}v\) with \(0<v\le a_i\) a dyadic rational, where \(A_i\) is the entire clock from the source. Thus \(v_2(V)\le A_i+H_i\); positivity and the dyadic denominator of \(v\) suffice. At the last date \(t\), all atoms in this same subsum have binary valuation at least \(A_t-\gamma H_t\). It follows that \(t-i\le H_i+\gamma H_t\), which also implies (2). On every sufficiently late chain we now have \(t-i\le C H_i\) for a fixed \(C\) independent of \(c,\eta,\kappa\). Enlarge \(C\) if necessary in the bounded-duration signed case.

## A drop between chains lowers the next starting height

Take \(c<1/[2(1+rC)]\), then choose the exponents above. If a chain beginning at \(i\) ends at \(t\) in a drop to the next marked date \(j\), then
\[
                 H_j<cH_t\le c(1+rC)H_i<H_i/2.                            \tag{3}
\]
Thus the logarithmic starting heights of subsequent chains at least halve. No infinite sequence of such chains can continue, since \(H_i\ge1\). The total time spent inside them is at most twice a constant times the first starting height by (2). Each intervening drop costs at most \(J\) steps and the number of chains is at most \(1+\log_2 H_i\). Consequently an unmarked block of length \(J\) follows within \(O(H_i)\) steps. From any late \(n\), the first mark is within \(J\) or the desired block already exists, and its log height is at most \(H_n+rJ\). This proves the theorem with the advertised physical-height clock.

The conclusion gives clean windows at every polynomial precision in the target, with boundedly many candidate binary digits and a margin for the allowed ternary digits. A result forcing a physically normalized Green spike to admit one of these approximants still remains open.

## One window for all positive rational anchors at a polynomial modulus

The same conclusion handles an arbitrary positive rational family simultaneously. For every \(\delta>0\) and \(J\ge1\) there are \(\eta>0\) and a constant such that every sufficiently late \(n\) has a \(J\)-block finishing within \(O_J(H_n)\) further odd steps, on which at every date
\[
    v_3(q a_i+p)<\lfloor\delta H_i\rfloor
    \quad\text{for all positive }p,q\le 2^{\eta H_i},\quad 3\nmid q .       \tag{4}
\]
Here and in the waiting bound constants may depend on \(\delta\) and the fixed orbit. Begin with \(\eta\le1/4\). If a near hit occurs, use the signed representative \(c_i=-p_i/q_i\). It has nonzero ordinary displacement \(a_i-c_i>0\), and
\[
 -\eta H_i\le v_2(a_i-c_i)\le \log_2(q_i a_i+p_i)\le(1+\eta)H_i+1.
\]
On a chain of exact bridges the previous duration proof therefore works uniformly before \(\eta\) is chosen, using the upper bound \(2H_i\) and the terminal lower bound \(-H_t/4\). Choose \(C,c\) accordingly. At a comparable pair of marks, multiply (1) by \(q_iq_j\), which is a ternary unit. The resulting fixed number of binary powers have integer coefficients of logarithmic height at most \(O(\eta H_i)+O_J(1)\). The uniform moving-coefficient estimate consequently forces exact equality after \(\eta\) is sufficiently reduced. The same height-drop proof gives (4). This argument needs only a high positive orbit throughout the proof interval. If desired one may take the union of these rational shadows and the signed binary shadows in statements 1–2, first taking the terminal lower valuation parameter to be \(\max(\gamma,1/4)\) and using the zero-chain signed-mantissa proof.

For comparison with the all-height ordinary census, put
\[
 Q(x)=\sup_{p,q\ge1,\ 3\nmid q}
             \frac{v_3(qx+p)}{\log(2\max(p,q))},
\]
where coprimality of \(p,q\) may be imposed. At any phase satisfying (4), the part with height at most \(2^{\eta H_i}\) has \(Q\le \delta H_i/\log 2\). For larger height \(h\), the elementary bound \(3^{v_3(q a_i+p)}\le h(a_i+1)\) gives \(Q\le(1+1/\eta)/\log3\). Thus for each \(\epsilon>0\) one can find such \(J\)-blocks with \(Q(a_i)\le\epsilon H_i\) at every phase and the same order of waiting time. The [ordinary census and its sharp typical scale](https://github.com/GettysburgResearch/collatz/blob/8fd938eb3ef7898a427d8a6c0e501a7777c4a6ec/research/six-hour-20261127/pointwise/ALL_HEIGHT_ORDINARY_CENSUS.md) concern a different sampling statement, with a score of order \(\log(3+H_i)\). A reciprocal-summable exceptional set can contain one complete escaping ray.
