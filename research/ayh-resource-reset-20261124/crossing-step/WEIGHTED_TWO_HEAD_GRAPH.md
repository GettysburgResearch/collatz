# A weighted graph of simultaneous true head disagreements

**Status.** PROPOSED written consequence of the ordinary-source incidence and transverse bounds. The finite-grid merger theorem used here retains its source qualification. This is a two-target upper bound for the original disagreement fraction, with an explicit arithmetic restriction on the relative clock and effective trit exponent. The full series is open.

Keep the notation, time slab and source exceptions of [the late witness theorem](LATE_WITNESS_TRACKS.md). Set
\[
 I_1=[3d,3.02d]\cap\mathbb Z,\qquad
 I_2=[3.08d,3.10d]\cap\mathbb Z,\qquad a=1-\tfrac12\log_2 3 .
\]
Use natural logarithms below except for \(\log_2\). For \(i=1,2\) let \(Z_i\) consist of the genuine discordant smaller heads \(z\) with
\[
 |\log_2 z-(d-at)|\le C_A\sqrt{d\log d}\quad\text{for some }t\in I_i.
\]
All heads can be restricted to the prescribed fixed interior mantissa arc. For large \(d\), every \(z_1\in Z_1\) is exponentially larger than every \(z_2\in Z_2\), while \(z_2\ge 2^{.3d}\).

Define a directed edge \(z_1\to z_2\) if there are integers \(v\in I_2-I_1,w\) with \(|w|\le C_A d\) and
\[
 \left|\log(z_2/z_1)+v\log2-w\log3\right|\le C_A/z_2,\qquad
 c_A\sqrt{d/\log d}\ \le\ |w-v/2|\ \le C_A\sqrt{d\log d}.
 \tag{1}
\]
Write \(a_j=R^{-1}\#\{x\in[7R,8R): f(x)\ne f(\lfloor x/81\rfloor)\}\). With suitably chosen positive constants in (1) we have
\[
 a_j\ll_A d^{-A}+\frac{\sqrt{\log d}}{d^2}
           \sum_{z_1\in Z_1}\frac{\#\{z_2\in Z_2:z_1\to z_2\}}{z_1}.
 \tag{2}
\]

**Forward count.** Fix a good discordant original child. There are at least \(c d\) genuine marked clocks in each interval. Select one witnessing head per clock. For a fixed mark in \(I_1\) with transverse coordinate \(u_1=k_1-\lfloor t_1/2\rfloor\), exclude marks in \(I_2\) with \(|k_2-\lfloor t_2/2\rfloor-u_1|\le L\), where \(L=\lfloor c'_A\sqrt{d/\log d}\rfloor\). For a single centered coordinate the simultaneous cap in the witness theorem is \(C_A\sqrt{d\log d}\); hence at most \((2L+1)C_A\sqrt{d\log d}\) clocks are excluded. Choose \(c'_A\) sufficiently small to leave at least \(cd/2\) clocks, including the \(O(1)\) discrepancy between half-times and their floors. Each source supplies \(\gg_A d^2\) ordered time pairs. At both times (2) of the witness theorem gives \(z_i=3^{k_i}2^{-t_i}n+O_A(1)\) in the very same original parent \(n\). Dividing and taking logarithms gives (1) with \(w=k_2-k_1,\ v=t_2-t_1\). The upper cutoff follows from the two original count envelopes. No choices of edges on independent sources have been multiplied.

**Reverse count.** For fixed \(z_1,z_2\), (1) permits at most one \((v,w)\) at large \(d\). Two different pairs would give a nonzero integral linear form in \(\log2,\log3\) of size \(O_A(1/z_2)\) with coefficients \(O_A(d)\). Multiplicative independence excludes an identically zero form, and the classical two-logarithm bound already used in \(\mathrm{HEAD\_INCIDENCE}\) bounds its absolute value below by \(c_A d^{-\nu}\). The exponential lower bound on \(z_2\) gives the contradiction. This step uses the specified polynomial separation input.

For the earlier head, the relation \(\log_2 z_1=d-at_1+O_A(\sqrt{d\log d})\) permits \(O_A(\sqrt{d\log d})\) integer \(t_1\); then \(t_2=t_1+v\) is fixed. Once \(t_1,z_1\) are fixed, at most one \(k_1\) can put the original parent \(n\) inside its sample with \(z_1=3^{k_1}2^{-t_1}n+O_A(1)\), since the sample's endpoint ratio is \(8/7+o(1)\) and consecutive exponents multiply the center by three. The allowable parent interval has length \(O_A(R/z_1)\). Its logarithmic length after enlargement to that scale is comparable with \(d\). For each original suffix \(r\), every truly discordant source fails its native pair certificate on that interval. The complete-grid bound therefore gives \(O_A(R/(z_1\sqrt d))\) possibilities. The 81 suffixes are fixed in number. Summing over the common clock translations, then dividing by the forward count and by \(R\), proves (2).

The one-target recurrence sees the harmonic mass of each \(Z_i\) alone. In (2) this mass is weighted by the degree in a joint arithmetic graph, with the narrow band about the ballistic diagonal removed. Separate marginal masses do not control this degree. The estimate still allows a diffusively spread two-color graph and does not demonstrate a strict contraction.

**Inputs.** PR 197 at \(\mathtt{6eb986b0ce0b1836a356474d25d709ed4e948b67}\), HEAD_INCIDENCE.md, and its pinned two-logarithm estimate in joint-renewal/LANDING_WEIGHT_TRANSFER.md. PR 146 at \(\mathtt{f431078244e868dc699fad011044f0d5e7f76437}\) supplies the uniform pair tail on the original strip. All additional source qualifications for late regeneration are listed in [the witness theorem](LATE_WITNESS_TRACKS.md).
