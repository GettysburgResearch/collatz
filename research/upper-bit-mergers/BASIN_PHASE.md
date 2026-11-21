# Which convergent pairs have an affine merger certificate?

**Proposed, unconditional.** Use the positive shortcut map $T(n)=n/2$ for even $n$ and $(3n+1)/2$ for odd $n$. For a positive integer $n$ reaching 1, let $s(n),h(n)$ be its odd-input count and clock at any visit to 1. The quantity

$$
 K(n)=2s(n)-h(n)
$$

is independent of the visit, since the cycle from 1 has one odd input in two steps. For every positive $n$ in this basin,

$$
 K(n)\ge -\log_2 n. \tag{1}
$$

Indeed $2T(x)/x$ is 1 on even inputs and at most 4 on odd inputs. Multiplying along the path gives $2^{h(n)}/n\le4^{s(n)}$.

## Exact classification inside the basin of 1

Let two integer affine families have positive slopes $A,B$ and let $x,y$ be their positive values at the same integer parameter. A lifted merger means there are two finite ordinary parity words ending at the same affine expression on an entire binary residue class of parameters containing the chosen parameter. If both $x,y$ reach 1, a lifted merger exists **if and only if** $B/A=2^u3^v$ for some integers $u,v$ and

$$
 K(y)-K(x)=-u-2v. \tag{2}
$$

At clocks $i,j$ with $p,q$ odd inputs, the endpoint slopes are $A3^p/2^i,B3^q/2^j$. Equal slopes force the stated factorization, $j-i=u$ and $p-q=v$. From a common endpoint follow the same path to 1. This gives (2). Conversely start with the two hits at 1. Append whole two-step cycles to the two paths so that $p-q=v$, adding cycles to whichever side requires them. Equation (2) then gives $j-i=u$. The endpoints and slopes agree. Every finite parity word stays legal under all sufficiently high binary shifts of the common parameter, so the two affine expressions coincide on an entire such class.

## The obstruction on the smallest nontrivial witness family

Put $e=6d+1$, $d\ge1$, $k=(2^{e-1}-1)/9$, $X=16k+1$, and $Y=32k+1$. The first four steps from $X,Y$ have two odd inputs each. Their endpoints are $9k+1=2^{e-1}$ and $18k+1=2^e-1$, respectively. Thus $X$ reaches 1 with precisely two odd inputs. Conversely the same first four steps show that every $k>0$ with a two-odd first-hit witness from $X$ has this form, since $9k+1$ must be a power of two and 2 has order six modulo 9.

The next $e$ steps from $2^e-1$ are odd, ending at $z_e=3^e-1$. If $Y$ reaches 1, the exact difference is

$$
 K(Y)-K(X)=2e-1+K(z_e)>(2-\log_2 3)e-1. \tag{3}
$$

Here $K(X)=-(e-1)$, $K(Y)=e+K(z_e)$, and (1) supplies the strict inequality. For **every** actual meeting at clocks $i,j$ with odd counts $p,q$, the left side of (3) equals $2(q-p)-(j-i)$. Any such meeting makes $Y$ converge because $X$ converges. In particular, no parameter of this two-odd family admits a lifted merger at any clocks, since (2) would give $-1$. This is a restriction on how these particular ordinary comparisons could be settled. For example $e=7$ has both arms reaching 1 and still has this obstruction.

