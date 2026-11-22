# Independent block exponents: an effective cycle theorem and a complete two-block exclusion

**Status, 22 November 2026:** written arithmetic proofs with an explicitly
identified external logarithmic-form theorem. The finite ordinary-source
resource mechanism, concrete Farey obstruction, and all 105 remaining
full-denominator cases are separately checked in Lean. The concrete all-exponent
exclusion also has an exact rational certificate and an independently implemented
checker. These evidence levels are distinct. This packet does not resolve
unrestricted Collatz convergence or exclude every positive cycle.

## Results and what changes

The parameter restriction in PR185 can be removed. Fix any finite list of
nonempty binary words `V₁,…,Vᵣ`. The positive ordinary cycles represented by

\[
                    V_1^{e_1}\cdots V_r^{e_r},\qquad
                    (e_1,\ldots,e_r)\in\mathbb N_0^r,
\tag{1}
\]

admit an effective, complete classification. The exponents are independent:
they need not lie on an affine line, have comparable sizes, or satisfy an
advance growth schedule. After identifying cycles already realized by one
block, there is an explicit upper bound on the **total shortcut clock** of
every remaining word. The full realization relation in the exponent lattice
is effectively semilinear.

The following particular family is completely excluded, with no outstanding
finite search:

\[
 P=(1,1,4,1,1,1,2),\quad Q=(2),\qquad
                 \boxed{P^aQ^b\text{ has no positive ordinary cycle}
                        \quad(a,b\ge1).}
\tag{2}
\]

Here the notation in (2) is for **odd gaps**: a gap `g` expands to the shortcut
parity word `1 0^(g−1)`. Thus `P=11100011110` and `Q=10` as binary words.
PR185 excluded the diagonal `P^kQ^k`. Equation (2) includes every independent
pair and every cyclic rotation of its word.

This follows the classical arithmetic mechanism for bounded numbers of
Collatz rises and falls: long legal repetitions force large divisibility,
while a small cycle denominator is limited by a logarithmic-form estimate.
Steiner's and Simons's work, developed into effective fixed-`m` cycle bounds
by Simons–de Weger, is the relevant lineage. Our contribution here is the
explicit arbitrary-block interface, the common-source Lean budget, and its
application to the repository's particular signed-block family. There is no
claim of historical novelty for the underlying finiteness principle.

## 1. Map, exact block data, and the full denominator

Use the ordinary shortcut map

\[
 T(n)=n/2\quad(n\text{ even}),\qquad
 T(n)=(3n+1)/2\quad(n\text{ odd}).
\]

First remove empty input blocks. If the resulting list is empty (`r=0`), it
contains no nonempty word and its positive cycle classification is empty;
no maximum is taken. All formulas below concern `r≥1`.

For each fixed nonempty binary block `Vᵢ`, calculate

\[
 L_i=|V_i|\ge1,\quad s_i=\#1(V_i),\quad
 F_i(x)=\frac{3^{s_i}x+C_i}{2^{L_i}},\quad C_i\ge0,
\]

by exact affine composition. Put

\[
 D_i=2^{L_i}-3^{s_i},\qquad c_i=C_i/D_i,\qquad
 K=\max_i(|D_i|+C_i),\qquad B=2\sum_i C_i.
\tag{3}
\]

The integer `Dᵢ` is odd and nonzero, including for an all-zero block.
Consequently `K≥1`; `cᵢ` may be zero, positive, or negative. Zero **exponents**
remain allowed.

For one exponent vector, let

\[
 L=\sum_iL_i e_i,\quad S=\sum_i s_i e_i,\quad
 M=3^S/2^L.
\]

The all-zero exponent vector has `L=0` and is excluded: a zero-clock identity
is not a cycle. For a nonempty word the formal periodic point is exactly

\[
                    x=\frac{C_W}{2^L-3^S}.
\tag{4}
\]

Every test in this packet retains this **entire denominator**. An actual
positive cycle has `S≥1`, `C_W>0`, and `M<1`. An all-zero word has only the
formal fixed point zero and contributes no positive cycle.

