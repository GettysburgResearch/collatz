# Directed five queries, a universal certificate compiler, and the joint minimum

**Status: proved conditional construction and exact cost theorem. Full Collatz remains open.**

This note makes the two proposed failure types use the same accounting. It
constructs an actual certificate program for every positive ternary unit,
with a proved finite number of physical-five queries and an exact bound on
their antecedents. It then puts that program alongside the existing reverse
program. The resulting joint induction is precise, but its return cost does
not close the latest Mersenne reduction.

Throughout, the positive ordinary shortcut map is

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\]

and \(C\) is its actual basin of 1. A ternary unit is a positive integer
not divisible by three. No ordinary component invariance under tripling is
assumed.

## Frozen dependencies and new contribution

| Dependency | Full commit | Role |
|---|---|---|
| PR157 | `64361ecca770092d6c8242dc6211e38818af2e50` | `research/global-closure-20261120/merger.md` and `reports/2026-11-20-global-closure/merger-certificate.json`: complete directed descent using forward physical-five closure. |
| PR163 | `051237135a34ae7d4b973ee5fcf5da04ded6f0fc` | `research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md`, H1--H2: complete reverse-query descent and the exact unit cost \(2025217/23\). |
| Latest PR146 | `fd991063721e9c157d318e40bb20131762f7d750` | `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`: a hard rank-five least reverse failure yields a smaller actual five failure. |
| Latest PR164 | `6fa6b429870a9cd53cde0fc77ad64a3c3956199f` | The new guarded P/Q and seed contractions do not yet constitute an all-source return rule. |

The directed affine cover and its contraction are credited to PR157. The
new conclusions here are its **sharp physical-five query cost**, the
**executable certificate program with its dependency order**, and the
**joint-minimum inequalities**. The reverse cost is reused, not claimed as
new.

The frozen PR157 JSON is copied as `directed_five_certificate.json`. Its
SHA-256 is

```text
751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1
```

## JF1. Exact all-lift physical-five query cost

For an odd ternary unit \(r\), write

\[
F(r):\qquad r\in C\Longrightarrow5r\in C.
\]

Set

\[
\boxed{B=\frac{3669265}{2239}.} \tag{1}
\]

**Theorem.** For every positive ternary unit \(n\), there is a finite
directed proof program from 1 to \(n\), whose only nonordinary operations
are calls to \(F(r)\) with

\[
\boxed{r\le Bn.} \tag{2}
\]

When executed in its specified order, every call receives a complete
ordinary certificate for its actual antecedent \(r\). If the call returns
a complete ordinary certificate for \(5r\), the program constructs the
ordinary certificate needed for the next step. For \(n>1\), the number of
five queries is at most

\[
\left\lceil\frac{\log n}{\log(20/19)}\right\rceil. \tag{3}
\]

The constant in (1) is sharp for the frozen affine cover. This is not a
claim that it is optimal over other possible constructions.

### The affine query calculation

PR157's cover has 464 cells, 55 words, and exactly 219 appearances of a
division by five. Every word has at most one such appearance. Write a cell
as

\[
n=mu+r_0,\qquad u\ge u_0,
\]

and write the value immediately after that division as
\(au+b\). The physical-five antecedent is its odd part. Thus it is at
most \(au+b\), and

\[
\sup_{u\ge u_0}\frac{au+b}{mu+r_0}
=\max\left\{\frac am,
\frac{au_0+b}{mu_0+r_0}\right\}. \tag{4}
\]

Indeed, the derivative of the ratio has constant sign; alternatively,
cross multiplication directly proves that the ratio lies between its
initial value and its limit. The expression is therefore valid on the
whole infinite cell.

The checker verifies all 219 ratios. Their maximum is (1), on word
`W17`, cell

\[
n=8640u+2239,\qquad u\ge0.
\]

The five antecedent at the maximizing position is

\[
14155776u+3669265. \tag{5}
\]

Its constant term is odd and its slope even, so stripping powers of two
does not reduce it. At \(u=0\), the query is exactly
\(F(3669265)\) for source 2239. Equality in (2) is attained at that cell
point, proving sharpness for this cover.

The checker also independently verifies every affine guard and the full
partition of the 497,664 residues coprime to 30 modulo 1,866,240. It checks
positivity, oddness at each odd operation, exact integrality of every
inverse, exclusion of multiples of three, and the endpoint inequality
\(q\le19n/20\) on every unrestricted lift. These checks use coefficients,
not selected numerical samples.

