# A fixed-cofactor rescue outside the 32 comparison exponents

**Status.** Unconditional ordinary-orbit identities and a written all-exponent criterion for positive integers under the shortcut map. The least-defect conclusion is a restricted exclusion. Universal convergence and pointwise rescue on the whole parameter row remain open.

## A supplied member of the delay tower

Take the preassigned cofactor 1 and valuation 128, so that $v=2^{128}$, $v\equiv4\pmod {27}$, and $j=66v-5$. The original second checkpoint meets an earlier Mersenne orbit at the displayed clocks.
$$
 T^{183}(32\,3^{42v-4}-17)
 = T^{42v+21+178}(2^{42v+21}-1).
$$
In fact the identity holds for **every** $v=2^{128}(1+2^{49}u)$, $u\ge0$. Taking $u=27w$ keeps the stipulated row. At all these sources $42v+21<j$, so the earlier Mersenne hypothesis gives convergence of the second checkpoint. Together with the two-bad-checkpoint theorem this excludes such a least-defect source. No choice of further digits is needed to apply the identity to $v=2^{128}$.

Write $3^{42v}=1+2^{131}V$. Repeated modular squaring with modulus $2^{180}$ gives
$$
 (3^{42})^{2^{128}}\equiv1+2^{131}R,
 \qquad(3^{42})^{2^{177}}\equiv1,\qquad R=357515049256705 .
$$
Thus $V=2^{49}K+R$ with integer $K\ge0$. The ordinary exit theorem gives the input $4\,3^{84}V-5$ at clock 134. The exponent $42v+21$ reaches its peak $3^{21}(2^{131}V+1)-1$. At $V=R$ the 49-step path from the first input has 25 odd steps and the 178-step path from the peak has 88. Both end at
$$
 25769221349192892822098750098086840813219442152713792 .
$$
Replacing $R$ by $R+2^{49}K$ adds $4\,3^{109}K$ to both endpoints. The actual words stay legal by the physical lifting identity
$T^t(2^t k+x)=3^{p_t(x)}k+T^t(x)$, where $p_t$ counts odd inputs. All parts of this argument, including the modular exponentiations and the two physical words, are kernel proofs in `CollatzFixedCofactorRescue.fixedCofactorFamily`.

For $h\le49$, none of the 32 exponents $2vi$, $1\le i\le32$, can give either normalized checkpoint a meeting at an ascent or within $v$ post-peak clocks. By the earlier comparison theorem only the same degree could do so. For degree 22 the comparison on the unit requires an odd-count advantage of 128 within $h$ clocks. For degree 21 the peak has 131 initial halvings, and the forced post-peak time is $h+129$. Its subsequent odd count is at most $h-2$ if $h\ge2$, and it is zero otherwise. The required count is at least 84. Thus the offset $+21$ supplies an actual rescue earlier than all the old comparisons in this clock range. This does not preclude arbitrarily late visits from those inputs.

### The original least parent and overlap with prior cases

Set $v=2^{128}(1+27\cdot2^{49}w)$ and $m=(11v-17)/27$. The theorem `FixedCofactorLeastParent.lean / rowArithmetic` proves $27m+17=11v$, $97+162m=66v-5$, and $42v+21<66v-5$. For the original parent $81z+527=1024\cdot 2^{66v-5}$, `parentBasin` proves $\operatorname{Basin}(z)$ from the usual minimality implication at smaller ordinary parents. The proof attaches the rank-three ordinary orbit equivalence at this very $z$, obtains the exact first bad index from the quantitative reverse return, and transfers convergence of the earlier Mersenne to the second raw checkpoint at clock 183. `leastExcluded` therefore rules out this original least reverse defect for every $w\ge0$, including $w=0$.

The progression has
$$
 m=138633556893715670299893358583312975037 + 11\cdot 2^{177}w.
