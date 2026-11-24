# Marked predecessors with a forced large descent

**Status.** This is a written result for the ordinary shortcut map. It gives a global reduction and leaves universal convergence open. The formal scope is stated at the end.

Let $T$ halve an even integer and send an odd integer to $(3n+1)/2$. For $d=\lfloor\log_2 n\rfloor$, call an odd $n$ marked when $(d+1)(n-2^d)\le 70\,2^d$, using the section of PR 173. Define

$$S=\{n\text{ marked}:5v_2(3n+1)\ge d+1\}.$$

**Theorem.** For every positive integer $q$ with $3\nmid q$, arbitrarily large elements $n$ of $S$ hit that same $q$. Each $n$ has an explicitly constructed prefix of $e\ge (d+1)/5$ shortcut clocks, consisting of one odd step followed by $e-1$ halvings. Its endpoint is at most $4n^{4/5}$. Consequently every positive integer reaches one if and only if every member of $S$ reaches one. In an octave $[2^d,2^{d+1})$, the number of candidates in $S$ is at most $1+70\,2^{d-\lceil(d+1)/5\rceil}/(d+1)$. This counts candidate sources, not components or missing trajectories.

### Constructing the predecessor

The source dependency is `lift_spec` in [PR 173, ShellCover.lean](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ShellCover.lean). Write $L^s$ for its ordinary four-clock inverse lift and $G=16/3$. For every positive ternary unit $w$ one has

$$T^{4s}L^s(w)=w,\qquad 3\nmid L^s(w),\qquad G^s(w-1)+1\le L^s(w)\le G^s w.$$

Put $\alpha=\log_2 3$. Choose arbitrarily large coprime pairs $a,Q$ with $|Q\alpha-a|\le 1/Q$, using the convergents of the irrational $\alpha$. Equivalently, use `rotation_grid` from [PR 173, ForwardSection.lean](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ForwardSection.lean). Its bound $N+1\le 4^Q$ guarantees arbitrarily large denominators. Take $Q\ge 10$ large enough that $q\le(3/2)^Q$. Set $K=2^Q$ and $u_s=L^s(Kq)$ for $0\le s\le Q$. Since $u_s$ is a ternary unit, exactly one $e_s\in\{Q,Q+1\}$ makes $2^{e_s}u_s\equiv1\pmod 3$. Define

$$x_s=(2^{e_s}u_s-1)/3,\qquad M_s=2^{e_s}G^s Kq/3.$$

The numerator defining $x_s$ is odd, so $x_s$ is a positive odd integer. The equation $3x_s+1=2^{e_s}u_s$ gives the stated physical prefix. Following it by $4s$ inverse-lift clocks and $Q$ halvings reaches $q$.

We need a mark at one of these sources. The inverse-lift bounds give $0\le M_s-x_s\le(2^{e_s}G^s+1)/3\le 2 M_s/K$. In particular $x_s/M_s\ge 1-2/K$. Since $\log 2\ge1/2$, $\log t\le t-1$ for $t>0$, and $K-2\ge4Q$, it follows that

$$0\le\log_2 M_s-\log_2 x_s\le 4/(K-2)\le1/Q.$$

Also $x_s\le M_s\le (2/3)\,2^{2Q}(16/3)^Q q\le(2/3)2^{5Q}$. Hence $\lfloor\log_2 x_s\rfloor+1\le5Q$. The lower bound for the inverse lift gives $x_s\ge (K^2-1)/3$, uniformly in $s$.

### A one-sided rotation hit

Set $b=\log_2 q-\alpha$. The model phase is $\log_2 M_s=b-s\alpha+E_s$ for the integer $E_s=Q+e_s+4s$. For any real $y$, the fractions $ja/Q$ modulo one are a permuted $Q$-point grid. Thus there are $0\le j<Q$ and $z\in\mathbb Z$ for which $1/Q\le y+j a/Q-z\le2/Q$. Apply this to $y=b-Q\alpha-2/Q$ and put $s=Q-j$. As $|j(\alpha-a/Q)|\le 1/Q$, the quantity $b-s\alpha-z$ lies between $2/Q$ and $5/Q$. The error between $\log_2 x_s$ and the model phase is at most $1/Q$, so

$$0\le\log_2 x_s-(z+E_s)\le6/Q.$$

Its product with $\lfloor\log_2 x_s\rfloor+1$ is at most 30. The established theorem `section_of_phase` admits products up to 35, so $x_s$ is marked. The uniform lower bound on the row makes these marks arbitrarily large as $Q$ increases.

### Descent, counting and the remaining obstruction

For $n=x_s$, the inequalities $e_s\ge Q\ge(d+1)/5$ and $n<2^{d+1}$ give $u_s=(3n+1)/2^{e_s}\le 4n^{4/5}$. At each octave the condition on $v_2(3n+1)$ picks one residue modulo $2^{\lceil(d+1)/5\rceil}$. Counting that class in the interval of width $70\,2^d/(d+1)$ proves the asserted bound. Universal convergence follows from convergence on $S$ because every ternary-unit target has a representative there. A positive multiple of three enters the unit domain after removing its initial powers of two and taking its next odd step.

The constructed descent leads to $u_s=L^s(2^Qq)\ge 2^Q q$. Its endpoint therefore remains above the original target $q$, even when the drop at $n$ removes a fixed fraction of its binary digits. To contradict the least nonconvergent target, a certificate must continue to a value below that target, or establish a merger with a smaller convergent component. Neither the sparse count nor the long forced prefix supplies that inequality.

