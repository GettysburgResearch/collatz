# Closing and splicing genuine cycle words

A nonconstant concatenation of full rotations of a positive ordinary lap of length $n$ has reduced denominator $d'$ satisfying $d'R>2^n$, with $R$ the span of the selected integer phases. The same elementary inequality includes rational laps from several cycles with multipliers on the same side of one and arbitrary repetitions of extremal pieces. For individual rational cycles, an exact formula gives the full reduced denominator of every proper factor in terms of its endpoint numerator displacement. Rhin's external logarithm-separation estimate implies that all almost-full proper prefixes at the minimum of an ordinary lap have denominator $2^{n+o(n)}$. The full return has denominator one. [Proof and source comparison](ROTATION_SPLICES.md)

If the list of rotations has least period $k$ in dictionary symbols and uses $a$ rotations, two boundary phases share at least $\lceil\log_a k\rceil-1$ complete symbols. Their common-denominator dyadic separation gives a lower bound growing as $k^{n/\log_2 a}$. Combined with the anchor height bound, this gives $d'\ge cP^2$ at every resulting least physical period $P$ for a positive ordinary parent, uniformly over all parent periods. This packing argument is a written proof.

These statements constrain attempts to obtain new ordinary periods from one hypothetical exceptional cycle. They do not exclude an individual such cycle or prove ordinary convergence. They are written proofs.

## Exact controls

Run both commands in this directory.

~~~sh
python -B check_splices.py
python -OB check_splices.py
~~~

The checker enumerates ordered same-side three-block splices of words through length three and all proper factors at every rotation of primitive necklaces through length ten. It checks the full gcd formula, all transported integer differences, the extremal-run denominator inequalities and the explicit mixed-side counterexample. [check_splices.py](check_splices.py)
