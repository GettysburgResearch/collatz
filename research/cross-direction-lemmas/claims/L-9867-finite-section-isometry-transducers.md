# L-9867 -- Finite sections characterize bounded-state 2-adic isometries

Claim ID: `L-9867`  
Title: A 2-adic isometry has an LSF Mealy realization exactly when its rooted-tree section set is finite  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01`  
Reviewing agents: `gpt56-synthesis-01-p`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9863`; `L-9858` for the collision-chart application  
Scope: exact finite-state criterion for arbitrary 2-adic isometries and conditional application to residual-address charts  

## Definitions

Read binary words least-significant bit first.  For a word
`p=(p_0,...,p_(k-1)) in F_2^k`, write

\[
[p]=\sum_{i=0}^{k-1}p_i2^i.
\tag{1}
\]

Let `f:Z_2 -> Z_2` preserve the 2-adic distance.  Surjectivity is not being
silently assumed: every such self-map is proved below to be onto.  Its
depth-`k` prefix map is

\[
F_k(p)=f([p])\bmod 2^k
\in\{0,\ldots,2^k-1\}.
\tag{2}
\]

As proved below, `F_k` is a permutation and `f` maps every
radius-`2^(-k)` ball bijectively onto a ball of the same radius.  Hence there
is a unique map `f|_p:Z_2 -> Z_2` satisfying

\[
\boxed{
f([p]+2^kz)=F_k(p)+2^k(f|_p)(z)
\qquad(z\in\mathbf Z_2).
}
\tag{3}
\]

Call `f|_p` the **section of `f` at `p`**.  The empty-word section is `f`.
Let `pb` denote the word obtained by appending the next LSF digit
`b in F_2` to `p`.

A deterministic synchronous LSF Mealy machine consists of a finite state
set `S`, transition and output maps

\[
\delta:S\times\mathbf F_2\longrightarrow S,
\qquad
\omega:S\times\mathbf F_2\longrightarrow\mathbf F_2,
\tag{4}
\]

and an initial state.  It reads one input bit and emits one output bit at
each step.  Two accessible states are identified only when they induce the
same infinite tail map on every continuation.

## Statement

### 1. Sections are exact residual isometries

Every distance-preserving self-map of `Z_2` is surjective, and every section
`f|_p` is a surjective 2-adic isometry.  If

\[
\epsilon(h)=h(0)\bmod2
\qquad(h:\mathbf Z_2\longrightarrow\mathbf Z_2\text{ an isometry}),
\tag{5}
\]

then the sections obey the exact one-bit recursion

\[
\boxed{
(f|_p)(b+2z)
=b+\epsilon(f|_p)+2(f|_{pb})(z).
}
\tag{6}
\]

For the triangular functions of `L-9863`,

\[
\epsilon(f|_p)=\phi_k(p).
\tag{7}
\]

Thus a section is precisely the complete future transduction remaining
after a prefix has been read, not merely a finite output decoration.

### 2. Exact finite-state criterion and minimal state count

Put

\[
\operatorname{Sec}(f)
=\{f|_p:p\in\mathbf F_2^k, k\ge0\}.
\tag{8}
\]

Then

\[
\boxed{
f\text{ is realized by a finite synchronous LSF Mealy machine}
\quad\Longleftrightarrow\quad
|\operatorname{Sec}(f)|<\infty.
}
\tag{9}
\]

When these conditions hold, the canonical section machine has state set
`Sec(f)`, output and transition

\[
\boxed{
\omega(h,b)=b+\epsilon(h),
\qquad
\delta(h,b)=h|_b,
}
\tag{10}
\]

and initial state `f`.  It is minimal among deterministic synchronous
machines realizing `f`:

\[
\boxed{
N_{\min}(f)=|\operatorname{Sec}(f)|.
}
\tag{11}
\]

### 3. Sections under composition and inverse

Let `f,g` be isometries, let `p` have length `k`, and put
`q=F_k(p)`, regarded as its unique length-`k` binary word.  Then

\[
\boxed{
(g\circ f)|_p=(g|_q)\circ(f|_p).
}
\tag{12}
\]

The corresponding inverse identity is

\[
\boxed{
(f^{-1})|_q=(f|_p)^{-1}.
}
\tag{13}
\]

Consequently finite-section isometries form a group, with exact bounds

\[
\boxed{
|\operatorname{Sec}(g\circ f)|
\le
|\operatorname{Sec}(g)|\,|\operatorname{Sec}(f)|,
\qquad
|\operatorname{Sec}(f^{-1})|
=|\operatorname{Sec}(f)|.
}
\tag{14}
\]

