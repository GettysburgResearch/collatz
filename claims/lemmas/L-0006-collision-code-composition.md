# L-0006 — 3-adic collision-code composition calculus

Claim ID: `L-0006`  
Title: Precision surplus and concatenation of parity collision codes  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `L-0005`  
Scope: finite sets of parity words and their affine constants  
Related counterexample candidates: none

## Statement

A finite set \(\mathcal C\subset\{0,1\}^L\) is a
**\((L,a,p)\) collision code** when:

1. every word in \(\mathcal C\) has exactly \(a\) ones;
2. there is a residue \(\beta\pmod{3^p}\) such that
   \[
   B(w)\equiv\beta\pmod{3^p}
   \qquad(w\in\mathcal C).
   \tag{1}
   \]

Usually \(p\ge a\). The quantity

\[
e=p-a
\tag{2}
\]

is the **precision surplus**. At \(p=a\), (1) is precisely the equal-signature
condition of `L-0005`.

Let \(\mathcal C_1\) be an \((L_1,a_1,p_1)\) code and
\(\mathcal C_2\) an \((L_2,a_2,p_2)\) code. Define

\[
\mathcal C_1\mathcal C_2
=
\{uv:u\in\mathcal C_1,\ v\in\mathcal C_2\}.
\tag{3}
\]

Then:

### 1. Concatenation law

For individual words,

\[
\boxed{
B(uv)=3^{a(v)}B(u)+2^{|u|}B(v).
}
\tag{4}
\]

Consequently, \(\mathcal C_1\mathcal C_2\) has length \(L_1+L_2\), weight
\(a_1+a_2\), cardinality

\[
|\mathcal C_1\mathcal C_2|
=|\mathcal C_1||\mathcal C_2|,
\tag{5}
\]

and guaranteed precision

\[
\boxed{p_{12}\ge\min(p_1+a_2,p_2).}
\tag{6}
\]

### 2. Surplus budget

Writing \(e_i=p_i-a_i\), the guaranteed surplus after concatenation is

\[
\boxed{e_{12}\ge\min(e_1,e_2-a_1).}
\tag{7}
\]

In particular, if

\[
e_1\ge0,
\qquad e_2\ge a_1,
\tag{8}
\]

then the product is an ordinary collision code at precision at least
\(a_1+a_2\), and its cardinality is the product of the two cardinalities.

A common fixed suffix of weight \(b\) raises precision by \(b\) and preserves
surplus. A fixed prefix of weight \(b\) consumes \(b\) units of available
surplus.

### 3. Pigeonhole tradeoff

For every \(L,a,p\), some \((L,a,p)\) code has cardinality at least

\[
\boxed{
\left\lceil\frac{\binom La}{3^p}\right\rceil.
}
\tag{9}
\]

Thus code cardinality and 3-adic precision can be traded quantitatively.

### 4. Geometric meaning of surplus

If \(p=a+e\) and two words in the code are inverted from one common output as
in `L-0005`, then their starting integers differ by a multiple of \(3^e\).
Thus precision surplus becomes an exact congruence constraint on the induced
collision alphabet.

## Motivation

Collision fibers are not merely sets of residues. Their parity words form
finite 3-adic codes. Precision surplus is a resource: a sufficiently precise
suffix code can absorb independent choices made in an earlier prefix code.
This gives a composition calculus for building structured alphabets rather than
finding them only through a flat census.

The long-range objective is to construct codes whose induced digit sets have
closure-friendly geometry: complete small-modulus projections, controlled
difference sets, or macro-tile relay structure.

## Proof

For (4), every odd symbol in \(u\) has all \(a(v)\) odd symbols of \(v\) after
it, so its contribution to \(B(uv)\) is multiplied by \(3^{a(v)}\). Every
position in \(v\) is shifted by \(|u|\), multiplying its contribution by
\(2^{|u|}\). This proves (4).

For two concatenations \(uv\) and \(u'v'\),

\[
\begin{aligned}
B(uv)-B(u'v')
&=3^{a_2}\bigl(B(u)-B(u')\bigr)\\
&\quad+2^{L_1}\bigl(B(v)-B(v')\bigr).
\end{aligned}
\tag{10}
\]

The first term is divisible by \(3^{p_1+a_2}\), and the second by \(3^{p_2}\)
because \(2^{L_1}\) is a 3-adic unit. Therefore their sum is divisible by
\(3^{\min(p_1+a_2,p_2)}\), proving (6). Unique fixed-length concatenation gives
(5). Subtracting the total weight \(a_1+a_2\) from the precision bound gives
(7), and (8) is immediate.

For (9), partition the \(\binom La\) weight-\(a\) words by the residue
\(B(w)\pmod{3^p}\). There are at most \(3^p\) classes.

Finally, if two words have constants differing by a multiple of \(3^{a+e}\),
then the inverse formula of `L-0005` gives

\[
n_u(y)-n_v(y)
=-\frac{B(u)-B(v)}{3^a},
\]

which is divisible by \(3^e\). ∎

## Concrete tensor example

The prefix code

\[
\mathcal P=\{100,001\}
\]

has length three, weight one, and constant residue \(1\pmod3\). The suffix code

\[
\mathcal S=\{100100,010001\}
\]

has length six, weight two, and constants

\[
11,
\qquad38,
\]

which are congruent modulo \(27=3^3\). Its surplus is one, exactly enough to
absorb the prefix weight. Therefore the four concatenations form a
length-nine, weight-three collision code modulo \(27\). Their constants are

\[
97,
313,
124,
340,
\]

all congruent to \(16\pmod{27}\).

## Dependency audit

- Only the finite constant formula and elementary divisibility are used.
- No statement about infinite word concatenation is made.
- Cardinalities multiply because block boundaries and lengths are fixed.

## Gap audit

- Precision surplus controls divisibility of digit differences, not vertical
  closure of the induced radix map.
- Infinite concatenation would define an infinite parity sequence and still
  require an independent finite-integer existence argument.
- The pigeonhole code need not possess useful internal geometry beyond its
  cardinality and congruence.

## Adversarial tests

`X-0003` checks (4) and the four-word tensor example exactly.

## Remaining uncertainty

The finite calculus appears complete and awaits independent reconstruction.

## Suggested next attack

Search for finite high-surplus component codes whose tensor products force a
prescribed small-modulus projection or a long interval inside the induced
difference set.
