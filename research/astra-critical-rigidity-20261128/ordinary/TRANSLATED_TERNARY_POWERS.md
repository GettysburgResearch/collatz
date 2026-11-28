# Earlier-exponent obstructions on every integral translate of the ternary powers

**PROPOSED written theorem.** Fix any integer $c$, put $F_n=3^n+c$, and use the ordinary positive shortcut map. Let $\lambda=\log_3 2$, $K=1+|c|$ and $C_c=3\lambda+2\log_3 K$. For each integer $H\ge3$ there is a class of exponents modulo $2^{H-2}$ with the following property. Take any $n$ in the class with $n>3H+C_c$ and $3^n\ge2|c|$. If a forward orbit from **any** earlier positive member $F_m$, $0\le m<n$, meets $T^i(F_n)$ at any native clock $j$, for $0\le i\le H$, its own odd grade $q$ satisfies
$$
             (2-\lambda)q\ \ge\ n-(1+\lambda)i-C_c.                   \tag{1}
$$
In particular $q>H$. On this progression no earlier exponent meets the first $H+1$ upper states with both clocks bounded by $H$. For any integer $B\ge0$ with $B+5<H$, even arbitrarily long native clocks cannot give such an earlier-exponent merger using at most $B$ odd departures on each arm. For every sufficiently large $H$ one can choose a qualifying exponent with $H=\log_2 n+O_c(1)$. If an additional congruence on $n$ of fixed odd modulus $b$ is imposed, the bound becomes $H=\log_2 n+O_{c,b}(1)$. Along those choices the lower-arm grade must be at least $(1/(2-\lambda)-o(1))n$, whose coefficient exceeds 0.730.

This applies to the unshifted powers and to every negative or positive integral shift. For $c=-1$ it strengthens the lower-arm coefficient in the earlier [Mersenne exponent obstruction](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/MERSENNE_EXPONENT_DESCENT.md). The proof permits shifts to be fixed before taking the progression. The comparison targets here are restricted to earlier members of this same translate.

## Seven signed representatives

For $c=-1$ select $v=-6$. Otherwise use the following row by $c\bmod8$. Each signed integer reaches the fixed state $-1$ under the shortcut rules. Its entire forward orbit has the indicated total number $E$ of even departures.

| $c\bmod8$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $v$ | −15 | −4 | −3 | −2 | −1 | −2 | −1 | −8 |
| $E$ | 5 | 2 | 2 | 1 | 0 | 1 | 0 | 3 |

The exceptional $v=-6$ has $E=3$. In every case $v-c\equiv1,3\pmod8$. Choose $3^n\equiv v-c\pmod{2^H}$. The powers of 3 modulo $2^H$ constitute precisely the two residue classes 1 and 3 modulo 8, with exponent period $2^{H-2}$. Indeed $v_2(3^{2^a}-1)=a+2$ for $a\ge1$ by successive squaring. Thus the required progression exists. By the Chinese remainder theorem any fixed odd modulus can also be imposed. With odd modulus $b$ (take $b=1$ in its absence), the combined class has period $M=b2^{H-2}$. Its unique representative $n$ in $[M,2M)$ satisfies the stated lower bounds for all sufficiently large $H$ and gives the asserted logarithmic scale.

For $d=n-m\ge1$, the two signed rational representatives are
$$
                         x=v,\qquad y=c+(v-c)/3^d .
$$
They determine the first $H$ respective parities of $F_n,F_m$ because two rationals with odd denominator that are congruent modulo $2^H$ have the same next $H$ branches. We claim there is **no** native time $t\ge0$ at which these two representatives have equal states **and** their odd grades satisfy $q_t-p_t=d$, where $p_t$ is the upper grade.

Here is a short exact verification for all integer shifts. Since $p_t\ge t-E$, equality of the grade difference requires $1\le d\le E$. Write the two offsets for a putative date as $A,C$. A word with odd grade $p$ and at most $e$ even departures satisfies
$$
                 0\le A/3^p < 2^e .
$$
For its $k$th odd letter, with $k$ starting at one, the contribution after dividing by $3^p$ is at most $2^{e+k-1}/3^k$. Summing the finite geometric progression proves the bound, including the empty sum. Equality of states when $q_t=p_t+d$ gives
$$
                   (3^d-1)c=A/3^{p_t}-3^d C/3^{q_t}.
