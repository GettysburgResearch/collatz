# A partial proof packet for the 512-residue witness closure

**Main claim: OPEN in this note.** This packet proves several exact reductions,
infinite merger families, and descending recurrences. It does not prove or
disprove the full implication stated below. The accompanying Python replay is
finite executable evidence; it is not formal verification or a substitute for
the algebraic proofs.

The dependencies of this note are the supplied witness definition and direct
integer algebra. No earlier research history, computational convergence bound,
or external theorem about Collatz convergence is assumed.

## Continuation results

The subsequent [direct reverse-tripling packet](../witness-global-closure-20261121/README.md)
reviews the newer repository criterion, independently reconstructs its
equivalence with this exact 512-residue assertion, and adds complete-witness
rewrites, least-failure bounds and conditional descending certificates.
Its source-qualified global equivalence uses PR146's finite cover; the
standalone integer-algebra dependencies of the original results below are
unchanged. The full assertion remains OPEN.

The following notes extend this packet without changing the OPEN status of
the main claim:

* [Complete-witness transfer between two seed pairs](continuation-algebra.md)
  proves an exact smaller-parameter reduction for
  `M > 3`, `M = 3 mod 2^121`: replace `M` by `(M+4011)/2`.
  [The strengthened prefix argument](continuation-j.md) lowers the required
  modulus to `2^119`.
  The supplied source witness keeps its length and loses one unit of total
  exponent. The implementation validates both prefix identities and reconstructs
  the original target only when the smaller target witness is available.
* [Two exact parameter contractions](continuation-negative.md) prove
  `C(M) <=> C((128M-69)/243)` for `M = 292863 mod 497664`, and
  `C(M) <=> C((512M-271)/729)` for `M = 774143 mod 1492992`.
  Both child parameters are positive and strictly smaller. The proofs and
  [standalone replay](verify_negative.py) give exact source and target witness
  conversions for both classes. The first rule is also included in the main
  verifier's recursive dispatcher.
* [Removing redundant J steps](continuation-j.md) doubles the parameter
  classes of the Q95 and P1215 descents to `m = 95 mod 256` and
  `m = 1215 mod 16384`, respectively, and proves the stronger seed-pair
  transfer just described.
* [General descent from a certified base pair](continuation-descent.md)
  gives an explicit precision threshold and a finite list of smaller P/Q
  premises. [The detailed parameter-one construction](continuation-lift.md)
  gives the fifteen-call specialization near `M=1`.
* [Global closure identities and a further merger](continuation-closure.md)
  proves `3n in E <=> n in E` for `n = 187 mod 256`, with explicit
  unequal-length prefixes. It also derives precise conditional consequences
  of the full P/Q assertion and proves a separate equivalence for global
  multiplication-by-three closure. It does not identify that stronger
  closure with the original claim.

These are proved transfer and induction rules, not a proof that their recursive
premises or their parameter classes cover every input.

## 1. The problem and the claim register

For a positive integer \(x\), define \(x\in E\) to mean that there are integers
\(r\geq0\) and

\[
0=A_0<A_1<\cdots<A_r
\]

such that

\[
\boxed{
3^r x+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r}.
}
\tag{1}
\]

For \(r=0\), the sum is empty, so (1) means \(x=1\). This is the mathematical
identity supplied in the problem; it is the definition used throughout.

The requested closure assertion is

\[
\boxed{
x\in E,\qquad x\bmod512\in\{129,257,385\}
\quad\Longrightarrow\quad
\frac{x+1}{2}\in E.
}
\tag{2}
\]

The output witness in (2) may have any finite length and any strictly increasing
exponents. No bound comparing its length or exponents to the supplied witness
is part of the assertion.

`PROVED-IN-NOTE` means that an integer-algebra proof is included here. It does
not mean that a proof assistant has checked the statement.

