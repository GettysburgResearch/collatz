# Attempt to close arbitrary cycles by GRH affine mixing

Date: 2026-11-22. Repository baseline: PR185 at
`4b0c2c27812db555061f5d9006de82a87e7e364f`.

**Outcome: the attempted unrestricted cycle exclusion does not close.**
The calculation below identifies the actual distribution that would need
control, proves that it is far from uniform at its cycle clock, and states
the much more specific cancellation still required. This is not a new
cycle exclusion family and is not a claim that every possible use of GRH
or expansion is impossible.

## 1. Why try this machinery?

The full cycle condition is divisibility of an exponentially large
binomial by an affine carry. Strong affine-walk mixing and arithmetic
expansion can sometimes control precisely this kind of congruence. A
particularly relevant primary theorem is Breuillard--Varju, *Cut-off
phenomenon for the ax+b Markov chain over a finite field*, Theorem 3 and
Corollary 4, arXiv:1909.09053v2, pp. 4--5:

<https://arxiv.org/pdf/1909.09053>.

Under RH for the Dedekind zeta functions of all number fields, their
fixed-multiplier chain with independent additive increments has a sharp
entropy-time cutoff for most primes and most multipliers. The theorem
does not assert this for each prescribed modulus and multiplier. Its
independent increments are another hypothesis. Its proof was not
reaudited here; its statement and entropy lower bound were read.

The user's permission to assume GRH therefore makes this a concrete
candidate, rather than a reference to an unspecified possible benefit.
The following calculation tests its actual Collatz interface.

## 2. The exact law, with the whole denominator

Fix integers A,p with 1 <= p <= A and D=2^A-3^p>0. For every binary
word w of length A containing exactly p ones, let d_0<...<d_(p-1) be
its one positions and put

\[
 C(w)=\sum_{i=0}^{p-1}3^{p-1-i}2^{d_i},\qquad
 F_w(x)=\frac{3^p x+C(w)}{2^A}.
\]

There are W=binomial(A,p) such words. Let rho_(A,p) be the distribution
of C(w) modulo the **whole** D under the uniform word law. Then

\[
 W\rho_{A,p}(0)
 =\#\{w:\ |w|=A,\ |w|_1=p,\ D\mid C(w)\}.                 \tag{1}
\]

Since C(w)>0, every divisible word has positive integral fixed point
x=C(w)/D. It is an actual parity cycle. One elementary proof is that
the first branch taken with wrong parity makes a half-integer with odd
numerator. Every subsequent branch leaves an odd numerator over a
strictly larger power of two. The final value cannot then be integral.

For an appended bit epsilon, the exact carry recurrence is

\[
 C_{j+1}=3^\epsilon C_j+\epsilon2^j.
\]

Thus Z_j=2^(-j)C_j modulo D follows the two affine maps

\[
 z\mapsto z/2,\qquad z\mapsto(3z+1)/2.                    \tag{2}
\]

The uniform law in (1) conditions on the total number p of applications
of the second map. Its multipliers and offsets are coupled. It is not
the fixed-multiplier iid-additive chain in the imported theorem.
Replacing it with that chain would change the cycle problem.

## 3. A universal entropy obstruction at the actual cycle clock

**Proposition.** If 4A<=7p, then

\[
 W^7<120^A,\qquad
 \|\rho_{A,p}-u_D\|_{TV}\ge1-W/D,                         \tag{3}
\]

where u_D is uniform on Z/DZ. The second inequality is useful when
W<D; it remains a valid inequality otherwise.

Proof. The binomial theorem gives

\[
 W(4/3)^p\le(1+4/3)^A=(7/3)^A.
\]

Raise to the seventh power and use 7p>=4A:

\[
 W^7\le\left(\frac{7^7}{3^3 4^4}\right)^A<120^A,
\]

because 7^7=823543<120*3^3*4^4=829440. The support of rho contains
at most W residues. If E is this support, rho(E)=1 and u_D(E)<=W/D;
the variational definition of total variation proves the second claim.

Every nontrivial positive cycle satisfies the strict version 4A<7p.
Indeed its p odd states q_i are all at least 3, and multiplication of
the exact odd-state equations gives

