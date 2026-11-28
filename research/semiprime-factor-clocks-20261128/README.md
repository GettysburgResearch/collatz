# Collatz first passage below the factors of an unbalanced semiprime

**PROPOSED written results.** Let \(T\) be the positive shortcut map, halving even inputs and sending an odd \(n\) to \((3n+1)/2\). Put \(\tau_b(n)=\inf\{j\ge0:T^j n<b\}\), allowing infinity. Use natural logarithms and set
\[
 d=\tfrac12\log(4/3),\quad v=\tfrac12\log3,\quad
 \mu=1/d,\quad \sigma=v/d^{3/2}.
\]
The family from PR #217 consists of \(n=pq\) with primes \(p<q\) and \(\log n<p\le(\log n)^2\). Its reduction of full convergence to convergence within the family imports separate dynamical results. The larger-factor theorem and the long ascending examples below use only classical prime estimates and the exact shortcut map. [PR #217 at a2d3f9c4](https://github.com/GettysburgResearch/collatz/blob/a2d3f9c44c798c1956d29f88d12ccb2904cb0eb4/research/astra-collision-factor-bridge-20261128/SEMIPRIME_SUFFICIENCY.md)

The companion [merger-floor note](FACTOR_MERGER_FLOOR.md) bounds how low a connection between the two actual orbits must reach and localizes the date of their first common vertex under the stated timing input.

## The larger-factor clock

Let \(X\to\infty\). For each prime \(\log X\le p\le(\log(2X))^2\), sample \(q\) uniformly among the primes in \((X/p,2X/p]\). For each fixed real \(z\), uniformly over these \(p\),
\[
 \Pr\!\left(\tau_q(pq)\le\mu\log p+z\sigma\sqrt{\log p}\right)
 \longrightarrow\Phi(z).
 \tag{1}
\]
The statement also holds under uniform sampling from the actual family in \((X,2X]\), with centering and scaling computed from each product's own \(p\).

