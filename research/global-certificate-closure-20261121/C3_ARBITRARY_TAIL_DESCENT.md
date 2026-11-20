# An arbitrary-tail descent for the c=3 reverse comparison

**PROPOSED.** This note proves a smaller-query reduction for an unbounded
language of actual source certificates. It does not prove the full reverse
criterion or Collatz. The positive source and its supplied witness remain
fixed throughout.

## 1. Sources and the one global minimum

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd},\end{cases}
\]

and its basin \(C\) of 1. The accelerated odd map is
\(U(n)=(3n+1)/2^{\nu_2(3n+1)}\). An odd witness consists of positive
exponent increments for successive applications of \(U\), ending at 1.

For eligible \(k>0\), \(4\nmid k\), put

\[
X=128k+1,\qquad Y=64k+1.
\]

The following inputs are already proved in the repository:

* PR163, `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
  `research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md`, H1–H2:
  if every reverse implication with upper antecedent less than a given
  \(X\) is available, every \(n<X/176106\) has a finite certificate using
  only such smaller reverse queries. The construction follows the 71
  directed paths and strong induction on positive ternary units. In
  particular, this applies with one globally least failing \(X=X_*\).
* The same pin, `REVERSE_CERTIFICATE_KERNEL.md` and
  `C3_SINGLE_RUN_CERTIFICATES.md`: in the fourth-valuation case \(c=3\),
  \[
  z=U^4(X),\quad z\equiv41\pmod {81},\quad
  X=\frac{512z-175}{81},\quad Y=\frac{256z-47}{81}.
  \tag{1}
  \]
  The source prefix is \((2,2,2,3)\); the target prefix
  \((2,2,2,1)\) ends at \(2z+1\).

This note strengthens the first-block calculation to an arbitrary supplied
tail, with an exact sufficient height guard. It does not assume that the
remaining odd state is 1, bound the remaining rank, or replace the source
by another ordinary integer.

## 2. The source block and an arbitrary tail

Define

\[
a=\nu_2(z+1)\geq1,\quad q=(z+1)/2^a,\quad
e=\nu_2(3^a q-1)\geq1,\quad
w=(3^a q-1)/2^e.
\tag{2}
\]

Then \(q,w\) are positive odd integers and

\[
z=\frac{2^a(2^e w+1)}{3^a}-1.
\tag{3}
\]

The first \(a\) accelerated steps from \(z\) have exact word

\[
(\underbrace{1,\ldots,1}_{a-1},e+1)
\tag{4}
\]

and end at \(w\). Thus stripping (4) from the supplied source witness
gives an actual witness for \(w\), of arbitrary remaining length. For
completeness, if the witness reaches 1 before this block has been fully
written, append exponent-2 loops at 1; this only concerns the degenerate
state \(z=1\), which is excluded by \(z\equiv41\pmod {81}\).

The corresponding \(a\) ordinary shortcut steps from \(2z+1\) all have
odd input and end at

\[
T^a(2z+1)=2\cdot3^a q-1=2^{e+1}w+1.
\tag{5}
\]

In particular, these steps also have accelerated exponent 1, since their
successors are odd. Set

\[
R=\begin{cases}
3^{(e-1)/2}w,&e\text{ odd},\\
2\cdot3^{e/2}w+1,&e\text{ even}.
\end{cases}
\tag{6}
\]

The exact normalizations
\(4^d v+1\sim3^{d-1}v\) and
\(2\cdot4^d v+1\sim2\cdot3^d v+1\), for odd positive \(v\), give

\[
Y\in C\quad\Longleftrightarrow\quad R\in C.
\tag{7}
\]

This is ordinary component equivalence, not a claim that multiplying an
arbitrary certified \(w\) by 3 preserves convergence.

### Explicit witness reconstruction

Let \((d_1,\ldots,d_s)\) be any witness for \(R\). If \(R=1\) and an
empty witness is supplied, first replace it by the one-entry witness
\((2)\).

* If \(e=2b+1\), a witness for \(Y\) is
  \[
  (2,2,2,1),\quad 1^a,\quad 2^b,\quad
  (d_1+2,d_2,\ldots,d_s).
  \tag{8}
  \]
  Here \(1^a\) and \(2^b\) mean repeated increments, not powers. After
  the first two blocks, the value is \(4^{b+1}w+1\). After \(b\)
  exponent-2 steps it is \(4R+1\), whose first exponent is exactly
  \(d_1+2\); its next state equals \(U(R)\).
* If \(e=2b\), a witness for \(Y\) is
  \[
  (2,2,2,1),\quad 1^a,\quad 2^b,\quad(d_1,\ldots,d_s).
  \tag{9}
  \]
  The exponent-2 block now ends exactly at \(R\).

Every intermediate value is positive and odd. These formulas also cover
\(e=1\), when \(R=w\) and the supplied tail alone settles the target.

## 3. Uniform height descent for every positive tail

Write \(H=176106\). The new sufficient condition is

\[
\boxed{e\geq3a+80.}
\tag{10}
\]

Under (10), for every positive odd \(w\) for which (1)–(3) are integral,

\[
\boxed{HR<X.}
\tag{11}
\]

No property of the tail certificate, beyond positivity of \(w\), is used
in this inequality.

**Proof.** Put

\[
B=(2/3)^a2^e w.
\]

Equation (3) gives

\[
X=\frac{512B+512(2/3)^a-687}{81}.
\tag{12}
\]

Condition (10) gives
\(B\geq(16/3)^a2^{80}>2^{80}\). Since
\(26\cdot2^{80}>687\), (12) implies

\[
X>6B.
\tag{13}
\]

For odd \(e\), (6) immediately implies
\(R\leq(9/4)3^{e/2}w\). For even \(e\), condition (10) gives
\(3^{e/2}w\geq4\), and hence the same bound follows from
\(2t+1\leq(9/4)t\). Therefore

\[
\begin{aligned}
\left(\frac{HR}{X}\right)^2
&<\left(\frac{3H}{8}\right)^2
   (3/2)^{2a}(3/4)^e\\
&=\left(\frac{3H}{8}\right)^2
   (243/256)^a(3/4)^{e-3a}\\
&\leq\left(\frac{528318}{8}\right)^2
   (243/256)(3/4)^{80}<1.
\end{aligned}
\tag{14}
\]

The final strict inequality has the short integer certificate

\[
3^5=243<256=4^4,
\qquad 528318^2\cdot243<2^{46}.
\tag{15}
\]

Indeed, the first inequality gives
\((3/4)^{80}<2^{-32}\); substitution reduces the last step of (14)
to the second inequality of (15). This proves (11).

## 4. Actual sources at every positive tail rank

The language above is nonempty at every prescribed positive tail rank,
even after fixing any \(a\geq1\) and \(e\geq3a+80\). Here is an explicit
ordinary construction, using the family of PR166,
`5996b9f525ca50978bc34f423192c36a87765bf3`,
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`,
FL4. Its rank-one case below is the direct elementary extension \(r=0\).

