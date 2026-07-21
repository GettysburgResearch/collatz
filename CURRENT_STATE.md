# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2 — Bootstrap exact collision-rewrite research program`  
Active draft PR: `#3`

## Project maturity

The active branch now contains three mathematical research sessions. No claim
has yet received independent review, so complete-looking finite theorems and
identities are recorded as `PROPOSED`.

There is currently **no positive-integer Collatz counterexample** in the
repository.

## Fixed framework

The active work uses the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Parity words are chronological. Mixed-radix digit strings are low-order first.
`NOTATION.md` fixes the conventions.

For a length-\(L\) parity word \(w\) with \(a\) odd steps,

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on its unique residue class modulo \(2^L\).

## Collision fibers and induced maps

Suppose a finite, possibly sparse set \(D\) satisfies

\[
T^L(2^Lq+r+d)=3^aq+s
\qquad(d\in D).
\]

When \(3^a>2^L\), `T-0002` induces the partial expanding radix map

\[
\boxed{
H_D(2^LB+d)=3^aB+d,
\qquad d\in D.
}
\]

One explicit invariant congruence class of induced states lifts exactly to
ordinary positive Collatz integers. An infinite admissible finite-integer orbit
of \(H_D\) would be a counterexample.

`T-0001` is the special case in which \(D\) is an initial interval.

## Exact finite collision atlas

`L-0003` gives an exact even/odd recursion for every residue's pair

\[
(a_L(r),s_L(r))
=
(\#\text{ odd steps},T^L(r)).
\]

Collision fibers are precisely the level sets of this pair. The complete table
through depth \(L\) can be generated in total \(O(2^L)\) arithmetic work.

`X-0002` exhaustively constructs the complete supercritical atlas through depth
22. The largest cardinalities found there are

```text
2, 3, 4, 5, 8, 12, 18.
```

The largest explicit census chart from that session is `O-0004`:

\[
T^{22}(4194304q+621248+d)=4782969q+708587
\]

for

\[
D=\{0,16,20,21,32,34,35,40,42,49,68,69,70,78,79,92,93,94\}.
\]

## New conceptual advance: inverse-signature collision codes

### L-0005 — Exact inverse reconstruction

For a finite word \(w\) of length \(L\), weight \(a\), and constant \(B(w)\),
define

\[
\boxed{
\sigma(w)\equiv2^{-L}B(w)\pmod{3^a}.
}
\]

If a common output \(y\) satisfies

\[
y\equiv\sigma(w)\pmod{3^a},
\]

then

\[
n_w(y)=\frac{2^Ly-B(w)}{3^a}
\]

is integral; whenever it is nonnegative, it follows \(w\) and reaches \(y\).
Thus equal signatures are exactly the finite congruence needed to build a
collision fiber backwards.

If

\[
y\equiv-1\pmod{2^k},
\]

then \(y\) has \(k\) forced consecutive odd steps. This permits a common tail
to add drift after the branching core has already merged.

### L-0006 — 3-adic code composition

A parity collision code is a fixed-length, fixed-weight set whose constants
agree modulo \(3^p\). The surplus

\[
e=p-a
\]

measures extra 3-adic precision.

For codes \(\mathcal C_1,\mathcal C_2\),

\[
B(uv)=3^{a_2}B(u)+2^{L_1}B(v),
\]

so concatenation has guaranteed precision

\[
p_{12}\ge\min(p_1+a_2,p_2)
\]

and surplus

\[
e_{12}\ge\min(e_1,e_2-a_1).
\]

A high-surplus suffix can therefore absorb independent prefix choices. This is
a finite algebra for designing structured collision alphabets rather than only
enumerating them.

## T-0005 — Large supercritical alphabets are guaranteed

Let \(L,a,k\) satisfy

\[
2^k-1>3^a,
\qquad
3^{a+k}>2^{L+k}.
\]

`T-0005` proves that a supercritical collision fiber exists with cardinality at
least

\[
\left\lceil\frac{\binom La}{3^a}\right\rceil.
\]

The proof is finite:

1. pigeonhole the weight-\(a\) words by inverse signature;
2. use CRT to choose one common output with a forced all-odd tail;
3. invert every word from that output;
4. verify positivity and the bound below the total input radix.

For \(L=3m\), \(a=m\), and the shortest supercritical tail \(k_m\), this gives

\[
|D_m|
\ge
\left\lceil\frac{\binom{3m}{m}}{3^m}\right\rceil
\sim
\frac{\sqrt3}{2\sqrt{\pi m}}
\left(\frac94\right)^m,
\]

while

\[
1<\frac{3^{m+k_m}}{2^{3m+k_m}}\le\frac32.
\]

Therefore supercritical collision-fiber cardinalities are provably unbounded
and exponentially large. `Q-0002` is resolved on the active branch, subject to
independent review.

### Strategic consequence

**Branching and drift are separate design resources.** A low-odd-density inverse
code can provide many branches; a common CRT odd tail can later make the chart
supercritical. Record alphabet size is no longer the principal scarcity.

## O-0005 — A 339-branch mildly supercritical chart

`X-0003` finds 339 length-24, weight-eight words with common signature 2906.
Appending the shortest supercritical odd tail gives

\[
\boxed{
T^{44}(17592186044416q+8952950628352+d)
=22876792454961q+11642373114938
}
\]

for a reproducible 339-element offset set \(D\) satisfying

\[
0\le d\le17207.
\]

The induced chart has expansion ratio approximately

\[
1.3003950957
\]

and lifting class

\[
A\equiv2689422486586
\pmod{5284606410545}.
\]

The offset alphabet has additional exact geometry:

- every residue class modulo 16 occurs;
- \([-934,934]\subseteq D-D\);
- the underlying collision fiber contains seven consecutive residues.

These properties make the chart more relevant to carry and `S`-unit closure
than cardinality alone.

## Universal local amplification

`L-0004` proves that every nontrivial collision chart has exact finite-horizon
carry pumps. For a closed carry path

\[
R_cX\longrightarrow ER_c,
\]

horizontal repetition gives

\[
R_cX^m\longrightarrow E^mR_c.
\]

Thus local stack amplification is universal. It still does not settle finite
vertical closure.

## Global structure of a hypothetical induced orbit

### T-0003 — Dual adic/real coding

For least digits \(d_t\), radices \(M<N\), and \(c=N-M\),

\[
A_0=\frac{c}{N}\sum_{t\ge0}d_t\left(\frac MN\right)^t
\]

holds in \(\mathbb Q_2\). In the real topology,

\[
A_t=C\left(\frac NM\right)^t+x_t,
\]

where \(x_t\) is bounded in the convex hull of the digit alphabet. Hence the
base-\(M\) word length grows with slope

\[
\log_M(N/M).
\]

A nontrivial ordinary-integer orbit cannot have an eventually periodic digit
itinerary.

### T-0004 — Run-length skeleton

Every maximal constant-digit phase has the exact form

\[
d+M^uC\longmapsto d+N^uC.
\]

An infinite orbit is equivalent to an infinite chain

\[
\boxed{
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1},
}
\]

