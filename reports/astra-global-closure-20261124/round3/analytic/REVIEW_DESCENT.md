# Independent reconstruction of the ordinary descent results

Reviewed the source bytes below. The maintainer recorded a separate fresh Lean build. I reconstructed the word arithmetic and original-floor inequalities independently.

| Source | SHA-256 |
|---|---|
| descent/README.md | df17d87e4039771ff585347a1ba8fe979f9d2a8bdf69b3030c2a9c2dc9c5013d |
| descent/RESET_AVOIDANCE.md | 66ca9281f4ebd397e39e827c2e1d6092b6dd13a72286046667de31cab229663a |
| descent/TwoLight.lean | fdddc3ede29502691ea2a27354abdd8b09faee98fc0f338bb3b970c9cf141964 |
| descent/ResetTiles.lean | 78a285a2933ef970f4f0f91d64e169f5c42ec3fe7b7fb1575c13e0e6ac3f69a3 |
| descent/LoopCone.lean | a468fc36f293b3314342558ef438f6de46d7baf1ff0dc87c3571a9cf80a93c60 |
| Earlier ResidualDescent.lean, including WordCert.realize | b5f149855866419b771e49127bdaabd1cb5749ec7d6f3b6091f3fb54bf1ccc98 |

## Infinite reset words and the catalog

**Verified.** For a chronological parity word, accumulate \(D,M,C\), initially \(1,1,0\). On an odd bit replace \(M,C\) by \(3M,3C+D\), then double \(D\) on either bit. This reconstructs the six source and target words in the Lean file. Each pair has the same \(D=2^A\), \(M=3^p\) and satisfies \(183C+D=M+128K\).

| Source | \(A\) | \(p\) | Source \(C\) | Target \(K\) |
|---|---:|---:|---:|---:|
| L | 3 | 2 | 7 | 10 |
| LLP | 11 | 6 | 1391 | 1999 |
| LLPP | 16 | 8 | 22759 | 32999 |
| LLPLPP | 24 | 12 | 5533975 | 8038775 |
| LLPPPLPLPP | 42 | 20 | 1373787197047 | 1998418881143 |
| LLPPPPLLLLP | 43 | 22 | 12698232390191 | 18222978432559 |

Set \(N_i=183q_i+1\). The source equations give \(D_iN_{i+1}=M_iN_i+128K_i\). Since \(8\mid D_i\) and \(M_i\) is odd, three future equations give \(8\mid N_i\), then \(64\mid N_i\), then \(128\mid N_i\) for every \(i\). In fact \(q_i\equiv121\bmod128\). Dividing by 128 gives the target word equation on \(Y_i=N_i/128\). In an ordinary word equation the first parity is forced modulo 2 by oddness of the remaining multiplier, and removing that bit gives the next such equation. This proves legality on integers. Every \(Y_i>2\), and the positive word lengths give unbounded cumulative clocks. If the target hit 1 at any time, all later endpoints would lie in \(\{1,2\}\). Hence \(Y_i\) is nonconvergent. At \(q_0+7=1024v,\ v\ge1\), \(Y_0=2m\) and \(m=732v-5\) is positive odd and below both \(q_0=1024v-7\) and the original light intermediate \(768v-5\). The affine association proves nonconvergence of the second trajectory without requiring an actual intersection of the two orbits.

**All positions in the six-tile language, verified as a written corollary.** At a catalog boundary the first three letters are LLP or LLL. The former gives direct descent at the paid endpoint. For LLL, \(8^3(q_3+7)=9^3(q+7)\) and odd \(q_3\) give \(1024\mid q+7\), as required by ResetTiles. Within a nonsingleton the next P follows \(0\le h\le4\) light blocks, since every such tile ends with P and the largest internal L-run is four. For \(h=0\) the next paid endpoint lies below \(q\) and its paid intermediate. For \(h\ge1\) the light source \(x\) is \(9\bmod16\) and so \(x\ge9\). The paid endpoint \(w\) satisfies
\[
 32w=9(9/8)^h(x+7)-58,\qquad
 256w\le117x+355<192x+64=256(3x+1)/4 .
\]
Here \((9/8)^4<13/8\). This gives both original floor inequalities. All those forward source endpoints are nonconvergent because later physical tile boundaries exceed 2 at arbitrarily large clocks. This result assumes the infinite source tiling. For the older residual headers the displayed factorizations \(\mathrm{LLPP}\cdot\mathrm{L}^3,\ \mathrm{LLP}\cdot\mathrm{LLPP},\ \mathrm{LLP}\cdot\mathrm{LLP}\cdot\mathrm L\) reproduce precisely the three words after prepending LL. The other thirteen header certificates are imported.

