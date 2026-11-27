# Exact finite-budget smaller-source selector

For the ordinary shortcut map \(T\), fix \(K\ge1\) and a positive ordinary source \(n\) with
\[
                         2n\ge K(1+3^K).                       \tag{1}
\]
At every virtual scale \(\delta\ge0\) and ramp length \(j\ge0\) with \(2^j\mid 2^\delta(n+1)\), put \(Y+1=3^j2^\delta(n+1)/2^j\). The finite registry below decides whether any positive \(m<n\) visits \(Y\) using at most \(j+K\) odd departures. If one exists it constructs an actual such source and returns the minimum odd grade. The quantifier on the lower physical clock is unrestricted.

`DecideSelector.lean` supplies an executable reference Boolean with a kernel-checked equivalence to the arbitrary-clock ordinary reachability statement. `PostSelector.lean` proves the maximal-postpeak equivalence below. The fast Python implementation stops at the first contraction; the equivalent exhaustive Lean Boolean enumerates all strictly contracting rows within the same grade budget. [Executable theorem](DecideSelector.lean) · [Maximal-word theorem](PostSelector.lean)

The companion note proves that one common set with at least \(259/960\) of all classes modulo \(3^K\) has no positive row at any scale. The density bound is a written argument. The direct finite controls below independently check examples of both outcomes. [Density argument](SCALED_DENSITY.md)

## Registry construction

Enumerate odd positive mirror magnitudes \(M\) that first reach 1 under the signed mirror shortcut \(x\mapsto x/2\) on even \(x\) and \(x\mapsto(3x-1)/2\) on odd \(x\). Record their exact first-hit word \(\sigma_M\), its odd grade \(h(M)\), and its even count \(\ell\). For \(M=1\) these are all zero. For each binary scale \(\delta\), put \(a=\ell+\delta\). At each reverse word starting at \(z=2^a(n+1)-M\), stop at the first node \(\gamma\) whose prefix length \(d\) and odd grade \(b\le K\) satisfy \(2^{a+d}<3^b\). The branch letters are in reverse time. A row consists of \(M,\sigma_M,\delta,\gamma\), and the single source residue \(r(\gamma,M,a)\bmod 3^b\) at which its endpoint is integral.

If \(C=0\) at the empty reverse word, appending an inverse even takes \(C\) to \(2C\); appending an inverse odd from current grade \(b\) takes \(C\) to \(2C+3^b\). The integer residue in the row solves
\[
                     2^{a+d}(r+1)\equiv 2^dM+C\pmod{3^b}.
\]
Finite enumeration needs only \(2^a<(3/2)^K\) and \(2^{a+d}<3^K\). Since \(M\le2^\ell\), the possible magnitudes are finite. Away from 1, each odd mirror step multiplies the magnitude by at least \(4/3\). At a first hit the even steps have divided by \(2^\ell\), so \(h(M)<3\ell\) for \(\ell>0\). This gives a finite ordinary-integer enumeration of every eligible mirror start, without a global mirror termination assumption.

The test accepts the rows at the requested \(\delta\) with \(h(M)\le j\) and \(n\equiv r\bmod3^b\). The minimum grade is \(j+\min b\) over accepted rows. If \(j=0\), the condition \(h(M)=0\) forces the odd magnitude \(M=1\), hence \(\ell=0\).

## Necessity with the improved cutoff

