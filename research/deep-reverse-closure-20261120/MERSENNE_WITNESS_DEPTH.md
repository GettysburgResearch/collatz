# Cheaper reverse witnesses for the hard rank-five Mersennes need unbounded depth

**PROPOSED.** This theorem concerns a particular predecessor-witness
architecture. It does not exclude an unbounded successful algorithm,
general ordinary paths with forward excursions, or full Collatz.

K3 in `REVERSE_CERTIFICATE_KERNEL.md` identifies the rank-five
fourth-gap-five case with

\[
e=119+162j,\quad j\ge0,\quad P=2^e,\quad M=P-1,
\]

and the known upper antecedent

\[
X=\frac{1024P-2573}{243},\qquad
Y=\frac{X+1}{2}=\frac{512P-1165}{243}.
\tag{1}
\]

The upper has a complete five-odd-input certificate; `Y` reaches
`M` along ordinary odd gaps `(2,2,2,1,2)`. If it were a least failure,
one way to contradict minimality would be to find another ordinary
predecessor `Y'` of `M` with

\[
Y'\equiv65,129,193\pmod{256},\qquad
X'=2Y'-1<X,\qquad X'\in C.
\tag{2}
\]

The residue condition makes `X'` an eligible upper antecedent of
the deep reverse criterion. This note proves that the number of
odd steps required from `Y'` to `M` cannot be bounded uniformly in
this exact exponent progression. In fact the lower bound below
does not even require the last condition `X' in C` in (2).

## W1. A rational-center obstruction

Let an inverse odd word have positive exponents `a_1,...,a_q`,
where each move is `I_a(v)=(2^a v-1)/3`, starting at `M=P-1`.
Write its endpoint as

\[
Y'(P)=\frac{2^A P-D}{3^q},\quad A=\sum_i a_i,\quad D>0.
\tag{3}
\]

If this word is integral at the ternary parameter

\[
P_*=11/4,
\tag{4}
\]

and its binary residue is one of the three residues in (2),
then its upper slope cannot be less than `1024/243`.
At equality, the only possible word with those properties is
`(2,1,2,2,2)`, which gives exactly the original `Y` in (1).

**Proof.** The center starts at `M_*=7/4`, which is one modulo
three. Integrality of the first inverse forces its first exponent
to be even and at least two. Its first output is therefore a
positive integer, namely `(7*2^(a_1-2)-1)/3`. Every subsequent
integral inverse output is again a positive integer.

Assume the upper slope is at most `1024/243`. The center endpoint
`V=Y'(P_*)` is a positive integer, and by `D>0` it satisfies

\[
1\le V<\frac{512}{243}\frac{11}{4}
=\frac{1408}{243}<6.
\tag{5}
\]

For all sufficiently large ordinary exponents `e`, the endpoint's
binary residue is

\[
Y'(2^e)\equiv-D3^{-q}\pmod{256}.
\]

At the center,

\[
V=-D3^{-q}+11\,2^{A-2}3^{-q}.                            \tag{6}
\]

If `A>=10`, (6) makes `V` congruent to one of `65,129,193` modulo
256, contradicting (5). If `A=8` or 9, it makes `V≡1 (mod 64)`,
so `V=1`. If `2<=A<=7`, the condition `Y'≡1 (mod 64)` forces
`v_2(V-1)=A-2`. For `1<=V<=5`, this leaves only `A=2,3,4`.
The integral possibilities with such small total exponent are
checked directly: `A=2` is the word `(2)`, with binary endpoint
`-5/3≡41 (mod 64)`, so it is ineligible; `A=3` gives `(2,1)`
and `V=1`, inconsistent with the required finite valuation;
at `A=4`, the first word `(4)` has `V=9`, and the two other
possibilities `(2,2)` and `(2,1,1)` are nonintegral. Thus only
`A=8,9` with `V=1` remain.

An integral inverse word from `7/4` to 1 is necessarily
`(2,1,2,...,2)`. To see this, its last move to 1 comes from 1
with exponent two or from 2 with exponent one. Remove any final
loops at 1. No inverse move from a positive integer can land at
2, since that would require `2^a v=7`. Therefore the state 2
must be the first inverse output, from exponent two at `7/4`.
The next move is exponent one, and all remaining moves are
the exponent-two loop at 1. Such a word has `A=2q-1`.
Among `A=8,9`, this gives only `q=5,A=9`, and direct expansion
gives exactly (1). Its upper slope is `1024/243`, with no strict
height saving. This proves W1.

The center (4) is used only for finite-word algebra and congruence.
It is not claimed to be an ordinary source or an all-time orbit.

