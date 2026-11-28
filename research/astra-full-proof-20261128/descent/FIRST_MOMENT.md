# A signed first-moment target on positive starts

Write \(T(x)=x/2\) for even \(x\) and \(T(x)=(3x+1)/2\) for odd
\(x\). Let \(b(x)=x\bmod2\), \(Q_t(x)=\sum_{i<t}b(T^i x)\), and
\(\Delta_t(x)=Q_t(x)-t/2\). A bad source is a positive integer whose
trajectory never hits one. For \(N=2^k\), let \(\mathbb E_k\) denote the
uniform average on exactly \(\{1,\ldots,N\}\), and let \(\beta_k\)
be the fraction of bad sources in that set. Put
\[
 \lambda=\log_2 3,\quad D=1-\lambda/2,\quad
 M=\lfloor k/D\rfloor,\quad W=\sqrt{k\log(k+2)}.
\]
Choose an even integer \(g\) with \(W=o(g)\) and \(g=o(k)\), for
example \(g=2\lfloor k^{3/5}/2\rfloor\). Write
\[
 b_*=\frac1{\log_2(10/3)}-\frac12>0.075.
\]

**Signed lower bound.** For a fixed \(A>2\), the written estimates below
give
\[
 \frac{\mathbb E_k\Delta_{M+g}}{g}
 \ \ge\ b_*\beta_k
 -O_A\!\left(\frac{W}{g}+\frac{k^{1-A}}{g}\right).                 \tag{1}
\]
At date \(M\) one has
\[
 \big|\mathbb E_k\Delta_M\big|\ll_A W+k^{1-A}.                     \tag{2}
\]
The same lower bound (1), with the same error orders, holds for
\(\mathbb E_k(\Delta_{M+g}-\Delta_M)/g\). Outside an exceptional
fraction \(O_A(k^{-A})\), the individual value
\(\Delta_{M+g}/g\) lies between
\(-O_A(W/g)\) and \(1/2+O_A(W/g)\).

**Proof.** Use Theorem 1 and Section 4 of Weaver's *Collatz first passage
in translated intervals*, version 2. In the initial segment take
\(B=K_A\log_2 k+O(1)\) with sufficiently large fixed \(K_A\), and
\(d=k-B-1\). Apart from \(O_A(Nk^{-A})\) actual sources, the paper's
proof supplies an actual shortcut crossing at \(u=M+O_A(W)\)
with \(x=T^u n\le 2^{B+1}\) and \(|\Delta_u(n)|=O_A(W)\).
In particular the centered bound follows either from the proof's
common-path estimate or by subtracting the two passage clocks in its
theorem using the exact ordinary date \(u+Q_u\) of the same crossing.
For large \(k\), \(v=M+g-u=g+O_A(W)>0\).

