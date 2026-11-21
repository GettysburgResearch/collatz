# A single class modulo 4096 suffices if every member passes

**Proposed theorem.** Let $f(n)$ denote the ordinary positive Collatz merger component, and let $P(n)$ mean $f(n)=f(3n)$. Each of the following assertions is equivalent to the full Collatz conjecture.

1. $P(n)$ holds for every odd multiple of $243$.
2. $P(n)$ holds for every positive $n\equiv1\pmod{4096}$.

This result requires every member of its indicated test family. The separate [modulo 64 theorem](ONE_CELL_SIXTY_FOUR.md) allows an arbitrary finite set of exceptions. A stabilized component label and an exact affine descent supply this proof.

## A label invariant under multiplication by 2 and 3

Assume the first assertion. For each $x$, define $F(x)$ to be the eventual value of $f(3^j x)$. This limit exists since $f(2n)=f(n)$ and every odd parameter divisible by $3^5$ passes $P$. In particular $F(2x)=F(3x)=F(x)$, and $f(3^j x)=F(x)$ for all $j\ge5$.

For every odd $u$ coprime to 3, $f(u)=F(u)$. To see this, choose arbitrarily large $a$ satisfying $2^a u\equiv1\pmod{3^6}$. Such exponents form one class modulo $2\cdot3^5$, since 2 generates the unit group modulo every power of 3. This also follows inductively from $v_3(2^{2\cdot3^j}-1)=j+1$. The odd preimage $z=(2^a u-1)/3$ passes $P$. With $g(x)=f(x-1)$, the ordinary identities therefore give $f(u)=f(z)=f(3z)=g(2^a u)=g(3^a u)$. On the indicated progression of exponents the binary residues of $3^a u$ run through its entire fixed class modulo 8 at every greater precision, since $v_2(3^{2\cdot3^5}-1)=3$. Choose the subclass of that residue modulo 8 in the [four adjacent ordinary-word certificates](ONE_CELL_SIXTY_FOUR.md#stabilizing-high-ternary-multiples). Then $g(3^a u)=f(3^a u)=F(u)$.

Consequently $F$ has the following additional equalities.

* For every odd ternary unit $w$, $F(3w+1)=F(w)$. Indeed $3w+1$ is a ternary unit after removal of powers of 2, so the ordinary step from $w$ gives the equality.
* For every odd $w$ and every $j\ge6$, $F(3^j w+1)=F(w)$. The odd input $3^{j-1}w$ has $f(3^{j-1}w)=F(w)$, and its ordinary step reaches $(3^jw+1)/2$, again a ternary unit after halvings.
* For $m\ge1$, put $z=2^m w-1$. If $v_3(z)=1$ or $v_3(z)\ge6$, then $F(z)=F(w)$. Write $z=3^j v$ with $3\nmid v$. The odd $v$ and $j$ satisfy one of the preceding two equalities, so $F(w)=F(2^m w)=F(3^jv+1)=F(v)=F(z)$.

## Finite affine descent

It suffices to prove $F(n)=F(1)$ on positive $n$ coprime to 6, since stripping powers of 2 and 3 preserves $F$. On a class $n=Mt+r$, $t\ge0$, track forms $a t+b$ with positive integral coefficients. Remove common factors 2 and 3 from $a,b$ whenever possible. Each removal preserves $F$ everywhere on the class. Two further moves are used.

1. If $a$ is even and $b$ odd, change the form to $3^j(at+b)+1$ for $6\le j\le10$. Also allow $j=1$ when $3\mid a$, $3\nmid b$.
2. For $1\le m\le12$, change the form to $2^m(at+b)-1$ if $9\mid a$ and $v_3(2^m b-1)=1$, or if $3^6$ divides both $a$ and $2^m b-1$.

The three equalities prove each move preserves $F$ for every $t\ge0$. The [integer verifier](check_stabilized_descent.py) starts at all unit classes modulo $162$. Whenever it reaches $a<M$, the endpoint $at+b$ is smaller than $Mt+r$ for every $t>(b-r)/(M-a)$. If no certificate is found in the bounded search it subdivides the class into its two binary lifts. Exhaustive verification terminates with 283 classes, largest modulus $41472$. Every positive parameter in those classes descends strictly except the single integer $1$. The search bounds affect only the effort to find a certificate: the final verification raises an error for any uncovered class. All affine coefficients and comparisons are exact integers.

Strong induction now gives $F(n)=F(1)$ on every positive integer. At a unit its original component label is $f(n)=F(n)$. Every positive integer enters a ternary unit by stripping powers of 2 and applying one odd step. Thus every positive integer belongs to the component of 1.

## Transport to one binary class

Write $J(t)=f(t+1)$. The ordinary identity $J(4t)=J(3t)$ and the equivalence of $P(1+16h)$ with $J(9h)=J(18h)$ give $P(1+16\cdot3h)\Longleftrightarrow P(1+16\cdot4h)$. A failure at $243u$, $u$ odd, forces a failure at $1+16\cdot81u$ or $1+32\cdot81u$ by the [two-successor identity](THREE_RAY_WINDOWS.md#when-three-divides-the-defect). Replacing the four factors of 3 by four factors of 4 gives respectively $1+4096u$ and $1+8192u$. Hence the binary assertion implies the ternary one. Full convergence directly gives both assertions.

## With finitely many exceptions

Suppose instead that only finitely many positive members of the binary test family fail. Transport by the same two successor maps then gives at most finitely many failed odd multiples of 243. The limit $F$ still exists everywhere, and the arbitrarily large CRT lifts still show $f(u)=F(u)$ at every ternary unit. The rule $F(3^j w+1)=F(w)$ for $j\ge6$ is now guaranteed when $3^{j-1}w$ exceeds the last exceptional parameter. The reverse move has the same eventual validity because the tested parameter is $(2^m w-1)/3$ in the high-valuation case. Each of the 283 certificates uses finitely many positive-slope forms in $t$. All required parameters therefore exceed that cutoff simultaneously for every sufficiently large $t$ in each class. Beyond one common threshold every core descends, so induction puts every $F$-value among those at a finite initial set of cores. Since each ordinary orbit enters a ternary unit with $f=F$, there are only finitely many ordinary merger components. This argument gives no bound of one on their number.
