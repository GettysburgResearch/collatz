# Independent Mersenne quotient and checkpoint review

The reviewed quotient manuscript and finite enumerator have SHA-256
`949e4034ef47c70df11f98627c2210a1723cbd194f1101deda87ca7d38d85c95`
and `d07adb5465c35a213fe9819d22417692fb595d2a7f16ca9f6ca280a669832c79`.
The reviewed checkpoint manuscript and eleven-row checker are
`4818e4f380e20bd19197510bde4baa65f1d16ea1598dfc9f2b11dad661620599`
and `658483ddaf236a56d05a600d4097db8b6e5fd82711f4fbfae1d53bf707563681`.

**Uniform quotient verified as a written theorem with exact finite
replay.** For the scalar $N=2^j$, each fixed uniformly legal ordinary
word preserves the form $2^u3^v N+c$. Integrality on the progression
forces $v=-d$ for $c=-m/3^d$ in lowest nonintegral terms,
and $v\ge0$ for integral $c$. Given a cyclic state, aligning two
center paths by whole turns matches both slope and intercept. For a
fixed word, sufficiently large ordinary exponents realize every
required parity; the exponent threshold can depend on the word.

For a center reaching the negative cycle, every preceding reflected
value is at least one by reversing from the cycle. During the
denominator-removing prefix of $J$ clocks and $d$ odd inputs one gets
$|c|\le2^{J-d}S^J(|c|)$. Combining the remaining integer bound with
$U=u-h+h_0(v+o-V)/q_0$ proves equation (2) independently of $J,h$.
The integer-center factor $(2^{h_0/q_0}/3)^v$ is at most one on all
three named cycles. Consecutive parameters force $d\le4$ for a uniform
query with the extra mod-3 residue, or $d\le5$ for bare integrality,
since $v_3(2^{162}-1)=5$. For the endpoint slope bound the relevant
inequality is strict and asymptotic in $j$, which suffices for the
stated eventual fixed-word claim.

An independent enumeration used the exact rational-power bound raised
to $q_0$, without the original floor relaxation, and classified
rational orbits by visits to designated phases with recurrence
detection. At the four states the residue and size filters left
272, 134, 377 and 117 candidate centers. The only admissible
$(d,m,u)$ were $(3,341,8)$ and $(1,13,5)$ at the first two states.
The two $e=6$ states had 29 and 12 candidate centers and no query.
These are proof-bounded candidate sets. The original 2,000-step
signed-classification guard raises an error on unresolved inputs
instead of discarding them. Both original scripts were replayed
normally and under optimized Python.

**The unrestricted ancestor clock in equation (3) is a separate
verified statement.** If $o\le7k+3$, every required inverse from
the simultaneous signed endpoint $-17$ is integral up to its last
division by three. Equation (1) gives $w+y\ge 4Qy/75$. The finite
low-orbit exclusions imply $y=17$ or $y\ge21$. The latter forces
$w>P$; the former is a number of complete cycle turns forcing
$w\ge P$. This gives the claimed lower bound on $o$ for any supplied
$w<P$, with no upper bound on the competing clock $L$. It neither
turns the quotient into a source-dependent search nor rules out
ancestors with at least $7k+4$ odd inputs.

**Two-checkpoint claims verified at their stated evidence levels.**
At the two admissible subparent queries, leastness transfers badness
to the triples. The two exponent-dependent ordinary turn counts
produce $3^{67+108m}-5$ and $2^r3^{3+7k}-17$. On $m=3\pmod {16}$
the first meets $3^{q+2}-1$ after eight clocks on each arm;
$0<q+2<j$ makes the earlier-Mersenne hypothesis applicable.

