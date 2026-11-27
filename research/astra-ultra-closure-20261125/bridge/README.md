# A reverse certificate at odd rank one forces a pure power

**Universal coverage remains open.** At the ordinary shortcut map, a reverse disagreement is a positive source with a bad lower arm and a converging triple. We first allow every odd reverse disagreement. The least attainable odd count for a converging triple of an odd positive source is one; the existence of a bad lower source in this layer is unknown. The identity below characterizes its entire arithmetic layer and converts descent in upper certificate cost into an explicit height budget. Here $C$ denotes convergence to 1, and a bad integer is one whose orbit never hits 1.

## The exact base case

Write \(Z_0=7\), \(Z_{m+1}=64Z_m+7\), so \(9Z_m+1=2^{6(m+1)}\). For any odd \(z\), if \(T^h(3z)=1\) with exactly one odd input, all clocks after the initial odd input are halvings. Thus \(9z+1=2^h\). The order of 2 modulo 9 is 6, so \(z=Z_m\) for some \(m\ge0\). Conversely every such triple hits in \(6(m+1)\) clocks with one odd input. A positive triple cannot hit with zero odd inputs because no positive power of two is divisible by three.

For \(k=3m+2\), two lower steps from \(Z_m\) reach \(4^k+1\). Then \(2k\) clocks reach \(3^k+1\), by repeated use of \(T^2(4v+1)=3v+1\). The integers \(3^k+1\) and \(3^{k-1}\) have identical immediate successor. Consequently

\[
 C(Z_m)\quad\Longleftrightarrow\quad C(3^{3m+1}).
\]

At a first bad tower \((w,r)\), a bad rank-one source therefore forces \(w=1\) and \(r\le 3m+1\). Every positive smaller base supports only good powers, and all earlier powers at the same base are good. In particular the rank-one base case is settled under the hypothesis \(w>1\). The case \(w=1\) asks for an actual return to an earlier power. The exponent sequence is zero-indexed throughout. The observation identifying the common successor of a pure power and a power plus one was independently supplied by the minimum-core lane.

## Two ordinary transports with unbounded savings

For a positive reference \(a\) with genuine hits \(T^h a=T^k(3a)=1\), let \(L\ge\max(h,k)\). Set
\[
 X=a+2^L4^d t,\qquad Y=a+2^L3^d t.
\]
At the lower arm, \(T^{h+2d}X=T^hY\). At the upper arm, \(T^{k+2d}(3X)=T^k(3Y)\). Each prefix at \(X\) uses exactly \(d\) more odd inputs than its partner. This iterates the prior paired reference contraction in the [minimum-source packet](../../astra-minimum-source-20261124/descent/README.md) and extends its checked single-arm equality to both saved counts and arbitrary certificate tails. The [previous first-tower prefix](../../astra-universal-closure-20261124/descent/CORE_PREFIX.md) uses the same ordinary-cycle identity.

For \(a=17,h=9,k=L=17\) and \(t\) a positive multiple of three, both \(X\) and \(Y\) are 17 modulo 48. Their common upper endpoint exceeds 2, so every given hit of \(3X\) contains the displayed prefix. For \(d>0\) the source height and its actual upper certificate odd count both decrease, within the prescribed residue. This gives an unbounded family at which both induction parameters are compatible.

A complementary ordinary ascent uses \(X=8\cdot2^d t-1\) and \(Y=8\cdot3^d t-1\) for positive \(t\). The lower arm takes \(d\) odd inputs from \(X\) directly to \(Y\). The upper arm takes three clocks from \(3X\) to \(9\cdot2^dt-1\), then \(d\) odd inputs to \(9\cdot3^dt-1=T^3(3Y)\). The last value is at least 8. Thus *every supplied hitting certificate* transfers with exactly \(d\) fewer odd inputs. Any earlier hit would trap the common endpoint in the two-cycle. The height satisfies the exact trade \(2^d(Y+1)=3^d(X+1)\). The prior minimum-source work already contains the one-step stable extension and the all-odd iterate. The long paired count and its interaction with the rank-one base case are the statements proved here.

## Descent that stays inside rank one

At the two classes \(m\equiv1878,3159\pmod {4096}\), the lower arms of \(Z_{m+1}\) and \(Z_m\) merge. For \(p=3^{3m+2}\), take \(a\equiv p\pmod{2^{14}}\) in the table. The 14-step lower prefixes give the same endpoint at the representatives.