### Why the proof program terminates

For an even unit \(n>1\), use the ordinary edge to \(n/2\). For an odd
unit divisible by five, use the directed edge to \(n/5\), which requests
\(F(n/5)\). Otherwise select the unique affine cell and its word. Each
case gives a positive unit endpoint

\[
q\le\frac{19}{20}n<n. \tag{6}
\]

Repeat at \(q\). These are strictly decreasing positive integers, ending
at 1. Inequality (6) gives the bound (3). There is at most one five query
at each level. Every later source is at most the original \(n\), so its
query bound \(Br\!_\text{source}\) is at most \(Bn\). The special
division-by-five case has antecedent \(n/5<Bn\).

### Why the program supplies each antecedent certificate

The affine word is written from \(n\) towards \(q\), with an arrow
\(x\rightsquigarrow y\) meaning
\(y\in C\Rightarrow x\in C\). First execute the recursively compiled
program for \(q\). Then read this word backwards.

All suffix edges after the unique `/5` are ordinary component
equivalences. They therefore transform the certificate for \(q\) into a
certificate for the value just after `/5`. Removing its initial powers of
two supplies an ordinary certificate for the odd antecedent \(r\).
Only at this point is \(F(r)\) requested.

Given an actual ordinary certificate for \(5r\), prepend the necessary
halvings to obtain the certificate for the value before `/5`, and
continue backwards through the remaining ordinary edges. At an inverse
edge \(y=(2^j x-1)/3\), the verified ordinary relation is
\(T^j(y)=x\); take the suffix at that clock. If a certificate reached 1
before the splice clock, append the actual cycle \(1,2,1\) as necessary.
At a forward odd edge \(x\to3x+1\), the two values have the same next
ordinary iterate. These are finite operations on actual positive
certificates.

Thus the compiler does not treat membership of a large oracle antecedent
as a free induction hypothesis. Its antecedent certificate is produced
from earlier completed stages. Its termination as a *conditional proof
program* is unconditional; termination of every unresolved physical-five
call is the open premise.

## JF2. A least five failure gives a certified initial interval

Suppose physical-five failures exist and let

\[
f_* = \min\{r>0:r\text{ odd},\ 3\nmid r,\ r\in C,\ 5r\notin C\}.
\]

Then

\[
\boxed{3\nmid n,\quad Bn<f_*\quad\Longrightarrow\quad n\in C.} \tag{7}
\]

Every query in JF1's program has antecedent below \(f_*\). Minimality
makes each such physical-five implication true. The program's dependency
order supplies its antecedent certificate, so it finishes with an ordinary
certificate for \(n\).

For a general positive \(n\), stripping powers of two gives an odd
\(v\le n\). If \(3\mid v\), its ordinary successor
\((3v+1)/2\) is a ternary unit and is at most \(5n/3\), since \(v\ge3\).
Consequently the corresponding all-integer interval is

\[
\boxed{\frac{5B}{3}n<f_*\quad\Longrightarrow\quad n\in C.} \tag{8}
\]

The unit version (7), rather than the coarser (8), is the one needed for
the joint comparison below.

### Failure localization without a new closure assumption

JF1 also gives the following positive logical statement:

\[
\boxed{n\notin C,\quad3\nmid n
\quad\Longrightarrow\quad
\exists r\le Bn:\ r\in C,\ 5r\notin C.} \tag{9}
\]

To see this directly, follow the finitely many decreasing program sources
from \(n\) to 1 and choose the last one outside \(C\). Its smaller
endpoint is in \(C\). The word cannot use only ordinary equivalences.
It contains exactly one `/5`; its ordinary suffix proves that the
antecedent is in \(C\), and its ordinary prefix proves that the multiplied
target is outside \(C\). This is an actual failed implication of the
required size. It does not require identifying nonconvergence by a finite
numerical test.

## JF3. Put the reverse and five minima on the same scale

A reverse failure is an upper source

\[
X=128k+1,\quad k>0,\quad4\nmid k,\quad
X\in C,\quad Y=64k+1\notin C.
\]

Let \(X_*\) be the minimum of this entire set, if nonempty. Reusing the
exact PR163 H1 cost, put

\[
\boxed{A=\frac{2025217}{23}.} \tag{10}
\]

The PR163 unit induction gives

