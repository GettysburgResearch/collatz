# Forward multiplication by five on the basin of one

**Status: PROPOSED conditional theorem, with an exact all-lift affine certificate.**
The conditional induction below is complete. Its physical closure premise is
**OPEN**. This packet does not prove the Collatz conjecture.

The map throughout is the positive ordinary shortcut map

\[
T(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n.\end{cases}
\]

Write \(C\) for its basin of 1 and \(U=\{n>0:3\nmid n\}\). Ordinary
component equivalence, written \(x\sim y\), means equality of two actual
forward iterates at independently chosen finite clocks. Every affine path in
this packet stays in positive ordinary integers. No tripling invariance of
ordinary components is assumed.

## Exact source boundary

The new proof uses elementary ordinary paths and the certificate supplied
here. These frozen repository sources motivated the direction and fix what
is being strengthened:

| Source | Frozen full SHA | Path and relevant statement |
|---|---|---|
| PR146 | `6863d298187af8b2619efbf78cc4b0aa8e627393` | [`research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md`](https://github.com/GettysburgResearch/collatz/blob/6863d298187af8b2619efbf78cc4b0aa8e627393/research/upper-bit-mergers/THREE_RAY_ONE_SIDED.md): forward basin closure under tripling, including its restricted one-sided criteria. |
| PR154 | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0` | [`research/structural-reset-20261120/component/PROOF.md`](https://github.com/GettysburgResearch/collatz/blob/fe40bb6f88e8094290ef01207d9bf7c4798d35d0/research/structural-reset-20261120/component/PROOF.md), CR-001 and CR-002: two-sided component rigidity from five-ray mergers on \(\mathcal E=\{4^a x:a\ge1,\ x\text{ odd},\ 3\nmid x\}\). |
| PR154 | `fe40bb6f88e8094290ef01207d9bf7c4798d35d0` | [`research/structural-reset-20261120/component/REDUCED_LAWS.md`](https://github.com/GettysburgResearch/collatz/blob/fe40bb6f88e8094290ef01207d9bf7c4798d35d0/research/structural-reset-20261120/component/REDUCED_LAWS.md): a sufficient system of equality laws, including exact tripling invariance. |

The equality-based selector in PR154 cannot simply be read as a directed
proof after replacing its hypotheses by one-way implications: an equality
may have been used in the wrong direction. We instead give a complete
directed certificate. It needs neither a core function invariant under
tripling nor any physical comparison at a multiple of three.

The narrower sufficient hypothesis below is a result relative to those
specified sources. No claim of priority over the wider literature is made.

## GCM-001: a complete directed descent on ternary units

Let \(S\subseteq U\) satisfy:

1. \(1\in S\).
2. For \(n\in U\), \(n\in S\iff2n\in S\).
3. For odd \(n\in U\), \(n\in S\iff3n+1\in S\).
4. For odd \(n\in U\), \(n\in S\Longrightarrow5n\in S\).

Then \(S=U\).

More precisely, for every \(n\in U\setminus\{1\}\) there is a positive
\(q\in U\) such that

\[
q\le\frac{19}{20}n<n,
\qquad q\in S\Longrightarrow n\in S.                 \tag{1}
\]

The implication has a finite explicit certificate using the stated laws.
For a number coprime to 30 it uses at most one application of law 4 and at
most 19 affine moves of the form described below. These bounds concern the
conditional proof, not a bound for an ordinary Collatz hitting time.

### Extend forward five to even ternary units

If \(n=2^v x\), with \(x\) odd and prime to three, law 2 gives
\(n\in S\iff x\in S\) and \(5n\in S\iff5x\in S\). Thus law 4
implies \(n\in S\Longrightarrow5n\in S\) on all of \(U\). This
extension uses only halving and doubling.

### The directed primitives

The certificate is written from the candidate \(n\) toward its smaller
representative \(q\). Every arrow \(x\rightsquigarrow y\) has the
semantic direction

\[
y\in S\Longrightarrow x\in S.                       \tag{2}
\]

| Primitive | Exact move and its domain | Why (2) holds |
|---|---|---|
| `B` | \(x\mapsto3x+1\), for odd \(x\in U\) | Law 3 is an equivalence. Physically, \(T(x)=T(3x+1)\). |
| `Ij`, \(j\ge1\) | \(x\mapsto y=(2^j x-1)/3\), only if \(y\) is a positive odd ternary unit | Law 3 at \(y\), then law 2. Physically, \(T^j(y)=x\). |
| `/2` | \(x\mapsto x/2\), for even \(x\) | Law 2 is an equivalence. |
| `/5` | \(x\mapsto x/5\), for \(5\mid x\) | The extended law 4 says membership at \(x/5\) implies membership at \(x\). |

In particular, the certificate never divides by three as a component
identity, never multiplies by five in the direction (2), and never uses an
inverse odd step whose new value is divisible by three.

### The affine certificate

The complete certificate is
[`merger-certificate.json`](../../reports/2026-11-20-global-closure/merger-certificate.json).
Its SHA256 is
`751523dd92445610a26302947a2f689aecc56a27eaf6fa1f9954eb2e59f5c7c1`.
It contains 55 words and 464 residue cells. A cell means

\[
n=M u+r,\qquad u\in\mathbb Z,\quad u\ge u_0.
\]

Its entry gives the word identifier and its endpoint \(q=A u+B\).
Each word is a sequence of pairs, for example `["I3","25"]`: first apply
the indicated affine operation, then divide successively by 2 and 5.
The only cell with \(u_0=1\) is \(n=1440u+1\); it excludes the base
case 1. Every other cell has \(u_0=0\).

The cells form the following complete partition of the positive integers
coprime to 30, apart from that base case:

| Modulus | Completed cells at this modulus | Classes refined into the next modulus |
|---:|---:|---|
| 1440 | 378, including \(1\pmod{1440}\) above its base | \(79,239,799,959,1159,1339\pmod{1440}\) |
| 8640 | 33 | \(1159,5479,7099\pmod{8640}\) |
| 51840 | 12 | \(5479+8640j\pmod{51840}\), \(0\le j<6\) |
| 311040 | 35 | \(299239\pmod{311040}\) |
| 1866240 | 6 | None |

At each refinement a remaining cell is split into its six disjoint residue
cells at the next modulus. The initial modulus has 384 residues coprime to
30. Consequently the displayed partition has no unassigned integer. The
checker also independently expands the final partition to the common
modulus 1,866,240 and verifies exactly its 497,664 residues coprime to 30,
with no omissions or overlaps.

For the base cell, the word `B /2 /2` gives

\[
1440u+1\rightsquigarrow1080u+1,
\qquad u\ge1.
\]

For an example involving inverse ordinary edges, the cell
\(n=8640u+239\) uses

```text
B/2 B/2 B/2 B/22 B/2 I3 I1 I1 I1 I1 I1 I2/5
```

Its endpoint is

\[
q=3072u+85=\frac{16n+1}{45}<n.
\]

The apparent denominator 45 in this final expression does not license a
free division by nine. Each inverse operation is checked separately, with
its positive odd ternary-unit source and its exact ordinary clock. The
single `/5` has precisely the one-way interpretation in (2).

At the deepest modulus, \(n=1866240u+299239\) has the shorter word

```text
B/2 B/2 B/22 B/2 B/2 B/22 B/25
```

and endpoint

\[
q=1594323u+255640=\frac{2187n+2707}{2560}<n.
\]

### Why a finite certificate proves all lifts

Represent the current value as \(a u+b\). Each step is an identity in the
unrestricted integer parameter \(u\), not a check at selected numerical
starts. The checker verifies:

- \(a>0\), \(a u_0+b>0\), \(3\mid a\), and \(3\nmid b\), before
  and after every primitive;
- for `B`, \(2\mid a\) and \(b\) odd;
- for `Ij`, exact divisibility of \(2^j a\) and \(2^j b-1\) by three,
  with the quotient form odd and prime to three for every lift;
- for every `/2` or `/5`, divisibility of both affine coefficients;
- the advertised endpoint \((A,B)\);
- \(M-A\ge0\) and \((M-A)u_0+r-B>0\), proving strict decrease;
- \(19M-20A\ge0\) and
  \((19M-20A)u_0+19r-20B\ge0\), proving the uniform bound in (1).

These coefficientwise checks prove positivity, domain legality and strict
descent for **every** integer in each infinite cell. The finite residue
cover is exhaustive, so there is no remaining ordinary input to select or
an all-depth guard that can return unresolved.

The greatest endpoint/source ratio across the cells, including their
unbounded limits, is exactly

\[
\frac{13403}{14119}<\frac{19}{20}.
\]

There are 1,284 affine moves across the full certificate. Of the 464 cells,
219 use a `/5`, each exactly once; the other 245 use ordinary equivalences
alone. The certificate's largest cost in the graph of ordinary undirected
edges and forward-five edges on all ternary units is 73. This augmented
graph cost is not a physical ordinary-orbit clock.

### Finish the induction

For even \(n\in U\), use \(q=n/2\). For odd \(n\in U\) divisible
by five, use \(q=n/5\) and the forward-five implication. Both choices
satisfy (1). Otherwise \(\gcd(n,30)=1\), and the complete certificate
supplies (1).

Strong induction in the usual positive integer order now proves \(n\in S\)
for every \(n\in U\): the terminal \(q<n\) is already in \(S\), and
reading the finite implications backward puts the original \(n\) in
\(S\). Intermediate vertices may exceed \(n\); they are justified by
the stated directed laws, not by an induction hypothesis at a larger
integer. This proves GCM-001.

## GCM-002: a single valuation layer and a single basin suffice

The following statements are equivalent:

1. Every positive ordinary integer reaches 1.
2. For every odd \(x\in C\) with \(3\nmid x\), one has \(5x\in C\).
3. For every \(t\in C\) with \(v_2(t)=2\) and \(3\nmid t\), one has
   \(5t+1\in C\).
4. For every \(t\in C\cap\mathcal E\), one has \(5t+1\in C\), with
   \(\mathcal E\) as in PR154.

These statements concern one basin in one direction. Statement 3 uses only
the first valuation layer \(t=4x\) of \(\mathcal E\), which has natural
density \(1/12\): \(v_2(t)=2\) has density \(1/8\), and excluding
multiples of three leaves a factor \(2/3\). Density is not used in the
proof of sufficiency.

### Proof

Take \(S=C\cap U\). The ordinary map gives laws 1--3 of GCM-001
unconditionally. Statement 2 supplies its forward-five law. Thus every
ternary unit converges.

For an arbitrary positive integer, first remove its powers of two. If the
remaining odd value \(z\) is divisible by three, then \(T(z)=(3z+1)/2\)
is a positive ternary unit. It therefore converges, and so does the
original number. This proves 2 implies 1 without assigning any unproved
tripling invariance to \(C\).

For odd \(x\), the two exact ordinary clocks

\[
T^3(20x+1)=\frac{15x+1}{2}=T(5x)                 \tag{3}
\]

give \(20x+1\in C\iff5x\in C\). Also \(4x\in C\iff x\in C\).
Consequently statements 2 and 3 are exactly the same closure assertion
after the substitution \(t=4x\). Statement 4 implies statement 3 by
restriction. Full convergence implies all of them. This proves the four
equivalences.

The higher layers from PR154 are unnecessary for this one-sided
criterion. The physical closure premise has not been derived from the
ordinary map; the theorem isolates it as a sufficient and necessary
remaining assertion.

## Evidence and exact replay

Run from the repository root:

```bash
python -X utf8 -B experiments/global_closure_merger.py
python -X utf8 -B experiments/global_closure_merger.py --compare reports/2026-11-20-global-closure/merger-report.json
```

The checker reads the frozen certificate hash, checks every affine guard,
the complete cover and the strict decrease, and rejects nine deliberately
broken controls. The controls include a nonintegral inverse, an inverse
that enters a multiple of three, a reversed five arrow, a missing residue
cell, a false endpoint and a legal but nondecreasing path. A separate set
of 1,856 concrete ordinary-clock replays is explicitly bounded and is not
used in place of the affine proof. `--output` creates a new report and
refuses to overwrite an existing evidence file.

The search that discovered the words is not a proof dependency. The
certificate and its exact verifier are sufficient to reconstruct every
claimed all-input implication. No convergence computation is used to
infer the open physical premise.

## The remaining physical obligation

The required lemma is now simply

\[
\boxed{\quad x\in C,\quad x\text{ odd},\quad3\nmid x
       \quad\Longrightarrow\quad5x\in C.\quad}        \tag{F5}
\]

A supplied finite orbit from \(x\) to 1 certifies its antecedent; it does
not automatically give an orbit for \(5x\). There is no step in this
packet that propagates (F5) through every inverse ordinary lift. The
completed directed induction begins **after** (F5), and cannot be used to
justify that premise itself.

The standard multiplier obstruction also remains: two fixed parity words
cannot give a merger between \(x\) and \(5x\) for two distinct values of
\(x\), because equality of affine slopes would require
\(2^a3^b=5\,2^c3^d\). This only rules out fixed-word identities. It does
not rule out a recursive ordinary construction with clocks depending on
its fixed positive input.

The precise next task is to construct that recursive physical closure, or
an independently justified narrower premise that entails it. Neither a
finite census of convergent examples nor a product of ratios taken from
unrelated ordinary sources supplies the missing pointwise implication.
