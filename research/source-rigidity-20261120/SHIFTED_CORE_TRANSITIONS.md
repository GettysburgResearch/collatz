# Uniform finiteness of transitions between shifted arithmetic cores

**Status: SOURCE-QUALIFIED proposed theorem, pending independent review.**
The external input is Evertse's quantitative S-unit theorem, stated
precisely below. The reductions to that theorem and the elementary clock
bound are proved here. No existence of an escaping orbit, exclusion of
all positive cycles, or full Collatz proof is claimed.

The result concerns one actual ordinary orbit. It excludes confinement
of its shifted values to a finite prime pool, and gives a quantitative
lower bound on the number of different shifted cores along any
hypothetical nonperiodic orbit. The core coordinates themselves and
S-unit finiteness principles are not claimed as new. The specific
interface studied here is the number of **distinct defect transitions
with a prescribed ordered pair of cores**.

## 1. Ordinary map and the shifted coordinate

Let

\[
 U(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1),
 \qquad n\in 2\mathbb N+1.
\]

Fix a positive odd ordinary source and write
\(n_j=U^j(n_0)\), \(a_j=a(n_j)\), and \(m_j=n_j+1\).
Thus every \(m_j\) is a positive even integer. The exact shifted relation
is

\[
 2^{a_j}m_{j+1}=3m_j+2^{a_j}-2.                 \tag{1}
\]

A **defect step** means \(a_j\ge2\); this is merely a name for the
non-one exponent, not a new dynamical condition.

Fix a finite set \(P\) of rational primes containing 2 and 3. Put
\(s=|P|\), and for positive integers define

\[
 [m]_P=\prod_{p\in P}p^{v_p(m)},\qquad
 R_P(m)=m/[m]_P.
\]

The core is \(q_j=R_P(m_j)\). It is an ordinary positive integer
coprime to every prime in \(P\). A single set \(P\) is used throughout
each assertion. Uniform finite bounds permit its selection after a
finite history is known; no assertion silently chooses a different
\(P\) at each time.

When \(P=\{2,3\}\), write

\[
 m_j=2^{\sigma_j}3^{\tau_j}q_j,
 \quad \sigma_j\ge1,\quad\tau_j\ge0,\quad (q_j,6)=1.
                                                               \tag{2}
\]

At an exponent-one step, \(m_{j+1}=3m_j/2\), so the core does not
change, \(\sigma\) decreases by one, and \(\tau\) increases by one.
There are exactly \(\sigma_j-1\) consecutive exponent-one steps from
time \(j\), followed by a defect. In particular a positive ordinary
tail cannot have only exponent-one steps. This follows from divisibility
by successively larger powers of two, not from a p-adic completion.

At a defect, necessarily \(\sigma_j=1\). Writing \(b=a_j-1\ge1\),
(1) becomes

\[
 2^b+3^{\tau_j+1}q_j
       -2^{b+\sigma_{j+1}}3^{\tau_{j+1}}q_{j+1}=1.   \tag{3}
\]

## 2. Exact external theorem and normalization