We use the following elementary legality fact, also present in PR185. If an
integer initial state has an integer final value under the prescribed formal
branches of a finite word, all prescribed parities are correct. At a first
incorrect parity a state has an odd numerator over two. Subsequent formal
steps preserve an odd numerator while increasing its power-of-two
denominator. It cannot become integral again. Thus a positive integer value
of (4) is an actual positive ordinary cycle, with positivity at every step.

## 2. A cyclic rotation with a small real numerator

For the selected exponent vector set

\[
 q_i=(3^{s_i}/2^{L_i})^{e_i}>0,
 \qquad F_i^{e_i}(x)=c_i+q_i(x-c_i).
\]

The rotation used here may depend on the exponent vector. This is permitted:
the result is a uniform bound for every vector, not the assertion that one
rotation works for all vectors.

**Rotation lemma.** If `∏qᵢ=M<1`, there is a cyclic rotation for which every
suffix product is at most one.

Write `P₀=1` and `Pⱼ=q₁···qⱼ`. Choose a minimum among
`P₀,…,Pᵣ₋₁`, and rotate after it. Every prefix product of the rotated list is
at least `M`: before wrapping it is `Pᵢ/Pⱼ`, and after wrapping it is
`M Pᵢ/Pⱼ`. The full prefix is `M`. Dividing `M` by a prefix gives the
suffix bound. This includes factors `qᵢ=1` from zero exponents.

At this rotated boundary, write `Qᵢ=qᵢ···qᵣ` and `Qᵣ₊₁=1`. The complete
affine translation is

\[
                     N=\sum_{i=1}^r c_i(Q_{i+1}-Q_i).
\tag{5}
\]

All `Qᵢ` lie in `(0,1]`. Since `|Dᵢ|≥1`,

\[
                     |N|\le2\sum_i|c_i|\le B.
\]

For a positive cycle, its ordinary state `x₀` at this boundary therefore
satisfies

\[
                     1\le x_0\le\frac{B}{1-M}.
\tag{6}
\]

No smallness claim has been made for every state on the cycle. The following
common-source argument transports (6) through all the intervening blocks.

## 3. Repeated-block divisibility and the common-source budget

Let `xᵢ` be the ordinary incoming state of a block repeated `eᵢ` times and
`xᵢ₊₁` its outgoing state. Set `mᵢ=Lᵢeᵢ` and `kᵢ=sᵢeᵢ`. The exact identity is

\[
 2^{m_i}(D_i x_{i+1}-C_i)
                 =3^{k_i}(D_i x_i-C_i).
\tag{7}
\]

Because a power of two is coprime to a power of three,

\[
                       2^{m_i}\mid D_i x_i-C_i.
\tag{8}
\]

If this defect is nonzero, its ordinary absolute value gives

\[
 2^{m_i}\le |D_i x_i-C_i|
       \le(|D_i|+C_i)(x_i+1)\le K(x_i+1).
\tag{9}
\]

Every ordinary shortcut segment of length `m` obeys

\[
             2^m(T^m(x)+1)\le3^m(x+1).
\tag{10}
\]

Using `3^m≤4^m`, (9)–(10) imply

\[
                K(x_{i+1}+1)\le[K(x_i+1)]^2.
\tag{11}
\]

Let `U=K(x₀+1)`. Iterating (11) gives
`K(xᵢ+1)≤U^(2^i)`. Multiplying the clock bounds (9) now yields

\[
          \boxed{2^L\le[K(x_0+1)]^{2^r-1}.}
\tag{12}
\]

This is a statement about **one ordinary source and its actual successive
states**. It does not choose a different source for each repetition cap.
The block contents and all repetition counts may differ from block to block.

The file [IndependentBlockBudget.lean](lean/IndependentBlockBudget.lean)
checks the integral argument. Its final theorem takes a list of certificates
(7), nonzero defects, and the common coefficient bound from (3), with every
outgoing state defined by the actual ordinary shortcut iteration. The four
public theorems are:

