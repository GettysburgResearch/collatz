# L-9865 -- Exact 64-bucket order statistics for survivor width lifts

Claim ID: `L-9865`  
Title: One width extension reduces the live minimum and successor to bucket-local candidates  
Status: `PROPOSED`  
Authoring agent: `gpt56-synthesis-01-a`  
Reviewing agents: `gpt56-synthesis-01-h`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9812`, `L-9815`, `L-9834`, `L-9847`, `L-9853`  
Scope: exact ordinary order statistics under one `64^n -> 64^(n+1)` survivor-width lift  
Related counterexample candidates: none

## Definitions

Put `Q_n=64^n`.  For `0<=j<n`, let

\[
\gamma_j^{(n)}
=\left[17\,64^j81^{-(j+1)}\right]_{Q_n},
\qquad
\alpha_n(\varepsilon)
=\left[\sum_{j=0}^{n-1}\varepsilon_j\gamma_j^{(n)}\right]_{Q_n},
\quad
\varepsilon\in\{0,1\}^n.
\tag{1}
\]

These are the standard depth-`n` survivor representatives.  Write

\[
\gamma_j^{(n)}=64^j\omega_{j,n},
\qquad
81^{j+1}\omega_{j,n}
=17+64^{n-j}q_{j,n},
\qquad
d_{j,n}
=\left[-q_{j,n}81^{-(j+1)}\right]_{64}.
\tag{2}
\]

For an old word `epsilon`, retain the unreduced coefficient sum, its
ordinary carry, and its next lift digit:

\[
\begin{aligned}
S_n(\varepsilon)
&=\sum_{j=0}^{n-1}\varepsilon_j\gamma_j^{(n)},\\
x_n(\varepsilon)
&=[S_n(\varepsilon)]_{Q_n}
=\alpha_n(\varepsilon),\\
\kappa_n(\varepsilon)
&=\left\lfloor\frac{S_n(\varepsilon)}{Q_n}\right\rfloor,\\
D_n(\varepsilon)
&=\left[
\kappa_n(\varepsilon)
+\sum_{j=0}^{n-1}\varepsilon_jd_{j,n}
\right]_{64}.
\end{aligned}
\tag{3}
\]

The new-coordinate digit is

\[
e_n
=\left[17\,81^{-(n+1)}\right]_{64}
=\left[17^{-n}\right]_{64}
\in\{1,49,33,17\},
\tag{4}
\]

with the four values listed in order of `n modulo 4`.

For `n>=2`, denote the first two nontrivial ordinary survivor
representatives by

\[
M_n^{[1]}
<M_n^{[2]},
\qquad
\{M_n^{[1]},M_n^{[2]}\}
\subset
\{\alpha_n(\varepsilon):
\varepsilon\ne0^n,1^n\}.
\tag{5}
\]

Thus `M_n^[1]` is the minimum `M_n` of `L-9812`, while
`M_n^[2]` is its next depth-`n` survivor.

For a finite ordered list `L`, let `head_2(L)` be its first at
most two entries and `tail_1(L)` its last entry when nonempty.  All
lists below retain their labels, even when only their numerical keys are
displayed.

## Statement

### 1. Exact full-survivor width lift, including the new bit

Every old coefficient has the exact ambient lift

\[
\boxed{
\gamma_j^{(n+1)}
=\gamma_j^{(n)}+Q_nd_{j,n}
\qquad(0\le j<n),
}
\tag{6}
\]

and the new coefficient is

\[
\boxed{
\gamma_n^{(n+1)}=Q_ne_n.
}
\tag{7}
\]

Consequently, for every old word `epsilon` and new bit
`b in {0,1}`,

\[
\boxed{
\alpha_{n+1}(\varepsilon,b)
=x_n(\varepsilon)
+Q_n
\left[D_n(\varepsilon)+be_n\right]_{64}.
}
\tag{8}
\]

The bracket in (8) is essential: the `b=1` copy can wrap from a high
old lift digit into a low new bucket.

The two constant words satisfy

\[
\boxed{
x_n(0^n)=0,\quad D_n(0^n)=0,
\qquad
x_n(1^n)=1,\quad
D_n(1^n)=-e_n\pmod {64}.
}
\tag{9}
\]

Hence the two excluded words `(0^n,0)` and `(1^n,1)` both lie
in new bucket zero.  Their siblings `(0^n,1)` and
`(1^n,0)` are nontrivial and must not be discarded.

### 2. Translated fibers acquire one additional carry bit

Let `h_N(c) in [0,Q_N)` be any translation fiber with compatible lift

\[
h_{N+1}(c)
=h_N(c)+Q_ND_N(c),
\qquad
D_N(c)\in\{0,\ldots,63\},
\tag{10}
\]

as in `L-9853/(10)`.  Let a base point have compatible lift

\[
a_{N+1}=a_N+Q_NA_N,
\qquad
0\le a_N<Q_N,
\quad
A_N\in\{0,\ldots,63\}.
\tag{11}
\]

Put

\[
z_N(c)=[a_N+h_N(c)]_{Q_N},
\qquad
\chi_N^a(c)
=\left\lfloor\frac{a_N+h_N(c)}{Q_N}\right\rfloor
\in\{0,1\}.
\tag{12}
\]

Then the exact translated-point lift is

\[
\boxed{
z_{N+1}(c)
=z_N(c)+Q_NB_N^a(c),
\qquad
B_N^a(c)
=\left[A_N+D_N(c)+\chi_N^a(c)\right]_{64}.
}
\tag{13}
\]

Thus translating a fiber does not merely add the base lift digit.  The
ordinary lower-width wrap `chi_N^a(c)` also changes its 64-bucket.

For two compatibly lifted endpoints `z_N^a(c),z_N^b(c)`, define

\[
g_N(c)
=\left[z_N^b(c)-z_N^a(c)\right]_{Q_N}
\in\{1,\ldots,Q_N-1\},
\qquad
w_N(c)=\mathbf1_{\{z_N^b(c)<z_N^a(c)\}}.
\tag{14}
\]

If their bucket digits in (13) are `B_N^a(c)` and
`B_N^b(c)`, then their oriented signed gap lifts by

\[
\boxed{
g_{N+1}(c)
=g_N(c)
+Q_N
\left[
B_N^b(c)-B_N^a(c)-w_N(c)
\right]_{64}.
}
\tag{15}
\]

Formula (15) includes both the old circular wrap and the new bucket wrap.
It is the width-lift companion to the signed translation fibers of
`L-9847`.

### 3. Exact order statistics of an arbitrary 64-bucket lift

Let `I` be a finite label set with at least two elements and distinct old representatives
`z_N(i) in [0,Q_N)` and compatible lifts

\[
z_{N+1}(i)=z_N(i)+Q_NB(i),
\qquad
B(i)\in\{0,\ldots,63\}.
\tag{16}
\]

For each bucket, order

\[
I_t=\{i\in I:B(i)=t\}
\quad\text{by increasing }z_N(i).
\tag{17}
\]

The complete increasing list at width `N+1` is the concatenation

\[
\boxed{
I_0,\ I_1,\ \ldots,\ I_{63},
}
\tag{18}
\]

with each list retaining its old order.  In particular, let
`t_0` be the least nonempty bucket.  The minimum is the first entry of
`I_(t_0)`.  Its successor is the second entry of that same bucket when
one exists; otherwise it is the first entry of the next nonempty bucket:

\[
\boxed{
\begin{aligned}
z_{N+1}^{[1]}
&=Q_N\,t_0+z_N\!\left(I_{t_0}^{[1]}\right),\\
z_{N+1}^{[2]}
&=
\begin{cases}
Q_N\,t_0+z_N\!\left(I_{t_0}^{[2]}\right),
&|I_{t_0}|\ge2,\\
Q_N\,t_1+z_N\!\left(I_{t_1}^{[1]}\right),
&|I_{t_0}|=1,
\end{cases}
\end{aligned}
}
\tag{19}
\]

where `t_1>t_0` is the next nonempty bucket in the second case.

If `t_*` is the largest nonempty bucket, the maximum is the last entry
of `I_(t_*)`.  Hence the two gaps adjacent to the new minimum in the
cyclic ordering of this same label set are

\[
\boxed{
\begin{aligned}
\Delta_+
&=z_{N+1}^{[2]}-z_{N+1}^{[1]},\\
\Delta_-
&=64Q_N-
\left(Q_N\,t_*+z_N(I_{t_*}^{[-1]})\right)
+z_{N+1}^{[1]}.
\end{aligned}
}
\tag{20}
\]

Thus `head_2(I_t)` for every bucket determines the first two order
statistics, while `tail_1(I_t)` additionally determines the cyclic
wrap predecessor.

### 4. Two-source merge recursion for the actual minimum and successor

For an output bucket `t in {0,...,63}`, define two old source lists,
ordered by increasing `x_n(epsilon)`,

\[
\boxed{
\begin{aligned}
\mathcal L_{t,0}
&=\{\varepsilon:
D_n(\varepsilon)=t,\ \varepsilon\ne0^n\},\\
\mathcal L_{t,1}
&=\{\varepsilon:
D_n(\varepsilon)=t-e_n\pmod {64},\
\varepsilon\ne1^n\}.
\end{aligned}
}
\tag{21}
\]

The first list supplies new bit zero, and the second supplies new bit one.
The complete nontrivial output-bucket list is the stable merge

\[
\boxed{
\mathcal B_t
=\operatorname{merge}_{x_n}
\left(
\mathcal L_{t,0}\times\{0\},
\mathcal L_{t,1}\times\{1\}
\right).
}
\tag{22}
\]

Its first two entries lie in the fixed candidate set

\[
\boxed{
\operatorname{head}_2(\mathcal B_t)
\subseteq
\operatorname{head}_2(\mathcal L_{t,0})
\cup
\operatorname{head}_2(\mathcal L_{t,1}),
}
\tag{23}
\]

which has at most four labeled words.  Its last entry is the larger of the
two available source tails.

Let `r_t=|mathcal B_t|`, let `t_0` be the least index with
`r_t>0`, and write `p_t^[j]` for the old lower representative
of the `j`-th entry of `mathcal B_t`.  Then

\[
\boxed{
\begin{aligned}
M_{n+1}^{[1]}
&=Q_n\,t_0+p_{t_0}^{[1]},\\
M_{n+1}^{[2]}
&=
\begin{cases}
Q_n\,t_0+p_{t_0}^{[2]},&r_{t_0}\ge2,\\
Q_n\,t_1+p_{t_1}^{[1]},&r_{t_0}=1,
\end{cases}
\end{aligned}
}
\tag{24}
\]

where `t_1` is the next occupied bucket when needed.

More explicitly, the actual forward successor gap is

\[
\boxed{
M_{n+1}^{[2]}-M_{n+1}^{[1]}
=
\begin{cases}
p_{t_0}^{[2]}-p_{t_0}^{[1]},&r_{t_0}\ge2,\\
(t_1-t_0)64^n+p_{t_1}^{[1]}-p_{t_0}^{[1]},
&r_{t_0}=1.
\end{cases}
}
\tag{25}
\]

The second line is the exact cross-bucket competition term.  Once the two
selected labels are known, their signed word and common-translation label
are those of `L-9847/(8)`; because the two values are consecutive in
the full survivor order above `0,1`, all isolation inequalities
`L-9847/(11)--(13)` apply to this actual selector.

### 5. Exact finite reduction and its information boundary

For one width extension, the live selector factors through:

- the 64 source-bucket occupancies;
- the first two old representatives in each of the two source lists (21);
- and, for the cyclic predecessor, the last representative in each source.

Thus the first two new representatives require at most four local candidates
per output bucket, at most `256` labeled candidates before the least
occupied bucket is known.  This is a fixed finite candidate reduction, not a
search over all pairwise signed differences.

It is not an autonomous recursion from the two unpartitioned numbers
`M_n^[1],M_n^[2]`.  Even in the abstract lift (16), three old points
`a<b<c` with bucket digits `(1,1,0)` have new minimum `c`,
whereas the same old order statistics with digits `(0,1,1)` have new
minimum `a`.  Therefore the old first two values alone do not determine
the next first value.  This example concerns the general 64-bucket mechanism;
it does not prove that no smaller survivor-specific state exists.

## Proof

### Coefficient and full-word lifts

From (2), the definition of `d_(j,n)` gives

\[
81^{j+1}
\left(\omega_{j,n}+64^{n-j}d_{j,n}\right)
\equiv17\pmod {64^{n-j+1}}.
\tag{26}
\]

The quantity in parentheses is in the canonical interval
`[0,64^(n-j+1))`, so it is `omega_(j,n+1)`.  Multiplication by
`64^j` proves (6).  Formula (7) follows directly by dividing the new
coefficient by `Q_n`.

Using (6)--(7), the unreduced sum at the new width is

\[
\begin{aligned}
S_{n+1}(\varepsilon,b)
&=S_n(\varepsilon)
+Q_n\sum_{j<n}\varepsilon_jd_{j,n}
+bQ_ne_n\\
&=x_n(\varepsilon)
+Q_n
\left(
\kappa_n(\varepsilon)
+\sum_{j<n}\varepsilon_jd_{j,n}
+be_n
\right).
\end{aligned}
\tag{27}
\]

Reduction modulo `64Q_n` proves (8).

The zero-word assertions in (9) are immediate.  For the one-word, the finite
geometric sum gives

\[
\sum_{j=0}^{n-1}
17\,64^j81^{-(j+1)}
=1-64^n81^{-n}
\equiv1\pmod {64^n}.
\tag{28}
\]

Applying (8) to the all-one extension and using
`alpha_(n+1)(1^(n+1))=1` gives
`D_n(1^n)+e_n=0 modulo 64`, completing (9).

### Translation carry and signed-gap lift

Equations (10)--(12) give

\[
\begin{aligned}
a_{N+1}+h_{N+1}(c)
&=a_N+h_N(c)+Q_N(A_N+D_N(c))\\
&=z_N(c)
+Q_N\bigl(\chi_N^a(c)+A_N+D_N(c)\bigr).
\end{aligned}
\tag{29}
\]

Reduction modulo `64Q_N` proves (13).

The definition of `w_N` gives the ordinary identity

\[
z_N^b(c)-z_N^a(c)
=g_N(c)-Q_Nw_N(c).
\tag{30}
\]

Add the two lift digits to (30) and reduce the coefficient of `Q_N`
modulo 64.  Since `0<g_N(c)<Q_N`, the resulting representative is
already in `(0,64Q_N)`.  This proves (15).

### Bucket order and the two-source selector

For two lifted labels `i,i'`, ordinary comparison first compares
`B(i)` and `B(i')`; only when those digits agree does it compare
`z_N(i)` and `z_N(i')`.  This proves the concatenation (18),
the first-two recursion (19), and the maximum and wrap formulas (20).

