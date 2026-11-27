# Exponentially light posterior tails on a positive-entropy family of geodesic words

**Written theorem.** Every infinite script on the symbols 1 and 2 with no consecutive twos has uniformly bounded full posterior likelihood ratio under the original geometric Syracuse law. All original-law competitors with excess division clock at least \(D\) have total relative weight \(O(q^D)\), with an absolute \(q<1\), uniformly over depth and script. The weighted lateral sibling costs of [the fixed-source theorem](TROPICAL_SIBLINGS.md) are therefore summable on this entire family. The conclusion holds on symbolic scripts without an ordinary positive source. Deciding whether any actual positive integer can stay in this family remains a separate arithmetic problem.

The two-path affine comparison and division-minimum theorem for words with no consecutive twos are Weaver's. Baton Relay also obtained the normalized carry potential in a study of balanced-word minima. The argument here uses it to count the full original weighted posterior, including competitors across all positive excess-clock shells. [Baton Relay, Paper 139, §4](https://rstation.ai/problems/collatz/papers/139) The earlier PR193 result treats the full posterior of one ordinary escaping source using an antichain estimate, and supplies a signed fixed-point control. Here the count bounds the set of affordable alternative affine sources in every excess-clock shell for each eligible script. [Weaver, Paper 1, Lemma 1 and Theorem 2](https://rstation.ai/problems/collatz/papers/1/v3) · [PR193 fixed-source posterior](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/POSTERIOR.md)

## A comparison theorem on individual scripts

Fix an infinite chronological script \(e_i\ge1\), indexed from zero. Put
\[
 A_i=\sum_{j<i}e_j,\qquad h_i=2^{A_i}/3^{i+1},\qquad
 G=\sum_{i\ge0}h_i,\qquad T_t=\sum_{i\ge t}h_i.
\]
For each \(n\), let \(r_n\bmod3^n\) be its exact ternary endpoint residue. At a positive odd lift of this residue the inverse words are precisely the competing \(n\)-letter scripts. Their original masses are \(2^{-\sum f_i}\). Write \(p_n(r_n)\) for their sum.

Assume there is a fixed integer \(K\ge0\) such that the total clock on **every** finite consecutive subword of the script exceeds the minimum for that subword's own terminal residue by at most \(K\). Assume also
\[
                         \sum_{i\ge0}(i+1)h_i<\infty.                  \tag{1}
\]
Then \(R_n=2^{A_n}p_n(r_n)\) increases to a finite limit. In particular the specific original word has conditional probability bounded away from zero, independently of \(n\).

For an explicit shell bound let \(\mathcal C_d\) be the set of affine constants of all competitors at **all** depths with total excess \(d\), defined below. For \(d\ge4\),
\[
 2^{-d}\#\mathcal C_d
 \ \ll_{G,K}\ (27/32)^{d/4}+2^{-d/4}+T_{\lfloor d/4\rfloor}+2^{-d}.    \tag{2}
\]
The hypothesis on every consecutive subword includes every suffix of every prefix. Exact minimization only for the prefixes from one fixed initial grade does not provide that hypothesis. No ordinary-source assumption, atom floor, or averaging over the original script enters this result.

### The affine constants and their center