- `nonfixed_block_cap`: (7) and a nonzero defect imply (9).
- `ordinary_segment_quadratic`: an actual segment satisfying its clock cap
  obeys (11).
- `source_clock_budget`: a list of actual segment clock caps implies (12).
- `independent_block_budget`: the exact affine certificates imply (12).

The module does not assume a cycle, a logarithmic-form bound, or a convergence
axiom. It does not claim to formalize the analytic argument below. It compiled
with Lean 4.34.1 using `-j1 -DwarningAsError=true`; the printed axiom lists are
`[propext, Quot.sound]` for all four public theorems.

### The zero-defect alternative is finite and must be kept

If `Dᵢxᵢ−Cᵢ=0`, then `xᵢ=cᵢ` is a positive integer and one copy of `Vᵢ`
returns it to itself. The legality fact proves that this is an actual cycle.
By determinism the original cycle is that same cycle. Such cycles are found
by the finite direct test of `Cᵢ/Dᵢ` for each fixed block, followed by physical
replay. We never assume these cycles are trivial.

This also handles a zero defect at a zero-exponent boundary: the incoming
state independently realizes `Vᵢ`, even though that particular supplied word
does not execute it. If no boundary has zero defect, (12) applies, including
zero exponents. There is no unhandled division by a zero defect.

## 4. An explicit logarithmic-form input and total-clock cutoff

Let

\[
                         C=2^{32}=4294967296.
\]

For `1≤S≤L` and `2^L>3^S`, Matveev's Corollary 2.3 gives the deliberately
loose specialization

\[
 \Lambda=L\log2-S\log3>\exp[-C(1+\log L)].
\tag{13}
\]

**Exact external input.** In Matveev (2000), §2, Corollary 2.3,
`C₁(n,κ)≤2^(6n+20)` and the coefficient parameter can be replaced by
`B*=max|bᵢ|`. Use `n=2`, the field `Q` of degree one, the positive real
logarithms of 2 and 3, coefficients `L,−S`, and heights
`A₁=log2`, `A₂=log3`. Here `B*=L`, `A₁A₂<1`, and the nonzero form is positive
by hypothesis. Thus (13) follows directly. No conditional number-theoretic
hypothesis is involved. The primary statement was read; this project does
not claim to have reverified the external paper's entire proof.

Since `1−exp(−u)≥min(u,1)/2` for `u>0`,

\[
           1-M\ge\tfrac12\exp[-C(1+\log L)].
\]

Equations (6) and (13) give

\[
 x_0\le2B e^C L^C,\qquad
 \log(x_0+1)\le C+C\log L+2B.
\tag{14}
\]

Taking logarithms in (12), using `log K≤K` and `1/log2<2`, yields

\[
                 L\le2^{r+1}(K+2B+C+C\log L).
\tag{15}
\]

For `L≥1`, both `1≤√L` and `log L≤√L`. Consequently

\[
       \boxed{L\le H(V_1,\ldots,V_r)
          :=\left[2^{r+1}(K+2B+2C)\right]^2.}
\tag{16}
\]

All constants in this cutoff are integers computed from the fixed input
blocks. This bound is intentionally coarse; the argument needs a terminating
cutoff, not an efficient exhaustive search up to it.

## 5. Complete classification over the exponent lattice

**Theorem AC-INDEPENDENT.** For every fixed finite list of nonempty binary
blocks, all its positive ordinary cycle realizations (1), with `L>0`, are
effectively classifiable.

An explicit terminating procedure is:

1. Calculate the block data (3). Test and replay every positive integral
   block fixed point `Cᵢ/Dᵢ`.
2. Calculate `H` in (16). Enumerate all exponent vectors with
   `1≤ΣLᵢeᵢ≤H` and test the exact full quotient (4). Replay each integral
   positive result and identify its minimal cycle.
3. Deduplicate the finitely many resulting cycles. The zero-defect alternative
   and (16) prove this list is complete, even for parameter vectors outside
   the finite enumeration.
