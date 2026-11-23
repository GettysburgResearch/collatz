# Independent review of the critical generic-ray construction

Date: 23 November 2026. Reviewer: checkpoint18 cycle lane.

**Disposition: the written GR+ and GR- constructions and their stated scope
are valid at the hashes below.** This is a mathematical and checker-source
review, not a Lean certification, an ordinary-source construction, or an
independent verification of every earlier repository or literature claim.

## Frozen artifacts

| Artifact | SHA256 |
|---|---|
| `GENERIC_RAY_CONSTRUCTION.md` | `a6189cb6e635c234bab815fb26370763bc3c30f3a1e4acfc2a9369819a5c1e14` |
| `check_generic_ray_controls.py` | `bf52556e132647391f42dcc5fae9d8d8ec373f313fc9ff1dc73fc654bcf833e6` |
| `GENERIC_RAY_CONTROLS.json` | `37928c786559a419f43e43452969d9cf919ff70b7ae5dfb84d5637a5e57a4d3f` |

The complete written proof was read before the two final clarity edits to
Section 6. Those edits were then reread at the final proof hash above. The
complete checker source and its recorded output were also read. The output's
embedded proof and checker hashes agree with the actual files. The root
reports successful normal and `python -O` executions with identical output
at the recorded result hash; this reviewer did not add another execution.

## Mathematical checks

The countable probability-one input event is justified: each fixed finite
word can be treated by independent nonoverlapping blocks in each residue
class of starting positions, and there are only countably many finite
words. The strong law separately supplies the unbounded first moment.
Uniform sublinearity of the raw partial sums, and hence of the running
regulators, follows from splitting off a fixed initial segment.

The pressure estimate covers insertion clocks, not just raw endpoints.
In raw block n, the preceding positive endpoint is at least n cubed in
multiplier, and each inserted one increases it. Since every clock in that
block is eventually at most 2n, the claimed cubic lower bound follows.
For the negative regulator, inserted twos decrease the multiplier from
the preceding upper bound n to the power minus three. The first blocks
also establish the strict origin inequalities; there is no exceptional
positive clock left untreated.

For arbitrary output prefixes, the exact relation j=n+J and the bound
J<=I_(n+1), or its negative-regulator counterpart, give J=o(j). The
deletion estimate for length-r word counts is valid even with repeated
insertions and at prefix boundaries. The mean is proved from the exact
gap-sum identity, rather than incorrectly inferred from convergence of
finite cylinder frequencies. The bridge bound concerns the range after
subtracting the endpoint slope, not total variation.

The two real series are correctly distinguished. GR+ has finite inverse
series S and divergent reversed series R, with a strict forward pressure
minimum. GR- has finite R and divergent S, with a strict forward pressure
maximum. GR- does not satisfy GR+'s minimum hypothesis. Neither output
law is asserted to be the stationary iid law or a canonical harmonic
path law merely because its points have iid empirical frequencies.

## Nonatomicity and the single infinite source

Each output coordinate is determined by finitely many raw coordinates;
indeed the first j raw gaps already produce at least j output symbols.
Thus the output map is measurable. On the joint event that the output
equals a fixed b and at most delta*n insertions have occurred, the raw
n-prefix is among at most binomial(ceil((1+delta)n),n) subsequences of the
corresponding prefix of b. Each candidate prefix has iid probability at
most p^n, regardless of its compatibility with the insertion rule. The
union bound is therefore valid without any injectivity of that rule.

The regulator tail probability tends to zero; the binomial term has
strictly negative exponential rate for delta=1/10. The displayed integer
comparison 11^11<15^10 proves the needed entropy margin. This proves
absence of each individual atom; no simultaneous uniform bound over
uncountably many outputs is needed.

The 2-adic code is odd and satisfies the exact identity

\[
3X(b)+1=2^{b_1}X(\operatorname{shift}b).
\]

The odd tail makes b_1 the exact valuation. Repeated decoding proves
injectivity. Countability of the rational 2-adic sources then proves
almost-sure irrationality. This argument does not assume that rational
gap words are eventually periodic. The construction supplies one
consistent infinite nonordinary source for each output, rather than
switching finite witnesses.

## Finite ordinary realization

The congruence in (22) is sufficient for all prescribed valuations, not
merely for final integrality. To see the intermediate implication
explicitly, for i<L split the carry as

\[
C_L=3^{L-i}C_i+2^{B_i}C_{\mathrm{tail}},
\]

where the nonempty suffix carry is odd. The final numerator is divisible
by 2^(B_L), and B_L>=B_i+1. Reducing the split identity modulo
2^(B_i+1) therefore yields

\[
3^i n+C_i\equiv 2^{B_i}\pmod{2^{B_i+1}}.
\]

Thus every intermediate quotient is an odd integer. The modulus
2^(B_L+1) in (22) makes the final quotient odd as well. The one-step
affine equations now give each exact prescribed valuation.

Positive lifts preserve positivity. Each of the finitely many states is
an affine function of the source with positive slope, so all can be put
above any fixed floor. Distinct odd clocks have slopes 3^i/2^(B_i), which
are unequal by unique factorization. Each pair therefore forbids at most
one source value, so a sufficiently large lift avoids all repetitions.
The sources may change as the prefix grows; injectivity of the irrational
full code rules out a single ordinary source realizing all prefixes.

## Checker scope

The exact comparisons in `endpoint_ok` implement the two logarithmic
barriers without floating-point approximations. The nondecreasing
increment loop implements their running ceiling maxima, and checking the
preceding integer at each new record verifies minimality. The checker
also checks literal insertion positions, every interstitial pressure
inequality, the two exact first-moment identities, and the strict origin
condition.

The finite-realizer routine uses the full modulus 2^(total_gap+1), checks
every actual odd-step valuation, and verifies the complete affine
identity. Its initial source lift already puts every state above the
requested floor: the source is at least (floor+1)*2^(total_gap+1), while
each state's slope is at least 2^(-total_gap). The stated finite bound on
collision-avoidance attempts follows from the number of pairs of states.
The extra j=L term in the 2-adic truncation correctly records an odd tail
modulo that full modulus.

The rational arithmetic distinguishes the two series and separately
checks the forward affine identity with the inverse sum ending before
the current clock. The four damaged controls cover an incorrect inserted
symbol, an insufficient insertion count, a swapped sign, and an incorrect
ordinary realizer. Checks use explicit exceptions, so they remain active
under `python -O`.

The six finite cases do not certify the infinite probabilistic claims;
those follow from the written proof. In particular the reproducible 5/8
sampler is explicitly distinguished from the theorem's critical
irrational-parameter law. No extrapolation from the finite fixtures is
used in this review.

## Limits of this review

No issue requiring a mathematical correction remains in the frozen
construction. The earlier repository reductions, the primary Atkinson
source, the stationary theorem attributed to PR180, and the separate
ordinary-source insertion theorem were not independently reverified in
this review. The present proof does not need an imported conditioned-walk
theorem. It establishes the stated generic-ray boundary; it does not
exclude a positive integer cycle or prove ordinary integer recurrence.
