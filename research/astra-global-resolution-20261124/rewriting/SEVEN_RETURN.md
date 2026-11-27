# Descent from one three-step return to the multiples of seven

**PROPOSED, kernel-checked reduction.** On positive integers let \(T(x)=x/2\) at even inputs and \(T(x)=(3x+1)/2\) at odd inputs. Write \(C\) for the actual basin of 1. Then
\[
  \text{every positive integer reaches 1}
  \quad\Longleftrightarrow\quad
  \forall u\ge0,\quad 9u+8\in C\ \Longrightarrow\ 8u+7\in C.
\]
The reverse implication in this equivalence uses a complete finite reduction. It removes the second transfer in the short table below. Proving the one displayed physical basin implication at every parameter remains open.

## How the extra edge arises

For \(x=8u+7\) the trajectory from \(7x\) first returns to a multiple of seven after three shortcut steps:
\[
  56u+49\ \longmapsto\ 84u+74\ \longmapsto\ 42u+37\
       \longmapsto\ 7(9u+8).
\]
Define \(H(8u+7)=9u+8\). There is also the physical identity \(T^3(3x)=H(x)\): the intermediate values are \(36u+32,18u+16\). Thus the residual condition asks whether convergence of \(3x\) implies convergence of \(x\) on this single binary class. Equivalently, convergence of \(y\) should imply convergence of \(2y+1\) for \(y=8\bmod 9\), since \(T^2(8u+7)=18u+17\).

The quotient of one other first return at seven gives a short introduction to the reduction. The following six disjoint rows cover every \(x>1\). The middle entry \(z\) is always positive and strictly smaller than \(x\).

| Source \(x\) | Smaller \(z\) | Physical witness |
|---|---|---|
| \(2u\) | \(u\) | \(T(x)=z\) |
| \(4u+1,\ u>0\) | \(3u+1\) | \(T^2(x)=z\), word 10 |
| \(16u+3\) | \(9u+2\) | \(T^4(x)=z\), word 1100 |
| \(32u+11\) | \(27u+10\) | \(T^5(x)=z\), word 11010 |
| \(8u+7\) | \(6u+5\) | \(T^3(7x)=7(9u+8)\), word 101, and \(T(z)=9u+8\) |
| \(32u+27\) | \(27u+23\) | \(T^5(7x)=7z\), word 10011 |

Parity words list source bits in chronological order. In the last row the intervening values are \(336u+284,168u+142,84u+71,126u+107\). Their residues modulo seven are \(4,2,1,2\). Strong induction therefore suffices if each of the last two quotient landings transfers convergence back to its source. [Six-row Lean proof](SevenReturn.lean)

## Removing the five-step return

The longer certificate dispenses with the last quotient transfer. In its graph ordinary edges may be traversed in either direction. The single extra edge is directed \(8u+7\to9u+8\). A path is read backwards when propagating membership in \(C\). The only new logical implication it uses is \(9u+8\in C\Rightarrow8u+7\in C\).

| Letter | Move on its exact integer domain | Meaning |
|---|---|---|
| h | \(2v\to v\) | ordinary |
| D | \(v\to2v\) | reverse ordinary |
| t | \(2v+1\to3v+2\) | ordinary |
| i | \(3v+2\to2v+1\) | reverse ordinary |
| S | \(8v+7\to9v+8\) | directed quotient return |

Each leaf starts from an affine progression \(a t+b\), \(t\ge0\), with \(b\) its least representative above 1. At a letter \(iv+j\to kv+l\), the checker requires the *identities* \(a=i a'\), \(b=i b'+j\), and replaces the row by \((ka',kb'+l)\). Hence each letter has its declared domain for every lift. A path ending at \(ct+d\) is accepted only if \(c\le a\) and \(0<d<b\). All intermediate points stay positive: this holds initially, and each of the five rules takes a positive integer in its stated domain to a positive integer.

An unresolved row splits into its \(k\) child rows, with high parameter \(t=kq+j,\ 0\le j<k\). Starting with \(t+2\), the successive radices are \(32,18,12,12,12\). The checker validates the subdivision and all 291 leaf paths, comprising 52 distinct words and 3,483 letters. Every path has length at most 38. The modulus of a deepest row is \(995328=2^{12}3^5\). The root covers all integers from 2 upward. The base case 1 is supplied separately.

| Modulus | Leaves certified at that level | Rows requiring a further split |
|---:|---:|---:|
| 32 | 31 | 1 |
| 576 | 13 | 5 |
| 6,912 | 49 | 11 |
| 82,944 | 126 | 6 |
| 995,328 | 72 | 0 |

