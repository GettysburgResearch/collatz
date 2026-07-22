# L-9908 -- Centered forced tails have an exact height cone and no positive ordinary lasso

Claim ID: `L-9908`
Title: The centered zero-block recurrence has a positive exponential height limit, while every eventually periodic control tail has a finite rational lasso obstruction
Status: `PROPOSED / CROSS-DIRECTION RECONSTRUCTION AND HEIGHT EXTENSION`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave22-fixed-width-sunit` (independent full-file cold review)
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: elementary affine iteration; local `T-9827` only for the run-coordinate crosswalk; live issue-#40 `D-8701`, `L-8701`, and `R-8701` at `e0593a9f59e7a8a8ce00106581ffa24d37963173` for independently overlapping statements
Scope: the exact `64 -> 81` zero-appended-block kernel in issue #40; autonomous finite-state abstractions and modular lassos
Related counterexample candidates: issue #40; PR #37 centered ordinary-survivor lane; PR #38 atom `ACL-N026`

## 1. Result in one paragraph

On an exact zero-appended-block tail, the ordinary nearest integer and the
itinerary bit obey

\[
 64B_{n+1}=81B_n+e_n-e_{n+1}.
\tag{1}
\]

Every positive integral path in this kernel is strictly increasing and lies
in an explicit two-sided exponential height cone.  In fact
`B_n(64/81)^n` converges to a positive real limit.  At the same time,
backward integrality identifies `B_0` with the negative of the corresponding
series in `Q_2`.  If the bit tail is eventually periodic, that series is one
rational number in both completions.  Its real size is at most `1/17`, so it
cannot equal a positive integer.  Equivalently, every proposed periodic
lasso has a finite integer numerator `D` whose forced tail state is

\[
 -D/(81^p-64^p),
\]

of absolute value at most `1/17`.  This gives a solver-independent lasso
rejection certificate and proves that an exact finite autonomous abstraction
cannot carry a positive survivor.  It does **not** exclude a genuinely
aperiodic path driven by unbounded height or completion data.

## 2. Exact forced-tail system

Let

\[
 B_n\in\mathbf Z_{\ge0},
 \qquad e_n\in\{0,1\}
\tag{2}
\]

satisfy (1) for every `n>=0`.  Put

\[
 d_n=e_n-e_{n+1}\in\{-1,0,1\},
 \qquad \beta={81\over64}.
\tag{3}
\]

For reference, integrality in (1) gives exactly the four continuation cases
recorded in issue #40:

\[
\begin{array}{c|c|c}
e_n&B_n\pmod {64}&(e_{n+1},B_{n+1})\\ \hline
0&0&(0,81B_n/64)\\
0&49&(1,(81B_n-1)/64)\\
1&0&(1,81B_n/64)\\
1&15&(0,(81B_n+1)/64).
\end{array}
\tag{4}
\]

Every other residue-symbol pair exits the zero-block kernel.

## 3. The exact ordinary height cone

### Theorem 1 -- strict escape and normalized convergence

If `B_0>=1`, then for every `n>=0`,

\[
 \boxed{B_{n+1}\ge B_n+1,}
\tag{5}
\]

and

\[
 \boxed{
 \beta^n\left(B_0-{1\over17}\right)+{1\over17}
 \le B_n\le
 \beta^n\left(B_0+{1\over17}\right)-{1\over17}.}
\tag{6}
\]

Moreover the real limit

\[
 \boxed{
 \xi_B:=\lim_{n\to\infty}\beta^{-n}B_n
 =B_0+\sum_{j\ge0}d_j{64^j\over81^{j+1}}}
\tag{7}
\]

exists and satisfies

\[
 \boxed{B_0-{1\over17}\le\xi_B
              \le B_0+{1\over17}.}
\tag{8}
\]

In particular `xi_B>0` on every positive ordinary path.

### Proof

Equation (1) gives

\[
 B_{n+1}-B_n={17B_n+d_n\over64}.
\tag{9}
\]

For `B_n>=1`, the numerator is at least `16`, so the right side is positive.
It is an integer, which proves (5) inductively.

Define the two affine heights

\[
 L_n=17B_n-1,
 \qquad U_n=17B_n+1.
\tag{10}
\]

A direct use of (1) gives the exact identities

\[
 \boxed{64L_{n+1}=81L_n+17(d_n+1),}
\tag{11}
\]

\[
 \boxed{64U_{n+1}=81U_n+17(d_n-1).}
\tag{12}
\]

Because `-1<=d_n<=1`, equation (11) implies
`L_(n+1)>=beta L_n`, while (12) implies
`U_(n+1)<=beta U_n`.  Iteration and division by `17` prove (6).

Forward iteration of (1) gives the finite identity

\[
 \boxed{
 \beta^{-n}B_n
 =B_0+\sum_{j=0}^{n-1}d_j{64^j\over81^{j+1}}.}
\tag{13}
\]

The series is absolutely convergent in the real absolute value, and

\[
 \sum_{j\ge0}{64^j\over81^{j+1}}
 ={1\over17}.
\tag{14}
\]

Equations (7)--(8) follow. **QED**

### PDR meaning of the height cone

No positive exact path can revisit an ordinary state `B`, and no bounded
ordinary-height region can contain an infinite zero-block path.  A finite
residue SCC is therefore not an ordinary lasso: every repeat necessarily
aliases a larger height.  A sound abstraction must either retain that
unbounded channel or prove that every possible channel value eventually
reaches one of the failing residue-symbol pairs omitted from (4).

## 4. The completion identity

### Theorem 2 -- the same digit series in two completions

Every integral all-time path (2), including a hypothetical positive one,
satisfies

\[
 \boxed{
 B_0=-\sum_{j\ge0}d_j{64^j\over81^{j+1}}
 \quad\hbox{in }\mathbf Q_2.}
\tag{15}
\]

Thus the series in (7) has:

- real value `xi_B-B_0`;
- `2`-adic value `-B_0`.

These values must not be identified unless an independent argument makes the
series a rational number.

### Proof

Solving (1) backwards through `N` steps gives

\[
 B_0=\left({64\over81}\right)^N B_N
     -\sum_{j=0}^{N-1}d_j{64^j\over81^{j+1}}.
\tag{16}
\]

Since every `B_N` is an integer,

\[
 \left| (64/81)^N B_N\right|_2
 \le 2^{-6N}\longrightarrow0.
\tag{17}
\]

The finite sums converge in `Q_2`, proving (15).  Equation (13) gives the
separate real value. **QED**

The distinction is essential. The real bound gives no Archimedean bound on
the ordinary integer represented by the `2`-adic value; on any hypothetical
positive path, the tail values would be unbounded by Theorem 1. Only the
rationalization in the next section permits a cross-place comparison.

## 5. Finite lasso certificates

Fix a starting index `N` and a proposed period `p>=1` satisfying

\[
 e_{N+j+p}=e_{N+j}\qquad(j\ge0).
\tag{18}
\]

Write `e_(N+p)=e_N` and define the finite integer

\[
 \boxed{
 D_{N,p}=\sum_{j=0}^{p-1}
 81^{p-1-j}64^j(e_{N+j}-e_{N+j+1}).}
\tag{19}
\]

### Theorem 3 -- exact lasso obstruction

If (18) has an integral continuation for all future times, then

\[
 \boxed{(81^p-64^p)B_N+D_{N,p}=0.}
\tag{20}
\]

Moreover

\[
 \boxed{
 |D_{N,p}|\le {81^p-64^p\over17},
 \qquad |B_N|\le {1\over17}.}
\tag{21}
\]

Consequently the only nonnegative integral lasso tail has

\[
 \boxed{B_N=0,}
\tag{22}
\]

and then (1) forces

\[
 B_n=0,\qquad e_n=e_N\qquad(n\ge N).
\tag{23}
\]

In particular, no positive ordinary forced-tail path has an eventually
periodic itinerary.

### Proof

Iteration of (1) across one period gives

\[
 64^pB_{N+p}=81^pB_N+D_{N,p}.
\tag{24}
\]

The same digit differences repeat in every period.  Solving (24) backwards
through `K` repeated periods gives

\[
 B_N=\left({64\over81}\right)^{Kp}B_{N+Kp}
 -{D_{N,p}\over81^p}
  \sum_{h=0}^{K-1}\left({64\over81}\right)^{hp}.
\tag{25}
\]

In `Q_2`, the first term tends to zero and the geometric sum converges.
Therefore

\[
 B_N=-{D_{N,p}\over81^p-64^p}
 \quad\hbox{in }\mathbf Q_2.
\tag{26}
\]

Both sides are rational, and the embedding `Q -> Q_2` is injective, so (20)
is an ordinary rational identity.

Since every digit difference has absolute value at most one,

\[
 \begin{aligned}
 |D_{N,p}|
 &\le\sum_{j=0}^{p-1}81^{p-1-j}64^j\\
 &={81^p-64^p\over81-64},
 \end{aligned}
\tag{27}
\]

which proves (21).  An integer of absolute value at most `1/17` is zero.
If `B_n=0`, equation (1) says

\[
 64B_{n+1}=e_n-e_{n+1}.
\tag{28}
\]

The right side lies in `{-1,0,1}`; integrality forces it to be zero.  Hence
`e_(n+1)=e_n` and `B_(n+1)=0`, proving (23). **QED**

### Certificate format

A proposed periodic word needs no trusted solver trace.  An independent
checker can:

1. read `p` and the `p` cyclic bits;
2. compute `D` from (19) using integers;
3. verify the one-period transition identity (24);
4. output the forced rational tail `-D/(81^p-64^p)`;
5. verify the universal bound (27).

For a positive lift, (20)--(21) are already contradictory.  This rejects the
lasso at every modulus simultaneously, rather than only up to one finite
PDR width.

## 6. Autonomous finite-state no-go

### Corollary 4 -- a finite exact controller cannot hide the height channel

Suppose that from some time `N` an exact forced-tail path admits a finite
state sequence `s_n \in S` and maps

\[
 s_{n+1}=F(s_n),
 \qquad e_n=E(s_n),
\tag{29}
\]

with `F:S->S` and `E:S->{0,1}` deterministic. Then the path is not positive.

Indeed, every orbit of a map on a finite set is eventually periodic, so its
output word `(e_n)` is eventually periodic.  Theorem 3 applies.

Therefore a finite PDR or transducer abstraction can be complete for a
positive infinite path only if at least one of the following remains outside
the autonomous finite state:

1. an unbounded ordinary-height/completion-block input;
2. genuine nondeterministic choices whose soundness is discharged later;
3. a nonlocal certificate proving that all such choices leave the kernel.

A closed modular SCC without one of these interfaces is a spurious
completion lasso, not an ordinary survivor.

## 7. Exact maximal-run crosswalk

The issue-#40 state is conjugate to the general binary chart already treated
by local `T-9827`.  Put

\[
 A_n=64B_n+e_n.
\tag{30}
\]

Then (1) is equivalent to

\[
 \boxed{64A_{n+1}=81A_n-17e_n,}
\tag{31}
\]

and `A_n \equiv e_n \pmod {64}`.  On a positive path `A_n>1`, so the exact
maximal-run zipper of `T-9827` applies.

Let a maximal run `k` have symbol `s_k`, length `ell_k`, starting index
`p_k`, and sign

\[
 \sigma_k=2s_k-1.
\tag{32}
\]

There is a positive odd integer `q_k` such that

\[
 \boxed{B_{p_k}=64^{\ell_k-1}q_k,}
\tag{33}
\]

and adjacent runs obey

\[
 \boxed{
 64^{\ell_{k+1}}q_{k+1}
 =81^{\ell_k}q_k+\sigma_k.}
\tag{34}
\]

In particular,

\[
 \boxed{
 v_2(81^{\ell_k}q_k+\sigma_k)=6\ell_{k+1},}
\tag{35}
\]

\[
 \boxed{
 q_k\equiv-\sigma_k81^{-\ell_k}
       \pmod {64^{\ell_{k+1}}}.}
\tag{36}
\]

Modulo `64`, the terminal odd-core skeleton is the following exact
four-phase table:

\[
\begin{array}{c|cccc}
&\ell_k=0&\ell_k=1&\ell_k=2&\ell_k=3\pmod4\\ \hline
s_k=0&q_k=1&q_k=49&q_k=33&q_k=17\\
s_k=1&q_k=63&q_k=15&q_k=31&q_k=47
\end{array}
\pmod {64}.
\tag{37}
\]

Here `81 \equiv17 \pmod {64}`, and `17` has order four modulo `64`.  The
entries `49` and `15` at run length one recover exactly the two switching
residues in (4).  Equations (34)--(36), rather than the four residues alone,
show the unbounded carry that a sound macro-transition must retain.

## 8. Relationship to the stronger symbolic barriers

A final live-source refresh found that issue #40 had independently published
the same recurrence in `D-8701`, strict monotonicity in `L-8701`, and the
periodic fixed-modulus lasso exclusion in `R-8701`. Those conclusions are
overlap, not claimed here as independent novelty. The additions in this
cross-direction manuscript are the sharp normalized height cone (6)--(8),
the explicit separation of the real and `Q_2` limits, and the exact
`T-9827` maximal-run crosswalk (30)--(37). The finite numerator (19) is kept
because it provides a common checker format for the overlapping lasso proof.

Theorem 3 gives a direct finite certificate for eventually periodic tails.
It is intentionally narrower than the independently developed recurrence
cone on PR #37:

- PR #37 `T-9319` forces a much larger linear factor-complexity slope for
  every nonconstant positive ordinary itinerary;
- local `T-9829` excludes eventual periodicity of maximal run lengths in
  every binary expanding chart.

The present claim contributes the exact issue-#40 state crosswalk, the
ordinary height cone, and the integer lasso certificate.  It does not claim
novelty for the bare conclusion that a positive itinerary is aperiodic.

## 9. Dependency and source audit

- Equations (5)--(28) use only finite affine iteration, geometric series,
  and injectivity of `Q -> Q_2`.
- Local `T-9827` is used only to avoid reproving the general maximal-run
  zipper in Section 7.  Substitution of (30) into its formulas gives
  (33)--(36) directly.
- Live issue-#40 claims `D-8701`, `L-8701`, and `R-8701` independently supply
  the recurrence, monotonicity, and periodic-lasso exclusion. This manuscript
  reconstructs those statements, sharpens monotonicity to the exact height
  cone, and supplies the cross-direction run zipper. It does not supply the
  requested universal safety invariant.
- PR #37 is comparison evidence only.  No unmerged PR #37 statement is a
  proof dependency.
- No computation, external theorem, density assumption, or unproved
  equidistribution statement is used.

## 10. Adversarial boundary

- **The two completion limits stay separate.**  Equation (15) is `2`-adic;
  equation (7) is real.  They are compared only after periodicity produces
  the explicit rational value (26).
- **A modular cycle is not an ordinary cycle.**  The strict height escape
  (5) shows why a residue may recur while the ordinary state never does.
- **Nondeterministic finite graphs are not excluded.**  An infinite path in
  a finite directed graph need not have an eventually periodic label word
  when fresh branch choices are allowed.  Corollary 4 assumes an autonomous
  deterministic state update.
- **Aperiodic survivors remain open.**  The exact recurrence could in
  principle be driven forever by a genuinely aperiodic unbounded carry.  No
  theorem here proves that it eventually reaches a failing row of (4).
- **The height cone points outward.**  Strict ordinary growth is not a
  termination ranking function.  It proves that any successful negative
  certificate must couple height to residue or completion blocks.
- **The trivial tails are preserved.**  `(B,e)=(0,0)` and `(0,1)` are the two
  constant zero-room paths.  They are not positive ordinary survivors.

## 11. Suggested next attack

Use (34)--(36) as the macrostate for the proof-carrying search.  For every
surviving abstract SCC, extract either:

1. a deterministic label lasso and reject it with (19)--(21); or
2. an explicit unbounded sequence of run carries `q_k` satisfying both the
   exact dyadic valuation (35) and the next odd-core cylinder (36).

The remaining negative theorem is to show that the second alternative
cannot persist.  A constructive result must retain the actual growing
`q_k`, not only its residue modulo one fixed power of `64`.
