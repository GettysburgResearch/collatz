# A necessary loss for a positive descent renewal

**PRN-001: PROVED-IN-NOTE; the full Collatz closure remains OPEN.** This is a
new elementary norm bound for the stated class of positive operators. It does
not rule out a witness-dependent proof, a sharper estimate on the actual
failure indicator, or a multistep argument.

## Statement

Let A and B be sets of positive integers with B contained in A and natural
densities delta>0 and beta, respectively. Fix 0<c<1. For every k in B,
let w(k,j)>=0 be coefficients indexed by j in A, with

\[
 w(k,j)=0\quad\text{unless }j\le ck,
 \qquad \sum_{j\in A}w(k,j)\ge1.
 \tag{1}
\]

Each row is finite because its allowed indices are bounded. The column
sums below may be infinite. For s>0 define

\[
 K_s=\sup_{j\in A}j^s
       \sum_{k\in B}k^{-s}w(k,j).
 \tag{2}
\]

Then

\[
 \boxed{K_s\ge\frac{\beta}{\delta}c^{s-1}\quad(0<s<1),
 \qquad K_1\ge\frac{\beta}{\delta}.}
 \tag{3}
\]

In particular, if A minus B has density zero, then

\[
 \boxed{K_s\ge c^{s-1}>1\quad(0<s<1),\qquad K_1\ge1.}
 \tag{4}
\]

Finite exceptions to the row conditions can be removed from B without
changing any conclusion. No arithmetic dynamics, probability assumption,
or external density theorem is used.

## Proof

For a set D of natural density gamma, partial summation gives

\[
 \sum_{n\le N,\ n\in D}n^{-s}
 =\frac{\gamma}{1-s}N^{1-s}+o(N^{1-s})\quad(0<s<1),
 \tag{5}
\]

and

\[
 \sum_{n\le N,\ n\in D}\frac1n
 =\gamma\log N+o(\log N).
 \tag{6}
\]

For example, write the counting function as gamma*x+o(x), split its
partial-summation integral at a fixed threshold, and bound the remaining
error by epsilon*x. This also proves that a density-zero set contributes
o(N^(1-s)) in (5) and o(log N) in (6).

If K_s is infinite there is nothing to prove. Otherwise positivity and
(1) give the finite-cutoff estimate

\[
\begin{aligned}
 \sum_{k\le N,\ k\in B}k^{-s}
 &\le \sum_{k\le N,\ k\in B}k^{-s}\sum_{j\in A}w(k,j)\\
 &\le \sum_{j\le cN,\ j\in A}\sum_{k\in B}k^{-s}w(k,j)\\
 &\le K_s\sum_{j\le cN,\ j\in A}j^{-s}.
\end{aligned}
\tag{7}
\]

For 0<s<1, insert (5), divide by N^(1-s)/(1-s), and let N tend to infinity.
This gives beta<=K_s*delta*c^(1-s). At s=1 use (6) and
log(cN)/log N -> 1, obtaining beta<=K_1*delta. These are exactly (3).
If A minus B has density zero, beta=delta and (4) follows. QED.

For the operator (Pf)(k)=sum_j w(k,j)f(j) on k in B, extended by zero on
A minus B, K_s is exactly its positive column norm on
ell^1(A,n^(-s)). Tonelli proves the upper bound, and testing a single
nonzero input coordinate proves equality. Thus (4) excludes a uniform
one-step strict contraction in that norm.

## Application boundary for the PR146 sparse sieve

The source is PR146 at
`fd991063721e9c157d318e40bb20131762f7d750`,
`research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`, the theorem under
the heading **A sparse sufficient set for the directed adjacent-pair test**.
It uses the eligible set

\[
 A=\{k>0:4\nmid k\},\qquad \delta=3/4,
\]

and retains a subset S with

\[
 \#(S\cap[1,N])=O(N^{\rho}/\log(2N)^{3/2}),
 \quad \rho=H_2(\log_3 2)<1.
\]

Every discarded comparison has a sufficient finite list of smaller
comparisons. Their upper starts satisfy

\[
 128j+1<\tfrac58(128k+1),
 \quad\text{hence }j<\tfrac58 k-\tfrac3{1024}<\tfrac58k.
\]

If one constructs a blanket positive renewal that retains at least unit
row mass at every k in A minus S, then (4) gives

\[
 K_s\ge(8/5)^{1-s}>1\quad(0<s<1),\qquad K_1\ge1.
 \tag{8}
\]

The sparse remainder alone therefore cannot pay for a strict one-step
positive contraction while all other source rows retain their mass.

**The nonempty-row hypothesis is essential.** The actual smaller-query
algorithm can return an empty query list when its ordinary part already
proves convergence. We have not proved that these zero-query rows have
density zero. Consequently (8) is not being asserted unconditionally for
that algorithm. Nor is the retained-set count an upper bound for all
genuine failed comparisons: the theorem controls where a global minimum
can occur.

More generally, if the rows retaining unit mass have density beta and
the other rows are killed, (3) gives the necessary condition

\[
 \frac\beta\delta<c^{1-s}
\]

for K_s<1 when 0<s<1. At s=1 it requires beta<delta. These are necessary
conditions, not sufficient estimates on a real operator. Establishing
enough actual killing, or a stronger estimate valid only for the genuine
failure indicator and its supplied upper witnesses, remains a possible
route to a proof.

## What the lemma does not establish

The lemma supplies no upper bound for a Collatz defect energy. It does not
say that a multistep operator cannot be transient, that every weighted norm
must fail, or that signed or witness-indexed transformations cannot close
the problem. It isolates the mass loss that a proposed one-step positive
renewal must prove rather than obtain just from height descent.

The proof and the density-zero strengthening were independently reviewed
by the symbolic-induction agent in this pass. This is an internal
mathematical review, not formal verification or external acceptance.
