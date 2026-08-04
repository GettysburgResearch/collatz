# Iteration 13: the global blocker is ordinary extraction, not another amplifier

All theorem-level claims remain `PROPOSED` pending independent reconstruction.
This iteration deliberately introduces no new encoding and no bounded experiment.
It isolates the one inference that the positive H program has repeatedly lacked,
proves the exact valid replacement, and gives an H-native countermodel to the
invalid compactness-plus-expansion inference.

Frozen cross-program context:

```text
PR #19 H frontier:                  e805dde4275daaef78ad74dbf1e469710481958e
PR #38 global cartography pass 5:   f49501b7ec0f79b83890f1485180141c51cc8206
PR #56 global extraction audit:     e42d12e8a9859a917d91870c2490cc1eb87b040f
PR #57 ordinary-extraction packet:  553fabe56bb30b91b789affe017c6813a72273f1
```

The conclusions below are proved natively for the H exact-block system.  They
agree with, and specialize, the repository-wide stabilization theorems in PRs
#56--#57.

Retain the exact H block maps

\[
 p^+=a_rp+1,
 \qquad
 a_r={3^{2r+1}\over2^{3r+2}},
 \qquad r\ge0,
\tag{1}
\]

on positive exact states `p>=16`, with

\[
 p=2^{3r+2}u,
 \qquad u\equiv1\pmod4,
 \qquad p\equiv1\pmod3.
\tag{2}
\]

For a finite exact word `w`, write its positive cylinder as

\[
 \mathcal C(w)=\Pi(w)+3\,2^{E_w+2}\mathbf Z_{\ge0}.
\tag{3}
\]

Every finite word has a nonempty cylinder, but that fact alone is not an
ordinary infinite-orbit theorem.

---

## T-9520: architecture-level ordinary extraction

**Claim ID:** `T-9520`  
**Title:** A fixed H architecture has an ordinary survivor exactly when its least roots stay bounded  
**Status:** `PROPOSED`  
**Dependencies:** `L-9502`; determinism of the exact H map  
**Scope:** every fixed prefix-closed class of H block itineraries

### Definitions

Let

\[
 \mathscr A=\bigsqcup_{L\ge0}\mathscr A_L
\tag{4}
\]

be a prefix-closed family of finite H words.  It may be the full H language, a
fixed finite-alphabet subsystem, one renewal machine, one macro grammar, or one
prescribed infinite itinerary and all its prefixes.

Let

\[
 S_L(\mathscr A)=
 \left\{
 p\in\mathbf Z_{\ge16}:
 \text{the first }L\text{ exact block letters of }p
 \text{ form a word in }\mathscr A_L
 \right\}.
\tag{5}
\]

If `S_L` is nonempty, put

\[
 m_L(\mathscr A)=\min S_L(\mathscr A);
\tag{6}
\]

and otherwise put `m_L=+infinity`.

### Statement

The sets are nested,

\[
 S_{L+1}(\mathscr A)\subseteq S_L(\mathscr A),
\tag{7}
\]

and the following are equivalent:

\[
\boxed{
\begin{aligned}
&\bigcap_{L\ge0}S_L(\mathscr A)\ne\varnothing;\\
&\sup_L m_L(\mathscr A)<\infty;\\
&m_L(\mathscr A)\text{ is eventually constant.}
\end{aligned}}
\tag{8}
\]

When these conditions hold, the eventual value

\[
 P=\lim_Lm_L(\mathscr A)
\tag{9}
\]

is itself one positive ordinary seed whose complete deterministic itinerary
lies in `mathscr A`.

If every finite level is nonempty but no ordinary survivor exists, then

\[
\boxed{m_L(\mathscr A)\longrightarrow+\infty.}
\tag{10}
\]

### Proof

Prefix closure and determinism give (7).  Hence the extended-integer sequence
`m_L` is nondecreasing.

If `P` lies in every `S_L`, then `m_L<=P` for every `L`, so the minima are
bounded.

Conversely, a bounded nondecreasing sequence of positive integers is eventually
constant, say `m_L=P` for `L>=L_0`.  By definition of the minimum, `P` belongs
to every `S_L` with `L>=L_0`; nestedness then puts it in all earlier `S_L` as
well.  Thus `P` lies in the intersection.  This proves (8)--(10).  QED.

### Fixed-itinerary specialization

For one infinite word `r=(r_0,r_1,...)`, take `mathscr A_L` to contain only its
length-`L` prefix.  Then

