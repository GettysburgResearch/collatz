# Algebraic companion: the conjugates that the joint real height misses

**Written diagnostic, not a new transcendence theorem.** This addresses one possible use of PR182's dyadic companion, frozen at 234fd2ece3a17c8950dce452291198705b4e6e60, research/high-variance-closure-20261124/ordinary-arithmetic/DYADIC_COMPANION.md.

Let x_i=T^i(n) for a fixed positive ordinary source n, let P_i count its first i odd inputs, and write A_i=2^(i+P_i)/3^i. Use PR182's splitting identity

    D(n)=B_i+A_i D(x_i),    B_i rational, D(x_i) in Z_2.

Suppose hypothetically that D(n)=alpha is algebraic of degree d>1, and fix its actual embedding into Q_2. For each i put alpha_i=(alpha-B_i)/A_i, an algebraic number in the same field of the same degree. For any other embedding sigma into an algebraic closure of Q_2, subtract the actual value:

    sigma(alpha_i)-alpha_i=(sigma(alpha)-alpha)/A_i.

Because alpha_i is 2-adically integral in the actual embedding, and i+P_i tends to infinity, the valuation of this difference is eventually negative. By the strong triangle inequality,

    v_2(sigma(alpha_i))=v_2(sigma(alpha)-alpha)-(i+P_i)

for every other embedding, eventually. The threshold is finite since the conjugates are distinct in characteristic zero. In particular exactly one conjugate remains integral at the chosen prime, while all other conjugates diverge 2-adically. The normalized absolute logarithmic Weil height consequently satisfies

    h(alpha_i) >= ((d-1)/d)(i+P_i) log 2 - O_alpha(1).

Here the local height contribution at 2 is the average of log max(1,|sigma(alpha_i)|_2) over all d embeddings into an algebraic closure of Q_2, counted with their local degrees; all other local height contributions are nonnegative. This is only a lower bound, but it shows why the bounded-denominator argument for rational D(n) cannot simply be repeated in a fixed number field.

If the real expansion of A_i tends to infinity on the proposed escaping trajectory (as in PR182's real-growth estimate), the differences of any two archimedean embeddings are proportional to 1/A_i and therefore tend to zero. This coalescence of archimedean conjugates is fully compatible with the 2-adic expansion just calculated. It does not bound the global height.

In particular, an approach using Northcott's finiteness theorem would need a bound on the contribution at all these other conjugate places, not just the actual 2-adic embedding and the real positive trajectory. Such a bound would itself contradict the displayed identity for any d>1. This isolates the missing Diophantine control without making a claim that algebraic irrational D(n) is possible or impossible on an ordinary orbit.

No appeal to the Subspace Theorem is made: the available rational approximants B_i have denominators 3^i, with the fixed embedding's error divisible by A_i 2-adically. An improvement beyond the corresponding moving height cost would be needed before applying an irrationality criterion. The present checkpoint does not produce that improvement.
