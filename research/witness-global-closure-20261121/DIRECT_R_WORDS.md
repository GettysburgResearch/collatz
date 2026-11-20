# Direct reverse-triple witness transformations

**Status: partial exact results; the universal closure remains OPEN.**

This note studies the direct implication

\[
R(m):\qquad 27m\in E\Longrightarrow9m\in E
\qquad(m>0\text{ odd}).
\]

It gives a complete first-letter normal form, explicit transformations of
arbitrary complete input witnesses on stated domains, and a finite reduction
of the first letter of a hypothetical least failure. It does not supply a
transformation for every source witness. The proofs of DRW-001 through
DRW-005 use only integer algebra and the defining witness identity. The
least-failure corollary DRW-006 additionally uses the precisely identified
height theorem RGA-003 in [REDUCTION_AUDIT.md](REDUCTION_AUDIT.md).

## 1. Witness convention

Write \(E\) for the positive integers admitting

\[
3^r n+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r},
\qquad 0=A_0<A_1<\cdots<A_r.
\tag{1}
\]

The empty witness is permitted exactly for \(n=1\). An **exponent word**
\(a_1,\ldots,a_r\) means \(a_i=A_i-A_{i-1}>0\). For a positive odd integer
define

\[
S(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Equation (1) is equivalent to an ordinary odd trajectory ending at 1,
whose exact valuations are the word letters. In one direction this follows
by multiplying the recurrences \(2^{a_i}n_i=3n_{i-1}+1\). Conversely,
reducing (1) successively modulo the next power of two forces each stated
valuation and leaves the shorter identity. All states are positive odd
integers. A witness may include exponent-2 loops at 1; no assertion below
requires a first-hit witness.

If \(n>1\), its witness has a first letter. The maps

\[
J(n)=4n+1,\qquad H(n)=2n+1
\]

will be used only at positive odd integer inputs. Since
\(3J(n)+1=4(3n+1)\), a nonempty witness
\((b,c_2,\ldots,c_L)\) for \(n\) gives the witness
\((b+2,c_2,\ldots,c_L)\) for \(J(n)\). In particular
\(J(n)\in E\iff n\in E\). For the exceptional empty witness of 1,
\(J(1)=5\) has witness \((4)\); the word transformations below avoid this
exception by proving their relevant tail endpoint exceeds 1.

For odd \(t>0\), direct iteration also gives

\[
4^k t+1\in E\iff3^{k-1}t\in E\quad(k\ge1),
\tag{2}
\]

and

\[
S^k(2\cdot4^k t+1)=2\cdot3^k t+1\quad(k\ge0).
\tag{3}
\]

For (2), the first \(k-1\) letters are 2 and their endpoint is
\(J(3^{k-1}t)\). Formula (3) has exactly \(k\) initial letters 2.

## 2. DRW-001 — the complete first-letter normal form

**Status: PROVED-IN-NOTE. Scope: every positive odd \(m\) and every complete
source witness for \(N=27m\).**

Let its first letter be \(a\), and put

\[
t=S(N),\qquad z=N/3=9m.
\]

Then

\[
N=\frac{2^a t-1}{3},\qquad
z=\frac{2^a t-1}{9},\qquad
2^a t\equiv1\pmod{81},\qquad t\in E.
\tag{4}
\]

The last assertion uses the supplied witness with its first letter removed;
it does not presume a new convergence theorem. Conversely, any positive
odd \(t\in E\) and \(a\ge1\) satisfying the congruence in (4) give a
positive odd multiple \(N\) of 27 with a known witness beginning with \(a\).

Here is the exact remaining endpoint in each case. Write
\(b=v_2(t+1)\) in the first two rows.

| Source first letter | Endpoint \(q\) equivalent to \(z\) | Prefix from \(z\), before a possible \(J\) removal |
|---|---|---|
| \(a=1\) | \((t+1)/(3\cdot2^b)\) | One letter \(b+1\), ending at \(q\) |
| \(a=2\) | \((t+1)/2^b\) | Letters \(1,b+1\), ending at \(q\) |
| \(a=2d\ge4\) | \(3^{d-2}t\) | Letters \(1,1\), then \(d-2\) letters 2, ending at \(J(q)\) |
| \(a=2d+1\ge3\) | \(2\cdot3^{d-1}t+1\) | Letters \(1,1\), then \(d-1\) letters 2, ending at \(q\) |

Every row asserts the equivalence \(z\in E\iff q\in E\), including both
directions. It does not assert \(q\in E\) merely because \(t\in E\).

### Proof of the low-letter rows

For \(a=1\), (4) gives \(t\equiv41\pmod{81}\), so
\(v_3(t+1)=1\). Also

\[
3z+1=\frac{2(t+1)}3.
\]

Its exact two-adic valuation is \(b+1\), and its odd successor is the
positive odd integer \((t+1)/(3\cdot2^b)\).

For \(a=2\), the first successor is

\[
z\xrightarrow{1}\frac{2t+1}{3}.
\]

This is an integer because \(t\equiv61\pmod{81}\). Multiplying that
successor by 3 and adding 1 gives \(2(t+1)\), so its next exact letter is
\(b+1\), with endpoint \((t+1)/2^b\).

### Proof for \(a\ge3\)

There are always two exact exponent-1 steps:

\[
z\xrightarrow{1}\frac{2^{a-1}t+1}{3}
\xrightarrow{1}2^{a-2}t+1.
\tag{5}
\]

For the first step, \(3z+1=2(2^{a-1}t+1)/3\), with odd quotient. For
the second, \(3(2^{a-1}t+1)/3+1=2(2^{a-2}t+1)\), again with odd
quotient. Apply (2) or (3) according to the parity of \(a\).

The even-row endpoint \(q=3^{d-2}t\) exceeds 1: if it were 1 then
\(d=2,t=1\), contradicting \(2^a t\equiv1\pmod{81}\). Thus the
nonempty-witness rule for \(J\) always applies in this row.

## 3. DRW-002 — exact reconstruction, with arbitrary output length

**Status: PROVED-IN-NOTE. Scope: the four rows of DRW-001.**

Suppose a complete witness for the displayed endpoint \(q\) has odd
length \(L\) and total exponent \(B\). Prefix it as in the table, adding
2 to its first letter in the even \(a\ge4\) row. The resulting witness
for \(z=9m\) has the following exact statistics:

| Source first letter | Target odd length | Target total exponent |
|---|---:|---:|
| \(a=1\) | \(L+1\) | \(B+b+1\) |
| \(a=2\) | \(L+2\) | \(B+b+2\) |
| \(a=2d\ge4\) | \(L+d\) | \(B+a\) |
| \(a=2d+1\ge3\) | \(L+d+1\) | \(B+a-1\) |

This is ordinary concatenation of exact odd trajectories. Consequently it
also proves (1) for the reconstructed word. In the first two rows an empty
endpoint witness is allowed if \(q=1\). In the other two rows \(q>1\).

## 4. DRW-003 — an arbitrary-witness rewrite when \(a=4\)

**Status: PROVED-IN-NOTE. Scope: all positive odd \(m\equiv31\pmod{32}\).**

Every complete source word for \(27m\) has the form
\((4,b,c_3,\ldots,c_r)\). There is a complete witness for \(9m\) given by

\[
\boxed{(4,b,c_3,\ldots,c_r)
\longmapsto(1,1,b+2,c_3,\ldots,c_r).}
\tag{6}
\]

The target odd length is \(r+1\), and its total exponent is unchanged.

Indeed, \(v_2(81m+1)=4\) is equivalent to \(m\equiv31\pmod{32}\).
The \(a=4\) row has \(q=t\), and (5) ends at \(J(t)\). The source
tail witnesses \(t\), so (6) follows by the \(J\) rule. This tail cannot
be empty because \(t=1\) would give \(27m=5\).

The transformation accepts the full supplied witness, including any
terminal loops at 1; it does not search for a target orbit.

## 5. DRW-004 — two unbounded word identities

**Status: PROVED-IN-NOTE. Scope: the displayed prefix languages only.**

An exponent followed by a superscript in this section means repetition of
a letter, rather than exponentiation of an integer. For \(k,\ell\ge0\),
the following source words for a positive odd multiple of 27 admit exact
rewrites:

\[
\boxed{(2^k,4,b,\ldots)
\longmapsto(1,2^k,1,b+2,\ldots),}
\tag{7}
\]

\[
\boxed{(2^k,3,1^\ell,2,b,\ldots)
\longmapsto(1,2^k,1^{\ell+2},b+2,\ldots).}
\tag{8}
\]

Each output witnesses one third of the source. Its odd length increases
by one; its total exponent is unchanged. Formula (7) contains (6).

Here is an algebraic proof that also checks ordinary legality. Put
\(F_a(n)=(3n+1)/2^a\) and \(D(n)=(n+1)/2\). As rational affine maps,

\[
F_1(n/3)=D(n),\quad F_2D=DF_2,\quad F_1D=JF_4,
\tag{9}
\]

and

\[
F_1D=HF_3,\quad F_1H=HF_1,\quad F_1H=JF_2.
\tag{10}
\]

During the source's initial exponent-2 steps, and at a following
exponent-3 or exponent-4 step, its relevant odd state is \(1\pmod4\).
Thus every intervening \(D(n)\) is a positive odd integer. The initial
target step has exponent 1 because its endpoint \(D(n)\) is odd. The
commutation in (9) therefore supplies exact target exponent-2 steps, and
the last identity in (9) gives the final exponent-1 step to \(J\) of
the source endpoint. This proves (7).

For (8), after the initial exponent-2 block, the first identity in (10)
changes the target state to \(H\) of the next source state. Such states
are always positive odd integers. Each following source letter 1 is
matched by a target letter 1 through the second identity in (10). The
source letter 2 is then matched by a target letter 1 ending at \(J\)
of the remaining source endpoint. Modify the tail witness by the \(J\)
rule to finish.

The needed tail endpoint cannot equal 1. For (7), the source state before
the last letter 4 would be 5; a preceding inverse exponent-2 step would
be \((4\cdot5-1)/3=19/3\), while without that step the whole source
would be 5, not a multiple of 27. For (8), the state before the last
letter 2 would be 1; an immediately preceding letter 1 would require
\(1/3\), and an immediately preceding letter 3 would require \(7/3\).
Both contradict ordinary integrality. Thus adding 2 to the first tail
letter is legitimate in every case stated.

These languages do not exhaust the admissible source words. For example,
the one-letter words in the next section belong to neither language.

## 6. DRW-005 — the exact one-letter residual

**Status: PROVED-IN-NOTE. Scope: every one-letter source witness.**

A one-letter witness for a positive odd multiple of 27 has the form

\[
N=\frac{2^{54k}-1}{3},\qquad k\ge1.
\tag{11}
\]

To justify the modulus, \(2^{54}\equiv1\pmod{81}\), and the order of
2 modulo 81 is 54. An elementary check is
\(2^{18}\equiv28\pmod{81}\), \(28^3\equiv1\pmod{81}\), and
\(2^{27}\equiv-1\pmod{81}\); neither maximal proper divisor 18 nor 27
of 54 is an order, so no proper divisor is an order.

The requested target satisfies the exact equivalence

\[
\boxed{\frac{2^{54k}-1}{9}\in E
\iff3^{27k-2}\in E.}
\tag{12}
\]

It follows either from DRW-001 with \(t=1,d=27k\), or from

\[
\frac{2^{54k}-1}{9}
\xrightarrow{1}\frac{2^{54k-1}+1}{3}
\xrightarrow{1}2^{54k-2}+1
=4^{27k-1}+1
\]

and (2). A witness of length \(L\), total exponent \(B\), for the pure
power in (12) gives a target witness of length \(L+27k\) and total
exponent \(B+54k\). No convergence assertion for all those powers is
made in this note. A single-letter source witness alone does not include
the additional witness required on the right of (12).

## 7. DRW-006 — a finite first-letter reduction for a least failure

**Status: PROVED-IN-NOTE conditional on the audited height theorem
RGA-003. Scope: a hypothetical least failing antecedent, not every
individual R instance in isolation.**

Suppose \(N_*\) is the least positive odd multiple of 27 such that
\(N_*\in E\) but \(N_*/3\notin E\). RGA-003 gives

\[
H=\frac{213597}{23},\qquad H'=\frac{355995}{23},
\]

with the properties that every positive ternary unit below \(N_*/H\)
converges and every positive integer below \(N_*/H'\) converges. For an
even integer, convergence here means that its odd part belongs to \(E\).

Let \(a\) be the first letter of the supplied witness for \(N_*\). Then

\[
\boxed{a\notin\{60,62,64,\ldots\}
\quad\text{and}\quad
a\notin\{65,67,69,\ldots\}.}
\tag{13}
\]

For \(a=2d\ge4\), the normal-form endpoint is \(q=3^{d-2}t\). Since
\(2^a t=3N_*+1\ge82\),

\[
\frac q{N_*}
=\frac{3^{d-1}t}{4^d t-1}
\le\frac{82}{243}\left(\frac34\right)^d.
\]

Exact integer arithmetic gives

\[
\frac{355995}{23}\frac{82}{243}\left(\frac34\right)^{30}<1.
\tag{14}
\]

The bound decreases with \(d\), so \(d\ge30\) puts \(q\) in the
certified interval. This contradicts \(N_*/3\notin E\).

For \(a=2d+1\) with \(d\ge2\), the endpoint
\(q=2\cdot3^{d-1}t+1\) is a ternary unit. Its ratio satisfies

\[
\frac q{N_*}
=\frac{2\cdot3^d t+3}{2\cdot4^d t-1}
\le\frac{2\cdot3^d+3}{2\cdot4^d-1}.
\]

The last bound decreases with \(d\), and exact arithmetic gives

\[
\frac{213597}{23}
\frac{2\cdot3^{32}+3}{2\cdot4^{32}-1}<1.
\tag{15}
\]

Thus every odd \(a\ge65\) is excluded. The decrease in \(d\) can be
checked by cross multiplication: the difference of consecutive cross
products is \(4\cdot3^d4^d+4\cdot3^d+18\cdot4^d>0\).

The exact unrestricted endpoint bounds used here do not also exclude
\(a=58\) or \(a=63\); the corresponding products exceed 1. This does
not assert those letters are actual failures. The remaining first letters
are \(1,2\), even letters through 58, and odd letters through 63.
DRW-003 and DRW-004 solve some of the corresponding word languages.

There is also a finite restriction on the low-letter rows. If \(a=1\)
or \(a=2\), put \(b=v_2(t+1)\). The respective residual endpoints are
ternary units: the congruences are \(t\equiv41\pmod{162}\) and
\(t\equiv61\pmod{162}\), with \(v_3(t+1)=1\) in the first case and
\(v_3(t+1)=0\) in the second. Their ratios satisfy

\[
\frac q{N_*}\le\frac{14}{27\cdot2^b}\quad(a=1),
\qquad
\frac q{N_*}\le\frac{62}{81\cdot2^b}\quad(a=2).
\tag{16}
\]

Indeed, the unbounded factors \((t+1)/(2t-1)\) and
\(3(t+1)/(4t-1)\) decrease with \(t\); their maxima over the respective
admissible ranges \(t\ge41\) and \(t\ge61\) are \(14/27\) and
\(62/81\). Multiplying either bound in (16) by \(H\) gives a number
less than 1 at \(b=13\), hence at every larger \(b\). Consequently

\[
\boxed{a\in\{1,2\}\quad\Longrightarrow\quad v_2(t+1)\le12}
\tag{17}
\]

for a least failure. This is a restriction on its beginning, not a bound
on the length of its complete source witness.

Handling every remaining complete word is still OPEN. Further least-failure
consequences, including the rank-one case and specified rank-two words, are
kept separately in [LEAST_R_FAILURE.md](LEAST_R_FAILURE.md).

## 8. Replay and evidence limits

Run from the repository root:

```sh
python3 research/witness-global-closure-20261121/check_direct_r_words.py
python3 -O research/witness-global-closure-20261121/check_direct_r_words.py
```

The checker uses exact integers and rational affine maps. It validates
the finite algebraic identities behind the unbounded word inductions,
reconstructs complete target witnesses for stated finite fixtures,
rejects malformed source witnesses, and checks the rational inequalities
in (14) and (15). Its bounded orbit routine is used only to obtain
explicit fixture witnesses; a failure to finish within its cap is an
error, never a claimed counterexample or a successful certificate.

The proof supplies the universal quantifiers for the stated normal forms
and word languages. Finite replay is not exhaustive coverage of all
source witnesses, formal verification, or a proof of universal R.