\[
 m_L(\mathscr A)=\Pi(r_0,\ldots,r_{L-1}).
\tag{11}
\]

Thus the unique `2`-adic ghost is a nonnegative ordinary integer exactly when
the least representatives stay bounded, equivalently when the appended carry
blocks are eventually zero.  This is the valid inference replacing

```text
for every L there exists a positive seed P_L
    therefore one positive seed works for every L.
```

The displayed implication is false; equation (8) gives the missing uniformity
condition.

---

## L-9531: an H-native supercritical ghost family

**Claim ID:** `L-9531`  
**Title:** Constant expanding H itineraries have positive finite shadows but negative nonordinary infinite ghosts  
**Status:** `PROPOSED`  
**Dependencies:** `D-9501`, `L-9502`  
**Scope:** constant block itineraries `r^infinity`, `r>=3`

### Statement

Fix `r>=3` and put

\[
 U=2^{3r+2},
 \qquad
 V=3^{2r+1}.
\tag{12}
\]

Then `V>U`, every finite word `r^L` has infinitely many positive exact ordinary
realizations, and every such finite orbit strictly increases at every step.
The unique infinite exact `2`-adic realization is

\[
\boxed{
 g_r=-{U\over V-U}
 =-{2^{3r+2}\over3^{2r+1}-2^{3r+2}}.
}
\tag{13}
\]

It satisfies the exact fixed equation

\[
 {V\over U}g_r+1=g_r,
\tag{14}
\]

belongs to `Z_2`, and obeys the exact state congruences, but

\[
\boxed{g_r\in\mathbf Z_2\setminus\mathbf Z,
\qquad g_r<0\text{ in the real embedding}.}
\tag{15}
\]

Consequently

\[
\boxed{
 \Pi(r^L)\longrightarrow+\infty
}
\tag{16}
\]

even though the multiplier of every prefix is

\[
 \left({V\over U}\right)^L>1
\tag{17}
\]

and tends to infinity.

For the first case `r=3`,

\[
\boxed{g_3=-{2048\over139}.}
\tag{18}
\]

### Proof

The ratio for `r=3` is `2187/2048>1`, and increasing `r` multiplies it by
`9/8`, so `V>U` for every `r>=3`.  The finite-cylinder theorem supplies
infinitely many positive representatives of every `r^L`.  Since `V/U>1`, every
positive finite step strictly increases.

The geometric fixed point is (13), and direct substitution proves (14).  Its
denominator `V-U` is odd, so `g_r` belongs to `Z_2`.  Moreover

\[
 {g_r\over U}=-{1\over V-U}\equiv1\pmod4,
\tag{19}
\]

because `V-U=3 mod 4`, and

\[
 g_r\equiv {-U\over-U}\equiv1\pmod3.
\tag{20}
\]

Thus the fixed ghost lies in the exact `r`-branch cylinder.  Since `V-U>1` is
odd and coprime to the power of two `U`, the reduced fraction is not an
ordinary integer; it is visibly negative over the reals.  If the least positive
representatives were bounded, `T-9520` would extract a positive ordinary
realization, which by uniqueness of the inverse-limit point would equal `g_r`.
This is impossible, proving (16).  QED.

---

## R-9511: compatibility, expansion, and conditional growth do not extract an integer

**Claim ID:** `R-9511`  
**Title:** The common positive-orbit skeleton is logically insufficient for ordinary extraction  
**Status:** `PROPOSED`  
**Dependencies:** `L-9531`  

The family in `L-9531` simultaneously has:

1. one exact positive ordinary cylinder at every finite depth;
2. infinitely many positive ordinary representatives at every finite depth;
3. one compatible infinite `2`-adic path;
4. exact deterministic affine transitions;
5. strict expansion at every finite step;
6. prefix multipliers tending to infinity;
7. conditional unbounded growth for any hypothetical positive ordinary
   realization.

Yet it has no positive ordinary infinite realization.

Therefore no argument using only the seven properties above can prove ordinary
extraction.  In particular, the following packages do not cross the boundary
without an additional architecture-specific theorem:

- finite-prefix compatibility or arbitrarily long shadows;
- compactness in `Z_2`;
- positive multiplier/refund or conditional growth;
- pressure, entropy, dimension, or sparse-survivor estimates;
- a finite SCC in a projected refund graph;
- infinitely many fresh primes conditional on survival;
- an intrinsic decoder with no forever-defined initial integer.

These results may still be valuable for exclusions or necessary conditions.
They simply do not imply boundedness of the least-root sequence in `T-9520`.

