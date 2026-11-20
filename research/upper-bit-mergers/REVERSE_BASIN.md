# A directed descent and the reverse basin implication

**Proposed theorem.** Let $T$ be the positive shortcut Collatz map and let $C$ be the set of starts whose ordinary forward orbit reaches 1. Each of the following conditions is equivalent to full Collatz convergence.

1. For every positive odd multiple $u$ of three, $3u\in C$ implies $u\in C$.
2. For every $k\ge0$, $32k+1\in C$ implies $16k+1\in C$.

The previously established [forward criterion](THREE_RAY_ONE_SIDED.md) states that either condition taken in the opposite direction is also sufficient. Thus either inclusion between the two sets of indices for $16k+1$ and $32k+1$ would settle the conjecture. Both inclusions remain open. The reverse criterion even suffices when required only for indices not divisible by four. The [Lean proof](ReverseBasin.lean) verifies the complete 26-leaf certificate, strong induction, the transfer to the restricted binary family, and the resulting equivalence for ordinary shortcut orbits.

The proof supplies a directed descent for every positive input. Allow ordinary edges $n\leftrightarrow T(n)$ and one extra move $u\to3u$ at positive odd multiples of three. In this graph, every $n>1$ has a path of at most **61** individual edges to a positive $n'\le9n/10$. Iteration reaches 1 in at most $61\lceil\log n/\log(10/9)\rceil$ edges. In particular any function invariant on ordinary orbits that is nondecreasing on these extra edges satisfies $f(n)\le f(1)$. The forward construction gives the other inequality, so every such ordered invariant is constant. These paths use the added directed edges and may traverse ordinary edges in reverse.

## The finite descent certificate

An even $n$ takes one ordinary step to $n/2$. For odd $n=Mt+r$ the [certificate and verifier](check_reverse_basin.py) give 26 disjoint progressions that together contain every positive odd integer. Each row includes a word in the following moves.

* $S_h(v)=(3v+1)/2^h$ from an odd $v$ with $2^h\mid 3v+1$ follows $h$ ordinary steps.
* $I_h(v)=(2^hv-1)/3$ when this is a positive odd integer traverses $h$ ordinary steps in reverse. In the forward direction $I_h(v)$ first steps to $2^{h-1}v$, which halves to $v$.
* $M(v)=3v$ is allowed only when $v\equiv3\pmod6$, and is always followed forward.

Here each $h\ge1$. For instance, $n=24t+15$ has word $M S_3 I_1$. Its intermediate values are $72t+45$, $27t+17$, and $18t+11$. Each move holds for all $t\ge0$ and the endpoint is below $9n/10$.

For each word the verifier propagates the integer coefficients of the form $at+b$. Divisibility conditions must hold on both coefficients. Every $S_h$ has an even slope and odd offset at its input, every $I_h$ has those parities at its output, and every $M$ has slope divisible by six and offset congruent to three modulo six. Positivity holds throughout. The 26 starting residues partition all 7,776 odd classes modulo their least common multiple 15,552. The words contain 444 expanded moves, including 36 forward triplings, and the longest contains 61 moves. For an endpoint $at+b$, the verifier checks $10a\le9M$ and $10(at_0+b)\le9(Mt_0+r)$ at the first admissible $t_0$ with $Mt_0+r>1$. By linearity the contraction holds for every later $t$. The only omitted input is 1 itself, where the empty path already ends at 1. This proves the directed descent.

## Why convergence propagates back along the constructed path

Membership in $C$ is preserved in both directions on ordinary edges. Under condition 1 it also propagates backwards on every allowed tripling. Starting at the terminal vertex 1 and reading the descent path backwards therefore puts $n$ in $C$.

To see that condition 2 suffices, the substitution used for the forward criterion can be read in either orientation. We give the details. Write $a\sim b$ when their ordinary orbits meet, and $J(t)=t+1$. Always $J(4t)\sim J(3t)$ by two ordinary steps. Also $3(16t+1)\sim J(18t)\sim J(32t)$, using two such exchanges for the second equivalence. For the first, four steps from $3(16t+1)$ and one step from $18t+1$ both reach $27t+2$. Consequently a forward move $16t+1\to32t+1$ links, with ordinary edges on either side, $J(9t)$ to $J(18t)$. Repeat at $2t$ and use $J(36t)\sim J(27t)$. For odd $t$, the starting vertex $3t$ shares an ordinary orbit with $J(9t)$ and $9t$ shares one with $J(27t)$. This replaces each forward tripling $3t\to9t$ in the descent by a path whose two extra edges are $16s+1\to32s+1$ for $s=t,2t$. Since $t$ is odd, neither index is divisible by four. Condition 2 propagates membership backwards along the replacement, giving condition 1. Full convergence implies both conditions immediately.
