# Which affine families admit marked first visits in every relative interval?

For a positive integer $a$, let $a_*$ be its part coprime to six, so $a=a_*2^{h(a)}3^{p(a)}$. Let $F$ be a finite list of affine functions $f(t)=a_ft+b_f$ with positive integer slopes and nonnegative integer intercepts. Write $T$ for the shortcut map and $O_i$ for its odd-departure count.

**The full placement theorem is equivalent to equality of the $a_{f,*}$ over the list.** Fix positive moduli $W,M,Q$ and a relative width $\delta>0$. There are positive real $C,K$ and an integer $G$, uniform over all the data below. For each positive $y$ prime to three, each real $X\ge Cy$, and each independent pair of residues $\tau\bmod M,\rho\bmod Q$, there are integers $D,g$ satisfying

$$
 D\equiv\tau\pmod M,\qquad g\equiv\rho\pmod Q,\qquad
 g\le G,\qquad 2^D y\le KX.
$$

For **every** source residue $c\bmod W$, there is a positive $t\equiv c\bmod W$ in $[X,(1+\delta)X]$ such that, for all $f\in F$, the **first** visit of $f(t)$ to $y$ occurs at clock $D+h(a_f)$, with precisely $g-p(a_f)$ odd departures. The same $D,g$ work for every $c$ and every arm. The target may be periodic or even. [AffineClassification.iff_common](AffineClassification.lean)

PR146 already identified the common prime-to-six condition for robust finite affine cylinders, the forced clock and grade differences, a constructive prefix bound, a $6^H$ obstruction for incompatible slopes, and infinitely many ordinary parameters visiting any supplied unit target. The present theorem adds first arrivals in every sufficiently large relative interval, a time within a fixed additive constant of $\log_2(X/y)$, bounded grade, independent time and grade residues, and simultaneous realization of every source residue. The new Lean proof covers nonnegative intercepts. PR146's original cylinder formulation also allows signed intercepts. [PR146 affine rays, pinned source](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/AFFINE_RAYS.md)

## The positive construction

Write $a_f=m2^{h_f}3^{p_f}$ with common $m$. Use a temporary integer parameter $U$. For every $0\le j<mW$, the first $h_f$ clocks on $2^{h_f}3^{p_f}(U+j)+b_f$ follow the word from $b_f$. The resulting affine profile has slope $3^{p_f+O_{h_f}(b_f)}$ and intercept

$$
 T^{h_f}(b_f)+j3^{p_f+O_{h_f}(b_f)}.
$$

Synchronize these finitely many profiles with the ordinary reference $U$. The deterministic finite-profile theorem gives a single cylinder $U=R+2^H v$. At time $H+h_f$, every displayed arm agrees with $T^H U$, and its odd count plus $p_f$ equals $O_H(U)$. This holds for every $v\ge0$ and all $j$ at once. [AffineGeometry.rows](AffineGeometry.lean)

Use the marked window theorem for the reference $U$ in this cylinder, in a window of width $\delta/2$ at $mX$. For each $c$ choose $0\le j<mW$ with $U+j\equiv mc\bmod mW$. This identifies $U+j=mt$ with the requested residue of $t$. The uniform threshold absorbs the finite shift $j$ and ensures $U>2^H y$ and $U\ge R$. For every $i\le H+h_f$, the initial arm is at least $2^{h_f}U>2^{H+h_f}y$. Its state after $i$ steps is at least its initial value divided by $2^i$, so it cannot visit $y$ in this prefix. The common suffix therefore transfers the genuine first visit, including when $y$ lies on a cycle. [AffinePlacement.first_of_prefix and marked](AffinePlacement.lean)

## An ordinary one-witness obstruction

For any actual meeting $T^i(at+b)=T^j(ct+d)$ with $i,j\le H$, write $u,v$ for the two true odd counts. The resulting alternative is

$$
 2^j3^u a=2^i3^v c,\qquad
 t\le 6^H(\max\{b,d\}+1).
$$

Indeed the affine numerator at length $i$ is $3^u(at+b)+q_i$, where $0\le q_i\le3^i-2^i$. The corresponding expression for the second arm has the analogous bound. After multiplying the two formulas to a common denominator, unequal integer slopes differ by at least one. The larger of the two scaled intercepts bounds $t$. The proof treats both clocks zero as well. [AffineGeometry.slope_or_small](AffineGeometry.lean)

For the uniform window assertion, set $X=Cy$ and let unit targets grow. The clock estimate forces $2^D\le KC$. The fixed arm delays give one bound $H$ on both actual clocks. The ordinary parameter $t\ge Cy$ eventually exceeds the displayed exception, so all selected slopes have the same part prime to six. For example, $t$ and $5t+1$ can meet at individual parameters using growing clocks. They cannot admit the uniform comparable-target conclusion here. Distinct coefficients $1,2,3,6$ do admit it for arbitrary nonnegative intercepts. [PrimeCore.characterization](PrimeCore.lean) and [AffineClassification.iff_common](AffineClassification.lean)

## A six-arm ordinary certificate

The six arms $t$, $2t+1$, $3t+2$, $6t+5$, $36t+17$, and $24t+11$ synchronize on $t=2{,}076{,}818+2^{21}v$. Their reference endpoint is $175{,}430+3^{11}v$. For $v=0$, their respective first-clock and grade pairs at target $1$ are $(148,80)$, $(149,80)$, $(148,79)$, $(149,79)$, $(150,78)$, and $(151,79)$. The literal replay also checks $v=1,13,1079$ and 30 independent-clock negative controls for the incompatible slopes $1,5$. [Finite replay](check_affine_windows.py)
