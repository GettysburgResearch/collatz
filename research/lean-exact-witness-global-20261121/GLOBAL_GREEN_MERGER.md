# Ordinary source capacity, component minima, and the Green merger

**Status: new unconditional written deductions and a core-Lean arithmetic
certificate. The full Collatz theorem is not proved.** This pass keeps the
previous Green-function packet frozen and pursues the proposed combination of
positive incoming drift with a smaller ordinary merger.

Three concrete results emerge. The Green weight has an exact decomposition
into unchanged original sources, with all loss occurring at even inputs.
On a hypothetical escaping component, sufficiently large exponents localize
its global maximum to one explicit finite ascent from the component minimum.
Separately, the cubic weight fails its incoming inequality on a cofinal,
fully specified family. That last failure persists beyond every finite core.

The smaller-merger theorem extends to every exponent at least two, with a
uniform quantitative margin above two. The localization theorem identifies
why this does not yet give a decreasing rank: the bad-drift certificate can
return precisely the original component minimum.

## 1. The exact retained-source coefficient

Use the ordinary shortcut map
\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]
For the actual path \(n_j=T^j(b)\), let \(p_t(b)\) count odd inputs before
clock \(t\), and put \(D_t(b)=3^{p_t(b)}/2^t\).

The shift by one gives the elementary one-step identities
\[
T(u)+1=
\begin{cases}
(u+2)/2,&u\text{ even},\\
3(u+1)/2,&u\text{ odd}.
\end{cases}
\tag{1}
\]
Consequently
\[
\boxed{
\frac{D_t(b)}{n_t+1}
=\frac{\alpha_t(b)}{b+1},
\qquad
\alpha_t(b)=
\prod_{\substack{0\le j<t\\n_j\text{ even}}}
\frac{n_j+1}{n_j+2}.
}
\tag{2}
\]
Every factor lies strictly between zero and one. In particular
\[
\frac{D_t(b)}{n_t+1}\le\frac1{b+1},
\tag{3}
\]
with equality exactly when the prefix contains no even input.
This statement concerns one actual source and one actual clock.

The new Lean module proves the equivalent exact natural-number identity
\[
2^t(n_t+1)=3^{p_t(b)}(b+1)+E_t(b),
\tag{4}
\]
where
\[
E_0=0,\qquad
E_{t+1}=
\begin{cases}
E_t+2^t,&n_t\text{ even},\\
3E_t,&n_t\text{ odd}.
\end{cases}
\]
It proves \(E_t>0\) exactly when an even input has occurred. It also proves
that an all-odd prefix of length \(t\) forces \(2^t\mid b+1\), so every
positive ordinary source has a finite first even input. No bounded search
or convergence witness is used.

For \(s>1\), retain the previous packet's finite Green series
\[
\mathscr R_s(n)
=\sum_{t\ge0}\sum_{\substack{b\ge1\\T^t(b)=n}}D_t(b)^s,
\qquad
W_s(n)=\frac{\mathscr R_s(n)}{(n+1)^s}.
\]
Its finiteness on every positive target, including periodic targets, was
proved in SECTION_MASS_ATTACK.md. Equation (2) gives the exact source form
\[
\boxed{
W_s(n)=
\sum_{t\ge0}\sum_{T^t(b)=n}
\frac{\alpha_t(b)^s}{(b+1)^s}.
}
\tag{5}
\]
Repeated visits remain distinct terms. If \(n\) is nonperiodic, each source
appears at most once, and therefore
\[
W_s(n)\le
\sum_{b\in\operatorname{Pred}(n)}(b+1)^{-s}.
\tag{6}
\]
This improves the unshifted coefficient bound in precisely the coordinate
used by the incoming residual.

## 2. An exact finite budget for every original source

Write
\[
\rho(u)=\frac{u+1}{u+2}\quad(u\text{ even}),\qquad
a_s(b)=(b+1)^{-s}.
\]
For every positive source, the decreasing product \(\alpha_t(b)\) has a
limit \(A(b)\in[0,1]\). Telescoping its loss gives
\[
\sum_{\substack{t\ge0\\T^t(b)\text{ even}}}
\bigl(1-\rho(T^t(b))^s\bigr)
a_s(b)\alpha_t(b)^s
=a_s(b)\bigl(1-A(b)^s\bigr).
\tag{7}
\]

