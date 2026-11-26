# Strict contraction through relative rank twelve, at every integer carry

**SOURCE-QUALIFIED computer-assisted proof, O8.** Use the normalized integer carry \(c\) and relative rank \(r=1+b-a\) in [PAIRED_CAPACITY.md](PAIRED_CAPACITY.md), where \(a,b\) are the lower and upper odd counts. Delete transitions that reach \(c=0\) or \(|r|>12\). On this countably infinite graph give a transition of bit pair \(e,f\) weight \(3^{-e-f}\), and let \(K\) sum weighted successor values. There is a positive \(h\) satisfying \(Kh\le(9/10)h\) everywhere. Carries have no upper cutoff in this assertion. If \(W_{p,12}\) counts *all* root-to-root pair words of grade \(p\) whose entire rank path stays in the stated strip, then
\[
                     W_{p,12}\le 10(81/10)^p .
\]
Indeed \(K^Hh(1,-1)\le(9/10)^Hh(1,-1)\), whereas every return word of clock \(H\) and grade \(p\) contributes \(9^{-p}h(1,-1)\). Sum over \(H\ge p\). The comparison applies to arbitrary, not just primitive, returns. A word that crosses the rank cutoff and comes back is outside this bound.

## All-carry verification

Writing \(r'=r+f-e\), the exact successor is
\[
  c'=\big(3^{(-r')_++f-(-r)_+}c+3^{(-r')_+} f-3^{(r')_+} e\big)/2 .
\]
Even \(c\) allows bits \(00,11\), and odd \(c\) allows \(10,01\). In both cases these are the only choices. The certificate includes integer carries divisible by three, even where a physical forward path would give a ternary unit. Reflection \((r,c)\mapsto(-r,-c)\) exchanges the arms and preserves all weights.

Start from \(b(c)=\lceil100\sqrt{|c|}\rceil\) at \(c\ne0\), with \(b(0)=0\). Whenever \(|c|>4\cdot3^{|r|+1}\), an active successor has \(|c'|\le13|c|/8\), since the multiplier is at most three and the additive part is at most \(3^{|r|+1}\). An idle successor has absolute value \(|c|/2\). Use \(1/\sqrt2<71/100\) and \(\sqrt{13/8}<13/10\). For even \(c\),
\[
 Kb(r,c)\le 100\sqrt{|c|}\big(71/100+13/90\big)+10/9 .
\]
For odd \(c\), \(Kb(r,c)\le100\sqrt{|c|}(13/15)+2/3\). Both are at most \((9/10)b(c)\) for every \(|c|\ge1\) to which the preceding tail estimate applies. This proves the tail comparison simultaneously at every rank.

The finite core is \(0<|c|\le4\cdot3^{|r|+1},\ |r|\le12\). The [integer checker](rank_pressure.cpp) raises selected values of \(b\) to enforce the comparison, and then begins a separate verification pass in which it cannot change any weight. It checks each core state and each possible predecessor of every raised state. For all other states, every surviving successor has its original weight, and the analytic tail comparison gives \(Kh=Kb\le(9/10)b\le(9/10)h\). For a fixed successor and bit pair the integer carry equation has at most one predecessor; the inverse scan solves that equation including both reflected representatives. A failed comparison, range check or iteration limit aborts the replay.

The immutable pass made 23,090,720 checks, including duplicates. Its weight differs from \(b\) on 835,391 reflection classes, the largest changed absolute carry is 2,684,354,560, and \(h(1,-1)=190\). The program uses integer square roots, powers and cross-multiplication. The initial core search is a way to construct a witness. The separate comparisons and the analytic tail establish its property. [Replay receipt](../../../reports/astra-unconventional-20261126/operator/rank_pressure_12.txt).

From the repository root, run:

~~~sh
c++ -O3 -std=c++20 -Wall -Wextra -Werror research/astra-unconventional-20261126/operator/rank_pressure.cpp -o /tmp/collatz-rank-pressure
/tmp/collatz-rank-pressure 12
~~~

## Where the unrestricted kernel first differs

At a positive rank \(r\), put \(e=v_2(3^r-1)\). If \(2^e\mid c\), every length-\(e\) common word \(w\) is available, with total weight \((10/9)^e\) as in [COMMON_HOLDS.md](COMMON_HOLDS.md). There is also an exact output constraint. Write \(u=(3^r-1)/2^e\), and \(c_w\) for the ordinary affine offset of the common word with \(k\) odd departures. Its output carry is
\[
                     c'=3^k(c/2^e)-u c_w.
\]
Given \(k\) and a desired residue \(c'\pmod{2^j}\), \(0\le j\le e\), the first \(j\) bits of \(w\) are determined: if \(x\) realizes \(w\), its affine endpoint gives \(c_w\equiv-3^k x\pmod{2^j}\), and \(u3^k\) is odd. Thus the total weight of common words landing in one specified residue modulo \(2^j\) is at most
\[
                            \tfrac98(10/9)^{e-j}.
\]
In detail, for given total grade \(k\), the prefix specifies its grade, so the tail has some determined grade \(m\le k\). Sum the upper bounds \(\binom{e-j}{m}9^{-k}\) over all \(0\le m\le k\) and then over \(k\). In particular, requiring all \(e\) output bits costs away the unrestricted growth at that one hold. A single ordinary pair wandering outside rank twelve need not prescribe such a restoring residue. Uniform control of excursions entering higher ranks is OPEN.

## No rank-independent per-clock factor on every affine state

For every \(L\ge3\), let \(D=2^L-3\), choose \(r\ge1\) with \(3^r\equiv1\bmod D\), and put \(c=-(3^r-1)/D\). Such a rank exists since \(3\nmid D\). The affine state \(y=3^r x+c\) has \(c\ne0\) and fixes the odd-denominator rational \(z=1/D\). Under the shortcut, one odd followed by \(L-1\) evens takes \(z\) back to itself, since \((3z+1)/2=2^{L-1}/D\). On the pair chart the common odd sends \(c\) to \((3c+1-3^r)/2=2^{L-1}c\), and every common even halves it. All carries on this loop are nonzero. Its total weight under \(K\) is \(1/9\).

Every finite number \(n\) of repetitions has positive ordinary realizations: choose arbitrarily large integers \(x\equiv D^{-1}\bmod 2^{nL}\), and put \(y=3^r x+c\). Both coordinates have the same first \(nL\) bits as \(z\), and their difference stays nonzero because equal parity branches are injective. The rational point specifies the cylinder. The ordinary points witnessing longer repetitions may change.

Consequently no everywhere finite strictly positive weight \(h\) on **all** nonmerged affine states can satisfy \(Kh\le\rho h\) for one \(\rho<1\). Iterating on this particular loop would require \(1/9\le\rho^L\) for every \(L\). This rules out extending the strip certificate to every rank and carry with a common per-clock rate. The construction does not establish accessibility of these charts from the fixed root \((1,-1)\). Its repeats contribute geometrically by odd grade, so the root return series and a possible grade-based estimate remain open.
