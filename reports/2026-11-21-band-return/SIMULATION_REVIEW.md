# Focused semantic review: ordinary marked simulation

**Review date:** 2026-11-21 UTC

**Reviewer:** `global_forcing`, separate from the simulation author
**Outcome:** PASS for the stated finite ordinary simulation and its documented scope.

## Reviewed artifacts

The final versions below were read from disk for this review.

| Artifact | SHA256 |
|---|---|
| `research/band-return-20261121/lean/BandSimulation.lean` | `92f4c26480cb907a774f4910b44f34cd04b2326d44b3e783f24d89e437699988` |
| `research/band-return-20261121/JOINING_ATTEMPT.md` | `047425cda73b74ce1618b9b2a7376d7ca42f40acdae15ee8630760200de64f34` |

This was a focused semantic review of ordinary positivity, markedness,
arbitrary finite horizon/precision/height, odd-prefix legality, and the
changing-source quantifier. It was not a new audit of the pinned PR173
dependency or a replay of experiments. The author reported a successful
strict Lean compilation in 5.03 seconds after two arithmetic proof fixes;
the main theorem statement did not change. This review did not repeat that
compiler run.

## 1. The witness is a positive ordinary integer

The construction is

\[
 D=2^m,\qquad b=D-m,\qquad
 n_m=2^b(2^m+1)-1=2^D+2^b-1.
\]

`buffered_seed_bounds` places it in the ordinary dyadic interval
\(2^D\le n_m<2^{D+1}\). In particular it is positive and its binary
depth is exactly \(D\). The inequalities \(m<2^m\) and positivity of
the displayed products justify the natural-number subtractions used in
the exact identities. There is no substitution of a negative or completed
2-adic input for this ordinary witness.

## 2. The actual marked-set guard is satisfied

The source is odd because \(b>0\). The proof retains the actual offset
from \(2^D\) and obtains

\[
 (D+1)(n_m-2^D)\le2\,2^D\le70\,2^D.
\]

Thus `buffered_seed_marked` proves the same marked predicate used by the
imported forward-section theorem. It even fits the narrower constant-two
bound; no enlarged or replacement section is used.

## 3. Horizon, precision, and height are simultaneously arbitrary

For any natural horizon \(L\), positive precision \(K\), and natural
height floor \(M\), the theorem chooses

\[
 m=M+L+K+2.
\]

The bound \(2m\le2^m\) gives \(b=2^m-m\ge L+K\), while the dyadic
lower bound gives \(M<n_m\). The credited ordinary rising-prefix theorem
then gives, for every \(0\le j\le L\),

\[
 T^j(n_m)+1=3^j2^{b-j}(2^m+1),
 \qquad T^j(n_m)\ge n_m,
 \qquad 2^K\mid T^j(n_m)+1.
\]

The divisibility claim is the exact finite congruence to \(-1\) modulo
\(2^K\). Since \(K>0\), every one of these states is odd, including
both endpoints of each of the first \(L\) steps. Those steps are therefore
ordinary odd shortcut steps with exactly one division by two, and also
successive steps of the odd-only map. The theorem states that every prefix
state is at least the source; oddness also makes the displayed finite
trajectory increasing. No behavior after this supplied horizon is asserted.

## 4. The changing-source quantifier is retained

The proved order of quantifiers is

\[
 \forall L,K,M\ (K>0)\quad
 \exists n>M\quad
 \forall j\le L:\ \text{the stated ordinary prefix properties hold}.
\]

The source depends on all three parameters. Neither the Lean statement nor
the reviewed note replaces this by one positive integer satisfying every
horizon and precision. The distinction is essential: as the precision
increases, these changing sources can approach \(-1\) in the 2-adic
topology while escaping to infinity in ordinary size. That limiting point
is outside the positive ordinary starting domain.

The note's finite empirical-law discussion is consistent with this
quantifier. All finite prefixes stay above the selected height floor,
so the finite Fourier error bound is uniform enough to let the horizon
and floor grow together. Concentration in increasingly precise \(-1\)
cylinders and a uniform leading-phase marginal can therefore describe a
limit obtained from different sources. This discussion does not supply
one infinite ordinary counterexample, and the Lean simulation theorem
does not claim a formal measure-convergence theorem.

## 5. The stationary law is used within its actual scope

For the limiting odd 2-adic update, \(z=-1\) satisfies
\(3z+1=-2\), has valuation one, and maps back to \(-1\). Circle
translation preserves uniform measure. Hence

\[
 \mathrm{Haar}(\mathbb R/\mathbb Z)\times\delta_{-1}
\]

is an invariant law with a uniform leading-phase marginal and formal
height drift \(\log_2 3-1>0\). The note explicitly identifies it as a
limiting stationary law, not a positive ordinary orbit or a Collatz
counterexample. It correctly uses this example to test an inference from
stationarity and phase marginals to halving statistics. It does not infer
ordinary divergence from the stationary law.

The remaining need to control the integer halving cocycle for a fixed
ordinary source is stated explicitly. Nontrivial periodic behavior is
also kept separate from the injective-orbit Fourier theorem.

## 6. Wording and final disposition

The earlier wording concern is resolved: Section 1 now says an orbit
**“that is not eventually periodic”** has distinct states. This is the
correct deterministic implication; merely not being periodic from time
zero would not suffice.

No remaining semantic correction was identified within the requested
scope. The finite ordinary construction, the marked predicate, and the
documented limitation of the real/2-adic law agree with the reviewed
theorem statements. This review supplies no full Collatz closure claim.
