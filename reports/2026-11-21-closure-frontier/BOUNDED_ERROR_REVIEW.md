# Independent review of the bounded-error conversion TM7

**VERIFIED AS A SOURCE-QUALIFIED CONSEQUENCE.** TM7 was contributed by
the author of the finite-conductor note, and was independently reconstructed
by the author of TM1--TM6. This division avoids counting authorship as an
independent review. The other ternary claims have their separate review.

Reviewed note: `TERNARY_STATIONARY_BOUNDARY.md`, SHA-256
`543c0bd7a72d5dec598898850a49a257a9ef3b55cd1fff8741d8699fbad57a7c`.

For the same actual bounded ordinary error `0<=e<=1`, split the periodic
density at precision `m`: `g_s=g_m+(g_s-g_m)`. The first term is bounded
pointwise by `2^m e`; the second by `|g_s-g_m|`. Its ordinary average
is exactly the Haar average because this last function is periodic.
No frequency assumption about the error itself is needed. Tao's
Proposition 1.14 bounds that Haar average uniformly in `s>=m`; when
`s<m`, the simpler bound `g_s<=2^m` suffices. This proves the displayed
uniform estimate with the same supplied error on both sides.

Taking `m=floor(log_2(1/delta_H)/2)` gives a first term at most
`sqrt(delta_H)` and an inverse-logarithmic second term. The zero-density
case follows separately from boundedness of each fixed periodic density.
At a cutoff divisible by `3^s`, the periodic average is already exactly
the Haar average, so the finite-scale statement also holds. Applying the
uniform constants to the varying errors `e_s` is valid: a fixed stretched
exponential upper bound and any fixed `A>1/beta` give `s delta_s->0`.
The constant-anchor argument from TM3 proves the claimed weighted-mean
conclusion for Boolean labels.

I independently opened the published Cambridge article and checked the
normalization, consistency identity (1.23), and Proposition 1.14 with its
definition (1.27). Its full Fourier proof is not re-proved or computationally
replayed here. The inference from that input is elementary and the constants
are uniform in the required parameters.

No defect was found. The statement does not create the needed ordinary
approximation and does not provide pointwise rigidity from mean constancy.
Those omissions are explicit in TM7 and remain outside this verdict.
This is internal agent reconstruction, not external acceptance or formal
proof-assistant verification.