The same obstruction occurs at every binary depth $4^s$ with $s\ge2$. Take any positive $a$ divisible by $2\cdot3^{s-1}$, put $k=(2^a-1)/3^s$ and $x=4^s k+1$. The pair $x,2x-1$ takes $2s$ steps with $s$ odd inputs on each arm to reach $2^a,2^{a+1}-1$ respectively, by iterating $T^2(4u+1)=3u+1$. The computation in (3) applies with $e=a+1$. Since $16\mid x-1$, the [four-versus-five-step identity](THREE_RAY_ONE_SIDED.md) is itself a lifted merger of $3x$ and $2x-1$. Thus $x,3x$ cannot have a lifted merger at any of these parameters either. With $s=6$, the [two shifted-arm identities](ADJACENT_128.md#two-shifted-classes-of-adjacent-pairs) transport this obstruction to the pair $2^{23}k+6464,2^{23}k+6465$. The upper arm there lies in the component of $x$ and reaches 1. Composition of lifted mergers is valid: restrict to the intersection of the binary neighborhoods and advance any two different clocks on the shared intermediate arm to their maximum.

There is a related limit on reducing the exponents themselves by affine-word identities. A lifted merger between the families $3^a t-1$ and $3^b t-1$ at $t=1$ preserves

$$
 I(a)=2a+K(3^a-1)=I(b)
$$

whenever one endpoint converges. This follows from (2), or directly by equating the endpoint slopes. Equality propagates along any finite chain of these certificates. Since $I(a)>(2-\log_2 3)a$ for $a\ge1$, every exponent connected to a convergent seed $b$ in this manner is strictly less than $I(b)/(2-\log_2 3)$. Finitely many verified seeds therefore cover only finitely many positive exponents in this proof scheme. Auxiliary affine families do not change the conclusion: along every lifted edge the quantity $K(x)+v_2(A)+2v_3(A)$ is invariant, where $A$ is the current family's positive integer slope.

## A uniform finite bound with an odd-step budget

For any $k\ge0$ start the two clocks at $x=X$ and $y=T(Y)=3x-1$. For $R\ge0$ put

$$
 H_R=(2R+1)\left\lceil3+(R+1)\log_2 3\right\rceil+1.
$$

If both paths use at most $R$ odd inputs through clock $H_R$, they already have a lifted merger by that clock in these aligned coordinates. This finite assertion has no convergence hypothesis. Consequently, if $X>2^{H_R}$ and both $X,Y$ reach 1 with at most $R$ odd inputs each, their phase difference is necessarily $K(Y)-K(X)=-1$.

To prove the bound, let $p_i,q_i$ count odd inputs in the two words through time $i$. Using the fixed budget $R$, form the signed integer

$$
 B_i=2^i\bigl(3^{R-q_i}T^i(y)-3^{R+1-p_i}T^i(x)\bigr).
$$

Its initial value is $-3^R$ and $2^i\mid B_i$. We first show that $B_i=0$ implies a lifted merger. Vary $x$ by $2^i m$ and $y$ by $3\cdot2^i m$ inside their two legal words. Their endpoint functions of $m$ have slopes $3^{p_i}$ and $3^{q_i+1}$. The equality $B_i=0$ says they have the same zero $m_*=-T^i(x)/3^{p_i}$, a rational with odd denominator. At this value the two rational starting points $z=x+2^i m_*$ and $3z-1$ follow the same words as their corresponding integer starts and both end at zero. Indeed the starting differences are divisible by $2^i$ in the rationals with odd denominator, so their parities at all $i$ steps agree with those of the original starts.

A rational of odd denominator that reaches zero after a word containing $p$ odd inputs has reduced denominator exactly $3^p$. In reversing the word from zero, the first odd inverse gives $-1/3$. Every subsequent odd inverse $(2u-1)/3$ increases the denominator's ternary exponent by one and every even inverse preserves it. If $p=0$ the start was zero. Here $p_i=0$ would give $z=0$ and $3z-1=-1$, whose orbit is fixed away from zero. Thus $p_i\ge1$. The reduced denominator of $3z-1$ is $3^{p_i-1}$, giving $q_i=p_i-1$. Now $B_i=0$ gives equal endpoints and the endpoint slopes are equal. Restricting the variation back to $x=16k+1$ gives the claimed lifted merger in $k$.

The difference $B_{i+1}-B_i$ vanishes if both inputs are even. Otherwise its absolute value is at most $2^{i+1}3^{R+1}$, by substituting the two ordinary branches in the definition. Prior to a lifted merger every $B_i$ is nonzero, so $|B_i|\ge2^i$. If $j<i$ is the latest odd-input position on either arm, summing the geometric bound gives $|B_i|\le 2^{j+3}3^{R+1}$. Hence $i-j\le3+(R+1)\log_2 3$. There are at most $2R$ odd-input positions in the two words together, and clock position zero already has the odd input $x$. The gaps between these positions and the terminal time cannot cover $H_R$ steps. This proves the finite assertion. Finally, a positive start greater than $2^{H_R}$ cannot reach 1 in its first $H_R$ steps, since each step is at least a halving. Apply the finite assertion to the two bounded-odd witnesses and then (2) to obtain the consequence about $K$.
