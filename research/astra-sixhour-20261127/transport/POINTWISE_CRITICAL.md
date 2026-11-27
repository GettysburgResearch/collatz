# Critical paired layers at actual upper-certified integers

**Proposed.** For a positive \(X\ge2\) with \(U=3X-1\) reaching 1, let
\[
 s_p(X)=\frac1X\!\!\sum_{\substack{(Y,3Y-1)\to(X,U)\\
                        p\text{ odd departures on each arm}}}
                       3^p2^{-H}.
\]
The sum is over all actual positive sources and clocks; each \(Y\)
occurs at most once because the upper target is transient. There is no
prescribed source-height budget.

## Moving upper-good targets and all odd grades

Let \(A(U)\) be the least positive ordinary ancestor of \(U\) under
the shortcut, allowing time zero. There is an absolute \(\delta>0\)
such that, on the first-landing and density inputs specified below,
\[
           \sup_{p\ge0} s_p(X)\ll A(U)^{-\delta}+1/X.                \tag{1}
\]
In particular the supremum tends to zero along every unbounded
sequence of ordinary upper-good terminals, whether or not the lower
source escapes. This includes upper terminals which are powers of two.

For \(p\ge1\), group each upper path by its initial even count \(a\)
and its final odd departing vertex \(z\). If \(j\ge1\) is the number
of clocks from \(z\) to \(U\), then \(z=(2^jU-1)/3\). All such
positive \(z\) are odd and transient because the target \(U\ge5\)
is transient. Once the initial \(a\) even clocks are stripped, the
first odd state \(w=(3Y-1)/2^a\) reaches \(z\) at odd depth \(p-1\).
Its multiplier \(M'\) on that part of the odd orbit gives exactly
\(M=2^{-a}(3/2^j)M'\). For each \(a,w\) there is at most one
eligible positive \(Y\).

Write \(d_z\) for the natural relative odd predecessor density.
The source-qualified uniform first-hit layer bound
\(L_{p-1}(z)\le C z d_z\) for odd units, including zero depth,
is the first-hit input in [PR200](https://github.com/GettysburgResearch/collatz/blob/ad70a3b831867cb8a74d402a2a1abdc419f5a09b/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md);
see also [Weaver, Paper 12](https://rstation.ai/problems/collatz/papers/12).
After summing \(2^{-a}\), the unit contribution is bounded by
\(C(U/X)\sum_j d_z\), as \(3z/2^j\le U\). If \(3\mid z\) then the
only possible odd depth is \(p-1=0\), and the entire exceptional
contribution is at most \((2/X)\sum_{j\ge1}3/2^j=6/X\).
At grade zero the only rooted word is empty (the initial carry is odd).

Distinct \(z\)'s in this sum have the same next odd vertex, the odd
part of \(U\). Their odd predecessor basins are disjoint because
each \(z\) is transient and no such \(z\) is in the forward orbit
after that common successor. Every such basin visits \(U\) on its
shortcut path. Fix \(F<A(U)\). An odd start that visits \(U\) cannot
land at or below \(F\) before that visit. Its first such odd landing
therefore lies on the ordinary forward orbit of \(U\), or it fails.
Use [the first-landing input](CRITICAL_FLOOR.md) in windows tending
to infinity, and the uniform distinct-orbit bound
\[
          |\operatorname{Orb}_T(U)\cap[1,F]|\ll F^{1-\epsilon}
\]
for some \(\epsilon>0\), allowing the transient prefix and cycle.
The latter follows by the bounded-multiplicity orbit compression
in [PR193, first-hit trace peaks](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/TRACE_PROFILE.md).
Any finite sum of the \(d_z\)'s is then \(O(F^{-\delta})\) for
some absolute \(\delta>0\); take the supremum over finite sets.
Choosing \(F=\lfloor A(U)/2\rfloor\) proves (1). Along large
upper-good \(U\), \(A(U)\to\infty\): the good starts up through any
fixed height form a finite set with a finite union of forward orbits,
and a nongood start cannot visit \(U\).

The earlier PR193 estimate on first-hit layers at odd units outside
all small trajectories supplies the analytic principle. Splitting
at the **last odd departure** handles even \(U\) and unbounded final
halving runs without replacing \(U\) by an odd part of possibly
bounded height. The conclusion controls each critical grade, not
the sum over all grades.

## Source height eliminated in a fixed disagreement trace

Suppose now that \(X\) is nongood. Every starting pair in \(s_p(X)\)
has opposite genuine basin labels and never merges. With the fair
native pair estimate of [PR146](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md),
\[
             \sum_{0\le p\le K}s_p(X)
                     \ll (1+\log(2X)+K)^{1/2}.                      \tag{2}
\]
Indeed there are \(O(Z/\sqrt{\log(2Z)})\) possible initial \(Y\)'s
per ordinary octave \([Z,2Z)\), by covering it by a bounded number
of complete binary grids of depth \(\lfloor\log_2 Z\rfloor\) and
using nonfusion. Each contributes at most \(1/Y\) by the positive
physical source formula. Their total up to \(X e^{C(K+1)}\) has
the bound in (2).

For a larger source, \(Y\le 2^H X/3^p\) implies
\(H>C(K+1)/\log2\). Dropping all constraints but its lower binary
word, at fixed \(H,p,X\) there are at most \(\binom Hp\) possible
sources. With \(p\le K\) and \(C\) large enough,
\[
     \sum_{p\le K}{H\choose p}3^p2^{-H}\le e^{-cH}
\]
by the binomial entropy bound (choose \(K/H\) sufficiently small
first). Summing over these clocks gives \(O(e^{-cK}/X)\).
Thus at every fixed actual disagreement target the all-source
critical layers have vanishing Cesàro mean, in contrast with the
positive source-qualified critical mean in the individual lower
inverse tree at an odd unit. The fixed-source upper certificate
does not yet make the series in (2) summable.

## Fair rooted mass without heights

The normalized Haar integral of the contextual all-clock inverse
sum is finite at the critical weight:
\[
                  \sum_{\rm rooted\ words}3^{-p}M
                  =\sum_{\rm rooted\ words}2^{-H}\le16 .
\]
At each fresh fair root visit the lower 4-bit word with initial
ordinary residue \(3\bmod16\) merges on its fourth clock and
contains no intermediate return to the starting root. Its chance
is \(1/16\). Induction under fresh fair bits gives the geometric
bound on the number of visits, including the initial one. Each
rooted word is legal on one terminal ternary cylinder of Haar
mass \(3^{-p}\). This permits an exceptional value at a prescribed
integer; equations (1) and (2) used actual ordinary constraints
to obtain their pointwise content.
