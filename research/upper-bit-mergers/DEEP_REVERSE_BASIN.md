# Reverse closure at odd multiples of nine suffices

**PROPOSED.** Let $C$ be the positive integers that reach 1 under the ordinary shortcut map. Each statement below is equivalent to full Collatz convergence.

1. For every positive odd multiple $z$ of 9, $3z\in C$ implies $z\in C$.
2. For every positive $k$ with $4\nmid k$, $128k+1\in C$ implies $64k+1\in C$.

Equivalently, it suffices to prove that $128k+1\in C$ implies $128k+2\in C$ at those same indices, since $128k+2$ halves to $64k+1$. The implications themselves remain open. The proof gives a bounded directed path for every class of integers prime to six. [Exact certificates and verifier](check_deep_reverse_basin.py)

Lean independently checks the affine moves, the strict decrease and the residue cover, then proves the equivalence for the ordinary shortcut map as `collatz_iff_deep_reverse_binary`. The Python verifier also checks the contraction and path lengths below. [Lean proof](ReverseBasin.lean)

## Descent on ternary units

Use a directed graph on positive integers. An ordinary pair $n,T(n)$ can be traversed in either direction. The extra arrows $z\to3z$ are available precisely at odd multiples of nine. Every vertex has a directed path **to** 1. To prove this, first consider an odd ternary unit $n>1$. The verifier gives a directed path of at most 198 edges from $n$ to a positive ternary unit at most $24n/25$. An even ternary unit simply halves to a smaller ternary unit. Strong induction therefore gives the path to 1 for every ternary unit. A multiple of three reaches a ternary unit by stripping factors of two and taking an odd ordinary step, since $3w+1$ is prime to three. This covers every positive start.

Each of the 71 certificates starts with a class $n=mt+r$, $t\ge0$, and tracks an integer affine expression $at+b$. A symbol $S_h$ sends it to $(3(at+b)+1)/2^h$ when every input is odd and the division is always integral; this gives an odd step and $h-1$ halvings. A symbol $I_h$ sends it to $(2^h(at+b)-1)/3$ when the quotient is an odd integer. The new value reaches the old one in $h$ native steps. The symbol $M$ triples the current value and requires $a\equiv0\pmod{18}$ and $b\equiv9\pmod{18}$. Thus every $M$ is traversed forward from an eligible source. The verifier checks all parities, divisions and positivity throughout every word.

The certificate classes cover all 20,736 residues prime to 6 modulo 62,208, with overlaps allowed. Each endpoint has $3\mid a$ and $3\nmid b$. The inequality $25(at+b)\le24(mt+r)$ is verified at the slope and at the smallest $t$ for which $mt+r>1$. These endpoint checks establish the claimed contraction throughout each infinite progression. The 71 paths contain 3,974 expanded moves, including 284 instances of $M$.

Now assume statement 1. Membership in $C$ propagates **backwards** along each directed path: ordinary edges preserve the component and at an extra arrow this is exactly the hypothesis. Starting at its endpoint 1 proves membership for every initial vertex. Thus statement 1 suffices for full convergence.

## The direction of the binary implication

Write $a\sim b$ for ordinary merger and $J(v)=v+1$. Two native steps give $J(4v)\sim J(3v)$. For $z=9h$ with $h$ odd, the odd ordinary step on either arm gives

$$
 z\sim J(27h),\qquad 3z\sim J(81h).
$$

A forward arrow $64k+1\to128k+1$ connects $J(27k)$ to $J(54k)$, in that order: three applications of $J(3v)\sim J(4v)$ give $J(27k)\sim J(64k)$ and $J(54k)\sim J(128k)$. Use the arrow first at $k=h$, then at $k=2h$. They give a directed path

$$
 z\sim J(27h)\leadsto J(54h)\leadsto J(108h)\sim J(81h)\sim3z.
$$

Its two indices are odd and twice odd, respectively. Consequently statement 2 propagates membership backwards from $3z$ to $z$, proving statement 1. Full convergence gives both statements immediately. The reduction uses the specified orientation at every comparison. [Earlier forward and reverse tripling criteria](THREE_RAY_ONE_SIDED.md)

## What the first nonempty rank would settle

