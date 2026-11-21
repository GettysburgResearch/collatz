# Independent written review of the physical merger route

**Verdict: the stated written deductions are valid with the displayed
hypotheses.** This review reconstructed the arithmetic and checked the
scope of the cited primary results. It does not certify a universal
merger, prove Collatz, or replace the separate Lean build receipt.

Reviewed source:

- `research/literature-reframe-20261122/PHYSICAL_MERGERS.md`
- SHA256 `bc31a74ea3797b5968e36652444eb45c88c902f0e17d662210a174f56bf6c0ff`
- Associated formal module `lean/PhysicalTailBarrier.lean`, SHA256
  `5a127bd32a9dd451696ccccd8bd963d1ea965a020a0f3cfee738f21d302293ec`.

## Reconstruction of the affirmative backtracing statement

For a residue `0<=r<2^h`, adding `2^h v` preserves the first `h`
shortcut parities. If the prefix contains `p` odd steps and ends at `e`,
its affine coefficient is `3^p/2^h`, giving
`T^h(r+2^h v)=e+3^p v`. When `p>0`, the occurrence of an odd step and
all subsequent halvings leave a nonzero residue modulo 3. Thus `e` is a
ternary unit. For unit target `q`, the fact that 2 generates the units
modulo `3^p` supplies the required exponent class for `2^k q=e mod3^p`.
Increasing `k` within that class makes the lift positive. The lifted
source reaches `2^k q` and then reaches `q` by `k` halvings. If `p=0`,
the range restriction on `r` forces `r=e=0`, and doubling handles the
case directly. The auxiliary zero residue does not produce a zero
actual lifted source.

This verifies (P1)–(P2), including the positive ordinary path, the residue
constraint, and the cofinal supply of representatives. The construction
does not give an upper height bound for a selected representative.

## Reconstruction of the all-parameter separation theorem

Let `z_t=T^t(z)`. In the shifted coordinate, an odd step multiplies
`z_t+1` by `3/2`, while an even step gives `(z_t+2)/2`. Consequently the
integer correction in (P3) transforms as

\[
 D_{t+1}=3D_t\quad\hbox{or}\quad D_{t+1}=D_t+2^t.
\]

Starting from `D_0=0`, both alternatives preserve `0<=D_t<3^t`.
The exponent is the actual odd-step count; an initially even source has
at most `t-1` odd steps when `t>0`.

Under (P4), `A-1` first halves, and the divisibility of `A+1` by `2^H`
forces the remaining first `a-1` steps to be odd for every `1<=a<=H`.
The exact shifted numerator is therefore `3^(a-1)(A+1)`. This verifies
the exponent `p_a=max(a-1,0)`, including `a=0`.

In a putative merger, cross-multiplication gives exactly (P6).
Both correction terms on its right are nonnegative and strictly less
than `2^H 3^H=6^H`, so their difference has absolute value below `6^H`.
Since it equals an integer multiple of `B>6^H`, that multiple must be
zero. Equality of the two left coefficients first gives `a=b` by their
2-adic valuations and then `p_b=p_a+r` by their 3-adic valuations. The
initially even erased branch instead has `p_b<=max(b-1,0)=p_a`. This
contradicts `r>=1`. The argument also directly proves the stated strict
necessary bound `B<6^H` for a merger when the other hypotheses hold.

Executing the initial rising runs gives the endpoints
`3^k u-1` and `3^(k-r)u-1`, whose shifted coordinates have ratio `3^r`.
Their smaller shifted coordinate is at least `u>6^H`. This proves the
substitution (P7) for every erasure depth, with unequal continuation
clocks allowed.

## The revised cofinal family and bit-height lower bound

For each `H>=1` and `s>=3H+4`, multiplication by `3^(3s)` permutes the
odd residues modulo `2^H`. Thus the chosen `c` exists uniquely and
`u=2^s+c` is odd. The resulting input satisfies

\[
 2^{4s}<n_s=2^{4s}+2^{3s}c-1<2^{4s+1},
\]

so its exact binary height is `d=4s`. Its offset is less than
`2^(3s+H)`. Using `4s+1<=8*2^floor(s/2)` and `s>=2H` bounds the marked
numerator by `8*2^(4s)`, strictly below the required `70*2^(4s)`.
The proper erased prefixes are odd and positive, so the preceding
packet's odd-prefix inheritance result applies with its stated domain.

The congruence for `c` gives `2^H | 3^k u+1`, and
`u>=2^s>6^H`. Therefore (P7) applies simultaneously to the whole erased
family. For the horizon assertion, the first `k=3s` steps increase the
source. Afterward every shortcut step is at least a halving. The endpoint
`3^k u-1` satisfies

\[
 \frac{3^k u-1}{2^s}\ge 2^k u-1=n_s
\]

because `3^k=27^s>=16^s=2^(k+s)`. This establishes the non-descent
claim through all `d=k+s` clocks, with the additive constants retained.

Finally `s=3H+4` gives `d=12H+16`. The separation theorem forces
`max(a,b)>H=(d-16)/12` for every successful post-run merger in the
displayed architecture. Thus the linear bit-height lower bound in (P9)
follows from the written family. The note correctly separates this
written specialization from the formal declarations (P3)–(P7).

## Literature scope checked

The semigroup characterization was checked against Applegate–Lagarias's
[author-hosted paper](https://websites.umich.edu/lagarias/doc/3x%2B1semigroup.pdf),
Theorem 1.1, and the [arXiv abstract](https://arxiv.org/abs/math/0411140).
It concerns multiplicative semigroup membership; the note preserves that
scope and does not interpret arbitrary multiplication as an ordinary edge.

Wirsching's [primary preliminary paper](https://www.math.uni-bielefeld.de/baake/algdyn/posden.pdf)
explicitly retains three conjectural gaps. Its Theorem 3 states strong
convergence on continuous functions and uniformity on bounded
equicontinuous families, matching the scope in the note. The theorem does
not itself cover changing unbounded atomic tests.

The [Monks primary sufficiency paper](https://monks.scranton.edu/content/pubs/SufficiencyRev4.pdf)
and the [four-author strongly sufficient sets paper](https://arxiv.org/pdf/1204.3904v2)
support the stated physical progression and `2 mod9` intersection results.
Their role here is correctly qualitative. No smaller-source selector is
attributed to them.

No mathematical revision was required by this review. The unresolved
step remains an actual source-bounded merger selector with unbounded
continuation clocks, or a different globally covering descent argument.
