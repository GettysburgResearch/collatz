# Constructing the actual parity-series family up to its critical boundary

Date: 23 November 2026. **Written construction and exact limitations; full
Collatz remains OPEN.** This attack constructs a meromorphic family for the
actual weighted parity series on the entire disc \(|z|<2\), identifies its
operator poles with actual positive cycles, and then tests the specific
forcing at the required boundary. The actual family itself has no
meromorphic continuation across any point of \(|z|=2\) in the natural
linear-growth sequence norm. This last statement already follows from
the known ordinary sources \(2^k\); it does not posit an escaping orbit.

The construction does not give a larger scalar continuation domain for an
escaping fixed source than its elementary radius estimate already gives.
Its useful output is the exact global construction, cycle-pole
classification, and the distinction between scalar continuation and a
uniform operator argument. No recurrence, triadic candidate, or full
convergence theorem is claimed.

## 1. The fixed original series and the actual operator

Use the shortcut map on positive integers
\[
 T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.
 \end{cases}
\]
Write
\[
 e_j(n)=T^j(n)\bmod2,\quad
 p_j(n)=\sum_{i<j}e_i(n),\quad
 b_j(n)=e_j(n)3^{-p_{j+1}(n)},\quad
 B_n(z)=\sum_{j\ge0}b_j(n)z^j.                         \tag{1}
\]
Every index in (1) is the literal orbit of the specified positive ordinary
source. Let
\[
 X=\{f:\mathbb N_{>0}\to\mathbb C:
       \|f\|_X=\sup_{n\ge1}|f(n)|/n<\infty\},
\]
and define the bounded weighted composition operator and forcing
\[
 (Kf)(n)=3^{-e_0(n)}f(Tn),\qquad g(n)=e_0(n)/3.        \tag{2}
\]
The exact identity
\[
                         (K^j g)(n)=b_j(n)            \tag{3}
\]
follows by multiplying the actual first \(j\) weights. Hence, as an
\(X\)-valued analytic germ,
\[
              B(z)=(I-zK)^{-1}g,\qquad B(z)(n)=B_n(z).\tag{4}
\]
For example, \(\|K\|_X=2/3\), attained at the row \(n=1\), so the
Neumann series justifies (4) in \(|z|<3/2\). All identities below agree
with this germ. The continuation does not define a new parity process.

The classical operator approach is contextual literature, not an imported
closing theorem. Neklyudov's *Functional analysis approach to the Collatz
conjecture*, Sections 1 and 4, treats ordinary Collatz composition and
pushforward operators on analytic-function spaces and relates resolvents
to orbit generating functions. Its operators, spaces, and weights are not
(2). The primary paper was opened:
<https://arxiv.org/html/2106.11859v9>.

## 2. A concrete meromorphic construction on the critical disc

Conjugate \(X\) to \(\ell^\infty\) by \(f(n)=nh(n)\). The conjugated
operator is exactly
\[
 (\widehat K h)(n)=a(n)h(Tn),\qquad
 a(n)=3^{-e_0(n)}\frac{Tn}{n}
     =\frac12+\frac{e_0(n)}{6n}.                       \tag{5}
\]
Thus \(\widehat K=\tfrac12 C_T+D C_T\), where
\(C_Th=h\circ T\) has norm one and \(D\) is multiplication by
\(e_0(n)/(6n)\). The latter is a norm limit of finite-rank diagonal
operators. This gives compactness directly; no arithmetic smoothing or
independence assumption is required.

Here is a finite-dimensional reduction that also constructs the
continuation without appealing to an unstated Fredholm theorem. For an
integer \(M\ge1\), let \(F_M f\) agree with \(Kf\) at \(1\le n\le M\)
and vanish otherwise, and put \(A_M=K-F_M\). Then
\[
 \operatorname{rank}F_M\le M,\qquad
 \|A_M\|_X\le q_M:=\frac12+\frac1{6(M+1)}.            \tag{6}
\]
The family
\[
 Q_M(z)=(I-zA_M)^{-1}=\sum_{j\ge0}z^jA_M^j
\]
is norm-holomorphic for \(|z|<q_M^{-1}\), with the usual geometric
remainder estimate. Write \(F_M=J_M L_M\), where \(J_M\) injects a
vector in \(\mathbb C^M\) as a function supported on \([1,M]\), and
\((L_M f)_i=(Kf)(i)\). Wherever the finite matrix is invertible,
\[
\begin{split}
 (I-zK)^{-1}={}&Q_M(z)\\
 &+zQ_M(z)J_M
       [I_M-zL_MQ_M(z)J_M]^{-1}L_MQ_M(z).             \tag{7}
\end{split}
\]
This follows by solving \(f=Q_M g+zQ_MJ_ML_Mf\) for \(L_Mf\).
The matrix determinant is holomorphic and equals one at zero. Its inverse
is therefore meromorphic by the adjugate formula, with finite-rank polar
parts in (7). Since \(q_M^{-1}\uparrow2\), and the formulas agree on
their common initial germ, they glue to
\[
 \boxed{(I-zK)^{-1}\text{ meromorphic on }|z|<2;
        \quad B(z)\text{ has that same continuation in }X.}     \tag{8}
\]

