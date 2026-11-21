# Reverse ψ-closure: unbounded descent and a finite expansion budget

**Status: partial ordinary theorems checked by Lean; the complete
closure argument remains OPEN.** This lane attacks the actual remaining
closure implication from PR174 rather than treating its equivalence to
Collatz as a solution.

Source: PR174 at
7034109ed60a26bc49824e1ed43c239ceca81194,
research/psi-closure-20261121/lean/Collatz/Closure.lean,
especially OpenLemma, collatz_iff_open_lemma, the four fail_mod4
rules, and basin_pow_four_succ. The newer PR146 at
f431078244e868dc699fad011044f0d5e7f76437 was read for its
terminal and interval-synchronization interfaces. No claim from those
new analytical notes is an input to the new Lean file.

Let T be the ordinary shortcut map and C its basin of one. Write

\[
\operatorname{Fail}(m):=(m\notin C)\wedge(3m-1\in C).
\]

## P1. An unbounded descent with the complete ordinary profile

Suppose r,v,m,u are natural numbers and

\[
3m=4^{r+1}v+2,\qquad 2u=3^r v+1.
\]

These integral guards imply m>u>0. At the common clock L=2r+3,

\[
T^L(m)=u,\qquad T^L(3m-1)=3u-1.
\]

Both paths have exactly r+1 odd inputs. Consequently
Fail(m) is equivalent to Fail(u). In particular m cannot be the
least positive failure of this unrestricted reverse relation.

An explicit parameterization removes the integral guards:

\[
v=6t+1,\quad
m=2\,4^{r+1}t+\frac{4^{r+1}+2}{3},\quad
u=3^{r+1}t+\frac{3^r+1}{2},\qquad t,r\ge0.
\]

The source is even. Thus this is a different branch from PR174's
already-proved m=1 modulo4 return. Equivalently, it handles the
entire family whose valuation v2(3m-2) is positive and even. A
returned u generally does not lie in the progression27k+1; the
minimality theorem is explicitly over all positive reverse-failure
bases. It is not an induction confined to the restricted OpenLemma
progression.

The proof follows the exact source profile
0,1,(1,0)^r,0 and target profile (1,0)^(r+1),0.
The induction establishes the full endpoint/count identity for
4^r v+1, not just basin membership. All statements concern positive
ordinary inputs and arbitrary actual r.

Lean declarations in
[PsiDescent.lean](../lean/Closure/PsiDescent.lean):
power_four_profile, paired_descent, failure_descends,
not_minimal_failure.

## P2. Even the first balanced ψ-return can expand

The attempted completion was to prove that every first balanced return
to the same relation has smaller ordinary base. That statement is false.
For every t>=0, put

\[
m=2469887+4194304t,\qquad q=2816534+4782969t.
\]

Lean proves

\[
T^{22}(m)=q,\qquad T^{22}(3m-1)=3q-1,\qquad q>m.
\]

Both paths have exactly14 odd inputs, and there is no positive
balanced return before clock22 on any member of the entire cylinder.
The affine multiplier is

\[
\frac{3^{14}}{2^{22}}=\frac{4782969}{4194304}>1.
\]

This is a whole ordinary progression, not an unrealized symbolic word.
The base execution is checked by kernel reduction with decide.
The unbounded t-quantifier follows from the proved finite binary-lift
identity profile_lift; no compiler oracle or numerical approximation
is used.

The correction identity that exposed the example is

\[
B=6867833,\quad D=21192164,\quad
D-3B=3^{14}-2^{22}.
\]

An exact exploratory enumeration found these two words. The correctness
of P2 does not depend on the completeness of that search. Its Lean
declarations are expanding_return and expanding_first_return.

Thus a rank strictly increasing in the ordinary base, with this same
relation as its other fixed state, cannot decrease at every first
return. This does not exclude a certificate-length rank, orientation
changes, selected returns, or a different global argument.

## P3. Arbitrarily many guarded expansions can be repaid

The continuation in
[Oriented.lean](../lean/Closure/Oriented.lean) treats the expanding return as
one allowed block, then proves a composite descent for an unbounded number
of those blocks.

ExpansionStep(x,y) means that there is a natural t such that

\[
x=2469887+2^{22}t,\qquad y=2816534+3^{14}t.
\]

