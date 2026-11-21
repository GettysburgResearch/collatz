# Cofinal collisions of binary exponent and trailing-one depth

This is a structural result about the narrowing section of PR #173, frozen at
`fa0c9e2a2851e6324391e39c17afcb5913185aec`. It does not prove universal Collatz
convergence. The formal construction is `BandCollision.lean`; its ordinary
word and congruence selector are in the companion `BandWord.lean`.

## Statement

For every natural cutoff `B`, there are distinct ordinary positive integers
`n,m` and a positive shortcut clock `t` such that:

- `n` and `m` are marked and exceed `B`;
- `T^t(n)=m`;
- `floor(log2 n)=floor(log2 m)`;
- `n=m=1 (mod 4)`, so both have exact trailing-one depth `v2(x+1)=1`;
- `(B+1)*2^t<=n`.

The last inequality is stronger than a bound on the two endpoints. Since
`x<=2*T(x)` for every ordinary positive input, it implies that every intermediate
state through clock `t` also exceeds `B`.

Consequently, no function of just binary exponent and trailing-one depth,
with values in a strict ordered rank domain, can strictly decrease on every
positive marked return beyond a finite cutoff. The function need not be
linear or monotone in either coordinate. An orbit segment whose two feature
pairs agree contradicts a strict decrease across its successive marked
returns. This conclusion does not exclude a rank using additional information
or a proof using a variable number of complete returns at each descent.

## Construction

Set `N=B+64`. The source's rational approximation theorem, together with
`3/2<log2(3)<2`, supplies integers `p,t` with

`4<=p<=N`, `p+2<=t<=2N`,

and

`N*3^p <= (N+1)*2^t <= (N+3)*3^p`.

The displayed multiplicative bounds follow directly from the logarithmic
approximation. If `|log(D/A)|<=1/u` with `u>=2`, the standard inequalities
`log(r)<=r-1` and `1-1/r<=log(r)` give

`(u-1)*A <= u*D <= (u+2)*A`.

Now put

`P=2^(8N)`, `Q=floor(P/(N+1))`, `L=P+4Q`.

The padding inequalities are

`Q>=N+1`, `Q>=8*3^p`.

They use only `N+1<=2^N`, `p<=N`, and elementary comparisons of powers.

The Chinese remainder theorem selects an ordinary `m` with

`L<m<L+8*3^p`, `m=1 (mod 4)`,

and

`2^t*m+2^(p+1)=5*3^(p-1) (mod 3^p)`.

Define the natural integer

`n=(2^t*m+2^(p+1)-5*3^(p-1))/3^p`.

The chosen range makes the numerator nonnegative and the congruence makes
the division exact. The resulting identity is

`3^p*n+5*3^(p-1)=2^t*m+2^(p+1)`.

It implies `n=1 (mod 4)`. Write `h=t-p-1`. The actual legal word consists of
the first two shortcut steps, then `p-1` increasing odd steps to `2^h*m`, then
`h` halvings to `m`. Thus its total shortcut clock is `t`. This is a proved
forward computation on the selected ordinary integers, rather than a formal
parity word whose source is left unrealized.

## Both endpoints remain in one marked octave

Write `A=3^p`, `D=2^t`, `C=5*3^(p-1)`, `E=2^(p+1)`. The affine identity is
`A*n+C=D*m+E`, with `C<=5A` and `E<=2A`. The multiplicative bounds imply

`N*m <= (N+1)*n+5*(N+1)`,

`(N+1)*n <= (N+3)*m+2*(N+1)`.

The interval selector and padding give `P+4Q<=m<=P+5Q`. Elementary integer
arithmetic then yields

`P<=n<=P+8Q`, `P<=m<=P+8Q`.

Both values lie below `2P`, so their binary exponent is exactly `8N`.
For either endpoint `x`,

`(8N+1)*(x-P) <= (8N+1)*8Q <= 64*(N+1)*Q <= 64P < 70P`.

This is the exact mark test.

The endpoints are distinct. The multiplier numerator `3^p` is odd and
denominator `2^t` is even. If `n=m`, their difference in the affine identity
would imply `n<=C` or `n<=E`. But `n>=P>=8*3^p`, while `C<=5*3^p` and
`E<=2*3^p`.

Finally, `B+1<=2^N`, `t<=2N`, and `n>=2^(8N)` give

`(B+1)*2^t <= 2^(3N) <= n`.

## Scope of the result

All quantified objects are ordinary natural integers. The cutoff is arbitrary,
and the full intervening path stays above it. The result rules out a proposed
class of ranks; it supplies neither a nonconvergent orbit nor a nontrivial
positive cycle. The required eventual marked-return descent remains open.
