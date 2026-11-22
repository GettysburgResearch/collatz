# Ordinary integrality, periodic shadows, and the full local-factor budget

**Full Collatz: OPEN. New arithmetic statements: PROPOSED with complete written
proofs; formal coverage is specified below.** This attempt uses the forced band
to seek an arithmetic contradiction for one fixed ordinary source. It gives an
exact obstruction to the direct Subspace-Theorem argument, including every
fixed finite collection of independently encoded returns. A different route,
through periodic shadows, gives an exact repetition certificate, but its
universal coverage remains unproved.

The normalization is

\[
T(n)=\begin{cases}n/2&n\equiv0\pmod2,\\(3n+1)/2&n\equiv1\pmod2,\end{cases}
\qquad U(x)=(3x+1)/2^{v_2(3x+1)}.
\]

The section and odd-orbit identities are frozen at PR 183,
`8659cf62ac685540cadeef320e596c852fbb0959`, using its byte-pinned PR 173 inputs
at `fa0c9e2a2851e6324391e39c17afcb5913185aec`. For an odd positive integer
\(x\), with \(d=\lfloor\log_2x\rfloor\), the section is

\[
D=\{x:(d+1)(x-2^d)\le70\,2^d\}.
\]

Every positive orbit enters this section. The source already proves that
first returns can expand arbitrarily; PR 183 proves that its particular
uniform short-return certificates do not cover all ordinary sources. This
note does not reclassify either result as new.

## 1. The intended global contradiction

Fix an ordinary positive odd source \(n\). Suppose it never reaches one.
The section theorem supplies infinitely many marked visits if the orbit is
unbounded; a nontrivial cycle also has marked visits. At such a visit,

\[
x_j=2^{d_j}+u_j,\qquad
0\le u_j\le\frac{70\,2^{d_j}}{d_j+1}.
\]

The tempting arithmetic step is to combine this small relative real error
with the large powers of two and three in the exact orbit formula, and invoke
the Subspace Theorem. The calculation below tests the complete product required
by that theorem. The result is stronger than the observation that the band
narrows slowly: for this natural fixed system of linear forms, the product
is exactly the integer \(u_j\). It never becomes small at a nontrivial odd
endpoint, even when \(u_j=1\).

## 2. Exact carry and its missing factor of three

Write

\[
x_0=n,\quad x_{j+1}=U(x_j),\quad
a_j=v_2(3x_j+1),\quad A_j=\sum_{i<j}a_i.
\]

Define an ordinary integer carry by

\[
B_0=0,\qquad B_{j+1}=3B_j+2^{A_j}.
\]

**AR-1.** For every \(j\ge0\),

\[
2^{A_j}x_j=3^j n+B_j.\tag{1}
\]

For every \(j>0\), \(B_j>0\) and \(3\nmid B_j\).

**Proof.** Multiply \(2^{a_j}x_{j+1}=3x_j+1\) by \(2^{A_j}\), and use (1)
at clock \(j\). This gives the stated recurrence and induction. The last
summand in \(B_{j+1}\) is a power of two, so reduction modulo three gives
\(B_{j+1}\equiv2^{A_j}\not\equiv0\pmod3\). Positivity is immediate.

This is the ordinary affine form underlying PR 183's logarithmic identity.
Both \(A_j\) and \(B_j\) belong to the actual source orbit. They cannot be
chosen independently to improve the estimate.

## 3. The three-place product is exactly the offset

Fix a positive odd clock \(j\), set \(A=A_j\), and suppose
\(x_j=2^d+u\) with \(d=\lfloor\log_2x_j\rfloor\). Use the primitive integer
vector

\[
\mathbf z=(X,Y,Z)=(3^j,2^{A+d},B_j).
\]

It is primitive because \(\gcd(X,Y)=1\). In particular, there is no common
integer content whose removal can improve its projective height. Choose the
following forms, whose coefficients remain fixed while \(j\) varies:

