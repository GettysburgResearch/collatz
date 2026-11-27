# Independent review of the finite-state affine obstruction

**Verdict: VERIFIED as a written theorem, AR5 only.** In a nonempty finite deterministic machine allowing both ordered blocks $L=(2,1)$ and $P=(1,4)$ from each state, assume the specified coefficient law on every transition with a common slope $0<a<1$. An integral affine shadow at an integer input $q$ then forces $83\mid q+7$. This verdict applies to the pinned statement and its AR2/AR4 dependencies used in the proof. The full arbitrary-machine deduction is written mathematics. No independent full Lean formalization of AR5 was used in this review.

**Frozen local sources** under `research/astra-global-closure-20261124/audit/`:

| File | SHA-256 |
|---|---|
| SHADOW_RIGIDITY.md | 8fc11084c6d8097169edc5f0bf855b8fb424978d913a2e47c6937bbd7ac3308a |
| MemoryShadow.lean | 3c12919535f8951fb04c3f2cd74e2369409189adfc7db8ec03f8b50301b79a54 |
| ResidueOrbit.lean | f5eb8ff6f62a344b289bbcec5bd2a13f762622a75445b1a25ee641764154a212 |
| shadow_checks.py | e80936fbb92a76f039dd06f1d37674e98b9927a1c20b2f288bd9e3416dfb54e6 |

The source question is TCP-5 in PR 191, commit `37b3916633cd32a0c173b20bb18ec3a7ec290a63`, `research/two-sided-cycle-packing-20261124/README.md`. The conclusion below is about total per-letter finite-state templates, with two odds and the original clock in each output block.

## Reconstruction

1. Put $x=7a-b_s$. The allowed $L$-carries give $9x-8x'=c\in\{5,7\}$. Summation around an $L$-cycle of length $r$ gives denominator dividing $9^r-8^r$, which is positive and odd. Pullback through the finite initial $L$-tail introduces only powers of 9. Iteration expresses $x$ as an average of future $L$-carries with weights $(8/9)^j/9$ summing to one. Boundedness of the finite set of offsets justifies removing the remainder. Thus $5\le x\le7$ and every reduced denominator is odd, with no ordinary all-$L$ realization needed.

2. For $P$, $32x'=9x+166a-c$, so $166a$ also has odd reduced denominator. Consequently $a=A/(2^uB_0)$ in lowest terms with $u=0$ or 1 and $B_0$ odd. At the anchor $x=a(q+7)-y$ with $y$ integral, so its odd denominator divides $B_0$. Set $z=B_0x$, $F=166A/2^u$. The edge laws make $8z'$ or $32z'$ integral from an integral $z$; odd denominator of $z'$ then forces it integral. All reachable states carry this lattice even though the original affine shadow need not stay integral on arbitrary future input words.

3. If two $x$ differ by a positive integer $h$, then $h=1$ or 2. For $h=1$ the difference of the two $L$-successors must be integral, since eight times it is an integer and its denominator is odd. But the latter numerator is $7,9,11$, each impossible. For $h=2$, the corresponding $P$-numerator lies in $[4,32]$, whose only multiple of 32 is 32. This forces a pair of successors differing by 1. Thus $x\bmod1$ determines $x$ on the reachable set.

4. Write $B_0=3^eD$, with $(D,6)=1$. On $z\bmod D$, both generators are permutations $f(z)=9z/8,\ g(z)=(9z+F)/32$. Direct composition gives $(fg)(gf)^{-1}$ equal to translation by $F/256$ under right-to-left composition. The inverse permutations can be realized as nonnegative powers of the generators on residues. Applying these words to a state is legal because transitions are total; inversion of state transitions is never required. The generated translations fill the complete additive subgroup $\gcd(D,F)\mathbb{Z}/D$. Coprimality of $A$ and $D$ makes $\gcd(D,F)$ exactly 1 or 83, including when $83^2\mid D$. In the latter case the anchor obeys $2^u z\equiv A(q+7)\pmod{83}$. Under the contradiction hypothesis its residue is nonzero. The multiplier $9/8\equiv53\pmod{83}$ has order 82 because its 41st power is $-1$ and its square is 70. Thus $f$-powers reach every nonzero coset mod 83, and translations fill each entire coset mod $D$.

5. Choose $2h\ge e$ and the pre-$L$ residue $4\cdot3^e(8/9)^h\bmod D$. Its residue is nonzero modulo 83 whenever this restriction applies. After $L^h$, the integer $z'$ is 0 modulo $3^e$ and equals $4\cdot3^e\bmod D$. The forced fractional part of $x'=z'/B_0$ is $4/D$ if $D>1$, since then $D\ge5$. For $x'=5+v+4/D,\ v=0,1$, the next $L$-edge gives the integer $8Dx''=9Dx'-Dc$. The odd reduced denominator of $Dx''$ forces divisibility of its right side by 8. It follows $(5+v-c)D\equiv4\pmod8$. Inverting any odd $D$ leaves 4 mod 8 fixed, whereas $5+v-c\in\{-2,-1,0,1\}$. Hence $D=1$ under the contradiction hypothesis.

6. If $B_0=3^e$, the composition of any fixed length-$h$ word, with $h\ge1,\ 2h\ge e$, erases the incoming $z\bmod B_0$ because its coefficient contains $9^h$ and the denominators are dyadic units. By step 3 it fixes the outgoing $x$, independently of the reachable start. Reading an $h$-word and then a letter therefore produces exactly the same outgoing offset as its last $h$ letters. Every $h$-word is legal from the anchor. This constructs a bona fide full bounded-past coefficient rule without assuming that state identities, individual output choices, or entire future trajectories coincide. This reasoning also handles $e=0$.

7. I checked the AR2 reduction used here. Oldest-letter siblings differ by $2d/9,\ d\in\{-1,0,1\}$, using their common $L$-successor. Comparing successor sibling differences after $L$ and $P$ eliminates the parent difference and forces $9\mid(d_L-4d_P)$. Its magnitude is at most 5, implying both digits vanish. Reduction to one letter follows by induction. Direct independent rational enumeration at one letter used $H=0,\pm2/9,\ X\in\{5,7\},\ Y\in\{5,7,11,19\},\ a=(Y+23X-23H)/166$ and the off-diagonal carries $X-9H,\ Y+9H$. The admissible slopes were precisely $60/83,61/83,63/83,67/83,572/747,724/747$. Their reduced denominators all contain 83, contradicting $2^u3^e$.

The modular computations and the six rows were independently evaluated with Python integer arithmetic and `fractions.Fraction`. As stress controls the pre-$L$ selection with $e=h=3$ reached the required $4\bmod D$ after division by 27 for $D=5,7,11,25,83,415,6889,2075$. These finite checks supplement the all-modulus proof.

The argument does not transfer to partial machines, source-dependent affine slopes without the edge identity, arbitrary changing macro-clocks, mixed past/future windows, or an exceptional individual infinite ordinary path. It proves no claim about convergence of a particular nonzero residue orbit.
