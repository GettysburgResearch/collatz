# Rational points where the ternary stationary envelope is infinite

**SOURCE-QUALIFIED written theorem.** Let \(E\) be Valbuena's greatest
lower semicontinuous representative of the ternary Syracuse stationary
density, relative to full additive Haar probability on \(\mathbb Z_3\).
Let \(\rho_j(z)=3^j\mu(z+3^j\mathbb Z_3)\), with \(\rho_0=1\).
Use the two rational affine maps
\[
 F_0(x)=x/2,\qquad F_1(x)=(3x+1)/2.
\]
On a rational with odd denominator the genuine shortcut map chooses its
branch by numerator parity. Formal images with arbitrary choices use
separate notation \(F_w\). The following distinction decides every
rational point of \(\mathbb Z_3\) structurally.

1. If \(z\) has odd denominator, then \(E(z)=\infty\) if and only if
   \(z\) is a **negative periodic point** of that genuine shortcut map.
   At every other such rational, \(\sup_j\rho_j(z)<\infty\).
2. For any rational \(z\in\mathbb Z_3\), let \(k\) be the exponent of
   two in its reduced denominator. Then \(E(z)=\infty\) if and only if
   there are a length-\(k\) formal word \(w\) and a negative periodic
   rational \(r\) of odd denominator with \(F_w(r)=z\).
   At every remaining rational \(z\), \(\sup_j\rho_j(z)<\infty\).
3. In every nonempty open real interval \(I\subset(0,\infty)\), each
   sufficiently large denominator \(2^k\) supplies at least
   \(c_I2^k/\sqrt{k}\) **distinct reduced positive dyadic rationals**
   in \(I\) at which \(E=\infty\). Thus evaluating the unmarked
   envelope on a finer dyadic grid cannot give an upper approximation
   to its mean on the ordinary-integer grid.

The criterion does not enumerate the signed cycles or assume that all
rational or ordinary trajectories are periodic. A positive periodic
rational has finite envelope. A positive escaping integer, if one exists,
would also have finite envelope at every fixed point of its trajectory.

## Inputs and their scope

Valbuena proves \(E\ge LE\) pointwise for the binary inverse operator,
\(E\ge c>0\) on ternary units, \(\mu=E\lambda\), and \(E(n)=g(n)\)
at positive integers. In particular he already proves \(E(-1)=\infty\)
and \(E(-2^{-a})=\infty\); we use these facts with credit. His Lean
bundle has **outsider-reported verification; no local rebuild**.
Weaver 200, Prop. 4.3, already proves the uniform-in-depth bound at
negative nonperiodic **odd integer** targets. The reciprocal floor and
packing argument below extends that proof to signed numerator lattices,
handles an even terminal numerator explicitly, and treats the positive
periodic case by first hits. We use the external written fixed-total
count of Weaver 200, Input 3.3, whose derivation cites Weaver–Wren 48.

