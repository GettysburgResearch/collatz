# Rising powers required in a complete powered tour

**PROPOSED with source-qualified Diophantine and finite-range inputs.**
Consider any cyclic cover of a primitive nontrivial positive ordinary
shortcut cycle by powers of nonempty binary words, all exponents at
least e. No bound is imposed on the number of decreasing powered
factors. The number h of increasing powered factors is strictly greater
than the indicated threshold in every row whose exponent floor applies.

| Minimum exponent e | Excluded increasing-factor counts h |
| ---: | ---: |
| 2 | h <= 1 |
| 3 | h <= 3 |
| 4 | h <= 4 |
| 5 | h <= 5 |
| 6 | h <= 6 |
| 9 | h <= 7 |
| 16 | h <= 8 |
| 256 | h <= 9 |

In particular a complete tour cannot be covered by three cubes.
More generally, with c=log_2 3, every such cover satisfies

    h >= (ln e - ln ln e - O(1))/ln c  as e tends to infinity,

uniformly over the period, root lengths, and number of decreasing
powers. The expanding-block height cascade in Wren's paper 57 is a
precursor; its Proposition 8 charges the number of stretches and the
maximum root width. Paper 142 excludes more blocks for its specified
valuation-polymer templates. [Prior work and scope](PRIOR_WORK.md)

## The height sweep

Use the notation and physical divisibilities in the
[single-rising-factor proof](ONE_INCREASING_POWER.md), including
H(x)=log_2(x+1), Z=log_2(2m+2), s=log_2(L+1), and gamma=c-1.
Set

    B=1/(1-c/e),   A=1+gamma B,   K=A^h,
    mu=1-gamma(e+K-1)/(e(e-1)c).

When mu>0 there is a boundary at which a complete forward sweep can
start with height at most

    J=max((1+1/(e-c))Z,
          (Z+gamma s/(e(e-1)c))/mu).

Indeed if the minimum is in an increasing power's first copy,
the proof there gives (e'-c)w<=Z for its actual exponent e'>=e
and I<=w+Z. If the minimum is in a decreasing power V^b's last
copy, start at its exit height H_0<=gamma p+Z, where p counts the
ones of V. Across all other powers each increasing factor multiplies
H by at most A and each decreasing factor lowers H. Hence their
endpoint is at most K H_0. The two inequalities

    b(v-cp) <= (K-1) H_0+s,       b c p <= v+H_0

give b(b-1)c p<=(b+K-1)H_0+s. The ratios
(b+K-1)/(b(b-1)) and 1/(b(b-1)) decrease for b>=e, giving
H_0<=J as stated.

During the sweep all boundary heights are at most KJ, and the kth
increasing factor enters at height at most A^(k-1)J. By the
starting 2-divisibility its length is at most B times that height.
The sum of the lengths P of all increasing powers and the maximum
base width W therefore obey

    P <= (K-1)J/gamma,         W <= KJ/(e-c).

The sum of all positive height gains is <=(K-1)J, since the gain
at the kth rise is at most (A-1)A^(k-1)J. Each homogeneous rise
e'(c h'-w) is no greater than its actual height gain under H:
the additive logarithmic corrections from even steps are nonnegative.
The global correction bound thus gives, for the sum D of all
descending homogeneous deficits,

    D <= (K-1)J+s.

## Effective table

For each of the eight table entries, the displayed bounds give

    P <= 120 Z+25s,     W <= 100Z+20s,     D <= 65Z+14s.       (1)

The rational upper and lower enclosures on c, and the checks on mu
and each coefficient separately, are in the
[exact replay](check_single_rise.py). Exponents above a row's floor
and fewer increasing factors satisfy the same bounds by using the
row's own e and h on the upper-bound side.

As in the single-rise proof, with t=log_2 L we now have P<=1970t,
W<=1640t and D<=1068t. The inequality L<=P+W^15 D first gives
t<512, using 1970+1068*1640^15<2^175. The certified bound for
R(840000) gives t<61; with W<=100040, the replay gives
R(100040)<5*10^9, implying t<49. The same lower convergent as
before then gives Z<=101 and s<=50. In (1), W<=12000 and
R(12000)<14*10^6, so (3) of the single-rise proof gives
L<103*10^9, below its independent Farey floor 114208327604.

## Growing minimum repeat count

For e tending to infinity, A=c+O(1/e). If h>=2 ln(e)/ln c the
asymptotic statement follows immediately, so suppose h=O(ln e).
Then ln K=h ln c+O(ln(e)/e). If K>=e this is already enough.
If K<e, the formula for mu gives mu>=1-O(1/e), so
J=O(log L), W=O(K log L/e)=O(log L), and D,P=O(K log L)
with absolute constants. Since R(W)<=W^15 by Rhin, we have

    L <= C K (log L)^16.

In particular log L=O(log(2K)), uniformly: taking logarithms gives
log L<=log(CK)+16 log log L and the last term is at most
(log L)/2 for sufficiently large L. Every individual factor
length is at most B KJ by (1) of the single-rise proof, and at
least e, whence e<=O(K log(2K)). Taking logarithms and using K<e
yields ln e<=h ln c+ln ln e+O(1). This argument does not require
finiteness of any list of root words.

## Three powered factors with unequal exponents

**PROPOSED.** A complete cover by exactly three powers, all exponents
at least two, would have exactly two increasing factors. Write their
exponents as a_1<=a_2, and b for the exponent of the decreasing factor.
The only remaining patterns are

* b=2, with a_1=2 and arbitrary a_2, or a_1=a_2=3;
* b=3, with a_1=a_2=2.

