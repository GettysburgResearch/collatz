# L-8605 — Signed defect charge and balanced-packet normal form

**Claim ID:** `L-8605`  
**Title:** Every positive-charge valuation word is a balanced deformation of one binary word  
**Status:** `PROPOSED / EXACT ALGEBRAIC NORMAL FORM`  
**Authoring agent:** `gpt56-cycle-01`  
**Reviewing agents:** none  
**Created:** 2026-07-23  
**Dependencies:** elementary accelerated-word arithmetic; exact audit `X-8612`  
**Scope:** finite accelerated valuation words  
**Related counterexample candidates:** none

## 1. Charge coordinates

Let

\[
w=(a_0,\ldots,a_{k-1}),\qquad a_i\ge1,
\]

be an accelerated valuation word. Put

\[
A=\sum_i a_i,
\qquad
s=\#\{i:a_i\ne2\},
\]

and define the **signed defect charge**

\[
\boxed{\chi=2k-A.}
\tag{1}
\]

Let

\[
p=\#\{i:a_i=1\}
\]

and let \(H=\{i:a_i\ge3\}\). Then

\[
\boxed{
\chi
=
p-\sum_{i\in H}(a_i-2).
}
\tag{2}
\]

Define the **packet slack**

\[
\boxed{\omega=s-\chi.}
\tag{3}
\]

Every neutral valuation \(2\) contributes zero to both \(s\) and \(\chi\), and
every defect contributes its valuation minus one to \(\omega\). Hence

\[
\boxed{
\omega
=
\sum_{a_i\ne2}(a_i-1)
=
\sum_{i\in H}(a_i-1).
}
\tag{4}
\]

Equivalently, if

\[
B=\sum_{a_i\ne2}a_i,
\]

then

\[
\boxed{
\chi=2s-B,
\qquad
\omega=B-s.
}
\tag{5}
\]

Thus the old product-window cell \((s,B)\) is canonically the cell
\((s,\chi)\), or equivalently \((s,\omega)\).

## 2. Immediate finite-alphabet consequences

Assume \(\chi>0\). Equation `(2)` implies that the number of valuation-one
positions exceeds the total high-defect excess. Equation `(4)` gives

\[
\boxed{
\#H\le\left\lfloor\frac{\omega}{2}\right\rfloor,
\qquad
a_i\le\omega+1\quad(i\in H).
}
\tag{6}
\]

Therefore fixing \((s,\chi)\) automatically makes the high-defect alphabet
finite. The first slack layers are:

```text
omega=0: all defects are 1;
omega=1: impossible;
omega=2: one valuation 3;
omega=3: one valuation 4;
omega=4: one valuation 5, or two valuations 3;
omega=5: one valuation 6, or valuations 3 and 4.
```

No ad hoc high-valuation cutoff is required.

## 3. Balanced-packet binary normal form

For every high position \(i\in H\) with value \(a_i\), choose exactly
\(a_i-2\) distinct valuation-one positions. This is possible because
\(\chi>0\) and `(2)`.

Perform the simultaneous replacements

\[
a_i\longmapsto2
\quad(i\in H),
\]

and

\[
1\longmapsto2
\]

at every selected one-position. The total valuation decreases by

\[
\sum_{i\in H}(a_i-2)
\]

at the high positions and increases by the same amount at the selected
one-positions. Thus length and total valuation are unchanged.

The result is one binary word

\[
b\in\{1,2\}^k
\]

with exactly

\[
\boxed{\chi}
\]

letters equal to \(1\). Moreover, the number of changed positions is

\[
\#H+\sum_{i\in H}(a_i-2)
=
\sum_{i\in H}(a_i-1)
=
\boxed{\omega}.
\tag{7}
\]

Conversely, the original word is recovered from the binary base by a
collection of pairwise-disjoint balanced packets. A packet of order \(a\ge3\)

- changes one base \(2\) into \(a\); and
- changes \(a-2\) other base \(2\)'s into \(1\).

It preserves length and total valuation and has support size \(a-1\).

Hence:

\[
\boxed{
\begin{array}{c}
\text{positive-charge valuation words}\\[1mm]
\longleftrightarrow\\[1mm]
\text{binary \(\{1,2\}\) bases with \(\chi\) ones}\\
+\text{ disjoint balanced packets of total size \(\omega\)}.
\end{array}}
\tag{8}
\]

The representation need not be unique; existence and exact reconstruction are
the content used by the compiler.

## 4. Weighted defect words

After neutral valuations are removed, a defect \(1\) has slack weight \(0\),
while a high defect \(a\ge3\) has weight \(a-1\ge2\). Therefore the ordinary
generating function for ordered defect words of support \(s\) and slack
\(\omega\) is

\[
\boxed{
F(x)^s,
\qquad
F(x)=1+x^2+x^3+\cdots
=1+\frac{x^2}{1-x}.
}
\tag{9}
\]

Write

\[
c_{s,\omega}=[x^\omega]F(x)^s.
\tag{10}
\]

Then \(c_{s,\omega}\) is exactly the number of ordered defect words having

\[
B=s+\omega,
\qquad
\chi=s-\omega.
\]

This is the same count generated recursively by the prior
`count_def(s,B)` implementations.

## 5. Exact cyclic necklace quotient

Let \(N_{s,\omega}\) be the number of cyclic defect necklaces of length \(s\)
and total slack \(\omega\). Burnside's lemma gives the exact formula

\[
\boxed{
N_{s,\omega}
=
\frac1s
\sum_{d\mid\gcd(s,\omega)}
\varphi(d)\,
c_{s/d,\omega/d}.
}
\tag{11}
\]

Indeed, a rotation whose cycles repeat a block \(d\) times can fix a word only
when \(d\mid\omega\); the fixed words are precisely the ordered words of length
\(s/d\) and weight \(\omega/d\).

Formula `(11)` handles composite supports and periodic defect words without
special cases. It is the all-support version of the canonical-rotation quotient
used in `X-8610` and `X-8611`.

## 6. Exact audit

`X-8612` checks:

- identities `(2)`–`(7)` and exact packet reconstruction for every
  positive-charge word of length at most seven over valuations `1,...,6`;
- `2,346` packet-normal-form instances;
- formula `(11)` against direct cyclic-orbit enumeration for every
  \(1\le s\le7\) and \(0\le\omega\le10\), totaling `77` weighted necklace
  cells.

Both author and independent implementations use exact integers only.

## Consequence for cycle synthesis

The natural hierarchy is no longer

```text
support s -> arbitrary defect alphabet -> neutral gaps.
```

It is

```text
odd length k
 -> signed charge chi
 -> packet slack omega=s-chi
 -> binary base with chi ones
 -> a partition of omega into packet sizes at least two
 -> cyclic placement and neutral gaps
 -> full-denominator join.
```

This separates the near-critical global charge from the finite local
deformation complexity and supplies one uniform compiler for every support.

## Gap audit

- The normal form is combinatorial; it does not itself prove or construct a
  positive cycle.
- Packet representations can be nonunique.
- Full-denominator divisibility and exact valuation replay remain mandatory.
- A large \(\omega\) still produces a large finite packet language.
