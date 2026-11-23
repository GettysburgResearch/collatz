# Retaining a full prefix makes ordinary sibling copies expensive

**Status.** This is a proved obstruction to one proposed way of amplifying a
fixed escaping source. It is not a descent theorem or an upper bound for the
canonical potential. The word length, every valuation, and the total clock are
unrestricted. The theorem applies to convergent, periodic, and escaping
trajectories alike. “Unrestricted depth” here means that the statement holds
for every supplied finite word; it does not identify words at different depths
or sum their potentials.

The companion `SiblingPrefixLift.lean` checks the general 3-adic divisibility,
the exact affine lift, and its height cost. Actual gap legality, the unit-source
condition, and the infinite geometric sum are proved below in ordinary
mathematics. No empirical mixing or unproved source equidistribution is used.

## 1. A fixed ordinary source and its actual word

Let

\[
p=p_0\longmapsto p_1\longmapsto\cdots\longmapsto p_s=q,
\qquad 3p_{i-1}+1=2^{a_i}p_i,
\tag{1}
\]

be an actual accelerated Collatz word. Every `p_i` is a positive odd integer
and every `a_i` is positive. Write

\[
A_i=\sum_{h=1}^{i}a_h,\qquad A=A_s,
\qquad 2^Aq=3^sp+C.
\tag{2}
\]

Here the ordinary word correction `C` is a nonnegative integer. For the empty
word, `s=A=C=0` and `q=p`.

For each integer `j≥0`, form the ordinary odd sibling

\[
q[j]=4^jq+\frac{4^j-1}{3}.
\tag{3}
\]

This is a positive odd integer and

\[
3q[j]+1=4^j(3q+1).
\tag{4}
\]

Consequently, `q[j]` has exactly the same next accelerated image as `q`. If
the next valuation at `q` is `a`, the next valuation at `q[j]` is `a+2j`.
The elementary sibling relation is cheap at the endpoint. The question is
whether it remains cheap when the whole history from a fixed source is
retained.

## 2. Exact integrality threshold

Pulling `q[j]` back through precisely the word in (1) gives the unique rational
candidate

\[
\begin{aligned}
p[j]
 &=\frac{2^Aq[j]-C}{3^s}\\
 &=4^jp+
   \frac{(4^j-1)(3C+2^A)}{3^{s+1}}.
\end{aligned}
\tag{5}
\]

Since `3C+2^A` is coprime to 3,

\[
\boxed{\quad p[j]\in\mathbb Z
\quad\Longleftrightarrow\quad 3^s\mid j.\quad}
\tag{6}
\]

For completeness, the valuation calculation behind (6) is

\[
v_3(4^j-1)=1+v_3(j)\qquad(j>0).
\tag{7}
\]

To prove it without an asymptotic theorem, write `j=3^r u`, where `3∤u`.
The binomial formula gives `4^u−1≡3u mod 9`, so its valuation is exactly
one. If `z=1+3^h v`, with `h≥1` and `3∤v`, then

\[
z^2+z+1=3\bigl(1+3^h v+3^{2h-1}v^2\bigr)
\]

has valuation exactly one. The identity `z^3−1=(z−1)(z²+z+1)` therefore
raises the valuation by precisely one. Repeat this `r` times. The case
`j=0` in (6) is immediate and does not use a valuation of zero.

The Lean theorem `affine_numerator_divisibility` checks, for arbitrary natural
`s,A,C,j`, the precise denominator condition

\[
3^{s+1}\mid(4^j-1)(3C+2^A)
\quad\Longleftrightarrow\quad 3^s\mid j.
\]

## 3. Every integral candidate really retains the word

Final integrality is not being substituted for actual orbit legality. Suppose
`3^s∣j` and put

\[
J_j=\frac{4^j-1}{3^{s+1}}\in\mathbb N.
\]

Equations (2) and (5) give two exact integer descriptions:

\[
\boxed{\quad
p[j]=p+2^A(3q+1)J_j
     =4^jp+J_j(3C+2^A).
\quad}
\tag{8}
\]

For every prefix of the supplied word, define

\[
p_i[j]=p_i+3^i2^{A-A_i}(3q+1)J_j,
\qquad 0\le i\le s.
\tag{9}
\]

These are positive integers. Their increments over `p_i` are even because
`q` is odd and `3q+1` is even. Thus every `p_i[j]` is odd. Direct substitution
using `A_i=A_{i-1}+a_i` shows

\[
3p_{i-1}[j]+1=2^{a_i}p_i[j].
\tag{10}
\]

Since the right endpoint is odd, the valuation in (10) is **exactly** `a_i`.
There are no unintended extra divisions by two. At `i=0`, (9) is (8), and
at `i=s` it is precisely (3). This proves that the complete original word
is retained as an actual positive ordinary trajectory.

Equivalently, the source increment in (8) is a multiple of `2^(A+1)`, which
preserves the full parity cylinder including the final odd endpoint. Formula
(9) additionally makes positivity and every intermediate valuation explicit.

For the empty word, all `j` are legal and (8) reduces to `p[j]=q[j]`, with
`p=q`. Thus (6)–(10) also cover `s=0` exactly.

## 4. Ternary units require an additional condition

Integral positive odd copies need not all be units modulo 3. Write a legal
index as `j=3^s ℓ`. Then

