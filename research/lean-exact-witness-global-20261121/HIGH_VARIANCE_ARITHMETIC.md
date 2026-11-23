# Cyclic phase averaging and the distinguished integer carry

Date: 2026-11-23. **Status: written theorems and a direct all-cycle
closing attempt. Full Collatz and unrestricted positive-cycle exclusion
remain OPEN.** No statement in this note is counted as a Lean theorem.

The new quantitative deduction uses cyclic averaging, rather than a
single traversal with a boundary. Its test window can exceed the period.
It bounds the leading-phase discrepancy of every positive integer cycle
by a power of its minimum, and gives a corresponding typical binary-run
lower bound. The arithmetic continuation retains the exact full
denominator through an integer carry circulation. A one-height-band
exclusion is reconstructed by an elementary modular argument; this is
related to the existing high/Christoffel-cycle literature and is not
presented as a new unrestricted-cycle result.

The main unclosed step is at the end: arbitrary height layers change the
geometric unit certificate into a weighted sum. Neither the phase estimate
nor the exact carry state bounds make that weighted sum a unit.

## 1. Conventions and the complete cycle

Let an actual odd cycle be

\[
 x_0,x_1,\ldots,x_{p-1},\qquad x_i\in\mathbb N_{>0}\text{ odd},
 \qquad 2^{a_i}x_{i+1}=3x_i+1,\quad a_i\ge1,
 \tag{HC1}
\]

with indices modulo \(p\). The primitive case has distinct states; the
phase argument also permits a repeated complete traversal. Set

\[
 A=\sum_{i<p}a_i,\quad m=\min_i x_i,\quad M=\max_i x_i,
 \quad\alpha=\log_2 3,
\]

\[
 \epsilon_i=\log_2\left(1+\frac1{3x_i}\right),\qquad
 \Lambda=A-p\alpha=\sum_{i<p}\epsilon_i>0,
 \qquad\eta=\Lambda/p.
 \tag{HC2}
\]

The identity follows by multiplying every edge in (HC1), or by summing
its logarithm. In particular

\[
 0<\eta\le\frac1{3m\log2}.
 \tag{HC3}
\]

Write \(\theta_i=\{\log_2x_i\}\), let
\(\mu=p^{-1}\sum_{i<p}\delta_{\theta_i}\), and define circular-interval
discrepancy

\[
 \mathcal D(\mu)=\sup_I|\mu(I)-|I||,
 \tag{HC4}
\]

using a consistent half-open convention.

## 2. Arbitrarily long test windows on one finite cycle

### Theorem HC1: boundary-free cyclic discrepancy

For **every** continued-fraction convergent denominator \(q\) of
\(\alpha\),

\[
 \boxed{\mathcal D(\mu)\le\frac4q+2q\eta.}
 \tag{HC5}
\]

There is no condition \(q\le p\), no remainder \(q/p\), and no
distinctness assumption on a test window longer than the period.

**Proof.** Extend (HC1) periodically to all integer times. For a start
\(j\in\{0,\ldots,p-1\}\), compare the actual length-\(q\) phase block
with

\[
 \theta_j,\ \theta_j+\alpha,\ldots,
 \theta_j+(q-1)\alpha\pmod1.
\]

The circular displacement at every position is at most

\[
 E_j=\sum_{t=0}^{q-1}\epsilon_{j+t}.
\]

If \(b/q\) is the corresponding convergent, the rational rotation
\(\theta_j+tb/q\), \(0\le t<q\), is a translated uniform \(q\)-grid.
Since \(|\alpha-b/q|<q^{-2}\), each irrational-rotation point is within
\(1/q\) of its grid point. Expanding and contracting a circular interval
therefore bounds the discrepancy of the irrational block by \(4/q\).
Expanding or contracting once more by \(E_j\) bounds the actual block
discrepancy by \(4/q+2E_j\). If an expansion fills the circle, the same
inequality follows from the trivial bound by one.

