# Compression can leave almost every five-ray merger undecided

**Status: SOURCE-QUALIFIED theorem; elementary counterexample to a counting transfer.**

The map throughout is the positive ordinary shortcut map
\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]
A meeting allows two independent nonnegative integer clocks. For a finite interval
of parameters \(I\) and an integer \(H\ge0\), put
\[
U_H(I)=\#\{t\in I:T^i(t)\ne T^j(5t+1)\text{ for every }0\le i,j\le H\}.
\]
This is a **finite-clock unresolved count**. It is not the number of pairs that
never meet. In particular, the results below do not supply Collatz counterexamples.

The starting point is the uniform joint-label compression in PR #146, frozen at
`561d48a4d3a793a59b1cdf0406062ae1a6d47515`,
`research/upper-bit-mergers/AFFINE_RAYS.md`, sections "Compressing the parameters
of the five-ray test" and "A sharper bound from the common binary digits".
At \(h=\lceil\log_2N\rceil\), an interval of \(N\) parameters presents only
\(O(N^{0.967})\) distinct endpoint-and-odd-count tuples
\[
L_h(t)=\bigl(T^h(t),s_h(t),T^h(5t+1),s_h(5t+1)\bigr).       \tag{1}
\]
That theorem counts questions. The results here show, on the actual ordinary
map, why it cannot by itself count answered parameters.

## FR-001: an elementary interval with no finite-clock answers

For every integer \(N\ge2\), set \(h=\lceil\log_2N\rceil\) and
\[
I_N=\{4\cdot6^h,4\cdot6^h+1,\ldots,4\cdot6^h+N-1\}.
\]
Then
\[
                         U_h(I_N)=N.                       \tag{2}
\]
The source-qualified compression count in (1) nevertheless applies to this
same interval, since its constant is independent of the interval's location.

For completeness, here is the elementary obstruction to short meetings. A
length-\(i\) parity word with \(p\) odd inputs has affine formula
\[
                         T^i(x)=\frac{3^p x+A}{2^i},
\qquad 0\le A\le3^i-2^i<3^i.                               \tag{3}
\]
The formula refers to inputs realizing that word. The offset inequality also
holds for the empty word. Composition proves it by induction; the all-odd word
has the maximal offset \(3^i-2^i\).

A meeting of \(t\) and \(5t+1\) at clocks \(i,j\le H\) therefore implies
\[
 (2^j3^p-5\cdot2^i3^q)t
                  =2^i(3^q+B)-2^jA.                       \tag{4}
\]
The integer coefficient on the left is nonzero, by its prime factor 5. Since
\(p\le i\), \(q\le j\), and the offsets obey (3),
\[
                         t<3\cdot6^H.                     \tag{5}
\]
This gives (2). No probabilistic, density, or transcendence input is used in
FR-001. It restates the incompatible-slope estimate in the pinned source in a
form that directly tests the proposed counting transfer.

## FR-002: almost all questions remain unanswered even in a natural shell

Let \(c=\log_2 3\). For every fixed \(0<\epsilon<c/2\), there is
\(\kappa_\epsilon>0\) such that, for all sufficiently large integers \(h\),
\[
U_{\lfloor(1+c/2-\epsilon)h\rfloor}
   ([2^h,2^{h+1})\cap\mathbb N)
       =2^h-O_\epsilon(2^{(1-\kappa_\epsilon)h}).            \tag{6}
\]
The cutoff is approximately \((1.79248-\epsilon)h\), with **both** clocks
permitted anywhere up to it. An explicit, deliberately coarse instance is
\[
\boxed{\quad
h\ge2^{60}\quad\Longrightarrow\quad
U_{\lfloor7h/4\rfloor}([2^h,2^{h+1}))
          \ge2^h-2^{9999h/10000}.
\quad}                                                     \tag{7}
\]
The enormous sufficient threshold in (7) comes from a direct use of the
Baker--Wüstholz constant. It is an effective mathematical bound, not a range
claimed to have been enumerated.

Only the fixed-algebraic-number lower bound for a nonzero logarithmic form is
external. There is no predecessor-density, cycle-exclusion, or convergence
assumption in (6) or (7).

### 1. A typical parity prefix stays high long enough

The first \(h\) parity bits of \(x\) are in bijection with \(x\bmod2^h\).
Indeed, once \(j\) bits are fixed, changing the next bit of the input changes
the parity of the \(j\)-th state by an odd coefficient. Both \(t\) and \(5t+1\),
as \(t\) ranges over a complete binary block of length \(2^h\), therefore sample
all \(h\)-bit parity words once. Independence between the two arms is unnecessary.

