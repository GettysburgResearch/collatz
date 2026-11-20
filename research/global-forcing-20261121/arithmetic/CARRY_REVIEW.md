# Independent reconstruction of the carry-four construction

**Internal review verdict: VERIFIED for CF2--CF4 at the pinned version.**
This is an independent mathematical reconstruction by the arithmetic-route
agent. It is not external referee acceptance or formal verification. No
mathematical repair was needed.

Reviewed file:
`research/global-forcing-20261121/certificates/CARRY_COMPILER.md`

SHA-256:
`394571cd06d55caa4465cdb7a1d76cefc1d36b29bfc41522ac5a2c136f6cf7ea`

The primary review covers the exact entry cylinder, ordinary carry and
exit, the correction formula, and the all-rank first-hit unit family.
The final section records a narrower inspection of the accompanying
parser. This verdict does not extend to later versions, to the imported
PR166 result, or to a universal five-closure claim.

## 1. Normalization and inverse integrality

For a positive odd source, an exponent word `(a_1,...,a_p)` specifies
the exact odd steps

\[
n_i=(3n_{i-1}+1)/2^{a_i},\qquad a_i\ge1.
\]

Put `A=sum(a_i)` and define its affine correction by

\[
B=\sum_{i=1}^{p}3^{p-i}2^{a_1+\cdots+a_{i-1}}.
\]

Then its endpoint is `(3^p x+B)/2^A`. Appending a letter replaces
`B` by `3B+2^A`, where `A` is the clock before appending that letter.
The last letter does not enter the correction itself.

The inverse-integrality argument used in CF4 is valid. If the endpoint
`q` is positive odd and `2^A q-B` is divisible by `3^p`, reduction
modulo three forces the innermost inverse
`(2^(a_p)q-1)/3` to be integral: its numerator differs by an invertible
power of two from the full numerator modulo three. Substitution and
division by three leave the analogous numerator for the shortened
word, divisible by `3^(p-1)`. Induction proves every successive
inverse integral. Each integral inverse is positive and odd, since
its numerator is positive odd. Reversing these identities gives exact
valuations, because every subsequent odd endpoint is odd.

Thus divisibility of the full numerator supplies actual ordinary
paths here. It is not merely a terminal congruence or a formal
composition of possibly nonintegral inverse branches.

## 2. CF2: exact entry, carry, and exit

For

`E=(2,1,1,1,2,1,7)` and `F=(3,6,1,2,1,1,1)`,

the correction recurrence gives respectively

`(B,A,p)=(3709,15,7)` and `(149617,15,7)`.

Their correction difference is
`149617-5*3709=4*2^15`, which gives the endpoint relation `5y+4`.

### The cylinder is necessary and sufficient

If `E` is exact, its final quotient must be odd. Therefore

\[
3^7x+3709\equiv2^{15}\pmod{2^{16}}.
\]

The coefficient is invertible modulo `2^16`, giving the single class
`x=25065 mod65536`. This proves necessity, not just sufficiency of
the displayed class.

The manuscript's two base paths replay exactly. For a positive source
in the class, write `x=25065+65536k` with `k>=0`. After `i` source
odd steps, the increment from the base path is

\[
3^i2^{16-S_i}k,
\]

where `S_i` is that word's cumulative division exponent. Since
`S_i<=15`, this is an even nonnegative integer at every odd state.
For the target word the increment is the same expression with its own
cumulative exponent and an additional factor five. Hence all base
states remain positive odd states and every edge has its original
exact valuation. This proves sufficiency for both words. The source
endpoint is `1673+4374k`; the target endpoint is five times it plus
four. All target entry states exceed one.

### A valuation-one step preserves the nonzero carry

If `U(z)` is obtained with exponent one, then

\[
3(5z+4)+1=5(3z+1)+8
\]

has quotient `5U(z)+4` after dividing by two. This quotient is odd,
so the target exponent is exactly one, not merely at least one.
It is positive and exceeds one. Induction therefore preserves carry
four through any specified finite run of valuation-one steps.

### The exit has exactly the stated exponents

Suppose `U(z)=v` uses exponent three and `U(v)=q` uses `b>=2`.
Then `v=1 mod4`, and

\[
3(5z+4)+1=8(5v+1).
\]

Since `v=1 mod4`, one has `5v+1=2 mod4`. Consequently the first target
valuation is exactly four. Its odd endpoint is `(5v+1)/2`, and the
next numerator is

\[
3(5v+1)/2+1=5(3v+1)/2=5\,2^{b-1}q.
\]

As `q` is odd, the second target exponent is exactly `b-1>=1`,
and the endpoint is `5q`. The intermediate target state is at least
three and the endpoint is at least five. No earlier target hit of
one occurs during this exit.

## 3. CF3: concatenation, resources, and the correction

Entry, the repeated carry step, and exit concatenate on the actual
successive ordinary states. The source and target each use `r+9`
odd inputs and clock `r+b+18`, for every `r>=0` and `b>=2` for which
the source prefix is legal. This claim does not assume source or
endpoint convergence.

The correction of `1^r` is `3^r-2^r`. Appending `(3,b)` gives

\[
B_{\mathrm{tail}}=3^{r+2}+2^{r+1}.
\]

Prefixing `E` therefore gives

