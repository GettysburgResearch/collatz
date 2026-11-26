# Finding and certifying ordinary inverse-gap predictors

When $D$ is finite and $S$ is given by an effective enumeration of its forbidden words, the low-entropy decoder theorem gives a terminating search under the promised hypotheses that $S$ is nonempty and $h(S)<\log3$. There is no claimed running-time or uniform precision bound as $S$ varies. For the specific all-interval drawdown bound $C=2$ a direct finite certificate gives the following result without an asymptotic argument.
$$
 \#\{0\le j<n:e_j\ne g(a_j\bmod 59049)\}
 \le \left\lfloor\frac{n+82}{9}\right\rfloor
 \qquad(n\ge1).
$$
Here $a_j$ are the actual successive positive odd inverse states, and every interval of the prescribed word satisfies $2^{\sum e_j}\le4\,3^\ell$. The rule $g$ below is exact and reproducible.

## Effective search

Fix a rational target error $\epsilon>0$. Enumerate $h$, all finite tables $g:(\mathbb Z/3^h)\to D$, and all finite prefixes of the forbidden-word enumeration, dovetailing the searches. The associated decreasing finite-type supershifts $S_M$ have intersection $S$. For fixed $g,h$ the error event $1_{g(X_0[h])\ne E_0}$ depends only on the initial $h$ labels. On each finite-type supershift its largest invariant mean is the maximum mean edge cost on a finite directed cycle. Use vertices of length at least $h-1$ and at least the longest retained forbidden length less one. Discard forbidden windows and assign each edge the error cost of its first $h$ labels. Every cycle represents a valid periodic sequence of the supershift. When several directed edges have the same endpoints the labels remain distinct.

For a fixed $g,h$ the maxima on $S_M$ decrease to the maximum on $S$. Indeed a subsequential limit of maximizing invariant probabilities is invariant, is concentrated on every $S_M$, and preserves the expected error by continuity. The proof of the uniform decoder supplies a table with maximum over $S$ strictly below $\epsilon/2$. Hence a finite stage certifies an error mean below $\epsilon/2$. This supplies a finite bound for arbitrary actual words: given a graph with $V$ vertices and maximum cycle mean $r$, erase cycles from any path. At most $V-1$ edges remain, so a length-$k$ path costs at most $rk+V$. Allowing the fixed boundary window length in an ordinary word provides an explicit onset giving error below $\epsilon$. One may instead verify a rational difference potential on every admitted edge, as below.

For rational $C=u/v\ge0$, the bounded-drawdown language has an effective forbidden-word enumeration. Its every-interval test uses the exact integer comparison $2^{v\sum e}\le2^u3^{v\ell}$. By the O18 entropy bound this procedure terminates for each fixed $C$ and error target. For a directly decidable language, a simpler exhaustive certificate checks a length-$k$ error block over all allowed $(k+h-1)$-words and tiles a longer word by consecutive blocks. The finite-type procedure also covers languages supplied by a one-sided enumeration of forbidden words.

## A certificate at $C=2$

Let $\mathcal W$ consist of the length-ten words on $\{1,2,3\}$ satisfying the interval inequalities. For $w\in\mathcal W$, compute $b(w)$ by evaluating $G_{w_0}\cdots G_{w_9}(0)$ modulo $3^{10}$. For residue $b$, take the smallest available first letter among words with $b(w)=b$, and take 1 if the set is empty. In the two residues $34445$ and $52589$ set the guess to 3. This defines $g$ on all 59,049 residues.

Use each $w$ as an edge from its length-nine prefix to its length-nine suffix. Write $m(w)=1_{g(b(w))\ne w_0}$. The exact checker constructs an integer vertex potential satisfying
$$
 0\le d(v)\le10,\qquad 9m(w)-1\le d(\operatorname{end} w)-d(\operatorname{start} w)
$$
on every edge. It checks 4,111 words, 1,921 vertices and 2,696 attained residues, including 14 with more than one possible first label. It independently follows each word backwards from an actual positive odd representative and checks every exact forward valuation on return. The compact specification of the rule and the potential inequality use integer arithmetic and do not require an optimizer.

For $n\ge10$, summing over $n-9$ successive completely observed windows bounds nine times their mistakes by $n-9+10=n+1$. The final nine letters add at most 81 to this bound. For $n<10$ the claimed inequality follows from the count of letters. The edge test uses only interval constraints through ten letters, so this particular certificate also holds for every finite ordinary word passing those local tests. A mixed-integer search supplied the two special table choices. The verification is independent of how they were found. No claim about the optimality of the factor $1/9$ is needed.

[Decoder and potential checker](check_decoder.py) · [Recorded finite controls](../../../reports/unconventional-20261126/DECODER_CONTROLS.json)