$$
Every such $m$ is 13 modulo 16. The old one-sixteenth has residue 3, and the old cylinder has initial residue 7 with period $2^{284}$, so both are disjoint. The old ternary rescue has $m\equiv181\pmod{2187}$. On this progression that happens exactly when $w\equiv403\pmod{2187}$, since $m\equiv2121+565w\pmod{2187}$. In particular the supplied cofactor-one index $w=0$ is outside all three prior cases. The overlap calculation is kernel-checked in `oldRows`. These comparisons address precisely those three indexed cases.

## An exact criterion for all earlier peak exponents

Let $v\ge128$, $v\equiv4\pmod {27}$, $d=v_2(v)\ge1$, $d=3k+r$, $0\le r<3$. Use either row
$$
 (e,b,\beta,a)=(22,d,d+4,1),\qquad (21,2k,3k+3,5).
$$
The normalized source is $B=3^b(3^{2ve}-1)/2^\beta-a$. For the **physical** word of length $0\le h\le v$ at $B$ denote its odd count by $p$ and its ordinary affine offset by $D$, so $T^hB=(3^p B+D)/2^h$. Put
$$
 H=h+\beta,\qquad N=2ve+b+p,\qquad C=2^\beta(D-a3^p)-3^{b+p}.
$$
Then $C$ is odd, and $2^H T^hB=3^N+C$.

