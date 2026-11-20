# Attempt to remove the finite-exception boundary by uniform high-exponent rigidity

**OPEN.** This records a specific attempted strengthening, not a theorem of full convergence.

Source: PR146, `6863d298187af8b2619efbf78cc4b0aa8e627393`,
`research/upper-bit-mergers/STABILIZED_CORE_DESCENT.md`, especially its final section.

## The exact candidate theorem

Under eventual success of the source's `1 mod4096` tripling family, its stabilized label F has

\[
F(2n)=F(3n)=F(n)\quad(n>0),
\]

and

\[
F(3n+1)=F(n)\quad(n>0\text{ odd},\ 3\nmid n).
\]

For all odd w, the high-exponent law

\[
F(3^j w+1)=F(w)
\tag{J1}
\]

is valid at j≥6 when the relevant parameter `3^(j−1)w` exceeds the last exceptional source. Hence there is one finite J such that (J1) holds for every positive odd w and every j≥J. This is an implication under the stated source hypothesis, not an unconditional property of actual component labels.

The proposed stronger bridge would show that the three displayed laws force F constant for **every finite J**. The current source has a complete finite affine descent when exponents 6 through 10 are available everywhere. With finite exceptions, those same finite words remain available at all sufficiently large parameters and yield finitely many labels, but their small-parameter uses are not automatically justified. Establishing the proposed uniform-J theorem would remove this particular finite-component boundary.

## Three closing attempts and the exact missing steps

### 1. Lower an exponent by affine conjugation

Free tripling makes (J1) at J imply all its higher-exponent instances, by substituting `3^r w`. The tempting reverse substitution `w/3` is illegal when w is a ternary unit. Extending F to positive rationals with denominators supported on 2 and 3 makes the multiplicative identities well-defined; it does **not** extend the domain of the additive law (J1). Its required odd ordinary input remains missing.

Conjugating high affine maps by the available ordinary maps leads to the same issue: an inverse ordinary odd step is allowed in the low law only when its preimage is a ternary unit. Cancellation of affine coefficients does not establish that domain condition. No legal finite word lowering J on every ordinary input was found.

### 2. Use an ordinary inverse route to a high-valuation leaf

A concrete repair would keep a supplied positive ordinary input n fixed and find an actual inverse route whose final odd leaf x has high ternary valuation and whose ternary core is smaller than the original input. For a single inverse step,

\[
x=\frac{2^a n-1}{3},\quad e=v_3(x),\quad
\operatorname{core}_3(x)=\frac{2^a n-1}{3^{e+1}}.
\]

If e+1≥J, the high law makes this final step legal for F even though x is divisible by three. But the necessary strict descent is the additional inequality

\[
2^a n-1<3^{e+1}n.
\tag{J2}
\]

Solving `2^a n=1 mod3^(e+1)` by the fact that 2 generates the unit group provides congruence compatibility. Its exponent can have size comparable to `3^e`; it does not imply (J2). Multistep routing must similarly keep the actual supplied-source and height inequalities, rather than only hit a modular target.

The earlier inverse-cone compiler's numerical slope concerns affine words on all prefixes of a chosen endpoint class. It is not a bound for routing one supplied input to an independently chosen ancestor residue. The distinction is explicitly documented in PR151, `COMPONENT_RUN_PLACEMENT.md`, section 5. Substituting that numerical budget into this different routing problem would change a quantifier. The available supplied-target routing theorem also does not supply the height gain needed by (J2).

### 3. Upgrade finitely many labels to one label

The source's finite-image conclusion cannot simply be relabeled as constancy. Multiplication invariance by 2 and 3 alone admits nonconstant finite-valued functions; for example the indicator that an integer's prime-to-six core is one is invariant under both multiplications. That example is **not** a countermodel to all the proposed laws, but it disproves the isolated inference from finite image and multiplicative invariance to constancy.

The remaining additive laws must still be used on their exact domains. We found neither a theorem making the stabilized label automatic or continuous nor a new descent eliminating its finite exceptional core. A finite-valued or computable labeling does not acquire those stronger regularity properties automatically.

## Outcome

The uniform-J rigidity statement remains a precise possible strengthening of the latest thin-family criterion. The attempted algebraic and arithmetic repairs did not prove it. The separately proved depth-two family addresses another proposed route—induction whose cost is controlled solely by the known arm's odd stopping depth—and does not establish or refute this uniform-J statement.

No full Collatz proof, universal ordinary merger selector, or convergence of every residual exponential target follows from this note.
