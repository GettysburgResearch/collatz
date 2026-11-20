# Endpoint congruences couple physical five renewals

**PROPOSED.** This is a positive renewal on a larger, still incomplete
ordinary source domain. It proves no absolute bound for the uncovered
energy and does not prove Collatz. The proof uses no GRH or predecessor
density assumption.

The new four-odd-step block is established in the neighboring certificate
packet. The proof below also reconstructs its exact identity. The earlier
ladder and its harmonic/subcritical constants are credited to PR166,
5996b9f525ca50978bc34f423192c36a87765bf3,
research/grh-certificate-closure-20261120/FIVE_CERTIFICATE_LADDER.md,
FL1--FL3, and LADDER_RENEWAL.md, R1--R6. The additional point here is that
the two inverse kernels cannot simultaneously attain their separate
worst cases: they constrain the **same actual endpoint modulo 27**.
CR3 then uses the same idea to add an **unbounded carry-ladder
sublanguage**, with a joint subcritical coefficient still below one.

## CR1. Statement

Use the shortcut Collatz map T and its positive odd acceleration U. Let
f be any ordinary-invariant map into a metric space, so f(Tn)=f(n).
For positive odd ternary units put

\[
 e(x)=d(f(5x),f(x)),\qquad
 E_s(X)=\sum_{\substack{x\le X\\x\text{ odd},\ 3\nmid x}}x^{-s}e(x).
\]

The endpoint one contributes zero because the actual path from 5 to 1
is known: e(1)=0. No other convergence is assumed.

Let H be PR166's union of the disjoint initial valuation cylinders
(2 repeated r times, b), r>=1, b>=4, restricted to odd ternary units.
Let

\[
 J=\{x>0:x\equiv271\pmod {512},\ 3\nmid x\}.
\]

H and J are disjoint: their first accelerated valuations are two and
one, respectively. Let R_s(X) be E_s(X) restricted to the complement
of H union J. Then

\[
 \boxed{E_1(X)\le R_1(X)+\frac{13}{14}E_1(X/6),}       \tag{CR1a}
\]

and, at the exact rational exponent s=21/25,

\[
 \boxed{E_{21/25}(X)\le R_{21/25}(X)
       +\frac{330293}{331700}E_{21/25}(X/6).}          \tag{CR1b}
\]

In particular, for either exponent, full energy is finite if and only
if the uncovered energy is finite. The bounds in the finite case are

\[
 E_1(\infty)\le14R_1(\infty),\qquad
 E_{21/25}(\infty)\le\frac{331700}{1407}R_{21/25}(\infty).
                                                               \tag{CR1c}
\]

These are deliberately simple rational bounds, not optimized constants.

## The new physical cylinder and its complete inverse fibers

For I_a(q)=(2^a q-1)/3, the exact identity is

\[
 5I_1I_1I_1I_b(q)=I_1I_2I_5I_{b-5}(5q),\qquad b\ge6.       \tag{1}
\]

Composition is read from right to left. The two correction numerators
are 65 and 325, respectively, and both words have four odd steps and
total shortcut clock L=b+3. If the source word is a legal positive
ordinary word, its total integer identity makes the target word legal
as well. One can check each inverse division, or reduce the common
total identity successively modulo the required powers of two.

The source domain is exactly J before the final ternary-unit restriction.
Its first three odd valuations are one, and

\[
 U^4(x)=q=\frac{81x+65}{2^L},\qquad
 L=v_2(81x+65)\ge9.
\]

Here q is the actual positive odd endpoint. Because an odd Collatz
numerator is one modulo three, q is a ternary unit. Equation (1) gives
T^L(5x)=5q and hence e(x)=e(q). Moreover x>=271 and

\[
 6q\le\frac{6(81x+65)}{512}\le x,
\]

the last inequality already holding for x>=15.

For a fixed odd ternary unit q, all possible sources are

\[
 x_L(q)=\frac{2^Lq-65}{81},\qquad
 L\ge9,\quad 2^Lq\equiv65\pmod {81},\quad 3\nmid x_L(q).
                                                               \tag{2}
\]

The order of two modulo 81 is 54. Thus the integral clocks form one
progression modulo 54; the last unit guard can only remove sources.
Successive members before that deletion satisfy