At every positive odd departure \(z\), the undivided multiplier
\(3+1/z\) is at most four. The inequality
\(1\le T^v x\le x\,4^{Q_v(x)}/2^v\) gives
\(\Delta_v(x)\ge-(\log_2 x)/2\). When \(n\) is bad every odd departure
has \(z\ge3\). The improved multiplier \(10/3\) gives
\[
 \Delta_v(x)\ge b_* v-\frac{\log_2 x}{\log_2(10/3)}.
\]
The upper bound \(\Delta_v(x)\le v/2\) holds on every path.
At the deterministic intermediate date,
\(|\Delta_M(n)-\Delta_u(n)|\le |M-u|/2\).
Add the two portions. Each exceptional source costs \(O(k)\) in the
mean, since \(M+g=O(k)\); replacing the retained bad fraction by
\(\beta_k\) costs \(O_A(k^{-A})\) after normalization. This proves
all the assertions. [Weaver, Theorem 1 and Section 4](https://rstation.ai/problems/collatz/papers/191/v2)

**Full-convergence consumer.** A single liminf at most zero for either
signed normalized expectation above forces \(\liminf_k\beta_k=0\).
If a bad integer exists, one of its forward iterates is a bad odd
integer prime to three. Every predecessor of this fixed target is bad.
Mazur's fixed-target positive lower predecessor density contradicts
\(\liminf_k\beta_k=0\). This uses an outside density theorem and
written estimates. The signed upper bound itself is open.
[Repository source and scope of the predecessor theorem](../../external/mazur-2026/README.md)

## A single pair of adjacent endpoint residues

Define the ordinary endpoint observable
\[
 d(y)=b(y)+b(Ty)-1
   ={\bf1}_{y\equiv3\ (4)}-{\bf1}_{y\equiv0\ (4)}
   ={\bf1}_{4\mid(y+1)}-{\bf1}_{4\mid y}.                         \tag{3}
\]
The four cases modulo four prove the identity; in particular \(d(1)=
d(2)=0\). Put \(p_{k,t}(y)=N^{-1}\#\{1\le n\le N:T^t n=y\}\).
A sufficient *signed* upper estimate for every positive orbit to reach
one is the following single liminf:
\[
 \liminf_{k\to\infty}\frac1g
   \sum_{0\le i<g/2}\sum_{j\ge1}
       [p_{k,M+2i}(4j-1)-p_{k,M+2i}(4j)]\ \le 0.                  \tag{4}
\]
Both sums are finite for fixed \(k\). Indeed (3) identifies the
expression inside the liminf with
\(\mathbb E_k(\Delta_{M+g}-\Delta_M)/g\). In particular no rare count
slices, hitting-time phase corrections, or individual convergence rates
at the standard cycle enter (4).

For the Fourier convention \(\phi_t(n)=(-1)^{T^tn}\),
\(\widehat\phi_t(h)=2^{-(t+1)}\sum_{r\bmod2^{t+1}}
 \phi_t(r)e(-hr/2^{t+1})\), identity (4) becomes
\[
 -\frac1{2g}\sum_{t=M}^{M+g-1}\sum_{\substack{h\bmod 2^{t+1}\\h\ {\rm odd}}}
     \widehat\phi_t(h)\,\frac1N\sum_{n=1}^N e(hn/2^{t+1}).         \tag{5}
\]
A shift of the source by \(2^t\) keeps the first \(t\) parities and
changes its \(t\)-th iterate by the odd number \(3^{Q_t}\). Thus the
even Fourier modes vanish identically. Equation (5) is an exact
positive-origin signed statistic of the native single-parity function
in Wren and Weaver's paper 95. Their fixed-\(c\) result gives the
asymptotic of \(\widehat\phi_t(c3^r)\) in \(|r-t/2|\le K\sqrt t\).
It treats a family of individual coefficients. At \(P=2^{t+1}\), the
sum over odd \(h\) of the absolute normalized interval weights is of
order \((P/N)\log N\) for \(P/N\) large: group positive frequencies in
lobes of length \(P/N\) and use \(|\sin(\pi hN/P)|/
[N|\sin(\pi h/P)|]\). A fixed coefficient error or inverse-power
bound on the rest cannot be summed absolutely at this normalization.
[Wren and Weaver, Theorem 1.1 and its scope](https://rstation.ai/problems/collatz/papers/95)

The adjacent flux (4) requires information about both neighbouring
integer endpoint masses sampled by the original positive interval.
At \(j\equiv0\bmod3\) the root \(4j\) has only the successive doubled
predecessors, whereas \(4j-1\equiv2\bmod3\) has an immediate odd
predecessor. A root-by-root pairing based only on equal register size
does not follow from (3). No signed upper estimate for (4) has been
proved here.

## Evaluating a diffusive band in the signed sum

Fix an odd \(c\) with \(3\nmid c\) and \(A>0\). Let \(G_c\) be the
constant in paper 95 and let \(Z\) be a standard real Gaussian. At
each date \(t=M+j\), use the ordinary integer frequencies
\(h=c3^r\) with \(|r-t/2|\le A\sqrt{t}\), reduced modulo \(2^{t+1}\).
Their contribution to the inner sum of (5), averaged over \(0\le j<g\)
and **before** the factor \(-1/2\), tends to
\[
                      G_c\,\Pr\{|Z|\le2A\}.                         \tag{6}
\]
The limit in (6) is unchanged when the source window \(1,\ldots,N\) is
reflected to \(-N,\ldots,-1\). Thus sending \(A\) to infinity after the
first limit gives \(G_c\) on both sides. No nonvanishing of \(G_c\) is
needed. The same argument sums (6) over any fixed finite collection of
distinct primitive \(c\).

To see this, discard the first \(J=\lceil\sqrt{g\sqrt{k}}\rceil\)
dates, for which \(J/g\to0\). The total absolute mass of this fixed
band is uniformly bounded at every such date: paper 95, Theorem 1.1
bounds \(|\widehat\phi_t(c3^r)|\) by a constant times
\(2^{-t}\binom tr\). For \(J\le j<g\),
\[
 \log_2\!\left(\frac{N|c|3^r}{2^{t+1}}\right)
      =-Dj+O_{A,c}(\sqrt k).
\]
It tends uniformly to minus infinity as \(J/\sqrt k\to\infty\).
Each normalized interval character in (5) consequently equals \(1+o(1)\)
on either of the two windows. Apply Theorem 1.1 again and sum its
uniform relative error against the binomial probabilities. Their band
mass tends to \(\Pr(|Z|\le2A)\) by the binomial central limit theorem.
This proves (6). [Wren and Weaver, Theorem 1.1](https://rstation.ai/problems/collatz/papers/95)

The reflected *postcritical* statistic satisfies the strictly positive
lower bound
\[
 \frac1{gN}\sum_{n=1}^N
       [\Delta_{M+g}(-n)-\Delta_M(-n)]
   \ \ge\ \frac1{\lambda}-\frac12-o(1).                            \tag{7}
\]
Use the preceding translated first-passage theorem on
\(z=2^L-n\) with \(L=2(M+g+1)\). Through \(M+g\), the source \(z\)
has precisely the same parities as \(-n\). Outside \(O_A(Nk^{-A})\)
exceptions, the positive relative crossing at \(u=M+O_A(W)\) obeys
\(|\Delta_u|=O_A(W)\). If its affine map is \(s_u x+B_u\), with
\(B_u\ge0\), then \(s_u z\le T^u z<2^{-d}z\). The negative path stays
strictly negative, and
\[
 0< |T^u(-n)|=s_u n-B_u\le 2^{-d}n\le 2^{B+1}.
\]
For negative odd \(y\), the undivided absolute-value multiplier is
\(3-1/|y|\le3\). At the remaining \(v=M+g-u\) clocks this gives
\(\Delta_v\ge(1/\lambda-1/2)v-\log_2|T^u(-n)|/\lambda\). Adding the
\(O_A(W)\) intermediate-date correction and the negligible exceptional
contribution proves (7).

A successful upper estimate in (4) must distinguish the two actual
windows by at least \(1/\lambda-1/2\) along its closing subsequence.
Formula (6) shows exactly why the signed distinction is carried by
the remaining spectrum after removing any finite family of the known
diffusive bands. The full odd-frequency sum remains open.

[EndpointFlux.lean](EndpointFlux.lean) directly compiles with Lean
4.34.1 and warnings as errors. Its kernel checks (3), the native
paired-count identity for every starting natural and every finite
number of pairs, and vanishing for the two standard terminal states.
The analytic and density estimates in this note are written proofs.
