# Pointwise Collatz continuation: paired fibers, complete denominators, and first landings

**Research checkpoint, 24 November 2026. Universal Collatz convergence remains OPEN.**

This packet adds an unconditional quantitative construction of paired first landings, an exact separation between diagonal and unequal endpoint fibers, and complete-denominator estimates for arbitrary positive Nielsen substitutions of a fixed seed. It also gives a uniform seed-complexity bound on one hypothetical escape or integer cycle. The proofs use the actual positive integer dynamics. The three new Lean modules certify the finite and integer statements specified below; the infinite analytic and Diophantine deductions are written proofs.

[Latest repository connections](LATEST_CONNECTIONS.md) · [Frozen source interfaces](SOURCES.json) · [Coordinator review](../../reports/astra-pointwise-resolution-20261124/ROOT_REVIEW.md)

Let
\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}
\qquad C=\{n>0:\exists h,\ T^h(n)=1\}.
\]

The previous, unchanged Lean theorem reduces full convergence to
\[
\forall k\ge0,\qquad 36k+8\in C\ \Longrightarrow\ 72k+17\in C.
\]
After two and three ordinary shortcut steps these inputs are
\[
A(k)=9k+2,\qquad B(k)=81k+20=9A(k)+2.
\]
The new work directly attacks this remaining implication. It does not prove it.

## 1. Prescribed common first landings, with an unconditional count

Fix a ratio \(1+\delta>1\), a clock modulus \(d\ge1\), a positive odd target \(a\le M\) prime to three, and a residue \(r\bmod d\). There are positive constants depending only on \(d,\delta\) such that every interval
\[
[X,(1+\delta)X],\qquad X\ge C_{d,\delta}M,
\]
contains at least
\[
\boxed{\quad c_{d,\delta}(X/M)^{2/5}\quad}
\]
different original parameters \(k\) for which both \(A(k)\) and \(B(k)\) first reach an odd value at most \(M\) at the same target \(a\), at the same shortcut clock \(t\equiv r\bmod d\). This is an unconditional written theorem. Its finite inverse-tree inequality and ordinary routing identities are kernel-checked.

The construction begins with the exact cylinder
\[
k=64v+12,\qquad T^6 A(k)=T^6 B(k)=243v+47.
\]
For every odd unit \(y\) and every total \(E\ge1461\), two legal inverse odd steps give
\[
m=\frac{2^Ey-2^v-3}{9}\equiv47\pmod{243},
\qquad T^E(m)=y.
\]
The exponent \(v\) is selected modulo the order of two modulo \(3^7\); both gaps are at least two. A variable but bounded choice of odd depth makes the source height fit the chosen interval while fixing its total clock modulo \(d\).

To obtain enough distinct incoming sources without an analytic atom theorem, use every unit-preserving inverse exponent \(2\le e\le20\). Put \(\lambda_e=2^e/3\). For every unit starting state, the legal four-step words satisfy
\[
\sum_w\left(\prod_{e\in w}\lambda_e\right)^{-2/5}>1.
\]
The rounded lower weights have common scale 10,000. Their minimum four-step numerator over all 243 residue classes is
\[
10\,261\,932\,046\,877\,717>10^{16}.
\]
Lean checks the weight inequalities and every residue. A finite stopping cut in the strictly increasing inverse tree supplies at least a constant times \((Y/M)^{2/5}\) distinct ancestors below \(Y\). The prescribed-total route then transfers them into the single residual cylinder, preserving the first landing and controlling multiplicity.

Under Weaver's stated first-landing theorem and its identified analytic inputs, the same construction improves the count to \(c_{d,\delta}X/M\). It also yields shrinking windows of width \(O(X/\log X)\) along an unbounded continued-fraction sequence of scales, with growing targets and a prescribed clock phase. The source-qualified linear estimate and the unconditional power estimate are distinct claims.

[Full construction, shrinking-window statements and exact dependencies](renewal/README.md) · [Lean](renewal/PairedLanding.lean) · [Independent review](transfer/REVIEW_RENEWAL.md)

## 2. Every unequal endpoint fiber has a quantitative height loss

Write
\[
X_i=T^i x,\qquad Y_i=T^i(9x+2),
\]
and let \(p_i,q_i\) count the odd inputs on these two actual paths. Put \(S_i=p_i+q_i\). The integer theorem proves
\[
\boxed{\quad X_h\ne Y_h\quad\Longrightarrow\quad
h\le S_h^2+6S_h+4.\quad}
\]