For the full survivor lift, equation (8) places a new-bit-zero word in bucket
`t` exactly when `D_n(epsilon)=t`, and a new-bit-one word there
exactly when `D_n(epsilon)=t-e_n modulo 64`.  Equation (9) shows that
the exclusions in (21) remove exactly the two trivial new words and no
others.  Within a common output bucket, (8) compares only
`x_n(epsilon)`, proving the stable merge (22).

In the merge of two ordered lists, an entry below the first two of its own
source has at least two same-source predecessors, so it cannot belong to the
first two of the merge.  This proves (23).  Applying (19) to the merged
lists proves (24), and subtraction gives (25).

Finally, after deleting the two trivial representatives `0` and `1`, the
selected values are consecutive; hence no survivor lies strictly between
them, and they are a successor edge of the complete survivor list.  The
translation representation and isolation
test of `L-9847` apply verbatim.  The three-point example in part 5
proves the stated failure of the unpartitioned two-number summary and
completes the claim. QED

## Motivation

`L-9847` turns a proposed successor edge into a pointed isolation
problem inside one signed translation fiber.  `L-9853` shows that the
fiber order changes by an exact 64-bucket lift and that neither inverse-unit
digits nor subset-sum carries may be omitted.  What was still absent was a
live selector: an exact rule locating the actual minimum and its successor
after the next width is added.

