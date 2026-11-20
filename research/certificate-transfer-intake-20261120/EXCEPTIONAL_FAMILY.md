# An explicit certified family outside the PDF's coalescent set

**Status: PROPOSED.** This is a source-aware comparison lemma, with a self-contained elementary proof. It does not prove or refute Collatz. It identifies an infinite family of eligible, already certified antecedents on which the uploaded PDF's particular coalescent-class certificate rule cannot apply. It does **not** exclude other certificate transformations or a separate guarded global induction.

The family and its finite paths are already in PR146. The phase invariant and its lower bound are also already in PR146. The contribution here is to combine those pinned results with the PDF's exact definition of its successful set, and to distinguish the single-transfer exponent from the updated ZIP's double-transfer exponent.

## Source boundary

All repository sources in this note are pinned at PR146 head
`e238c63a5d57f96bb063b7472498d1977df51951`.

| Source | Claim used |
|---|---|
| [`research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/DEEP_REVERSE_BASIN.md), section “What the first nonempty rank would settle” | Complete classification of the four-odd-step antecedents, their finite partner paths, and the target powers `3^(27s-1)`. |
| [`research/upper-bit-mergers/BASIN_PHASE.md`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/BASIN_PHASE.md), equation (1) and “Exact classification inside the basin of 1” | The grade `K=2r-tau`, its lower bound, and the phase obstruction to a lifted merger. |
| [`research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/BOUNDED_RANK_TRANSFER.md), “Applying the bound to actual certificates” and “An exact test on an entire family of stopping certificates” | Prior context: known certificate depth does not imply a bounded lifted merger; phase and finite-prefix arguments must retain their stated directions and scopes. No additional result from this file is needed in the proof below. |

The uploaded manuscript *Collatz certificates under x ↦ (x+1)/2: a density-one theorem and the open remainder*, dated 20 November 2026, defines the set `G` in its “Coalescent classes and the main theorem” section and states the suffix certificate rule in Lemma 2. The updated ZIP's `problem2.py`, section 4, checks a **two-transfer** consequence involving `3^(27s-2)`. Input hashes and manuscript review status belong to the accompanying intake report; the lemma here does not assume the manuscript's probabilistic theorem.

## 1. Map and successful set

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

Let `E` be the positive odd integers reaching 1, equivalently the integers with a finite exponent certificate

\[
3^r x+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r},
\qquad 0=A_0<A_1<\cdots<A_r.
\tag{1}
\]

The eligible domain is

\[
\mathcal C=\{x=128m+1:m\ge1,\ 4\nmid m\}.
\]

For `x` in this domain put `y=(x+1)/2=64m+1`. A parameter belongs to the manuscript's set `G` if two finite legal parity words from the affine families `128m+1` and `64m+1` yield the same affine endpoint on a binary residue class of `m` containing that parameter. The manuscript presents this as equality at clocks `n+7,n+6`, with equal odd counts, after reading `n` binary digits of `m`.

This is an **all-lift affine merger**. A meeting of the two numerical orbits at one parameter is weaker and is not excluded by membership outside `G`.

## 2. Proposed lemma: the entire first certificate layer misses G

For every integer `s>=1`, write

\[
H=54s,\qquad q_s=\frac{2^H-1}{81},\qquad m_s=2q_s,
\]

and define

\[
x_s=256q_s+1=\frac{2^{H+8}-175}{81},
\qquad
y_s=128q_s+1=\frac{2^{H+7}-47}{81}.
\tag{2}
\]

Then:

1. `x_s` lies in the eligible class `257 mod 512` and belongs to `E`.
2. Its first arrival at 1 has exactly four odd inputs and clock `H+8`, with exponent certificate
   \[
   (0,2,4,6,H+8).
   \tag{3}
   \]
3. Its partner satisfies the unconditional finite-path identity
   \[
   T^{H+7}(y_s)=3^{27s}+1,
   \tag{4}
   \]
   with exactly `27s+4` odd inputs before that endpoint and no earlier visit to 1.
4. `x_s` does not belong to `G`, irrespective of whether `y_s` reaches 1.
5. The question whether `y_s` reaches 1 is exactly the question whether `3^(27s-1)` reaches 1, through explicit ordinary meetings.

In particular, the PDF's coalescent-class certificate rule leaves an explicit infinite set of already certified antecedents outside its acceptance set. This statement is fully compatible with `G` having relative natural density one.