\[
 x_{L+54}=2^{54}x_L+\frac{65(2^{54}-1)}{81}>2^{54}x_L.      \tag{3}
\]

There is one actual clock and endpoint per source; no source multiplicity
is discarded. For a nonzero endpoint contribution q>=5, (2) gives

\[
 \sum_{x\in J:\,U^4x=q}x^{-s}
 \le\frac{(81/499)^s}{1-2^{-54s}}q^{-s}.                  \tag{4}
\]

At s=1 the coefficient in (4) is less than 1/6, since
13*2^54 > 499. Combining this with PR166's 16/21 bound gives
16/21+1/6=13/14. Both families send x<=X to q<=X/6, proving CR1a.

## CR2. Endpoint compatibility at exponent 21/25

Write s=21/25 and a=(3/4)^s. The following exact upper bounds will be
used:

\[
 a<\frac{393}{500},\quad
 (15/76)^s<\frac{13}{50},\quad
 (5/52)^s<\frac7{50},\quad
 (81/499)^s<\frac{11}{50},\quad
 (81/32755)^s<\frac1{125}.                               \tag{5}
\]

Every comparison in (5) is the corresponding positive integer
inequality after taking the 25th power; the accompanying checker records
all five. Also 2^(-6s)<1/32, because 6s=126/25>5. The geometric
factor for any period at least six is consequently less than 32/31.

For a ladder inverse with run length r, PR166's exact formula is

\[
 x_{r,b}=1+(4/3)^r\frac{2^bq-4}{3},\qquad
 2^{b-2}q\equiv1\pmod {3^{r+1}}.                        \tag{6}
\]

At fixed r its legal b occupy one progression of period 2*3^r before
the source-unit deletion. For q>=5, using b>=4 gives the inverse weight
bound (15/76)^s a^r times the geometric factor. If b>=5, the stronger
bound is (5/52)^s a^r times that factor.

### Case q=7 modulo 27

The complete ladder kernel is bounded, as in PR166, by

\[
 \frac{32}{31}\frac{13}{50}
 \frac{393/500}{1-393/500}
 =\frac{81744}{82925}.                                  \tag{7}
\]

But the new inverse block now satisfies 2^L*7=65 mod27, or
2^L=17 mod27. Two has order 18 modulo 27 and 2^15=17 mod27, so
L=15 modulo 18. Since L>=9, actually L>=15.
Its first source obeys x/q >= (2^15-13)/81=32755/81.
Thus the entire new kernel has coefficient less than

\[
 \frac{32}{31}\frac1{125}=\frac{32}{3875}<\frac1{100}.
\]

The sum of the two kernels is therefore less than

\[
 \frac{81744}{82925}+\frac1{100}
 =\frac{330293}{331700}<1.                              \tag{8}
\]

### Case q is not 7 modulo 27

For every ladder run r>=2, the choice b=4 would make (6) imply
4q=1 mod27, equivalently q=7 modulo 27. It is therefore impossible
in this case; every such run has b>=5. Keep the b>=4 bound only for
r=1. Summing both ladder parts and (4), and using (5), gives the common
upper coefficient

\[
 \frac{32}{31}\left[
 \frac{13}{50}\frac{393}{500}
 +\frac7{50}\frac{(393/500)^2}{1-393/500}
 +\frac{11}{50}\right]
 =\frac{8865224}{10365625}
 <\frac{330293}{331700}.                                \tag{9}
\]

This is the important coupling: adding separate global suprema would
lose subcritical contraction, whereas the two exact endpoint cases
retain it. All terms are inverse fibers of the actual source map, not
an assumed fresh residue distribution after a return.

## Positive summation, finite cutoffs, and the remaining gap

Partition H union J by its unique actual endpoint q. Apply (8)--(9)
at that same q and multiply by e(q). Sources x<=X have q<=X/6.
The q=1 terms vanish. Positive summation proves CR1b. Because E_s(X)
is finite at every finite X, one may bound E_s(X/6) by E_s(X), subtract
the resulting finite term, and then increase X. This proves CR1c
without subtracting infinite energies.

