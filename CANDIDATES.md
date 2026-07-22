# Candidate counterexamples

Last updated: 2026-07-22

There is currently **no candidate positive integer**, no regular sanctuary, and no finite symbolic construction proved to define an infinite positive-integer Collatz trajectory.

# Certificate boundary

A valid candidate must begin with one explicit finite positive integer and replay its unique deterministic Collatz trajectory forever. Compatible dyadic prefixes, a graph-directed completion point, positive pressure, or an unmarked expanding population are not candidate certificates.

Finite-state regular marked grammars belong to the exact regular-sanctuary program of PR #12 by `L-0015` and `T-0020`. The phase-34 tower route is genuinely different only because its block lengths and correction precision grow with scale.

# Available tower infrastructure

The negative eleven-cycle supplies four phase-34 self-return tower types. At height `t`, every type has

\[
K_t=11(t+1),
\qquad
G_t=7(t+1),
\]

and performs

\[
A_t+2^{K_t}h
\longmapsto
B_t+3^{G_t}h
\]

for every ordinary finite high tail `h`.

Every pair of instances has one canonical connector

\[
B+3^G\eta
=
\bar A+2^{\bar K}\theta,
\]

with

\[
0\le\eta<2^{\bar K},
\qquad
0\le\theta<3^G.
\]

Every finite schedule therefore has infinitely many ordinary realizations. Infinite closure remains the only relevant test.

# Connector control is finite-word computable

The following are now infrastructure rather than existential data:

- offset Montgomery precision lifting (`L-0026`);
- cycle-aligned Newton doubling (`L-0027`);
- exact connector compilation (`T-0025`);
- the padding-counter isometry (`T-0028`);
- adaptive 512-cell prefix routing (`T-0029`);
- the positive ordinary quadratic bulk generator (`T-0030`).

No infinite inverse-prefix word must be preloaded. Every required finite connector word can be generated from finite stage data.

# Corrected stage form

For one fixed corrected 256-transition stage at scale `m`,

\[
z^+
=
\frac{3^{A_m}z+C_m}{2^{D_m}},
\]

where

\[
A_m=\frac{5369}{2}2^m+1792,
\]

\[
D_m=\frac{1085579}{256}2^m+2816.
\]

Let `R_m` be the canonical correction and `S_m` the canonical cap. Every stage input is

\[
z=R_m+2^{D_m}Y_m
\]

and its output is

\[
z^+=S_m+3^{A_m}Y_m.
\]

# Major correction: the free quotient cannot survive

`L-0030` proves

\[
0\le S_m<3\,3^{A_m}.
\]

`T-0031` proves

\[
2^{D_{m+1}}>512\,3^{A_m}.
\]

Hence every valid ordinary stage transition satisfies

\[
\boxed{
0\le Y_{m+1}<\frac{Y_m+3}{512}.
}
\]

Every positive integer `Y_m` strictly decreases. Any ordinary infinite stage realization therefore reaches

\[
Y_m=0
\]

after finitely many scales.

The former preferred candidate—a growing self-feeding Montgomery quotient—is impossible in this coordinate. The raw stage remains supercritical, but its ordinary path must move along the canonical corrections themselves.

# Current preferred candidate format

A future candidate consists of:

1. a finite starting scale `m_0`;
2. one explicit finite stage word and canonical correction `R_(m_0)`;
3. one explicit marked positive Collatz integer entering that correction;
4. a total rule producing later stage words `w_m`;
5. exact late-stage stitching
   \[
   \boxed{S_m(w_m)=R_{m+1}(w_{m+1})};
   \]
6. exact expansion of every compressed stage into its 256 local connector blocks;
7. permanent positivity and avoidance of `1,2`.

After the quotient has vanished, the stage-boundary residuals are exactly

\[
z_m=R_m,
\qquad
z_{m+1}=S_m=R_{m+1}.
\]

No inverse-limit object is substituted for an ordinary marker.

# Shrinking-cusp constraint

Every late stitched correction must satisfy

\[
R_{m+1}=S_m<3\,3^{A_m}.
\]

Relative to its own modulus,

\[
\frac{R_{m+1}}{2^{D_{m+1}}}
<2^{-\Xi_m},
\]

where

\[
\Xi_m
=
\frac{22173699}{5248}2^m-rac{1106}{41}.
\]

Thus a candidate stage word must place its canonical correction inside an exponentially shrinking completion-height cusp at every sufficiently large scale.

# Constructive candidate architecture

A theorem-quality construction may use:

- the four phase-34 tower types as a finite alphabet;
- adaptive counter addresses to route low connector prefixes;
- finite Newton/Montgomery work tapes;
- occasional transitions through other negative-cycle phases;
- larger collision alphabets as rare repair stages;
- a nonregular substitution or pushdown directive for the stage words.

The output must prove exact cap-to-correction equality, not merely prefix agreement.

# Obstructive candidate audit

Before promoting any proposed directive, check whether another branch already excludes its complexity class:

- direct dyadic boundary directives: PR #33 `T-9702`;
- finite-state regular marked systems: PR #12 / `T-0020`;
- finite-state strictly causal feedback: issue #21 `T-9603`--`T-9604`;
- short eventually periodic stack directives: PR #20;
- finite high-tail libraries with affine counter rules: `T-0021`.

# Leading next experiments

## Exact stage correction search

Compute canonical pairs

\[
(R_m(w),S_m(w))
\]

by the incremental residue-block recurrence rather than one giant inverse. Search directly for

\[
S_m(w)=R_{m+1}(w').
\]

The search should expose:

- the new residue blocks;
- completion height;
- exact replay metadata;
- the marked physical boundary.

## Fixed-room transfer

After removing the fixed 256-cycle exponent cap, the normalized stage multiplier squares under scale doubling. Adapt PR #16's fixed-room past/future framework to the stage correction sequence.

## Completion-height lower bound

A uniform theorem keeping every late correction above

\[
3\,3^{A_{m-1}}
\]

would exclude this phase-34 stitching architecture completely.

# Routes not sufficient by themselves

The following are not candidates:

- arbitrarily long finite tower schedules;
- a nested counter address in `Z_2`;
- a growing local high tail without the next-stage correction;
- positive full-stage information surplus;
- a generated connector word with no physical residual membership;
- a finite-state marked grammar;
- a compact attractor;
- an ordinary quadratic work tape not embedded in the marked Collatz state.

# Non-negotiable candidate checks

A future `K-####` file must prove:

- one finite positive starting integer explicitly;
- exact agreement with every deterministic Collatz step;
- entry into the first stated canonical correction;
- total generation of every later stage word;
- exact cap-to-correction equality from some finite scale onward;
- exact local integrality inside every compressed stage;
- nonnegative ordinary values at every boundary;
- no substitution of a 2-adic completion for the marker;
- justified unboundedness or permanent avoidance of the terminal cycle.
