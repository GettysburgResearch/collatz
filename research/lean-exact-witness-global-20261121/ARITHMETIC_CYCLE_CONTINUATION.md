# Uniform arithmetic separation and cycle occupation

Date: 2026-11-22. **Status: written deduction from the published S-unit
input and the frozen arithmetic-return theorem. Full Collatz and exclusion
of all nontrivial positive cycles remain OPEN.**

This continuation upgrades a return to an unspecified finite core into
**finiteness of the entire set of sparse endpoint pairs**, at every fixed
nonexceptional odd separation. The intermediate step is an explicit,
elementary upper bound on the full ordinary clock of an orbit beginning
with few binary runs. It also gives a uniform finite-window occupation
inequality, valid for every actual orbit, and a finiteness theorem for
cycles having a prescribed positive fraction of low-complexity states.
Every unbounded nondecreasing run moment diverges on an escaping ordinary
shortcut orbit and is proper on the set of positive cycles.

The map is the accelerated odd map

\[
 U(n)=(3n+1)/2^{v_2(3n+1)}
\]

on positive odd integers. The ordinary map is the shortcut map
\(T(n)=n/2\) for even \(n\), \(T(n)=(3n+1)/2\) for odd \(n\).
An accelerated step with valuation \(a\) takes exactly \(a\) shortcut
steps. Let \(R(n)\) count maximal runs of ones in the ordinary binary
expansion of a positive integer.

## 1. A bound on the actual ordinary clock from the initial run count

### Lemma AP1: one power perturbation

If \(u\ge0\) and \(k\ge0\), then

\[
 |R(u+2^k)-R(u)|\le1, \qquad R(0):=0. \tag{AP1}
\]

Indeed, adding \(2^k\) changes either one zero to one, or changes the
consecutive string of ones beginning at position \(k\) to zeros and
changes the next zero to one. In the first case the new bit creates one
run, extends a neighboring run, or joins two neighboring runs. In the
second case, inspect the unchanged bit below the string and the unchanged
bit above the newly created one: the alteration replaces one intervening
run by at most two and can remove at most one run. Leading zero bits may
be appended before this argument, so the highest-bit case is included.
These alternatives give (AP1). Subtracting one power, when the result is
nonnegative, has the same bound by reversing the addition.

If \(u\) is odd, the carry for adding one begins at the lowest bit and
there is no unchanged lower run. It follows more specifically that

\[
 R(u+1)\le R(u) \quad (u\text{ odd}). \tag{AP2}
\]

### Lemma AP2: valuation and run growth

For every positive odd integer \(n\), with \(a=v_2(3n+1)\),

\[
 \boxed{a\le2R(n),\qquad R(U(n))\le3R(n).} \tag{AP3}
\]

**Valuation bound.** The least nonnegative solution to
\(3n+1\equiv0\pmod {2^a}\) is

\[
 r_{2k}=\sum_{j=0}^{k-1}4^j,\qquad
 r_{2k+1}=\sum_{j=0}^{k}4^j.
\]

Here the even formula is used for \(k\ge1\) and the odd formula for
\(k\ge0\). Their binary expansions have respectively \(k\) and
\(k+1\) separate ones. They are exactly the lowest \(a\) bits of
\(n\). Extending those bits upwards cannot join two of their distinct
runs, so \(R(n)\ge\lceil a/2\rceil\).

**Run bound.** Use the canonical signed expression

\[
 n=\sum_{j=1}^{R(n)}(2^{b_j}-2^{c_j}),
 \qquad 0\le c_1<b_1<c_2<b_2<\cdots<c_{R(n)}<b_{R(n)}.
\]

Starting at \(n\), add the \(R(n)\) positive powers
\(2^{b_j+1}\), then subtract the \(R(n)\) powers \(2^{c_j+1}\).
The final value is \(3n\). Every intermediate subtraction leaves a
positive value, since the sum of the remaining subtractions is exactly
its excess over \(3n>0\). Lemma AP1 therefore gives
\(R(3n)\le R(n)+2R(n)=3R(n)\). Since \(3n\) is odd, (AP2) gives
\(R(3n+1)\le3R(n)\). Removing trailing zero bits preserves run count,
which proves the second half of (AP3). ∎

The tempting sharper inequality \(R(3n+1)\le2R(n)\) is false:
\(n=227=(11100011)_2\) has two runs, while
\(3n+1=682=(1010101010)_2\) has five. No sharper inequality is used.

### Theorem AP3: explicit properness at a fixed odd clock

Let \(q_i=U^i(n)\), \(a_i=v_2(3q_i+1)\), and
\(A_h=\sum_{i<h}a_i\), on the same actual orbit. If \(R(n)\le S\),
then for every \(h\ge0\),

