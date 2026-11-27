# Macroscopic thickening of exact ordinary ancestor sets

**Status:** written proof; finite algebra Lean draft in LeanCore.lean is not compiled. The published 0.84 exponent is an external input, not replayed here.

Let T(n)=n/2 for even n and (3n+1)/2 for odd n. Anc(a) consists of positive integers whose actual T-orbit visits the fixed positive integer a, including a itself. Write U for the accelerated map on positive odd integers. A unit below means a positive integer prime to 3; an odd unit is prime to 6.

## Theorem A (local thickening)

Fix an odd unit a, integers M>=1, d>=0, r0 modulo 2^d, and real 0<A<B. For every sufficiently large X there are at least c X^eta pairwise disjoint intervals of M consecutive positive integers inside [AX,BX], all contained in Anc(a), with first element r0 modulo 2^d. Here eta=log(2)/log(64/3). Using the published Krasikov–Lagarias predecessor theorem (Theorem 6.1, exponent 0.84), the bound improves to c X^0.84/log(2X). Constants can depend on all fixed parameters.

This assertion is stronger than finding arbitrarily long blocks somewhere: the target a, block length and relative macroscopic interval are fixed, and the estimate holds at EVERY sufficiently large cutoff.

### 1. A finite ordinary block synchronizer

For fixed h, the parity word of T through h steps depends only on the initial integer modulo 2^h. If a representative r has p odd inputs, the exact lift is

    T^h(r+2^h t) = T^h(r)+3^p t.

Proof: refine t modulo 2 at every step; the current coefficient 3^p is odd, so either next parity can be chosen. The same identity holds on Z, and a sufficiently large lift makes all original inputs positive.

Begin with the prescribed residue r0 modulo 2^d and the M arms x+i, 0<=i<M. At depth h every arm has profile a_i+3^p_i t. For two arms X,Y put s=p_Y-p_X, s+=max(s,0), s-=max(-s,0), and define the integer offset D by

    3^s- Y = 3^s+ X + D.

Both normalized coefficients are odd. Thus for even D the arms have the same parity, and for odd D they have opposite parities. Either parity of X can be prescribed using the next input bit. While s!=0:
* If D is nonzero even, choose both even, replacing D by D/2.
* If D=0, choose both odd. D becomes (3^s- - 3^s+)/2, a nonzero integer.
* For odd D, choose X odd if s>0, X even if s<0. Then |s| decreases by one. The next normalized offset remains integral.

This reaches s=0 in finitely many steps (each finite nonzero even offset has finite 2-valuation). Now swap arms if necessary to make D>=0. A positive even D is halved. For positive odd D choose X even, Y odd, giving Y'=3X'+F with F=(3D+1)/2. Halve both until the offset is odd f>0. Choose X odd, Y even. The new difference is (f-1)/2, nonnegative and at most (3D-1)/4<D. This reaches zero. Equal endpoints and equal counts remain equal under every later refinement. Apply the construction successively to merge all M arms into a single profile.

Append a common odd step, with parity chosen by the next bit. The resulting constants h,p,r,z satisfy p>=1, 3∤z, and

    for all integers t: T^h(r+2^h t+i)=z+3^p t, 0<=i<M.

The residue r refines r0; take its canonical representative. This is a finite cylinder, not a claim about any preassigned initial x outside the cylinder. The argument is an explicit elementary reconstruction of the equal-profile idea in PR146.

### 2. A finite bank of inverse phases

Put L=2*3^(p-1) and let ell be the discrete logarithm to base 2 of units modulo 3^p, valued modulo L. The order assertion follows by factoring 4^k-1, or induction using v3(4^(3^j)-1)=j+1.

For an odd unit q>2 and any unit residue r' modulo 3^p, choose e in [2,1+2*3^p] satisfying

    2^e q = 3r'+1 (mod 3^(p+1)).

