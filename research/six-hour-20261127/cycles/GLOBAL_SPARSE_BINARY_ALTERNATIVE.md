# A global density alternative for deep canonical grades or valuations above two

Let a primitive positive rational Collatz cycle have odd period P, common reduced denominator d, and positive valuations e_i. At a maximizing cut of E_i−iθ, θ=(Σe_i)/P, put z_i=⌊iθ⌋−E_i≥0. With c=10⁻⁸, every sufficiently large such cycle satisfies

$$
 d>P^c \quad\text{or}\quad
 \#\{i:z_i\ge2\ \text{or}\ e_i\ge3\}>cP .
 \tag{1}
$$

The assertion under the logarithm-ratio input μ(log₂3)≤3 is uniform in the maximizing cut. It has no prescribed height, real-width, or valuation cap. For ordinary cycles it gives the second alternative, and for binary-valued ordinary cycles it forces positive density of canonical grades at least two. Arbitrarily high actual grades and arbitrarily large valuations are admitted elsewhere. The assertion is ineffective. It does not rule out cycles satisfying the second alternative.

We use the certified full binary fifth moment of FIFTH_POSITIVE_CERTIFICATE.md, its located source transfer in FIFTH_MOMENT_SOURCE_REDUCTION.md, the imported fixed-place Subspace Theorem behind Weaver 145 Lemma 4, and arXiv:2610.28079v1 Theorem 11.1 for the final exponent comparison. Weaver 145 Theorem 3 treats sparse excess above canonical grade one with unrestricted valuations, giving a located exponent 11/25 and a density-or-slope-approximation alternative. Its source-shift transport and terminal-lift analysis, and the later SPARSE_REAL_DEPTH_ALTERNATIVE.md, are antecedents. The present result uses the stronger binary local moment and conditions on both sparse high grades and sparse nonbinary transitions. It changes the resulting conclusion on denominators and on ordinary cycles.

## Repair of the whole cyclic word

Assume on a sequence P→∞ that d≤P^c and B={i:z_i≥2 or e_i≥3} has size at most cP. At grade z_i≤1 the rooted cycle identity gives

$$
 N_i=d x_i\le Y:=4d/(2^\theta-3).
$$

Indeed the rotated partial valuation sum at length j is at most jθ+1+z_i, so summing the geometric upper bound on every carry term and dividing by the cycle multiplier gives x_i≤2^{1+z_i}/(2^θ−3). Distinct primitive numerator phases give Y≥(1−c)P. Therefore θ→λ=log₂3 and Y→∞. For large P the mechanical gaps m_i=⌊(i+1)θ⌋−⌊iθ⌋ belong to {1,2}, with neither two consecutive ones nor three consecutive twos, including across the cyclic seam. This follows from 3/2<θ<5/3 and the floor counts on two and three letters.

Clip each grade to b_i=min(1,z_i). For m_i=1, positivity of e_i=m_i+z_i−z_{i+1} gives b_i≥b_{i+1}. For m_i=2 the desired inequality b_i≤b_{i+1} can fail only at a site e_i≥3. Orient the mechanical-two edges i→i+1 and the mechanical-one edges i+1→i. Let u_i be the minimum of b over all vertices reachable by a directed path starting at i, including i itself. Each directed path on this cycle travels in a single chronological direction; the runs of equally oriented edges have length at most two. The repaired bits obey every required weak inequality and hence produce valuations m_i+u_i−u_{i+1} in {1,2}. If b_i=1 but u_i=0, a directed path from i crosses a bad edge. Only a mechanical-two edge can be bad, and its initial vertex j has e_j≥3. The path has at most two edges, so i=j or i=j−1 cyclically. Thus the changed-grade set D={i:z_i≠u_i} is contained in B∪(B−1); we use the looser bound |D|≤3cP.

## A translated original source on a common modulus

Take η=10⁻⁶, τ=1/2000000 and b=⌈((5+η)/(4+η))(log₂Y+3)/θ⌉. At least (1−6c−3c/τ)P distinct starting slots have neither endpoint i,i+b in D and at most τb changed grades strictly between them. This uses the two endpoint exclusions and Markov's inequality on the cyclic incidence count, valid for b>P as well. All retained starts have z_i=u_i≤1, so their numerators are ≤Y.

Rebase a retained window, put M_j=⌊jθ+t⌋ with 0≤t<1, and write z_j,u_j for its local grades. Its actual and repaired local dates are

$$
 A_j=M_j+z_0-z_j,\qquad \widetilde A_j=M_j+u_0-u_j .
$$