| Claim ID | Status | Exact scope |
|---|---|---|
| W512-001 | OPEN | The full implication (2). |
| W512-010 | PROVED-IN-NOTE | Equivalence of (1) with a finite accelerated odd trajectory ending at 1. |
| W512-011 | PROVED-IN-NOTE | Concatenating witnesses and padding a witness by the loop at 1. |
| W512-012 | PROVED-IN-NOTE | \(J(z)=4z+1\) preserves membership in \(E\) for positive odd \(z\). |
| W512-013 | PROVED-IN-NOTE | The two exact \(4^k\) normalization identities in Section 2. |
| W512-020 | PROVED-IN-NOTE | Equivalence of (2) with both \(P(m)\) and \(Q(m)\) for every positive odd \(m\). |
| W512-030 | PROVED-IN-NOTE | Five-step merger for \(x=128M+1\), \(M\equiv6\pmod{16}\). |
| W512-031 | PROVED-IN-NOTE | Six-step merger for \(x=128M+1\), \(M\equiv35\pmod{128}\). |
| W512-032 | PROVED-IN-NOTE | Seven-step merger for \(x=128M+1\), \(M\equiv401\pmod{1024}\). |
| W512-033 | PROVED-IN-NOTE | The \(k+5\)-step merger family in Section 4, for every integer \(k\geq1\) satisfying its congruence. |
| W512-034 | PROVED-IN-NOTE | Conversion of any supplied source witness into a target witness when one of the stated mergers applies. |
| W512-040 | PROVED-IN-NOTE | Descending reduction of \(Q(m)\) for \(m\equiv19\pmod{128}\), including even intermediate \(h\). |
| W512-041 | PROVED-IN-NOTE | Descending reduction of \(Q(m)\) for \(m\equiv95\pmod{512}\), including even intermediate \(h\). |
| W512-042 | PROVED-IN-NOTE | Descending reduction of \(P(m)\) for \(m\equiv1215\pmod{32768}\), including even intermediate \(h\). |

## 2. Witnesses, trajectories, and elementary identities

For positive odd \(n\), write

\[
T(n)=\frac{3n+1}{2^{\nu_2(3n+1)}}.
\]

A displayed list \([a_1,\ldots,a_s]\) below specifies exact successive
valuations \(a_i=\nu_2(3n_{i-1}+1)\), not merely a list of divisions that leave
integers.

### W512-010: the witness determines the odd trajectory

Suppose (1) holds. For \(0\leq i\leq r\), put

\[
N_i=3^i x+\sum_{j=0}^{i-1}3^{i-1-j}2^{A_j},
\qquad n_i=\frac{N_i}{2^{A_i}}.
\]

Reducing (1) modulo \(2^{A_i}\) shows that
\(3^{r-i}N_i\) is divisible by \(2^{A_i}\). Since 3 is odd, \(n_i\) is an
integer. All its defining summands are positive, so \(n_i>0\). Also,

\[
3n_{i-1}+1=2^{A_i-A_{i-1}}n_i,
\qquad n_r=1.
\]

Every \(n_i\) is odd: for \(i<r\), an even \(n_i\) would make
\(3n_i+1\) odd, contrary to the next displayed equation and
\(A_{i+1}-A_i\geq1\); \(n_r=1\) is odd as well. Consequently,

\[
A_i-A_{i-1}=\nu_2(3n_{i-1}+1),\qquad n_i=T(n_{i-1}).
\]

Conversely, unrolling any finite odd trajectory from \(x\) to 1 gives (1).
In particular, every element of \(E\) is odd. A supplied witness follows the
unique odd trajectory, with any extra steps occurring after the first arrival
at 1.

### W512-011: concatenation and padding

If a prefix from \(x\) to \(z\) has length \(p\) and cumulative exponents
\(A_0,\ldots,A_p\), and a witness from \(z\) to 1 has length \(q\) and
cumulative exponents \(B_0,\ldots,B_q\), their concatenation has exponents

\[
C_i=A_i\quad(0\leq i\leq p),\qquad
C_{p+j}=A_p+B_j\quad(1\leq j\leq q).
\tag{3}
\]

This follows either by substituting the second identity into the first, or
from the exact trajectory just proved. Since \(3\cdot1+1=2^2\), a witness
can be extended by any number of terminal steps of exponent 2.

### W512-012: the \(J\) identity

For positive odd \(z\), let \(J(z)=4z+1\). Then

\[
3J(z)+1=4(3z+1),\qquad T(J(z))=T(z).
\tag{4}
\]

