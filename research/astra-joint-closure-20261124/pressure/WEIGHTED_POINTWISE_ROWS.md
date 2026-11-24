# A one-fifth lower exponent on individual ordinary paired rows

**Status: PROPOSED theorem with an exact finite integer certificate.**
For the positive shortcut map, write \(N_{e,p}(q)\) as in
[FIRST_HIT_PACKING.md](FIRST_HIT_PACKING.md): one fixed odd positive
target prime to three, two literal endpoints \(q,5q\), one common
physical clock \(e\), equal grades \(p\), odd unit sources, and
first-arm real affine offset at most \(1/2\).

**Theorem.** For every fixed such \(q\) and every sufficiently large real
\(X\), some *single* row satisfies, with \(G=2^e/3^p\),
\[
 X/(2^{400}q)\le G\le X/(q-1/2),\qquad
 N_{e,p}(q)\ge c_q X^{1/5}/\log X .
\]
The exhibited sources lie in \([X/2^{400},X]\).
In particular a single failed comparison at \(q\) would imply
\(\gg_q X^{1/5}\) failed comparisons up to \(X\) when summing the rows.
There is no assumption about the convergence or nonconvergence of either arm.

The earlier uniform first-return pressure theorem gives exponent \(1/9\)
for an aggregate tree. Here a larger finite bank and a nonconstant
weight on the child's first four ternary digits give \(1/5\); a fixed
terminal branch and a bounded number of grades per clock then give
the individual-row estimate. This argument supplies neither central
balance \(p/e\to1/2\) nor the near-linear exponent requested by PT.
[PR 200 pressure theorem, exact source](https://github.com/GettysburgResearch/collatz/blob/9fc000d840f365340539e426c9beb05a34edbd82/research/regularity-rigidity-20261124/RATIO_PRESSURE.md)

## Complete branch bank and finite inequality

Track a cylinder \(x=r+2^h t\) at \(h\) shortcuts by its two endpoints
\(a+3^pt, b+5\cdot3^kt\). Start with \((h,r,a,b,p,k)=(1,1,2,8,1,1)\).
Stop a cylinder the first time \(p=k,\ b=5a\). Otherwise refine at the
next binary bit \(v\in\{0,1\}\). The new intercepts are
\(T(a+3^pv),T(b+5\cdot3^kv)\), and each grade increases by the
parity of its input. Prune at clock 27 or grade above 8 on either arm.
This gives 2,276 records \((h,r,p,C)\), where \(C=2^h a-3^p r\)
is the ordinary carry, positive and at most \(C_* = 73,526,095\).
The formula for each child cylinder follows by writing \(t=v+2t'\);
thus a record applies to every lift, beyond the finite replay examples.

For a parent \(y\) and record choose a padded clock \(j\) from
\(\max(h,\operatorname{bitlength}(3^p)+1)\) to 400. Retain it when
\(x=(2^jy-C)/3^p\) is an integer unit modulo three. Since \(C\)
is odd, each such \(x\) is odd. Also \(x\equiv r\bmod 2^h\), so its
first common return goes to \((2^{j-h}y,5\cdot2^{j-h}y)\) after
\(h\) clocks. Common halvings supply the odd endpoints \((y,5y)\).
Given the source, the first positive equal-grade ratio-five return
therefore identifies its record, and stripping powers of two from
that first endpoint identifies its parent and padding uniquely.

Put \(g=2^j/3^p>2\). The certificate specifies a positive integer
weight \(V(v)\) for every unit class \(v\bmod81\). For every positive
odd unit \(y\ge Q=2C_*+3\), the following inequality holds over its
actual inverse children:
\[
 \sum_{x} g^{-1/5}V(x\bmod81)>V(y\bmod81).
\]
Indeed, for each record, clock and possible child class \(v\), the
necessary and sufficient residue test is
\[
 y\equiv (C+3^pv)2^{-j}\pmod {81\cdot3^p}.
\]
The checker sums the lower integer weight
\(\lfloor 2^{20}g^{-1/5}\rfloor V(v)\) for each such incidence and
subtracts \(2^{20}V(y\bmod81)\). Every unit class modulo \(3^{12}\)
is tested. The minimum difference is exactly 14,671,262, attained
at residue 86,108. All fifth roots are integer floors verified by
bisection; no floating-point weights enter the certificate.
The modulus covers every grade since \(p\le8\). Positivity holds at
all actual nodes since \(x=g y-C/3^p\ge(3/2)y\) for \(y\ge Q\).
The checker also literally replays each first return on three lifts.
[Checker](check_weighted_pressure.py) · [Exact output](../../../reports/astra-joint-closure-20261124/pressure/WEIGHTED_PRESSURE.json)

## From weighted branches to the supplied target and clock

Choose a fixed padded branch with chronological initial six-bit word
\(101000\) and map \(F_a(z)=(9z+7)/2^a\). For \(z=64t+49\), direct
iteration gives the six-clock pair \((9t+7,5(9t+7))\) and two odd
inputs per arm. Choose \(a\ge6\) so \(2^a q\equiv7\pmod9\) but
\(2^a q\not\equiv7\pmod{27}\). The powers of two generate the
18 unit classes modulo 27, so such exponents are arbitrarily large.
Then \(q_0=(2^a q-7)/9\) is an odd unit in the prescribed binary
cylinder. Take \(a\) large enough that \(q_0\ge Q\) and
\((18C_*+7)/2^a\le1/2\). This choice depends on the target, once only.

Grow the finite-branching inverse tree from \(q_0\); heights increase
by at least \(3/2\) per edge and at most \(2^{400}\). The unique-parent
decoder and strict height increase imply that every tree vertex has a
different ordinary value. Give each child probability proportional to
\(g^{-1/5}V(x\bmod81)\). The finite pressure inequality bounds the
probability of a path to \(x\) by
\[
 (\prod g)^{-1/5}\frac{V(x\bmod81)}{V(q_0\bmod81)}
 \le (q_0/x)^{1/5}\frac{\max V}{\min V},
\]
because \(x\le q_0\prod g\). Stop on first attaining height
\(X/2^{400}\). This finite stopping set has total probability one
for sufficiently large \(X\); each endpoint lies in
\([X/2^{400},X]\). Thus it contains \(\gg_q X^{1/5}\) distinct
ordinary sources.

Read each stopped path forward to \(q_0\). Its individual affine
maps have slope \(1/g\le1/2\) and offset \(C/2^j\le C_*\).
Composition gives total first-arm offset at most \(2C_*\) by the
geometric series. Append the same \(F_a\) to every such trajectory.
The two arms reach exactly \(q,5q\), and the final first-arm offset
is at most \(1/2\) by choice of \(a\). All the words consist of
completed paired return records with common grade on both arms;
the possible terminal padding ends at an odd value.

For each resulting word, \(x=G(q-\beta)\) with
\(0\le\beta\le1/2\), giving the displayed scale range.
There are \(O_q(\log X)\) possible physical clocks: the inverse tree
has at most \(\log(X/q_0)/\log(3/2)\) edges, each of length at most 400,
and the terminal branch has fixed clock. At each fixed clock the scale
range spans a factor at most \(2^{400}q/(q-1/2)\), allowing only
\(O_q(1)\) integer grades because consecutive grades change scale by
a factor three. Pigeonholing over these rows proves the assertion.

## Remaining gap

The potential controls height growth across all eligible paths and
allows their clock and grade ratios to vary. Taking a subsequence
of these rows fixes a limiting ratio, without prescribing its value.
The argument gives no pointwise estimate at a specified central ratio.
The first-hit packing bound permits both this lower exponent and the
stronger, still-open PT lower bound along selected central rows.