The present claim supplies that rule.  A new survivor bit creates two source
lists per output bucket, separated by the odd periodic digit `e_n`.
Only the first two entries of each source can affect the new minimum and
successor.  The resulting selected pair can then be fed into the signed-fiber
isolation test, with every lower carry, bucket wrap, and cross-bucket gap kept
exact.

## Dependency audit

- `L-9812` supplies the interpretation of `M_n^[1]` as the
  nontrivial survivor minimum.
- `L-9815` supplies the ordinary successor viewpoint.
- `L-9834` supplies injectivity of the survivor coding, so all ordered
  lists have distinct numerical keys.
- `L-9847` supplies the signed common-translation fiber and the exact
  two-sided isolation test for the selected successor edge.
- `L-9853` supplies the ambient lift digits for a fixed translation
  fiber; equations (6)--(8) add the full new survivor coordinate.
- The translated-base carry, signed-gap lift, bucket-local order statistics,
  and two-source live selector are proved directly here.
- No numerical minimum certificate, randomness, equidistribution, or
  asymptotic cancellation estimate is used.

## Gap audit

- The bucket recursion is exact after the partition by `D_n(epsilon)`
  is known.  Constructing all 64 source heads without further structure may
  still require exponentially many old words.
- The result reduces the selector to fixedly many candidates for one width
  extension; it does not propagate those bucket heads by a bounded-state
  recurrence across all widths.
