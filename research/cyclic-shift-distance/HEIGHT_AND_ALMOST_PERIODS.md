# How many shifts can nearly preserve a cycle word?

**PROPOSED / SOURCE-QUALIFIED for the logarithmic period estimates.** In a
primitive positive cycle of length L>=2^20, at most 6D² shifts, including
the identity, have Hamming distance at most D from the parity word, for
each integer D>=1. A nonidentity shift r of distance d must also satisfy

    |k r - a L| <= 2d²  for some integers 1<=k<8d and a.

The second condition restricts the location of low-distance shifts when
d is much smaller than the cube root of L. Neither bound presumes a block
arrangement. The proof supplies exact height tests for smaller periods.

## Centered height

Use the [cycle notation and Rhin input](README.md). Let
F_0=0 and F_(i+1)-F_i=b_i-q/L so that F is periodic. Its oscillation
B=max F-min F is the largest centered odd-count excess on a cyclic interval.
Write M=max_i x_i. Starting at the least phase and using the exact product
along the arc to a largest one gives

    M <= m exp(lambda) 3^B <= L^16 3^B.                       (1)

Indeed the coefficient of a length-h segment is
3^(number of ones - hq/L) exp(-h lambda/L), and its correction product
is bounded by the full product exp(lambda). The second bound follows from
m<=L^14.3/3 and exp(lambda)<=q+1 as in the main note.

Different phases beginning with the same h parities have nonzero integer
difference divisible by 2^h. Thus h<=log_2 M. A shift of distance d has
an agreeing cyclic run of length at least (L-d)/d, giving

    L/d - 1 <= 16 log_2 L + c B,     c=log_2 3.                (2)

For L>=2^20, 1+16 log_2 L <= sqrt(L)/2 (check the initial value and
monotonicity of sqrt(L)/(1+16 log_2 L)). So if d<=sqrt(L), then

    B >= L/(2 c d).                                           (3)

For any shift r of distance d_r, the height increment F_(i+r)-F_i is a
centered length-r odd count. As i increases around the circle, its values
increase by one d_r/2 times and decrease by one d_r/2 times. Their mean
is zero. In particular

    |F_(i+r)-F_i| <= d_r/2  at every phase i.                 (4)

A single physical unit shift also changes F by at most one.

## Counting shifts

Let A be the shifts of distance <=D, of cardinality K. This symmetric set
contains zero. The subgroup it generates in the cyclic group of order L
has order n and index g=L/n. In any of its cosets, join two indices if
their difference is in A. Each closed radius-one ball has K vertices.
On a diameter geodesic of length s the vertices at positions 0,3,6,...
have disjoint closed radius-one balls. Consequently s<3n/K. Equation (4)
bounds the height difference within each coset by 3nD/(2K). From any
index, at most floor(g/2) physical unit steps reach the coset of any target.
Since n>=K and n<=L this proves

    B <= g/2 + 3nD/(2K) <= L(1+3D)/(2K).                     (5)

For D>sqrt(L) the shift count is already <D². If D<=sqrt(L) and some
nonidentity shift belongs to A, then (3) gives B>=L/(2cD). Equations
(3) and (5) imply K<=cD(1+3D)<6D² for D>=2. When A contains only the
identity, K=1 gives the claim directly.

## Locating a single low-distance shift

For d>sqrt(L/2), take k=1 and the nearest multiple aL to r. Otherwise
set N=floor(L/(2d²))>=1. Among 0,r/L,...,Nr/L modulo one, two points
have circular gap at most 1/(N+1), counting coincidences. Thus there are
1<=j<=N and p with |jr/L-p|<=1/(N+1). Reduce p/j to a/k. Then

    |r/L-a/k| <= 1/k²,       |kr-aL| <= L/(N+1) < 2d².

It remains to show k<8d. The k multiples of a/k form the uniform
grid on the circle. Use signed representatives u with |u|<=k/2. Each
u r/L is within 1/(2k) of its grid point. Every point is within 1/(2k)
of the grid, hence any two physical indices can be connected by at most
k/2 shifts by ±r followed by at most L/k unit steps. Equation (4) yields

    B <= k d/4 + L/k.

If k>=8d, then k<=N<=L/(2d²) puts the right side at most L/(4d).
This contradicts (3) because c<2. This calculation also covers a zero
residue kr-aL, which is a genuine low-order rotation.

The estimates do not rule out all high-distance or resonant shifts.
The [checker](shape_check.py) independently enumerates small binary circles
for the height, subgroup and displacement bounds used in the proof.
