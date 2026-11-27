# All fixed gate clocks on genuine ordinary paths

**PROPOSED written theorem.** Use \(H,F,P,m,q\) from the
[first-column theorem](PERMUTATION_COLUMNS.md). Fix a positive integer
\(t\) and \(R>1\). Give each *actual* \(m\) for which \(H^t(m)=q\)
exists and \(X\le q<RX\) the weight \(1/(m\log R)\). From \(q\) toward
\(m\), record the \(t\) successive internal words \(w_1,\ldots,w_t\).
Their weighted joint law converges in total variation to \(t\)
independent copies of \(p(w)=1/(4\,2^{S(w)})\). The \(t\) real ratios
of consecutive child to parent converge jointly in distribution with
these words to \((z(w_1),\ldots,z(w_t))\), where
\(z(w)=4\,2^{S(w)}/3^{|w|}\). There is no cutoff on the realized
words or any intermediate physical state.

For a prescribed tuple let \(J=\sum_i|w_i|\) and \(S=\sum_iS(w_i)\).
Each gate child is obtained by \(u\mapsto 4u-1\), followed by the
ordinary partial permutation steps of its word. Composing the lifts in
the first-column theorem gives exactly one class of \(q\bmod3^J\).
Indeed after \(r\) internal letters and \(h\) gates, changing \(q\) by
\(3^r\) changes the state by the ternary unit \(4^h2^{S_r}\).
The final state is \(4^t2^S q/3^J+O_{\boldsymbol w}(1)\).
Every intermediate state is positive on large realizers. For fixed
tuple the harmonic shell sum consequently tends to
\(4^{-t}2^{-S}=\prod_i p(w_i)\). Each backward construction is a
genuine first-gate flight even when its last point is itself a gate:
in forward \(H\)-time only strictly positive permutation times count.

For completeness the all-depth tightness argument must now include
the other gates. The slow map has three dyadic input words, of lengths
\(1,2,2\) and probabilities \(1/2,1/4,1/4\) on uniform dyadic input.
The last word is the gate. Its affine numerator slope is one; the
other slopes are three. Hence every prescribed slow word defines
one residue class modulo the power of two of its total binary clock.
The number of \(m\in[M,2M)\) having at most \(t\) gates in the first
\(k\) slow steps is bounded by
\[
       C_t(k+1)^t\{M(3/4)^k+2^k\}.                               \tag{1}
\]
Sum the class counts over the at most \(t\) gate positions and all
other choices. Fixing \(h\) gate positions gives total dyadic mass
\((1/4)^h(3/4)^{k-h}\) and at most \(2^k\) words. Each indicated
\(m\) with total internal length \(J\) has at most \(t\) gates in
its first \(J\) slow steps. Its ratio is squeezed by
\[
              3^t(2/3)^J \le m/q\le4^t(4/3)^J.
\]
For \(J\ge K\) repeat the shell argument with
\(k=\lfloor \min\{\max(K,c|\log(M/X)|-C_{t,R}),
                        (\log M)/(2\log2)\}\rfloor_+\).
The polynomial in (1) can be absorbed into fixed smaller positive
exponents in both terms of the bound. Finitely many small \(m\)
have at most one \(H^t\) root each. This proves tightness after \(X\)
tends to infinity; it does not use recurrence of every positive source.
In particular a slowly increasing clock \(t(X)\to\infty\) may be chosen
by diagonalization to have word-law total variation tending to zero.
This existential choice does not give a rate for \(t(X)\).

## Arbitrary finite real profiles in the basin of 1

For any \(t\), any positive vector \(\lambda_1,\ldots,\lambda_t\), and
any \(\epsilon>0\), there are arbitrarily large actual positive
\(H\)-paths visiting 1 after this finite segment whose consecutive
child-to-parent ratios belong to
\((e^{-\epsilon}\lambda_i,e^\epsilon\lambda_i)\), in outward order.
Indeed the numbers \(4\,2^{a}/3^j\), \(j\le a\le2j\), are dense in
the positive reals. In logarithms this follows by density of the
fractional parts of \(j\log_2 3\): the integer \(a\) near
\(j\log_2 3+\log_2(\lambda_i/4)\) can be chosen with arbitrarily
small error and satisfies the two inequalities for large \(j\).
Select a word of length \(j\) with that letter sum at each stage.
The ternary congruence of the prescribed tuple can be realized by
arbitrarily large \(q=(2\cdot4^r+1)/3\): these are the iterates of
\(u\mapsto4u-1\) at \(1\), and they exhaust every class modulo \(3^J\)
as \(r\) varies. In fact \(4\) has order \(3^J\bmod3^{J+1}\), as
\(v_3(4^{3^h}-1)=h+1\) by cubing and induction. Thus the required
congruence \(2\cdot4^r\equiv3q-1\bmod3^{J+1}\) has a solution.
Every such \(q\) hits 1 in exactly \(r\) gate steps (each internal
word empty). At all sufficiently large chosen \(q\), the actual
ratios approximate the finitely many selected homogeneous ratios.

In particular even simultaneous supercritical forward growth at every
one of any prescribed number of first-gate steps occurs on genuine
convergent orbits. A uniform contraction at a fixed gate depth in a
bare power of height cannot prove convergence. The growth witness
varies with the prescribed length. The finite cylinders alone give
no single point whose forward path grows forever.

## The exact individual obligation

For odd \(x=2m-1\), a gate input to \(F\) means \(x=5\bmod8\).
All nontrivial ordinary predecessors of 1 under the accelerated odd map
have the form \(x=(2^a-1)/3\) with even \(a\ge4\), hence lie in that
residue. Thus every convergent \(m>1\) has a gate. A never-gated
\(m>1\) either lies on a nontrivial gate-free finite permutation cycle
or has a distinct inverse-permutation ray tending to infinity. The
first-gate assertion is consequently precisely the \(5\bmod8\)
residue-avoidance problem of Yolcu, Aaronson and Heule, in the
coordinate used here. A positive answer would still leave the
possible nonconvergence of an infinite sequence of finite first
flights. [Yolcu, Aaronson and Heule, §4.5](https://www.cs.cmu.edu/~mheule/publications/collatz.pdf)