Then q'=(2^e q-1)/3 is a positive odd unit, q'>q, and T^e(q')=q (one odd input followed by e-1 even inputs). It satisfies q'=r' modulo 3^p, hence

    ell(q') = ell(q)+e-j (mod L),
    j=ell(3+(r')^(-1)).

The function r' -> 3+(r')^(-1) permutes the units, so j can be prescribed arbitrarily. In particular take j=0 at each inverse step. After k such steps, with total clock E_k, the resulting q_k satisfies

    ell(q_k)=ell(q)+E_k (mod L),
    log2(q_k)=log2(q)+E_k-k log2(3)+epsilon_k,

where |epsilon_k|<=C_N/q for 0<=k<=N and q>2. This follows by multiplying 1-1/(2^e q_previous); every intermediate q_previous>=q and e>=2. Also q_k<=K_N q with K_N fixed for a finite bank.

Choose positive a'<b' with [2^h a'/3^p,2^h b'/3^p] strictly inside (A,B). We seek y=2^b q_k in [a'X,b'X], with y=z modulo 3^p. The latter is exactly

    b+E_k = ell(z)-ell(q) (mod L).

The possible real log2 y, ignoring epsilon_k, form translated integer lattices with step L and shifts -k log2 3. The rotation by log2 3 modulo L is irrational. A sufficiently long finite initial segment of its orbit is a net with mesh smaller than a fixed fraction of log2(b'/a'). For completeness, density follows by pigeonholing fractional parts to obtain an arbitrarily small nonzero displacement modulo L; its consecutive multiples form a net, and negative indices can be approximated by positive indices by recurrence. Compactness gives a finite net. Thus some k<=N and integer V in the required congruence have log2(q)+V-k log2 3 in the log interval with a fixed interior margin. Set b=V-E_k. For all q above a fixed threshold the error epsilon_k is smaller than this margin. If also q<=a'X/K_N, then y>=a'X>=q_k, so b>=0. No uniform bound on b is needed.

Now put

    x = r+2^h (y-z)/3^p.

It is a positive integer for large X, refines the prescribed residue, and the whole M-block lies inside [AX,BX]. All M arms have common endpoint y after h steps, reach q_k after b halvings, then reach q. All statements concern actual integer trajectories.

### 3. Counting and bounded multiplicity

For fixed a, take as pool the odd units q>Q in Anc(a) with q<=c0 X, with c0 positive small enough for the preceding bank. The assignment q -> x has bounded multiplicity: x determines y=T^h(x), its odd part determines q_k, and q must be one of the finitely many T^j(q_k) with j bounded by N times the bound on e. This remains true even if some nodes lie on a cycle. Every distinct x supplies an interval of length M. Greedily discard overlapping intervals; any retained interval removes at most 2M-1 possible starting integers.

An elementary pool estimate uses the inverse tree on odd units. For every odd unit v, among e=1,...,6 exactly two satisfy 2^e v=4 or 7 modulo 9. The two children (2^e v-1)/3 are positive odd units, each <=(64/3)v. Their accelerated parent is v. At any fixed depth k the 2^k vertices are distinct because U is deterministic and the two children at each vertex are distinct. Hence there are >=cY^eta distinct odd unit ancestors below Y for all large Y; discarding q<=Q changes only a constant.

For the stronger exponent use the published predecessor estimate of Krasikov and Lagarias, Theorem 6.1, for any fixed a coprime to 3. Their 0.84 lower bound counts ordinary ancestors. Among ancestors n<=Y, if 3|n, strip initial twos to an odd m and apply the first odd shortcut, yielding (3m+1)/2 prime to 3, <=(3Y+1)/2. The orbit has not previously reached a because every earlier input was divisible by 3. If 3∤n, keep n itself. Multiplicity of the conversion is O(log(2Y)): for a given output there is at most one such m and O(log Y) initial powers of 2. For every resulting unit v (even allowed), choose e in [2,7] to obtain a positive odd unit inverse (2^e v-1)/3, <=(128/3)v; multiplicity <=7 since v is one of its first seven iterates. This supplies >=cY^0.84/log(2Y) odd units. Rescaling Y by a fixed constant finishes the local bound. The external theorem is not claimed to be independently verified here.

## Theorem B (weighted stopping-time residues)

For n reaching 1, define W(n) to be the sum of fixed nonnegative integer weights w_e and w_o on the even and odd inputs before the first hit of 1. For n not reaching 1, give it the separate symbol infinity. Fix m>=2 with gcd(m,w_e,w_o)=1. For every residue c modulo m, the conclusion of Theorem A holds with Anc(a) replaced by {n: W(n)=c mod m}, even without assuming Collatz. The pool uses known ancestors of 1. Moreover the block can be required to reach 1 by its supplied actual trajectory.

Use the same synchronizer h,p,r,z and put u=w_o-w_e and P=w_e h+up. Choose all pool q>2 in Anc(1), so the constructed paths cannot visit 1 before q (the 1,2 cycle is closed). Each inverse step above gives W(q')=W(q)+w_e e+u.

Write g=gcd(m,w_e), d0=gcd(m,w_e L), and

    delta(q)=W(q)-w_e ell(q) (mod d0).

This is well-defined since d0 divides w_e L; it also covers w_e=0. An inverse step changes delta by u+w_e j. As j ranges modulo L, w_e j ranges over all multiples of g modulo d0 (d0/g divides L). Because gcd(u,g)=1, choose t in [1,g] so that t u has the desired difference modulo g, then choose j=0 for the first t-1 steps and the final j to reach any desired delta modulo d0. All t inverse exponents are bounded as in Section 2.

Steer q to q_* such that

    delta(q_*)=c-P-w_e ell(z) (mod d0).

The congruences for padding become compatible:

    V=ell(z)-ell(q_*) (mod L),
    w_e V=c-P-W(q_*) (mod m).

Indeed after writing V=ell(z)-ell(q_*)+Lk, solvability is precisely the displayed delta congruence. Their solution set is one residue class modulo K=lcm(L,m/g), including the case w_e=0.

Starting from q_*, append k inverse steps with j=0, restricting k to multiples of m. Total appended clock E_k gives ell(q_k)=ell(q_*)+E_k and W(q_k)=W(q_*)+w_e E_k+uk, with uk=0 modulo m. The same congruences for V=b+E_k now enforce both the endpoint and the final weight, independently of k. Irrational rotation by m log2 3 modulo K gives a finite net of these restricted k. Apply exactly the interval argument of Section 2, now with the extra bounded steering bank included in K_N. The common h-step weighted prefix cost is P, the b halvings add w_e b, and the remaining path has W(q_k); their sum is c modulo m. Multiplicity is still bounded by the total bounded inverse clock after stripping the odd part of y. The ancestor pool of 1 gives the claimed elementary and external exponents. In particular this covers shortcut stopping time (1,1), unaccelerated stopping time (1,2), and number of odd inputs (0,1), modulo every m>=2.

Neither theorem says an arbitrary prescribed source has a terminating trajectory. They manufacture actual blocks in any macroscopic interval while preserving a fixed target, with a quantitative count.