# A global antichain bound for the ordinary Abel envelope

**Status: written deduction from the source-qualified construction below;
not Lean-formalized and not a full Collatz closure.** One simultaneous
Abel extraction gives a global bound for disjoint predecessor sets. The
bound is stronger than applying the source's one-target estimate
separately, but it does not control a comparable escaping ray.

## 1. Fixed input and normalization

Use PR180 at commit
`d0349de2108abb7c8fb8393c086610e3372df116`, specifically
[`GLOBAL_RENEWAL_ATTACK.md`, §8](https://github.com/GettysburgResearch/collatz/blob/d0349de2108abb7c8fb8393c086610e3372df116/research/lean-forward-band-20261121/GLOBAL_RENEWAL_ATTACK.md).
The inspected source content has SHA256
`a3582838d1d8b907efd40ce005226e1d4decab6fcc2ae805e4b20840e950fe8d`.
This addendum assumes that source's ordinary inverse-word interpretation,
clock-tail estimate, and simultaneous Abel construction. It does not
independently certify the analytic atom floor imported there, and it does
not silently substitute a published predecessor theorem for that input.

Let `q` be a positive odd integer prime to three. An admissible inverse
word `w` of accelerated depth `s` has total shortcut clock `A(w)`, source `n_w`,
weight `omega_w=3^s 2^(-A(w))`, and affine correction `beta_w`, with

\[
q=\omega_w n_w+\beta_w,\qquad
0\le\beta_w<q,\qquad
U^s(n_w)=q.
\tag{A1}
\]

All positive-depth sources are positive odd integers; they need not
themselves be prime to three. The empty word has source `q` and weight
one. Write `D_s(q)` for the sum of these weights, and let

\[
F_\rho(q)=(1-\rho)\sum_{s\ge0}\rho^sD_s(q),
\qquad 0<\rho<1.
\tag{A2}
\]

The source supplies one sequence `rho_j` tending to one on which every
positive ordinary argument converges simultaneously:

\[
F(q)=\lim_jF_{\rho_j}(q)<\infty.
\tag{A3}
\]

This same `F` has a positive absolute floor on ternary units and satisfies
`PF<=F` for the first-power positive inverse operator. Neither a separate
subsequence for each target set nor a different envelope chosen for each
argument is used here.

Put `R=64/3`. The two cutoff estimates retained from the source are

\[
A(w)\le6s\ \Longrightarrow\ n_w\le qR^s,
\qquad
\sum_{\substack{|w|=s\\A(w)>6s}}\omega_w
\le(64/81)^s\quad(s\ge1).
\tag{A4}
\]

The second bound holds even before restriction to a target residue.
Its total over positive depths is `64/17`.

## 2. Simultaneous antichain theorem

Let `A` be any finite set of positive odd ternary-unit targets such that:

- each target is **not itself periodic** under the ordinary shortcut
  map `T`; eventual entry into a cycle is allowed;
- distinct targets are forward incomparable: neither target has an
  ordinary forward iterate equal to the other.

Then the single envelope in `(A3)` satisfies

\[
\boxed{\sum_{q\in A}\frac{F(q)}q\le\log(64/3).}
\tag{A5}
\]

The logarithm is natural. The empty set is immediate. For a nonempty
set let `Q=max A`, and define

\[
B_S=\sum_{s=0}^S\sum_{q\in A}\frac{D_s(q)}q.
\]

For each retained word, `(A1)` gives `omega_w/q<=1/n_w`, while
`(A4)` places its source at most `QR^S`. These sources are distinct
across the entire sum:

1. At a fixed target and depth, a positive odd source determines all
   its actual accelerated exponents and therefore its word.
2. Two different depths hitting the same target would make that target
   periodic, which is excluded.
3. A source hitting two different targets would make those targets
   forward comparable, which is also excluded.

Consequently the normalized retained sum is at most
`H_floor(QR^S)`, the ordinary harmonic sum. The discarded clocks from
all targets contribute at most `(64/17) sum_(q in A) 1/q`. Thus

\[
B_S\le C_A+S\log R,
\qquad
C_A=1+\log Q+\frac{64}{17}\sum_{q\in A}\frac1q.
\tag{A6}
\]

All terms are nonnegative, so Abel summation is exact:

\[
\begin{aligned}
\sum_{q\in A}\frac{F_\rho(q)}q
 &=(1-\rho)^2\sum_{S\ge0}\rho^SB_S\\
 &\le(1-\rho)C_A+\rho\log R.
\end{aligned}
\tag{A7}
\]

There are only finitely many targets. Taking their limits along the
same sequence in `(A3)` proves `(A5)`. No exchange of an infinite
target sum with a limit is needed. By applying `(A5)` to finite subsets,
the corresponding series bound also holds for a countable antichain of
nonperiodic targets.

### Periodic targets require their cycle factor

The hypothesis excluding periodic targets cannot simply be removed from
`(A5)`. For a periodic odd target let `E_q` be its least positive shortcut
period, let `p_q` be the odd count in that cycle, and set

\[
\eta_q=1-3^{p_q}2^{-E_q}>0.
\]

For a nonperiodic target set `eta_q=1`. The source's geometric summation
of repeated hits gives total weight at most `q/(eta_q n)` for one
source hitting `q`. Repeating the preceding proof with normalization
`eta_q/q` therefore yields, for any finite forward-incomparable set of
positive odd unit targets,

\[
\boxed{\sum_{q\in A}\eta_q\frac{F(q)}q\le\log(64/3).}
\tag{A8}
\]

This weighted extension does not identify the possible cycles.

## 3. The comparable-ray boundary

The theorem controls disjoint predecessor sets. Successive states of
one forward orbit are comparable, so they cannot all be inserted into
`(A5)`. The source's inverse inequality makes the distinction explicit.
Put `h(q)=F(q)/q`. If `q_(i+1)=U(q_i)` with actual exponent `a_i`,
the one inverse parent `q_i` gives

\[
h(q_{i+1})\ge
\frac{3q_i}{3q_i+1}h(q_i).
\tag{A9}
\]

If that orbit is injective and
`sum_i 1/q_i<infinity`, the product of the displayed factors has a
positive limit. Since the unit floor makes `h(q_0)>0`, `(A9)` then
forces a positive lower bound for `h(q_i)` along the whole ray. The
reciprocal summability is itself a conditional consequence of the
source's separately qualified population premise `(PDU)` and its
disjoint off-orbit parents. It is not assumed to follow from `(A5)`
alone.

Thus uniform decay `F(q)/q -> 0` on large ordinary odd units would exclude
such an escaping ray. The antichain estimate does not prove that decay:
it permits normalized mass on a comparable ray while its disjoint side
branches have summable charges.

The same distinction persists for the first-moment criterion in
[`ORDINARY_RENEWAL.md`](ORDINARY_RENEWAL.md). For the actual orbit minimum
`m(n)=min_j U^j(n)` and integer `X>=1`, the exact layer-cake identity is

\[
\sum_{\substack{n\le X\\n\text{ odd},\ 3\nmid n}}\frac{m(n)}n
=\sum_{R=1}^{X}
\sum_{\substack{n\le X\\n\text{ odd},\ 3\nmid n\\m(n)\ge R}}\frac1n.
\tag{A10}
\]

Tightness of these survivor tails does not supply summability over `R`.
The new bound controls a single antichain's normalized inverse mass;
it provides no additional summable bound on the right side of `(A10)`.
No finite first moment, uniform sublinearity, or exclusion of all escapes
is claimed in this addendum.