\[
\begin{aligned}
B_r
 &=3709\,3^{r+2}+2^{15}(3^{r+2}+2^{r+1})\\
 &=36477\,3^{r+2}+2^{r+16}\\
 &=1351\,3^{r+5}+2^{r+16}.
\end{aligned}
\]

Independently, the target tail `(1^r,4,b-1)` has correction
`3^(r+2)+5*2^(r+1)`. Prefixing `F` gives
`182385*3^(r+2)+5*2^(r+16)=5B_r`. This verifies the claimed
correction equality without inferring an affine identity from one
numerical example.

Neither this calculation nor concatenation proves ordinary height
descent. The manuscript correctly does not require such descent for
the carry block.

## 4. CF4: the lift supplies a unit at every stated rank

The base congruence is exactly

\[
4^{81}\equiv43255=1+178\,3^5\pmod{3^{10}}.
\]

To see why the same coefficient persists, suppose

`4^(3^(r+4))=1+178*3^(r+5)+O(3^(r+10))`.

After cubing, the unknown linear error is divisible by `3^(r+11)`.
The quadratic contribution has valuation at least `2r+11`, and the
cubic contribution at least `3r+15`; both are at least `r+11`.
This proves the next case. Hence the manuscript's lifted congruence
holds for every nonnegative `r`.

Raising it to `t=t_r` introduces no further terms modulo `3^(r+10)`:
every term of degree at least two has valuation at least `2r+10`,
which suffices even at the boundary `r=0`. Since

\[
t_r\equiv88\,2^{-r}\pmod{243},
\qquad
178\cdot88\cdot2^{16}\equiv217\equiv1351+81\pmod{243},
\]

and `b_r+2=2*3^(r+4)*t_r`, the numerator of `x_r` satisfies

\[
\begin{aligned}
2^{r+b_r+18}-1351\,3^{r+5}-2^{r+16}
&=2^{r+16}(2^{b_r+2}-1)-1351\,3^{r+5}\\
&\equiv81\,3^{r+5}
 =3^{r+9}\pmod{3^{r+10}}.
\end{aligned}
\]

This proves full divisibility and `x_r=1 mod3`. The residue `t_r`
is a unit modulo three, lies in `1,...,242`, and is never zero.
Consequently `b_r>=2*3^(r+4)-2>=160`.

### Positivity and first-hit status

Apply the inverse-integrality argument in Section 1 to the endpoint
one and the full word `W_(r,b_r)`. All intermediate inverse values
are positive odd integers. The first inverse value is
`(2^(b_r)-1)/3>1`. Every subsequent integral inverse of an odd
integer `u>1` also exceeds one: an output equal to one would require
`2^a u=4`, impossible for odd `u>1` and `a>=1`.

Thus every source odd state before the final endpoint exceeds one,
and its first-hit odd rank is exactly `r+9`. No even intermediate
shortcut state can equal one. The claimed first-hit status therefore
holds for the shortcut map as well as its odd acceleration.

For the target, the entry states exceed one by the cylinder argument,
the loop states are of the form `5z+4>1`, and the exit's two endpoints
are `(5v+1)/2>=3` and five. Appending the exponent-four edge from
five to one gives its first hit, with rank `r+10` and four extra
shortcut steps. This supplies an ordinary certified source unit and
target at every odd rank at least nine. The sources vary with `r`;
there is no claim about a single fixed orbit having arbitrarily many
such initial runs. Here “rank” means first-hit odd count, not the
multiplicative rank used elsewhere in the arithmetic packet.

## 5. Supplemental execution and parser inspection

An independent short integer program, separate from the author's
checker, authenticated the proof hash and reconstructed the two entry
corrections and the unique residue. It replayed entry lifts `k=0,1`,
checked the two small modular constants, and directly checked the
source and target first-hit words at the following indices:

| `r` | `t_r` | `b_r` | Source bits | Source odd rank | Target odd rank |
|---:|---:|---:|---:|---:|---:|
| 0 | 88 | 14254 | 14258 | 9 | 10 |
| 1 | 44 | 21382 | 21386 | 10 | 11 |
| 4 | 127 | 1666492 | 1666494 | 13 | 14 |

The last case checks the residue wrap after the initial successive
halvings of `t_r`. Each replay checked exact valuations, positive odd
states, absence of an earlier one, the closed correction, and the
one-extra-odd-input target. The execution completed with exit code
zero. These finite examples supplement the preceding proofs; they do
not establish the all-parameter claims by enumeration. No broad orbit
search or full repository validation was performed for this review.

The accompanying `parse_blocks` implementation was also inspected.
The carry prefix starts `(2,1)`, a valuation-two block starts with a
run of twos followed by a letter at least four, and the short block
starts with three ones. These alternatives do not overlap. Inside a
carry block, the maximal run of ones must be followed by `(3,b)`;
inside a valuation-two block, the maximal run of twos must be followed
by its final letter. These rules make parsing unique and consume a
positive number of letters at each success. Failed guards return an
unresolved result. The caller first validates the supplied first-hit
source word, and validates the compiled target before returning it.
This inspection supports the stated handling of the new carry blocks;
it does not replace independent review of the imported block theorem
or claim complete coverage of all source certificates.

The first unsupported global step remains exactly the one stated in
the manuscript: proving a total successful transformation on arbitrary
supplied certificates, or providing another argument for the uncovered
inputs. The verified construction does not settle that obligation.
