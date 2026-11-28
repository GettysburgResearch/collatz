# First return to an unlike right corner

Use the positive shortcut map and the binary invariant color of
[the address argument](DYADIC_BOUNDARY_ADDRESSES.md). Set
`g(v)=f(v+1)-f(v)`. Indices with `g(v) != 0` have their literal
signed orientation.

After a zero choice from an odd lower endpoint, the new upper endpoint
`B` is odd and `B-1,B` have opposite colors. If there is another zero
then, setting `m>=1` equal to half the distance in digits between these
two zeros, its upper endpoint is exactly

    B' = 4^m B - 1.

More explicitly, the lower endpoints during intervening right choices
are `2^h B-1`, with `1 <= h < 2m`. Their color is `f(B-1)`.
The next midpoint `2^(2m) B-1` has color `f(B)`, since the next
choice is left. Thus `2m` is the first positive index with
`f(2^h B-1)=f(B)`. If the next zero never occurs, all these integer
shadows have color `f(B-1)`. Every shadow has the same color as
`3^h B-1`: its first `h` shortcut steps are all odd and end there.

There is an exact opposite-color multiplier defect at **every long
return**, meaning `m>=2`:

    f(3B') = f(B-1) != f(B').

In fact write `n=(B'-1)/2=2^(2m-1)B-1`. The intervening right
choices give `f(n)=f(B-1)`, and `n=3 mod 4`. Its first two
departures are odd and it attains `(9n+5)/4` after them. Since
`B'=2n+1`, the first odd departure from `3B'` has predivision
value `9B'+1=2(9n+5)`. Taking the odd part on both sides proves
that `3B'` and `n` physically merge. The proof applies in either
orientation. Infinitely many long returns therefore give infinitely
many such literal defects, all inside one explicitly nested
sequence of dyadic corners.

At a late short return the same argument does not apply: `B` is odd,
so `4B-1=3 mod 8` and its associated `n=2B-1` is `1 mod 4`.
If all sufficiently late returns are short, the original address
eventually alternates, with period two. Finitely many zeros give an
eventual all-ones address. These special alternatives have not been
excluded.

The elementary identity behind the single-edge marked image is

    g(2n) = g(3n+1)    for odd n.

Indeed `f(2n)=f(n)=f(3n+1)` and `f(2n+1)=f(3n+2)`.
Consequently testing counted mergers at a marked ternary edge by itself
adds no stronger test to the corresponding binary prefix: after one
step from `2n,2n+1` the states are `n,3n+2`. The trajectory from
`n` and that from `3n+1` agree one step later. If the latter pair
`3n+1,3n+2` counted-merges at a positive time `t`, the original
pair counted-merges at `t+1`, since the initial one-step odd-count
offset is cancelled by the extra odd departure from `n`.

These statements narrow a potential transport argument to corner
returns, with all colors evaluated at ordinary integers. They neither
supply a smaller defect at the first long return nor exclude an
infinite succession of such returns.
