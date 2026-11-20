# A 13/6 inverse-cone compiler

**Status: PROPOSED, independently checked computer-assisted universal conversion theorem.**

This packet proves a quantified statement about inverse symbolic conversion. It
does not prove forward Collatz descent, boundedness, or termination. It extends
the inverse-credit construction in PR #141, pinned at
`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`.

## 1. The theorem and its exact domain

Use the shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

**Theorem.** For every integer \(t\ge1\) and every integer
\(0<c<3^t\) with \(3\nmid c\), there are integers \(k,r\), and one
length-\(k\) parity word containing exactly \(t\) odd events, such that

\[
0<r<2^k,
\qquad T^k(2^k x+r)=3^t x+c
\quad\text{for every integer }x\ge1,
\]

and

\[
 k\le \left\lfloor\frac{13t+V(c\bmod3^{12})-1}{6}\right\rfloor
 \le \boxed{\left\lfloor\frac{13t+65}{6}\right\rfloor}.
\]

The function \(V\), supplied by the certificate, has domain the residues not
divisible by three modulo \(3^{12}=531441\), and values in \(\{0,\ldots,66\}\).
Its domain includes both parities. The same parity word works for every
positive prefix \(x\); the compiler never chooses a branch based on \(x\).
Every trajectory in the displayed identity stays above one.

Choosing between this construction and the already proved constructions in
#141 gives

\[
k\le\min\left\{4t-2,\ 3t,\
\left\lfloor\frac{7t+17}{3}\right\rfloor,\
\left\lfloor\frac{13t+65}{6}\right\rfloor\right\}.
\]

Thus the asymptotic worst-case cost of **#141's explicit bounded-alphabet
online credit construction** improves from \(7/3\) to \(13/6\) shortcut
steps per prescribed ternary factor. The larger additive constant means
the previous bounds remain useful for shorter tails.

