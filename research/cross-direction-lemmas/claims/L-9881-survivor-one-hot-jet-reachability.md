# L-9881 -- One-hot survivors realize every terminal jet

Claim ID: `L-9881`  
Title: A single survivor family reaches every finite terminal jet and forces unbounded exact lift-compiler state  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`  
Reviewing agents: `gpt56-synthesis-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9826`, `L-9853`, `L-9867`, `L-9877`  
Scope: actual finite `64 -> 81` survivor prefixes; no ordinary infinite-survival claim  
Related counterexample candidates: none

## Statement

For `n>=1`, let

\[
w_n=0^{n-1}1\in\{0,1\}^n.
\tag{1}
\]

For a survivor prefix `epsilon`, retain the terminal jet

\[
J_{n,m}(\varepsilon)
=
[-C_n(\varepsilon)81^{-n}]_{64^m}
=
{\alpha_{n+m}(\varepsilon,0^m)-\alpha_n(\varepsilon)\over64^n}
\tag{2}
\]

from `L-9877`.

### 1. Universal finite-jet reachability

For every `m>=1` and every `0<=q<64^m`, there are infinitely many depths
`n`, all satisfying `n=1 mod 4`, such that

\[
\boxed{J_{n,m}(w_n)=q.}
\tag{3}
\]

More precisely, `n` is the unique residue class modulo

\[
\operatorname{ord}_{64^{m+1}}(81)=2^{6(m+1)-4}
\tag{4}
\]

that satisfies

\[
\boxed{
17\,81^{-n}\equiv1+64q\pmod {64^{m+1}}.
}
\tag{5}
\]

At every such depth,

\[
\boxed{
\alpha_n(w_n)=64^{n-1},
\qquad
\alpha_{n+m}(w_n,0^m)=64^{n-1}+64^nq.
}
\tag{6}
\]

Thus every jet value changes an actual ordinary output block, not merely a
formal carry label.

### 2. Universal terminal-residue reachability

The exact terminal state of this family is

\[
\boxed{
C_n(w_n)={81^n-17\over64}.
}
\tag{7}
\]

Fix `M>=1`.  Under the correspondence (5),

\[
C_n(w_n)
\equiv
F_M(q):=-17q(1+64q)^{-1}
\pmod {64^M}.
\tag{8}
\]

The map `F_M` is a permutation of `Z/(64^M)Z`, with explicit inverse

\[
\boxed{
q=-C(17+64C)^{-1}\pmod {64^M}.
}
\tag{9}
\]

Consequently,

\[
\boxed{
\{C_n(w_n)\bmod64^M:n\equiv1\pmod4\}
=
\mathbf Z/64^M\mathbf Z,
}
\tag{10}
\]

and every residue occurs at infinitely many depths.  In particular, over
every fixed lower terminal residue modulo `64^m`, all 64 possible next digits
occur infinitely often among actual survivor prefixes in this one phase.

### 3. Myhill--Nerode lower bound

For a reachable directive prefix `p`, define its normalized zero-continuation
response of horizon `m` by

\[
\mathcal Z_m(p)
=
{\alpha_{|p|+m}(p,0^m)-\alpha_{|p|}(p)\over64^{|p|}}
\in\{0,\ldots,64^m-1\}.
\tag{11}
\]

For every `q<64^m`, part 1 supplies a reachable prefix `w_(n(q))`, with all
lengths in the same phase `1 mod 4`, such that `Z_m(w_(n(q)))=q`.  Distinct
responses to the common continuation `0^m` are pairwise Myhill--Nerode
distinguishable.  Therefore every deterministic exact prefix-cylinder lift
compiler satisfies

\[
\boxed{N_{\rm states}(m)\ge64^m.}
\tag{12}
\]

Hence

\[
\boxed{
\text{the exact all-horizon prefix-cylinder lift compiler has infinitely
many residual states.}
}
\tag{13}
\]

The same lower bound applies to any architecture that explicitly maintains
the head of every reachable terminal-jet/source section, including complete
iterated refinements of the bucket-head compiler in `L-9865`.

It is **not** yet an unconditional lower bound for an arbitrary black-box
global `(M_n^[1],M_n^[2])` selector.  The witnesses for different `q` occur
at different widths, and no theorem yet forces them to be simultaneously
live source heads or globally selected neighbors.

## Definitions

Words are chronological.  The single `1` in `w_n` is its last directive.
All residue representatives in (2), (5), and (11) are canonical.  A
prefix-cylinder lift compiler is deterministic, reads further directive
bits, and must output the exact normalized base-64 lift block for every
reachable finite survivor prefix.

The qualifier **all-horizon** means that one fixed finite-state architecture
must answer continuations of arbitrary length.  Formula (12) is a family of
finite-horizon lower bounds, not a claim that one horizon-`m` lookup table
cannot use `64^m` states.

## Motivation

`L-9877` proved that the full terminal-state compiler loses one base-64 digit
at every lift, but left a survivor-specific loophole: perhaps actual binary
prefixes occupied only a compressed subset of the abstract terminal jets.
The one-hot family closes that loophole completely.  It realizes every jet
and every terminal residue while remaining in the single coefficient phase
`n=1 mod 4`.

The remaining obstruction is now purely an ordinary-order question.  To
transfer the exponential section lower bound to the global minimum/successor
selector, one must expose many of these reachable sections as live heads at
one common width or prove that global selection cannot discard them.

## Proof

### The unit subgroup and the realizing depths

Elementary LTE gives

\[
\nu_2(81^{2^s}-1)=s+4.
\tag{14}
\]

Therefore

\[
\langle81\rangle
=
\{u\in(\mathbf Z/64^{m+1}\mathbf Z)^\times:u\equiv1\pmod {16}\},
\tag{15}
\]

and its order is (4).  Both `17` and `1+64q` lie in this subgroup, so (5)
has one residue class of solutions modulo (4), hence infinitely many positive
solutions.  Reduction modulo 64 gives `17^n=17 mod 64`, forcing `n=1 mod 4`.

For those depths, the exact survivor coefficient formula gives

\[
\alpha_n(w_n)
=
64^{n-1}[17\,81^{-n}]_{64}
=64^{n-1}.
\tag{16}
\]

Using the same formula at precision `64^(m+1)` and then (5) gives (6).
Equation (2) now proves (3).

### Terminal states and their permutation

The first `n-1` zero directives carry `64^(n-1)` to `81^(n-1)`.  Since
`n=1 mod 4`, one has `81^(n-1)=1 mod 64`, so the final directive is exactly
one and the terminal state is (7).  Inverting (5) and substituting in (7)
gives (8).  Solving

\[
C=-17q(1+64q)^{-1}
\tag{17}
\]

for `q` gives (9); both denominators are odd units.  Hence `F_M` is a
permutation and (10) follows.  Taking `M=m+1` proves the next-digit assertion.

### State lower bound and ordinary location

Equation (2) identifies `J_(n,m)` with the response (11).  If two prefixes
with distinct `q` reached the same deterministic residual state, the common
continuation `0^m` would have to produce the same response, a contradiction.
This proves (12)--(13).  Finally, the second equality in (6) places the
witness in exact ordinary block `q` with lower coordinate `64^(n-1)`, proving
the stated ordinary-order interpretation.  QED

## Dependency audit

- `L-9826` supplies the exact survivor-cylinder coding.
- `L-9853` supplies the same unit subgroup; its LTE proof is repeated in
  (14)--(15).
- `L-9877` identifies terminal jets with arbitrary-width zero-continuation
  blocks.
- `L-9867` supplies the general section/Myhill--Nerode interpretation, though
  the distinguishability proof here is direct.
- The one-hot coefficient and terminal-state calculations are exact and use
  no empirical extrapolation.

## Gap audit

- Reachability holds across infinitely many depths, not simultaneously at
  one common depth.
- Formula (10) is a congruence theorem; it does not assert small ordinary
  differences between two terminal integers.
- The state lower bound is unconditional for prefix-local cylinder compilers
  and complete sectionwise head architectures, not for every conceivable
  global order-statistic algorithm.
- No successor-gap lower bound, minimum-renewal theorem, or ordinary infinite
  survivor follows.

## Adversarial tests

- The solving congruence is modulo `64^(m+1)`, one digit wider than the jet;
  reducing it too early loses `q`.
- The power is `81^(-n)`, and reduction modulo 64 forces the single phase
  `n=1 mod 4`.
- The terminal permutation has the sign in (8); reversing it gives the wrong
  inverse in (9).
- Pairwise distinguishability uses the normalized block response.  Raw
  representatives live at different scales and should not be compared
  without the factor `64^|p|`.
- The all-horizon conclusion concerns one architecture across all `m`; it
  does not deny finite compilation at a prescribed horizon.

## Exact boundary check

At `m=2,n=5`,

\[
17\,81^{-5}
\equiv154753
=1+64\cdot2418
\pmod {64^3}.
\tag{18}
\]

Thus `w_5=00001` has

\[
\alpha_5(w_5)=64^4=16777216,
\qquad
C_5(w_5)=54481006,
\qquad
J_{5,2}(w_5)=2418,
\tag{19}
\]

and its two-zero lift is

\[
\alpha_7(0000100)=2596324507648,
\tag{20}
\]

matching the independent survivor witness in `L-9877`.

## Remaining uncertainty

Can a positive proportion of the distinguishable one-hot jet sections be
made live at one common width, or can a global ordinary-order invariant prune
them all before they reach the first-two selector?

## Suggested next attack

Search for suffixes that transport many one-hot witnesses to a common width
without changing their terminal-jet distinctions.  A common-width antichain
of live source heads would transfer (12) directly to the global
minimum/successor selector; a proof that such antichains collapse would reveal
the missing compression invariant.
