# Three strict reductions of the exact five-ray obligation

**PROPOSED, unconditional.** Write \(E(t)\) for the assertion that the
ordinary shortcut orbits of \(t\) and \(5t+1\) meet. PR146 proves
\(\forall t>0\ E(t)\) equivalent to Collatz. The rules here reduce that
same assertion to a smaller positive parameter. Their union is not a
complete cover.

## 1. Two six-step forward returns

For every positive integer in the indicated class,

| guard | new parameter \(s\) | word from \(t\) | word from \(5t+1\) |
|---|---|---|---|
| \(t\equiv11\pmod{64}\) | \((27t+23)/64\) | `110100` | `000111` |
| \(t\equiv35\pmod{64}\) | \((9t+5)/64\) | `110000` | `000011` |

Both rows satisfy the exact identities

\[
T^6(t)=s,\qquad T^6(5t+1)=5s+1,\qquad 1\le s<t.   \tag{1}
\]

For the first row the odd counts are both 3 and the numerator offsets
are 23 and 152. Thus the second endpoint is
\((27(5t+1)+152)/64=5(27t+23)/64+1\).
For the second row the counts are both 2 and the offsets are 5 and 80;
its second endpoint is \((9(5t+1)+80)/64=5(9t+5)/64+1\).
The canonical positive starts 11 and 35 both map to \(s=5\).
Final integrality determines the stated parity words, so every lift is
physical. Positivity and strict decrease also follow directly from
\(27t+23<64t\) and \(9t+5<64t\) for every positive integer \(t\).

Consequently \(E(t)\Longleftrightarrow E(s)\) in either row. This is a
reduction between two five-ray questions, not a claim that either arm has
already reached 1.

## 2. A third reduction from a certified three-ray parameter

Let \(M,r\) be the constants in `THREE_RAY_POSITIVE_FAMILY.md`.
If \(t=4u\) and \(u\equiv r\pmod M\), set \(s=3u=3t/4<t\).
The 37-step certificate gives \(T^{37}(u)=T^{37}(s)\), while

\[
T^2(t)=u,\qquad T^2(5t+1)=15u+1=5s+1.             \tag{2}
\]

Thus \(E(t)\Longleftrightarrow E(s)\). A concrete meeting certificate
\(T^a(s)=T^b(5s+1)=z\) composes to

\[
T^{a+39}(t)=T^{b+39}(5t+1)=T^{37}(z).              \tag{3}
\]

The clocks in (3) are deliberately padded for simple exact composition;
no minimality claim is made. Dyadic extensions of the three-ray guard can
also be used after recording their additional common halving clocks, but
the implementation below uses the displayed guard only.

## 3. A clean unbounded run of the second guard

The map \(F(t)=(9t+5)/64\) has fixed point \(1/11\). For every \(k\ge1\),
the single congruence

\[
11t\equiv1\pmod{64^k}                              \tag{4}
\]

certifies \(k\) consecutive applications of the second row, with

\[
F^k(t)=\frac1{11}+\left(\frac9{64}\right)^k
                  \left(t-\frac1{11}\right).
\]

The positive intermediate parameters are integral and strictly decrease.
This follows either by induction on the congruence or by final integrality
of the concatenated physical words. The run therefore terminates on every
positive integer; the rational fixed point is not a positive integer.
For each \(k\), (4) has infinitely many positive ordinary solutions.
This proves an unbounded family of recursive reductions, not coverage of
all parameters.

An explicit terminal family is

\[
t=(4^m-1)/3,\qquad m\ge1.                          \tag{5}
\]

For these parameters, \(T^{2m}(t)=1\) and
\(T^{2m}(5t+1)=5\); both arms therefore reach 1 at the common clock
\(2m+4\). This includes \(t=1\).

Arbitrarily long runs in (4) can be made to end in (5). Choose \(m\ge1\)
with \(11\cdot4^m\equiv14\pmod{3^{2k+1}}\); such \(m\) exist because
4 generates the units congruent to 1 modulo three. Put \(s=(4^m-1)/3\)
and \(t=1/11+(64/9)^k(s-1/11)\). To check both denominators explicitly,
put \(w=(11s-1)/9^k\), which is an integer by the chosen congruence.
Then \(t=(1+64^k w)/11\) is integral because \(64\equiv9\pmod{11}\)
and \(9^k w=11s-1\equiv-1\pmod{11}\). This also gives (4), while
\(t>s>0\). Hence this is an explicit family of
successful certificates with unbounded recursive depth. Its enormous
members are supplied by the written arithmetic, not enumerated in the
finite replay.

