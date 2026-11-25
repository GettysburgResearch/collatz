# Independent review of three physical post-peak mergers

**Verdict VERIFIED for the written three-parent merger under (1), its
nonempty progressions and their density.** The two-parent companion
also passes the same arithmetic reconstruction. This review addresses
the local arithmetic README at SHA-256
a28f8ddbf451a752e9b8a588f6b0d19c748cd901e42f9a86fd358aabf9f199b1
and the seed/terminal numerals used there. The Lean file was still
being edited during this review; module compilation is separately
accounted for by the author and the root build. No unconditional
pointwise cover of all positive tower indices follows.

1. For $j=11+162m$ the parent is an integer: $2^{162}=1\bmod243$
   fixes $128\cdot2^j-271\bmod243$ at its value for the initial
   parent 3233. It fixes the quotient modulo three, and the defining
   numerator fixes the quotient modulo 16, giving $17\bmod48$.
   All parents have the base low 9 bits since
   $81(Z_m-Z_0)=2^{18}(2^{162m}-1)$. The base lower word
   $1010110$ has full numerator offset 143, so $T^7 Z_m=2^j-1$.
   The base upper word $110000001$ has numerator offset 271, so
   $T^9(3Z_m)=(81Z_m+271)/512=2^{j-2}$. The first nine terms
   before that landing exceed one at the base and all larger
   lifts; the latter trajectory then halves exactly $j-2$ times.
   This independently proves the upper's three-odd first hit at
   $j+7$ for every index. After the seven lower steps the next
   $j$ inputs are odd and land on $3^j-1$. Thus the common local
   comparison starts at different original clocks $7+j$.

2. I independently iterated with **one fixed odd denominator**
   $D=3^{475}$, updating a numerator $N$ to $N/2$ or
   $(3N+D)/2$ using its parity. The numerators
   $3^{475+t}-D$ at $t=11,-151,-475$ first reached $D$ at
   $(89,45),(327,151),(947,475)$ respectively (clock, odd count).
   At clock 947 they all equal $D$ with counts $474,461,475$.
   For $R=3^{162m}=1+2^{947}t_0$, the actual integer post-peak
   starts differ from those three centers by
   $3^{11-162i}2^{947}t_0$ in the odd-denominator rationals. Their
   first 947 physical parities consequently agree with the centers'
   and the terminal increments are $3^{485}t_0,3^{310}t_0,t_0$.
   The rational centers serve to compute finite affine coefficients
   of the actual positive integer prefixes.

3. $t_0=4^{L+1}u$ under (1), including $L=0$. From $1+4v$ the
   odd-then-even pair lands on $1+3v$. The $L+1$ physical laps
   leave exactly $1+3V_g$, $V_g=3^{g+L}u$ odd. Its next step
   equals the next step of $V_g$. Thus **the full 1379-clock
   comparison applies with no extra or missing step**. The PR206
   literal 'one' at 45a6a111321f947a8482c9e96e898435b57cee09
   was fetched and compared digit for digit to the local seed.
   It is already the least nonnegative residue modulo $2^{1379}$.
   SHA-256 of its ASCII decimal digits is
   6e75e0a4b98f2378f51315a20952ebad667234b851ca52faad4701480527870e.
   A $2^{1379}b$ change of the common base contributes
   $3^{658}b$ at each terminal since $P+g=658$. The quotient
   $b$ is nonnegative, including a possible zero lift.

4. The following independent ordinary composite test joins the two
   banks and both trailing steps. For $L=0,1,7,215$, set
   $e=949+2L$, $M=2^{1379}$ and choose the least nonnegative $u$
   satisfying $3^Lu=S\bmod M$ and $2^eu=-1\bmod D$ by CRT. Put
   $n=(2^eu+1)/D$. Starting separately at $3^s n-1$ for
   $s=0,324,486$, literal shortcut iteration reached the predicted
   common endpoint at respectively 2328, 2330, 2342 and 2758
   steps in the four tests. The common terminal bit lengths were
   1796, 1797, 1807 and 2137. Every 947-step intermediate and
   every post-lap endpoint and common successor were separately
   compared with their affine formulas. These twelve composite
   starts are positive integers; the chosen $n$ need not itself
   be a power of three. Full original upper and lower entry clocks
   were also checked at $m=0,1,7,31,63$.

5. For every $m>0$,
   $\nu_2(3^{162m}-1)=3+\nu_2(m)$ by difference of squares.
   Thus $m=2^{946+2L}w$ has the necessary valuation exactly when
   $w$ is odd. For $B=3^{162\cdot2^{946+2L}}$ the map
   $(B^w-1)/2^{949+2L}$ preserves binary valuations of
   differences; it permutes residue classes at every finite
   precision. Its parity is the parity of $w$. Multiplication by
   $3^L$ is a permutation, so (1) defines one class of $m$
   modulo $2^{2325+2L}$. An independent binary lifting computation
   with multiplicative residuals recovered valid $m$ residues for
   $L=0,7,32$, of bit lengths 2325, 2337, 2388 and exact
   valuations 946, 960, 1010. These checks used modular powers;
   they did not expand the ordinary orbit of those $Z_m$.
   Every odd modulus is coprime to each period. Distinct $L$ have
   disjoint valuations, and the remainder after $L$ has density
   at most that of divisibility by $2^{946+2L}$, so the geometric
   series gives $4\,2^{-2325}/3$ with no countable-additivity
   assumption about natural density.

6. For the two-parent companion the same two centers both hit one
   by 327 at the same parity of time. Their augmented grades there
   are $175,0$. Replacing $947$ by $327$ yields the valuation
   $326+2L$ and period $2^{1705+2L}$. The extra $g=175$ row was
   checked directly at the same seed and augmented final grade.
   If one parameter belonged to both the two-parent and the
   three-parent progressions, their $L$ values would differ by
   310. The two identical odd quotients $u$ would then force
   $3^{310}=1\bmod2^{1379}$, whereas
   $\nu_2(3^{310}-1)=3$. Thus the union of the two displayed
   families has density $(4/3)(2^{-1705}+2^{-2325})$.

[Reviewed statement](../../../../research/astra-global-closure-20261124/round13/arithmetic/README.md) · [PR197 upper family](https://github.com/GettysburgResearch/collatz/blob/10d87fee615d1095990d6b7ea329126b4cf7aa5a/research/ayh-resource-reset-20261124/closing-proposal/MersenneBarrier.lean) · [PR206 tower certificate](https://github.com/GettysburgResearch/collatz/blob/45a6a111321f947a8482c9e96e898435b57cee09/research/clock-itineraries/TowerFrontierMergers.lean)