| \(m\bmod4096\) | \(a\) | Common endpoint | Odds from \(a+1\) | Odds from \(27a+1\) |
|---|---:|---:|---:|---:|
|1878|14417|1925|7|4|
|3159|13451|200|5|2|

Since \(3^{12288}\equiv1\pmod {16384}\), the power residue persists throughout each progression. The derivative factor \(27\) between the two perturbations cancels the three extra odd inputs, giving \(T^{14}(27p+1)=T^{14}(p+1)\) on all lifts. A bad rank-one source on either successor row thus gives a smaller bad rank-one source with an explicit one-odd upper certificate. These are two sufficient rows.

## A quantitative joint descent criterion

At a first bad tower, every bad rank-one destination obeys the exact floor
\[
 w=1,\qquad 9Z_m+1=2^{6m+6}\ \ge\ 2^{2r+4}=16\cdot4^r.
\]
A chain starting at a reverse defect of height \(z\) and ending at a bad rank-one source \(Y\) can tolerate increases of intermediate source height. Charge a saving of \(d\) odd inputs when \(2^d(Y+1)\le3^d(z+1)\). Charges add under composition. Both transports above satisfy this condition. If the cumulative charge is \(D\) and
\[
 9\cdot3^D(z+1)<2^D 2^{2r+4},
\]
the destination is below the necessary floor. This implication, including composition of the cost bounds, is proved in Lean.

There is a simple sufficient numerical range when \(w=1\). PR197's bounded return supplies at least one canonical \(z\le2^{40}3^r\). For \(r\ge1600\) and \(3D\le2r\), the preceding strict inequality follows. Indeed \(z+1\le(2^{40}+1)3^r\). After cubing, it suffices that
\[
 [9(2^{40}+1)]^3 243^r < 16^3 256^r ,
\]
since \((3/2)^{3D}\le(3/2)^{2r}\). The exact integer comparison holds at 1600 and persists by \(243<256\). This last rate consequence is a written derivation with an exact arithmetic control. The theorem with the exact inequality has no lower cutoff on \(r\). This packet supplies no separate assertion for each of the first 1,600 pure powers.

## Where the global argument stops

For \(w>1\), a terminating transfer to any rank-one reverse disagreement would contradict minimum-core goodness. For \(w=1\), a transfer ending at a rank-one disagreement strictly below the exact floor would contradict the earlier-power hypothesis. Neither alternative currently supplies a transfer on every source. In the sufficient asymptotic regime a total chain with the indicated cost and a bound \(3D\le2r\) on its actual total saving are both required. A bound on the initial upper-certificate rank can supply the second input if the chain strictly decreases that same rank at every step.

The positive-anchor hypothesis entails specified common low binary digits still present after both known reference hitting clocks. Goodness of smaller bases alone gives no such timing. The negative row has its own divisibility condition. In PR197's `QuantitativeReturn.lean`, `descSound` handles `.jump` by testing the basin label of a freshly queried tripled value. In the true branch the quantitative proof obtains membership of that upper arm without a bound on its odd count and with no common-suffix assertion relative to a preceding certificate. The output of `bounded_return` is an actual defect with a height bound. This proof supplies neither the needed chain nor a rank bound. No impossibility of a stronger return theorem is claimed.

The clocked multiple-of-three ancestor in PR193 and the specific ordinary certificate in PR195 likewise give exact mergers on their own stated domains. Neither forces the simultaneous good-reference alignment above at a supplied first tower or re-entry into the rank-one layer within its budget.

[Lean source](PairedReturn.lean) · [Finite control](check_bridge.py) · [PR197 bounded return](https://github.com/GettysburgResearch/collatz/blob/b27a6fe31a487adf5615e173329ad009b975a3cd/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean) · [PR195 ordinary certificate](https://github.com/GettysburgResearch/collatz/blob/51e2c43a60950e446eabe782c5b1cb1d0ae11bab/research/astra-global-closure-20261124/round9/formal/FinalProposal.lean) · [PR193 multiple ancestor](https://github.com/GettysburgResearch/collatz/blob/24cdd0e5471d4421716cfce6bd88916f858f994c/research/astra-universal-proof-20261124/UniversalProposal.lean)