\[
3\nmid n,\quad An<X_*\quad\Longrightarrow\quad n\in C. \tag{11}
\]

This uses its exact ratio instead of rounding it to 88053. The proof is
unchanged: every conditional reverse upper is at most \(An\), and hence
strictly below the same least reverse failure.

If Collatz fails, both actual failure sets are nonempty by their complete
directed constructions. Their simultaneous global minima satisfy

\[
\boxed{
\frac{X_*}{5A}\le f_*
\le B\,\frac{27X_*+101}{128}.
} \tag{12}
\]

For the left inequality, \(5f_*\) is a bad ternary unit, so (11) implies
\(5Af_*\ge X_*\). For the right inequality, the actual ordinary path

\[
T^6(64k+1)=27k+1=\frac{27X_*+101}{128}
\]

ends at a bad ternary unit. Apply (9). These minima are taken over all
failures of their respective types; no change to a minimum at a selected
rank is made.

Equivalently, a five failure at \(f\) forces some reverse failure with
upper source at most

\[
\boxed{5Af=\frac{10126085}{23}f.} \tag{13}
\]

This follows either from the complete reverse descent applied to the bad
unit \(5f\), or from the minimum bound in (12). It is an all-source
return statement, with the exact interface cost required by a joint
induction.

## JF4. What the latest hard rank-five reduction does and does not close

Latest PR146 proves that a hard rank-five least reverse failure has

\[
e=119+162j,\quad P=2^e,\quad X_*=(1024P-2573)/243,
\]

and yields an odd unit \(q\) with

\[
q<X_*/4,\qquad q\in C,\qquad5U(q)\in C,\qquad5q\notin C. \tag{14}
\]

The known source has a first valuation one followed by a run of valuation
threes. Equation (14) is stronger than a density statement: it supplies an
actual failed comparison with an actual certified antecedent. In
particular,

\[
\frac{X_*}{5A}\le f_*<X_*/4. \tag{15}
\]

This interval is nonempty. A new failure type is not by itself a
contradiction.

For precision, try assigning scalar costs

\[
\operatorname{cost}_R(X)=aX,\qquad
\operatorname{cost}_F(q)=bq,\qquad a,b>0.
\]

To certify descent for every call allowed by the bound \(q<X/4\), it
suffices to require \(b/a\le4\). To certify descent for every return
allowed by (13), it requires

\[
b/a>5A=10126085/23.
\]

Those sufficient uniform guards are incompatible. The two-way budget
product is

\[
\boxed{\frac{5A}{4}=\frac{10126085}{92}>1.} \tag{16}
\]

This calculation does **not** rule out a better return construction, a
nonlinear rank, or a rank using the supplied certificate. It says exactly
that the two currently proved size interfaces do not supply a decreasing
scalar rank. Treating their composition as a smaller call would be the
first unsupported step.

## The remaining constructive obligation

For the actual \(q\) in (14), a sufficient new return would be an ordinary
proof of \(5q\), or a finite proof using only reverse queries whose upper
antecedents are strictly below the original \(X_*\). This can depend on
the full source certificates and have unbounded length. An all-source
return with reverse budget strictly below \(4q\) would suffice in this
family, but is much stronger than the available generic budget (13).

At its first ordinary step, the comparison has the exact form

\[
U(5q)=5U(q)-2.
\]

Knowing both \(U(q)\in C\) and \(5U(q)\in C\) does not supply a
certificate for this shifted target. Consuming the valuation-three run
must therefore carry the nonzero negative offset and must pay for every
subsequent call with the original bound \(X_*\). Dropping that offset,
reversing a forward-five implication, or resetting the global minimum is
not a valid completion.

No such all-source guarded return has been proved in this note. The
compiler makes the required certificates and cost guards concrete and
reviewable; it does not mark its unreturned oracle calls as solved.

## Exact replay

From this directory:

```bash
python -B check_joint_failure_costs.py
python -O -B check_joint_failure_costs.py
python -B check_joint_failure_costs.py --program 2239
```

The checked report is `joint_failure_cost_report.json`. The universal
part checks the 464 unrestricted affine families, all 219 query costs,
and the complete residue partition. Separate bounded execution replays
construct ordinary certificates for 13 example sources; they test the
dependency order and certificate splices, and are not used to infer
universal physical-five closure. All verification failures use explicit
exceptions, so optimized Python does not disable the checks.
