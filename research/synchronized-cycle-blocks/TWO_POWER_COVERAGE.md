# Two disjoint powered factors leave a positive fraction of every cycle

**PROPOSED, with the same Rhin and Eliahou inputs as the
[two-power exclusion](TWO_POWER_EXCLUSION.md).** In any primitive
nontrivial positive ordinary shortcut cycle of length L, two disjoint
cyclic factors U^a,V^b with a,b>=2 leave at least L/252 positions
uncovered. The powers, root words, locations, and both gaps are arbitrary.
More precisely, their total uncovered length d satisfies

    L <= 250d + 208 Z + 41s,
    Z=log_2(2m+2), s=log_2(L+1), m=least phase.                (1)

Thus even asymptotically their coverage is at most 249/250+o(1).
The argument requires the two factors themselves to be exact powers;
it allows arbitrary parities at all uncovered positions.

Use the notation and local divisibilities from the two-power note, and
write c=log_2 3, gamma=c-1, theta=gamma/c. We have c<8/5 and theta<3/8.
A gap of t physical steps changes log_2 of the positive state by at most
t in absolute value: each one-step ratio lies between 1/2 and 2. The
total absolute variation over the gap portions is thus at most d.

## Opposite directions

Cut just before the increasing power U and write the cyclic layout
U^a G V^b J. Let x,y be the endpoints of U^a and z,w those of V^b,
so x<y and w<z. The lower boundary states x and w are joined by J.
If m belongs to a gap, both lower boundary logarithms are at most
log_2(m)+d: in G use x<=y and w<=z, and in J both endpoints are
directly within d steps. If m is inside a power, the same fixed-offset
monotonicity as before puts it in the first U copy or the last V copy.
Its corresponding lower boundary obeys the previous local bound, and
the other lower boundary costs at most d additional logarithmic units.

Consequently equations (2) of the two-power note hold with Z'=Z+d:
use x for the starting 2-divisibility and w for the ending
3-divisibility. For a gap minimum one may take H=u-q. With g ones
in the gaps, the global length and odd count are au+bv+d and aq+bp+g.
As cg-d<=gamma d<=d, equation (3) there holds with s'=s+d.
The same two elementary estimates give au+bv<=208Z'+41s'.
Adding d proves (1).

## Identical directions

Both powers are increasing or both are decreasing. The sum of the
magnitudes of their endpoint log changes is at most d since the gaps
must undo their sum. Any two of the four boundary log heights differ
by at most 2d. For a base word of length t and h ones, repeated e>=2
times, the endpoint log change is e(ch-t) plus the sum of its positive
step corrections. The total of these corrections over the tour is at
most s. Thus

    |ch-t| <= (d+s)/2.

Set M=max(|U|,|V|) and P=max(a|U|,b|V|), so M<=P/2.
The last inequality implies

    max(t-h,gamma h) <= theta t + (d+s)/2.

If m lies inside a power, it occurs in its extremal copy. For an
increasing power the entering boundary has log at most log_2 m+t-h
by backward tracing. For a decreasing power the leaving boundary has
log at most log_2(m+1)+gamma h by forward tracing. If m lies in a gap,
some boundary has log at most log_2 m+d. In every case the log of
every boundary is at most Z+theta M+3d+s.

Apply the starting 2-divisibility of the longer full power at its entry
x. Its slope integers A,B satisfy max(A,B)<=2^(t+(d+s)/2). Its bonus C
satisfies C<=2^(t+gamma h). Hence

    P <= log_2(|B-A|x+C)
      <= t+theta M+Z+4d+2s+1
      <= (1+theta)P/2+Z+4d+2s+1.

Since (1-theta)/2>1/4, this gives
L<=2P+d<=8Z+33d+16s+8, which is bounded by the right hand side of (1).

Finally, the cited Rhin estimate gives Z<=16 log_2 L for L>=2, while
s<=2 log_2 L, and Eliahou's period bound gives L>=2^24 for a nontrivial
cycle. On this range 3410 log_2 L/L is decreasing and is at most
3410*24/2^24<1-250/252. Equation (1) therefore implies d>=L/252.
The stronger asymptotic constant follows directly from (1).

## Independent finite checks

The [exact replay](check_power_coverage.py) checks the local divisibilities,
direction, extremal-copy minimum and height inequalities on positive
ordinary cylinders. It also checks the arithmetic constants and a second
route to the cited length floor. Under Barina's published ordinary
verification through 2^68, a nontrivial minimum m exceeds 2^68. For its
total odd count Q, the step correction gives
0<L/Q-c<=1/(3m ln 2)<2^(-68). The fractions 16785921/10590737 and
17087915/10781274 strictly bracket the entire interval [c,c+2^(-68)],
as certified by rational bounds on the logarithms in the replay. Their
cross determinant is one. Every reduced fraction strictly between them
therefore has denominator at least 21372011. In particular L>=Q>2^24.
This independent calculation uses the published finite range as external
input. The local replay is bounded and separate from the proof.
[Barina, *Improved verification limit for the convergence of the Collatz
conjecture*, 2025](https://doi.org/10.1007/s11227-025-07337-0)
