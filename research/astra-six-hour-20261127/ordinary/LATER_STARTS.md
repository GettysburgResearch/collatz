# All later Mersenne starts at the ternary 590 control

Grant every later Mersenne form \(2^UN-1\), \(U\ge0\), as a possible initial bad label in the fixed-word grammar of the [590 theorem](../../astra-unconventional-20261126/renormalization/FINITE_COVER_BARRIER.md). The ternary coordinate is \(N_*=590\), and the limiting dyadic coordinate is zero. For each fixed starting form allow every finite ordinary forward or inverse word. The complete subcap list at \(\alpha\le128/81\) is still exactly the previous eight affine forms, all from \(U=0\). The conditional measure of controls having precisely this list in each ball \(N\equiv590\bmod3^D,\ D\ge385\), is at least
\[
                 1-\frac{1180(128/81)^2}{10000}>0.705 .
\]
Granting these initial bad labels is a formal strengthening of the word grammar. Ordinary badness of those later Mersennes has not been established.

Indeed the earlier signed clearing reduction applies unchanged at every fixed \(U\). At positive denominator depth, a candidate at 590 is an ordinary integer \(1\le x\le932\). Its clearing visit satisfies
\[
       T^h x=590\cdot2^{U+E'}-y,\qquad1\le y\le2^{E'},
\]
where the reflected orbit of \(y\) reaches one with exactly \(E'\) even departures. Every \(x\) through 932 reaches one in at most 113 clocks and the largest forward site is 125252. Thus \(590\cdot2^U-1\le125252\) forces \(U\le7\). The complete finite replay exhausts those offsets with the stronger cutoff \((590\cdot2^U-1)2^{E'}\le T^h x\) at each visit. Its seven clearing candidates all have \(U=0\). At nonpositive denominator depth the cap forces \(E=U=0\), producing the identity or its first forward edge. The identity is already among the seven, leaving eight distinct forms. [All-offset replay](check_later_peaks.py) · [Receipt](../../../reports/astra-six-hour-20261127/ordinary/later-590.json)

At depth \(D\) any legal prefix at any target in the ball is legal at 590, and its leading affine coefficient is \(\alpha=2^{E+U}(2/3)^D\). The [5,900,000-source replay and continuation bound](../../astra-unconventional-20261126/renormalization/HAAR_BARRIER.md) give \(\alpha>R=10000\) and a conditional chance at most \(A^2/\alpha^2\) to continue to a coefficient at most \(A=128/81\). This holds after identifying equal affine prefixes. At a fixed slope, across every \(U,E\) together there are at most \(590\alpha\) different prefixes as affine forms. Indeed the positive integer \(x=\alpha590-b\) determines \(b\) uniquely at fixed \(\alpha\), and it lies in \([1,590\alpha]\). For any two words giving the same form, the legal future depends only on that endpoint. The dyadic center and slope agree and the ternary target variation at depth \(D\) has full Haar law. Thus each distinct total \(U+E\) is counted once. Summing \(590A^2/\alpha\) over the doubling sequence of slopes greater than \(R\) costs less than \(1180A^2/R\). The shorter depth forms remain as in the 590 classification, proving the measure estimate.

This result does not constrain input-dependent postpeak words or other ordinary sources used in the positive results.
