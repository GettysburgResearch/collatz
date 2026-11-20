# A smaller sufficient system of functional identities

**PROPOSED elementary corollary of CR-002.** This is an abstract rigidity
statement. It does not establish the restricted ordinary merger hypothesis
used to obtain these identities from Collatz components.

Let \(F:\mathbb N_{>0}\to A\), for any set \(A\), satisfy

\[
F(2n)=F(3n)=F(n)\qquad(n\ge1),                       \tag{R1}
\]
\[
F(3n+1)=F(n)\qquad(n\text{ odd},\ 3\nmid n),        \tag{R2}
\]
\[
F(15n+1)=F(n)\qquad(n\text{ odd}).                   \tag{R3}
\]

Then \(F\) is constant. The multiplier-five invariance and multiplier-nine
law used by the [complete selector](PROOF.md) follow from this smaller
system; they need not be assumed separately.

**Derive multiplier five.** If \(x\) is odd and prime to three, (R3) at
\(x\) and (R2) at \(5x\) have the same upper expression:

\[
F(x)=F(15x+1)=F(5x).
\]

For arbitrary \(n=2^v3^i x\) with \(x\) odd and prime to three, repeated
(R1) gives \(F(n)=F(x)\) and \(F(5n)=F(5x)\). Thus
\(F(5n)=F(n)\) for every positive \(n\).

**Derive multiplier nine.** If \(n\equiv3\pmod4\), put
\(p=(15n+1)/2\). It is positive, odd, and prime to three. Using (R3),
doubling invariance, (R2) at \(p\), and the just-proved multiplier-five
invariance gives

\[
F(n)=F(p)=F(3p+1)
 =F\!\left(\frac{5(9n+1)}2\right)=F(9n+1).
\]

All four laws (A)--(D) of CR-002 now hold on exactly their stated domains.
Its complete integer descent proves constancy. No enlargement of the
domain of (R2) was used.

This proof identifies the algebraic mechanism: two legal affine
representations of the same integer force an additional multiplicative
identity. It supplies a shorter sufficient presentation of the conditional
rigidity theorem, not a claim that these are logically necessary or minimal
axioms. For actual Collatz component labels, the tripling and transferred
affine identities still depend on the open merger assumption.
