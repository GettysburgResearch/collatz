# Removing the query-residue restriction after 405 laps

**Kernel theorems.** On the same e=6 parent, let $N=2^{9+162m}$ and suppose the pump supplies ordinary $t,w$ with
$$
81w+2399=128\,2048^n t,\qquad 6561\,2187^nt=8192N+101936,\qquad 81z+271=512N .
$$
For every $n\ge405$, one has $2^{40}w<z$. The first equation forces $w\equiv81\pmod {128}$, in particular $w>0$. Every such parent is excluded as a least reverse defect, independently of $w\bmod 3$. If $z$ were bad, its lower meeting with $w$ would make $w$ bad. The quantitative return theorem at this actual $w$ would produce a reverse defect $y\le2^{40}w<z$.

Set $F=2^{40}$. At $n=405$ the exact integer inequality
$$
 F\,2048^{n+1}\le6561\,2187^n
$$
holds, and it fails at 404. Multiplication by $2048<2187$ propagates the bound to every later lap count. The source and parent equations give
$$
16F(81w+2399)\le6561\,2187^n t=16(81z+271)+101936 .
$$
Since $16F\cdot2399>16\cdot271+101936$, the desired height bound is strict. The simpler test $F\,2048^n\le2187^n$ first holds at 423. The Lean file checks all four numerical comparisons directly. The threshold 405 is sharp for the height statement over whole progressions: at each fixed $n\le404$ arbitrarily large valid parameters exist, $t$ tends to infinity with them, and the negative margin in the coefficient inequality eventually dominates the fixed additive terms. This last sharpness deduction is written. It does not exclude other reasons for a least-defect contradiction at smaller depths.

**Exact additional parameters.** Put $G=8+7n$ and $A=13047808$. Eliminating $t$ yields
$$
3^{G+4}w=2^{11n}(2^{29+162m}+A)-2399\,3^G .
$$
Consequently a positive integral $w$ is selected at large parameters by exactly one congruence
$$
2^{11n}(2^{29+162m}+A)\equiv2399\,3^G\pmod {3^{G+4}} .
$$
The congruence implies $3^G$ divides $2^{29+162m}+A$, since $2^{11n}$ is a ternary unit. The quotient $q=(2^{29+162m}+A)/3^G$ is divisible by 128 because the numerator is divisible by 128 and the denominator is odd. Thus $t=q/128$ is an ordinary integer and the same physical start and target equations hold. The earlier signed-cycle proof then applies in full.

Normalizing by the unit $2^{11n}$ gives the correct initial residue $2^{29}\equiv -A\pmod {243}$. Since $2^{162}$ has exact ternary valuation five after subtraction of one, successive cubing and digit lifting give one residue class for $m$ modulo $3^{G-1}$. This is three times the density previously obtained at that lap count. The three lifts modulo $3^G$ correspond to the three distinct output digits $w\bmod3$. In particular this adds two complete ordinary progressions at every $n\ge405$. All these new classes remain inside $m\equiv3122\pmod{19683}$.

The Lean theorem integral_shift proves how one period changes a physical realization. Write $P=3^{G-1}$. One has $2^{162P}=1+3^{G+4}(3u+1)$. Shifting $m$ by $P$ increases $w$ by $2^{20+11n}N(3u+1)$, a nonzero residue modulo three independent of $m$ since $N\equiv2\pmod3$. The shift also gives the ordinary $t$ for the new parameter. Iterating this shift, excluded_progression proves the original-parent exclusion on an entire progression above any requested parameter bound. Starting from cofinally many of the certified narrow-class parents, three_digits realizes every output digit among three successive shifts. Uniqueness of the wider residue follows from the period argument above.

**Scope.** These results use the physical mergers at PR197's e=6 parent and its unconditional quantitative reverse-defect return. The comparison $y$ supplied by that return can differ from $w$. The widened progression still leaves other ordinary parameters unresolved. [WideCenterPump.lean](WideCenterPump.lean)