My finite check lifted each source's required parity bits one by one. Adding \(2^i\) to a source after \(i\) prescribed steps toggles the next parity via an endpoint shift of \(3^{p_i}\). All 216 ordered triples of catalog tiles with an LLP continuation gave strict original-floor inequalities at all 3,780 tested positions.

## Direct finite descent in the cone

**Verified.** One PLL takes \(z\) to \(z'\) with \(2048z'=729z+4213\). The real fixed point \(4213/1319<4\) gives \(z_s\le(729/2048)^s z_0+4\). The initial lights satisfy \(q_r+7=(9/8)^r(q_0+7)\). For the next paid endpoint one gets
\[
 32w\le9(9/8)^r(729/2048)^s(q_0+7)+41 .
\]
The stated cone gives \(160w\le117q_0+1024\). Three initial genuine lights force \(q_0+7\) a positive multiple of 1024, so \(q_0\ge1017\) and its light intermediate is integral. The inequalities \(0<w<(3q_0+1)/4<q_0\) follow, using the stipulated oddness of \(w\). This is a later ordinary point of the source itself. Its direct descent applies with any valid continuation.

## Positive intercept and the size obstruction

**Verified for the stated symbolic nonreturn; the proposed ordinary nonconvergence inference fails.** For an entry word with clocks \(A\), source odd count \(p\), and carry \(C\), the target requires \(p-2\) odd inputs and \(384K=61C+1195\cdot2^A-3^{p-1}\). Independent parity lifting for each of the four source entries followed by LL and an odd endpoint, and direct iteration from \((183x+1)/128\), gave \((A,p,K)\) respectively
\((61,34,8369972547102266119)\), \((58,32,1040345204821122287)\), \((53,30,32641194658480951)\), and \((67,38,536649599247780160663)\). At the terminal source \(q\), \(61(q+7)/384+2\) is integral because the next two L supply \(128\mid q+7\), and the preceding L supplies \(3\mid q+7\). The exact target carry and odd count then extend the identity to the full prescribed cylinder.

Write \(Q=q+7,\ Y=aQ+c,\ R=c/a\). The L and P updates are \(8Q'=9Q\) and \(32Q'=9Q+166\). With \(k\) target odd steps, \(a'=3^{k-2}a\); nonnegative target carries give \(R'\ge9R/8\) on L, \(R'\ge(9R-166)/32\) on P. Starting at \(R=768/61>12\), at least 37 L and three arbitrary letters maintain a positive intercept throughout and return \(R>12\). Three P are the smallest possible updates during the burst. The original chart has intercept \(-10\), excluding identity with any such subsequent chart on an unbounded ordinary residue class. Any fixed-clock uniform identical return must also have matching odd count and clocks by unique factorization of the slopes. Isolated numerical meetings remain possible.

For the ordinary size check, let \(b\) count source blocks, \(A\) their clocks and \(u\) target odd visits. Convergence of the target gives \(u=A/2+O(1)\) on the eventual cycle \(1,2\). Each source block has multiplier \(9/2^\ell\) with additive numerator at most 7. For physical \(q_i\ge3\),
\[
 q_b\le q_0\,3^{2b}2^{-A}(34/27)^b,\qquad
 a_b Q_b=O\!\left((\sqrt3/2)^A(34/27)^b\right)
        =O\!\left((17\sqrt3/36)^b\right).
\]
Indeed \(Q_b\le(10/3)q_b,\ a_b=(61/384)3^{u-2b},\ A\ge3b\), and \(17^2\cdot3<36^2\). Thus the slope contribution decays under the hypothetical convergence. On the sparse group family an upcoming run of \(r\) lights also gives \(3r\le b\log_2(9/8)+O(1)\), incompatible with the proposed lower threshold \(0.67b+O(1)\). Surviving positive intercepts alone do not refute convergence of the comparison for an ordinary source. Arbitrarily large positive realizations of each finite parity string do not produce one positive integer realizing the full infinite schedule.
