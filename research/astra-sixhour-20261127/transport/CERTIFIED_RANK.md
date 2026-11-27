# An exponential high-rank tail on upper-certified ordinary returns

**PROPOSED written theorem.** The shortcut is \(T(2x)=x,\ T(2x+1)=3x+2\).
A rooted word takes \((Y,3Y-1)\) to \((X,3X-1)\) in \(H\) common clocks,
making \(p\) odd departures on each arm. At time \(t\), write
\(d_t=b_t-a_t\) for upper minus lower odd count, so that the affine
rank in the [preceding packet](../../astra-unconventional-20261126/operator/PAIRED_CAPACITY.md)
is \(1+d_t\). Put \(R(w)=\max_{t\le H}|d_t|\) and \(M(w)=3^p/2^H\).
Fix \(B>0\) and an ordinary target cutoff \(X_0\ge2\). Let \(\mathcal W\)
be the distinct words having an ordinary realization with \(X\ge X_0\),
\(Y\le BX\), and with \(3X-1\) reaching 1. The lower arm may escape, enter
any cycle, or undergo repeated laps. Each word is counted once.

There is a finite \(D(X_0)\le (3/2)512\), with \(D(X_0)\to1\), such that
for every \(R,H_0\ge0\) and \(1<s\le2\),
\[
 \sum_{\substack{w\in\mathcal W\\R(w)\ge R,\ H(w)\ge H_0}}3^{-p(w)}
 \le [B D(X_0)]^s\,d_s^{\max(H_0,2R)}
       \frac{2(1+\eta_s)}{(1-\eta_s)(1+\eta_s^{-R})},
 \quad
 d_s=\frac{1+3^{s-1}}{2^s},\qquad \eta_s=3^{1-s}.                 \tag{1}
\]
The cutoffs are integers. In particular the all-clock tail at \(s=2\) is
\(4[B D(X_0)]^2/(1+3^R)\). For \(1<s<2\) the factor \(d_s<1\) also gives
exponential decay in a simultaneous clock cutoff. Every earlier
\(|1+d_t|>12\) path has \(R(w)\ge12\).

## The rank walk at the mismatch clocks

For the lower parity word, independently choose each next bit \(e\)
with \(\Pr(e=1)=q\). Any finite lower word determines the source's binary
residue, hence forces the upper word. At the current integral affine
state \((1+d,c)\), the upper bit is \(f=e+(c\bmod2)\bmod2\).
The clock is a mismatch precisely if \(c\) is odd, a decision already
made before exposing \(e\). Thus the mismatch increments \(f-e\) are
\(+1\) with probability \(1-q\) and \(-1\) with probability \(q\).
One may prepare independent Bernoulli streams for mismatch and common
clocks, drawing from the appropriate stream according to the past.
After a merger or if there are only finitely many physical mismatches,
continue the unused mismatch stream independently; its full simple walk
dominates the count of actual visits in the argument below.

A contextual root return has \(d=0,c=-1\). In particular the *next*
clock must mismatch. There is at most one such visit at each mismatch
index, including index zero. Every ordinary word counted above is a
contextual return: its final grades are equal, so equality of the
required affine line at a single positive realization fixes the
intercept identically on its dyadic cylinder.

For \(q>1/2\) put \(\eta=(1-q)/q<1\). The full mismatch walk starting
at zero has \(G=(1+\eta)/(1-\eta)\) expected visits to zero, including
the initial one: its return probability after the first step is
\((1-q)+q\eta=2(1-q)\). Hitting zero from \(-R\) has probability
\(\eta^R\), and hitting from \(+R\) has probability one.
These hitting probabilities follow by solving the two-term gambler's-ruin
recurrence on finite intervals and then increasing their far endpoint.
On first exit to either endpoint of \([-R,R]\), the probabilities of
\(+R,-R\) are respectively \(\eta^R/(1+\eta^R),1/(1+\eta^R)\).
Consequently the expected number of visits to zero *after* the maximum
absolute displacement has reached \(R\) is \(2G/(1+\eta^{-R})\).
For \(R=0\) this formula equals \(G\) directly. The clock sum of lower
Bernoulli probabilities of the actual return words shares this upper
bound. It counts every visit, rather than only first returns.

## The physical change of weights

For any realization in \(\mathcal W\), the upper target is at least
five, converges to 1, and is transient. All its upper-path departures
before reaching it are distinct; an earlier repetition would prevent
the first visit to a transient target, and a transient target is
visited only once. Write \(C(X_0)\) for a common upper bound on the
odd-step distortion products of all these upper paths. One can take
512 from [the standalone distortion estimate](../../astra-unconventional-20261126/operator/SUFFIX_MASS.md).
The same estimate's convergent series of shell majorants has tails
tending to zero for the sum of reciprocal odd departures.
Given an ordinary floor \(F\), each good starting integer up through
\(F\) has a finite forward orbit. Their finite union has a finite
maximum. Once \(3X_0-1\) exceeds it, every upper path here stays above
\(F\); a nongood start cannot reach a good target. Thus one can take
\(C(X_0)\to1\), with no effective height threshold asserted.