### Every finite word in the two six-step guards can end at a terminal

The construction extends to an arbitrary nonempty ordered word of length
\(k\) in the first two rows. Write its successive affine maps as
\(F_j(t)=(a_jt+b_j)/64\), with \((a_j,b_j)\) equal to \((27,23)\)
or \((9,5)\). Their composition is

\[
F_w(t)=\frac{3^e t+B}{64^k},\qquad
e=\sum_{j=0}^{k-1}\log_3 a_j,
\]

where \(B_0=0\) and \(B_{j+1}=a_jB_j+b_j64^j\), so \(B=B_k\).
Both basic maps are increasing and carry \(1\) strictly below \(1\).
They also carry the interval \((0,1)\) into itself. Consequently

\[
                  0<B<64^k-3^e.                  \tag{6}
\]

Choose any positive \(m\) satisfying

\[
4^m\equiv1+3B\,64^{-k}\pmod{3^{e+1}}.             \tag{7}
\]

Here \(64^{-k}\) denotes a modular inverse. The right side is a unit
congruent to 1 modulo three, so the fact that 4 generates that group gives
one class of solutions \(m\pmod{3^e}\), hence infinitely many positive
solutions. Set

\[
s=\frac{4^m-1}{3},\qquad
t=\frac{64^k s-B}{3^e}.                           \tag{8}
\]

Equation (7) proves that \(t\) is an integer, and (6) proves \(t>s\ge1\).
The concatenated left parity word has length \(6k\), odd count \(e\),
and integral nominal endpoint \(s\). Final integrality identifies its
unique legal binary source class, so the entire left word is physical.
The concatenated right word has nominal endpoint \(5s+1\), which is
also integral, and is physical for the same reason. At each intermediate
stage the selected row is therefore legal. Its positive integer parameter
strictly decreases by (1).

After the selected \(k\) reductions, the terminal certificate (5) yields

\[
              T^{6k+2m+4}(t)=T^{6k+2m+4}(5t+1)=1. \tag{9}
\]

Thus every prescribed finite guard word has infinitely many positive
ordinary realizations, all with explicit proof certificates ending at 1.
Distinct words of the same length give disjoint binary source classes,
because their left parity words differ. Classes for words of different
lengths may be nested when one word is a prefix of another.
These are valid proof sequences of arbitrarily large depth; no claim
that a shorter certificate is impossible is intended. This construction
still does not cover every fixed ordinary input.

## 4. A terminating partial proof-producing selector

The accompanying program repeatedly applies the first applicable guard,
recording its exact transport. At a terminal of form (5), it returns the
explicit common-clock certificate and composes all recorded transports.
If no guard and no terminal applies, it returns **UNRESOLVED**.

Every reduction strictly decreases the positive integer parameter, so the
program terminates. Termination does not mean universal success. With only
the symbolic terminal (5), the smallest uncovered input is \(t=2\): it
satisfies none of the three guards. Its actual paths do meet, so this is
a hole in the selector, not a Collatz counterexample. Adding a finite
ordinary terminal cache resolves such examples but supplies no proof that
the remaining complement is empty.

The distinction is essential: (1) and (2) are genuine well-founded
reductions, but no invariant or guard-cover theorem has been proved for
every remaining ordinary input. Multiplication by three is not used as
an unproved transport. The third guard uses its actual 37-step witness.

## Provenance

The universal five-ray formulation and compatible affine constructions
are from PR146 at `561d48a4d3a793a59b1cdf0406062ae1a6d47515`.
The new source head `7d04c4dd756cfe495eb3eee78eba35a99085cd2a` contains
additional three-ray smaller-input and window reductions; these remain
separate source results. The explicit return identities above and their
strict parameter decrease are proved locally. No broad priority claim is
made for affine Collatz rewriting or recursive descent.