| Place | First form | Second form | Third form |
|---|---|---|---|
| \(\infty\) | \(X\) | \(Y\) | \(nX+Z-Y\) |
| \(2\) | \(X\) | \(Y\) | \(nX+Z\) |
| \(3\) | \(X\) | \(Y\) | \(Z\) |

Every row consists of three linearly independent forms: each coefficient
matrix has determinant one. Thus the issue is the size inequality, not a
failure of the rank hypothesis.

Use \(|p|_p=p^{-1}\). The real error and the local factors are exact:

\[
nX+Z-Y=2^A u,
\]

\[
\begin{aligned}
\prod_{i=1}^3|L_{i,\infty}(\mathbf z)|
  &=3^j\,2^{A+d}\,2^A u,\\
\prod_{i=1}^3|L_{i,2}(\mathbf z)|_2
  &=2^{-(A+d)}\,2^{-A},\\
\prod_{i=1}^3|L_{i,3}(\mathbf z)|_3
  &=3^{-j}.
\end{aligned}
\]

The second equality uses that \(x_j\) is odd; the third uses
\(3\nmid B_j\). Consequently:

**AR-2.** The complete unnormalized local-factor product is

\[
\boxed{\quad
\prod_{v\in\{\infty,2,3\}}\prod_{i=1}^3
 |L_{i,v}(\mathbf z)|_v=u.\quad}\tag{2}
\]

At every odd endpoint \(x_j>1\), \(u\ge1\): the only odd nonnegative
integer that is a power of two is one. Thus the product in (2) is at least
one. Markedness is not needed for the identity; it only supplies an upper
bound on \(u\).

### Comparison with the exact theorem hypothesis

Theorem E in Adamczewski–Bugeaud [AB07, p. 555] requires a fixed finite set of
places and full-rank forms, with the normalized product at most
\(H(\mathbf z)^{-m-\varepsilon}\) for some fixed \(\varepsilon>0\). Here
\(m=3\). Since the vector is primitive integral, its finite-place vector
norms are one. With the paper's Euclidean infinite-place height, the
normalized product is exactly

\[
u\,H(\mathbf z)^{-3}.
\]

The required inequality is therefore \(u\le H(\mathbf z)^{-\varepsilon}\).
For a nontrivial marked endpoint the left side is at least one and the right
side is strictly below one. It fails at every such endpoint.

This conclusion excludes this explicit form system. It is not a theorem that
no possible application of the Subspace Theorem can help Collatz. A different
construction would have to retain a new source of approximation beyond the
factors already present in (2).

## 4. Keeping several returns does not repair this product

Take any fixed number \(r\) of marked visits from the same source, and retain
one copy of the preceding three-coordinate system for each visit. Use the
block diagonal forms at the three places. Their rank is \(3r\), the
concatenated integer vector is primitive, and its unnormalized product is

\[
\prod_{h=1}^{r}u_{j_h}\ge1.\tag{3}
\]

The normalized product is \(H^{-3r}\prod_hu_{j_h}\), so the required
additional factor \(H^{-\varepsilon}\) is still absent. Equation (3) handles
every fixed finite number of independently encoded returns, including very
long returns. Letting the number of coordinates grow with the orbit clock
does not satisfy the fixed-dimension hypothesis of the same theorem.

An attempted reanchoring at each marked state creates another issue: forms
such as \(x_{j_h}X+Z-Y\) now have coefficients depending on the visit. The
fixed-form theorem cannot be applied to that family without an additional
theorem about moving forms and verification of its height hypotheses.
Keeping the original source \(n\) fixed avoids this issue, but then (2)
applies exactly.

### A genuinely coupled elimination was also tested

Take two marked states \(x=2^d+u\) and \(y=2^e+v\), both greater than one,
on the same ordinary orbit, separated by \(q>0\) odd steps and \(a\) binary
divisions. Their actual tail carry \(c\) satisfies

\[
2^a y=3^q x+c,\qquad
c=\frac{B_{j+q}-3^qB_j}{2^{A_j}}.
\]