We use Jan-Hendrik Evertse, *The number of solutions of decomposable
form equations*, **Theorem 3**, printed page 7 (PDF page index 6),
[author-hosted primary PDF](https://pub.math.leidenuniv.nl/~evertsejh/95-decforms.pdf).
The theorem was inspected in the full text and in an image of that page.

In the notation needed here, let \(K\) be a number field and
\(\mathcal S\) a finite set of its places containing every infinite
place. Let \(t=|\mathcal S|\), and let \(c_1,\ldots,c_d\in K^*\)
be arbitrary nonzero coefficients. Then

\[
 c_1u_1+\cdots+c_du_d=1,\qquad
 u_i\in\mathcal O_{\mathcal S}^*,                    \tag{4}
\]

has at most

\[
 (2^{35}d^2)^{d^3t}                                \tag{5}
\]

solutions for which every nonempty subsum of the left side is nonzero.
The coefficient heights and their prime supports do **not** occur in
this bound. The coefficients need not themselves be \(\mathcal S\)-units.

Our field is \(\mathbb Q\), our places are
\(\mathcal S=\{\infty\}\cup P\), and \(d=3\). Thus define

\[
 B_s=(9\cdot2^{35})^{27(s+1)}.                       \tag{6}
\]

Here \(s\) counts finite primes and \(s+1\) counts places. In the
basic case \(P=\{2,3\}\),

\[
 B_2=(9\cdot2^{35})^{81}=2^{2835}3^{162}<2^{3092}.
                                                               \tag{7}
\]

These constants are deliberately not optimized. The source theorem is
a bound on the number of solutions, not a supplied effective list of
their heights. Nothing below treats (6) as a bound on their sizes.

## 3. The transition theorem

### SC1: uniform bound for one ordered core pair

Fix \(P\), and fix positive integers \(q,q'\) coprime to every prime
in \(P\). Among **all** positive odd ordinary integers \(n\), there
are at most \(B_s\) distinct defect transitions

\[
 n\longmapsto n'=U(n),\qquad a(n)\ge2,
 \qquad R_P(n+1)=q,\quad R_P(n'+1)=q'.               \tag{8}
\]

The bound is uniform in the two cores and in the actual primes of
\(P\). It has no bound on \(a(n)\).

**Proof.** Write \(m=n+1=q u\) and \(m'=n'+1=q'v\), where
\(u,v\) are positive integer \(P\)-units. Set

\[
 u_1=2^{a-1},\qquad u_2=u,\qquad u_3=2^{a-1}v.
\]

All three are \(\mathcal S\)-units. Dividing (1) by two gives

\[
 u_1+\frac{3q}{2}u_2-q'u_3=1.                       \tag{9}
\]

The fixed coefficients are \((1,3q/2,-q')\). In particular the
primes of \(q,q'\) are **not** added to \(P\).

Let the three signed summands be \(X,Y,Z\). Each is nonzero. Moreover

\[
 X+Y>0,\qquad X+Z=2^{a-1}(1-m')<0,
 \qquad Y+Z=1-2^{a-1}<0.                            \tag{10}
\]

The inequalities use \(m'\ge2\) and \(a\ge2\). The full sum is
one. Thus every required subsum is nonzero. Evertse's theorem gives at
most \(B_s\) triples \((u_1,u_2,u_3)\).

The encoding is injective: \(u_1\) determines \(a\), \(q u_2\)
determines \(m\) and hence \(n\), and \(u_3/u_1\) determines
\(v\) and hence the endpoint. Distinct ordinary transitions therefore
give distinct solutions of (9). This proves (8). \(\square\)

The exponent-one exception is exact. If \(a=1\), then \(Y+Z=0\)
and (9) is degenerate. There are arbitrarily many exponent-one steps
with one prescribed core: \(m=2^h q\), for arbitrary \(h\ge2\),
already provides them when \(q\) is coprime to \(P\). Consequently
SC1 cannot be stated for all transitions.

### SC2: finite cofactor families and actual defect complexity

Let \(A,B\) be finite sets of positive core values. The total number
of distinct ordinary defect transitions whose initial core lies in
\(A\) and final core lies in \(B\) is at most

\[
 B_s |A|\,|B|.                                     \tag{11}
\]

This follows by assigning each transition to its ordered pair and
summing SC1. In particular, if both cores are at most a real number
\(H\ge1\), their number is at most \(B_s\lfloor H\rfloor^2\).
The bound overcounts inadmissible core values, which is harmless.

Suppose the actual states \(n_0,\ldots,n_N\) are pairwise distinct.
Define

\[
 D_N=\#\{0\le j<N:a_j\ge2\},\qquad
 K_N=\bigl|\{R_P(n_j+1):0\le j\le N\}\bigr|.
\]

Then

\[
 \boxed{D_N\le B_s K_N^2.}                          \tag{12}
\]

No transition is counted repeatedly because its source states are
distinct. The endpoint at time \(N\) is intentionally included in
\(K_N\). Equation (12) would not hold as an occurrence bound for an
indefinitely repeated positive cycle.

For a hypothetical nonperiodic ordinary orbit, all its states are
distinct, and there are infinitely many defects. From (11), along the
sequence of defect times \(j\),

\[
 \max\{R_P(n_j+1),R_P(n_{j+1}+1)\}\longrightarrow\infty.
                                                               \tag{13}
\]

This is a limit along defect transitions, including the maximum of
both endpoints. It does not say that one particular endpoint's core
tends to infinity at every odd time. Exponent-one runs are not counted
by (13).

### SC3: finite shifted prime support forces eventual periodicity

If, for some finite prime set, every sufficiently late \(n_j+1\) has
all its prime divisors in that set, then the ordinary orbit is
eventually periodic. More generally the same follows if, for a fixed
finite \(P\supset\{2,3\}\), its sufficiently late cores belong to a
fixed finite set.

**Proof.** Assume instead that the orbit is nonperiodic, so all its
states are distinct. After discarding the finite initial segment,
(11) bounds the number of defects by a fixed finite constant. All later
exponents would therefore equal one, contrary to the ordinary
divisibility statement following (2). \(\square\)

Every finitely generated multiplicative subgroup of
\(\mathbb Q_{>0}^*\) is contained in the unit group for some finite
prime pool. Thus eventual membership of the shifted values in one
such subgroup also implies eventual periodicity. No rank-only bound
for a general subgroup is claimed from (6): a rank-one rational
generator can involve arbitrarily many different primes.

This is an eventual-periodicity conclusion. Every positive cycle has
finite shifted prime support, so SC3 does not exclude a nontrivial
cycle or prove eventual arrival at 1.

## 4. An elementary clock for a fixed ordinary source

Let

\[
 h_0=\log_2(n_0+1),\quad \gamma=\log_2(3/2),
 \quad \alpha=1+\gamma=\log_2 3.
\]

The shifted relation gives, for every \(a\ge1\) and \(m\ge2\),

\[
 m'\le\frac32 m.
\]

One direct check subtracts the two sides after multiplication by
\(2^a\): the difference is
\(3m(2^{a-1}-1)-2^a+2\), which is zero at \(a=1\) and
nonnegative at \(a\ge2\). Hence

\[
 \log_2 m_j\le h_0+\gamma j.                        \tag{14}
\]

Let \(R_k\) be the time just after the \(k\)-th defect, with
\(R_0=0\). At time \(R_k\), exactly \(\sigma_{R_k}-1\) ones
precede the next defect. Its completion is therefore

\[
 R_{k+1}=R_k+\sigma_{R_k}
 \le R_k+\log_2m_{R_k}
 \le \alpha R_k+h_0.
\]

Iteration proves

\[
 R_k\le\frac{h_0}{\gamma}(\alpha^k-1).              \tag{15}
\]

If the first \(N\) transitions contain \(D_N\) defects, the next
defect has not finished by time \(N\). Therefore

\[
 N<R_{D_N+1}\le\frac{h_0}{\gamma}
                     (\alpha^{D_N+1}-1),
\]

and

\[
 D_N\ge
 \left\lfloor\log_{\alpha}
       \left(1+\frac{\gamma N}{h_0}\right)\right\rfloor.
                                                               \tag{16}
\]

Combining (12) and (16), for every simple prefix,

\[
 \boxed{
 K_N\ge\left[
 \frac{1}{B_s}
 \left\lfloor\log_{\alpha}
       \left(1+\frac{\gamma N}{h_0}\right)\right\rfloor
 \right]^{1/2}.}                                   \tag{17}
\]

The source \(n_0\) remains fixed in the asymptotic interpretation.
For an escaping orbit, (17) implies
\(\liminf K_N/\sqrt{\log N}\ge1/\sqrt{B_s\log\alpha}\).
The constants are very small; this is a structural count, not a
practical search bound.

There is also a fully integer conservative clock useful for exact
checks. Let \(\ell=\lceil\log_2(n_0+1)\rceil\). Since
\(m_j\le2^j m_0\), the same recurrence gives
\(R_k\le\ell(2^k-1)\). Thus

\[
 N<\ell(2^{D_N+1}-1).                              \tag{18}
\]

## 5. Optional inherited strengthening: super-square-root logarithmic growth

The elementary bound above is independent of any repository
Diophantine result. A stronger count follows **conditionally on the
specified prior theorem**, whose proof was reopened at its exact pin:

- PR145, `dd245a712f985909f541590e3f6c179b7ba011e4`;
- `research/pointwise-run-defects/COMPRESSED_DESCENT.md`;
- final section, “Allowing the number of powers to grow.”

That source states: for every \(\eta>0\) there is \(C_\eta\) such
that a simple shortcut segment of length \(L\), described by \(k\)
powered pieces and base/gap budget \(B\), satisfies

\[
 L\le C_\eta e^{\eta k}
       (\log_2(n_0+1)+B+1).                         \tag{19}
\]

Its status is PROPOSED, ineffective, with the rational p-adic Subspace
Theorem as an external dependency. Its correctness is not made
unconditional by this citation.

For the first \(N\) accelerated transitions, each exponent-one step
contributes shortcut parity letter 1. A defect \(a_j\ge2\)
contributes a final odd letter 1 and a positive block
\(0^{a_j-1}\). Merge adjacent odd letters. The whole shortcut word
is a concatenation of at most \(2D_N+1\) nonempty constant-letter
blocks. Taking each base word to be 0 or 1 gives

\[
 k\le2D_N+1,\qquad B=k,
 \qquad L=\sum_{j<N}a_j\ge N.                       \tag{20}
\]

On a nonperiodic ordinary orbit this shortcut segment is simple too:
a repeated shortcut state would imply eventual periodicity and hence
repetition of odd states. If \(D_N\le A\log N\) along an unbounded
sequence, select \(\eta>0\) with \(2\eta A<1\). Equations
(19)–(20) would give \(N\le O(N^{2\eta A}\log N)=o(N)\), a
contradiction. Consequently this pinned source implies

\[
 \frac{D_N}{\log N}\longrightarrow\infty,
 \qquad
 \boxed{\frac{K_N}{\sqrt{\log N}}\longrightarrow\infty.}        \tag{21}
\]

The first limit is an application of the inherited compressed-word
theorem; it is not advertised as newly proved by the S-unit transition
argument. It concerns the **number** of non-one exponents, which must
not be confused with their total excess \(\sum(a_j-1)\).

## 6. What remains open and what was actually checked

SC1 controls transitions between prescribed arithmetic cores. It does
not bound the number of different cores visited by a fixed source.
The lower bounds (17) and (21) are compatible with indefinite production
of new cores. Neither the prime-height dispersion of PR154 nor the
shifted approximation identities of PR156 prove a conflicting upper
bound. This missing upper bound, or a different arithmetic principle
excluding the diffuse case, is the first unsupported closing step.

The companion `CLOSURE_ATTEMPTS.md` gives the source comparison, a
direct one-defect family producing arbitrarily large new cores, and
the precise obstacles in the approximation and growing-prime attempts.
It preserves the distinction between changing local witnesses and one
all-time ordinary source.

`check_shifted_core_transitions.py` checks actual finite ordinary
transitions, core factorization, (1), (3), (9), every subsum in (10),
the exact run lengths and the integer clock (18). It also checks the
explicit local counterfamily and negative controls. Finite computation
does not verify Evertse's infinite finiteness theorem, the huge bound
(6), the optional theorem (19), or either all-time Collatz alternative.

The replay passed 3,291 transition checks from 1,097 different ordinary
sources over three prime pools, 2,946 exact run-formula checks, and 54
simple-prefix controls containing 749 odd edges and 1,493 shortcut
edges. Deliberate large-division cases include exponent 1,025. Nine
outside-pool creation controls and seven negative controls passed.
Normal and optimized (`-OO`) executions produced byte-identical
`shifted-core-report.json` output. These are finite algebra and domain
checks, not additional mathematical hypotheses.
