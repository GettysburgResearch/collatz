# Forward consequences of an all-word inverse potential

**Collatz remains open.** This packet proves exact arithmetic statements
about an inverse potential, its growth on a hypothetical escaping forward
orbit, and the limits of finite local tests. It does not establish a
uniform ordinary upper bound on the potential.

Use the odd Collatz map $U(n)=(3n+1)/2^{v_2(3n+1)}$ and legal inverse
letters $I_g(z)=(2^g z-1)/3$ on ternary units. The potential is

$$W(z)=\sup_{\text{all legal finite words}}(8k-5A),$$

where $k$ is the number of inverse odd edges and $A$ their total shortcut
cost; include the empty word. This is an **all-word supremum**, not the
selected-path minimum used by the earlier inverse compiler.

## Results and their limits

| Result | Exact scope |
|---|---|
| $h\{W\ge B\}\le(5/6)^B$ | Elementary normalized ternary Haar bound; no critical stationary theorem imported. |
| $\{W=\infty\}$ is dense and $G_\delta$ | Haar nullity does not separate this set from an ordinary integer using any finite residue precision. |
| Forward defect grows on escape | With $c_*=3/\log_2(3/2)$, every escaping ordinary orbit forces $W(n)-c_*\log_2(n+1)$ to grow at least $K\ln\ln n$ asymptotically, $K=(c_*-5)/\ln(\log_2 3)>1/4$. |
| Nontrivial ordinary cycles have infinite potential | The proof uses the exact drift above 32 and complete finite replay below that floor. It does not prove ordinary finiteness of $W$. |
| Positive noninteger rational cycles approximate any supplied ordinary unit at any fixed binary and ternary precisions | Their states can all exceed any prescribed real floor and have $W=\infty$. The nontrivial common denominator is explicitly retained. |
| Immediate ordinary convergers have arbitrarily large certified finite-word scores | $n_q=(2^{3^{q+1}+1}-1)/3$ satisfies $U(n_q)=1$ and $W(n_q)\ge3q$. Finiteness of the full supremum at these integers is not asserted. |

## Read the closure boundary before using a proposed bound

The apparently promising global bound

$$W(n)\le c_*\log_2(n+1)+\tfrac14\ln(1+\log_2(n+1))+C$$

would suffice to settle Collatz. It has **not** been proved.
Moreover, existence of such a bound is equivalent to Collatz together
with the additional unproved statement $W(1)<\infty$.
The simpler bound $W(n)\le5\log_2n+C$ is equivalent to the same pair
of assertions. Larger allowable error terms in these formulas do not
make their existential global statements logically weaker.

If $W(1)<\infty$, the bound

$$W(n)\le5\log_2n+W(1)+1$$

already follows on the actual basin of 1. Applying it outside that basin
would assume the membership that needs proof.

## Proofs and replay

- [Elementary potential, Haar tail, exact forward drift and cycles](PROOF.md).
- [Quantitative log-log growth on an actual escaping orbit](LOGLOG_GROWTH.md).
- [Exact equivalence and the remaining global obligation](CLOSURE_BOUNDARY.md).
- [Rational local countermodels and immediate-converger controls](RATIONAL_CYCLES.md).
- [Independent finite truncation reconstruction](check_potential.py).
- [Exact rational-cycle construction and replay](check_rational_density.py).
- [Investigation report and source pins](../../reports/2026-11-20-forward-closure/README.md).

Run the two standard-library programs from the repository root:

    python -X utf8 -B research/forward-inverse-defect/check_potential.py
    python -X utf8 -B research/forward-inverse-defect/check_rational_density.py

Their output checks bounded arithmetic interfaces. The infinite results
rest on the written arguments; neither program tests the missing global
bound or decides Collatz.
