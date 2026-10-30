# A finite rank envelope that controls one-step transport

**Status: PROPOSED, with complete elementary proofs below and bounded independent
replay. Collatz remains OPEN.** This packet constructs a new proper integer rank
whose moments cannot explode in one shortcut step. It does not prove that this
rank decreases, nor that its induced return process contracts.

## 1. What is inherited, and what changes

The actual-prefix rank below is **not new**. It is the rank `Gamma` of APR-001--009,
PR106 at commit
`7b7471ea0e7b359a2ac46fb1e6aff269331509c3`, particularly:

- [PROOF.md](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/prefix-rank/PROOF.md);
- [PERIODIC_SWITCHING.md](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/prefix-rank/PERIODIC_SWITCHING.md);
- [SPIKES.md](https://github.com/GettysburgResearch/collatz/blob/7b7471ea0e7b359a2ac46fb1e6aff269331509c3/research/astra-linear-frontier/prefix-rank/SPIKES.md).

An initial investigation independently rediscovered its finite evaluator,
rotation guard, and periodic-word selection mechanism. The source comparison
identified the duplication before publication. Those statements are credited to
PR106 here. No new priority is claimed for them.

The new step is a least integer majorant `Phi` of `Gamma`, with three simultaneous
properties: exact finite evaluation, the same critical sublevel exponent, and a
uniform global one-step growth factor. A Bellman identity then gives a new total
contact-return interface. This is a concrete repair of one transport obstruction,
not the missing strict contraction estimate.

## 2. Maps, rank, and the killed boundary

Write

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\qquad
S(1)=1,\quad S(n)=T(n)\ (n>1).
\]

All inputs are positive ordinary integers. `T` remains the ordinary shortcut map
inside the prefix rank; `S` absorbs at 1 in the forward envelope and transport.

For nonzero integers `d`, put `g(d)=d^2/3^{v_3(|d|)}`. Define

\[
\Gamma(1)=0,\qquad
\Gamma(n)=\min\left(\{g(n)\}\cup
 \{4^k g(T^k(n)-n):k\ge1,\ T^k(n)\ne n\}\right),\quad n\ge2.
\]

Zero displacements are omitted. They are not assigned rank zero. APR-001 gives

\[
n\le\Gamma(n)\le n^2,
\qquad
k\le\lfloor\log_2 n\rfloor
\]

for every candidate capable of improving the baseline. The bound follows from
`2^k T^k(n)=3^q n+A`, `0<=A<=3^k-2^k`, and

\[
n\le 2^k|d|+A\le 3^k|d|\le4^k g(d).
\]

Thus the inherited rank itself is an exact finite computation, with no unknown
stopping-time oracle. Its component at a primitive expanding periodic word can
decrease while the ordinary state increases. However APR-009 shows that it also
has unbounded one-step multiplicative spikes.

## 3. ORD-001: the integer envelope is total and efficiently computable

Define

\[
\boxed{\displaystyle
\Phi(n)=\max_{j\ge0}\left\lceil\frac{\Gamma(S^j(n))}{3^j}\right\rceil.}
\tag{1}
\]

Then `Phi(1)=0`, and for every `n>=2`:

\[
n\le\Gamma(n)\le\Phi(n)\le(n+1)^2.
\tag{2}
\]

The maximum in (1) is attained and can be evaluated in `O(log n)` forward
positions, using `O((log n)^2)` actual-prefix comparisons and integers with
`O(log n)` bits. These are iteration and bit-size bounds, not a unit-cost claim
for unbounded integers.

### The construction is not just the height-squared rank in disguise

For every integer `h>=1`,

\[
\Phi(6^h)\le12^h,
\qquad
\frac{\Phi(6^h)}{(6^h)^2}\le3^{-h}\longrightarrow0.
\tag{2a}
\]

Indeed the first `h` shortcut steps are halvings. At position `0<=j<h`, the
baseline gives
`Gamma(2^(h-j)3^h)<=4^(h-j)3^h`, so its contribution to (1) is at most
`12^h/12^j` before rounding, hence at most the integer `12^h`. The whole tail
from time `h` contributes exactly `ceil(Phi(3^h)/3^h)`, at most

\[
\left\lceil\frac{(3^h+1)^2}{3^h}\right\rceil
=3^h+3\le12^h.
\]

This proves (2a). A height-squared rank already has bounded step growth; the
point here is that the minimal envelope preserves substantial arithmetic rank
savings on an explicit unbounded family, as well as the sublevel exponent.