### The exponent barrier for a smaller representative

An inverse strategy might try to start at the postdescent target $q$ and find an element of $S$ in its component with size $O(q^{5/4-\varepsilon})$. Applied to the first drop of $n\in S$, such a bound would give a new member of $S$ strictly below $n$ for all sufficiently large $n$. Convergence would then follow by strong induction once the finite base cases were settled.

The difficulty persists for any choice of the rotation parameter or the amount of initial doubling. Whenever an inverse construction gives $3x+1=2^e u$, $5e\ge \lfloor\log_2x\rfloor+1$, and $u\ge q$, one has

$$q^5\le u^5\le4^5 x^4,\qquad x\ge(q/4)^{5/4}.$$

This rules out the proposed power saving across unbounded targets for every construction with these three properties. On the rows used above the stronger lower bound $x\ge (2^Q q/4)^{5/4}$ follows. Taking all extra halvings does not rescue this specific construction on odd targets. For $s\ge1$, `inv4` has residues $4,8,4,10,5,8$ modulo 16 on its six unit branches, so $v_2(u_s)\le3$. The first actual odd endpoint is at least $2^{Q-3}q$. For $s=0$ it is exactly $q$ when $q$ is odd.

The exponent $5/4$ can actually occur in ordinary marked one-step inverse families. For $m\ge2$, let $e=m+1$ and choose $1\le r<2^{e+1}$ with $3r+1\equiv2^e\pmod {2^{e+1}}$. Then $x=2^{5m}+r$ has $d=5m$ and $v_2(3x+1)=e$. It is marked because $r<2^{m+2}$ and $(5m+1)2^{m+2}\le70\,2^{5m}$. The exact odd endpoint $q=(3x+1)/2^e$ has size $q\sim(3/2)2^{4m}$ while $x\sim2^{5m}$. Thus $x/q^{5/4}\to(2/3)^{5/4}$. A subcritical selector would have to exploit a different feature of the component, such as an actual ascent from an endpoint smaller than its target. The inverse construction and octave counts give no such ascent for every fixed target.

### An independently prescribable odd suffix

A variant gives a mark in every fixed odd residue $r\pmod {2^k}$, with $1\le r<2^k$. Fix $r,k$ and a positive ternary-unit target $q$. If $a$ is the number of odd inputs to the first $k$ clocks from $r$ and $b=T^k(r)$, then $a\ge1$ and $3\nmid b$. Indeed, the final odd step has a unit output, and the subsequent halvings preserve this property. The affine lift of [PR 182, OffsetDescent.lean](https://github.com/GettysburgResearch/collatz/blob/cbec52dde5bed390a693310dd04e911033ba0cc9/research/lean-dyadic-descent-20261121/OffsetDescent.lean) gives $T^k(2^kv+r)=3^av+b$.

The powers of two run through every unit modulo $3^a$. One elementary proof starts at $v_3(4-1)=1$ and cubes $4^{3^t}=1+3^{t+1}h$ with $3\nmid h$ to obtain $v_3(4^{3^{t+1}}-1)=t+2$. Thus $4$ has order $3^{a-1}$, while $2$ has order $2\cdot3^{a-1}$ since it is $-1$ modulo three. For each inverse-row value $u_s$, pick $0\le j_s<2\cdot3^{a-1}$ with $2^{j_s}u_s\equiv b\pmod{3^a}$. As $Q$ increases the quantity $2^{j_s}u_s$ is uniformly larger than $b$. Hence

$$x_s=2^k(2^{j_s}u_s-b)/3^a+r$$

is a positive odd integer in the prescribed residue and hits $u_s$ in $k+j_s$ clocks. Set $M_s=2^{k+j_s}G^sKq/3^a$. The inverse-lift bound gives $|x_s-M_s|/M_s\le C_{k,r}/K$: for example use $C_{k,r}=1+b+r3^a$, $G^s\ge1$, $q\ge1$. As $Q\to\infty$, the logarithmic error is uniformly at most $1/Q$; this follows from $|\log t|\le |t-1|/\min(1,t)$ for $t>0$. Also $\lfloor\log_2 x_s\rfloor+1\le5Q$ for large $Q$, since $j_s$ and $k$ are bounded independently of $Q$ and $G<8$. The phase of $M_s$ is $\log_2q-a\alpha-s\alpha$ plus an integer. The same one-sided grid argument gives a marked predecessor in the required residue; the row lower bound tends uniformly to infinity. Each specific source is preserved through this construction. The result supplies arbitrarily high representatives in any one prescribed odd cylinder. The power-descent conclusion above uses the special growing suffix of $-1/3$ and is a separate result.

### Formal scope and replay

`cofinal_marked_power_predecessors` proves the arbitrary-target, arbitrarily-large-source theorem above, including the physical prefix, the subsequent hit of $q$, and the integer bound $u^5\le4^5x^4$. `universal_iff_marked_power` proves the exact global equivalence. The octave counting estimate, the general fixed-suffix variant and the sharpness example are written arguments. `cylinder_predecessor` formalizes the exact ordinary gluing step of the fixed-suffix variant. The axiom audit on the two global declarations lists `propext`, `Classical.choice` and `Quot.sound`.