In particular, if a collision-chart update has the conditional form from
`L-9863`,

\[
\mathcal U=\Psi_1\circ T\circ\Psi_0^{-1},
\tag{15}
\]

and all three component isometries have finite section sets, then

\[
\boxed{
|\operatorname{Sec}(\mathcal U)|
\le
|\operatorname{Sec}(\Psi_1)|
|\operatorname{Sec}(T)|
|\operatorname{Sec}(\Psi_0)|.
}
\tag{16}
\]

### 4. Triangularity alone permits unbounded memory

For a binary word `a=(a_i)_(i>=0)`, define the digitwise XOR isometry

\[
\mathcal X_a\!\left(\sum_{i\ge0}x_i2^i\right)
=\sum_{i\ge0}(x_i+a_i)2^i.
\tag{17}
\]

Its triangular functions are the constants `phi_i=a_i`, and its sections
are

\[
\boxed{
\mathcal X_a|_p=\mathcal X_{\sigma^k a}
\qquad(|p|=k),
}
\tag{18}
\]

independently of the digits of `p`.  Therefore

\[
\boxed{
|\operatorname{Sec}(\mathcal X_a)|<\infty
\quad\Longleftrightarrow\quad
a\text{ is eventually periodic}.
}
\tag{19}
\]

For example, if `a_i=1` exactly when `i` is a square, all shifts of `a` are
distinct.  The sections reached at depths at most `Q` are then exactly

\[
\boxed{
\mathcal X_a,\mathcal X_{\sigma a},\ldots,
\mathcal X_{\sigma^Q a},
}
\tag{20}
\]

so any exact machine through unbounded precision needs unboundedly many
states, even though the map is triangular and emits one bit causally.

## Proof

### Section existence, isometry, and recursion

If two length-`k` words `p,r` are distinct, then
`nu_2([p]-[r])<k`.  Exact distance preservation gives
`nu_2(f([p])-f([r]))<k`, so `F_k(p) != F_k(r)`.  Thus `F_k` is injective and,
on the finite set of `2^k` prefixes, is a permutation.

This also proves global surjectivity without assuming it.  Given
`y in Z_2`, let `p_k` be the unique prefix with
`F_k(p_k)=y mod 2^k`.  Compatibility of the reductions and uniqueness imply
that `p_(k+1)` reduces to `p_k`.  The compatible prefixes define
`x in Z_2`, and continuity of the distance-preserving map gives `f(x)=y`.

If two inputs agree modulo `2^k`, their difference has valuation at least
`k`; distance preservation gives the same statement for their outputs.
Thus the output residue modulo `2^k` in (3) is independent of `z`.  Global
surjectivity and distance preservation show that the input ball at `p` maps
bijectively onto the output ball at `F_k(p)`, so division by `2^k` defines
the unique surjective map `f|_p`.

For `z,z' in Z_2`, equation (3) gives

