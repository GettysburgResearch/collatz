# A spectral literature check: reciprocal departure weights erase escape

**Status.** An elementary unconditional operator calculation. It is not a proof of Collatz. The purpose is to test whether a proposed spectral tool retains the ordinary obstruction before using its claimed gap.

During the six-hour literature attack we inspected James C. Hateley, *The Collatz Conjecture and the Spectral Calculus for Arithmetic Dynamics*, version 6, posted 28 January 2026. Its equations (1)–(3) use the **unaccelerated** map

\[
 C(n)=\begin{cases}n/2&2\mid n,\\3n+1&2\nmid n,\end{cases}
 \qquad (Pf)(y)=\sum_{C(x)=y}\frac{f(x)}x.
\]

The source asserts a principal eigenvalue 1 and, in several places, a positive fixed profile with inverse-linear decay. We do not import these assertions. The calculation below applies to this exact displayed operator; rescaling it or changing its weights defines a different operator. [Primary source, v6, equations (2)–(3), (33), (94)–(95), and Remark 5.35](https://www.preprints.org/manuscript/202511.1440/v6)

## An explicit norm bound, with no hypothesis about any orbit

Put \(X_\sigma=\{f:\sum_{n\ge1}|f(n)|n^{-\sigma}<\infty\}\). On \(X_1\),

\[
 \boxed{\ \|P^3f\|_{X_1}\le\tfrac18\|f\|_{X_1}.\ }
 \tag{1}
\]

Indeed each source \(m\) makes a unique three-step contribution to \(C^3m\), of coefficient \([m\,Cm\,C^2m]^{-1}\). After dividing by the terminal height to take the norm, its ratio to the initial norm \(1/m\) is

\[
 \frac1{Cm\,C^2m\,C^3m}\le\frac18.
\]

The inequality follows because every three consecutive positive states have product at least eight. If their first state is at least eight, positivity suffices. The seven smaller starts give products \(8,8,150,8,640,180,1694\). Triangle inequality handles collisions between different sources, first for finite support and then by norm convergence. The universal product bound and its reciprocal consequence are checked in [ReciprocalOperator.lean](ReciprocalOperator.lean).

The positive vector supported on \(\{1,2,4\}\), with values \(h(1)=h(2)=1\) and \(h(4)=2\), satisfies \(Ph=h/2\). Thus

\[
                        r(P|X_1)=\tfrac12 .                         \tag{2}
\]

In particular there is no nonzero fixed vector in this space. No finite computation of a large Collatz range is used.

## Every polynomial weighted space has the same spectral radius

For any fixed real \(\sigma\), the normalized column at \(m\) has norm

\[
 \frac{m^{\sigma-1}}{(Cm)^\sigma}\le \frac{K_\sigma}{m},
 \qquad K_\sigma=\max(2^\sigma,4^{-\sigma}),
\]

since \(m/2\le Cm\le4m\). Keeping only columns \(m\le N\) gives a finite-rank operator, and the discarded operator norm is at most \(K_\sigma/(N+1)\). Hence \(P\) is compact on every \(X_\sigma\).

Moreover \(P:X_\sigma\to X_{\sigma-1}\) is bounded, by the same comparison of \(Cm\) and \(m\). A nonzero eigenvector with eigenvalue \(\lambda\ne0\) therefore belongs to \(X_{\sigma-j}\) for every integer \(j\ge0\), because \(f=\lambda^{-j}P^jf\). Choose \(j\) so that \(\sigma-j\le1\). Then \(f\in X_1\), and (1) forces \(|\lambda|\le1/2\). Compactness says every nonzero spectral value is an eigenvalue. The cycle vector above belongs to every \(X_\sigma\), so (2) holds for every fixed real \(\sigma\).

The compact-operator spectral step is standard functional analysis, stated as written mathematics here. The Lean kernel does not formalize compactness or the spectrum.

## Why this gap says nothing about escape

Along an injective ordinary trajectory \(n_0,n_1,\ldots\), the departure product obeys

\[
       \prod_{i<k}\frac1{n_i}\le\frac1{k!},
\]

because its positive integer states are distinct. The operator suppresses even a hypothetical escaping trajectory superfactorially. Its norm decay is therefore compatible with the very behavior a closing proof would have to exclude.

There is also a direct normalization check. The correct finite-support identity

\[
             \sum_y(Pf)(y)=\sum_x\frac{f(x)}x
\]

equates **two different functionals**. It does not make \(L(f)=\sum_xf(x)/x\) invariant. At \(f=\delta_1\), \(Pf=\delta_4\), so \(L(f)=1\) while \(L(Pf)=1/4\). A profile \(h(n)\sim c/n\), \(c>0\), cannot satisfy \(Ph=h\) either: at odd \(n>1\) there is only the even predecessor, so \(Ph(n)=h(2n)/(2n)\sim c/(4n^2)\).

This check rejects that particular proposed import. Other operator formulations use different weights and spaces. For example, Béhani proves hypercyclicity of a Collatz operator independently of whether the conjecture holds; this is an explicit reminder to verify the implication back to individual ordinary trajectories. [Béhani, *Linear dynamics of an operator associated to the Collatz map*, abstract and introduction](https://arxiv.org/abs/2303.03203)

Our previously frozen ordinary two-copy transfer instead uses the weights \((3x/(3x+1))^2\), whose product remains positive on an escaping simple trajectory. Its source-specific survival is the unresolved issue. Replacing those weights by reciprocal departures would destroy the needed signal. [Exact source and survival identity at frozen PR193](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/COLLISION_SOURCE.md)