4. To describe precisely which outside vectors realize these known cycles,
   use the following finite parameter procedure on each of their states.

For a fixed ordinary incoming state `x` and a single block, put
`Δ=Dᵢx−Cᵢ`. If `Δ=0`, every exponent is legal and returns to `x`. If `Δ≠0`,
integrality after `e` repetitions is equivalent to

\[
                  2^{L_i e}\mid\Delta,
\]

and hence to

\[
                  0\le e\le\lfloor v_2(\Delta)/L_i\rfloor.
\tag{17}
\]

For the converse, use (7), oddness of `Dᵢ`, and the fact that the formal final
state has only a power-of-two denominator; the legality fact then applies.
Every allowed exponent in (17) has an explicitly computable outgoing state.
Traverse the finite block list, branching over these finite choices and
leaving an exponent free whenever the block fixes the incoming state. Keep
exactly paths returning to their initial state. This gives a finite union of
Cartesian parameter boxes whose coordinates are singletons or all of
`N₀`, with the all-zero vector removed. In particular it is an effective
semilinear description of the complete realization relation.

The procedure may be impractical for some block inputs. No finite search of
that general size was executed here. The next section gives a concrete
application in which exact approximation makes the required enumeration tiny
while its scope remains all independent exponents.

## 6. Complete exclusion of `P^aQ^b`, with independent positive exponents

The exact block maps are

\[
 F_P(x)=-41+\frac{2187}{2048}(x+41),\qquad
 F_Q(x)=1+\frac34(x-1).
\tag{18}
\]

Suppose `a,b≥1` and a positive integer `x` realizes a cycle `P^aQ^b`.
Set

\[
 r=2187/2048,
 \quad q=(3/4)^b,
 \quad M=r^a q,
 \quad L=11a+2b,
 \quad S=7a+b.
\]

The `P` block is strictly expanding at positive states, and its only formal
fixed point is `−41`. Its output `y` therefore exceeds `x≥1`. The `Q` block
has fixed point 1, so neither boundary has zero defect. The cutoff (16)
applies with

\[
 K=5838,\quad B=11400,\quad r_{\rm blocks}=2,
 \qquad H=4722397970736130105600.
\tag{19}
\]

In particular `1≤S≤L≤H`.

The complete cycle equation and repeated `P`-legality give, respectively,

\[
       x+41=\frac{42(1-q)}{1-M},\qquad 2048^a\mid x+41.
\tag{20}
\]

For divisibility, (7) has the defect `−139(x+41)` and `139` is odd. Since
`x+41>0`,

\[
 0<1-M<\frac{42}{2048^a},\qquad
 0<\Lambda:=L\log2-S\log3<\frac{84}{2048^a}.
\tag{21}
\]

The second estimate uses `42/2048<1/2` and
`−log(1−u)≤2u` for `0≤u≤1/2`.

### The complete range with `b≥a` is immediately impossible

If `b≥a`, then

\[
 M\le(6561/8192)^a\le6561/8192
                       <1-42/2048\le1-42/2048^a,
\]

contradicting (21). It therefore suffices to consider `1≤b<a`.

### One exact rational interval excludes the entire tail `a≥16`

Put `α=log3/log2`. The certificate gives adjacent Farey fractions

\[
 \frac{p}{q_0}
 =\frac{7373006092034578625129}{4651848916728231124485}
 <\alpha<
 \frac{u}{v}
 =\frac{325919355854421968365}{205632218873398596256}.
\tag{22}
\]

The following are checked by exact rational arithmetic:

\[
 q_0u-pv=1,\qquad q_0+v>H,\qquad
 \frac uv-\alpha>\frac{168}{2048^{16}}.
\tag{23}
\]

To certify the logarithms, for `z=2,3` and `t=(z−1)/(z+1)`, use 128 terms of

\[
 \log z=2\sum_{j=0}^{127}\frac{t^{2j+1}}{2j+1}+R_z,
 \qquad
 0<R_z\le\frac{2t^{257}}{257(1-t^2)}.
\tag{24}
\]