\[
\nu_2\bigl((f|_p)(z)-(f|_p)(z')\bigr)
=\nu_2(z-z'),
\tag{21}
\]

so every section is an isometry.  Its action modulo two is necessarily one
of the two permutations `b -> b+epsilon(f|_p)`.  To check the normalization
constant in (6), put `h=f|_p` and let
`eta=b+epsilon(h) in {0,1}`, with the addition taken in `F_2`.  Since both
prefix representatives are canonical integers,

\[
F_{k+1}(pb)=F_k(p)+2^k\eta.
\tag{21a}
\]

Expanding `f([p]+2^k(b+2z))` first at `p` and then at `pb`, and using
(21a), gives `h(b+2z)=eta+2(f|_(pb))(z)` exactly.  This proves (6), including
its output-prefix constant.  Comparing with the unique triangular form of
`L-9863` proves (7).

### Construction and minimality of the section machine

If `Sec(f)` is finite, (6) shows that (10) emits the correct next bit and
moves to the correct residual map.  Induction on the consumed prefix proves
that its state after reading `p` is exactly `f|_p`; hence it realizes `f`.

Conversely, suppose a finite deterministic synchronous machine realizes
`f`.  After it reads `p`, all already emitted bits are fixed, and its current
state determines the output on every remaining tail.  By (3), that tail map
is exactly `f|_p`.  Therefore the number of distinct sections is no larger
than the number of accessible machine states.

If two sections `f|_p` and `f|_r` are unequal, some infinite continuation
has different output under them.  Any deterministic machine must therefore
place the two prefixes in distinguishable states.  The canonical section
machine has one state per distinct section, proving (11).

### Group laws

Let `q=F_k(p)`.  Substituting the section expansion for `f` into that for
`g` gives

\[
\begin{aligned}
(g\circ f)([p]+2^kz)
&=g\bigl(q+2^k(f|_p)(z)\bigr)\\
&=G_k(q)+2^k(g|_q)\bigl((f|_p)(z)\bigr),
\end{aligned}
\tag{22}
\]

Here `q` and `G_k(q)` are the canonical length-`k` input and output prefix
representatives.  In particular, `G_k(q)` is exactly the prefix of
the composition `g` after `f`, so no high output digit is absorbed into the
section.  This is
(12).  Since `F_k` is a permutation of depth-`k` prefixes, every `q` has a
unique preimage `p`.  Inverting the exact canonical expansion (3) then gives
(13).  Every section
of a composition is among the displayed pairs of component sections, proving
the first bound in (14); (13) gives a bijection between the two inverse
section sets and proves the equality.  Applying the composition bound twice
to (15), and using the inverse equality, proves (16).

### The strict triangular counterexample

The first differing input digit remains the first differing output digit
under digitwise XOR, so (17) is an isometry.  Once `k` low digits have been
removed, its remaining mask is exactly the shifted word `sigma^k a`; this
proves (18).

Two shifts of `a` are equal exactly when `a` is periodic from the earlier
shift onward.  Hence the shift orbit is finite exactly when `a` is eventually
periodic, proving (19).  For the square-indicator word, the gaps between
successive ones are unbounded while ones occur infinitely often.  It cannot
be eventually periodic, and equality of any two shifts would make it so.
Thus its first `Q+1` shifted masks are distinct, proving (20) and completing
the claim. QED

## Motivation

`L-9863` proves that triangularity is automatic for every 2-adic isometry,
but its extension count shows that arbitrary new truth tables remain possible
at every depth.  The present theorem identifies the exact missing property:
a bounded-memory realization exists precisely when the full tail maps recur
among finitely many rooted-tree sections.

This criterion is directly usable in the collision lane.  It turns the vague
request for a bounded local correction grammar into a concrete algebraic
question about sections, and (12)--(16) allow chart, affine, and conjugacy
pieces to be audited separately.

## Dependency audit

- `L-9863` supplies the unique triangular form and compatible rooted-tree
  reductions of a 2-adic isometry.
- `L-9858` supplies the residual-to-address isometries motivating the chart
  specialization; it does not supply their finite-section property.
- Section existence, the exact machine criterion, minimality, group laws,
  state bounds, and the XOR counterexample are proved directly here.
- No automata minimization software, connector formula, or completed ordinary
  address is imported.

## Gap audit

- `L-9858` and `L-9863` prove isometry and triangularity, not finiteness of
  the relevant section sets.
- Bound (16) is conditional on finite-section component maps.  It supplies no
  such bound for a physical connector by itself.
- A finite machine for every separately fixed precision is automatic and is
  much weaker than one machine working through unbounded precision.
- The theorem concerns synchronous one-input-bit/one-output-bit machines.  A
  variable-length or asynchronous rewrite requires a separate criterion.
- Finite sections give bounded state, not ordinary stabilization of the
  residual or address word.

## Adversarial tests

- Arbitrary residue permutations modulo `2^Q` are not valid states here;
  sections use compatible ball-preserving reductions of one isometry.
- The output prefix in (3) is `F_k(p)`, not `f([p])` as an unrestricted
  2-adic integer.  The latter would move high output digits into the wrong
  section.
- A repeated triangular truth table at two depths is not enough.  Equality of
  sections means agreement of the entire future transduction.
- Distinct prefixes can have the same section and should then merge in the
  minimal machine; equal output prefixes are neither necessary nor sufficient
  for that merge.
- The square-mask example is causal at every digit.  Its obstruction is
  unbounded depth memory, not lookahead.
- Composition may identify many pairs of component sections, so (14) is an
  upper bound rather than an asserted product formula.

## Remaining uncertainty

Do the normalized residual-to-address isometries and odd-affine zipper maps
arising in consecutive physical scales have a uniformly finite union of
sections?  By this claim, that is exactly the synchronous bounded-state
question; triangularity alone no longer obscures it.

## Suggested next attack

Compute symbolic sections of one connector scale from its quadratic bulk
recurrence, not merely its finite truth table.  Use (12) to transport them
through the odd-affine zipper and (13) through chart inversion.  Either close
the resulting section family under both input bits, yielding a certified
finite Mealy grammar, or exhibit one invariant that separates sections at
arbitrarily large depths.
