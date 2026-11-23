# Finite witness-clock normalization and the residual attack

**Status.** The normalization theorems in
[`lean/CollatzGlobal/AdaptiveDescent.lean`](lean/CollatzGlobal/AdaptiveDescent.lean)
and [`lean/CollatzGlobal/PsiNormalization.lean`](lean/CollatzGlobal/PsiNormalization.lean)
are checked by Lean 4.34.1 using its core library. The second file connects
the finite residual condition to the **full Collatz conjecture inside Lean**.
The residual closing statement is **OPEN**; its equivalence does not prove it.

We use the positive shortcut map `T(n)=n/2` on even inputs and
`T(n)=(3n+1)/2` on odd inputs. Write `orbit(n,t)=T^t(n)` and let
`oddCount(n,t)` count odd inputs before clock `t`. All sources and paths
below are ordinary natural integers. A supplied hit certificate is an exact
equality `orbit(n,d)=1`; `d` need not be the first hit.

## AD1. A total finite normalization of every supplied certificate

A balanced return at clock `t` means

\[
T^t(5n)=5T^t(n),\qquad p_{5n}(t)=p_n(t).
\]

The executable function `lastReturn(n,d)` scans the finite set
`{0,...,d}` and selects its last balanced return. Clock zero always qualifies.
Set

\[
\ell=\operatorname{lastReturn}(n,d),\qquad
q=T^\ell(n),\qquad e=d-\ell.
\]

Lean checks the following statements for every `n,d`, with the hit
hypothesis required only for the displayed hit certificate:

1. `0 <= ell <= d`, and `ell` is a balanced return.
2. If `T^d(n)=1`, then `T^e(q)=1`.
3. There is no balanced return of `q` at any clock `1 <= t <= e`.
4. `5n` reaches one if and only if `5q` reaches one.
5. Given an exact target certificate `T^a(5q)=1`, the compiler produces
   the exact ordinary certificate `T^(ell+a)(5n)=1`.
6. Applying normalization to `(q,e)` again returns `(q,e)`.
7. Every certified output `q` is odd, including the zero-clock output `q=1`.

The key identity is concatenation of actual paths and their odd counts:

\[
T^{s+t}(n)=T^t(T^s(n)),\qquad
p_n(s+t)=p_n(s)+p_{T^s(n)}(t).
\]

If the output had a positive return at `t <= e`, concatenating it with
the return at `ell` would give a later return at `ell+t <= d`, contradicting
the finite maximality of `ell`. This proves the residual property without
an infinite search. Target transport uses the same concatenation identity
and the actual equality `T^ell(5n)=5q`.

The rank for consuming any selected positive return is the **remaining
source certificate clock**: `d-t < d`. It is not the ordinary source value.
This allows expanding ordinary returns. The following instance is reduced
inside the Lean kernel:

\[
\begin{aligned}
T^{127}(19483)&=1,\\
T^{30}(19483)&=21091,\\
T^{30}(5\cdot19483)&=5\cdot21091,\\
p_{19483}(30)&=p_{5\cdot19483}(30)=19,\\
\operatorname{lastReturn}(19483,127)&=30.
\end{aligned}
\]

Thus the value increases from `19483` to `21091` while the supplied
certificate clock falls from `127` to `97`. Both sources are odd ternary
units. The normalization uses the actual finite orbit; it does not infer
legality from a completed binary code or from a random input.

The primitive-recursive implementation scans finite clocks directly. No
uniform clock bound, oracle for all-time terminal membership, or target
convergence certificate is used to select its output.

## AD2. The exact residual theorem needed by this compiler

Define the finite predicate

\[
\operatorname{FiniteResidual}(n,d):
\quad \forall t\in\{1,\ldots,d\},\quad
\text{there is no balanced return at }t.
\]

The remaining statement is

\[
\boxed{\forall n,d,\quad T^d(n)=1\ \land\
\operatorname{FiniteResidual}(n,d)
\quad\Longrightarrow\quad 5n\in C.}
\tag{RF}
\]

The Lean theorem `five_closure_iff_finite_residual` proves that (RF) is
equivalent to unrestricted forward-five closure `n in C => 5n in C`.
The reverse direction runs AD1 on a supplied witness for `n in C` and
then transports the residual target certificate back to `5n`.

This file does not import a Lean proof of the separate global
forward-five-to-Collatz criterion. It formalizes the complete normalization
of the five-closure problem. Any use of that separate criterion must retain
its own source and verification boundary.

