# A finite original-word cubic energy in the critical short-clock region

Let \(q=3^n\). Draw the original \(n\) independent positive geometric gaps of parameter \(1/2\), write \(S_n\) for their sum, and \(F_n\bmod q\) for the genuine Syracuse affine endpoint intercept. Use the orientation of [PR 195, MARKED_FIBRES (1)–(2)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/MARKED_FIBRES.md), so an exponent word is compatible with the odd endpoint \(y\) exactly when \(F_n\equiv y\pmod q\). Put \(P_{n,s}(r)=\Pr(S_n=s,F_n\equiv r\bmod 3^n)\), with the empty law \(P_{0,0}(0)=1\) on the trivial quotient, and zero at impossible clocks. For each ternary residue \(r\) use its unique positive odd representative \(y_r<2q\).

At a specified positive odd \(y\) of primitive ordinary period \(\ell\le n\), let \(b\) be the true native total in that lap. Define
\[
 B_{n,s}(y)=P_{n,s}(y\bmod q)
    -{\bf1}_{\{\ell\le n\}}2^{-b}P_{n-\ell,s-b}(y\bmod 3^{n-\ell}), \tag{1}
\]
with the second summand zero if no positive return through \(n\) occurs from this particular \(y\). This is nonnegative. Indeed the unrestricted normalized inverse row is \(qP_{n,s}(y\bmod q)/y\): each word carries \(2^{-s}\) and determines exactly one positive odd input by successive genuine inverse steps. Every word giving a prior visit contains, at its *terminal* end, the unique primitive lap from \(y\) back to \(y\). Removing that particular lap is a bijection to all words at the shorter clocks ending at \(y\), with no first-arrival restriction there. This gives precisely (1) in probability units and shows that \(q B_{n,s}(y)/y\) is the actual normalized odd first-arrival mass.

In particular the fixed-root impulse net from [the first-arrival spectrum](FIRST_ARRIVAL_ROW_SPECTRUM.md) is
\(H_y=h(y)/y\) for nonperiodic \(y\), and \(H_y=(1-3^\ell2^{-b})h(y)/y\) for periodic \(y\), where \(h(y)\) is the Cesàro limit of \(3^j\Pr(F_j\equiv y\bmod3^j)\). Sum (1) over native totals and take Cesàro limits: shifting the raw trace by a fixed primitive length preserves its Cesàro limit, while the genuine first-hit grade masses already have an individual limit by the signed-source convolution. The stronger individual-depth trace and its dependency status are recorded in [the positive trace budget](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md).

Take the integer \(L_n=\lfloor n/\lceil\log_2(n+2)\rceil\rfloor\) and \(\lambda=\log_2 3\). With the charges and written inputs of [the common-depth proof](COMMON_DEPTH_CUBIC_RESIDUE.md),
\[
 \lim_{n\to\infty}\frac{q^3}{\log n}
 \sum_{r\bmod q}\ 
 \sum_{\substack{s\ge n\\y_r2^s/q\le 2^{L_n}}}
             \frac{B_{n,s}(y_r)^3}{y_r^3}
       =\frac1{4\pi\sqrt3}\sum_C H_C^3 .                              \tag{2}
\]
One may equivalently discard all canonical targets with a positive ordinary return through \(n\), and use \(P_{n,s}\) itself at all other canonical targets. The discarded genuine first-visit cube sums belong to the union of eventually periodic basins, already proved to be \(o(\log n)\). All finite tests here concern the target up to depth \(n\). The crop is the exact integer comparison \(y_r2^s\le3^n2^{L_n}\). Only \(s\le\lambda n+L_n\) can occur in the displayed polynomial, a lower large-deviation region of the unconditioned geometric sum of mean \(2n\).

To verify the canonical range, each greater odd representative of \(r\) is \(y_r+2q h,\ h\ge1\); ignoring its first-visit subtraction only increases its cube. The sum of all the lifted cubes is bounded by
\[
  \sum_{r,s} P_{n,s}(r)^3 \sum_{h\ge1}(2h)^{-3}=O(n^{-1}),
\]
because each \(P_{n,s}(r)\le\max_s\Pr(S_n=s)=O(n^{-1/2})\) and the joint masses sum to one. Thus one representative per actual ternary residue suffices with vanishing absolute error. Among the remaining true first-visit rows, the physical height octaves \(2^k\le p<2^{k+1}\) with \(L_n-O(1)\le k\le32n\) have total cube sum \(O(\log\log(n+2))\); higher octaves have exponential tail. These are the original first-row bounds proved in the common-depth note. Removing that range changes the normalized limit by zero. This proves (2).

The underlying iid cutoff event has probability exponentially small in \(n\). That scalar fact gives no sublogarithmic upper in (2), because the cubed row normalization is \(q^3/y_r^3\) before summing. For an inherited physical word from \(x\) its mass after normalization is exactly \(q2^{-s}/y=1/p\), which can remain of constant order as its individual iid probability tends to zero. Equation (2) requires control of **multiple** compatible words at the same original \((s,r)\) weighted at its prescribed least positive odd representative. Finite-quotient average moment control with no \(y_r^{-3}\) resolution does not evaluate this energy. A matched relative upper for the whole displayed energy, or an independent proof that it is \(o(\log n)\), remains open.

The [finite checker](check_first_arrival_energy.py) reconstructs every raw and true first-arrival row at odd depths zero through five and native totals at most thirteen by independent ordinary forward iteration, verifies the primitive-lap subtraction, and compares the [exact rational cubic sums](first_arrival_energy_checks.json).