\[
 2^A=\prod_{i=0}^{p-1}(3+1/q_i)\le(10/3)^p.
\]

But (10/3)^4<2^7, since 10000<10368. Hence 2^(4A)<2^(7p).
The elementary eligibility cone in (3) therefore covers every
nontrivial cycle, with no bound on its valuation alphabet or period.

The existing Matveev input in the repository supplies absolute effective
c>0,K>0 with

\[
 D\ge c2^A A^{-K}                                        \tag{4}
\]

whenever D>0 and p<=A. See the specialization in
`research/profound-closure-20261122/BOUNDED_POWER_LANGUAGES.md`, Section 4,
and Matveev, Corollary 2.3, <https://www.mathnet.ru/eng/im314>.
Combining (3)--(4) gives the all-parameter bound

\[
 \boxed{\|\rho_{A,p}-u_D\|_{TV}
 \ge1-c^{-1}A^K(15/16)^{A/7}.}                           \tag{5}
\]

In particular the distance tends to **one**, uniformly over the entire
nontrivial-cycle eligibility cone with D>0. The enormous effective
constant in (4) is harmless for this asymptotic conclusion; no numerical
threshold or enumeration at that threshold is claimed.

The issue is intrinsic to the law at the prescribed clock, even if one
imagines a stronger affine-mixing theorem that removes all exceptional
primes and multiplier restrictions. There are exponentially fewer legal
fixed-count words than residues of D. Extra random steps can create more
entropy, but change A, p, D and the return equation simultaneously.

## 4. The precise zero-residue target survives

The distance statement does not prevent a strong estimate for the
particular residue zero. Here is what would suffice.

A primitive cycle with shortcut period A gives A distinct cyclic
rotations of its parity word. Every rotation has the same (A,p,D), has
an integral fixed point, and contributes to (1).

To justify primitivity of the parity word itself, if w=v^k with k>1,
the affine map F_v has a positive multiplier different from one.
Any fixed point of F_v^k is then already a fixed point of F_v. The
integrality argument from Section2 makes v physically legal there,
contradicting least state period A. Thus the A rotations really are
distinct. Consequently

\[
 \text{primitive cycle at }(A,p)
 \quad\Longrightarrow\quad \rho_{A,p}(0)\ge A/W.          \tag{6}
\]

The rotation action is free on a primitive word; this does not count
repetitions of a shorter cycle as A distinct words. Equivalently,
restricting to words beginning in 1 gives p rotations among
binomial(A-1,p-1) words, with the identical ratio
p/binomial(A-1,p-1)=A/W.

Thus a proof of

\[
 \rho_{A,p}(0)<A/\binom A p                               \tag{7}
\]

for all sufficiently large eligible pairs would eliminate every
sufficiently long primitive positive cycle. Remaining finite pairs
would then need an actual effective cutoff and verification. No such
bound is proved here.

For completeness define

\[
 \widehat\rho(t)=\frac1W\sum_w
 \exp(2\pi i tC(w)/D).
\]

The exact Fourier target is

\[
 1+\sum_{t=1}^{D-1}\widehat\rho(t)<AD/W.                  \tag{8}
\]

The left side is the nonnegative real number D*rho(0). This target
requires cancellation with its signs; a general statement that some
Fourier modes contract does not establish it. Parseval keeps another
diagnostic visible:

\[
 \sum_{t=0}^{D-1}|\widehat\rho(t)|^2
 =D\sum_r\rho(r)^2\ge D/W.                              \tag{9}
\]

There is substantial Fourier energy because the law is sparse. Passing
to individual prime divisors of D also leaves the simultaneous
prime-power intersection in (1) unpaid. No independence across those
factors follows from GRH.

### Atom-specific continuation: keep the integer multiplicity

The next attempt retained zero rather than trying to repair total
variation. Put N_r=#{w:C(w)=r modD}. Then the required bound is the
integer statement N_0<A. A sufficient, stronger anti-concentration
statement would be max_r N_r<A. Such a statement was not established;
it would be substantially stronger than ordinary entropy growth.

The exact collision energy is

