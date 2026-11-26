# Detecting the complete cycle denominator with primitive modular markers

**PROPOSED. Written theorem with finite Lean kernels.** Use the shortcut map $x\mapsto x/2$ on even departures and $(3x+1)/2$ on odd departures. A binary word of length $h>0$ and weight $p>0$ has lap matrix and positive rational fixed point
\[
 M=\begin{pmatrix}g&B\\0&d\end{pmatrix},\quad g=3^p,\quad d=2^h,\quad D=d-g>0,\quad x_*=B/D=r/q,
\]
with $r,q>0$, $\gcd(r,q)=1$. Cyclic rotations have the same positive reduced denominator $q\mid D$ and successive numerators $r_i$ obey $2r_{i+1}=3^{b_i}r_i+b_iq$. In particular $(q,6)=1$.

## Testing a marked rational phase

At an integer trace $t$ choose a determinant-one matrix $K=\left(\begin{smallmatrix}u&v\\w&t-u\end{smallmatrix}\right)$ with $w>0$. The condition $\operatorname{tr}(MK)=dt$ is precisely $D u=B w$. It requires the first column of $K$ to point in the direction of the finite fixed cusp. An integral determinant-one first column is primitive. Hence at this rational cut the only possible integral marker is
\[
 K_t(r,q)=\begin{pmatrix}r&-(r^2-tr+1)/q\\q&t-r\end{pmatrix}.                    \tag{1}
\]
Conversely (1) has determinant one, so an integral trace-$t$ marker exists **if and only if $q\mid r^2-tr+1$**. At $t=0$ this is an elliptic involution in the projective group and $MK$ also has trace zero. At $t=1$ the marker has projective order three. For any $q$ its canonical rational matrix in (1) has exact common denominator
\[
                    I_t(r,q)={q\over \gcd(q,r^2-tr+1)}.                       \tag{2}
\]
This denominator is for the displayed primitive first column. Arbitrary rescaling of the rational first column can change denominators. Only integral markers force the primitive normalization above.

At a single cut $\gcd(r^2+1,r^2-r+1)=1$ because the difference is $r$. Thus simultaneous integral trace-zero and trace-one markers exist precisely at an ordinary integer, $q=1$. There is also a same-trace test across two **actual** adjacent cuts. At an even departure $r_i=2r_{i+1}$. Any number dividing both $r_i^2+1$ and $r_{i+1}^2+1$ divides $3$ by subtraction of four times the second expression. Consequently $c_i=\gcd(q,r_i^2+1)$ and $c_{i+1}=\gcd(q,r_{i+1}^2+1)$ are coprime divisors of $q$, giving
\[
        \operatorname{lcm}(I_0(r_i,q),I_0(r_{i+1},q))=q,
        \qquad \max(I_0(r_i,q),I_0(r_{i+1},q))\ge\sqrt q.                \tag{3}
\]
In particular two integral trace-zero markers at these cuts are equivalent to an ordinary cycle for this word. Counting cyclic incidences in (3), at least $(h-p)/2$ distinct indexed cuts have primitive marker denominator at least $\sqrt q$. Distinct indexed cuts can represent the same phase on an imprimitive presentation. Every positive periodic word in the displayed range has at least one even departure since $2^h>3^p$.

Apply the same population and constants as the [complete-divisor theorem](../arithmetic/COMPLETE_DIVISORS.md). For all fixed-weight near-critical words outside its stated exceptional proportion, at least $(h-p)/2$ cuts have marker denominator at least $\sqrt D\exp(-h^{1-H+\epsilon}/2)$. This uses the actual complete reduced denominator. The conclusion is exponential in $h$ wherever $\log D\asymp h$. It does not exclude an exceptional primitive ordinary word with $I_0=1$ at all cuts.

## A finite modular return can be physically realized without integer closure

Write $T^x=\left(\begin{smallmatrix}1&x\\0&1\end{smallmatrix}\right)$. On every actual ordinary odd edge $x\to y$, $2^a y-3x=1$ gives
\[
  \begin{pmatrix}3&1\\0&2^a\end{pmatrix}
       =T^y\operatorname{diag}(3,2^a)T^{-x}.
\]
Hence translations at the two ends reduce every integral finite edge path to its clock diagonal. The marked translations at the two ends coincide on a cycle. Discarding that distinction by taking independent integral left and right frame changes also diagonalizes every open path.

In fact for **each** fixed congruence level $L\ge1$, choose an arbitrarily large even $a$ such that $2^a\equiv 1$ modulo the odd part of $L$. Then $D=2^a-3>1$ is coprime to $2^aL$. Taking arbitrarily large positive $x$ with $D x\equiv1\pmod {2^{a+1}L}$ gives
\[
              y=(3x+1)/2^a=x+(1-Dx)/2^a\equiv x\pmod {2L}.
\]
Here $x$ is odd, so $y$ is positive odd and the displayed clock is exact. In particular these are genuine edges with a closed marked cusp modulo $L$ and arbitrarily large ordinary ends. But the one-edge rational lap has center $1/D$, its trace-zero canonical marker has denominator $D$, and its unique positive real fixed point is nonintegral. A finite-level modular or Hecke argument identifying the two translations requires an additional input that distinguishes a fixed physical root from this family.

[EllipticMarkers.lean](EllipticMarkers.lean) checks the primitive-column theorem, the trace alignment, the integral existence equivalence, and the two polynomial divisor obstructions. The population bound and the realizable congruence controls are written deductions. A prohibition on simultaneous genuine integer closure at every rotation remains open.
