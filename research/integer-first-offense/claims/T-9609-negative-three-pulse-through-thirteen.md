# T-9609 — All fixed-weight negative-three pulse grammars through thirteen unpulsed letters are cycle-free

**Claim ID:** `T-9609`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pro-04`  
**Issue:** #46  
**Date:** 2026-07-26  
**Dependencies:** `T-9608`, `L-9610`  
**Scope:** aligned fixed-weight grammars in the exact negative-three pulse chart  
**Related counterexample candidates:** none

## 1. Statement

For every

\[
0\le a\le13,
\qquad
b\ge1,
\]

consider the complete alphabet of all chronological macro words containing
exactly `a` copies of

\[
A:\quad 8y'=9y+3
\]

and exactly `b` copies of

\[
B:\quad 16y'=9y,
\]

where `y=h-3` and the physical shortcut-Collatz state is

\[
n=-5+2h.
\]

Then no finite word over that complete macro alphabet has a nontrivial positive
integral cycle.

Equivalently:

\[
\boxed{
\begin{array}{c}
0\le a\le13,\ b\ge1,\\
\text{arbitrary macro choice and arbitrary repetition length}
\end{array}
\Longrightarrow
\text{only the trivial physical cycle }n=1.}
\tag{1}
\]

The result is simultaneous in pulse count, macro length, branch count, and
macro repetition length.

## 2. Retained range `0<=a<=5`

`T-9608` already proves `(1)` for every `0<=a<=5` and every `b>=1`.
We therefore assume

\[
6\le a\le13.
\tag{2}
\]

For one fixed-weight macro put

\[
Q=8^a16^b,
\qquad
P=9^{a+b},
\qquad
D=Q-P,
\tag{3}
\]

and use the centered constant interval

\[
E_{\min}=3\,9^b(9^a-8^a),
\qquad
E_{\max}=3\,16^b(9^a-8^a).
\tag{4}
\]

All centered constants are strictly positive.

## 3. Supercritical packets

If `P>Q`, then for a proposed nonnegative macro cycle of length `R`,

\[
(Q^R-P^R)y_0
=
\sum_{t=0}^{R-1}P^{R-1-t}Q^tE_{i_t}>0.
\tag{5}
\]

The left side is nonpositive. Hence no positive cycle exists.

For the range `(2)`, the supercritical packets are exactly:

```text
a=6,7,8,9:      b=1;
a=10,11,12,13:  b=1,2.
```

There is no equality case because a positive power of two cannot equal a
positive power of three.

## 4. The uniform terminal-residue region

Assume `P<Q`. By `L-9610`, the gate

\[
E_{\max}<24D
\tag{6}
\]

excludes every positive cycle. Using `(3)` and `(4)`, `(6)` is equivalent to

\[
9^a(16^b+8\,9^b)<9\,8^a16^b.
\tag{7}
\]

For fixed `a`, the ratio

\[
{E_{\max}\over D}
=
{3(9^a-8^a)
 \over
 8^a-9^a(9/16)^b}
\tag{8}
\]

strictly decreases with `b` throughout the contracting range. It therefore
suffices to check the first listed `b` in each row:

| `a` | first `b` covered by `(6)` | left side of `(7)` | right side of `(7)` | margin |
|---:|---:|---:|---:|---:|
| 6 | 2 | 480,422,664 | 603,979,776 | 123,557,112 |
| 7 | 2 | 4,323,803,976 | 4,831,838,208 | 508,034,232 |
| 8 | 3 | 427,367,846,088 | 618,475,290,624 | 191,107,444,536 |
| 9 | 3 | 3,846,310,614,792 | 4,947,802,324,992 | 1,101,491,710,200 |
| 10 | 3 | 34,616,795,533,128 | 39,582,418,599,936 | 4,965,623,066,808 |
| 11 | 3 | 311,551,159,798,152 | 316,659,348,799,488 | 5,108,189,001,336 |
| 12 | 4 | 33,333,463,613,633,544 | 40,532,396,646,334,464 | 7,198,933,032,700,920 |
| 13 | 4 | 300,001,172,522,701,896 | 324,259,173,170,675,712 | 24,258,000,647,973,816 |

Thus every contracting packet in `(2)` is closed except

\[
(8,2),
\qquad
(9,2),
\qquad
(12,3),
\qquad
(13,3).
\tag{9}
\]

The rest of the proof eliminates these four complete alphabets exactly.

## 5. A word-independent phase modulo seven

The uncentered letters satisfy

```text
A: h' == 2h mod 7;
B: h' == h  mod 7.
```

Hence every fixed-weight macro obeys

\[
h'\equiv2^a h\pmod7.
\]

After `h=y+3` and multiplication by `Q`, this gives the exact constant phase

\[
\boxed{
E_w\equiv3\,2^b(2^a-1)\pmod7,}
\tag{10}
\]

independently of the chronological word.

We combine this with the cycle-minimum form from `L-9610`:

\[
E_w=3rD+Pk,
\qquad
r\equiv0\text{ or }8\pmod9.
\tag{11}
\]

## 6. Exceptional packet `(a,b)=(8,2)`

Here

\[
Q=4,294,967,296,
\quad
P=3,486,784,401,
\quad
D=808,182,895,
\quad
E_{\max}=20,174,979,840.
\tag{12}
\]

The exact inequalities

\[
E_{\max}<27D,
\qquad
E_{\max}<24D+P
\tag{13}
\]

force, via `(11)`,

\[
r=8,
\qquad
k=0.
\]

Thus the only possible first-edge target is `24D`.

Equation `(10)` gives

\[
E_w\equiv1\pmod7.
\]

But `D≡2 mod7`, so

\[
24D\equiv6\pmod7.
\]

The target is disjoint from the complete block alphabet.

## 7. Exceptional packet `(a,b)=(9,2)`

Here

\[
Q=34,359,738,368,
\quad
P=31,381,059,609,
\quad
D=2,978,678,759,
\quad
E_{\max}=194,459,720,448.
\tag{14}
\]

Since `E_max<66D`, `(11)` leaves only

\[
r\in\{8,9,17,18\}.
\tag{15}
\]

The exact height inequality `3rD+Pk<=E_max` gives

| `r` | maximum `k` |
|---:|---:|
| 8 | 3 |
| 9 | 3 |
| 17 | 1 |
| 18 | 1 |

Because `a` is divisible by three, `(10)` gives `E_w≡0 mod7`; also
`D≡0 mod7` and `P≡4 mod7`. Therefore `(11)` forces

\[
k\equiv0\pmod7.
\]

The displayed bounds imply `k=0`.

Modulo `8`, every block constant is

\[
E_w\equiv0\text{ or }3\pmod8,
\tag{16}
\]

according as the first physical letter is `B` or `A`. Since `D≡7 mod8`, the
remaining targets are

\[
3rD\equiv5r\pmod8.
\]

This excludes `r=9,17,18`; only `r=8` remains.

For `r=8`, the target is `24D`, and

\[
24D\equiv8\pmod{16}.
\tag{17}
\]

The first two physical letters give the complete alphabet residue set

\[
E_w\pmod{16}\in\{0,3,11\}:
\tag{18}
\]

```text
starts with B   -> 0;
starts with AB  -> 3;
starts with AA  -> 11.
```

Thus `(17)` is impossible.

## 8. Exceptional packet `(a,b)=(12,3)`

Here

\[
Q=281,474,976,710,656,
\quad
P=205,891,132,094,649,
\quad
D=75,583,844,616,007,
\]

\[
E_{\max}=2,626,069,214,146,560.
\tag{19}
\]

Since `E_max<36D`, the terminal residue leaves `r=8` or `9`. The exact `k`
bounds are respectively `3` and `2`.

Now `a` is divisible by three, so `(10)` gives `E_w≡0 mod7`; moreover
`D≡0` and `P≡1 mod7`. Hence `k≡0 mod7`, and the height bounds force `k=0`.

The same modulo-`8` argument as in Section 7 excludes `r=9`. For `r=8`,

\[
24D\equiv8\pmod{16},
\]

while the odd macro length again gives the exact alphabet set `(18)`. Hence
this packet is cycle-free.

## 9. Exceptional packet `(a,b)=(13,3)`

Here

\[
Q=2,251,799,813,685,248,
\quad
P=1,853,020,188,851,841,
\quad
D=398,779,624,833,407,
\]

\[
E_{\max}=24,479,047,857,451,008.
\tag{20}
\]

Since `E_max<63D`, `(11)` leaves

\[
r\in\{8,9,17,18\}.
\]

The exact height bounds are

| `r` | maximum `k` |
|---:|---:|
| 8 | 8 |
| 9 | 7 |
| 17 | 2 |
| 18 | 1 |

Equation `(10)` gives `E_w≡3 mod7`. Reducing `(11)` modulo seven yields

\[
k\equiv5(r+1)\pmod7.
\tag{21}
\]

Together with the table, only

\[
(r,k)=(8,3),
\qquad
(r,k)=(9,1)
\tag{22}
\]

remain.

The second pair has target residue

\[
3rD+Pk\equiv6\pmod8,
\]

contradicting `(16)`.

For `(r,k)=(8,3)`, the target is

\[
24D+3P\equiv107\pmod{128}.
\tag{23}
\]

Only the first three physical letters can contribute modulo `128`. They give
the complete table

| first three letters | `E_w mod 128` |
|:---|---:|
| `BBB`, `BBA` | 0 |
| `BAA`, `BAB` | 48 |
| `ABA`, `ABB` | 43 |
| `AAB` | 67 |
| `AAA` | 3 |

Thus

\[
E_w\pmod{128}\in\{0,3,43,48,67\},
\]

which excludes `(23)`.

## 10. Conclusion

Sections 3--9 prove `(1)` for `6<=a<=13`; `T-9608` supplies the earlier
range. Therefore every fixed-weight negative-three pulse grammar with at most
thirteen `A` letters is cycle-free at every repetition length.

This closes the first eight previously uncovered `A`-layers in one theorem and
raises the first open aligned fixed-weight cycle packet to

\[
\boxed{a\ge14.}
\tag{24}
\]

## 11. Why this is not a bounded census

The theorem is unbounded simultaneously in

```text
b;
macro length a+b;
number of macro branches binomial(a+b,b);
macro repetition length;
chronological switching among branches;
total non-2 support aR across R macros.
```

Only four finite alphabets are enumerated, after the general terminal-residue
theorem removes every other packet in the declared infinite range.

## 12. Gap audit

- The first open aligned fixed-weight layer is `a=14`; unrestricted Collatz words remain much broader.
- The theorem excludes cycles, not the six-branch aperiodic ordinary-root problem.
- Scale-varying summaries and nonaligned internal repairs remain outside scope.
- The exact physical chart is inherited from the independently reconstructed source branches; no source status is promoted here.
- All theorem-level statements remain `PROPOSED` pending independent reconstruction.
