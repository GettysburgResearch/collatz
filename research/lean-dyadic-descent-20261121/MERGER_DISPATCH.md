# Original-source descent from the tripled first gap

**Status: VERIFIED.** `MergerDispatch.lean` passed Lean with `-j1 -DwarningAsError=true`; every printed axiom closure contains only the standard Lean axioms. The checked source SHA-256 is `cd34962cee9831194a95c19c13c948b14fbc3c7f4be232841cff924ff4a5720d`. The results are unconditional ordinary descent identities and a necessary condition for an orbit with no descent. Universal convergence remains **OPEN**.

The map is the shortcut ordinary Collatz map

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2.\end{cases}
\]

All clocks below count applications of this map. They do not count accelerated odd steps or certificate comparison handoffs.

## What is proved

For a positive ordinary source \(n>1\), factor

\[
9n+1=2^A u,\qquad u\text{ odd}.
\]

For odd \(n\), the number \(A\) is the first odd-step gap of the source \(3n\). The even-source case is included separately as \(A=0\). The argument does **not** assume that \(3n\) has a convergence certificate. It uses the factorization directly to prove a strictly smaller actual forward iterate of the original \(n\).

| Exact gap | Actual forward endpoint | Consequence |
|---|---|---|
| \(A=0\) | \(T(n)=n/2\) | Descent |
| \(A=1\) | \(T^2(n)=(3n+1)/4\) | Descent for \(n>1\) |
| \(A=2b+2\), \(b\ge1\) | \(2T^{2b+3}(n)=3^b u+1\) | Descent |
| \(A=2b+3\), \(b\ge3\) | \(T^{2b+2}(n)=2\cdot3^b u+1\) | Descent |

Consequently, if the original source satisfies

\[
\forall t\ge0,\qquad T^t(n)\ge n,
\]

then

\[
\boxed{v_2(9n+1)\in\{2,3,5,7\}.}
\]

`no_descent_valuation_residual` states this at the canonical valuation, without a supplied factorization. `no_descent_gap_residual` is the corresponding exact-factorization interface.

This restriction applies to the **original source**, for example to a least nonconvergent source under ordinary value induction or the minimum of a hypothetical nontrivial cycle. It does not restrict the gap at every future point of that orbit. A later value \(x>n\) can descend below \(x\) while remaining above \(n\). Thus the four values are not a finite-state alphabet for the whole trajectory, and repeated application to successive states would require a new original-source comparison.

## Component and least-counterexample applications

A positive source that is minimal among all positive sources sharing an actual forward value with it has no forward descent. `component_minimum_valuation_residual` therefore gives the same four-gap restriction. A least nonconvergent source would have this component-minimum property: a smaller source has a convergence certificate by minimality, and equality of actual forward values transports that certificate to the original source. This application is formalized as `least_counterexample_valuation_residual`.

The auxiliary common-orbit partner in `odd_gap_smaller_partner` is the smaller value \(w=2\cdot3^b u+1\), with \(T(w)=T^{2b+3}(n)\). In this family, \(w\) is itself the preceding actual iterate \(T^{2b+2}(n)\). No component-minimum hypothesis is needed to obtain the four-gap forward restriction.

## Proof of the descent families

For \(A\ge2\), the factorization forces \(n\equiv3\pmod4\), and direct substitution gives

\[
T^2(n)=2^{A-2}u+1.
\]

The affine lift already established in `OffsetDescent.lean`, applied to the terminal cycle \(1\mapsto2\mapsto1\), gives

\[
T^{2b}(2^{2b}u+1)=3^b u+1,
\]

and

\[
T^{2b+1}(2^{2b+1}u+1)=3^{b+1}u+2.
\]

When \(A=2b+2\), the first endpoint is even because \(u\) is odd. One final halving produces the displayed even-gap endpoint. For \(b\ge2\), induction gives the integer margin

\[
9\cdot3^b+20\le2\cdot2^{2b+2}.
\]

Multiplying by \(u\ge1\) and using \(9n+1=2^{2b+2}u\) proves the endpoint is smaller than \(n\). At \(b=1\), the source equation excludes \(u=1\), so oddness gives \(u\ge3\), and the strict comparison follows directly.

For \(A=2b+3\), apply the even-clock lift to the coefficient \(2u\) and stop one clock before the displayed odd-clock endpoint. This gives

\[
T^{2b+2}(n)=2\cdot3^b u+1.
\]

For \(b\ge3\), the corresponding margin is

\[
18\cdot3^b+20\le2^{2b+3}.
\]

Its first case is \(506\le512\). Multiplying by \(u\ge1\) pays for the endpoint's additive \(+1\) and proves descent below the original source. Both margins are elementary inductions: increasing \(b\) multiplies the dyadic side by four and the principal ternary term by three.

The earlier endpoint matters. For example, \(9\cdot967+1=2^9\cdot17\), and the formula gives \(T^8(967)=919<967\), whereas the next value is \(T^9(967)=1379>967\). Testing only the later odd-gap endpoint would miss this descent.