The entries of the finite reduction retain actual first returns. If
\(\tau_i\) is the first positive clock for which
\(T^{\tau_i}(i)\in[1,M]\), the \(i\)-th row of
\(zL_MQ_MJ_M\) has one nonzero entry,
\[
            z^{\tau_i}3^{-p_{\tau_i}(i)},             \tag{9}
\]
at that returned state. If there is no return, the row is zero. This is
because iteration by \(A_M\) stops at its first small input.
The analytic series and its norm error are constructive; deciding that
one row in (9) vanishes identically would decide a no-return question.
The reduction does not silently turn that decision into a finite search.

## 3. Every interior operator pole is an actual positive cycle

The following classification concerns the resolvent on the specified
space \(X\). It does not assume that all positive orbits are periodic.

**Theorem 1.** Let \(|\lambda|>1/2\). The kernel of \(K-\lambda I\)
has one complex dimension for each primitive positive cycle \(C\) whose
length \(A(C)\) and odd count \(p(C)\) satisfy
\[
                         \lambda^{A(C)}=3^{-p(C)}.    \tag{10}
\]
There are only finitely many such cycles. Each kernel vector vanishes
outside their forward basins. Every such eigenvalue is semisimple.
Consequently all poles of (8) are simple finite-rank poles and are
exactly the numbers
\[
                 z^{A(C)}=3^{p(C)}                    \tag{11}
\]
arising from actual primitive positive cycles.

**Proof.** Choose \(M\) so that \(q_M<|\lambda|\). For an eigenvector,
equation (5) gives
\[
 \frac{|f(n)|}{n}
 =\frac{a(n)}{|\lambda|}\frac{|f(Tn)|}{Tn}.           \tag{12}
\]
A non-eventually-periodic positive orbit has distinct states and tends
to infinity: infinitely many visits to a finite set would repeat a
state, forcing eventual periodicity. On such an orbit, every sufficiently
late input exceeds \(M\). Iterating (12) from any fixed late clock
and using \(f\in X\) gives a bound tending to zero. Thus \(f\) vanishes
on every such orbit and all its earlier states.

On a cycle, multiplying the unnormalized eigenvector equations gives
(10), unless the value vanishes on the entire cycle. One amplitude
determines all phases. A cycle obeying (10) cannot lie wholly above
\(M\), since multiplying (12) there would give
\(|\lambda|^{A(C)}\le q_M^{A(C)}\). Distinct cycles are disjoint, so
at most \(M\) compatible cycles exist.

Conversely prescribe a compatible cycle amplitude. On its basin pull it
back by
\[
 f(n)=\lambda^{-\tau}3^{-p_\tau(n)}f(T^\tau n),        \tag{13}
\]
where \(\tau\) is the first hit of the cycle, and put \(f=0\) elsewhere.
Before that hit all states are distinct, hence at most \(M\) inputs lie
in \([1,M]\). In (12), every other factor is below one and every small
factor is at most \(\max(1,(2/3)/|\lambda|)\). Thus (13) is bounded in
the norm \(X\), uniformly over its entire ordinary basin. It is an
eigenvector. This proves the kernel classification and its dimension.

If \((K-\lambda I)f=g\) with \(g\) an eigenvector, restrict to a
compatible cycle. Its weighted cyclic matrix has minimal polynomial
dividing \(X^{A(C)}-3^{-p(C)}\), which has no repeated roots. Its
\(\lambda\)-eigenspace therefore has zero intersection with the range
of the shifted matrix. Hence \(g\) vanishes on each compatible cycle,
and the already proved kernel classification gives \(g=0\). There
are no nontrivial Jordan chains. To see the pole-order consequence
directly, insert a Laurent expansion in
\((I-zK)(I-zK)^{-1}=I\). A pole of order at least two supplies a
nonzero highest coefficient with range in \(\ker(K-\lambda I)\),
and its next coefficient supplies a generalized eigenvector mapping
onto a nonzero multiple of that range. This is the excluded chain.
Thus the finite-dimensional reduction (7) has only simple poles.

