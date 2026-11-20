# Conditional reverse-triple bypasses with a strict height bound

**Status: PROPOSED exact conditional reductions; the complete reverse-triple
theorem remains OPEN.** The retained finite certificate has 27 disjoint
infinite cells and an explicit unresolved complement. A separate
parameterized identity applies at every integer index `k >= 3`. Neither
statement supplies a successful selector for every source witness.

## Setting and dependency boundary

For positive odd integers use the accelerated ordinary map

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]

Write \(E(n)\) for existence of a finite complete odd witness to 1, allowing
terminal exponent-2 loops at 1. Equivalently, its positive increments have
cumulative exponents \(0=A_0<A_1<\cdots<A_r\) satisfying

\[
3^r n+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r}.
\]

The assertion under investigation is

\[
R(m):\qquad E(27m)\Longrightarrow E(9m),
\qquad m>0\text{ odd}.
\]

The ordinary algebra below is self-contained. The parallel
[direct witness note](DIRECT_R_WORDS.md), DRW-003 and DRW-004, already proves
the full first-letter-4 case and two unbounded prefix languages. Some
retained cells are instances of those identities; they are baseline
coverage, not independent new discoveries. The conditional ladder in
RB-004 uses the previously known ordinary merger
\(54p+1\sim27p\) on \(p\equiv3\pmod8\), reconstructed explicitly below.

The broader investigation inspected PR157 at
`64361ecca770092d6c8242dc6211e38818af2e50`, PR163 at
`051237135a34ae7d4b973ee5fcf5da04ded6f0fc`, and PR166 at
`5996b9f525ca50978bc34f423192c36a87765bf3`. Their conditional global
theorems and five-multiplier certificate languages motivate the search;
no open premise from them is assumed here.

## RB-001 — the conditional path criterion

Set \(J(n)=4n+1\), with inverse \(K(n)=(n-1)/4\) on positive odd
outputs. An operation \(U_a\) is permitted only when its input and output
are positive odd integers and \(U_a(n)=(3n+1)/2^a\); consequently its
exponent is exact. Define \(I_a(n)=(2^a n-1)/3\), again only with a
positive odd integer output.

| Operation | Map | Membership relation and guard |
|---|---|---|
| `U,a` | \((3n+1)/2^a\) | Ordinary equivalence, exact exponent \(a\). |
| `I,a` | \((2^a n-1)/3\) | Ordinary equivalence, positive odd integral output. |
| `J,1` | \(4n+1\) | Ordinary equivalence for positive odd \(n\). |
| `K,1` | \((n-1)/4\) | Ordinary equivalence for \(n\equiv5\pmod8\), positive output. |
| `M,3` | \(y\mapsto3y\) | Read backwards for membership: \(E(3y)\Rightarrow E(y)\), using \(R(y/9)\). Require \(9\mid y\) and \(0<y<9m\). |
| `V,3` | \(3y\mapsto y\) | The same conditional implication read in the direction of known membership. Require \(9\mid y\) and \(0<y<9m\). |

A certificate gives two paths with the same exact affine endpoint:

1. A path from \(9m\), using ordinary equivalences and `M` only.
2. A path from \(27m\), using ordinary equivalences and `V` only.

Every conditional call has parameter \(p=y/9\), which is a positive odd
integer strictly less than \(m\). It follows that

\[
\bigl[\ R(p)\text{ holds for every positive odd }p<m\ \bigr]
\quad\Longrightarrow\quad R(m)
\tag{1}
\]

on the certified cell. To prove (1), start with known membership at
\(27m\), follow its path to the common endpoint, and traverse the
\(9m\) path in reverse. Each conditional operation now has the direction
\(E(27p)\Rightarrow E(9p)\), with \(p<m\).

Thus a complete cover, together with any explicitly excluded finite base
cases, would prove all \(R(m)\) by strong induction. A partial cover
only excludes its cells from a least failure. No induction hypothesis is
used at a larger intermediate vertex.

## RB-002 — arbitrary supplied witnesses and child-call order

`transform(source, cell, child_solver)` in
[check_r_bypass.py](check_r_bypass.py) implements exactly the proof order
above. It validates the supplied complete witness before using it. The
callback receives the complete witness currently established for
\(27p\), and must return a validated witness for \(9p\).

The child calls are sequential. A later child-source witness may depend
on the answer to an earlier child call, so the implementation does not
replace the dependency chain by an unordered list of presumed witnesses.
If a callback is absent or returns `None`, execution stops with
`UNRESOLVED` and the first outstanding child witness. A wrong child
source, malformed witness, or source outside the certified class is
rejected, not counted as a proof. The transformer performs no target
trajectory search.

