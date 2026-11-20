# A larger physical five renewal with correlated endpoint residues

**PROPOSED.** Three new physical families enlarge the complete ladder of
PR166. Retaining their common ternary endpoint residue gives strict
contraction at the harmonic and `21/25` exponents. A further decomposition
handles every first valuation at least three at the cost of a specified
sparse adjacent energy. That remainder is not bounded here. Collatz is
not proved.

Use the positive shortcut map `T` and odd map
`U(n)=(3n+1)/2^v2(3n+1)`. Let `f` take values in a metric space and
satisfy `f(Tn)=f(n)` for every positive integer. Put

\[
e(x)=d(f(5x),f(x)),\qquad
E_s(X)=\sum_{\substack{0<x\le X\\x\text{ odd},\;3\nmid x}}x^{-s}e(x).
\tag{1}
\]

Finite-cutoff sums are finite; infinite sums are nonnegative extended
quantities. In particular `e(1)=0`, by the known path from 5 to 1.
Every contributing odd ternary-unit endpoint is at least 5.

## Exact dependencies

The old ladder is PR166, `5996b9f525ca50978bc34f423192c36a87765bf3`,
`research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md`,
FL1--FL3. Its renewal is `LADDER_RENEWAL.md`, R1--R6. The earlier PR162
block and PR163 single-cylinder estimate are credited there.

The three new words were supplied by the parallel five-certificate
author, then independently reconstructed here. The exact source is
`HOMOGENEOUS_FIVE_TRANSPORT.md`, SHA-256
`f2872fad5c04e3aba9219f4b54576ef438d2922d7dcad9b0a8423974c4d2c31b`,
HT3--HT4. Their general decoder and complete four-odd-step classification
belong to that companion proof. This note needs only the three identities,
also proved directly below. Its additional content is their simultaneous
residue-conditioned all-source congestion bound.

The implication from finite five energy to rigidity is the separate
PR163 theorem, `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
`research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, FE1 and
Section 4. Its harmonic consequence retains its positive-density input;
its `21/25` consequence retains its predecessor-count input. Neither
external input is needed for the elementary inequalities here.

## ER1. Combined physical domain

The old domain `H_0` consists of actual exponent prefixes `(2^r,b)`,
where `r>=1` denotes repeated letters two and `b>=4`. Its odd unit
endpoint `q` satisfies

\[
x=\frac{2^{2r+b}q-B_r}{3^{r+1}},\quad B_r=4^{r+1}-3^{r+1},
\quad q\le x/7,\quad T^{2r+b}(5x)=5q.
\tag{2}
\]

Thus `e(x)=e(q)`. This domain has relative density `1/24` among odd
ternary units and lies in `x=1 mod16`.

Add these families, always restricting the source to a ternary unit:

| `a` | Source word | Guard | Target word from `5x` | `B` | Source cylinder |
| ---: | --- | --- | --- | ---: | --- |
| 1 | `(1,1,1,b)` | `b>=6` | `(1,2,5,b-5)` | 65 | `271 mod512` |
| 2 | `(1,1,2,b)` | `b>=4` | `(1,5,1,b-3)` | 73 | `135 mod256` |
| 4 | `(1,1,4,b)` | `b>=4` | `(1,3,5,b-3)` | 121 | `87 mod1024` |

Writing `L=a+2+b`, their exact identities are

\[
\boxed{x=\frac{2^Lq-B}{81},\qquad T^L(x)=q,\qquad T^L(5x)=5q.}
\tag{3}
\]

For four odd inputs at positions `0,A_1,A_2,A_3`, the correction is
`27+9*2^A_1+3*2^A_2+2^A_3`. The source corrections are `65,73,121`;
the target corrections are exactly five times these. Both clocks are
`L`. Full numerator divisibility gives all successive inverse divisions:
reduce modulo three, divide, and repeat. Positive exponents make each
integral inverse state odd. An integral inverse `(2^a v-1)/3` of a
positive odd integer, with `a>=1`, is positive. Hence these are actual
ordinary paths, not only rational affine identities.

The cylinders follow from `81x+B=0 mod2^(a+2+b_min)`. Exact affine
parity checks give the first three valuations `(1,1,a)` on every lift,
and final valuation at least `b_min`. The actual last valuation supplies
the unique complete row word. The three cylinders are pairwise disjoint
and outside `H_0`.

