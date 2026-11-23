# Literature-driven attacks on the closing step

23 November 2026. **Full Collatz, the original residue-512 implication,
and `FloorIntervalStep` remain OPEN.** This continuation starts from
published PR177 head `aaa132e904e4e6d0b438e963f76d72d79e2c7f34`.
Three parallel attacks and a coordinating multiplier attack were directed
at the actual missing construction, ordinary escape mass, and complete
cycle denominator. The latest selected peer heads and primary-source
inspection scopes are recorded in the accompanying reports and lane notes.

The strongest positive deduction is a finite test for **exact equality to
the complementary point**, together with joint arrival at the standard
cycle. The new source-tail construction is explicit, but its exact
denominator proves that the whole family fails that test. A separate
ordinary renewal theorem constructs a Haar limit while retaining the
unknown ordinary endpoint, and quantifies the source reweighting cost.
The complete-cycle attack produces an exact certificate excluding one
specified universal local-energy proof mechanism.

## 1. A finite exact-recognition theorem

For a positive ordinary input n and a supplied signed triadic candidate
\(a/3^r\), define

\[
F(r)=\prod_{j<r}(1+3^j),\quad
B=n\max(1,|a|)F(r),\quad E=\operatorname{bl}(B),\quad H=9E+1.
\]

The [new written deduction](triadic/FINITE_DUAL_RECOGNITION.md) strengthens
the interpretation of PR176's finite test. If the first H complementary
parity tests pass, the actual paired orbit reaches

\[
\boxed{(n_J,a_J/3^{r_J})=(1,2)\quad\text{at some first-hit }J\le8E.}
\]

Consequently the supplied candidate is exactly \(\Omega(n)\). With the
complete complementary carry D_H and original even count b_H, the same
horizon gives a finite equivalence:

\[
\boxed{2^H\mid3^{b_H}a+3^rD_H
       \quad\Longleftrightarrow\quad a/3^r=\Omega(n).}
\]

The proof handles zero numerator before locating the first hit, keeps
unreduced presentations, and uses the remaining bits to force a small
integer residual to vanish. It decides equality for a given candidate;
there is no asserted bound on a search for one. This theorem is written
mathematics, not an additional Lean result.

## 2. The complete source witness gives a candidate, but no cancellation

The [source-tail construction](triadic/SOURCE_TAIL_TRANSPORT.md) computes
the dual \(u/3^s\) of any certified ordinary source x>2. If its first hit
uses A_0 shortcut clocks and p_0 odd inputs, its exact reduced exponent is

\[
s=A_0-p_0-1>0.
\]

For every actual target prefix K and every dyadic source lift t>=0,

\[
q_{K,t}=\frac{2^{K+t}(u+3^s)-3^{s+t}(2^K+D_K)}{3^{s+t+b_K}}
\]

has the required K complementary bits. Its numerator is a three-unit,
so the displayed denominator is exact. The general denominator-exhaustion
argument proves

\[
r>b_K\quad\Longrightarrow\quad
K<8\operatorname{bl}(n|a|F(r)).
\]

Thus this entire transplanted-source family fails the paid horizon, for
all K,t and every amount of terminal source padding. The only exceptional
actual terminal endpoints are 1 and 2; those reproduce the existing
boundary candidates, whose required height saving remains open.

[SourceTailPullback.lean](triadic/SourceTailPullback.lean) proves ten finite
construction and numerator-unit declarations. The source-denominator
interpretation, all-parameter horizon failure, and exact recognition
theorem retain their explicitly separate written-proof scope.

## 3. Ordinary conditional Haar with the endpoint still retained

The [renewal theorem](atomic/ORDINARY_RENEWAL_AND_RETAINED_ENDPOINT.md)
starts from the existing finite pressure probability on a hypothetical
escaping ordinary component. The symmetry S(n)=64n+21 preserves the
ordinary successor and gives the exact conditional law

