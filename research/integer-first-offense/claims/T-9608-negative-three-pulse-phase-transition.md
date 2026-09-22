# T-9608 — All fixed-weight negative-three pulse grammars with at most five unpulsed letters are cycle-free

**Claim ID:** `T-9608`
**Status:** `PROPOSED`
**Agent:** `gpt56-pro-04`
**Issue:** #46
**Date:** 2026-07-26
**Dependencies:** `L-9608`, `L-9609`; the two exact physical letters independently derived in PR #45 `L-8405` / PR #51 `O-8001`
**Scope:** aligned fixed-weight grammars in the negative-three pulse chart
**Related counterexample candidates:** none

## 1. Exact physical alphabet

Use the ordinary coordinate

\[
n=-5+2h.
\]

The two exact two-odd-step shortcut-Collatz blocks are

\[
A:\quad 8h'=9h,
\tag{1}
\]

and

\[
B:\quad 16h'=9h+21.
\tag{2}
\]

Center at the trivial fixed point `h=3`:

\[
y=h-3.
\]

Then

\[
A:\quad 8y'=9y+3,
\qquad
B:\quad 16y'=9y.
\tag{3}
\]

Let one macro word contain exactly

\[
a=\#A,
\qquad
b=\#B,
\qquad
L=a+b.
\]

Every such word has common summary

\[
Q=8^a16^b,
\qquad
P=9^{a+b},
\tag{4}
\]

and an exact centered constant `E_w`:

\[
QF_w(y)=Py+E_w.
\tag{5}
\]

## 2. Exact centered constant interval

The uncentered constant from PR #45 `L-8405` is

\[
C_w=
21\sum_{j:w_j=B}
9^{L-1-j}2^{3j+B_j},
\tag{6}
\]

where `B_j` counts prior `B` letters. Since

\[
E_w=C_w-3(Q-P),
\tag{7}
\]

moving pulses monotonically through the word gives

\[
\boxed{
E_{\min}=3\,9^b(9^a-8^a),}
\tag{8}
\]

attained by `A^aB^b`, and

\[
\boxed{
E_{\max}=3\,16^b(9^a-8^a),}
\tag{9}
\]

attained by `B^bA^a`.

For completeness, the centered constants of the two adjacent two-letter words are `27` for `AB` and `48` for `BA`. In an arbitrary fixed context, replacing `AB` by `BA` therefore raises the total constant by `21` times a positive power of `2` and a positive power of `9`. Repeated adjacent swaps put every `B` on the right for the minimum and on the left for the maximum. Equivalently, `A^a` has centered constant `3(9^a-8^a)`; composing it before or after `B^b` gives `(8)` and `(9)`.

Equivalently, if the `A` letters occur at positions `q`, and `A_q,B_q` count the prior letters of each type, the centered recursion `(3)` gives the direct toll formula

\[
\boxed{
E_w=3\sum_{q:w_q=A}9^{L-1-q}2^{3A_q+4B_q}.}
\tag{10}
\]

Every centered constant is therefore divisible by `3`. When `P<Q`, `L-9609` applies with

\[
g=3,
\qquad
D=Q-P.
\]

Its direct height condition is

\[
E_{\max}<3D.
\tag{11}
\]

After cancellation, `(11)` is exactly

\[
\boxed{
9^a(16^b+9^b)<2\,8^a16^b.}
\tag{12}
\]

## 3. Uniform region

If `a=0`, the alphabet consists only of `B^b`, whose centered map is

\[
16^b y'=9^b y.
\]

Its only nonnegative integral cycle is `y=0`, corresponding to `h=3` and the trivial physical state `n=1`. Hence assume `a>=1`.

All parameter ranges listed below are contracting: `P<Q`. The left-to-right ratio in `(12)` decreases with `b`. The following four exact boundary checks hold:

\[
9^2(16+9)=2025<2048=2\,8^2 16,
\tag{13}
\]

\[
9^3(16^2+9^2)=245673<262144=2\,8^3 16^2,
\tag{14}
\]

