# Finite certificates at the two recurrent ternary residues

**PROPOSED, unconditional.** Let $P(u)$ denote agreement of the labels at $u$ and $3u$, where any positive labeling invariant under the ordinary Collatz shortcut step is allowed. These two identities bound the recurrent parts of the [one-residue modulo 64 proof](ONE_CELL_SIXTY_FOUR.md).

| Ordinary input $u$, $t\ge0$ | Congruence at the rational fixed point | Word from $u$ to $3u$ | Only tripling test required |
|---|---|---|---|
| $162t+67$ | $162\mid29u+1$ | `ODDIIDDIMOOOEEEEI` | $P(1152t+477)$ |
| $648t+443$ | $648\mid509u+17$ | `DDDDIVOOOEOOEEIDI` | $P(2304t+1575)$ |

Here $D$ doubles, $I$ takes the positive odd preimage $(2x-1)/3$, and $O,E$ are ordinary shortcut steps. The letter $M$ triples the current input and $V$ divides it by three. In each case the smaller endpoint of this extra edge is the indicated positive odd multiple of nine. All ordinary letters preserve the label. The two rows are exact identities of affine functions of $t$. The [verifier](check_three_rays.py) checks the divisions, parities, target test class, positivity, and final two coefficients. For example the final values are respectively $486t+201$ and $1944t+1329$.

The two recurrent return maps are $u'=(32u+1)/3$ and $u'=(512u+17)/3$. For either one, putting $W=(A-3)u+B$ for its coefficients $A,B$ gives $W'=A W/3$. Thus four consecutive integral applications require $3^4\mid W$ at the start of those four applications. One preceding application makes $W$ divisible by the needed binary factor, namely 2 in the first row and 8 in the second. Five repetitions of either map from ordinary positive integers therefore place its second input in the corresponding row. A true failed unit at that input forces an actual failed odd nine-multiple at the displayed test. This replaces arbitrarily long recurrent runs with a bounded comparison. It does not assume any convergence for the two rational fixed points.