J adds a relative density 1/256 among odd ternary units to the
disjoint ladder density 1/24. The combined relative density is 35/768.
These densities are only a description of the source domain; they are
not an energy estimate for an arbitrary invariant label.

PR163, 051237135a34ae7d4b973ee5fcf5da04ded6f0fc,
research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md, FE1 and
section 4, supplies the separate five-to-tripling energy comparison and
its source-qualified rigidity consequences. CR1 does not reproduce that
result. No argument here proves R_1 or R_(21/25) finite. In particular,
localizing every comparison into a larger source, as in PR146
fd991063721e9c157d318e40bb20131762f7d750,
research/upper-bit-mergers/FIVE_STEP_SEEDS_AND_MULTIPLIERS.md, does not
give this missing absolute upper bound.

The next decisive estimate remains a bound for the entire uncovered
defect, or a successful physical reduction on every required source.

## CR3. Adding an unbounded carry-ladder sublanguage

The certificate packet supplies the new pair of seven-odd-step words

\[
 E=(2,1,1,1,2,1,7),\qquad F=(3,6,1,2,1,1,1).
\]

They both use 15 shortcut clocks and take (x,5x) to (y,5y+4).
Each following valuation-one step preserves the carry four. The exit
(3,b) on the first arm and (4,b-1) on the second kills that carry for
b>=2. Thus the paired words

\[
 E,1^r,3,b\quad\hbox{and}\quad F,1^r,4,b-1                \tag{10}
\]

give the actual endpoints (q,5q) for every r>=0 on their legal source
domains. The full certificate theorem permits every b>=2.

Here restrict to the **safe sublanguage b>=r+2**, and call its source
domain G, again restricted to odd ternary units. Its cylinders for
different r are disjoint, since r counts the consecutive valuation-one
steps after E before the next valuation three. G is disjoint from H
and J: its first two valuations are 2,1; H begins with a positive
run of twos followed by a valuation at least four; J begins with one.

Let Q_s(X) denote E_s(X) restricted outside H union J union G. Then

\[
 \boxed{E_{21/25}(X)\le Q_{21/25}(X)
       +\frac{248549}{248775}E_{21/25}(X/6),}             \tag{CR3a}
\]

\[
 \boxed{E_1(X)\le Q_1(X)+\frac45E_1(X/6).}               \tag{CR3b}
\]

The corresponding finiteness equivalences have bounds

\[
 E_{21/25}(\infty)\le\frac{248775}{226}Q_{21/25}(\infty),
 \qquad E_1(\infty)\le5Q_1(\infty)
\]

when the uncovered energy is finite. The new uncovered energy remains
unbounded by this argument.

### Exact source formula and inverse geometry

The correction numerator of E is 3709. Its endpoint is
y=(3^7 x+3709)/2^15. The r valuation-one steps send y to
(3^r(y+1)-2^r)/2^r, while the last two steps send z to
(9z+11)/2^(b+3). Consequently

\[
 q=\frac{3^{r+9}x+1351\,3^{r+5}+2^{r+16}}
          {2^{r+b+18}},
\]

or, equivalently,

\[
 x=\frac{2^{r+b+18}}{3^{r+9}}q
     -\frac{1351}{81}
     -\left(\frac23\right)^r\frac{65536}{19683}.          \tag{11}
\]

For q>=5 and b=r+2+delta with delta>=0, this gives

\[
 \frac{x}{q}\ge C\left(\frac43\right)^r2^\delta,\qquad
 C=\frac{4849051}{98415}>49.                             \tag{12}
\]

Indeed, first subtract at most
(1351/81+65536/19683)/5 when r=0, and enlarge that subtraction by
(4/3)^r 2^delta to obtain a valid lower bound at general r,delta.
Its difference from the leading coefficient 2^20/3^9 is exactly C.
Every nonzero defect contribution from G therefore has q<x/49.

At fixed r,q, the correction numerator in (11) is coprime to three.
The allowed b form one progression of period
P_r=2*3^(r+8) before the source-unit deletion. Consecutive integral
inverse sources grow by more than 2^(P_r), exactly as in (3).
At s=21/25 the geometric factor is less than

\[
 G_0=\frac{65536}{65535},
\]

