# Rechoosing the inverse center on a prescribed ternary cylinder

Use the positive shortcut map $T$. Write $j(m)=11+162m$,
$P(m)=2^{j(m)}$ and $M_m=P(m)-1$. An ordinary e6 parent satisfies
$81z+271=128P(m)$ and $T^7z=M_m$. The proofs below use ordinary positive
inverse branches throughout.

## A shrinking source inside every prescribed cylinder

For every $a,k,f\ge0$, put
$$
 d=k+5,\qquad p=18\left(\left\lfloor(f+4d+4)/9\right\rfloor+1\right).
$$
There exist $h\le4d$ and $0\le v<3^{p+3}$ such that, for every $i\ge0$ and
$$
              m=a+3^k v+3^{k+p+3}i ,
$$
one can take an ordinary $w>0$ with $w\equiv17\pmod{48}$,
$$
 T^{4+p+h}w=M_m,\qquad q_{4+p+h}(w)=2+p+d,\qquad 2^f w<M_m .
$$
Here $q_h$ is the number of odd inputs before clock $h$. The construction
chooses a new inverse word at $M_a$ for each requested cylinder. Both its
clock and its additional ternary precision admit upper bounds linear in
$k+f$. The conclusion supplies a full subprogression in every starting
cylinder. It leaves arbitrary individual members of the starting cylinder
undecided. The separately treated perfect-power parameters have a genuinely
pointwise quantifier. [Formal construction](AdelicSwitch.lean)
[Pointwise perfect-power theorem](PerfectPowerParents.lean)

Lyapunov Weaver previously gives the unit-preserving inverse gaps and
the subsequent block of consecutive odd inverses on a refined ternary
ball, in a construction for ranked source pairs at additive translates.
Here the exact ternary precision of the exponential parameter transfers
that construction to the supplied $M_m$. The extra terminal residue
produces $w\equiv17\pmod{48}$ at any prescribed saving, with the
displayed ordinary clocks, grades and least-parent consequence.
[Paper 179/v1, Appendix B.3](https://rstation.ai/problems/collatz/papers/179)

For $m\ge0$ and $t>0$, elementary lifting gives
$$
                 v_3(P(m+t)-P(m))=5+v_3(t).
$$
The coefficient of the next digit for a positive step $3^s$ is $2$ modulo
three after division by $3^{5+s}$. Thus each selected ternary cylinder
carries the complete set of remaining ternary digits after normalization.
[Formal metric identity](AdelicSwitch.lean)

At the ordinary input $M_a$, repeatedly choose an admissible inverse odd
step $(2^g y-1)/3$ that ends on another ternary unit. The gaps for unit
residues $1,2,4,5,7,8$ modulo nine are respectively $2,1,2,3,4,1$.
After $d$ such steps we have a positive $b$ with $T^h b=M_a$ and $h\le4d$.
For $m=a+3^kv$ write $P(m)=P(a)+3^dQ$. The same physical word lifts to
$b'=b+2^hQ$. As $v$ varies, $b'$ sweeps every ternary residue. Choose the
next $p+3$ digits so that $b'+1=3^pt$, with $t\equiv11\pmod{27}$.
The $p$ consecutive inverse odd branches then end at $2^pt-1\equiv10
\pmod{27}$, using $18\mid p$. The four-step identity
$T^4(48n+17)=27n+10$ supplies the required positive $w$.
The ordinary forward inequality $3^{q_H}w\le2^HT^Hw$ gives the strict
saving since $2^{f+4+p+h}<3^{2+p+d}$. For example, the elementary bound
$2^3<3^2$ suffices with the displayed $p$. Every lift preserves these
statements.

For $f=40$ the lower source precludes a least reverse defect at the supplied
parent. If $z$ were bad, $w$ would be bad. The established return bound gives
a reverse defect $y\le2^{40}w<M_m<z$. This comparison works without an
assumption on the basin of $3w$. [Formal least-parent consumer](AdelicParent.lean)