\[
J_j\equiv\ell\pmod3,
\qquad
\boxed{\quad p[j]\equiv p+2^A\ell\pmod3.\quad}
\tag{11}
\]

Here is a direct proof of the first congruence. Induction by cubing shows

\[
4^{3^s}\equiv1+3^{s+1}\pmod{3^{s+2}}.
\]

Raising this congruence to the nonnegative integer power `ℓ` and dividing
`4^(3^s ℓ)−1` by `3^(s+1)` gives `J_j≡ℓ mod 3`. The second congruence
then follows from (8).

If the original source `p` is a unit, exactly one residue class of `ℓ mod 3`
produces nonunit sources; the other two classes produce units. In particular,
`ℓ≡0 mod 3` preserves the original unit residue. For example, the actual
word `7→11` has `s=A=C=1`. The first legal nonzero index is `j=3`, but its
lifted source is

\[
p[3]=483,\qquad q[3]=725,\qquad 3\cdot483+1=2\cdot725.
\]

Thus the first legal lifted source in this example is divisible by 3.
It must not be included in an inverse tree whose states are required to be
ternary units.

When `s≥1`, legal indices `j` are multiples of 3 and (7) implies
`q[j]≡q mod 3`. Therefore a unit endpoint remains a unit. At `s=0`, the
source and target are the same sibling, and (11) gives their common unit
condition.

## 5. The first copy and the total source weight

If `j>0` is legal, then `j≥3^s`. By (8),

\[
\boxed{\quad p[j]\ge4^jp\ge4^{3^s}p.\quad}
\tag{12}
\]

Thus the first nontrivial legal index is exactly `3^s`, its source height
cost is at least `4^(3^s)`, and the next sibling gap adds at least
`2·3^s` shortcut clocks. All these statements hold for arbitrary supplied
valuations. There is no bounded-valuation hypothesis.

The values `p[j]` at legal indices are strictly increasing: (5) is a
strictly increasing affine function of `4^j` because `p>0`. Consequently
the following is a sum over distinct physical source integers. The entire
inverse-square weight of the **nonzero** literal-prefix copies satisfies

\[
\begin{aligned}
\sum_{\substack{j\ge1\\3^s\mid j}}\frac1{p[j]^2}
&=\sum_{\ell\ge1}\frac1{p[3^s\ell]^2}\\
&\le\frac1{p^2}\sum_{\ell\ge1}16^{-3^s\ell}\\
&=\boxed{\frac{p^{-2}}{16^{3^s}-1}}.
\end{aligned}
\tag{13}
\]

This estimate includes unit and nonunit copies. Restricting the sum to the
unit sources allowed by (11) only decreases it. It also covers `s=0`, when
the denominator is 15. For a fixed original source and prefixes of growing
odd depth, the right side tends to zero doubly exponentially in that depth.

The measured quantity in (13) is the original source weight `p[j]⁻²`, as used
in the fixed-source endpoint sums. It is **not** a bound on `G(p[j])`, on
the component measure `ν(p[j])`, or on an inverse Green function that has
already accumulated the weights of other sources.

## 6. What the failed amplification argument was missing

An escaping orbit supplies arbitrarily long actual prefixes. Replacing an
endpoint by a bounded-index sibling certainly gives a cheap endpoint in the
same component. But (6) shows that no fixed nonzero sibling index can retain
those prefixes once their odd depths grow beyond its 3-adic valuation.
The first legal retained-prefix copies instead satisfy (12)–(13). This
rules out the particular claim that the elementary sibling relation alone
replicates the same positive original source mass at every depth.

Changing the supplied word can evade this divisibility obstruction. The
calculation does not exclude a cheap different-word ancestor, and it does
not prove one exists. Counting coefficient-neutral words is not a substitute:
even an insufficient count to cover all ternary residue classes would not
exclude the possibility that the actual fixed-source endpoints always lie
in the classes covered.

There is a separate accounting issue with summing over many height floors.
For a single source `p`, intermediate point `n`, and endpoint `q`, the word
coefficients satisfy the exact multiplicative identity

\[
\omega(p\to n)\,\omega(n\to q)=\omega(p\to q).
\]

Charging the same trajectory at several floors charges the same original
atom several times. Those intermediate points are comparable under forward
iteration, so a budget for incomparable inverse branches cannot be applied
to them. The literal sibling construction would have supplied genuinely
distinct atoms, but its exact source cost is (13).

**The unresolved step remains a source-sensitive bound on the actual
potential carried by an unrestricted arrival word, or a valid word-changing
construction that produces cheaper sources with controlled total weight.**
Neither bound is proved here. In particular, this packet supplies no global
weighted-arrival upper bound and no proof of Collatz convergence.

## 7. Formal scope

`SiblingPrefixLift.lean` uses the pinned project Lean/mathlib runtime and
contains no Collatz assumption or custom axiom. Its public theorems establish:

- the exact 3-adic valuation for every positive index;
- the denominator and sibling-index divisibility equivalences for all depths;
- coprimality of the full affine correction;
- the natural-number sibling identity and exact quotient;
- the two expressions for the legal lifted source and its affine endpoint;
- the unrestricted height bound and the first nonzero lift height.

The proofs in Sections 3–5 establish the extra orbit, unit, and infinite-sum
claims directly. Their formalization is not claimed by this module. The
compilation log audits every public theorem's axioms; the receipt records the
source hash and compiler status.
