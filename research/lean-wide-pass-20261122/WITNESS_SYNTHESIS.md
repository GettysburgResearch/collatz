# Complete witnesses and physical word erasure in one source order

**Status: PROVED Lean interface; total dispatch remains OPEN.**
The new module is [WitnessSynthesis.lean](lean/WitnessSynthesis.lean).
It compiles arbitrary physical dyadic erasures into the complete-source
induction used by the latest alphabet-four work. It permits two independent
endpoint clocks and retains the literal supplied source word. There is no
new residue census, word-length cutoff, conjectural axiom, or assertion that
every target has an erasure.

## 1. Exact source refresh and what it changes

| Source | Frozen head | Relevant statements inspected |
|---|---|---|
| PR177 | `a0a0d76f91b4e3846c1b1f0706cad56cb6098317` | `BOUNDED_GAP_ATTACK.md`, `LOW_INTERVAL_REFINEMENT.md`, `PSI_SUFFIX_ATTACK.md`, `MERGER_RETAINED_EVEN.md`, and the corresponding core Lean source, especially `BoundedGapCofinal.lean`, `GapMultiset.lean`, and `GapComparison.lean` |
| PR185 | `6d2765ef462fb575c49d4133b54286be7ffe68ec` | `HalfSourceMerge.lean`, `LongDiamondErasure.lean`, `MarkedErasure.lean`, and the packet README |
| PR184 | `366dab89ee9548084ab9b5e4e90ff82abf287a20` | The physical band-coupling architecture inherited by PR185; its guarded mergers remain guarded |
| PR146 | `f431078244e868dc699fad011044f0d5e7f76437` | `WITNESS_TRANSFER.md`, including the distinction between a supplied antecedent witness and an uncontrolled returned target witness |
| PR164 | `9582df78eb4d768eb748d3cf367ba97582308a52` | `SOURCE_ZERO_DESCENT.md`, especially its literal two-arm substitutions, exact valuation corrections, and retained complete tails |
| PR172 | `b22d94240f3d44a04231508e5dfe9a4947a57125` | `C3_ARBITRARY_TAIL_DESCENT.md` and `INVERSE_CARRY_SELECTOR.md`, including the unresolved returned-witness resource exchange and the all-parameter obstruction to that particular inverse carry selector |

These are source inspections, not claims to have freshly rebuilt every
listed branch. The new module uses the already compiled ordinary map and
complete `GapTrace` representation in PR180. Its local proof was replayed
with Lean 4.34.1 and warnings as errors.

The decisive change from the preceding witness pass is PR177's **unguarded
alphabet-four predecessor construction**. Given a certified odd unit `q`
with its actual tail word, it supplies certified predecessors above every
bound using only gaps one through four before that same tail. An arbitrary
gap at least five anywhere in the source word pays for this entire prefix
under the highest-changed-grade order. An initial even run at least four
does so as well.

Consequently, the previous arbitrary terminal-gap/Mersenne query is no
longer the most informative boundary for this interval architecture. The
latest source has already moved the universal obligation to complete words
over the fixed alphabet one through four. Word length and the number of
gap-four letters remain unbounded.

The four-letter pump cannot be inserted without a grade payment at that
last level. Removing one grade eight does not pay for arbitrarily many
new grade-eight letters in the same well-founded order. Nor does the
existence of a new convergent source imply that its requested target
converges. Both obligations are retained below.

## 2. The exact complete-source representation

The ordinary shortcut map is

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.
\end{cases}
\]

`GapTrace(q,1,A)` records every actual positive-gap equation
\(3q_i+1=2^{a_i}q_{i+1}\), with terminal value one. The new
`PoweredTrace(S,e,A)` retains an explicitly positive `q`, the identity
\(S=2^e q\), and this exact odd word. Its complete ordinary hitting clock
is `e+sum(A)`, proved by `powered_trace_hit`.

The grade formula is exactly PR177's:

\[
\Gamma(e;A)=
 \bigl(\{2e+1\}\text{ if }e>0\bigr)
 \uplus\{2a:a\in A\}.
\]

`GradeDrop(new,old)` is the same literal highest-changed-multiplicity
formula: at some grade the new count is smaller, and every larger grade
has unchanged count. The well-foundedness theorem belongs to the cited
PR177 source; this compact interface does not reimport that full branch
or announce a different rank.

`source_grade_peel` proves directly that

\[
                    \Gamma(e;A)\prec\Gamma(e+1;A).
\tag{W1}
\]