Take a competitor \(f_0,\ldots,f_{n-1}\) at the same terminal residue. Choose any positive ordinary representative \(x_0\) of the full dyadic cylinder of the reference word, put \(x_i=S^i x_0\), and reconstruct the competing ancestors \(b_i\) of \(x_n\). These are positive ordinary integers. Write
\[
 d_i=\sum_{k=i}^{n-1}(f_k-e_k),\qquad
 c_i=b_i-2^{d_i}x_i,\qquad \theta_i=2^{-d_i}c_i .
\]
The constants depend only on the two words. Indeed \((d_n,c_n)=(0,0)\) and backward substitution determines earlier constants. At all times \(d_i\ge-K\) by the hypothesis at the terminal residue of the suffix. Direct substitution gives
\[
 2^{e_i}\theta_{i+1}=3\theta_i+2^{-d_i}-1,\qquad
 \theta_0=\sum_{i<n}h_i(1-2^{-d_i}).                                   \tag{3}
\]
In particular, with \(d=d_0\) and \(c=c_0\),
\[
 -(2^K-1)G \le c/2^d\le G,\qquad
 G-c/2^d=\sum_{i<n}h_i2^{-d_i}+T_n .                                  \tag{4}
\]
For \(d\ge0\), \(c\) is an integer. For \(-K\le d<0\), it belongs to \(2^{-K}\mathbb Z\). At one depth and a given \(d\), \(c\) determines the competitor uniquely since it determines \(b_0\), whose path is deterministic. Each pair \((d,c)\) persists at every later depth by appending the reference edges. Indeed, changing \(x_0\) by a multiple of \(2^{A_n+1}\) changes \(b_0\) by the corresponding multiple of \(2^{A_n+d+1}\), preserving both exact word cylinders and the affine identity. The unique odd 2-adic seed of the infinite reference word thus realizes each fixed affine merger. Therefore \(R_n\) increases and is bounded by \(\sum_{d\ge-K}2^{-d}\#\mathcal C_d\).

### The ordinary dyadic cylinder count

Fix \(d\ge4\), \(t=\lfloor d/4\rfloor\), \(h=\lfloor3d/4\rfloor\). If a common endpoint occurs before \(t\), extend the alternative by the reference letters up to time \(t\). We may use an ordinary representative of the reference word extended through \(\max(t,n)\). Write \(F_i\) for the sum of the first \(i\) alternative exponents, including this extension when needed. Then \(b_0=2^dx_0+c\equiv c\pmod{2^d}\), and \(c\) is odd.

Among odd residues modulo \(2^d\), the condition \(F_t>h\) has proportion
\[
  \eta_d=\Pr(E_1+\cdots+E_t>h)
       \le 2^t(3/4)^h\ll(27/32)^{d/4},
\]
where \(\Pr(E=e)=2^{-e}\) for \(e\ge1\) independently. To see the exact equality, every length-\(t\) word of total \(v\le h\) occupies one odd cylinder modulo \(2^{v+1}\), of relative odd mass \(2^{-v}\). These cylinders are disjoint, and \(h+1\le d\). The inequality follows from \(\mathbb E(4/3)^E=2\). This calculation uses only the varying offsets \(c\), which range in a fixed real interval of length \(O_{G,K}(2^d)\) by (4). Covering that interval by \(O_{G,K}(1)\) complete residue blocks bounds the exceptional count by \(O_{G,K}(2^d\eta_d)\).

For a remaining offset, \(F_t\le h\). Its first possible common endpoint occurs at some \(n\ge t\), since at an earlier merger \(F_n=d+A_n\ge d>h\). For \(i<t\) we have \(d_i=d+A_i-F_i\ge d-h\). Applying (4) and using \(d_i\ge-K\) on the rest yields
\[
  0\le G-c/2^d \le 2^{-d+h}G+2^K T_t.
\]
There are at most \(1+2^d(2^{-d+h}G+2^KT_t)\) integers in this interval of possible \(c\). This proves (2). Its sum in \(d\) is finite, since
\(\sum_{d\ge0}T_{\lfloor d/4\rfloor}=4\sum_i(i+1)h_i\).
The finitely many remaining shells have finite counts by (4). This proves the theorem.

## The full original law for words without consecutive twos

Apply Weaver's division-minimum theorem to every consecutive subword over \(\{1,2\}\) with no consecutive twos. It gives \(K=0\). Indeed each subword has a positive odd realization, and every legal alternative at its endpoint residue gives another genuine positive odd ancestor of that realization's endpoint. The prior comparison covers all such ancestors. Also \(A_i\le(3i+1)/2\), so \(h_i\le(\sqrt2/3)(\sqrt8/3)^i\). The constants in (2) are now absolute. With \(q=(8/9)^{1/8}<1\), equation (2) implies \(2^{-d}\#\mathcal C_d\ll q^d\). Summing \(d\ge D\) proves the asserted positive exponential tail. The no-consecutive-twos language has Fibonacci growth and positive entropy. It contains uncountably many nonperiodic scripts with nonordinary dyadic seeds, since ordinary integers are countable.

To see the sibling consequence directly, the original normalized posterior gains all off-path parents first joining at the next clock. For the parent \(B^j r_n\), \(j\ge1\), take one minimum-cost length-\(n\) word and append the exponent \(e_n+2j\). Its total excess is \(m_n(B^j r_n)-A_n+2j\). Its affine source first joins at time \(n+1\). These choices occupy disjoint increments of \(R_n\). Because \(m_n(r_n)=A_n\) on this language, uniform boundedness of \(R_n\) gives
\[
 \sum_{n\ge1}\sum_{j\ge1}4^{-j}
        2^{m_n(r_n)-m_n(B^jr_n)}\ll1
\]
with an absolute bound. Nonunit siblings have infinite minimum and zero weight. The same argument sums all competitor words and available shorter-parent exponents in the full normalized increment. The estimates use the original law.

Every finite reference prefix can be realized on actual ordinary paths converging to 1 by ordinary inverse routing. The full infinite symbolic assertions alone imply no single positive integer follows a reference script forever. The missing exchange statement specialized to this class therefore entails an actual ordinary exclusion for the class. Existing work also studies the broader question of avoiding the residue \(5\bmod8\), which includes all odd scripts with gaps at most two. [Ordinary finite routing](ORDINARY_DECODER_CONTROLS.md) · [Yolcu, Aaronson and Heule, Section 4.5](https://emreyolcu.com/research/rewriting-collatz.pdf)
