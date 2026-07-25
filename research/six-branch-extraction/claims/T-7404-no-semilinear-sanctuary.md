# T-7404 — No semilinear sanctuary in the six-branch survivor set

Claim ID: `T-7404`  
Title: The complete six-branch survivor set contains no infinite arithmetic progression and no nonempty semilinear forward-invariant sanctuary  
Status: `PROPOSED`  
Authoring agent: `gpt56-extraction-01`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `D-7401`  
Scope: the stationary six-branch minimal-word system  
Related counterexample candidates: none

## Statement

Let

\[
S_\infty=\bigcap_{n\ge0}S_n
\]

be the set of positive ordinary integers whose canonical rational-base digits
remain forever in

\[
\mathcal A=
\{229376,258048,290304,326592,367416,413343\}.
\]

Then:

1. `S_infinity` contains no infinite arithmetic progression.
2. More quantitatively, if
   \[
   R+M\mathbf Z_{\ge0}\subseteq S_n,
   \]
   and `v=nu_2(M)`, then
   \[
   \boxed{2^{19n-\min(v,19n)}\le6^n.}
   \tag{1}
   \]
3. Consequently `S_infinity` contains no infinite semilinear subset of the
   positive integers.
4. There is no nonempty semilinear set `X subseteq S_infinity` satisfying
   \[
   F(X)\subseteq X.
   \]

Thus no Presburger/ultimately-periodic ordinary sanctuary can certify a
counterexample inside this chart.

## Proof

### 1. Exact finite-depth residue count

By `D-7401`, every length-`n` word over the six allowed digits selects one
residue class modulo

\[
Q^n=2^{19n}.
\]

The deterministic digit map makes different words select different classes:
if two roots were congruent modulo `Q^n`, exact forward division would recover
the same first `n` canonical digits. Hence `S_n` is the union of exactly

\[
6^n
\tag{2}
\]

residue classes modulo `Q^n`.

The argument below needs only the upper bound `6^n`.

### 2. Residues occupied by one arithmetic progression

Fix an arithmetic progression

\[
R+M\mathbf Z_{\ge0},
\qquad M>0,
\]

and put

\[
v=\nu_2(M).
\]

Modulo `Q^n=2^(19n)`, this progression occupies exactly

\[
{Q^n\over\gcd(M,Q^n)}
=
2^{19n-\min(v,19n)}
\tag{3}
\]

distinct residue classes. If the entire progression lies in `S_n`, every one
of these classes must be among the at most `6^n` legal classes. This proves
`(1)`.

For every fixed `M`, once `19n>v`, inequality `(1)` becomes

\[
2^{19n-v}\le6^n,
\]

or

\[
\left({2^{19}\over6}\right)^n\le2^v.
\]

Since `2^19>6`, this fails for all sufficiently large `n`. Therefore no
infinite arithmetic progression is contained in every `S_n`, proving part 1.

### 3. Semilinear subsets

Every infinite semilinear subset of `Z_(>0)` contains an infinite arithmetic
progression. Part 1 therefore shows that `S_infinity` contains no infinite
semilinear subset.

### 4. Forward-invariant sanctuaries

For every positive integer `x`,

\[
F(x)=\left\lceil{Px\over Q}\right\rceil>x
\]

because `P>Q`. Hence the forward orbit of any point is strictly increasing and
contains infinitely many distinct integers.

If a nonempty semilinear set `X subseteq S_infinity` were forward invariant,
then the full infinite orbit of any `x in X` would lie in `X`. Thus `X` would be
infinite, contradicting part 3. ∎

## Constructive significance

The theorem closes an exhaustive certificate class rather than a bounded
search:

```text
finite union of arithmetic rays / ultimately periodic value set
  + exact forward invariance
  + six-branch legality
```

cannot occur.

This is distinct from saying that one survivor does not exist. A survivor orbit
could be highly nonsemilinear, as the rational-base complexity results already
suggest. The theorem prevents a value-space Presburger sanctuary from being
mistaken for the missing ordinary extraction.

## Dependency audit

- Only finite-word residue completeness from `D-7401` is used.
- The one-dimensional characterization of an infinite semilinear set as
  containing an arithmetic progression is elementary Presburger arithmetic.
- No external density theorem, experiment, or unmerged cycle claim is used.

## Gap audit

- Automatic sets of integers need not be semilinear; the theorem does not
  exclude every finite automaton reading binary representations.
- A single all-time orbit need not itself be semilinear.
- Zero density, absence of progressions, and absence of a Presburger sanctuary
  do not imply `S_infinity` is empty.
- No lower bound for the least roots `m_n` is obtained.

## Adversarial tests

1. The progression step `M` may contain an arbitrarily large power of two.
2. The progression need not begin at its least nonnegative residue.
3. Only an upper bound of `6^n` legal classes is required, so accidental class
   collisions would not weaken the proof.
4. The finite-set case is excluded separately by strict forward increase.
5. The theorem is about value-space semilinearity, not symbolic eventual
   periodicity.

## Suggested next attack

Any positive certificate must now leave both the finite rational-section class
of `T-7403` and the semilinear value-sanctuary class of this theorem. The next
valid target remains a direct proof that the least roots stabilize or escape.