### Proof of integrality, eligibility and the certificate

The elementary congruence `2^27 = -1 mod 81` gives `81 | 2^(54s)-1`. The quotient `q_s` is positive and odd. In fact `q_s = 3 mod 4`, since its numerator is `-1 mod 4` and `81 = 1 mod 4`. Therefore `m_s` is twice odd, and

\[
x_s=128m_s+1\equiv257\pmod{512}.
\]

The successive odd vertices from `x_s` are

\[
256q_s+1
\ \longmapsto\ 192q_s+1
\ \longmapsto\ 144q_s+1
\ \longmapsto\ 108q_s+1
\ \longmapsto\ 1.
\tag{5}
\]

The first three division exponents are exactly 2. For the fourth,

\[
3(108q_s+1)+1=324q_s+4=4(81q_s+1)=2^{H+2}.
\]

All four preterminal odd vertices exceed 1. Thus (5) is the first-hit certificate, and its cumulative exponents are exactly (3). In particular its odd count is 4 and its shortcut clock is `H+8`.

These are all eligible antecedents with four odd inputs before their first visit to 1. Indeed, from an arbitrary `x=128m+1>1`, the first three accelerated odd steps have exponents `2,2,2` and end at `54m+1>1`. A fourth odd step ends at 1 precisely when

\[
162m+4=2^h.
\]

This forces `m=2q` and `2^(h-2)=81q+1`. The order of 2 modulo 81 is 54: `2^27=-1 mod81` and `2^18=28 mod81`, excluding every proper divisor of 54, while `2^54=1 mod81`. Hence `h-2=54s` for some `s>=1`, giving exactly (2). In particular no eligible antecedent has first-hit odd count below four.

### Proof of the partner path

Three odd-even pairs from `y_s=128q_s+1` give

\[
T^6(y_s)=54q_s+1=\frac{2^{H+1}+1}{3}.
\]

The next step is odd and gives

\[
T^7(y_s)=2^H+1.
\tag{6}
\]

For `0<=i<=H`, the exact shadow identity is

\[
T^i(2^H+1)=T^i(1)+2^{H-i}3^{\lceil i/2\rceil}.
\tag{7}
\]

To prove it, before the last step the difference from the cycle through 1 is even, so the two inputs have the same parity. On an odd input the difference is multiplied by `3/2`; on an even input it is halved. Induction gives (7). Every displayed value is greater than 1.

Since `H` is even, `T^H(1)=1`, and the segment in (7) has `H/2=27s` odd inputs. Equations (6) and (7) prove (4), with a total of `4+27s` odd inputs. The initial seven states also precede any visit to 1.

### The phase bound

For any positive integer `n` that reaches 1, let `r(n)` count its odd inputs and let `tau(n)` be its first hitting clock. Define

\[
K(n)=2r(n)-\tau(n).
\]

The same value is obtained from any later visit to 1, because a complete turn of the cycle `1 -> 2 -> 1` adds one odd input and two clocks. Hence for every finite prefix of length `L` with `p` odd inputs,

\[
K(n)=2p-L+K(T^L(n)).
\tag{8}
\]

The following elementary inequality is the one already used in `BASIN_PHASE.md`:

\[
K(n)\ge-\log_2 n.
\tag{9}
\]

Indeed `2T(v)/v` equals 1 on an even input and is at most 4 on an odd input. Multiplication along a path to 1 gives `2^tau/n <= 4^r`, which is (9).

### No coalescent class can contain x_s

Suppose for contradiction that `x_s` belongs to `G`. Then its partner `y_s` reaches 1, because it merges with the already certified `x_s`.

Let a purported affine merger use `i` clocks and `p` odd inputs on the `x` arm, and `j` clocks and `q` odd inputs on the `y` arm. The two initial slopes in the parameter `m` are 128 and 64. Equality of the endpoint slopes requires

\[
128\,3^p2^{-i}=64\,3^q2^{-j}.
\]

Unique factorization gives `p=q` and `i=j+1`. Following the common endpoint to 1 and using (8) therefore forces

\[
K(y_s)-K(x_s)=1.
\tag{10}
\]

On the other hand, (3) gives `K(x_s)=8-(H+8)=-H`. Put `w_s=3^(27s)+1`. The prefix (4) and (8) give

