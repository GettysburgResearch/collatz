# Whole-suffix psi reduction and a smaller ordinary merger partner

**Status: PROVED in Lean core for the displayed unrestricted source languages;
OPEN for universal coverage and full Collatz.**

Normalization: `T(n)=n/2` for even `n`, `(3n+1)/2` for odd `n`, and
`B(n)` means that an ordinary finite orbit reaches one. A positive gap word
is a complete supplied odd convergence certificate. The source order is
exactly the graded multiset `Gamma` already proved well founded in
`Collatz/GapMultiset.lean`; no different rank is substituted in the composition.

Formal source: [`Collatz/PsiSuffix.lean`](lean/Collatz/PsiSuffix.lean).
It builds on the published PR177 source at
`00a611094043afeb256d6532b477c0709e8ed270`.

## 1. An unrestricted, suffix-consuming comparison

Write `2^[j]` for a word of `j` copies of the exponent two, and let

\[
 P_{j,k,a}=(2^{[j]},1,2^{[k]},a),\qquad j,k\ge0,\quad a\ge3.
\]

For **every** supplied complete certificate

\[
 \operatorname{Certificate}(n,P_{j,k,a}\Vert\tau),
\]

`whole_witness_handoff` constructs a positive integer `t` satisfying all of

\[
 \operatorname{Certificate}(3^kt,(a-2)\Vert\tau),
\]
\[
 \Gamma(0;(a-2)\Vert\tau)
  \prec\Gamma(0;P_{j,k,a}\Vert\tau),
\]
\[
 B(2n-1)\iff B(t),
\]
\[
 3^{j+1}n+2\,4^j
   =3^{j+1}+2\,4^{j+k+1}t.
 \tag{S1}
\]

There is no supplementary residue guard, length bound, chosen replacement
witness, or convergence oracle. The tail `tau` is exactly the supplied tail.
The divisibility by `3^k` follows from the source equations themselves.

The first-gap replacement lowers `a` by two, while consuming all the listed
ones and twos. The old prefix has `j+k+2` gaps and total `2j+2k+a+1`;
the replacement has one gap of value `a-2`. Thus the source clock drops by
`2j+2k+3`, independently of the untouched tail. The multiset proof does not
need this additional clock decrease.

### Derivation

A source gap two, `3x+1=4y`, preserves the psi basin comparison:

\[
 B(2x-1)=B(3x-1)=B(2y-1).
\]

An arbitrary leading run therefore reduces to a source `u`, with the exact
shifted identity

\[
 3^j(n-1)=4^j(u-1).
\]

The following source gap one gives `3u+1=2u_0`. The next `k` gaps two and
final gap `a>=3` imply

\[
 u_0=4^{k+1}t+1,
 \qquad \operatorname{Certificate}(3^k t,(a-2)\Vert\tau).
 \tag{S2}
\]

For the induction behind S2, the case `k=0` is the exact inverse of
`v -> 4v+1`, which reduces its first exponent by two. At the next gap two,
the source relation forces the auxiliary `t` to be divisible by three;
removing that factor increments the explicit `3^k`. No division over
rational states is substituted for an ordinary integer path.

Finally `3u-1=2*4^(k+1)*t`, so ordinary halvings give `B(2u-1) iff B(t)`.
The same equations give S1. The largest removed exponent dominates the one
inserted exponent, and the complete common tail cancels in `Gamma`.

### What this closes and what it calls

- At `k=0`, the child source is `t` itself. The theorem
  `closes_without_twos` therefore proves `B(2n-1)` outright for the entire
  unbounded language `(2^[j],1,a,tau)`, `a>=3`.
- At `k=1`, the result is a direct reverse-tripling query.
- For arbitrary `k`, the exact remaining query is
  `B(3^k*t) -> B(t)`, with the strictly smaller, explicitly supplied child
  certificate shown above.

The last statement is not discharged by calling a reverse-tripling theorem
`k` times and silently reusing its output certificates. Such an output need
not decrease the source multiset: the canonical certificates for `45` and
`15` are respectively `(3,2,3,4)` and `(1,1,1,5,4)`. The latter introduces
an exponent five absent from the former. Direct reverse-power coverage or
an additional justified composition argument is needed.