Start the formal carry language at $(0,0,-1)$. From $(t,p',E)$ append either $(t+1,p',E)$ or $(t+1,p'+1,3E+2^t)$. Write $S_t$ for the resulting carries, retaining a witnessing odd count when needed.

**Theorem.** For each supplied source, either row, and each $0\le h\le v$, the following are equivalent.

1. Some $1\le n<j$ and $0\le t\le v+\beta$ give $T^hB=T^t(3^n-1)$.
2. $C\in S_H$.

Every meeting in (1) has $t=H$ and $n=N-p'$, where $p'$ counts the odd inputs from the peak. Conversely **every** witnessing $p'$ in (2) selects this actual earlier exponent and gives the meeting. When $C<0$ membership is equivalent to $C=-1$, in which case the choice $n=N$ works. For odd $C>0$, if membership is possible at any depth, it is already possible at depth at most $1+\lfloor\log_2(C+3)\rfloor$. One may append even symbols to pad to any greater depth. The depth in the equivalence is still $H$.

**Proof of separation for arbitrary $n$.** We use the bounds $d\le v/8$ and $B>3^{42v}/32$ proved in the companion 32-exponent note. Thus $T^hB>3^{42v}/2^{v+5}$. For $n<4v$, $T^t(3^n-1)+1\le(3/2)^t3^n<3^{6v}$ because $t\le v+d+4<2v$, which is smaller than the source. Otherwise $n\ge4v$. Write $E=D'-3^{p'}$ for the peak word, with $|E|\le3^t$. A meeting yields
$$
 2^t3^N-2^H3^{n+p'}=2^H E-2^t C .
$$
The left side is a multiple of $3^{4v}$. Set $J=v+d+4$. Both clocks $H,t\le J$, and $|C|\le81\,3^{h+d}$ by $0\le D\le3^h-2^h$ and the displayed definition. Consequently the right side has absolute value at most $82\,6^J<3^{4v}$: $J\le5v/4$, $6<3^2$, and $82<3^{3v/2}$. Both sides vanish. The powers of 2 in the left equality give $t=H$, equality of the powers of 3 gives $n=N-p'$, and the right equality gives $E=C$.

Conversely choose a witness in $S_H$. Since $p'\le H\le5v/4$, $1\le N-p'\le N\le44v+d+v<j$. The witness applied formally to $3^{N-p'}-1$ gives exactly $T^hB$. A parity mismatch would produce a dyadic rational of denominator at least 2 in lowest terms. Both subsequent branches double such a denominator, so a final integer forces ordinary legality at every step. The kernel theorem `realize` establishes this without a legality assumption, while `physical` proves the opposite direction for a physical word. This is also an $O(H^2)$ elementary decision in physical shortcut steps. Try the $H+1$ candidate odd counts, run their peak words on residues modulo $2^H$, and compare the signed carry and the count. Modular exponentiation costs are additional.

**Proof of the signed recognition rules.** A formal negative carry at level $t$ has the form $-2^i$, $0\le i\le t$. This is immediate for the initial value, and appending an even step preserves it. A negative odd-branch successor $2^t-3\,2^i$ requires $i=t$ or $i=t-1$, giving a negative power of 2 in either case. All such values occur by $i$ initial odd steps and then even steps. Odd $C<0$ therefore forces $C=-1$, represented by all evens. For odd $C>0$, remove trailing even symbols. At the last odd symbol at index $i$, $C=2^i+3E$. The index is positive, since the first odd symbol at index zero gives $-2$ and all subsequent carries would stay even. Thus $E$ is odd. Either $E\ge0$ or $E=-1$. In both cases $2^i\le C+3$, as required. These implications are kernel-checked for all clocks and carries in `AllMersenneCarries.lean`. The analytic separation for $n\ge4v$ above is a written proof.

**Uniform additional delay at every cofactor.** For each fixed positive source and $h\le v$ the all-exponent criterion gives the further implication
$$
 2^h\le a+3^b/2^\beta
 \quad\Longrightarrow\quad
 T^hB\ne T^t(3^n-1)
 \quad(1\le n<j,\ 0\le t\le v+\beta).
$$
Indeed the initial formal numerator is $C_0=-2^\beta a-3^b\le-2^{\beta+h}$. During the next $h$ clocks an even branch preserves this numerator. An odd branch at index $i<h$ adds $2^{\beta+i}$ to three times the preceding numerator, which can only decrease it. Thus $C_h\le C_0<-1$ and the negative-carry classification applies. This formal-word bound is kernel-checked in `negativePrefix`. The two respective real cutoffs on $2^h$ are $1+(3/2)^d/16$ and $5+(9/8)^k/8$. Both grow without bound with $d$, for every supplied cofactor. These delays start at the normalized inputs, after the mandatory raw prefixes. A bounded number of additional clocks cannot solve the whole row by allowing all earlier Mersenne exponents in this range.

**Restriction on a finite-source Subspace Theorem argument.** PR 210 uses approximants to a *single* infinite ternary critical-record coordinate, formed from successively repeated prefixes and fixed algebraic linear forms. The two numbers $U,V$ at our ordinary source are rational integers. Their shared power base gives no sequence of repeated prefixes about one algebraic critical-record limit with controlled height. The exact carry equation here uses arithmetic separation without such a hypothesis. A proof that at least one of the two actual carry sequences enters its prescribed language, or a different ordinary return after this clock range, remains open.

## Sources and replay

- PR 197 at `10d87fee615d1095990d6b7ea329126b4cf7aa5a`, `paired-reductions/CheckpointUnitExit.lean` (ordinary unit exits), `paired-reductions/THIRTY_TWO_ORDINARY_COMPARISONS.md` (size and matched-degree restrictions) and `source-progress/MersenneTwoCheckpoints.lean` (two bad checkpoints). All paths are under `research/ayh-resource-reset-20261124/`.
- PR 210 at `592328fecf8ea2cf41736294856d95f890a1ba98`, `research/critical-record-rational-rigidity-20261125/SUBSPACE.md`, S1/S2 (record-limit hypotheses). No conclusion of that proposed argument is used above.
- Daniel Bernstein and Jeffrey Lagarias, *The 3x+1 conjugacy map*, Canadian Journal of Mathematics 48 (1996), 1154–1169, [doi:10.4153/CJM-1996-060-x](https://doi.org/10.4153/CJM-1996-060-x). Finite parity coding is relevant context. The carry sign classification and physical realization used here are proved directly.
- Run `python -B check_all_earlier.py` and `python -O -B check_all_earlier.py`; no Python assertion flags affect the checks. The script separately exercises the signed language, small literal ordinary integers and the fixed binary-power family using modular arithmetic.