\[
K(y_s)=2(27s+4)-(54s+7)+K(w_s)=1+K(w_s).
\tag{11}
\]

Combining (10) and (11) would require `K(w_s)=-H`. But

\[
w_s=3^{27s}+1<4^{27s}=2^H,
\]

so (9) gives

\[
K(w_s)\ge-\log_2 w_s>-H,
\]

a contradiction. If `y_s` does not reach 1, it cannot merge with `x_s` in the first place. Thus in either case `x_s` is outside `G`.

Whenever `y_s` does converge, the quantitative phase defect is

\[
K(y_s)-K(x_s)-1
=H+K(w_s)
\ge H-\log_2(3^{27s}+1)>0.
\tag{12}
\]

The obstruction survives arbitrarily many appended loops at 1: those loops preserve `K`.

### Identification of the single-transfer target

The even integer `w_s=3^(27s)+1` and the odd integer `3^(27s-1)` have the same next shortcut iterate,

\[
T(w_s)=\frac{3^{27s}+1}{2}
=T(3^{27s-1}).
\]

Together with (4), this proves the last assertion. All the paths are ordinary positive paths. No assumed convergence of either pure power enters their construction. This completes the proof.

## 3. Why the updated ZIP has the different exponent 27s-2

The updated `problem2.py` applies the requested implication **twice**. With the notation above,

\[
x_s=256q_s+1,
\qquad y_s=128q_s+1,
\qquad z_s=\frac{y_s+1}{2}=64q_s+1.
\]

Since `q_s = 3 mod 4`, `y_s = 385 mod 512`, so this is indeed another eligible antecedent if its convergence has first been established.

Three odd-even pairs give

\[
T^6(z_s)=27q_s+1,
\qquad
T^7(z_s)=\frac{27q_s+1}{2}=T(9q_s).
\tag{13}
\]

Also `9q_s=(2^H-1)/9`, and two direct odd steps give

\[
T(9q_s)=\frac{2^{H-1}+1}{3},
\qquad T^2(9q_s)=2^{H-2}+1.
\tag{14}
\]

Apply (7) with `H-2` in place of `H`. It follows that

\[
T^{H+6}(z_s)=3^{27s-1}+1.
\tag{15}
\]

This even endpoint has the same next iterate as `3^(27s-2)`. Therefore

\[
z_s\in E\quad\Longleftrightarrow\quad 3^{27s-2}\in E.
\]

There is no disagreement between the two exponents:

| Transfer made from the explicit certified x_s | Ordinary target |
|---|---|
| Once: `x_s -> (x_s+1)/2 = y_s` | `3^(27s-1)` |
| Twice: additionally `y_s -> (y_s+1)/2 = z_s` | `3^(27s-2)` |

The second implication needs membership of `y_s`, which is exactly the unresolved conclusion of the first on this family. The two-transfer consequence must not be reported as the direct target of the first-layer question.

## 4. What this comparison does and does not say

The family grows exponentially in `s`, so it has zero relative natural density in the eligible domain. Its exclusion from `G` does not conflict with the PDF's density-one claim.

It proves that the PDF's specific suffix-copying rule, based on a common all-lift affine merger, cannot handle any member of this certified first layer. It does not prove that the partners diverge, that their actual numerical orbits fail to meet, or that every other certificate method fails. If a partner converges, its numerical orbit necessarily meets the certified source at 1.

A separate guarded argument may exclude the same family as the location of a **least** counterexample without constructing the all-lift affine merger prohibited here. Consequently this note must not be used to say that all current repository methods leave the family untreated. The only excluded mechanism is membership in the uploaded manuscript's `G`.

The manuscript's phrases “the orbits are unrelated” and “no identity links the two orbits afterwards” should therefore be read narrowly or replaced. The exact conclusion is: **no pair of finite parity words gives the same affine endpoint on a binary residue class through that parameter**. This leaves ordinary meetings, adaptive comparisons, other intermediate sources, and different induction invariants available.

## Evidence level

The argument above establishes the quantified claim symbolically. During preparation, a separate short exact-arithmetic replay checked the four-step certificates and the partner checkpoints for `s=1,...,5`. That finite replay is corroboration, not the proof of the universal statement. No new Lean verification, independent review of later PR heads, or complete repository gate is claimed by this file.
