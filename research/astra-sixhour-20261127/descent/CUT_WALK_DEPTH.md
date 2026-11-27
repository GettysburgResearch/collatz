# Ordinary lower bounds on the length of an original-cut walk

**PROPOSED written theorem.** A cut walk from \(z\) may use positive ordinary shortcuts in either direction and directed jumps \(y\to3y\) only at \(y\equiv17\bmod48,\ 0<y<z\). Size the walk by its total number of single edges, including inverse edges and jumps. For every fixed upper first-hit rank \(r\ge3\), there are arbitrarily large canonical \(z\) with that true upper rank for which every walk from \(z\) to \(3z\) has length \(\Omega(\log\log z)\). On the same controls, even reaching **any** smaller canonical ordinary lower representative already costs that many edges. No requirement that the smaller representative have a good upper is imposed in this exclusion.

A second consequence, using the source-qualified linear-budget inverse-routing theorem in Paper 48/v2, gives a growing-rank sequence on which the lower bound is \(\Omega(\log z)\) and \(\Omega(H)\) for the *true upper first-hit clock* \(H\). These are lower bounds on proof mechanisms at actual positive sources. They do not produce a nonbasin source.

## The imported all-word calculation at 590

We use precisely the following prior classification. Start at \(N-1\), with limiting dyadic coordinate \(N_2=0\) and ternary coordinate \(N_3=590\). For any fixed legal ordinary path, the endpoint is an affine form \(\alpha N-b\). Among all such paths of arbitrary length with \(0<\alpha\le128/81\), the complete prior list (even allowing a second initial form \(2N-1\)) is
\[
 (8/9,13/9),\ (1,1),\ (256/243,623/243),\ (32/27,61/27),\
 (4/3,5/3),\ (1024/729,2735/729),\ (3/2,1),\ (128/81,271/81).
\]
The binary and ternary residues across these forms allow only the final entry to be canonical. The earlier proof reduces arbitrary paths to forward followed by reverse edges, discharges their reduced ternary denominator, and exhausts the ordinary integer specializations from 1 through 932. Its replay reached maximum height 125252 and longest first hit 113. We independently reran that frozen enumeration. The new result below uses the table to control **every numerical walk at a given positive ordinary source**, including a walk chosen after inspection of the input and its entire course. [PR195 all-word theorem and checker](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/FINITE_COVER_BARRIER.md)

## Quantitative transfer to positive integers

Given a desired horizon \(L\ge1\), set \(t=L+7,\ K=t+2\). Choose a positive odd ternary unit \(u\) with a supplied first hit at one and an integer \(e\) satisfying
\[
 e\ge4t+10,\qquad N=2^{e+2}u\equiv590\pmod {3^K}.
\]
Then \(z=(128N-271)/81\) is a positive integer congruent to 17 modulo 48. Its lower reaches \(N-1\) at clock seven and its upper reaches \(2^e u\) at clock nine. See the physical opening and the suffix proof in [the upper-word note](UPPER_WORDS.md).

Consider a numerical ordinary walk of at most \(L\) steps from this \(z\). Prepend the seven legal inverse edges from \(N-1\) to \(z\). Each visited value is some \(\alpha N-b\), starting from \(\alpha=b=1\). Every slope is a positive rational with denominator dividing \(6^t\), dyadic valuation at least \(-t\), and ternary valuation at least \(-t\). At one edge the absolute value of the center grows by at most a factor two plus one; hence \(|b|<2^{t+1}\). Each branch used on the ordinary input is legal at the two local coordinates in the prior theorem. The input difference from the signed dyadic center has valuation at least \(e+2-t\ge4\); the difference from the 590 ternary specialization has valuation at least \(K-t\ge1\). This holds during the entire walk, including guarded inversions, and preserves the final residue test modulo 48.

If the numerical endpoint is \(y\le z\), its slope must be \(\alpha\le128/81\). Otherwise \(\alpha-128/81\ge1/(81\cdot6^t)\). Since \(N>1000\cdot12^t\), this slope gap exceeds every possible intercept difference at that \(N\). The frozen table now applies. Its sole canonical endpoint is \(z\) itself. All its other forms satisfy \(16y\ge9z\) at the indicated ordinary inputs; the smallest-slope form has exactly \(16y=9z+7\). Thus every ordinary site reached within the specified budget also exceeds the certified \(z/2^{40}\) floor.

A cut walk of length at most \(L\) therefore cannot make its first directed jump. A purely ordinary walk from \(z\) to \(3z=(384N-813)/81\) is impossible in that budget as well. If its endpoint slope differed from \(384/81\) the same denominator and intercept bounds would preclude numerical equality. If the slopes agreed, numerical equality would give an affine identity, whose signed centers would lie in the same ordinary signed rational component. The lower center \(-271/81\) reaches \(-1\); the upper center \(-271/27\) reaches zero. These are distinct fixed points. This proves the claimed pointwise length exclusion without assuming the purported path works on any other input. The kernel verifies the common denominator, the sharper intercept bound \(|b|\le2^t\), the transfer of the numerical height cap, and the exclusion of accidental slope equality with the numerical triple. The finite checker separately enumerates actual undirected neighborhoods at six fixed-rank controls and five growing-rank controls through distance 24. [AffineDepth.lean](AffineDepth.lean) · [Numerical checker](check_cut_depth.py) · [Finite receipt](../../../reports/astra-sixhour-20261127/descent/cut-depth-finite.json)

