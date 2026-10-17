# L-0025 — Exact rational sandwich for the negative-eleven-cycle margin

Claim ID: `L-0025`  
Title: Integer-power certificates for every dyadic Hensel budget comparison  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: none  
Scope: the negative eleven-cycle multiplier \(3^7/2^{11}\)  
Related counterexample candidates: none

## Statement

Put

\[
\boxed{
\sigma=7\log_2 3-11.
}
\tag{1}

Then

\[
\boxed{
\frac5{53}<\sigma<\frac4{41}.
}
\tag{2}

Consequently:

### 1. Immediate high-tail budget at \(C=7\)

\[
\boxed{
\frac{11}{128}<\sigma.
}
\tag{3}

### 2. Two-connector residual budget at \(C=8\)

\[
\boxed{
\frac{5643}{65536}<\sigma.
}
\tag{4}

### 3. Failure of the \(C=7\) residual budget

\[
\boxed{
\sigma<\frac{22}{128}=rac{11}{64}.
}
\tag{5}

All sign claims in `T-0022`--`T-0024` can therefore be certified without decimal logarithms.

## Proof

Direct integer calculation gives

\[
3^{53}
=19383245667680019896796723
>
19342813113834066795298816
=2^{84}.
\tag{6}

Hence

\[
\log_2 3>rac{84}{53}.
\]

Multiplying by seven and subtracting eleven,

\[
\sigma
>
\frac{588}{53}-11
=
\frac5{53}.
\tag{7}

For the upper bound,

\[
3^{41}
=36472996377170786403
<
36893488147419103232
=2^{65}.
\tag{8}

Therefore

\[
\log_2 3<rac{65}{41}
\]

and

\[
\sigma
<
\frac{455}{41}-11
=
\frac4{41}.
\tag{9}

This proves (2).

For (3),

\[
\frac5{53}-\frac{11}{128}
=
\frac{57}{6784}>0.
\]

For (4),

\[
\frac5{53}-\frac{5643}{65536}
=
\frac{28601}{3473408}>0.
\]

For (5),

\[
\frac{11}{64}-\frac4{41}
=
\frac{195}{2624}>0.
\]

Combining with (2) proves every consequence. ∎

## Interpretation

The negative eleven-cycle provides only a narrow bit margin. The exact comparisons distinguish three different costs:

- one future connector costs at most \(11/128\) bits per unit tower height;
- two future connectors under the corrected schedule cost at most \(5643/65536\);
- two connectors under the faster 128-step lane cost \(11/64\).

The cycle margin lies strictly between the second and third costs. This is why the one-connector 128-stage precursor works, but true residual regeneration requires the 256-stage lane.

## Verification

`X-0012` evaluates both integer inequalities (6) and (8) and checks all rational comparisons exactly with `fractions.Fraction`.