$$
The lower word has at most $E-d$ even departures. Positivity of both offsets therefore forces
$$
                (3^d-1)|c|<3^d2^{E-d}.                                  \tag{2}
$$
This restricts $|c|<24$ since $E\le5$. The table lists **every** remaining pair, with a finite terminating certificate. Write $\delta=q_t-p_t$. An entry $(t,\delta,=)$ means the two rational states agree at date $t$ and hence their grade difference is permanently the indicated value. An entry $(t,\delta,-1)$ means the upper state is already $-1$, so the grade difference can only decrease thereafter. At every strictly earlier date the simultaneous state and grade conditions are checked directly.

| $c$ | $d$ and corresponding $(t,\delta,\text{reason})$ |
|---:|---|
| −16 | $1:(14,0,-1)$ |
| −8 | $1:(8,0,=),\ 2:(10,1,-1)$ |
| −1 | $1:(4,0,-1),\ 2:(4,1,-1),\ 3:(4,-1,-1)$ |
| 0 | $1:(15,0,-1),\ 2:(7,4,=),\ 3:(7,0,-1),\ 4:(7,2,-1),\ 5:(7,2,-1)$ |
| 1 | $1:(3,0,-1),\ 2:(2,0,-1)$ |
| 2 | $1:(5,0,-1)$ |
| 8 | $1:(11,0,-1),\ 2:(10,1,-1)$ |
| 16 | $1:(12,0,-1)$ |

All entries use integer arithmetic: retain the denominator $3^d$ for the lower arm and apply $y'\mapsto(3y'+3^d)/2$ to odd numerators and $y'\mapsto y'/2$ to even ones. This takes at most 15 steps per listed pair. The equality-control row $(c,d)=(0,2)$ matters: these rational states do meet, but their common date has grade difference 4, which persists. [Finite signed and physical replay](check_translated_powers.py) · [Integer receipts](TRANSLATED_POWER_CONTROLS.json)

## Excluding vanishing slopes

At a purported positive meeting put $p,q$ for the grades, $A,C$ for the word offsets, and $d=n-m$. Clearing the two native denominators gives
$$
 3^m(2^j3^{p+d}-2^i3^q)=2^i(3^qc+C)-2^j(3^pc+A).                       \tag{3}
$$
The integer in parentheses is nonzero. Otherwise unique factorization would give $i=j$ and $q=p+d$. Equation (3) would then give $3^q c+C=3^p c+A$. As $i=j\le H$, the same affine words act on the two signed representatives. Since $3^q y=3^q c+3^p(v-c)$, those signed endpoints coincide with the forbidden grade difference $d$. In particular the right side of (3) is a *nonzero* multiple of $3^m$.

## The cost on the earlier arm

An independent sharp interval bound for any offset $C$ of grade $q$ and length $j$ is
$$
             0\le C\le 2^j\big((3/2)^q-1\big).
$$
For fixed $j,q$ the offset is a sum of positive contributions from the odd dates, and is largest when the final $q$ letters are all odd. Equivalently, the last, penultimate and preceding odd contributions to $C/2^j$ are bounded respectively by $1/2,3/4,9/8,\ldots$. The stated bound is attained by that word.

Using $3^q\le2^j(3/2)^q$ and its upper-arm counterpart, the nonzero divisibility (3) implies
$$
 m\le\lambda(i+j)+(1-\lambda)\max(p,q)+\log_3(2K)
 \le \lambda j+(1-\lambda)q+i+\log_3(2K).                              \tag{4}
$$
Suppose $q\le n$, since larger $q$ immediately proves (1). The common endpoint $Y$ is at least $3^n2^{-i-1}$. Since $n\ge i+2$, this gives $Y\ge2(3/2)^q$. On the lower arm
$$
        Y=2^{-j}(3^q F_m+C)\le2^{-j}3^q K3^m+(3/2)^q ,
$$
so $Y/2\le2^{-j}3^q K3^m$. Substituting the lower bound for $Y$ yields
$$
                     n\le q+m-\lambda j+\lambda i+2\lambda+\log_3 K .
$$
Together with (4) this is (1). If a meeting had upper grade at most $B\le H-6$, it would have upper clock below $H$, because even the first $H$ steps already have grade at least $H-5>B$. The lower grade would then exceed $H$, proving the arbitrary-clock assertion.