It is positive, odd, and prime to three. Its last summand proves the
prime-to-three statement. Its first summand is odd and all its other
summands are even, proving oddness. Here every odd-step valuation is at
least one.

Eliminating the fixed source gives the coupled band equation

\[
3^q2^d-2^{a+e}+c=2^a v-3^q u=:\mathcal R_{xy}.\tag{3a}
\]

Now use the primitive vector
\((X,Y,Z)=(3^q2^d,2^{a+e},c)\), with forms \((X,Y,X-Y+Z)\) at infinity
and the coordinate forms at two and three. This is a fixed full-rank form
system; its coefficients do not depend on either endpoint. Its complete
local product is

\[
|\mathcal R_{xy}|.\tag{3b}
\]

The monomial local factors cancel their real sizes exactly. As \(a\ge1\)
and \(u\) is odd, \(\mathcal R_{xy}\) is odd and nonzero. The new
coupling therefore still gives a product at least one. If the two offsets
happen to be identical, it gives the stronger explicit lower bound
\(u|2^a-3^q|\ge u\).

With three successive marked states, with block parameters \((q,a)\) and
\((r,b)\), the coupled remainders satisfy

\[
\mathcal R_{xz}=2^a\mathcal R_{yz}+3^r\mathcal R_{xy},
\qquad
\gcd(|\mathcal R_{xy}|,|\mathcal R_{xz}|)
=\gcd(|\mathcal R_{xy}|,|\mathcal R_{yz}|).\tag{3c}
\]

The equality of gcds uses oddness of \(\mathcal R_{xy}\). Thus ordinary
integrality does not automatically accumulate an extra power of two in this
gcd. A small shared gcd or a new cancellation would have to come from another
arithmetic property of the actual return words. AR-5 below explicitly
constructs unbounded ordinary three-return examples where this gcd is one.

These computations do not exclude all possible coupled constructions. They
identify the remainder that survives the two-return elimination, the exact
three-return relation it obeys, and why those two particular closing attempts
do not produce the required power saving.

## 5. A route that can escape the cancellation: periodic shadows

Let \(w\) be a finite parity word of length \(q\ge1\) and weight \(s\).
If its one-positions are \(d_0<\cdots<d_{s-1}\), set

\[
C_w=\sum_{i=0}^{s-1}3^{s-1-i}2^{d_i},\qquad D_w=2^q-3^s.
\]

Its affine map and periodic two-adic realizer are

\[
F_w(x)=\frac{3^s x+C_w}{2^q},\qquad
\xi_w=\frac{C_w}{D_w}.
\]

The integer \(D_w\) is nonzero and odd. Bernstein–Lagarias conjugacy is an
isometry: parity words agree for their first \(L\) digits exactly when their
sources agree modulo \(2^L\) [BL96, §1]. Consequently, for an ordinary
integer \(x\), the exact number of initial parity digits agreeing with
\(w^\infty\) is

\[
\boxed{\quad v_2(D_wx-C_w)\quad}\tag{4}
\]

when \(D_wx-C_w\ne0\); agreement is infinite if the numerator is zero.
The use of the full denominator is essential.

**AR-3, an exact repetition certificate.** If \(w^r\) is a prefix of the
actual parity word of \(x\), then either \(D_wx=C_w\), giving an actual
periodic source, or

\[
2^{rq}\le |D_wx-C_w|.\tag{5}
\]

Indeed, (4) gives divisibility by \(2^{rq}\), and a nonzero ordinary
integer divisible by that power has absolute value at least that power.
When \(w\) is the actual first \(q\)-clock block of \(x\),

\[
D_wx-C_w=2^q(x-T^q(x)),\tag{6}
\]

so (4) becomes \(q+v_2(x-T^q(x))\) unless the source is periodic. These
identities give the maximal exact residence in every periodic shadow, not
only in one fixed short-word family.

For a preperiod \(U\) of length \(p\) and weight \(a\), followed by a
period \(V\), the full numerator testing the original fixed source \(n\)
is

\[
N_{U,V}(n)=3^aD_Vn+D_VC_U-2^pC_V.
\]

