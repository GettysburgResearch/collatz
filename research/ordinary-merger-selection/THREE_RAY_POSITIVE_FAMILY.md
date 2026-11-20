# A fixed 37-step merger with a factor-three smaller partner

**PROPOSED, unconditional.** All paths use the positive shortcut map
\(T(n)=n/2\) for even \(n\), \(T(n)=(3n+1)/2\) for odd \(n\).
This is an explicit successful class, not a complete three-ray selector.

Put

\[
M=2^{37}=137438953472,\quad r=84997906089,\quad
A=1577799630949,\quad C=523998152183.
\]

Read the following parity words from left to right, starting at time zero:

```
u = 1011111111011011110101111011100001100
v = 1101101101011011100110110110110101101
```

Both have length 37. Their odd counts are 25 and 24, respectively, and
their affine numerator offsets are both \(A\). Thus, for every \(t\ge0\),
with \(m=r+Mt\) and \(N=3m\),

\[
\boxed{T^{37}(m)=T^{37}(N)=C+3^{25}t,\qquad m=N/3<N.} \tag{1}
\]

## Exact proof and ordinary legality

For a word of length \(h\) and odd count \(q\), write its affine map as
\((3^q x+B)/2^h\). Start at \(B=0\); an even letter leaves \(B\)
unchanged and an odd letter at position \(i\) replaces it by
\(3B+2^i\). This reconstructs both displayed offsets and counts.
The exact congruence \(3^{25}r+A\equiv0\pmod M\) gives the source class
of \(u\). Its endpoint is \(C+3^{25}t\). The affine endpoint of \(v\)
at \(3m\) is identical, because \(3^{24}(3m)=3^{25}m\).

Final integrality selects the physical parity word: a length-\(h\) word
has exactly one source class modulo \(2^h\), and its affine numerator,
whose source coefficient is odd, has exactly one integral class as well.
The physical class satisfies that congruence, so they coincide. Positive
starts retain positive actual iterates. Hence both words in (1) are legal
ordinary paths, not merely formal affine expressions.

## Arbitrarily long failure of direct forward descent

Every nonempty prefix of \(v\), of length \(i\) and odd count \(b_i\),
satisfies \(3^{b_i}>2^i\). It suffices to check the ends of zero steps:

| \(i\) | \(b_i\) | \(i\) | \(b_i\) |
|---:|---:|---:|---:|
| 3 | 2 | 6 | 4 |
| 9 | 6 | 11 | 7 |
| 14 | 9 | 18 | 12 |
| 19 | 12 | 22 | 14 |
| 25 | 16 | 28 | 18 |
| 31 | 20 | 33 | 21 |
| 36 | 23 | | |

An odd step increases the corresponding multiplier by \(3/2\).
The nonnegative affine offsets therefore give \(T^i(N)>N\) for
\(1\le i\le37\).

For any prescribed \(L\ge0\), choose

\[
t\equiv(-1-C)(3^{25})^{-1}\pmod{2^L}.              \tag{2}
\]

The common endpoint is then \(-1\pmod{2^L}\), so its next \(L\)
shortcut steps are all odd. Each strictly increases a positive value
greater than 1. Thus infinitely many positive sources in (1) have

\[
T^i(N)>N\quad(1\le i\le37+L),
\]

while retaining the same fixed 37-step merger with the smaller source
\(N/3\). The source varies with \(L\); no single source is claimed to
resist every horizon.

Moreover, a positive multiple of three has no smaller positive ancestor:
its only inverse shortcut predecessor is its double, and this remains a
multiple of three. All its predecessors are therefore \(2^jN\).
The merger in (1) is genuinely two-sided, and is not a smaller-ancestor
certificate for \(N\).

Any exact ternary valuation \(v_3(N)=a\ge1\) can be imposed simultaneously
with (2): prescribe \(r+Mt\equiv3^{a-1}\pmod{3^a}\), then use CRT.

## Scope and the attempted transport to arbitrary parameters

For \(E_3(x)\) denoting \(x\sim3x\), dyadic scaling gives
\(E_3(2^j x)\Longleftrightarrow E_3(x)\). The displayed certificate thus
covers every parameter whose odd part is \(r\pmod M\). It does not change
an uncovered odd part into a covered one. Every other odd residue modulo
\(M\) is a hole in this particular guard.

There is an exact limitation on a natural attempt to enlarge it. Suppose
an affine lift \(R(x)=\alpha x+\beta\) and fixed physical words return
\(R(x)\) to \(x\), and \(3R(x)\) to \(3x\), identically on infinitely
many parameters. Equality of slopes forces the two words to have the same
clock \(h\) and odd count \(q\), with \(\alpha=2^h/3^q\). Their constants
then require \(B_v=3B_u\). If \(q>0\), each word offset is a unit modulo
three, by its last odd term, which is impossible. Hence \(q=0\), both
offsets vanish, and \(R(x)=2^h x\).

This excludes only uniform direct-return lifts of that form. It does not
exclude more general two-sided transports, parameter-dependent words, or
finite-hitting terminal certificates. In particular multiplication by three
cannot be used to move an arbitrary parameter into the class: that is the
unproved invariance being sought.

## Relationship to the source packet

PR146 at `561d48a4d3a793a59b1cdf0406062ae1a6d47515` already constructs
successful subclasses for compatible affine slopes in every binary class
(`AFFINE_RAYS.md` and `PREFIX_COMPRESSION.md`). Its negative-five checkpoint
also gives additive smaller partners beyond a protected prefix. No novelty
is claimed for those general mechanisms. The contribution here is this
specific fixed-clock, factor-three certificate with every prefix of the
larger arm noncontracting, together with the explicitly qualified selector
boundary. `FIVE_RAY_RECURSION.md` uses it as a parameter-decreasing guard.

Fresh PR146 head `7d04c4dd756cfe495eb3eee78eba35a99085cd2a` adds
`THREE_RAY_SMALLER.md`; its independent smaller-input certificates must be
credited when integrating this fixture. The present guard has
\(r\equiv1\pmod8\), whereas the reported new seven-certificate exclusion
concerns a least failed odd input \(7\pmod8\). These are different guards;
no disjointness or dominance of their full consequences is asserted here.

`check_merger_selector.py` independently reconstructs the words and replays
ordinary instances, including the arbitrary-horizon and CRT controls.