\[
\mu(\,\cdot\mid v_2(3n+1)\ge6j+1)=(S^j)_*\mu,
\qquad \mu(v_2(3n+1)\ge6j+1)=64^{-sj}.
\]

On the explicitly enlarged full odd component, with its separately
normalized probability \(\mu^+\), the symmetry S_4(n)=4n+1 gives

\[
\boxed{\frac1J\sum_{j<J}(n\mapsto(S_4^jn,Un))_*\mu^+
       \Longrightarrow m_{\mathbb Z_3}\otimes U_*\mu^+.}
\]

This is full ternary Haar independent of the retained ordinary next state.
It follows from exact finite residue periods, without a higher-rank
rigidity assumption. The ordinary endpoint law stays present. The
valuation phase retains the identity \(u(3x+1)=q\), resolving the
discontinuity at the limiting binary pole.

For 1<s<2, the limiting ternary coordinate has a finite pressure Green
integral, but every finite cumulative conditioned average has infinite
Green integral. The note gives both limits exactly. It also proves an
arbitrary-weight lower bound: flattening residues at depth K by mixtures
of these symmetry powers requires an L^u density cost exponential in
\(3^K\), relative to the original ordinary pressure measure. These are
conditional written theorems; they neither assert an escaping component
exists nor eliminate one.

## 4. A direct complete-cycle invariant, and an exact dual obstruction

The [cycle attack](cycles/POSITIVE_CARRY_CLOSURE_ATTEMPT.md) retains the
whole denominator \(2^A-3^p\), the complete carry, and actual nonnegative
integer quotient data. It seeks a nearest-neighbor energy whose local
flux telescopes and whose source-to-zero gap is positive for every
primitive positive rational candidate word above the stated floor.

The accompanying integer certificate consists of 34 legal local
transitions, with total coefficient 40. Their exact sum forces

\[
2\delta_{11}+3\delta_{01}+3\delta_{10}\le0.
\]

The primitive words \(11101010(11011010)^{k-1}\) have precisely the
obstructed pair counts and all rational cycle states above 21. Their full
numerical gcd is also calculated, with no discarded denominator factors:

\[
D_k=256^k-243^k,\quad
C_k=319D_k/13-36\,243^{k-1},\quad
\gcd(D_k,C_k)=\begin{cases}13&k\equiv7\pmod{13},\\1&\text{otherwise}.
\end{cases}
\]

Every member is nonintegral. The result excludes the precisely stated
local monotonicity-and-universal-separation mechanism; it does not exclude
all local arguments with additional global integrality information, and
does not prove integer-cycle exclusion.

## 5. The multiplier bridge needs input-dependent ordinary clocks

The [coordinating attack](witness/MULTIPLIER_TRANSPORT.md) tests how the
global Applegate--Lagarias semigroup theorem might be lifted to ordinary
mergers. For a multiplier m having a divisor d>1 coprime to six,

\[
T^k(mn)=T^l(n),\quad k,l\le N\quad\Longrightarrow\quad n<6^N.
\]

Two new core Lean theorems prove this bound and the impossibility of a
uniform merger clock. They allow the actual words to vary with the source.
A finite menu of physical paths therefore cannot implement the wild prime
multipliers universally. The unbounded source-dependent compiler that
would be needed for the original question is not constructed here.

## Evidence and the remaining full-theorem step

The [execution and review report](../../../reports/lean-exact-witness-global-20261121/literature-closure/README.md)
separates the twelve newly audited finite Lean declarations, the written
theorems, and the exact finite carry certificate. No earlier research
corpus or large historical census was rerun. External literature appears
as named motivation or a precisely pinned interface, never as a new Lean
axiom.

The universal construction of a candidate passing its own finite horizon,
the exclusion of the unchanged ordinary escape component, and the
all-word numerical cycle divisibility contradiction remain unproved.
The original supplied tuple remains unrestricted, as does the length and
exponent size of any eventual output certificate.
