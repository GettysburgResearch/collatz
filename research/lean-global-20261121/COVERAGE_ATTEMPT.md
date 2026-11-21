# Common rank: an infinite uncovered family in the same psi goal

**Outcome:** the common numerical rank is well-founded and supports the
specified forward and negative-reference moves. The proposed union of those
moves is not a complete certificate procedure. The exact infinite family
below has a complete source certificate, admits no same-goal forward return
within that certificate, and fails every one of the eight negative-template
guards. `Coverage.lean` and `PsiCoverage.lean` formalize these coverage facts.
No statement here calls an uncovered source a Collatz counterexample.

The parameter family itself is credited to the earlier rank-five work
(PR163 and its uses in PR168/PR172). The new result is its complete
same-goal coverage obstruction for the combined common-rank procedure.

## 1. The bridge between the goals is retained exactly

A psi goal at `(m,d)` supplies an ordinary certificate

\[
 T^d(3m-1)=1
\]

and asks for a certificate for `m`. The rank is the actual source score

\[
 P_\psi(m,d)=3m(201/200)^d.
\]

For `m=27M+1`, the binary source `128M+1` reaches `3m-1=81M+2`
in seven shortcut clocks, and its target `64M+1` reaches `m` in six.
The packet's `PsiTemplateBridge.lean` formalizes this ordinary bridge.
Thus the negative templates really can be expressed in the same psi goal;
their clock increment is still `+a` after conjugation.

The two proposed move classes are:

1. A same-goal forward return at `0<t<=d`, satisfying
   `T^t(3m-1)=3T^t(m)-1`, sends the goal to
   `(T^t(m),d-t)`. The common-rank guard further requires
   `T^t(m) * 200^t < m * 201^t`.
2. A negative-reference rule on `m=27M+1` sends
   `M` to `(2^a M+c)/3^b` and changes the source clock to `d+a`.
   Each of the eight supplied rows requires `M=-1 mod2048`, in addition
   to its own ternary, positivity, and physical-prefix guards.

For the negative rules, `27c+3^b<2^a` and
`402^a<200^a*3^b` prove the strict common-score decrease. This is a
substantive positive compatibility result. It does not assert that a rule
is available at each goal.

## 2. A whole infinite certified family has no positive psi return

Put

\[
 e=119+162j,\quad W=2^e,\quad
 M=(8W-22)/243,\quad m=27M+1=(8W-13)/9.
\]

The ordinary source is

\[
 S=3m-1=8(W-2)/3.
\]

Its first four steps are halvings, reaching `(W-2)/6`, an odd number.
The next step reaches `W/4=2^(e-2)`, followed by `e-2` halvings to one.
Thus the source has the complete certificate clock

\[
 d=e+3.
\]

The target's first three steps are exactly

\[
 m\longmapsto(4W-5)/3\longmapsto2W-2\longmapsto W-1.
\]

It then follows `e` rising odd steps:

\[
 T^{3+u}(m)=3^u2^{e-u}-1\qquad(0\le u\le e).
\]

Let `S_t=T^t(S)` and `R_t=T^t(m)`. The early comparisons are

| Clock | Exact target/source relation |
|---|---|
| 1 | `R_1=S_1+1` |
| 2 | `R_2=3S_2+2` |
| 3 | `R_3=3S_3+1` |
| 4 | `R_4=9S_4+2` |

For every `5<=t<=e+3`,

\[
 S_t=2^{e+3-t},\qquad R_t=3^{t-3}S_t-1>S_t.
\]

Consequently `R_t>S_t>0` at **every** positive clock through the
supplied source certificate. The required psi-return equality
`S_t=3R_t-1` is impossible. This excludes all same-goal forward
returns, so a choice of a different return or a different score guard
cannot help within this witness window.

The source reaches one at the displayed clock; the formulas also show
that its earlier values exceed one. The Lean statement proves the complete
certificate and all positive-return exclusions. It does not assume or
establish convergence of the target `m`.

### Kernel-checked family and integrality

`singular_psi_residual` uses the integral equations

\[
 3m=16q+1,\qquad 3q+1=16\,2^a,
\]