The ordinary witness operations are exact:

- `U,a` removes the first increment \(a\). If the supplied word is empty,
  its source is 1; the only permitted such forward operation is `U,2`.
  One may pad by a single terminal 2 and remove it, leaving the same empty
  witness. This handles paths that continue after the supplied first hit.
- `I,a` prepends \(a\).
- `J,1` adds 2 to the first increment. At source 1 with the empty word,
  use the exponent-2 loop first: the resulting witness for 5 is `(4)`.
- `K,1` subtracts 2 from the first increment. Its input exceeds 1 and is
  \(5\pmod8\), so the word is nonempty and that increment is at least 3.

All remaining increments are retained verbatim. These rules apply equally
to a first-hit source witness and to any source witness padded by an
arbitrary number of terminal 2s. The output is validated anew. Intermediate
ordinary values are positive; no negative template or merely two-adic
trajectory is used.

The literal complete-word identity is equivalent to the recurrence used
by the validator. The public `cumulative` property returns the cumulative
tuple for the reconstructed witness, including its initial zero.

## RB-003 — retained all-lift certificate and exact open complement

The complete finite artifact is
[r-bypass-certificate.json](r-bypass-certificate.json). A cell means

\[
m=M u+r,\qquad
u\ge\max\left(0,\left\lceil\frac{m_{\min}-r}{M}\right\rceil\right).
\]

For every operation the checker carries both rational coefficients of
the affine form in \(u\). It verifies integer coefficients, an even
slope and odd intercept, positive value at the minimum \(u\), and a
positive slope. These checks prove positive odd integrality for every
lift. For `M` and `V` it additionally verifies divisibility by 9 of both
coefficients and coefficientwise strict decrease relative to \(9m\).
The two endpoint forms are compared as exact `Fraction` objects.

The 27 retained cells are disjoint. Their relative natural density among
positive odd parameters is exactly

\[
\frac{153468843955}{1043677052928}
\approx0.14704629513933304.
\tag{2}
\]

This is density of **verified conditional path cells**, not an assertion
that all inputs in conditional cells converge unconditionally. Their
remaining child obligations are retained. Ten of the 27 cells use
ordinary equivalences alone; the other 17 contain 29 conditional calls
in total.

Let \(a=v_2(81m+1)\) be the first source increment. The finite artifact
has the following extent; the infinite languages in DRW-004 and RB-004
are not silently added to these figures.

| First source increment | Retained cells | Covered fraction of that increment class |
|---:|---:|---:|
| 1 | 13 | \(11253377779/521838526464\), approximately 2.16% |
| 2 | 9 | \(1278145/16777216\), approximately 7.62% |
| 3 | 3 | \(7/16\) |
| 4 | 1 | 1, the previously proved DRW-003 cylinder |
| 5 | 1 | \(1/1024\) |
| 6 and higher | 0 | 0 in this finite artifact |

The artifact also lists **341 unresolved residue cells**. To audit the
partition, the checker tests each pair of classes for disjointness using
the exact CRT condition
\((r-s)\not\equiv0\pmod{\gcd(M,N)}\). It then checks that their total
relative density, including unresolved cells, is exactly 1. Because this
is a finite family of periodic sets, their common modulus is finite;
disjointness and total density 1 prove that no odd integer is lost. Any
finite exceptions caused by lower thresholds are checked separately.
There are no such excluded base parameters in the retained packet.

The search processed 128 cells and performed 60 distinct seed searches,
with at most 2,000 heap removals per side of each search, inverse
exponents at most 8, and affine slope cap 10,000. The maximum modulus of
an **attempted partition cell** was 4,096. A discovered word can require
a finer class; the retained certificate moduli are therefore not bounded
by 4,096. Search limits are not part of the proof of a successful cell.
An unresolved search is not a claim that no longer path exists.

The unresolved classes include large parts of the source first-letter
1, 2, 3 and 5 cases. In particular, (2) is not a universal cover. No
finite budget has been presented as a termination argument for the
selector.

## RB-004 — an unbounded conditional ladder and exact length decrease

For every integer \(k\ge3\), suppose

\[
p=\frac{3^{k-3}(27m-1)}{2^{2k+1}}
\quad\text{is a positive integer with }p\equiv3\pmod8.
\tag{3}
\]

Then \(R(p)\Rightarrow R(m)\), and

\[
\frac p m<\frac{27}{128}\left(\frac34\right)^{k-3}
\le\frac{27}{128}<1.
\tag{4}
\]

