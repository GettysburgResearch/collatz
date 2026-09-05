# L-9885 -- Centered renewal digits are survivor block digits

Claim ID: `L-9885`
Title: Centered nearest-cylinder renewal digits exactly classify unchanged survivor blocks and minimum plateaux
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01-b`
Reviewing agents: `gpt56-synthesis-01`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: `PR16/L-9313`, `PR16/L-9314`, `L-9877`, `L-9883`
Scope: finite `64 -> 81` survivor cylinders, centered nearest-integer residues, and ordinary minima
Related counterexample candidates: none

## Setup

Fix a finite or infinite binary word beginning

\[
e_0e_1e_2\cdots.
\tag{1}
\]

In the centered nearest-integer recurrence of `PR16/L-9313`, let `R_k` be
the least initial representative modulo `64^k` that realizes the first `k`
transitions through the digit `e_k`. Put `R_0=0`. Upon adjoining `e_(k+1)`,
the appended base-64 digit of `PR16/L-9314` is

\[
q_k={R_{k+1}-R_k\over64^k}\in\{0,\ldots,63\}.
\tag{2}
\]

For a survivor prefix `epsilon` of length `n` and suffix `u` of length `m`,
use the block key from `L-9877` and `L-9883`:

\[
K_{n,m}(\varepsilon,u)
=
[J_{n,m}(\varepsilon)+81^{-n}r_m(u)]_{64^m},
\tag{3}
\]

so that

\[
\alpha_{n+m}(\varepsilon u)
=\alpha_n(\varepsilon)+64^nK_{n,m}(\varepsilon,u).
\tag{4}
\]

## Statement 1 -- exact centered/survivor crosswalk

For every finite word of length `k+1`,

\[
\boxed{
\alpha_{k+1}(e_0\cdots e_k)=e_0+64R_k.
}
\tag{5}
\]

Consequently, for every split into a length-`n` prefix and length-`m`
suffix,

\[
\boxed{
K_{n,m}(\varepsilon,u)
={\alpha_{n+m}(\varepsilon u)-\alpha_n(\varepsilon)\over64^n}
=\sum_{j=0}^{m-1}q_{n-1+j}64^j.
}
\tag{6}
\]

In particular, the following conditions are equivalent:

\[
\boxed{
\begin{aligned}
K_{n,m}(\varepsilon,u)=0
&\iff q_{n-1}=\cdots=q_{n+m-2}=0\\
&\iff R_{n-1}=R_n=\cdots=R_{n+m-1}\\
&\iff \alpha_{n+m}(\varepsilon u)=\alpha_n(\varepsilon).
\end{aligned}
}
\tag{7}
\]

Thus a survivor block is zero exactly when the centered nearest-integer
cylinder keeps its old ordinary representative throughout the suffix. For a
fixed prefix `epsilon`, at most one suffix of any prescribed length has this
property.

## Proof of Statement 1

Choose any infinite extension of the finite word under discussion.
`PR16/L-9313` gives, in the `2`-adic completion,

\[
B_0^*={\Phi(e)-e_0\over64}.
\tag{8}
\]

For a finite prefix through `e_k`, reduction modulo `64^k` says

\[
\alpha_{k+1}(e_0\cdots e_k)
\equiv e_0+64R_k\pmod {64^{k+1}}.
\tag{9}
\]

Both sides are the canonical representatives in `[0,64^(k+1))`: indeed,

\[
0\le e_0+64R_k\le64^{k+1}-63.
\tag{10}
\]

This proves the exact equality (5), not merely a congruence.

Subtract (5) at lengths `n+m` and `n`, and telescope (2):

\[
\begin{aligned}
\alpha_{n+m}-\alpha_n
&=64(R_{n+m-1}-R_{n-1})\\
&=64\sum_{j=0}^{m-1}q_{n-1+j}64^{n-1+j}.
\end{aligned}
\tag{11}
\]

Division by `64^n` and comparison with (4) proves (6). All digits in (6)
lie in `0,...,63`, so their base-64 sum is zero exactly when every digit is
zero. This proves (7). One-step zero-child uniqueness from `PR16/L-9314`
iterates to give uniqueness of the whole suffix. **QED**

## Statement 2 -- the finite renewal sieve

Let `S_n^(nt)` denote the nontrivial canonical survivor representatives at
depth `n`. Define

\[
\mathcal P_{n,m}
=\{\alpha_n(\varepsilon)\notin\{0,1\}:
 \text{some }u\in\{0,1\}^m
 \text{ has }K_{n,m}(\varepsilon,u)=0\}.
\tag{12}
\]

Then

\[
\boxed{
S_{n+m}^{(nt)}\cap[0,64^n)=\mathcal P_{n,m},
\qquad
\mathcal P_{n,m+1}\subseteq\mathcal P_{n,m}.
}
\tag{13}
\]

If `P_(n,m)` is nonempty, the global nontrivial minimum is exactly

\[
\boxed{
M_{n+m}^{[1]}=\min\mathcal P_{n,m}.
}
\tag{14}
\]

For a prefix `epsilon`, define its zero-renewal lifetime

\[
\ell_n(\varepsilon)
=\sup\{m\ge0:\text{an }m\text{-digit zero-renewal suffix exists}\}.
\tag{15}
\]

The value may be infinite. For fixed `n`, the following are equivalent:

\[
\boxed{
\mathcal P_{n,m}\ne\varnothing
\text{ for arbitrarily large }m
\iff
\text{some nontrivial ordinary survivor below }64^n
\text{ has an infinite continuation.}
}
\tag{16}
\]

For `n>=2`, if `epsilon_*` realizes `M_n^[1]` and has lifetime `\ell`, then

\[
\boxed{
M_{n+t}^{[1]}=M_n^{[1]}\qquad(0\le t\le\ell),
}
\tag{17}
\]

and, when `\ell<\infty`,

\[
\boxed{
M_{n+\ell+1}^{[1]}>M_n^{[1]}.
}
\tag{18}
\]

Thus the exact plateau length of the ordinary minimum is its centered
zero-renewal lifetime.

### Proof

Equation (4) shows that a depth-`n+m` representative is below `64^n` exactly
when its nonnegative block key is zero. Equation (7) then proves the set
identity in (13); deletion of the two constant words accounts for the
nontrivial superscript. A longer zero run contains every shorter one, proving
nestedness. If the set is nonempty, every survivor outside it is at least
`64^n`, so (14) follows.

There are only finitely many depth-`n` prefixes, and every zero child is
unique. Hence nonemptiness for arbitrarily large `m` selects one prefix with
arbitrarily long compatible zero extensions; finite compactness gives an
infinite zero extension. This proves (16). Applying (14) to the old minimum
through its exact lifetime proves (17). At the first nonzero renewal digit,
that value disappears. If `P_(n,\ell+1)` is nonempty, all of its members are
old depth-`n` representatives at least `M_n^[1]`, and equality is absent. If
it is empty, every new survivor is at least `64^n>M_n^[1]`. In either case the
new minimum is strictly larger, proving (18). **QED**

## Statement 3 -- exact reformulation of one-hot exposure

At a nontrivial exposing depth `n>=5` from `L-9883`, the one-hot candidate is

\[
A_*=64^{n-1}.
\tag{19}
\]

For every lower nonconstant depth-`n` prefix define

\[
H_n^-=\max_{2\le\alpha_n(\varepsilon)<A_*}\ell_n(\varepsilon),
\tag{20}
\]

with `H_n^-=\infty` if one lifetime is infinite and `H_n^-=-1` if the set
is empty. Then the candidate exposed by an `m`-digit suffix is the global
minimum exactly when

\[
\boxed{m>H_n^-.}
\tag{21}
\]

Equivalently, `L-9883/(13)` is the pure centered renewal barrier

\[
\boxed{
R_{n-1}(\varepsilon)\ge64^{n-2}
}
\tag{22}
\]

for every nonconstant length-`n` cylinder whose next `m` digits
`q_(n-1),...,q_(n+m-2)` all vanish. The exposing one-hot cylinder has equality
in (22).

### Proof

By (13), a lower competitor exists exactly when a lower depth-`n` prefix has
zero-renewal lifetime at least `m`. This is precisely the negation of (21).

Equation (5) writes every old coordinate as

\[
\alpha_n(\varepsilon)=e_0+64R_{n-1}(\varepsilon).
\tag{23}
\]

Because `e_0` is `0` or `1`, it cannot bridge the 64-unit gap between
successive values of `64R`. Therefore

\[
\alpha_n(\varepsilon)\ge64^{n-1}
\iff
R_{n-1}(\varepsilon)\ge64^{n-2}.
\tag{24}
\]

This proves (22); the one-hot equality follows from (19) and `e_0=0`.
**QED**

## What this advances

- The block-zero obstruction left by `L-9883` is now identical to a finite
  run of the centered renewal digit `q_k=0`; the two programs use the same
  arithmetic state.
- Global one-hot exposure is no longer an opaque comparison over all lifted
  words. It is the finite lifetime test (21) over lower old prefixes.
- Minimum plateaux acquire an exact centered-cylinder meaning through
  (17)--(18).
- Arbitrarily long nonempty sieves at one fixed old width are equivalent to
  an infinite ordinary survivor, rather than merely suggestive of one.

## Dependency audit

- `PR16/L-9313` supplies the centered least representatives and completion
  identity (8).
- `PR16/L-9314` supplies the appended digits and one-step zero-child
  uniqueness.
- `L-9877` supplies the exact arbitrary-width block compiler (4).
- `L-9883` supplies the one-hot exposure candidate and its original
  block-zero criterion.
- No real full-shift argument, empirical minimum table, or infinite-survival
  assumption is used.

## Gap audit

- No finite or asymptotic upper bound for `H_n^-` is proved.
- Statement (21) does not show that any exposing suffix is globally promoted.
- Once `P_(n,m)` is empty, positive lifted blocks determine the new minimum;
  this lemma does not order those blocks.
- Real centered full-shift support does not force the arithmetic event
  `q_k=0`.
- The equivalence (16) at fixed `n` is conditional in content: proving its
  right side impossible remains the ordinary-section problem.

## Adversarial checks

- The index shift is essential: a word of length `n` has centered residue
  `R_(n-1)`, so its first future digit is `q_(n-1)`.
- Equation (5) is exact because both representatives lie in the same canonical
  interval; a congruence alone would not justify (6).
- Base-64 digits in (6) are canonical and nonnegative, so no hidden carry can
  make a nonzero digit string sum to zero.
- A zero-renewal suffix is unique when it exists, but existence is not
  asserted.
- The two trivial representatives are removed before taking minima.

## Remaining uncertainty

Can the signed-difference valuation law of `L-9834` bound `H_n^-` for the
lower cylinders relevant to (21)? A successful bound along infinitely many
exposing depths would promote the restricted one-hot selector to the true
global survivor minimum.

## Suggested next attack

Assume a lower prefix shares `m` zero-renewal digits with the one-hot exposed
cylinder. Apply `L-9834` at their first differing chronological digit and
compare its exact `2`-adic separation with the centered inequality
`R_(n-1)<64^(n-2)`. Either force `m` below an explicit function of the first
difference or classify the exceptional lower-predecessor patterns.
