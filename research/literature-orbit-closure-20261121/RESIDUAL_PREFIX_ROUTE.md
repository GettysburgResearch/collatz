# Expanding prefixes followed by variable-clock physical mergers

## What is proved

**The strongest coverage theorem is now `AL27HalfSelector.lean`: a complete,
explicit family of relative natural density 1/2 inside the entire branch
`27 mod 128`, with a physical partner satisfying**

\[
16x+3=9n,\qquad T^{k+5}x=T^{k+9}n.
\]

**For every member, the original source never drops below its starting value
through the displayed source merger clock.** The half selector uses the
three-step prefix, followed by an arbitrary odd run and the short two-clock
diamond. Its proof and exact density calculation are given in Section 0.

The narrower selector in Section 3 also now has the stronger partner

\[
64x_{\rm small}+51=9n,\qquad
T^{k+9}x_{\rm small}=T^{k+15}n.
\]

That narrower family is already contained in the broad half; its 1/128
relative density inside `34587 mod 73728` must not be added again. Its role
is a stronger partner bound. For k≥8, its source also never descends through
its longer merger clock k+15.


`ResidualPrefixErasure.lean` proves a reusable transfer theorem: an actual
expanding Collatz prefix can be followed by an arbitrarily long initial odd
run and an endpoint diamond, while the resulting partner is still smaller
than the *original* source. `ResidualPhaseSelector.lean` discharges the
endpoint selector on infinitely many complete arithmetic progressions inside
one of the earlier 130 unresolved AL27 cells.

The original prefix-seven construction has the non-dyadic affine relation

\[
1024x=729n+29,
\]

and the actual merger is

\[
T^{k+5}x=T^{k+15}n.
\]

Here every integer \(k\ge6\) is allowed. Every selected source belongs to
\(n\equiv34587\pmod{73728}\), and no selected source descends through time
\(k+7\), hence none descends in the earlier search budget of 13 steps.

This narrow selector is a partial family, not the whole residue class. Its
exact natural density *within that one class* is \(1/128\). It is contained
in the broad half selector and does not supply additional disjoint coverage.
No unconditional convergence theorem for all positive integers is asserted.

All uses of \(T\) mean the ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

## 0. The broad half selector

For every integer k≥0 define

\[
a_k=(28\,2^{5k+1}+9\,3^k)\bmod36,
\qquad w=a_k+36t\quad(t\ge0).
\]

Here 28 and 9 are CRT idempotents modulo 9 and 4. Since
\(2^6\equiv1\pmod9\), they give

\[
2^kw\equiv2\pmod9,\qquad
3^{k+3}w\equiv3\pmod4.
\]

Set \(z=\lfloor2^kw/9\rfloor\), \(n=128z+27\), and
\(x=2^{k+3}w-1\). Then \(9z+2=2^kw\), and the actual three-step prefix is

\[
T^3n=144z+31=2^{k+4}w-1.
\]

Apply the short endpoint diamond after that odd run, deleting one initial
odd step. This gives

\[
16x+3=9n,\qquad0<x<n,\qquad T^{k+5}x=T^{k+9}n.
\]

The whole original source path through clock k+9 stays at least n. Its first
three steps increase the source, the next k+4 steps are an odd run, and the
last two steps are halvings. If S is the end of the odd run, then

\[
S=3^{k+4}w-1,\quad9n=128\,2^kw-13,
\]

so

\[
9(S-4n)=(729\,3^k-512\,2^k)w+43>0.
\]

Thus even the two final halvings do not descend below n. This no-descent
statement is kernel-checked for every k,t, not just for finite examples.
For instance, the previously uncovered base 34587 has k=7,w=19 and partner
19455, with

\[
T^{12}(19455)=T^{16}(34587)=841448.
\]

For each k, Lean proves the full progression formula and canonical base:

\[
n(k,t)=n(k,0)+2^{k+9}t,\qquad0<n(k,0)<2^{k+9}.
\]

The core w is odd, so k is exactly \(\nu_2(9z+2)\). The progressions are
therefore disjoint. Their relative density inside `27 mod 128` is

\[
\sum_{k\ge0}\frac{128}{2^{k+9}}=
\sum_{k\ge0}2^{-k-2}=\frac12.
\]

For the countable union, the tail k≥K lies in the single condition
\(2^K\mid9z+2\), of relative density \(2^{-K}\). This proves that the
natural density equals the geometric sum. The arithmetic progression and
parity statements are checked in Lean; this elementary natural-density
argument is written mathematics rather than a Lean density theorem.

This half overlaps substantially with the earlier 446/576 certificate
cover. It is not a disjoint extra half and does not settle the branch.

## 1. The general transfer theorem

Write the source as \(n=2^h z+b\), let \(p\) be the number of odd steps in the
first \(h\) steps from \(b\), and put \(c=T^h b\). The existing exact prefix
identity is

\[
T^h n=3^p z+c.
\]