\[
9^4(16^3+9^3)=31656825<33554432=2\,8^4 16^3,
\tag{15}
\]

and

\[
9^5(16^4+9^4)=4257255753<4294967296=2\,8^5 16^4.
\tag{16}
\]

Consequently `L-9609` excludes every positive cycle in the complete fixed-weight macro alphabet throughout

\[
\boxed{
\begin{array}{ll}
1\le a\le2,&b\ge1,\\
a=3,&b\ge2,\\
a=4,&b\ge3,\\
a=5,&b\ge4.
\end{array}}
\tag{17}
\]

This already covers arbitrary macro choices and arbitrary repetition length; no macro word is prescribed.

## 4. The one-pulse narrow exceptions

For `b=1`, the macro constants are

\[
C_j=21\,9^{a-j}8^j,
\qquad 0\le j\le a.
\tag{18}
\]

For `a=3,4`, the common multiplier is contracting and the complete alphabet width is below `Q`:

\[
{W\over Q}
={21\over16}
\left(\left({9\over8}\right)^a-1\right)<1.
\tag{19}
\]

Thus `L-9608` collapses every arbitrary macro grammar to a primitive one-block fixed point.

For `a=3`,

\[
D=16\,8^3-9^4=1631=7\cdot233.
\]

For `a=4`,

\[
D=16\,8^4-9^5=6487=13\cdot499.
\]

Every constant in `(18)` has prime support contained in `{2,3,7}`. Since `D\mid E_j` is equivalent to `D\mid C_j` by `(7)`, no primitive centered constant is divisible by the complete denominator in either case. Hence

\[
\boxed{(a,b)=(3,1),(4,1)\text{ are cycle-free at all repetitions}.}
\tag{20}
\]

## 5. Exact exceptional target `(a,b)=(4,2)`

Here

\[
Q=1048576,
\qquad
P=531441,
\qquad
D=517135,
\]

and

\[
598995\le E_w\le1893120.
\tag{21}
\]

Every target from `L-9609` has `m+k` divisible by `3`. Since `6D>E_max`, only `m+k=3` is possible. Of its three candidates,

\[
D+2Q>E_{\max},
\qquad
2D+Q>E_{\max},
\]

so the sole surviving target is

\[
3D=1551405.
\tag{22}
\]

But every uncentered `C_w` is divisible by `21`, while modulo `7`

\[
Q\equiv4,
\qquad
P\equiv1,
\qquad
D\equiv3.
\]

Therefore

\[
E_w=C_w-3D\equiv5\pmod7,
\]

whereas

\[
3D\equiv2\pmod7.
\]

The exact target set is disjoint from the alphabet, so `(4,2)` is cycle-free.

## 6. The first supercritical packet `(a,b)=(5,1)`

At

\[
(a,b)=(5,1),
\]

one has

\[
Q=16\,8^5=524288,
\qquad
P=9^6=531441,
\qquad
P-Q=7153>0.
\tag{23}
\]

All centered constants are positive. Around any proposed positive macro cycle of length `R`, iteration would give

\[
(Q^R-P^R)y
=
\sum_{t=0}^{R-1}P^{R-1-t}Q^tE_{i_t}>0.
\]

The left side is negative. Hence no positive cycle exists.

This is precisely the existing six-branch divergent-orbit chart: positive cycles are impossible by supercriticality, while one all-time ordinary root would be unbounded.

## 7. Exact exceptional target `(a,b)=(5,2)`

Here

\[
Q=8388608,
\qquad
P=4782969,
\qquad
D=3605639,
\]

and

\[
6386283\le E_w\le20183808.
\tag{24}
\]

Again `6D>E_max`, so `m+k=3`. The target `D+2Q` exceeds `E_max`; the only possible targets are

\[
2D+Q=15599886,
\qquad
3D=10816917.
\tag{25}
\]

Reduce the centered constants modulo `9`. In the direct `A`-toll formula, every term vanishes modulo `9` except possibly a final `A`. Thus

