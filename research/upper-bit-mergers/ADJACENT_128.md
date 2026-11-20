# One pair of neighbors after every multiple of 128

**PROPOSED.** For the positive shortcut Collatz map, full convergence is equivalent to the following statement. For all sufficiently large $k$, the orbits starting at $128k+1$ and $128k+2$ have a common iterate, with independent clocks allowed. The same equivalence holds with $54$ in place of $128$. The reduction to one binary class has a written proof and an exact finite verifier. The changes of variables below are verified in Lean. [Single-class reduction](ONE_CELL_SIXTY_FOUR.md) · [Lean proof](HighBit.lean)

## Why these adjacent integers occur

Write $a\sim b$ when the two orbits meet. The status of a comparison is unchanged by advancing either arm any finite number of steps. The two base paths at clock five are

$$
 1\to2\to1\to2\to1\to2,\qquad
 3\to5\to8\to4\to2\to1.
$$

The first path has three odd inputs, the second two. A shift of $32m$ in a starting value adds $3^s m$ to its endpoint when its five-step path has $s$ odd inputs. Taking shifts $64k$ and $192k$ gives exactly

$$
 T^5(64k+1)=54k+2,\qquad T^5(3(64k+1))=54k+1.
$$

For $A(m)$ denoting $m+1\sim m+2$, we also have $A(3u)\Longleftrightarrow A(4u)$: two steps take $4u+1$ to $3u+1$ and $4u+2$ to $3u+2$. Three applications identify $A(54k)$, $A(72k)$, $A(96k)$ and $A(128k)$ term by term. The claimed equivalence now follows from the single-class theorem. The same termwise identities preserve the endpoints' actual component labels, so they apply to every partition of the components.

## How many pairs would have to stay apart?

Suppose two positive starts have distinct components $B$ and $C$. There are an absolute $M>1$ and a constant $c_{B,C}>0$ such that for every sufficiently large $R$, **every** partition separating $B$ from $C$ separates $128k+1$ and $128k+2$ for at least $c_{B,C}R^{0.164}$ indices $R<k\le MR$. This follows from the local count for all odd tripling parameters, the finite affine transfer into $1\bmod64$, and the identities above. The transfer even allows restricting these indices to $4\nmid k$. At a sequence of growing cutoffs the full failure count below $X$ divided by $X^{0.84}$ is unbounded, by the disjoint-predecessor amplification and the bounded-multiplicity transfer. The constants from the finite proof can be large. [Odd-parameter shells](ODD_TRIPLING_SHELLS.md) · [Localized transfer](ONE_CELL_SIXTY_FOUR.md#the-count-transfers-without-loss-of-exponent) · [Predecessor amplification](TWO_SCALE_TRIPLING.md)

There is an upper bound $O(N/\sqrt{\log(2N)})$ in every interval of $N\ge2$ indices $k$. To see its scope precisely, start with $54k+1,54k+2$. After one step the arms, in increasing order for $k\ge0$, are $X=27k+1$ and $3X-1$. The odd multiplier 27 makes the next $h$ base-parity bits exactly uniform in any interval of $2^h$ indices. The excursion bound at level one and offset $-1$ proves the estimate. The order $1/\sqrt h$ is sharp for the fraction missing a finite deadline in sufficiently distant binary blocks. Indeed, the fair level-jump walk survives $h$ decisions with probability $\gg1/\sqrt h$. On that event there is no equal-slope merger. For $y=54k+1>2\cdot 6^{h+1}$, any independent-clock merger of $y,y+1$ through clock $h+1$ must have equal slopes: the affine offset equation has right side of absolute value less than $2\cdot6^{h+1}$ and left side an integer multiple of $y$. Clock zero cannot itself give an equal-slope merger of the two distinct starts. This proves the finite-deadline lower estimate for the $54k$ pair. A positive power saving for permanent failures would require further control beyond that estimate. [Upper estimate](THREE_RAY_UPPER.md) · [Fair walk and slope separation](THREE_RAY_CLOCKS.md) · [Obstruction to bounded descent through smaller pairs](ADJACENT_DESCENT.md)

## Two shifted classes of adjacent pairs

Full convergence is equivalent to **eventual** merger of $1024k+16$ and $1024k+17$. At clock nine the base starts $16,17$ reach $2,1$ respectively, each after three odd steps. A shift of $1024k$ adds exactly $54k$ to each endpoint. The lower intercepts $21$ and $23$ also work at the same modulus.

A separate criterion requires merger of $2^{23}k+6464$ and $2^{23}k+6465$ for **every** integer $k\ge0$. At clock 23 the base starts reach $2,1$ with seven and six odd steps, respectively. Hence the shifted endpoints are $3^7 k+2$ and $3^6 k+1$. The pair $3456k+1,3456k+2$ reaches these same endpoints at clock seven. Its meeting is precisely the tripling comparison at $4096k+1$, by substituting $64k$ for $k$ in the clock-five identity above. The implication to full convergence here uses the all-member hypothesis of the [stabilized descent](STABILIZED_CORE_DESCENT.md).

These moduli are the largest possible under the following fixed-word requirement. For $S=54$ or $3456$, start from $Ck+r,Ck+r+1$ with a positive integer $C$ and fixed integer $r$. Match the two starts, in either order, to $Sk+1,Sk+2$ by fixed pairs of forward parity words valid for every sufficiently large integer $k$. For each matched pair the two terminal affine functions must agree. The maximum $C$ is $1024$ for $S=54$, attained exactly at $r=16,21,23$. For $S=3456$ the maximum is $2^{23}$, attained exactly at $r=6464$. Reductions using multiple comparisons or a partition of the parameters can use different word choices.

To verify the classification, put $t=v_2(S)$. A target word can have at most $t$ steps, since after $t$ steps its coefficient on $k$ is odd and the next parity varies. Extend both sides of each matching identity until its target has taken exactly $t$ steps. The target endpoints have the form $3^P k+2,3^{P-1}k+1$, with $P=4,7$ respectively. The two source words must now have the same clock $h=v_2(C)$, by matching coefficients. The arm ending at $2$ has one more odd step than the arm ending at $1$, and at most $P$ in all. Their intercepts are positive because the shortcut preserves nonpositivity. The intercept of the arm ending at $2$ is at most $2^{h+1}/3<2^h$, by its positive odd count and the nonnegative offset in its iterate. Consequently $0<r<2^h$.

For each low-bit prefix $r_0$ of length $j$, record the two endpoints $x,y$ at clock $j$ and odd counts $p,q$. Appending bit $b\in\{0,1\}$ shifts those endpoints by $b3^p,b3^q$ before the next step. Discard any prefix exceeding $P$ on either arm, or with equal counts and equal endpoints, since every lift of the latter stays merged. At each surviving prefix test the two exact endpoint and coefficient identities. The search exhausts all prefixes at depths 16 and 35, after visiting 333 and 34,146 states respectively. This gives the maxima above. [Exact classifier](check_adjacent_cells.py)