Every new endpoint has `q<=x/3`: use
`q<=(81x+B)/2^(a+2+b_min)`. For `a=1,4` the claim holds on every
positive source in the cylinder. For `a=2` it reduces to `13x>=219`,
where the least source is 135.

Let `H` be this union. Its relative natural density is

\[
\frac1{24}+\frac1{256}+\frac1{128}+\frac1{512}
=\boxed{\frac{85}{1536}}.
\tag{4}
\]

The old ladder tail has the controlled density established in FL3;
the added union is finite. Thus natural density here does equal the
sum of the disjoint binary cylinder measures.

## ER2. Correlated inverse-fiber estimate

For an endpoint `q>=5`, fix `c=q mod81`, `1<=c<=80`, `3 not dividing c`.
Let `q_c` be the least odd integer at least 5 in that residue. Let
`b_r(c)` be the least `b>=4` satisfying

\[
2^{b-2}c=1\pmod{3^{r+1}},\qquad r=1,2,3.
\tag{5}
\]

The class has period `P_r=2*3^r`. Indeed `2^2=1+3`, and every cubing
increases the ternary valuation of the difference from one by one.
For `r=1,2`, put

\[
A_r(c)=\frac{3^{r+1}}{2^{2r+b_r(c)}-B_r/q_c}.
\tag{6}
\]

All legal inverse sources at fixed `r,q` have `b=b_0+jP_r`.
Equation (2) gives `x_(b_0+jP_r)>=2^(jP_r)x_b_0`. Therefore

\[
\sum_b(q/x_b)^s\le\frac{A_r(c)^s}{1-2^{-P_rs}}.
\tag{7}
\]

Keeping sources divisible by three, which the actual domain deletes,
only increases this bound.

For `r>=3`, legality implies (5) at `r=3`, so `b_0>=b_3(c)` and
`P_r>=54`. Also

\[
x_b=1+(4/3)^r(2^bq-4)/3
\ge (4/3)^r(2^{b_3(c)}-4/q_c)q/3.
\]

Set `Z_s=(3/4)^s` and `A_infty(c)=3/(2^b_3(c)-4/q_c)`. The full
infinite ladder tail is bounded by

\[
\sum_{r\ge3,b}(q/x_b)^s
\le\frac{A_\infty(c)^s Z_s^3}{(1-Z_s)(1-2^{-54s})}.
\tag{8}
\]

For each new row `(a,B,b_min)`, let `d_a(c)` be the least `b>=b_min`
with `2^(a+2+b)c=B mod81`, and put

\[
G_a(c)=\frac{81}{2^{a+2+d_a(c)}-B/q_c}.
\tag{9}
\]

Its inverse exponents have period 54. Positivity of `B` gives the
same geometric comparison, so its contribution is at most
`G_a(c)^s/(1-2^(-54s))`. Combining all families, define

\[
\Gamma_s(c)=\frac{A_1(c)^s}{1-2^{-6s}}
+\frac{A_2(c)^s}{1-2^{-18s}}
+\frac{A_\infty(c)^s Z_s^3}{(1-Z_s)(1-2^{-54s})}
+\frac{G_1(c)^s+G_2(c)^s+G_4(c)^s}{1-2^{-54s}}.
\tag{10}
\]

The crucial point is to add at one common endpoint residue before
maximizing. The complete 54-residue certificate gives

\[
\boxed{\Gamma_1(c)<5/8,\qquad\Gamma_{21/25}(c)<91/100.}
\tag{11}
\]

At exponent one all comparisons are rational. For exponent `21/25`,
each rational power `v^(21/25)` is enclosed above by the least `k/10^9`
such that `k^25 denom(v)^21 >= 10^225 num(v)^21`. Upper bounds are
used in positive numerators and in `1-upper` denominators. No floating
point is used. The largest certified grid bounds for (10) are
`620437297/10^9` at `c=43` and `905153231/10^9` at `c=61`.

## ER3. Renewal and finite-energy equivalence

Let `R_s(X)` be (1) restricted to `x outside H`. Then

\[
\boxed{E_1(X)\le R_1(X)+\frac58 E_1(X/3),}
\qquad
\boxed{E_{21/25}(X)\le R_{21/25}(X)
                         +\frac{91}{100}E_{21/25}(X/3).}
\tag{12}
\]

Every source in `H` has one actual endpoint `q<=X/3`, with `e(x)=e(q)`.
Group the nonnegative terms by endpoint and apply (10)--(11). No
bounded-label or initial summability assumption enters the proof.

