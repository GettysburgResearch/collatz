# Unit gaps on balanced rows grow faster than logarithmically

**PROPOSED written theorem.** Fix $\epsilon>0$. In any sequence of ordinary odd paths with $b\to\infty$, total shortcut clock $2b$, terminal $q>1$ and relative affine carry at least $\epsilon$, the number $h$ of gaps of length one satisfies

\[
                       h/\log b\longrightarrow\infty .
\]

The elementary integer bound in [SparseClock.lean](SparseClock.lean) gives a logarithmic lower bound. The stronger limit here uses Evertse's Corollary 1 for a bounded number of summands at a time. Its constants need not be effective. The conclusion includes paths with repeated states.

## A bound for a segment with a fixed number of exceptions

Call a gap exceptional when its length differs from two. Fix an integer $R\ge1$ and $\eta>0$. Consider any segment of $n$ odd steps ending at $q>1$, with at most $R$ exceptional gaps of total length $E$. Its clock $S$ can be arbitrary. Then

\[
       n\le(1+\eta)\log_3 q + C_{R,\eta}(E+1).                 \tag{2}
\]

All states $x_0,\ldots,x_n=q$ exceed one because the odd map fixes one. Write $w_i=x_i-1$, let $e_i$ be the gap starting at $x_i$, $A_i=\sum_{j<i}e_j$, and $c_i=2^{e_i}-4$. With $D=\{i:e_i\ne2\}$ the shifted gap equations telescope to

\[
    U=V+\sum_{i\in D} B_i,\qquad U=3^n w_0,\quad V=2^S w_n,
    \quad B_i=2^{A_i}3^{n-1-i}c_i .                         \tag{3}
\]

Every proper nonempty subsum of (3), brought to one side, is nonzero. For an exceptional gap, the two-adic valuation of $c_i$ is one if $e_i=1$ and two if $e_i\ge3$. Thus $v_2(B_i)=A_i+\min(e_i,2)\le A_{i+1}$. Every later exceptional term has valuation strictly greater than $A_{i+1}$. The valuation of $V$ is at least $S+1$, since $q>1$ is odd. In any nonempty subset of the right-hand terms, the least valuation occurs exactly once. Its sum is nonzero. A proper zero subsum containing $U$ would have a nonempty complementary zero subsum among the right-hand terms.

If $D$ is empty, $3^n\mid w_n$, giving (2) immediately. Otherwise put $i_-=\min D$, $i_+=\max D$, $P=A_{i_-}$ and $J=n-1-i_+$.

All terms other than $U$ are divisible by $2^P$, so $2^P\mid w_0$. All terms other than $V$ are divisible by $3^J$, so $3^J\mid w_n$. Divide all terms by $2^P3^J$. Write $z=w_0/2^P$, $v=w_n/3^J$ and $X=3^{n-J}z$. The first internal term is now $3^{i_+-i_-}c_{i_-}$, and the last is $2^{A_{i_+}-P}c_{i_+}$. Their common divisor with all other terms, $g$, is at most $|c_{i_-}c_{i_+}|\le 2^{2E}$. In fact the part of $g$ prime to three divides $|c_{i_-}|$ and its three-part divides $|c_{i_+}|$. The argument also applies when these indices coincide.

For a nonzero integer $t$, let $|t|_*$ be its positive part prime to six. Evertse's Corollary 1 over the rationals, with primes $\{2,3\}$, implies for each fixed arity and each $0<\delta<1$ that the product of the $|t|_*$ of a primitive nondegenerate zero sum is at least a positive constant times its maximum absolute term to the power $1-\delta$. Absorb the finitely many exceptions into the constant. There are at most $R+2$ terms here. Apply the result after division by $g$. The maximum absolute term is at least $X/g$. The product of the prime-to-six parts is at most $zv\prod_{i\in D}|c_i|\le zv2^E$ because division by $g$ can only decrease those parts. Consequently

\[
   3^{n-J}=X/z\le C_{R,\delta} X^\delta v\,2^{3E},
   \qquad 3^n\le C_{R,\delta} X^\delta w_n\,2^{3E}.           \tag{4}
\]

Finally $3w_i/(2^{e_i}w_{i+1})=1+c_i/(2^{e_i}w_{i+1})$ equals one on neutral gaps and is at most two on every other gap. Multiplying gives $X\le U\le2^R V$, and $S\le2n+E$. Taking logarithms of (4) gives
$(\log 3-2\delta\log 2)n\le(1+\delta)\log q+O_{R,\delta}(E+1)$.
Choose $\delta$ sufficiently small in terms of $\eta$ to get (2). This use of the subspace theorem requires both the primitive normalization and the no-proper-subsum argument. [Evertse, *On sums of S-units and linear recurrences*, Corollary 1, printed p. 227](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

## Grouping the exceptions

Use (2) with $\eta=1$. The inverse size inequality gives $x_0\le(4/3)^n 2^E q$ by multiplying the inverse gap slopes. In base-three logarithmic height, one segment therefore takes $L=\log_3 q$ to at most $K L+C_R(E+1)$ with the **same** $K=1+2\log_3(4/3)>1$ for every fixed $R$.

Split a whole balanced path with $d$ exceptions into at most $t=\lfloor d/R\rfloor+1$ consecutive segments, each with at most $R$ exceptions. Their exceptional clocks sum to $2d$. Read them in reverse order. At segment $j$, counting from zero, the starting logarithmic height is at most $K^j(\log_3 q+C_R(2d+t))$. Apply (2) separately to each segment and sum the geometric progression. This yields

\[
 b\le C'_R K^{\lfloor d/R\rfloor+1}(\log_3 q+2d+t+1).
\]

Balance gives $d\le 2h$, and the relative-carry upper bound gives $q\le 2(3/2)^h/\epsilon$. Hence $\log b\le (2h/R+1)\log K+O_{R,\epsilon}(\log(h+2))$. First this forces $h\to\infty$. Then $\limsup(\log b)/h\le 2\log K/R$ for every fixed $R$. Letting $R$ grow proves the stated limit. No uniformity in Evertse's constants as $R$ varies is used.

The argument controls the whole path. In fact the fixed gate $a$ in `rows_of_failure` already forces linearly many unit gaps in the common suffix. Let the suffix have $n$ gaps, clock $v$, and $h_s$ unit gaps. Each other gap costs at least two, so $2n-h_s\le v$. On a nonconverging ray, $5v\le8n+5a$ by the clock bound. Consequently $5h_s+5a\ge2n$. At fixed $a$ and $n=b-\lfloor b/12\rfloor$, the common suffix satisfies the proposed whole-path obstruction by itself. Any missing-word proof using this strategy must constrain which units can occur jointly with the prescribed prefix. [Formal suffix bound](SparseClock.lean)