`peel_powered_source` supplies the corresponding physical source
\(S'=T(S)=S/2=2^e q\) and retains **every letter** of `A`. It chooses
no fresh convergence witness for an intermediate target. This avoids the
uncontrolled returned-witness rank that obstructed the earlier resource
exchange in PR172.

## 3. Every physical half-size merger is a valid interval step

The active interval is the same as PR177's:

\[
                          0<t\le2S+1.
\tag{W2}
\]

Suppose the source is supplied as \(S=2^{e+1}q\), and a physical
certificate supplies positive `x` and **independent** clocks `a,b` with

\[
                2x+1\le t,\qquad T^a(x)=T^b(t).
\tag{W3}
\]

The inequalities give \(x\le S\). After halving the source once, the
child interval has ceiling

\[
                         2S'+1=S+1,
\]

so the child query `(S',x)` is active. Its complete source certificate is
the old odd word with initial even run decreased by exactly one, and W1
proves its grade decrease. The lower-grade interval hypothesis therefore
certifies `x`; the actual meeting W3 transports that certificate to `t`.

This is `half_size_merger_rule`. It applies to any physical merger meeting
the displayed size bound, not only to a particular short diamond or a
fixed binary residue. The two target clocks never need to be identified.

## 4. Arbitrary-length erasure, with two endpoint clocks

Write

\[
n=2^k u-1,\qquad x=2^{k-r}u-1,
\qquad 0<r\le k,\quad u>0,
\quad 2^{k-r}u>1.
\tag{W4}
\]

The last inequality guarantees a positive partner. In particular the
interface also permits `r=k` when `u>1`; the erased endpoint may be even.
For arbitrary natural clocks `L,R`, suppose an actual endpoint certificate
gives

\[
T^L(3^{k-r}u-1)=T^R(3^k u-1).
\tag{W5}
\]

The forced initial odd runs give

\[
\boxed{
2^r(x+1)=n+1,\qquad
2x+1\le n,\qquad
T^{k-r+L}(x)=T^{k+R}(n).
}
\tag{W6}
\]

`erase_prefix_asynchronous` proves W6 for all displayed parameters, with
no bound on the erased length or either endpoint clock. The proof uses
the ordinary orbit identities, so the meeting is physical; it does not
replace a formal affine equality by an unstated integrality claim.

`erasure_interval_rule` composes W6 with section 3. Thus **every** such
erasure is accepted by the common complete-source rank after one source
halving, independently of the erased target length. PR185's half-,
quarter-, and eighth-source families are synchronized special cases
`L=R`. Their endpoint hypotheses remain exactly those proved in that
source. Its marked-preservation theorem is an additional benefit where a
positive odd erased partner is required; markedness is unnecessary for
this interval rule.

The result is a compiler for supplied physical erasures. It is not a
claim that W5 has a suitable solution for every target.

## 5. Why independent endpoint clocks are needed

The two-clock diamond is valid when `v=3 mod4`. In the other odd phase,
put `v=4r+1`. The new kernel theorem `unresolved_endpoint_pair` gives

\[
\boxed{T^2(v-1)=r,\qquad T^2(3v-1)=9r+2.}
\tag{W7}
\]

This is an exact unbounded affine carry. It does not yield a convergence
transfer from `r` to `9r+2` merely because one endpoint has a known
certificate. The latest high-gap construction cannot pay its low-alphabet
replacement for free.

There is also a small exact reason not to impose synchronous clocks as a
universal interface. For `n=7`, use `k=3,u=1`. The possible positive odd
pure erasures have endpoint pairs `(8,26)` and `(2,26)`. Neither pair
ever meets at a common clock: after clock eight the first member is two
and the second is one, and their phases on `1 -> 2 -> 1` remain opposite.
The finitely many earlier clocks are checked in the kernel. This is
`seven_has_no_synchronous_endpoint_erasure`, quantified over **every**
clock, not a failed bounded search.

The new asynchronous interface handles the same case exactly:

\[
T^3(8)=T^8(26)=1,
\qquad T^5(3)=T^{11}(7)=1.
\]

`seven_asynchronous_erasure` is the corresponding instantiation. This
example motivates the clock interface; it is not proposed as a new
numerical verification frontier or a counterexample to Collatz.

## 6. The remaining global source language

After PR177's proved high-gap, coefficient-prefix, synchronized-step, and
retained-even rules, an uncovered interval state has a complete nonempty
source word over gaps at most four, with no nonempty supplied prefix whose
coefficient is noncontracting. Write `a` for its first gap and
\(c=\nu_2(3t+1)\) for the target's first gap. Its possible initial
valuations are restricted as follows by that source's proved rules:

| Initial source even run | First source gap | Remaining target first gaps |
|---:|---|---|
| 1 | 2 or 3 | 1 |
| 2 | 2 | 1 |
| 2 | 3 or 4 | 1 or 2 |
| 3 | 2 | 1 |
| 3 | 3 | 1 or 2 |
| 3 | 4 | 1, 2, or 3 |

For initial run three, the source core additionally lies outside the
published retained-even cover. The word length, values, and number of
gap-four letters are still unrestricted. The new compiler settles any
state in this residual language for which a physical erasure W5 is
supplied; it does not enlarge this table by a new finite search.

The first unsupported step remains a total successful selection on this
unbounded residual language, preserving the same rank and the actual
target clocks. W7 identifies a concrete comparison that a completion must
handle. Neither an arbitrary new inverse prefix nor an output witness
obtained from another closure query can silently be declared lower-ranked.

## 7. Local replay

The new module passed Lean 4.34.1 with `-DwarningAsError=true`, against the
existing compiled PR180 dependencies. Its nine public theorem axiom
reports contain only the standard `propext`, `Classical.choice`, and
`Quot.sound` (some use fewer). No `sorryAx` or conjectural axiom is used.
The ordinary map and complete-source representations are unchanged.

This replay proves the displayed all-parameter interfaces and the exact
clock boundary. It does not turn the still-unproved dispatcher into a
universal theorem. Repository integrity and the integrated build remain
separate checks recorded by the parent checkpoint.
