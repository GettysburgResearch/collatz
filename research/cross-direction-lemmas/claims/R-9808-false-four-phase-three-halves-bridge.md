# R-9808 -- The four-phase `3/2` bridge for `81/64` is arithmetically invalid

Claim ID: `R-9808`
Title: The identity underlying PR16/L-9312 is false, so its fixed four-phase schedule is not established
Status: `PROPOSED`
Authoring agent: `gpt56-synthesis-01`
Reviewing agents: `gpt56-synthesis-01-wave13-survivor-twohot`
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: branch-qualified `PR16/T-9315` only for naming the centered `81/64` variables; the refutation itself is elementary
Scope: the fourth-power decomposition and schedule asserted in `PR16/L-9312`, plus claims that explicitly depend on that schedule
Refuted route: embedding the centered `81/64` powers as every fourth point of one full `3/2` orbit
Related counterexample candidates: none

## Refuted assertion

`PR16/L-9312/(7)` asserts

\[
{81\over64}=\left({3\over2}\right)^4
\tag{1}
\]

and, after defining

\[
Y_m=\xi\left({3\over2}\right)^m,
\tag{2}
\]

uses (1) to identify

\[
Y_{4n+r}
={3^r\over2^r}(B_n+u_n),
\qquad
\xi\left({81\over64}\right)^n=B_n+u_n.
\tag{3}
\]

That identification is false. Consequently the fixed radii and centers in
`L-9312/(10)--(13)` do not follow from the centered `81/64` hypothesis.

This refutes the displayed bridge and every proof step which imports its
four-phase schedule. It does **not** prove that the centered `81/64`
condition has a solution or has no solution.

## Theorem 1 -- there is no pure `3/2` sampling identity

There is no integer `k>=1` for which

\[
\left({3\over2}\right)^k={81\over64}.
\tag{4}
\]

In particular, `k=4` gives

\[
\boxed{
\left({3\over2}\right)^4={81\over16}\neq{81\over64}.
}
\tag{5}
\]

### Proof

Unique factorization applied to (4) would give

\[
3^k2^{-k}=3^4 2^{-6}.
\tag{6}
\]

The exponent of `3` forces `k=4`, while the exponent of `2` forces `k=6`.
No integer satisfies both equations. Direct substitution gives (5).
**QED**

## Theorem 2 -- the missing factor grows exponentially

For the variables in (2)--(3), the exact relation is

\[
\boxed{
Y_{4n+r}
=4^n{3^r\over2^r}(B_n+u_n),
\qquad 0\le r<4.
}
\tag{7}
\]

Thus the error inherited from the centered decomposition is

\[
\boxed{
4^n{3^r\over2^r}u_n,
}
\tag{8}
\]

not `(3/2)^r u_n`. Even under

\[
|u_n|<{1\over81},
\tag{9}
\]

the transported upper bound is

\[
\left|4^n{3^r\over2^r}u_n\right|
<{4^n(3/2)^r\over81},
\tag{10}
\]

which is not one of the fixed radii

\[
{1\over81},\quad {1\over54},\quad {1\over36},
\quad {1\over24}
\tag{11}
\]

claimed uniformly in `n` by `L-9312`.

### Proof

The exact ratio between the two bases is

\[
\left({3\over2}\right)^4
={81\over16}
=4{81\over64}.
\tag{12}
\]

Therefore

\[
\begin{aligned}
Y_{4n+r}
&=\xi\left({3\over2}\right)^{4n+r}\\
&=4^n{3^r\over2^r}
 \xi\left({81\over64}\right)^n,
\end{aligned}
\tag{13}
\]

and substitution of `B_n+u_n` proves (7)--(8). Equation (10) is the direct
consequence of (9). **QED**

## Corollary -- the scheduled-center proof also changes

The integer part in (7) is

\[
4^n{3^r\over2^r}B_n.
\tag{14}
\]

It is not the center `(3^r/2^r)B_n` used in `L-9312/(14)`. For example,
once `2n>=r`, the factor `4^n/2^r` is integral, so (14) has center zero
modulo one for every integer `B_n`; this is incompatible with treating the
three fixed residues `0,15,49 mod64` as producing the same phase centers at
every `n` by the displayed argument.

This does not show that no other scheduled representation exists. It shows
that the particular four-phase schedule in `L-9312` is not obtained from
the variables which the file defines.

## The correct multiplicative accounting

The ratio `81/64` has four factors of `3` and six factors of `2`:

\[
{81\over64}=3^4 2^{-6}.
\tag{15}
\]

It can be represented by a six-step mixed schedule containing four steps of
multiplier `3/2` and two steps of multiplier `1/2`, in any fixed order:

\[
\boxed{
\left({3\over2}\right)^4
\left({1\over2}\right)^2
={81\over64}.
}
\tag{16}
\]

Such a schedule is not a full orbit of the single multiplier `3/2`. Its
phase centers and error radii depend on the chosen order of the six mixed
steps and must be derived anew. In particular, no theorem about all powers
of `3/2` can be imported through (16) without proving an additional bridge.

## Dependency propagation audit

At the PR-16 head fetched for this audit,
`1bb8c6b9fa7df170a59b6f6658d0150c16628f13`, the false identity or its
four-phase conclusion appears in the following places.  The cited schedule
passages are unchanged from source commit `fac3cc4` (the aggregate claim
ledger has since received unrelated additions):

- `research/adelic-cusp/claims/L-9312-four-phase-three-halves-schedule.md`:
  equations (7)--(14) and the stated theorem;
- `research/adelic-cusp/CENTERED_LITERATURE_AUDIT.md`: the claimed bridge to
  the `3/2` literature;
- `research/adelic-cusp/CENTERED_POWER.md`: the four-phase summary;
- `reports/gpt56-pro-04/2026-07-22-15-centered-power-equivalence.md`: the
  schedule report;
- `research/adelic-cusp/claims/R-9303-real-cylinder-emptiness.md`: wording
  which treats `L-9312` as an exact geometric presentation;
- `research/adelic-cusp/claims/Q-9303-centered-cylinder-nonstabilization.md`
  and the branch claim ledger: dependency summaries which include `L-9312`.
- `experiments/X-9304-centered-power-replay/README.md`, `run.py`, and the
  frozen result metadata: the advertised "four-phase schedule" checks use
  the locally restarted points
  `xi*(81/64)^n*(3/2)^r`.  Those finite local checks are arithmetically valid,
  but they do not check the claimed single orbit `Y_(4n+r)` and therefore do
  not validate the bridge.

The following pieces are not refuted by the arithmetic above:

- the centered `81/64` equivalence in `T-9315`, which uses the base
  `beta=81/64` directly;
- the three-state residue table `B_n mod64 in {0,15,49}`, which follows from
  the nearest-integer recurrence without using (1);
- the full symbolic centered-error recurrence in `L-9313`;
- the exact nearest-cylinder block arithmetic in `L-9314`, after removing
  its descriptive cross-reference to the false schedule;
- the centered reconstruction, carry, sign, and residue checks in `X-9304`;
  only their interpretation as a replay of one full `3/2` orbit is rejected;
- `T-9316` and `T-9317`, provided their proofs use `beta=81/64` directly and
  do not invoke `L-9312`.

Each survivor in this list still requires its own dependency audit; absence
from the refutation is not independent verification.

## What this advances

- It prevents a false transfer from the centered `81/64` frontier to
  Mahler/Dubickas theorems about the full `3/2` orbit.
- It isolates a possible repair: derive a genuine six-phase mixed
  `{3/2,1/2}` schedule, or remain entirely in the direct `81/64` recurrence.
- It preserves the valid nearest-integer residue and cylinder work rather
  than discarding the entire PR #16 direction.

## Gap and scope audit

- A false proof identity is enough to reject the submitted proof of
  `L-9312`; it is not, by itself, a counterexample to the conditional
  schedule statement if the centered hypothesis happens to be empty.
- No claim is made here that a different implication to some scheduled
  family is impossible.
- Equation (16) is only multiplicative bookkeeping. It does not supply the
  missing mixed-state theorem.
- The refutation does not decide `Q-9303`, the threshold equality in
  `T-9317`, or the Collatz conjecture.

## Adversarial checks

- Decimal values agree with the prime-factor calculation:
  `81/64=1.265625`, while `(3/2)^4=5.0625`.
- At `n=0`, the missing factor `4^n` equals one, which can conceal the error
  in a single-block check. Any replay must include `n>=1`.
- At `n=1,r=0`, equation (7) gives
  `Y_4=4(B_1+u_1)`, not `B_1+u_1`.
- The residue table modulo `64` precedes the false fourth-power
  decomposition and does not depend on it.

## Remaining uncertainty

Can a carefully ordered six-phase mixed schedule connect a published
forbidden-region theorem to the direct `81/64` threshold? No such source
match or phase-state proof is currently present.

## Suggested next attack

Keep `beta=81/64` as the primary base. If a literature transfer through
`3/2` is still desired, choose one explicit word containing four `3/2`
steps and two `1/2` steps, derive all six centers and radii from the
nearest-integer recurrence, and verify that the cited theorem actually
covers that nonautonomous mixed schedule.