ExpansionChain(k,m,q) is exactly a sequence of k such guarded ordinary
returns, beginning at m and ending at q. Every block carries the actual
22-clock trajectories and both odd counts14 from P2. It is not an
arbitrary algebraic edge with the same multiplier.

Define the positive integer charge

\[
E(x)=588665x+6867833.
\]

Every block satisfies

\[
2^{22}y=3^{14}x+6867833,\qquad
2^{22}E(y)=3^{14}E(x).
\]

For every natural k,m,q with ExpansionChain(k,m,q), Lean proves

\[
(2^{22})^kE(q)=(3^{14})^kE(m),\qquad
(2^{22})^k\mid E(m),\qquad
(2^{22})^k\le E(m).
\]

The divisibility follows from the proved coprimality of the powers of
2 and3. Consequently a fixed ordinary m cannot begin arbitrarily long
consecutive runs of this expanding block. This is a finite-source
escape result for this block, independent of convergence.

The second estimate is

\[
3^k(q+12)\le4^k(m+12).
\]

Now take any natural k,r,v,m,q,u satisfying

\[
\operatorname{ExpansionChain}(k,m,q),\quad k\le r,\quad m\ge9,\quad
3q=4^{r+1}v+2,\quad2u=3^rv+1.
\]

The exit is precisely the ordinary P1 return, and r>=k is the explicit
payment guard. Lean proves

\[
8u\le3m+40,\qquad0<u<m,
\]

\[
T^{22k+2r+3}(m)=u,\qquad
T^{22k+2r+3}(3m-1)=3u-1.
\]

Both paths have exactly14k+r+1 odd inputs. The resulting theorem
charged_failure_descends gives

\[
0<u<m,\qquad\operatorname{Fail}(m)\iff\operatorname{Fail}(u).
\]

This permits arbitrarily many individually expanding blocks in a valid
descent proof. It does not require every individual return to decrease
the ordinary base.

As a concrete whole-cylinder instance, for every natural t,

\[
m=2469887+2^{29}t,\qquad
u=594113+3^{17}t
\]

satisfy the paired return at clock29, with17 odd inputs on each arm and
0<u<m. This is one expanding22-clock block followed by P1 with r=2.
In particular, the base expanding example m=2469887 descends to594113
through the exact composite itinerary.

Main declarations: expansion_chain_charge, expansion_chain_divisibility,
expansion_chain_budget, no_unbounded_expansion, expansion_chain_height,
charged_exit_bound, charged_paired_descent, charged_failure_descends,
repaid_expanding_cylinder.

## What is still being attacked

For m in the remaining even branch, the synchronized compression reaches
relations with offsets2,4,7 rather than returning directly to offset1.
The explicit expanding cylinder defeats the unrestricted rule that all
same-orientation first returns lower height, while P3 proves a valid
way to repay an unbounded run of that cylinder.

The missing implication is specific: leaving the expanding cylinder
does not yet give a P1 exit with r>=k. Its next base can have odd
valuation v2(3q-2), can be odd itself, or can have an even valuation
too small for the proved payment guard. Nor is there a proved common
integer charge that decreases across all the alternative offset and
orientation resets. Finite escape from one return cylinder is not
finite escape from the entire unresolved state space.

A known certificate on the member arm can still shorten across an
expanding return. But not every input has an adequate return before that
certificate ends, and the first member-arm layer already contains the
unproved powers-of-three convergence problem identified by PR174.
The next proposed attack allows swapped pairs (3u-1,u), literal
mergers, and the odd-valuation offset states, with a rank on their
combined relation state. No total well-founded grammar or closure
proof is asserted here.

## Actual Lean evidence

Both files were executed with Lean4.34.1:

    lake env lean -DwarningAsError=true Closure/PsiDescent.lean
    lake env lean -DwarningAsError=true Closure/Oriented.lean

Both executions exited zero. Printed axiom reports for the six main
declarations in each file use only propext, Classical.choice, and Quot.sound.
There is no sorry, native_decide, or added conjectural axiom.
The packet's publication receipts independently identify the actual
checkout and complete build.

Frozen SHA-256 for PsiDescent.lean:
536c35499a71a3cbb416fdbb6a2f5a30fae543c3361dd60048a32b22ab3b49f9.

Frozen SHA-256 for Oriented.lean:
af43f06c35bc960e255c9fccc66dc347ef125e6e53321b87cccc2404e22b523e.
