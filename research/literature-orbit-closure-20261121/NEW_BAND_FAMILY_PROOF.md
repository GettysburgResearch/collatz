# A quarter-source merger inside a non-descending binary horizon

Map: the shortcut Collatz map `T(n)=n/2` for even `n` and `(3n+1)/2`
for odd `n`. Status: exact ordinary identities and a complete written proof;
Lean verification is recorded separately by the accompanying compiler logs.
These results do not establish the universal partner cover or Collatz.

For every integer `j>=0`, put

\[
k=64j+31,\qquad s=2j+8,\qquad d=k+s=66j+39,
\]

\[
n_j=2^d+2^k-1,
\qquad
x_j=2^{k-2}(2^s+1)-1=\frac{n_j-3}{4}.
\]

We prove all three assertions simultaneously:

1. Both `n_j` and its smaller partner `x_j` belong to the repository's
   forced marked band.
2. `T^t(n_j)>=n_j` for every `0<=t<=floor(log_2 n_j)=d`.
3. Despite that failure of forward descent, `0<x_j<n_j` and
   \[
   T^{k+6}(x_j)=T^{k+8}(n_j),\qquad k+8\le d.
   \]

Thus the orbit of `n_j` shares an actual future with a source nearly four
times smaller, and the meeting point on the original arm occurs by the end of
its native binary horizon. Both dyadic exponents `k,d` are odd.
This extends beyond the even-run and immediate smaller-predecessor cases
used for the earlier two-power horizon family.

## 1. The source-deletion mechanism

For any positive integer `u` and `b>=0`, the first `b` steps from
`2^b*u-1` are odd steps, giving

\[
T^b(2^b u-1)=3^b u-1.
\]

Suppose two endpoint expressions `v-1` and `3^r v-1` coalesce after the
same number `h` of steps. If `v=3^{k-r}u`, the sources

\[
n=2^k u-1,\qquad x=2^{k-r}u-1
\]

then satisfy

\[
T^{k-r+h}(x)=T^{k+h}(n),\qquad 2^r(x+1)=n+1.
\]

This uses exactly the fixed source `n`; no multiplier is chosen after
changing the source, and no generic 2-adic realizer is substituted for an
ordinary integer. If `r>0` and `k>r`, the new source is positive and smaller.

There is a useful extra property: this source deletion preserves the
marked band. More generally, let `x>0` be odd and
`n=2^r(x+1)-1` be marked. Writing `e=floor(log_2 x)`, one has

\[
\lfloor\log_2 n\rfloor=e+r,\qquad
n-2^{e+r}=2^r(x-2^e)+(2^r-1).
\]

The source band inequality, after discarding the nonnegative second term,
implies

\[
(e+r+1)2^r(x-2^e)\le70\,2^r2^e.
\]

Cancel `2^r` and decrease the coefficient to `e+1`. This is precisely the
band inequality for `x`. Thus every admissible dyadic erasure gives a
**smaller marked** common-future partner directly. The generic height
condition used to force a later marked visit of an arbitrary partner is
unnecessary for this construction. `MarkedErasure.lean` proves this
preservation theorem and its combination with the source-deletion lemma.

## 2. The short and long endpoint diamonds

If `v=3 mod 4`, then

\[
T^2(v-1)=T^2(3v-1)=\frac{3v-1}{4}.
\]

The smaller arm takes one halving and one odd step; the larger arm takes
two halvings. Applying the source-deletion mechanism with `r=1` improves
the earlier three-quarter-source formula to `x=(n-1)/2` on the same phase
class.

A separate eight-clock identity handles a phase in the complementary
class. For every `a>=0`,

\[
T^8(256a+184)=T^8(768a+554)=27a+20.
\]

The parity words are `00011100` and `01000001`. Equivalently,

\[
v\equiv185\pmod{256}
\quad\Longrightarrow\quad
T^8(v-1)=T^8(3v-1).
\]

This eight-clock identity was found independently by the symbolic and
rewriting searches; the formal proof is adapted from the rewriting agent's
standalone Lean proof. It is a complete affine identity on the indicated
ordinary progression, rather than a finite numerical sample.