The signed-suffix extraction gives an odd \(M\), \(h(M)\le j\), and a true inverse prefix from \(z=2^a(n+1)-M\) to a smaller \(m\). Its grade \(b\) is positive and at most \(K\). Write its intermediate affine states as \(D_i(n+1)-B_i\), beginning with \(D_0=2^a,\ B_0=M\). If any \(D_i<1\), stop at the first such state. The same mirror parameters remain in force and the selected state is positive and smaller than \(n\), since \(B_i\ge1\). At its grade \(b'\le b\), it supplies an accepted row.

If no strict crossing occurs, all previous \(D_i\ge1\). An even inverse leaves \(B_i/D_i\) unchanged, and an odd inverse changes it by precisely \(1/(2D_i)\). Thus \(B/D\le1+b/2\) at the endpoint. Here \(D=2^{a+d}/3^b\ne1\) since \(b>0\), so \(D>1\), \(3^b(D-1)\ge1\), and \(D/(D-1)\le1+3^b\). Writing \(m=Dn+(D-B)<n\) gives
\[
                 2n < bD/(D-1)\le b(1+3^b)\le K(1+3^K),
\]
contradicting (1). This proves the necessity without the earlier threshold \(n+1\ge2(9/2)^K\).

## Sufficiency and the original ordinary source

For a matching row, reverse \(\gamma\) from \(z\) and call the resulting endpoint \(m\). Integrality at the last reversed vertex implies integrality at every earlier vertex, either by the affine-word parity lemma or by persistence of a reduced denominator divisible by three under each later inverse operation. Every integral ordinary inverse of a positive source is positive. In particular \(z>0\), since \(z=2^{\ell+\delta}(n+1)-M\ge2^\ell n\). The strict crossing and \(B\ge1\) give \(m=D(n+1)-B<n\). The forward word from \(m\) to \(z\) is \(\gamma\) in reverse order.

Set \(v=2^\delta(n+1)/2^j\). Append \(j-h(M)\) stationary odd loops at \(-1\) to the signed path from \(-M\) to \(-1\). The resulting signed suffix has length \(j+\ell\) and grade \(j\). Translating its start by \(2^{j+\ell}v\) preserves every parity and translates its endpoint by \(3^jv\). It therefore takes the positive state \(z\) to \(Y=3^jv-1\). Concatenation gives the asserted ordinary visit with exactly \(j+b\) odds. Every true visit supplies an accepted row of weakly smaller grade, and each accepted row gives a true visit at its own grade. This proves the minimum claim.

## Exact maximal-postpeak decision

Let \(n=2^Hv-1,\ v>0\), and let \(w\) be a physical postpeak word of length \(t\), grade \(f\), and \(q=t-f\) even departures from \(P_H=3^Hv-1\) to \(Y\). Suppose \(H\ge21q+9K+3\) and \(w\) has largest grade in its signed-offset fibre. For each equally long \(\beta\) with \(C_\beta=C_w\), let \(u\) be its grade and put \(\delta=f-u\ge0\). Run the finite selector just described at \(j=H+\delta\) and this exact scale. A positive result for at least one \(\beta\) is equivalent to an ordinary smaller visitor at \(Y\) of grade at most \(H+f+K\).

Indeed, the checked cone theorem excludes grade at most \(H+f\). For each next possible grade \(H+f+b\), the checked paid-peak theorem rewrites any visit as an actual earlier visit to \(P_{H+\delta}\) at grade \(H+\delta+b\), using one such \(\beta\). Conversely, when a registry row gives a visit to \(P_{H+\delta}\), appending \(\beta\) reaches exactly \(Y\): the equal signed offsets give
\[
  2^tY=3^{H+f}v+C_w=3^u(3^{H+\delta}v-1)+A_\beta .
\]
Integral endpoint parity makes this a physical ordinary tail. Therefore \(H+f+\min b\), with the minimum over these matching words and their accepted rows, is the exact price whenever it lies within the budget.

## A positive family requiring the scaled predecessor

Let \(n\equiv60\bmod81\), \(n=2^Hv-1\), and \(3^Hv\equiv3\bmod4\). The true two-step postpeak word is \(EO\). The word \(EE\) has its same signed offset \(-1\), one fewer odd, and scale \(\delta=1\). The reverse prefix \(EOOOO\) from \(2(n+1)-1\) supplies
\[
              m=\frac{64n-33}{81}<n.
\]
Its actual forward word to the \(EO\) endpoint is \(O^4 E O^{H+1}EE\), of grade \(H+5\). This direct construction holds wherever \(H\ge1\) and the two displayed congruences hold. For \(H\ge60\), the complete selector additionally shows this is the minimum, while \(P_H\) itself has no smaller visitor of grade at most \(H+4\). The latter statements use all first-crossing rows up to budget four. There are nine rows at that precision, three of them are the only rows of grade at most three. Thus the positive postpeak decision genuinely uses the other member of the offset fibre.

The congruences describe an infinite class for every fixed \(H\ge1\): first choose \(v\) modulo 81 by invertibility of \(2^H\), and choose \(v\) independently modulo 4 for the physical \(EO\) condition. For example \(H=81,v=101\) works.

The independent ordinary inverse DFS in the control program searches by integer predecessors, with no signed offsets, modular registry, or restriction on the physical clock. It prunes a node \(x\) if even all remaining \(r\) permitted odd inverses cannot bring it below \(n\), using \(2^r(x+1)\ge3^r(n+1)\). Even inverses increase \(x+1\) and every odd inverse multiplies it by exactly \(2/3\), so this also proves finiteness of the individual searches. The two algorithms agree on all 7,644 pure cases tested through \(K=6\), and on 120 \(EO\) cases through \(K=4\). Exactly one of the 81 fourth-precision residues has a low-cost \(EO\) merger while its pure target is protected: residue 60. [Selector and direct replay](scale_selector.py) · [Finite counts](SELECTOR_CONTROLS.txt)

## Shell lower bound

For sufficiently large \(N\), take \(K=\lfloor\log_3N-\log_3\log_3N\rfloor-1\). Then \(K3^K\le N/3\) and \(3^K=o(N)\), so (1) holds simultaneously on \([N,2N)\). Counting odd integers in the common protected classes gives at least \((259/1920-o(1))N\) ordinary odd sources in every such shell. Every smaller visitor to any point on the initial all-odd ramp of each chosen ordinary source requires at least the ramp's odd grade plus \(K+1\). For their eligible maximal postpeak words the same bound applies above \(H+f\). For the ramp statement no largeness hypothesis on its length is needed.

Unbounded price, complete ordinary convergence, and unconditional existence of a later merger for every source remain open. The source-specific finite equivalence does not assume a universal finite reachability oracle.
