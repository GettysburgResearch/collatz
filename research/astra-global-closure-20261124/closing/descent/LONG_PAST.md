# A smaller predecessor of the actual light intermediate after twelve blocks

Let \(T\) be the ordinary shortcut map. Suppose the positive source \(x\) follows the twelve consecutive L/P blocks **PLPPPLPPLPPP**, ending at \(q\). Suppose only that the next two shortcut steps give the integer \(f=(3q+1)/4\). Then there is an explicit positive odd \(m<f\) with
\[
                       T^{38}(m)=f=T^{56}(x).
\]
If the path from \(f\) does not converge, the smaller \(m\) cannot converge. The history can follow arbitrarily long finite L/P scripts, since any finite concatenation is realized by its ordinary dyadic parity cylinder. The theorem places no restriction on the orbit after \(f\). No recurrence of this particular history is asserted.

**The certificate at the prescribed state.** Write \(\xi=(q+7)/2\) and \(\xi_{\rm in}=(x+7)/2\). The two block maps act by \(\xi\mapsto9\xi/8\) on L and \(\xi\mapsto(9\xi+83)/32\) on P. The given word has 54 clocks and 24 odd inputs. Direct composition gives
\[
 \begin{split}
 2^{54}q&=3^{24}x+4310659012756573,\\
 2^{54}\xi&=3^{24}\xi_{\rm in}+65204735786187547 .
 \end{split}
\]
Thus \(\xi\equiv42625563916\bmod 3^{23}\). Substituting \(4f=3q+1\) into the first equation yields a full extra ternary digit:
\[
 2^{56}f=3^{25}x+30946375547751703,\qquad
 f=63938345869+3^{24}j,\qquad j\ge0.
\]
Here \(3^{24}=282429536481\); the displayed least residue is verified by multiplying by \(2^{56}\) modulo \(3^{24}\). Take
\[
 m=62228755903+2^{38}j
   =\frac{2^{38}f-458686216993}{3^{24}}
   =\frac{3x-316169}{262144}.
\]
The first expression gives positive odd integrality and \(m<f\), since \(62228755903<63938345869\) and \(2^{38}=274877906944<3^{24}\). At \(j=0\) the first 37 shortcut bits are 1111110111110111101100011110001000101. They have 24 odd visits and carry 458686216993, and their terminal value is \(127876691738=2\cdot63938345869\). One further even step reaches \(f\). On the residue class the same 38 bits are legal: changing the start by \(2^{38}j\) changes the endpoint by \(3^{24}j\) and preserves every parity. Equivalently, the integer endpoint equation fixes the input modulo \(2^{38}\) because its odd multiplier is invertible.

**Relation to the central section.** If the following block is a genuine L, \(f\equiv3\bmod4\). Here \(v_3(f-1)=3\) and \((f-1)/27\equiv17\bmod27\) throughout, so such \(f\) belong to the odd PR174 section \(f\equiv55\bmod108\). This \(17\bmod27\) differs from the \(16\bmod27\) of the basic height-three tour family and the \(22\bmod27\) on the \(9148\bmod 3^{13}\) entrance. Also \(\xi\equiv67\bmod729\), different from the \(229\bmod729\) at the end of LPP. The full L is a genuine additional binary condition; for example \(j=0\) gives an integral \(f\equiv1\bmod4\) in the arithmetic residue calculation. Only the partial two-clock equation is needed for the certificate. [PR174](https://github.com/GettysburgResearch/collatz/tree/c92cd473de3b85ceb945702a726d2eb7350a6af8)

The history has isolated L's and ends in three P's. The six explicit fixed-half/ramp certificates in PR192 do not already give a partner below this \(f\) by merely starting one inside the twelve letters. For an interior start \(z\) before the last P, its initial L run there has length at most one. The corresponding fixed half is \((z-7)/2\); every listed ramp at such a run is at least that large. Each such \(z\) is at least the last P entrance \(z_*=(32q-5)/9\). Indeed, before that entrance each remaining L can be paired with a succeeding P, and any unmatched P is contracting. The composite LP satisfies \((81z+103)/256<z\) for positive \(z\ge1\), and \(P(z)<z\). Consequently every such proposed partner is at least \((16q-34)/9>f\) for the large positive \(q\) in this cylinder. This comparison concerns those six prescriptions applied within this fixed history. Other merger constructions and more distant prior paths are unrestricted. The companion seven-letter example has a different overlap: its prescribed \(f\) already has a 23-clock predecessor by truncating PR192's PLPL row. [PR192, six fixed-half/ramp prescriptions](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/DESCENT_EXTENSION.md)

The Lean theorem takes twelve raw integer block equations and \(4f=3q+1\), derives the needed residue of \(f\) internally, and proves the positive odd smaller source and its full physical 38-clock trajectory. The source-period observations and prior-certificate comparison are written deductions. [LongPast.lean](LongPast.lean)

