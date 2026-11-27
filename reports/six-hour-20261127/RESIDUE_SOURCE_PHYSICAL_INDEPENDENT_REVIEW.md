# Independent review of the physical source in a fixed fractional-part fibre

I accept **Source bounds in one fractional-part fibre of a rational Collatz cycle**, frozen SHA-256 fbc36853257d915e229513d5f3985af95061e5e8d3d381321840684df06d9a73. The five bounded-width exponents are per populated residue, with uniform constants in the full reduced denominator, period, numerator residue and slope numerator. The three improved bounded-strip diversity conclusions and the two fifth-moment global alternatives use the separately quoted exponent-three result. Of the four physical occupation rows, the first two use the 2018 bound, and the elementary first row avoids the Subspace Theorem. The denominators of the rational slope and of the odd phases have different roles in the proof.

## Source locations and injectivity

In a length-$b$ physical window let $K$ be its actual total, and $B=\sum_{j<b}3^{b-1-j}2^{A_j}$ its full numerator. Starting at $N=r+dJ$, the identity $2^KN'=3^bN+dB$ gives
$$
 J\equiv-3^{-b}B-rd^{-1}\pmod{2^K}.
$$
At an end with $N'=r'+dJ'$, reduction modulo $3^b$ gives
$$
 J'\equiv2^{-K}B-r'd^{-1}\pmod{3^b}.
$$
Dividing by $d$ occurs modulo the respective prime powers, where it is a unit. In a fixed fibre the integer coordinate is the physical floor. Every two distinct phases in the same fibre give distinct such coordinates. If $2^K>X_0$, every fixed word and source translation can identify at most one in $[0,X_0]$. A starting floor of zero is harmless. For the elementary terminal census one can take $3^b>X_0$ directly; changing the horizon by $O(1)$ preserves its exponent. One can also use the original factor two because terminal numerators are odd, hence terminal floors have one parity at fixed residue.

Fixing record positions, endpoint grades, intercept cell and changed raw/repaired grades determines every changed partial date. The full source translation is therefore
$$
 -rd^{-1}-3^{-b}(B_{\rm raw}-B_{\rm repaired})\pmod{2^K}.
$$
The second term is a known integer residue because the record fixes all summands which differ. Unchanged endpoints preserve $K$. For a fixed record the analytic proof can enlarge to complete repaired paths inside that single translated source interval. The Fourier bound is uniform in its center. In a raw four-copy treatment the common translation cancels in each balanced difference. Neither the frequency coefficient nor the small nonzero integer tested by fixed-place separation retains any $d$ or $r$. The construction does not assert that the sequence of physical floors itself obeys the ordinary odd map.

For bounded $X$, each fibre contains at most $\lfloor X\rfloor+1$ phases, including the lowest possible representative. On any sequence $X\to\infty$ in one of the bounded strips, $0<2^\theta-3\le 2^W/X$ forces $\theta\to\log_2 3$. Thus every fixed near-critical slope neighborhood in the original source count applies uniformly for large $X$, irrespective of $P,d,r$ or the reduced numerator $a$ of $\theta$. Choose the packing slack to fit the desired exponent error before sending the horizon to infinity. All packing lengths are chosen at the scale $\log(1+X)$ and not at $\log(dX)$. Windows may wind around a short primitive period. The source estimates only require the finite physical recurrence across the chosen window. The resulting rates are $\gamma/3$ for the four-segment bounds and $\gamma/4$ for the five-segment bounds, giving all five listed exponents.

The only sum over residues uses the count $R$ of those attained by the cycle. The subgroup $S$ is an upper bound through the multiplied orbit residue recurrence. The subgroup may contain unoccupied classes. Under the separately quoted exponent bound $M$, the positive height inequality gives $1+X=O_\epsilon(q^{M+\epsilon})$ for the reduced slope denominator $q$. For bounded $q$, bounded width gives either a slope uniformly separated above $\log_2 3$, or one of finitely many rational slopes in a compact neighborhood. Thus the same bound covers the bounded-height branch. With $P=gq$ and fixed-place per-fibre exponent $C$ this yields $R\gg_\epsilon gq^{1-MC-\epsilon}$. In the first three rows $g\mid S$ follows separately from the height-at-most-two order theorem.

## Sparse canonical and physical populations

With $R\le P^\delta$ and a positive proportion of phases under the clean physical cap $X_0$, one has $P\ll R(1+X_0)$, so $X_0\gg P^{1-\delta}$. The former period-to-numerator comparison is replaced before applying any local count. The cyclic incidence argument gives the required positive proportion globally; it need not give this same proportion in each individual fibre. The located-source upper bound is applied to the retained starts of every fibre and then summed. Bounded records cost exactly the same number of bits per local window. Unbounded raw grades and valuation jumps are covered by their original weak-composition charges. The unit-frequency raw degree or repaired-frequency separation is at least as strong as the previous small-denominator comparison. Thus $(1-\delta)\le MC$ would be necessary under simultaneous failure of each stated alternative. The six displayed margins are strictly positive and match exact rational recomputation.

For an interval $[s,K_0 s]$ about the physical minimum, put $n=\lfloor\log_2(K_0s)\rfloor$. In the shortcut dynamics each of the first $n$ intermediate rational states is at least $s$, since the even states descend to an odd phase by division by a nonnegative power of two. If the initial state is at most $K_0s$ and the final state at least $s$, the product identity implies $k/n\ge5/8$ for all sufficiently large $s$, uniformly in the unbounded distant excursions. For fixed $r$ every shortcut word determines exactly one floor residue modulo $2^n$ from its starting numerator $r+dJ$. The physical band shortens this to at most two potential integer floors. Counting such words gives $O_{K_0}(R s^{24/25})$ genuine starting phases. Under positive occupied proportion and $R\le P^\delta$, initial distinctness gives $s\gg P^{1-\delta}$ and the sharper census gives $P/s\ll P^{(25\delta-1)/24}=o(1)$ in every row. The accumulated correction on any oriented cyclic arc is at most $P/(3s\log2)$, establishing global uniform depth versus physical height even at sites far outside the low band.

For the mixed physical fifth-moment row, the retained low starts already give $s\gg P^{1-\delta}$. The correction needed in each local repaired window is only $O(\log s/s)$ when its horizon is based on $K_*s$. The cycle slope controls the final height through $\theta-\lambda\le 1/(3s\log2)$ and the reduced denominator bound. The per-residue location retains the previous positive fifth-moment margin. The high magnitudes and all large positive valuations remain permitted at the charged sites.

## Exact controls

My checker constructs 115 genuine primitive rational cycles and checks both prime-power sources in 14,544 physical windows. There are 5,831 winding windows, 8,165 zero starting floors, and 13,743 cases with both translations nonzero. In 10,330 windows I swap two adjacent unequal valuations only in the comparison history, preserving the actual endpoint duration and moving exactly one interior partial date. The uniquely determined additive correction restores the physical starting floor in every case; omitting it changes every tested raw location. I separately verified every entry of 66 complete finite shortcut parity tables, totaling 12,848 parity cylinders. The normal and optimized Python runs agree bit for bit. A finite window with an artificial comparison history tests the source translation and is not described as a second actual rational orbit.

Reviewed by the independent all-height reviewer on 27 November 2026 UTC.
