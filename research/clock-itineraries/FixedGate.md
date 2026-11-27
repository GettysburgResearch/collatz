# What a missing row detects at one fixed gate

Let `after n a` be the ordinary odd value reached from odd `a` after `n` odd gaps, and let `elapsed n a` count the intervening shortcut steps. Both functions are executable. The theorem `route_read` proves that every marked route with this source and depth has exactly these values. [Lean module](FixedGate.lean)

For an odd positive gate $a$ prime to three, write $n=b-m$, $q=\operatorname{after}(n,a)$, and $v=\operatorname{elapsed}(n,a)$. If $m\ge 2$ and $v+6m+7\le2b$, then

\[
           \operatorname{FullRow}(a,b,m)\quad\Longleftrightarrow\quad q>2 .
\]

Indeed the actual suffix supplies its clock and endpoint. Every prefix word has a completion at clock $2b-v$ by the free-mark theorem. Conversely the suffix of a full row has endpoint above two, and the ordinary dynamics determine that endpoint uniquely. This statement concerns one finite calculation on one fixed gate, including gates known to converge.

## A sharp uniform bound for the suffix clock

Every finite odd path from $a$ to $q>2$ of $n$ gaps and clock $v$ satisfies

\[
      \frac{2^{5v}q^5}{2^{8n}a^5}\le\frac{100000}{59049}.
\]

At an odd source $y\ge32$ the one-gap factor is $(3+1/y)^5/2^8\le1$. If the path ever uses an odd value below $32$, the rest lies on one of sixteen specific ordinary orbits. All sixteen reach one by odd depth $41$. Lean checks every earlier depth with endpoint above two. The maximal factor is attained on the path $9,7,11,17,13,5$, which takes nine shortcut steps. This proves the uniform bound and its optimal constant. [Theorems `distortion` and `distortion_sharp`](FixedGate.lean)

The constant is below two. For integers $H,Q$ with $a\le2^H$ and $2^Q\le q$, comparison of integer powers of two therefore gives $5v+5Q\le8n+5H$. With $2\le m\le b$ and $22m+5H+35\le2b+5Q$, one obtains the same pointwise full-row equivalence from endpoint heights alone.

In particular, put $m=\lfloor b/12\rfloor$. For every $b\ge30(\lfloor\log_2 a\rfloor+1)+210$, the row is missing if and only if the ordinary shortcut orbit is at one at the explicit time $\operatorname{elapsed}(b-m,a)$. Thus on the scale used in the universal criterion, missing a binary prefix is already an ordinary finite hitting certificate for the gate. Proving a row missing at every gate still requires an argument forcing an actual hit. [Theorem `missing_iff_hits`](FixedGate.lean)