For the all-$a$ first-checkpoint obstruction fix $H$, then
$B\ge\max(288,H)$ and a sufficiently large exponent. Small $a$ are
separated by the elementary height ratio. For $a\ge3H+3$, divisibility
forces equality of the leading coefficients, hence equal clocks
and $\delta=a-q=p-t$. Continuing a putative signed merger to the
$-1$ phase from $-58$ yields $7+\delta$ even inputs on the second
representative. For nonnegative $\delta$, its initial reflected
magnitude is at most $2^{7+\delta}$; thus $-7\le\delta\le2$.
The ten signed traces exclude all of these. The conclusion allows
arbitrarily long *prescribed* deadlines over varying ordinary
sources and gives no all-time nonmerger of one source.

On the $B=288$ cylinder, the 11 choices of $r$ exhaust the
progression because $162\cdot2^{284}$ is invertible modulo 11.
The return $m\mapsto m+11\cdot2^{284}$ changes $s$ by
$1134\cdot2^{284}$, leaving $3^s$ fixed modulo $2^{287}$. Every
tested clock is at most 285. Independently decoding each row, I
checked the two endpoint functions using literal integer orbits at
two distinct positive values of $X$ in its fixed binary cylinder,
with the required factor of $3$ for any negative exponent offset.
These two evaluations determine the affine identity since the
words are fixed on that cylinder. All eleven pairs matched.
$0<s+\delta<j$ holds on the full row. Thus this is an ordinary
conditional exclusion on an entire exponent progression, even
though the eleven certificates are a finite replay. It is separate
from the Lean one-sixteenth theorem. Only the rational sign
obstruction is obtained from the polynomial identity at limits;
it places no general convergence condition on an irrational limit.

**Final density section and integration.** The checkpoint manuscript
with the added density section is SHA-256
`6cae0c040058024d57f72cbd25fbea5103e87f76c86af96a276fe8391fb3ef0f`.
Under the pinned PR146 full-grid symbolic absorption bound at fixed
gap four, at most $C2^h/\sqrt h$ residue classes fail the sufficient
synchronization test. For every odd positive $D$,
$v_2(3^{108D}-1)=4$. The sequence
$3^{67+108(b+Di)}-5$ therefore visits distinct residues during each
period of $2^{h-4}$ indices for $h\ge4$. For $h=\lfloor\log_2 M\rfloor$,
at most 32 periods cover an interval of $M$ indices. This yields the
stated source-qualified $O(M/\sqrt{\log(2M)})$ finite-deadline bound
uniformly in $b,D$, with small $M$ absorbed in the constant. Its
upper Banach density consequence is for the set of exponents whose
specific checkpoint pair never meets. It gives no stopping bound at
an individual exceptional exponent.

A fresh isolated kernel build using Lean 4.34.1 and Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612` passed all six public
declarations of `MersenneTwoCheckpoints.lean`, SHA-256
`6baca0d4b3da675d026f9735bf71a6b6363bf3b9c89988a5ff167d2eeb1f99b0`.
The prior `MersenneParity.lean` source used in that build has SHA-256
`04b39dadfc74dd38aed1c43c5f6d94e99d06d90a98da96fe0e39ae40cfef07e8`.
The independent build of `MersenneProgressCases.lean`,
`1fd0e0850ab9847f43082ff5c53ea07d34ddf0a4b24c41304d5856f015eda406`,
passed its two public declarations using the restored baseline dependencies.
With the supplied parent equation, uniqueness of the rank-three source
identifies its Mersenne basin equivalence. The prior exact-first-bad
consumer uses unconditional bounded return and below-parent minimality
to select $j$ and to certify all earlier indices. The one-sixteenth
closure contradicts nonbasin membership at that $j$. The last
corollary derives the below-parent implication from the stated global
leastness; it requires no unrestricted higher-rank assumption. The
printed axiom lists contain only standard foundational dependencies.

The standalone `MersenneRescueWords.lean` certificate is SHA-256
`85073e9d4202e936560591f2ae6eb91ba281c9507eacb728b399d26931b97118`.
It certifies the 11 specified pairs of affine words for *all* integer
lifts of their listed binary residues. Independently recomputing
$y=3^{s+\min(\delta,0)}\bmod 2^h$ gave all 11 recorded residues, together
with the required slopes and clocks. The exponent-to-residue bridge is
the separately checked written modular argument.