If \(U\) is an actual prefix and \(x_p=T^p(n)\), then

\[
N_{U,V}(n)=2^p(D_Vx_p-C_V).\tag{7}
\]

Thus a valid global argument could prove enough efficient repeated words to
force \(2^L>|N_{U,V}(n)|\). It would then force the numerator to vanish,
without needing an irrationality theorem. It must still exclude any
nontrivial positive cycle thereby obtained. No such universal repetition
estimate is proved here.

### A source-height version needing no periodic rational

If two distinct ordinary integers \(x,y\) share their first \(L\) actual
parity digits, then

\[
2^L\mid x-y,\qquad 2^L\le|x-y|.\tag{8}
\]

For the inequality, an elementary witness is the clock
\(k=v_2(|x-y|)\). Write \(y=x+2^kt\) with \(t\) odd when \(y>x\).
The exact prefix-lift identity gives

\[
T^k(y)=T^k(x)+3^{q_k(x)}t,
\]

so the parities at clock \(k\) differ. If \(|x-y|<2^L\), then \(k<L\),
contradicting equality of the proposed prefixes. This finite source-height
certificate is formalized directly in `BandArithmetic.lean`.

## 6. What the primary complexity theorems actually supply

Dubickas [Dub09, Theorem 5] uses (8) and
\(T^k(n)<(3/2)^k(n+1)\) to prove that a hypothetical divergent positive
trajectory has parity factor complexity with

\[
\liminf_{L\to\infty}\frac{p(L)}L
\ge\frac{\log2}{\log(3/2)}=1.709511\ldots.
\]

This is a necessary lower bound, not the upper bound needed to force an
efficient repetition. More precisely, let

\[
M(N)=\max_{0\le k\le N}T^k(n).
\]

If the orbit has no repeated values and \(M(N)<2^L\), its first \(N+1\)
length-\(L\) factors are distinct, by (8). Therefore

\[
p(L)\ge N+1.\tag{9}
\]

This keeps the actual source-dependent growth envelope. For example, a
hypothetical divergent orbit satisfying \(\log M(N)=o(N)\) must have
\(p(L)/L\to\infty\): for every fixed \(K\), take \(N=\lfloor KL\rfloor\)
in (9), then let \(L\to\infty\). This is an elementary consequence of the
same argument, not a claim that the growth hypothesis has been proved.

Adamczewski–Bugeaud [AB07, Theorems 1B and 6] instead concern the Hensel
digits of the algebraic number itself. The parity word of \(n\) is the
binary expansion of \(\Phi^{-1}(n)\), not the Hensel expansion of \(n\).
One cannot transfer algebraicity or rationality across \(\Phi^{-1}\).
Bernstein–Lagarias explicitly formulate the reverse rationality assertion
as their Periodicity Conjecture [BL96, pp. 2–3]. It is not an available lemma
that can be used to prove Collatz.

## 7. Narrow leading bands preserve every finite low-bit itinerary

There is an exact reason that markedness alone cannot supply the missing
finite repetition law. Fix any positive odd ordinary \(u\), and fix any
finite horizon \(L\). For every sufficiently large \(d\ge L\), put

\[
n_d=2^d+u.
\]

Then \(n_d\) is odd, has binary depth \(d\), and is marked, because
\((d+1)u/2^d\to0\). For every \(k<L\), the prefix-lift identity gives

\[
T^k(n_d)=3^{q_k(u)}2^{d-k}+T^k(u),
\]

whose first summand is even. Hence \(n_d\) and \(u\) have identical parity
itineraries through the whole prescribed horizon. The finite parity-cylinder
bijection supplies a positive odd \(u\) for every prescribed binary word
whose first digit is one. Thus **every finite odd-start parity word occurs
at arbitrarily large marked sources**.

This does not construct a single ordinary source following arbitrary data
forever: the witnesses vary with the depth. It does show that a universal
repetition theorem cannot follow from the leading-band condition and a
fixed amount of low-bit information alone.