\[
E=\sum_r N_r^2=W+\#\{(v,w):v\ne w,\ C(v)=C(w)\pmod D\}.
\]

A primitive integer cycle supplies A(A-1) distinct ordered
off-diagonal collisions at zero. Thus E-W<A(A-1) would suffice too.
But the standard Cauchy--Schwarz bound on one atom is N_0<=sqrt(E),
and even the unavoidable diagonal gives E>=W. Since W grows
exponentially at the cycle ratios, this bound cannot reach A. Removing
the diagonal still counts collisions at every nonzero residue; a
generic large-sieve estimate does not single out the cyclic zero
configuration. This is a quantitative accounting of the attempted
estimate, not a lower bound asserting that those unwanted collisions
must occur in every eligible law.

An entropy-growth argument also needs an unusually fine target here.
Because the word law is uniform and its fibers have sizes N_r,

\[
\log W-H(\rho)=\frac1W\sum_r N_r\log N_r.
\]

A primitive zero fiber forces an entropy loss at least
A log(A)/W. Therefore near-injectivity to an error **strictly below**
that exponentially small scale would exclude it. A lower entropy-rate
bound alone does not give this accuracy, and other residue fibers also
contribute to the same loss. This further attempt did not produce the
required estimate for the actual conditioned carry law.

There is also an exact arithmetic structure that an improved sieve
could retain. If w starts with epsilon and rot(w) moves that bit to
the end, ordinary rational cyclic transport gives

\[
2C(\operatorname{rot}w)=
 \begin{cases}C(w),&\epsilon=0,\\3C(w)+D,&\epsilon=1.
 \end{cases}
\]

Consequently every rotation of a zero-residue word remains zero.
These are highly dependent collisions. Treating the A rotations as
independent samples would manufacture a factor D^(-A) and incorrectly
prove exclusion. The actual modular action is multiplication by
1/2 or3/2, with zero fixed. I obtained no cancellation theorem that
controls this dependent zero configuration uniformly for the
arithmetically prescribed D. The nonuniform target (7), rather than
the false uniform-mixing target, is the unfinished implication.

## 5. What the other deep arithmetic inputs supplied

I also inspected Evertse--Schlickewei--Schmidt's primary statement,
<https://annals.math.princeton.edu/2002/155-3/p04>, and the full sparse
cycle-difference argument in the recent primary exposition
<https://rstation.ai/problems/collatz/papers/22/v3>.

The former controls nondegenerate equations in a fixed dimension and a
fixed-rank multiplicative group. The latter uses torus gcd estimates on
an exact sparse remainder, retaining the entire denominator, and obtains
unbounded defect requirements plus stronger effective inequalities from
cycle-specific structure. Its number of terms still grows for an
arbitrary word. I did not obtain a universal sparse representation or
an estimate implying (7). Those imported statements have not been
recast as a general cycle exclusion.

The distinct new literature lead
<https://rstation.ai/problems/collatz/papers/173/v1> proves a finite
descent-or-complexity alternative using Rauzy graphs, S-unit equations
and fixed-forms Subspace arguments. Its premise is a bounded local
factor-complexity ratio. It does not provide that upper bound for an
arbitrary cycle or divergent orbit. This source was sent to the escape
and integration attacks for a more detailed examination.

## 6. Scope and reproducibility

The mathematical content added here is the direct count, rotation and
entropy calculation (1)--(9), together with a concrete failed import of
GRH affine mixing. The three declarations in `CycleWordEntropy.lean`
prove the binomial weighted bound, its cone weight comparison, and
`binomial(A,p)^7 < 120^A` for every A>0, p<=A, 4A<=7p. They were
compiled with warnings as errors under Lean4.34.1 and their axiom
audits use only the standard proof axioms. Matveev, GRH, total variation
and full cycle exclusion are not axioms or formalized conclusions of
that module. The remaining arguments are written mathematics.
The exact finite controls in
`cycle_law_controls.py` test the carry law, ordinary realization,
rotation accounting, support bound and binomial inequality. Their
finite range is stated in their output and does not prove the
asymptotic or unrestricted claims. No new bounded search was used to
infer the absence of all cycles.
