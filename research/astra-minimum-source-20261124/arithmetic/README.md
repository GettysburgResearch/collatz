# The least bad odd multiple of three

**PROPOSED. The universal transfer remains OPEN.** Use the ordinary shortcut map $T(2j)=j$, $T(2j+1)=3j+2$ on positive integers. Write $C$ for the basin of 1 and $x\sim y$ if their forward orbits meet. Each directed comparison below asks whether $v\in C$ implies $3v\in C$ for a positive odd $v$, allowing multiples of three. The earlier odd-*unit* criteria, in either direction, and their explicit finite tables are at [PR195, round seven](https://github.com/GettysburgResearch/collatz/blob/0e8a7f9f965416189b30b57b8aa818fbcb7757c7/research/astra-global-closure-20261124/round7/head/README.md). The following reduction stands on the elementary identities in its table. We make no priority claim for the general odd-tripling criterion.

## A smaller representative with a smaller comparison

For every integer $n>1$, the following cases give $0<z<n$. A query is needed in three cases. Its source is $z$, always odd, and satisfies $9z\le 8n+1$.

| Input | Smaller $z$ | Ordinary identity | Extra comparison |
|---|---:|---|---|
| Even $n$ | $n/2$ | $T(n)=z$ | None |
| Odd $n$ divisible by 3 | $n/3$ | $3z=n$ | $z\to3z$ |
| Odd $n=2\bmod3$ | $(2n-1)/3$ | $T(z)=n$ | None |
| Odd $n=4\bmod9$ | $(8n-5)/9$ | $T^3(z)=n$ through $(4n-1)/3,2n$ | None |
| Odd $n=7\bmod9$ | $(4n-1)/9$ | $T^2(3z)=n$ through $2n$ | $z\to3z$ |
| Odd $n=1\bmod9$ | $(8n+1)/9$ | $T^4(3z)=T(n)$ through $4n+1,6n+2,3n+1$ | $z\to3z$ |

The remaining odd residues modulo 9 after removing $0\bmod3$ and $2\bmod3$ are $1,4,7$. Substitution verifies positivity, parity and each physical edge. Thus a directed implication on all positive odd inputs proves universal convergence by strong induction on $n$. Conversely universal convergence gives the implication. In particular a failure of Collatz guarantees an odd discordance without using an analytic theorem.

Let $q$ be the **least positive odd integer of either label orientation** for which $q$ and $3q$ have different basin membership. Every positive odd $v<q$ has equal labels on $v,3v$. By the table and strong induction,

$$
  0<n\le q\ \Longrightarrow\ n\in C,\qquad
  8n+1<9q\ \Longrightarrow\ n\in C\quad(n>0).
$$

In the first induction $v< n$ ensures the comparison is available even for $n=q$. In the second its bound $9v\le8n+1<9q$ suffices. Hence $q$ is good and $3q$ is bad. Every smaller odd multiple of three has the form $3v$ with $v<q$ good and $v,3v$ equally labeled, so $3q$ is the **least bad odd multiple of three**. A smaller even bad multiple would halve to a smaller odd bad multiple, so $3q$ is also the least bad multiple of three without a parity qualifier. For $N$ the least positive integer outside $C$, this gives

$$
                   (9q-1)/8\le N\le3q,
                   \qquad q<N.
$$

The strict cutoff permits equality $8N+1=9q$. One may obtain $9q\le8N+1$ directly by applying the table at $N$. Its smaller $z$ is good, so a comparison occurs, $3z$ is bad, and $q\le z$. These inequalities apply to the minimum over **all odd $q$**. They give no bound on the size of a smallest ternary-unit witness relative to this new minimum. The table and the two finite-induction statements for any orbit-invariant label are kernel-checked in [SourceDeletion.lean](SourceDeletion.lean).

## Source changes in the two original components

If $q=8k+7$, then $T^3(3q)=9k+8=T(6k+5)$ and $6k+5<q$. Since the entire interval through $q$ is good, this eliminates the complete class, including arbitrary lengths of its initial odd run on the $q$ arm.

A second reduction exchanges the original two components. Put $q=3007+4374t$, $x=2815+4096t$ for any $t\ge0$. Then

$$
 T^{12}(x)=13532+19683t=T(3q),\qquad
 T^{12}(3x)=4511+6561t=T(q).
$$

The clock-12 words of 2815 and 8445 have nine and seven odd inputs respectively. A high-bit lift by $2^{12}t$ adds $3^9t$ to the first endpoint; the lift on the second arm has high quotient $3t$. Both equalities therefore hold for every lift. Here $x$ is positive, odd and strictly below $q$. Any original discordance supplies a smaller discordance with exchanged labels. The unrestricted odd minimum admits every $t$. If one instead requires an odd ternary unit, the replacement is a unit exactly when $t\ne2\bmod3$. The module checks both identities on the entire progression.

## Ternary digit deletion with a fixed source budget

For an odd $n>1$ with $n=1\bmod9$, set $F(n)=(8n+1)/9$. The last table row gives $n\sim3F(n)$. Two applications beginning at $n=1+486k$ with $k>0$ require comparisons at $1+432k$ and $1+384k$. Both are strictly smaller odd ternary units. Six physical steps at the second value give

$$
   T^6(1+384k)=1+162k=1+(n-1)/3.
$$

Indeed it agrees with the parity word of 1 through six steps, with high quotient $6k$ and three odd inputs. Thus any invariant label admitting those two comparisons has the same value at $n$ and $1+(n-1)/3$. It can delete successive ternary digits at a fixed comparison ceiling as long as the current odd input remains $1\bmod243$. For $n=1\bmod 3^K$, $K\ge4$, this gives at least $K-4$ deletions. The proof retains its validity even under the narrower unit-only premise. It is the theorem `delete_digit`. This construction also shows why agreement of a proposed source with 1 to high ternary precision can be used numerically independently of its free high binary digits. An application to one arm still needs a route from the other arm.

## A restriction on every clock of the minimum bad triple

Let $x_0=3q$ and let $x_j$ be its successive odd Syracuse values, writing $3x_{j-1}+1=2^{a_j}x_j$ with $a_j\ge1$. Then

$$
                             a_j\le 2\cdot3^j\quad (j\ge1).
$$

If $a_j>L=2\cdot3^j$, replace this exponent by $a_j-L$ and reconstruct backwards from the **same** $x_j$, using the same earlier $a_i$. Since $2^L\equiv1\bmod 3^{j+1}$, the first changed predecessor is integral and congruent to $x_{j-1}$ modulo $3^j$. Each earlier inverse operation $(2^{a_i}y-1)/3$ costs one ternary digit, leaving the new starting vertex congruent to $x_0$ modulo 3. Every intermediate value is positive and odd: before division its numerator is a positive multiple of three, and it is odd. The changed predecessor is strictly smaller, and the earlier inverse operations preserve strict order. This produces a smaller positive odd multiple of three in the very same bad component, contradicting minimality. Euler's theorem for $3^{j+1}$ supplies the stated exponent. The exponent replacement constructs a different actual integer in the same component when its guard is satisfied. A stronger numerical bound follows directly from the established floor. Put $L=\max(q+1,\lceil(9q-1)/8\rceil)$ and $S_j=\sum_{i=1}^j a_i$. The exact odd-step product gives

$$
    2^{S_j}=\frac{3q}{x_j}\prod_{i=0}^{j-1}(3+1/x_i)
      \le (3q/L)(3+1/L)^j.
$$

In particular $a_j\le 1+\log_2(3q/L)+j\log_2((3+1/L)/2)$ since each of the other $j-1$ exponents is at least one. On a prefix with $x_0,\ldots,x_{j-1}$ pairwise distinct, their ordered values are at least $L,L+2,\ldots,L+2(j-1)$. Using $1+t\le e^t$ and an integral comparison bounds the product by $3^j e^{1/(3L)}(1+2j/L)^{1/6}$. These growth bounds hold along the supplied fixed ordinary trajectory and allow an infinite orbit.

More generally, on any actual odd branch revisit the same odd target by a positive odd multiple of three below $3q$, or reach the established good interval, and that minimum witness is discharged. The argument above gives neither conclusion at every remaining source. In particular an upper orbit with only modest stripping exponents need never activate the exponent replacement. The earlier canonical $B$ and its directed 291-leaf table remain separate [previous branch and review](../../astra-closing-step-20261124/descent/README.md).
