# Independent review: ordinary finite phase concentration and the triadic verifier

Reviewer: `source_surgery`, independent of the authors of the files reviewed.
Date: 23 November 2026.

**Verdict: PASS within the stated finite and fixed-input scopes.**
This review reconstructs the written arithmetic and reads every public Lean
statement. It also checks the source-level logic of the triadic verifier.
It does not claim a compiler execution or a run of the Python verifier;
the parent packet records those independent executions separately.

## Exact reviewed files

| File | SHA-256 |
|---|---|
| `research/literature-round4-20261123/ACTUAL_LAW_RIGIDITY.md` | `a57e7aef865315ef3471a25e0fee18de4d6db75cf40455a0d658912666783e08` |
| `research/literature-round4-20261123/ActualLawRigidity.lean` | `9248f4e4041d3241038fef6a64ed502b2ab203228345c3aec3e9c4e735d432b8` |
| `research/literature-round4-20261123/verify_triadic.py` | `0470da316c8e5cadb1c0b5a51452a5e9cfe2adcfb3f5b442f7cce2729fe48327` |

## 1. Complete gap words and the signed periodic comparison

For a positive gap word of length `d`, the recursive carry used in the Lean
file expands to the complete chronological sum in equation (1) of the note.
Splitting at a concatenation gives
`C(uv)=3^|v| C(u)+2^(sum u) C(v)`. Substituting a one-letter split and its
rotation gives exactly

\[
3b_j=\Delta+2^{g_j}b_{j+1},\qquad
\Delta=3^d-2^{A_v}>0.
\]

Thus the negative rational states `-b_j/Delta` obey the same scripted affine
edges. This is used only as a comparison identity. The constructed ordinary
states are separately proved positive; no negative rational cycle is passed
off as an ordinary positive one.

Subtracting the signed comparison from an actual edge and telescoping yields

\[
2^{a_j}(\Delta q_j+b_j)=3^j(\Delta p+b_0).
\]

Cancelling coprime powers gives both `3^j | Delta*q_j+b_j` and
`2^(a_j) | Delta*p+b_0`. Also `Delta` is odd and prime to three, because its
two defining powers are positive and have different prime support. The first
divisibility therefore gives the advertised residue at every precision
`3^m` once `j>=m`. The second, together with positivity of `Delta*p+b_0`,
gives the exact source lower bound. In particular the same positive source
cannot follow this expanding periodic script forever. The theorem does not
require a separate absence-of-positive-cycles assumption.

## 2. The CRT realization pays for the exact valuations

The source congruence is imposed modulo `2^(A_T+1)`, including the final odd
bit. Hence the final quotient is odd. At any earlier clock `i`, splitting
the complete carry cancels the remaining odd power of three and gives
integrality of the intermediate quotient. Reducing the same split modulo
two shows that quotient is odd: the remaining nonempty carry is odd, while
the remaining total gap is positive. This establishes every prescribed gap
as the exact valuation of `3q_i+1`, rather than only a divisibility lower
bound. Positive source and nonnegative carries establish positivity.

The extra congruence `p=1 mod 3` makes the initial source a ternary unit.
Every subsequent output is a ternary unit from its own exact edge equation.
The CRT modulus `3*2^(A_T+1)` is therefore sufficient for all claimed domain
conditions.

Two different observation clocks have distinct rational affine slopes:
otherwise a nontrivial power of three would equal a power of two. Each pair
of clocks consequently excludes at most one source. With
`B_T=T(T+1)/2`, any `B_T+1` consecutive admissible CRT lifts above the floor
contain a source avoiding all coincidences. The first lift is strictly below
`H+Q_T`, so the last is strictly below `H+(B_T+1)Q_T`, as stated. The
construction consequently supports uniform weights on genuinely distinct
ordinary states.

## 3. Block frequencies, warmup, and the carry controls

The full-alphabet Eulerian construction gives a cyclic order-`L` de Bruijn
word of length `d=B^L`. The number of starts with a prescribed mapped
length-`ell` gap word is
`B^(L-ell) product c_(u_i)`, which gives exactly the product probability
for every `ell<=L`. Cyclic rotation does not alter these counts.

Rotating at a largest prefix ratio makes every forward ratio `R_j<=1`.
Across a period boundary there is the extra factor `rho<1`; repeated
periods retain the bound. For arbitrary `i>=f`, writing both clocks by
period quotient and remainder proves `R_i/R_f<=K_v`. This controls every
present window, not just the initial one.