Fix \(\delta>0\). On either arm, let \(q_i\) count its odd inputs in the first
\(i\) steps. A binomial exponential estimate and a union bound give
\[
 \#\{t:\text{some arm and some }1\le i\le h
                       \text{ has }q_i<i/2-\delta h\}
 \le 2h\,2^h e^{-2\delta^2h}.                               \tag{8}
\]
Here is a short derivation of the estimate used in (8). For \(i\) independent
fair bits with sum \(Q\),
\(\mathbb E e^{-\lambda(Q-i/2)}=\cosh(\lambda/2)^i
\le e^{i\lambda^2/8}\).
Exponential Markov with \(\lambda=4\delta h/i\) bounds the lower tail by
\(e^{-2\delta^2h^2/i}\le e^{-2\delta^2h}\). This uses only
\(\cosh x\le e^{x^2/2}\), obtained by integrating \(\tanh x\le x\).

Outside this exceptional set, positivity of the affine offset implies, for
\(x=t\) or \(5t+1\) and \(0\le i\le h\),
\[
 \log_2 T^i(x)\ge h-i+cq_i
    \ge h-(1-c/2)i-c\delta h
    \ge(c/2-c\delta)h.                                     \tag{9}
\]
After time \(h\), each further shortcut step decreases a positive value by at
most a factor of two. Set \(\delta=\epsilon/(2c)\). Through the clock in (6),
every state on both arms is consequently at least
\[
                              2^{\epsilon h/2}.            \tag{10}
\]

For the explicit instance (7), use \(\delta=1/100\) and \(H=\lfloor7h/4\rfloor\).
The exact integer comparison \(2^{19}<3^{12}\) gives \(c>19/12\), so (9) and
the extra at most \(3h/4\) halvings give
\[
 \log_2\min_{x\in\{t,5t+1\},\,0\le i\le H}T^i(x)
   \ge\left(\frac{49c}{100}-\frac34\right)h
   >\frac{31h}{1200}>\frac h{40}.                          \tag{11}
\]
The exceptional count in (8) is at most
\(2h\,2^h e^{-h/5000}\le2^{9999h/10000}\) for \(h\ge2^{60}\).
For example, write \(2^r\le h<2^{r+1}\), \(r\ge60\), and use
\(10000(r+2)<2^r\) to absorb \(2h\); also \(e>2\).

### 2. A meeting while both arms are high is arithmetically impossible

For any positive path, direct multiplication of its step ratios yields
\[
 \log T^i(x)=\log x+p\log3-i\log2
       +\sum_{z\text{ odd input on the prefix}}
                            \log(1+1/(3z)).                \tag{12}
\]
If the two arms meet at \(i,j\le H\), with odd counts \(p,q\), and all their
states before the meeting are at least \(m\), (12) gives
\[
 0<|\Lambda|\le\frac1{5t}+\frac{2H}{3m},\qquad
 \Lambda=(p-q)\log3-(i-j)\log2-\log5.                       \tag{13}
\]
The strict nonvanishing is unique factorization: a rational number supported
on primes 2 and 3 cannot equal 5. This is the step that would fail for a
compatible-slope comparison such as \((t,3t+1)\).

The fixed-number Baker--Wüstholz theorem supplies \(A,C>0\) with
\(|\Lambda|>A(2+H)^{-C}\). With (10), the upper bound in (13) is exponentially
small in \(h\), whereas this lower bound is a negative power of \(h\). They
contradict each other for all sufficiently large \(h\). Equations (8)--(10)
prove (6).

To verify the explicit threshold in (7), the published constant is enough.
The theorem for \(n\) logarithms in a field of degree \(d\) uses
\[
 C(n,d)=18(n+1)!\,n^{n+1}(32d)^{n+2}\log(2nd).
\]
For \((2,3,5)\), take \(n=3,d=1\); the modified heights are
\(1,\log3,\log5\), and the coefficient height is at most \(\log H\) here.
All three logarithms \(\log6,\log3,\log5\) are below 2, since
\(e^2>1+2+2+8/6+16/24=7\). Thus the constant multiplying \(\log H\) is less
than the exact integer
\[
 18\cdot24\cdot81\cdot32^5\cdot8
       =9393093476352<10^{13}.                              \tag{14}
\]
Writing \(C_0=10^{13}\), the resulting lower bound is
\(|\Lambda|>(2h)^{-C_0}\). By (11), the upper bound in (13) is less than
\(2h\,2^{-h/40}\). For \(2^r\le h<2^{r+1}\), \(r\ge60\),
\[
40(C_0+1)(r+2)<2^r\le h,
\]
so \(2h\,2^{-h/40}<(2h)^{-C_0}\). The strict integer inequality at \(r=60\)
holds by direct arithmetic and propagates to larger \(r\) by doubling.
This proves the stated sufficient threshold.