Thus \(J(z)\in E\) if and only if \(z\in E\). For a nonempty witness, the
conversion from \(z\) to \(J(z)\) adds 2 to the first exponent; the reverse
conversion subtracts 2. For the zero-length witness at \(z=1\), first pad by
the exponent-2 loop. This oddness restriction matters: (4) is not a license
to replace an arbitrary even \(z\) by \(J(z)\) in a convergence assertion.

### W512-013: normalization of powers of four

For positive odd \(z\) and \(k\geq1\),

\[
T^{k-1}(4^kz+1)=4\cdot3^{k-1}z+1=J(3^{k-1}z),
\]

so

\[
\boxed{4^kz+1\in E\quad\Longleftrightarrow\quad3^{k-1}z\in E.}
\tag{5}
\]

For positive odd \(z\) and \(k\geq0\),

\[
\boxed{T^k(2\cdot4^kz+1)=2\cdot3^kz+1.}
\tag{6}
\]

All the steps explicitly taken in these formulas have exponent 2: whenever
the coefficient of the odd \(z\) contains at least \(2^3\),

\[
T(2^e z+1)=2^{e-2}(3z)+1\qquad(e\geq3).
\]

The remaining application of (4) in (5) is made to an odd integer.

## 3. W512-020: an exact pair of conditional assertions

For positive odd \(m\), define

\[
P(m):\quad27m\in E\Longrightarrow54m+1\in E,
\]

\[
Q(m):\quad54m+1\in E\Longrightarrow9m\in E.
\tag{7}
\]

The full claim W512-001 is equivalent to the assertion that **both** \(P(m)\)
and \(Q(m)\) hold for **every** positive odd \(m\).

To prove this, write \(x=128M+1\). The specified residues are exactly the
positive \(M\) with \(M\not\equiv0\pmod4\).

* If \(M=m\) is odd, three exponent-2 steps send \(x\) to \(54m+1\).
  Two exponent-2 steps send \((x+1)/2=64m+1\) to
  \(36m+1=J(9m)\). Thus this case of (2) is exactly \(Q(m)\).
* If \(M=2m\) with \(m\) odd, three exponent-2 steps send
  \(x=256m+1\) to \(108m+1=J(27m)\), and three exponent-2 steps send
  \((x+1)/2=128m+1\) to \(54m+1\). Thus this case is exactly \(P(m)\).

Conversely, each positive odd \(m\) produces allowed source integers in both
of these constructions. The reduction therefore loses no case of the problem.

## 4. Exact merger families

Throughout this section,

\[
x=128M+1,\qquad y=64M+1=\frac{x+1}{2}.
\]

Each result identifies a common odd value after the same finite number of odd
steps. It therefore proves \(x\in E\Longleftrightarrow y\in E\) on its
stated class. The resulting witness construction is given in Section 5.

### W512-030: \(M\equiv6\pmod{16}\)

Put

\[
u=\frac{81M+2}{8},\qquad \lambda=\nu_2(3u+1).
\]

The exact five-step prefixes are

\[
\begin{array}{c|c}
\text{source }x&[2,2,2,4,\lambda]\\
\text{target }y&[2,2,2,1,\lambda+2].
\end{array}
\tag{8}
\]

After their first three steps, the values are \(54M+1\) and \(27M+1\).
The next steps give \(u\) and \(4u+1\), respectively, and (4) gives the
common fifth value \(T(u)\). For \(M=16t+6\), \(u=162t+61\) is odd and
all the displayed valuations are exact. In terms of \(x\), this class is
\(x\equiv769\pmod{2048}\).

### W512-031: \(M\equiv35\pmod{128}\)

Put

\[
n=\frac{27M+1}{2},\qquad G=81M+2,\qquad
u=\frac{243M+7}{64},\qquad \lambda=\nu_2(3u+1).
\]

The exact six-step prefixes are

\[
\begin{array}{c|c}
x&[2,2,2,1,6,\lambda]\\
y&[2,2,3,2,1,\lambda+2].
\end{array}
\tag{9}
\]

Here \(T^4(x)=G\), \(T^3(y)=n\), \(T(G)=u\), and
\(T^2(n)=4u+1\). For \(M=128t+35\), the last pair is

