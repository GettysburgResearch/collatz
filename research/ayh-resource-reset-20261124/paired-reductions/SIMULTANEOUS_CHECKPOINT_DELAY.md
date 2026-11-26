# A simultaneous ordinary delay at both Mersenne checkpoints

**Status.** Unconditional written theorem for the shortcut map on positive integers. The theorem concerns finite initial segments of ordinary orbits. The supplied examples are parameters of the rank-three arithmetic family. No assertion that any example is a reverse defect is needed. Universal pointwise rescue and Collatz remain open.

Use the two checkpoints in PR 197, head `156652e03fe7a78f9cd4442039779cc622fdf3de`, path `research/ayh-resource-reset-20261124/source-progress/MersenneTwoCheckpoints.lean`, Git blob `00bf04bc8051e7cb3d2a7d9457c9e1b7bab388c7`, claims `two_bad_checkpoints` and `checkpoint_exponents`. The original single-arm obstruction and second-arm rescue are in `TWO_CHECKPOINT_RESCUE.md`, Git blob `8819cdbd95b5bb5767db3ef1396c814fa07eb461` at the same head. Those earlier claims remain unchanged.

## The ordinary theorem

Let v≥128 satisfy v≡4 mod 27 and put

$$m=(11v-17)/27,\quad j=66v-5,\quad q=44v-1,\quad s=42v-4.$$

Substitution gives j=97+162m, q=67+108m, (j−1) mod 11=5 and s=3+7 floor((j−1)/11). Write A=3^q−5, B=32·3^s−17, H=v₂(v)+4 and K=floor(4(j−2H−6)/9). For every 0≤i≤H, every positive a<j and every 0≤l≤a+K,

$$T^i(A)\ne T^l(2^a-1),\qquad T^i(B)\ne T^l(2^a-1).$$

In fact all the post-ascent comparisons of length at most K also fail for **every** a≥1, including a≥j. On the explicit subfamily v=4·2^(18t), t≥1, the source-side delay H=18t+6 is unbounded, while K/j tends to 4/9. On every fixed ternary residue class for m there is such an unbounded delay. To see this, use CRT to take m₀≡1 mod 88 in that ternary class. Then v₀=(27m₀+17)/11 is integral with v₂(v₀)=2. In a specified class modulo 3^b take v=v₀·2^(18·3^b t). The binomial expansion of (1+27c)^(3^b) gives 2^(18·3^b)≡1 mod 3^(b+3), preserving m modulo 3^b.

## Signed comparison and ordinary precision

The correlated rational pair x=1/3,y=1/81 on r=5 satisfies 3^70 y^22=27 x^21. At the two starts the signed rational trajectories (parity is the numerator parity for odd denominators) have prefixes

* −14/3, −7/3, −3, −4, −2, −1, followed by the fixed point −1.
* −1345/81, −659/27, −325/9, −161/3, −80, −40, −20, −10, −5, followed by the cycle −5, −7, −10.

In particular both always have value at most −1. A length-i shortcut word is an increasing affine map W(n)=(3^p n+D)/2^i where p counts odd inputs and 0≤D≤3^i−2^i. This follows by appending one branch and induction. Two odd-denominator rationals congruent modulo 2^i follow the same i parities, since each step loses at most one bit of precision. For even n, v₂(3^n−1)=2+v₂(n), by factoring off an odd geometric sum and successively squaring 9. Thus v₂(3^q−1/3)=v₂(v)+4 and v₂(32·(3^s−1/81))=v₂(v)+8. The indicated signed input has the positive source's first H physical parities on both arms.

Given either checkpoint write it as 2^e 3^g−b, with (e,g,b)=(0,q,5) or (5,s,17), and u=1/3 or 1/81 respectively. Applying its physical word of length i gives the numerator 2^e 3^(g+p)+C, where C=D−b3^p and |C|≤17·3^i. Evaluating the same word at 2^e u−b gives (2^e3^p u+C)/2^i≤−1. Hence

$$-17\cdot 3^H < C+2^i < 0. \tag{1}$$

Every branch, chosen by either parity rule or arbitrarily, sends the *real* interval (−1,∞) into itself.

## Separation in size and ternary divisibility

Let d=v₂(v). Since 2^d≥8d for d≥6 and v≥128, one has d≤v/8 and H≤v/8+4. It follows that K≥H and s≥K+H+3, and floor(v/2)≥2H+6. The binomial theorem gives (2187/2048)^12>(17/16)^12>2. Consequently

$$3^s/2^j=(32/81)(2187/2048)^{6v}> 2^{\lfloor v/2\rfloor-2}.$$