Suppose this endpoint has the form \(y=2^k u-1\), and an actual synchronous
endpoint diamond permits erasing \(r\) initial odd steps:

\[
T^H(3^{k-r}u-1)=T^H(3^ku-1).
\]

Then the ordinary source

\[
x=2^{k-r}u-1
\]

has the common future

\[
T^{k-r+H}x=T^{h+k+H}n.
\]

The exact comparison with the original source is

\[
x<n\quad\Longleftrightarrow\quad
3^p z+c+1<2^r(2^h z+b+1).
\]

Two useful sufficient conditions are now proved in Lean:

- **Entire progression:** \(3^p\le2^{h+r}\) and
  \(c+1<2^r(b+1)\).
- **Explicit eventual range:** \(3^p<2^{h+r}\) and \(z\ge c+2\).

The second condition uses the integer gap of at least one between the two
leading coefficients. It supplies a finite, deliberately conservative cutoff.
The endpoint diamond remains an explicit hypothesis in these generic
lemmas; the next construction discharges it.

## 2. The prefix and endpoint diamond

For the difficult binary cylinder \(n=128z+27\), the initial states are

\[
\begin{aligned}
128z+27&\to192z+41\to288z+62\to144z+31\\
&\to216z+47\to324z+71\to486z+107\to729z+161.
\end{aligned}
\]

Consequently \(h=7,p=6,c=161\). Erasing three odd steps overcomes this
expansion because

\[
729<2^{10}=1024,\qquad162<8\cdot28=224.
\]

The earlier short–long–short diamond proves, whenever \(v\equiv147\pmod{256}\),

\[
T^8(v-1)=T^8(27v-1).
\]

Set \(v=3^{k-3}u\). If

\[
729z+162=2^ku,\qquad 3^{k-3}u\equiv147\pmod{256},
\]

then the prefix and the diamond combine into the stated merger. Straight
arithmetic gives

\[
128\cdot8x=729n+29.
\]

Starting the odd run at time three gives the stronger partner. Indeed

\[
T^3n=144z+31=2^{k+4}w-1.
\]

The same eight-clock diamond now removes three steps from this longer run,
giving \(x_{\rm small}=2^{k+1}w-1\). Consequently

\[
64x_{\rm small}+51=9n,\qquad
T^{k+9}x_{\rm small}=T^{k+15}n.
\]

This is not multiplication inside an unrestricted semigroup: both sides of
the merger are literal ordinary Collatz trajectories, formalized using the
repository's existing `CollatzShell.step` and `orbit` definitions.

## 3. An explicit selector for every run length

The following constants are Chinese-remainder idempotents:

\[
6400\equiv(1,0)\pmod{(81,256)},\qquad
14337\equiv(0,1)\pmod{(81,256)}.
\]

Also \(2^{54}\equiv1\pmod{81}\) and \(3^{64}\equiv1\pmod{256}\).
For every \(k\ge6\), define the least nonnegative residue

\[
w_k=\left(6400\,2^{53k+1}+14337\cdot147\,3^{63(k+1)}\right)\bmod20736.
\]

For an arbitrary integer \(t\ge0\), set

\[
\begin{aligned}
w&=w_k+20736t,&u&=81w,\\
z&=9\left\lfloor\frac{2^kw}{81}\right\rfloor,&
n&=128z+27,&x&=2^{k-3}u-1.
\end{aligned}
\]

The selector is positive and odd. It satisfies

\[
2^kw\equiv2\pmod{81},\qquad3^{k+1}w\equiv147\pmod{256}.
\]

The first congruence gives \(2^kw=81q+2\), so
\(729z+162=2^ku\). The second gives the required diamond phase because
\(3^{k-3}u=3^{k+1}w\).

Every source is divisible by 9. Also

\[
729n=2^{k+7}u-1053,
\]

so \(k\ge6\) implies \(n\equiv1819\pmod{8192}\). These two congruences are
exactly \(n\equiv34587\pmod{73728}\).

Some first representatives are:

| k | w_k | n(k,0) | x(k,0) | Source clock | Partner clock |
|---:|---:|---:|---:|---:|---:|
| 6 | 281 | 255771 | 182087 | 21 | 11 |
| 7 | 12979 | 23627547 | 16820783 | 22 | 12 |
| 8 | 14225 | 51791643 | 36871199 | 23 | 13 |
| 9 | 2779 | 20236059 | 14406335 | 24 | 14 |
| 10 | 17225 | 250857243 | 178588799 | 25 | 15 |

The seven fixed prefix states all exceed the original source, and the next
\(k\) states belong to an initial odd run and increase. This proves the
no-descent statement through \(k+7\); it is not an assertion about the entire
binary-logarithmic horizon for arbitrary \(t\).

There is a stronger checked statement for k≥8: no descent occurs through
clock k+15, including the common endpoint. Write W=3^ku. The phase gives
W≡129 mod256, so W−1=256a+128 and the next eight states have minimum
2a+1=(W−1)/128. The coefficient inequality

\[
729\,3^k\ge16384\,2^k\qquad(k\ge8)
\]

