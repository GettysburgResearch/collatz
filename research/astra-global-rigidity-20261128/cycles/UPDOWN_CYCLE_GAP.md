# A counterexample to the proposed up-down cycle gap

For a set \(S\) of positive integers, Vasilyev chooses \(U(x)=\lceil3x/2\rceil\) on \(S\) and \(D(x)=\lceil x/2\rceil\) elsewhere. Question 7.1 asks whether every simple cycle with length \(\ell\) and \(a\) upward edges satisfies \(2^\ell<3^{a+1}\). The paper checked every cycle of length at most 30 and every cycle with maximum at most 160. [Vasilyev, *Up or down at every integer*, v1, §7](https://borowiecki.dev/pdf/2611.20344)

**The answer is negative.** Start at 4, take 298 steps, and use \(U\) at time \(i\) precisely when bit \(i\) of the following hexadecimal integer is one, starting with bit zero at time zero.

```
39babef0fd2abcd777de1a6adf8addcdd39b6babb5b67b2ddefe072dadcdd5f7d0eefdd7b
```

The walk has 298 distinct positive vertices, maximum 998, returns to 4 and uses \(a=187\) upward edges. Exact integer comparison gives \(2^{298}>3^{188}\), hence \(2^{298}/3^{187}=3.05677924\ldots\). Distinctness ensures a single set \(S\) realizes every specified choice. The Lean file checks the complete list of vertices, its cyclic adjacency, its upward-edge count and the power comparison. The independent standard-library checker decodes the branch mask and compares its output with the literal Lean vertices.

The same checker contains a separate 6471-step certificate starting at 4 with maximum 15996 and 4081 upward edges. Its ratio is \(2^{6471}/3^{4081}=6.81179282\ldots\). This gives a lower bound for the supremum in the second part of the question. A finite assignment computation suggested the walks: use one incoming and one outgoing edge per chosen vertex, with an unselected vertex represented by a self-loop in the assignment problem. Extract individual permutation cycles and test each one by exact integer arithmetic. The proofs from the supplied words have no solver or floating-point dependency. [Exact checker](check_updown_counterexample.py) · [Lean witness](UpDownCounterexample.lean)

## A universal upper bound in terms of length

For every simple cycle of length \(\ell\),
\[
                         2^\ell/3^a\ll (1+\ell)^{1/3}.
\]
Write \(m_x=3\) on upward sources and \(m_x=1\) on downward sources, and let \(e_x=x\bmod2\), so the successor is \((m_x x+e_x)/2\). Put \(H=\sum_{x\in C}1/x\), \(O=\sum_{x\in C,\;x\text{ odd}}1/x\) and \(J=\sum_{x\in C,\;m_x=1}1/x\). Invariance under the cyclic permutation gives
\[
 H=2J+\tfrac23(H-J)-E,\qquad
 0\le E=\sum_{x\in C}\big(2/(m_xx)-2/(m_xx+e_x)\big)
                   \le2\sum_{k\ge1}k^{-2}.
\]
Thus \(J=H/4+O(1)\). Distinctness gives \(H\le\log(1+\ell)+O(1)\) and \(O\le\tfrac12\log(1+\ell)+O(1)\). The multiplicative identity around the cycle now gives
\[
 \log(2^\ell/3^a)=\sum_{x\in C}\log(1+e_x/(m_xx))
        \le O/3+2J/3\le\tfrac13\log(1+\ell)+O(1).
\]
The finiteness and exact value of the unrestricted supremum remain open here.

The one-point harmonic estimate has a matching infinite-permutation example. Use \(D\) exactly at the odd integers whose factor remaining after removing all powers of three is \(1\bmod3\), and use \(U\) elsewhere. Every output \(y\equiv0\pmod3\) has the single chosen even upward predecessor \(2y/3\), and every \(y\equiv1\pmod3\) has the single odd downward predecessor \(2y-1\). For \(y\equiv2\pmod3\), the candidate odd sources \(2y-1\) and \((2y-1)/3\) have the same reduced factor modulo three, so exactly one supplies the required incoming edge. The downward sources \(3^j(6k+1)\) have density \(1/4\) by summing the disjoint progressions. The harmonic rounding sum over all inputs \(x\le X\) is therefore \((1/3+o(1))\log X\). This example concerns a permutation of the infinite set of positive integers. Turning its truncated sums into a single simple cycle would require closure information.
