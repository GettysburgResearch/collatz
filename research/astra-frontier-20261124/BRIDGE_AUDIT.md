# Collision signs and ordinary prefixes ending at a prescribed target

**Status.** The two collision estimates are consistent. The finite-word theorem below is an independent written deduction. Its quantifiers identify an obstruction to deriving a collision lower dimension for one fixed escaping orbit. Neither escape nor nonstandard cycles are excluded. No historical priority claim is made.

## Which way the inequalities point

Let \(U(q)=(3q+1)/2^{v_2(3q+1)}\) on positive odd integers. For one injective orbit \(q_j=U^j(q_0)\), write \(\pi_M=(M+1)^{-1}\sum_{j=0}^M\delta_{q_j}\) and \(\mathrm{Col}_m(\pi)=\sum_{a\bmod 3^m}\pi(a)^2\). Put \(\ell=\log_2 3\) and \(\theta=[\ell\log\ell-(\ell-1)\log(\ell-1)]/\log 3\approx0.949955527\).

* PR185, Theorem 3, proves \(\mathrm{Col}_m(\pi_M)\ge c\sqrt m\,3^{-\theta m}\) when \(m^2=O(M)\). Under its source-qualified ordinary harmonic flow, the same direction holds for every moving inverse law \(\zeta_{M,r}\). Its exact endpoint mass at \(q_j\) is \(v_j/[(M+1)v_{j+r}]\), and \(\sup_r\|\zeta_{M,r}-\pi_M\|_{\rm TV}\to0\). Equation (20) gives the *open target* in the opposite direction. [PR185, Theorem 3 and equation (20)](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/central-closure-20261123/COLLISION_LOGARITHMIC_GAIN.md#L302-L378) · [exact endpoint comparison](https://github.com/GettysburgResearch/collatz/blob/2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d/research/rigidity-closing-20261122/SAME_SOURCE_INVERSE_ENTROPY.md#L100-L138).
* PR189 S1 proves in writing that each ternary empirical limit \(\mu\) of that orbit satisfies \(\limsup_m-\log\mathrm{Col}_m(\mu)/(m\log 3)<\theta\). Hence eventually \(\mathrm{Col}_m(\mu)\ge3^{-(\theta-\delta_\mu)m}\) for a positive \(\delta_\mu\). The stationary gap process has mean at most \(\ell\). Its entropy rate either falls strictly below the geometric maximum or attains that maximum and is iid geometric. In the latter case its word collision is \((2\ell-1)^{-m}\); grouping words by endpoint increases collision. [PR189 S1](https://github.com/GettysburgResearch/collatz/blob/a0be70b1ffa075cbc50755ac76036108c028d120/research/stationary-carry-rigidity-20261124/README.md#L48-L144).

At each fixed \(m\), projection to \(\mathbb Z/3^m\) is continuous, so the first lower bound passes to the limit and agrees with the second. Injectivity makes the empirical measures escape all finite sets of ordinary positive integers. Compactness on \(\mathbb Z_3\) recovers residue laws. The ordinary positive integers are dense there. For instance, uniform measures on \(-1+3^{\lfloor\sqrt j\rfloor}\mathbb Z_3\) have \(\mathrm{Col}_j=3^{-j+\lfloor\sqrt j\rfloor}\) and converge to the point mass at \(-1\). A moving-precision upper bound alone cannot be transferred to the dimension of its weak limit. An upper bound *at the rate and scales in PR185 equation (20)* would already contradict PR185 directly.

A precise compactness target is available. There exists a weak limit with upper collision dimension at least \(\theta\) if and only if there are \(m_j\uparrow\infty\), positive \(\epsilon_j\downarrow0\) and \(M_k\uparrow\infty\) such that simultaneously for \(1\le j\le k\),

\[
\frac{\#\{(u,v)\in[0,M_k]^2:3^{m_j}\mid q_u-q_v\}}{(M_k+1)^2}
\le 3^{-(\theta-\epsilon_j)m_j}+1/k .
\]

Take a weakly convergent subsequence to pass each fixed constraint to the limit. Conversely, select sufficiently good increasing scales for the given limit, then approximate its first \(k\) residue laws along its actual subsequence. The existence of these simultaneous ordinary pair estimates for an escaping source is open.

## Finite trajectories with arbitrary terminal component

**Theorem.** Let \(w=(a_0,\ldots,a_{n-1})\) be any finite word of positive integer gaps, including the empty word. Let \(m\ge0\), \(u\bmod3^m\) be arbitrary, and \(t\) be any positive odd integer coprime to three. Infinitely many positive odd ordinary starts \(x\equiv u\bmod3^m\) execute exactly \(w\), and then a single step of gap \(r\) to \(t\). The allowed positive \(r\) form one arithmetic progression outside a finite initial segment.

**Proof.** Put \(A_i=\sum_{j<i}a_j\), \(A=A_n\), \(C=\sum_{i<n}3^{n-1-i}2^{A_i}\). Write \(Q=(2^r t-1)/3\) for the last state of the word. The full affine equation \(2^A Q=3^n x+C\) gives

\[
x=\frac{2^{A+r}t-2^A-3C}{3^{n+1}}.
\]

Prescribe the source class by

\[
2^{A+r}t\equiv 2^A+3C+3^{n+1}u\pmod{3^{n+m+1}}.
\]

The right side is congruent to \(2^A\bmod3\). Both sides have unit coefficients. The order of \(2\) modulo \(3^h\) is \(2\cdot3^{h-1}\). For completeness, \(v_3(4^{3^j}-1)=j+1\) by factoring \(X^3-1\) for \(X\equiv1\bmod3\). The factor \(X^2+X+1\) has ternary valuation exactly one. Thus the order of \(4\) is \(3^{h-1}\). The sign of \(2\bmod3\) and the size of the unit group give the claimed order of \(2\). Consequently \(r\) lies in one class modulo \(2\cdot3^{n+m}\), with arbitrarily large representatives. Such an \(r\) yields positive integral \(x\) in the required class. The equation modulo three gives \(Q\in\mathbb Z\).

For the intermediate steps, split \(C=3^{n-i}C_{0,i}+2^{A_i}C_{i,n}\), using relative exponents in each subword carry. Then

\[
2^{A_i}(2^{A-A_i}Q-C_{i,n})=3^{n-i}(3^i x+C_{0,i}).
\]

Since \(2^{A_i}\) is a ternary unit, \(x_i=(2^{A-A_i}Q-C_{i,n})/3^{n-i}\) is integral. Adjacent subwords give \(3x_i+1=2^{a_i}x_{i+1}\). All \(x_i\) are positive for sufficiently large \(r\). The number \(x_n=Q\) is odd for \(r>0\), and the backward equations make all predecessors odd. Each valuation is therefore exactly prescribed. The final equation \(3Q+1=2^r t\) has exact valuation \(r\). The starts strictly increase with \(r\).

## An explicit collision-one family that reaches one

For \(N,m\ge0\) put \(d=2^{3^{N+m}}+1\), \(r=3^{N+m}+1\), and

\[
q_0=2^{N+1}\frac{d}{3^{N+1}}-1,\qquad
q_i+1=2^{N+1-i}3^i\frac{d}{3^{N+1}}\quad(0\le i\le N).
\]

The identity \(v_3(2^{3^j}+1)=j+1\) follows from \(X^3+1=(X+1)(X^2-X+1)\), with \(X^2-X+1\equiv3\bmod9\) for \(X\equiv-1\bmod3\). Thus the \(q_i\) are positive odd integers and \(v_3(q_i+1)=m+i\). The first \(N\) gaps are one since \(3q_i+1=2q_{i+1}\) with odd endpoint. In particular \(q_{i+1}>q_i\). The last state satisfies \(q_N=(2^r-1)/3\), so \(U(q_N)=1\) with gap \(r\). All \(N+1\) distinct states lie in the single residue \(-1\bmod3^m\), giving \(\mathrm{Col}_m(\pi_N)=1\).

The entire trajectory has known actual scalar. From the gaps \(1^N,r,2,2,\ldots\),

\[
h(q_0)=\frac{1-3^{-N}}2+\frac{r+1}{3^{N+1}}
=\frac12+3^{m-1}+\frac{1}{2\cdot3^{N+1}}.
\]

For \(m\ge1\), at \(0\le i\le N\) the integer carry is \(3^{i+m-1}\), and the centered fractional phase is \(1/(2\cdot3^{N-i+1})\). Thus its first \(N+1\) *canonical* \(b\)-digits also equal one, including the time of the large physical gap.

If an escaping component exists, take any ternary-unit \(t\) on it in the general theorem, \(w=1^N\), and \(u=-1\). The whole orbit of the new source is then injective, and the designated \(N+1\) states still have collision one. Specifying an eventual component leaves freedom for arbitrary finite prefixes. The sources vary with \(N,m\). Appending a finite history preserves the limiting time distributions of each fixed future. The example therefore rules out a source-uniform finite estimate; the fixed-source asymptotic estimate remains open.

## Rational phases

PR188's carry cocycle bounds physical running height in terms of canonical drawup. PR182 round 12 strengthens this with entire-prefix divergence \(P_N=3^N/2^{\sum b_i}\to\infty\) for an injective orbit. At a rational phase of period \(L\) and mean \(\beta\), \(P_{jL}=(3^L/2^{L\beta})^j\). Since \(\ell=\log_2 3\) is irrational, the two signs are strict. For \(\beta>\ell\), contraction gives a finite classifier for the supplied phase, including a phase-dependent cycle bound. For \(\beta<\ell\), \(P_{jL}\) grows exponentially. The polynomial running-height lower exponents \(6.1874\ldots\) for the \(7/8\) phase and \(166.2319\ldots\) for the \(729/1456\) phase coexist with the available exponential upper bounds. No argument here makes the actual scalar rational or makes a low phase contract. [PR188, SC1–SC3](https://github.com/GettysburgResearch/collatz/blob/beed685ab713923191ae40c9559bf7400298d2d3/research/scalar-carry-cocycle-20261124/SCALAR_COCYCLE.md#L21-L72) · [PR182, R12-1–3](https://github.com/GettysburgResearch/collatz/blob/cbec52dde5bed390a693310dd04e911033ba0cc9/research/phase-packing-round12-20261124/README.md#L53-L294) · [PR189, F1–F6](https://github.com/GettysburgResearch/collatz/blob/a0be70b1ffa075cbc50755ac76036108c028d120/research/stationary-carry-rigidity-20261124/FINITE_PHASE_ENTROPY.md#L85-L184).

The scoped errata distinguish an injective positive orbit, finite realizations and one stabilized root. [E-INTEGRATION-003, E-D-002, E-D-007](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/integrated/ERRATA.md#L21-L82).

## Replay

The independent exact Python control covers 85 words of length at most three over gaps 1 through 4, five targets, all starting residues modulo \(3^m\) for \(0\le m\le2\), and two exponents per progression. Its 11,050 ordinary witnesses all executed the literal gaps and target step. The explicit family passed all 55 pairs \(0\le N,m\), \(N+m\le9\), and 165 actual canonical digit checks. Normal and optimized Python produced identical counts.
