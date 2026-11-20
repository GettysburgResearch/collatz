# Complete induced dynamics in the shifted two-prime class

**PROPOSED, SOURCE-QUALIFIED on the explicit two-logarithm estimate stated below.**
This strengthens the class-preserving transition analysis of PR161. It does
not prove convergence after an orbit leaves this class, nor full Collatz.

## Inputs and exact difference from PR161

Use the positive ordinary odd map

\[
U(n)=(3n+1)/2^{v_2(3n+1)},\qquad
\mathcal S=\{2^s3^t-1:s\ge1, t\ge0\}.
\]

The frozen local input is PR161, head
`4a0536b587fc91ee0c7bb1b160c06dda16ddbf23`,
`research/source-rigidity-20261120/SHIFTED_SMOOTH_CYCLES.md`,
SS1--SS4. It proves the seven-element within-class basin, excludes all
cycles in the class except 1, and obtains eventual-confinement closure
using an Evertse S-unit bound. Those conclusions are not new here.

The additional result here is the **complete list of class-preserving
boundary edges**, including every unbounded index. It removes the
possibility of the increasing infinite index path left by SS1 alone and
gives an exact first-exit clock. It uses a different external theorem:
the following explicit Diophantine estimate, which is not re-proved here.

Jeffrey C. Lagarias, *Ternary Expansions of Powers of 2*,
[arXiv:math/0512006v4](https://arxiv.org/pdf/math/0512006v4),
Lemma 2.2(1), equation (2.4), printed pages 10--11, states

\[
\left|\log_3 2-\frac pq\right|
\ge\frac1{1200q^{14.3}}
\quad(q\ge1, p\in\mathbb Z).
\tag{L}
\]

The paper derives this bound from Simons--de Weger and Rhin's
two-logarithm theorem. The exact displayed lemma and its hypothesis were
read in the primary paper. No result for the Erdős ternary-digit
conjecture, no asymptotic-only irrationality measure, and no estimate
with an unstated threshold is substituted for (L).

## Theorem CS1: only three boundary edges stay in the class

Put \(N_k=2\cdot3^{k-1}-1\), \(k\ge1\). Then

\[
U(N_k)\in\mathcal S\quad\Longleftrightarrow\quad k\in\{1,2,4\}.
\tag{1}
\]

The three boundary edges are

\[
1\longmapsto1,\qquad 5\longmapsto1,\qquad 53\longmapsto5.
\tag{2}
\]

**Proof.** Set \(b=v_2(3^k-1)\). The actual boundary transition is

\[
U(N_k)=\frac{3^k-1}{2^b}.
\tag{3}
\]

If its endpoint belongs to \(\mathcal S\), some integers \(s'\ge1\)
and \(t\ge0\) satisfy

\[
3^k+2^b-1=2^{B}3^t,\qquad B=b+s'.
\tag{4}
\]

The elementary valuation identity is

\[
b=\begin{cases}1,&k\text{ odd},\\2+v_2(k),&k\text{ even}.
\end{cases}
\tag{5}
\]

For even \(k\), (5) follows by factoring \(3^{2^v u}-1\) first by
the odd geometric sum and then by successive squarings; the initial
valuation is \(v_2(3^2-1)=3\), and each subsequent factor
\(3^{2^v}+1\) has valuation one. Thus in every case \(2^b\le4k\).

Suppose now \(k\ge128\). Then
\(0<2^b-1<4k<3^k\), so the 3-adic valuation of (4) gives
\(t=v_3(2^b-1)<k\). Write \(K=k-t\ge1\). Also

\[
2^B\le2^B3^t=3^k+2^b-1<3^k+4k<4^k,
\]

and hence \(B<2k\). For completeness, \(3^k+4k<4^k\) holds for
every \(k\ge3\): it holds at 3 and is preserved on multiplying the
exponential part by 3, since
\(3^{k+1}+4(k+1)<3\cdot4^k-8k+4<4^{k+1}\).

Taking natural logarithms of (4) after dividing by \(3^k\),

\[
0<\Lambda=B\log2-K\log3
=\log\left(1+\frac{2^b-1}{3^k}\right)
<\frac{4k}{3^k}.
\tag{6}
\]

Apply (L) with \(p=K\), \(q=B\), and multiply by \(B\log3\).
Because \(\log3>1\), \(B\ge1\), and \(B<2k\),

\[
\Lambda\ge\frac{\log3}{1200B^{13.3}}
>\frac1{1200(2k)^{14}}.
\tag{7}
\]

Together (6)--(7) would force

\[
3^k<4800\,2^{14}k^{15}.
\tag{8}
\]

This is false for every \(k\ge128\). At \(k=128\) the reverse
strict inequality is an exact integer comparison. Moreover

\[
\frac{(k+1)^{15}}{k^{15}}
\le\frac{129^{15}}{128^{15}}<3
\quad(k\ge128),
\]

where the last inequality is also an exact integer comparison. Thus
\(3^k/k^{15}\) strictly increases throughout this range, preserving
the reverse of (8). No approximate logarithms are used in this cutoff.

It remains to check \(1\le k<128\). For each such \(k\), calculate
the positive odd integer \(u=(3^k-1)/2^{v_2(3^k-1)}\), divide
\(u+1\) by its complete powers of 2 and 3, and test whether the
remaining cofactor is one. The complete exact computation in
`check_shifted_smooth_complete.py` returns precisely

| \(k\) | \(b\) | \(s'\) | \(t\) | \(u\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 1 |
| 2 | 3 | 1 | 0 | 1 |
| 4 | 4 | 1 | 1 | 5 |

These entries directly verify (2). This finite complement, together
with the all-size argument above, proves (1). \(\square\)

## Corollary CS2: exact exit clock and all-time classification

For a source \(n=2^s3^t-1\in\mathcal S\), put \(k=s+t\).
Every exponent-one step with \(s\ge2\) replaces \((s,t)\) by
\((s-1,t+1)\). Exactly \(s-1\) such steps reach \(N_k\).

If \(k\notin\{1,2,4\}\), the first \(s\) states (times 0 through
\(s-1\)) are in \(\mathcal S\), and the time-\(s\) state is
outside it by CS1. Thus its exact first exit time is

\[
\boxed{\tau_{\mathcal S}(n)=s=v_2(n+1).}
\tag{9}
\]

For \(k\in\{1,2,4\}\), listing the positive exponent pairs gives
exactly

\[
\boxed{1,3,5,15,23,35,53.}
\tag{10}
\]

Their paths all reach 1, the longest being
\(15\to23\to35\to53\to5\to1\). Consequently every source in
\(\mathcal S\) either exits at the explicit clock (9) or is one of
the seven sources already classified in PR161. No infinite increasing
class-preserving path exists. In particular eventual confinement to
\(\mathcal S\) implies arrival at 1 without invoking Evertse's bound.

This is an exact description of the subgraph induced by
\(\mathcal S\). It does not assert convergence of any source after
its first exit. For example, the exit can increase the original source:
\(7\to11\to17\to13\), with the first three states in the class,
leaves at 13, which is larger than 7.

## Corollary CS3: an effective outside-visit count

Retain the notation \(n_j=U^j(n_0)\),
\(a_j=v_2(3n_j+1)\), and \(q_j=R_{\{2,3\}}(n_j+1)\).
For a finite prefix put

\[
D_N=\#\{0\le j<N:a_j\ge2\},\qquad
C_N=\#\{0\le j\le N:q_j>1\}.
\]

If \(n_0,\ldots,n_N\) are pairwise distinct, then

\[
\boxed{D_N\le2C_N+2.}
\tag{11}
\]

Indeed a defect with both endpoints in \(\mathcal S\) starts at
one of \(1,5,53\) by CS1. The source 1 cannot occur on a simple
prefix containing that outgoing edge, since its endpoint is also 1.
The other two edges occur at most once each. Every remaining defect
touches a vertex outside \(\mathcal S\), and each such vertex is
incident to at most two edges. This proves (11). The additive two is
attained by the simple segment \(53\to5\to1\), so it cannot be
removed for arbitrary simple prefixes.

On any orbit that never reaches 1, none of \(1,5,53\) can occur,
so the stronger occurrence bound holds for every \(N\), even if
the orbit is periodic:

\[
\boxed{D_N\le2C_N.}
\tag{12}
\]

The elementary defect clock can be reconstructed without a unit
equation theorem. Set
\(h_0=\log_2(n_0+1)\), \(\gamma=\log_2(3/2)\), and
\(\alpha=\log_2 3=1+\gamma\). The shifted recurrence

\[
2^{a_j}(n_{j+1}+1)=3(n_j+1)+2^{a_j}-2
\]

gives \(n_{j+1}+1\le(3/2)(n_j+1)\), and therefore
\(\log_2(n_j+1)\le h_0+\gamma j\). If \(R_i\) is the time
just after the \(i\)-th defect and \(R_0=0\), the next defect
finishes exactly \(v_2(n_{R_i}+1)\) odd steps later. Consequently

\[
R_{i+1}\le\alpha R_i+h_0,
\qquad R_i\le\frac{h_0}{\gamma}(\alpha^i-1).
\]

Since \(N<R_{D_N+1}\), it follows that

\[
D_N\ge\left\lfloor\log_{\alpha}
  \left(1+\frac{\gamma N}{h_0}\right)\right\rfloor.
\tag{13}
\]

Combining (12) with (13) gives every counterexample the effective
finite-prefix restriction

\[
\boxed{C_N\ge\frac12\left\lfloor\log_{\alpha}
  \left(1+\frac{\gamma N}{h_0}\right)\right\rfloor.}
\tag{14}
\]

This strengthens PR161's bound by removing its enormous subtractive
constant \(B_2\) and its Evertse dependency for this specific class.
The asymptotic threshold
\(\liminf C_N/\log N\ge1/(2\log\alpha)\) is the same previously
obtained threshold, not a new one. No incompatible upper bound on
\(C_N\) follows from (14).

## Why this does not close the latest PR146 target

PR146 at `e238c63a5d57f96bb063b7472498d1977df51951`,
`research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`, reduces its first
nonempty antecedent rank to convergence of \(3^{27j-1}\), \(j\ge1\).
Neither (1) nor (9) controls those powers' complete subsequent orbits.
More generally, leaving a shifted-smooth class creates a new cofactor,
and (L) does not bound the number or future evolution of such cofactors.

The proposed global arithmetic argument would need an additional
source-persistent restriction on those new cofactors, or a descent after
the exit. The elementary prime-support peak bounds in PR159 and the
ordered prime-height budgets in PR160 are lower complexity requirements
for a counterexample; they do not supply that upper restriction. The
full Collatz proof therefore remains open at that step.