Both date systems start at zero and satisfy A_b=\widetilde A_b=K since z₀=u₀ and z_b=u_b. In particular K=bθ+O(2). Fix the ordinary floor cell of t, the two endpoint bits and the changed positions. At each changed position record both z_j and u_j. Once this profile is fixed, all A_j−Ã_j vanish outside the record and both dates are known at each recorded position. Modulo the actual 2^K, the starting numerator consequently satisfies the exact translation

$$
 N_i\equiv -d\sum_{j<b}2^{\widetilde A_j}3^{-j-1}+C
 \pmod{2^K},\qquad
 C=-d\sum_{j\in D\cap(0,b)}(2^{A_j}-2^{\widetilde A_j})3^{-j-1}.
 \tag{2}
$$

All 3-powers here are inverted modulo this same dyadic modulus. In particular (2) transfers location before any Fourier operation. For a fixed record, each actual source requires a repaired binary path in a *single translated interval* of length Y/2^K on the source circle. A word and the fixed translation determine at most one numerator in [1,Y], as 2^K>Y. We enlarge to the complete binary path language at the outset, and then count paths in that translated interval via the nonnegative Fejér majorant. No inequality between fractional moments of a selected path subset and its superset is used. The exact common entrance and terminal grades avoid a terminal-lift cost. The source-segment treatment now uses only the ordinary binary dates and its regular bounded-width placement; no large raw interior date appears in its separation test.

The profiles cost at most exp((H(τ)+5τ ln2)b) up to a polynomial in b. There are at most exp(H(τ)b) choices of a subset of size q≤τb. For a marked run of length ℓ, its preceding raw grade is an unmarked bit, which costs at most two to record. At each of its ℓ sites j, the integer v_j=1+z_{j-1}−z_j is nonnegative because z_j≤z_{j-1}+1; this follows from m_{j-1}≤2 and e_{j-1}≥1. Across the run Σv_j≤ℓ+1. Thus there are at most binom(2ℓ+1,ℓ) raw lists after fixing its preceding bit, by stars and bars. This is at most 2^{2ℓ} by the adjacent-binomial identity in row 2ℓ. Each repaired grade at a changed site costs one bit. These costs combined are at most 2^{4q}, and the stated 2^{5q} suffices. A large negative grade jump causes no unrecorded multiplicity.

## The strict margins

For the five segments set h=⌊K/(5+η)⌋ and a=⌊(1−η)h/θ⌋. In the Fourier sampling proof the difference tested by the Subspace Theorem is dk with |k|≤8a2^{(1−η)h+O(1)}. Because Y≥(1−c)P, we have log₂d≤(c(4+η)+o(1))h and c(4+η)<η/2. This leaves exponential separation slack for the imported theorem. The source interval may have any translation, as the phase in the Fourier majorant has modulus one. The moment for every complete binary segment has exponent γ=4/3−1/10000 in base 3 for all large P by the strict margin of FIFTH_POSITIVE_CERTIFICATE.md. The number of phase types and endpoint/exterior choices costs O(b) times 2^{b−5a+6}. Applying the five-segment bound to every repaired profile gives

$$
 \limsup\frac{\log P}{\log Y}
 \le C_*=
 \frac{6η/λ+γ(1−η)+(5+η)(H(τ)+5τ\log2)/\log3}{4+η}.
$$

Here H denotes binary entropy in nats. The crude bounds λ>3/2, ln3>1 and H(τ)+5τ ln2≤21τ follow from ln(2000000)<15, ln2<1. For the first logarithm comparison one may use e>8/3 and 8¹⁵>2000000·3¹⁵. Therefore

$$
 C_*\le\frac{2666577000221}{8000002000000},\qquad
 1-(3+c)\frac{2666577000221}{8000002000000}
 =\frac{27097267122999779}{800000200000000000000}>0.
$$

On the other hand μ(λ)≤3 implies θ−λ≥P^{-3-o(1)} with constants absorbed in the logarithmic asymptotic, since the reduced denominator of θ is at most P. Hence limsup log Y/log P≤3+c, contradicting the strict product margin. This proves (1). The same argument with d=P^{o(1)}, |B|=o(P), and profile costs exp(o(b)), gives the source-only height exponent (2) of the fifth certificate for the clean local cap Y, before any logarithm-ratio input.

The independent finite control sparse_binary_global_check.py tests whole-clock directed repair, actual valuation differences and global source translation on 679 cyclic grade words. It verifies 10,722 translated dyadic residues including repeated windows and two odd drifts. Omitting the translation fails on every tested changed window, while clipping alone leaves a violation on 591 complete words. The controls include 607 windows reaching grade three or higher; the written encoding proves the bound for all grades.