Finally a positive cycle has a nonzero carry \(C\) in
\((2^A-3^p)n=C>0\), so \(2^A>3^p\). All roots in (11) lie within
\(|z|<2\), as required. Conversely each compatible eigenvector makes
the resolvent singular. This proves the pole assertion. \(\square\)

For a fixed source eventually entering a cycle, \(B_n\) is rational by
its actual eventually periodic word. Its positive real pole at
\(z=3^{p/A}\) does not cancel, because the cycle numerator has positive
coefficients and at least one odd input. Individual complex cycle poles
may cancel in that scalar function; Theorem 1 classifies the full
operator resolvent, not every scalar numerator.

For a fixed non-eventually-periodic source, the same tail estimate from
(12), applied to \(K^jg\), proves that its original power series already
converges for every \(|z|<2\). In this case (8) agrees with that series
and has no scalar pole there. This scalar radius fact also follows
elementarily from the eventual lower bound on all orbit states.

## 4. The actual forcing itself reaches a sharp norm boundary

It would be tempting to try to continue the constructed family a little
beyond two and then invoke arithmetic rationality for each coordinate.
The following obstruction applies to the actual forcing \(g\), not just
to arbitrary vectors in the operator space.

**Theorem 2.** The \(X\)-valued meromorphic family \(B(z)\) in (8) has
no meromorphic continuation across any point of \(|z|=2\).

**Proof.** The actual \(1,2\) cycle gives
\[
 B_1(z)=\frac1{3-z^2}.
\]
The known source \(2^k\) has exactly \(k\) initial even steps before
reaching one. Hence, first as a germ and then by continuation,
\[
                  B_{2^k}(z)=\frac{z^k}{3-z^2}.       \tag{14}
\]
Define the bounded restriction \(R:X\to\ell^\infty(\mathbb N_0)\) by
\((Rf)_k=f(2^k)/2^k\). Then
\[
             R((3-z^2)B(z))=w(z),\qquad
             w(z)=((z/2)^k)_{k\ge0}.                \tag{15}
\]
The right side is norm-holomorphic for \(|z|<2\).

Fix \(|z_0|=2\). Any meromorphic extension of \(w\) near \(z_0\)
would have no pole: each coordinate is the entire polynomial
\((z/2)^k\), so every negative Laurent coefficient has all coordinates
zero and is the zero vector. The extension would therefore be
norm-continuous with value \(((z_0/2)^k)_k\). But for every \(0<t<1\),
\[
 \left\|w(tz_0)-((z_0/2)^k)_k\right\|_\infty
       =\sup_{k\ge0}(1-t^k)=1.                      \tag{16}
\]
This is a contradiction. Since \(3-z_0^2\ne0\), an extension of
\(B\) would give one of \(w\) by (15). \(\square\)

This theorem is compatible with every individual \(B_n\) being rational.
It concerns uniform control as the original source ranges over all positive
integers. Its witnesses are explicitly convergent sources; no unproved
orbit is used. The missing pointwise arithmetic continuation cannot be
obtained merely by passing this global norm construction through its
critical circle.

## 5. Polynomial reweighting has an exact optimal boundary

The next attempt was to give large sources less norm weight. For any
real \(\alpha\), put
\[
 X_\alpha=\{f:\sup_{n\ge1}|f(n)|/n^\alpha<\infty\}.
\]
The operator (2) is bounded on every such space. Let \(\|\cdot\|_{\rm ess}\)
denote distance in operator norm from compact operators, and let
\(r_{\rm ess}\) be the spectral radius in the quotient by compact
operators.

**Theorem 3.** For every integer \(k\ge1\),
\[
 \|K^k\|_{{\rm ess},X_\alpha}
 =\left(2^{-\alpha}\max(1,3^{\alpha-1})\right)^k,
\]
and hence
\[
 \boxed{r_{{\rm ess},X_\alpha}(K)
       =2^{-\alpha}\max(1,3^{\alpha-1})\ge\frac12,}  \tag{17}
\]
with equality exactly at \(\alpha=1\).

