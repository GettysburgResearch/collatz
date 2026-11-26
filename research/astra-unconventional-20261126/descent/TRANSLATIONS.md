# Fixed-source translations and the sharp consecutive-block bound

**PROPOSED.** Write \(\Lambda(y)=(\operatorname{Good}(y),\operatorname{Good}(3y-1))\). A block here means actual ordinary pairs with a common clock, equal odd counts on both arms, and the same two physical outcomes. Three consecutive starts are possible. Four are impossible. A separate return family can spend arbitrarily close to ten clocks per odd on each arm. [Strict Lean block proof](Translations.lean) · [Return-word replay](paired_words.py)

## A full ternary digit at one fixed endpoint

For each nonnegative integer \(t\), the two neighboring starts \(204+256t,205+256t\) both return to \(22+27t\) at clock 8 with three odds per arm. The upper starts reach \(3(22+27t)-1\). The two lower affine numerators have constants 124 and 97. Their difference is \(3^3\), so their inverse images at the very same ordinary endpoint differ by one.

At \(X=551+729t\), take any of
\[
  Y=24748+32768t,\qquad 24749+32768t,\qquad 24750+32768t.
\]
Every \((Y,3Y-1)\) reaches \((X,3X-1)\) at clock 15 with six odd departures per arm. The three lower starts cover all residues modulo three. For any prescribed ternary digit, the choice is made after fixing \(X\). The physical height is explicit and grows at asymptotic ratio \(32768/729\). The two identities follow by direct base replay at \(t=0\) and the ordinary prefix-lift formula. Lean proves both identities for every \(t\).

Suppose four consecutive starts \(b,b+1,b+2,b+3\) had such a return. The four lower inputs cannot share both grade and endpoint at any clock below four. At clock zero the starts differ. For clocks one to three, fewer than four parity words have any given grade, and one parity word and endpoint determine a unique start. At clock four some lower input has already physically merged with an upper input. The following cases show this by elementary shortcuts.

| Condition on the four starts | Cross merger |
|---|---|
| They contain \(n=4k+2\) and \(n+1\) | \(T^2(n)=T^2(3(n+1)-1)=3k+2\) |
| \(b=8k+7\) | Use \(n=b+2=8(k+1)+1\). Then \(T^3(n)=T^3(3(n+1)-1)=9(k+1)+2\) |
| \(b=16k+3\) | \(T^4(b)=T^4(3b-1)=9k+2\) |
| \(b=16k+11\) | \(T^4(b)=T^4(3(b+1)-1)=27k+20\) |

The first row covers \(b\equiv0,1,2\bmod4\). The remaining three rows cover \(b\equiv3\bmod4\). A physical merger persists at all later clocks, whereas positive \(X\) and \(3X-1\) are distinct. Lean checks the fourth-clock identity on all sixteen residues and lifts the word pair with its precise difference of one in the grades. This settles consecutive starting pairs. A progression with stride divisible by a large power of two has a different binary prefix structure.

## Repair of every nonmerged paired prefix

Use the normalized relative state \((d,C)\) of [the exact return grammar](PAIRED.md). Thus \(d=1+s-p\) and the two germs satisfy \(3^{\max(-d,0)}V-3^{\max(d,0)}U=C\). Start at \((1,-1)\). Any finite binary prefix that has kept the two affine germs distinct can be completed to an exact return to \((1,-1)\).

Indeed, the deterministic two-form controller in PR195 merges any two distinct integral affine germs whose free coefficients are powers of three. Apply it to the lower and upper forms, counting the initial upper coefficient three as one additional grade. Stop one clock before the first equality. Two simultaneous even steps preserve a nonzero disparity up to division by two, and two simultaneous odd steps are injective. At the last mismatch the arriving slopes must be equal. Direct substitution shows that the only two premerger states are \((1,1)\) and \((-1,-1)\). The respective lower parity words \(001\) and \(100000001\) return them to \((1,-1)\). Each bit can be imposed on the free parameter and forces the upper parity. The resulting grade difference is the initial one, so the original lower and upper grades agree. Positive ordinary lifts exist on the resulting binary cylinder. This repair changes the binary continuation. An ordinary endpoint fixed in advance must also pass the ternary image condition. [PR195 deterministic merger](https://github.com/GettysburgResearch/collatz/blob/f192322f70073ba44bc9f98785a51c27a4da9ee5/research/astra-global-closure-20261124/round13/trace/STEERING.md)

## An internal cycle at twenty clocks per two odds

The following three lower parity words have unique upper words from their listed initial states.

| Segment | Initial state | Lower parity string | Final state | Lower, upper odds |
|---|---|---|---|---|
| Prefix | \((1,-1)\) | \(\mathtt{00000001000000001}\) | \((9,-9899)\) | \(2,10\) |
| Lap | \((9,-9899)\) | \(\mathtt{00000000001000000001}\) | \((9,-9899)\) | \(2,2\) |
| Exit | \((9,-9899)\) | \(\mathtt{0000000000100000001111000001000111000}\) | \((1,-1)\) | \(9,1\) |

The lap passes through \((10,-14848),(9,-9856),(10,-115),(9,-9899)\) after successive event blocks of lengths \(1,10,8,1\). The prefix, \(n\) laps and the exit therefore give an ordinary contextual return with \(H=54+20n,\ p=11+2n\) for every \(n\ge0\). The binary cylinder of each finite word has positive ordinary lifts. Its lower and upper affine constants obey \(D_u-3D_\ell=3^p-2^H\). The lap's rational fixed points are \(527360/1048567\) and \(262147/1048567\). They satisfy the same internal chart relation. A fixed endpoint in that chart admits \(n\) reverse laps only if its lower coordinate agrees with the first rational center modulo \(3^{2n}\). The ordinary endpoint cannot acquire unlimited free laps from this one loop.

## A uniform bound for a single prescribed target

Let \(W_p\) count all contextual returns of grade \(p\), over all clocks. Fix a target \(A\bmod3^L\), a source cylinder \(B\bmod3^b\), and a budget \(P\) with \(b\le L\). Suppose **every** positive integer \(X\equiv B\bmod3^b\) has a paired ancestor \(Y\equiv A\bmod3^L\) of grade \(p\le P\). Then
\[
  3^{L-b}\ \le\ \sum_{p=0}^P W_p\,3^{-p},\qquad W_0=1.
\]
For a given word, \(2^HX=3^pY+D_\ell\) puts all its usable endpoints into the one residue \(2^{-H}(D_\ell+3^pA)\bmod3^{L+p}\). Count the residues modulo \(3^{L+P}\) covered by the source cylinder and sum the maximum contributions of the words. Every residue has positive ordinary representatives. The same lower bound holds for an additional coprime modulus on \(X\) by the Chinese remainder theorem. In particular \(X=26+72t\) occupies the full ternary cylinder \(8\bmod9\). The target may be chosen separately for each \(L\) and may be the single root of the canonical terminal congruence. Uniformity over ordinary sources is essential. Spending \(P\le L\) would require an exponential upper growth rate of at least 9 for \(W_p\). Whether that rate is attained remains open here.
