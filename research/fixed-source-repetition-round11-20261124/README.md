# Fixed-source repetition across changing return types

24 November 2026. Parent PR182 f94a2ae1caba9a1857feda892ee1779695eea9d2.
Status: written proofs, exact finite controls, Lean candidate pending compiler replay.
Full Collatz remains OPEN. No external review or new kernel check is claimed.

## 1. Repository synthesis and why this attack

The 30 latest updated PR metadata records were inspected. In particular the
following current heads and their stated boundaries were examined:

- #182 f94a2ae1caba9a1857feda892ee1779695eea9d2: actual scalar equivalence;
  GENERAL_PHASE_RETURN.md, ARITHMETIC_TOWER.md, RETURN_TOWER.md and
  ActualScalar.lean under research/carry-tower-round10-20261123;
  PHASE_RIGIDITY.md in round9 and GERM_BRIDGE.md in round8. These are the
  direct source inputs.
- #173 fa0c9e2a2851e6324391e39c17afcb5913185aec and #184
  366dab89ee9548084ab9b5e4e90ff82abf287a20: universal band entrances and
  merger consumers; no all-source smaller partner is supplied.
- #177 25bf9b95a9404998e8e55aa401773488cd3dd4b8: density-free germ criterion,
  full predecessor projection, and all-template bound; the germ construction
  and absolute moving-root mass are missing.
- #175 67664c6bf555bf7f7fcec987acb79500071dce4b and #185
  2ac1f63b5f8d51ab4b472307b52cc89c9ef6df9d: complete residual denominators
  and unconditional defect budget, not all-cycle exclusion.
- #178 398b3a04da071e96362005792417bd5cf8cc6497: full numerical gcd on
  a specified family, and arithmetic-germ criteria.
- #176 81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a, #180
  7cfd911d35382d9d3bc988060ba88ade78a4267e: actual source bounds and
  collision-law boundaries. Shannon entropy does not give the required
  tilted collision upper.
- #183 68345f60a4f757acb42a69a4ac95910f8ce26163: block compression and
  ordinary channels. Its fixed-word repetition rank is related, but our
  target is equal windows at two different starts, not a consecutive power.
- #146 f431078244e868dc699fad011044f0d5e7f76437 and #179
  27a2c7414fdb92eeca57ad552a9ab5c36d8430d8: physical five-closure and
  budget transfer. Their universal source construction is still absent.
- #186 1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493: literature machinery guide.

Except the direct #182 sources identified above, this is a metadata/body
orientation, not a full re-audit of the branch contents. The key target is
to retain one source while controlling multiple changing return types.
Round10 R10-A2 excluded rational realizations of the L/P bit-count scripts
only for caps k<=4 by a lacunarity comparison. The following argument
removes that restriction. It is based on the classical parity-cylinder
congruence, not a claim of priority for that congruence.

## 2. General fixed-source repetition theorem (R11-1)

Take a finite alphabet of distinct positive gap words, each with exactly
p odd steps. The complete affine equation of letter w is

    2^A_w x' = 3^p x + C_w,

where A_w is the sum of its positive gaps and C_w is the complete positive
integer carry. Put a=min_w A_w. Suppose lambda>1 dominates every multiplier
3^p/2^A_w, and choose C>=0 with

    C_w/2^A_w <= (lambda-1) C

for every letter. Such C exists, e.g. the maximum of these ratios.

Allow one fixed signed rational source q0 in Z_2, with odd denominator b>0.
A literal infinite realization means that the actual rational odd map
(with the exact valuation of the nonzero 3q+1) follows these words. Every
block-boundary state can be written q_j=x_j/b with odd integer x_j, since
the only divisions are exact powers of two in the numerator. Then

    Y_j=|x_j|+bC <= lambda^j Y_0.

This follows at one step by the triangle inequality and the chosen C.
No positivity of q_j is needed for this absolute-height bound.

Suppose two length-m blocks of letters starting at i<j are identical.
Their complete binary clock A is at least am and their full carries are
identical. Subtract the two full affine equations:

    2^A (x_(j+m)-x_(i+m)) = 3^(pm) (x_j-x_i).

The terminal numerators are odd; hence 2^(A+1) divides x_j-x_i because
3^(pm) is odd. If x_i != x_j,

    2^(am+1) <= |x_j-x_i| <= 2 lambda^j Y_0,
    and therefore 2^(am) <= lambda^j Y_0.                   (1)

If x_i=x_j, determinism of the literal odd map and the fixed common word
length p force the whole subsequent letter tails equal. Distinct alphabet
letters encode distinct p-gap words. Thus the script is eventually
periodic. This remains true for signed rational sources.