## 8. Precise remaining global obligation

Before stating the missing theorem, the following stronger construction tests
whether a near return of leading phases might itself force repeated parity.

### AR-4: arbitrarily close actual marked returns with immediate parity disagreement

Let integers \(q,A\) satisfy

\[
q\ge8,\quad q\le A<2q,\quad
1<\gamma:=3^q/2^A\le1+4/q.\tag{10}
\]

Choose **any** valuation word \(a_0,\ldots,a_{q-1}\in\{1,2\}\) with
\(a_0=1\) and \(\sum_i a_i=A\). Such words exist because \(A<2q\).
Put \(A_i=\sum_{h<i}a_h\) and

\[
C=\sum_{i=0}^{q-1}3^{q-1-i}2^{A_i}.
\]

Choose the unique residue \(0\le r<2^{A+2}\) satisfying

\[
3^q r+C\equiv2^A\pmod{2^{A+2}},\tag{11}
\]

and define

\[
d=A+q+8,\qquad x=2^d+r,\qquad
y=\frac{3^q x+C}{2^A}.
\]

Then all of the following hold:

\[
\begin{gathered}
U^q(x)=T^A(x)=y,\qquad x<y,\\
\lfloor\log_2x\rfloor=\lfloor\log_2y\rfloor=d,
\qquad x,y\in D,\\
0<\frac{y}{2^d}-1<\frac5q,\qquad
1<\frac yx<1+\frac5q,\\
x\equiv3\pmod4,\qquad y\equiv1\pmod4.
\end{gathered}\tag{12}
\]

Thus the first two shortcut parity digits at \(x\) are \(11\), whereas
those at the later marked point \(y\) are \(10\). They agree for exactly
one initial parity digit, even though the two points are in the same
shrinking dyadic band and their ordinary ratio tends to one along this
construction. The endpoint is an actual later iterate of the marked-return
map; it is not asserted to be the first return.

**Proof of legality.** The multiplier \(3^q\) is invertible modulo
\(2^{A+2}\), so (11) specifies one residue. The finite parity-cylinder
bijection, applied to the word

\[
1\,0^{a_0-1}\,1\,0^{a_1-1}\cdots1\,0^{a_{q-1}-1}\,1\,0,
\]

shows that it is exactly the residue whose first \(q\) actual odd-step
valuations are the chosen \(a_i\), and whose terminal odd state is
\(1\pmod4\). There is also a direct ordinary proof. Let
\(C_0=0\), \(C_{i+1}=3C_i+2^{A_i}\), and
\(N_i=3^i x+C_i\). For \(i<q\), reduce

\[
N_q=3^{q-i}N_i+
 \sum_{h=i}^{q-1}3^{q-1-h}2^{A_h}
\]

modulo \(2^{A_i+1}\). The first tail term has valuation exactly \(A_i\),
and all subsequent terms have larger valuation. Since \(N_q\) is divisible
by \(2^A\), this gives
\(N_i\equiv2^{A_i}\pmod{2^{A_i+1}}\).
Thus \(N_i/2^{A_i}\) is an odd ordinary integer at every intermediate
clock. The terminal quotient is \(1\pmod4\) by (11), so each adjacent
identity \(2^{a_i}x_{i+1}=3x_i+1\) has exactly the prescribed valuation.
All these states are positive because their affine numerators are positive.

Since \(d\ge A+2\), replacing \(r\) by \(x\) preserves this full
finite itinerary. Its first valuation is one, so \(x\equiv3\pmod4\);
(11) gives \(y\equiv1\pmod4\). In particular, \(r\) is positive and odd.

**Proof of the band and size bounds.** The elementary inequality
\(q\le2^q\) gives

\[
0<\frac r{2^d}<2^{-q-6}\le\frac1{64q}.
\]

Because \(A_i\le A\),

\[
0<C\le2^A\sum_{i=0}^{q-1}3^{q-1-i}
 =2^A\frac{3^q-1}{2}<2^{A-1}3^q.
\]