Let \(\mathcal C\) be one complete ordinary component: two sources belong
to it when their forward orbits meet, with independent clocks. It is closed
under the forward map and under all positive ordinary predecessors. Put
\[
M_s(\mathcal C)=\sum_{b\in\mathcal C}a_s(b),\qquad
C_s(\mathcal C)=\sum_{b\in\mathcal C}a_s(b)A(b)^s.
\]
Both sums are finite, since \(M_s(\mathcal C)\le\zeta(s)-1\).
Nonnegative summation of (7), using (5), proves
\[
\boxed{
C_s(\mathcal C)
=M_s(\mathcal C)-
\sum_{\substack{u\in\mathcal C\\u\text{ even}}}
\bigl(1-\rho(u)^s\bigr)W_s(u).
}
\tag{8}
\]
Thus the entire even-input loss has a finite, exact budget. This identity
uses neither a predecessor-density hypothesis nor an exchange of
pointwise and moving-target limits.

For example, because \(s>1\) implies
\[
1-\rho(u)^s\ge\frac1{u+2},
\]
one obtains the unconditional bound
\[
\sum_{\substack{u\in\mathcal C\\u\text{ even}}}
\frac{W_s(u)}{u+2}\le M_s(\mathcal C).
\tag{9}
\]

The ordinary incoming operator is
\[
(\mathcal LW)(n)=W(2n)+
\mathbf1_{n\equiv2\ (3)}W((2n-1)/3).
\]
The Green equation becomes
\[
W_s(n)=a_s(n)+\rho(2n)^sW_s(2n)
+\mathbf1_{n\equiv2\ (3)}W_s((2n-1)/3).
\tag{10}
\]
Consequently its residual is
\[
\boxed{
\Delta_s(n):=W_s(n)-(\mathcal LW_s)(n)
=a_s(n)-\bigl(1-\rho(2n)^s\bigr)W_s(2n).
}
\tag{11}
\]
Equations (8) and (11) show that this residual is absolutely summable on
each complete component and that
\[
\sum_{n\in\mathcal C}\Delta_s(n)=C_s(\mathcal C)\ge0.
\tag{12}
\]
There is no cancellation of two infinite total masses in this proof: the
two terms on the right side of (11) have separately finite sums.

There is also a finite height-boundary formula:
\[
\sum_{\substack{n\in\mathcal C\\n\le N}}\Delta_s(n)
=
\sum_{\substack{n\in\mathcal C,\ n\text{ odd}\\(2N-1)/3<n\le N}}W_s(n)
-
\sum_{\substack{n\in\mathcal C,\ n\text{ even}\\N<n\le2N}}W_s(n).
\tag{13}
\]
It follows by cancelling the exact predecessor sets in the finite sum.
Its limit is the source capacity in (12), rather than an automatically
zero boundary term.

## 3. What that capacity means on an escaping component

This section uses one additional, explicitly pinned input: the unconditional
injective odd-orbit count in the PR175 source listed below. It gives
\[
\#\{q\le X:q\text{ on one injective unit odd orbit}\}
\le5X^{39/40}.
\tag{14}
\]
This is the orbit-count input, not the separate source-qualified ordinary
predecessor-density floor used in the canonical-envelope papers.
Nonnegative integration gives, when every such state is at least \(m\),
\[
\sum_q\frac1q\le200m^{-1/40}.
\tag{15}
\]

Suppose \(\mathcal C\) is an escaping component, and let \(m\) be its least
positive integer. Every orbit in it is injective. Between consecutive odd
states, the reciprocals of all even inputs sum to less than the reciprocal
of the following odd state. An initial even run contributes at most \(1/m\).
Every odd state after the first is a ternary unit. Thus (15) implies
\[
\sum_{\substack{j\ge0\\T^j(b)\text{ even}}}
\frac1{T^j(b)+1}\le201m^{-1/40}
\quad(b\in\mathcal C).
\tag{16}
\]
Using \(\log(1+x)\le x\) in the product (2), put
\[
\delta_m=\exp(-201m^{-1/40}).
\]
Then
\[
\boxed{\delta_m\le A(b)<1\quad(b\in\mathcal C).}
\tag{17}
\]
Strictness at the upper endpoint follows because a positive ordinary orbit
cannot have an infinite all-odd suffix. In particular
\[
\boxed{
\delta_m^s M_s(\mathcal C)
\le C_s(\mathcal C)<M_s(\mathcal C),
\qquad
C_s(\mathcal C)\ge\frac{\delta_m^s}{(m+1)^s}>0.
}
\tag{18}
\]