An exponent with a superscript below denotes repetition of a letter.
The two paths are

\[
\begin{aligned}
27m&\xrightarrow{\ 2^{k-1}\ }72p+1
       \xrightarrow{2}54p+1
       \xrightarrow{1}81p+2
       \xrightarrow K\frac{81p+1}{4}
       \xrightarrow{I_2}27p,\\
9m&\xrightarrow{\ 1,2^{k-1}\ }36p+1
       \xrightarrow K9p
       \xrightarrow M27p.
\end{aligned}
\tag{5}
\]

Here \(M\) invokes just the smaller assertion \(R(p)\). The terminal
ordinary merger \(54p+1\sim27p\) is the known
\(p\equiv3\pmod8\) base class, displayed in full rather than imported
as an unproved tripling law.

**Proof for every \(k\).** Put \(F_a(n)=(3n+1)/2^a\) and
\(D(n)=(n+1)/2\). Direct rational affine calculation gives

\[
F_1(n/3)=D(n),\qquad F_2D=DF_2,\qquad
F_2^j(n)=1+\left(\frac34\right)^j(n-1).
\tag{6}
\]

Equation (3) makes the last expression, at \(n=27m,j=k-1\),
equal to \(72p+1\). It also implies
\(v_2(27m-1)=2k+1\). Therefore all \(k\) displayed initial source
letters 2 are exact, and every intermediate \(D\) value before the
last such letter is positive odd. Commuting \(D\) past the first
\(k-1\) source steps proves the second line's ordinary prefix.
Since \(p\equiv3\pmod8\),

\[
81p+2=J\left(\frac{81p+1}{4}\right),\qquad
U_2(27p)=\frac{81p+1}{4},\qquad36p+1=J(9p)
\]

are all ordinary positive-odd identities. This proves (5). Finally,
expanding (3) as
\(p=(3/4)^{k-1}(3m/8-1/72)\) proves (4).

There is also strict decrease in the supplied odd-witness length. If its
statistics at \(27m\) are \((R,A)\), strip the \(k+1\) source letters,
remove \(J\), and prepend the inverse exponent 2. The resulting supplied
child witness for \(27p\) has

\[
(R_{\rm child},A_{\rm child})=(R-k,A-2k-1).
\tag{7}
\]

If the child solution for \(9p\) has statistics \((L,B)\), lift it by
\(J\) and prepend the target prefix in (5). The reconstructed witness
for \(9m\) has

\[
(L+k,B+2k+1).
\tag{8}
\]

Every endpoint to which a first-increment modification is applied exceeds
1, since \(p\ge3\). Thus neither (7) nor (8) requires an unspecified
nonempty-tail assumption. Terminal padding in the supplied source and
child witnesses is retained exactly.

For each \(k\), (3) specifies one odd residue class modulo
\(2^{2k+4}\); `ladder_cell(k)` computes it by exact modular inverses and
returns a certificate accepted by the same universal verifier. For
example \(k=4\) is \(m\equiv19\pmod{4096}\), with
\(p=(81m-3)/512\). The classes for different \(k\) are disjoint because
\(v_2(27m-1)=2k+1\). Their union has relative density \(1/384\) among
odd \(m\). This union overlaps the finite artifact, so its density is
not added to (2).

The checker verifies the generator identities in (6), the terminal
affine identities, and the full positive-odd cylinder \(p=8u+3\).
The induction above, rather than a finite census of \(k\), proves the
unbounded statement. Additional fixtures at \(k=3,4,5,8\) test the
constructor and the exact statistics (7) and (8).

## Replay and evidence limits

From the repository root, run

```bash
python -B research/witness-global-closure-20261121/check_r_bypass.py
python -O -B research/witness-global-closure-20261121/check_r_bypass.py
```

The checker uses only the Python standard library. Its default writes
no files. Both modes validate all 523 retained affine forms, all 29
conditional-call guards, and the complete certified/unresolved
partition. The finite reconstruction fixtures use bounded trajectory
search only to obtain their explicitly identified source and child
witnesses; the actual transformer never calls that fixture helper.

The replay includes 108 finite-artifact reconstructions, 54 of them with
padded source words and all using padded child answers where applicable;
34 missing-child checks; four additional padded ladder reconstructions;
and rejection controls for false endpoints, false partitions, malformed
witnesses, a reversed conditional arrow, a nondecreasing self-call, and
a wrong child answer.

The `--seed` and `--adaptive` modes expose the bounded exploratory search
and print their output as JSON. They never convert exhaustion into a
negative mathematical result. The retained checkpoint has 341 open
partition cells and leaves the all-source theorem unresolved.