## Finite-prefix scope

The four-gap restriction has an elementary interpretation as a finite prefix test. If \(A\ge8\), write \(9n+1=256v\) with \(v>0\). The same affine lift gives

\[
T^8(n)=27v+1<n,
\]

because \(9(27v+1)<256v-1\) is equivalent to \(13v>10\). The other eliminated exact gaps are \(A=4\), which descends at clock five, and \(A=6\), which descends at clock seven, together with the elementary gaps zero and one. Thus the complement of the four-gap residual is already removed within eight ordinary clocks. This observation is a direct mathematical consequence of the identities in the module, rather than an additional separately declared Lean theorem.

The residual can equivalently be written as the disjoint congruence classes

\[
n\equiv3\pmod8,\qquad n\equiv15\pmod{16},\qquad
n\equiv39\pmod{64},\qquad n\equiv71\pmod{256}.
\]

These occupy \(32+16+4+1=53\) residue classes modulo \(256\). The union is only a necessary cover of possible no-descent sources; it is not the exact set failing every descent test through clock eight. For example, \(39\) belongs to the residual but \(T^8(39)=38\). This counts an initial-source restriction, not a probability law for states along an orbit. It explains both the coverage and the limited scope: the four-gap result is a verified finite prefix reduction, not a closed recursive program for the remaining sources.

## Relation to the current certificate and merger work

The comparison with external work was made at these immutable heads:

- PR177, `00a611094043afeb256d6532b477c0709e8ed270`, `research/lean-exact-witness-global-20261121/lean/Collatz/GapHandoffs.lean`: the reverse-tripling high-gap handoff keeps the whole certificate suffix. Its source certificate is additional input; the direct endpoint identities above require no certificate for \(3n\).
- PR184, `366dab89ee9548084ab9b5e4e90ff82abf287a20`, `research/lean-band-coupling-20261121/lean/RisingMerge.lean`: the rising merger supplies a smaller ordinary partner under its exact phase guard. Its smaller-source comparison must be made against the original induction source.
- PR182, `8372e302041a55057742a9e6ee9b4fa600c88fdb`, this packet's `OffsetDescent.lean`: the exact affine lift and terminal-cycle counts used in the new proof.

The new module imports the PR182 affine identities and mathlib's canonical natural-number factorization definitions. It needs no real analysis or band-hitting hypothesis. It does not assume PR177's open complete comparison selector or PR184's open universal merger coverage.

## The unresolved transfer is explicit

For every remaining odd original source, put \(p=(3n-1)/4\). Then \(0<p<n\) and \(T(n)=2p+1\). A least-counterexample argument supplies the complete convergence certificate of \(p\). If \(A\ge3\), the source \(p\) is odd and

\[
3p+1=2^{A-2}u.
\]

Thus the three odd residual gaps \(A=3,5,7\) give initial Hplus comparisons with certified source first gaps \(1,3,5\). PR177 consumes a first gap of one using the literal certificate suffix, but that suffix's ordinary value can exceed the original \(n\). The residual classification cannot then be reapplied to the new comparison target without a fresh comparison to \(n\). At \(A=2\), \(p\) is even, and normalizing its powers of two leads instead to the even-source Hplus/Psi transfer. Neither normalization supplies a total successful selector.

For the two remaining odd gaps \(A=5,7\), the source factor \(u=(9n+1)/2^A\) is strictly smaller than \(n\). Ordinary strong induction would therefore supply a certificate for \(u\). The wanted trajectory, however, reaches respectively

\[
9u+2,\qquad27u+2.
\]

A certificate for \(u\) does not immediately certify any of these values. Even the smallest comparison illustrates the missing mechanism. Write the first certified odd step of \(u\) as

\[
3u+1=2^a v,\qquad a\ge1,\quad v\text{ odd}.
\]

Then exact forward arithmetic gives

\[
T^a(9u+2)=3^{a+1}v-1.
\]

The known certificate has advanced to its suffix at \(v\), but the wanted coefficient has grown with its first gap \(a\). At a terminal suffix \(v=1\), this still asks for convergence of the resulting powers-of-three-minus-one family. No universal certificate transfer for that family is supplied here. Advancing a certificate suffix therefore does not, by itself, close the ordinary-value induction.

The two smallest residual gaps \(A=2,3\) also remain unbounded families. For example, every odd-exponent Mersenne source \(n=2^d-1\) with odd \(d\ge5\) has \(v_2(9n+1)=3\). It also misses the simple odd-predecessor guard \(n\equiv2\pmod3\) and the PR184 basic rising-merger phase guard \(3^{d-1}\equiv3\pmod4\). These are examples of survivors of these specific guards, not examples of nonconvergent orbits.

The first unsupported step remains a selector that produces a merger or descent below the original \(n\) for every residual source. Proving a local drop below a later, larger orbit point would not supply that selector.