There is an exact moving-target formula, not merely a lower bound for one
atom. Define
\[
\beta(b)=\frac{A(b)}{b+1}.
\]
If \(T^t(b)=n\), the remaining product identity is
\(A(b)=\alpha_t(b)A(n)\). Hence (5), with no repeated visit, gives
\[
\boxed{
A(n)^sW_s(n)=
\sum_{b\in\operatorname{Pred}(n)}\beta(b)^s.
}
\tag{19}
\]
For a forward orbit \(n_j=T^j(x)\), its predecessor sets increase and their
union is the whole ordinary component: independent meeting clocks
suffice. Also \(A(n_j)\to1\), since these are tails of the convergent
nonzero product. Therefore
\[
\boxed{W_s(n_j)\longrightarrow C_s(\mathcal C)>0.}
\tag{20}
\]
The unshifted and shifted Green traces thus retain the same kind of
ordinary component capacity that PR185 found for its harmonic reference.
Here the source weights and the attenuation are explicit, and the
population-density hypothesis is not used.

For comparison, if the component enters any positive cycle, that cycle
contains an even input. Each complete circuit multiplies \(\alpha\) by
a fixed number strictly below one, so \(A(b)=0\) for every source in that
component and \(C_s(\mathcal C)=0\). This does not identify the cycle as the
one through one. The Green loss absorbs every positive cycle in the same
way, so it cannot distinguish the desired cycle without a further input.

### First-entrance subtraction retains a positive old-source term

Fix \(x\) in an escaping component, and put \(P_j=\operatorname{Pred}(n_j)\).
The disjoint sets \(P_0\) and \(P_{j+1}\setminus P_j\) partition the component.
Equation (19) is therefore the literal first-entrance decomposition
\[
A(n_j)^sW_s(n_j)
=\sum_{b\in P_0}\beta(b)^s
+\sum_{i<j}\ \sum_{b\in P_{i+1}\setminus P_i}\beta(b)^s.
\tag{21}
\]
The original term is at least \(\beta(x)^s>0\). The later-entry terms have
finite total \(C_s(\mathcal C)-\sum_{b\in P_0}\beta(b)^s\).
Deleting the first term would delete the original source whose absorption
is in question. It is not a free renewal step.

## 4. The smaller-merger implication for every exponent at least two

For every real \(s\ge2\) and positive integer \(n\),
\[
\boxed{
\Delta_s(n)\le0
\ \Longrightarrow\
n\text{ is periodic}
\quad\text{or}\quad
\exists\,0<b<n,\ t:\ T^t(b)=2n.
}
\tag{22}
\]
No canonical-density or chain-count input is needed for this theorem.

To prove it, assume that \(n\) is nonperiodic and no smaller source reaches
\(2n\). The latter target is nonperiodic because \(T(2n)=n\). A source
equal to \(n\) reaching \(2n\) would give a positive return to \(n\).
All sources in (6) are consequently at least \(n+1\), with one visit each:
\[
W_s(2n)\le
\sum_{b\ge n+1}(b+1)^{-s}
\le\int_{n+1}^\infty x^{-s}\,dx
=\frac{(n+1)^{1-s}}{s-1}.
\tag{23}
\]
The mean-value estimate gives
\[
(n+1)^s-(n+\tfrac12)^s
<\frac{s}{2}(n+1)^{s-1}.
\tag{24}
\]
Substituting (23)--(24) into (11) proves positive residual. More
quantitatively, for \(s>2\),
\[
\boxed{
\Delta_s(n)>
\frac{s-2}{2(s-1)}(n+1)^{-s}.
}
\tag{25}
\]
At \(s=2\), using the exact difference \(n+3/4\) gives
\[
\boxed{\Delta_2(n)\ge\frac1{4(n+1)^3}>0.}
\tag{26}
\]
The previous packet's unshifted estimate gives the slightly stronger
\(1/((n+1)(2n+1)^2)\) at this endpoint.

The implication admits finite certificates. If the sum in (11) reaches
its nonpositive-residual threshold, the capacity upper bound (23) is
strictly below that threshold. Some finite packet of actual contributions
already exceeds the capacity. A repeated source supplies a cycle, a source
equal to \(n\) supplies a cycle, and otherwise a source below \(n\) must
occur. Thus the smaller merger is a physical finite path.

