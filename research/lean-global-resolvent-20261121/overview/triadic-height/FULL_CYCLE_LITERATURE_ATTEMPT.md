# Full numerical cancellation: the attempted literature bridge

Date: 2026-11-23. **Unclosed direct attack. No new cycle census or
unrestricted cycle-exclusion theorem.**

The source refresh used PR182 at
`b78819e95ee7d39f02022de991b42217821e7590`,
`research/closure-round2-20261123/CYCLE_CANCELLATION.md`, and PR185 at
`2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d`,
`research/central-closure-20261123/PRIMITIVE_DENOMINATOR_GROWTH.md`
and `PRINCIPAL_FIBER_CONTROL.md`.

For a length-A binary word with p ones at positions d_i, keep the
complete quantities

\[
D=2^A-3^p>0,\qquad
C(w)=\sum_{i=0}^{p-1}2^{d_i}3^{p-1-i}.
\]

The desired statement remains that D cannot divide C(w) for a
nontrivial primitive positive integer-cycle word. Polynomial denominator
growth does not bound the quotient after the numerical evaluation gcd.
The source control already absorbs the full principal component at the
correct evaluation, so a principal-factor witness is insufficient.

## The direct additive-combinatorial attack

Let N_0(A,p) count all words in this fixed length/weight class with
C(w)=0 modulo D. A primitive nontrivial cycle of length A contributes
A distinct rotations to this same zero fibre. Consequently the
pointwise estimate N_0(A,p)<A would exclude that candidate. This is the
existing zero-fibre target, not a new equivalence or theorem.

The attempted new step was to use all cyclic placements together with
the many independent local swaps in a word to prove this pointwise
bound. Each disjoint swap supplies an additive 2,3-unit generator modulo
the **same** D. However, cyclic rotations of a zero word preserve the
same divisibility condition; they do not provide independent congruence
events. For several swaps the displacement is a signed sum of units,
whose divisibility by D is not excluded by the individual unit facts.
The whole-fibre local packing estimates in PR182 already stop here.

Tao's primary 2011 discussion treats precisely these dependent simplices
and their large additive cubes. Its Propositions 6 and 7 run in the
direction *cycle exclusion implies separation of powers of two and
three*. The discussion after Proposition 7 explicitly does not derive
avoidance of the single residue zero from a distribution estimate:
<https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/>.

Breuillard--Varju's primary *Cut-off phenomenon for the ax+b Markov
chain over a finite field* studies a fixed multiplier and independent
identically distributed additive increments over a prime field. The
abstract and opening setup of the primary PDF were read:
<https://ora.ox.ac.uk/objects/uuid%3Ad49495ed-7750-48f1-844e-76eb91a6910b/files/s2f75rb26g>.
Those hypotheses do not produce the conditioned fixed-weight carry
law at the intrinsic A-step clock, modulo the entire potentially
composite D. Its strongest cited cutoff statement also has almost-all
prime/parameter qualifiers and a Dedekind-zeta hypothesis. Even granting
that hypothesis would not remove the law, modulus and pointwise-target
mismatches. No GRH premise is used in this checkpoint.

**First missing line:** a uniform pointwise estimate for this exact
complete carry law, strong enough to give fewer than A zero words.
Replacing the law, retaining one prime factor, assuming independent
cyclic rotations, or passing from typical moduli to this D does not
prove that estimate. No such estimate was obtained in this pass.

## The extremal-word alternative

The parallel proposal was to optimize an actual ordinary ancestor at
one common root and then invoke balanced-word/high-cycle rigidity.
`OPTIMAL_ANCESTOR_BALANCE.md` independently checks the valid optimizer
continuation and gives an exact obstruction to that bridge: source 31
is an unrestricted all-depth coefficient optimizer for each target in
31,47,71,107,161,121,91, while its six-gap word is unbalanced. A separate
three-gap example shows that a balancing move exits the integer fibre.
These controls are actual convergent trajectories, not hypothetical
counterexamples. They identify which new infinite or arithmetic premise
would have to be supplied before the extremal literature could close
the problem.

The complete denominator and the actual ordinary source were retained
throughout. This pass supplies no claim that a nontrivial integer cycle
has been excluded.