**Proof.** Under \(f(n)=n^\alpha h(n)\), the coefficient in the one
nonzero entry of the \(n\)-th row of \(K^k\) is
\[
             3^{-p_k(n)}\left(\frac{T^k(n)}n\right)^\alpha.
                                                               \tag{18}
\]
For fixed \(k\), the finitely many affine parity branches give, uniformly
as \(n\to\infty\),
\[
 (18)=2^{-\alpha k}3^{(\alpha-1)p_k(n)}+o(1).
\]
Truncating finitely many output rows is finite rank. Therefore the
essential norm is at most the maximum over \(0\le p\le k\), which is
the right side of (17) to the \(k\)-th power.

For the matching lower bound, both extreme words have arbitrarily large
literal ordinary realizers. The all-even word has \(n=2^k m\) and
endpoint \(m\). The all-odd word has \(n=2^k m-1\) and endpoint
\(3^k m-1\). At intermediate clocks the latter orbit is exactly
\(3^j2^{k-j}m-1\), so the prescribed first \(k\) parities really are
odd. Let \(m\) increase along distinct endpoints and test with the
normalized singleton functions at those endpoints. They have norm one
and are weakly null: after conjugacy to \(\ell^\infty\), any bounded
linear functional is absolutely summable on a sequence of distinct
coordinate unit vectors, by choosing signs in finite sums. Every compact
operator therefore sends them to zero in norm. The selected output rows
of \(K^k\) tend respectively to
\(2^{-\alpha k}\) and
\(2^{-\alpha k}3^{(\alpha-1)k}\). No compact perturbation can reduce
the norm below their maximum. The spectral-radius formula in the
quotient gives (17).

For \(\alpha\le1\), (17) is \(2^{-\alpha}\ge1/2\); for
\(\alpha\ge1\), it is
\(\tfrac12(3/2)^{\alpha-1}\ge1/2\). Equality in either case requires
\(\alpha=1\). \(\square\)

Thus a plain polynomial reweighting cannot give this operator a compact
perturbation with spectral radius strictly below one half. For
\(0\le\alpha\le1\), the forcing restriction (15) has its analogous
norm boundary at \(|z|=2^\alpha\le2\). For \(\alpha<0\), the forcing
\(g\) does not even belong to \(X_\alpha\). For \(\alpha>1\), that particular
forcing obstruction moves outward, but the all-odd ordinary cylinders
increase the essential spectral radius. The latter is an operator-norm
statement; it does not prove a scalar natural boundary for any fixed
ordinary source.

## 6. The unchanged-source gluing question

At the required arithmetic point, the exact finite affine identity is
\[
 n+\sum_{j<k}b_j(n)2^j
       =\frac{2^kT^k(n)}{3^{p_k(n)}}.                 \tag{19}
\]
Its right side tends to zero in \(\mathbb Q_2\), so the formal series
always has binary value
\[
                         B_n(2)=-n\quad(2\text{-adically}).
                                                               \tag{20}
\]
For an escaping positive source, the earlier qualified reciprocal-sum
and positive-product inputs give a finite positive real sum in (19).
Those inputs and their qualification are retained; they are not proved
by the operator construction. Such a real sum differs from (20).

For an eventually periodic positive source, its rational \(B_n\) instead
has analytically continued value \(-n\) at two. One can check this from
the finite prefix and cycle formula, or from
\[
 (2-z)A_n(z)=2n+zB_n(z),\qquad
 A_n(z)=\sum_{k\ge0}T^k(n)3^{-p_k(n)}z^k.
\]
The cycle denominator at two is nonzero because \(2^A>3^p\).

The construction (8) reaches the exact critical disc but supplies no
scalar neighborhood across two on which arithmetic rationality can be
invoked. At an escaping fixed source it gives no larger scalar disc
than direct convergence already provides. Theorem 2 prevents obtaining
that neighborhood by uniform continuation of this \(X\)-valued family.
Theorem 3 explains why replacing \(n\) by a plain polynomial weight
does not improve the universal Fredholm bound.

