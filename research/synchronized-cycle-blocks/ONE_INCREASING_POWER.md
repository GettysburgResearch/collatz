# A cycle cannot cover one tour by powers with just one increasing factor

**PROPOSED, source-qualified.** In every cyclic factorization of a
primitive nontrivial positive ordinary shortcut cycle into exact powers
of nonempty words, each exponent at least two, at least two factors are
increasing. At least one is decreasing. There is no bound on the number,
sizes or arrangements of the factors in this assertion. A factor
W^e is increasing precisely when 3^ones(W)>2^|W| by the
[physical sign lemma](TWO_POWER_EXCLUSION.md).

The finite number theory inputs are the Rhin estimate on log 2/log 3
cited in the [cycle-height note](../cyclic-shift-distance/README.md)
and Barina's reported verification of all positive starts below 2^68.
The [exact arithmetic replay](check_single_rise.py) certifies the
intermediate ranges. The verified initial range is external.
[Barina, *Improved verification limit for the convergence of the Collatz
conjecture*](https://doi.org/10.1007/s11227-025-07337-0)

Fourier Wren derives the powered-block brackets and two-block commutator in paper 57. [Prior results and scope comparison](PRIOR_WORK.md)

## Physical heights

Write c=log_2 3, gamma=c-1, H(x)=log_2(x+1), Z=log_2(2m+2) at the
global minimum m, and s=log_2(L+1) for period L. For every proper power
W^e in the cover, put w=|W|, h=ones(W), K_e=1+gamma/(1-c/e).
The [starting divisibility](../cyclic-shift-distance/POWER_COVERS.md)
gives ew<=cw+H(x). A physical step grows the state plus one by a
factor at most 3/2. Thus

    ew <= H(x)/(1-c/e),      H(end) <= K_e H(x).               (1)

This remains valid if a single powered factor covers the whole cycle
because its base word is shorter than L. Write K=K_2<4 and
1/(1-c/2)<5. Decreasing factors only lower H, and a cycle must have
both directions. Suppose there is just one increasing factor, and
write I for its entering height.

As one iterates a fixed word, states at each fixed offset strictly
follow its sign. The global minimum therefore lies in the first copy
of the increasing factor or the last copy of a decreasing factor.
In the first case its entering state x obeys x<=2^(w-h)m. The
sharper bound ew<=ch+log_2(x+2^(w-h)) from the two-power note then
gives ew<=cw+Z<=c ew/2+Z. Hence I<=w+Z<=4Z.

In the second case call that descending power V^b, write v,p for its
base length and ones, and H_0 for its exit height. Forward tracing
from m gives H_0<=gamma p+Z. The ending 3-divisibility at its exit
gives bcp<=v+H_0. Starting after V^b, the other factors, with only
one increasing exception, can reach height at most K H_0. In particular
I<=H_0. Each even step multiplies the state plus one by
(1+1/(x+1))/2, while each odd step multiplies it by exactly 3/2.
The total base-two logarithm of the positive corrections is <=s:
the ordinary phases are distinct, and the product of 1+1/j for
1<=j<=L telescopes to L+1. Thus

    b(v-cp) <= (K-1) H_0 + s,
    b(b-1) c p <= (b+K-1) H_0 + s.

The ratio (b+K-1)/(b(b-1)) decreases for integers b>=2 and is at
most (K+1)/2. Substituting the last inequality in H_0<=gamma p+Z gives

    (1-gamma(K+1)/(2c)) H_0 <= Z+gamma s/(2c).

The coefficient is positive, and the exact rational bounds
19/12<c<485/306 give H_0<=10Z+2s. Both cases therefore imply

    I <= 10Z+2s,       maximum boundary height <= 40Z+8s.

The sum D of e(w-ch) over all decreasing powers is controlled by
the sole increasing base (w_+,h_+) of exponent e_+. The global
log correction gives D <= e_+(ch_+-w_+)+s. The right side is
at most gamma e_+w_++s, hence at most 30Z+7s by (1). We obtain

    growing physical length P <= 50Z+10s,
    every base width          <= 100Z+20s,
    total descending deficit D<= 30Z+7s.                       (2)

## Successively narrower finite ranges

For t=log_2 L>=1 we have Z<=16t and s<=2t. If W bounds all base
widths, put R(W)=max w/(w-ch) over positive w<=W and 0<=h<=w
with w>ch. Summing the length of the decreasing powers gives

    L <= P+R(W)D.                                              (3)

The Rhin bound gives w-ch>=w^(-13.3) for w>=2; for w=1 a decreasing
word has h=0. Consequently R(W)<=W^15. Equations (2) and (3)
give L<=820t+494t(1640t)^15<2^175 t^16. For t>=512 the left side
2^t exceeds this upper bound: this holds at 512 and 2^t/t^16 is
increasing there. Thus t<512.

The exact inequalities R(840000)<4*10^12 and R(98400)<5*10^9
can be checked by a single comparison per w, using h=floor(w/c).
Starting with t<512, (3) gives t<60, then t<49.
For this range the rational number n/d=766512153894657/483615324366283
satisfies 0<c-n/d<1/(2d*2^49). For the total odd count Q, positivity
gives L/Q>c, so Ld-nQ>=1. Since Q<=L<2^49, we have L-cQ>1/(2d)>2^(-50).
The correction formula at the least state yields
m<=Q/(3 ln(2)(L-cQ))<2^99. Therefore Z<=101 and s<=50.
Equations (2) and (3), now with R(12000)<14*10^6, give L<48*10^9.

Finally m>=2^68 from the external verified range yields
0<L/Q-c<=1/(3m ln 2)<2^(-69) since ln 2>2/3. The two fractions

    103768467013/65470613321,   10439860591/6586818670

strictly bracket [c,c+2^(-69)] and have cross determinant one.
Any reduced fraction between them has numerator at least the sum
114208327604 of their numerators, and unreduced fractions have at
least that numerator as well. This contradicts the upper bound.
The argument does not rule out coverings with two or more
increasing factors.
