# Independent review of the nonhomogeneous boundary

**Verdict: PASS for NB1–NB3 at the hashes below.** The result is an exact
architecture boundary for homogeneous transport from terminal base 1.
It does not establish nonconvergence of any positive integer, rule out
nonhomogeneous certificate methods, or prove Collatz.

## Frozen inputs and scope

| Input | SHA-256 |
|---|---|
| `NONHOMOGENEOUS_BOUNDARY.md` | `2fe095a83e155f80dc7ed97c306ea24e00c169e196a6570fa271a20886d686c3` |
| `check_nonhomogeneous_boundary.py` | `592f17558fc0280576fc1d13114dc4e312e680809cd54e665ff3fdd3813629a9` |

The files were reviewed in
`collatz-global/research/global-certificate-closure-20261121`.
The final checker-description wording was corrected from “endpoint
certificates” to “positive odd endpoints” before these hashes were taken.
The arbitrary-endpoint loop proves legal prefixes, whereas the NB2 loop
supplies complete first-hit certificates. No reviewed source file was
edited by this reviewer.

## NB1: correction sum and physical target clock

For the source word \((1,3^m,b)\), with the superscript denoting repeated
letters, the odd positions are

\[
0,\ 1,\ 4,\ldots,3m+1.
\]

Their affine correction is exactly

\[
B=3^{m+1}+2\sum_{j=0}^{m}3^{m-j}8^j
  =\frac{3^{m+2}+2\cdot8^{m+1}}5.
\]

This identity is independent of the final gap \(b\). With
\(p=m+2\), \(h=3m+4\), and \(L=h+b-3\), it gives

\[
3^p(5x+1)=2^h(5\cdot2^{b-3}q-1).
\]

Since \(\gcd(3^p,2^h)=1\), the declared \(K\) is integral; its
numerator and denominator are odd, and it is positive. Thus
\(\nu_2(5x+1)=h\) is exact. The subsequent formula

\[
T^t(5x)=2^{h-t}3^tK-1\quad(0\leq t\leq h)
\]

describes the actual positive shortcut trajectory. Every input with
\(t<h\) is odd and greater than one, and the endpoint \(E=3^hK-1\)
is even and greater than one.

The clock distinction in the note is necessary and correct. The first
\(h-1\) accelerated gaps are one, but the \(h\)-th accelerated gap is
exactly \(1+\nu_2(E)>1\). Thus the computation uses \(h\) odd shortcut
inputs, not \(h\) accelerated exponent-one steps. The independent replay
checks this distinction explicitly.

## NB2: actual first-hit sources at every rank

The elementary valuation identity
\(\nu_3(4^{3^j}-1)=j+1\) gives order \(3^p\) for 4 modulo
\(3^{p+1}\). Since \(2\equiv-1\pmod3\), the order of 2 is exactly
\(2\cdot3^p\), the number of units in that residue ring. Consequently
the discrete logarithm in NB5 exists and is unique modulo that period.
Its parity is odd because the congruence modulo three is
\(2\cdot2^s\equiv1\).

The selected residue makes \(K\equiv c\pmod3\); the stated parity
choice of \(c\) makes \(2^hK\equiv2\pmod3\). The source therefore
satisfies \(x\equiv2\pmod3\). Its integrality also follows directly by
multiplying the NB5 congruence modulo \(3^p\) by \(2^h\) and using
\(5B=3^p+2^h\). Oddness follows from the numerator
\(2^L-B\), since \(B\) is odd.

Backward construction of the full word from 1 proves every intermediate
inverse integral and positive odd. The last inverse \(I_b(1)>1\)
because \(b\ge4\). No earlier inverse of an odd value greater than one
can equal one: that would require \(2^a u=4\) with odd \(u>1\).
Therefore the source certificate is genuinely first-hit and has rank
\(p\), without hidden terminal padding.

Increasing \(s\) by its exact positive period gives infinitely many
distinct ordinary sources at each \(p\ge2\). The target needs at least
\(h=3p-2\) odd inputs if it ever reaches one. Neither this rank lower
bound nor the construction presumes that the target converges.

## NB3: grade obstruction and terminal padding

For a convergent positive integer \(n\), the first-hit product identity is

\[
2^{d(n)}=n\prod_{i\text{ odd input}}(3+1/n_i).
\]

Before the first hit, every odd input is at least three. Dividing by
\(4^{o(n)}\) proves \(2^{g(n)}\leq n\), including the even-input-only
case. The argument does not need a bound on an unknown stopping time.

For an NB2 source, the fixed target prefix has \(h\) clocks and \(h\)
odd inputs, with no earlier arrival at one. If the target converges, its
grade decomposes as \(g(5x)=-h+g(E)\). Since
\(g(x)=m+b-3\), substitution gives exactly

\[
2^{g(5x)-g(x)}
\leq\frac{E}{2^{4m+b+1}}
<\frac{45}{16}\left(\frac9{16}\right)^m<4.
\]

The strict upper estimate simply drops the positive quantity
\(3^{2m+2}+1\) from the numerator. The resulting grade difference is
strictly less than two.

Conversely, a homogeneous complete transport with equal clocks and odd
counts on its two arms, ending at 1 and 5, would force that difference to
be exactly \(g(5)-g(1)=2\). A path reaching 5 cannot previously have
reached 1, because the ordinary orbit of 1 stays in its two-cycle. Adding
terminal source cycles changes clock and odd count by \((2,1)\), and
therefore cannot change this grade contradiction. Composition of any
finite number of homogeneous blocks preserves equality of both counts.

If the target does not converge, it cannot reach the known convergent
terminal 5. The two cases establish the boundary without assuming target
convergence. The restrictions to terminal base 1 and homogeneous blocks
are explicit and essential; a different terminal family, unequal counts,
or a guarded nonhomogeneous construction is not excluded.

## Independent replay

`review_nonhomogeneous_boundary.py` imports no author checker functions.
It independently constructs source words backwards, solves exponent
congruences by direct cyclic enumeration rather than ternary lifting, and
checks the exact target shortcut prefix and final accelerated-gap
distinction. It replays 56 arbitrary positive odd endpoint prefixes and
12 actual first-hit sources at ranks 2, 3, 4, 5, 7, and 10. It separately
checks the correction recurrence, the exact rational grade majorant, and
invariance under terminal padding.

Normal and `python3 -OO` runs of this independent checker both passed.
The author's checker also passed independently in both modes, with
328 endpoint-prefix checks, 18 first-hit examples, and the same report
SHA-256 in each mode:

```text
5d7d484f4a742b1e39f5ba1139220ad37d45085302d673fd17b1142d8cc5c2c5
```

The universal conclusions rest on the displayed identities, the exact
order argument, and the grade inequality. The finite replay is
implementation evidence. Attribution to the prior grade invariant,
complete homogeneous recognizer, and stronger rank-one overhead
obstruction is preserved; this review makes no new priority claim.