The residual class is nonempty even at one odd input: Lean checks
`T^4(5)=1` and `FiniteResidual(5,4)`. Here the target also converges, but
the residual predicate by itself does not contain its certificate.
The compiler therefore returns a precise unresolved mathematical question,
not a spurious failure or a guessed convergence proof.

## PN1. A finite normalizer connected to full Collatz inside Lean

The same construction works on the ordinary pair `(3m-1,m)`, whose first
arm has a supplied hit certificate. Define a numerical relation return by

\[
T^t(3m-1)=3T^t(m)-1.
\]

For this pointwise finite algorithm the odd counts need not match. Let
`ell=lastPsiReturn(m,d)` be the last such return through the supplied
clock `d`, and put `q=T^ell(m)`, `e=d-ell`. Lean proves

\[
q>0,\qquad T^e(3q-1)=1,\qquad
m\in C\Longleftrightarrow q\in C,
\]

and that the residual pair has no positive relation return through `e`.
The last return strictly precedes the source hit: otherwise
`1=3*T^d(m)-1`, impossible for a positive ordinary integer. Hence `e>0`.
Every target certificate `T^a(q)=1` compiles to the actual certificate
`T^(ell+a)(m)=1`.

Write `FinitePsiResidual(m,d)` for the finite no-return predicate. The exact
remaining global statement is

\[
\boxed{\forall m,d,\quad m>0,\quad 3\nmid m,\quad T^d(3m-1)=1,\quad
\operatorname{FinitePsiResidual}(m,d)
\quad\Longrightarrow\quad m\in C.}
\tag{PRF}
\]

The theorem `collatz_iff_finite_psi_residual` proves in Lean that (PRF) is
equivalent to convergence of **every positive ordinary integer**. For the
nontrivial direction it normalizes a supplied source certificate for each
input to PR174's `OpenLemma` and invokes the credited, kernel-checked
PR146/PR174 reverse criterion. Thus the global link here has no additional
paper-only five-closure dependency. The initial target `27k+1` is a ternary
unit, and Lean proves that every ordinary shortcut step preserves that
property. The normalized target is therefore a ternary unit as well;
the closing hypothesis need not cover multiples of three.

The predicate remains nonvacuous at the first source layer. Lean checks
`T^5(32)=1` and `FinitePsiResidual(11,5)`, with `3*11-1=32`. The primitive-recursive scan
terminates for every supplied input; the mathematical assertion that its
residual target always converges is precisely (PRF), not a property inferred
from termination of the scan.

### An expanding psi family admitted by the common rank

`PsiExpansion.lean` proves an unrestricted affine family of actual
ordinary relation returns. For every natural `h`, define

\[
m_h=106495+2^{52}h,\qquad r_h=131455+3^{33}h.
\]

Both seed arms have `33` odd steps through clock `52`, so exact high-bit
lifting proves

\[
T^{52}(m_h)=r_h,\qquad
T^{52}(3m_h-1)=3r_h-1,\qquad
m_h<r_h,\qquad r_h200^{52}<m_h201^{52}.
\]

Thus this entire family increases the ordinary value while passing the
strict common-rank guard. The kernel also verifies
`T^196(319484)=1` for the seed source `319484=3*106495-1`; the child source
`394364` consequently has a supplied certificate at clock `144`.
For general `h`, source convergence remains an explicit supplied
certificate hypothesis. The family proves a return and a strict rank
comparison, not convergence of every lifted source. Inputs with
`h mod 3 != 2` are ternary units.

These are psi goals, exactly the goal type of the conjugated
negative-reference rules in `COMMON_RANK.md`. Therefore the common rank
handles demonstrated ordinary growth and clock growth within the same
comparison problem; the five-goal example is no longer the sole
expanding-value illustration.

## How this uses the latest work

- PR174, `7034109ed60a26bc49824e1ed43c239ceca81194`,
  `research/psi-closure-20261121/lean/Collatz/Closure.lean`, supplies the
  imported ordinary basin definitions and elementary equivalences, through
  the credited PR146 core source. Its `OpenLemma`, powers-of-three first
  layer, and shadow laws remain separate routes.
- PR146, `f431078244e868dc699fad011044f0d5e7f76437`,
  `research/upper-bit-mergers/FIVE_RETURN_CLOCK_AND_TERMINALS.md`, proves
  the paper-level all-time terminal reduction using an effective deadline
  after the first source hit. The present finite-certificate normalization
  needs neither that deadline nor all-time terminal recognition. It does
  not claim to supersede its stronger all-time terminal classification.
- At the same PR146 head, `WHOLE_INTERVAL_SYNCHRONIZATION.md` constructs
  large blocks associated with a fixed failed comparison. That construction
  does not prove (RF). The supplied ordinary source and its finite hit
  certificate are retained throughout our normalization.