The restriction \(s\ge2\) has content. At large \(n\), the product of the
bare tail bound in (23) and the difference in (24) approaches
\(s/(2(s-1))\). For \(1<s<2\) this exceeds one. That calculation does not
disprove a stronger arithmetic estimate in that interval; it identifies
what the literal source-capacity estimate actually proves.

## 5. Component-minimum localization: the maximum exists but returns its source

Let \(\mathcal C\) again be an escaping component with minimum \(m\).
The minimum is odd, because an even minimum would halve to a smaller
member. Let
\[
m=n_0,n_1,\ldots,n_\ell=e
\]
be its initial all-odd ascent, including its first even state \(e\).
This finite prefix exists by the divisibility theorem in section 1.
Its states before \(e\) are odd and strictly increasing.
Also \(e/2>m\): a smaller value contradicts minimality and equality gives
a cycle.

Choose any integer exponent
\[
p\ge\max\{\,2(e+1),\ 3(m+1)+1\,\}.
\tag{27}
\]
Then \(W_p\) has a unique global maximum on the entire component, attained
at the explicit state \(e\).

Here is a direct quantitative proof. The source \(m\) contributes exactly
\((m+1)^{-p}\) at every state of the displayed ascent. At every other
target, it is either absent or has passed the even input \(e\), so its
contribution is at most
\[
\left(\frac{e+1}{e+2}\right)^p(m+1)^{-p}
\le\frac13(m+1)^{-p}.
\tag{28}
\]
The last inequality is Bernoulli's inequality and (27). All other sources
are at least \(m+1\), and their total contribution, at any nonperiodic
target, is at most
\[
\sum_{b\ge m+1}(b+1)^{-p}
\le\frac{(m+1)^{1-p}}{p-1}
\le\frac13(m+1)^{-p}.
\tag{29}
\]
Thus outside that finite ascent,
\[
W_p(n)\le\frac23(m+1)^{-p},
\]
while on it \(W_p(n)\ge(m+1)^{-p}\).
At each odd input \(u\), equation (10) at \(T(u)\) gives
\[
W_p(T(u))=
W_p(u)+a_p(T(u))+
\rho(2T(u))^pW_p(2T(u))>W_p(u).
\tag{30}
\]
The maximum is therefore attained uniquely at its last state \(e\).
This localization uses only literal source bounds; section 3's chain-count
input is unnecessary.

At its next state \(n=e/2\), however, the same original source already
causes a negative residual. Its negative contribution in (11) is at least
\(\frac23(m+1)^{-p}\), while
\[
a_p(n)\le
\left(\frac{m+1}{m+2}\right)^p(m+1)^{-p}
\le\frac14(m+1)^{-p}.
\]
Hence
\[
\boxed{
\Delta_p(e/2)\le-\frac5{12}(m+1)^{-p}<0.
}
\tag{31}
\]
The smaller merger in (22) can be the already supplied path
\(m\to e\), with \(m<e/2\). It need not produce a source below \(m\).

This resolves the specific maximizer proposal. There really is a maximum
for sufficiently large exponents, even without a global properness
estimate. But the fallback merger at the ensuing negative drift can
return the original minimum. A new rank must account for that exact
self-return; neither the maximum nor the numerical size of its later
endpoint makes it a strict descent.

## 6. A cofinal obstruction to the cubic weight, with a Lean path certificate

The failure of the raw weight is stronger at the fixed exponent three.
For every integer \(k\ge9\), set
\[
b_k=2^k-1,\qquad e_k=3^k-1,\qquad n_k=(3^k-1)/2.
\]
All \(k\) input clocks in the following path are odd:
\[
T^j(b_k)=3^j2^{k-j}-1\quad(0\le j\le k).
\tag{32}
\]
Thus \(T^k(b_k)=2n_k\), its coefficient is \((3/2)^k\), and its single
contribution to \(W_3(2n_k)\) is \(8^{-k}\).
Equation (11) therefore gives
\[
\Delta_3(n_k)
\le
\frac{8^{k+1}-3\cdot9^k-3\cdot3^k-1}
{(3^k+1)^3\,8^k}.
\tag{33}
\]
The numerator is negative for every \(k\ge9\):
\[
8^{10}=1073741824
<1162261467=3\cdot9^9,
\]
and multiplication by eight on the left and nine on the right preserves
the strict inequality. Hence
\[
\boxed{\Delta_3(n_k)<0\quad(k\ge9).}
\tag{34}
\]
The targets \(n_k\) are unbounded. No finite exceptional core makes the
raw cubic weight satisfy the incoming inequality on all remaining
positive integers. This statement assumes no convergence of \(b_k\) or
\(n_k\).

