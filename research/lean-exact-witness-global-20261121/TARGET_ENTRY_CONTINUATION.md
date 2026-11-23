# Complete-witness transport: unbounded output length and a terminating signed normalizer

**Status: the universal target-entry step remains OPEN.** This continuation
keeps the original target and attempts to transform the entire supplied
certificate. It proves a quantified obstruction to length-bounded output
construction directly in the user's residue-512 formulation. It then follows
the resulting variable-length construction through an arbitrary source word,
using a terminating signed rational normalizer. That normalizer leaves an
explicit ordinary target; its convergence is not supplied by normalization.

The six public statements in
[`lean/Collatz/WitnessLengthSeparation.lean`](lean/Collatz/WitnessLengthSeparation.lean)
are core-Lean theorems. The arbitrary-word normalizer and the six-step
Mersenne family below have written proofs and exact executable controls;
they are not counted as Lean declarations.

## 1. Four input odd steps cannot bound the output length

For an integer `h>=1`, put

\[
m=27h,\qquad K=\frac{4^m-1}{81},\qquad
x=256K+1,\qquad y=128K+1=\frac{x+1}{2}.
\tag{TE1}
\]

The quotient is an integer: `4^27=1 mod81`, and hence the same congruence
holds for `4^(27h)`. It is positive and odd. In particular

\[
x\equiv257\pmod{512}.
\]

The complete input word is exactly

\[
\boxed{[2,2,2,2m+2].} \tag{TE2}
\]

Its correction is 175, and its complete certificate identity is

\[
3^4x+175
=81(256K+1)+175
=256(81K+1)
=2^{2m+8}.
\tag{TE3}
\]

Thus this family consists of actual positive inputs in the set E from the
question, each with a four-odd-step certificate. In increasing-tuple form
the witness is `0,2,4,6,2m+8`.

The actual output trajectory begins

\[
128K+1\xrightarrow{2}96K+1
\xrightarrow{2}72K+1
\xrightarrow{2}54K+1
\xrightarrow{1}4^m+1.
\tag{TE4}
\]

The arrows are exact accelerated odd gaps. It then follows the states

\[
z_i=3^i4^{m-i}+1\qquad(0\le i\le m-1),
\]

with gap two between successive displayed states. Every displayed state
is odd and exceeds one. Therefore every possible complete output
certificate must contain the exact prefix

\[
\boxed{[2,2,2,1]\mathbin{++}[2]^{m-1},}
\tag{TE5}
\]

and a nonempty complete tail at the odd endpoint

\[
4\cdot3^{m-1}+1>1.
\]

In particular, if an output certificate exists, its length `r_out` obeys

\[
\boxed{r_{\rm out}\ge m+4=27h+4.} \tag{TE6}
\]

This is a statement about **every** output certificate, not just the
first one found by an algorithm. At an odd state, the power of two in
`3n+1` is uniquely determined when its quotient is required to be odd.
The Lean proof uses that uniqueness to consume (TE5) from an arbitrary
supplied output certificate. It preserves a nonempty complete tail, and
then transfers the length bound to the original arbitrary increasing
tuple, retaining its actual given length and every exponent.

Consequently, for every natural bound R there is an actual four-step
input in residue 257 whose half has **no certificate of length at most
R**. This rules out every total certificate transformer with an output
length bound depending only on input length. It does not exclude a bound
depending on the input exponents, and it does not establish that output
certificates exist for infinitely many members of this family.

The user's allowance of arbitrarily longer output witnesses is therefore
essential to a complete general transformation. This theorem is an
obstruction to an extra restriction, not a counterexample to the user's
unrestricted implication.

### The two ordinary clocks are retained

For the shortcut map `T(n)=n/2` on evens and `(3n+1)/2` on odds,

\[
\boxed{T^{2m+8}(x)=1,\qquad
T^{2m+7}(y)=3^m+1<y.} \tag{TE7}
\]

The final inequality follows from `3^m<4^m=81K+1` and `K>0`.
Thus none of these outputs can be a least positive Collatz counterexample.
The inequality is a strict descent; it does not assert convergence of
every smaller integer or provide a complete certificate for `3^m+1`.

The file uses index `h>=0` with `m=27(h+1)` to avoid an empty exceptional
parameter. `four_step_input`, `exact_clocks`, `output_prefix_and_tail`,
`output_length_lower_bound`, `tuple_length_lower_bound`, and
`no_input_length_bound` are the six public statements. No conjectural
existence assumption or output-length cutoff appears in their proofs.

## 2. An arbitrary complete source word has a terminating signed normalizer

The length separation suggests unfolding a large exponent into an
arbitrarily long physical target word. I tested this on the entire source
word, allowing a signed carry and retaining every ternary denominator.

Let a nonempty complete source word W have length r, total A, and correction
C, so

\[
3^r x+C=2^A.
\]

The target `y=(x+1)/2` satisfies the exact identity