On the entire table the smaller endpoint is at most \(118x/123\). This supplementary rational bound follows by taking the larger of \(c/a\) and \(d/b\) on each affine leaf. The formal proof requires only strict descent. Reading a successful path backwards and applying strong induction gives \(\forall x>0,\ P(x)\) for any label \(P\) containing 1 and closed under ordinary equivalence and the displayed one-way implication. Taking \(P=C\) proves the equivalence. The actual orbit definition and forward invariance at the \(1,2\) cycle are included. [Full certificate and Lean proof](SingleReturn.lean)

## Where least failure stops

Write \(r=u+1\). The remaining implication is \(9r-1\in C\Rightarrow8r-1\in C\). A failure at \(r=3s\) is exactly a failure at \(2s\): \(T(18s-1)=27s-1\) and \(T(16s-1)=24s-1\). Repeating this strict parameter reduction discharges all positive \(r\) divisible by three once the ternary units are known. Thus a least failing parameter is prime to three. For such parameters the original source may itself be the first extra edge: the words on \(32t+7,32t+15,32t+23,32t+31\) start with S. On some deeper leaves a required transfer even lies above the original input. At \(x=122875\), for example, letter 26 requests a transfer at \(20970919\). These are exact size comparisons inside a proposed argument, not examples of orbit divergence. Induction on the original integer alone cannot justify that transfer.

There is a further physical reduction on the binary-child formulation. Every \(y=9r-1\) has child \(2y+1=18r-1\). If \(r=2s\), ordinary steps on both coordinates exchange this pair with that for \(3s\), preserving both labels. Repeat until the parameter is odd. This process terminates because each exchange lowers its binary valuation by one. If the odd parameter is \(4k+3\), the two inputs \(36k+26\) and \(72k+53\) actually meet at \(27k+20\), after two and three steps respectively. This discharges the entire class. At odd parameter \(4k+1\) the two inputs are \(36k+8\) and \(72k+17\). Consequently the fully formalized remaining condition can be written
\[
       \boxed{\ \forall k\ge0,\quad 36k+8\in C\Longrightarrow72k+17\in C.\ }
\]
This asks for closure under appending the binary digit 1 on a single class modulo 36, with positive *ordinary* antecedents already known to converge. A failing parameter, if one exists, therefore yields such an even antecedent. The first parameter reduction in this section minimizes size; the second takes a finite number of actual physical steps and can increase size. Those reductions need not select the same witness. [Formal equivalence, theorem collatzIffEvenChild](SingleReturn.lean)

The synchronization bound in PR146's THREE_RAY_UPPER already gives \(O(N/\sqrt{\log(2N)})\) exceptions in each interval of \(N\) parameters for the unrestricted-clock physical meeting on this restricted tripling ray. Indeed a parameter interval maps to an interval of length \(8N\) on the unrestricted ray. This gives two-way physical transfers off that exceptional set. The kernel proof requires the directed implication on every outstanding ordinary source. An estimate allowing a single permanent physical failure does not discharge it. [Fixed-head upper bound](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md)

## Sources and relation to previous reductions

Yolcu, Aaronson and Heule, *An Automated Approach to the Collatz Conjecture*, JAR 67 (2023), §4.5, equation (10), obtain the *same* affine branch \(H(x)=(9x+1)/8\) on \(x=7\bmod8\) in a different partial system. Their second branch is \(3x/4\) on multiples of four. Their Proposition 4.15 relates termination of that partial system to residue avoidance. Here \(H\) is coupled to ordinary edges in a finite descent proof, using the first return at seven to identify the specific physical implication left open. [Author manuscript](https://emreyolcu.com/research/rewriting-collatz.pdf)

Applegate and Lagarias, *The 3x+1 semigroup*, JNT 117 (2006), Theorem 1.1 and §2, obtain a full semigroup result using lists of multipliers and a separate treatment of the long all-odd class. A product of their ratios need not be the ratio of two points on one orbit. Each displayed return here is a specified physical path on its scaled coordinate. [Primary paper](https://websites.umich.edu/lagarias/doc/3x%2B1semigroup.pdf)

PR146 at f431078244e868dc699fad011044f0d5e7f76437 already provides global multiplier criteria, restricted tripling criteria including a different \(1\bmod16\) family, and two- and three-adic obstructions to finite smaller-partner searches. PR157 at 64361ecca770092d6c8242dc6211e38818af2e50 gives a forward multiplication-by-five criterion. The claim here is the indicated five-step-to-three-step elimination and full formal coverage with a single *directed* restricted return. [PR146 restricted tripling](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_ONE_RESIDUE.md) · [PR146 bounded-clock obstruction](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/ADJACENT_DESCENT.md) · [PR157](https://github.com/GettysburgResearch/collatz/blob/64361ecca770092d6c8242dc6211e38818af2e50/research/global-closure-20261120/merger.md)
