# An explicit finite harmonic condition with a complete Lean implication

**Kernel-checked sufficient criterion for the full positive Collatz conjecture.
The finite-sum estimate required by that criterion is OPEN.**

Use the actual shortcut map
\[
 T(x)=
 \begin{cases}
 x/2,&x\text{ even},\\
 (3x+1)/2,&x\text{ odd},
 \end{cases}
 \qquad
 q_j(x)=\#\{0\le i<j:T^i(x)\text{ odd}\}.
\]
For an integer \(N\ge1\), define the finite set and rational number
\[
 \mathcal S_N=
 \{\,r:1\le r<2^N,\quad 5j\le8q_j(r)\text{ for every }0\le j\le N\,\},
 \qquad
                         H_N=\sum_{r\in\mathcal S_N}\frac1r.       \tag{1}
\]
Every condition in (1) is an ordinary finite integer calculation. No
probability distribution, stationary measure, density theorem or cycle
classification is an input to its formal implication.

The new Lean theorem says:
\[
 \boxed{\quad
  \bigl[\forall B\ge1\ \exists N\ge1:\ H_N<1/B\bigr]
  \ \Longrightarrow\
  \bigl[\forall x\ge1\ \exists h\ge0:\ T^h(x)=1\bigr].
 \quad}                                                          \tag{2}
\]

The same file proves the finite form: a single strict inequality
\(H_N<1/B\) certifies convergence of every positive integer at most \(B\).
It defines (1) directly as a finite filtered sum of rational reciprocals
and proves every link to the ordinary conclusion. The hypothesis in the
left box has not been proved.

[BinaryPrefixCriterion.lean](BinaryPrefixCriterion.lean), theorem
BinaryPrefixCriterion.collatz_of_small_finite_mass, is the formal proposal.
Its dependencies are the repository's actual shortcut map, finite
iteration, odd count and exact binary-prefix lift. All arithmetic
arguments below through (6), including the small input certificates,
are inside that Lean implication.

## Why every hypothetical least bad input is detected

Suppose a positive input fails to reach one. Choose the least positive
bad input \(m\) among **all** bad inputs. It is no larger than the supplied
failure; it need not belong to the same component. Every actual iterate
of \(m\) is positive and bad, hence at least \(m\). Direct kernel
calculations prove convergence for every input from 1 through 32.
Therefore \(m\ge33\). The first step also shows that \(m\) must be odd.

For every odd \(x\ge33\),
\[
                         (3x+1)^5\le256x^5.                       \tag{3}
\]
One fully integral verification writes \(x=33+v\) and expands the
nonnegative difference as
\[
 13v^5+1740v^4+87840v^3+1998720v^2+17978880v+18660608.
\]
For an even step the corresponding identity is
\(2^5T(x)^5=x^5\). Multiplying the appropriate inequalities along
the actual orbit gives
\[
       2^{5j}T^j(m)^5\le2^{8q_j(m)}m^5.
\]
Because \(T^j(m)\ge m>0\), cancel \(m^5\) and compare powers of two:
\[
                            5j\le8q_j(m).                         \tag{4}
\]
The very same fixed ordinary \(m\) therefore passes every prefix gate.
This does not infer an ordinary seed from changing finite witnesses.

Now fix any \(N\ge1\) and put \(r=m\bmod2^N\). Oddness gives
\(1\le r<2^N\) and \(r\le m\). Exact parity-cylinder lifting preserves
the grades at **all** clocks \(j\le N\): the difference of the sources
is a multiple of \(2^N\), and the ordinary affine lift applies at
clock \(j\) with the remaining \(N-j\) bits. Thus
\(r\in\mathcal S_N\), and
\[
                           H_N\ge\frac1r\ge\frac1m.                \tag{5}
\]
If the supplied bad input were at most \(B\), then \(m\le B\) would
force \(H_N\ge1/B\) at every \(N\ge1\). This proves the finite
certificate and (2).

The positive clock restriction matters: the formal positive-source
set at depth zero is empty, so \(H_0=0\). Every certificate and the
full implication explicitly require \(N>0\).

## The written converse and the exact ordinary atoms

There is also a self-contained written converse. Let
\(D=\bigcup_{N\ge1}\mathcal S_N\), and set
\[
 d=H_2(5/8)<1,
 \qquad H_2(t)=-t\log_2t-(1-t)\log_2(1-t).
\]
In a shell \(2^j\le r<2^{j+1}\), membership in some
\(\mathcal S_N\) implies \(N\ge j+1\). The first \(j\) binary
decisions already have at least \(5j/8\) odd departures. The
shortcut parity-prefix bijection gives one residue modulo \(2^j\)
per binary word, and each such residue occurs once in this shell.
The binomial exponential bound gives
\[
 \#(D\cap[1,X])\ll X^d,\qquad
 \sum_{\substack{r\in D\\r>X}}\frac1r\ll X^{d-1}.                 \tag{6}
\]