This is an H-native countermodel, not an artificial affine system imported from
outside the problem.

---

## Blunt repository assessment

The current program is not wholly circular.

Genuine progress includes:

- complete frozen architecture classes excluded negatively, notably the
  corrected-stage class reviewed in PRs #33/#44;
- exact positive-cycle denominator interfaces, strong length/support barriers,
  and proof-producing finite exclusions;
- exact ordinary machines replacing informal future-dependent directives;
- false compactness, carry, and completion inferences discovered and repaired;
- the H exact-cylinder, renewal, and ordinary-section reductions themselves.

But the direct positive-orbit program has not crossed its decisive existence
boundary.  PR #19's one-integer decoder, PR #45's fixed chart, PR #49's
intrinsic quotient refund, and PR #51's run core each sharpen the map that an
ordinary seed would follow; none currently proves that one finite seed remains
in all moving cylinders.  Growth after legality is not the missing implication.

The accurate status is therefore:

```text
negative / exhaustive-class exclusions:
    genuine mathematical progress;

positive ordinary extraction:
    exact reformulations and strong necessary conditions,
    but no extracted root and no bounded least-root theorem.
```

---

## Why the target is genuinely weaker than Collatz

Take `mathscr A` to be the complete H exact language.  Proving

\[
 m_L(\mathscr A)\longrightarrow\infty
\tag{21}
\]

proves termination of the H partial system.  This is genuinely weaker than the
full Collatz conjecture: it excludes only shortcut-Collatz trajectories that
remain in the residue-restricted H subsystem.  It does not settle trajectories
that leave that subsystem.

For a strict architecture `mathscr A` inside H, (21) is weaker still: it
eliminates that complete prescribed class and nothing outside it.

In the opposite direction, boundedness is a sufficient counterexample
certificate.  The stabilized seed `P` gives

\[
 n_0={P-4\over3},
 \qquad
 N_0=8n_0+1,
\tag{22}
\]

and exact replay produces a positive infinite H orbit and hence a genuine
shortcut-Collatz counterexample.  After repository review this is precisely the
kind of object that can be promoted to a `K-####` candidate.

Thus the least-root decision is not a euphemism for the whole Collatz
conjecture.  Its negative side resolves a strict subsystem; its positive side
would produce an explicit counterexample to the full problem.

---

## The separate cycle blocker

The positive-cycle lane is finite rather than compactness-based.  For a word
`w`, write

\[
 F_w(p)={V_wp+C_w\over U_w}.
\tag{23}
\]

A positive cycle requires the entire denominator condition

\[
\boxed{
 D_w:=U_w-V_w>0,
 \qquad
 D_w\mid C_w,
 \qquad
 p={C_w\over D_w}\ge16,
}
\tag{24}
\]

followed by exact intermediate valuation replay.  Proper-factor divisibility,
near-integrality, a compatible prime-power subset, or a real multiplier window
is not enough.

A proof that (24) never occurs would eliminate every H cycle, an exhaustive and
genuinely weaker class, but it would not exclude nonperiodic H survivors.
Accordingly this iteration chooses ordinary extraction as the more global
blocker.

---

## Q-9515: the only H-global decision that changes the status

**Claim ID:** `Q-9515`  
**Title:** Decide the least positive H roots, not another finite shadow  
**Status:** `IDEA`

For the full H language, define

\[
 m_L=\min\{p\ge16:p\text{ has an exact H future of }L\text{ blocks}\}.
\tag{25}
\]

Exactly one of the following holds:

\[
\boxed{
\begin{array}{ll}
\sup_Lm_L<\infty
&\Longrightarrow
m_L\text{ stabilizes at one explicit infinite H seed};\\[2mm]
m_L\to\infty
&\Longrightarrow
\text{every positive H orbit terminates.}
\end{array}}
\tag{26}
\]

The same dichotomy applies to every fixed strict architecture by replacing the
full language with `mathscr A`.

A result changes the global status only if it proves one side of (26), or the
full-denominator cycle condition (24) for one explicit word.  Longer finite
prefixes, additional conditional growth, another `Z_2` path, or another
projected SCC do not supply the missing inference.

### Recommended offense

Choose one fixed architecture and attack only its scalar least-root sequence.
For H itself this is `m_L`; for the intrinsic renewal chart it is the least
positive `Z` surviving `L` renewals.  Prove a uniform upper bound and extract the
seed, or prove divergence and eliminate the entire class.  Do not change the
architecture with `L`, and do not replace ordinary boundedness by `2`-adic
compactness.