### Proof and an exact stopping rule

At every positive integer,

\[
S(x)+1\le\frac32(x+1).
\]

Together with `Gamma(x)<=x^2` this gives

\[
\frac{\Gamma(S^j(n))}{3^j}
\le \left(\frac34\right)^j(n+1)^2.
\tag{3}
\]

The right side decreases to zero. If the current largest evaluated integer is
`B`, then once

\[
3^j(n+1)^2\le4^jB,
\tag{4}
\]

all later rounded candidates are at most `B`. This is an integer-exact stopping
rule. In particular, a cutoff that makes (3) at most one always suffices; it is
logarithmic in `n`. Each evaluated ordinary state has logarithmic bit size, and
the inherited prefix evaluator uses logarithmically many further steps.

The `j=0` term proves the lower bounds in (2). Every unrounded term is at most
the integer `(n+1)^2`, so rounding does not violate the upper bound. QED.

## 4. ORD-002: Bellman identity, minimality, and bounded transport

The following are exact all-input statements:

\[
\Phi(n)=\max\left(\Gamma(n),\left\lceil\frac{\Phi(S(n))}{3}\right\rceil\right),
\qquad
\Phi(S(n))\le3\Phi(n).
\tag{5}
\]

Moreover `Phi` is the **least integer-valued majorant** of `Gamma` with the
second property: if `F:N_{>0}->N` satisfies `F>=Gamma` and `F(Sn)<=3F(n)` for
every `n`, then `Phi(n)<=F(n)` for every `n`.

### Proof

Splitting the maximum in (1) at `j=0`, and using
`ceil(ceil(x)/3)=ceil(x/3)`, gives the first equality in (5). The second follows
immediately. Alternatively each candidate at `S(n)` is at most three times the
corresponding rounded candidate at `n`.

For minimality, induction gives
`Gamma(S^j n)<=F(S^j n)<=3^j F(n)`. Since `F(n)` is an integer, every rounded
term of (1) is at most `F(n)`. Taking the maximum proves the claim. QED.

### Same critical sublevel exponent

Let `N_Phi(M)=#{n>=2:Phi(n)<=M}`. APR-003 and (2) imply, for `M>=1`,

\[
\max(0,\lfloor\sqrt M\rfloor-2)
\le N_\Phi(M)
<5\bigl(\lfloor\log_4 M\rfloor+1\bigr)\sqrt M.
\tag{6}
\]

The upper bound holds because a `Phi` sublevel is contained in the corresponding
`Gamma` sublevel. The lower bound uses the integers `2<=n<=floor(sqrt M)-1`.
Consequently

\[
\sum_{n\ge2}\Phi(n)^{-s}<\infty\quad\Longleftrightarrow\quad s>1/2.
\tag{7}
\]

For convergence use dyadic shells and (6). At `s=1/2`, the upper bound in (2)
gives `Phi(n)^(-1/2)>=1/(n+1)`, so the series diverges; smaller exponents also
diverge. Thus prepaying the spikes does not sacrifice the old critical exponent.

### A function space preserved by actual one-step transport

Let `K` push a nonnegative mass on `{2,3,...}` forward by `T`, killing it on first
arrival at 1. For every real `p>=0`,

\[
\sum_{y\ge2}\Phi(y)^p(Kf)(y)
\le3^p\sum_{n\ge2}\Phi(n)^p f(n).
\tag{8}
\]

This follows by summing the pointwise bound (5) over the actual surviving
sources. Therefore a finite `Phi` moment cannot become infinite in a single
shortcut step. For `w_s(n)=Phi(n)^(-s)`, `s>0`, the at-most-two predecessor
formula also gives

\[
(K w_s)(y)\le2\,3^s w_s(y).
\tag{9}
\]

For `s>1/2`, these are strictly positive summable weights. Equations (8)--(9)
give bounded operators, **not contraction**: their displayed constants exceed
one. A general signed mass has the same norm bounds by positivity.

The change of space is real. Finite `Gamma` moment is a weaker hypothesis than
finite `Phi` moment; the old moment-explosion example need not belong to the
new space. No claim is made that the old source envelope automatically gains
this stronger integrability after transport.

The inclusion is strict for every fixed `p>0`. Put
`kappa=2 log(4)/log(12)>1` and assign mass `3^(-kappa h p)/h` to `3^h`,
for `h>=10`. The inherited spike estimate gives
`Gamma(3^h)=3^h` and `Phi(3^h)>3^(kappa h)/3`. Thus this mass has finite
`Gamma^p` moment but infinite `Phi^p` moment. A rapidly decaying positive
background can be added if full support is desired.