The new core-Lean module proves (32), its exact odd count, and the
all-\(k\) integer inequality in one certificate theorem. The interpretation
as a Green residual in (33) is the written real-series deduction above;
there is no new Lean axiom for that interpretation.

The same single-source calculation gives a broader written result. For
any fixed real
\[
s>\frac{\log3}{\log(3/2)},
\]
the residual at these same targets is negative for all sufficiently large
\(k\). Indeed the ratio of the source loss in (11) to its positive term is
\[
\frac{(3^k+1)^s-3^{sk}}{2^{s(k+1)}}
\ge
\frac{s}{2^s}
\left(\frac{3^{s-1}}{2^s}\right)^k
\longrightarrow\infty.
\tag{35}
\]
The lower bound uses convexity of \(x^s\).
This does not rule out a finite-core repair of \(W_2\), and does not address
every exponent between two and the displayed threshold.

## 7. Formal coverage and reproducibility

New module:
[SourceGreenCoefficient.lean](lean/Collatz/SourceGreenCoefficient.lean).
It imports the existing ordinary shortcut map and Lean-core coprimality,
and introduces no analytic constants or assumptions.

The public results are the shifted affine identity, positive and zero
defect characterizations, the coefficient bound and its strict/equality
cases, the all-odd count and identity, the divisibility and finite
first-even conclusions, the parameterized ordinary ascent, and the cubic
all-clock path certificate. The real Green sums, component capacities,
maximum localization, and residual consequences remain written proofs.

The companion audit is
[AuditSourceGreenCoefficient.lean](lean/AuditSourceGreenCoefficient.lean).
The build uses Lean 4.34.1, one worker, and warnings as errors. The
committed receipt records the exact commands, source hashes, compiler
output, and axiom output. It also identifies precisely which assertions
are paper deductions.

## 8. Source boundary and the next mathematical step

| Frozen source | Use in this packet |
|---|---|
| PR177, a0a0d76f91b4e3846c1b1f0706cad56cb6098317, SECTION_MASS_ATTACK.md | All-\(s>1\) finiteness of the actual inverse Green series and its exact Poisson equation. The earlier note and replay are unchanged. |
| PR175, 2bc2ad37b490a5aea63658eaf657bc048da4532e, CANONICAL_POTENTIAL_SUPERLEVELS.md, section 4 | The unconditional injective-chain count used only in section 3. That note pins its elementary cylinder proof in ORBIT_MELLIN.md at 2055b8a311ab87d07bffc730154a7f8546fe382c, blob 16c943601ce791afb1bbd5f02f3a9ea88ef38520. |
| PR185, 276be8154f4e867acc0230466b34d9cb224aacf5, ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md | Comparison with its ordinary harmonic reference, exact source transport, and positive escaping-atom energy. None of its source-qualified density premises is imported into sections 1, 2, 4, 5, or 6. |
| PR180, bfba8feaefb3d0910456cdd92d2afcf9e8785b4d, ENERGY_SYNTHESIS.md | Its moving-target correction and all-clock resolution boundary motivate retaining the source formula (5), rather than dropping the height or source factor. No new estimate is inferred from its resolution term. |
| PR176, 8aeb843bba254f065743b6fa277a70906b51d520, SOURCE_ENVELOPE.md and COFINAL_ENVELOPE_LIMITATION.md | Its literal certificate envelope can certify a merger when the partner is in the rank-paid interval. The Green theorem produces a partner below the later state \(n\), and does not itself place it below that original certificate envelope. |

The precise missing connection is now visible in a finite configuration.
At the maximum of the Green weight, a negative residual can be paid by the
original source's initial ascent. To use the source-envelope induction,
one needs a new arithmetic operation that either puts a partner inside
the original paid interval, or strictly lowers the supplied certificate
rank while retaining that same target. The capacity calculation does not
provide either operation.

The section and population inputs do not change this bookkeeping merely
by producing more inverse sources: all their contributions enter (5) and
the later-entry sum in (21) with their original weights. A fixed original
atom remains positive on a hypothetical escaping component. The new
finite-budget identity, explicit component-minimum maximum, and cofinal
cubic family establish concrete facts about that mechanism; they do not
turn it into a proof of absorption or a classification of positive cycles.