## Fixed first-hit rank

For a fixed supplied \(u\), two generates the units modulo \(3^K\). Choose \(e\) in \([2\cdot3^{K-1},4\cdot3^{K-1})\) with the required congruence. This ensures \(e\ge4t+10\), while \(\log_3 e=L+O(1)\). Since \(\log_2 z=e+O_u(1)\), the excluded budget \(L\) has order \(\log\log z\). Take \(u=1\) for true upper rank three. For each \(r\ge4\) fix a first-hitting \(u>1\) with \(r-3\) odd departures as constructed in [UPPER_WORDS.md](UPPER_WORDS.md). The same lower bound then holds at the given rank, with actual upper first-hit clock \(e+9+h_u\).

## Linear-in-height and linear-in-certificate obstruction at growing rank

**Source-qualified deduction.** Paper 48/v2 Theorem 8 and equations (80)–(83) give, from the positive odd unit 5, an ordinary route of \(b=\Theta(K)\) odd inverse steps of total valuation \(2b\) to a positive odd unit in any prescribed class modulo \(3^K\), for all sufficiently large \(K\). The upper bound and a common linear choice of \(b\) are what is used here. Its proof uses a published-on-rStation analytic routing estimate; that input has not been formalized or independently reproved in this packet. [Paper 48/v2, §9](https://rstation.ai/problems/collatz/papers/48)

Set \(e=4t+10\). Prescribe \(u\equiv590\cdot2^{-e-2}\bmod3^K\) in that routing theorem. The produced \(u\) reaches 5 after exactly \(2b\) shortcut clocks with \(b\) odd departures. No earlier visit to one is possible because one's cycle never visits 5. As the four-clock path \(5,8,4,2,1\) adds one odd departure, this produces the genuine upper first hit for \(3z\) at
\[
                         H=e+9+2b+4,\qquad r=b+4.
\]
The affine inverse identity gives \(0<u\le5(4/3)^b\). Thus \(\log_2 z,\ H,\ r\) all have order \(L\). The pointwise exclusion above therefore costs a positive constant times each of those parameters on this sequence. This construction steers the *cofactor for an obstruction*; it does not steer an original unknown disagreement or furnish a descent.

The prior positive-Haar extension of the 590 calculation gives an additional distinction: the all-word obstruction is not confined to that single ternary point. Its positive mass statement by itself does not assert that any fixed ordinary exponent belongs to the infinite obstruction. The finite positive bounds above use explicit depth, coefficient spacing and actual positive first-hit words instead. [PR195 positive-measure barrier](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/HAAR_BARRIER.md)

## A finite ordinary consequence of the positive-measure refinement

For a fixed supplied suffix \(u\), enumerate the admissible exponents as \(e=e_0+162k\), \(k\ge0\). There is a set of ordinary indices of positive lower natural density on which the above numerical cut-walk lower bound is at least
\[
            \log_3 k-3\log_3\log_3 k-O(1).
\]
This assertion concerns finite budgets growing with the actual integer index; it does not place any individual integer in the infinite exceptional set.

Indeed, PR195 supplies a set \(E\) of positive relative Haar mass \(\delta>0\) in \(590+3^5\mathbb Z_3\) on which the eight subcap forms are the same as at 590. One may use \(\delta=0.410\cdot3^{-380}\). For \(m\ge385\), take the union \(E_m\) of all classes modulo \(3^m\) meeting \(E\). Its relative mass is at least \(\delta\). The map \(k\mapsto2^{e_0+2}u(2^{162})^k\) traverses these classes exactly once per period \(3^{m-5}\), by \(v_3(2^{162v}-1)=5+v_3(v)\). Every point represented by a class in \(E_m\) has the earlier numerical exclusion through budget \(L\) when \(m\ge L+8\) and \(e\ge4(L+7)+10\): transfer each proposed finite walk to a point of \(E\) in that class in place of 590. The same signed binary coordinate and rational-slope bounds apply.

Fix \(\eta>0\) and count \(\eta X\le k\le X\) at precision \(m=\lfloor\log_3 X-2\log_3\log_3 X\rfloor\). All sufficiently large such \(k\) meet the binary budget, and this \(m\) exceeds the claimed length bound plus eight. The period is \(o(X)\); complete periods give at least \(\delta(1-\eta)X-o(X)\) ordinary indices. Letting \(\eta\downarrow0\) proves the lower-density assertion.