This is not a claim to the best existential cone budget. The fixed-total
spreading argument in [rStation paper 48, version 2, Lemma 7 and Theorem
8](https://rstation.ai/problems/collatz/papers/48) gives, at sufficiently
large depth, words with total \(2t\); its onset is not numerically supplied
and its permitted alphabet grows with depth. The contribution here is an
explicit all-depth online policy with actions at most ten, a fixed finite
lookahead, and a small independently replayable integer certificate. None
of the analytic claims in that external manuscript is used to verify it.

## 2. The finite certificate

Write \(M=3^{12}\), and define

\[
\phi_a(c)=\frac{2^a c-1}{3}.
\]

For every positive integer \(c\) with \(3\nmid c\), the supplied table admits
an action \(a\in\{1,\ldots,10\}\) such that \(d=\phi_a(c)\) is a positive
integer not divisible by three and

\[
6a+V(d\bmod M)\le13+V(c\bmod M).\tag{1}
\]

The action can be chosen using only \(c\bmod M\). Crucially, it works for
**every** positive ordinary integer in that residue class, not just the
smallest representative.

### Why the finite verification has the required universal quantifier

Let \(c=r+Mq\), with \(1\le r<M\), \(3\nmid r\), and \(q\ge0\). Then

\[
\phi_a(c)=\frac{2^a r-1}{3}+2^a3^{11}q.
\]

Once the first summand is integral, its residue modulo \(M\) depends only on
\(q\bmod3\). Integrality is independent of \(q\), and the property of being
a unit modulo three is also independent of the unexamined higher digits.
Therefore, for each residue \(r\), checking a **single chosen action** on
the three ordinary inputs \(r,r+M,r+2M\) checks (1) for every positive
integer with that residue. Positivity at the least representative implies
positivity at all other representatives.

The standalone verifier directly checks the three inputs by integer
multiplication and division. It checks 354,294 residue rows and 1,062,882
selected-action lifts. Its action counts are:

| Action | Number of residue rows |
|---:|---:|
| 1 | 93,315 |
| 2 | 93,315 |
| 3 | 58,915 |
| 4 | 58,915 |
| 5 | 23,954 |
| 6 | 23,954 |
| 7 | 829 |
| 8 | 829 |
| 9 | 134 |
| 10 | 134 |

The values are encoded in increasing unit-residue order
\(1,2,4,5,\ldots,M-2,M-1\). Their SHA-256, taking one byte for each credit,
is

```
2f12342f3a4a25ff8ed31c03ddba77b66a17d8bfea62dfaac0c0ea1cbb3273dc
```

The gzip container is only a storage format; the verifier reads the JSON
with Python's standard library. Neither numerical optimization nor the
synthesis program is part of the verification trust base.

## 3. The well-founded conversion rank

A symbolic state has the form

\[
Y=2^b3^s x+c,
\qquad s\ge1,\quad c>0,\quad3\nmid c.
\]

For \(s\ge2\), choose an action certified by (1). Inverting one block gives

\[
\phi_a(Y)=2^{b+a}3^{s-1}x+\phi_a(c).
\]

It is integral for every integer \(x\). Its new constant is a positive
unit, so the process can continue. Define

\[
R(s,c)=13s+V(c\bmod M)-1\quad(s\ge1),
\qquad R(0,c)=0.
\]

Equation (1) gives

\[
R(s,c)-R(s-1,\phi_a(c))\ge6a
\quad(s\ge2).\tag{2}
\]

For the final inversion \(s=1\), use \(a=1\) when \(c\equiv2\pmod3\),
and \(a=2\) when \(c\equiv1\pmod3\). This always produces a positive
integer. A final unit condition is unnecessary. Since
\(R(1,c)=12+V(c\bmod M)\ge12\), the last cost \(6a\le12\) is paid too.
The table also confirms that

\[
\min_{r\in(\mathbb Z/M\mathbb Z)^\times_3}
\bigl(13+V(r)-6a_{\rm final}(r)\bigr)=1;
\]

thus the terminal offset used above is exact for this potential.

All nonterminal ranks are natural numbers. Summing their decreases,
including the terminal step, proves

\[
6\sum a\le13t+V(c\bmod M)-1.
\]

Set \(k=\sum a\). This proves the cost bound.

## 4. Positivity, the suffix bound, and the forward word

Starting from \(b=0,s=t,0<c<3^t\), maintain

\[
0<c<2^b3^s.
\]

After an inverse step,

\[
0<\phi_a(c)<2^{b+a}3^{s-1}.
\]

After the \(t\)-th step, the source therefore equals
\(2^k x+r\) with \(0<r<2^k\).

For any positive integral target \(Y\), if \(z=\phi_a(Y)\) is integral,
then \(z\) is odd and

\[
T(z)=2^{a-1}Y,
\qquad T^a(z)=Y.
\]

The first event in this block is odd; the next \(a-1\) events are even.
Reverse the list of inverse actions to obtain the required forward word,
with exactly \(t\) odd events.

The final affine target \(3^t x+c\) can be even. Consequently the last
block should be described as an exact shortcut block; its \(a\) need not
equal the full odd-map valuation if that target is even. No odd-map
interpretation is needed for the theorem.

At every inverse endpoint, the affine coefficient is at least two and the
constant is at least one when \(x\ge1\). The endpoint is therefore at least
three. Intermediate forward points within a block are positive powers of
two times such endpoints. None reaches one.

## 5. Reproduction and independent checks

Run, from this packet's directory:

```sh
python verify_credit.py
```

No third-party Python package is needed. The command verifies the whole
finite inequality certificate, then rejects an all-zero-potential mutation
at residue five. It also independently replays the forward **affine** maps
of 6,575 compiled cones: every unit tail through \(t=8\), and five tails
at each of \(t=40,100,1000\). Each replay checks parity independently of
the prefix, coefficient, intercept, suffix range, odd count, and cost.
These replays are implementation regressions; the universal theorem rests
on Sections 2–4, not on their finite range.

A second agent wrote a separate scalar verifier without importing this
verifier or the synthesis routine. It checked the same 354,294 rows and
all three selected-action lifts, found the same action counts and terminal
minimum, and rejected the zero-potential mutation at residue five.

For synthesis, the optional NumPy program can regenerate the values:

```sh
python search_credit.py --digits 12 --p 13 --q 6 --amax 12 --limit 700 --out regenerated.json
```

The integer recurrence stabilized at iteration 670, with minimum zero and
maximum 66. Although synthesis allowed actions through 12, independent
verification finds a valid action through 10 in every row. The runtime
field in regenerated JSON is observational metadata and is not expected
to be byte-identical.

## 6. What this does not transfer to the forward problem

The rank \(R\) decreases because an inverse conversion consumes one of the
prescribed \(t\) ternary factors. A forward Collatz trajectory is not
equipped with such a decreasing counter. This proof supplies no rank
decrease on the forward critical returns, no bound on their number, and no
strict descent below the original source.

There is also a proved obstruction to seeking a universal contracting
same-prefix compiler. As already shown in #141, covering all
\(2\cdot3^{t-1}\) unit tails with maximum length \(K\) requires

\[
\binom Kt\ge2\cdot3^{t-1}.
\]

The asymptotic slope must consequently be at least the root
\(\rho\approx1.6417941208\) of

\[
\rho\log\rho-(\rho-1)\log(\rho-1)=\log3.
\]

Since this is greater than \(\log_2 3\approx1.5849625007\), no improvement
to this same-prefix, all-tail interface can make every source numerically
smaller for every positive prefix. This obstruction applies even if one
replaces the particular potential by an arbitrarily large dictionary.

Fixed-target ancestor steering is a different problem. It asks, for a
given ordinary target \(u\) and chosen residue \(y\pmod{3^s}\), for an
ancestor \(z\equiv y\pmod{3^s}\) with controlled size. The compiler above
does not prescribe its output residue. In particular, its positive-prefix
theorem does not even express the target one as \(3^t x+c\). Extending the
algebra to a zero prefix still does not force the desired ancestor residue.

A finite strategy steering into a residue modulo \(3^s\) also does not
automatically compose digit by digit: each inverse division consumes one
known ternary digit, and subsequent actions can change the digits already
steered. A scale-uniform steering lemma preserving the needed congruence
information is not proved or used in this packet. The external routing
results require separate review before using them in any further
composition. No deduction of forward descent from those results is made
here.