\[
u=486t+133,\qquad T^2(n)=1944t+533=4u+1.
\]

The next step merges by (4). This gives
\(x\equiv4481\pmod{16384}\), a subfamily of the original residue
\(385\pmod{512}\).

### W512-032: \(M\equiv401\pmod{1024}\)

Put

\[
n=\frac{27M+1}{4},\qquad G=81M+2=12n-1,\qquad
u=\frac{27n-1}{128},\qquad \lambda=\nu_2(3u+1).
\]

The exact seven-step prefixes are

\[
\begin{array}{c|c}
x&[2,2,2,1,1,8,\lambda]\\
y&[2,2,4,1,3,1,\lambda+2].
\end{array}
\tag{10}
\]

In this class \(n\equiv147\pmod{256}\). Its first three exponents are
\([1,3,1]\), while those of \(G\) are \([1,8]\). Directly,

\[
T^2(G)=\frac{27n-1}{128}=u,
\qquad
T^3(n)=\frac{27n+31}{32}=4u+1.
\]

After the final step the paths merge by (4). This gives
\(x\equiv51329\pmod{131072}\), a subfamily of the original residue
\(129\pmod{512}\).

### W512-033: an infinite family indexed by \(k\)

Let \(k\geq1\), and suppose

\[
\boxed{
27M+2\equiv3^k2^{k+2}\pmod{2^{k+4}}.
}
\tag{11}
\]

Equivalently, write

\[
27M+2=2^{k+2}h,
\qquad h\text{ odd},\qquad h\equiv3^k\pmod4.
\]

This implies \(M\equiv2\pmod8\), so these are allowed source integers.
Set

\[
u=\frac{81M+2}{4},\qquad
q=\frac{3^{k+1}h-1}{2},\qquad
\lambda=\nu_2(3q+1).
\]

Then \(q\) is a positive odd integer, and the exact prefixes of length
\(k+5\) are

\[
\begin{array}{c|c}
x&[2,2,2,3,\underbrace{1,\ldots,1}_{k-1},2,\lambda]\\
y&[2,2,2,1,\underbrace{1,\ldots,1}_{k},\lambda+2].
\end{array}
\tag{12}
\]

An empty block of ones when \(k=1\) is omitted.

For the proof, the first four steps give \(u\) and \(2u+1\), and

\[
u+1=2^k(3h).
\]

Starting with \(2^kw-1\), the first \(k-1\) odd steps have exponent 1 and
give \(2\cdot3^{k-1}w-1\). If \(3^kw\equiv3\pmod4\), the next
exponent is exactly 2 and the result is \((3^kw-1)/2\). Starting instead
with \(2^{k+1}w-1\), the first \(k\) exponents are 1 and the result is
\(2\cdot3^kw-1\), which is four times the former result plus 1.

Take \(w=3h\). The required congruence holds because
\(3^{k+1}h\equiv3^{2k+1}\equiv3\pmod4\). The two values are therefore
\(q\) and \(4q+1\), and their next step merges by (4).

For example, (11) starts with
\(M\equiv2\pmod{32}\) at \(k=1\),
\(M\equiv10\pmod{64}\) at \(k=2\), and
\(M\equiv122\pmod{128}\) at \(k=3\).
The proof covers every \(k\geq1\); a finite replay can only test finitely
many such instances.

## 5. W512-034: splicing an arbitrary supplied witness

Suppose one of (8)--(12) gives a merger after \(L\) odd steps. Let
\(A_0,\ldots,A_r\) be the supplied source witness. If \(r<L\), extend it
by terminal exponent-2 steps at 1 until \(r\geq L\). By W512-010, its first
\(L\) steps are the forced source prefix in the applicable merger result.

Let \(B_0=0,B_1,\ldots,B_L\) be the cumulative exponents of the target
prefix, and extend them by

\[
\boxed{B_j=B_L+A_j-A_L\qquad(L\leq j\leq r).}
\tag{13}
\]

The two prefixes have the same endpoint. Therefore (13) appends the supplied
source tail to the target prefix, exactly as in (3), and gives

\[
3^r y+\sum_{j=0}^{r-1}3^{r-1-j}2^{B_j}=2^{B_r}.
\]