[Valbuena, pinned envelope theorem, superharmonic inequality and dense infinite values](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex)
· [Weaver, relative predecessor growth, Input 3.3, Lemmas 4.1–4.2 and Prop. 4.3](https://rstation.ai/problems/collatz/papers/200/v1)
· [Weaver–Wren, original bounded-real fixed-total count](https://rstation.ai/problems/collatz/papers/48/v2)

## 1. A signed reciprocal predecessor floor

Fix \(d\ge1\) coprime to six. The actual map on signed numerators is
\(T_d(n)=n/2\) on even \(n\), and \((3n+d)/2\) on odd \(n\).
For a nonperiodic odd unit numerator \(x\) (here unit means \(3\nmid x\)),
its predecessor basin has lower density at least \(c/(|x|+d)\) on
symmetric intervals \([-Y,Y]\), with an absolute \(c>0\).

To see this use the external fixed-total count, at precision zero beyond
the word length. For every sufficiently large depth \(j\), central total
\(|S-2j|\le\sqrt j\), and unit ternary class \(z\bmod3^j\), there
are at least \(c_1 2^S/(3^j\sqrt j)\) words of depth \(j\) and total
\(S\), whose real offset \(B_w\) is at most an absolute \(F\) and
whose ternary offset is \(z\). Here the affine map is
\(v\mapsto(3^j/2^S)v+B_w\), with \(B_w\ge0\). Apply this at
\(z=x/d\), a well-defined ternary unit. Let
\(L=\log_2(Y/(|x|+d))\), choose depths within \(c_2\sqrt L\) of
\(L/(2-\log_2 3)\), and take \(S=\lceil L+j\log_2 3\rceil\).
For small fixed \(c_2>0\), the central-total condition holds for all
large \(Y\) with this fixed target. Each compatible source numerator is
\[
 n=2^S3^{-j}(x-dB_w),\qquad |n|\le2\max(1,F)Y.
\]
Ternary legality gives integral inverse numerators at every step. Each
such numerator is odd since an inverse step is \((2^e v-d)/3\), with
\(e\ge1\). At the odd target the exponents are consequently the actual
valuations. Sources at the same depth are distinct by deterministic
forward decoding, and sources at different depths are distinct because
\(x\) is nonperiodic. There are order \(\sqrt L\) eligible depths,
each yielding at least a constant times \(Y/((|x|+d)\sqrt L)\)
sources. Rescale the fixed interval constant to get the claimed floor.
A signed population is essential here because a rational inverse prefix
at a small positive target can start at a negative numerator.

## 2. Uniform reciprocal packing for simple signed segments

For each fixed \(d\) as above, there exists \(C_d<\infty\) such that
every simple segment of \(T_d\) satisfies
\[
                 \sum_{n\text{ on segment},\ n\ne0} |n|^{-1}\le C_d.
\]
Here is the two-sided modification of Weaver 200, Lemma 4.2. Write
\(Y=2^m\), \(l=\lfloor m/4\rfloor\), and consider states with
\(Y\le |n|<2Y\). The last \(l\) positions cost at most \(l/Y\).
A parity cylinder of length \(l\) is a single residue modulo \(2^l\)
for odd \(d\), by the usual affine induction. Words with more than
\(3l/5\) odd steps occupy at most \(2^{lH_2(3/5)}\) classes, so their
reciprocal contribution is \(O(2^{-l(1-H_2(3/5))})\). All other
states have \(l\)-step images of absolute value at most
\[
 2Y(3^{3/5}/2)^l+d((3/2)^l-1).
\]
The affine offset bound follows from the all-ones word at real seed zero.
The images at eligible positions are distinct by simplicity. Their
reciprocal cost, still weighted at the original \(|n|\ge Y\), is
\(O((3^{3/5}/2)^l+d(3/2)^l/Y+1/Y)\). All displayed bounds are
summable over \(m\); the finitely many small states cost \(O(1)\).

Consequently the product of \(|3n/(3n+d)|\) over odd departing states
of any simple segment is at most \(K_d<\infty\). For \(|n|>2d\)
the positive part of its logarithm is \(O(d/|n|)\). Each of the
remaining finitely many odd states occurs once at most, and no denominator
vanishes because \(3\nmid d\).

## 3. Exact-depth first hits and the classification

For any nonzero signed target numerator \(t\), let \(A_j(t)\) sum the
multipliers \(\omega_w=3^j2^{-S_w}\) of the formal inverse odd words
of depth \(j\) whose ternary legality at \(t/d\) makes them actual
first hits of \(t\). At \(j=0\) use the empty word. At positive depth
each word gives a unique odd source \(n\). Internal inverse states
are odd; the final forward coast to \(t\) may stop at an even state.
Equivalently each path starts odd and reaches the prescribed state with
exactly \(j\) odd departures. Its exponents are determined uniquely:
all coasts but the last end at the next odd input, and the last ends at
\(t\) during the halving run. For \(t\ne0\), a halving run cannot
visit the same state twice. Distinct words of this depth have distinct
sources.

The nonperiodic leaves of any one first-hit layer have pairwise disjoint
predecessor basins. Indeed if one such leaf reached another before its
first hit of \(t\), the later leaf would have fewer odd departures left
(the starting leaf was odd). A leaf reached at or after \(t\) and
returning to \(t\) would be periodic. Apply the floor from Section 1
to all unit nonperiodic leaves to get
\(\sum_n (|n|+d)^{-1}\ll1\) over them. For nonunit leaves use the
injective charge \(n\mapsto4n+d\), which is a unit, with outermost
exponent increased by two. Its initial detour may pass through \(t\)
earlier than the original hit. This can happen only when the changed
segment before rejoining passes through \(t\): its added numerator
states after the new odd departure are \(2(3n+d)\) and \(3n+d\),
and the joining state is \((3n+d)/2\). Also the new start could equal
\(t\). The three affine equations give at most three exceptional \(n\)
per target and depth. In all other cases the charge is a first-hit leaf
of the same depth. If that charge is periodic, it belongs to the finite
cycle of \(t\). Since \(|4n+d|+d\le4(|n|+d)\), all the nonperiodic
nonunit leaves cost \(O_{d,t}(1)\), uniformly in \(j\). When \(t\)
is nonperiodic there are no periodic parents and, even retaining these
at most three exceptions, the upper bound is absolute. At periodic
\(t\), include its finitely many periodic leaves separately.

On any positive-depth first hit the visited states before and including
\(t\) are distinct (a repeat strictly before the first hit could never
reach a new target). Multiplying the affine step formulas now gives
\[
 \omega_w=\frac{|t|}{|n|}\prod_{i=1}^j
                \left|\frac{3n_i}{3n_i+d}\right|
 \ \le\ K_d |t|/|n|,
\]
with \(n_i\) the odd departures. Since \(|n|\ge1\),
\((|n|+d)/|n|\le1+d\). This proves
\(\sup_j A_j(t)<\infty\), and \(A_j(t)\ll_d |t|\) for nonperiodic
\(t\). If \(3\mid t\), positive-depth cylinder densities vanish
anyway.

The exact inverse-word expansion of \(\rho_j(t/d)\) sums these same
multipliers over **all** depth-\(j\) visits. At a nonperiodic target all
visits are first. At a positive periodic target, extra laps have one
fixed multiplier \(0<\Lambda<1\) and a fixed positive odd count \(s\);
this sign follows from \(t/d=\Lambda t/d+B\), \(B>0\). Thus the
all-visits bound is at most \(\sup_j A_j(t)/(1-\Lambda)\), with the
following even-target convention: if the source is odd and the target
even, every first hit already has positive odd count, so the empty word
at depth zero only overcounts possible laps. For an odd periodic source
that is itself the target, the empty first hit and later full laps are
included. At zero, \(\rho_j(0)=0\) for \(j\ge1\).

For every \(z\in\mathbb Z_3\), lower semicontinuity and
\(\mu=E\lambda\) give \(E(z)\le\liminf_j\rho_j(z)\). This proves
finiteness in the cases just bounded. At a negative periodic point
\(r\), the return of its genuine word has multiplier \(A>1\), since
\(r=Ar+B\) with \(B>0\). Units remain units under every physical
odd departure and halving; a nonzero cycle containing an odd departure
therefore consists of ternary units. Valbuena's pointwise inequalities
\(E(F_0x)\ge E(x)/2\), \(E(F_1x)\ge3E(x)/2\), and unit floor give
\(E(r)\ge A E(r)\), \(E(r)>0\). Hence \(E(r)=\infty\).

For denominator \(2^k d\), use binary stationarity of the actual
cylinder densities. For \(j\ge1\) it gives the pointwise equation
\[
 \rho_j(z)=\tfrac12\rho_j(2z)+
 \tfrac32\mathbf1_{z\equiv2\ (3)}\rho_{j-1}((2z-1)/3).
\]
After \(k\) legal inverse steps, every remaining leaf has denominator
dividing \(d\): each inverse step clears one power of two, and the odd
inverse is used only when its numerator is divisible by three.
For \(j\ge k\) this finite expansion consists of the leaf cylinder
densities at depths \(j-|w|_1\) weighted by \(3^{|w|_1}2^{-k}\).
If all these leaves have bounded cylinder densities, so does \(z\).
If a leaf is negative periodic, the pointwise superharmonic lower
inequalities transport its infinite value to \(z\). Conversely any
word taking an odd-denominator ternary integer leaf to \(z\) is legal
in this expansion. This proves assertions 1 and 2.

## 4. Positive dyadic grids contain many infinite values

The explicit signed path \(-1\mapsto-1/2\mapsto-1/4\mapsto1/8\)
uses formal branches \(0,0,1\). Hence \(v=1/8\) and all its formal
images have infinite envelope. A length-\(t\) image of \(v\) has
reduced denominator exactly \(2^{t+3}\), since from any reduced
numerator over \(2^b\) with \(b\ge1\), both branch numerators over
\(2^{b+1}\) are odd.

A uniformly random length-\(t\) formal image of \(v\) lands in a
fixed nonempty open interval \(I\subset(0,\infty)\) with probability
at least \(p_I>0\) for all large \(t\). An elementary proof avoids
assuming a density for the real stationary law. The one-step inequality
\[
 \mathbb E\sqrt{F_b(x)}\le
 (\sqrt{1/2}+\sqrt{3/2})\sqrt{x}/2+1/(2\sqrt2)
\]
has leading coefficient strictly below one, so some fixed \(M\) captures
at least half the mass at all dates. There is a fixed word mapping
\([0,M]\) into \(I\). Indeed the positive orbit of zero under the
formal semigroup meets every such interval: the values
\(2^{-b}((3/2)^a-1)\) are dense on the positive half-line, by
irrationality of \(\log_2(3/2)\) and choosing \(a,b\to\infty\).
For a word sending zero into \(I\), prepend enough halvings so that
the image of \([0,M]\) remains inside \(I\). The probability of this
one terminal word supplies the asserted uniform floor.

The number of odd letters under the uniform word law is binomial.
Choose fixed \(C_I\) so that, outside
\(|j-t/2|\le C_I\sqrt t\), the mass is at most \(p_I/2\).
At least \(p_I2^{t-1}\) words in that grade interval land in \(I\).
At a fixed grade the images of \(v\) are distinct: equality forces
identical affine intercepts since the slopes agree. Equal slope and
intercept give the same residue modulo \(2^t\) for the ordinary
integer seed making the endpoint integral. The parity-word bijection
makes this seed's word unique. Thus one rational image is counted at
most \(2C_I\sqrt t+2\) times. Setting \(k=t+3\) proves assertion 3.

For orientation, all \(\rho_j\) have Haar mean one, and \(E\) has Haar
mean one. The positive dyadic points above belong to a countable Haar-null
set. The classification explains which signed branches feed these poles.
It gives no upper control on the spatial average of the finite values
\(E(n)\) over ordinary positive integers and no convergence conclusion
for their trajectories.

## Finite replay

The accompanying standard-library checker computes complete ternary prefix
rows by summing the geometric exponent progression exactly through depth
four. A local run of `python -B check_rational_envelope.py` passed 1,009
finite binary-expansion comparisons, 1,629 truncated signed inverse words,
positive and negative rational cycle examples, and all 4,096 length-12
formal images from `1/8` (3,793 distinct endpoint values). It checks the
finite formulas and conventions. The classification, uniform-in-depth
bound and positive-interval counting conclusion use the proofs above.
