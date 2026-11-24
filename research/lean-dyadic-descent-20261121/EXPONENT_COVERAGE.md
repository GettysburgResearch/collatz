# From selected exponents to simultaneous blocks

**Full Collatz remains OPEN.** This extension strengthens PR182's unbounded
selected-exponent theorem to arbitrarily large intervals of prescribed exponents.
PR182 already supplied several concrete bounded windows; the new intervals
exist arbitrarily far out. One interval
works simultaneously for every supplied offset certificate within a clock
budget; no separate offset-size restriction is required. The clock budget may
then grow linearly with the selected block. An exact counting theorem gives
upper natural density at least `5/6` among the exponents on the `2^d+1` ray,
even for the fixed power saving `y^120<n^119`. These are statements about
actual marked-return contractions, not proofs that all of the starting values
converge.

The normalization is the ordinary shortcut map `T`: halve an even input, and
send an odd input to `(3n+1)/2`. `Marked` and `returns` are exactly the PR173
definitions already imported by this packet. Every point and every clock in
the construction is an ordinary natural number.

## 1. One approximation covers a whole exponent window

Write `alpha=log_2 3`. The preceding `InfiniteDescent.lean` proves, without a
Diophantine hypothesis, that arbitrarily large natural `q` admit a natural `a`
such that

\[
0<q\alpha-a,\qquad q(q\alpha-a)<2.
\]

Its modular-inverse construction selects the positive side of an ordinary
rational approximation, and PR173's integer-power separation bound makes
the resulting exponents unbounded. That argument is reused unchanged.

The new theorem `endpoint_marked_phase_window` proves, for every such pair,

\[
1\le e\le10q
\quad\Longrightarrow\quad
3^q2^e+1\text{ is marked}.
\]

This is an interval in the free binary exponent, not a finite list of
numerically good approximation pairs. In particular its length grows without
bound with the selected `q`.

### Why the additional exponent fits

For `y=3^q 2^e+1`, keep the additive correction explicitly:

\[
\log_2 y=e+q\alpha+\varepsilon,
\qquad
\varepsilon=\log_2\left(1+\frac1{3^q2^e}\right).
\]

For `e>=1`, the elementary logarithm bound gives
`0<=epsilon<=1/3^q`. The natural-number inequality `2q<=3^q` therefore
gives `2q epsilon<=1`. The phase above the integer `e+a` satisfies

\[
\delta=q\alpha-a+\varepsilon\ge0,
\qquad 2q\delta\le5.
\]

Meanwhile `e<=10q`, `alpha<2`, and `epsilon<=1` imply
`floor(log_2 y)+1<=14q`. Hence

\[
(\lfloor\log_2y\rfloor+1)\delta\le35.
\]

The existing, proved `section_of_phase` theorem turns this inequality into
the exact integer mark test with coefficient 70. Since `e>=1`, the endpoint
is odd as required. No rounding error or lost additive one is omitted.

## 2. One block works for all bounded supplied certificates

Fix an arbitrary natural clock budget `H`, a desired contraction factor `C`, and
an arbitrary threshold for the next block. Choose a good `q` large enough that

\[
q>5(H+C+1).
\]

Then **every** prescribed exponent in the common block

\[
\boxed{\quad 2q+H+1\le d\le12q-H\quad}
\]

works simultaneously for every odd offset `r` with any supplied ordinary
certificate `T^h(r)=1`, `h<=H`.

For its actual odd count `p=p_h(r)`, put

\[
s=q-p,\qquad e=d-(h+2s).
\]

Because `p<=h<=H`, the padded clock `h+2s` lies between `2q-H` and `2q+H`.
The displayed block therefore guarantees `1<=e<=10q` for every supplied
certificate at once. Exact ordinary high-bit transport gives

\[
T^{h+2s}(2^d+r)=3^q2^e+1=:y.
\]

The supplied certificate itself implies `r<=2^h<=2^H`, by the nonnegative
affine remainder. Thus there is no need to choose `q` larger than `r`.
The source is marked using the bounds on `d` and the elementary inequality
`12q+1<=70*4^q`:

\[
(d+1)r\le(12q+1)2^H\le70\,2^{2q+H}\le70\,2^d.
\]

