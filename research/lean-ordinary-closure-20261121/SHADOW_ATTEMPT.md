# Global ψ-closure attempt: certificate shadows and an exact escape macro

## Outcome

This attempt did **not** prove the PR174 `OpenLemma`, convergence of every
power of three, or the Collatz conjecture. It did produce a Lean-checked,
executable macro that skips every consecutive traversal of the expanding
signed −5 cycle. Its termination proof uses a decreasing arithmetic
coordinate even while the ordinary orbit increases. The unresolved task is
to supply a rank that decreases across successive macro exits.

The file `NegativeFiveEscape.lean` imports the unchanged PR174
`Collatz.Closure` foundation. All assertions below about that file are
theorems checked by Lean 4.34.1; no `sorry`, custom axiom, convergence
assumption, or bounded search is used in its general theorems.

## Why the known arm's finite certificate is not yet a global rank

The attempted global construction starts from the PR174 signed shadow

\[
n=3^k m-c,
\]

where the ordinary integer \(m\) has a known finite path to one. The two
shadow transition laws in `Collatz.Shadow` allow the two ordinary paths to
be synchronized while the coefficient exponent remains nonnegative.

Consuming that known certificate is a genuine finite process. However, its
terminal states need not solve the target arm: once \(m=1\), the target can
still be

\[
n=3^k-c,\qquad 0\le c<3^k.
\]

The first-layer Jacobsthal construction already present in PR174 includes
the terminal cases \(c=0\) for every exponent \(k\). In that construction,
the known arm \(3m-1\) is a power of two, and PR174 proves that the desired
target membership is equivalent to \(3^k\) converging. Thus a
lexicographic induction headed by the known certificate's remaining
length requires an additional theorem at certificate length zero. It
cannot assign that base case for free.

Continuing the known arm through its \(1\to2\to1\) cycle does not make the
coefficient exponent monotone. For example, if \(c\) is even and

\[
c'=(3c+3^k-1)/2
\]

is odd, two synchronized clocks produce

\[
(k,c)\longmapsto
\left(k+1,\frac{9c+3^{k+1}-5}{4}\right).
\]

The target has then followed its ordinary two-clock word. An ordinal
candidate must justify this increase using another decreasing component.
The consumed known certificate supplies no such component at this stage.

Nor should the desired terminal condition be stated as \(k=0\): the
already-converged target \(n=1\) has all representations
\((k,c)=(k,3^k-1)\), and its synchronized two-clock loop keeps \(k\)
unchanged. A successful measure has to recognize this whole terminal
surface.

These calculations identify the missing part of this particular attempt;
they are not an impossibility theorem for all ordinal or certificate
methods.

## A total arithmetic macro for the expanding −5 shadow

The signed shortcut cycle

\[
-5\to-7\to-10\to-5
\]

gives the following exact **positive ordinary** path for every \(z>0\):

\[
8z-5\to12z-7\to18z-10\to9z-5.
\]

Induction on the number of blocks proves the literal-clock identity

\[
\boxed{T^{3r}(8^r z-5)=9^r z-5}\qquad(r\ge0,\ z>0).
\]

This is `negative_five_run` in Lean. The clock is the ordinary shortcut
clock, not an accelerated odd-step counter.

For an arbitrary positive input \(n\), factor

\[
n+5=8^r z,\qquad z>0,\quad8\nmid z,
\]

by repeatedly dividing the defect \(n+5\) by eight. The executable
function `stripEight` uses structural well-founded recursion on this
decreasing defect. The `escape` function returns

\[
\operatorname{escape}(n)=(3r,9^r z-5).
\]

The theorem `escape_spec` proves all of the following for every positive
input:

- The algorithm terminates.
- The reported endpoint is exactly the reported ordinary iterate.
- The endpoint is positive.
- Its residue modulo eight is not three, so the current −5 block run is
  maximal.
- The endpoint is in the ordinary basin exactly when the input is.

This uses a well-founded coordinate to skip arbitrarily long upward
runs. It makes no claim that the next run has a smaller coordinate.

## The exact remaining obstruction

Ordinary numerical size is not that missing global coordinate. The
Lean-checked instance

\[
\operatorname{escape}(262139)=(18,531436),
\qquad T(531436)=265718>262139
\]

shows that completing the entire expanding run and taking its first
post-exit halving need not restore descent.

For a power-of-three input, the same construction has

\[
z=\frac{3^k+5}{8^r},\qquad
T^{3r}(3^k)=9^r z-5.
\]

The quotient \(z\) is an ordinary integer with an arithmetic relation to
\(k\), not another established pure-power target. No proof obtained here
turns that quotient into a lower exponent or controls all subsequent
exits. Treating this transformation as convergence of all powers of
three would be the first unsupported step.

## Verification

From the shared PR174-compatible Lean project, the following command
completed successfully with no output:

```sh
/workspace/scratch/46eba7b29f50/lean-4.34.1-linux/bin/lake env lean \
  /workspace/scratch/46eba7b29f50/agent-psi-global/NegativeFiveEscape.lean
```

The general path and exit theorems are induction proofs. The one
explicit non-descent example is reduced by the Lean kernel using
`simp`; it is not substituted for an unbounded assertion.
