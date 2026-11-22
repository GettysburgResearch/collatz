# A reachable negative cycle blocks the naive rational-shadow closure

## Result and precise limit

Throughout, `T(n)=n/2` for even `n`, and `T(n)=(3n+1)/2` for odd `n`.
One application is one ordinary shortcut clock.

The remaining valuation-three family in PR180's `MIXED_COVER.md` contains
an ordinary source/target configuration whose rational target shadow is
the negative seventeen Collatz cycle. Its positive high part expands by
`2187/2048` every eleven shortcut clocks. The initial three halvings of
that cycle do **not** undo the preceding growth relative to the original
target.

The main new theorem is an all-parameter, actual-orbit statement. For
natural numbers `b,H,d`, put

\[
q=2048b+429,\qquad n=8q-1=16384b+3431.
\]

If

\[
\boxed{486b+102=2^H d,}
\tag{1}
\]

then

\[
\boxed{T^j(n)>n\qquad(1\le j\le13+H).}
\tag{2}
\]

This is `original_target_no_descent` in `HeadThreeNegativeCycle.lean`.
All clocks in (2) refer to the same original positive integer. The
theorem is not a statement about a succession of unrelated finite
witnesses or an unlifted 2-adic orbit.

There are complete ordinary source certificates with arbitrarily large
`H`, by the elementary construction in Section 4. Their final gap is
large, so the repository's existing high-gap source rewrite remains
available. A separate complete alphabet-four witness exhibits one whole
negative cycle inside the exact bounded-four domain. We do **not** prove
unbounded complete alphabet-four realization, nor rule out smaller
merger partners, source replacements, or the new extremal-source policy.
This is a counterexample to a proposed universal rational-shadow
contraction inference, not to Collatz or to the whole mixed program.

## 1. The cycle occurs in the actual final residual

The source is PR180 at
`ab3973099f0d285bbe88972382ad599bb02cd460`,
`research/lean-joint-20261122/MIXED_COVER.md`, Sections 8--10.
Its final family is

\[
q=256j+173,\quad u=96j+65,\quad n=2048j+1383,
\]

with supplied source prefix `[3,2,2]`. Our subfamily is `j=8b+1`.
It has the exact ordinary source prefix

\[
\begin{aligned}
2048b+429&\xrightarrow{3}768b+161
\xrightarrow{2}576b+121
\xrightarrow{2}432b+91\\
&\xrightarrow{1}648b+137
\xrightarrow{2}486b+103=r.
\end{aligned}
\tag{3}
\]

Every endpoint is positive and odd, so every indicated gap is exact.
`source_entry` proves the full source trace. The original powered source
is `S=4q`; the target remains `n=2S-1` throughout the comparison.

Thirteen actual target steps give

\[
T^{13}(n)=354294b+74222=729r-865.
\tag{4}
\]

The target has not descended during any of those thirteen steps.
`head_three_entry` and `head_three_entry_no_descent` prove both assertions
uniformly in `b`, by exact affine step identities. There is no numerical
bound on `b`.

At the source gap-two fixed point `r=1`, the target expression in (4) is

\[
729\cdot1-865=-136.
\]

The signed shortcut map sends this number around the negative cycle

\[
-136,-68,-34,-17,-25,-37,-55,-82,-41,-61,-91,-136.
\tag{5}
\]

It has seven odd steps and eleven total steps. Thus its multiplier on a
positive high part is `3^7/2^11=2187/2048>1`. Negative cycles themselves
are familiar; the new point is the exact entrance (3)--(4) from the
current final head-three residual, with the original-target inequality
proved for every intermediate clock.

## 2. Why the three initial halvings do not give original-target descent

Use the positive complement map already formalized in `NegativeCarry`:

\[
S(c)=\begin{cases}c/2,&c\text{ even},\\(3c-1)/2,&c\text{ odd}.
\end{cases}
\]

Let `C_j=S^j(136)` and let `o_j` count odd complement steps through clock
`j`. The positive counterpart of (5) gives, for every `j>=0`,

\[
\boxed{C_j\le136,\qquad 2^j\le8\,3^{o_j}.}
\tag{6}
\]