**The first word.** Set \(Y=X/p\), \(b=\log p\), and \(t=\lfloor\mu b+z\sigma\sqrt b\rfloor\). Here \(t=O_z(\log\log X)\). For \(Q=2^t\), Siegel–Walfisz gives uniform prime counts on the odd residues of \(q\) in \((Y,2Y]\). The modulus is a fixed power of \(\log Y\) at most. The sum over the reduced residues of the absolute errors, divided by the number of primes in the octave, is \(O_{z,A}((\log X)^{-A})\) for any fixed \(A\), by using the prime theorem with a larger error exponent. Multiplication by odd \(p\) permutes these residues. The usual parity-word bijection identifies the \(2^{t-1}\) odd source residues with the \(t\)-letter shortcut words beginning with an odd bit. Indeed the two lifts of a prefix modulo \(2^j\) have endpoints separated by the odd number \(3^s\), where \(s\) is its number of odd departures. The first bit is fixed and the remaining \(t-1\) bits are asymptotically independent fair bits in total variation. [Terras, single-source stopping times and parity words](https://doi.org/10.4064/aa-30-3-241-252) · [Walfisz, original paper](https://doi.org/10.1007/BF01218882) · [Green, Proposition 4.2, a modern Siegel–Walfisz statement](https://annals.math.princeton.edu/wp-content/uploads/annals-v161-n3-p11.pdf)

**The crossing.** Write \(K_j\) for the number of odd departures before date \(j\) and \(S_j=j\log2-K_j\log3\). Multiplying the true updates gives
\[
 \log\frac{n}{T^j n}=S_j-E_j,\qquad
 E_j=\sum_{\substack{0\le i<j\\T^i n\ \mathrm{odd}}}
                 \log\!\left(1+\frac1{3T^i n}\right)\ge0.
\]
If every input before \(j\) is at least \(q\), then \(E_j\le j/(3q)\), including the date of the first crossing. With \(M_t=\max_{0\le j\le t} S_j\), the following implications also handle a path that never crosses:
\[
 \{M_t>b+t/(3Y)\}\subseteq\{\tau_q(pq)\le t\}
                      \subseteq \{M_t>b\}.
 \tag{2}
\]
For the first inclusion, assume no crossing through \(t\), use the bound on \(E_j\) for every \(j\le t\), and obtain a contradiction. For the second, evaluate at the actual first crossing. This argument keeps the variation of the prime \(q\) within its octave.

Under the fair-word law the increments after the initial odd departure have mean \(d\), variance \(v^2\), and satisfy \(\mathbb E e^{-(S_{i+1}-S_i)}=1\). For the reversed fair suffix the exponential of its negated partial sum is a nonnegative mean-one martingale. The maximal inequality gives \(\Pr(M_t-S_t>u)\le(3/2)e^{-u}\) for \(u\ge\log(3/2)\), allowing for the final reversed deterministic odd increment. The largest atom of \(S_t\) is \(O(t^{-1/2})\) by the binomial formula, and its lattice spacing is \(\log3\). Using \(u=\log(t+2)\) in (2) changes the crossing probability from \(\Pr(S_t>b)\) by at most \(O(\log(t+2)/\sqrt t)\) plus the residue error. The binomial central limit theorem and
\((dt-b)/(v\sqrt t)\to z\) give (1). The initial odd step contributes a bounded shift in the mean.

For \(\log(2X)<p\le(\log X)^2\), every sampled product lies in the stated family. The two boundary ranges for \(p\) have combined reciprocal sum \(O(1/\log X)\), by their lengths and least elements. Their prime-pair count is \(O(X/\log^2 X)\) using the prime-counting upper bound for \(q\). Summing the prime number theorem in the interior and using Mertens's prime reciprocal estimate gives \((\log2+o(1))X/\log X\) products. This proves the actual-family version.

## How long the exceptional starts can rise

For every sufficiently large \(k\) and **every** length-\(k\) parity word beginning with an odd departure, there is a member \(n=pq\) of the family realizing the word with
\[
  \log_2 n\le(12/5+o(1))k.
\]
In fact one may use each prime \(p\in(4k,8k)\). Such primes exist by Bertrand's postulate. Let \(a\) be the unique odd starting residue for the word modulo \(2^k\), and let \(r\in[1,2^k)\) represent \(ap^{-1}\bmod 2^k\). Prescribe \(q\equiv 2^k+r\bmod 2^{k+1}\). This is an odd class and its least positive representative exceeds \(2^k\). Chang's Corollary 11 for smooth moduli supplies a prime \(q<(2^{k+1})^{12/5+o(1)}\), uniformly over reduced classes. Its hypothesis holds since 2 is the only prime dividing the modulus. Thus \(q>2^k>p\), and
\[
 k\log2<\log(pq)\le(12/5+o(1))k\log2<4k<p
       \le8k<(k\log2)^2
\]
eventually. The high lift prevents a small accidental representative. Classical Linnik alone gives the same statement with a larger fixed exponent. [Chang, Corollary 11](https://math.ucr.edu/~mcc/paper/143%20Char060114.pdf) · [Xylouris, least primes in progressions](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/150/1/83078/on-the-least-prime-in-an-arithmetic-progression-and-estimates-for-the-zeros-of-dirichlet-l-functions)

For the all-odd word \(n\equiv-1\bmod 2^k\),
\[
 T^j n+1=(3/2)^j(n+1)\qquad(0\le j\le k).
\]
Hence infinitely many members rise for at least \((5/12-o(1))\log_2 n\) consecutive dates. Their peak exceeds \(n^{1+(5/12)\log_2(3/2)-o(1)}\). Since a shortcut step can decrease a value by at most a factor of two, their first drop below \(n\), and therefore below \(q\), comes no earlier than \(((5/12)\log_2 3-o(1))\log_2 n\). A uniform \(O(\log p)\) deadline for dropping below the larger factor is false.

There is also a relative count in each product octave. Fix \(0<\theta<5/12\), let \(k=\lfloor\theta\log_2 X\rfloor\), and choose any nonempty collection \(W\) of odd-start words of length \(k\), possibly depending on \(X\). Uniformly for all such collections and for each \(p\) in the prime fibres of (1),
\[
 \Pr\{\operatorname{word}_k(pq)\in W\}
 = (1+o_\theta(1))\, |W|/2^{k-1}.
\]
The same estimate holds in the actual product family. In particular the number of its members in \((X,2X]\) rising on every one of the first \(k\) steps is
\[
  (\log2+o_\theta(1))\, 2^{1-k} X/\log X .
\]
Thus these long ascents occur polynomially often at every sufficiently large scale.

For the relative estimate, use (8.4)–(8.5) of Chang's proof with \(Q=2^k\) and \(y=Y\) or \(2Y\), where \(Y=X/p\). For some fixed \(\epsilon_\theta>0\), \(y>Q^{12/5+\epsilon_\theta}\). Every real character modulo a power of two comes from a character of conductor dividing 8, since every odd square is \(1\bmod8\) and all residues \(1\bmod8\) are squares. The finitely many real primitive \(L\)-functions are nonzero at 1. Any exceptional term therefore tends to zero uniformly. The zero-free error \(y^{-c\eta}\) tends to zero by (8.5), since the largest prime divisor of \(Q\) is 2 and \(\log y\asymp_\theta\log Q\). Thus \(\psi(y;Q,a)=(1+o_\theta(1))y/\varphi(Q)\) uniformly in odd \(a\). Subtract the two endpoints. All proper prime powers together have weight \(O(\sqrt Y\log^2 Y)=o(Y/\varphi(Q))\) since \(\theta<1/2\). Throughout the octave the prime log weights equal \((1+o(1))\log Y\). Now apply the parity bijection. Each boundary \(p\) from (1) contributes at most \(O(|W|X/(pQ\log X))\) even if only part of its octave is admissible, by the same upper bound on the whole octave. This controls the fringe relative to the mass of \(W\), including when \(W\) is a singleton. [Chang, equations (8.4) and (8.5)](https://math.ucr.edu/~mcc/paper/143%20Char060114.pdf)

## The smaller-factor clock under the single-source timing input

**SOURCE-QUALIFIED.** Leen's *Exact rates in Collatz synchronization* supplies the exact binary cylinders, balanced shortcut dictionary and uniform pair-absorption estimate (TeX labels `pair:cylinders`, `pair:dictionary`, `pair:uniform-tail`, source SHA-256 `d2f961635d339a4b215c82b1f2f8b9ca53143043f4c58b9aa67290f46056996e`). His *Brownian motion in Collatz orbits* supplies the fate–clock invariance principle and time-to-minimum corollary (labels `thm:main`, `cor:min`, source SHA-256 `211bc4fe107b3821e510486be28cf53f69751f71394582822faf385d09561e37`). [Original pair manuscript](https://zenodo.org/api/records/23268751/files/collatz-synchronization-rates.tex/content) · [Original clock manuscript](https://zenodo.org/api/records/23269488/files/collatz-brownian-motion.tex/content)

The following upper transfer uses an ordinary fusion theorem of Leen as its dynamical input and Brun–Titchmarsh for its prime counts. Let \(D\) be odd with \(1\le D\le X^{1/16}\), and sample primes \(q\in(X/D,2X/D]\). Fix an exceptional set \(E\) of ordinary starts in \((X/2,3X]\). Assume membership of \(m\) and \(m+j\) agrees whenever their actual paths fuse by \(t=\lfloor\tfrac14\log_2 X\rfloor\), for original \(m\in(X,2X]\) and \(1\le j\le X^{1/2}\). Put \(e=\#E/X\). With an absolute implied constant,
\[
 \Pr(Dq\in E)\ll e^{1/3}+\sqrt{(1+\log D)/\log X}.
 \tag{3}
\]
To see this, put \(h=2\log D/\log X+\max(e^{2/3},1/\log X)\) and \(H=\lfloor X^h\rfloor\). If \(h>1/2\), use the trivial bound after adjusting the constant. Each unshifted sample in \(E\) supplies \(H\) incidences. After translating by \(j\), an integer in \(E\) can receive at most \(O(H/[D\log(H/D)])\) incidences by Brun–Titchmarsh in an interval of length \(H/D\), with a harmless absolute adjustment for bounded length. For fixed \(j\), the failing fraction of binary residues modulo \(2^t\) is \(O(\sqrt{(1+\log(1+j))/t})\) by Leen. Odd \(D\) permutes these residues. Brun–Titchmarsh in each residue bounds its number of sampled primes by \(O(X/(D2^t\log X))\). The total normalized failure for each shift is therefore \(O(\sqrt h)\). Division by \(H\) and by the prime sample size gives \(O(e/(h-\log D/\log X)+\sqrt h)\), proving (3). The argument supplies an upper bound for rare marks and does not establish equality of positive probability laws. [Leen, uniform balanced pair absorption and ordinary cylinders](https://doi.org/10.5281/zenodo.23268751) · [Montgomery and Vaughan, Brun–Titchmarsh](https://doi.org/10.1112/S0025579300004708)

Apply (3) with \(D=p\). Leen's ordinary minimum law is tight, and his centered capped first-passage process converges in the uniform topology to continuous Brownian motion. These laws hold also on a fixed octave by subtracting counts. Uniformly for the indicated \(p\), ordinary starts through these octaves have minimum below \(p\) with probability tending to one. Their first date below \(p\) differs from the first date \(\tau_*\) of the global orbit minimum by \(o_P(\sqrt{\log X})\). Indeed use the larger threshold \(2(\log(2X))^2\) and the smaller threshold \(\frac12\log X\). On the event of hitting the smaller one, the difference is bounded by the clock from first passage at the larger one to the global minimum. Its normalized value tends to zero by continuity at the endpoint of Leen's process, since the centering shift is \(O(\log\log X)\). For starts from \((X/2,3X]\), all values before \(t\) exceed these thresholds, since \(T^i m\ge m/2^i\). Consequently failure to visit below \(p\), or visiting below \(p\) but having a large clock difference, is unchanged by fusion. The upper transfer preserves these vanishing exceptions on every prime fibre. The times \(\tau_*\) themselves are tight about \(\mu\log X\) on the \(\sqrt{\log X}\) scale on these fibres, by applying (3) to the tails restricted to starts which visit below \(p\), then sending the tail threshold to infinity. In particular
\[
 \tau_p(pq)=\mu\log X+O_P(\sqrt{\log X}),\qquad
 \tau_*(pq)-\tau_p(pq)=o_P(\sqrt{\log X})
\]
uniformly, with the probability of an infinite first passage tending to zero. A Brownian limiting distribution on the prime fibres is not claimed for this second clock. Its conclusion is compatible with a positive-density component whose minimum is a fixed integer greater than 1. [Leen, fate–clock invariance principle and time-to-minimum corollary, v2](https://doi.org/10.5281/zenodo.23269488)

Paper 233 studies fixed-target visits along ordered prime factorizations under ordinary RH, and early meetings with the smaller factor when the other clock is unrestricted. Paper 209 studies consecutive primes and first meetings with smaller orbits. Here the earlier clock measures passage below the *numerical value* of the larger factor. The merger estimates concern the two actual paths from the product and its larger factor. [Prime factors of Collatz predecessors, §§3–6](https://rstation.ai/problems/collatz/papers/233) · [Prime starts in the Collatz graph, theorems A–C](https://rstation.ai/problems/collatz/papers/209)

## Finite checks

[FactorClock.lean](FactorClock.lean) uses the pinned PR #214 shortcut and proves both the before-crossing product estimates in integer form and the exact entire all-odd prefix. The probabilistic and prime-distribution arguments are written proofs. [check_semiprime.py](check_semiprime.py) gives a deterministic 307-digit witness. Its smaller prime is 2003. The larger prime is certified using the prime \(r=2^{521}-1\), verified by Lucas–Lehmer. The order test modulo each prime divisor of \(q\) implies that divisor is \(1\bmod r\), and \(q<r^2\). The product rises through all of the first 480 dates. Its first drops below the product, larger prime and smaller prime occur at dates 1793, 1814 and 6838. It reaches 1 at date 6922.

The first common vertex occurs at (product date, larger-prime date) = (6916, 4572), at value 20. Their first common value at the same date is 2 at date 6921. The replay checks the full paths to their first repetitions, every odd-start binary word through length nine, 1,280 finite floor bounds, and 543 actual small mergers at equal or unequal dates.

Run the arithmetic certificate from the repository root.

    python -X utf8 -B research/semiprime-factor-clocks-20261128/check_semiprime.py

For the Lean statements, use a Lean 4.34.1 executable and a built Mathlib checkout at commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. From the repository root run

    python -X utf8 -B research/semiprime-factor-clocks-20261128/check_lean.py --lean /path/to/lean --mathlib /path/to/mathlib

The runner builds the pinned local affine kernel and this packet in a fresh directory and reports the axioms for all three theorem roots. The first-pass, minimum-clock, prime-counting and logarithmic-form limits remain written mathematics. Convergence of every member of the explicit family remains open.
