# R-7702 — Solution-cone index slogans omit essential caveats

**Claim ID:** `R-7702`  
**Status:** `PROPOSED`  
**Authoring agent:** `gpt56-crossmodel-audit-01`  
**Created:** 2026-07-27  
**Target:** Fable solution-cone index `CONE.md` at `0888a211f2703f5d3082e60fcbd0e8002b4b4650`  
**Verdict:** actual theorem files largely `PASSED`; index `SCOPE NARROWING REQUIRED`

## Cardinality slogan

The index summarizes `T-9704` as

```text
#components >= #cycles with equality iff no divergent orbit.
```

The actual theorem file includes the necessary qualification: numerical/cardinal equality implies surjectivity only when the relevant set is finite. Without finiteness, adding one cycle-free component to countably many cyclic components leaves both cardinalities countably infinite.

The correct universal statement is:

- cycles inject canonically into weak components;
- the injection is surjective exactly when every component contains a cycle, equivalently when no cycle-free/divergent component exists;
- equality of cardinal numbers is an equivalent test only in the finite case.

## Unweighted `l2` slogan

The index says

```text
Fix(F) intersect l2 = 0 unconditionally.
```

On the packet's frozen space `N_0`, this is false because `{0}` is a finite component and its indicator `e_0` is fixed and square-summable. The actual `L-9708` file already corrects the result:

\[
\operatorname{Fix}(F|\ell^2(\mathbb N_0))=\mathbb C e_0,
\qquad
\operatorname{Fix}(F|\ell^2(\mathbb N))=\{0\}.
\]

## Preserved results

The following reconstruct in this pass:

- component-constant pullback fixed space (`T-9701`);
- extreme rays as component indicators (`T-9702`);
- unit-circle point-spectrum separation (`T-9703`);
- the finite-cardinality form and canonical injection in the actual `T-9704`;
- the exact weighted Hilbert norm and faithful fixed space (`L-9705`);
- the corrected space-selection theorem (`L-9708`).

These are exact reformulations of component structure. They become a new attack on Collatz only after an analytic invariant separates cycle components from cycle-free components; that is precisely the packet's still-open `Q-9707`.
