# A nonlinear carry budget and obstructions to polynomial orders

**Status: PROPOSED, with elementary written deductions and exact bounded
replay. Collatz remains OPEN.** This pass tries the mixed binary/ternary
rewrite route rather than combining the earlier prime-height and occupancy
constraints. It obtains a source-persistent nonlinear controller, exact
rewrite-work accounting, and three obstructions to proposed order classes.
The controller may stop with **UNRESOLVED carry budget**; no bound on its
required allowance for every ordinary source is proved.

## 1. Frozen system, attribution, and ordinary interpretation

The mixed-base system is due to Emre Yolcu, Scott Aaronson, and Marijn J. H.
Heule, [*An Automated Approach to the Collatz Conjecture*](https://arxiv.org/abs/2105.14697v3),
arXiv version 3, 31 December 2022; *Journal of Automated Reasoning* 67,
article 12 (2023), [DOI 10.1007/s10817-022-09658-8](https://doi.org/10.1007/s10817-022-09658-8).
Section 3.2 supplies the system and its termination equivalence; Example
4.3 supplies the two-dimensional interpretation used in section 3 below.
Their natural-matrix impossibility theorem in section 3.1 concerns the
**unary** system. It is not the mixed-base obstruction proved here.

In the repository's alphabet, a proper word is `c w d`, with interior over
`a,b,e,f,g`. Start with the ordinary value 1 and read left to right:

| Letter | Ordinary action |
| --- | --- |
| `a`, `b` | `2x`, `2x+1` |
| `e`, `f`, `g` | `3x`, `3x+1`, `3x+2` |

The final `d` has no arithmetic action. Write `N(w)` for the positive
ordinary value and `b(n)` for binary bitlength. The eleven rules are

```text
ad -> d      bd -> gd
ae -> ea     af -> eb     ag -> fa
be -> fb     bf -> ga     bg -> gb
ce -> cb     cf -> caa    cg -> cab
```

The first two rules perform the killed-at-1 shortcut map `T`; the other
nine preserve ordinary value. Every proper word of value 1 is `cd`.
For odd-event statements use `U(n)=(3n+1)/2^v2(3n+1)`.

The prefix potential

\[
 H(w)=\sum_{\text{ternary letters in }w}
 b(\text{ordinary prefix value before that letter})
\]

and its exact one-step changes are inherited from PR #141,
`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`,
`research/ay-persistent-20261031/PROOF.md`, HC-5--HC-6. That packet's
finite-popcount guard is not used here. PR #145 at
`dd245a712f985909f541590e3f6c179b7ba011e4`,
`research/binary-run-occupancy/README.md`, was read to keep its fixed-source
carry and finite-complexity boundaries separate from the present claims.
The old linear recharge obstruction is PR #157 at
`64361ecca770092d6c8242dc6211e38818af2e50`,
`research/global-closure-20261120/arithmetic.md`, GA-005.

## 2. CSO-001: exact work, confluence, and a sharp administrative envelope

Every administrative rewrite decreases `H` by exactly one. An even
dynamic rewrite leaves `H` unchanged. At an odd dynamic source `n`, the
rule `bd -> gd` increases it by exactly `b(n)-1`.

For any finite proper rewrite sequence of length `L`, with `k` dynamic
events at ordinary inputs `n_0,...,n_(k-1)`, define

\[
 c(n)=\begin{cases}1&n\text{ even},\\b(n)&n\text{ odd}.
 \end{cases}
\]

Then the exact, unconditional identity is

\[
 \boxed{L=H(w_0)-H(w_L)+\sum_{j<k}c(n_j).}             \tag{1}
\]

The sequence of dynamic values is exactly the ordinary shortcut orbit
from `N(w_0)`. Neither it nor the creation cost depends on the intervening
administrative schedule.

**Proof of the local changes.** In an internal swap, the ternary letter's
prefix changes from `2x` or `2x+1` to `x`, losing exactly one bit of
bitlength. Later prefixes agree by the affine identity. A `c`-boundary
rule removes a ternary letter whose prefix was 1. The two dynamic claims
follow directly from the last-letter arithmetic. Summing these exact
changes proves (1).

The administrative subsystem is confluent on proper words and every
maximal administrative derivation has **exactly `H(w)` steps**. Indeed it
terminates by the integer decrease. A word with a ternary letter cannot
be irreducible: its leftmost ternary letter has `c` or a binary letter
immediately before it. Its unique administrative normal form is therefore
the canonical binary spelling of its unchanged positive value.

There is the following explicit envelope, uniform over every mixed
representation of the same ordinary value:

\[
 \begin{split}
 H(w)&\le E(N):=
 \sum_{j=1}^{\lfloor\log_3N\rfloor}
 b\!\left(\left\lfloor N/3^j\right\rfloor\right)\\
 &\le\frac{b(N)(b(N)-1)}2,\qquad N=N(w).              \tag{2}
 \end{split}
\]

The first bound is attained at every `N=3^t` by the proper word `c e^t d`.
Moreover

\[
 E(N)=\frac{(\log_2N)^2}{2\log_2 3}+O(\log N).         \tag{3}
\]

For the proof, the prefix before the `j`-th ternary letter counted from
the right is at most `floor(N/3^j)`: its suffix includes `j` multiplications
by three and all digit additions are nonnegative. There are at most
`floor(log_3 N)` ternary letters. Since `3^j>=2^j`, each summand is at most
`b(N)-j`, proving the second bound. Equality on powers of three follows
by inspecting their all-ternary word. Finally each summand equals
`floor(log_2 N-j log_2 3)+1`; summing this arithmetic progression with
bounded rounding error proves (3).

If a supplied ordinary orbit reaches 1 for the first time after `tau`
shortcut steps, then **every** complete rewrite derivation from any proper
representation of its source has the same length

\[
 H(w_0)+\sum_{j<\tau}c(T^jN).                         \tag{4}
\]

Every prefix has at most `tau` dynamic events, so (1) also bounds its
length without first presupposing rewrite termination. An irreducible
proper word for the full system must be `cd`, proving the assertion.
No equality of arbitrary paths with different numbers of dynamic events
or an unproved cycle exclusion is being asserted.

### The exact missing scalar super-solution

If one could give a total nonnegative integer function `K` with `K(1)=0`
and

\[
 K(n)\ge K(Tn)+c(n)\qquad(n>1),                       \tag{5}
\]

then `K(N(w))+H(w)` would decrease by at least one on every literal rule.
Conversely, under Collatz convergence the finite sum in (4), without its
initial `H`, defines such a `K` with equality. This is an exact weighted
cost formulation of the missing global result, not a construction of a
total `K`. Administrative scheduling by itself supplies no upper bound
on that ordinary dynamic cost.

## 3. CSO-002: a nonlinear rank with one fixed carry allowance

Here a concrete controller does succeed, with an explicit unresolved
outcome. Use the following affine matrix interpretation from AYH Example
4.3, translated to the repository alphabet. Interpret a word by composing
its letter functions in written order, so `[xy]=[x] o [y]`, and evaluate
at the zero vector. This interpretation is a rank, not the ordinary
left-to-right numerical decoder.

| Symbol | Matrix | Added vector |
| --- | --- | --- |
| `a` | `[[1,1],[1,0]]` | `[0,0]` |
| `b` | `[[1,3],[3,4]]` | `[1,1]` |
| `c` | `[[1,5],[0,0]]` | `[0,0]` |
| `d` | `[[1,0],[1,0]]` | `[1,1]` |
| `e` | `[[7,2],[2,5]]` | `[2,1]` |
| `f` | `[[2,1],[1,1]]` | `[1,0]` |
| `g` | `[[2,2],[2,4]]` | `[0,2]` |

Let `P(w)` be the first coordinate of `[w](0)`. For every rule except
`af -> eb`, its left interpretation minus its right interpretation has
a nonnegative matrix and a nonnegative vector whose first entry is at
least one. Every letter matrix has `(1,1)` entry at least one. Therefore
these ten rules decrease `P` by at least one in **every** context.
This subsystem termination proof is credited to AYH; it is not a new
claim here.

For the omitted carry rule the two local interpretations are

\[
 [af](x)=\begin{pmatrix}3&2\\2&1\end{pmatrix}x+
              \binom11,\qquad
 [eb](x)=\begin{pmatrix}13&29\\17&26\end{pmatrix}x+
              \binom{11}8.
\]

Entrywise comparison gives `[eb](x)<=26[af](x)` for `x>=0`.
Nonnegative affine left contexts preserve this multiplicative upper
bound, so every such rewrite satisfies

\[
 P(w')\le26P(w).                                     \tag{6}
\]

Fix **once at the original source** a nonnegative integer allowance `K`.
Maintain the number `r` of allowed `af -> eb` occurrences still available.
Every other rule is admitted; that rule is admitted only when `r>0`, and
consumes one unit. Then

\[
 \boxed{\rho(w,r)=26^r P(w)+r\in\mathbb N}            \tag{7}
\]

strictly decreases on every admitted literal rewrite. A non-carry rule
decreases `P`; a carry rule uses (6) and decreases `r` by one. Thus every
schedule of this controller has at most

\[
 26^K P(w_0)+K                                       \tag{8}
\]

steps. It ends at `cd` or at a word blocked by the exhausted carry allowance.
The latter outcome is **UNRESOLVED**, not a convergence certificate.

For a canonical binary input of ordinary value `N`,

\[
 P(w_0)\le6\,8^{b(N)-1}\le6N^3.                      \tag{9}
\]

The right boundary sends zero to `(1,1)`; each binary letter multiplies
the maximum coordinate by at most eight, and the left boundary costs at
most a factor six. For an arbitrary proper mixed word the same reasoning
gives `P(w_0)<=6*11^(b(N)-1)`, since there are at most `b(N)-1` interior
letters and their augmented row sums are at most eleven.

This rank permits unbounded source height and unbounded run complexity.
It does not permit increasing the allowance after it is exhausted:
doing so raises its leading factor. The unproved global obligation is a
finite allowance sufficient for each fixed ordinary source. The original
paper's section 4.3 already identifies relative termination of any one
rule as a full closing condition after its proper-subsystem results.
Equation (7) is a quantitative budget transfer from that published rank,
not a proof of the required relative termination.

Under the deterministic schedule that fully normalizes after each odd
dynamic event, the exceptional occurrence has a concrete carry meaning.
Its ternary carry state is 1 and it crosses a binary zero, emitting a one
and changing carry state to 0. The three carry states are `e,f,g`.
This interpretation does not replace the actual event count by a fresh
average or assume the count is independent of the source.

## 4. CSO-003: no scalar natural polynomial rule-removal interpretation

Assign every symbol a **nonconstant** polynomial in `N[X]`. Use ordinary
functional composition as above, and suppose all eleven rule inequalities
`[left](t)>=[right](t)` hold for every `t in N`. Then all five interior
symbols `a,b,e,f,g` are the identity polynomial. Every rule has equal
interpretations. In particular this class cannot even begin rule removal
by making one rule strict and the others weak.

**Degree collapse.** Write `a,b,e,f,g` temporarily for their positive
degrees. Six necessary inequalities are

\[
 g\ge f,\quad e\ge f,\quad af\ge eb,\quad bf\ge ga,
 \quad f\ge a^2,\quad b\ge g.                        \tag{10}
\]

They come respectively from `ag`, `be`, `af`, `bf`, `cf`, and `bd`.
Multiplying the third and fourth yields `f^2>=eg`; the first two force
`e=f=g`. Then `a=b`, and `a>=f>=a^2` forces all five degrees to be one.
The boundary degrees cancel because both boundary polynomials are
nonconstant.

**Slope collapse.** Now apply the same argument to the positive integral
slopes of these five affine polynomials. The `cf` inequality again gives
`f>=a^2`, even if the polynomial for `c` has higher degree. All five
slopes are one.

**Offset collapse.** Write their nonnegative offsets as `A,B,E,F,G`.
The necessary inequalities include

\[
 G\ge A+B,\quad B\ge G,\quad G\ge F,\quad E\ge F,
 \quad A+F\ge E+B.                                   \tag{11}
\]

The first follows from `cg -> cab` by strict monotonicity of the boundary
polynomial. The second follows from `bd -> gd`. They force `A=0,G=B`.
The last inequality together with `E>=F` forces `B=0`. Hence `G=F=E=0`
as well. This proves the claim.

The same proof works for the completely reversed system: degrees and
leading products have the same inequalities, and the boundary maps are
strictly increasing and unbounded. This result does **not** exclude
orders on guarded proper words with constant boundary maps, semantic
orders, general matrices, arctic interpretations, or ordinal constructions.

## 5. CSO-004: upper-triangular positive-diagonal matrix collapse

The analogous obstruction holds in **every dimension** for natural affine
matrix interpretations whose matrices are all upper triangular and have
strictly positive diagonal entries. Assume every rule is weakly oriented
componentwise on all nonnegative integer vectors. Then each interior
letter is the identity affine function, and again no rule is strict.

Homogenize an affine map by adjoining its offset as the last column and a
final diagonal entry one. All resulting matrices remain upper triangular
with positive diagonal. Componentwise inequalities on every input imply
entrywise inequalities of these augmented matrices.

On each diagonal coordinate, (10) applies to the scalar diagonal entries,
so all interior diagonals equal one. If an interior matrix has a nonzero
off-diagonal entry, choose the smallest superdiagonal distance at which
any of the five interior matrices does. At an entry `(i,j)` of this
distance, all products of interior matrices add their respective entries:
all cross terms use shorter distances and vanish. The comparisons with
the boundary matrices multiply the difference by a positive boundary
diagonal entry. Thus these five nonnegative entries obey exactly (11),
which forces them all to vanish, a contradiction.

This includes diagonal interpretations of arbitrary dimension. It does
not cover matrices with feedback below the diagonal or zero diagonal
coordinates. The credited two-dimensional interpretation in section 3
uses both features. The same first-superdiagonal argument works after
reversing every rule; only the side on which a positive boundary diagonal
multiplies the difference changes.

## 6. CSO-005: every fixed polynomial additive run-energy collapses

Counting only runs discarded their lengths. Squared run lengths initially
look more promising: the old valuation-three recharge family shortens a
long run and releases a linear amount of squared energy. Two different
exact carry collapses defeat that attempted repair.

For odd `m=2k+1>=3`,

\[
 n=\frac{2^{m+2}-5}{3},\quad a(n)=2,\quad U(n)=2^m-1.
                                                               \tag{12}
\]

Its binary source is `(10)^(k-1)1001`: every one-run has length one,
every zero-run has length one except one of length two. Its total squared
run energy is `m+3`; its image has energy `m^2`.

For even `m=2k>=4`,

\[
 n=\frac{2^{m+1}+1}{3},\quad a(n)=1,\quad U(n)=2^m+1.
                                                               \tag{13}
\]

Its binary source is `(10)^(k-1)11`, with total squared run energy `m+2`.
Its image has a zero-run of length `m-1`. Both statements follow directly
from `3n+1=4(2^m-1)` and `3n+1=2(2^m+1)`, respectively.

There is an all-degree obstruction, allowing **signed coefficients**.
Let `P,Q,R` be real polynomials and consider, on positive odd integers,

\[
 \begin{split}
 V(n)={}&P(b(n))+
 \sum_{\text{one-runs }J}Q(|J|)+
 \sum_{\text{zero-runs }J}R(|J|)\\
 &+\lambda B(n)+\mu r(n)+\nu s_2(n)+\eta\log_2 n,
 \qquad B(n)=v_2(n+1)-1.                             \tag{14}
 \end{split}
\]

Here `r(n)` is the number of one-runs in the ordinary binary expansion,
and `s_2(n)` is its popcount, the number of one-bits.

If `V` is bounded below on all positive odd integers and
`V(U(n))<=V(n)` for every odd `n>1`, then **all coefficients of degree
at least two in `P,Q,R` vanish**. Thus no fixed polynomial additive
run-length energy supplies a genuinely nonlinear monotone rank in this
class.

**Proof.** Suppose the largest degree is `d>=2`, and call the degree-`d`
coefficients of `P,Q,R` respectively `alpha,beta,gamma`, assigning zero
when a degree is smaller. In (12), the source has `O(m)` runs of lengths
one or two and bitlength `m+1`; the image has bitlength `m` and one run
of length `m`. Consequently its potential change is
`beta*m^d+O(m^(d-1))`, so `beta<=0`. In (13), the source bitlength is
`m` and the image bitlength is `m+1`; the same argument gives `gamma<=0`.

For `n=2^m-1`, its next odd state is `3*2^(m-1)-1`, of binary form
`10` followed by `m-1` ones. Bitlength increases from `m` to `m+1`,
whereas the one-run contribution changes from `Q(m)` to `Q(m-1)+Q(1)`.
The change in (14) is therefore

\[
 d(\alpha-\beta)m^{d-1}+O(m^{d-2})+O(1).
\]

Here countdown decreases by one, run count increases by one, popcount
is unchanged, and logarithmic height changes by a bounded amount. Hence
`alpha<=beta`. On the same all-ones sources, boundedness below requires
`alpha+beta>=0`. Together with `beta<=0`, this forces
`alpha=beta=0`. Finally, on `2^m+1`, boundedness below forces
`gamma>=0`, hence `gamma=0`. This contradicts the choice of the largest
nonzero degree. The claim follows.

Once only affine terms remain, the run sums reduce to ordinary bitlength,
popcount, and run count: the sum of one-run lengths is popcount, the sum
of zero-run lengths is bitlength minus popcount, and an odd binary word
has one fewer zero-run than one-run. The earlier PR157 recharge family
then also forces the net countdown coefficient to be nonpositive in any
such weakly decreasing potential. No impossibility of every nonlinear,
nonadditive, position-sensitive, or history-dependent rank is claimed.

## 7. What remains after these attempts

The polynomial and triangular-matrix obstructions concern precise order
classes, not termination itself. The run-energy theorem rules out a broad
repair of the earlier additive resource but not an unbounded hierarchy
of carry patterns. The successful controller retains one original
allowance and admits genuine ordinary steps; it does not recharge that
allowance for free.

The remaining concrete obligation is either a total solution of (5), or
a proved finite allowance sufficient for each original source in (7),
or a different order outside the excluded classes. None is established.
The exact administrative envelope and the published ten-rule order cannot
by themselves control how often the exceptional carry is created.

The checker
[`creative_symbolic_order.py`](../../experiments/creative_symbolic_order.py)
verifies the rule matrices and factor-26 certificate symbolically, checks
the work identity and administrative envelope on a bounded complete word
corpus, replays bounded carry controllers, and checks the explicit
carry-collapse families. Its report is
[`symbolic-report.json`](../../reports/2026-11-20-creative-closure/symbolic-report.json).
The general impossibility theorems rest on the written arguments, not a
finite search over polynomial degrees or coefficients.

```sh
python -X utf8 -B experiments/creative_symbolic_order.py --compare reports/2026-11-20-creative-closure/symbolic-report.json
```

No formal proof-assistant or external mathematical review is claimed.
