# A quantitative necessary escape from the shifted smooth class

**SOURCE-QUALIFIED proposed theorem.** For one fixed positive ordinary
source, every counterexample to Collatz must visit shifted values with a
prime outside `{2,3}` at least logarithmically often. This covers both a
nonperiodic orbit and a hypothetical nontrivial positive cycle. It gives
a sufficient convergence condition allowing sparse arithmetic exceptions;
no unconditional upper bound for those exceptions is proved.

The frozen dependencies are:

* `SHIFTED_CORE_TRANSITIONS.md`, SHA-256
  `f53846e08e1522058797c6cab57111cf9c7ed4385f39b0e055ab05264f7acb71`,
  SC1 and the elementary clock, equations (15)–(16). Its external
  dependency is Evertse's S-unit theorem. The optional PR145
  compressed-word theorem is not used.
* `SHIFTED_SMOOTH_CYCLES.md`, SHA-256
  `e3db28e9e944a36dacd54f661cda8a1856664bfac3d248caefdf23b1a9875c60`,
  SS2: the only positive odd cycle whose every shifted value is
  `{2,3}`-smooth is `{1}`. That cycle theorem is elementary.

Use the positive odd map `U(n)=(3n+1)/2^{v_2(3n+1)}` and one fixed
source `n_0`. Let `n_j=U^j(n_0)`, `a_j=v_2(3n_j+1)`, and let `q_j`
be the factor of `n_j+1` remaining after all powers of 2 and 3 are
removed. Define

\[
D_N=\#\{0\le j<N:a_j\ge2\},\qquad
C_N=\#\{0\le j\le N:q_j>1\}.
\tag{1}
\]

The endpoint `N` is intentionally included in `C_N`. It counts visits,
with multiplicity, and not the number of distinct cores. Write

\[
B_2=(9\cdot2^{35})^{81},\quad
h_0=\log_2(n_0+1),\quad
\gamma=\log_2(3/2),\quad\alpha=\log_2 3.
\tag{2}
\]

Unsubscripted logarithms below are natural logarithms.

## SE1. A finite-prefix inequality

Suppose `n_0,...,n_N` are pairwise distinct. SC1 permits at most `B_2`
defect edges with ordered core pair `(1,1)`. Every other defect edge
has at least one endpoint with `q_j>1`. Each such vertex is incident
with at most two edges of this path. Therefore

\[
\boxed{D_N\le B_2+2C_N.}
\tag{3}
\]

The factor two cannot be removed from this incidence argument: the
actual ordinary segment

\[
17\xrightarrow{a=2}13\xrightarrow{a=3}5
\]

has two defects touching just one outside-class vertex. Its shifted
cores are respectively `1,7,1`.

The source-pinned elementary clock gives

\[
D_N\ge
\left\lfloor\log_{\alpha}
\left(1+\frac{\gamma N}{h_0}\right)\right\rfloor.
\]

Consequently every such simple prefix satisfies the explicit bound

\[
\boxed{
C_N\ge\frac12\left[
\left\lfloor\log_{\alpha}
\left(1+\frac{\gamma N}{h_0}\right)\right\rfloor-B_2
\right].}
\tag{4}
\]

One may replace a negative right side by zero. The finite additive
constant is enormous; (4) is a structural inequality, not a useful
numerical stopping test at current computation scales.

## SE2. A necessary property of every actual counterexample

If the fixed orbit never reaches 1, there are two exhaustive cases.
If no state repeats, all prefixes are simple and the orbit is
nonperiodic. If a state repeats, determinism makes the orbit eventually
periodic; its cycle cannot contain 1. A repeated state before a first
visit to 1 is impossible, which is also why every actual first-hit
prefix is simple.

In the nonperiodic case, (4) holds for every `N`, and hence

\[
\liminf_{N\to\infty}\frac{C_N}{\log N}
\ge\frac1{2\log\alpha}.
\tag{5}
\]

In the periodic counterexample case, SS2 guarantees at least one
outside-class vertex in its cycle. If the period has `p` odd states
and `r>=1` of them have `q>1`, then

\[
C_N=\frac rpN+O_{n_0}(1),
\qquad\frac{C_N}{\log N}\longrightarrow\infty.
\tag{6}
\]

Thus (5) is necessary for **every** counterexample, including a
nontrivial cycle. In particular,

\[
\boxed{
\liminf_{N\to\infty}\frac{C_N}{\log N}
<\frac1{2\log(\log_2 3)}
\quad\Longrightarrow\quad n_0\text{ reaches }1.}
\tag{7}
\]

The condition `C_N=o(log N)` is sufficient. Eventual shifted smoothness
would make `C_N` bounded; condition (7) does not assume boundedness in
advance. No assertion is made that there exists an actual terminating
orbit with infinitely many exceptions: after a visit to 1 all later
shifted values are 2. The substantive result is the finite-prefix
inequality (4) and the necessary logarithmic frequency (5), rather
than a claim about a newly exhibited larger set of ordinary starts.

## The remaining obligation

There is no proved upper estimate of the form (7) for an arbitrary
ordinary source. The S-unit bound controls repeated use of one
ordered core pair; it permits the introduction of new cores.
The endpoint capacity estimates do not control this visit count.
PR157's smaller-charge occupation theorem bounds reciprocal-height
charge with periodic states removed; it does not bound the number
of outside-class visits and cannot supply (7).

A concrete next obligation is to prove a source-persistent upper
bound below the threshold in (7), or an independent restriction on
the creation and reuse of nonsmooth shifted cores. Counts over
different starting integers, reciprocal-height summability, and
bounded computations along a long finite prefix do not establish
that bound. The present synthesis therefore strengthens the
necessary arithmetic behavior of a counterexample without resolving
the unrestricted conjecture.