Average this inequality over all \(p\) starting positions. Each fixed
offset \(t\) permutes the original cycle. Consequently the averaged
block measure is **exactly** \(\mu\), and

\[
 \frac1p\sum_{j<p}E_j
 =\frac1p\sum_{t<q}\sum_{j<p}\epsilon_{j+t}
 =q\eta.
\]

This proves (HC5) at every positive convergent denominator, including
denominators arbitrarily larger than \(p\). \(\square\)

The cyclic Fourier version also has no endpoint term. For every integer
\(h\), the exact cyclic telescope and
\(|e^{it}-1|\le|t|\) give

\[
 |e^{2\pi ih\alpha}-1|\,|\widehat\mu(h)|
 \le2\pi|h|\eta.
 \tag{HC6}
\]

Equation (HC5), rather than an optimization of (HC6), gives the sharper
exponent used next.

### Theorem HC2: a power of the actual minimum

Put \(\tau=7.616\) and \(\beta=1/(\tau+1)=1/8.616\).
There is an absolute positive constant \(C\) such that every cycle (HC1)
satisfies

\[
 \boxed{\mathcal D(\mu)\le C\eta^\beta\le C' m^{-\beta}.}
 \tag{HC7}
\]

The constants inherit Rhin's effective positive linear-form constant;
no numerical value for that constant is computed here.

**Proof.** Rhin's inequality, in the precise form reproduced by
Lagarias--Soundararajan, Lemma 5.3, equation (5.11), implies
\(|q\alpha-b|\ge c q^{-\tau}\) for the convergents of \(\alpha\).
The convergent successor estimate gives \(q'\le C_0q^\tau\).
Thus the largest convergent denominator \(q\le Q\) obeys

\[
 c_0Q^{1/\tau}\le q\le Q
\]

for sufficiently large \(Q\). Choose
\(Q=\eta^{-\tau/(\tau+1)}\) in (HC5). Both terms are
\(O(\eta^{1/(\tau+1)})\). Enlarging the constant covers the remaining
bounded range of \(\eta\), and (HC3) proves the second inequality.
\(\square\)

This differs from applying PR178's discrepancy estimate to one primitive
traversal: that result is uniform in the traversal length and has a
harmonic correction budget. Here the input is the exact periodic
correction \(\Lambda/p\), cyclic windows have no boundary loss, and the
bound is expressed in the actual minimum.

### Corollary HC3: quantitative binary-run occupation on every cycle

Let \(R(n)\) be the number of one-runs in the finite binary expansion of
\(n\). For integers \(\ell,S\ge1\), put

\[
 K(\ell,S)=\sum_{j=0}^{\min(2S-1,\ell-1)}\binom{\ell-1}{j}.
\]

If \(2^{\ell-1}\le m\), all states have at least \(\ell\) binary
digits. Their leading words with at most \(S\) one-runs are contained
in at most \(K(\ell,S)\) length-\(\ell\) cylinders. Each cylinder has
phase length at most \(2^{1-\ell}/\log2\). Therefore

\[
 \boxed{
 \frac1p\#\{i<p:R(x_i)\le S\}
 \le K(\ell,S)
       \left(\frac{2^{1-\ell}}{\log2}+C'm^{-\beta}\right).}
 \tag{HC8}
\]

For the counting justification, a word beginning in one with at most
\(S\) one-runs has at most \(2S-1\) transitions. This inclusion is
enough for (HC8); equality in that transition count is not required.

Taking \(\ell=\lfloor\beta\log_2m\rfloor\) for sufficiently large
\(m\) gives, for fixed \(S\),

\[
 \frac1p\#\{i<p:R(x_i)\le S\}
 =O_S\bigl(m^{-\beta}(\log m)^{2S-1}\bigr).
 \tag{HC9}
\]

For every fixed \(0<c<1/4\), the standard binomial bound yields

\[
 \frac1p\#\left\{i<p:R(x_i)\le
 \left\lfloor c\lfloor\beta\log_2m\rfloor\right\rfloor\right\}
 =O_c\left(m^{-\beta(1-H_2(2c))}\right),
 \tag{HC10}
\]

where \(H_2(u)=-u\log_2u-(1-u)\log_2(1-u)\).
Indeed \(K(\ell,\lfloor c\ell\rfloor)
\le2^{(\ell-1)H_2(2c)}\), with a harmless adjustment for the finitely
many small \(\ell\). In particular, for every \(\rho>1\) and
\(0<\kappa<\beta\log_2\rho/4\),

\[
 \boxed{\frac1p\sum_{i<p}\rho^{R(x_i)}
       \ge c_{\rho,\kappa}m^\kappa}
 \tag{HC11}
\]

once \(m\) is sufficiently large. These are necessary conditions on
actual integer cycles, not evidence that no such cycle exists.

## 3. A complete one-band exclusion, with the distinguished ideal kept

### Theorem HC4: a nontrivial integer cycle has \(M\ge2m+1\)

Suppose the primitive odd cycle (HC1) satisfies \(M<2m\). Then
\(p=1\), \(a_0=2\), and \(x_0=1\).

**Order step.** Since \(M\le2m-1\), a gap at least three would send
its source below \(m\). Thus every gap is one or two. A gap-one source
satisfies \(x\le(2M-1)/3\); a gap-two source satisfies
\(x\ge(4m-1)/3\). These domain ranges are disjoint and in that order.
Within each range the map is increasing. Every gap-one image is at least
\((3m+1)/2\), whereas every gap-two image is at most
\((3M+1)/4\le(3m-1)/2\). So the two image ranges occur in the reverse
cyclic order without interleaving.

Sort the \(p\) distinct states increasingly and label them
\(0,\ldots,p-1\). If \(k\) states have gap two, the cycle permutation
is exactly \(j\mapsto j+k\pmod p\). If \(k=p\), all gaps are two,
and the complete affine identity gives the fixed state one. Otherwise
primitivity implies \(\gcd(k,p)=1\), and the actual gap word starting
at the minimum is

\[
 a_i=1+\left\lfloor\frac{(i+1)k}{p}\right\rfloor
        -\left\lfloor\frac{ik}{p}\right\rfloor,
 \qquad A=p+k.
 \tag{HC12}
\]

The case \(k=0\) is impossible for a positive cycle because every step
would increase its source. In the nonconstant case \(\gcd(A,p)=1\).

**Full-denominator step.** Put

\[
 A_i=\sum_{j<i}a_j=\left\lfloor\frac{iA}{p}\right\rfloor,
 \quad D=2^A-3^p>0,
 \quad C=\sum_{i<p}3^{p-1-i}2^{A_i}.
\]

The original cycle gives \(D\mid C\). Assume \(D>1\).
Both 2 and 3 are units in \(\mathbb Z/D\mathbb Z\). Choose integers
\(r,s\) with \(pr+As=1\), and set \(u=2^r3^s\) in this same
ring. Negative exponents mean ordinary unit inverses. The complete
denominator relation implies

\[
 u^p=2,\qquad u^A=3.
\]

Since \(pA_i-Ai\) runs through the complete interval
\(0,-1,\ldots,-(p-1)\),

\[
 3^{-(p-1)}C=\sum_{j=0}^{p-1}u^{-j}=:P\pmod D.
\]

The geometric identity gives the explicit inverse certificate

\[
 \boxed{u^{p-1}(u-1)P=u^p-1=1\pmod D.}
 \tag{HC13}
\]

Thus \(C\) is a unit at the **distinguished evaluation modulo the
whole \(D\)**, contradicting \(D\mid C\). Hence \(D=1\).
The equation \(2^A=3^p+1\), reduced modulo eight when \(A\ge3\),
is impossible: its right side is four for odd \(p\) and two for even
\(p\). The remaining cases give \((A,p)=(2,1)\), and then \(x_0=1\).
Finally, in a nontrivial integer cycle both \(M\) and \(m\) are odd,
so \(M\ge2m\) strengthens to \(M\ge2m+1\). \(\square\)

**Provenance boundary.** The balanced/Christoffel high-cycle exclusion
is existing mathematics, including Kevin Knight's published
*Collatz high cycles do not exist*. The publisher's abstract and
author's bibliography were inspected; the publisher full text returned
403 and the HAL PDF returned an access-denied page. Consequently this
note does not claim to have audited Knight's complete proof, nor claim
historical novelty for HC4. The displayed order proof and modular unit
certificate above are self-contained. They are also the elementary
distinguished-ideal version of PR185's already stated balanced-interval
norm calculation, without its larger norm aggregation.

## 4. All height layers: where order can first fail

For an arbitrary primitive integer cycle let

\[
 k_i=\left\lfloor\log_2(x_i/m)\right\rfloor\ge0,
 \qquad y_i=x_i/2^{k_i}\in[m,2m).
\]

The \(y_i\) are distinct: equality would make two distinct odd positive
integers differ by a power of two. Define the unnormalized image

\[
 z_i=3y_i+2^{-k_i}=(3x_i+1)/2^{k_i}.
\]

Every \(z_i\) lies strictly between \(3m\) and \(6m\). In the upper
bound use the integer fact \(x_i\le2^{k_i+1}m-1\). Thus the effective
normalizing exponent

\[
 e_i=a_i+k_{i+1}-k_i
\]

is always one or two, and \(y_{i+1}=z_i/2^{e_i}\). This keeps every
original gap and every height layer; it does not replace the original
cycle by a gap-one/two integer cycle.

### Lemma HC5: an exact order-inversion gate

Suppose \(y_i<y_j\), but \(z_i\ge z_j\). Then \(k_j>k_i\).
Writing \(d=k_j-k_i\), there is a positive odd integer

\[
 \delta=x_j-2^d x_i
\]

such that

\[
 \boxed{1\le\delta\le(2^d-1)/3.}
 \tag{HC14}
\]

The inequalities follow by multiplying the two compared orders by
\(2^{k_j}\):
\(x_j>2^dx_i\), but
\(3x_j+1\le2^d(3x_i+1)\).
If \(k_j\le k_i\), the correction at \(j\) is at least the correction
at \(i\), so the order cannot reverse. Oddness makes \(\delta\) odd.

For \(d=1\), (HC14) has no positive integer solution. For \(d=2\),
the only possibility is \(\delta=1\), with equality of the two
\(z\)'s. Equality implies \(U(x_i)=U(x_j)\), impossible for distinct
states in a primitive cycle. Therefore a genuine inversion in such a
cycle requires **at least three height layers of separation**, \(d\ge3\).

This supplies a global order constraint, but not a global order theorem.
For example, the literal positive odd sources \(n\) and \(8n+1\)
satisfy

\[
 n<(8n+1)/8,\qquad 3n+1>(3(8n+1)+1)/8=3n+1/2.
\]

These sources are not asserted to belong to one cycle. They show that
the local order rule really changes when the third layer is allowed.
Excluding their simultaneous occurrence on an arbitrary cycle would
itself need an additional actual-orbit argument.

Even if no inversion occurs, normalizing an arbitrary multilevel cycle
does not recover HC13. When its effective code is balanced, set
\(k=A-p\), its rotation increment, and start at the smallest normalized
state. The original cumulative gaps have the form

\[
 A_i=\left\lfloor iA/p\right\rfloor+k_0-k_i.
\]

At the same distinguished modulus the former geometric sum becomes

\[
 P=2^{k_0}\sum_{i<p}2^{-k_i}u^{-(ik\bmod p)}.
 \tag{HC15}
\]

The varying factors \(2^{-k_i}\) are units, but a sum of units need not
be a unit. Dropping them would alter the original numerator. The
geometric telescoping identity HC13 does not apply to HC15.

## 5. An autonomous integer carry retaining the complete denominator

Here is an exact alternative to replacing the distinguished ideal by a
norm. Fix any positive gap word \(a_0,\ldots,a_{p-1}\), not necessarily
realized by an integer cycle. Define the integer linear map

\[
 (L_a v)_i=2^{a_i}v_{i+1}-3v_i
\]

with cyclic indices. Its determinant is nonzero because
\(2^A\ne3^p\). The unique rational vector \(x\) solving
\(L_a x=\mathbf1\) is the complete rational cycle. Its denominators
are odd, so it has a well-defined coordinatewise binary expansion in
\(\mathbb Z_2\).

Start the **integer** carry vector at \(c^{(0)}=\mathbf1\). For each
step let \(b_i^{(t)}\in\{0,1\}\) be the parity of \(c_i^{(t)}\), and
put

\[
 \boxed{c_i^{(t+1)}=
 \frac{c_i^{(t)}+3b_i^{(t)}-2^{a_i}b_{i+1}^{(t)}}2.}
 \tag{HC16}
\]

The numerator is even, including at negative carries. If
\(v^{(t)}=L_a^{-1}c^{(t)}\), reduction modulo two gives
\(v_i^{(t)}\equiv c_i^{(t)}\pmod2\), because every \(a_i\ge1\).
Thus

\[
 v^{(t+1)}=(v^{(t)}-b^{(t)})/2.
 \tag{HC17}
\]

The bits in (HC16) are exactly the binary digits of the original
rational cycle, not independent choices. Consequently

\[
 \boxed{c^{(t)}=0\text{ for some }t
 \quad\Longleftrightarrow\quad x\in\mathbb Z_{\ge0}^p.}
 \tag{HC18}
\]

The forward implication follows by reversing (HC17). For the reverse
implication choose \(2^t\) larger than every coordinate of \(x\), so
every binary quotient vanishes. In the positive-denominator case the
rational cycle is strictly positive, so (HC18) is precisely ordinary
positive-cycle integrality. This keeps the original numerator and every
factor of \(D\).

There is a simple invariant finite box:

\[
 \boxed{1-2^{a_i}\le c_i^{(t)}\le2\quad\text{for every }i,t.}
 \tag{HC19}
\]

For the upper bound, an even \(c\le2\) contributes \(c/2\le1\)
before the nonpositive neighbor term, while an odd \(c\le2\) contributes
\((c+3)/2\le2\). For the lower bound, if
\(c\ge1-2^{a_i}\) is odd, the smallest possible next value is
\(2-2^{a_i}\). If it is even, its smallest allowed value is
\(2-2^{a_i}\), and the smallest next value is \(1-2^{a_i}\).
The initial vector belongs to the box, proving the invariant.

The carry system therefore eventually repeats for each fixed word.
Finite-state repetition does **not** prove that the only words reaching
zero are repetitions of the trivial cycle. It only makes the exact
full-denominator integrality test a finite reachability problem for that
word. A uniform ranking, conserved obstruction, or classification of the
zero basin across all positive gap words was not obtained here.

## 6. A sandpile/M-matrix attack on the same distinguished class

The carry circulation suggested applying the general M-matrix
chip-firing theory. This suggestion retains the entire integer lattice,
so it avoids the wrong-conjugate loss of an algebraic norm.

Let \(P(v)_i=v_{i+1}\), and let \(D_a\) be diagonal with entries
\(2^{a_i}\). Then

\[
 L_a=D_aP-3I,\qquad B_a=L_aP^{-1}=D_a-3P^{-1},
 \quad\det B_a=2^A-3^p=D>0.
 \tag{HC20}
\]

This is a nonsingular M-matrix. For a direct proof, put
\(H=3D_a^{-1}P^{-1}\). All its entries are nonnegative and
\(H^p=(3^p/2^A)I\), so the geometric series gives
\(B_a^{-1}=(I-H)^{-1}D_a^{-1}\ge0\).
The finite integer group

\[
 \mathbb Z^p/B_a\mathbb Z^p
\]

has order \(D\). The class of \(\mathbf1\) is zero precisely when
\(P x=B_a^{-1}\mathbf1\) is integral, which is exactly the original
cycle integrality condition. No prime factor is removed in this
formulation.

Guzman--Klivans' M-matrix theory supplies a unique energy-minimizing,
equivalently z-superstable, nonnegative representative of each class.
It applies even when some row sums are negative. The tempting extra
claim was that \(\mathbf1\) must already be the nonzero superstable
representative, except for the trivial Collatz word. That claim is
false even for pure dyadic diagonals, as the next control shows.
Ordinary stability is insufficient: when \(p>1\),
\(1<2^{a_i}\) makes every vertex initially stable, but membership in
the zero class can involve a whole nonnegative multi-firing vector.
For \(p=1\), the scalar matrix \(2^{a_0}-3\) must be handled separately
rather than confusing its diagonal with \(2^{a_0}\).

### The all-ones vector need not be z-superstable, even in the dyadic case

Take \(a=(1,1,3)\), so \(D=32-27=5\), and

\[
 B_a=\begin{pmatrix}2&0&-3\\-3&2&0\\0&-3&8\end{pmatrix}.
\]

For \(z=(5,8,3)^T\), direct multiplication gives

\[
 B_a z=(1,1,0)^T,\qquad
 \mathbf1-B_a z=(0,0,1)^T\ge0.
 \tag{HC21a}
\]

Thus \(\mathbf1\) is not z-superstable. It is nevertheless
chi-superstable: every nonempty proper subset has a coordinate in the
subset whose cyclic predecessor is outside, where \(B_a\chi\ge2\).
For the full subset the final coordinate is \(8-3=5>1\).
This is exactly the distinction that the general M-matrix theorem
preserves when row sums are allowed to be negative.

The true rational odd cycle of this word is
\((19,31,49)/5\), so this is not an integer cycle. In fact
\(g=(0,0,1)^T\) is the z-superstable representative: its inverse image
is \(B_a^{-1}g=(6,9,4)^T/5\). If a nonzero integral \(w\ge0\)
satisfied \(B_aw\le g\), positivity of the inverse would force
\(w_2=0\). A nonempty proper support then has a boundary coordinate
\((B_aw)_i\ge2>g_i\), a contradiction. The energy theorem therefore
returns this nonzero representative, rather than certifying the original
all-ones vector as already minimal.

### An exact control isolating the dyadic restriction

If one uses only positive inverse, even diagonal, constant off-diagonal
three, and positive odd integer states, the intended nonvanishing claim
is false. Consider

\[
 x=(31,47,71,107,161,121,91,137,103),
 \quad d=(2,2,2,2,4,4,2,4,10).
 \tag{HC21}
\]

Every displayed equation
\(d_i x_{i+1}=3x_i+1\) is exact, with cyclic indices. Moreover

\[
 \prod_i d_i-3^9=20480-19683=797>0.
\]

The corresponding nonsingular M-matrix therefore has its all-ones
vector in the zero class, with a strictly positive integral firing
vector. Replacing \(2^{a_i}\) by \(d_i\) in HC16, its carry starts
at all ones and reaches all zeros after eight binary columns, as it
must because its maximum source is \(161<256\).

This is **not** an ordinary Collatz cycle: the final divisor is ten,
and the actual accelerated successor of \(103\) is \(155\), not
\(31\). Precisely one factor five has been removed at that transition.
The example shows that the general M-matrix machinery cannot by itself
settle the proposed zero-class assertion. A successful application must
use the pure powers of two in every diagonal entry. Neither a weighted
burning argument nor an energy comparison establishing that additional
dyadic assertion was obtained here.

The nine integer edge identities, determinant 797, and eight-step carry
termination in this control were checked directly with integer
arithmetic. This is a targeted control on the suggested general theorem,
not a search for actual Collatz cycles.

## 7. Scope of the closing attempt and source pins

The intended global argument was to use phase rigidity to force enough
order, then use a distinguished-ideal unit certificate to exclude the
whole cycle. HC5--HC7 give the phase estimate, and HC13 gives a genuine
whole-modulus unit certificate in the one-band case. HC14--HC16 retain
exactly what changes in arbitrary layers. The missing statement is a
uniform control of the weighted distinguished sum HC15, or equivalently
an obstruction to HC18 for every nontrivial positive gap word. It is
not supplied by the bounded carry box, a generic algebra norm, or the
large-run occupation estimate.

This note does not claim that every cycle is narrow, every normalized
order is preserved, or an arbitrary cyclic word has bounded description
complexity. In particular a high-run lower bound cannot be reinterpreted
as the low-run return hypothesis of the sparse arithmetic-return theorem.

Repository pins inspected:

- PR177, `0444986571f09f302cb3687b4bba3552600e4119`,
  `ARITHMETIC_CYCLE_CONTINUATION.md`: preceding qualitative properness of
  run moments across cycles. Its S-unit input is not used in HC1--HC19.
- PR178, `7e4569476e152f6b8537bdc1711df595ec1ffd89`,
  `research/whole-repo-synthesis-20261122/phase/EFFECTIVE_PHASE_AND_RUNS.md`:
  actual-edge phase recurrence, continued-fraction block comparison, and
  the precise Rhin specialization. The cyclic averaging and minimum
  parameter are the changes here.
- PR185, `39ba48e6a8af781193e28c679ea8ab64663c3aa6`,
  `research/rigidity-closing-20261122/CYCLOTOMIC_ZERO_FIBER.md`, N1--N2,
  N24--N27: balanced-interval unit case, wrong-conjugate norm obstruction,
  and the need to retain the distinguished ideal.
- PR175, `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`,
  `research/lean-global-closure-20261121/closing/ZERO_ATOM_CLOSING_ATTEMPT.md`:
  arbitrary-word zero-fiber/minimum census and its remaining exclusion
  threshold. That threshold has not been met here.

Primary literature inspected:

1. Lagarias--Soundararajan, *Benford's Law for the 3x+1 Function*,
   author manuscript v2, Lemma 5.3 and (5.11),
   <https://arxiv.org/pdf/math/0509175>. This supplies the stated Rhin
   linear-form input. Their different theorem averaging over starting
   seeds is not used. Rhin's original chapter proof was not reconstructed.
2. Halbeisen--Hungerbuhler, *Optimal bounds for the length of rational
   Collatz cycles*, especially Lemmas 4--5 and the sharp mechanical-word
   minimum, <https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf>.
   Inspected as prior-art context for the balanced-cycle calculation.
3. Knight, *Collatz high cycles do not exist*, Discrete Mathematics
   349(3), 114812 (2026), DOI
   <https://doi.org/10.1016/j.disc.2025.114812>. Publisher abstract and
   author bibliography inspected; full-text access limitations are stated
   above. No theorem from inaccessible text is silently imported.
4. Sterin--Woods, *The Collatz process embeds a base conversion algorithm*,
   v4, <https://arxiv.org/pdf/2007.06979>, Theorem 42, Lemma 46 and
   Conjecture 50: finite/infinite base conversion and the existing
   cyclic-integer reachability viewpoint. The carry recurrence HC16 is
   derived directly here, not asserted to settle their conjecture or the
   integer reachability problem.
5. Guzman--Klivans, *Chip-firing and energy minimization on M-matrices*,
   primary manuscript <https://arxiv.org/pdf/1403.1635>, Definition 2.2,
   the energy in (3.1), Definitions 4.1--4.3, Theorems 3.4 and 4.6,
   and Corollary 4.7. These statements and the proof of the
   z-superstability/energy-minimum equivalence were inspected. This supplies the precise applicability
   boundary in Section 6. The Collatz zero-class exclusion is not a
   conclusion of that theorem.

No large numerical search, historical Lean rebuild, or external theorem
proof replay was used as evidence for these written deductions.
