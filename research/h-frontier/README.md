# The H exact-cylinder and infinite-survivor frontier

**Agent:** `gpt56-h-01`  
**Issue:** [#17](https://github.com/gfreund123/collatz/issues/17)  
**Packet status:** isolated research packet for review; not a canonical ledger  
**Last updated:** 2026-07-21

## Executive summary

This packet consolidates and audits a multi-thread investigation of the partial
map

\[
H(n)=
\begin{cases}
3n/4,&n\equiv0\pmod4,\\[1mm]
(9n+1)/8,&n\equiv7\pmod8,\\[1mm]
\text{undefined},&\text{otherwise}.
\end{cases}
\]

No proof of termination and no positive infinite orbit is claimed here. The
main advances are a precise exact-cylinder model, a finite carry recursion, a
2-adic ghost/stabilization theorem, an exponentially sparse survivor sieve, and
a proof that every nonperiodic infinite exact orbit would automatically escape
in real multiplier capital. The remaining obstruction is sharply isolated as a
one-sided nonperiodic path, or equivalently a positive ordinary-integer value of
a real-escaping 2-adic ghost.

A proposed signed-displacement theorem would prove that every contracting exact
cylinder descends. The theorem has passed an exact exhaustive audit on 55,986
words, but the supplied general induction contains a real proof gap in its
mixed-sign carry/half-plane step. It is therefore recorded as a conjecture with
a precise missing lemma, not silently promoted to a theorem.

## Repository integration boundary

At issue start, `main` contained the operating README but not the canonical
ledgers named there. Draft PR #3 proposes one bootstrap, issue #4 tracks a
larger migration, and PR #6 contains an adjacent termination-method frontier.
This packet therefore:

- lives under `research/h-frontier/`;
- reserves provisional identifiers in the `*-9500` range;
- does not edit `CURRENT_STATE.md`, `CLAIMS.md`, `OPEN_PROBLEMS.md`, or
  `NEGATIVE_RESULTS.md`;
- cross-references PR #6 rather than duplicating its mixed-radix termination
  inventory; and
- asks an integrator to index or alias these stable IDs later without silently
  renumbering them.

## Why this subsystem matters to the counterexample mission

Let the shortcut Collatz map be

\[
C(N)=\begin{cases}N/2,&N\text{ even},\\(3N+1)/2,&N\text{ odd}.
\end{cases}
\]

If `n -> H(n)` is legal and `N=8n+1`, then:

- for `n = 0 mod 4`, two shortcut steps send
  \(N\) to \(8(3n/4)+1\);
- for `n = 7 mod 8`, three shortcut steps send
  \(N\) to \(8((9n+1)/8)+1\).

Hence a positive infinite H-orbit would lift to a genuine nonconvergent shortcut
Collatz orbit. A disproof of H would therefore disprove Collatz. A proof of H
would not prove full Collatz, but its exact-cylinder and ghost mechanisms are
natural candidates for reuse in broader residue-avoidance and marked-boundary
problems.

## 1. Exact block system

Write `A(n)=3n/4` and `B(n)=(9n+1)/8`. Every infinite H-orbit has infinitely
many `A`-states: an eventual infinite B-run would require `8^j | n+1` for every
`j`.

At an A-state `n=4x`, set

\[
p=3n+4=12x+4.
\]

A block consists of one A-step followed by exactly `r` B-steps, returning to an
A-state. Put

\[
e_r=3r+2,\qquad s_r=2r+1,\qquad
 a_r=\frac{3^{s_r}}{2^{e_r}}.
\]

The block is exact legal precisely when

\[
p=2^{e_r}u,\qquad u\equiv1\pmod4,\qquad p\equiv1\pmod3,
\]

and then

\[
\boxed{p^+=a_rp+1=3^{s_r}u+1.}
\]

The formal state `p=4` is fixed by `r=0`; it corresponds to `x=0` and is not a
positive H A-state. Positive H A-states have `p>=16`.

## 2. Finite words and exact cylinders

For `w=(r_0,...,r_{L-1})`, define

\[
E_k=\sum_{i<k}e_{r_i},\qquad
S_k=\sum_{i<k}s_{r_i},\qquad
M_k=\frac{3^{S_k}}{2^{E_k}}.
\]

The endpoint is

\[
F_w(p)=M_Lp+M_L\sum_{k=1}^L\frac1{M_k}
      =\frac{3^{S_L}p+C_w}{2^{E_L}},
\]

where

\[
C_w=\sum_{k=1}^L2^{E_k}3^{S_L-S_k}.
\]

Define the direct ghost residue

\[
g_w\equiv-\sum_{k=1}^L2^{E_k}3^{-S_k}
\pmod{2^{E_L+2}}.
\]

Then the exact positive cylinder is one arithmetic progression

\[
\boxed{
C(w)=\Pi(w)+3\,2^{E_L+2}\mathbb Z_{\ge0},
}
\]

where `Pi(w)` is the least positive integer satisfying

\[
\Pi(w)\equiv g_w\pmod{2^{E_L+2}},\qquad
\Pi(w)\equiv1\pmod3.
\]

Every finite word is realizable. This has two important consequences:

1. no finite forbidden-word argument on the itinerary alone can solve the
   infinite problem;
2. arbitrarily long expanding shadows are expected and are not counterexamples.

### Correction: direct and recursive cylinders agree

An earlier thread claimed that the final ghost congruence enforced only endpoint
integrality and could miss intermediate exactness. That claim is false. Reducing
the final congruence modulo each `2^(E_{i+1}+2)` forces every intermediate
endpoint to be divisible by 4, which is equivalent to the preceding block's
exact core being `1 mod 4`.

The direct residue agrees with the suffix recursion

\[
\alpha((r)v)\equiv
2^{e_r}3^{-s_r}(\alpha(v)-1)
\pmod{2^{e_r+E_v+2}}.
\]

Experiment `X-9501` verifies this equality on 55,986 words.

## 3. Carries, ghosts, and bounded representatives

Let `F_w(Pi(w))=4Y_w`. If

\[
p=\Pi(w)+3\,2^{E_w+2}t,
\]

then

\[
\frac{F_w(p)}4=Y_w+3^{S_w+1}t.
\]

Appending `r` selects a unique carry

\[
c(w,r)\in\{0,\ldots,2^{3r+2}-1\}
\]

with

\[
c(w,r)\equiv
(2^{3r}-Y_w)(3^{S_w+1})^{-1}
\pmod{2^{3r+2}},
\]

and

\[
\boxed{
\Pi(wr)=\Pi(w)+3\,2^{E_w+2}c(w,r).
}
\]

Therefore least representatives are nondecreasing along every branch.

For an infinite itinerary `r`, define its 2-adic ghost

\[
\mathcal G(\mathbf r)=
-\sum_{L\ge1}2^{E_L}3^{-S_L}\in\mathbb Z_2.
\]

A positive ordinary integer realizes the itinerary forever if and only if the
finite representatives eventually stabilize; equivalently, all sufficiently
late carries are zero. Thus the infinite integer problem is exactly an eventual
zero-carry problem, not a finite-word problem.

## 4. Multiplier capital and the toll identity

Set

\[
\kappa=\frac{\log(4/3)}{\log(9/8)},\qquad
R_L=\sum_{i<L}r_i,\qquad
K_L=R_L-\kappa L.
\]

Then

\[
M_L=\prod_{i<L}a_{r_i}=\left(\frac98\right)^{K_L}.
\]

The affine recurrence gives

\[
\boxed{
\frac{p_L}{M_L}=p_0+\sum_{k=1}^L\frac1{M_k}.
}
\]

Since `a_{r_i}=(p_{i+1}-1)/p_i`, it also gives the exact Euler product

\[
\boxed{
p_0+\sum_{k=1}^L\frac1{M_k}
=p_0\prod_{j=1}^L\left(1-\frac1{p_j}\right)^{-1}.
}
\]

## 5. Infinite survivors are harmonically sparse

Let `I_h` be the set of positive exact states with an exact future of length
`h`. Fixed-length cylinders are disjoint and have total density

\[
\boxed{
d(I_h)=\frac1{12}\left(\frac27\right)^h.
}
\]

Let `I=intersection_h I_h` be the infinite-survivor set. A growing-depth
cylinder count yields

\[
\#\{n\le X:n\in I\}
\le C X\exp(-c\sqrt{\log X}),
\]

and therefore

\[
\boxed{\sum_{n\in I}\frac1n<\infty.}
\]

This is stronger than zero density. It is also exactly strong enough to combine
with the toll-Euler identity.

If an infinite exact orbit is nonperiodic, its states are distinct members of
`I`; hence their reciprocal sum converges. The Euler product stays bounded, so

\[
\sum_{k\ge1}\frac1{M_k}<\infty,
\qquad M_k\to\infty,
\qquad K_k\to\infty.
\]

Thus:

\[
\boxed{
\text{Every nonperiodic infinite exact orbit is automatically real-escaping.}
}
\]

## 6. The sharp LX equivalences

The following statements are equivalent:

1. there exists an infinite exact orbit whose every finite prefix has `K_L>0`;
2. there exists a nonperiodic infinite exact orbit;
3. there exists an infinite exact orbit with `K_L -> +infinity`;
4. the finite extremal quantity
   \[
   \mu_L=\min\{\Pi(w):|w|=L,\ K_j(w)>0\text{ for }1\le j\le L\}
   \]
   fails to tend to infinity;
5. for some finite bound `B`, the bounded-representative tree below has an
   infinite branch.

The implication from (2) to (3) is the survivor-harmonic theorem. To pass from
(3) to (1), shift to the unique global minimum of `K_L`; uniqueness follows
from irrationality of `kappa`.

## 7. Bounded-representative rewrite target

For `B>=4`, let `R_B` be the tree of finite prefix-expanding words `w` with
`Pi(w)<=B`. The carry formula makes `R_B` finitely branching. At a state with
`P=Pi(w)`, exponent `E`, endpoint `Y`, and ternary exponent `S`, every successor
is generated by one of finitely many carries

\[
0\le c\le\left\lfloor\frac{B-P}{3\,2^{E+2}}\right\rfloor.
\]

Put

\[
N_c=Y+3^{S+1}c.
\]

A successor exists exactly when

\[
v_2(N_c)\equiv0\pmod3,
\qquad N_c/2^{v_2(N_c)}\equiv1\pmod4,
\]

with `r=v_2(N_c)/3`, the least-carry condition `c<2^(3r+2)`, and the next prefix
remaining expanding.

Consequently

\[
\boxed{
\mu_L\to\infty
\iff
\text{every finitely branching tree }R_B\text{ terminates.}
}
\]

This is the cleanest computer-assisted proof target in the packet. A CEGAR
workflow can abstract residues and bank height, search for positive-mean cycles,
then refine every spurious cycle with additional exact arithmetic.

## 8. Contracting-cylinder descent: strong evidence, incomplete proof

Normalize

\[
U_w=2^{E_w},\quad V_w=3^{S_w},\quad D_w=U_w-V_w,
\]

\[
B_w=\frac14C_w,\quad A_w=\alpha(w)/4,\quad
Y_w=F_w(\alpha(w))/4,\quad \Delta_w=A_w-Y_w.
\]

The proposed signed-displacement theorem is

\[
D_w>0\Longrightarrow0\le\Delta_w<D_w,
\]

\[
D_w<0\Longrightarrow D_w<\Delta_w<0,
\]

with equality only for all-zero words in the contracting case. It would imply
that every contracting exact cylinder descends, except for the formal `p=4`
fixed point.

The one-letter case is exact, and concatenation gives the correct carry identity

\[
\Delta_{uv}=\Delta_u+\Delta_v+hD_u+jD_v,
\]

\[
D_{uv}=U_vD_u+V_uD_v.
\]

However, the submitted proof then asserts—without a complete mixed-sign
argument—that the carry relation places these two linear forms in the same
half-plane. That assertion is not a formal consequence of the displayed bounds
alone; analogous abstract tuples can fail it. A word-specific carry-rectangle
lemma is still required.

`X-9501` found no counterexample for every word of length at most 6 over
`r in {0,...,5}`: 55,986 words, including 25,751 contracting words. This is
strong evidence, not a universal proof.

## 9. Current exact proof frontier

A complete proof of H would follow from both:

1. **signed displacement / contracting-cylinder descent**, closing the finite
   descent half; and
2. **weighted bounded-representative termination**, excluding a nonperiodic
   one-sided infinite exact path.

The second is the deeper infinite obstruction. It can be phrased equivalently as

\[
\boxed{
\text{A real-escaping 2-adic ghost is never a positive ordinary integer.}
}
\]

or

\[
\boxed{
\text{The deterministic normalized rewrite has no positive-reward infinite ray.}
}
\]

With `p=4Y`, define the exact domain

\[
\mathcal D=\{Y>0:Y\equiv1\pmod3,\ v_2(Y)\equiv0\pmod3,
\ Y/2^{v_2(Y)}\equiv1\pmod4\}.
\]

For `r(Y)=v_2(Y)/3` and `u(Y)=Y/2^{3r(Y)}`, define

\[
\Psi(Y)=\frac{3^{2r(Y)+1}u(Y)+1}{4}.
\]

The remaining theorem is the weighted termination assertion that no infinite
derivation `Y -> Psi(Y)` has

\[
\sum_{i<L}(r(Y_i)-\kappa)\to+\infty.
\]

The fixed point `Y=1` shows why ordinary termination is the wrong target.

## 10. Additional structural restrictions

Several useful secondary facts survive audit:

- adjacent odd cores are coprime;
- finite odd-prime support would force eventual periodicity by the standard
  S-unit finiteness theorem;
- an old prime reappearing after a block segment must divide that segment's
  affine offset;
- two-sided exact windows have density
  \[
  \frac1{12}\left(\frac27\right)^h\left(\frac38\right)^k;
  \]
- every finite itinerary is realizable, so any proof object must carry arithmetic
  state, not only a finite word grammar.

These facts constrain counterexamples but do not close the one-sided boundary.

## Suggested review order

1. [`CLAIM_INVENTORY.md`](CLAIM_INVENTORY.md)
2. [`../../experiments/X-9501-h-exact-audit/README.md`](../../experiments/X-9501-h-exact-audit/README.md)
3. [`../../reports/gpt56-h-01/2026-07-21-17-h-frontier-synthesis.md`](../../reports/gpt56-h-01/2026-07-21-17-h-frontier-synthesis.md)

## Immediate next attacks

1. Prove or refute the word-specific carry-rectangle lemma underlying signed
   displacement.
2. Implement bounded trees `R_B`, including exact certificates of exhausted
   branches and replayable counterexample traces for every surviving abstraction
   cycle.
3. Search for a finite weighted interpretation of the normalized map `Psi` that
   permits the fixed point `Y=1` but forbids positive-mean nonperiodic rays.
4. Use the survivor harmonic measure to design a transfer operator on exact
   states, rather than relying on itinerary-only finite automata.