The chosen warmup `J=max(m,L)` has two separate purposes. It puts every
sampled endpoint beyond the ternary-lock precision `m`, and it supplies
all backward tested gap blocks through depth `L`. The full length
`T=J+N+L-1` supplies the forward tested blocks too, including the final
sample. Since `d|N`, there is no phase-frequency boundary error.

The correction identity `q_j=p/(R_j Lambda_j)` has the correct orientation.
Monotonicity of `Lambda` gives
`q_f/q_(f+i)<=R_(f+i)/R_f<=K_v`. Substitution in the complete carry gives
`C(w)/3^m=(1/3) sum R_(f+i)/R_f<=mK_v/3`. The separate multiplicative
correction lower bound follows from `q_i>=p` and
`log(1+u)<=u`; it does not replace this exact carry calculation.

## 4. The collision is an actual off-diagonal effect

After warmup, equal script phases have the same residue modulo `3^m`.
Each phase has empirical mass exactly `1/d`. Ordered same-phase pairs
therefore contribute `1/d`, even if some different phases have coincident
residues. All sampled ordinary states are distinct, so the ordinary
diagonal is exactly `1/N`; the unequal congruent-pair mass is at least
`1/d-1/N`.

For a fixed phase, the previous `m`-windows have the same complete word and
the same total gap and carry quotient. Distinct source states are congruent
modulo `2^A`, so their source quotients are distinct. The box diagonal sum
within the phase is `1/(dN)`, while its actual residue collision is `1/d^2`.
The factor `N/d` is retained by summing the box square roots before squaring.
Nothing in this calculation changes the empirical weights or erases
repeated words.

The fair `{1,2}` comparison is also exact. The last gap is recovered from
the endpoint residue modulo three, and its inverse affine step recovers
the preceding code modulo the next smaller power of three. Induction gives
injectivity of the `m`-gap ternary code, hence collision `2^(-m)` under a
genuinely iid fair word. The constructed finite law agrees with that word
law only through the prescribed depth `L`, and has phase collision at
least `2^(-L)`. The finite ordinary source changes with the requested
horizon, as the source divisibility bound requires. This does not furnish
an escaping source, a fixed-source time limit, or a canonical harmonic law.

## 5. Literature and formal boundary

I directly checked the relevant statements in the primary sources:

* [Hochman, Theorem 2.7](https://annals.math.princeton.edu/wp-content/uploads/annals-v180-n2-p07-p.pdf)
  assumes a small entropy increase under convolution of two measures. The
  note correctly retains the need to establish an actual convolution law
  before applying it to a dependent arithmetic process.
* [Eberhard–Varju, Theorem 1.1](https://arxiv.org/html/2003.08117v2)
  assumes independent identically distributed innovations and gives its
  entropy-controlled mixing conclusion for a proportion tending to one
  of admissible moduli, with an entropy threshold. The note correctly
  separates these hypotheses from a conclusion at every `3^m`.

The full-alphabet Eulerian construction was reconstructed directly above.
This review does not independently re-audit PR180's newest stationary-law
theorem; the finite construction does not use it as a premise.

The twelve public Lean statements retain the actual edge equations,
comparison equations, coprimality, and phase code as explicit hypotheses.
They prove the complete finite algebra, divisibility, source payment,
phase cardinality and weighted collision inequality, and affine coincidence
uniqueness. The note accurately leaves the Eulerian existence, CRT
selection, probability interpretation, and limiting comparisons in written
mathematics. I found no hidden infinite-orbit or iid premise in the formal
statements.

## 6. Source-level review of `verify_triadic.py`

The strict necessary bound is `tau<3(r+1)`. Starting with `orbit=[n]`, the
loop condition `len(orbit)<clock_bound` visits exactly the permitted clocks
`0,...,3(r+1)-1`, unless it reaches 1 earlier. A timeout rejects the supplied
denominator budget without making an assertion about later convergence.

At a found first hit of 1, the backward routine starts the dual at 2 and
uses the opposite inverse branch of every actual original step. The
comparison `a*dual.denominator == dual.numerator*3^r` is exact and accepts
unreduced presentations correctly. It also handles signed numerators and
rejects zero when it differs from the computed dual. At source 1 the loop
does nothing and compares with 2; at source 2 it reaches 1 in one step and
compares with 1. Input guards require integer data, a positive original
source, and a nonnegative denominator exponent.

The decision therefore uses both the finite original path and exact
backward equality. It does not substitute a short matching parity prefix,
and it does not claim a universal successful denominator selector. This
matches the written theorem interface in `TRIADIC_RIGIDITY.md`.

No remaining mathematical or source-level implementation correction is
requested for the bound file versions above.