For \(r\geq0\) and \(h\geq1\), set

\[
w_{r,h}=1+\frac{4^{r+1}(4^{3^r h}-1)}{3^{r+1}}.
\tag{17}
\]

Its exact first-hit witness is

\[
(\underbrace{2,\ldots,2}_{r},\ 2+2\cdot3^r h),
\tag{18}
\]

so its tail rank is exactly \(r+1\), with no terminal padding. All
preterminal values exceed 1. Integrality follows from
\(\nu_3(4^n-1)=1+\nu_3(n)\), which follows by factoring when \(3\nmid n\)
and applying the binomial expansion once per factor of 3.

For fixed \(r\), the map \(h\mapsto w_{r,h}\) permutes the residues
modulo every power \(3^L\). Indeed, for distinct nonnegative \(h,h'\),
the same valuation identity gives

\[
\nu_3(w_{r,h}-w_{r,h'})=\nu_3(h-h').
\tag{19}
\]

Thus the induced map on the \(3^L\) residue classes is well-defined and
injective, hence bijective. The auxiliary value \(h=0\) is used only for
this residue calculation; actual witnesses always use \(h>0\).

Take \(L=a+4\), and select the unique class of \(h\) modulo \(3^L\)
for which

\[
w_{r,h}\equiv
2^{-e}\bigl(3^a\cdot42\cdot2^{-a}-1\bigr)
\pmod {3^{a+4}}.
\tag{20}
\]

Here \(2^{-e}\) is the inverse modulo \(3^{a+4}\), and \(2^{-a}\)
may be taken modulo 81 inside its displayed product. Equation (20) gives

\[
q=\frac{2^e w_{r,h}+1}{3^a}\equiv42\cdot2^{-a}\pmod {81},
\qquad z=2^a q-1\equiv41\pmod {81}.
\tag{21}
\]

The selected residue of \(w\) is a ternary unit. Since \(e\geq1\),
the integral \(q\) is odd, so \(a=\nu_2(z+1)\) and
\(e=\nu_2(3^a q-1)\) are exact. Positivity follows from the large-gap
guard. Formula (1) now supplies an eligible actual source \(X\), with
the source prefix (4) and the explicit tail (18).

There are infinitely many positive \(h\) in the selected class, and their
strictly increasing values of \(w\) give infinitely many distinct
ordinary sources. Therefore, for every fixed \(a\geq1\), every fixed
\(e\geq3a+80\), and every prescribed positive tail rank, infinitely many
actual certified sources satisfy the new guard. Rank-zero tails require
\(w=1\) and are not asserted for every fixed pair \((a,e)\).

## 5. Two exact conclusions

### One globally least failure

Suppose \(X=X_*\) is the globally least eligible failing antecedent.
The same \(X_*\) is used in (1), (11), and H2. Under (10), H2 certifies
\(R\), and (8) or (9) then certifies \(Y\), a contradiction. Consequently

\[
\boxed{
\text{A least failure with }c=3\text{ must have }
e\leq3a+79,\text{ and it cannot have }e=1.
}
\tag{22}
\]

This excludes an infinite, unbounded-rank certificate language with
arbitrary remaining tails. It is stronger in scope than an exclusion
restricted to \(w=1\), but does not cover the whole \(c=3\) family.

### A smaller-reverse-query compiler

For any fixed eligible \(X\) with its supplied witness, assume an oracle
that transforms witnesses under all eligible reverse implications whose
upper antecedent is strictly below \(X\). The H1–H2 construction produces
a witness for every \(n<X/H\) using only finitely many calls to that
oracle. All calls have actual upper antecedent less than \(X\); their
ordinary intermediate heights need not be less than \(X\).

Under (10), call that construction at the explicit integer \(R\) in
(6), then use (8) or (9). This returns the requested witness for \(Y\)
from smaller reverse instances. The call tree is finite because the unit
descent contracts by at most \(24/25\) at each stage, with halving and the
one-step conversion from multiples of 3 handled exactly as in H2. This is
a conditional compiler, not an unconditional termination proof for every
eligible source.

## 6. Certificate resource exchange beyond the height guard

There is a second exact transformation, whose missing closure is recorded
because it is relevant to a possible joint induction. Assume \(a\geq4\),
and let the supplied witness for \(w\) have rank \(r_w\) and final
exponent \(A_w\). From (2),

\[
2^e w\equiv-1\pmod {81},\qquad 2^{27}\equiv-1\pmod {81}.
\]

Consequently

\[
m=\frac{2^{e+27}w-1}{81}
\tag{23}
\]

is a positive odd integer, and \(27m\) has the known witness
\((e+27)\) followed by the supplied witness of \(w\). The eligible
antecedent \(X'=256m+1\) therefore has a known witness of rank
\(r_w+4\) and final exponent

\[
A'=A_w+e+35.
\tag{24}
\]

The original supplied source witness has

\[
r=r_w+a+4,\qquad A=A_w+a+e+9.
\]

Thus

\[
\boxed{r'=r-a,\qquad A'=A+26-a.}
\tag{25}
\]

In particular, \(a\geq27\) strictly lowers the known source exponent,
even though \(X'\) is larger than \(X\).

The reverse implication at \(X'\) is \(P(m)\). If available, it gives
the canonical target

\[
R'=\begin{cases}
3^{(e+25)/2}w,&e\text{ odd},\\
2\cdot3^{(e+26)/2}w+1,&e\text{ even}.
\end{cases}
\tag{26}
\]

In the canonical levels of PR164,
`6fa6b429870a9cd53cde0fc77ad64a3c3956199f`,
`continuation-descent.md`, this is exactly **26 levels above** (6).
The 26 successive downward \(P/Q\) implications would reach \(R\),
provided their levels remain in that mechanism's domain. The endpoint
level is \(e-1\), so this requires \(e\geq5\); the already solved case
\(e=1\) is separate, and \(e=2,3,4\) is not covered by this downward
chain.

**Unresolved inference.** Formula (25) does not supply a well-founded
global induction: the first returned target witness can have an
uncontrolled final exponent, and subsequent downward calls cannot be
declared smaller on the strength of (25). Nor does the least-value
argument apply to \(X'\), which is larger. No bound on those returned
witnesses or all-input completion of this exchange is claimed here.

## 7. Replay

Run `check_c3_arbitrary_tail.py` normally and with `python3 -OO`.
The checker uses explicit exceptions rather than removable `assert`
statements. It checks the exact integer inequalities, positive odd affine
prefixes, arbitrary-tail witness composition on concrete independently
certified instances, the height guard on both parities with nontrivial
tails, the residue construction at prescribed positive tail ranks, and the
certificate exponent/rank exchange. The infinite claims
come from the displayed identities and monotonic inequalities, not from
the finite sample count. The H1–H2 height constant remains a separately
pinned dependency with its own exact 71-path replay.
