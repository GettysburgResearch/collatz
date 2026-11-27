# An all-clock height budget for ordinary paired returns

**PROPOSED written theorem.** Use the positive ordinary shortcut map
\(T(2n)=n, T(2n+1)=3n+2\). A paired word of length \(H\) sends
\((Y,3Y-1)\) to \((X,3X-1)\) with the same odd count \(p\) on both arms.
Let \(W_p(B)\) count distinct words for which at least one positive ordinary
realization satisfies \(Y\le BX\), with \(B>0\). Different realizing integers
and repeated occurrences of the same word do not increase the count.
There is an absolute constant \(K\) with

\[
             \sum_{p\ge0}3^{-p}W_p(B)\le K\min(B,B^2).                 \tag{1}
\]

There is no bound on the clock, grade, relative rank, number of positive
cycles or length spent on a cycle. The endpoint-height condition is essential
to the argument. Its lower-arm proof works for any upper chart for which the
lower word determines the upper word on the same realizing cylinder.

## The weighted occupation estimate

For a binary word of length \(h\) with \(k\) ones, write
\(M=3^k/2^h\). Put \(A(D)=\sum_{w:M(w)\ge1/D}3^{-k(w)}\), including the
empty word if eligible. Then \(A(D)\ll\min(D,D^2)\) for every \(D>0\).
Here and below constants are absolute.

Give each bit an independent fair distribution, put \(S_h=\log M_h\), and
choose \(\theta=1/2\). The multiplier
\(r=(1+\sqrt3)/(2\sqrt2)<1\) satisfies \(\mathbb E e^{\theta S_h}=r^h\).
At the first visit to any particular unit interval, the expected number
of visits to that interval from then on is at most
\(K_0=e^{\theta}/(1-r)\). Indeed, at lag \(j\) a further visit requires a fresh
increment sum at least \(-1\), whose probability is at most
\(e^{\theta}r^j\). Independence at this stopping time follows by summing over
the countably many finite first-entrance words. For an interval with left
end \(s\), the first-entrance probability is at most \(\min(1,e^{-s})\):
\(M_h\) is a nonnegative mean-one martingale and its probability of ever
attaining \(e^s\) is at most \(e^{-s}\). This last assertion also follows by
prefix-free summation of the word weights \(2^{-h}M_h=3^k4^{-h}\).

Decompose \([-\log D,\infty)\) into unit intervals with left endpoints
\(s_j=j-\log D\). A word contributes \(2^{-h}e^{-S_h}=3^{-k}\), so

\[
 A(D)\le K_0\sum_{j\ge0}e^{-s_j}\min(1,e^{-s_j})
 \le K_0\min\bigl(D/(1-e^{-1}),D^2/(1-e^{-2})\bigr).
\]

## First hits and all repeated final laps

On a physical path the endpoint/source ratio is \(M\) times
\(\prod_{x {\rm odd departure}}(1+1/(3x))\). Use the absolute bound
\(C=512\) for this product on paths with distinct departing values, from
the elementary shell calculation in
[the source distortion proof](../../astra-unconventional-20261126/operator/SUFFIX_MASS.md).
That proof counts the odd departing values and includes the last clocks
before a truncation. The same proof applies to the distinct departing
values of one primitive lap.

Choose any one witnessing realization of each paired word. Its lower word
has a prefix ending at the first visit to \(X\). All departures of that
prefix are distinct, including when \(X\) is periodic, since any earlier
repetition would force a first visit to \(X\) within the first repetition.
Hence \(M_{\rm prefix}\ge1/(CB)\). If the prefix ends before the full
word, determinism forces the nonempty remainder to consist of \(n\ge1\)
copies of the primitive cycle lap based at \(X\). Its multiplier satisfies
\(M_{\rm lap}\ge1/C\), since its endpoint/source ratio is one. Its grade
\(k\) is positive, because a positive orbit cannot cycle using only halvings.

At fixed length the lower word determines the realizing residue
\(Y\bmod 2^H\), hence \(3Y-1\bmod 2^H\) and the entire upper word. Thus the
map from the selected pairs to their prefix, optional primitive lap and
repetition count is injective: their concatenation recovers the lower word.
No uniqueness of the split across *different* witnesses for a word is needed.
Summing over even inadmissible combinations gives

\[
 \sum_p3^{-p}W_p(B)\le A(CB)
     \left(1+\tfrac32 A(C)\right),
\]

since \(\sum_{n\ge1}3^{-nk}\le(3/2)3^{-k}\). As \(C\) is fixed this proves
(1), including \(CB\ge1>B\) by adjusting the absolute constant.

## Scope of the capacity bound

Fix one entrance residue \(Y\equiv a\pmod{3^L}\). A specified paired
word of grade \(p\) permits at most one residue of \(X\bmod3^{L+p}\)
by its lower affine equation \(2^HX=3^pY+c_w\). On normalized ternary
Haar measure the terminal union has mass at most
\(K3^{-L}\min(B,B^2)\). If a finite collection covers every ordinary
target in a terminal cylinder modulo \(3^b\), then its union contains
that entire ternary cylinder, by reducing at one common modulus.
The same conclusion follows if a countable collection covers the
entire ternary cylinder. In either case
\(3^{L-b}\le K\min(B,B^2)\).
Countable coverage of just its positive ordinary targets does not entail
coverage of that cylinder on Haar measure. The fixed-source steering
and universal Collatz questions remain open.