- Concurrent PR176, `bff01093f3eb073216f9ec610130d16067fcc1fd`,
  `research/lean-global-resolvent-20261121/lean/Collatz/TerminalFive.lean`,
  formalizes existence of a source-clock-minimal **failed** comparison
  whose every strict successor has a convergent fivefold multiple. It
  excludes even asynchronous proportional returns at that failure. Its
  minimality hypothesis concerns actual nonmembership of the target and
  quantifies over all smaller source certificates. The present normalizer
  instead computes from any supplied finite source certificate without
  deciding nonmembership. Neither residual class is silently substituted
  for the other.

This contribution is an executable formal normalization of the entire
supplied-source domain, including expanding returns. It is not a claim
that last-return reduction as a mathematical idea originated here.

## Closing attempts and the exact steps they did not supply

### 1. Consume all balanced returns, then induct on the witness clock

The positive part is now implemented: every successful call strictly
lowers the supplied clock, and the total finite normalization computes its
terminal result. The missing step is (RF). Calling the normalization
again cannot help: idempotence is proved. The ordinary rank-one terminal
families in the frozen PR146 source already survive the balanced-return
architecture, so shorter source certificates alone do not force coverage.

### 2. Combine witness-clock descent with decreasing-parameter templates

The prior negative-reference templates decrease their ordinary parameter
while some increase the supplied source clock. Our expanding-return example
decreases the clock while increasing the ordinary value. Neither
lexicographic ordering of just these two coordinates decreases on both
classes of moves. This prompted the positive synthesis in
[`COMMON_RANK.md`](COMMON_RANK.md): the proper rank
`P(n,d)=(n+1)(201/200)^d`, with explicit strict guards, handles all eight
negative-reference rows and the displayed expanding psi family. Its
well-foundedness is proved in Lean. Exact seven/six-step conjugation puts
the negative-reference rows into the same psi goal type as numerical
psi returns. Universal coverage by these guarded moves remains unproved.

The simple inverse of the displayed return emphasizes the issue: the
valid path transports a source certificate from `(21091,97)` back to
`(19483,127)`, reversing the clock decrease. Allowing all sound
bidirectional transports permits a two-step loop. Soundness of each move
does not give termination of arbitrary switching. This is a limitation of
that unguarded scheduling argument; the strict common-rank guard rejects
the inverse of an admitted return.

### 3. Replace balanced returns by asynchronous numerical returns

At one ordinary point, unequal clocks can be useful: the source `5`
reaches `4` at clock two, while its target `25` reaches `20=5*4` at
clock ten. This gives a valid numerical transport outside the
equal-clock language. It does not define a whole-cylinder identity.

For fixed source and target parity words of lengths `t,u`, let
`L=max(t,u)`. If the ratio-five endpoint equality holds for two ordinary
inputs differing by `2^L` on those same words, subtraction of the two
exact affine equalities gives

\[
3^{p_Y}2^{L-u}=3^{p_X}2^{L-t}.
\]

Unique factorization forces `u=t` and `p_Y=p_X`. Thus a genuinely
asynchronous numerical return is isolated within that fixed pair of
binary cylinders. This elementary observation is written reasoning here,
not a named Lean theorem. The attempted closing construction still needs
a total rule selecting valid numerical transports for every residual;
finite examples do not supply one.

### 4. Induct on the convergent arm in the ψ route

PR174 already identifies its first layer with convergence of every power
of three. Transporting an arbitrary convergent-arm witness changes the
affine offset and may increase its exponent. The shadow equality when
that arm reaches one is compatible with a larger unresolved partner.
No inequality or common rank obtained in this pass eliminates that
partner. Treating this first layer as a base case would assume an unproved
infinite family. PN1 makes the finite residual interface executable and
formalizes its complete global consequence, while leaving this actual
closing obligation visible.

There is a positive, differently scoped discharge of the entire first
layer. If `3m=2*4^(i+1)+1`, then `3^i<m`, for every exponent `i`.
The theorem `jacobsthal_closed_under_ordinary_floor` combines this exact
inequality with PR174's `basin_jacobsthal` equivalence: under the explicit
hypothesis that every positive integer smaller than `m` converges, `m`
converges too. Thus this layer cannot contain a globally least ordinary
counterexample. Minimality of the source witness clock or of the new
common rank does not supply that ordinary floor, so the lemma cannot be
used as an unconditional residual base rule.

The full conjecture remains open. The next theorem is (PRF), or a genuinely
terminating extension that handles its finite residuals with actual
ordinary certificates. The five-comparison branch separately targets (RF).
