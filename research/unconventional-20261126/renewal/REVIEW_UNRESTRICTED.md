# Independent review of the logarithmic gauge for unbounded incoming slopes

**Verdict — VERIFIED at the stated pin.** I rederived both strict
sides of the theorem in
[UNRESTRICTED_GAUGE.md](../operator/UNRESTRICTED_GAUGE.md),
SHA-256 `74e455ba41cda2453b4d21a6cc1ef14b3aa04278f6a705f97d2fcf639e5c30c6`.
The problem with the critical power of the logarithm is resolved by a
separate [integral-test proof](INCOMING_GAUGE_TEST.md). The following
checks concern the original proof before that extension.

* The probability of a word under the centered Bernoulli law is
  exactly $3^{-\theta q}e^{hS_k}$, with $h=-\log(1-p)/\log 2>1$.
  At first passage above $L$, the word ends in an odd letter, and
  $q\ge L/\log(3/2)$. These first passages cover the set $X$ even
  when different high-slope scripts at the same ternary target are
  incompatible. They each specify one ternary class of depth $q$.
  Dividing the tilted word probability by $e^{hS_k}$ sums the
  $g_\gamma$ cost by $e^{-hL}\mathbb E\tau_L^\gamma$ for
  $0\le\gamma<1/2$. The one-sided tail integrates as claimed for
  $0<\gamma<1/2$ and tends to zero at infinity, proving passage
  almost surely.
* In the rotation step let $P_j$ be the central partial sums and
  rotate after an index maximizing $P_j$ for $0\le j<m$. Before
  the old endpoint the rotated sums are nonpositive, at the old
  endpoint they are at most $\delta$, and past it they are at most
  $\delta$ again. This argument allows a periodic word, since each
  rotation orbit has size at most $m$. After prefixing $-b$, the
  largest permitted interior height is $-b+\delta\le-a/4$.
  The relevant odd count exists with density $a/(2\log3)>0$ in
  the central lengths, by irrationality of $\log2/\log3$. The
  rounded lower and upper length cutoffs cost only boundedly many
  lengths.
* On $-S_i\in[r,r+1)$ with survival, the reverse last-third sums
  $S_i-S_{i-j}$ are at least $-r-1$. The first and last bounds
  involve disjoint increments, and conditioning on both leaves
  the independent middle block whose final value lies in a unit
  interval. Its spacing is $\log 3>1$ and its largest atom is
  $O(i^{-1/2})$. The upper bound after summing the exponential
  weights is uniform from $i=0$ with $1+i$ in the denominator.
  The expectation on the event $N\le\tau\le2N$ includes the
  future survival through $N-1$ when $i\le N/2$. Therefore it is
  $O(N^{-1/2})$. Dividing this by the lower event probability
  $cN^{-1/2}$ gives a single finite cutoff on the exponential
  occupation, valid for every large $N$.
* A prefix ending inside stage $j$ determines all previous whole
  excursions, since its successive first increases are intrinsic.
  If $r<N_j/2$ then its completion requires survival to $N_j-1$,
  giving a conditional normalizer cost bounded by a constant
  times $1+|S_r^{\rm loc}|$. The bound is valid even when this
  expression is much larger than $\sqrt{N_j}$. If $r\ge N_j/2$,
  the reciprocal event probability is $O(\sqrt{N_j})$. Since
  $\sum_{i\le j}\log N_i\sim\log N_j$, completed normalizer
  costs have the claimed power at the full *native* length $k$.
  A prefix at a stage boundary can use the next empty partial
  stage with normalizer exactly one.
* Stopping exactly at the $q$th odd letter gives a partition of the
  product paths into finite prefixes. Every path has infinitely
  many odd letters by the positive endpoint gains. At fixed
  $k,q$, the last odd index follows from $v_2(A)$, since only the
  last odd summand has that least valuation, and then subtraction
  decodes each earlier one. The affine relation identifies the
  specified ternary class $2^ky\equiv A\pmod{3^q}$. The real
  range of $A/3^q$ is at most $e^{D(q)-S_k}$ with
  $D(q)=O(j+\log(j+1))=o(\log q)$ uniformly over these prefixes.
  This uses the bounded exponential occupation, including in the
  current *partial* excursion. The extra one for the number of
  representatives is absorbed by taking $D(q)$ above the running
  maximal $S_k$. After multiplying by the word bound, the
  remaining $e^{(h-1)S_k}$ sums over $k$ by a geometric series
  on the negative side of the lattice of spacing $\log2$.
  Polynomial factors in $(-S_k)_+$ are harmless there. On the
  positive side $S_k\le D(q)$; no factor $O(q)$ is needed when
  summing clocks. This justifies the claimed exponent.
* The mass estimate on ternary cells implies the asserted
  infinite measure at the larger gauge by the divergent ratio.
  The dense unit seeds $-2^{-j}$ are legal: $j$ inverse doublings
  reach $-1$ and arbitrary inverse odd steps then remain there.
  Since 2 generates each $(\mathbb Z/3^k)^\times$, these seeds
  are dense in the units. Haar nullity follows also from the
  positive codimension. At ordinary positive $y$, every incoming
  slope is at most $y$ by positivity of its positive integral
  source and of its carry.

As a finite control I propagated survival probabilities and cumulative
weighted occupations to native time 1024. The exact decisions use
$3^q>2^k$ for the first hit and
$2\,3^{4q}\ge3\,2^{4k}$,
$8\,3^{4q}\le27\,2^{4k}$ for the terminal height window.
The arithmetic probabilities below use floating point. Columns give
$\sqrt N\Pr(N\le\tau\le2N,\ a/4\le S_\tau\le3a/4)$ and
$\sqrt N\mathbb E[V;N\le\tau\le2N]$. This control tests the
distinction between endpoint conditioning and the unrestricted
first-passage occupation.

| $N$ | Scaled window mass | Scaled occupation |
|---:|---:|---:|
| 16 | .077005 | 1.176634 |
| 32 | .067237 | 1.505815 |
| 64 | .073688 | 1.854601 |
| 128 | .068208 | 2.150678 |
| 256 | .065169 | 2.285147 |
| 512 | .065802 | 2.425629 |

The lower construction supplies a subset with a coherent nested
script. The proof of the upper bound requires no single coherent
script at an arbitrary point of $X$. This audit establishes no
quantitative ordinary diagonal estimate.
