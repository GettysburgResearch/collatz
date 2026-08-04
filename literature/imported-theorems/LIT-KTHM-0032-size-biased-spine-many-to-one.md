# LIT-KTHM-0032 — Mass-conserving trees, size-biased spines, and many-to-one

**Type:** standard spine identity with complete finite proof.  
**Sources:** Lyons--Pemantle--Peres; Hardy--Harris.  
**Maps to:** `PR3/T-0018` and `PR3/T-0019`.

## Statement

Let a finite rooted tree carry positive masses `m(v)` satisfying

```text
m(v)=sum_(u child of v) m(u)
```

at every nonterminal vertex. Define a random spine by choosing, from `v`, a child `u` with probability

```text
P(v->u)=m(u)/m(v).
```

Then for every depth-`L` vertex `u`,

```text
P(spine_L=u)=m(u)/m(root).                       (1)
```

Consequently, for every function `g` on generation `L`,

```text
E[g(spine_L)]
 = (1/m(root)) sum_(|u|=L) m(u) g(u).           (2)
```

This is the elementary many-to-one identity.

## Proof

For the unique path

```text
root=v_0,v_1,...,v_L=u,
```

the transition probabilities telescope:

```text
P(spine_L=u)
 = product_(j<L) m(v_(j+1))/m(v_j)
 = m(u)/m(root).
```

Summing `g(u)` against `(1)` gives `(2)`. ∎

## Doob-transform form

Suppose an underlying reference process chooses each binary child with probability `1/2`, and let `h` be a positive harmonic function satisfying

```text
h(v)=(h(v0)+h(v1))/2.
```

Assign mass

```text
m(v)=2^(-|v|) h(v).
```

Then mass is conserved and the spine transition is

```text
P_h(v->vi)=(1/2)h(vi)/h(v),
```

the exact Doob `h`-transform.

## Native application

PR #3 constructs interval masses with

```text
m(v)=length(v),
m(v0)+m(v1)=2m(v),
```

and then normalizes by `2^(-|v|)`. Its distinguished child transition is exactly the shortcut Collatz map on the marked rank. Therefore the repository's endpoint formula

```text
Q([w]) = 2^(-|w|) * endpoint_mass / root_mass
```

is a deterministic size-biased-spine law, and the ordinary marked trajectory is its exact spine.

The standard literature suggests the next reusable tools:

- additive/derivative martingales;
- entropy production under the size-biased change of measure;
- `L log L` nondegeneracy tests;
- many-to-one estimates for path observables;
- spine large deviations.

## Non-consequences

The identity does not show that a rare or infinite spine corresponds to a new ordinary integer. In PR #3 the ordinary marked spine already exists because it is the deterministic orbit of the initial rank. The missing theorem is instead closure of a useful connector/counter grammar along that spine.