\[
\boxed{3^r y=2^{A-1}+z_0,\qquad
z_0=\frac{3^r-C}{2}\in\mathbb Z.} \tag{TE8}
\]

Here C is odd. Its last summand is a power of two modulo three, so
`3 does not divide C`. Hence `3 does not divide z_0`. The full prefix of
the supplied source word determines C; the last gap does not occur in C.
No source state or complete tail is replaced by an unrelated witness.

Consider the following exact integer procedure, starting at `(r,z_0)`:

\[
(j,z)\longmapsto
\begin{cases}
(j,z/2),&z\text{ even},\\
(j-1,(z+3^{j-1})/2),&z\text{ odd and }j>0.
\end{cases}
\tag{TE9}
\]

Stop at `j=0`. This is the shortcut map on the signed rational number
`z/3^j`, written without fractions.

**Termination is unconditional.** While `j>0`, the numerator is prime
to three and therefore nonzero. An even step strictly decreases `|z|`.
An odd step decreases j; if the new j remains positive, its numerator
is again prime to three. Thus the lexicographic natural rank `(j,|z|)`
strictly decreases. The procedure reaches a signed integer K at some
finite clock k, after exactly r odd steps. This conclusion makes no
assumption about the future behavior of K under signed Collatz.

### Exact compilation to the original target

Suppose the normalizer finishes by clock `k<=A-1`. Then

\[
\boxed{T^k(y)=2^{A-1-k}+K.} \tag{TE10}
\]

Indeed, retain the invariant

\[
3^{j_i}T^i(y)=2^{A-1-i}+z_i.
\tag{TE11}
\]

At every step before k, the unused exponent is positive. Thus the parity
of the actual positive target state equals the parity of `z_i`, since
`3^j` is odd and the high power of two is even. In the even branch the
invariant divides by two. In the odd branch, applying the actual shortcut
map gives

\[
3^{j_i-1}T^{i+1}(y)
=2^{A-2-i}+\frac{z_i+3^{j_i-1}}2.
\]

This is exactly (TE9), including its denominator change. At j=0 one
gets (TE10). All these are physical clocks of the original target.

If `k>A-1`, the formal normalizer still terminates, but the compilation
has spent its binary precision first. Once the high exponent reaches
zero, its high block is odd and can change the next parity. The formal
signed path may no longer be substituted for the actual target path.
No endpoint from beyond that clock is licensed by (TE11).

This clock condition can fail for a literal first-hit complete input in
the original residue class. For `x=129`, the first-hit certificate has
`r=44,A=77`. Its normalizer takes `k=86` and ends at `K=7`, beyond the
available precision 76. The actual target is `y=65`, which reaches one
at clock 19. Its first parity disagreement with the continued formal
trace occurs exactly at clock 76. This is an exact control of the
compilation boundary, not a bad-query counterexample.

This normalizer is not a new convergence decision procedure. It compiles
a finite original-target prefix when its stated clock is funded. It leaves
the explicit positive ordinary value `2^(A-1-k)+K`, whose complete
certificate remains to be obtained.

## 3. Actual variable-length continuation: a six-step input yields Mersenne targets

The normalizer's signed endpoint is not restricted to zero or a positive
small state. For the source prefix `[2,2,2,3,3]`, followed by its final gap
a, one has

\[
r=6,\qquad A=a+12,\qquad C=7207,\qquad
z_0=-3239.
\]

The signed rational trace is exactly

\[
-\frac{3239}{729},\quad
-\frac{1498}{243},\quad
-\frac{749}{243},\quad
-\frac{334}{81},\quad
-\frac{167}{81},\quad
-\frac{70}{27},\quad
-\frac{35}{27},\quad
-\frac{13}{9},\quad
-\frac53,\quad -2.
\tag{TE12}
\]

Thus `k=9`, `K=-2`. One further actual even step gives

\[
\boxed{T^{10}(y)=2^{a+1}-1.} \tag{TE13}
\]

These are complete ordinary inputs in the original residue domain for
every

\[
a=340+486h,\qquad h\ge0,\qquad
x=\frac{2^{a+12}-7207}{729}.
\tag{TE14}
\]

For integrality it suffices to check `2^352=7207 mod729` and
`2^486=1 mod729`. Positivity is immediate. Since `a+12>=9`, the original
certificate identity modulo 512 gives `x=257 mod512` (indeed
`7207+729*257=512*380`). The input has exactly the complete six-gap word
`[2,2,2,3,3,a]`.

There is also a direct all-exponent prefix certificate for (TE13):

\[
\boxed{y\xrightarrow{[2,2,2,1,1,2]}2^{a+1}-1.} \tag{TE15}
\]

Its correction is 2215 and its total is 10, and (TE8) gives

\[
729y+2215=2^{10}(2^{a+1}-1).
\]

The remaining variable-length continuation is physical and exact. Put
`b=a+1`. The next b ordinary inputs are odd, and