Since `E_s(X/3)<=E_s(X)`, subtract at finite cutoffs and then take
monotone limits. Full energy is finite exactly when the corresponding
remainder is finite, and in that case

\[
\boxed{E_1(\infty)\le\frac83R_1(\infty),\qquad
E_{21/25}(\infty)\le\frac{100}{9}R_{21/25}(\infty).}
\tag{13}
\]

This improves both the renewable domain and comparison factors of the
pinned PR166 result. The complement remains infinite; its density alone
does not bound the defect energy of an unknown invariant label.

## ER4. Exact attempt to eliminate every larger first valuation

For a source with first valuation `a>=3`, put `q=U(x)` and `b=a-2`.
Two actual shortcut steps give

\[
T^2(5x)=5\,2^bq-1,\qquad f(5\,2^bq)=f(5q).
\]

Consequently

\[
e(x)\le e(q)+j_a(q),\qquad
j_a(q)=d(f(5\,2^{a-2}q-1),f(5\,2^{a-2}q)).
\tag{14}
\]

Define `J(X)` by summing `j_a(q)/x` over exactly these ordinary odd
unit sources `x<=X`. It retains the source cutoff and all multiplicities.
Let `R_12(X)` be the five energy on sources outside `H` whose first
valuation is one or two. These sets partition the remaining sources.

For an endpoint in residue `c`, the least legal `a>=3` is `a_c=4`
when `c=1 mod3`, and `a_c=3` otherwise. Inverse exponents differ by
two, so their complete normalized sum is at most

\[
\eta(c)=\frac3{2^{a_c}-1/q_c}\frac1{1-1/4}.
\tag{15}
\]

Deleting nonunit sources only improves this bound. Also `q<=x/2` for
every such source. The same 54-residue rational calculation verifies
`Gamma_1(c)+eta(c)<7/8`; the largest grid upper bound is
`870801198/10^9`, at `c=43`. Grouping the old and new endpoint charges
before maximizing therefore proves

\[
\boxed{E_1(X)\le R_{12}(X)+J(X)+\frac78 E_1(X/2).}
\tag{16}
\]

Finiteness of `R_12(infinity)+J(infinity)` would imply
`E_1(infinity)<=8(R_12(infinity)+J(infinity))`. This is an exact further
reduction, not a proof that these remainders are finite.

### First unsupported step in the attempted closure

Ordinary invariance does not identify the two adjacent labels in (14).
The tempting replacement `j_a(q)<=K e(q)` has no proof. At `q=1`,
its right side is zero. For even `a=2m>=4` with `3 not dividing m`,
the eligible source `(4^m-1)/3` has a known one-step odd certificate
to 1. Declaring `j_a(1)=0` for every ordinary invariant label, in
particular the indicator of the basin of 1, asserts convergence of its
five-times companion. This is the still-open rank-one family in PR157,
`64361ecca770092d6c8242dc6211e38818af2e50`,
`research/global-closure-20261120/closing-attempts.md`, GCL-001--002,
also retained in PR166's ladder boundary. It is not an actual
counterexample to the proposed replacement.

For a bounded label the fixed-endpoint `q=1` contribution to `J` is
geometrically summable without requiring it to vanish. The genuine
energy gap is the sum over all unbounded endpoints and the remaining
valuation-one/two sources. Neither reciprocal-height occupation nor
saturated first-hit capacity estimates this sum. The complete
five-to-tripling comparison cannot be applied backwards; its inequality
has the opposite direction. No finite all-source estimate for `R_12+J`,
or for the original `R_s`, is established.

The companion [density/congestion note](DENSITY_CONGESTION.md) explains
another limitation of simply adding transport cylinders while demanding
a uniform column-sum constant below one. It explicitly preserves the
difference between Haar measure and ordinary-source coverage, and between
arbitrary positive charges and actual invariant-label defects.

## Verification

`check_expanded_renewal.py` reconstructs all 54 coefficient rows and
integer rational-power enclosures, nine affine prefix steps on whole
source cylinders, 96 literal paired-block controls, the high-valuation
residual identities, and three corrupted target corrections. It imports
no other checker and uses explicit exceptions. Normal and `-OO` reports
match byte for byte. These finite certificates check the constants and
algebra; the proof supplies the infinite geometric sums, ordinary domains
and finite-cutoff limiting arguments.