with \(d_k\) in the active alphabet, \(u_k\ge1\), positive cofactors, and the
required divisibility conditions.

This remains the cleanest scale-independent global target.

## Computational state

### X-0001

Consecutive collision bundles through depth 17.

### X-0002

Complete supercritical collision fibers through depth 22 and exact checks of
the fiber recursion, arbitrary-fiber conjugacy, carry pumping, dual coding, and
run-length skeleton.

### X-0003

Equal-signature classes for \(1\le m\le8\), shortest supercritical odd tails,
and direct verification of every selected trajectory. Largest classes:

```text
2, 4, 7, 17, 34, 74, 157, 339.
```

The theorem guarantees, at the same parameters:

```text
1, 2, 4, 7, 13, 26, 54, 113.
```

The program also verifies the collision-code tensor law and all geometry stated
for `O-0005`.

## Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

A solution must construct either:

1. a finite aperiodic macro-tile grammar whose emitted rows close vertically
   while the high-order boundary remains an ordinary finite word; or
2. a finite family of positive cofactor schemas closed under the run-length
   `S`-unit equations and the lifting congruence.

Compatible finite prefixes, a periodic adic tiling, or an alphabet of unbounded
cardinality remain insufficient.

## Immediate research priorities

1. **Structured collision codes.** Use `L-0006` to force complete small-modulus
   projections, long difference intervals, or tensorable precision surplus in
   an unbounded family.
2. **Exploit O-0005 arithmetically.** Convert its modulo-16 coverage and bounded
   difference interval into uniform cofactor relays for `T-0004`.
3. **Variable-tail and multi-chart grammar.** Build several charts from one
   branching core with different common tails, then use chart changes to manage
   boundary growth and lifting classes.
4. **Vertical macro-tiles.** Search for finite relays, not isolated horizontal
   carry cycles.
5. **Finite-versus-adic criterion.** Extend `T-0003` to aperiodic morphic,
   substitutional, code-composed, or `S`-adic itineraries.
6. **Independent audit.** Reconstruct `L-0005`, `L-0006`, `T-0005`, and
   `O-0005`, especially the inverse-converse, positivity bounds, CRT root, and
   mild-expansion claim.