The key integer is
\[
D_i=3^{p_i}Y_i-9\,3^{q_i}X_i.
\]
Its vanishing forces a genuine meeting: exact ternary valuations in the affine carry equations give \(p_i=q_i+2\). Otherwise a joint run of \(L\) halvings forces \(2^L\mid D_i\), while \(|D_i|\le12\,3^{S_i}\). Summing the possible even runs over their increasing odd-count levels gives the displayed bound.

Consequently every member of the fixed unequal fiber \(X_h=A,\ Y_h=B\), \(A\ne B\), satisfies
\[
\frac{x}{2^h}\le
\max(A,B/9)\,
3^{-\max(0,\sqrt{h+5}-3)/2}.
\]
This concerns changing original sources with fixed endpoint marks. It does not assert that the square-root odd-count estimate is stronger than elementary estimates for one fixed starting integer.

The diagonal has a different exact extremum. If \(X_h=Y_h=Z\), then \(x<2^hZ/27\). Every source at or above \(2^hZ/81\) must satisfy
\[
x\equiv46\pmod{64},\qquad 2^hZ=27x+38.
\]
The governing odd positions are uniquely \((1,2,3)\) on the left and \(5\) on the right; the uniqueness equation is proved in Lean. Intersecting with \(x=9k+2\) gives precisely \(k=64v+12\).

For each fixed positive ternary unit \(Z\), this largest family is attained on infinitely many clocks even under the residual restriction. Hence the limsup of the largest \(x/2^h\) is \(Z/27\) on that diagonal and zero at every fixed unequal pair. Targets divisible by three have empty diagonal fibers.

We also give a literal twelve-step inverse branch preserving both futures. A failure at \(k=81t+69\), if supplied, produces a failure at \(4096t+3500\). The written continuation bounds the entire source population generated from a fixed pair by arbitrary bounded-clock inverse choices. For each fixed budget \(H\), its count is
\[
O_{H,z}\!\left(X^{\,1-\log_2(64/63)/H}\right).
\]
The proof includes isolated accidental returns and independent clocks. It therefore addresses varying bounded choices, beyond the failure of repeating one fixed branch. It leaves unbounded clocks open.

[Paired fiber proofs](transfer/README.md) · [Lean](transfer/PairedPrefix.lean) · [Independent review](arithmetic/REVIEW_TRANSFER.md)

## 3. Both complete denominators through arbitrary positive Nielsen moves

Start with the dictionary \(A=0,B=1\). Swap its members, or replace either by concatenation with the other on either side, any number of times. Fix a seed word containing \(a>0\) zero symbols and \(b>0\) one symbols. Let its expanded length and odd count be \(L,p\), and \(g=\gcd(a,b)\).

For the physical periodic phase let \(d_{\rm phys}\) be its reduced denominator. For the companion maps \(w\mapsto3w/2\) at zero and \(w\mapsto(3w+1)/4\) at one, let \(d_{\rm comp}\) be the corresponding reduced denominator. Along every expanding sequence of these dictionaries,
\[
\begin{aligned}
\log d_{\rm phys}
&\ge \frac1g\log\max(2^L,3^p)-o(L),\\
\log d_{\rm comp}
&\ge \frac1g\log\max(2^{L+p},3^L)-o(L).
\end{aligned}
\]
There is no limiting-density assumption in these lower bounds. In particular, coprime seed counts give the full leading logarithmic denominator in both coordinates.

At an irrational limiting density, both estimates become equalities with the same explicitly computable fraction \(c(w)\in[1/g,1]\). Define the seed suffix polynomial \(S_1(X,Y)\), set \(Z=X^{a/g}Y^{b/g}\), and factor
\[
G=\gcd(Z^g-1,S_1)
=\prod_{j\in J}\Phi_j(Z).
\]
Then
\[
c(w)=1-\frac{\sum_{j\in J}\varphi(j)}{g}.
\]
For the primitive seed 00101101 this fraction is \(3/4\).

