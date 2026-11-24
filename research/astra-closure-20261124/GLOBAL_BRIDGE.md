# Why sharp carry charges do not exclude the expanding $7/8$ phase

**Written result.** On an infinite two-block language at canonical phase $7/8$, every edge attains the sharp two-tier carry inequality and paid edges occur with positive lower density. Nevertheless the canonical multiplier grows exponentially and the positive real affine trajectory escapes. Each finite prefix also has arbitrarily large positive ordinary realizers. There is a computable aperiodic script of this kind with no single positive ordinary realizer. The $7/8$ phase for an actual all-time positive ordinary source remains open.

The scalar and gap conventions are those of PR182 at `cbec52dde5bed390a693310dd04e911033ba0cc9`, `research/carry-tower-round10-20261123/ActualScalar.lean`. Its `research/scalar-rigidity-round9-20261123/CARRY_RETURN.md`, R9-C1, gives the individual expanding macros used here.

## Equality on every prefix

At even odd-orbit clocks take canonical phase $7/8$, at odd clocks $5/8$. The canonical gaps are $2,1,2,1,\ldots$. Starting with carry zero, use either of the following pairs. In the table $R=3^{a-b}((d+1)/(c+1))^2$ for an edge with physical gap $a$, canonical gap $b$, and source and destination carries $c,d$.

| Pair | Supplied physical gaps | Carries | Edge factors $R$ | Ordinary affine formula |
|---|---|---|---|---|
| $L$ | $2,1$ | $0,0,0$ | $1,1$ | $(9q+7)/8$ |
| $P$ | $1,4$ | $0,1,0$ | $4/3,27/4$ | $(9q+5)/32$ |

Every line satisfies $a+d=b+3c$. With $h_i=p_i+c_i$, the recurrence $h_{i+1}=3h_i-a_i$ and boundedness give $h_i=\sum_{j\ge0}a_{i+j}/3^{j+1}$ by exact telescoping. Thus the discounted scalar of the supplied infinite gap word is exactly $7/8$ at its start. Each $P$ pays one strict nondebit and one debit, attaining both optimal constants. Consequently the product with factors $(4/3)^{J-D}(27/4)^D$ is an **equality at every prefix**, including prefixes ending halfway through a pair.

## Positive-density paid returns and real escape

Use the macros $L^{11}P$ and $L^{12}P$ in any order. Writing $m=11$ or $12$, there are $2(m+1)$ odd steps in one macro and the full affine return is
$$
T_m(x)=\lambda_m(x+7)-29/16,\qquad
\lambda_m=\frac{9^{m+1}}{2^{3m+5}}.
$$
This follows from $L(x)+7=9(x+7)/8$ followed by $P$. The least multiplier is $\lambda_{11}=282429536481/274877906944>1$, and $7\lambda_m-29/16>0$. The canonical multiplier in the same macro is $(9/8)^{m+1}=4\lambda_m$. Its factor four is exactly the converted sharp charge $((4/3)(27/4))^{\log_3 2}=4$. At least one debit occurs every 26 steps up to an initial or final partial macro.

For a concrete real trajectory use $x_0=32+\sqrt2$ and $x_{i+1}=(3x_i+1)/2^{a_i}$. At the $k$-th macro boundary $x\ge x_0\lambda_{11}^k$. Within that macro every value is at least three quarters of its starting value: $L(x)>x$, the intermediate $L$ step is $(3x+1)/4$, and the intermediate $P$ step is $(3x+1)/2$. Hence $\sum_i1/x_i<\infty$, the ordinary-form correction product stays bounded, and the scalar envelope $h_i\le1+\log_2(x_i)/3$ holds throughout since $h_i\le13/8$. All these real states are distinct: a repetition would impose a rational fixed point of a nonempty segment with slope $3^u/2^v\ne1$, whereas every $x_i$ is irrational. The exponents in this real trajectory are supplied by the script.

## Exact finite ordinary witnesses and the missing equality

For a specified finite gap word with total clock $A$, the backward maps $y\mapsto(2^a y-1)/3$ send the odd 2-adic ball onto one odd residue class modulo $2^{A+1}$. Indeed each is affine, has odd denominator and scales the binary radius by $2^{-a}$. At a positive ordinary source in that residue class the prescribed forward gaps are literal valuations: the successive chosen quotients are odd, and positivity follows from the forward formula. Each class contains arbitrarily large ordinary sources. Nested prefixes give a unique 2-adic source.

Even the **true infinite ordinary scalars** of changing witnesses approximate $7/8$. For a length-$n$ prefix, take its least positive residue $Q_n\le2^{A+1}$. Its actual endpoint is at most $2^nQ_n$, since every ordinary odd step increases height by at most a factor two. Here $A\le4n$. The true and supplied scalar tail identities have the same prefix sum, so
$$
|h(Q_n)-7/8|=3^{-n}|h(U^nQ_n)-h_n|=O((n+1)3^{-n}).
$$
The implicit constant is uniform over all scripts in the two-macro language by the true scalar envelope and $1/2<h_n\le13/8$.

For an explicit separation, enumerate the finite binary words in increasing length, using the two macro types as letters. At stage $j\ge1$, append the $j$-th enumerated word; then append whichever of the two next macros excludes $j$ from the resulting positive ordinary prefix cylinder (choose the first if both exclude it). This is a finite congruence test. The two extensions are disjoint: after eleven $L$'s the first begins $P$ with gap one and the second begins another $L$ with gap two. Every finite binary word occurs in the resulting script, so it is not eventually periodic. Each positive integer is excluded at its own stage and all subsequent stages. The least ordinary witnesses consequently tend to infinity: a bounded nondecreasing sequence of minima of nested cylinders would stabilize at a common positive integer. Thus this script has all the displayed scalar, strict-charge, real-height and finite ordinary properties, but no positive ordinary source realizes its whole word.

This construction leaves open whether some *other* script is realized by one positive ordinary source. Any proof excluding $7/8$ must use a property coupling the same positive ordinary source to its entire valuation word that this construction lacks. Pointwise sharpness, positive debit density, bounded real correction, and convergence of scalars along changing ordinary witnesses all hold here.