As \(\gamma\le3/2\), this yields

\[
\begin{aligned}
0<\frac y{2^d}-1
 &=\gamma-1+\gamma\frac r{2^d}+\frac C{2^{A+d}}\\
 &<\frac4q+\frac3{128q}+\frac3{1024q}
 <\frac5q<1.
\end{aligned}
\]

Hence both binary depths are \(d\). Also
\(d+1=A+q+9\le3q+8\le4q\), so

\[
(d+1)\frac{x-2^d}{2^d}<\frac1{16},\qquad
(d+1)\frac{y-2^d}{2^d}<20<70.
\]

Both points are marked. The inequalities \(\gamma>1\), \(C>0\) give
\(y>x\), and \(x\ge2^d\) makes the same upper calculation imply
\(y/x<1+5/q\). This proves (12).

**Unbounded parameter set.** The one-sided approximation theorem in PR 182
gives arbitrarily large \(q\) with an integer \(A\) satisfying
\(0<q\log_2 3-A<2/q\). For large \(q\), these integers lie between \(q\)
and \(2q\). On \(0\le t\le1\), convexity gives \(2^t\le1+t\); thus
these approximants satisfy (10), with room to spare. This is also a standard
consequence of the lower continued-fraction convergents of the irrational
number \(\log_2 3\). No conjecture about its partial quotients is needed.

For each admissible pair \((q,A)\), all
\(\binom{q-1}{A-q}\) choices of the valuation word are retained. Distinct
words give distinct residues in (11). The construction does not assert a
single ordinary source realizing an infinite freely chosen valuation word.

The finite regression checks all 330 such words for \((q,A)=(12,19)\), and
ten words each for \((53,84)\) and \((665,1054)\). Their source binary
lengths are respectively 40, 146 and 1728. These finite examples corroborate
the exact general construction; its quantifiers are supplied by the proof
above and the one-sided approximation input.

### AR-5: three close genuine returns can have no common remainder factor

This construction tests the next hoped-for implication in (3c): perhaps the
coupled remainders become highly divisible when several marked returns are
close. They need not.

Take

\[
q\ge8,\qquad q<A<2q,\qquad
1<\gamma=3^q/2^A\le1+2/q.\tag{13}
\]

Choose a valuation prefix \(P\) of length \(q-2\), with entries in
\(\{1,2\}\) and total \(A-3\). This is possible because
\(q-2\le A-3\le2(q-2)\). Define two valuation blocks

\[
w_1=P(1,2),\qquad w_2=P(2,1).
\]

They have the same number \(q\) of odd steps and binary length \(A\). If \(c_P\)
is the carry of the common prefix, their complete carries are exactly

\[
c_1=9c_P+5\,2^{A-3},\qquad
c_2=9c_P+7\,2^{A-3},\qquad
c_2-c_1=2^{A-2}.\tag{14}
\]

Realize the concatenation \(w_1w_2\) by the unique residue
\(r\pmod{2^{2A+2}}\) forcing its terminal quotient to be \(1\pmod4\),
using the same construction and intermediate-numerator proof as AR-4. Set

\[
d=2A+2q+8,\qquad x_0=2^d+r,\qquad
x_1=U^q(x_0),\qquad x_2=U^q(x_1).
\]

Then \(x_0<x_1<x_2\); all three states have binary depth \(d\), are
marked, and satisfy

\[
0<\frac{x_i-2^d}{2^d}<\frac5q\qquad(i=0,1,2).\tag{15}
\]

For completeness, \(r/2^d<1/(64q)\), \(\gamma\le5/4\), and
\(\gamma^2-1\le4.5/q\). The full concatenated carry divided by
\(2^{2A+d}\) is less than
\(\gamma^2 2^{-2q-9}\le25/(8192q)\). Therefore

\[
\frac{x_2}{2^d}-1
<\frac{4.5}{q}+\frac{25}{1024q}+\frac{25}{8192q}
<\frac5q<1.
\]

