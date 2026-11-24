# A residue-free smaller ordinary orbit for separated paid returns

**Lean checks the separated-input descent and the finite triple-paid merger. Universal descent remains open.** On the ordinary accelerated odd Collatz map let an exact two-gap block be either
\[
 L=(2,1),\quad L(q)=(9q+7)/8,\qquad
 P=(1,4),\quad P(q)=(9q+5)/32 .
\]
Say that a one-sided infinite input is separated if at least six L's occur between consecutive P's. There is no requirement on the initial number of L's.

**Theorem.** For every positive ordinary infinite separated input and every odd state on that input, including either intermediate phase inside its blocks, there is a strictly smaller positive ordinary odd source whose trajectory never reaches one. No congruence restriction on the starting value is imposed. In particular the globally least positive odd nonconverger, if it exists, cannot occur anywhere on this class of inputs.

The earlier [PR191, TCP-5](https://github.com/GettysburgResearch/collatz/blob/37b3916633cd32a0c173b20bb18ec3a7ec290a63/research/two-sided-cycle-packing-20261124/README.md) permits all L/P schedules when the boundary satisfies its modulus-83 guard. The present theorem removes that guard on a schedule class. It includes contracting and expanding complete words: the multiplier on a P and six L's is below one, while on a P and eleven L's it exceeds one. The [PR193 partner theorem](https://github.com/GettysburgResearch/collatz/blob/c6cb5e66516a86c33a757154983bbddc822510de/research/astra-universal-descent-20261124/shadow.md) constructs finite actual endpoint mergers subject to different guards. Our comparison is a separate infinite ordinary orbit, with no common endpoint assumed.

## Constructing the smaller source

Use the dyadic slope and denominator
\[
 D=2^{18}=262144,\quad m=251349,\quad \lambda=m/D.
\]
Define seven phases: F for at least seven L's remaining before the next P, and phases 6 through 1 for exactly that many L's. A P is its own phase. An infinite positive input cannot terminate in all L's, since iterating L gives \(8^h\mid q+7\) for every \(h\). Thus every phase has its stated meaning, even at time zero.

Use the following corrections \(K\) and literal target gap pairs. F and 6 share their correction.

| Input phase | \(K\) | Target gap pair | Target carry \(c'\) |
|---|---:|---|---:|
| F | −75565 | (2,1) | 7 |
| 6 | −75565 | (1,2) | 5 |
| 5 | −141101 | (2,1) | 7 |
| 4 | −149293 | (2,1) | 7 |
| 3 | −158509 | (2,1) | 7 |
| 2 | −168877 | (1,2) | 5 |
| 1 | −246077 | (1,2) | 5 |
| P | −332927 | (2,3) | 7 |

For an input boundary \(q_j\), define \(y_j=(m q_j+K_j)/D\). On an input edge of total binary clock \(A\in\{3,5\}\) and input carry \(c\in\{7,5\}\), the table satisfies
\[
 2^A K_{j+1}=9K_j+D c'-m c,\qquad
 2^A y_{j+1}=9y_j+c'.
\tag{1}
\]
F can be followed by F or 6. A P can be followed by 6 or F, both with the required reset correction. All other transitions are fixed. To derive the dyadic choice, set the free normalized correction to \(7\lambda-7\), its fixed value on L. Changing an L carry from 7 to 5 subtracts a quarter after that edge. Changing the P carry from 5 to 7 and imposing reset gives
\[
 83\lambda=84-\left((9/8)^6+(9/8)^2+9/8\right).
\]
The right side has numerator divisible by 83 over \(8^6\). This yields the stated fraction and the table by (1).

**Ordinary realization on the fixed input.** Every \(y_j\) is a dyadic rational with denominator at most \(D\). If the reduced denominator at some time is \(2^v\) with \(v>0\), then \(9y_j+c'\) has reduced denominator exactly \(2^v\); after the edge it is \(2^{v+A}\). Repetition contradicts the uniform cap. Thus all boundary shadows are integers. Their parity is odd by (1) modulo two. For a displayed pair \((u,A-u)\) one has \(c'=3+2^u\), and
\[
 3(3y_j+1)=2^u\big(2^{A-u}y_{j+1}-1\big).
\]
The parentheses are odd, proving the first gap is exactly \(u\). Dividing gives the second exact gap since the terminal boundary is odd. Both input and target blocks have two odd steps and odd total binary clock. After a hit on one all odd gaps would equal two, so an infinite concatenation of either alphabet cannot hit one. This argument uses indefinitely many edges of one fixed ordinary input, without replacing it by different finite witnesses.

For the positivity bound, the ordinary odd sources at most 15 all reach one (direct iteration). Consequently each input boundary of a positive infinite input is at least 17. All the corrections lie strictly between \(-2D\) and zero, and \(9/10<\lambda<1\). Hence \(0<y_j<q_j\) everywhere.

**Comparison at every odd phase.** At a boundary use \(y_j\). On a P the original intermediate \((3q_j+1)/2\) exceeds its boundary. At any unchanged L the target intermediate \((3y_j+1)/4\) is positive and strictly smaller than the corresponding original intermediate. At a switched L let \(1\le k\le6\) denote the number of remaining L's, including the current one. The input boundary immediately following the next P equals
\[
 Q=\big[9(9/8)^k(q_j+7)-58\big]/32 .
\]
For \(q_j\ge17\) this is strictly less than \((3q_j+1)/4\). Indeed \((9/8)^6<21/10\), giving \(320Q<189q_j+743<240q_j+80\) when \(q_j\ge17\). This later input state never converges and supplies the comparison directly. This finishes the proof including initial partial runs.

The residue guard removed here can actually fail on arbitrarily long matching *finite* positive inputs: any finite L/P gap script gives a nonempty odd dyadic class, and the Chinese remainder theorem permits \(q+7\not\equiv0\bmod83\) independently. No assertion of an infinite positive L/P orbit is needed or made.

## An asynchronous finite merger through a close cluster

There is also a positive result for a class explicitly outside the six-separated condition. Let an arbitrary finite ordinary prefix consist of $r$ L blocks followed by **three consecutive P blocks**, with $r\ge0$. The following suffix of the trajectory can be unrestricted. Then
\[
 m=(q_0-7)/2>0,\qquad m<q_0,\quad m<(3q_0+1)/4,\qquad
 T^{3r+14}(m)=T^{3r+15}(q_0).
\]
Here $T$ is the shortcut Collatz map. If the original source is nonconvergent, so is this explicit smaller partner. The smaller comparison holds at the initial original odd intermediate as well: on an initial L it equals $(3q_0+1)/4$, whereas an initial P has larger intermediate $(3q_0+1)/2$. For instance the statement applies after any suffix restart at a block boundary with this pattern.

To see why it works, each L edge $8q'=9q+7$ transports the half via $8m'=9m+7$. Its actual three shortcut bits are $101$; the endpoint of the *final* shadow L is allowed to be even. At the triple P entry write $u=q_r$, at its end write $z=q_{r+3}$. The three ordinary clocks give $32768z=729u+6965$ and $16384z=729((u-7)/2)+6034$. The latter numerator identity has the target shortcut word $01111000100010$. In detail, $v=(u-7)/2=16384t+2846$ for some $t\ge0$, and the 14 physical steps take it to $729t+127=z$. The residue follows from coprimality of 729 and 16384, or by directly multiplying the displayed identity by an inverse modulo 16384. Propagation through the leading L's and concatenation prove the result for arbitrary $r$. This is an unequal-clock, exact **merger**, with no condition on the ternary residue of the input.

[descent_Triple.lean](descent_Triple.lean) proves the complete theorem on finite raw ordinary boundary equations, including the arbitrary L prefix, all fourteen shortcut steps, endpoints, positivity and strict inequalities. The strict Lean 4.34.1 run exited zero, source SHA-256 `c77134e6062994a093f370ac24b79ff78d184b3043be565946afc6f8c8301033`. Its public `Collatz.TriplePaid.triple_paid_merger` reports only `propext`, `Classical.choice` and `Quot.sound`.

## Attempt to close all return schedules

An initially tempting approach was to choose one rational slope and keep repairing the bounded affine correction on every L/P segment. The theorem above uses source infinitude to get ordinary shadows. The following obstruction explains why imposing the stronger *finite uniform coverage* requirement fails, even if a repair may inspect the whole segment.

**Obstruction.** No fixed rational \(0<\lambda<1\) and finite bound \(B\) can shadow **every positive finite** L/P input path by positive odd boundary values \(y_i\) with \(|y_i-\lambda q_i|\le B\), keeping two odd target steps of the same total binary length at each block. Every legal target gap split is permitted, and different horizons may choose different shadows. This is an obstruction to a universal proof template. It does not assert that an infinite least nonconverger would realize any prescribed finite word.

Here are the details. Write \(\lambda=m/d\) in lowest terms. The errors belong to a finite subset of \(d^{-1}\mathbb Z\). On an arbitrarily long constant-L input, the signed limiting source is \(-7\) in the 2-adic integers. Every prescribed finite prefix has positive lifts in any chosen odd-modulus class by the ordinary gap congruence and CRT. Choose a subsequence with constant initial error and nested target digits (finite branching). On the signed limit, the shadow starting from \(z=-7\lambda+e\) is 2-adically odd and has a bounded real orbit, since the signed source stays fixed and the errors stay bounded. Its real iterates are \(z'=(9z+c')/8\) with \(c'\in\{5,7\}\). Inverting and taking the bounded tail limit gives \(-7\le z\le -5\).

Write \(d=2^v d_o\) with \(d_o\) odd. Thus \(z=N/d_o\) with odd integer \(N\). Choose a positive input source in each prescribed residue \(r\bmod d_o\); integrality of its shadow gives \(2^v N\equiv-m(r+7)\bmod d_o\). All \(d_o\) classes for \(N\) must occur. Yet its first target L edge gives \(N/d_o\equiv9\) or \(11\bmod16\), and \(N\) lies in an interval of length \(2d_o\). There are at most \(2(\lfloor 2d_o/16\rfloor+1)<d_o\) such integers for odd \(d_o\ge3\). Therefore \(d_o=1\).

For a dyadic slope the same signed limiting shadow is an odd integer, hence either \(-7\) or \(-5\). Prepend H P's to the future all-L input. During P the error satisfies \(e'=(9e+c'-5\lambda)/32\) with \(c'\in\{5,7,11,19\}\). For sufficiently large fixed H, its final error is positive for every starting error of modulus at most B, since the minimum forcing is \(5(1-\lambda)>0\). The junction therefore has the unique error \(e_*=7\lambda-5\). This conclusion also holds after any further specified finite *past* word; take positive lifts of its concatenation with the P block and arbitrarily long L future, as above. On reversing a block at a known error, the target carry is uniquely determined if it exists: the options in either alphabet are pairwise distinct modulo nine, and the denominator of the error is a power of two. The reverse equation is \(9e_{\rm prev}=2^Ae+\lambda c-c'\). Thus reversing the H P's yields a common initial error from which arbitrary further past words are possible in reverse. Their finite reachable set \(R\) is nonempty and closed under both reverse labels.

Every member of \(R\) has arbitrary P past, hence belongs to \([(5-5\lambda)/23,(19-5\lambda)/23]\), in particular is positive. Repeated reverse L steps on \(z=e-7\lambda\) send \(z\mapsto(8z-c')/9\). The dyadic denominator clears after enough steps because division by nine preserves the 2-adic valuation, and all states are dyadic. Subsequent states are odd integers. Their real distance to \([-7,-5]\) tends to zero by the contraction ratio \(8/9\), so eventually they equal \(-7\) or \(-5\). Positivity of the error rules out \(-7\). Thus each state reaches \(e_*\); moreover each satisfies \(e\ge e_*\), because reverse L preserves the strict half-line below \(e_*\). This includes \(e_*\in R\). It follows from the P bounds that \(\lambda\ge60/83\) and
\[
 0\le s=e-e_*\le (134-166\lambda)/23\le14/23 .
\]
Reversing the finite path to \(e_*\) shows that each such \(s\) is a sum of distinct terms \((9/8)^k/4\), \(k\ge0\). At most two terms fit in \(14/23\), and \(k\le7\). There are exactly thirteen allowed sums, including zero. Reverse P at \(e_*\) now forces \(\lambda=(115+c'+9s)/166\). None of these 52 candidates is dyadic, by the exact finite integer check in the companion script. This contradicts the only remaining denominator possibility.

The stronger finite-wall hypothesis need not follow from least-source minimality. The positive six-separated theorem only forces a least counterexample following this alphabet to include a pair of P's with fewer than six intervening L's. A short pair gives a local contraction, but an earlier long L run can leave its endpoint above the original minimum. A proof that such defects force a return *below the fixed starting minimum*, or that they can be handled by a different ordinary shadow, is missing. Arbitrary high-carry paths outside L/P are a further open obligation. [Yolcu, Aaronson and Heule](https://doi.org/10.1007/s10817-022-09658-8) prove that termination of their full mixed-radix rewriting system is equivalent to Collatz; the equivalence supplies no well-founded order for this unresolved case.

## Exact verification

The unmarked-input theorem `Collatz.SeparatedDescent.separated_descent` in [descent_Separated.lean](descent_Separated.lean) was accepted by Lean 4.34.1, release commit `5045d0056413266e57c625dcd7c365b10e377c52`, with `-j1 -DwarningAsError=true`. The checked source SHA-256 is `db565fc09d38a450761c41cd1e01ad0de08ebcd8ceab90f12d4ead839404c16e`. It imports only `Std`. Its raw hypotheses are the Boolean separation rule, oddness and the displayed boundary clock laws; classification into the eight table rows is proved internally. Its conclusion covers any selected boundary or original odd intermediate and supplies a smaller odd positive integer with no literal shortcut iterate equal to one. All five printed transitive axiom inventories contain only `propext`, `Quot.sound` and, for the orbit conclusions, `Classical.choice`. The all-rational-slope finite coverage obstruction above is a written theorem.

The formal proof in fact forces the shadow to be an integer from the next **six** edges of the same sequence: their binary clocks contain at least 18 factors of two. The infinite-input hypothesis is used to keep producing the shadow and its unbounded ordinary clock. [descent_controls.py](descent_controls.py) ran in both ordinary and optimized Python, with identical successful results: 86 ordinary finite paths, 1,204 literal boundary comparisons, 83 initial values outside the old residue guard, all 52 candidates in the finite arithmetic obstruction, and 130 asynchronous triple-paid mergers. A legal initial run of 30 L's followed by two consecutive P's gives the starting L intermediate 811469695751566770196375928827. Its final boundary is 2930702791929351476163046976593 and every intervening odd value is above the starting intermediate. This is a finite control against using a local close-pair contraction as a return below the original floor.