**External-source verification.** The formula just used is reproduced by
G. Wüstholz, *One Century of Logarithmic Forms*, section 5, printed pages 5--6,
in *A Panorama in Number Theory or the View from Baker's Garden* (Cambridge,
2002). The author is a coauthor of the original theorem. The publisher's
[ten-page excerpt](https://assets.cambridge.org/97805218/07999/excerpt/9780521807999_excerpt.pdf)
was opened, and its printed page 6 was visually inspected in this work. It states
the modified-height definitions and the displayed constant. The original paper
is A. Baker and G. Wüstholz, *Logarithmic forms and group varieties*, J. reine
angew. Math. **442** (1993), 19--62,
[DOI](https://doi.org/10.1515/crll.1993.442.19). The argument here imports that
theorem; it does not independently reprove its transcendence-theoretic content.

## FR-003: the exact missing weight in the proposed transfer

Let \(f(n)\) denote the actual ordinary merger component. In a fixed interval
\(I\), partition parameters into the fibers \(F_\ell\) of the tuple (1). Since
equal tuples give a meeting on each corresponding arm,
\[
 [f(t)\ne f(5t+1)]\quad\text{is constant on every }F_\ell.
\]
Consequently the permanent failure count is **exactly**
\[
 B(I)=\sum_{\ell:\ f(\ell_{\rm first})\ne f(\ell_{\rm third})}
                                                    |F_\ell|.  \tag{15}
\]
There is no removal of the factors \(|F_\ell|\) in this identity. A bound on
the number of labels only bounds the number of summands.

By FR-001, a uniform label count \(O(N^{0.967})\) coexists with \(N\) unanswered
ordinary pairs at the compression clock. By FR-002, on the natural shells it
coexists with \(N-O(N^{1-\kappa})\) unanswered pairs even at clocks strictly
longer than the compression clock. Thus it is false to read the compression
count as a bound on the finite-clock unresolved count. These theorems do not
assert that the same parameters remain unresolved at unrestricted clocks.

The pinned source's criterion \(B(X)=O(\log X)\) along an unbounded sequence
would prove full Collatz. To reach it from compression requires an additional
theorem controlling either successful meetings for the retained questions or
the **weighted** mass of retained questions that never meet. Neither theorem
has been established here. Component thickness does not supply this weight or
an answer for the endpoints of a retained pair.

## Evidence, negative controls, and unresolved approaches

[`check_finite_clock_barrier.py`](check_finite_clock_barrier.py) uses only exact
integers and fractions. It checks the rational margins in (11), (14), and the
dyadic threshold comparisons; all parity words through length 12; the complete
pair of word lists through length 6; the first 12 explicit intervals in FR-001;
and the marginal parity-word bijections on the first 12 positive dyadic shells.
It records the label and unresolved counts actually computed. It does not claim
to enumerate (7), establish an unrestricted merger, or check Baker--Wüstholz
by finite computation. Its negative controls exhibit a compatible-slope pair
meeting at one step and a five-ray pair unanswered at its short cutoff but
subsequently meeting at 1.

Two other directions were investigated but are not claimed as results:

- Restricting the universal five-ray test to parameters prime to three has not
  been proved sufficient. Moreover, **both** endpoints are ternary units only
  when \(t\equiv2\pmod3\), not for every parameter prime to three. The elementary
  least-counterexample descent can land on \(t=3n/5\) when \(5\mid n\), so the
  omitted residue class cannot simply be discarded.
- Some exact paired inverse returns were found, for example on the classes
  \(t=64u+11\) and \(t=64u+35\), both arms at clock 6 return respectively to
  \((27u+5,5(27u+5)+1)\) and \((9u+5,5(9u+5)+1)\).
  These are ordinary identities on positive lifts. They do not cover every
  hypothetical failed parameter, and no universal branching argument follows.

PR #149 was also consulted at the supplied head
`92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
`research/forward-inverse-defect/CLOSURE_BOUNDARY.md`, to preserve the distinction
between all ordinary input bounds and selected or almost-everywhere inverse
behavior. No theorem from that file is needed for FR-001--FR-003.
