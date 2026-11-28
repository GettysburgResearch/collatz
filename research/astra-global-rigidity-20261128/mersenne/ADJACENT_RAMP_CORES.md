# Complete classification of two consecutive small shifted cofactors

For a positive odd integer $x$ write
$$
     x+1=2^s3^h\beta,\qquad s\ge1,\quad h\ge0,\quad (\beta,6)=1,
     \qquad A=s+h.
$$
The shortcut map $T(2a)=a$, $T(2a+1)=3a+2$ takes $s$ consecutive odd steps to the even integer $3^A\beta-1$. Write $f=v_2(3^A\beta-1)$ and take its $f$ consecutive halvings to the next odd $x'$. Define $s',h',\beta'$ by $x'+1=2^{s'}3^{h'}\beta'$. The exact identity at the next ramp start is
$$
    3^A\beta+2^f-1=2^{f+s'}3^{h'}\beta'.                                  \tag{1}
$$
The elementary ramp formula and the prime-to-six cofactor on a ramp are prior work. The cutoff below concerns consecutive *shifted* cofactors. It neither constrains primes of the unshifted states nor assumes that any later cofactor stays small. [Verger-Gaugry, Theorem 1.2 and Proposition 2.1](https://arxiv.org/abs/2611.14569) · [Paper 168, Lemma 3](https://rstation.ai/problems/collatz/papers/168) · [Paper 138, Corollary 6 on primes of unshifted ascending successors](https://rstation.ai/problems/collatz/papers/138)

**Pointwise conclusion.** Every positive odd $x$ with $\beta,\beta'\le1000$ reaches 1. There are exactly 2,857 such ordinary starts. The largest is $9,382,229$. Their 1,094 different pairs $(A,\beta)$ all have $A\le12$, and their full checked paths through $x'$ reach 1 in at most 163 shortcuts. In particular $\beta=\beta'=1$ occurs exactly at $A=1,2,4$, and $x'=1,1,5$ respectively. The analytic reduction excludes larger exponents over the full ordinary domain. [Exact certificate](adjacent_core_controls.json) · [Integer checker](check_adjacent_cores.py)

## A uniform first exponent bound

Assume $\beta,\beta'\le1000$. Kunrui Yu's rational Corollary 2 with $p=2$, $n=2$, $\alpha_1=3$, $\alpha_2=\beta$, $b_1=A$, $b_2=1$ gives
$$
     f < 10^{18}\log(4A).                                                   \tag{2}
$$
To check this coarse constant, take the ordered sizes $A_1=3$, $A_2=1000$. The exponent of the last rational is 1, so Yu's extra maximum uses $A_{n-1}=3$. The constant $273297\cdot36^2<4\cdot10^8$, the factor $3^8<10^4$, $2^2/(\log2)^4<64$, the product of the two logarithmic sizes is less than 14, and the last maximum is less than 20. The form $3^A\beta-1$ is nonzero and the corollary permits dependent rational bases. [Yu, *Linear forms in p-adic logarithms II*, Corollary 2, pp. 20–21](https://www.numdam.org/item/CM_1990__74_1_15_0.pdf)

Suppose $A\ge10^{40}$. Equation (2) gives $f<A/10$; this follows already at $10^{40}$ and $\log(4A)/A$ is decreasing. Since $2^f-1<3^A$, (1) implies $h'=v_3(2^f-1)<f$. Put $v=A-h'>0$, $k=f+s'$. From (1), $2^k\le3^A\beta+2^f-1<1001\cdot3^A$, whence $k<3A$. Thus
$$
   0<\Lambda=2^k3^{-v}(\beta'/\beta)-1
     =\frac{2^f-1}{3^A\beta}<\exp(-0.9A).                                \tag{3}
$$
Apply the real-field version of Matveev as stated by Bugeaud, Mignotte and Siksek in Theorem 9.4. The rational logarithmic heights of $2,3,\beta'/\beta$ are bounded by $1,2,7$. Drop the third term if the ratio is 1. With $D=1$, $n\le3$ and $B\le3A$, their constant $1.4\cdot30^{n+3}n^{4.5}\prod_j A_j$ is less than $10^{15}$. Hence $\log\Lambda>-10^{15}(1+\log(3A))>-0.1A$, contradicting (3). This proves $A<10^{40}$. [Bugeaud–Mignotte–Siksek, Theorem 9.4](https://samirsiksek.github.io/siksek.github.io/papers/fibannalsfinal.pdf)

## An exact binary reduction

For $H\ge3$, the order of $3$ modulo $2^H$ is $2^{H-2}$. The base case is $H=3$. The lift follows inductively from $v_2(3^{2^j}-1)=j+2$ for $j\ge1$ by factoring the difference of squares, whose new factor is 2 modulo 8 for $j\ge1$. The image consists of the units equal to 1 or 3 modulo 8. A target in the image has one exponent class modulo $2^{H-2}$. Starting with its exponent modulo 2, lift one bit at a time. At depth $j$ the two representatives $r$ and $r+2^{j-2}$ have different next bits. Exponent zero represents the positive minimum $2^{H-2}$ when the target is one.

There are 333 positive $\beta\le1000$ coprime to six. For each, compute the least positive solution of $3^A\equiv\beta^{-1}\pmod{2^{200}}$ when it exists. All 166 solvable residues have positive minimum exceeding $10^{40}$. Thus (2)'s $f$ is in fact $<200$ for the remaining $A$. Next, for each of the 333 values and $1\le f<200$ compute the least positive solution of
$$
           3^A\equiv(1-2^f)\beta^{-1}\pmod{2^{300}}.
$$
All 33,036 solvable residues again have positive minimum exceeding $10^{40}$. Therefore $k=f+s'<300$. The verifier also checks its lift against exhaustive enumeration at every modulus $2^j$, $3\le j\le11$, and checks every returned residue by direct modular powering.

If $A\ge200$, then $h'=v_3(2^f-1)<200$ because $2^f-1<3^A$. Now (1) yields
$$
             3^A\le3^A\beta< 2^{300}3^{200}\cdot1000<3^{510}.
$$
The alternative $A<200$ already satisfies this bound. The checker enumerates all $1\le A\le510$, computes $x'$ and its shifted cofactor exactly, and retains the 1,094 transitions with $\beta'\le1000$. For each it runs the physical trajectory from $x'$ to 1, and reconstructs and verifies the paths from every starting $x=2^s3^{A-s}\beta-1$ for $1\le s\le A$. Distinct triples $(s,h,\beta)$ give distinct starting integers by uniqueness of the valuations. The fact these starts also lie in the previously verified ordinary convergence range does not give the all-exponent classification used to find them.

## What happens at arbitrary cofactor bounds

For any finite collection of transitions, form the multiplicative group generated by all observed $\beta$ and $\beta'$ values, with rank $r$ in the positive rationals. In each transition (1), the vector
$$
          (3^A\beta,\ 2^f,\ -2^{f+s'}3^{h'}\beta')
$$
has coordinate sum 1. Its three proper two-term subsums are nonzero. Indeed cancellation of the first and last would force $2^f=1$, cancellation of the second and last would force $3^A\beta=1$, and the first two are positive. The three coordinates lie in a subgroup of $(\mathbb Q^*)^3$ of rank at most $(r+1)+1+(r+2)=2r+4$, since the sign is torsion. A collection of $M$ distinct positive crests gives $M$ distinct vectors. Evertse–Schlickewei–Schmidt's Theorem 1.1 gives
$$
        M\le\exp\bigl(18^9(2r+5)\bigr).                                 \tag{4}
$$
The rank counts only the prime-to-six parts of the shifted values at both ends. A nonperiodic positive trajectory has infinitely many complete ramps; each is finite by the initial $2$-valuation, and repeated crests give periodicity. Its shifted cofactors therefore generate an infinite-rank group. A trajectory confined to any fixed finite pool of primes in its shifted cofactors must be eventually periodic. Equation (4) alone does not exclude a nontrivial cycle. [Evertse–Schlickewei–Schmidt, Theorem 1.1](https://arxiv.org/abs/math/0409604)