All increments of \(B\) are positive. This construction uses the actual
supplied witness; it does not infer target convergence from a numerical test
of a representative of the residue class.

## 6. Descending recurrences for \(P\) and \(Q\)

These are conditional induction steps. A row reducing \(Q(m)\) to \(P(p)\)
proves \(P(p)\Rightarrow Q(m)\); it does not assert \(P(p)\) without a
proof. Each parameter \(p\) below is positive, odd, and strictly smaller
than \(m\).

### W512-040: \(Q(m)\) for \(m\equiv19\pmod{128}\)

Define

\[
h=\frac{27m-1}{128}=2^b u,\qquad u\text{ odd},\qquad
p=3^{\lfloor b/2\rfloor}u.
\]

The exact source and target prefixes are

\[
T^3(54m+1)=\frac{729m+37}{64}=54h+1
\quad\text{with }[1,4,2],
\]

\[
T^3(9m)=\frac{243m+23}{32}=36h+1
\quad\text{with }[1,2,2].
\tag{14}
\]

Thus the remaining implication is
\(54h+1\in E\Rightarrow36h+1\in E\).

* If \(b=2s\), take \(s\) exponent-2 steps on each side. The resulting
  pair is \(54p+1\) and \(36p+1=J(9p)\). Hence \(Q(p)\) proves
  \(Q(m)\).
* If \(b=2s+1\), take \(s\) such steps on the source and \(s+1\) on the
  target. The pair is \(108p+1=J(27p)\) and \(54p+1\). Hence \(P(p)\)
  proves \(Q(m)\).

All uses of \(J\) now have odd arguments. Also

\[
1\leq p\leq h=\frac{27m-1}{128}<m.
\]

This includes even \(h\). Restricting prematurely to odd \(h\) would retain
only the smaller class \(m\equiv147\pmod{256}\).

There is exact witness bookkeeping as well. If the given source witness has
length \(R\) and final exponent \(A\), and the smaller assertion supplies
an output witness of length \(L\) and final exponent \(B\), then:

| Parity of \(b\) | Witness supplied to the smaller assertion | Witness constructed for \(9m\) |
|---|---|---|
| \(b=2s\) | Source \(54p+1\): length \(R-3-s\), final exponent \(A-7-2s\). | Length \(L+3+s\), final exponent \(B+7+2s\). |
| \(b=2s+1\) | Source \(27p\): length \(R-3-s\), final exponent \(A-9-2s\). | Length \(L+4+s\), final exponent \(B+7+2s\). |

The recursive source witness is strictly shorter. The output witness is
allowed to be longer.

### W512-041: \(Q(m)\) for \(m\equiv95\pmod{512}\)

Define

\[
h=\frac{27m-5}{512}=2^b u,\qquad u\text{ odd},\qquad
p=3^{\lceil b/2\rceil}u.
\]

The exact prefixes give

\[
T^3(54m+1)=\frac{729m+25}{32}=432h+5=J^2(27h)
\quad\text{with }[1,2,3],
\]

\[
T^4(9m)=\frac{729m+121}{256}=54h+1
\quad\text{with }[1,1,4,2].
\tag{15}
\]

The outer \(J\) may be removed because its argument \(J(27h)\) is odd.
The remaining pair is therefore \(108h+1\) and \(54h+1\).

* If \(b=2s\), take \(s\) exponent-2 steps on both sides. The pair becomes
  \(J(27p)\) and \(54p+1\); \(P(p)\) proves \(Q(m)\).
* If \(b=2s+1\), take \(s+1\) such steps on the source and \(s\) on the
  target. The pair becomes \(54p+1\) and \(J(9p)\); \(Q(p)\) proves
  \(Q(m)\).

Here

\[
p\leq\frac32h=\frac{81m-15}{1024}<m.
\]

The source witness supplied to the smaller assertion is shorter by \(3+s\)
steps in the even case and \(4+s\) steps in the odd case. All the reversed
\(J\) operations have odd positive arguments greater than 1, so they preserve
the witness length and only subtract 2 from a first exponent.

### W512-042: \(P(m)\) for \(m\equiv1215\pmod{32768}\)

Define

