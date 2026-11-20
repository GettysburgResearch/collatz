# A clock barrier for asynchronous mergers of shifted powers

**PROPOSED, unconditional.** This is an elementary consequence of exact
two-word cancellation, applied to the shifted-power obligations identified
in PR146 at `92820dd336b010215eb8a6eb4878a31b58a67656`.
It supplies a limitation and a certificate-propagation rule, not a successful
merger at an arbitrary exponent.

Use the shortcut map \(T\). For a binary parity word \(u\) of length \(p\),
let \(a\) be its odd count and \(A_u\) its affine offset:

\[
T_u(x)=\frac{3^a x+A_u}{2^p}.
\]

For every such word, including the empty word,

\[
0\le A_u\le3^p-2^p.                                \tag{1}
\]

Indeed appending an even letter leaves the numerator offset unchanged;
appending an odd letter at depth \(i\) replaces it by \(3A+2^i\).
The all-odd word maximizes this recurrence and has offset \(3^p-2^p\).

For \(c\ge0\), define the shifted constant

\[
D_u(c)=3^a c+A_u,\qquad
0\le D_u(c)\le(c+1)3^p-2^p.                        \tag{2}
\]

These are affine-word constants. A parity word legal at \(3^k+c\) is not
automatically legal at \(c\); no ordinary orbit of the center is asserted.

## 1. The two-word dichotomy

**Theorem.** Let \(k,l\ge1\), \(c,d\in\{0,1,2\}\), and suppose an actual
ordinary merger satisfies

\[
T^p(3^k+c)=T^q(3^l+d).
\]

Let \(u,v\) be the two actual parity words, with odd counts \(a,b\), and
put \(L=\max(p,q)\). At least one of the following holds:

- **Homogeneous identity:** \(p=q\), \(k+a=l+b\), and
  \(D_u(c)=D_v(d)\).
- **Clock lower bound:** \(L\ge\min(k+a,l+b)\ge\min(k,l)\).

**Proof.** Assume \(p\le q=L\), interchanging the arms if necessary.
After dividing the merger equation by the common factor \(2^p\),

\[
2^{q-p}3^{k+a}-3^{l+b}
=D_v(d)-2^{q-p}D_u(c)=R.                           \tag{3}
\]

The left side is divisible by \(3^N\), with \(N=\min(k+a,l+b)\).
Both nonnegative terms defining \(R\) are strictly below \(3^{q+1}\),
by (2), \(c,d\le2\), and \(2^{q-p}3^p\le3^q\).
Hence \(|R|<3^{L+1}\). If \(N\ge L+1\), divisibility forces \(R=0\).
Equation (3) then equates a power of two times a power of three with a
power of three. Unique factorization gives \(p=q\) and \(k+a=l+b\);
the shifted constants also agree. If \(R\ne0\), we instead have
\(N\le L\), as required. QED.

In particular, a genuinely unequal-clock merger needs at least
\(\min(k,l)\) shortcut steps on one arm. For two members of the same
triple \(3^k,3^k+1,3^k+2\), every merger with both clocks below \(k\)
has equal clocks and equal odd counts.

The theorem does not say such a short merger exists. It also does not
exclude mergers at larger clocks, or nonhomogeneous mergers whose clocks
already exceed the stated bound.

## 2. A short certificate automatically propagates in the exponent

In the homogeneous case, replacing \((k,l)\) by \((k+t,l+t)\) preserves
the affine endpoint equality for every integer \(t\ge0\). To preserve the
two actual parity words, choose \(t\) divisible by the multiplicative order
of 3 modulo \(2^L\): use period 1 for \(L\le1\), period 2 for \(L=2\),
and period \(2^{L-2}\) for \(L\ge3\).

Then the two new sources have the same residues modulo \(2^L\) as the old
ones. A length-\(L\) parity word is determined by that residue, so both
paths remain ordinary and legal. Their common endpoint follows from the
same identity. Thus a merger below \(\min(k,l)\) is necessarily part of
an infinite arithmetic progression of certified exponents.

This gives a precise alternative for a shifted-power attack: either find
and cover exponent classes by homogeneous certificates, or permit genuinely
asynchronous clocks growing at least linearly with the exponent. For
common-exponent triples, a fixed catalogue of unequal-clock words can
address only exponents at most its largest clock. In the general
two-exponent setting, the restriction is on $\min(k,l)$.

The last statement is a finite-catalogue limitation, not a prohibition on
adaptive constructions with unbounded word length.

## 3. General fixed nonnegative shifts

For arbitrary fixed nonnegative integers \(c,d\), put
\(C=1+\max(c,d)\) and \(s=\lceil\log_3 C\rceil\).
The same proof gives \(|R|<C3^L\). Unless the homogeneous identity holds,

\[
\min(k+a,l+b)\le L+s-1.                            \tag{4}
\]

For \(c=d=0\), this improves to \(\min(k+a,l+b)\le L-1\).
The source shifts are fixed in this statement; allowing them to grow with
the exponents changes the bound through \(s\).

## Verification and scope

`check_shifted_power_rigidity.py` reconstructs actual shortcut orbits,
independently recovers their affine offsets from source and endpoint, and
checks the dichotomy for every observed pair in its stated finite range.
For homogeneous certificates it replays positive exponent shifts using
the required period. The all-exponent conclusion follows from the proof,
not from that finite replay.

No external number-theoretic theorem is needed. A Subspace-theorem input
is unnecessary for this bounded-clock rigidity statement; the exact
ternary divisibility already supplies the conclusion.