The earlier scaled coefficient theorem applies uniformly because
`q>5(p+C+1)`. It gives

\[
(C+1)3^q<2^{h+2s}.
\]

Multiplying by `2^e` and retaining the endpoint's `+1` proves both `y<2^d+r`
and `C y<2^d+r`. Finally, `captures` shows that this marked endpoint is a
positive iterate of the actual marked return process. The result also
preserves the physical basin equivalence through the displayed forward hit.

The formal interface is `arbitrarily_large_simultaneous_blocks`. It works for
all certificates that are supplied, without asserting that every positive
offset has one within the clock budget. It chooses one `q` before quantifying
over the offsets, clocks, and all exponents in the common block.

### The offset family can grow with the block

The stronger `growing_certificate_blocks` selects a good `q` beyond
`N+10(C+1)` and then sets `H=floor(q/10)`. The elementary inequality
`5(H+C+1)<q` still holds. Consequently the common block

\[
2q+\lfloor q/10\rfloor+1\le d\le12q-\lfloor q/10\rfloor
\]

works simultaneously for **every supplied offset certificate of length at
most `floor(q/10)`**. Every such offset is bounded by `2^floor(q/10)`, and
the clock budget and this size bound have no fixed ceiling. This strengthens
the variable-offset quantifier. It does not assert that every offset below
that numerical bound has such a short certificate, or infer the existence of
large certified offsets merely from a growing numerical upper bound.

## 3. A fixed power saving in the original source

The stronger coefficient estimate allows the saving factor to grow with the
selected block itself. Put

\[
H=\lfloor q/10\rfloor,\qquad q=10H+v,\qquad 0\le v\le9,
\qquad C=2^{H+1}.
\]

For `q>=100`, hence `H>=10`, the exact integer inequalities
`3^10<=2^16` and `3^9<=2^15` give

\[
3^q\le2^{16H+15},\qquad
(C+1)3^q\le2^{17H+17}.
\]

For any supplied certificate with `p<=h<=H`, the padded clock satisfies

\[
h+2(q-p)\ge2q-H=19H+2v>17H+17.
\]

Thus the full scaled coefficient guard holds with this exponentially growing
`C`. The theorem `exponential_simultaneous_blocks` concludes `C y<n` for
every supplied certificate and every prescribed exponent in the common
block. It uses the same proved one-sided approximants as before.

This gives a fixed power saving relative to the original source. Whenever
`d<=12q` and `r<2^d`,

\[
n=2^d+r\le2^{d+1}\le2^{12q+1}
 \le2^{120(H+1)}=C^{120},
\]

because `12v+1<=109<120`. Combining this with `C y<n`, and keeping all
arithmetic in natural numbers, proves

\[
\boxed{\qquad y^{120}<n^{119}.\qquad}
\]

This is the statement used by `power_saving_simultaneous_blocks`: the actual
smaller marked endpoint has a uniform power saving, simultaneously over the
growing certificate budget. No real-power convention or numerical logarithm
approximation is part of that conclusion.

For the offset-one ray, its zero-clock certificate lets the coefficient guard
cover the larger full block `[2q+1,12q]`, with the same fixed power saving.
The theorem is `power_plus_one_power_saving_blocks` and has no unproved basin
premise.

## 4. An unconditional exponent-density statement

Take `r=1`, with its exact zero-clock certificate, so `H=0`. For every `C`
there are arbitrarily large `q` such that **all** exponents

\[
2q+1\le d\le12q
\]

have an actual smaller marked return satisfying

\[
C\,R^k(2^d+1)<2^d+1
\qquad\text{for some }k>0.
\]

There is no unproved basin premise in `power_plus_one_blocks`. The stronger
`power_plus_one_power_saving_blocks` supplies the same entire block with
`y^120<(2^d+1)^119`.

Define `successCount(C,M)` to count positive exponents `d<=M` with the
specified marked-return contraction. The predicate is mathematical; this
definition is not an assertion of a total algorithm deciding arbitrary
Collatz termination. The theorem `power_plus_one_upper_density` proves the
exact finite inequalities

