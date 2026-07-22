# Cross-direction lemma forge: wave nineteen

Agent: `gpt56-synthesis-01`
Issue: `#29`
Branch: `agent/gpt56-synthesis-01/29-cross-direction-lemmas`
Date: 2026-07-22

## Scope

This compact final wave used the interfaces exposed by wave eighteen:

- generalize physical phase-return rigidity from the PR #35 `4 -> 5` chart
  to every binary expanding completion;
- identify exactly what remains after removing the visible Vandermonde from
  the combined period-ten determinants; and
- test whether the remaining cap connector word has a bounded low-bit scale
  law.

The first two directions produced theorem packets.  The cap direction found
a useful same-scale congruence and finite recurrence counterexamples, but no
source-uniform asymptotic theorem, so no cap claim was added.

## `T-9823` -- universal binary-chart oscillation

Let `U=2^a`, let odd `V>U`, put `C=V-U`, and suppose positive ordinary tails
greater than one satisfy

```text
U M_(n+1)=V M_n-C epsilon_n,
epsilon_n in {0,1}.
```

If `h<h'` are consecutive occurrences of symbol `s`, the return coordinate
`Z_n=M_n-(1-s)` gives the exact law

```text
v_2(VM_h-U+s(U-C))=a(h'-h).
```

With `alpha=log_U V`, both symbols and the phase-switch set meet every affine
multiplicative shell.  Each has logarithmic lower count `1/log(alpha)`, and
ordered switch positions have growth base at most `alpha`.

More sharply, if `r_j<r_(j+1)` are consecutive switch indices and
`s_j=epsilon_(r_j)`, the repeated flank symbol returns after
`r_(j+1)-r_j+1` steps.  Hence

```text
v_2(VM_(r_j)-U+s_j(U-C))=a(r_(j+1)-r_j+1),
r_(j+1)-r_j < (alpha-1)r_j+log_U(VM_0)-1.
```

This supplies a pointwise grammar criterion in addition to the averaged
switch floor.

Every finite word `epsilon_0...epsilon_(L-1)` also has one exact initial
residue cylinder

```text
M_0 = C V^(-L) D_L mod U^L,
D_L=sum_(j<L) epsilon_j U^j V^(L-1-j),
```

with infinitely many sufficiently large positive representatives.  Hence a
finite forbidden-block grammar cannot exclude an ordinary survivor in any
binary chart; the missing restriction must transport one-root coherence.

Specializations include

```text
4 -> 5:   v_2(5M_h-4+3s)=2(h'-h),
64 -> 81: v_2(81M_h-64+47s)=6(h'-h).
```

The second has logarithmic symbol/switch coefficient
`1/log(log_64 81)=18.1502565060...`.

## `T-9824` -- the visible Vandermonde leaves cubic height

For the row-factor-stripped combined-moment alternant `A_n(z)` of `T-9821`,
column expansion followed by ordinary Vandermonde division gives the exact
positive Schur sum

```text
A_n(z)/V_n(z)
 =sum_h (prod_j C_(h_j) lambda^(j h_j)) s_(mu(h))(z).
```

Its total-degree band is exactly

```text
(r-1)n(n-1)/2  through  (r-1)n(n+1)/2.
```

At the principal specialization `z_i=lambda^i`, the quotient `Q_n` has exact
orders

```text
v_2(Q_n)=54S(r-1)n(n-1)(n-2)/6,
v_3(Q_n)=-4{n gamma_*+9S(r-1)n(n-1)(2n+5)/6}.
```

Thus for every `r>=2` the quotient left after the obvious Vandermonde removal
already has cubic two-place height.  This proves that the visible common
factor alone cannot supply `T-9821`'s quadratic primitive-height target.  It
does not rule out further content shared across different Cramer minors;
their endpoint ratios remain only quadratic.

## Cap low-bit boundary

The exact same-scale relation from `T-9820` reduces modulo 64 to

```text
Z_m(a,b)=5-57J_m(a,b) mod 64,
J_m(a,b)=45-9Z_m(a,b) mod 64.
```

So the low six bits of `Z_m` and `J_m` are identical information, not a new
carry.  Exact finite source values rule out time-homogeneous update rules
based only on fixed `(a,b)` and `Z mod2` or `Z mod16`.  These are bounded
counterexamples, not an all-scale theorem.  The unresolved datum is still the
high quotient in the next-scale definition of `Z`.

## Review and non-results

- `T-9823` received independent checks of the return coordinate, terminal
  parity, strict floor endpoints, shell indexing, and finite-cylinder sign.
- `T-9824` received independent checks of its Schur partition, positivity,
  selector sums, valuation signs, and the limited scope of its cubic bound.
- Exact bounded replays were used only as redundant checks, not premises.
- Neither theorem constructs or excludes an ordinary survivor, proves a
  period-ten value irrational, or resolves any Collatz conjecture.

All claims remain `PROPOSED` pending external review.  No `K-####` candidate
is proposed.  The final memory snapshot remained healthy at 9.42 GiB free
with 38.9% of physical memory in use.

## Recommended next actions

1. In any binary-chart grammar, bound minority-symbol or switch counts above;
   `T-9823` supplies the exact universal lower target.
2. Factor content jointly across the normalized Cramer alternants rather than
   within one alternant; `T-9824` proves the ordinary Vandermonde is exhausted.
3. For the cap, retain the scale/high-quotient datum in `Z_m`; fixed low bits
   cannot support an autonomous update.