because P_r s>16. It is essential that this is the inverse clock
progression of the same fixed endpoint, not a renewed random law.

### A common endpoint determines the exit congruence

Every source in G satisfies

\[
 2^bq\equiv7\pmod {27}.                                 \tag{13}
\]

For r>=1, this follows by applying integrality to its last three
source valuations (1,3,b): their correction numerator is 31 and
their first two clocks sum to four. For r=0 the last three are
(7,3,b), with correction numerator 1417 and first two clocks summing
to ten. Both give (13) modulo 27.

For each ternary-unit q, let b_0 be the unique residue in {0,...,17}
satisfying (13). Since b>=r+2, its least possible excess delta obeys

\[
 \delta\ge (b_0-r-2)\bmod18,                             \tag{14}
\]

where the remainder lies between zero and 17. Put

\[
 \widehat a=\frac{393}{500},\qquad
 \widehat t=\frac9{16}.
\]

The additional exact integer comparisons

\[
 (98415/4849051)^{21/25}<1/25,\qquad 2^{-21/25}<9/16
\]

are certified respectively by

\[
 98415^{21}25^{25}<4849051^{21},\qquad
 16^{25}<2^{21}9^{25}.                                  \tag{15}
\]

Positive summation of (12)--(14), grouping r by its residue modulo
18, bounds the complete inverse G kernel at q by

\[
 \frac{G_0}{25}\,
 \frac{\displaystyle\sum_{j=0}^{17}
       \widehat a^j\widehat t^{(b_0-j-2)\bmod18}}
      {1-\widehat a^{18}}\ q^{-s}.                     \tag{16}
\]

The sum is finite rational arithmetic. In the three required cases
the following exact bounds hold:

| q modulo 27 | b_0 | Upper bound for the coefficient in (16) |
|---:|---:|---:|
| 7 | 0 | 1/300 |
| 16 | 12 | 1/8 |
| 25 | 6 | 1/8 |

The checker clears the positive denominators in these three rational
comparisons. Formula (16) is also bounded for every q by
G_0/[25(1-hat a)], simply dropping the powers of hat t.

### Joint bound for all three physical source families

There are three endpoint cases.

1. If q=7 modulo 27, use CR2's coefficient 330293/331700 for H union J
   and 1/300 for G. Their sum is

   \[
    \frac{330293}{331700}+\frac1{300}
    =\frac{248549}{248775}<1.                           \tag{17}
   \]

2. If q=16 or 25 modulo 27, CR2's other coefficient applies. Including
   G gives

   \[
    \frac{8865224}{10365625}+\frac18
    <\frac{248549}{248775}.                             \tag{18}
   \]

3. If q is not 7 modulo 9, no ladder run, including r=1, can use b=4:
   equation (6) would imply q=7 modulo 9. Use the stronger 5/52 bound
   for the entire old ladder, the general J bound, and the coarse G
   sum after (16). Their total coefficient is at most

   \[
    \frac{32}{31}\left[
       \frac7{50}\frac{\widehat a}{1-\widehat a}
       +\frac{11}{50}\right]
      +\frac{G_0}{25(1-\widehat a)}
    =\frac{1026910336}{1086897975}
    <\frac{248549}{248775}.                             \tag{19}
   \]

These cases exhaust all positive odd ternary-unit endpoints. They
prove the fiber estimate for CR3a. Every nonzero contribution has
q<=x/6, so the cutoff remains X/6.

For CR3b, use the stronger power on each individual inverse ratio:

\[
 (q/x)^1\le6^{-4/25}(q/x)^{21/25}
          <\frac45(q/x)^{21/25}.
\]

The last comparison is the exact integer inequality
5^25<6^4*4^25. Combining it with the coefficient below one in CR3a
gives a harmonic coefficient at most 4/5. Positive summation and
finite-cutoff subtraction finish the stated finiteness implications.

The proof enlarges the renewal to arbitrarily long run-one blocks.
It does not assume that a general source enters this safe sublanguage.
The full carry theorem also allows b<r+2, which is deliberately not
assigned a contracting weight here. All remaining ordinary sources
are retained in Q_s, whose finite energy is still the decisive open
input.
