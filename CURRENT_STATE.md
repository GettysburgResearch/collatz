# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch now contains ten mathematical research sessions. No claim has
received the repository's independent review, so complete-looking finite
theorems remain `PROPOSED`.

There is currently **no positive-integer Collatz counterexample**, no regular
sanctuary, and no closed counter-stack grammar in the repository.

## Fixed map

The shortcut map is

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a chronological parity word \(w\) of length \(L\) and weight \(a\),

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one canonical residue class modulo \(2^L\).

## Existing finite resources

Earlier sessions provide:

- complete finite collision-fiber recursions;
- induced partial radix maps;
- sparse and consecutive supercritical collision charts;
- mixed-radix carry rewrites and finite-horizon pumps;
- inverse-signature collision codes;
- exponentially unbounded mildly supercritical branch count;
- arbitrary finite \(3\)-adic precision;
- geometry-preserving tensor amplification;
- complete collision-alphabet projection modulo \(2^b\) for every \(b\);
- negative-template rational-base return systems;
- finite and graph-directed return criteria;
- normalized real-window and aspect-ratio constraints;
- synchronous coupling to moving negative phases;
- cycle-padded mismatch towers;
- fair, growth-tilted, and phase-escape Kraft identities.

These are exact finite resources. None selects one ordinary positive state that
survives forever.

## Finite intervals and marked particles

### L-0014 — finite interval renormalization

Every ordinary state \(n>0\) can be represented by a finite interval

\[
[v,q),
\qquad q-v=n.
\]

The exact interval rules are

\[
[v,q)
\longmapsto
\left[
\left\lceil\frac v2\right\rceil,
\left\lceil\frac q2\right\rceil
\right)
\]

for even length and

\[
[v,q)
\longmapsto
\left[
\left\lfloor\frac{3v}{2}\right\rfloor,
\left\lceil\frac{3q}{2}\right\rceil
\right)
\]

for odd length. The new interval length is \(T(n)\).

### T-0018 — ordered particle completion

With

\[
R_0(x)=\lfloor x/2\rfloor,
\qquad
R_1(x)=\lceil3x/2\rceil,
\]

the identity \(R_0(x)+R_1(x)=2x\) has a finite two-child ordered-particle
rewrite. Uniform descendants realize the phase-escape measure.

One distinguished child has rank exactly \(T(j)\), so a finite marked root
generates the ordinary shortcut-Collatz trajectory as a marked spine.

### T-0019 — marked versus unmarked likelihood

For an ordinary trajectory \(n_t\) with parity prefix \(w_L\),

\[
\mathbb Q_{n_0+1}([w_L])
=
\frac{n_L}{2^Ln_0}.
\]

The branch population gains the factor \(n_L\), but the one fully marked
descendant of the specified root has mass only

\[
\frac1{2^Ln_0}.
\]

Positive unmarked escape pressure therefore does not establish an accepted
ordinary spine.

# Literature review incorporated

The branch

```text
agent/gpt56-pro-03/4-literature-audit
```

and draft PR #13 were inspected before the present continuation.

## What is standard infrastructure

The imported suite identifies as standard and reusable:

- subsequential/rational images of regular languages;
- exact closure of one fixed DFA by finite reachability;
- greatest safe kernels of finite relations;
- short canonical witness bounds;
- rational-base address identities;
- positive cycle-mean phase potentials;
- clopen-cover obstructions;
- finite-state tilted transfer bounds;
- compact graph-directed attractors.

The live review's central advice for PR #3 is:

> Treat graph expansion as solved infrastructure. Concentrate on an exact
> arithmetic selector, an invariant survivor set, one ordinary quotient, and
> exact block replay.

A compact attractor or compatible completion path remains insufficient because
it may contain no ordinary integer.

## Neighboring exact tool

PR #12 supplies a large exact regular-sanctuary laboratory:

- canonical LSD-first finite-word semantics;
- the exact shortcut subsequential transducer;
- product-graph closure and concrete witnesses;
- maximal safe accepting-state kernels;
- short canonical witnesses;
- certificate checking independent of synthesis.

The present session proves precisely when the marked-particle route belongs to
that existing program.

# New session: regular-collapse boundary

## L-0015 — regular interval and marker projection

Encode finite endpoints synchronously in LSD-first binary. For a regular
endpoint-pair language \(G\), define

\[
\operatorname{Len}(G)
=
\{\operatorname{bin}_{\rm LSD}(q-v):
\operatorname{conv}(v,q)\in G\}.
\]