The remainder follows by replacing every later denominator by 257 and
summing a geometric series. These are rational lower and upper bounds, not
floating point evaluations. The checker also verifies `log2>1/2`.

If `a≥16`, (21) implies

\[
 0<\frac LS-\alpha
       =\frac{\Lambda}{S\log2}
       <\frac{168}{2048^{16}}.
\]

Thus `p/q₀<L/S<u/v`. Any positive integers `L,S` strictly inside this
Farey interval have `S≥q₀+v`. Indeed the integers

\[
              uS-vL\ge1,\qquad q_0L-pS\ge1
\]

satisfy the exact identity

\[
              S=q_0(uS-vL)+v(q_0L-pS)\ge q_0+v.
\]

This contradicts `S≤H`. The argument does not require `L/S` to be reduced,
does not use an assumed continued-fraction computation, and excludes every
`a≥16` at once.

### The remaining finite set uses the whole denominator

It remains that `1≤a≤15` and `1≤b<a`, exactly 105 pairs. The complete quotient
at the original boundary is

\[
 x=\frac{
      2048^a4^b-42\,2048^a3^b+41\,2187^a3^b
     }{2048^a4^b-2187^a3^b}.
\tag{25}
\]

For 20 pairs the denominator is nonpositive. For the other 85 pairs it is
positive and does not divide the numerator. The generator records exact
remainders. The checker independently composes every expanded binary word
and reduces its affine correction modulo its **complete** cycle denominator;
it does not merely rerun the generator's closed formula.

This proves (2). A cyclic rotation of one of these words would give the same
ordinary cycle at another state and is therefore excluded too. Boundary
families remain explicit: `a=0,b>0` gives repetitions of the trivial cycle;
`a>0,b=0` has no positive periodic point; `a=b=0` is the excluded empty word.

### Executed certificate checks

The three artifacts are

- [independent_pq_generate.py](certificates/independent_pq_generate.py),
- [independent_pq_certificate.json](certificates/independent_pq_certificate.json),
- [independent_pq_verify.py](certificates/independent_pq_verify.py).

Executed successfully:

```text
python -X utf8 -B research/global-synthesis-20261122/certificates/independent_pq_generate.py
python -X utf8 -B research/global-synthesis-20261122/certificates/independent_pq_verify.py --self-test
```

The checker verifies the affine block data, specialization constants, exact
cutoff, logarithm remainder enclosures, determinant, denominator sum, tail
gap, `b≥a` reduction, complete finite-pair coverage, and every whole-denominator
remainder. It rejects a changed Farey endpoint, a changed cutoff, a missing
finite pair, and a changed remainder. It uses explicit exception checks,
not assertions that disappear under Python optimization.

This executable evidence checks the arithmetic data in the written theorem.
It does not replace the proof of the infinite parameter coverage, formalize
Matveev, or constitute a Lean proof of (2).

The additional module
[IndependentPQCertificate.lean](lean/IndependentPQCertificate.lean) checks
two central integer parts independently:

- `tail_farey_obstruction` excludes arbitrary natural `L,S` with `S≤H` and
  the two strict cross-multiplied Farey inequalities (22).
- `small_full_denominator_exclusion` proves all 105 remaining cases using
  kernel `decide` over `Fin 16`. Its axiom list is empty; it does not use
  `native_decide`. `small_natural_exponent_exclusion` exports the result for
  ordinary natural-number parameters.

This module also passed Lean 4.34.1 with `-j1 -DwarningAsError=true`. The
Farey theorem and natural-parameter corollary use only `propext` and
`Quot.sound`. The exact real logarithm enclosure remains certified by the
rational Python checker and the proof of (24); Matveev and the infinite
analytic reduction remain written inputs.

## 7. The global consequence and the unclosed quantifier

For a fixed finite dictionary `D` of binary words, let `L_D` be the greatest
word length, `C_D` the greatest affine correction, and `K_D` the greatest
`|Dᵢ|+Cᵢ`. If a primitive positive cycle of length `L>L_D` has a decomposition
into `r` repeated dictionary blocks, no one such block can fix its incoming
state: that would give a shorter positive return than the primitive period.
Therefore