Conversely, the new space is strictly larger than the elementary height-squared
moment space. For every `p>0`, the full-support mass

\[
f_p(n)=\Phi(n)^{-(p+1)}
 +\sum_{h\ge1}\frac{12^{-hp}}{h^2}\,\mathbf1_{n=6^h}
\]

has finite `Phi` moment by (7) and (2a), but its height-squared moment diverges:

\[
\sum_n n^{2p}f_p(n)\ge\sum_{h\ge1}\frac{3^{hp}}{h^2}=\infty.
\]

Thus using `(n+1)^2` directly would lose admissible source distributions that
the new bounded-transport space retains. This is a strict function-space
improvement, not merely a relabeling of ordinary height.

## 5. ORD-003: a total, logarithmic-time contact map

Define the contact set

\[
\mathcal C=\{n\ge2:\Phi(n)=\Gamma(n)\}.
\]

Every positive source reaches `C` or 1 after `O(log(n+1))` shortcut steps.
More explicitly, for `n>=2`, it cannot spend `j` consecutive steps outside
`C` before absorption whenever

\[
4^j(\Phi(n)-1)>3^j(n+1)^2.
\tag{10}
\]

### Proof

At a noncontact state, (5) says
`Phi(n)=ceil(Phi(Sn)/3)`. Hence

\[
\Phi(Sn)-1\ge3(\Phi(n)-1).
\tag{11}
\]

If the first `j` states are noncontact and absorption has not occurred, iterate
(11) and combine it with (2)--(3):

\[
3^j(\Phi(n)-1)
\le\Phi(S^j n)-1
<(9/4)^j(n+1)^2.
\]

Condition (10) contradicts this. Since `Phi(n)>=n`, the least such `j` is
`O(log(n+1))`. QED.

The first *positive-time* return from a contact state to `C`, killed on hitting
1, is consequently also a total finite operation, with a logarithmic clock
bound depending on its source. This is a different induced map from PR106's
safe/unsafe return map. Its ranks, source measure and stopping set must not be
silently substituted into the older transport theorems.

**The remaining sufficient target is precise.** Prove a strict inverse
supersolution inequality on this actual contact-return operator for a strictly
positive summable weight, or construct a total physical lower-`Phi` merging
selector on `C`. Neither is supplied here. Bounded one-step growth does not
give a uniform bound for an unbounded number of return steps; multiplying (8)
by the actual return clock produces `3^(p r)`, which still requires control.

### Contact first return does not decrease the rank

The complete physical examples

\[
11\longmapsto17\longmapsto26,\qquad
19\longmapsto29\longmapsto44
\]

have contact endpoints and noncontact interiors. Their endpoint ranks are
`48 -> 192` and `192 -> 1728`, respectively. Thus merely inducing on `C` does
not give a lower-rank selector. The next subsection computes the complete
inverse fans and rules out all unmodified decreasing rank-only weights for
the proposed row inequality.

### The old compulsory-spike family is absorbed into the new interface

APR-009 proves, for `n=3^H`, `H>=1`,

\[
\Gamma(n)=n,\qquad
\Gamma(Tn)>n^\kappa,
\quad \kappa=\frac{2\log4}{\log12}>11/10.
\]

Thus

\[
\Phi(3^H)>\frac13\,3^{\kappa H},
\qquad
\frac{\Phi(3^H)}{\Gamma(3^H)}>\frac13\,3^{(\kappa-1)H}\longrightarrow\infty.
\tag{12}
\]

For `H>=10`, the weaker exponent `11/10` already implies `Phi(3^H)>Gamma(3^H)`.
For `H=1,...,9`, exact replay gives the respective `Phi` values

`8, 16, 196, 1600, 33368, 132496, 1196836, 10758400, 217936328`.

Every positive power of three is therefore outside `C`. This is an all-`H`
consequence of the inherited spike theorem plus nine finite exact checks. It
does not imply that all other unsafe sources are removed.

The replay also records many larger powers, up to `3^128`. Their apparent
quadratic growth is an observation, not a newly proved asymptotic formula.
The `6^h` savings in (2a) were also replayed for `1<=h<=128`.

### ORD-005: complete finite inverse contact fans

Let `R_C(x)=y` be the first positive-time contact return, with shortcut clock
`r>=1`, and `y in C`. Write `M=Phi(y)` and

