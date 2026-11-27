# A denominator-uniform census of all signed rational Collatz cycles

Let a nonzero rational Collatz cycle use the usual shortcut map on rationals of odd denominator, with parity taken from the reduced numerator. Write \(d_C\) for the common reduced denominator, \(n_C\) for its **least** physical period and \(u_C\ge1\) for the odd count. Put
\[
          g_C=|n_C\log2-u_C\log3|,\quad p=\log_3 2 .
\]
A cycle has constant sign: the positive half-line maps to itself and zero is fixed. Its common denominator is prime to six, by the usual affine fixed-point formula and its rotation identities. Equivalently its magnitudes are \(a/d_C\) with positive integer numerator and numerator map
\[
 T_{d,\varepsilon}(a)=a/2\ (a\text{ even}),\qquad
        T_{d,\varepsilon}(a)=(3a+\varepsilon d)/2\ (a\text{ odd}),
\]
where \(\varepsilon\) is the sign, restricted to actual positive magnitudes. Fixed-time maps are injective on the union of all cycles with each one denominator and sign. We count genuine orbits once; a presentation repeating a shorter word does not create a new period. These are the standard rational-cycle and generalized \(3x+d\) correspondences. [Halbeisen–Hungerbühler, *Optimal bounds for the length of rational Collatz cycles*](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf), [Kaneda, *Two remarks on the 3x+d cycle conjecture*](https://www.fq.math.ca/Papers1/53-2/KanedaM2172015.pdf)

### Uniform state and gap bounds

For either sign, let \(A_d(X)\) count the distinct magnitudes through real height \(X\) on the union of all cycles of reduced denominator \(d\). There are absolute constants \(h<1,C\) with
\[
                     A_d(X)\le C d X^h\qquad(d\ge1,\ X\ge1).          \tag{1}
\]
One may take \(h=49/50\) entirely elementarily, or every fixed \(h>H_2(p)\). With the fixed-place Subspace Theorem there is a fixed admissible \(h<H_2(p)\).

For the elementary bound take \(X=2^k\). Given a parity word through \(k\) steps, its initial numerator occupies one residue modulo \(2^k\), since \(d\) is odd. There are at most \(d\) representatives in \([1,d2^k]\). Words with at least \(3k/5\) ones contribute \(O(d(k+1)2^{H_2(3/5)k})\), where \(H_2(3/5)<49/50\). All lower words send a real magnitude at most \(2^k\) to a magnitude at most \(3^{3k/5}+(3/2)^k\le2^{(1-c)k}\) for some fixed \(c>0\) at large \(k\). The affine correction is positive for positive cycles and negative for reflected negative cycles; its absolute value is at most \((3/2)^k\). The low-group image has a uniform bound \(A_d(2^{\lceil(1-c)k\rceil})\) by fixed-time injectivity. Substitution gives (1), with all constants independent of \(d\) and with small \(k\) absorbed in the trivial \(d2^k\). The same induction with the high-odd cutoff \((p-\eta)k\) gives every fixed \(h>H_2(p)\). Here and below finite statements at real cutoffs follow by rounding upward dyadically.

For the strict version use the full binary graph of [the finite-state theorem](../phase7/FINITE_STATE.md), its time \(t=k+\lfloor ek\rfloor\), and its normalized standard source \(R(w)=r(w)/2^t\). A numerator realizing this word satisfies \(a\equiv\varepsilon d\,r(w)\pmod{2^t}\). Thus
\[
                  a/(d2^t)=\varepsilon R(w)+j/d
\]
for some integer \(j\). In \(0<a/d\le2^k\) there are at most \(2d+2\) possible \(j\)'s, each specifying an interval of length \(2^{k-t}\) for \(R(w)\) and at most one numerator for that word and lift. Summing the strict high-odd bound for these translated arcs costs \(O(d)\), even if some arcs overlap. The low-count real images are bounded at a strictly smaller scale as before. This proves (1) with a fixed \(h<H_2(p)\), uniformly in \(d\).

For all \(0<t\le1\) and all \(h<s\le1\), (1) gives
\[
 \sum_{C:d_C=d}g_C^s\ll_s d,\qquad
       \#\{C:d_C=d,\ g_C\ge t\}\ll d\,t^{-h}.                         \tag{2}
\]
All odd magnitudes \(y\) on a positive cycle contribute \(\log(1+1/(3y))\) to its gap. On a negative cycle they contribute \(-\log(1-1/(3y))\). The global minimum of the magnitudes on a negative cycle is odd, and its odd successor \((3y-1)/2\) cannot be smaller, hence this minimum is at least 1. On \(y\ge1\), either contribution is bounded by \(1/(2y)\). For positive small magnitudes \(a/d\le1\), summing even over all \(1\le a\le d\) gives
\[
       \sum_{a=1}^d\log(1+d/(3a))
          \le\log\binom{2d}{d}\le2d\log2 .
\]
The same sum with each logarithm raised to \(s\le1\) is \(O(d)\), since \(v^s\le1+v\). Use subadditivity \((\sum b_i)^s\le\sum b_i^s\) and (1) at large magnitudes to conclude the moment estimate. For the weak estimate, count the minima below \(1/t\) by (1), then divide the total gap of cycles above that floor, \(O(d t^{1-h})\), by \(t\). In particular every individual nonzero signed cycle satisfies \(d_C\gg g_C\), with absolute implied constant. If \(u_C/n_C\) stays a fixed distance from \(p\), its denominator is at least a fixed multiple of its physical period. The all-cycle sum in (2) is uniform over all periods for each fixed denominator.

### Distinct periods with a denominator cutoff

Put \(A=D^2\), \(D,N\ge1\). Summing (2) over denominators \(d\le D\) contributes \(O(A t^{-h})\) realized cycles with gap at least \(t\). The vectors of smaller gap lie in \(|np-u|\le t/\log3\). Applying the two-dimensional lattice argument of [PERIOD_CENSUS.md](../phase7/PERIOD_CENSUS.md) to this double-sided strip shows that the number of distinct **reduced slopes** of the cycles with \(n_C\le N,d_C\le D\) is
\[
                     O\big(A+(A N^h)^{1/(h+1)}\big).                  \tag{3}
\]
The same bound counts all their period vectors after removing at most one rational ray. With a bound \(\|bp\|\gg_\mu b^{1-\mu}\), the number of **all distinct period vectors** satisfies
\[
      O_\mu\left(A+(A N^h)^{1/(h+1)}
                        +(A N^{h(\mu-1)})^{1/(\mu h+1)}\right).        \tag{4}
\]
Indeed the count is bounded by a constant times \(A t^{-h}+1+Nt+(N^{\mu-1}t)^{1/\mu}\) for all \(0<t\le1\). Take the smaller of 1 and the two individual balance scales \((A/N)^{1/(h+1)}\) and \((A^\mu/N^{\mu-1})^{1/(\mu h+1)}\). This gives (4), including when \(A\) itself dominates. Neither a fixed verification floor nor an averaged word assumption enters (1)–(4).

The next [shrinking-floor theorem](SHRINKING_FLOOR.md) strengthens the dependence on \(D\) when the gaps have a positive lower bound. In particular at a density-one set of physical periods every nonzero rational cycle has denominator exceeding any prescribed constant multiple of the square root of its period. All such conclusions are universal in the choice of word at those periods. Typical-word gcd estimates at a fixed period and type answer a different question. [Fixed-type denominator law](../phase4/DENOMINATOR_LAW.md)
