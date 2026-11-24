# Top determinant, full numerical denominator, and the clock-series boundary

**Pins.** PR194 `b1bf1f151a2da8936f80d229f132d0b7539ba42c`,
`research/astra-birth-rigidity-20261124/TOP_COMPONENT.md`, theorem parts 1–3,
and `LATEST_SOURCE_SYNTHESIS.md`, LS2. The zero criterion is PR191
`37b3916633cd32a0c173b20bb18ec3a7ec290a63`, TCP-4 (9).
The comparison is PR192 `be783656f0e889fe0d5318a2f7a9140099cb94b5`,
`research/astra-phase-and-cycle-20261124/CYCLE_FACTORS.md`, §§3–4, and PR196 R1.

**Top-component theorem — verified written argument, with the rational
binomial irreducibility criterion as imported in the source.**
Set A=ga, p=gb, (a,b)=1. At a root z of the degree-bφ(g) component,
w=2^a/z^b is a primitive g-th root. Regrouping z^(1−p)Q(z) by odd index
modulo b gives Σ z^(−i)P_i(w), with the j-th coefficient in row i equal
to 2^(d_{i+jb}−aj). For odd g, reduction of X^g−1 at 2 is squarefree,
so 2 is unramified in Q(w). A monic degree-e factor of Z^b−2^a/w has
constant-term valuation ea/b since every root has valuation a/b; hence
b divides e and the binomial is irreducible there. For g=2^t, the
component is Z^(bc)+2^(ac), c=2^(t−1). Negative sign excludes a square;
an odd prime divisor of bc divides b but not ac. The exceptional −4
times a rational fourth power in the binomial criterion requires 4|bc
and ac≡2 mod 4, exactly g=4 and b even. In the irreducible cases the
extension degree b forces every row to vanish at w if Q(z)=0. For
g=ℓ^t, divisibility by Φ_g repeats each row of coefficients with period
g/ℓ, exactly equivalent to an A/ℓ shift of the marks. The reverse
implication follows by the same row identity. For g=1 the positive rows
cannot vanish. This independently agrees with PR192's prime-power
survival theorem in the same range. PR192 also describes polynomial
survival on the split case; PR194 exhibits explicit primitive partial
cancellation there. The quantifier over clock ratios is essential:
the exceptional g=4 does not force vanishing for each primitive word.

**Exceptional witnesses and arithmetic.** The g=4, A=28, p=16 example
has common quartic Z^4−16 Z²+128 and loses only 65 of its numerical top
factor 22945. For g with distinct prime divisors r<s, the three rows of
the (5g,3g) example each sum to zero at primitive g-th roots (cosets are
full root-of-unity sums). The indicator periods g/r and g/s have lcm g;
every putative repetition count divides g and would have to preserve both.
Thus the word is primitive and the monic top polynomial divides Q in Z[Z],
giving complete top numerical absorption. These statements distinguish
zero determinant, partial numerical cancellation, and total absorption of
one component.

**LS2 — verified for the actual common reduced denominator d.** Only r−1
marks of the r-grid lie off the s-grid, leaving one of its s interiors
untouched. Its L=g/s−1 consecutive baseline blocks have affine
map (27x+37)/32 with fixed center 37/5. All mixed boundary states satisfy
37/5<x≤58/5 by contracting cyclic extrema, with strictness at the minimum
because a nonbaseline block occurs. Subtracting the baseline fixed path
across L blocks and multiplying by 5d gives 32^L | (5dx−37d). The
integer on the right lies in [1,21d], proving 21d≥32^(g/s−1). This
estimate can stay bounded if s varies with g. It coexists with complete
top cancellation. R1 instead compares two rotations of the *same* cycle
and gives the divisor D/gcd(D,C_v−C_v') of d from their common suffix.
LS2 compares a run to an *external* fixed rational baseline. Neither
claim forces its respective match on an arbitrary word.

**Full-gcd limit.** PR192 §4 supplies examples in which every determinant
is nonzero and every numerical component divides its determinant; the
TCP-4 denominator certificate is then one even with a nonintegral actual
cycle. Conversely top absorption alone cannot make the entire candidate
integral, as LS2 demonstrates. The unrestricted requirement is still to
exclude D|Q(3) for every nonstandard primitive contracting word, or prove
another universal obstruction.

**PR195 GS1 — source-qualified scope.** At
`a24ef018147a1e16bf314d14085e2d0d6c620d32`,
`research/astra-global-closure-20261124/analytic/README.md`, GS1 is
for a fixed positive odd ordinary source with exact valuations g_j
and A_n=Σ_{j<n}g_j. Its formal series has coefficients 2^A_n. Eventual
periodicity of its states, eventual periodicity of its gaps, rationality
of this series, and D-finiteness over Q(z) are equivalent. The 2-adic
telescope gives uniqueness of an ordinary state from an infinite gap tail.
The D-finite-to-periodic implication imports Bell–Smertnig for coefficients
in a finitely generated multiplicative group. Its disjoint progressions
give affine exponents on residue classes; monotonicity sandwiches them
between consecutive values of one class and forces equal slopes. This
cross-review did not independently establish the imported theorem. The
single 2-adic value at 1/3 holds for every source and supplies no differential
equation. Even universal D-finiteness would leave nonstandard cycles to
exclude.

**Execution.** Fresh replay of PR194's pinned check_top_component.py checked
11,957 normalized contracting words, 11,495 equivalences (70 repeated
words), the quartic arithmetic, and twelve mixed-prime cases. No new
Lean replay, LS2-specific numerical replay, or PR195 execution was performed.