\[
\boxed{\quad
\forall N\ \exists M>N:\quad
5M\le6\,\operatorname{successCount}(C,M).
\quad}
\]

The proof takes `M=12q` and includes the entire `10q`-element interval
`[2q+1,12q]` in the counted set. Thus the upper natural density among the
positive **exponents** is at least `5/6`, for each fixed factor `C`.

The main strengthened counting theorem `power_plus_one_power_saving_density`
also proves

\[
\forall N\ \exists M>N:\quad
5M\le6\,\operatorname{powerSuccessCount}(M),
\]

where the counted exponents have an actual marked return `y` with the fixed
power saving `y^120<(2^d+1)^119`. Thus the same `5/6` upper-density bound holds
for this single power-saving property, not only separately for fixed
multiplicative factors.

This is not a density assertion among all ordinary positive integers. Nor
does it claim convergence of every member of the covered exponent blocks:
their explicitly smaller marked endpoints still require their own
convergence proofs.

## 5. Attempt to close the remaining cover

The current-source comparison includes:

| Source | Frozen head | Relevant boundary |
|---|---|---|
| [PR183](https://github.com/GettysburgResearch/collatz/pull/183) | `8659cf62ac685540cadeef320e596c852fbb0959` | A supplied offset certificate and an explicit endpoint-height budget give a smaller actual marked return. Some thin-band offsets outlast the entire binary horizon. |
| [PR184](https://github.com/GettysburgResearch/collatz/pull/184) | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | Exact reserved splices give genuine alternative ordinary merger partners, but a useful splice requires a genuinely cheaper history and the correct original-source or marked-partner bound. |
| [PR175](https://github.com/GettysburgResearch/collatz/pull/175) | `06215e69346c4d32bf970af9c846a6894586c1e7` | Cofinal parity cylinders occur in the marked set; an exponentially thin relative offset does not ensure a short certificate. |

The common blocks improve the prescribed-exponent quantifier within each
block, but do not show that their union covers every exponent. The explicit
growing clock budget covers all supplied certificates up to `floor(q/10)`;
it cannot be silently enlarged to an arbitrary certificate length after a
particular marked source is supplied.

There is also a separate offset-size gap. In the growing-budget result,
`d>=2q+H+1>21H`, so `r<=2^H` implies `r^21<n`. The forced inverse-logarithmic
band can instead have offsets of order `n/log n`. The theorem covers every
supplied short certificate in its block, but does not establish that an
arbitrary forced marked state has such a small or quickly certified offset.

There is also a concrete reason to keep the sign of the approximation. If an
irrational angle has an exceptionally accurate upper rational approximation
`a/b`, with `epsilon=a/b-alpha>0`, then for a long initial range of positive
`j`, the phases `j alpha` can avoid the small interval just above an integer.
For example, the elementary residue calculation gives
`fract(j alpha)>=1/(2b)` throughout `1<=j<=L` whenever
`L epsilon<=1/(2b)` and the indicated approximation is nonexact. For residue
zero the phase lies just below the next integer; for a nonzero residue the
positive rational-grid gap is at least `1/b` before the perturbation.
The finite `+1` in `3^j2^e+1`, `e>=1`, cannot cross a dyadic boundary: the
integer gap before adding it is at least `2^e`. Accordingly, a sufficiently
strong estimate forbidding such upper approximations cannot be assumed as
an automatic consequence of irrationality. This is a structural conditional
observation, not a claim here that an explicit ordinary Collatz trajectory
never converges or that a particular unproved asymptotic property of
`log_2 3` has been established.

A complete proof still needs control of the exponents and variable offsets
outside the constructed common blocks, or a genuinely different ordinary
continuation/merger mechanism that forces a lower marked partner there.
Repeating the original offset history in PR184's splice returns the original
source and supplies no strict saving. The current block theorem does not
replace that missing universal existence argument.

## Formal source and verification

All new statements are in [ExponentCoverage.lean](ExponentCoverage.lean).
The preceding PR182 source identities and PR173 imports are retained.
The new file is intended for the packet's pinned Lean4.34.1/Mathlib replay;
the root execution report records the actual compilation and axiom audit.
No new conjectural axiom or admitted proof is used.