For $k>0$ the smallest possible number of odd inputs on a path from the antecedent $y=128k+1$ to its first arrival at 1 is four. The implication in statement 2 restricted to that rank is equivalent to

$$
                       3^{27j}+1\in C\qquad\text{for every }j\ge1.
$$

Indeed three successive odd-even pairs take $y$ to $54k+1>1$, using $T^2(4v+1)=3v+1$ each time. Exactly one further odd input suffices precisely when $162k+4=2^h$. This gives $k=2(2^{h-2}-1)/81$. The order of $2$ modulo $81$ is $54$ since $2^9\equiv26$ and $2^{27}\equiv-1\pmod{81}$, and $2^{18}\not\equiv1\pmod{81}$. Thus $h-2=54j$ for $j\ge1$, and all such $k$ are twice odd as required.

The same three odd-even pairs from $x=64k+1$ reach $27k+1=(2^{54j+1}+1)/3$. Its next odd step gives $2^{54j}+1$. During another $54j$ clocks this input follows the parities of the cycle $1,2$. At clock $i$ in that segment its exact value is $T^i(1)+2^{54j-i}3^{\lceil i/2\rceil}$, so it stays above 1 and ends at $3^{27j}+1$. Consequently $x$ belongs to $C$ precisely when this shifted power does. Its path already uses $27j+4$ odd inputs by that checkpoint.

One more ordinary step identifies the question with convergence of the pure powers $3^{27j-1}$ for every $j\ge1$. Indeed the even start $3^{27j}+1$ and the odd start $3^{27j-1}$ both step to $(3^{27j}+1)/2$. The Lean theorem `deep_rank_four_shifted_power` constructs the index for every $j\ge1$ and verifies both ordinary paths through the specified checkpoints. [Lean source](HighBit.lean)

These pure powers have unbounded time to first descent. For any $H\ge3$ prescribe the first three parities odd, odd, even, then $H-3$ odd parities. The parity-word bijection gives one residue modulo $2^H$, necessarily $3\bmod8$. Powers of three attain every such residue: $3^2=9$ generates the residues $1\bmod8$ modulo $2^H$, since $v_2(9^{2^s}-1)=s+3$ by successive squaring. The exponents $27j-1$ cover every class modulo the power-of-two order of three. Infinitely many of the required pure powers therefore follow the word. Its first three steps send $n$ to $(9n+5)/8>n$, its first two increase, and every later prescribed step increases. A fixed forward deadline cannot give descent on this four-odd-input subproblem.

## Five odd steps can reach any prescribed odd target coprime to three

Write $U(v)$ for the odd part of $3v+1$ at odd $v$. For every positive odd $t$ coprime to three there are infinitely many eligible indices $M$ for which
$$ U^5(128M+1)=U^5(64M+1)=t. $$
Choose any sufficiently large $a$ with $2^{a+3}t\equiv14\pmod{243}$, and put $M=(2^{a+3}t-14)/243$. Such exponents form one class modulo 162 because 2 generates the units modulo 243. Reduction modulo 16 gives $M\equiv6\pmod{16}$. On this class the first three odd steps from the two starts reach $54M+1$ and $27M+1$. Their next odd steps reach $u=(81M+2)/8$ and $4u+1$, respectively. Substitution gives $3u+1=2^a t$ and $3(4u+1)+1=2^{a+2}t$, proving the claim. Every earlier odd vertex exceeds $t$ for sufficiently large $a$, so this is the first visit to $t$ on each path. The five-step merger and the special case $t=1$ occur in the two follow-ups. [Merger W512-030](https://github.com/GettysburgResearch/collatz/blob/85aad425a3bc714e27b1b8cb7e299f85c7025a05/research/witness-closure-512-2026-11-20/README.md) · [Rank-five parameterization K3](https://github.com/GettysburgResearch/collatz/blob/051237135a34ae7d4b973ee5fcf5da04ded6f0fc/research/deep-reverse-closure-20261120/REVERSE_CERTIFICATE_KERNEL.md)

Five is the least uniform bound for first visits on both arms. For target 1 the rank-four calculation above forces the other arm to use at least $27j+4$ odd inputs, and the antecedent always uses at least four. The construction gives pairs in every ordinary orbit component: any positive start can be halved to an odd value, whose next odd iterate is coprime to three. It leaves open the transfer at an arbitrary prescribed index $M$.