In the parallel interval-domain attack, the active relation is
`0<target` and `target<=2*source+1`. The child `(3^k*t,t)` belongs to that
domain automatically. Its existing interval induction hypothesis can
therefore discharge this entire suffix language directly, without a
separate universal reverse-power premise. Ordinary source consumption
already handles nonterminal odd sources in that broader interval domain;
the explicit suffix theorem additionally retains the compressed source,
full affine equation, and the smaller-partner composition below.

## 2. Compose the entire asymmetric reset into reverse nine

The previously proved `AsymmetricPsiReset` accepts an actual powered source
certificate

\[
 S=2^e q,\qquad e\ge3,\qquad\operatorname{Certificate}(q,\tau),
\]

and arbitrary `j,m` satisfying

\[
 3^{j+13}m+75116642\,4^j
   =16777216\,4^jS+3^{j+13}.
 \tag{S3}
\]

Its child source begins

\[
 (2^{[j]},1,2,2,3,1,3,2,1,2,3,2,3,e-1)\Vert\tau.
\]

The new theorem applies S1 with `k=2,a=3` to that actual supplied child.
`asymmetric_to_reverse_nine` consequently constructs a positive `t` such
that

\[
 \boxed{531441t+578545=131072S},\qquad 0<t<S,
 \tag{S4}
\]

and supplies the complete certificate

\[
 \operatorname{Certificate}
 (9t;(1,1,3,2,1,2,3,2,3,e-1)\Vert\tau).
 \tag{S5}
\]

Its grade is strictly below the **original** parent grade `Gamma(e;tau)`,
and

\[
 B(2S-1)\iff B(t).
 \tag{S6}
\]

The composition uses transitivity of the same proved multiset relation.
Neither the intervening reset's large source nor its long certificate is
used as an unranked induction hypothesis. The ordinary smaller partner
`t` is independent of the pump depth; S3's deeper nested guards select the
same compressed relation S4.

The previously checked depth-zero guard

\[
 S=20136632,\qquad m=211899691
\]

has

\[
 t=4966399,\qquad 9t=44697591.
\]

Here the reverse-nine **known source** is larger than `S`, while its
**wanted target** is smaller than `S`. The complete-witness rank and
ordinary component-size comparison have different roles, both retained
in the Lean theorem.

## 3. The smaller merger also holds without a convergence witness

The theorem `asymmetric_small_partner` takes only positive integers `S,t`
satisfying S4. It proves the exact positive-gap prefix

\[
 t\xrightarrow{(1^{[10]},2,2,3)}3S-1
\]

and the basin equivalence S6, together with `t<S` and `t<2S-1`.
The parent target `2S-1` reaches `3S-1` in one ordinary shortcut step.

The displayed child prefix has length13, total ordinary clock17, and
correction1604563. Multiplying S4 by three gives its full identity

\[
 3^{13}t+1604563=2^{17}(3S-1).
\]

The positive-prefix compiler supplies every intermediate oddness and
integrality condition. This is a genuine common ordinary endpoint and a
strictly smaller component representative; it is not an extrapolation of
a finite binary shadow.

S4 defines a single ternary progression for `S` modulo `3^12`, with `t`
positive. This standalone merger statement is broader than the reset's
`3^13` depth-zero entrance. It still does not assert a suitable merger for
every positive `S`.

## 4. The remaining global step

The new theorems connect the existing unbounded source reset to both the
reverse-power comparison language and ordinary smaller-component descent.
They close the complete `k=0` suffix language and expose the actual child
for every larger `k`.

For the concrete reset, the reverse-nine source starts `(1,1,3)`. Its
source endpoint after those three gaps is `u`, with
`243t+19=32u`; five consecutive target odd steps then reach `u+6`.
This gives the next exact reverse-nine-to-add-six interface, investigated
in the parallel merger attack. It does not make the add-six comparison
true without a complete rule for its supplied source.

The universal obligation remains coverage of every activated comparison
under the shared source order, or a valid source-bounded ordinary merger
for every input. The current Lean statements do not assume either.
