# One valuation layer of five-ray mergers is sufficient

**Status: PROPOSED alternative elementary certificate.** Concurrent PR157
at `64361ecca770092d6c8242dc6211e38818af2e50` already proves a stronger
one-sided first-layer criterion. The equivalence below is therefore
credited source overlap, not a new project-level reduction. This note
preserves a smaller thirteen-row certificate for the symmetric statement
and identifies why its demands do not close an ordinary induction. The
merger hypothesis itself remains open; no Collatz proof is asserted.

Use the positive ordinary shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

Write `x∼y` for meeting of the two ordinary forward orbits at independent
finite clocks. Let `E(t)` denote `t∼5t+1`.

## SL1. Single-layer rigidity

Let `f` map the positive integers into any set and satisfy

\[
f(T(n))=f(n)\quad(n\ge1),
\qquad f(5x)=f(x)\quad(x>0\text{ odd},\ 3\nmid x).       \tag{1}
\]

Then `f` is constant.

In fact there is an explicit selector which, for each `n>1`, supplies
`q<n` and a finite sequence of ordinary edges and applications of (1)
proving `f(n)=f(q)`. It always satisfies

\[
1\le q\le\frac{10}{11}n.                              \tag{2}
\]

All selected paths have at most fifteen edges. Consequently the number
of edges in the **conditional augmented graph** from `n` to 1 is at most
`15 ceil(log_(11/10) n)`. This is not a bound on ordinary Collatz clocks.

### Allowed letters

Read words from left to right. Each letter preserves `f`:

| Letter | Move | Domain |
|---|---|---|
| `D` | `x→2x` | every positive integer |
| `E` | `x→x/2` | even `x` |
| `O` | `x→(3x+1)/2` | odd `x` |
| `I` | `x→(2x−1)/3` | `x≡2 (mod 3)` |
| `M` | `x→5x` | `3∤x` |
| `V` | `x→x/5` | `5∣x` and `3∤x` |

For `I`, the output is positive and odd, and its next ordinary step is
`x`. To justify `M,V` on even ternary units, write `x=2^v u`, where `u`
is odd and prime to three. Both `x` and `5x` halve to the two sources in
(1). Thus the given odd-domain hypothesis is sufficient for every use
in the table. Neither multiplication by three nor a five-ray hypothesis
at a higher valuation layer is used.

### Thirteen affine certificates

For each row, write `n=M_0 u+r`, `u≥0`. The displayed word is legal for
every such ordinary parameter. Its endpoint is `a u+b`.

| `M_0` | `r` | Word | Endpoint `a u+b` | Endpoint in `n` |
|---:|---:|---|---|---|
| 12 | 11 | `I` | `8u+7` | `(2n−1)/3` |
| 16 | 3 | `OOEE` | `9u+2` | `(9n+5)/16` |
| 24 | 7 | `MOOEVI` | `18u+5` | `(3n−1)/4` |
| 32 | 11 | `OOEOE` | `27u+10` | `(27n+23)/32` |
| 16 | 15 | `OMOOEVII` | `12u+11` | `(3n−1)/4` |
| 32 | 23 | `OOOEE` | `27u+20` | `(27n+19)/32` |
| 96 | 91 | `MOOVOEE` | `81u+77` | `(27n+7)/32` |
| 20 | 3 | `OV` | `6u+1` | `(3n+1)/10` |
| 20 | 15 | `OOV` | `9u+7` | `(9n+5)/20` |
| 60 | 51 | `ODDIV` | `48u+41` | `(4n+1)/5` |
| 60 | 27 | `OODMIIVV` | `24u+11` | `(2n+1)/5` |
| 160 | 39 | `OMOOVOEV` | `81u+20` | `(81n+41)/160` |
| 160 | 59 | `OOEMOODDVDIVIII` | `128u+47` | `(4n−1)/5` |

Every modulus divides 480. Their union contains all 120 residues
`3 (mod 4)` modulo 480. This is a finite congruence-cover assertion, not
a census of trajectories below 480. Legality and inequalities are
identities in the unrestricted variable `u`.

### Exact verification rule and proof

Propagate a positive affine form `a u+b` through each word. For `E`
check that `a,b` are even. For `O` check that `a` is even and `b` odd.
For `I` check that `3∣a` and `b≡2 (mod 3)`; its new form is
`(2a/3)u+(2b−1)/3`. For `M` check `3∣a,3∤b`. For `V` additionally
check `5∣a,b`. Each output has positive integral coefficients. These
checks prove every step on every nonnegative integer `u`.

For each final row the table gives `0<a<M_0`, `0<b<r`, and

\[
11a\le10M_0,\qquad11b\le10r.
\]

They prove strict descent and (2) simultaneously for all `u≥0`.
The companion verifier checks every row with exactly these integer
conditions and verifies the complete residue cover.

An even `n` halves. For `n≡1 (mod 4)`, `n>1`, the ordinary word `OE`
ends at `(3n+1)/4≤4n/5<10n/11`. For `n≡3 (mod 4)`, take the first
applicable row of the table. The congruence cover guarantees one exists.
This constructs the promised selector. Strong induction gives
`f(n)=f(1)` for every positive integer. Iterating (2) gives the stated
augmented-path length bound. ∎

## SL2. Reconstruction of the single-layer equivalence

The following are equivalent:

1. Every positive ordinary integer reaches 1.
2. `x∼5x` for every positive odd `x` prime to three.
3. `E(4x)` for every positive odd `x` prime to three.

