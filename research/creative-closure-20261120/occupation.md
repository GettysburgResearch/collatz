# Coalescence information and saturated first-hit capacity

**Status: PROPOSED, with written proofs and exact bounded replay. Collatz
remains unresolved.** Two positive constructions retain the mass of every
original ordinary source: an all-time coalescence-information budget and a
saturated first-hit capacity. The latter has a finite Dirichlet moment even
when periodic states are retained. Neither construction establishes the
required upper bound for time occupation. We prove where the most direct
payment and compactification attempts fail, including all uncomputed sources,
and give an exact finite positive repair beyond the first obstruction.

## 1. Frozen ordinary interfaces and the closing target

Use the positive shortcut map \(T(n)=n/2\) for even \(n\), and
\(T(n)=(3n+1)/2\) for odd \(n\), killed at 1. We use the moving rank,
acceleration \(A\), and **quarter-safe** return \(B\) of
[PR152, AT2--AT3](https://github.com/GettysburgResearch/collatz/blob/2391a9c1e4a7f77233b951d2eb6da92e76652e7c/research/gemini-global-closure-20261120/ACTUAL_TRANSPORT.md).
Explicitly,

\[
 z_a(n)=(3^a-2^{a+1})n+3^a-2^a,
 \qquad R(n)=\min_{a\ge0}z_a(n)^2/3^{v_3(z_a(n))}.
\]

A zero numerator has component rank zero. The pinned source proves that the
minimum is among \(a=0,1,2,h\), where \(h=v_3(2n+1)\); \(h\) need only be added
when \(h\ge3\). It also proves \(R(1)=0\) and \(n-1\le R(n)\le n^2\) for
\(n\ge2\). The active mode is 0 for even \(n>1\) and \(v_2(n+1)\) for odd
\(n>1\). With \(k=\lfloor v_2(z_a(n))/(a+1)\rfloor\ge1\), \(A\) consumes
\(k\) actual shortcut words \(1^a0\).

Put \(G=\{n>1:4R(A(n))\le R(n)\}\) and \(U=\{n>1\}\setminus G\).
From \(u\in U\), \(B\) applies \(A\) once and then follows \(G\) until its
next endpoint in \(U\cup\{1\}\). Positive-integer rank descent makes this
return total. Its killed pushforward is

\[
 (Hf)(y)=\sum_{u\in U:B(u)=y}f(u),\qquad y\in U.
\]

Endpoint rows and original-source columns are retained. Write
\(\bar B(1)=1\) and \(\bar H\) for the corresponding pushforward on
\(U\cup\{1\}\), which retains absorbed mass at a cemetery point.

Our one fixed input and charge are exactly those of
[PR157, GCT-001--004](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/transport.md):

\[
 f_0(u)=\frac1{u(u+1)}\quad(u\in U),\qquad
 m_0=\sum_{u\in U}f_0(u)\le\frac12,
\]
\[
 \psi(u)=1+\log\log(R(u)+6),\qquad
 \psi_*=1+\log\log7>0.
\]

For a surviving return, the proved height budget is
\(\psi(Bu)\le\psi(u)+\log6\). If \(m_\infty\) is the original mass of
sources never absorbed at 1, PR157 proves, including sources entering cycles,

\[
 \mathcal G_N(f_0):=
 \sum_{j<N}\sum_{y\in U}\frac{(H^jf_0)(y)}{\psi(y)},
 \qquad
 \liminf_{N\to\infty}\frac{\mathcal G_N(f_0)}{\log N}
 \ge\frac{m_\infty}{\log6}.                         \tag{1}
\]

Thus an upper bound \(o(\log N)\) for this **fixed, full-support** input
would close Collatz. It has not been proved here. The resident baseline is
main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; importing the displayed
interfaces does not remove qualifications attached to that baseline.

## 2. OCC-001: a finite, exact coalescence-information budget

Let \(p_j=\bar H^j f_0\), with \(p_0(1)=0\), and define the unnormalized
entropy \(S(p)=\sum_y-p(y)\log p(y)\), taking \(0\log0=0\). Initially,

\[
 S(f_0)\le\sum_{n\ge2}\frac{\log(n(n+1))}{n(n+1)}
 \le\sum_{n\ge2}\frac{2(\log2+\log n)}{n^2}
 \le2+2\log2<4.                                      \tag{2}
\]

The last step integrates the decreasing function
\(2(\log2+\log x)/x^2\) over \([1,\infty)\).
For an original atom \(u\), set \(x_j=\bar B^ju\) and

\[
 I_j(u)=\log\frac{p_j(x_j)}{f_0(u)}.
\]

Its carrier contains that atom and never loses mass along the atom's path.
Hence \(I_j(u)\) is nonnegative and nondecreasing, bounded by
\(\log(m_0/f_0(u))\). Grouping atoms by their exact endpoint gives

\[
 \sum_u f_0(u)I_j(u)=S(f_0)-S(p_j).                    \tag{3}
\]

All terms are controlled by the finite initial entropy: since
\(f_0(u)\le p_j(x_j)\le m_0<1\),
\(|\log p_j(x_j)|\le|\log f_0(u)|\). Thus the regrouping is legitimate.
In particular the successive coalescence charges

\[
 J_j:=S(p_j)-S(p_{j+1})
 =\sum_x p_j(x)\log\frac{p_{j+1}(\bar Bx)}{p_j(x)}
 \ge0                                                \tag{4}
\]

satisfy the all-time estimate

\[
 \boxed{\sum_{j\ge0}J_j\le S(f_0)+m_0\log m_0<\infty.} \tag{5}
\]

Indeed \(S(p_j)\ge-m_0\log m_0\). These are standard deterministic
information identities applied to the actual return. No novelty is claimed
for entropy contraction itself, and no independent bits are introduced.

### The proposed payment and its whole-source failure

Let \(\ell_j=\sum_{y\in U}p_j(y)/\psi(y)\). The estimate
\(\ell_j\le J_j\) for all \(j\) would make \(\mathcal G_\infty\) finite,
and (1) would finish the problem. It is false for the actual input above.
The exact checker encloses all original sources and proves at \(j=8\)

\[
 \ell_8\in[0.001747115078,\ 0.001756275362],\qquad
 J_8\in[0.000744022152,\ 0.001481949455],
\]
\[
 \boxed{\ell_8-J_8>0.000265165623.}                    \tag{6}
\]

This refutes the **unit coefficient, one-return** payment. It does not
refute a larger coefficient or a source-specific amortized comparison.
Such an estimate remains a concrete missing step. The same computation
certifies a whole-source upper bound \(0.311755297211\) for (5) and

\[
 \mathcal G_{16}(f_0)
 \in[0.140781091451,\ 0.140927655978].                 \tag{7}
\]

These finite values are not an all-time extrapolation.

Here is the omitted-source control behind (6). For a source cutoff \(M\),

\[
 \sum_{u>M}f_0(u)\le\frac1{M+1},\qquad
 E_M:=\sum_{n>M}\frac{\log(n(n+1))}{n(n+1)}
 \le\frac{2(\log(M+2)+1)}{M+1}.                       \tag{8}
\]

For the entropy bound, put \(m=M+1\), use
\(\log(n(n+1))\le2\log(n+1)\), and sum by parts:

\[
 \sum_{n=m}^{\infty}\frac{\log(n+1)}{n(n+1)}
 =\frac{\log(m+1)}m
   +\sum_{n=m+1}^{\infty}\frac{\log(1+1/n)}n
 \le\frac{\log(m+1)+1}{m}.
\]

At \(M=65536\), direct exact mass accounting and (8) show \(m_0<1/3<e^{-1}\).
Thus \(h(t)=-t\log t\) is increasing on the entire mass range. If
\(p_j^{(M)}\) denotes the actual pushforward of originals at most \(M\), then
monotonicity, \(h(a+b)\le h(a)+h(b)\), and entropy contraction of the omitted
input give, **uniformly at every return**,

\[
 S(p_j^{(M)})\le S(p_j)\le S(p_j^{(M)})+E_M.            \tag{9}
\]

Consequently \(J_j\) lies within \(E_M\) of the finite-source entropy drop,
and \(\ell_j\) lies between its finite-source value and that value plus
\(1/((M+1)\psi_*)\). This controls even omitted sources coalescing into
small retained endpoints; there is no endpoint truncation assumption.

### Why input-independent entropy payment also fails

There is an actual one-return convergent source \(3\in U\), \(B(3)=1\),
and \(f_0(3)=1/12\). Let \(q=f_0/m_0\). Equation (2) gives
\(S(q)=S(f_0)/m_0+\log m_0<48\). For

\[
 f_\epsilon=(1-\epsilon)\delta_3+\epsilon q,
 \qquad0<\epsilon<1,
\]

the input is a probability positive on every unsafe integer, while

\[
 S(f_\epsilon)\le
 \epsilon\bigl(\log(1/\epsilon)+49\bigr)\longrightarrow0,
 \qquad
 \mathcal G_1(f_\epsilon)\ge\frac{1-\epsilon}{\psi(3)}.
                                                               \tag{10}
\]

The entropy estimate follows from the entropy of the two-part mixture and
\(-(1-\epsilon)\log(1-\epsilon)\le\epsilon\).
Thus no finite coefficient, uniform over all positive full-support inputs,
can pay even the first charge from their total coalescence entropy. This is
an actual-map control, not an invented replacement dynamics. It does not
decide a comparison restricted to the specified \(f_0\).

## 3. OCC-002: saturated first-hit capacity and its inverse identity

A second mechanism records coalescence through first hits. Define, for
\(y\in U\), the first-hit capacity

\[
 C(y):=\sum_{u\in U}f_0(u)
       1\{B^ju=y\text{ for some }j\ge0\}.             \tag{11}
\]

Here each original atom is counted **at most once at each endpoint**.
The symbol \(C\) distinguishes capacity from the acceleration \(A\).
Always \(0<f_0(y)\le C(y)\le m_0\le1/2\), and
\(C(By)\ge C(y)\) on surviving edges.

If \(y\) is **not periodic under \(B\)**, then

\[
 \boxed{C(y)=f_0(y)+\sum_{x:B(x)=y}C(x).}              \tag{12}
\]

To prove this, every original source reaching \(y\), other than \(y\)
itself, has a unique predecessor \(x\) at its first hit. Conversely every
source reaching such an \(x\) reaches \(y\) next. Two predecessor basins
cannot overlap: otherwise a single deterministic path would visit \(y\)
twice, making \(y\) periodic. The original source \(y\) cannot lie in a
predecessor basin for the same reason. This proves a disjoint partition of
the source set and then (12) by nonnegative summation.

For every real \(p\ge1\), (12) implies

\[
 H(C^p)(y)\le\bigl(C(y)-f_0(y)\bigr)^p<C(y)^p
 \quad\text{at every nonperiodic }y.                  \tag{13}
\]

For infinite predecessor sets, first apply
\(\sum a_i^p\le(\sum a_i)^p\) to finite subsets and pass monotonically
to the limit. **Summability of \(C^p\) is not established.** At a periodic
point the capacities are equal around its cycle; the cycle predecessor
already contributes \(C(y)\), so (12) with its extra positive \(f_0(y)\)
cannot hold. Neither this exception nor the missing summability may be
dropped from (13).

## 4. OCC-003: a saturated Dirichlet budget, including periodic states

The input is the finite-simple-path interval theorem
[PR153, FID-DRIFT-001, 002 and 005](https://github.com/GettysburgResearch/collatz/blob/eb04a5d79020cefa0ba46794095b5766c5ff66a4/research/fixed-integer-descent/drift.md),
whose manuscript SHA-256 is
`d73a93d8a803996bde7b15f33e307d28385c8ffe2f9b99f449dfea35140c3338`.
It bounds visits by one finite simple shortcut path to any integer interval
of width \(X\ge1\) by a universal \(F(X)\), with

\[
 F(X)\le10X^{29/30},\qquad
 F(X)\le C_\alpha X^\alpha
 \quad\bigl(\alpha>h_*:=H_2(\log_3 2)\bigr).           \tag{14}
\]

Here \(H_2\) is binary entropy and \(h_*\approx0.949956\). The second
constant is effective but not presented as a practical numerical constant.
We import this one-path theorem, **not a density bound for a whole basin**.

The distinct unsafe values of any one \(B\)-orbit are a subset of the
distinct values of its actual \(T\)-orbit. Before its first repetition a
deterministic \(T\)-orbit is simple; after repetition its complete value set
is contained in its preperiod and one traversal of its cycle. Every finite
subset of the distinct value set is therefore covered by a finite simple
\(T\)-path. Apply (14) to that path, then Tonelli to the original source
weights in (11). For every integer \(a,X\ge1\),

\[
 \boxed{\sum_{y\in U\cap[a,a+X)}C(y)\le m_0 F(X).}    \tag{15}
\]

No periodic states have been deleted. Saturating visits, rather than
assuming an orbit never repeats, is what makes (15) valid for cycles.

For real \(Q\ge1\), the cumulative capacity at endpoints at most \(Q\)
is at most \(10m_0 Q^{29/30}\): use the integer interval
\([1,1+\lfloor Q\rfloor)\). The layer-cake identity consequently gives,
for \(s>29/30\) and \(L\ge1\),

\[
 \boxed{\sum_{y\in U:y\ge L}\frac{C(y)}{y^s}
 \le \frac{10s}{s-29/30}\,m_0 L^{29/30-s}.}            \tag{16}
\]

Indeed write \(y^{-s}=s\int_y^\infty t^{-s-1}\,dt\), interchange
nonnegative sums, and bound the cumulative mass in \([L,t]\) by the
larger cumulative mass in \([1,t]\). The recursive bound in (14) likewise
proves finiteness for every \(s>h_*\), by choosing \(h_*<\alpha<s\).
For \(s=1\), (16) becomes

\[
 \sum_{y\ge L}\frac{C(y)}y\le300m_0 L^{-1/30}
 \le150L^{-1/30}.                                    \tag{17}
\]

Replacing \(f_0\) by only its originals above \(M\) gives the same estimates
with \(m_0\) replaced by at most \(1/(M+1)\). Thus this is also an analytic
original-source tail, valid at all times and without an endpoint cutoff.

The weights \(w_s(y)=C(y)y^{-s}\) are therefore positive, full-support and
summable for every \(s>h_*\), including exponents below one. A second
automatic compactification is

\[
 v_c(y)=C(y)^{c b(y)},\qquad
 b(y)=\lfloor\log_2 y\rfloor+1,\qquad c>1.            \tag{18}
\]

Since \(C\le1/2\), \(v_c(y)\le2^{-c b(y)}\le y^{-c}\), hence it is
summable too. These are genuine finite positive constructions. However,
(16) charges a first hit once; it is **not** an upper bound for (1), which
charges every surviving return. In particular (16) cannot exclude a cycle.

## 5. OCC-004: whole families fail on an actual edge; a finite repair

The actual unsafe return has \(B(31)=121\), with
\(R(31)=144\), \(R(121)=1764\). Its complete known-convergent \(B\)-path is

\[
 31,121,91,103,175,445,334,167,319,1822,911,244,46,23,1.
                                                               \tag{19}
\]

The checker replays all physical shortcut words and rank guards on this
path. The first return is the six-letter shortcut word \(111110\).

For every original unsafe \(u\le M\), follow at most \(K\) returns, adding
its weight to each encountered endpoint once. A source is resolved when it
hits 1 or repeats a state, since then its full distinct value set is known.
Let \(C_{M,K}\) be the recorded capacity and \(r_{M,K}\) the initial mass
of unresolved originals. Uniformly for **every** unsafe endpoint,

\[
 C_{M,K}(y)\le C(y)\le
 C_{M,K}(y)+r_{M,K}+\frac1{M+1}.                       \tag{20}
\]

This follows by charging each unrecorded original at most once. It requires
no convergence assumption about sources beyond \(M\).
At \(M=8192\), \(K=64\), all 2941 unsafe originals are resolved at 1 within
37 returns, so \(r_{M,K}=0\). Exact rational arithmetic gives

\[
 C(31)\in[0.002674948874,\ 0.002797004288],\qquad
 C(121)\in[0.004177085212,\ 0.004299140626].             \tag{21}
\]

Using the unrounded rational lower and upper bounds, the checker verifies

\[
 C(31)^2\,121>C(121)^2\,31,\qquad
 \frac{C(31)^5}{C(121)^7}>5000.                        \tag{22}
\]

As \(121/31>1\), the first inequality proves

\[
 \frac{w_s(31)}{w_s(121)}
 =\frac{C(31)}{C(121)}(121/31)^s>1
 \quad\text{for every real }s\ge\tfrac12.             \tag{23}
\]

Thus \(Hw_s(121)>w_s(121)\) on the entire range in which (16) or its
recursive improvement guarantees summability. The second inequality,
and \(b(31)=5,b(121)=7\), similarly give

\[
 \frac{v_c(31)}{v_c(121)}>5000^c>1\quad(c>1).           \tag{24}
\]

Both natural nonlinear compactifications fail as inverse supersolutions on
a known-convergent actual edge. This refutes these two families, not every
nonlinear construction and not a source-specific occupation estimate.

### Repairing a finite defect does not close the all-source problem

The failure at 121 can be repaired positively and exactly. If \(r\ge0\)
has finite support on explicitly certified terminating \(B\)-orbits, then

\[
 V=\sum_{j\ge0}H^j r
\]

is a finite sum, with \((I-H)V=r\). Consequently

\[
 H(w+V)-(w+V)=Hw-w-r.                                 \tag{25}
\]

For \(w=w_1=C(y)/y\), (17) gives \(\|w\|_1\le150\), so
\((Hw-w)(121)\le150\). Take \(r=150\delta_{121}\) and use the thirteen
nonabsorbed states in (19) starting at 121. The resulting \(V\) has total
mass 1950 and satisfies \((I-H)V=150\delta_{121}\) exactly. Hence \(w+V\)
is still positive and summable, removes the defect at 121, and creates no
new defect elsewhere. The checker verifies this exact coboundary.

This pursues the construction beyond merely rejecting its first edge.
What is missing is a finite total budget for repairs over **all** remaining
defects. For an unproved terminating orbit the finite patch is unavailable;
even over certified orbits, an infinite sum of positive patches needs its
own mass estimate. Equation (25) does not provide that estimate or assume
it by naming a stopping time.

## 6. Source comparison and verification boundary

The nearby analytic packets were read at exact heads before freezing this
note. They concern different measures and do not supply the missing payment.

- PR159 `0e7d2841b1591073c6399f91f3b6944ebcdbdbd5`,
  [DIRECTED_BOUNDARY_CIRCULATION.md](https://github.com/GettysburgResearch/collatz/blob/0e7d2841b1591073c6399f91f3b6944ebcdbdbd5/research/allhands-global-closure-20261120/DIRECTED_BOUNDARY_CIRCULATION.md),
  DC1--DC3: positive balanced tripling currents and one-sided spatial
  coercivity for **ordinary invariant labels**. Capacity \(C\), transported
  mass \(p_j\), and \(I_j\) are not such invariant labels. Its circulation
  does not identify temporal coalescence charges with tripling fluxes.
- PR160 `6d877e718f5ef9d57fe1830912c444359718747a`,
  [CRITICAL_SINGULARITY.md](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/critical/CRITICAL_SINGULARITY.md),
  CS-001--003, and
  [SINGLE_SLICE_ENERGY.md](https://github.com/GettysburgResearch/collatz/blob/6d877e718f5ef9d57fe1830912c444359718747a/research/closure-attacks-20261120/critical/SINGLE_SLICE_ENERGY.md),
  SE-001--002: critical Dirichlet normalization loses fixed ordinary atoms,
  and finite spatial defect energy would imply rigidity under its stated
  source-qualified inputs. We retain each original \(f_0(u)\), without that
  normalization or a positive-density dependency. Their unresolved global
  propagation is not inserted into (5), (12), or (16).
- PR158 `cf49a68bf93e98c97a18dc3d1a4186faf534e422`,
  [PRIMITIVE_TRACE.md](https://github.com/GettysburgResearch/collatz/blob/cf49a68bf93e98c97a18dc3d1a4186faf534e422/research/ordinary-basin-closure-20261120/PRIMITIVE_TRACE.md),
  Sections 2--5: an exact geometric tail and finite endpoint head for a
  Jacobian-weighted all-odd-source moment, with a separate cycle obligation.
  This is distinct from the original-source tail (8), saturated first-hit
  tail (20), and cycle-inclusive target (1). Its polynomial head bound is
  explicitly unproved. We do not claim a transfer between those moments.

These are bounded scope comparisons, not reviews or blanket acceptance of
their external dependencies. The information identity and first-hit
partition are elementary; the quantitative spatial improvement in (16)
is credited to the pinned PR153 theorem.

Run from the repository root:

```bash
python -X utf8 -B experiments/creative_occupation.py --compare reports/2026-11-20-creative-closure/occupation-report.json
python -X utf8 -O -B experiments/creative_occupation.py --compare reports/2026-11-20-creative-closure/occupation-report.json
```

The report uses 23,517 original unsafe sources through 65,536 for sixteen
entropy returns, and 2941 originals through 8192 for complete first-hit
capacity. It checks 3475 exact finite-source flow identities and 10,425
convex-power inequalities, and independently sums the finite original-atom
information at clock nine to enclose the same value as the entropy
difference. In total it physically replays 27,771 actual \(B\)-edges, 72,968
accelerations, and 200,655 shortcut edges. Logarithms use outward integer
intervals at scale \(10^{30}\), range reduction, and a bounded atanh-series
remainder. Capacity uses exact rational sums with a common denominator
\(\operatorname{lcm}(1,\ldots,8193)\). Explicit exceptions remain active
under optimized Python. The map and logarithm routines adapt the author's
prior PR157 checker; this author replay is not labelled independent review.

The bounded computation certifies the numerical inequalities and the tested
physical paths. Equations (5), (12), (15), (16), and the universal parameter
ranges (23)--(24) are written deductions with their stated inputs. The
missing conclusion remains an actual upper estimate for
\(\mathcal G_N(f_0)=o(\log N)\), or another closing positive mechanism.
Neither finite information nor saturated spatial mass has been substituted
for that missing time-occupation estimate.