## W2. Arbitrarily large depth is needed on actual ordinary inputs

For every integer `H>=5`, there are infinitely many exponents
`e=119+162j`, `j>=0`, for which no eligible odd predecessor `Y'`
reaches `M=2^e-1` with at most `H` odd inputs while satisfying
`2Y'-1<X`.

Choose

\[
4\,2^e\equiv11\pmod{3^H},\qquad e\ge4H+11.              \tag{7}
\]

Such exponents exist in the specified progression. Indeed
`2^119≡11/4 (mod 243)` and
`v_3(2^162-1)=5`. Successive cubing gives
`v_3((2^162)^(3^m)-1)=5+m`, so powers of `2^162` run through
all units congruent to one modulo 243 at every higher ternary
precision. The allowed `j` form one residue modulo `3^(H-5)`.
There are arbitrarily large ordinary representatives in that class.

The depth-zero predecessor is `M≡255 (mod 256)` and is ineligible.
Suppose therefore that an inverse word of depth `1<=q<=H` reaches
an eligible `Y'`.
Its initial and all intermediate divisions are integral at `P=2^e`.
Congruence (7) then makes them integral also at `P_*` as ternary
numbers. The first center exponent is even and at least two, so
its denominator four clears immediately; all subsequent center
outputs are positive ordinary integers, as in W1.

It remains to exclude the possibility that a large negative
intercept gives numerical saving despite a larger affine slope.
The exact inverse-word formula is

\[
Y'=\frac{2^A}{3^q}(P-E),\qquad
E=1+\sum_{i=1}^q3^{i-1}2^{-A_i}\le(3/2)^q,
\tag{8}
\]

where `A_i=a_1+...+a_i>=i`. Put
`lambda=2^(A+1)/3^q` and `lambda_0=1024/243`.
If `lambda>lambda_0`, writing the two fractions with denominator
`3^max(q,5)` gives integers `m>b` and hence

\[
\frac\lambda{\lambda-\lambda_0}
=\frac m{m-b}\le b+1\le1025\,3^q.
\]

From (7),
`P>=2^(4H+11)>1025*9^H`, so by (8)
`(lambda-lambda_0)P>lambda E`. It follows that

\[
(2Y'-1)-X
=(\lambda-\lambda_0)P-\lambda E+2573/243-1>0,
\]

contrary to the assumed height saving. Thus `lambda<=lambda_0`.
W1 now leaves only the original word, which gives `2Y'-1=X`,
again not a strict saving. This proves W2.

The least exponent in (7) above its stated lower bound is at
most `max(119,4H+11)+162*3^(H-5)`. Thus these depth lower bounds
can be obtained with `H>=log_3 e-O(1)`. The theorem is about
varying positive ordinary inputs; it does not assert that one
fixed input lacks every finite witness.

## Scope of the unsuccessful closing attempt

An unbounded certificate-dependent procedure remains possible.
In particular `v_3(4*2^e-11)` is finite for every positive ordinary
exponent `e`, although it is unbounded across this progression.
It supplies a lower bound on the needed inverse depth rather than
a terminating selection rule.

There is an exact attempted way to spend that precision. Write
`eta=v_3(4P-11)>=5`, `h=eta-5`, and

\[
Y=1+\frac{128(4P-11)}{243}.
\]

Repeated exponent-two inverses around the fixed point 1 give

\[
I_2^i(Y)=1+(4/3)^i(Y-1),\qquad0\le i\le h.              \tag{9}
\]

These are positive ordinary integers, and each consumes one unit
of the finite ternary valuation. However every nonzero repetition
increases numerical height, with the associated upper value
`1+(4/3)^i(X-1)>X`. Moreover its lower value is one modulo 256
when `i>=1`, outside the allowed three binary classes. At `i=h`,
put `Q=(4P-11)/3^eta`. The last value is
`1+128*4^h*Q`, which is divisible by three if `Q≡1 (mod 3)`.
In that case it has no odd predecessor at all. If `Q≡2 (mod 3)`,
an exponent-one inverse is available. Before taking it the earlier
height growth remains; taking it changes the leading height factor
to `(2/3)*(4/3)^h`, which exceeds one for `h>=2`. The case `h=1`
can repay height. This gives individual successful cases, not a
uniform repayment proof.

Thus finite precision alone neither preserves the required upper
height guard nor guarantees a next legal branch. The attempted
induction has not proved a uniform repayment after the exit,
or another actual state measure that decreases while maintaining
that guard. That is its first unsupported step. W2 counts odd
inputs on a path ending exactly at the prescribed Mersenne;
it is different from a bound on general ordinary-walk clocks.
