# Two different five-failure certificates below one thirteenth of the reverse source

**Status: proved conditional exclusion target, not a proof of Collatz.**

For every hard rank-five Mersenne candidate that is the *global least
reverse failure*, this note constructs a smaller physical-five failure
whose source begins with valuation **three or four**, instead of the
first-valuation-one construction in latest PR146. Both the source and its
next five comparison antecedent have explicit ordinary paths into the
same already proved initial interval. This produces two additional
physical certificate boundaries that a complete compiler must handle.

The source dependencies are:

- PR163 `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
  `research/deep-reverse-closure-20261120/LEAST_FAILURE_HEIGHT.md`, H2:
  if \(X\) is the global least reverse failure, then
  \(176106n<X\Rightarrow n\in C\).
- PR163, `MERSENNE_WITNESS_DEPTH.md`, equations (1)--(2): the ordinary
  Mersenne predecessor and upper family used below.
- PR146 `fd991063721e9c157d318e40bb20131762f7d750`,
  `research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md`:
  the earlier first-valuation-one smaller-five construction.
- Live PR146 `66970775e4bdc945a68308e37a8eb028ebde42d2`,
  `research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md`: reviewed
  after this construction. Its prescribed-class lift does not give a
  smaller comparison for a fixed input, so it is not used to discharge
  any query here.

Use the ordinary positive shortcut map \(T\), its basin \(C\), and the
odd map \(U(n)=(3n+1)/2^{v_2(3n+1)}\). Put \(H=176106\).

## SF1. The exact smaller-five construction

Let

\[
e=119+162j,\qquad P=2^e,\qquad
M=P-1,\qquad X=\frac{1024P-2573}{243}.
\]

Suppose this \(X\) is the global least reverse failure. Its actual lower
companion is in the ordinary component of \(M\), so \(M\notin C\).

Define

\[
q=\begin{cases}
\displaystyle\frac{32P-61}{135},&e\equiv119\pmod{324},\\[6pt]
\displaystyle\frac{128P-271}{405},&e\equiv281\pmod{324}.
\end{cases} \tag{1}
\]

**Theorem.** These are positive odd ternary units and, in both cases,

\[
\boxed{q<X/13,\qquad q\in C,\qquad5U(q)\in C,
\qquad5q\notin C.} \tag{2}
\]

The memberships in (2) use the same least-source \(X\). No separate
minimum within one rank or one exponent class is used.

### Integrality and the target's ordinary path

The exponent progression gives

\[
4P\equiv11\pmod{243}.
\]

Consequently

\[
32P-61\equiv27\pmod{243},\qquad
128P-271\equiv81\pmod{243}. \tag{3}
\]

Their ternary valuations are exactly three and four, respectively. The
remaining factor of five divides the first numerator when \(P\equiv3\)
modulo five and the second when \(P\equiv2\) modulo five. These are
precisely the two exponent classes in (1). The odd numerators and odd
denominators prove oddness; (3) proves the unit condition.

Starting at \(M\), the legal positive inverse words give

\[
Y_0=I_1I_2(M)=\frac{8P-13}{9},
\]

\[
Y_1=I_2(Y_0)=\frac{32P-61}{27},\qquad
Y_2=I_2(Y_1)=\frac{128P-271}{81},
\]

where \(I_a(v)=(2^a v-1)/3\), only at the displayed integral odd
values. Therefore the actual target words are

\[
5q\xrightarrow{(2,1,2)}M
\quad\hbox{or}\quad
5q\xrightarrow{(2,2,1,2)}M. \tag{4}
\]

The notation lists exact accelerated odd exponents. Thus \(5q\notin C\)
in either phase.

The exact source-height identities are

\[
q=\frac{9X+23}{160}
\quad\hbox{or}\quad
q=\frac{3X+5}{40}. \tag{5}
\]

Since \(X>65\), each is strictly less than \(X/13\). The first phase
even has \(q<X/17\). These are inequalities for the actual fixed
integers, including their additive terms.

## SF2. Both successor-five values have a small ordinary representative

In the first phase, the source first exponent is four and

\[
U(q)=\frac{2P-1}{45},\qquad
5U(q)=\frac{2P-1}{9},\qquad
T^2(5U(q))=2^{e-1}+1. \tag{6}
\]

In the second phase the source first exponent is three and

\[
U(q)=\frac{16P-17}{135},\qquad
5U(q)=\frac{16P-17}{27},\qquad
T^5(5U(q))=2^{e-1}+1. \tag{7}
\]

All clocks here are literal shortcut clocks. Since \(e-1\) is even,
repeated two-clock ordinary blocks give

\[
T^{e-1}(2^{e-1}+1)=3^{(e-1)/2}+1. \tag{8}
\]

At the first allowed exponent,

\[
H(3^{59}+1)
=2488445773071741578696111817941208
<2800677917044761016159461789561878273=X_{119}. \tag{9}
\]

When \(e\) increases by 162, \(X\) grows by more than \(2^{162}\),
whereas \(3^{(e-1)/2}+1\) grows by less than \(3^{81}\). Since
\(3^{81}<2^{162}\), (9) persists for every allowed exponent. H2 at
the same least \(X\) now proves \(5U(q)\in C\) in both phases.

## SF3. The valuation-three phase has a short source prefix and a fast tail

For \(e\equiv281\pmod{324}\), the exact source word

\[
(3,2,1,4)
\]

reaches

\[
r=\frac{2^{e-3}+1}{5}. \tag{10}
\]

This is an identity on the entire exponent progression, not a numerical
prefix observed at selected exponents. For example its affine form is

\[
T^{10}(q)=\frac{81q+259}{1024}=r.
\]

The exact odd parities follow from the fixed low binary bits of the
source; the independent checker verifies them in the affine parameter.

For every applicable integer \((F2^\ell+1)/5\) with \(\ell\ge3\),
the ordinary three-clock block with parities odd, even, even gives

\[
T^3\left(\frac{F2^\ell+1}{5}\right)
=\frac{3F2^{\ell-3}+1}{5}. \tag{11}
\]

Here \(e\equiv2\pmod3\). Thus \(m=(e-5)/3\) applications of (11)
take (10) to

\[
R=\frac{4\cdot3^m+1}{5}<3^m. \tag{12}
\]

The exact first-exponent inequality

\[
H3^{92}<X_{281}
\]

holds. At each increase \(e\mapsto e+324\), its left side grows by
\(3^{108}\), whereas \(X\) grows by more than \(2^{324}\).
Therefore \(HR<X\) holds throughout this phase. The complete ordinary
source prefix has \(10+3m\) shortcut clocks. H2 proves \(q\in C\).

## SF4. The valuation-four phase has a different contracting rational cycle

For \(e\equiv119\pmod{324}\), the exact source word

\[
(4,1,2,1,1,2,1)
\]

reaches

\[
r=\frac{81\cdot2^{e-7}+19}{5}. \tag{13}
\]

Its shortcut clock is 12 and its affine form is

\[
T^{12}(q)=\frac{2187q+16553}{4096}=r.
\]

For \(\ell\ge5\), the actual five-clock parity block odd, odd, odd,
even, even satisfies

\[
T^5\left(\frac{F2^\ell+19}{5}\right)
=\frac{27F2^{\ell-5}+19}{5}. \tag{14}
\]

This is the rational offset cycle with fixed value \(19/5\) for the
five-clock affine map; the actual inputs in (14) are ordinary positive
integers. Its slope is \(27/32<1\). When the endpoint remains odd, the
accelerated word is \((1,1,3)\). If the last block ends at an even
integer, (14) is still the exact ordinary five-clock prefix; no extra
accelerated parity is claimed.

Write \(e-7=5m+\ell\), with \(0\le\ell\le4\). After \(m\)
blocks, the endpoint is

\[
R=\frac{81\cdot27^m2^\ell+19}{5}
\le20\cdot27^m2^\ell. \tag{15}
\]

It has the useful uniform bound

\[
\boxed{R^5<3^{3e}.} \tag{16}
\]

Indeed, using \(e=5m+\ell+7\),

\[
\frac{R^5}{3^{3e}}
\le\frac{20^5}{3^{21}}\left(\frac{32}{27}\right)^\ell
\le\frac{20^5 32^4}{3^{33}}<1,
\]

where the final exact comparison is

\[
3355443200000<5559060566555523.
\]

At \(e=443\), the checker verifies the integer inequality

\[
H^5 3^{1329}<X_{443}^5. \tag{17}
\]

For every subsequent increment by 324, the left side grows by
\(3^{972}\) and the right side by more than \(2^{1620}\). Since
\(27<32\), (17) persists. Together with (16), it proves \(HR<X\)
for every exponent in this phase starting at 443. The source ordinary
prefix has \(12+5m\) clocks, so H2 proves \(q\in C\).

The one remaining exponent is \(e=119\). Here the exact 136-clock
ordinary prefix from

\[
q=157538132833767807158969725662855653
\]

ends at

\[
9900175581272098130203189984031.
\]

Multiplying this endpoint by \(H\) gives a number strictly below
\(X_{119}\) in (9). All 137 ordinary states are included in
`base_119_ordinary_prefix.json`, and the checker verifies every transition.
This is one fixed finite certificate, followed by H2, and does not stand
in for the all-exponent argument above. It completes the proof of (2).

## What these new boundaries require

The result moves the failed comparison into two different source
certificate patterns. It does not reverse a physical-five implication or
remove the target's affine offset.

Let \(u=U(q)\), whose five multiple is already certified by SF2. In the
valuation-four case,

\[
U(5q)=20u-1=4(5u)-1;
\]

in the valuation-three case,

\[
U(5q)=10u-1=2(5u)-1.
\]

Consequently the remaining physical tasks are to certify these shifted
targets from the actual known certificate for \(5u\), or to produce a
reverse query whose upper source stays strictly below the original
\(X\). The known generic all-source reverse conversion has cost
\((10126085/23)q\), so substituting \(q<X/13\) still does not pay that
return cost. The corresponding scalar two-way budget product is
\(10126085/299>1\).

The formulas above do not yet supply a smaller reverse instance. They
supply actual smaller five failures, with different initial valuations
and fully justified source memberships, for a subsequent physical
construction to use. Treating either shifted target as already certified
would be the first unsupported step.

## Verification

```bash
python -B check_smaller_five_failures.py
python -O -B check_smaller_five_failures.py
```

The checker proves the short affine prefixes with exact rational
arithmetic and a uniform two-adic guard, checks the two unrestricted
cycle blocks, and checks the exact induction bases. It separately replays
the actual positive paths at 32 exponents. Those bounded replays test the
implementation; the coefficient identities and growth comparisons prove
the unbounded statements. `smaller_five_report.json` records the checks.
