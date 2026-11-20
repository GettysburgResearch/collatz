# A six-run guarded order for all eleven AYH rules

**PROPOSED, with exact bounded replay.** This transfers the proved
107-odd-event run-cap clock to the actual eleven-rule system on proper
words. The guard is essential. No unrestricted Collatz proof,
unrestricted string termination proof, or context-compatible reduction
order is claimed.

## Attribution and precise dependence

The mixed binary/ternary encoding and rewriting system are due to
Emre Yolcu, Scott Aaronson, and Marijn J. H. Heule,
[*An Automated Approach to the Collatz Conjecture*](https://arxiv.org/abs/2105.14697v3),
Journal of Automated Reasoning 67, 12 (2023),
[DOI 10.1007/s10817-022-09658-8](https://doi.org/10.1007/s10817-022-09658-8).

The administrative potential, ordinal construction, and generic rewrite
budget are reconstructed from PR #141 at
`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`,
[`research/ay-persistent-20261031/PROOF.md`, HC-5--HC-6](https://github.com/GettysburgResearch/collatz/blob/5025ef464d4b6d4f4a412a3e33c3477de68dfa8b/research/ay-persistent-20261031/PROOF.md).
That source uses a ten-popcount guard and an odd clock at most 79.
The change here is the six-*one-run* guard and the independently checked
clock at most 107 from [RC-5](arithmetic.md#5-complete-finite-replay-through-cap-six)
and [M3](modular_hitting.md#m3-consequence-for-actual-odd-collatz-trajectories).
This transfers the construction to a different guard through a new
finite-core theorem; it is not a new general ordinal construction.
The two numerical guards are incomparable: ten isolated ones pass the
old popcount guard but fail the six-run guard, whereas a sufficiently
long one-run input passes the new guard but fails the old one.

## Encoding, guard and clock

A proper word is `c w d`, with `w` over `a,b,e,f,g`. Start with value 1
at `c` and read the interior left to right:

| Letter | Action on the current value |
|---|---|
| `a` | `2x` |
| `b` | `2x+1` |
| `e` | `3x` |
| `f` | `3x+1` |
| `g` | `3x+2` |

The final `d` has no arithmetic action. Denote the resulting positive
integer by `N(w)`. Let `b(N)` be its binary bitlength and define

\[
H(w)=\sum_{\substack{\text{ternary letter }e,f,g\\\text{in }w}}
b(\text{positive prefix value immediately before that letter}).
\]

Use `U(n)=(3n+1)/2^v2(3n+1)` on odd positive integers. Let `q(n)` be
the first odd-event time at which the trajectory reaches 1 or has more
than six binary one-runs. Include time zero, so `q=0` on those terminal
states. The separately proved cap-six theorem makes `q` a total integer
function with `0<=q<=107`. At any active odd source,

\[
q(U(n))=q(n)-1.
\]

Permit rewrites only when `N(w)>1` and
`runs(oddpart(N(w)))<=6`. Stop immediately when either condition fails.
This guard is a condition on the current ordinary value, not on the
literal count of symbols in the mixed word.

## RW-1: a rank decreasing on every permitted rule

The eleven rules, with the repository's letter names, are

```text
ad -> d      bd -> gd
ae -> ea     af -> eb     ag -> fa
be -> fb     bf -> ga     bg -> gb
ce -> cb     cf -> caa    cg -> cab
```

On guarded proper words the lexicographic natural-number triple

\[
\rho(w)=\bigl(q(\operatorname{oddpart}N(w)),\ v_2(N(w)),\ H(w)\bigr)
\]

strictly decreases on every permitted rewrite. Equivalently use the
ordinal `omega^2 q + omega v2(N) + H`, below `omega^3`.

**Proof, including all eleven rules.** Each of the six internal
binary/ternary swaps preserves the composed affine value. It moves one
ternary letter left across a binary letter. Its old prefix is `2x` or
`2x+1`, with bitlength `b(x)+1`; its new prefix is `x`, with bitlength
`b(x)`. Every later prefix value agrees by the affine identity. Thus
each such swap preserves `N` and decreases `H` by exactly one.

The three `c`-boundary rules replace the values 3, 4, and 5 by their
binary spellings. They remove one ternary letter whose prefix value is
1 and whose contribution to `H` is therefore one. All later prefix
values again agree. These nine administrative rules preserve the first
two rank coordinates and decrease the third.

The rule `ad -> d` performs `N -> N/2`. It preserves the odd part,
leaves `H` unchanged, and decreases `v2(N)` by one.

The rule `bd -> gd` acts on an odd `N>1` and performs
`N -> (3N+1)/2`. Its new odd part is `U(N)`, so the first coordinate
decreases by one. It creates a ternary letter with prefix `(N-1)/2`,
increasing `H` by exactly `b(N)-1`; this is permitted because the
earlier rank coordinate strictly decreases. The terminal value 1 is
represented only by `cd`, which has no outgoing rule. QED.

An active proper word is never stuck. If it has a ternary letter, its
leftmost one has either `c` or a binary letter immediately to its left,
and one of the nine administrative rules applies. If it has none, its
nonempty binary interior ends in `a` or `b`, enabling a dynamic rule.
Consequently every maximal guarded rewrite sequence stops at 1 or at
a genuine run-cap exit, regardless of scheduling.

## RW-2: a bound on literal rewrites

For a proper input word with value `N`, bitlength `b=b(N)`, and initial
administrative potential `H`, every guarded rewrite sequence has at most

\[
\boxed{H+108(b-1)+5885}
\]

literal rewrites. This counts dynamic and administrative rules.

**Proof.** Write `d` for the number of odd dynamic events and `k` for
all dynamic events. The rank law gives `d<=q(oddpart N)<=107`.
An odd shortcut step multiplies its positive input by at most two;
an even step halves it. Since the final value is at least one,

\[
k\le\lfloor\log_2 N\rfloor+2d=b-1+2d.
\]

Only an odd event increases `H`. Immediately before the `j`-th odd
event, bitlength is at most `b+j-1`; its `H` creation is at most
`b+j-2`. Total creation is therefore at most

\[
d(b-1)+\frac{d(d-1)}2.
\]

Every administrative event consumes exactly one unit. Thus the total
number of literal rewrites is at most

\[
H+(d+1)(b-1)+\frac{d(d-1)}2+2d.
\]

The expression increases with `d>=0`; substitute `d=107`, using
`107*106/2+214=5885`. A finite prefix of any purported longer sequence
satisfies the same estimate, so the bound does not presuppose a final
state. QED.

## Why the restrictions cannot be dropped

The guard cannot be omitted from this rank. The ordinary integer 5461,
with binary spelling `1010101010101`, has seven one-runs. Its canonical
binary word has rank `(0,0,0)`. The actual rule `bd -> gd` takes its
value to 8192, whose resulting mixed word has rank `(0,13,12)`.
The rank increases because this source is outside the guard.

The order is defined semantically on proper words and this stopped
relation. No monotonicity under arbitrary string contexts is proved.
After a cap exit, raising the cap may raise the clock; it does not
provide a decreasing continuation of this order. Unrestricted
termination of the AYH system remains open.

## Exact bounded replay

[`fixed_integer_rewriting.py`](../../experiments/fixed_integer_rewriting.py)
checks every applicable rule occurrence in all proper words with
interior length at most six. It also checks leftmost, rightmost and
rotating schedules on a smaller complete corpus and selected binary
sources, including the sharp odd-clock witness 74475. Separate large
one-run sources have 64, 257, 1024 and 4096 bits. Their dynamic steps
check the same exact rank law; no numerical cutoff is used to infer
all-source coverage.

The checker independently decodes the mixed values and bitlength-sum
potential. It rejects an incorrect administrative value identity,
improper words, and the attempted unguarded step above. Merely counting
ternary letters is also shown not to replace `H`. Exact counts and the
literal schedule totals are in the frozen
[`rewriting-report.json`](../../reports/2026-11-20-fixed-integer-descent/rewriting-report.json).

```bash
python -X utf8 -B experiments/fixed_integer_rewriting.py \
  --compare reports/2026-11-20-fixed-integer-descent/rewriting-report.json
```

The finite corpus checks the implementation and local interfaces. The
universal guarded result depends on the written rank proof and the
separate complete cap-six certificate, not on extrapolation from that
corpus. No formal proof-assistant build is claimed.