\[
h=\frac{243m-333}{32768}=2^b u,\qquad u\text{ odd},\qquad
p=3^{\lceil b/2\rceil}u.
\]

For \(m=1215+32768t\), \(h=9+243t>0\). The exact prefixes are

\[
T^5(27m)=\frac{6561m+1249}{2048}=432h+5=J^2(27h)
\quad\text{with }[4,1,1,2,3],
\]

\[
T^5(54m+1)=\frac{13122m+14786}{32768}=54h+1
\quad\text{with }[1,2,8,2,2].
\tag{16}
\]

The remaining pair is the same pair as in (15). Consequently:

* If \(b=2s\), \(P(p)\) proves \(P(m)\), with \(p=3^s u\).
* If \(b=2s+1\), \(Q(p)\) proves \(P(m)\), with \(p=3^{s+1}u\).

The normalization is exactly the odd-argument \(J\) removal and the
exponent-2 steps used for W512-041, so even \(h\) is included. Moreover,

\[
p\leq\frac32h=\frac{729m-999}{65536}<m.
\]

The source witness supplied to the smaller assertion is shorter by \(5+s\)
steps in the even case and \(6+s\) steps in the odd case. The intermediate
odd sources to which \(J\) is reversed are at least 27; no first-arrival-at-1
exception occurs.

## 7. Executable replay and its limits

The companion [verify.py](verify.py) can be replayed from the repository root:

```sh
python3 research/witness-closure-512-2026-11-20/verify.py
```

The same replay can be run with Python assertions disabled:

```sh
python3 -O research/witness-closure-512-2026-11-20/verify.py
```

The script's emitted result is the authority for which fixtures it actually
checks and whether that particular execution succeeds. Its scope is finite checks of
affine identities, exact exponents, witness reconstruction, merger instances,
and implemented descending reductions. In particular:

* Testing finitely many \(M\) or \(k\) does not establish universal coverage.
* An exact rational affine identity checks an algebraic formula, not every
  congruence condition or every unimplemented branch of a closure argument.
* An unsupported residual case must remain `UNRESOLVED`; it is neither a
  successful witness conversion nor a counterexample to W512-001.
* The universal scopes claimed above rest on the proofs in this note. A
  finite replay is useful corroboration and an implementation check.

The extended verifier was run independently by its author and the integrating
agent in normal and optimized Python. Both modes returned identical `PASS`
JSON. It checks all three fixed certificates, the k-family schema, the original
and strengthened P/Q descents, the four CA-003 seed witnesses, its strengthened
J transfers, and the first contraction from `continuation-negative.md`.
Finite reconstruction checks comprise 41 transformed fixtures, five Q19
cases, thirteen Q95/P1215 cases, four CA-003 cases, and four negative-template
cases. The old Q95/P1215 and CA-003 subsets are checked independently.
Eleven malformed witnesses, 25 invalid certificates or reconstructions, and
16 incomplete forced-prefix witnesses are rejected. Five nonminimal source
witnesses and five nonminimal child target witnesses check terminal padding;
two source and two target round trips check the reversible transfers.

The independent [verify_negative.py](verify_negative.py) replay checks both
contraction families. It reports sixteen complete prefix parity certificates,
twelve source and twelve target reconstructions, and four malformed-witness
rejections. It also passes normally and with Python assertions disabled.

Unsupported recursive children remain `UNRESOLVED`, and both scripts explicitly
report `full_claim: UNRESOLVED`. These counts are not a convergence bound or an
exhaustive coverage claim.

## 8. The unresolved proof obligation

The merger classes in Section 4 are sufficient classes, not an exhaustive
partition of the three original residue classes. The descending rules in
Section 6 prove valid steps for a simultaneous induction on \(P\) and \(Q\),
but this note does not show that every positive odd parameter is dispatched
by those rules or by a proved base case.

To close W512-001 by this approach, one still needs a complete argument that
establishes both implications in

\[
27m\in E\quad\Longrightarrow\quad54m+1\in E
\quad\Longrightarrow\quad9m\in E
\]

for every positive odd \(m\), or a different complete construction of the
target witness from the supplied source witness. Neither a counterexample
nor such a complete construction is supplied here. W512-001 remains OPEN.