The intermediate endpoint has an even smaller bound by the same estimate
with one block. Also \(d+1\le6q+7\le7q\), so the marked-band left side,
divided by \(2^d\), is less than \(35<70\). Positivity of the carries and
\(\gamma>1\) give strict increase.

Writing \(u_i=x_i-2^d\), the coupled remainders of (3a) are

\[
\mathcal R_{01}=c_1+(3^q-2^A)2^d,
\qquad
\mathcal R_{12}=c_2+(3^q-2^A)2^d.
\]

They are odd and differ by exactly the power of two in (14). Hence

\[
\boxed{\gcd(\mathcal R_{01},\mathcal R_{12})=1.}\tag{16}
\]

The two actual parity blocks agree up to their final three digits \(110\)
versus \(101\). Thus the initial parity words at \(x_0\) and \(x_1\)
agree for exactly \(A-2\) digits, and
\(v_2(x_1-x_0)=A-2\). The construction supplies a long repeat, but its
length is much less than the source height \(d=2A+2q+8\), so it does not
violate the ordinary repetition certificate (8).

The same exact PR 182 approximation theorem used in AR-4 provides an
unbounded set of parameters satisfying (13). This is an unbounded family of
positive ordinary finite witnesses. It does not assert that one fixed source
has such triples forever, that these are first returns, or that any source
fails to converge. It shows that even a third genuine close marked return
does not force the particular gcd amplification proposed after (3c).

AR-4 and AR-5 were independently reconstructed by the merger lane at the
stated hypothesis level; that narrow review does not verify a global closing
inference.

### The still-missing closing statement

The arithmetic literature leaves two materially different possible advances:

1. Prove a source-preserving, efficiently repeated parity structure on every
   unresolved orbit, strong enough to violate (5) or (8), and handle the
   periodic alternative with the complete denominator.
2. Construct coupled return forms whose complete local-factor product gains
   a genuine fixed power of their height, while keeping a fixed dimension,
   fixed coefficients and one fixed ordinary source.

AR-4 rules out inferring an efficient repeat from the closeness of one
prescribed genuine marked return: even its second parity digit can differ.
It does not rule out a subtler theorem selecting another, later return on
every nonconvergent orbit. The forced band gives neither hypothesis above.
PR 182's deterministic Fourier
cancellation for an escaping odd orbit, frozen at
`8372e302041a55057742a9e6ee9b4fa600c88fdb`, also does not provide a parity
repetition rate or the required low-bit valuation average. The exact product
calculation prevents treating a collection of leading-phase approximations
as if it supplied those missing facts.

The first unsupported step in the attempted full proof is therefore explicit:
there is no proved arithmetic rule forcing one of these stronger relations
for the same prescribed ordinary source after its unresolved longer returns.
Full Collatz, universal coefficient stopping, and exclusion of every
nontrivial positive cycle remain open.

## Formal and finite-check coverage

`BandArithmetic.lean` formalizes AR-1, the prime-to-three and primitive-vector
facts, the exact evaluated product in AR-2, its positive lower bound, the
finite independent-return product bound, the parity-preserving offset lift,
and the ordinary source-displacement certificate (8). It does not formalize
the Subspace Theorem, the local-norm interpretation, periodic two-adic
conjugacy, or an infinite complexity argument. Their written uses above keep
their exact hypotheses visible.

`check_arithmetic.py` uses exact integers and fractions to check the complete
three-place products, periodic-shadow break depths, preperiod numerators,
and marked parity lifts on specified finite ranges. A successful run checks
16,384 actual odd prefixes, 4,591 nonperiodic shadow break depths, 8 exact
periodic shadows, 18,396 preperiod identities, 1,023 marked parity lifts, and
350 close actual marked returns with the immediate parity disagreement of
AR-4, and 230 marked triples with coprime coupled remainders from AR-5.
AR-4 and AR-5 are written theorems, not additional Lean theorems in this
checkpoint.
These are implementation regressions and examples, not an all-source
convergence computation. Primary references and exact theorem scopes are in
[`SOURCES.md`](SOURCES.md).