There is also an explicit analytic diagnostic for the missing inference.
Let \(\rho=\log_3 2\), choose an integer \(K_0\) sufficiently large
that
\(\rho+2/((K_0+1)\log3)<1\), and define
\[
 F(k)=\rho(k+K_0)+\frac{2}{\log3}\log(k+K_0+1),\quad
 p_k=\lfloor F(k)\rfloor-\lfloor F(0)\rfloor,\quad
 e_k=p_{k+1}-p_k.
\]
Then \(e_k\in\{0,1\}\),
\(p_k=\rho k+(2/\log3)\log(k+1)+O(1)\), and the same weighted
coefficient rule \(b_k=e_k3^{-p_{k+1}}\) gives
\[
 \sum b_k2^k<\infty,\qquad
 \operatorname{radius}\sum b_kz^k=2.                 \tag{21}
\]
Its parity density is irrational, so its parity word is not eventually
periodic. The elementary finite-window argument in the preceding
HOLONOMICITY packet then shows that this series is neither rational nor
D-finite. Thus the multiplicative coefficient restriction, holomorphy
inside the critical disc, and summability at its positive boundary do
not alone force the desired recurrence.

This diagnostic is deliberately **not** asserted to be the itinerary
of a positive ordinary integer. Its binary value has not been identified
as \(-n\) for such an integer. That remaining ordinary-source arithmetic
condition is exactly the condition a successful scalar theorem must use;
dropping it would change the problem.

No scalar continuation theorem using that condition was obtained here.
Nor was a successful actual triadic candidate constructed. A valid next
attempt would need source-dependent scalar cancellation or an arithmetic
function space that preserves the one fixed ordinary evaluation while
going beyond the critical continuation supplied by (8).

## 7. Difference from the adjacent pressure-operator work

PR176's PRESSURE_WIENER_ATTACK uses the odd-unit pullback
\((A_s h)(n)=(3/2^{a(n)})^s h(Un)\) on weighted \(\ell^1\) spaces.
Its known-basin approximate fixed vectors defeat closed-range estimates
for its positive pressure kernel. Its INDEPENDENT_KERNEL_ATTACK retains
the positive coefficient envelope and proves an exact geometric
coefficient-repetition obstruction to a boundary derivative bootstrap.

Here the operator is (2), the variable counts shortcut time, the forcing
is the actual weighted parity coefficient, and the norm allows linear
ordinary-source growth. Equations (7)--(11) construct the full actual
family and classify its interior poles. Equations (14)--(17) concern
this family and every polynomial-growth version of its composition
operator. Neither adjacent pressure kernel is identified with \(B\),
and no separate Mahler equation is inferred.

## 8. Source pins and verification scope

The written argument above is self-contained apart from standard Banach
space facts explicitly used in the compact-operator norm calculation.
The finite-dimensional inverse (7) proves the needed meromorphy directly.
No Lean formalization or finite census is claimed for these infinite
operator statements. The two all-constant word families and the powers
of two are exact symbolic constructions.

Relevant repository sources inspected at their exact heads:

- PR180, `7d4ad9f11d3d7a54c67b0c6cff4f13a2ab967161`,
  `research/profound-step-20261123/HOLONOMICITY.md`: actual parity
  coefficients, finite-window recurrence rigidity, and the scalar
  rationality and continuation boundary.
- PR176, `4171e1fe40e41842af9f800bd821084b724cf8f9`,
  `research/lean-global-resolvent-20261121/overview/integer-boundary/PRESSURE_WIENER_ATTACK.md`
  and `INDEPENDENT_KERNEL_ATTACK.md`: the different pressure operator,
  its actual positive kernel, and existing regularity obstructions.
- The same PR176 head, `overview/source-construction/CARRY_CONSTRUCTION_ATTACK.md`
  and `INFINITE_OPTIMAL_RAY_ATTEMPT.md` under the same research root:
  failed candidate freedom and the exact fixed-source adelic tail cost.
- PR177, `f47a5ec51aa5853f104013a6d5046d6220ff7423`,
  `research/lean-exact-witness-global-20261121/literature-closure/triadic/SOURCE_TAIL_TRANSPORT.md`:
  the all-parameter failure of source-tail padding at its own horizon.
- PR178, `c91b80a3156e640ad471cf30c47721145ae21eb1`,
  `research/central-step-20261123/triadic/OPTIMAL_SELECTOR_AND_HEIGHT.md`:
  whole-candidate optimization and the exact denominator-weight cost.
- PR182, `cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`,
  `research/literature-round4-20261123/TRIADIC_RIGIDITY.md`:
  the true triadic denominator's stopping-time interpretation; no
  universal successful exponent selector is imported.

The primary Bell--Smertnig and Bost--Chambert-Loir inputs remain those
specified, with exact hypotheses, in the pinned HOLONOMICITY packet.
The present attempt does not claim a strict adelic capacity margin,
algebraicity, or equality of real and binary sums from (8).