\[
                L\le4^{r+1}(K_D+4rC_D+2C)^2.
\tag{26}
\]

Thus a hypothetical sequence of increasingly long primitive cycles must
have unbounded repeated-block description length in every fixed dictionary,
with at least logarithmic growth supplied by (26). The elementary height
step can be sharpened by retaining `log₂3` instead of rounding it up to 2,
but no improvement of that constant supplies a bound on `r`.

The unclosed global quantifier is precise: an arbitrary candidate word may
use arbitrarily many blocks, or introduce arbitrarily long new block
contents. Every word can be put in a finite schema, but the cutoff and the
finite classification change with that schema. No finite set of schemas is
shown to cover all possible cycles. The generic theorem also makes no
claim that an aperiodic ordinary orbit eventually belongs to one such
bounded product language.

The full conjecture would still require exclusion of all remaining cycle
descriptions and of escaping ordinary trajectories, or an independent
descent/merger argument covering them together. The present theorem closes
the independent-exponent obligation for **every supplied bounded product**,
and the concrete family (2) is fully settled. These are the exact scopes.

## 8. Frozen dependencies and primary sources

1. **PR185, `276be8154f4e867acc0230466b34d9cb224aacf5`:**
   [EFFECTIVE_FIXED_BLOCK_CYCLES.md](https://github.com/GettysburgResearch/collatz/blob/276be8154f4e867acc0230466b34d9cb224aacf5/research/whole-repo-closure-20261122/EFFECTIVE_FIXED_BLOCK_CYCLES.md),
   §§2,4,6,7. This is the one-parameter predecessor: full-denominator legality,
   affine rotation, defect cap, and the signed `P` block. Its diagonal
   exclusion is not assumed to cover the independent exponents here.
2. **PR186, `1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493`:**
   [03_arithmetic_and_logic.md](https://github.com/GettysburgResearch/collatz/blob/1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493/literature/deep-machinery-20261122/03_arithmetic_and_logic.md),
   §§B,E,F, and the T08–T09 task cards. These motivate the all-parameter
   arithmetic interface; their proposed global applications are not assumed.
3. **PR182, `45354128f890fb479f6c23b547368bcddd9cebe6`:**
   [LITERATURE_RIGIDITY_BRIDGE.md](https://github.com/GettysburgResearch/collatz/blob/45354128f890fb479f6c23b547368bcddd9cebe6/research/lean-dyadic-descent-20261121/LITERATURE_RIGIDITY_BRIDGE.md)
   was inspected for an alternative global route. Its ordinary Fourier/Besicovitch
   statements are not dependencies of any theorem in this file.
4. **E. M. Matveev (2000),** *An explicit lower bound for a homogeneous rational
   linear form in the logarithms of algebraic numbers. II*, Izvestiya:
   Mathematics **64**(6), 1217–1269, §2, Corollary 2.3.
   [Primary journal record](https://www.mathnet.ru/eng/im314),
   [indexed English primary PDF](https://www.mathnet.ru/links/ece4aa0032f96dfaf141673d5dc77324/im314_eng.pdf),
   DOI [10.1070/IM2000v064n06ABEH000314](https://doi.org/10.1070/IM2000v064n06ABEH000314).
   The exact specialization is given in §4 above.
5. **J. Simons and B. de Weger (2005),** *Theoretical and computational bounds
   for m-cycles of the 3n+1-problem*, Acta Arithmetica **117**(1), 51–70.
   [Author-hosted published paper](https://deweger.net/papers/%5B35%5DSidW-3n%2B1-ActaArith%5B2005%5D.pdf),
   [author-hosted 2007 revision inspected](https://www.deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.43%5B2007%5D.pdf).
   Its introduction and §§1.2–1.4 describe the fixed-number-of-runs mechanism
   and its Steiner–Simons lineage. No numerical census from that work is used
   by the new certificate.
