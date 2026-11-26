# Resolving every common-parity run with one rational trajectory

**PROPOSED.** This gives a closed description of the common-parity portion of the two-arm transducer in [PAIRED_CAPACITY.md](PAIRED_CAPACITY.md). Here its weight is \(1\) for two even departures, \(1/9\) for two odd departures and \(1/3\) for a mismatch. The initial pair is allowed to range over a complete dyadic cylinder. The terminal ordinary \(X\) is not prescribed in the following count.

At a state of nonzero relative rank swap arms if needed and write the larger-slope arm \(y=3^s x+c\), where \(s\ge1\) and \(c\) is an integer. A fresh parameter runs through all residues of the coordinate \(x\) modulo each power of two, because its affine slope in the parameter is an odd power of three. Suppose \(c\ne0\). Put \(d=3^s-1\), \(e=v_2(d)\), \(v=v_2(c)\). Let \(B_t\) be the sum of weights of the common parity words of length \(t\), each distinct lower word counted once.

## O6. Explicit common-word resolvent

* If \(v<e\), then \(B_t=(10/9)^t\) for \(0\le t\le v\), and \(B_t=0\) for \(t>v\).
* If \(v\ge e\), put \(D=d/2^e\), \(n=-c/2^e\), \(z=n/D\). Then \(B_t=(10/9)^t\) for \(t\le e\). For \(t\ge e\),
  \[
     B_t=(10/9)^e\,9^{-k_{t-e}(z)},
  \]
  where \(k_j(z)\) is the odd count on the first \(j\) shortcut clocks of the single odd-denominator rational \(z\).

Indeed two starting values have the same first \(t\) parities exactly when they agree modulo \(2^t\). If their first parities agree, their shortcut difference equals their starting difference times an odd factor divided by two. Induction gives the claim as well as the bijection between residues and words. The common-word condition is therefore \(dx\equiv-c\pmod{2^t}\). For \(t\le\min(e,v)\) this puts no restriction on \(x\). When \(v<e\) the first unsolvable congruence occurs at \(t=v+1\). In the other case, for \(t\ge e\) it says exactly \(x\equiv z\pmod{2^{t-e}}\). The prescribed first \(t-e\) bits have weight \(9^{-k_{t-e}(z)}\), and all final \(e\) bits are free. Every finite word counted has positive ordinary realizations by taking a sufficiently large parameter in its residue class. The rational \(z\) itself serves only to describe the common prefix and can be negative.

The positive odd denominator \(D\) is prime to three. With a fixed denominator \(D\), the rational numerator \(n_j\) evolves by \(2n_{j+1}=n_j\) on an even departure and \(2n_{j+1}=3n_j+D\) on an odd one. Starting from \(n\ne0\), no subsequent numerator is zero. An odd predecessor of zero would require \(3\mid D\), and an even predecessor would already be zero. Thus \(2^j\le|n|(3+D)^{k_j(z)}\), by multiplying the one-step bounds and using \(|n_j|\ge1\). In particular, there are at most \(1+\log_2|n|+k\log_2(3+D)\) indices \(j\) with \(k_j(z)=k\). Summing the geometric series gives
\[
 \sum_{t\ge0} B_t \ll (10/9)^e\big(1+\log(1+|c|)+s\big).
\]
This controls all valuation jumps in a single run. Also \(e=1\) for odd \(s\) and \(e=2+v_2(s)\) for even \(s\), by factoring \(3^{2m}-1\) repeatedly. The displayed factor \((10/9)^e\) grows at most polynomially in \(s\). At rank zero the analogous answer is \(B_t=(10/9)^t\) through \(v_2(c)\), and zero after it, since the common-run congruence is then \(2^t\mid c\). No uniform bound at all intercepts follows from the rank-zero formula.

For \(v\ge e\) the weighted *first mismatches* after \(t=e+j\) common bits have total
\[
 \tfrac23(10/9)^{e-1}\,9^{-k_j(z)} 9^{-(1-b_j(z))}.
\]
The first \(j\) bits follow \(z\), the next bit differs from its \(j\)-th bit \(b_j(z)\), the next \(e-1\) bits are free, and the mismatch allows either lower exit bit. For \(v<e\) the mismatch is forced immediately after \(v\) common bits, with total weight \((2/3)(10/9)^v\). Controlling a product or sum of such exit kernels over a changing sequence of ranks and intercepts is OPEN.

## An infinite correlation at the initial ordinary affine relation

For \(x\in\mathbb Z_2\) let \(F(x)=\sup_{t\ge0}2^{t/2}3^{-k_t(x)}\). Its Haar integral is finite, since the sum of the expectations of its terms is \(\sum_t(2\sqrt2/3)^t\). Its square is not integrable, since \(F(x)^2\ge2^{v_2(x)}\) off zero. The proposal to use the positive correlation \(H(g)=\int F(x)F(gx)\,dx\) at \(g(x)=3x-1\) fails at the exact initial relation.

Specifically, write \(x=3+16u\). Four shortcut clocks send both \(x\) and \(3x-1=8+48u\) to \(2+9u\), using respectively two and one odd departures. Therefore on this entire cylinder,
\[
 F(x) F(3x-1)\ge(16/27) F(2+9u)^2 .
\]
The odd affine function of \(u\) preserves Haar measure. Hence \(H(3x-1)=+\infty\). The calculation differentiates exact affine merger on one cylinder from the distinct ordinary endpoint pairs counted in (1)–(3) of the capacity note.
