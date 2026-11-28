# Adjacent forward and backward grid orbits from true low bits

Let a nontrivial positive ordinary cycle have least odd state \(m\), greatest odd state \(X<4m\), and least odd period \(p\). Use \(K=2m\), and fold every odd state \(x\) into the fundamental grid octave by \(z=cx\in[K,2K)\), \(c=1\) or \(2\). As in [the rounded-clock theorem](../phase8/DIGITAL_ROTATION.md), write a forward native edge after folding as
\[
                     Bz'=3z+c,\qquad B=2^b\in\{2,4\}.
\]
The \(z\) form a periodic orbit of the *backward* grid map \(G_K\), traversed in reverse native time. The immediate integer successors \(u=z+1\) form a periodic orbit of the *forward* grid map \(F_K\), in native time.

Indeed \(X\equiv1\bmod4\), since otherwise its odd successor \((3X+1)/2\) would exceed \(X\). Hence \(X\le4m-3\). The folded states obtained by doubling are at most \(2(2m-1)=4m-2\). Thus all shifted states are strictly inside the octave:
\[
                            K+1\le u\le2K-1.
\]
Their integer rounding law is exact,
\[
                    B u'-3u=B-3+c\in\{B-2,B-1\}.                    \tag{1}
\]
Since every target is at least \(K+1\), there is no finer half-grid point immediately below its normalized value. Formula (1) therefore gives the actual upward grid ceiling on every edge, including the chronological return to the least representative. The two cycles in this statement use adjacent grid positions. The general adjunction alone only identifies the absolute clocks, as the \(K=2\) example in the earlier note illustrates.

The complementary forward defect is \(2-c\in\{0,1\}\). At a genuine \(b=1\) date the transition \((c,c')=(2,1)\) cannot occur, by positivity of the native exponent \(e=b+\log_2c'-\log_2 c\). The lower-bit condition also excludes \(4\mid z\) at every date.

Increasing the resolution to \(K+1\) inserts the ray of \(K+1/2\). The upper orbit has minimum \(K+1\) because the least physical odd state folds to \(K\). At the incoming edge its winding is two and its defect is at least two by (1). Thus the newly inserted ray lies between its input multiplied by three and its former target, including possible equality at the new ray: this specific upper orbit is destroyed. Other upper orbits can preserve the common clock. For an exact larger orbit on the same prescribed calendar put \(u^{\rm other}=z+1+k\). Its edge condition becomes
\[
                      k'=\left\lfloor {3k+(2-c)\over B}\right\rfloor.\tag{2}
\]
In particular \(k=0\) is absorbing, and a nonzero periodic \(k\ge0\) is strictly positive at every date. The question whether the genuine low bits exclude such an orbit in the intervening spatial gap is open. If no other orbit exists, the [threshold inversion](STAIRCASE_INVERSION.md) would force \(U(A,p)=2m+1\) for the reduced native clock. The proved comparison alone gives \(U(A,p)\ge2m+1\).

### Calibrations of the strictness question

At resolution \(K=35\) the reverse orbit from 35 has period five, avoids multiples of three, and has largest state 61. The forward orbit shifted up by one satisfies (1), yet \(\eta_{35}=\eta_{36}=8/5\). One reverse state is divisible by four, and \(K\) is odd. At resolution \(K=6\) the reverse orbit is \(6,8,10\), its shifted companion is again a forward orbit, and \(\eta_6=\eta_7=5/3\). Here \(K\equiv2\bmod4\) as for an odd minimum, but the three-coprimality and four-freeness conditions fail. These examples isolate the extra arithmetic needed to force a change in the clock.

The [finite kernel](ClockInversion.lean) proves the translated rounding identity, the binary discrepancy in (2), the seam defect, and the finite progression interlacing telescope. The physical orbit, ordered fixed vector and resulting grid comparisons are written theorems.