Now take `v=147 mod 256`. Then `v=3 mod 4`, `3v=185 mod 256`, and
`9v=3 mod 4`. Padding the short identities to clock eight gives

\[
T^8(v-1)=T^8(3v-1)=T^8(9v-1)=T^8(27v-1).
\]

The first three endpoints permit deletion of two initial odd steps,
giving a quarter-source partner. All four permit deletion of three,
giving an eighth-source partner. The corresponding general identities
are proved in `LongDiamondErasure.lean`.

## 3. Why the displayed family has the required phase

Let `u=2^s+1` and `v=3^{k-2}u`. Since `s>=8`, `u=1 mod 256`. Also

\[
3^{64}\equiv1\pmod{256},\qquad3^{29}\equiv147\pmod{256}.
\]

Therefore `v=147 mod 256`. The initial odd-run identities send `x_j`
to `v-1` after `k-2` clocks and `n_j` to `9v-1` after `k` clocks.
The eight-clock diamond then proves

\[
T^{k+6}(x_j)=T^{k+8}(n_j).
\]

The equation `4x_j+3=n_j` proves the claimed source saving exactly.
Finally, `k+8<=k+s=d` because `s>=8`.

## 4. Marked-band membership

Because `0<2^k<=2^d`, the value `n_j=2^d+2^k-1` lies in
`[2^d,2^{d+1})`, so its binary exponent is exactly `d`. It is odd.

The band condition is

\[
(d+1)(n_j-2^d)\le70\,2^d.
\]

Here

\[
d+1=66j+40\le70(j+1)\le70\,2^j\le70\,2^s.
\]

Multiplying by `2^k` and using `n_j-2^d=2^k-1<=2^k` proves the condition.

## 5. No descent anywhere in the native horizon

The first `k` steps form an increasing odd run. The state at its end is

\[
T^k(n_j)=3^k u-1.
\]

At any later step the shortcut map is at least division by two, so for
`0<=a<=s`,

\[
T^{k+a}(n_j)\ge\frac{3^k u-1}{2^a}
\ge\frac{3^k u-1}{2^s}.
\]

Since `k>=2s`, write `k=2s+b`, `b>=0`. Then

\[
\frac{3^k}{2^{k+s}}=(9/8)^s(3/2)^b\ge1.
\]

It follows that

\[
3^k u-1\ge2^s(2^k u-1)=2^s n_j.
\]

Thus `T^t(n_j)>=n_j` throughout `0<=t<=k+s=d`. This proof supplies the
general lemma `no_descent_through_run_plus_gap`: any positive `u` and
parameters `k>=2s` have this non-descent prefix.

## 6. What is finished, and the first remaining inference

The three claims are unconditional arithmetic statements about positive
ordinary integers. Every member of the family is excluded from being the
least positive counterexample or the least marked counterexample: under
the corresponding strong induction, its smaller marked partner converges,
and the exact common future transfers convergence.

This does not independently prove convergence for every member of the
family. Its partner need not belong to the same parameterized family;
an induction only on `j` would therefore be invalid. The full theorem
still requires a smaller partner for every possible least source, or the
corresponding marked-component cover with its source bound preserved.

The literature supplied the exact word/cylinder viewpoint and identified
which formal consequences are safe. Bernstein–Lagarias conjugacy alone
does not preserve rationality in the needed direction. Dubickas's
complexity theorem supplies a lower bound on possible divergent parity
languages, but does not force repetitions. Here the positive step is an
explicit ordinary diamond and its lift, not an invocation of one of those
unproved converse statements.

## File and verification boundaries

`HalfSourceMerge.lean` proves the generic deletion theorem and its
two-clock specialization. `LongDiamondErasure.lean` proves the
eight-clock identity, its short--long--short composition, and the
quarter/eighth-source instances. `MarkedErasure.lean` proves that deletion
preserves the marked section. `NewBandFamily.lean` packages the
specific family, markedness, native-horizon non-descent, and the merger.
Compiler logs, rather than this prose, record which files have completed
kernel checking.

The pre-existing `ShellCover.odd_run`, `ShellCover.orbit_add` and
`ForwardSection.Marked` are the only repository interfaces used. No
assumption of GRH or of an unproved Collatz closure is used.