R11-1: every non-eventually-periodic script with a fixed rational
realization must satisfy (1) at EVERY repeated window.

This also gives a finite statement: whenever 2^(am)>lambda^j Y_0,
the two states coincide, so any explicitly exhibited later mismatch is
impossible. Both copies, all carries and the same original source remain
in the proof. No probability or independence is used.

## 3. Every bit-count cap, with an explicit finite rejection (R11-2)

Use the previous round's two words L=(2,1), P=(1,4):

    L(q)=(9q+7)/8,       P(q)=(9q+5)/32.
    a=3, lambda=9/8, C=7, p=2.

For each integer k>=1 let s_k(n)=1 if n>0 has at most k one-bits and 0
otherwise; bit 0 selects L, bit 1 selects P. In particular this is the
same family as R10-A3, not a newly defined script. Every infinite
symbolic script of L/P has discounted gap scalar 7/8 because each
two-gap charge is 7/9. Every finite prefix has a positive ordinary
realizer, by its parity cylinder.

Fix ANY rational candidate source a0/b in Z_2 (a0,b odd, b>0), including
negative values, and put Y=|a0|+7b. Choose a power of two H such that

    H >= 2^(k-1),        Y < 4^H.

For 0<=t<H, popcount(H+t)=popcount(2H+t)=1+popcount(t).
Consequently the two length-H windows at H and 2H are identical.
The upper height at the later start satisfies

    lambda^(2H) Y < (9/8)^(2H) 4^H = (81/16)^H < 8^H.

R11-1 forces x_H=x_(2H). But take u=2^(k-1)-1 < H and t=H+u.
Then H+t=2H+u has k one-bits and 2H+t=3H+u has k+1 one-bits.
The two labels are different. Both lie below 4H, contradicting
determinism if the prefix through 4H blocks is realized.

R11-2: NO signed rational 2-adic source realizes this infinite script
for ANY finite k>=1. In particular its unique physical 2-adic completion
is irrational, not just nonordinary. For B=bitlength(Y), take H as
the least power of two >= max(ceil(B/2),2^(k-1)).
The first actual mismatch is within 8H odd transitions, strictly less
than 16 max(ceil(B/2),2^(k-1)). This is linear in source numerator/denominator
bit-height for each fixed k. The proof needs neither the gap-ratio
threshold nor a p-adic transcendence theorem.

For signed rational candidates the statement is about literal rational
odd trajectories; the Lean file covers the finite natural-number core.
The conclusion for the unique physical completion follows from the
classical nested complete cylinders with increasing binary clocks, or
equivalently the inverse series in R10-A2.

## 4. Subword complexity and automata (R11-3)

Let P(m) count distinct length-m factors anywhere in the infinite script.
For a nonperiodic rational realization choose a repeated window among
the first P(m)+1 starting positions 0,...,P(m). By (1),

    P(m) >= (am log 2 - log Y_0)/log lambda.

In particular liminf P(m)/m >= a/log_2(lambda).
For L/P the coefficient is 3/log_2(9/8)=17.654847577...
For the actual round10 W/V pair at scalar 729/1456,

    W=(1,1,1,1,1,1,2,2,2,2,2,3)
    V=(1,1,1,1,1,1,1,5,2,2,2,3)
    W(q)=(531441q+700273)/524288
    V(q)=(531441q+1227505)/2097152,

take a=19, p=12, lambda=531441/524288, C=98. Both words have the
same discounted charge, as replacing (2,2) with (1,5) retains the
weighted two-term sum. The complexity coefficient rises to
19/log_2(531441/524288)=971.866577472...

A separate concrete consequence: let the script be generated by a
deterministic finite automaton with output, with K states, reading the
usual base-d expansion, most significant digit first, d>=2. Among the
states after reading positive integers 1,...,K+1, two agree, say i<j.
For every H=d^r, appending the padded r-digit representation of t gives
identical outputs at iH+t and jH+t for 0<=t<H. Thus (1) requires
2^(aH)<=lambda^((K+1)H)Y_0 if the script is not eventually periodic.
If lambda^(K+1)<2^a this fails for large r.

Hence every non-eventually-periodic script in that class has no rational
realization. In particular this excludes all non-eventually-periodic
automatic L/P scripts with K<=16, and W/V scripts with K<=970,
in ANY integer base. The integer thresholds follow respectively from
9^17<8^18 and 531441^971<524288^972 (the next powers fail).
The all-k result above does not need any bound on K.