Both initial checkpoints exceed 3^s/2. Each positive step is at least a halving, so through H clocks every checkpoint value exceeds 2^(j+H+2).

At l≤a, the earlier Mersenne value is 2^(a−l)·3^l−1. Equality would imply that 3^min(g,l) divides C+2^i. By (1), this forces l≤H+2. Its value is therefore less than 2^(j+H+2), a contradiction.

At l=a+k with k≤K, take the physical length-k branch V of the start 3^a−1, having d' odd inputs and offset D'. Write E=D'−3^d', so |E|≤3^k. If a<K+H+3, then V(3^a−1)+1≤(3/2)^k3^a, since T(n)+1≤3(n+1)/2 on positive integers. This is at most 3^(H+3)(9/2)^K<2^j, by (9/2)^4<2^9 and the definition of K. Otherwise both a,g are at least K+H+3. A meeting requires

$$2^{k+e}3^{g+p}-2^i3^{a+d'}=2^i E-2^k C.$$

The right side has absolute value at most 18·2^H·3^K. Here 2^K3^H≤2^H3^K since K≥H. The left side is divisible by 3^(K+H+3), which exceeds that bound. Hence both sides vanish. The two affine maps W(2^e X−b) and V(3^(a−g) X−1) now have equal slopes and equal intercepts; replacing X=3^g by the positive rational u preserves equality. The first gives a value at most −1 and the second gives a value strictly greater than −1. This proves the theorem.

## Pointwise reduction at exhaustion of these signed cycles

These identities also retain information when the initial binary precision runs out. For supplied v≡4 mod 27 with d=v₂(v)≥1 define the odd integers

$$U=(3^{44v}-1)/2^{d+4},\qquad V=(3^{42v}-1)/2^{d+3}.$$

Both are on earlier ordinary Mersenne orbits, of exponents q+1 and s+4 respectively. Five physical steps from A and eight from B give exactly

$$2^{d-1}3U-1,\qquad 2^d V-5.$$

Indeed the signed prefixes have two and four odd inputs and endpoints −1 and −5; their slopes determine the identities. The first prefix is legal since d+4≥5. For the second, the precision is d+8≥8. Following d−1 of the ordinary odd steps from the first endpoint, and floor(d/3) three-step turns T^3(8n−5)=9n−5 from the second, gives

$$3^d U-1,\qquad 2^{d\bmod3}3^{2\lfloor d/3\rfloor}V-5.$$

Thus every hypothetical exceptional v satisfying d≥1 forces these two **ordinary** values bad alongside the two explicitly good odd numbers U,V. Their ordinary input clocks from the checkpoints are d+4 and 8+3 floor(d/3), respectively. With W=3^(2v) their unnormalized numerators are W^22−1 and W^21−1, with exact common divisor W−1. For a fixed odd c and v=c·2^d the units satisfy U(d+1)=U(d)+2^(d+3)U(d)^2 and V(d+1)=V(d)+2^(d+2)V(d)^2, whether or not both consecutive v are in the original row. This follows by factoring a square; eighteen iterations carry the explicit family to its next member. The two badness conclusions are one-way implications under the least-defect hypothesis. The arithmetic recurrence alone does not transport Collatz basin status across different parameters.

## Decision procedure for signed obstructions with denominator a power of three

All rational solutions to the coupling with nonzero coordinates have w=x/y and x=3^(3−14r)w^22, y=3^(3−14r)w^21. On the exponent row r one must additionally impose its actual binary residue restrictions. At any odd prime other than 3, a denominator in reduced form persists under *both* shortcut branches. Thus both signed starting values can ever become integers only if w has denominator a power of three (and is a dyadic unit, as on the original row).

For any such rational checkpoint n with reduced denominator 3^a there is a terminating test for the property “every signed forward value is ≤−1.” Stop at the first value >−1 or at the first negative integer. Both stopping labels are absorbing as sign statements. While the value remains ≤−1 and its denominator has not cleared, its magnitude is at most |n|3^p/2^h at time h, where p<a is its odd count. This uses |(3n+1)/2|≤3|n|/2. Hence after floor(log₂(|n|3^a))+1 steps one of the two tests has held. This criterion covers all rational shadows that reach an integral sign trap, irrespective of whether the eventual negative integer orbit is cyclic. Odd denominators with other prime factors, and general dyadic limits, need separate analysis.

Neither the sign decision nor the finite-prefix obstruction rules out a later meeting of the same supplied positive orbits. The first unsupported step in this reduction is a pointwise rescue or descent after the displayed ordinary odd-unit checkpoints.

## Linear-length ordinary rescue after every singular depth

Fix d≥1, any positive odd ternary-power modulus 3^b and any prescribed residue for m modulo 3^b. One can explicitly construct a progression of ordinary v=2^d c with c odd, v≡4 mod 27, and the prescribed ternary residue for m, on which A meets the orbit of the earlier Mersenne input 2^(q+1)−1. At most 52d+19 further clocks on both arms suffice after the two starts 3^d U−1 and U. All positive members use exactly the same branch words. For v≥128 the lower bound above applies to these same ordinary sources through clock d+4 from A. This gives an unconditional rescue of order d at *every* unbounded delay depth. It supplies a constructive extension of partial parameter data. Choosing the extension changes c, so a preassigned infinite sequence of bits for c needs a separate argument.

Here are the elementary choices. For the pair (X,3^sX+D), retain the ordering by affine slope, swapping after a step if necessary. The bit in the following table is the parity of X, the lower-slope start. When s=0 either consistent orientation can be retained. The four rows are the direct shortcut updates from PR 146, head `f431078244e868dc699fad011044f0d5e7f76437`, `research/upper-bit-mergers/THREE_RAY_UPPER.md`, blob `e7be1addad96aca971e4ecc1aea09a1d1086ed75`. Only the arithmetic updates and elementary level-zero word are needed here; no probability estimate enters the proof.

| Current condition | Bit 0 gives (s',D') | Bit 1 gives (s',D') |
|---|---|---|
| D even | (s,D/2) | (s,(3D+1−3^s)/2) |
| D odd, s>0 | (s+1,(3D+1)/2) | (s−1,(D−3^(s−1))/2) |
| D odd, s=0 | (1,(3D+1)/2) | (1,(1−3D)/2) |

State (0,0) is absorption. At each positive level s, use bit 1 on an odd offset, dropping the level. On an even offset use a bit minimizing the valuation of the next offset, with v₂(0)=∞. Write e=v₂(3^s−1). For 0<v₂(D)<e, both options decrease v₂(D) by one. For v₂(D)≥e, at least one option has valuation e−1: if v₂(D)=e choose bit 0, and if v₂(D)>e choose bit 1. Thus within e+1 clocks the level decreases. For odd s one has e=1, and for even s one has e=2+v₂(s). Since the sum of v₂(s) over 1≤s≤d is less than d, the greedy phase takes at most 4d clocks from (d,−1).

Throughout that phase, 1+|D'|+3^s'≤2(1+|D|+3^s) by the displayed updates and s'≤s. At grade zero one therefore has |D|<2^(6d+1). Use bit 0 for each nonzero even D. On odd |D|≥3 the word 01 for D≡3 mod 4 or 11 for D≡1 mod 4 returns to grade zero with offset (3D−1)/4 or −(3D+1)/4, respectively. The magnitude falls by a factor at most 5/6; an even-offset step reduces it by a factor two. Four reductions, using at most eight clocks, more than halve magnitude. The states with D=1 and D=−1 absorb by 001 and 101 respectively. These give the claimed crude length bound of 52d+19 and an algorithm for the actual word.

After h chosen bits, write U=u+2^h k. Each current arm is an integer affine function of k, with an odd coefficient given by a power of 3. Thus the next base-arm bit chooses exactly one lift u modulo 2^(h+1), even after an orientation swap. The first greedy bit from (d,−1) is 1, so the resulting U is odd.

For v=2^d c with c odd, let F_d(c)=(3^(44·2^d c)−1)/2^(d+4). For any distinct positive c,c' (odd or even),

$$v_2(F_d(c)-F_d(c'))=v_2(c-c').$$

Indeed the difference numerator is an odd power of 3 times 3^(44·2^d|c−c'|)−1. Thus F_d induces a permutation modulo every 2^h preserving parity. Each chosen odd U class has a unique odd-cofactor preimage, computable one binary digit at a time. Independently impose 11·2^d c≡17+27m₀ mod 3^(b+3), with 11·2^d a unit modulo that ternary power. CRT gives the required positive ordinary c progression. The earlier Mersenne start reaches 3^(q+1)−1 after q+1 clocks and then reaches U after d+4 halvings. This completes the claimed physical rescue.

More generally, specify in advance any valid f≥1 bits of c, including its odd first bit. These fix f native base-arm bits through the isometry. If absorption has not occurred there, the state has s≤d+f and 1+|D|+3^s≤4^f(2+3^d): direct inspection gives the factor four at arbitrary steps, including the one possible upward jump. Greedy descent therefore uses ≤4(d+f) further clocks and arrives at a grade-zero offset of binary length at most 6(d+f)+2. The same final reduction gives a rescue within 52(d+f)+19 *further* clocks. Hence the construction extends any finite odd-cofactor prefix on every specified ternary class. The new extension is free data, not a certificate for a fixed unmatched ordinary cofactor.

## Ordinary stopping distribution at the normalized pair

There is a distinct estimate for the time to merge the two normalized ordinary inputs U and 3^d U−1, for d≥2. In each fixed ternary m class, sample a complete cofactor period of 2^(h−1) odd candidates for h≥1, in a sufficiently late interval. The fraction missing an ordinary same-clock meeting by h is bounded above and below by absolute constants times min(1,d/√h). In particular its median is of order d² as d grows. This estimate concerns this specified comparison alone, after normalization. The linear steered constructions above and this quadratic typical scale have different quantifiers.

For the upper bound use the written arbitrary-state tail in PR 146's pinned `THREE_RAY_UPPER.md`, last section. It bounds symbolic survival from state (s,D) by C(1+s+√(|D|/3^s))/√h on the complete binary grid. Substitution of (d,−1) and conditioning on the first input U being odd costs at most a factor two. The isometry and odd ternary stride above give the exact odd grid.

For the lower bound the first bit on these inputs is 1, taking the pair to level d−1; every subsequent jump of a positive level has a fresh unbiased sign by the state table. Extend the signs with unused independent fair signs if needed. Each physical clock takes at most one jump. Survival of the simple symmetric walk started at d−1 for h jumps is therefore sufficient to avoid grade zero through h physical clocks. Reflection and the central binomial bounds give survival at least c min(1,(d−1)/√h): the reflected count is a central interval of width 2(d−1) in the h-step law, and the atoms within one central standard deviation of the correct parity are at least c'/√h. For the median lower bound, the probability of hitting zero by h jumps is at most h/(d−1)² by the second-moment maximal inequality. The earlier upper estimate gives the median upper bound.

On late enough lifts this survival is a statement about numerical ordinary equality. At clock k≤h, nonmatching grades of a numerically equal pair give
$$(3^{p}-3^{d+p'})U=D'-3^{p'}-D,$$
where both D,D' lie between zero and 3^k−2^k. Thus U≤2·3^h. Every positive cofactor with U>2·3^h excludes that accident. A prior symbolic absorption would persist. This proves the physical lower as stated. The inherited PR 146 probability bound is a source-qualified input to the upper half only.

For the explicit unmodified cofactors c=1 at v=4·2^(18t), t=1,2,3, exact paired affine replay finds the first normalized same-clock merger at 1,442, 746, and 2,904 clocks, respectively. These three m have residues 13,854, 40,235, 19,366 modulo 59,049 and all are 13 modulo 16. They lie outside the earlier 214-certificate ternary bank and the earlier one-sixteenth kernel case. For each example the same merger works for every admissible c≡1 modulo 2^h, with h the stated merger clock. The finite calculation gives no conclusion for an arbitrary c.

## Kernel and replay boundary

`CheckpointUnitExit.lean`, theorem `twoOrdinaryExits`, proves both normalized ordinary equalities and attachment of both odd factors to their earlier ordinary Mersenne trajectories for every strictly positive d and odd cofactor. Its proof derives the exact factorizations internally by repeated squaring. The public `distinct_at_positive_shadow` checks the real-word separation for arbitrary words. The full two-sided horizon obstruction, the greedy length analysis, and the distribution statement above are written proofs. Run `python -B check_checkpoint_delay.py` for the exact signed traces, ordinary endpoint tests, 130 binary/ternary rescue constructions, and three preassigned cofactor certificates.

## Coupling on the next binary scale

The normalized variables remain related even for a preassigned cofactor. With W=3^(2v), one has v₂(W−1)=d+3. The polynomial 21X^22−22X^21+1 has a double root at 1. Its coefficient of (X−1)^2 is 231, which is odd. Thus the exact valuation on the next scale is

$$v_2(21U-11V)=2(d+3)-(d+4)=d+2.$$

Consequently the next d+2 physical parities from V can be computed from the odd-denominator rational (21/11)U. The two full-precision ordinary integers remain distinct. More generally, Z=(W−1)/2^(d+3) is a third known good odd factor from Mersenne exponent 2v. Each 1≤i≤32 gives a good odd factor of W^i−1, from exponent 2vi<j when v≥128. All of their initial binary residues are functions of the same Z through the polynomial geometric sum. Thus the second scale retains exact correlations at each individual source; independent resampling of the two normalized units would change the model.
