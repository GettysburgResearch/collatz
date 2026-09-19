# Lower-source merging across two actual exits

**PROPOSED pending independent mathematical review.** This is the first
research packet following [strategy issue #121](https://github.com/GettysburgResearch/collatz/issues/121).
It is not a Collatz solution or a mathematical-status promotion.

## The main result

For a given input of the form

$$
n=8^k u-5,\qquad k\ge1,\quad u\text{ positive odd},
$$

read its actual next parameters

$$
h=v_2(9^ku+1)-4,\qquad a=(9^ku+1)/2^{h+4}.
$$

If **h>=1** and **3^(h+1)a=1 mod4**, explicit physical paths give

$$
T^{3k+h+6}(n)=T^{3k+h+5}\!\left(\frac{n-5}{2}\right).
$$

These paths cross arbitrarily many expanding `110` blocks, their actual
exit, a second arbitrarily long odd run, and its guarded exit. Both parameters
are unbounded; the theorem is not a finite dictionary or a numerical census.

On the infinite specialization **n=3 mod12**, one further ordinary inverse
step composes uniformly:

$$
\boxed{T^{3k+h+6}(n)=T^{3k+h+6}\!\left(\frac n3-2\right).}
$$

For **k>=23**, every positive-time state on the displayed n arm is still
strictly above n. Since 3|n, n also has no smaller pure ancestor at any backward
depth. Thus neither forward descent within this whole arm nor direct inversion
at the source supplies the reduction; the two-sided physical certificate does.

## A concrete example

```text
k=23, h=1, u=343
n = 202471462953036038537211
x =  67490487651012012845735 < n/3
T^76(n) = T^76(x) = 213749140432556803774475 > n
```

The minimum of T^j(n), 1<=j<=76, is the displayed endpoint, still above n.
The proof supplies all-parameter scope; the checker independently replays
this example and the rest of the declared finite corpus.

## Read and run

Start with [the complete proof](PROOF.md), especially Sections 3–5. The
[experiment](../../experiments/X-AEM-001-exit-merging/README.md) has a standalone
generator, an independently implemented verifier, a fixed canonical artifact,
failed controls, and a terminating **partial** ordinary-value normalizer.
[Sources and limits](SOURCES_AND_LIMITS.md) distinguish the known first
odd-exit merger from this two-stage assembly and the current proposed status.
The [execution receipt](../../reports/astra-exit-merging-01/validation.json)
records actual native checks, not a full repository validation.

```bash
python -B experiments/X-AEM-001-exit-merging/run.py --example 23 1 0
python -B experiments/X-AEM-001-exit-merging/verify.py \
  experiments/X-AEM-001-exit-merging/results/canonical.json --self-test
```

## Exact progress boundary

This is a composable reduction rule, not a complete cover. The reduced source
in the divisible-by-three family satisfies x=7 mod32 for k>=2: it has an
explicit three-odd-step hard exit, whose universal handling is not proved.
The bridge and final congruence guards have real failures, retained in the
artifact. We did not prove every input eventually satisfies these guards or
find a well-founded cover of every remaining transition.

No new rank was introduced. The discovery uses arithmetic shadow structure;
the certificate uses one ordinary source order. No claim of external novelty,
full Lean verification, publication to remote, or Collatz completion is made.
See [publication handoff](../../reports/astra-exit-merging-01/PUBLISH.md).
