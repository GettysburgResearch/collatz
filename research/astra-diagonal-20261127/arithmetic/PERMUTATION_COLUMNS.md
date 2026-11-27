# First gate columns of Collatz's 1932 permutation

**PROPOSED written theorem.** On positive integers set \(P(3k)=2k\),
\(P(3k+1)=4k+1\), and \(P(3k+2)=4k+3\). This is the Collatz–Klamkin
permutation, also called the Conway amusical permutation in the inverse
orientation. Its inverse sends \(2k,4k+1,4k+3\) to \(3k,3k+1,3k+2\),
respectively. Call \(2\bmod3\) the gate residue.

Starting from a positive integer \(m\), run \(P^{-1}\) to the first
strictly positive time at which the value is a gate. If that gate is
\(3q-1\), write \(H(m)=q\). This is a partial map. Fix \(1<R<\infty\).
Give each actual first-gate child \(m\) of every \(X\le q<RX\) the
mass \(1/(m\log R)\), without a depth or height cutoff. The total mass
tends to one. The number \(j\) of internal steps after \(P(3q-1)\) in
the forward column and their ordered branch word
\(w=(a_1,\ldots,a_j)\in\{1,2\}^j\) have limiting mass
\[
                    p(w)=1/(4\,2^{a_1+\cdots+a_j}).
\]
At fixed \(w\), the physical child-to-parent ratio tends to
\(z(w)=4\,2^{a_1+\cdots+a_j}/3^j\).
The mass distribution on the countable word alphabet converges in total
variation. The pair (word, real ratio) converges weakly, with the
discrete topology on words. The internal length is geometric with exit
probability \(1/4\). Given its length, the letters are independent
with probabilities \(2/3,1/3\).
The limiting law has \(\mathbb E\log z=3\log(4/3)\). That is a moment of
the limiting law. A negative-tail estimate for this unbounded observable
would be needed to transfer that moment itself.

## Relation with the full positive problem