Then

\[
\boxed{\operatorname{Len}(G)\text{ is effectively regular}.}
\]

The proof uses the two-state binary addition relation

\[
v_i+n_i+c_i=q_i+2c_{i+1},
\]

regular projection, right quotient by \(0^*\), and canonical intersection.

Fixed and diagonal interval gauges preserve regularity. Regular
population/marker configuration languages have regular marked-rank
projections.

## T-0020 — finite-phase regular block collapse

Let finitely many regular phase languages \(L_i\) be covered by regular edge
domains \(D_e\), with fixed block lengths \(b_e\), and suppose

\[
T^{b_e}(D_e)\subseteq L_{\tau(e)}.
\]

If the phase languages are nonempty and avoid \(1,2\), then

\[
\boxed{
K=
\bigcup_e\bigcup_{0\le k<b_e}T^k(D_e)
}
\]

is a nonempty one-step regular sanctuary.

Conversely every regular sanctuary is a one-phase instance.

Therefore:

\[
\boxed{
\text{finite phases + regular domains + fixed finite blocks}
\iff
\text{regular sanctuary}
}
\]

at the level of existence.

### Marked-grammar consequence

A finite-phase regular marked interval, marked particle, carry-phase, or
negative-target grammar with rational marker extraction and fixed exact block
replay compiles effectively to the regular-sanctuary class of PR #12.

Finite endpoint decoration and finite phase labels may simplify a certificate,
but they do not enlarge its existential power.

## X-0011 — exact compilation bridge

The standard-library-only experiment implements:

- endpoint-pair DFAs;
- exact difference projection with one carry bit;
- high-zero removal by right quotient;
- canonical determinization;
- the exact shortcut transducer;
- concrete closure witnesses;
- maximal safe-state kernels.

It verifies random finite endpoint languages, multiple gauges, the infinite
fixed-gauge all-positive control, exact closure, semantic emptiness of the safe
kernel, and fixed-block normalization.

# Strategic correction

The previous broad target included finite-state, substitutional, and pushdown
marked-particle grammars. `T-0020` separates them.

A **regular finite-state** marked grammar is already the PR #12 problem. A
finite graph of fixed macro-blocks is also already the PR #12 problem.

The route becomes genuinely new only with at least one unbounded or nonregular
ingredient:

1. a pushdown stack;
2. an unbounded cycle-padding or valuation counter;
3. variable block lengths not reducible to finite phases;
4. a nonregular arithmetic survivor;
5. a non-rational marker/configuration coupling.

This prevents duplicate search under interval, particle, phase, carry, and
regular-language notation.

# Central unresolved step

The strongest current target is a **counter-stack marked sanctuary**.

Use a state of the form

\[
(i,t,\rho,n),
\]

where:

- \(i\) is finite negative-phase control;
- \(t\ge0\) is an unbounded cycle-padding counter;
- \(\rho\) is a finite low-order residue obligation;
- \(n\) is one explicitly marked ordinary positive integer.

A certified transition should have the form

\[
(i,t,\rho,n)
\longmapsto
(j,t+\Delta_e,\rho',T^{b_e(t)}(n))
\]

and prove:

1. exact cylinder selection;
2. stack/counter nonnegativity;
3. closure of the residue obligation;
4. positive graph-cycle growth above an explicit threshold;
5. one finite initial marked configuration;
6. no substitution of a \(2\)-adic inverse-limit path for the marker.

This class is not compiled away by `T-0020` because the block length and residue
obligation depend on unbounded memory.

# Immediate priorities

1. **Padding-counter transition law.** Derive the exact next valuation and odd
   quotient after a cycle-padded mismatch, retaining a free high quotient.
2. **Residue automaton over a unary counter.** Prove periodic dependence of the
   low-order obligation on the padding height and encode it in finite control.
3. **Counter update synthesis.** Seek edges with
   \(t'\ge t-\!C\), preferably \(t'=t+\Delta\), and positive full-cycle growth.
4. **Marked interoperability.** Keep the ordinary particle marker explicit and
   replay every macro-edge through the distinguished child of `T-0018`.
5. **Regular controls.** Compile every finite-state approximation through
   `L-0015` and submit it to PR #12 rather than maintaining a duplicate verifier.
6. **Independent audit.** Reconstruct `L-0015`, `T-0020`, and `X-0011`,
   especially high-zero canonicalization and terminal-cycle exclusion.