and proves the source certificate at clock `a+8` together with the
finite residual property. Taking `a=e-5` gives the family above.
`rank_five_psi_residual` obtains these equations directly from
`243M+22=8*2^e`, with `e>=5`.

To include the entire exponent progression without relying on an
unstated divisibility claim, `hardParameter` is defined by the exact
integer recurrence

\[
 M_0=(8\,2^{119}-22)/243,\qquad
 M_{j+1}=2^{162}M_j+22(2^{162}-1)/243.
\]

Only the two fixed constants require evaluation. Lean checks both exact
integer identities and then proves

\[
 243M_j+22=8\,2^{119+162j},\qquad j<M_j
\]

by induction. `hard_psi_family` packages cofinality, the complete ordinary
source certificate, the residual property, and the failed negative guard.

## 3. The whole negative-reference catalog misses the same family

Reducing `243M+22=8*2^e` modulo four gives

\[
 M=2\pmod4.
\]

This is incompatible with `M=-1 mod2048`. Therefore none of the eight
negative-reference transformations applies, independently of the ternary
residue, the supplied certificate length, or the value of the common rank.
This exact arithmetic statement is `rank_five_parameter_misses_negative_guard`.

The obstruction is not merely a finite search failure or a poor constant:
there are arbitrarily large ordinary, eligible, certified residual sources
on which **both proposed same-goal move classes have no accepted step**.
The theorem concerns forward returns within the supplied clock. Looking
arbitrarily far beyond that clock, or adding another asymmetric template,
would be a different rule requiring its own termination and coverage proof.

## 4. A least ordinary failure floor cannot be substituted for the new rank

The common potential also changes what a minimal-counterexample argument
is allowed to assume. A smaller ordinary source may have a longer canonical
source certificate and a larger score. This issue is present even without
artificially padding a witness.

`Coverage.lean` checks the exact first-hit certificates

\[
 d(1153)=96,\qquad d(1281)=36,
\]

where these are binary sources `128*9+1` and `128*10+1`. Nevertheless

\[
 1154\,201^{60}>1282\,200^{60},
\]

so the smaller source has the larger potential. After the seven-clock
bridge the same issue occurs directly in the psi source chart:

\[
 d(731)=89,\qquad d(812)=29,\qquad
 732\,201^{60}>813\,200^{60}.
\]

The first-hit assertions quantify over every earlier clock using finite
`Fin` types; the comparisons use exact integer powers. They are ordinary
kernel-checked calculations.

Thus a proof choosing the least score cannot automatically reuse an older
result whose hypothesis is the least ordinary reverse failure. For example,
PR172's smaller-five construction uses the specific least-source conclusion
`176106 r<X => r in C`. That premise provides convergence, but no bound on
the resulting first-hit clock that would make its query smaller in the new
score. A successful use of that route here must retain its original
least-source hypothesis or establish the needed score-controlled query
certificates separately.

## 5. The actual next closing statement

The rank proof resolves how the admitted move types can terminate together.
The remaining obligation is a **typed coverage theorem**: for every supplied
psi source certificate, provide either a target certificate or a sound
finite set of smaller-score psi queries. The family in Sections 2–3 proves
that the current two move classes do not meet this specification.

An additional transformation must first handle these residuals and then
all other possible source certificates. Solving the displayed rank-five
family alone would not establish universal coverage. This pass supplies no
complete new transformation and no full Collatz proof.

### Dependencies and verification scope

- The exact negative-template rows and arbitrary-witness splicing are the
  frozen PR168 result at `e4599b32e4b1a955ac9315d46782d4ad6a5db96c`,
  `research/closure-frontier-20261121/NEGATIVE_TEMPLATE_GRAMMAR.md`.
  The current packet formalizes the new rank and psi conjugation; it does
  not relabel that earlier paper proof as newly formalized template legality.
- The previously constructed smaller-five conditional bridge was inspected
  at PR172 `b22d94240f3d44a04231508e5dfe9a4947a57125`,
  `research/global-certificate-closure-20261121/SMALLER_FIVE_FAILURES.md`,
  specifically its same-least-source hypotheses and source certificates.
- `Coverage.lean` and `PsiCoverage.lean` prove the new statements described
  above. Their compilation and public axiom audits are recorded in the
  publishing packet. No conjectural closing premise is introduced as an axiom.
