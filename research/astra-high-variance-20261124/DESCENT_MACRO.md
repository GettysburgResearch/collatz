# Descent from the three residual prefixes with infinitely recurring paired paid returns

Let $T(n)=n/2$ for an even input and $(3n+1)/2$ for an odd input. The two actual odd-to-odd blocks are $L=(2,1)$ and $P=(1,4)$, with boundary laws $8L(q)=9q+7$ and $32P(q)=9q+5$. A macro is a finite string of these blocks. The five permitted tail macros are
$$\mathcal M=\{L,\ L^6P,\ L^6PP,\ L^6PLP,\ L^6PLLP\}.$$

**Theorem.** Suppose a positive ordinary input has infinite block word $L^r W\mathcal M^\omega$, with $r\ge0$ and $W$ any of **PPLLL, PLLPP, PLLPL**. Then there exists a smaller positive odd ordinary nonconverger below the initial boundary. For $r>0$ it is also below the first light intermediate. Consequently none of the three original-floor candidates can be the globally least odd nonconverger on this language. The tail can contain infinitely many close paid pairs with any mixture of zero, one and two intervening light blocks. A tail with arbitrary overlapping paid clusters remains open.

The previous finite prefix code covers the other thirteen five-letter headers without tail restrictions. Thus all sixteen headers are covered if their following tail is in $\mathcal M^\omega$. This statement includes no assertion that such an infinite positive ordinary path exists.

## Two expanding ordinary comparisons

For a word $V$, write $2^A q'=3^p q+C$. Its carry begins at zero and appending a letter with clock $a$ and offset $c$ updates it to $9C+2^A c$. Choose the multiplier $\lambda=M/2^d$ from the table below. At every tail-macro boundary put
$$Y=\lambda(q+7)-7.$$
Both multipliers exceed one. The needed strict size saving comes earlier on the ordinary path. There is no requirement that $Y$ be smaller than its current source boundary.

| Initial header $W$ | $M$ | $d$ | $\ell$ | Entrance target clocks | Entrance odds |
|---|---:|---:|---:|---:|---:|
| PPLLL | 5583 | 12 | −6 | 30 | 16 |
| PLLPL | 5583 | 12 | −6 | 30 | 16 |
| PLLPP | 72873 | 16 | −9 | 36 | 19 |

On a tail macro the target numerator is $3^pY+K$ with
$$K=\lambda(C-7\cdot3^p+7\cdot2^A)+7(3^p-2^A).$$
For each of the ten combinations of macro and multiplier, $K$ is an integer and is the carry of an ordinary length-$A$ shortcut word with $p$ odd inputs. Here is a short complete certificate convention for these finite facts. For proposed time $A$, odds $p$, carry $K$, take $b=-K(3^p)^{-1}\bmod 2^A$ in $[0,2^A)$. Iterate $b$ exactly $A$ times, verify the count $p$ and the equality $2^A T^A(b)=3^p b+K$. Each lift $2^A t+b$ follows the same bits and reaches $3^p t+T^A(b)$. All ten words are printed by [descent_macro.py](descent_macro.py).

Since $2^A Y'=3^pY+K$, a reduced binary denominator $2^e>1$ at any time grows to $2^{e+A}$ at the next macro. All denominators divide $2^d$, which proves every $Y$ is an integer on the one given infinite ordinary path. Positivity follows from $\lambda>1$ and $q>0$. The carry certificate makes successive $Y$'s actual iterates. Their concatenated target trajectory cannot hit one. Indeed each macro has $2p-A\ge1$, so the cumulative excess of odd over even inputs is unbounded. A shortcut trajectory that reaches one then alternates between one and two, giving bounded cumulative excess.

## A smaller source at the original floor

Let $q_0$ be the initial boundary and $q$ the boundary immediately before the first P. The $r$ light equations and oddness force a positive integer $v$ such that
$$q_0+7=2^{3r+1}v,\qquad q+7=2\cdot 9^r v.$$
For $r\ge7$ take $m=M2^{2r+\ell}v-1$. It is positive and odd. Its first $2r+\ell$ steps are odd and end at $z=M3^\ell(q+7)/2-1$. The table gives $(m+1)/(q_0+7)=M2^{\ell-r-1}\le5/8$. Here $q_0+7\ge2^{22}$, so $m<(3q_0+1)/4<q_0$.

If the initial residual header has data $(A,p,C)$, define $B=A+d-1$, $u=p-\ell$ and
$$K=\frac M2(C-7\cdot3^p+7\cdot2^A)-7\cdot2^B+3^u.$$
Then $3^u z+K=2^B Y$ at the start of the infinite comparison tail. The three checked target words are

| Header | Chronological target parity bits |
|---|---|
| PPLLL | 010100011001111000011101101101 |
| PLLPL | 010101011101010100010110011101 |
| PLLPP | 011101011001110101101100000110011100 |

Therefore $m$ reaches an actual nonconvergent $Y$. The input and the comparison tail can have entirely different later orbits.

For $r\le6$ the actual first paid endpoint $[9(9/8)^r(q_0+7)-58]/32$ already beats the required floor for $q_0\ge17$. Substitution at $r=6,q_0=17$ verifies the worst intercept and slope, or the seven affine comparisons can be checked separately. Every smaller positive odd input reaches one by direct iteration. The original infinite macro path also has unbounded positive odd excess, so the small inputs cannot be among its sources. This completes the initial-floor proof.

## Uncovered schedules

The reset uses an entire macro and can reorder the odd positions across its internal letters. For both displayed multipliers, $L^6PPP$ does not satisfy the reset-carry test. In particular an arbitrary sequence of triple paid clusters is outside this proof. Such clusters may cause long net contractions, but an arbitrarily long initial light run can place them high above the original floor. An isolated local contraction is insufficient to conclude.

The separate [signed-pair obstruction](DESCENT_PAIR.md) explains why simply waiting for more light letters after PP cannot bring the original all-odd ramp back to the original boundary at a uniform affine clock. The comparison constructed here uses a different positive ordinary tail.

## Kernel scope

[descent_macro.lean](descent_macro.lean) passed Lean 4.34.1 with `-j1 -DwarningAsError=true` and only `Std`. Its SHA-256 is `c3cb02722e2c633b8416d091867ae36e41dbccc1bfbbb7171e52a6f4ab52f65d`. The five audit declarations cover infinite denominator clearing, literal tail nonconvergence, all three asynchronous entrances, descent from the initial raw light prefix for $r\ge7$, and the paid-boundary inequality for $r\le6$. The tail interface supplies the exact source macro boundary laws and $q_j\ge3$; each is forced by an actual positive L/P macro input. The small-$r$ arithmetic lemma takes the composed initial light-to-paid equation. The three tail and entrance theorems use only `propext` and `Quot.sound`; the two floor theorems also use `Classical.choice`.

A different two-state comparison supports unbounded runs of consecutive P's. Its entrance condition and exact scope are given in [DESCENT_PAID_RUNS.md](DESCENT_PAID_RUNS.md).