The parameters in statement 3 are exactly `t` with `v2(t)=2` and
`3∤t`, a set of natural density `1/12`.

**Proof.** Statement 1 immediately implies both merger statements.
For an odd positive `x`, the literal ordinary paths are

\[
4x\to2x\to x,
\]

\[
20x+1\to30x+2\to15x+1\to(15x+1)/2,
\qquad5x\to(15x+1)/2.
\]

Thus `E(4x)` is precisely `x∼5x`, so statements 2 and 3 are equivalent.
Apply SL1 to actual ordinary component labels to obtain statement 1.
The density follows because odd ternary units have density `1/3`, and
multiplication by four scales it to `1/12`. ∎

## Source-fixed adaptive composition: the exact unresolved demand

SL1 is an all-input theorem **under** its multiplier hypothesis. Its
rank decreases after a whole augmented path. It is not an ordinary
proof that the multiplier edges in that path exist.

The distinction can be seen in one explicit infinite class, without
any search-limit argument. For `n≡7 (mod 24)`, the row `MOOEVI` uses

\[
\begin{aligned}
n&\xrightarrow{M}5n
 \xrightarrow{O}(15n+1)/2
 \xrightarrow{O}(45n+5)/4\\
 &\xrightarrow{E}5(9n+1)/8
 \xrightarrow{V}(9n+1)/8
 \xrightarrow{I}(3n-1)/4.
\end{aligned}                                             \tag{3}
\]

Its endpoint is smaller, but the first `M` already demands the unknown
comparison `n∼5n` at the original parameter itself. Moreover, on the
subprogression

\[
n=31+48u,\qquad u\ge0,
\]

the `V` step demands the comparison at the odd ternary unit

\[
y=(9n+1)/8=35+54u>n.
\]

Consequently this same certificate cannot be used as an induction proof
of `x∼5x` with strictly smaller demand parameter `x`. In the proof of
constancy, its multiplier identities are hypotheses. In an attempted
unconditional recursive proof, they would be self or larger demands.
Physical orientation and cancellation of the total endpoint do not
supply these missing ordinary mergers.

The new compilation task is therefore precise: replace the multiplier
uses in a complete cover by already established ordinary paths or by
smaller demands under one genuine well-founded rank. Neither (3), the
other rows, nor the finite replay proves such a replacement. This is
the first unsupported inference toward full Collatz in this attempt.

## Frozen sources and overlap

- **PR157**, `64361ecca770092d6c8242dc6211e38818af2e50`,
  `research/global-closure-20261120/merger.md`, GCM-001–002, and
  `closing-attempts.md`: already proves the stronger one-sided law
  `x in C, x odd, 3∤x => 5x in C` sufficient for Collatz, with a
  complete directed certificate. It includes the single-layer reduction
  in SL2. The smaller symmetric certificate below does not replace or
  strengthen that one-sided theorem.

- **PR154**, `fe40bb6f88e8094290ef01207d9bf7c4798d35d0`,
  `research/structural-reset-20261120/component/PROOF.md`, CR-001–002,
  and `REDUCED_LAWS.md`: the existing sufficient restricted family is
  `t=4^a x`, `a≥1`, `x` odd and prime to three. The single-layer implication, also already proved more strongly in PR157,
  removes every layer except `a=1`. The alternative proof here uses the thirteen displayed ordinary/unit-five
  paths, rather than assuming the stabilized multiplier-three laws of
  that packet.
- **PR146**, `6863d298187af8b2619efbf78cc4b0aa8e627393`,
  `research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md`,
  `DIRECTED_TRIPLING.md`, `STABILIZED_CORE_DESCENT.md`, and
  `ADJACENT_128.md`: the current source already has directed tripling
  closure, a bounded directed return, the all-member class modulo4096,
  and eventual adjacent-pair criteria. No such source theorem is claimed
  as new here. A one-sided unit-five hypothesis is not established by
  this symmetric cover; reversing a path reverses its multiplier moves.
- **PR151**, `02a9f6ad17e5f1904cb4ff806fd0217d199e8437`,
  `research/ordinary-merger-selection/FIVE_RAY_RECURSION.md`: its two
  six-step recursive guards have odd parameters `11,35 (mod64)` and
  do not directly cover the even first layer `t=4x` here. Its successful
  mixed-word families and incomplete guard cover retain their scope.
- **PR153**, `eb04a5d79020cefa0ba46794095b5766c5ff66a4`,
  `research/fixed-integer-descent/mergers.md` and `rewriting.md`:
  the adaptive smaller-tripling and guarded rewriting results remain
  separate. In particular that source already contains the
  `P(25+64u)` smaller comparison also obtained through the Q section in
  the preceding pass; it is not a new result of this pass.
- **PR156**, the previous Q-section packet,
  `research/global-rigidity-20261120/Q_SECTION_GUARDS.md`, frozen file
  SHA-256 `a8ce19689b31abf002c77d6696e351a1f6db781d35b4c17fb21f834bbf08494b`:
  physical orientation can improve a particular descent, and bounded
  clocks do not cover every positive input. SL1 does not remove that
  distinction or turn an increasing number of finite examples into
  ordinary all-source coverage.

No external theorem is needed for SL1 or SL2. The finite computation
finds and verifies the displayed affine certificates. The proofs apply
to every ordinary integer in each class, independently of the size of a
sampled start. The complete Collatz conjecture remains open.