\[
E_w\equiv0\text{ or }3\pmod9.
\tag{26}
\]

On the other hand, `P` is divisible by `9` and

\[
Q\equiv D\equiv5\pmod9,
\]

so both targets in `(25)` are congruent to `6 modulo 9`. No target occurs.

## 8. Exact exceptional target `(a,b)=(5,3)`

Now

\[
Q=134217728,
\qquad
P=43046721,
\qquad
D=91171007,
\]

and

\[
57476547\le E_w\le322940928.
\tag{27}
\]

As before, `6D>E_max`, `D+2Q>E_max`, and the only possible targets are

\[
2D+Q=316559742,
\qquad
3D=273513021.
\tag{28}
\]

Modulo `8`, the direct centered formula has only one possible nonzero term: the first letter contributes `3` exactly when it is `A`; every later toll is divisible by `8`. Hence

\[
E_w\equiv0\text{ or }3\pmod8.
\tag{29}
\]

But `Q≡0`, `P≡1`, and `D≡7 modulo 8`, so the two targets in `(28)` are congruent to `6` and `5`. Again the target set is disjoint from the alphabet.

## 9. Main theorem

Combining the uniform region and the exact exceptions gives:

\[
\boxed{
\begin{array}{c}
\text{For every }b\ge1\text{ and every }0\le a\le5,\\
\text{no finite word over the complete fixed-weight }(a,b)\text{ macro alphabet}\\
\text{has a nontrivial positive integral cycle.}
\end{array}}
\tag{30}
\]

The only integral fixed point in the whole family is

\[
a=0,
\qquad y=0,
\qquad h=3,
\qquad n=1,
\]

the trivial Collatz cycle.

The theorem is unbounded simultaneously in:

- pulse count `b`;
- physical macro length `a+b`;
- number of available macro branches `binomial(a+b,b)`;
- grammar repetition length;
- chronological switching among the macro branches.

No bounded word search or finite-prefix extrapolation is used.

## 10. Exact cycle/divergence phase transition

Within the one-pulse family `b=1`:

```text
packet lengths 1--5:
    P<Q;
    all arbitrary aligned cycle grammars close negatively;

packet length 6, with (a,b)=(5,1):
    P>Q;
    positive cycles are impossible by supercriticality;
    one forever-defined ordinary root would instead be divergent;
    ordinary extraction is the sole remaining issue.
```

Thus the six-branch least-root system is not an arbitrary laboratory. It is the first supercritical one-pulse packet immediately beyond a complete all-repetition cycle-free regime, and all of its contracting fixed-weight siblings with `a<=5` are now excluded.

## 11. Why this is genuine progress

The result eliminates an exhaustive infinite class of exact physical Collatz grammars. It is strictly weaker than Collatz because words with six or more `A` letters, changing block summaries, nonaligned repairs, and unrestricted Collatz valuations remain outside scope.

It also closes an unbounded centered-support family: concatenating `R` macros gives `aR` non-`2` valuations, so the theorem is not a fixed-support census.

## 12. Gap audit

- The theorem does not decide the six-branch least-root sequence.
- It does not cover fixed-weight packets with `a>=6`.
- It does not cover scale-varying summaries or nonaligned internal repairs.
- It excludes cycles; a supercritical aperiodic all-time path is a separate ordinary-extraction problem.
- The physical interpretation uses the exact `n=-5+2h` replay already derived in the cited source branches; no source status is promoted here.

## 13. Adversarial checks

1. Formulas `(8)` and `(9)` agree with the existing fixed-weight numerator formula after centering at `h=3`.
2. The target congruence is `m+k≡0 mod3`, not merely `m≡0 mod3`.
3. Every exceptional target list is obtained from the exact inequality `Dm+Qk<=E_max`; a target hit would still be only necessary.
4. The residue arguments classify the whole block alphabet, not a sampled list.
5. A coarse affine exclusion is stronger than needed for a physical negative theorem: intermediate-domain constraints can only remove more candidates.