The telescoping identity on the upper arm gives
\[
 M(w)\ge \frac{3X-1}{(3Y-1)C(X_0)}
       \ge\frac{1-1/(3X_0)}{B C(X_0)}
       =\frac1{B D(X_0)}.
\]
For \(q_s=3^{s-1}/(1+3^{s-1})\) the Bernoulli probability \(\nu_s(w)\)
of the lower word satisfies
\[
                  M(w)^s3^{-p(w)}=d_s^{H(w)}\nu_s(w).
\]
Strict log-convexity gives \(d_s<1\) between 1 and 2, with equality at
both endpoints. A word returning to zero after displacement \(R\) needs
at least \(2R\) clocks. Apply the rank-walk visit estimate and the previous
lower bound for \(M\) to obtain (1). A single source's realized bits have
nowhere been assumed random; the biased law counts distinct finite words.

## Why an upper certificate gives no uniform ternary maximum principle

A rooted word of grade \(p\) is legal at exactly one lower terminal
class modulo \(3^p\). Its source is \(Y=(2^H X-c_w)/3^p\); once the
terminal is in that class and sufficiently large, this is a positive
ordinary realization of the stipulated two-arm word. In fact choose
\[
                  X_j=\frac{2\cdot4^j+1}{3}\quad(j\ge0).
\]
Then \(3X_j-1=2\cdot4^j\) reaches 1 using no odd departures. For
distinct \(j,j'\), \(v_3(X_j-X_{j'})=v_3(j-j')\), by
\(v_3(4^a-1)=1+v_3(a)\). Thus these \(X_j\) cover every ternary
class, with arbitrarily large ordinary representatives. Along any
compatible class \(Y/X\to1/M(w)\) from below or with equality.

Even a prescribed longer upper prefix allows this variation. Given
\(T^\tau(3X-1)=1\) with \(q\) odd departures, put
\[
 X_j=X+2^\tau\frac{2^{2\cdot3^qj}-1}{3^{q+1}}\quad(j\ge1).
\]
The same \(\tau\)-clock upper word now ends at \(2^{2\cdot3^qj}\);
only halvings follow. Its first hit at 1 is at \(\tau+2\cdot3^qj\),
since an earlier hit would force the state at \(\tau\) to be 1 or 2.
Again \(v_3(X_j-X_{j'})=v_3(j-j')\), so this very prefix and fixed
upper odd count allow arbitrarily large representatives in every ternary
class. Fixing both the complete word and its endpoint exactly at 1
instead specifies one ordinary terminal.

For every \(R\) there is a nonmerged prefix of \(R\) lower even clocks
and \(R\) upper odd clocks: choose \(2^R\mid Y\), and \(3Y-1\equiv
-1\bmod2^R\). The prior [rooted completion controller](../../astra-unconventional-20261126/descent/TRANSLATIONS.md)
extends this prefix to a contextual return. Append sufficiently many
copies of any fixed [return of multiplier greater than one](../../astra-unconventional-20261126/operator/PAIRED_GAIN.md).
The resulting return still reaches distance \(R\) and can have arbitrarily
large \(M\). Realize it on the preceding upper-certified targets. Therefore
for any fixed \(B>0\) the high-rank tail of the pointwise inverse sum
of \(M(w)^s\) over eligible words has unbounded supremum on those
ordinary terminals, even with a prescribed upper prefix and fixed upper
odd cost. Formula (1), by contrast, sums the *masses of their legality
cylinders*, and by integration gives no pointwise bound for a prescribed
ordinary terminal. The construction does not fix the lower component
of these auxiliary upper-certified realizations.

There is a local obstruction at any \(X\) with contextual incoming
words of unbounded grade. Given a neighborhood \(X\bmod3^L\), choose
an incoming word \(v\) at \(X\) with \(p(v)\ge L\). Append this *fixed
suffix* to the high-rank and gain-producing word above, increasing the
number of gainful repetitions to offset \(M(v)\). Every final terminal
of the full contextual word now belongs to the legality cylinder of
\(v\) and hence to \(X\bmod3^L\). The same upper-certified realization
works. Thus the unnormalized operator is unbounded in every such
neighborhood. Infinitely many distinct incoming ordinary sources at a
fixed target require unbounded grades by the prior
[fixed-grade clock bound](../../astra-unconventional-20261126/operator/PAIRED_CAPACITY.md).

The physically normalized sum behaves differently. For \(s>1\) put
\[
 F_{s,R}(X)=\sum_{\substack{Y\to X\ {\rm ordinary\ paired}\\R(w)\ge R}}
                         (M(w)/X)^s
\]
on the upper-good positive terminals \(X\ge2\), even without a height
budget on \(Y\). Each fixed \(Y\) contributes at most once to a given
\(X\), since the upper target is transient. Every contributing \(Y\)
has a good upper with finite trajectory, hence contributes at only
finitely many terminals and ranks. Finally \(M(w)\le X/Y\) by the
physical lower-arm height product, regardless of repeated lower cycles.
The tails from \(Y>J\) are bounded simultaneously by
\(\sum_{Y>J}Y^{-s}\). Finite truncation gives
\[
 \sup_{X\ {\rm upper\ good}} F_{s,R}(X)\longrightarrow0\quad(R\to\infty),
 \qquad F_{s,0}(X)\longrightarrow0\quad(X\to\infty\text{ in ordinary height}).
\]
In the ternary topology upper-good lifts \(X_j\to X\) can have unbounded
ordinary height, so such an ordinary trace with positive value at \(X\)
cannot be continuous there. The tail truncation uses \(s>1\).