Generalization: for p>=2 choose A=floor(log_2(3^p)), so p+1<=A<2p.
Construct a word W with A-p gaps two and 2p-A gaps one, beginning (2,1).
Replace that pair by (1,4) to obtain V. Both have p odd steps, equal
discounted charge, and clocks A and A+2. Every symbolic W/V script has
the same rational discounted scalar (charge divided by 1-3^-p).
Its canonical multiplier lambda=3^p/2^A belongs to (1,2), so
lambda^(K+1)<2^A holds for K<=p. This gives a family of arbitrarily large
finite-state exclusion thresholds. Taking lower approximants A/p to
log_2(3) with small positive error further enlarges the threshold.
It does not restrict general unconstrained carry scripts to this alphabet.

## 5. General critical-source complexity consequence (R11-4)

For any nonperiodic positive ordinary odd orbit, two equal length-m gap
windows yield a difference of sources divisible by 2^(A+1), where A>=m.
Thus if both starting states are below 2^m they cannot be distinct.
In particular, if the actual orbit satisfies log q_j=o(j), then for
every fixed real L>0, all states through floor(Lm) are below 2^m for
sufficiently large m. This follows by a uniform tail bound from the
definition of o(j), with the finitely many early states absorbed as m
increases. Their m-gap windows are pairwise distinct: the orbit is
injective since it is nonperiodic. Consequently

    P_gap(m)/m -> infinity.

An infinite gap alphabet already makes P_gap(m) infinite. If the
actual mean gap tends to log_2(3), the subexponential height hypothesis
follows from

    log q_j = log q_0 + j log 3 - (sum_{i<j}g_i) log 2
                  + sum_{i<j} log(1+1/(3q_i)).

Distinct positive ordinary q_i tend to infinity, so the final correction
is o(j) by Cesaro averaging. Thus no nonperiodic critical ordinary
gap itinerary has linear subword complexity. This is an exact,
same-source symbolic restriction, not an entropy or collision bound for
a limiting probability measure. It does not exclude superlinear
complexity or supercritical physical growth.

## 6. Remaining central obligation and literature boundary

This argument rules out a broad source-realization mechanism across
changing return types. It does NOT force repeated early windows for an
arbitrary ordinary orbit, imply arithmetic rationality of its actual
scalar, or exclude arbitrary periodic cycles. In fact arbitrary
binary scripts have the same formal scalar 7/8 in the L/P model;
finite symbolic complexity is not forced by that scalar alone.
They have arbitrary finite ordinary realizers. Controlling one fixed
source is precisely the missing condition.

Relevant independent literature lead (not imported as a theorem):
"Automatic, primitive, and nonprimitive parity in rational Collatz
dynamics", https://rstation.ai/problems/collatz/papers/16 (Oct 2026,
written candidate, varying review scope). Its automatic/primitive
results concern shortcut parity and rational realizations; this note
instead gives a short direct fixed-source argument for specific
equal-odd-length gap-block languages, including signed sources, and
explicit finite rejection clocks. No general automaticity or
transcendence claim is taken from that manuscript. The classical
congruence underlying R11-1 is well known; no historical priority
claim is made.

The next useful attack is to obtain a repetition-index bound at the
correct source-height scale for arbitrary paid words, not just a
constant-word rank or finite-state script. At critical drift a
linear-complexity bound would suffice to exclude escape, but the
repository has no such general bound. The separate full-denominator
cycle obligation remains.

## 7. Verification boundary

RepetitionWindow.lean is a proposed finite natural-number core (complete
carry cancellation, coprime divisibility, bounded-source equality,
finite equal-window/mismatch rejection). It has no sorry or custom axiom,
but it has NOT been compiled in this session: Lean and Lake are not
installed and network cloning is unavailable in the local execution
environment. Do not count its theorem declarations as kernel checked
until a strict replay and axiom audit succeed. The signed-rational,
automaton and infinite complexity consequences are written proofs.

repetition_controls.py was executed locally in normal Python and under
-O with byte-identical output. It uses explicit checks, not assert.
Observed output:
{"bit_caps": 12, "cap_replays": 48, "cap_symbols": 16448, "edges": 23064, "fixed_source_tests": 1548, "near_critical_constructions": 99, "paths": 3432, "repeated_windows": 53868, "scope": "finite exact arithmetic only"}

The controls include signed rational finite paths, both full affine
systems, exact binary divisors, explicit shifted mismatch for caps 1--12,
small fixed-source finite budgets, and 99 near-critical word pairs.
The general proof, not the finite enumeration, covers all k.
The replay does not demonstrate any universal orbit property.