\[
 R(q_i)\le3^i S,\qquad
 \boxed{A_h\le S(3^h-1).} \tag{AP4}
\]

The first bound follows by induction from (AP3), and the second follows
by summing \(a_i\le2\cdot3^i S\). In particular the ordinary clock
has been bounded without imposing any new cap on the supplied actual
valuations.

The exact affine identity

\[
 3^h n+C_h=2^{A_h}q_h,\qquad
 C_h=\sum_{i<h}3^{h-1-i}2^{A_i}\ge0
\]

now gives

\[
 \boxed{3^h n\le2^{S(3^h-1)}U^h(n).} \tag{AP5}
\]

Thus for fixed \(S,h,B\), every positive odd integer with
\(R(n)\le S\) and \(U^h(n)\le B\) satisfies
\(n\le2^{S(3^h-1)}B\). This is a uniform finite-preimage statement
for the restriction to bounded run count; no eventual-convergence or
periodicity premise is involved.

## 2. Finite sparse-endpoint pairs

We use the precise finite sets from
[LITERATURE_ARITHMETIC_RETURN.md](LITERATURE_ARITHMETIC_RETURN.md), frozen
at PR177 head `e4ca639326bac73da8c2a698dec8a749e5efbe68`:

* \(\mathscr R_d\) is the finite set of positive coordinate ratios in
  nondegenerate signed \(\{2,3\}\)-unit zero relations having at most
  \(d\) terms;
* \(\delta_d=\min\mathscr R_d\);
* \(\mathscr H_S=\{|v_3(r)|:r\in\mathscr R_{4S},\ v_3(r)\ne0\}\).

