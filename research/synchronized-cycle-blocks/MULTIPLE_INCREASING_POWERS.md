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