\[
T^{10+i}(y)=3^i2^{b-i}-1\quad(0\le i\le b),
\qquad T^{10+b}(y)=3^b-1.
\tag{TE16}
\]

This inserts `b-1` exact gap-one transitions between odd states, followed
by one additional odd shortcut step whose displayed endpoint `3^b-1`
is even. It does not label that final step a complete accelerated odd gap.
Every complete output certificate, if it exists, needs at least `6+b`
odd steps. The forced target excursion also exceeds every fixed multiple
of the input source's size along this family, because

\[
x<\frac{2048}{729}\,2^b,
\qquad
T^{10+b}(y)=3^b-1,
\]

and `(3/2)^b` is unbounded. The input has only six odd steps throughout.
In fact every source odd gap in (TE14) is at least two, so its odd
states strictly decrease until one. Its complete ordinary peak is
`(3x+1)/2`, at its first clock. The same unbounded ratio therefore holds
relative to the whole supplied source trajectory's peak, not just its
starting value. The target's displayed high point occurs one ordinary
clock before that source reaches one.

This excludes a fixed multiplicative bound on target height in terms of
source height for this fixed input length. It does not exclude every
polynomial bound in the numerical input value.
These statements concern a forced finite part of each ordinary target;
they do not assert that any member escapes forever.

Equation (TE15) gives the exact equivalence

\[
y\text{ reaches }1
\quad\Longleftrightarrow\quad
2^{341+486h}-1\text{ reaches }1.
\tag{TE17}
\]

The transformation has therefore reached a concrete family of ordinary
Mersenne targets. The supplied six-step certificate for x does not
provide the remaining complete tail for that Mersenne integer or for
`3^b-1`. No success theorem is inferred from having normalized every
source coefficient or from the rank decrease of the auxiliary signed
procedure.

The controls also include a genuinely terminating output branch. The source
prefix `[2,2,2,4]` has `r=5,C=1549`; its normalizer reaches `K=0` at clock
eight. For every funded integral terminal exponent, the actual output
then is a power of two and its complete certificate is obtained by
extending the last actual gap. This local success does not cover the
signed endpoints in (TE12).

## 4. Attempts to close the general target

The signed normalizer was tested as a way to cross the original finite
source boundary, rather than produce another competing source. Its exact
termination does not give either missing resource: sufficient binary
precision through its formal clock, or a complete certificate for the
ordinary value left after that clock.

A same-clock source/target coupling had already retained every parity
disagreement in PR176's exact signed debt. Reindexing the two clocks did
not produce a new sign estimate. I did not formalize that rearrangement
as a new result. Prefixwise odd-count dominance also did not yield the
needed source-word exchange: moving the odd positions changes the
correction, while integrality still requires divisibility by the whole
`3^r`. No grade-funded permutation with that property was found.

For the normalizer, appending terminal gap-two padding to the input
changes its r, A, C and signed initial numerator simultaneously. It is
not legitimate to increase A while retaining the old signed trace and
the same original input. A general rewrite that funds the normalizer's
clock, retains the original target, and pays for its remaining ordinary
tail would be a closing step. It has not been supplied.

## Verification and source boundary

- Parent science: PR177 at
  `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
  `HIGH_VARIANCE_WITNESS.md`, `JOINT_MINIMAL_COUNTEREXAMPLE.md`, and
  `WITNESS_CLOSURE_CONTINUATION.md`.
- Current PR180 read at `04572b94c8a58f964ba9b2b1b1bccfe7e9b12ae2`,
  `research/high-variance-20261123/GLOBAL_SOURCE_SYNTHESIS.md`:
  complete low-gap clusters and the source-only coercivity boundary.
- Current PR182 read at `aa12c13601cacec2c8496f1349b4947457dc1b45`,
  `research/high-variance-20261123/SOURCE_SURGERY.md`:
  all-depth forced routes and their changing-root qualification.
- PR176 read at `fdcb137214f4be8ac30dbb025d6eeb6568e22e2a`,
  `research/lean-global-resolvent-20261121/overview/returns/WHOLE_SOURCE_DEBT_ATTEMPT.md`:
  actual same-clock debt and the failed source-clock deadline.
- The new Lean source was built with Lean 4.34.1, then separately compiled
  with warnings treated as errors. The dedicated
  [`AuditWitnessLengthSeparation.lean`](lean/AuditWitnessLengthSeparation.lean)
  audits its six public declarations. No custom axiom or admitted proof is
  used. Existing dependency objects were reused.
- [`target_entry_controls.py`](target_entry_controls.py) checks the exact
  families, forced paths, signed normalizer and its physical compilation.
  Normal and optimized runs use explicit guards. These finite controls
  supplement the displayed written proofs; they are not universal target
  convergence tests.

The original implication allows precisely the unbounded output lengths
that (TE6) requires. Its proof or disproof remains open in this checkpoint.