For the first eleven phases, the second inequality is an exact finite
calculation; its least ratio occurs after the first three even steps.
Every subsequent cycle multiplies `3^{o_j}/2^j` by `2187/2048>1`.
`negative_cycle_uniform` checks the extension to all clocks by strong
induction, using the exact cycle return and the even-count addition law.

Write `Q=2^H d=486b+102`, and let `y=T^13(n)`. Equations (1) and (4)
give

\[
y+136=729Q.
\]

For every `0<=j<=H`, the already proved complement lifting theorem gives
the exact ordinary identity

\[
T^j(y)+C_j=729\,3^{o_j}2^{H-j}d.
\tag{7}
\]

Combining (6)--(7) yields

\[
8T^j(y)\ge729Q-1088.
\]

The comparison is against the **original** target:

\[
\begin{aligned}
729Q-1088-8n
&=729(486b+102)-1088-8(16384b+3431)\\
&=223222b+45822>0.
\end{aligned}
\tag{8}
\]

Thus every one of these actual endpoints is above `n`. Combining with
the first thirteen steps proves (2). A proof that merely checked the
full-cycle multiplier would miss the three early halvings; (6)--(8)
cover them explicitly.

## 3. Actual long source words are retained

For every `k,d>=0`, there is an exact source trace

\[
1+2\,4^k d
\xrightarrow{\,2^{[k]}\,}
1+2\,3^k d,
\tag{9}
\]

where `2^[k]` denotes a list of `k` gaps equal to two. All intermediate
states are odd. `source_twos` proves (9) structurally for arbitrary `k`.
`source_long_prefix` composes it with (3) whenever

\[
486b+102=2^{2k+1}d.
\]

This is a literal positive ordinary prefix, including every exact gap;
the negative shadow is only an arithmetic device for tracking its
associated target. A complete source tail may be attached only when an
actual certificate for the endpoint is supplied.

## 4. Unbounded complete-source realization: an elementary construction

This section is a **written proof**, independently checked by the exact
construction in `negative_cycle_certificate.py`. The modular calibration
has not been added to the Lean theorem count.

Fix any `k>=2`. Define

\[
s=\bigl(34\,4^{(24-k)\bmod27}\bigr)\bmod81,
\qquad a=2+2\,3^{k+1}s.
\tag{10}
\]

Since `4^27=1 mod81` and `34` is a unit modulo 81,

\[
1\le s\le80,\qquad4^{k+3}s\equiv34\pmod{81}.
\tag{11}
\]

Set

\[
t=\frac{2^a-4}{3^{k+1}},\qquad
r=1+4^kt,\qquad u=1+3^kt=\frac{2^a-1}{3}.
\tag{12}
\]

We show `r=103 mod486`, so that `b=(r-103)/486` is an ordinary
nonnegative integer and (3) is available.

For `k>=2`, define

\[
B_k=\frac{4^{3^{k+1}}-1}{3^{k+2}}.
\]

The base `k=2` is the exact integer
`B_2=222399981598543`, which is 16 modulo 81. Cubing gives the identity

\[
B_{k+1}=B_k+3^{k+2}B_k^2+3^{2k+3}B_k^3.
\]

Consequently every `B_k` is an integer and `B_k=16 mod81`. The binomial
theorem, using `k+3>=5` to dispose of all terms of degree at least two
modulo 243 after division, now gives

\[
\begin{aligned}
t
&=\frac{4\bigl((1+3^{k+2}B_k)^s-1\bigr)}{3^{k+1}}\\
&\equiv12 B_k s\equiv192s\pmod{243}.
\end{aligned}
\]

Therefore, by (11),

\[
r-1=4^kt\equiv3\,4^{k+3}s\equiv102\pmod{243}.
\tag{13}
\]

The integer `a` is even and greater than two. The quotient `t` is a
multiple of four, so `r-1` is even. Equation (13) lifts to
`r-1=102 mod486`, as required. The binomial lower bound gives `t>=12`;
since `k>=2`, this gives `r>=193`, and its residue class then ensures
`r>=103` and `b>=0`.

Equation (12) supplies the complete exact source word

\[
\boxed{
[3,2,2,1,2]\mathbin{++}2^{[k]}\mathbin{++}[a]
}
\tag{14}
\]

