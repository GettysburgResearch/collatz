# Independent review: the head-three negative-shadow obstruction

2026-11-22. **Verdict: PASS, within the stated scope.**

Reviewed the new `lean/HeadThreeNegativeCycle.lean`, its written
note and complete-source construction. Reconstructed the arithmetic
independently rather than importing the author's checker. No mathematical
error was found. The unbounded family has a high final source gap; the
alphabet-four assertion is one explicit complete source.

## 1. Ordinary source and original target

The source is `q=2048b+429`, its powered source is `S=4q`, and the target
is always `n=2S-1=16384b+3431`. The exact odd-source path is

\[
2048b+429\xrightarrow{3}768b+161
\xrightarrow{2}576b+121
\xrightarrow{2}432b+91
\xrightarrow{1}648b+137
\xrightarrow{2}486b+103=r.
\]

All displayed states are positive odd integers for every natural `b`;
the exponents are exact valuations. The five odd transitions consume
ten shortcut clocks. Direct affine reconstruction of all thirteen target
steps gives

\[
T^{13}(n)=354294b+74222=729(r-1)-136,
\]

and every intermediate target state at clocks 1 through 13 is strictly
greater than the same original `n`. The coefficients in the Lean module
agree with these independently reconstructed states, including the
halvings at clocks 4 and 10.

## 2. Sign, parity, and every intermediate comparison

The positive complement map is `R(c)=c/2` on even inputs and
`R(c)=(3c-1)/2` on odd inputs. It represents the absolute value of the
signed negative Collatz orbit. Its actual cycle is

\[
136,68,34,17,25,37,55,82,41,61,91,136.
\]

There are seven odd steps and four even steps. If `C_j=R^j(136)` and
`o_j` counts odd inputs before clock `j`, then

\[
C_j\le136,\qquad 2^j\le8\,3^{o_j}\quad(j\ge0).
\]

The ratio `3^(o_j)/2^j` has minimum `1/8` in the first period, after
the three initial halvings. Each subsequent full period multiplies that
ratio by `2187/2048>1`.

Suppose `486b+102=2^H d`. For `0<=j<=H`, the target and complement
have the same parity at every required preterminal step, because their
sum still contains the required power of two. Therefore

\[
T^{13+j}(n)+C_j=729\,3^{o_j}2^{H-j}d.
\]

No claim about matching parities after the supplied binary window is
needed. Multiplication by eight and the uniform multiplier bound give

\[
8T^{13+j}(n)\ge729(486b+102)-1088,
\]

\[
729(486b+102)-1088-8n=223222b+45822>0.
\]

This proves the original-target inequality at every clock through
`13+H`, not merely at complete negative periods. The natural-number
subtraction in the complement map causes no sign issue: every complement
is positive, and the existing lift retains it by an additive equality.

## 3. The unbounded complete-source construction

For `k>=2`, take the integer residue

\[
s=34\,4^{(24-k)\bmod27}\bmod81,
\qquad a=2+2\,3^{k+1}s.
\]

Here subtraction occurs in the integers before reduction modulo 27.
Since `4^27=1 mod81`, one has `1<=s<=80`, `3` does not divide `s`,
and `4^(k+3)s=34 mod81`.

An independent calibration proof uses

\[
A_m=\frac{4^{3^m}-1}{3^m},\qquad m\ge3.
\]

The exact base has `A_3=48 mod243` and `3|A_3`. Cubing gives

\[
A_{m+1}=A_m+3^m A_m^2+3^{2m-1}A_m^3.
\]

Both correction terms vanish modulo 243 for `m>=3`, so
`A_m=48 mod243` for every such `m`. The binomial expansion similarly
gives

\[
\frac{4^{3^m s}-1}{3^m}\equiv48s\pmod{243}.
\]

Define

\[
\tau=\frac{2^a-4}{3^{k+1}},\quad
r=1+4^k\tau,\quad u=1+3^k\tau=\frac{2^a-1}{3}.
\]

The quotient is integral and `tau=192s mod243`. Thus

\[
r-1\equiv3\,4^{k+3}s\equiv102\pmod{243}.
\]

Also `v_2(tau)=2`, since `a>2` and the denominator is odd. Hence `r`
is odd, and the congruence strengthens to `r=103 mod486`. Bernoulli's
inequality gives `tau>=12`, so `r>=193`; therefore
`b=(r-103)/486` is a nonnegative integer.

The actual odd states after `j` of the next `k` gap-two transitions are

\[
1+3^j4^{k-j}\tau\qquad(0\le j\le k).
\]

They are all positive and odd, every gap is exactly two, and the endpoint
is `u`. The final exact gap is `3u+1=2^a`, reaching one. Therefore the
complete ordinary source word is

\[
[3,2,2,1,2]\mathbin{++}[2]^k\mathbin{++}[a].
\]

Its shortcut clock from `q` is `10+2k+a`. Finally
`v_2(r-1)=2k+2`, so the target has no descent through clock `2k+15`.
This is a complete-source construction for every `k>=2`; its modular
calibration remains written mathematics, not an additional Lean theorem.

## 4. Lean statement and the complete alphabet-four witness

The main formal statement quantifies natural `H,b,d,t` and assumes only
`486b+102=2^H*d`, `0<t`, and `t<=13+H`. Its conclusion compares
`orbit t (16384*b+3431)` strictly against the same original target.
There is no completeness, convergence, or arbitrary-shadow hypothesis
hidden in that statement. The pin itself prevents `d=0`.

`GapTrace` stores positive exponents and exact edge equations. In the
general prefix the displayed endpoint formulas are odd. For the complete
concrete trace, endpoint one together with all the supplied positive gaps
also retains the actual ordinary semantics; the independent checker
separately tests the exact valuation at every edge.

The complete alphabet-four source is

\[
q=58849709,\quad b=28735,\quad H=11,\quad d=6819.
\]

Its 46 odd steps have total shortcut clock 99 and end at one. All gaps
are at most four. Its target `470797671` stays strictly above itself
through clock 24 and equals `10871688401` at that clock. As a finite
scope control, its observed first descent is at clock 64, to `310287853`.
The theorem claims no descent only through 24.

## 5. Execution evidence and scope

Independent replay of the new Lean module passed with warnings as errors:
source SHA256
`cffc9b414abaa6cb2d346a433a820bd3da44be5afcc9b684a7c601f48c10df5d`.
All ten public axiom audits passed. The reported axioms are confined to
the standard `propext`, `Classical.choice`, and `Quot.sound`; the finite
cycle itself uses no axioms. Previously replayed imported modules were
reused, rather than broadly rebuilding old work.

Independent finite arithmetic checks covered `b=0,...,511` with every
admissible binary pin, 551 complement clocks, 640 calibration instances,
81 residue calibrations including `k>24`, complete sources `k=2,...,8`,
and the entire alphabet-four witness. All passed. Logs and receipt:
[compiler log](../../reports/central-obstruction-20261122/negative-shadow-review-lean.log) and [receipt](../../reports/central-obstruction-20261122/negative-shadow-independent-review.json).
The [archived independent review worksheet](../../reports/central-obstruction-20261122/review_negative_shadow.py.txt) is preserved as executed. It refers to the original local author checkout; use this packet's `check.py` for the portable published-checkout replay.

One wording clarification was requested: the unbounded family refutes a
**fixed, source-independent** upper bound on original-target descent
time in this family. It does not refute bounds allowed to grow with the
source's height. Its proved window has order `k`, whereas its binary
source length has order `3^k`. The large terminal gap also leaves the
repository's high-gap source replacement available. Neither unbounded
alphabet-four realization nor failure of all merger/replacement policies
has been established.
