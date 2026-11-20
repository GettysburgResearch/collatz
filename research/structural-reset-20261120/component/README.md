# Ordinary component rigidity from a restricted merger domain

The new result is a complete **conditional** arithmetic closure:

> Collatz is equivalent to \(t\sim5t+1\) only for parameters \(t\) prime to
> three whose 2-adic valuation is a positive even integer.

That parameter set has natural density \(1/9\). The hypothesis on it is still
open. The contribution is a proof that this restricted hypothesis already
forces all ordinary component labels to coincide, closing the earlier
FR-008 domain-extension gap.

[PROOF.md](PROOF.md) is self-contained. Its central algebraic theorem says that
a function invariant under multiplication by 2, 3 and 5, together with three
specified affine laws on their exact ordinary domains, must be constant.
The proof supplies a total integer descent, not another finite-depth cover.
The required affine law with multiplier 9 comes from two actual odd steps
starting at \(5n\); retaining that relation is what makes the new closure
possible.

Run the exact arithmetic check with:

```sh
python -X utf8 -B research/structural-reset-20261120/component/check_component_rigidity.py
```

The checker verifies certificates symbolically on every residue cell modulo
480 and proves their inequalities for every positive lift. It does not test
or assume Collatz convergence on a finite range. No external mathematical
theorem is a proof dependency.

**Status:** complete proposed proof; the parent agent independently checked
the conditional identities and every descent case. The first unsupported
step is proving the stated restricted ordinary merger hypothesis itself.
