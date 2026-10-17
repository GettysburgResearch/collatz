# LIT-KTHM-0040 — A finite state-dependent affine potential gives a universal stabilization obstruction

**Type:** self-contained finite-control Lyapunov theorem.  
**Maps to:** PR #33 after its common absolute-trap theorem, and normalized PR #3 stage relations.

## Setup

Let `I` be a finite control set. Every allowed edge `e:i->j` carries an affine update

```text
z' = alpha_e z + beta_e                              (1)
```

on ordinary integers. Suppose there are rational constants

```text
a_i>0,
b_i,
delta>0,
R>=0
```

such that for every allowed edge and every ordinary `z` in its domain with `|z|>R`,

```text
V_j(z') <= V_i(z)-delta,
V_i(z)=a_i|z|+b_i.                                   (2)
```

## Theorem

Every infinite ordinary path enters the finite set

```text
{(i,z): i in I, |z|<=R}                              (3)
```

in finitely many steps. If no state in that finite set can lie on an infinite admissible path, then no infinite ordinary path exists.

More generally, if the finite set contains only ultimately periodic bounded paths, then every infinite ordinary path is ultimately periodic.

## Proof

Assume a path remains outside `(3)` for `N` consecutive steps. Iterating `(2)` gives

```text
V_(i_N)(z_N) <= V_(i_0)(z_0)-N*delta.                (4)
```

Because `I` is finite and `a_i>0`, the potentials are bounded below on all ordinary states. Equation `(4)` cannot hold for arbitrarily large `N`. Thus the path enters `(3)`.

The final assertions follow by exhaustive analysis of the finite induced transition system on `(3)`. ∎

## Why this is stronger than a common absolute trap

Some individual slopes `|alpha_e|` may exceed one. State-dependent weights can nevertheless decrease on every allowed edge, or after refining the control graph, when admissible cycles have negative total gain.

## Proof-producing search interface

1. freeze the finite edge graph and exact affine maps;
2. solve the finite rational inequalities `(2)`;
3. verify them symbolically or with exact Farkas certificates;
4. compute the finite trap `(3)` exactly;
5. replay every trap transition.

If no potential exists, a cycle or occupation-measure dual can identify the exact relaxed obstruction and guide congruence refinement.