For each fixed \(r\), it is in the principal interval once
\(2^N>r\). After that it either persists in every later gate or
disappears permanently. Dominated convergence with the summable
weights \(1/r\) proves
\[
 \lim_{N\to\infty}H_N
   =\sum_{\substack{r\ge1\\5j\le8q_j(r)\text{ for all }j}}\frac1r. \tag{7}
\]
If an input reaches one, its subsequent shortcut parities repeat
one odd and one even step. Its odd frequency tends to \(1/2\),
so it eventually fails the \(5/8\) gate. Hence full Collatz would
make (7) zero. Conversely any counterexample supplies the fixed
positive atom (5). Thus vanishing of this particular finite sum is
equivalent to full Collatz, as written mathematics.

The Lean file proves the entire sufficient direction (2) and the
finite certificate; it does not formalize this entropy count,
dominated convergence or the converse.

## A rational decreasing upper reserve

The harmonic sequence itself need not decrease. A parent least
residue \(r<2^N\) has two next binary lifts, \(r\) and \(r+2^N\).
The first can retain its old reciprocal. The only new reciprocal
is at most \(2^{-N}\). If \(P_N\) is the fair-bit probability of
passing the gate through \(N\), this gives
\[
                         H_{N+1}\le H_N+P_N.                     \tag{8}
\]
Use the unique empty parity cylinder at depth zero for this
counting statement: \(P_0=1\), \(H_0=0\), and the source one is
born on its first odd digit.

At an accepted word let \(D_N=8q_N-5N\ge0\). The next fair bit
changes this debt by \(+3\) or \(-5\); the latter branch is killed
when the result would be negative. The elementary reserve obeys
\[
 1+\tfrac12(D+8)+\tfrac12\mathbf1_{\{D\ge5\}}D\le D+5.            \tag{9}
\]
Define
\[
 V_N=\mathbb E_{\rm fair\ bits}
             [\,\mathbf1_{\rm gate}(D_N+5)\,].
\]
Then \(P_N+V_{N+1}\le V_N\). Combining with (8), the rational
sequence \(H_N+V_N\) is nonincreasing, starting at five.

A binomial Chernoff estimate gives
\[
 P_N\le\beta^N,\qquad
 \beta=\frac43\left(\frac35\right)^{5/8}<\frac{97}{100},
 \qquad
 0\le V_N\le(3N+5)\beta^N.
\]
Thus the reserve vanishes and the augmented sequence has the
same limit (7). Its exact values require only the finite debt
recurrence: each debt \(D\) sends one count to \(D+3\), and, when
\(D\ge5\), one to \(D-5\). Equation (9) is also a Lean theorem.
The birth count, binomial estimate and global reserve use are
written arguments with exact finite controls.

The reserve limits how much new harmonic mass can be born. It
does not bound how long an existing seed can keep passing the
gate. In particular \(P_N\to0\) does not imply \(H_N\to0\):
the probability is a count normalized by \(2^N\), while the
harmonic mass can retain a fixed ordinary source.

## Relation to the earlier trace and evidence

The [global exponent-prefix trace](escape/GLOBAL_PREFIX_TRACE.md)
uses the original geometric exponent law, has gate \(4A_j\le7j\),
and separates escape from cycles by a centered affine parameter.
The present binary gate is sharper, using the elementary
convergence certificates through 32. It admits a short complete
formal implication without the ternary posterior machinery.
Both criteria preserve ordinary atoms and leave their vanishing
open. The birth-reserve argument follows the same principle,
with two binary children and reserve five in place of the
geometric sibling family and reserve nine.

The [control](check_binary_prefix.py) reconstructs the actual
least sources and endpoints by the binary affine lift through
clock 22. At clocks through 11 it independently scans every
positive residue and compares the complete sets. It checks
each parent's reciprocal birth charge, matches the entire
debt histogram with the separate fair-bit recurrence, and
encloses the finite harmonic sums with integer floors and
explicit error counts. The numerical rows are
[BINARY_PREFIX_CONTROLS.json](BINARY_PREFIX_CONTROLS.json).

The root compiled the formal theorem with warnings treated as
errors. The escape agent independently rebuilt and reconstructed
its mathematical chain, including the positive-clock requirement
and the reciprocal inequality direction. Fresh checkpoint replay
and exact source hashes are recorded with the publication packet.

**Next mathematical obligation.** Prove, for the explicitly
defined sum (1), that for every positive integer \(B\) some
positive depth has \(H_N<1/B\). The rest of the sufficient
implication is already checked in Lean. No such estimate is
claimed in this checkpoint.
