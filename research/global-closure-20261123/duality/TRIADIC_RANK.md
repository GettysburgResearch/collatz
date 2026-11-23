# Constructing a triadic dual: a full closing rank and the unresolved source step

**Status.** The closing implication is proved, including a concrete Lean
formalization. The construction of a dual for every positive ordinary
integer is **OPEN**. Consequently this packet does not prove Collatz.

The target is stronger than rational-dual existence: construct

\[
                    \Omega(n)\in\mathbb Z[1/3]
                    \qquad(n\in\mathbb Z_{>0}).                 \tag{1}
\]

A successful construction would settle both escaping trajectories and
nontrivial positive cycles. The new work gives a well-founded rank for
one unchanged finite candidate, a finite sufficient congruence with an
explicit height budget, and a direct attempt to obtain that budget from
the original and complementary affine carries. That last attempt did
not provide the required small residue.

The earlier [rational-dual packet](../../high-variance-20261123/arithmetic/RATIONAL_DUAL_CERTIFICATE.md)
already decides any *supplied* rational candidate. This continuation does
not extend its census. It changes the construction target to denominators
supported at 3 and makes the resulting full-convergence implication
explicit.

## 1. Ordinary input, complementary parity, and the stronger target

Use the shortcut map

\[
 T(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(3x+1)/2,&x\equiv1\pmod2.
 \end{cases}
\]

For a rational number with odd denominator, parity is its residue modulo
2. The map is defined by the same branches on those rationals.

Monks and Yazinski define the 2-adic involution \(\Omega\) by complementing
the whole parity sequence. Their Theorem 2.1 identifies rationality of
\(\Omega\) on positive integers with the absence of divergent positive
orbits. Rationality alone leaves the positive-cycle question. See their
[primary paper, Theorem 2.1](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf),
published as *The autoconjugacy of the 3x+1 function*, Discrete Mathematics
275 (2004), 219–236,
[DOI](https://doi.org/10.1016/S0012-365X(03)00125-0).

The present target keeps only the localization \(\mathbb Z[1/3]\). Its
closing argument is elementary, and the rationality reduction is not
claimed as new literature. The exact scope is:

> **Triadic closure.** If \(n>0\) has a complementary parity trajectory
> starting at one rational \(a/3^r\), with \(a\in\mathbb Z\) and
> \(r\in\mathbb N\), then the ordinary orbit of \(n\) reaches 1.

Conversely, a supplied finite trajectory from \(n\) to 1 constructs such
a dual. Put the dual value 2 opposite the terminal 1, and pull it backward:

\[
 y_i=\begin{cases}
       2y_{i+1},&x_i\text{ odd},\\
       (2y_{i+1}-1)/3,&x_i\text{ even}.
      \end{cases}                                           \tag{2}
\]

These operations preserve \(\mathbb Z[1/3]\) and impose the required
parities. Appending the complementary \(1,2\) tails supplies all later
clocks. Thus (1), quantified over positive ordinary inputs, is equivalent
to full convergence, with no separate cycle premise. Signed numerators
are necessary: the published example is \(\Omega(3)=-4/9\).

## 2. Denominator cancellation gives an actual well-founded rank

Keep a state

\[
                    (x,w,r),\qquad x>0,\quad w\in\mathbb Z,
                    \quad y=w/3^r.                            \tag{3}
\]

Opposite parity means \(x+w\) is odd. It is enough to retain the displayed
power of 3; lowest terms are not required. The exact transitions are

\[
\begin{array}{c|c|c|c}
\text{branch}&x'&w'&r'\\ \hline
x\text{ odd}&(3x+1)/2&w/2&r\\
x\text{ even},\ r>0&x/2&(w+3^{r-1})/2&r-1\\
x\text{ even},\ r=0&x/2&(3w+1)/2&0.
\end{array}                                                   \tag{4}
\]

Every numerator division is integral when the parity test passes. In
particular the middle row is the exact rational identity

\[
 \frac{3(w/3^r)+1}{2}
       =\frac{(w+3^{r-1})/2}{3^{r-1}}.                         \tag{5}
\]

If the initial fraction is reduced and \(r>0\), an original-even step
removes exactly one denominator factor of 3, while an original-odd step
preserves the denominator exponent. For \(r\ge2\), the new numerator in
(4) is still a unit modulo 3; for \(r=1\), the denominator is exhausted.
The proof below also works with unreduced data.

### 2.1 A zero numerator cannot persist along a positive ordinary input

If \(w=0\), a passed parity test requires \(x\) odd, and the first row
keeps the numerator zero. An all-time compatible path would therefore
have an all-odd ordinary tail.

Such a tail is impossible for one positive ordinary starting integer.
Writing its states as \(x_j\), the identity

\[
                  2(x_{j+1}+1)=3(x_j+1)                      \tag{6}
\]

implies \(2^k\mid x_0+1\) for every \(k\), because powers of 2 are
coprime to 3. A fixed positive integer \(x_0+1\) cannot have that
property. This is an all-time ordinary argument, not an extraction from
changing finite witnesses.

### 2.2 The rank decreases at every remaining nonterminal step

Set

\[
 P=x|w|,\qquad E(x,w)=2P+\mathbf1_{\{w=1\}},\qquad
                         \mathcal R=(r,E(x,w)),               \tag{7}
\]

ordered lexicographically in \(\mathbb N^2\). Consider a compatible
step with \(x>1\) and \(w\ne0\).

For original-odd \(x\),

\[
               4x'|w'|=(3x+1)|w|<4x|w|.                    \tag{8}
\]

The integer product strictly decreases. Twice that decrease pays for
any change of the indicator in (7).

For original-even \(x\) and \(r>0\), the first coordinate \(r\)
strictly decreases, irrespective of the size or sign of the new numerator.
This pays for denominator cancellation and any associated increase of
\(P\).

For original-even \(x\) and \(r=0\),

\[
                   4x'|w'|=x|3w+1|.                         \tag{9}
\]

If \(w\ne0,1\), then \(|3w+1|<4|w|\), so the integer product again
strictly decreases. The only remaining case is \(w=1\), when
\(w'=2\) and \(x'|w'|=x|w|\). The indicator drops from 1 to 0.
Thus (7) decreases in this case as well.

An all-time compatible path avoiding \(x=1\) has no zero numerator by
Section 2.1, and would give an infinite descending chain in
\(\mathbb N^2\). This proves triadic closure. There is no assumption
about the number of inverse words, the number of eventual cycles, or a
uniform source-height bound.

## 3. What Lean proves

[TriadicDualClosure.lean](lean/TriadicDualClosure.lean) defines the three
integer transition rules, the literal shortcut orbit, and a deterministic
trajectory from the single finite state \((n,a,r)\).

Its main declaration is

```text
alltime_triadic_candidate_reaches_one
```

It proves that if every actual parity test on that trajectory passes,
then the ordinary shortcut orbit of the original positive integer reaches
1. The module also checks the rational interpretation (5), the all-odd
tail contradiction, exclusion of zero numerators on an all-time path,
the complete rank decrease, and equality of the stored first coordinate
with the literal ordinary orbit at every clock.

The finite bound in the next section has a written proof; it is not
presented as a Lean theorem. Neither the existence of \(a,r\) for an
arbitrary \(n\) nor the 2-adic construction of \(\Omega\) is encoded as
an axiom. The [audit](lean/TriadicDualAudit.lean) and
[execution receipt](../../../reports/2026-11-23-global-closure/duality-lean-receipt.json)
record the exact formal scope.

## 4. An explicit finite congruence and height target

Here is a finite arithmetic condition sufficient for full convergence.
It avoids placing an unverifiable infinite-parity premise inside the
construction target.

For \(m\ge0\), define

\[
 \operatorname{bl}(m)=\min\{L\ge1:m<2^L\}.
\]

Fix \(n>0\), \(a\in\mathbb Z\), \(r\ge0\), and put

\[
\begin{split}
 N&=\operatorname{bl}(n),\\
 B&=\max(1,|a|,3^r),\qquad L=\operatorname{bl}(B),\\
 R&=rL,\qquad E=N+L+R,\\
 \boxed{H(n,a,r)=R+8E+2=8N+(9r+8)L+2.}                       \tag{10}
\end{split}
\]

Read the **actual** first \(H\) parities \(e_0,\ldots,e_{H-1}\)
of the fixed ordinary input \(n\), and let

\[
 b_i=\sum_{j<i}(1-e_j),\quad D_0=0,\quad
 D_{i+1}=3^{1-e_i}D_i+(1-e_i)2^i.                            \tag{11}
\]

Here \(D_i\) is the complete ordered affine carry for the complementary
word. There is no replacement of the word by its count or convex hull.

> **Finite triadic certificate.** If
>
> \[
>             \boxed{2^H\mid3^{b_H}a+3^rD_H,}              \tag{12}
> \]
>
> then the original ordinary input \(n\) reaches 1 by clock \(H\).

### 4.1 Congruence means the entire supplied prefix is legal

The complementary affine word sends \(a/3^r\) to

\[
              \frac{3^{b_H}a+3^rD_H}{3^r2^H}.              \tag{13}
\]

Condition (12) says that the terminal value has odd denominator. Pulling
back the literal word from that terminal value uses \(y\mapsto2y\)
on a zero bit and \(y\mapsto(2y-1)/3\) on a one bit. Each inverse
imposes its displayed parity and keeps an odd denominator. Consequently
(12) gives opposite parity at *all* of the first \(H\) starting states,
not only an affine equality at the final state.

### 4.2 Exhausting the denominator has an elementary clock bound

While \(r_j>0\), equation (4) and \(3^{r_j-1}\le B\) give

\[
                              |w_j|\le B.                    \tag{14}
\]

This holds initially and is preserved by both relevant rows of (4).
At a fixed positive denominator exponent, \(L\) consecutive original-odd
steps would divide a nonzero integer numerator by \(2^L>B\), which is
impossible while all the divisions remain integral. Therefore, unless
a zero numerator or \(x=1\) is met first, each denominator level is
consumed in at most \(L\) steps. By some clock \(j\le R=rL\), the
candidate has reached \(r_j=0\), a zero numerator, or the ordinary
terminal state.

Every positive ordinary shortcut step satisfies \(x_{i+1}\le2x_i\).
Thus

\[
                     x_j\le n2^j\le n2^R.                  \tag{15}
\]

If a zero numerator is reached by \(j\le R\), compatibility through
clock \(H\) would make the next \(H-j\) ordinary starting states odd.
Equation (6) then implies
\(2^{H-j}\mid x_j+1\). But \(x_j+1\le2^{N+R}\), whereas
\(H-j\ge H-R>N+R\). This is impossible. Zero is therefore included
in the finite bound, not silently discarded.

### 4.3 The integral pair has a logarithmic termination budget

Suppose \(r_j=0\), \(w_j\ne0\), and no ordinary state has reached 1.
An integral numerator cannot subsequently become zero: halving an even
nonzero integer is nonzero, and \(3w+1=0\) has no integer solution.

For every compatible integral step, \(P_i=x_i|w_i|\) does not increase.
It contracts by at least \(5/6\), except when \(w_i=1\). In that case
\(w_{i+1}=2\); compatibility at the next state forces its original
coordinate to be odd, and, if it is not 1, the next step contracts by
at least \(5/6\). Hence

\[
                   P_{i+2}\le(5/6)P_i.                     \tag{16}
\]

The initial integral product satisfies

\[
                        P_j\le nB2^R<2^E.                  \tag{17}
\]

The exact inequality \(6^4>2\cdot5^4\) gives

\[
                  (5/6)^{4E}2^E<1.                         \tag{18}
\]

After \(8E\) further compatible steps avoiding 1, equations
(16)–(18) would force the positive integer product below 1. Since
\(j+8E\le R+8E<H\), this is a contradiction. This proves (12).

The constants in (10) are chosen for a short integer proof. Optimizing
them is not the construction problem pursued here.

## 5. The attempted universal construction

The desired source lemma can now be stated without an all-time dual:

> **OPEN — source-dependent small triadic residue.** For every fixed
> positive ordinary \(n\), find \(K,a,r\) with
> \(K\ge H(n,a,r)\) and
> \[
>                    2^K\mid3^{b_K}a+3^rD_K,               \tag{19}
> \]
> where \(b_K,D_K\) are obtained from that same original input and
> the complete actual \(K\)-step word.

A solution to this lemma would prove the full theorem by Section 4.
Conversely, a convergent input supplies one exact triadic dual through
(2); it satisfies (19) at every \(K\), including one beyond its own
height budget. Thus this is an exact full-strength construction target.
No length, denominator, numerator, or alternative clock is bounded in
advance independently of \(n\).

### 5.1 Centered residues do not supply the needed height

Let

\[
          \omega_K\equiv-3^{-b_K}D_K\pmod{2^K}.             \tag{20}
\]

For each proposed \(r\), condition (19) asks for a representative

\[
                         a\equiv3^r\omega_K\pmod{2^K}.     \tag{21}
\]

Choosing a centered representative always gives
\(|a|\le2^{K-1}\). In general this has \(\operatorname{bl}(|a|)\)
of order \(K\), whereas (10) requires

\[
        \operatorname{bl}(B)
           \le\frac{K-8\operatorname{bl}(n)-2}{9r+8}.       \tag{22}
\]

The natural complementary carry itself has denominator \(3^{b_K}\),
so substituting that exponent without a separate height improvement does
not establish (22).

A general 2-adic approximation theorem cannot give this budget uniformly
for arbitrary \(\omega_K\). Here is a direct counting reason, requiring
no asymptotic equidistribution hypothesis. Any pair satisfying (22) has
\(r\le K\) and \(\operatorname{bl}(|a|)\le\lfloor K/8\rfloor\).
Thus all such pairs represent at most

\[
             (K+1)\bigl(2^{\lfloor K/8\rfloor+1}+1\bigr)  \tag{23}
\]

residue classes modulo \(2^K\). This is exponentially fewer than
\(2^K\) for large \(K\). Duplicated representations only decrease the
count. This does **not** refute (19): the actual \(\omega_K\) of one
fixed positive ordinary input is a highly specific residue. It shows
why unrestricted rational approximation or merely increasing a finite
list of denominator exponents cannot supply the missing universal
source lemma.

### 5.2 The two actual carries: what the direct cancellation attempt gives

Let \(C_0=0\) and

\[
 C_{i+1}=3^{e_i}C_i+e_i2^i,\qquad s_i=i-b_i.
\]

The original ordinary coordinate gives the strong congruence

\[
           U_i:=3^{s_i}n+C_i=2^i x_i,
           \qquad C_i\equiv-3^{s_i}n\pmod{2^i}.            \tag{24}
\]

I tried to combine (24) with \(D_i\) to force the small representative
in (21), using determinant and product identities rather than treating
the complementary word as an independent random word.

The determinant-like carry

\[
                    W_i=3^{b_i}C_i-3^{s_i}D_i
\]

has the exact recurrence

\[
 W_{i+1}=\begin{cases}
 3W_i+2^i3^{b_i},&e_i=1,\\
 3W_i-2^i3^{s_i},&e_i=0.
 \end{cases}                                                 \tag{25}
\]

It is odd for every \(i\ge1\). Substitution of (24) gives

\[
          W_i\equiv-3^{s_i}(3^{b_i}n+D_i)\pmod{2^i}.        \tag{26}
\]

These are exact coupled identities. They do not give an upper bound for
the centered residue in (21). In particular, the two signs in (25)
retain the original word; replacing them by average cancellation would
be an additional, unsupported estimate.

The product route is also exact. Put
\(z_i=D_i/2^i\) and \(P_i=x_i z_i\). This is a real forced
complementary trajectory starting at zero, not an asserted rational
parity dual. Directly from the two carries,

\[
 P_{i+1}=\begin{cases}
 (3/4)P_i+z_i/4,&e_i=1,\\
 (3/4)P_i+x_i/4,&e_i=0.
 \end{cases}                                                 \tag{27}
\]

The original-even forcing term contains the actual \(x_i\). I did
not bound it uniformly along the unknown ordinary trajectory. Moreover,
(21) depends on the carry modulo \(2^i\), so a bound on an uncentered
real product would still have to preserve that exact residue. Equations
(25)–(27) therefore do not provide the height saving in (22).

## 6. Relation to the newest repository work and stopping point

The current complete-source-cut work in PR180 allows all replacement
lengths and shows why source minima and positive boundary mass alone do
not force a cheaper source across the actual target floor. The present
lane retains the original input while changing the witness object to a
signed triadic dual. It does not claim that the source-cut theorem
constructs this dual.

PR176's current Mahler attempt correctly leaves finite extraction rank
unproved. No finite-rank or separate Mahler equations were obtained here
for the dual carries either. Monks–Yazinski supplies the parity-dual
framework; it does not supply (19). The exact read sources are in the
[source receipt](../../../reports/2026-11-23-global-closure/duality-sources.json).

The central advance of this lane is a **formal full-convergence closing
mechanism** once a triadic dual is constructed, plus a finite source
condition that would construct one strongly enough to close. The
unproved step is precisely the source-dependent small-residue assertion
(19). No finite approximation, generic rationality principle, or
unproved carry cancellation is used to assert it.
