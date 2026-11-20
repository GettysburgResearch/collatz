# Positive energy renewal on the complete ladder family

**PROPOSED elementary consequence of FL1--FL3. The uncovered energy is
still open; this is not a Collatz proof.** No GRH input is used.

This extends the single-block renewal in PR163, full source head
`051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
`research/deep-reverse-closure-20261120/CLOSING_ATTEMPTS.md`, section D.
That source proves the coefficient `64/441` for the single cylinder
`x=49 mod64`. Here all the disjoint ladder cylinders are included.

## Definitions and statement

Let f take values in a metric space and satisfy f(Tn)=f(n) on every
positive ordinary integer. For odd ternary units, put

\[
 d_5(x)=d(f(5x),f(x)),\qquad
 E(X)=\sum_{\substack{1\le x\le X\\x\text{ odd},\ 3\nmid x}}
       \frac{d_5(x)}x.
\]

Let H be the union of all the cylinders in FL3 of
[FIVE_CERTIFICATE_LADDER.md](FIVE_CERTIFICATE_LADDER.md), restricted to
odd ternary units. Let R(X) be the same sum restricted to x outside H.
All sums at finite X are finite and nonnegative. Then

\[
\boxed{E(X)\le R(X)+\frac{16}{21}E(X/7).}                 \tag{R1}
\]

Consequently

\[
\boxed{E(\infty)<\infty\quad\Longleftrightarrow\quad
R(\infty)<\infty,\qquad
E(\infty)\le\frac{21}{5}R(\infty)\quad
\text{when }R(\infty)<\infty.}                          \tag{R2}
\]

The set H has relative density 1/24 among odd ternary units. This is a
larger source domain than PR163's single-block domain, with a different
upper coefficient. It is not a full cover or a bound on R.

## Proof with source multiplicity and truncation

For x in H there is a unique initial word `(2 repeated r times, b)` with
r>=1 and b>=4. Let its actual endpoint be q. FL1--FL3 give

\[
T^{2r+b}(x)=q,\qquad T^{2r+b}(5x)=5q,\qquad q\le x/7,
\]

where q is a positive odd ternary unit. Thus d_5(x)=d_5(q).

Fix r and q. All integral inverse sources have

\[
x_b=\frac{2^{2r+b}q-B_r}{3^{r+1}},\qquad
B_r=4^{r+1}-3^{r+1}>0.                                  \tag{R3}
\]

Integrality is equivalent to
`2^(b-2)q=1 mod3^(r+1)`. Since 2 has exact order
`P_r=2*3^r` modulo `3^(r+1)`, these b occupy one progression
`b=b_0+kP_r`, k>=0, with b_0 its least member at least four.
Every member gives a positive odd source with the stated initial word.
The additional guard `3 not dividing x_b` can only delete sources.

The inverse formula also gives

\[
x_{b_0}=1+(4/3)^r\frac{2^{b_0}q-4}{3}
       \ge 4(4/3)^r q,
\]

because b_0>=4 and q>=1. Since B_r>0, (R3) yields

\[
x_{b_0+kP_r}\ge 2^{kP_r}x_{b_0}.
\]

It follows, including the possibly deleted nonunit sources in the upper
bound, that

\[
\sum_{\substack{b\ge4\\b\text{ legal},\ 3\nmid x_b}}
\frac1{x_b}
\le\frac{(3/4)^r}{4(1-2^{-2\cdot3^r})}\,\frac1q.
\]

The cylinders for different r are disjoint, and each actual source has
one endpoint and exponent word. There is no unidentified source
multiplicity in this sum. As `2*3^r>=6`, the complete nonnegative sum
over r satisfies

\[
\sum_{r\ge1}\frac{(3/4)^r}{4(1-2^{-2\cdot3^r})}
\le\frac1{4(1-2^{-6})}\sum_{r\ge1}(3/4)^r
=\frac{16}{21}<1.                                       \tag{R4}
\]

Restricting the original sources to x<=X restricts every endpoint to
q<=X/7. Applying the preceding source bound separately at each q proves
`E(X)-R(X)<=16 E(X/7)/21`, which is (R1). Since E(X/7)<=E(X), subtracting
the finite quantity `16 E(X)/21` gives `E(X)<=21 R(X)/5`. Take increasing
cutoffs. The converse in (R2) is immediate from R(X)<=E(X).

The finite cutoffs are essential: no subtraction of infinite energies
occurs in this proof.

## The same complete family also contracts at the subcritical exponent .84

For s>0 replace the weight 1/x in E and R by x^(-s), writing E_s and
R_s. The endpoint q=1 contributes zero: ordinary invariance and the
known path from 5 to 1 give d_5(1)=0. Every other odd ternary-unit
endpoint has q>=5. For such endpoints the earlier bound improves to

\[
x_{b_0}\ge (76/15)(4/3)^r q,
\]

since `(16q-4)/(3q)>=76/15`. The same complete geometric summation gives

\[
E_s(X)\le R_s(X)+C_s E_s(X/7),\qquad
C_s=\left(\frac{15}{76}\right)^s
\frac{(3/4)^s}{1-(3/4)^s}\frac1{1-64^{-s}}.                \tag{R5}
\]

At the rational exponent s=21/25=.84, exact bounds give

\[
(15/76)^s<13/50,\quad (3/4)^s<393/500,\quad64^{-s}<1/32.
\]

The first two are verified without numerical rounding by the integer
inequalities

\[
15^{21}50^{25}<76^{21}13^{25},\qquad
3^{21}500^{25}<4^{21}393^{25}.
\]

The last follows from `6*21/25>5`. Thus

\[
\boxed{E_{.84}(X)\le R_{.84}(X)
       +\frac{81744}{82925}E_{.84}(X/7),\qquad
       \frac{81744}{82925}<1.}                           \tag{R6}
\]

In particular finiteness of the full .84 energy is equivalent to
finiteness on the uncovered complement, and in the finite case

\[
E_{.84}(\infty)\le\frac{82925}{1181}R_{.84}(\infty).
\]

This is a deliberately coarse rational coefficient. It suffices to
retain contraction at the subcritical exponent used in PR163. The
argument uses no assumption that an arbitrary endpoint q converges.
Only the already proved edge from 5 to 1 removes the q=1 term.

## What the theorem does and does not complete

PR163's `FIVE_SLICE_ENERGY.md` propagates finite five energy to the full
tripling energy, with its stated source qualifications for the subsequent
rigidity consequences. R1 enlarges the family on which the five defect can
be charged to a smaller actual source; R6 does the same at exponent .84.
Both leave the full complement R_s.

Nothing proved here forces the defect of every uncovered source into H,
or bounds its sum. The uncovered domain is infinite. Its relative density
does not determine its harmonic energy for an unknown invariant label.
The finite-prime constructions under GRH in [GRH_INTERFACES.md](GRH_INTERFACES.md)
do not estimate this label-dependent remainder. Thus R2 sharpens the
identified analytic obligation, but does not settle it.

`check_ladder_renewal.py` checks the inverse progressions, positive
geometric comparison, exact rational coefficient and finite truncation
constraints. These finite checks support the implementation; the proof
above supplies the unbounded statement.