from `q=2048b+429` to one. The twos end at `u`, and
`3u+1=2^a`. Every endpoint is positive and odd. This proves a complete
ordinary certificate for every `k>=2`, independently of the target's
convergence.

Finally, `v_2(2^a-4)=2`, and the denominator in (12) is odd. Thus

\[
v_2(r-1)=2k+2.
\]

The kernel-checked theorem (2) applies with `H=2k+2`, proving no descent
of the original target through clock `2k+15`. This gives arbitrarily
long fully realized windows, with complete source certificates.

**High-gap boundary.** In (10), `a>=56`. These are not complete
alphabet-four witnesses. A high source gap licenses an already-known
lower-grade cofinal replacement in the repository. This construction
therefore refutes a fixed, source-independent upper bound on original-target descent time and
the naive shadow contraction claim; it does not refute a policy allowed
to change the supplied source.

## 5. One complete alphabet-four witness

The actual instance

\[
b=28735,\quad q=58849709,\quad S=235398836,\quad n=470797671
\]

has `r=13965313` and

\[
r-1=2^{11}\cdot6819.
\]

Its supplied complete source word is

```
[3,2,2,1,2,2,2,2,2,2,1,3,2,3,1,4,2,2,2,2,2,2,4,
 2,1,2,2,1,2,2,4,3,2,1,2,3,1,2,1,4,1,3,1,2,3,4]
```

The word has shortcut clock 99, every gap is at most four, and its
endpoint is one. The target satisfies (2) through clock 24; the last
displayed target endpoint is `10871688401`. Thus a full negative cycle
really occurs inside a complete bounded-four source. The theorem
`complete_cap_four_example` checks the complete source, the alphabet
bound, and the all-intermediate original-target inequality.

This single witness does not establish unbounded bounded-four windows.
It may admit an independent successful source replacement or an earlier
smaller merger partner. It is not asserted to be a grade record in the
new extremal-source program.

## 6. Formal evidence and the next mathematical obligation

`HeadThreeNegativeCycle.lean` imports the existing `NegativeCarry`
module, whose source SHA256 is
`011a50ca04eebf2efb5c9ddb402ad0f89d9af77077a52483ddb573d662235e08`.
It reuses the established exact complement lift and source-prefix
semantics. The negative cycle itself is checked by kernel reduction;
all-window lifting and original-target comparison are symbolic proofs.
The complete-source calibration in Section 4 remains a written theorem.

All ten public theorem audits passed Lean 4.34.1 with one worker and
warnings as errors. Their reported axioms are subsets of `propext`,
`Classical.choice`, and `Quot.sound`; the finite cycle itself uses none.
There is no `sorry`, custom axiom, or `native_decide`. The source receipt
and complete build output are retained separately for exact replay.

The exact checker passed in ordinary and optimized Python modes. It
checked the complete constructions for `k=2,3,4,5`, the full alphabet-four
example, and the cycle arithmetic. Both modes rejected four damaged
controls: a wrong binary pin, a nonexact source gap, a wrong source
endpoint, and substituting the enlarged intermediate carry for the
original target. The last control matters because that carry immediately
halves even though its original target remains below every endpoint in
the proved window. These finite checks exercise the implementation;
the unbounded statements are supplied by the Lean and written proofs.

The remaining mixed-coverage problem is not solved. In particular, the
unproved step is not merely that every current positive rational shadow
eventually contracts: this source-derived shadow is negative and has an
expanding cycle. A complete solution must use further source information,
a successful source rewrite, a smaller ordinary merger, or another
global argument. The new extremal-source policy is one such candidate;
the obstruction above does not test its universal completeness.

## Integration with the independent extremal-source attempt

The full-interval version of the proposed source-clock policy was subsequently
refuted in [EXTREMAL_SOURCE_CLOCK_FAILURE.md](EXTREMAL_SOURCE_CLOCK_FAILURE.md):
source 1092 is globally maximal at its permitted grade, but its new target
2047 needs 58 clocks for first descent while the source reaches one in 23.
This is a separate counterexample; it does not assert that the narrower
head-three extremal-source question has been resolved.