In the coordinate \(m=(x+1)/2\) of a positive odd Collatz state \(x\),
define \(F=\pi P^{-1}\), where \(\pi(3k+2)=k+1\) and \(\pi\) fixes the
other two classes. Its three branches are
\[
       F(2k)=3k,\quad F(4k+1)=3k+1,\quad F(4k+3)=k+1.
\]
The first two are the exact odd steps with exponents one and two. The
third removes a sibling: \(x=8k+5=4(2k+1)+1\) and
\(3x+1=4(3(2k+1)+1)\). Consecutive sibling removals strictly decrease
\(m>0\). Until the next accelerated odd successor there are finitely
many sibling removals followed by exactly one of the first two branches.
Conversely each sibling removal preserves the eventual-1 basin indicator
because both siblings have the same odd successor. Hence \(F\) reaches 1
from \(m\) exactly when the ordinary orbit of \(2m-1\) reaches 1. This
covers unbounded exponents. Between gate compressions \(F\) follows
\(P^{-1}\) exactly.
Prior work identified the two surviving branches and studied their formal
incidence series. The added compression recovers all odd exponents.
[Prior mixed-base theorem](../../astra-unconventional-20261126/arithmetic/MIXED_MAHLER.md)
· [Finite ordinary map and first-flight Lean kernels](AmusicalReturn.lean)
· [Simons, bounds for permutation sequences, 2022](https://arxiv.org/abs/2205.10582)
· [Karras and de Weger, modular determinants of the full permutation, 2026](https://arxiv.org/abs/2601.15463)

The \(H\)-fibre of \(q\) is the single column
\[
         P(3q-1),\ P^2(3q-1),\ \ldots,\ P^\tau(3q-1),
\]
where \(\tau\) is the first positive forward gate time, with all positive
iterates included if it never occurs. The initial gate enters this list
if the orbit returns there before meeting a different one. An element
at time \(j+1\) has precisely \(j\) intervening nongates before the
initial gate in the inverse direction. Conversely inverting a finite
first-gate path puts its child in this list. Different columns are
disjoint, because the first gate determines the root. This argument
allows finite gate-free cycles, infinite gate-free rays and infinite
individual columns.

Universal convergence is equivalent to both of the following: every
\(m>1\) has \(H(m)\) defined; every such \(m\), under successive
defined applications of \(H\), eventually reaches 1. Indeed
\(P(1)=P^{-1}(1)=1\), so \(m>1\) cannot reach 1 during an ungated
permutation flight. A finite \(F\)-passage to 1 consists of complete
flights and a last gate compression. Conversely the finite flights
expand to the original \(F\)-path. Every finite permutation cycle
\(C\) obeys this gate balance for each real \(F\)-invariant \(b\):
\[
  \sum_{g\in C,\ g\equiv2\ (3)} b(g)
       =\sum_{g\in C,\ g\equiv2\ (3)} b((g+1)/3).
\]
It follows by summing \(b(Pn)=b(\pi n)\) around the cycle. A gate-free
cycle gives an empty identity. Neither this balance nor bijectivity
proves universal first-gate return.

## Exact finite column laws

The seed child is \(m_0=4q-1\). At a nongate the allowed forward
branches are \(y\mapsto2y/3\) when \(y=0\bmod3\) and
\(y\mapsto(4y-1)/3\) when \(y=1\bmod3\). Name them 1 and 2.
For a prescribed word, exactly one residue class of \(q\bmod3^j\)
realizes all \(j\) internal letters. After \(t\) letters write
\(3^t m_t=4\,2^{S_t}q-c_t\), with \(S_t\) the letter sum and \(c_t\)
an integer depending on the word. On the realizing class modulo \(3^t\),
changing \(q\) by \(3^t\) changes \(m_t\) by the ternary unit
\(4\,2^{S_t}\). Exactly one lift gives the prescribed next residue.
The endpoint itself may be a gate. The word records the steps used to
reach it.

On that class \(m_j=z(w)q+O_w(1)\). Harmonic summation on an arithmetic
progression gives
\[
 \lim_{X\to\infty} \frac1{\log R}
   \sum_{\substack{X\le q<RX\\w\ {\rm realized}}}1/m_j
       =1/(3^jz(w))=p(w).
\]
The ratio convergence is uniform at fixed word. Finite sums of these
limits cover every bounded length.

## Tightness over arbitrarily long physical columns

The number of ordinary \(m\in[M,2M)\) surviving the first \(k\)
inverse steps without an output gate is
\[
             O\big(M(3/4)^k+2^k\big).                         \tag{1}
\]
For each inverse word of allowed letters with clock \(S\), one dyadic
class modulo \(2^S\) occurs. An even branch consumes one specified
bit and an input \(1\bmod4\) consumes two. The endpoint numerator
after clearing a word's denominator has odd coefficient \(3^k\); hence
the classes lift successively as asserted. Summing \(M/2^S+1\) over
the \(2^k\) words proves (1).

Each child at internal depth \(j\) survives its first \(j\) inverse
steps. At every internal forward step \(2y/3\le P(y)\le4y/3\).
Since \(3q\le4q-1\le4q\), we have
\[
            3q(2/3)^j\le m_j\le4q(4/3)^j.                     \tag{2}
\]
Thus in the shell above and \(q\in[X,RX)\),
\(j\ge c|\log(M/X)|-C_R\) for an absolute \(c>0\).
If \(j\ge K\) as well, (1) and (2) bound the shell's \(1/m\) mass by
\[
     O_R\!\left(\exp[-\delta\max(K,|\log(M/X)|)]+M^{-\eta}\right)
                                                                  \tag{3}
\]
for absolute \(\delta,\eta>0\). Indeed take the nonnegative integer
part of \(\min(\max(K,c|\log(M/X)|-C_R),\log M/(2\log2))\) as the
surviving depth. Dividing (1) by \(M\) bounds the second term by
\(M^{-1/2}\). The first is bounded by the sum of the exponential and
a fixed negative power of \(M\). Distinct roots cannot multiply the
bound on one child.

Fix \(M_0\) and sum (3) over dyadic \(M\ge M_0\). The exponential
part is \(O_R((K+1)e^{-\delta'K})\); the power part is
\(O_R(M_0^{-\eta})\). Among the finitely many smaller \(m\), each
has at most one finite first-gate root. Eventually none lie over
\([X,RX)\). This uses no algorithm deciding which small sources have
a first gate. Taking the limsup in \(X\) and then sending \(M_0\)
to infinity leaves an exponentially decaying bound in \(K\). This
proves tightness, finiteness of the original sums at fixed \(X\), and
the stated all-depth convergence.

## Boundary for pointwise estimates

Arbitrarily large ordinary \(q\) satisfy \(4q-1\equiv0\bmod3^j\).
Such a column contains \(m=(4q-1)(2/3)^j\). Even one \((q/m)^s\) is
therefore arbitrarily large as \(j\) varies, for every fixed \(s>0\).
A one-column contraction in a bare power of height fails although the
limiting Mellin transform
\[
 \mathbb E[z^{-t}]
 =\frac{4^{-1-t}}{1-3^t(2^{-1-t}+4^{-1-t})}
\]
is below one for small positive \(t\). The formula holds wherever
the displayed geometric sum converges. Positive \(\mathbb E\log z\)
gives the local strict inequality. The averaged measure does not bound
a specified long first flight or the mass at a particular cycle.
