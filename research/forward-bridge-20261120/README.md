# What permanently survives the balanced-prefix filter

**PROPOSED, unconditional.** The Collatz conjecture remains open. This packet
classifies an entire sector of the permanent ordinary representatives in the
prefix filter of [PR #146](https://github.com/GettysburgResearch/collatz/pull/146),
frozen at `92820dd336b010215eb8a6eb4878a31b58a67656`. It does not prove that the
unresolved upper-bit pairs merge.

Use the shortcut map `T(n)=n/2` for even `n` and `T(n)=(3n+1)/2` for odd `n`.
For a positive integer that reaches 1, let

\[
 g(n)=2q(n)-\tau(n),
\]

where `tau` is the first-arrival shortcut clock and `q` its odd-input count.
The expression is unchanged by continuing around `1 -> 2 -> 1`.

The exact results are:

1. Two starts in the basin of 1 eventually have the same endpoint **and the
   same odd count at one common clock** exactly when their grades `g` agree.
   Consequently a convergent start `x=1+3w` is retained as a least representative
   at every eligible prefix depth precisely when it is the least `1 mod 3`
   integer in its grade class.
2. Every convergent non-power of two obeys the sharp gap
   `n * 2^g(n) >= 5/4`. Equality holds exactly for `n=5*2^j`, `j>=0`.
3. The permanent convergent representatives with nonpositive grade are
   **exactly**

   \[
   \{4^m:m\ge0\}\ \cup\ \{10\,4^m:m\ge0\}\ \cup\ \{7\}.
   \]

4. Taken together, all eligible upper-bit merger obligations based at this
   classified sector are equivalent to convergence of the same two families
   already isolated in PR #146:
   `3^a+1` for `a>=1`, and `3^a+2` for `a>=2`.
   The added representatives introduce no further infinite family of
   obligations. The finite exceptional upper arms are checked explicitly.

The grade itself is an elementary branch-count invariant. PR #145 already
studies both branch counts and balanced coalescence in
[CLOCK_CHARACTERS.md](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/profinite-orbit-averages/CLOCK_CHARACTERS.md).
No novelty is claimed for retaining branch counts. The contribution here is
the exact connection to permanent representatives, the sharp gap with its
equality classification, and the resulting complete nonpositive-grade sector.

Read [the proof](PROOF.md). Run
`python -B research/forward-bridge-20261120/check.py` for the finite exact replay.
The proof is not inferred from this bounded computation.

## Why this matters, and where it stops

Permanent survival in the prefix filter is not evidence of forward
nontermination: the complete sector above consists of known convergent
integers. The filter retains an exact integer invariant, not merely the
two phases of the eventual cycle. Allowing a one-step clock lag after reaching
the cycle removes the phase distinction, but does **not** preserve the
equal-slope identity on arbitrary higher binary lifts; the latter needs the
odd-count condition as well.

The statement gives a precise search boundary. Positive-grade minima remain
outside this classification. So do ordinary starts whose convergence has not
been established, because `g` is defined using a finite arrival at 1. Finite
depth representatives can also disappear later. None of these sets is proved
empty. In particular the convergence of the two shifted-power families is
still open here, and no argument in this packet passes from sparse
representatives to a complete terminating merger procedure.
