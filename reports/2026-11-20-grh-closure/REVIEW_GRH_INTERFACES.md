# Independent scoped review of the GRH interfaces

**Verdict: VERIFIED for the elementary deductions G1--G5 at the exact
hashes below, retaining the explicitly cited GRH theorems as SOURCE-QUALIFIED
inputs. No mathematical correction was required.** This is an independent
AI reconstruction and bounded arithmetic replay, not human referee
acceptance or formal verification.

| Frozen author object | SHA-256 |
|---|---|
| `GRH_INTERFACES.md` | `b78c2beca423087bbc6a130ba9af3127073ff86a48d81fd991f6dec4ae2ccba2` |
| `check_grh_interfaces.py` | `9144e66b97790f08ed5b20ae54c8c2455e449315640f1f3d9e19718e770fa22c` |

I read the complete note and checker and independently reconstructed the
algebra, quantifiers, height conditions and periodicity argument. I did
not import the author checker into the reviewer implementation.

## G1: what the prime selection actually certifies

The least-prime theorem is applied only to a reduced residue class modulo
2^H, with H>=2. Its bound gives a prime below
`2^(2H+1) H^2`, so the stated bit length follows directly. The affine
prefix identity and the binary parity-word bijection transfer exactly H
parities. They do not transfer full basin membership.

For the all-odd cylinder, writing `p+1=2^H a` gives the literal iterates
`3^j 2^(H-j) a-1` through j=H. Every required earlier input is odd and
positive, and the prefix strictly increases. Combining the lower size
`p>=2^H-1` and the conditional upper size gives the asserted
`(1/2-o(1)) log_2 p` lower bound on first descent. The words are finite;
no unknown subsequent orbit is called convergent.

I checked the primary bibliographic record of Bach--Sorenson and section
1.2 of [Carneiro--Milinovich--Quesada-Herrera--Ramos,
arXiv:2404.08380v2](https://arxiv.org/html/2404.08380v2). The latter explicitly
states the absolute GRH bound with `(phi(q) log q)^2` for q>3, which also
implies the coarser bound used in G1. The external analytic proofs were not
reconstructed or formally rebuilt in this review.

## G2: prescribed valuation level versus fully stripped core

The exact order `2*3^(e-1)` and the exponent for -1 follow from the
3-adic lifting identity. For an inverse at the prescribed level, the
strict height condition is

    (2^a-3^e)n < 1.

Because its left coefficient is an integer and `2^a=3^e` is impossible,
this is equivalent to `2^a<3^e`, with no discarded endpoint case.
The class n=-1 modulo 3^e forces
`a=3^(e-1) mod 2*3^(e-1)`. At e>=3 its least exponent exceeds the
allowed height budget. No assertion about a least prime can change this
exact congruence.

The count `floor(log_2 3^e)` of successful residue classes is also exact:
the eligible exponents are precisely the positive integers below
`log_2 3^e`, and are distinct modulo the full multiplicative order.

The critical caveat is correctly retained. Division by *more* powers of
three than the prescribed e can create a smaller actual core even if the
quotient at level e is large. The note does not exclude that repair,
arbitrary valuation choices, multi-step inverse routes, or a prior forward
excursion. This is a scoped obstruction, not a proof that inverse routing
can never work under GRH.

## G3: certified depth-one obstruction family

For `n_E=(2^(3^E+1)-1)/3`, the exponent `3^E+1` is even. Thus n_E is a
positive odd integer and its entire accelerated certificate is the single
step to 1 with that exact division exponent. Its ordinary shortcut clock
is large; the note does not confuse it with its odd depth one.

The key valuation is

    n_E+1 = 2(2^(3^E)+1)/3.

Since `3^E` is odd, elementary lifting gives
`v3(2^(3^E)+1)=1+v3(3^E)=E+1`. Division by three leaves **exactly E**.
In particular n_E is a ternary unit and is -1 modulo every 3^e for e<=E.
G2 therefore applies at every prescribed level 3<=e<=E on a source with
an explicit complete convergence certificate. This proves exactly the
claimed strengthening, while preserving G2's higher-actual-valuation caveat.

## G4: conductor/discriminant scale and its interpretation

For the cyclotomic field at 3^e, the degree is `2*3^(e-1)`. The standard
cyclotomic discriminant formula gives exponent

    e*2*3^(e-1) - 3^(e-1) = (2e-1)*3^(e-1),

as stated. Hence the displayed least-prime Chebotarev scale is of order
`e^2*9^e`. This comparison does not say a particular least prime must be
that large; it says the theorem supplies no uniform O(e) inverse-exponent
guarantee. G2 separately supplies an exact class where that guarantee is
impossible at the prescribed level.

The statement about prime exponents in the obstructing class is correct:
for e>=3 every positive exponent is divisible by at least 9. If a prime
instead denotes an auxiliary source or cofactor, an actual ordinary path
and the height budget remain separate obligations. No unstated Frobenius
encoding of an orbit is inferred. The note appropriately avoids claiming
logical independence between GRH and Collatz.

## G5: eventual periodicity forces constancy

Doubling invariance first transports eventual period q to every positive
input by multiplying both compared arguments above the threshold. Writing
q=2^r m and multiplying n and n+m by 2^r then removes the binary factor
from the period.

Modulo odd m, both parity choices have positive representatives, giving
`F(2a)=F(a)` and `F(3a+1)=F(a)`. If m=3^s d, iterating the second map s
times produces `3^s a+(3^s-1)/2`. Replacing a by a+d changes that input
by m, proving that d is a period.

Modulo d, both 2 and 3 are invertible. Conjugating the affine law by
doubling gives `F(3a+2)=F(a)`, as well as `F(3a+1)=F(a)`. Since 3a+1
runs over all residues, every adjacent pair agrees. This proves constancy
for an arbitrary codomain, including all modulus-one cases.

The fixed-conductor character conclusion follows because every finite
character combination is periodic at the common conductor. It does not
exclude approximate expansions with growing conductors; their required
error and conductor costs are left explicit.

## Independent bounded execution

`review_grh_interfaces_independent.py` imports no author routine. It checks
ordinary parity lifts, scans actual odd representatives for affordable
inverse exponents, computes `v3(n_E+1)` by literal repeated division, and
uses a separate breadth-first quotient graph for the periodic-label lemma.
The graph uses doubling and the affine map directly on odd moduli, unlike
the author's union-find on native shortcut edges for all moduli.

The normal and `-OO` executions produced byte-identical reports in
`grh-interface-independent-report.json`. Coverage and exact source hashes
are recorded there. Removing the affine law leaves three components
modulo seven, providing a negative control for the use of the odd-step law.

These finite examples do not prove GRH, the external least-prime bound,
or all-time convergence. The universal elementary claims rely on the
written reconstructions above. I did not rerun the author checker or
perform repository-wide validation in this review.