- The abstract three-point example rules out only the unpartitioned
  first-two summary.  It is not a survivor-specific lower bound on every
  possible compressed state.
- Signed-fiber isolation remains necessary rather than sufficient against
  survivor points outside that fiber.
- No lower bound on the actual gap (25), no repeated failure of renewal, and
  no divergence of `M_n^[1]` is proved.
- The cyclic wrap formula (20) concerns the same label set being sorted; it
  must not be silently substituted for a predecessor in a different enlarged
  survivor set.

## Adversarial tests

- The raw carry `kappa_n(epsilon)` in (3) is part of the bucket digit.
  Summing only the coefficient lift digits gives the wrong order.
- The new-bit-one bucket is `[D_n+e_n]_64`; replacing it by ordinary
  addition loses the wrap into low buckets.
- Both trivial extensions land in bucket zero, but their two sibling
  extensions are nontrivial candidates in buckets `e_n` and
  `-e_n`.
- The first two entries of a bucket require both source heads.  Keeping only
  the smaller source head misses same-source second place.
- When the least occupied bucket is a singleton, the successor comes from the
  next occupied bucket and its gap contains the signed lower-coordinate term
  in (25); it is not merely one bucket width.
- Formula (13) contains the lower translation carry `chi_N^a(c)`.
  Omitting it can move a translated point by a whole bucket.
- Formula (15) contains the old endpoint wrap `w_N(c)`.  Omitting it
  changes the lifted signed gap by `Q_N`.
- The isolation inequalities are applied only after the actual two labels are
  selected; exceptional points of an ambient subfiber are not promoted to
  live successors.

## Remaining uncertainty

Can the first two entries of all source lists in (21) be updated from one
width to the next by a finite family of signed-carry sections?  A positive
answer would turn the one-step candidate reduction into a true bounded-state
minimum/successor selector.  A negative answer would require a
survivor-specific family in which arbitrarily deep entries of an old bucket
become new bucket leaders.

## Suggested next attack

Attach to each source head its endpoint residue, signed-difference label, and
next coefficient-lift digit.  Refine the 64 buckets by these finite data and
test whether the two-source merge closes under one more lift.  If it does,
combine the resulting finite selector with `L-9847/(11)--(13)`; if it
does not, extract two survivor words with identical proposed summary but
opposite next bucket order.
