# Independent review of the 13/6 inverse-credit packet

**Review outcome:** the supplied finite certificate and the universal
inverse-cone implication pass this review. This is an arithmetic conversion
result, not a proof of forward Collatz descent or termination. This review
does not establish literature priority or replace proof-assistant checking.

## Exact material reviewed

The symbolic agent's `PROOF.md`, `PROVENANCE.md`, `verify_credit.py`,
`credit_13_6.json.gz`, and raw `credit_m12_13_6.json` were inspected. The
antecedent was read directly at repository PR #141, commit
`5025ef464d4b6d4f4a412a3e33c3477de68dfa8b`, path
`research/ay-transversal-20261031/INVERSE_CREDIT.md`.

The raw synthesis JSON SHA-256 is

```
4c2b1b162df906d7f4283e2a068266357755ad43ec3a3a00e7327544bd676c36
```

The ordered potential-byte SHA-256 is

```
2f12342f3a4a25ff8ed31c03ddba77b66a17d8bfea62dfaac0c0ea1cbb3273dc
```

## Independent scalar verification

The separate script `verify_credit_independent.py` imports neither the
NumPy synthesis program nor the symbolic agent's verifier. Using unbounded
Python integers, it recomputes each candidate inverse numerator on all three
ordinary lifts, checking integrality, positivity, the nonzero residue modulo
three, and the credit inequality. The receipt is
`credit_independent_report.json`.

It verified 354,294 rows modulo 531,441 and 1,062,882 lifts of their selected
actions. The largest potential is 66. The minimum credit slack is zero;
the minimum terminal credit is one. The least accepted action is at most
ten in every row, although the exploratory synthesis allowed twelve.
Replacing the potential by zero fails at residue five.

The symbolic agent's final standard-library verifier was also run. It
passed the same full table check, its mutation test, and 6,575 forward
affine cone replays. The affine replays cover all unit constants through
ternary length eight and five selected constants at each of lengths 40,
100, and 1,000. These finite cone replays test the implementation; the
universal implication uses the argument below.

## Quantifiers and proof checks

Let \(M=3^{12}\). The table supplies, for each unit residue \(r\), one
action \(a\le10\) that works on all three values \(r+jM\), \(j=0,1,2\).
For \(c=r+Mq\),

\[
\frac{2^a c-1}{3}
=\frac{2^a r-1}{3}+2^a3^{11}q.
\]

Consequently its residue modulo \(M\) depends only on \(q\bmod3\).
Integrality and the unit condition also have the required lifting property.
The positive least representative gives positivity for every positive
lift. Thus the finite check proves the single-action, all-lifts inequality

\[
6a+V((2^a c-1)/3\bmod M)\le13+V(c\bmod M).
\]

In the symbolic state \(2^b3^s x+c\), an inverse block divides out one
factor of three without depending on the prefix \(x\). For \(s\ge2\),
the rank \(13s+V(c)-1\) decreases by at least \(6a\). At \(s=1\), choose
\(a=1\) or two according to \(c\bmod3\), and set the terminal rank to
zero. The available rank is at least twelve and pays the final cost.
No unit condition is needed after this last step.

The strict invariant \(0<c<2^b3^s\) yields a final binary suffix
\(0<r<2^k\). Each integral inverse source is odd. Its exact shortcut
block has one odd event followed by \(a-1\) even events. Reversing all
blocks therefore proves, for every positive integer prefix \(x\),

\[
T^k(2^k x+r)=3^t x+c,
\qquad
k\le\left\lfloor\frac{13t+V(c\bmod M)-1}{6}\right\rfloor.
\]

The final affine target may be even. The proof correctly describes that
edge as a literal shortcut block, rather than identifying its length with
the full odd-map valuation in every instance. All affine endpoints exceed
one for positive prefixes, and intermediate halving states also exceed
one. Thus the physical stop-at-one convention creates no hidden exception.

## Relationship to prior work and composition limits

PR #141 already supplied the inverse-cone interface, the same all-three-
lifts argument, the terminal rank mechanism, and a 7/3 finite-credit
certificate. The present verified table improves that explicit finite
lookahead construction to 13/6; it is not a new general proof method.

During review the parent located an external claim of an existential
\(2t+O(1)\) cone bound. The publication language should therefore compare
13/6 specifically with the repository's finite-lookahead, bounded-alphabet
credit certificate, rather than claim the best asymptotic bound for all
cone compilers. That external result is not required by this proof.

The compiler chooses a binary suffix; it does not prescribe its ternary
residue at a fixed ordinary target. A fixed-target steering theorem does
not follow by substituting a desired ternary residue for this output.
Likewise a sequence of separate finite-precision steering certificates
does not automatically retain digits through later divisions by three.
Newer external papers reportedly address such steering, so the safe
boundary is that the present packet neither proves nor uses such a
composition theorem.

The existing counting obstruction remains applicable: a compiler covering
all unit tails with worst length \(K\) must satisfy
\(\binom Kt\ge2\cdot3^{t-1}\). Its asymptotic threshold exceeds
\(\log_2 3\). Thus this same-prefix, all-tail interface cannot deliver a
strict numeric decrease in every case, regardless of its finite table's
size. The actual forward descent obligation remains unproved.
