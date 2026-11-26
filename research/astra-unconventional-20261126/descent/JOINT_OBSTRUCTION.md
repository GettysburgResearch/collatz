# Two ordinary comparisons can fail at the same hard parent

**Proposed written synthesis.** Fix \(P,H\ge4\), put \(L=3^P2^{H-3}\), and write \(m=11+162j,\ z_m=(2^{m+7}-271)/81\). There is an actual \(j\in[L,2L)\) for which the following statements hold together.

1. Start at \(2^m-1\) and take any number of physical clocks with \(k\) odd departures and at most 24 even departures, reaching \(V\). No ordinary positive \(Y<2^{-40}z_m\) reaches \(V\) on a path with \(q\) odd departures and \(q-k\le P\). This includes the whole initial ascent, and it allows arbitrarily many original odd departures beyond the peak.
2. For every \(0\le t<m\) and all independently selected \(0\le i,l\le H\), one has \(T^i(3^m-1)\ne T^l(3^t-1)\).

In particular, \(P=H=n\ge4\) gives ordinary parents with \(m\asymp 6^n\). Both the excess-odd limit on the smaller-source test and the clock limit for comparison against every earlier peak then equal \(\log_6 m+O(1)\). The first statement uses the local distortion constant \(512\) and the written stopping-tree argument. The second uses the general kernel-checked positive peak separation. [Suffix mass and even departures](../operator/SUFFIX_MASS.md) · [Ordinary peak separation](SignedDelay.lean) · [Physical and signed proof](POSTPEAK_DELAY.md)

## Proof

Use \(S=24,\ D=40,\ m_0=34,\ C=512\) in equation (3) of the suffix-mass proof. The hypotheses apply to every \(j\ge1\). The ternary envelope has normalized mass below \(0.07422\). For a witness with \(q-k\le P\), its reverse stopping suffix uses some grade \(p\le P\). Its terminal class is modulo \(3^p\). For each fixed cut center and integer displacement, the index map is \(j\mapsto2^{11+162j+d}+A\), which changes valuations by exactly five. A nonempty pullback of a terminal class is therefore one whole index class modulo \(3^{\max(p-5,0)}\). This includes negative \(d\), since 2 is a ternary unit. Consequently the union of **all** pullbacks of such stopping suffixes with \(p\le P\) is a union of classes modulo \(3^P\), even though the set of candidate paths and centers has no imposed cardinality bound. This union lies in the same envelope of mass less than one. Some entire index class \(j\equiv b\bmod3^P\) avoids it, and every positive index in that class satisfies the first claim.

Independently, impose
\[
       81j+6\equiv0\pmod{2^{H-3}}.
\]
This selects one binary class since \(81\) is odd. It gives \(2^{H-2}\mid m+1\), and hence \(2^H\mid3^{m+1}-1\) by \(v_2(3^{2u}-1)=3+v_2(u)\). The coprime moduli \(3^P\) and \(2^{H-3}\) supply exactly one simultaneous \(j\in[L,2L)\). In particular \(m\ge3H+1\), since \(2^{H-3}\ge H/2\) for \(H\ge4\). Put \(M=(3^{m+1}-1)/2^H\). The inequality \(m\ge3H+1\) gives \(3^{m+1}-1>2\cdot12^H\), so \(M>2\cdot 6^H\). The theorem `all_earlier` now gives the second claim at this same ordinary parameter.

The conclusion leaves unrestricted excess grade, later postpeak clocks and other forms of comparison available.