Finiteness is the explicit application there of Evertse–Schlickewei–Schmidt,
*Linear equations in variables which lie in a multiplicative group*,
Annals of Mathematics 155 (2002), Theorem 1.1.
[Published primary source](https://annals.math.princeton.edu/2002/155-3/p04);
[authors' paper](https://arxiv.org/pdf/math/0409604).
The external theorem remains a written input, not a Lean axiom.

### Theorem AP4: global finiteness at every nonexceptional separation

Fix \(S\ge1\) and \(h\ge1\) with \(h\notin\mathscr H_S\).
Write \(\delta_{4S+h}=P/Q\) in lowest terms, with \(P,Q\ge1\).
Every actual pair

\[
 m=U^h(n),\qquad R(n)\le S,\quad R(m)\le S
\]

satisfies

\[
 \boxed{
 n< B_{S,h}:=2^{S(3^h-1)+h}Q,
 \qquad m<2^{2h}Q.
 } \tag{AP6}
\]

In particular, **there are only finitely many such pairs of ordinary
integers**, even if no lower floor is assumed for the intermediate orbit.

**Proof.** Theorem 2 of the frozen arithmetic-return note gives an actual
odd input \(q_i\), with \(0\le i<h\), such that
\(q_i<2^hQ\). Applying (AP5) at this same clock \(i\) gives

\[
 n\le2^{S(3^i-1)}q_i
 <2^{S(3^h-1)+h}Q.
\]

For positive odd \(q\), \(U(q)\le(3q+1)/2\le2q\).
Consequently \(m\le2^{h-i}q_i<2^{2h}Q\). All the values in this
argument belong to the supplied actual orbit. ∎

The constants remain ineffective unless the finite unit-ratio sets are
effectively determined; the published ESS finiteness/count statement by
itself is not a bound for the sizes of those ratios. The factor multiplying
\(Q\) and the dependence of the ordinary clock on \(S,h\) are explicit.
No bound uniform in the unbounded separation \(h\) is asserted.

## 3. A uniform finite-window occupation inequality

The previous note proved an upper Banach density statement after assuming
escape. The finite-pair bound gives the following inequality before any
orbit limit is taken.

### Theorem AP5

For every \(S\ge1\) and integer \(K\ge2\), there exist integers
\(D\ge1\) and \(B\ge1\), depending only on \(S,K\), such that
for **every** actual positive odd orbit \((q_j)\), every \(J\ge0\),
and every \(N\ge1\),

\[
\boxed{
\#\{J\le j<J+N:R(q_j)\le S\}
\le
\#\{J\le j<J+N:q_j<B\}
+D\left\lceil\frac{N}{DK}\right\rceil.
} \tag{AP7}
\]

In particular the last term is at most \(N/K+D\).

**Proof.** Take

\[
 D>\max(\mathscr H_S\cup\{0\}),\qquad
 B=\max_{1\le r<K}B_{S,rD}.
\]

Each \(rD\) lies outside \(\mathscr H_S\). If two indices
\(i<j\), with difference one of \(D,2D,\ldots,(K-1)D\), both
have run count at most \(S\), (AP6) forces the **earlier** value
\(q_i<B\). Therefore, among indices with \(q_j\ge B\), each
set of at most \(K\) consecutive slots in one residue class modulo
\(D\) contains at most one low-run visit.

Partition the given interval, starting at \(J\), into blocks of
\(DK\) consecutive indices and one possible shorter final block.
Each such block contributes at most \(D\) high-value, low-run visits.
Every remaining low-run visit is counted by the finite-core term in
(AP7). This proves the displayed inequality. ∎

This estimate does not assume that the whole interval stays above its
floor. The contribution of actual visits below \(B\) is explicitly
retained. This avoids replacing a source-conditioned return by an
unconditional mixing statement.

## 4. Consequences for the cycle alternative

### Corollary AP6: uniform sparsity on cycles of large minimum

For the same \(S,K,B\), every positive odd cycle with all its states
at least \(B\) has

\[
 \boxed{
 \frac{\#\{q\text{ in one primitive odd period}:R(q)\le S\}}
      {\text{odd period}}
 \le\frac1K.
 } \tag{AP8}
\]

Apply (AP7) to arbitrarily many traversals of the same cycle, divide by
the number of steps, and let that number grow. The additive \(D\)
vanishes. Repeated traversals have not been counted as distinct cycles.

For every fixed \(S\ge1\) and \(\varepsilon>0\), it follows that
there are only finitely many positive cycles on which at least an
\(\varepsilon\) fraction of the odd states have at most \(S\) runs.
Indeed, choose \(K\) with \(1/K<\varepsilon\). Every such cycle
contains an odd integer below the resulting \(B\). Distinct cycles
are disjoint, by determinism, and there are only finitely many such
integers.

Equivalently, along every sequence of pairwise distinct positive cycles,

\[
 \frac{\#\{q\text{ in the cycle}:R(q)\le S\}}
      {\text{odd period}}
 \longrightarrow0
 \quad\text{for every fixed }S. \tag{AP9}
\]

This is a restriction on an infinite family of cycles. It does not rule
out a single additional cycle, or assert that any additional cycle exists.

### Corollary AP7: general unbounded moments

Let \(F:\mathbb N\to[0,\infty)\) be nondecreasing and unbounded.
For every escaping positive odd orbit,

\[
 \inf_{J\ge0}\frac1N\sum_{J\le j<J+N}F(R(q_j))
 \longrightarrow\infty. \tag{AP10}
\]

For the finite-core term in (AP7), escape makes the total number of visits
below each fixed \(B\) finite. Hence the low-run sets have upper Banach
density zero. At each fixed \(S\), the lower limit of the displayed
averages is at least \(F(S+1)\); then let \(S\) grow.

Likewise, the average of \(F(R(q))\) over a primitive positive cycle
tends to infinity along every sequence of pairwise distinct cycles, by
(AP9). Thus every fixed upper bound on that average permits only finitely
many positive cycles. These statements apply to arbitrarily slowly growing
\(F\); exponential weights are not required.

## 5. Transfer to the same ordinary shortcut clock

### Corollary AP8: ordinary-time divergence on every escape

For every positive integer \(x\) whose ordinary shortcut orbit escapes,
and every nonnegative, nondecreasing, unbounded \(F\),

\[
 \boxed{\frac1L\sum_{k<L}F(R(T^k(x)))\longrightarrow\infty.} \tag{AP11}
\]

This is an initial-segment Cesàro statement on the **same** ordinary
orbit. No assertion uniform over ordinary starting times is needed or made.
In particular, long intervals of halvings are not assigned the weight of a
single odd step.

**Proof.** First take an odd start \(q_0=x\). With the actual odd states
\(q_j\), gaps \(a_j\), and shortcut clocks \(A_N\) from Section 1,
the edge equations give the exact logarithmic telescope

\[
 A_N=N\log_2 3+\log_2q_0-\log_2q_N
 +\sum_{j<N}\log_2\!\left(1+\frac1{3q_j}\right). \tag{AP12}
\]

Escape gives \(q_j\to\infty\), so the final sum is \(o(N)\), by
Cesàro averaging. Since \(q_N\ge1\),

\[
 A_N\le N\log_2 3+o(N). \tag{AP13}
\]

Fix \(S\). Among the first \(N\) odd states, \(N-o(N)\) have
run count greater than \(S\), by the odd-time result. They occur at the
distinct, actual shortcut clocks \(A_0,\ldots,A_{N-1}\).

For an arbitrary large shortcut horizon \(L\), choose \(N\) with
\(A_N\le L<A_{N+1}\). The first \(N\) odd states are all included
before \(L\), even if \(L\) lies deep inside the next halving block.
Crucially, apply (AP13) at \(N+1\), not only at \(N\):

\[
 L<A_{N+1}\le(N+1)\log_2 3+o(N+1).
\]

It follows that

\[
 \boxed{
 \liminf_{L\to\infty}\frac1L
  \#\{0\le k<L:R(T^k(q_0))>S\}
 \ge\log_3 2.
 } \tag{AP14}
\]

For each fixed \(S\), the lower limit of the averages in (AP11) is
therefore at least \((\log_3 2)F(S+1)\). Let \(S\) grow. If the
original \(x\) is even, its initial finite sequence of halvings ends at
an odd source. Omitting or adding that fixed finite initial segment does
not affect divergence of nonnegative Cesàro averages, so the same conclusion
holds for the original \(x\). ∎

The density conclusion in (AP14) is deliberately weaker than density one.
Rare long halving blocks could put substantial ordinary-time mass on
low-run states; the proof has not eliminated them. Controlling the final partial halving block is sufficient for divergence
of every unbounded moment.

### Corollary AP9: ordinary-time moments are proper on positive cycles

Let a positive cycle have primitive odd period \(r\) and ordinary
shortcut period \(A\). Multiplying its actual odd edges gives

\[
 2^A=\prod_{j<r}\left(3+\frac1{q_j}\right)\le4^r,
 \qquad A\le2r. \tag{AP15}
\]

Every odd state is one of the ordinary samples in that same period.
Consequently

\[
 \boxed{
 \frac1A\sum_{k<A}F(R(T^k(q_0)))
 \ge\frac12\,\frac1r\sum_{j<r}F(R(q_j)).
 } \tag{AP16}
\]

By Corollary AP7, the ordinary-period mean therefore tends to infinity
along every sequence of pairwise distinct positive cycles. Every fixed
bound on that mean permits only finitely many positive cycles.

In fact, their minima tend to infinity, so
\(A/r\) lies between \(\log_2 3\) and
\(\log_2(3+1/\min q_j)\), and tends to \(\log_2 3\).
The constant one half in (AP16) is the simple uniform bound; no
asymptotic replacement is needed for the finiteness conclusion.

## 6. What this changes, and the unsupplied global step

The new arithmetic conclusion controls the whole pair of sparse ordinary
endpoints uniformly over all positive sources. The elementary clock bound
(AP4) is what rules out a remote bounded-run source dropping into the finite
core by an unbounded valuation in a fixed number of odd steps. The finite
occupation inequality then treats escaping and periodic alternatives in
one statement, retaining the actual finite-core contribution.

I also tested Corvaja–Zannier (2005), *S-unit points on analytic
hypersurfaces*, Theorem 1
([primary paper](https://numdam.org/item/10.1016/j.ansens.2004.09.003.pdf)),
on multivariable fixed-block cycle quotients. Comparable block exponents
satisfy its growth conditions, but the relevant positive-cycle conclusion
is subsumed by PR183, head
`68345f60a4f757acb42a69a4ac95910f8ce26163`,
`research/profound-step-20261122/arithmetic/FREE_EXPONENT_CYCLES.md`,
BC-T3: that result already handles all independent exponents in a fixed
finite list of mixed parity blocks, effectively. No weaker fixed-schema
finiteness theorem is claimed as progress here.

Neither (AP7) nor the existing fixed-block classification supplies a
universal upper bound on run moments or a universal compression theorem.
An individual nontrivial cycle could have high run complexity throughout;
a hypothetical escape must have increasingly high complexity in occupation.
The new result makes those alternatives more uniform and precise, but
neither is contradicted by the current argument. The global arithmetic
step would need to force low-complexity occupation or a successful descent
on the **same** unresolved ordinary orbit, without assuming that its
parity word belongs to a fixed bounded-complexity language.

## Evidence boundary

* AP1–AP3 have elementary written proofs above. The separate module
  `lean/Collatz/BinaryRunClock.lean` defines the actual recursive binary
  run count (`fromBit`, `runs`) and proves `gap_bound`,
  `triple_add_one_runs`, `edge_runs`, `prefix_clock_bound`,
  `capped_prefix_clock`, `prefix_runs_bound`, `source_height_bound`, and
  `capped_endpoint_source_bound`. In particular it checks the all-input
  valuation bound, ordinary-clock bound, and finite source ceiling without
  importing AP1 as a premise. Its multiplication-by-three proof uses a
  finite carry automaton and establishes the stronger inequality
  `runs (3*n+1)+1 ≤ 3*runs n` for odd inputs.
* AP4–AP9 are written deductions using the explicitly pinned ESS return
  theorem and the finite clock result. The S-unit input and the infinite
  finiteness/packing conclusions are not counted as Lean declarations.
* Small exploratory arithmetic checks were used only to reject an overly
  sharp run-growth guess; they are not premises of any stated theorem.
* No finite cycle enumeration or computational verification of Collatz is
  claimed. Publication and any additional finite Lean consumers are reported
  by the root checkpoint separately.