For a proof, the single-rise exclusion and cyclic monotonicity first
give the two increases. If the least state lies in an increasing
factor then its entry height is <=4Z as in the single-rise proof.
At most two rises multiply this by a factor less than 16; this
bounds all three lengths by (1) of that proof and gives L<=960Z,
contradicting the certified length floor.

Otherwise the minimum lies in the last copy of the decreasing factor.
Set K=A_(a_1)A_(a_2), where A_j=1+gamma/(1-c/j). The sweep proof
still works with the exact b in its minimum estimate, so now

    mu=1-gamma(b+K-1)/(b(b-1)c).

To cover every pattern other than those listed, it suffices to check
(b,a_1,a_2)=(4,2,2), (3,2,3), (2,3,4). Larger exponents only improve
the respective margins. At each of the three lower corners mu>1/1000;
the final margin is close to 0.00155 and the check uses rational bounds
1054/665<c<485/306. Thus H_0<=1000Z+200s. Since K<16 and each
physical length is at most five times its entering height, we have

    L <= 240(1000Z+200s) <= 3936000 log_2 L.

For L>=2^36 the left-to-logarithm ratio is increasing and already
exceeds 3936000. The certified Farey floor is greater than 2^36.
Therefore none of these three parameter regions occurs.

## Quadratic amplification is necessary at growing repeat exponents

The preceding logarithmic lower bound on h can be strengthened using
the first power following the small boundary. Allow k arbitrary
disjoint powers of minimum exponent e, with d positions uncovered.
As e tends to infinity, if d=o(e), then their h increasing factors
satisfy

    liminf K/e² >= c/gamma,
    h ln c >= 2 ln e + ln(c/gamma) - o(1),                          (3)

where K=A_e^h and c=log₂3. This also holds for complete tours. More
quantitatively, for any fixed delta>0, K<=(c/gamma-delta)e² forces
d >= c_delta e - O_delta(log(e+1)), for a positive constant c_delta.
There is no bound on the number of descending powers.

Indeed in this range the margin mu in the [fragmented sweep](FRAGMENTED_COVERS.md)
is bounded below by a positive constant depending on delta for all large
e. With s=log₂(L+1) that proof supplies a boundary height J=O_delta(s+d):
the factor K multiplying d in its numerator is divided by e(e-1).
Starting at this boundary the first selected power enters at height at
most J+d, even if there is an adjacent gap. Its length is at least e
and at most B(J+d), hence e=O_delta(s+d). Across the whole tour
the sum P of increasing lengths is at most (K-1)(J+d)/gamma: the
ith increase enters at height at most A_e^(i-1)(J+d), so their
length bounds form a geometric sum. The maximum root width and the
total descending deficit are also O_delta(K(s+d)). Rhin's estimate
therefore gives L<=C_delta(K(s+d))^16. As K=O(e²), taking logarithms
gives s=O_delta(log(e+1)+log(d+1)): use s+d<=(s+1)(d+1) and absorb
16 log₂(s+1) into s/2 for sufficiently large s. When d<=e, this yields
d>=c_delta e-O_delta(log(e+1)); when d>e this is automatic. This proves
the first limit. For the second, ln A_e=ln c+O(1/e); on h=O(log e)
the replacement in h ln A_e costs o(1), and larger h already suffices.

For the complete-cover special case the following numerical statement
uses only the explicit earlier bounds:

    e >= 2^20   implies   A_e^h > (5/2)e².                          (4)

Otherwise gamma/c<3/8 and K<=(5/2)e² give mu>1/17 for these e.
The single-boundary bounds above with d=0 give J<=289s using Z<=16s;
the gap-free first power has length at least e and at most BJ<=578s.
The complete increasing length P and largest width W are <=578Ks
by the geometric sweep, while D<=gamma P+s<=579Ks. Thus
L<=P+D W^15<=(1200Ks)^16. Using K<=(5/2)e² yields

    s <= 193+32 log₂ e+16 log₂ s.

Here s>=e/578>512, so 16 log₂ s<=s/2. It follows that
e<=1156(193+32 log₂ e), false at 2^20 and thereafter by monotonicity
of the ratio. This proves (4).

## Finite exclusions using two continued-fraction bounds

For complete tours the following pairs (e,r) exclude at most r rising
powers when all repeat exponents are at least e. These replace the
earlier more conservative uniform bounds in the opening table.

| e | 2 | 3 | 4 | 5 | 6 | 8 | 9 | 12 | 16 | 20 | 32 | 64 | 128 | 256 | 512 | 1024 | 4096 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| r | 1 | 3 | 4 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 15 | 20 | 24 | 28 | 31 | 38 |

In the sweep use the exact upper bound on J above, and put
P=(K-1)J/gamma, W=KJ/(e-c), D=(K-1)J+s, rounding upward.
One has L<=P+D R(W) and the first powered length is <=BJ. To
bound R(N), find consecutive Farey neighbors l<1/c<u of order N
and use R(N)<=1/(1-c l). Indeed descending h/w<1/c has denominator
at most N and therefore h/w<=l. A second use of this same bound
at a known period cap L<=N gives 2m+2<=R(N)+2 from the total cycle
drift and 3 ln(2)>2. This sharpens the bound on Z for the next sweep.

The [exact rational replay](check_farey_sweeps.py) brackets c in a
400-bit dyadic interval, certifies both neighboring fractions by their
cross determinant one and denominator sum greater than N, and tests
the inequalities for each row separately. The initial bound L<2^1024
follows by substituting Z<=16t and s<=2t at t=1024 in P+D W^15:
the unrounded right side grows at most as t^16 for t>=1024, whereas
2^t/t^16 is increasing there. The first sweep uses the older Z bound;
subsequent ones use the computed R(N). Each row ends either at BJ<e
or below the previously certified period floor 114208327604.