implies W−1≥128n. This validates the longer no-descent horizon. For k=8,t=0,
the stronger partner is 7283199, and

\[
T^{17}(7283199)=T^{23}(51791643)=88590800.
\]

Since the sources are divisible by 3, they have no smaller direct ordinary
ancestor: the only predecessor of a target divisible by 3 is its double,
and iterating backwards gives only powers-of-two multiples until one stops.
The new smaller source merges at the later displayed endpoint.

## 4. Exact coverage

For each fixed \(k\ge6\), the Lean theorem `source_progression` proves

\[
n(k,t)=n(k,0)+M_k t,\qquad
M_k=9\,2^{k+15}=73728\,2^{k+2}.
\]

`source_base_bounds` proves \(0<n(k,0)<M_k\). Thus this is one complete
positive residue progression, not a tail with unhandled small exceptions.
Moreover

\[
\nu_2(T^7n(k,t)+1)=k,
\]

because \(T^7n+1=2^ku\) and \(u\) is odd. Different values of \(k\) therefore
produce disjoint progressions. Relative to the ambient class modulo 73728,
the progression for \(k\) has density \(2^{-(k+2)}\), giving

\[
\sum_{k=6}^{\infty}2^{-(k+2)}=\frac1{128}.
\]

The countable sum is legitimate for natural density: for any \(K\ge6\), all
progressions with \(k\ge K\) lie in the single binary divisibility condition
\(2^K\mid T^7n+1\). Within the ambient progression, this condition has
relative density \(2^{-(K-6)}\), tending to zero. Finite partial sums give the
lower bound and this vanishing tail gives the matching upper bound.

The progression formula, positive canonical representative, and parity facts
are kernel-checked. The density argument in this section is an ordinary
mathematical deduction; no Lean measure-theoretic density theorem is claimed.

## 5. Why another finite eight-clock phase list does not close this branch

A complete finite word computation for odd residues \(1\le v<256\) gives:

| Erased steps r | Phases with T^8(v−1)=T^8(3^r v−1) and matching affine slopes |
|---:|:---|
| 1 | all 64 phases v≡3 mod4, together with v=185 |
| 2 | v=147,185 |
| 3 | v=147 |
| 4,5,6,7,8 | none |

`residual_phase_analysis.py` reproduces this finite classification using
literal forward paths and odd counts. It is a Python computation, not a
new Lean completeness theorem. The eight-clock identity for r=3 is already
Lean-proved in the imported diamond module. Erasing only one or two steps
cannot make this prefix's partner smaller, so the r=3 phase is the entire
useful eight-clock catalogue in this particular architecture.

There is also a structural obstruction, limited to the **seven-step prefix**,
to *any finite bounded-clock catalogue*
of synchronous pure dyadic erasures for this prefix. Let
\(W=3^ku\), the full odd-run endpoint plus one, and let H bound every
catalogued endpoint clock. Choose \(W\equiv1\pmod{2^H}\). CRT allows
arbitrarily large such sources inside the ambient class. The right-hand
endpoint \(W-1\) then takes only even steps at every catalogued clock.

If a binary/ternary cylinder identity erased \(r\ge2\) steps, its other
endpoint would start at \(v-1\), where \(v=W/3^r\) is odd. Let p be that word's
odd count. Comparing the two affine slopes on the infinite cylinder forces
p=r. If the odd steps have positions \(i_1<\cdots<i_r\), numbered from zero,
the first even step forces \(i_j\ge j\). The affine carry therefore obeys

\[
B=\sum_{j=1}^r3^{r-j}2^{i_j}
\ge2(3^r-2^r)>3^r-1\qquad(r\ge2).
\]

But equality with the all-even endpoint requires

\[
3^r(v-1)+B=3^rv-1,
\]

hence B=3^r−1, a contradiction. The positive construction above uses an
unbounded **source** clock but keeps endpoint clock eight; this argument
explains why that particular selector cannot be upgraded to a finite full
phase cover. A complete argument would need additional structure, such as
unbounded endpoint clocks or genuinely different affine partner rules. Those
possibilities are not ruled out here. In particular this is **not** an
obstruction to the improved three-step prefix: its single-step erasure has
r=1, exactly the case in which the carry inequality allows equality. The
broad half selector in Section 0 exploits this distinction.

## Lean validation and scope

All three new modules compile with Lean 4.34.1, one worker, and
`-DwarningAsError=true`, against the pinned repository dependencies and
Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
The 29 printed public theorem audits use only `propext`, `Classical.choice`,
and `Quot.sound`. There is no `sorry`, `native_decide`, or custom axiom.

`basin_by_smaller_induction` states the correct induction use: if every
smaller positive source is in the basin, the selected source is too. It does
not assume that the new partner belongs to this selected family, and does
not turn partial residue coverage into universal convergence.

The superseded `ResidualAL27Family.lean` only treated k=8 mod1728. Its
periodic subfamily is unnecessary once the stronger all-k selector is used.