\[
D=\lceil\log_3 M\rceil.
\]

Then every such source has `r<=D`. Consequently **every inverse row of the
actual contact-return operator is a finite, completely enumerable set**.
There is no unexamined inverse tail in this interface.

For `r>=2`, the `r-1` interior states are noncontact. Repeated use of (5) and
`ceil(ceil(a/3)/3)=ceil(a/9)` gives

\[
\Phi(Sx)=\left\lceil\frac{M}{3^{r-1}}\right\rceil\ge2.
\]

Hence `M>3^(r-1)`, or `r<=ceil(log_3 M)`. The same bound holds for `r=1`
because `M>=2`. This proves the depth bound.

To enumerate, start at `y` and use the exact shortcut predecessors `2z` and,
when it is a positive odd integer greater than 1, `(2z-1)/3`. Stop a branch
as soon as a contact predecessor is reached; expand a noncontact predecessor.
Along an expanded edge its `Phi` rank is the previous rank divided by three,
rounded up, and is strictly smaller. The depth bound prevents an infinite
branch. Every stopped source has the required physical return, and every
physical return must occur in this search by following its inverse path.

The binary tree immediately gives at most `2^(D+1)-2` tested predecessors.
Independent review sharpened this substantially. At inverse depth `d>=1`,
each tested predecessor `x` has a parent of rank
`ceil(M/3^(d-1))` (for `d=1`, the parent is the endpoint itself). Since each
shortcut predecessor is at most twice its parent, every such `x` satisfies

\[
x\le2\left\lceil\frac{M}{3^{d-1}}\right\rceil.
\tag{12a}
\]

There is at most one path from a particular source at a particular depth,
because its forward map is deterministic. Thus (12a) also bounds the width.

The unrestricted shortcut inverse tree has depth-`d` width at most `F_(d+2)`,
where `F_0=0,F_1=1` are Fibonacci numbers. To see this, a target of residue
zero modulo three has only one predecessor, also residue zero; a target of
residue one has only one predecessor, residue two; and a target of residue
two has one even predecessor of residue one and possibly one odd predecessor
of arbitrary residue. Induction therefore bounds the three types' widths by
`1,F_(d+1),F_(d+2)`. Killing at 1 and stopping at contacts only removes nodes.

Consequently the complete number of tested nodes is at most

\[
\sum_{d=1}^{D}\min\left(F_{d+2},
  2\left\lceil\frac{M}{3^{d-1}}\right\rceil\right)
=O(M^\alpha),
\quad
\alpha=\frac{\log\varphi}{\log(3\varphi)}\approx0.3046,
\quad \varphi=\frac{1+\sqrt5}{2}.
\tag{12b}
\]

Split the sum where `(3 phi)^d` is of order `M`: its increasing geometric
part and decreasing geometric part both have order `M^alpha`; the ceilings
add `O(log M)`. This is a complexity bound for one exact inverse row, **not**
a bound on the number of exceptional Collatz sources. Each accepted source
comes with its exact clock. The implementation checks the depth, source-height
and width bounds and raises an error on failure, rather than silently
discarding an over-budget branch.

Two exact rows are:

| Contact endpoint | Phi(endpoint) | All contact predecessors, with (clock, Phi) |
|---:|---:|---|
| 26 | 192 | 11: (2,48); 34: (2,1024); 52: (1,2704) |
| 44 | 1728 | 19: (2,192); 58: (2,3136); 88: (1,7744) |

For `w_s=Phi^(-s)` and **every** `s>0`, the source 11 alone gives

\[
(K_Cw_s)(26)\ge w_s(11)=4^s w_s(26)>w_s(26).
\]

So a global inverse supersolution is not obtained by trying another positive
power of the new rank. More generally any strictly positive nonincreasing
function of `Phi` alone fails at this row: its source-11 contribution is at
least its endpoint-26 weight, and the two other predecessors contribute
strictly positive amounts. A successful weight needs information beyond a
monotone function of `Phi`, or a further certified induction/return mechanism.
For `s=1`, the exact full row ratios are `11515/2704` at 26 and `57951/5929`
at 44. These are failures of the suggested weight, not failures of the finite
inverse-row theorem. They concern the current contact operator killed only
at one. Finite corrections to the weight or enlarging a certified terminal
set are not excluded by these two rows.

## 6. ORD-004: the exact critical real factor 9/4

There is an additional real-valued version:

\[
\Psi(n)=\sup_{j\ge0}(4/9)^j\Gamma(S^j n).
\tag{13}
\]

The supremum is attained, is rational, and is computable by a total finite
algorithm. It satisfies

\[
\Gamma\le\Psi\le(n+1)^2,\qquad
\Psi(n)=\max\{\Gamma(n),(4/9)\Psi(Sn)\},\qquad
\Psi(Sn)\le(9/4)\Psi(n).
\tag{14}
\]

It is the least real majorant with this growth bound. The same sublevel
exponent and corresponding bounded-transport statements follow.

### Why critical-tail evaluation terminates

At an odd nonabsorbed step, `(Sx+1)/(1.5(x+1))=1`. At an even source `x>=2`,
the same ratio is

\[
\frac{x+2}{3(x+1)}\le\frac49.
\]

If `E_j` is the number of even steps before time `j`, then

\[
(4/9)^j\Gamma(S^j n)
\le (16/81)^{E_j}(n+1)^2.
\tag{15}
\]

After the right side is at most the current maximum, every future candidate
is bounded. An unabsorbed positive ordinary orbit must have infinitely many
even steps: an all-odd tail would decrease the finite integer
`v_2(x+1)` by one on every step. Hence the algorithm reaches this cutoff or
absorption. No assumption of Collatz convergence is used.

This argument does **not** give the logarithmic shortcut-time complexity of
`Phi`. The number of required even steps is logarithmic, but their intervening
odd runs can become long. Also, rounding (13) to integers does not preserve
the exact factor `9/4`; (14) is deliberately stated for the rational envelope.

## 7. Validation and adversarial cases

Run from the repository root:

```sh
python -B experiments/beeping-density-swarm-20261030/check_rank_envelope.py --bound 10000 --out /tmp/rank-envelope.json
```

The saved result is
[rank_envelope_results.json](../../experiments/beeping-density-swarm-20261030/rank_envelope_results.json).
The recorded run checked the
size inequalities, integer Bellman identity and factor-three bound for every
`2<=n<=10000`. Separate implementations replayed `Gamma` and `Phi` for
`2<=n<=1000`; the reference prefix evaluator deliberately continued beyond the
proved candidate cutoff, and the reference envelope used a fixed tail bound
and backward Bellman recursion. Eleven selected critical real envelopes were
also checked exactly with rational arithmetic.

The contact-return checker additionally followed all contact sources through
1000, finding 718 nonkilled source/endpoint pairs and 552 distinct endpoint
fans. It replayed every one of their 1011 listed inverse leaf paths and checked
that each original forward source was recovered with the correct clock. These
are bounded interface tests; completeness beyond the sample follows from
ORD-005, not from the finite census.

There were `5590` one-step decreases and `4409` increases in the tested range;
`7174` sources were contact states. These finite frequencies have no asserted
asymptotic meaning. The first rank increases include

| Source | Next source | Phi before | Phi after |
|---:|---:|---:|---:|
| 3 | 5 | 8 | 22 |
| 5 | 8 | 22 | 64 |
| 9 | 14 | 16 | 48 |
| 14 | 7 | 48 | 49 |

So even a numerical halving can increase this rank. Properness, bounded
transport and a total contact map are established; global descent is false.
The longest evaluated envelope horizon in that finite range was 23 steps,
and the longest contact-hitting time was seven steps. These numbers validate
interfaces only. The universal claims rest on the displayed proofs.

The code raises explicit exceptions for failed checks and does not depend on
Python `assert`, optimization-sensitive tests, external packages, or a
trajectory-until-convergence loop.

## 8. Research significance and limits

The earlier obstruction showed that the particular `Gamma` moment can blow
up in a single step. It did not prove that every rank with its useful counting
exponent has this defect. The envelope gives an explicit counterexample to
that broader inference, and is optimal within the stated majorant class.
It leaves the half-exponent counting law intact and supplies a function space
in which actual shortcut transport is bounded.

The remaining mathematical cost is visible: the operator bound is greater
than one; `Phi` changes the source integrability condition; and control of
the induced contact return requires a new estimate. No safe-region decay rate,
all-source envelope reset, or inverse supersolution is inherited automatically.
The next useful experiment is to search for an arithmetic weight on the
contact set and measure its complete inverse fibers with the actual return
clocks, retaining failures. A theorem must then control those fibers uniformly
for one fixed ordinary source population. The present packet does not supply
that theorem or a Collatz proof.