The structural identity is the affine commutator
\[
K=(U-1)d_0-(V-1)c.
\]
It stays a unit outside two and three under every dictionary move. Thus the complete carry of the expanded word obeys
\[
(U-1)C=c(U^aV^b-1)+K S_1(U,V).
\]
This reduces cancellation to a fixed polynomial gcd on rational S-unit points. Corvaja–Zannier bounds it away from finitely many exceptional translates. Unimodular clock vectors exclude those translates at irrational density. At arbitrary density, the primitive-clock factor remains irreducible on every translate containing a dictionary point and has a positive root where the suffix sum cannot vanish. A fixed resultant then bounds cancellation there as well.

The exceptional analysis is necessary. The note gives an actual family where a higher cyclotomic factor acquires complete cancellation after specialization, despite being absent from the two-variable symbolic gcd.

[Complete fraction theorem](arithmetic/DENOMINATORS.md) · [All-density exceptional-translate proof](arithmetic/EXCEPTIONAL_TRANSLATES.md) · [Finite Lean identities](arithmetic/SeedDenominator.lean)

## 4. A pointwise restriction on the word of a hypothetical counterexample

On a fixed escaping ordinary orbit from \(n\), every used member of any such two-block expansion of a length-\(L\) prefix has length \(O(\log(n+1))\), uniformly in the dictionary and seed. Therefore its seed length satisfies
\[
r\ge\frac{L}{C\log(n+1)}.
\]
For a primitive positive integer cycle of period \(L\), the corresponding bound is \(r\ge L/[C\log(2L)]\).

The periodic repetitions of each dictionary member are mechanical words, with at most \(m+1\) length-\(m\) factors. Among \(m+2\) windows on an injective ordinary segment, two parity words agree. Their distinct initial states differ by a nonzero multiple of \(2^m\), while their heights grow by at most \((3/2)^{m+1}\). This bounds the mechanical segment by the logarithm of its starting height. The two successive used blocks are controlled at the same original source.

This lower bound does not supply an opposing upper bound. Indeed, every hypothetical escaping component has a fixed positive ancestor starting with parity bits 0011. Every prefix of that ancestor of length at least four has minimum seed length exactly its full length under these moves. A possible argument using a specially chosen later starting mark remains unresolved.

[Pointwise proof and the fixed-ancestor construction](arithmetic/README.md)

## 5. The remaining universal implication

The new constructions produce many actual pairs with a common future. The universal criterion requires controlling a prescribed pair whose futures are allegedly disjoint. Those are different retained events.

Under the frozen coalescence and natural-density inputs, the joint hitting set for two fixed odd unit targets has positive natural density precisely when the targets are forward-comparable. At \(k=3\), the pair is \((29,263)\). Both reach one, but neither reaches the other, and the joint hitting set has density zero despite containing this ordinary witness. Lean checks the two complete finite traces and their incomparability.

Thus existence of an occupied fiber and positive marginal target densities do not force a positive joint proportion. The paired prefix bound, the common landing construction, and the denominator theorems have not supplied the missing one-source implication. The previous equivalence remains a criterion, not a proof of Collatz.

## Verification and reproduction

The aggregate audit targets all public declarations in the three new Std-only modules, using Lean 4.34.1 and warnings as errors. It appends complete axiom reports, allowing only propext, Classical.choice and Quot.sound. Both new exact Python controls also run normally and with optimization, with identical output required. The checks concern this continuation; older Lean packets are not rebuilt.

| Module | Public declarations | Certified scope |
| --- | ---: | --- |
| SeedDenominator.lean | 6 | Affine commutator and suffix identities, clock determinant, initial values, finite window-count budget |
| PairedPrefix.lean | 6 | Proportionality implies meeting, even-run and total-clock bounds, marked source-height bound, actual inverse branch, unique extremal word equation |
| PairedLanding.lean | 6 | Iteration, residual cylinder, two-gap route, actual incomparable targets, ordered visits after fusion, finite four-generation cut inequality |

The real-valued asymptotics, stopped-tree growth proof, whole-word mechanical coding, polynomial factorization and imported Diophantine and analytic theorems remain written mathematics. The Lean file does not state full convergence.

Run:

    python -X utf8 -B research/astra-pointwise-resolution-20261124/check.py \
      --lean /path/to/lean-4.34.1/bin/lean \
      --out /path/outside/this/packet

[Executed kernel and control receipt](../../reports/astra-pointwise-resolution-20261124/kernel/CHECKS.json) · [Final source hashes](../../reports/astra-pointwise-resolution-20261124/SOURCE_HASHES.json)
