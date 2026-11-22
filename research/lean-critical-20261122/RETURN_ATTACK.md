# One full reference for every finite return depth

**Status: SOURCE-QUALIFIED written analytic deductions, with a Lean finite
collision core. Full Collatz closure remains OPEN.**

This continuation combines PR176's new polylogarithmic band-access clock
with the actual-source framework of PR180 and the collision criterion of
PR186. It constructs **one finite measure with every finite logarithmic
height moment**, retaining periodic tails and every original source.
Against that same reference, every fixed iterate of the actual entrance
law has an \(L^p\) density for every finite \(p>1\). A quantitative bound
and an original-source truncation error are proved below.

The new conclusion includes the entire entrance residual. It does not
restart the source weights after a return. Its remaining defect is the
growth of the bound with the return index: the estimate obtained here is
much larger than the critical recurrence scale.

The finite complete-fiber quadratic inequality and an elementary actual
return-clock bound are checked in
[ReturnCritical.lean](lean/ReturnCritical.lean). The lognormal time-weight
lemmas are checked separately in
[LognormalClock.lean](lean/LognormalClock.lean). The infinite source measures,
general \(L^p\) argument, and imported Diophantine theorem remain written
mathematics.

## 1. Frozen sources and what is new

| Source | Exact head and path | Role |
|---|---|---|
| PR180 | bfba8feaefb3d0910456cdd92d2afcf9e8785b4d; research/lean-wide-pass-20261122/RETURN_SYNTHESIS.md | Full clock-weighted references, original-source accounting, and the earlier fourth-log-moment construction. |
| PR176 | 8aeb843bba254f065743b6fa277a70906b51d520; research/lean-global-resolvent-20261121/overview/POLYLOG_BAND_ENTRANCE.md | The already proved, source-qualified shortcut entrance and positive-return clock \(O((1+\log n)^{4.117})\). This clock improvement is credited to PR176, not claimed here. |
| PR183 | 907a540943090968bc683b1b9246208e9053c1f8; research/literature-closing-20261121/transport/RETURN_TRANSPORT.md | Actual entrance law, killed return operator, retained residual, and distinct-atom recurrence budget. |
| PR186 | 1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493; literature/deep-machinery-20261122/04_returns_operators_and_termination.md, section 4 | The \(L^p\) version of that retained-atom budget. |
| PR185 | 276be8154f4e867acc0230466b34d9cb224aacf5; research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md | A separate collision contraction against an infinite harmonic reference. The finite reference below is a different measure. |

The primary ratio estimate underlying PR176 is also corroborated in the
published paper by Aihua Fan, Hervé Queffélec and Martine Queffélec,
[*The Furstenberg set and its random version*](https://ems.press/content/serial-article-files/47663),
L'Enseignement Mathématique 70 (2024), definition on p.70 and Theorem 2.1
on p.71. It states the Diophantine exponent \(4.117\) for
\(\log 2/\log 3\), citing Rhin and Wu–Wang. PR176 gives the reciprocal
conversion and the complete ordinary-clock argument. No number-theory
assertion is inserted as a Lean axiom here.

The following are the additions of this pass:

1. A full lognormal-clock reference with all logarithmic moments.
2. Complete-fiber \(L^p\) control for every fixed actual return iterate,
   including the residual from unmarked original sources.
3. An explicit common-reference bound and a power-saving error when
   truncating the original source sum.
4. A stronger recurrence target furnished by the reference's lognormal
   rank moment.
5. A countermodel isolating why finite-depth regularity alone does not
   settle the return-index growth.

## 2. Maps, original labels, and the common reference

Use the actual shortcut map \(T\), the accelerated odd map
\(U(n)=(3n+1)/2^{v_2(3n+1)}\), and the same constant-70 marked set \(D\).
Let \(o(n)\) be the odd part of \(n\). Put

\[
\mu=\sum_{n\ge1}n^{-4}\delta_n,\qquad
\rho=E_*\mu,\qquad \ell(n)=1+\log n,
\]

where \(E\) is first marked entrance, including time zero. Let \(R\) be
first strictly positive marked return. Let \(Q\) push forward by \(R\),
killing at 1 exactly as in PR183. In particular a failed original source
keeps its positive weight \(n^{-4}\) in every surviving packet.

For every odd clock \(j\), define the **full** marked packet

\[
\widetilde\nu_j(m)=\mathbf1_D(m)
 \sum_{\substack{n\ge1\\U^j(o(n))=m}}n^{-4}.
\tag{C1}
\]

The original label is \(n\), not its odd part or its current endpoint.
Multiple even sources with the same odd part, multiple sources meeting
at the same endpoint, and all repeated visits are counted with their
original weights.

Choose

\[
c_j=\exp\!\big(-[\log(j+2)]^2\big),\qquad
\boxed{\ \beta=\sum_{j\ge0}c_j\widetilde\nu_j.\ }
\tag{C2}
\]

This is one fixed reference, independent of the later return index and
of \(p\). Since \(m\in D\) is itself an original source at clock zero,

\[
\beta(m)\ge c_0m^{-4}>0\qquad(m\in D).
\tag{C3}
\]

### Theorem C1: all finite logarithmic height moments

For every real \(r\ge0\),

\[
\boxed{\ \sum_m\beta(m)\ell(m)^r<\infty.\ }
\tag{C4}
\]

**Proof.** Every positive odd state satisfies \(U(x)\le2x\), hence

\[
\ell(U^j(o(n)))\le\ell(n)+j.
\]

For any finite \(r\), both \(\sum_j c_j\) and
\(\sum_j c_j(j+1)^r\) converge. One elementary estimate is

\[
rx-x^2\le\frac{(r+2)^2}{4}-2x,
\qquad x=\log(j+2),
\]

so \(c_j(j+2)^r\) is bounded by a constant times \((j+2)^{-2}\).
The new LognormalClock module checks this kind of domination and the
resulting time-moment summability.

Since \((a+b)^r\le2^r(a^r+b^r)\) for nonnegative \(a,b\), Tonelli gives

\[
\sum_m\beta(m)\ell(m)^r
\le2^r\left[
 \left(\sum_n n^{-4}\ell(n)^r\right)\left(\sum_jc_j\right)
 +\zeta(4)\sum_jc_jj^r\right]<\infty.
\]

This proof includes full periodic tails, with no repetition cutoff.
It does not need predecessor density or the earlier occupation estimate.
QED.

The reference also has a stronger rank moment. For every \(0<a<1\),

\[
\boxed{\ \sum_m\beta(m)
 \exp\!\left(a[\log\ell(m)]^2\right)<\infty.\ }
\tag{C5}
\]

Indeed \(\ell(n)+j\le\ell(n)(j+1)\). Write
\(x=\log\ell(n)\), \(y=\log(j+1)\), and choose
\(\theta> a/(1-a)\). The inequality

\[
a(x+y)^2
 \le a(1+\theta)x^2+a(1+1/\theta)y^2
\]

has clock coefficient \(a(1+1/\theta)<1\). The resulting source sum
\(\sum_n n^{-4}\exp(C_a[\log\ell(n)]^2)\) is finite, and the clock
sum is bounded by \(\sum_j\exp(-b_a[\log(j+2)]^2)\) for some \(b_a>0\).
Both estimates follow from the fact that \((\log x)^2=o(x)\).

## 3. Complete endpoint fibers: the exact transport inequality

Here is a general finite or countable inequality. Let source weights
\(w_s\ge0\), a source-to-endpoint map \(f\), and positive allocations
\(a_s\) satisfy

\[
\lambda(m)\ge\sum_{f(s)=m}a_sw_s.
\]

For every \(p>1\), putting \(\nu=f_*(\sum_s w_s\delta_s)\),

\[
\boxed{\ \sum_m\frac{\nu(m)^p}{\lambda(m)^{p-1}}
       \le\sum_s w_sa_s^{1-p}.\ }
\tag{C6}
\]

For a finite fiber, apply Hölder, or Jensen with weights
\(a_sw_s/\sum a_sw_s\), to the values \(a_s^{-1}\). The result is

\[
\left(\sum w_s\right)^p
\le\left(\sum a_sw_s\right)^{p-1}
   \sum w_sa_s^{1-p}.
\]

Increasing finite subsets proves the countable version. Summing complete
fibers proves C6. Any additional reference mass only improves its left
side. Equal endpoints are deliberately grouped before taking the power.

The finite \(p=2\) forms are the checked theorems
fiber_quadratic_bound and aggregate_quadratic_bound in ReturnCritical.
The latter counts every original source once in the final source budget.

### An elementary complete-tail result before using the new clock input

Fix \(\eta>0\). Let \(\mu_D=\sum_{n\in D}n^{-4}\delta_n\), and form the earlier reference
\(\alpha_\eta=\sum_j (j+1)^{-5}[\log(j+2)]^{-\eta}
 \widetilde\nu_j^{\,D}\) from those original marked sources.

The existing square-root section argument gives an actual first positive
odd-return clock \(\tau(n)\) satisfying

\[
\tau(n)^2\le8n.
\tag{C7}
\]

ReturnCritical checks this clock bound, including periodic sources.
The proof first applies the existing odd-section construction to \(U(n)\),
then uses \(U(n)\le2n\). It is a corollary of the earlier section theorem,
not a new irrationality estimate.

Apply C6 with \(f(n)=R(n)\) and the allocation at its actual clock
\(a_n=(\tau(n)+1)^{-5}[\log(\tau(n)+2)]^{-\eta}\). It proves

\[
\frac{Q\mu_D}{\alpha_\eta}\in L^p(\alpha_\eta)
\qquad\left(1<p<\frac{11}{5}\right).
\tag{C8}
\]

The entire source tail is bounded by a constant times

\[
\sum_{n>N}n^{-4+(5/2)(p-1)}
 [\log(n+1)]^{\eta(p-1)}.
\]

It converges precisely in the displayed sufficient range. At \(p=2\)
the tail is \(O_\eta(N^{-1/2}[\log(N+1)]^\eta)\). This estimate is over
all branches and all collisions. Its domain is the fresh marked law;
the next section reaches the full entrance law and every fixed return
depth by using the newer polylogarithmic clock.

## 4. A polynomial-in-source-log bound at every fixed return depth

The source-qualified PR176 theorem supplies an absolute \(C\) such that
first entrance and positive return take at most
\(C\ell(n)^{4.117}\) shortcut steps. Each odd step consumes at least one
shortcut step. Thus it supplies the same upper bound for the associated
odd clocks.

For each original source \(n\), let \(J_k(n)\) be the odd clock, measured
from \(o(n)\), of \(R^k(E(n))\) under the underlying unkilled return map. It is defined on all
sources, including those already in the cycle through 1; \(Q\) retains only
the surviving labels. The marked
times are strictly increasing after the first entrance.

There is an absolute constant \(A\ge1\) such that, with

\[
d_k=5^{k+1},\qquad s_k=1+5+\cdots+5^k=\frac{d_k-1}{4},
\]

\[
\boxed{\ \ell(n)+J_k(n)+2
 \le A^{s_k}\ell(n)^{d_k}.\ }
\tag{C9}
\]

**Proof.** Round the supplied exponent \(4.117\) up to 5, using
\(\ell(n)\ge1\). Increase \(A\) to absorb constants and small inputs.
The entrance estimate gives C9 at \(k=0\). If
\(H_k=\ell(n)+J_k(n)+2\), the next endpoint height is at most \(H_k\).
The positive-return clock is at most \(C H_k^5\), so

\[
H_{k+1}\le H_k+C H_k^5\le A H_k^5.
\]

This proves C9 by induction. All clocks belong to the same original
trajectory. No newly sampled or relabeled source appears. QED.

In particular, for every fixed \(k\) and every finite \(r\ge0\),

\[
\boxed{\ \sum_m(Q^k\rho)(m)\ell(m)^r<\infty.\ }
\tag{C10}
\]

This follows by bounding the source sum by
\(A^{rs_k}\sum_n n^{-4}\ell(n)^{rd_k}\). It includes the residual
from original sources outside the marked set. It supplies finite
moments at every fixed return depth, not a uniform bound in that depth.

## 5. All finite \(L^p\) spaces against the same full reference

### Theorem C2: actual complete transport at each fixed depth

For every integer \(k\ge0\) and every real \(1<p<\infty\),

\[
\boxed{\ \frac{Q^k\rho}{\beta}\in L^p(\beta).\ }
\tag{C11}
\]

The quotient is the literal ratio of atom weights on \(D\); C3 makes
it well-defined.

**Proof.** At its actual endpoint, each surviving original source \(n\)
has the reference allocation \(n^{-4}c_{J_k(n)}\). All of these selected
pairs \((n,J_k(n))\) occur in C2, so C6 gives

\[
\mathcal E_{k,p}:=
\sum_m\frac{(Q^k\rho)(m)^p}{\beta(m)^{p-1}}
\le\sum_{n\ge1}n^{-4}
 \exp\!\left((p-1)[\log(J_k(n)+2)]^2\right).
\tag{C12}
\]

Killing only restricts the original source set. Periodic surviving
sources and endpoint collisions remain in the displayed sum.

Put \(c=1+\frac14\log A\). From C9,

\[
\log(J_k(n)+2)\le d_k(c+\log\ell(n)).
\tag{C13}
\]

For fixed \(k,p\), the resulting exponential of
\(O_{k,p}((\log\log n)^2)\) is \(n^{o(1)}\), proving convergence.
The next calculation gives a quantitative bound and a complete source
tail. QED.

### An explicit bound, retaining its return-index dependence

Set

\[
b=(p-1)d_k^2,\qquad
B_{k,p}=\exp\!\left(2b[c+\log(1+4b)]^2\right).
\tag{C14}
\]

Then

\[
\boxed{\ \mathcal E_{k,p}\le B_{k,p}\zeta(7/2).\ }
\tag{C15}
\]

To verify the constants, write \(v=\log n\) and \(M=1+4b\).
The elementary inequality \(\log(1+x)\le\sqrt x\) for \(x\ge0\)
and \(1+v\le M(1+v/M)\) give

\[
\log(1+v)\le\log M+\sqrt{v/M}.
\]

Consequently

\[
b[c+\log(1+v)]^2
\le2b[c+\log M]^2+\frac{2b}{M}v
\le2b[c+\log M]^2+\frac12v.
\]

Thus the summand in C12 is at most \(B_{k,p}n^{-7/2}\).
This proves C15.

For fixed \(p\), this upper bound has

\[
\log B_{k,p}=O_p(25^k(k+1)^2).
\tag{C16}
\]

It is an actual bound on the full transported law, but is much too large
for the recurrence criteria below. The clock constant from PR176 has
not been numerically extracted; C14 is an analytic bound in that
specified constant, not a numerically certified cutoff.

### Original-source truncations converge in every such norm

Let \(\rho_N=E_*(\sum_{1\le n\le N}n^{-4}\delta_n)\). Applying the
same complete-fiber argument only to labels \(n>N\) gives

\[
\boxed{
\left\|\frac{Q^k\rho-Q^k\rho_N}{\beta}\right\|_{L^p(\beta)}^p
\le \frac25 B_{k,p}N^{-5/2}\qquad(N\in\mathbb N,\ N\ge1).
}
\tag{C17}
\]

The integral bound is
\(\sum_{n>N}n^{-7/2}\le\int_N^\infty x^{-7/2}\,dx\).
The cutoff is imposed on original sources, never on final endpoints or
selected fibers. It therefore retains all collisions involving kept
sources and controls the complete omitted source tail.

## 6. What estimate would now close the nonperiodic alternative?

Let \(z_k\) be distinct returned endpoints of one surviving source, with
unchanged weight \(a>0\). Write
\(\mathcal E_k=\mathcal E_{k,2}\). At each endpoint,

\[
\beta(z_k)\ge\frac{a^2}{\mathcal E_k}.
\tag{C18}
\]

Because beta has every finite logarithmic moment, a common bound

\[
\mathcal E_k=O\!\left((k+1)[\log(k+2)]^M\right)
\tag{C19}
\]

for **any fixed finite \(M\)** would exclude all such sources.
Indeed select a logarithmic moment of order \(r\ge M\) and group
return indices into dyadic blocks. At least half the distinct endpoints
in the block \(2^b\le k<2^{b+1}\) are at least \(2^{b-1}\).
The lower contribution from that block to the reference moment is
bounded below by a constant times \(b^{r-M}\). The sum over blocks
diverges.

The stronger C5 allows a larger target. If, for any fixed \(\gamma<1\),

\[
\boxed{
\mathcal E_k
=O\!\left((k+1)
 \exp\!\{\gamma[\log\log(k+e^e)]^2\}\right),
}
\tag{C20}
\]

then choose \(\max(\gamma,0)<a<1\) in C5. The corresponding dyadic
block contributions grow as

\[
\exp\!\left((a-\gamma)(\log b)^2+O(\log b)\right)
\]

up to a positive constant and therefore cannot be summable.
This would exclude every nonperiodic surviving source. These are
sufficient targets, not estimates proved by C15.

Neither C19 nor C20 alone excludes a nontrivial positive cycle, whose
repeated endpoints can reuse the same reference atoms. A separate
cycle exclusion or a positive-cost killed occupation estimate is still
needed for full Collatz.

## 7. A family closed under actual return transport, with explicit loss

The same construction gives a composition theorem, not just a list of
finite-depth norms. For \(s>1\) and \(a>0\), define

\[
\beta_{s,a}=
\sum_{\substack{n\ge1\\j\ge0}}n^{-s}
 e^{-a[\log(j+2)]^2}\mathbf1_D(U^j(o(n)))
 \delta_{U^j(o(n))}.
\tag{C21}
\]

Every member has all finite logarithmic height moments, by the proof of
C4. The original common reference is \(\beta=\beta_{4,1}\).

### Theorem C3: return-stable family with source and clock parameter loss

For every \(s>s'>1\) and \(a>25b>0\), there is a finite explicit
constant \(K\) such that

\[
\boxed{\ Q\beta_{s,a}\le K\beta_{s',b}.\ }
\tag{C22}
\]

All original labels and all complete endpoint fibers are retained.
The exponent change concerns the original source label \(n\); no weight
is replaced by a power of the current state.

**Proof.** For a marked occurrence \((n,j)\), let \(u>j\) be its next
marked odd clock under the unkilled map. For each fixed original \(n\),
the assignment \(j\mapsto u\) is injective on its marked occurrences:
it takes consecutive visit times to their successors. This remains true
when the endpoint values repeat on a cycle.

The imported return clock and \(U(x)\le2x\), after the same enlargement
of \(A\) as above, give

\[
u+2\le A(\ell(n)+j+1)^5
 \le A\ell(n)^5(j+2)^5.
\]

Write \(x=\log(j+2)\), \(y=\log\ell(n)\), \(c_0=\log A\).
Then \(\log(u+2)\le5x+5y+c_0\). Completing the square gives

\[
b[\log(u+2)]^2-ax^2
\le \frac{ab}{a-25b}(5y+c_0)^2.
\]

Let

\[
\delta=s-s',\qquad
t=\frac{25ab}{a-25b},\qquad
K=\exp\!\left(
2t\left[\frac{c_0}{5}+
       \log\!\left(1+\frac{2t}{\delta}\right)\right]^2
\right).
\]

The same scalar calculation as in C14--C15, with
\(M=1+2t/\delta\), gives

\[
t\left(y+\frac{c_0}{5}\right)^2\le\log K+\delta\log n.
\]

Consequently each complete labeled occurrence obeys

\[
n^{-s}e^{-a[\log(j+2)]^2}
\le K n^{-s'}e^{-b[\log(u+2)]^2}.
\]

The injectivity of \((n,j)\mapsto(n,u)\) permits summation without
counting any target occurrence twice. Grouping arbitrary equal endpoints
preserves the inequality. Killing at 1 only deletes terms. This proves
C22. QED.

The finite quadratic comparison at the heart of this proof is entirely
deterministic. Its source-height and return-clock inputs are explicit.
It does not assert mixing or a fresh-law replacement.

### Bounded operators between these weighted spaces

For any \(1<p<\infty\), any signed \(f\in L^p(\beta_{s,a})\), and
the same parameters,

\[
\boxed{
\left\|\frac{Q(f\beta_{s,a})}{\beta_{s',b}}\right\|_{L^p(\beta_{s',b})}^p
\le K^{p-1}\|f\|_{L^p(\beta_{s,a})}^p.
}
\tag{C23}
\]

Apply Hölder on each actual return fiber with source measure
\(\beta_{s,a}\), then use \(Q\beta_{s,a}\le K\beta_{s',b}\).
The absolute values are controlled by \(Q(|f|\beta_{s,a})\).
Thus the family supplies legitimate spaces for composing actual returns.

For example, one may choose

\[
s_j=2+2^{1-j},\qquad a_j=50^{-j}.
\tag{C24}
\]

Then \(s_0=4\), \(a_0=1\), \(s_j>s_{j+1}>2\), and
\(a_j>25a_{j+1}\) at every step. In the constant from C22,
\(\delta_j=2^{-j}\) and \(t_j=50^{-j}\), so

\[
\sum_{j\ge0}\log K_j
\le\frac{100}{49}\left[\frac{\log A}{5}+\log3\right]^2.
\]

Consequently

\[
Q^k\beta_{4,1}
\le K_*\beta_{2+2^{1-k},\,50^{-k}}
\]

for one finite \(k\)-independent constant
\(K_*=\exp((100/49)[(\log A)/5+\log3]^2)\).
Every reference on the right remains finite with every logarithmic
moment.

The full original entrance law enters this family as well. C9 at
\(k=0\) gives \(J_0+2\le A\ell(n)^5\). The same scalar absorption
with \(t=25\), \(\delta=1\) shows

\[
n^{-4}\le K_0 n^{-3}c_{J_0(n)},\qquad
K_0=\exp\!\left(50\left[\frac{\log A}{5}+\log51\right]^2\right).
\]

Its selected occurrence pairs are part of \(\beta_{3,1}\), so
\(\rho\le K_0\beta_{3,1}\). Now use
\(s_j=2+2^{-j}\), \(a_j=50^{-j}\). The corresponding logarithmic
constant sum has \(\log5\) in place of \(\log3\), and proves the
complete, all-depth domination law

\[
\boxed{
Q^k\rho\le K_0K_{**}
 \beta_{\,2+2^{-k},\,50^{-k}}
\quad(k\ge0),\qquad
K_{**}=
\exp\!\left(\frac{100}{49}
 \left[\frac{\log A}{5}+\log5\right]^2\right).
}
\tag{C24a}
\]

The constant is uniform in the return index; the reference is not.
Every original residual atom is retained.

The loss is material. The clock concentration \(a_j\) tends to zero,
and the resulting references become progressively larger along long
actual histories. C22 therefore does not prove power boundedness, a
critical energy estimate in the single original space, or boundedness
of a critical mixture over \(j\). Its value is an exact
source-preserving composition family in which that loss is measurable.

The reference limit has an ordinary interpretation. By monotone
convergence, \(\beta_{2+2^{-k},50^{-k}}\) increases to the full marked
Green occupation measure with original source weights \(n^{-2}\).
At a nonperiodic marked target \(m\), each original source hits it at
most once, so the limiting atom is at most \(\zeta(2)\). At a
periodic marked target it is infinite, because the source \(n=m\)
returns indefinitely. Thus the full limit is not sigma-finite. On a
hypothetical escaping marked ray, one unchanged original weight would
persist at every distinct returned endpoint, making even the restricted
nonperiodic limit have infinite total mass. Finite individual atoms do
not establish finite total mass or a finite logarithmic moment. This
is the same input/output distinction addressed by the compact Green
map in [POTENTIAL_ATTACK.md](POTENTIAL_ATTACK.md).

## 8. Why finite-depth regularity cannot be upgraded just by interpolation

The reference construction removes two problems: it is finite with strong
height moments, and every actual finite return packet belongs to all its
finite \(L^p\) spaces. It does not make \(Q\) bounded on those spaces
with a useful uniform norm. Finiteness of each \(\mathcal E_{k,p}\)
does not estimate its growth with \(k\).

Here is an explicit deterministic countermodel to an inference using
only the scalar height and access bounds. It is **not** the Collatz map
and does not preserve the actual Collatz phase cocycle or its affine
integer branches.

On the positive odd integers choose \(h_0=256\),
\(h_{j+1}=h_j^2\), and define

\[
q_j=2^{h_j}+1,\qquad a_l=3\cdot2^{l-1}+1.
\]

Set

\[
F(q_j)=a_{h_j},\quad
F(a_l)=a_{l+1}\ (h_j\le l<h_{j+1}-1),\quad
F(a_{h_{j+1}-1})=q_{j+1}.
\tag{C25}
\]

Send every other positive odd integer to 1, and fix 1. These rules
have disjoint source domains. Every edge satisfies \(F(n)\le2n\).

For the **same** constant-70 marked set, every \(q_j\) is marked,
whereas every \(a_l\), \(l\ge256\), is unmarked. The return from \(q_j\)
to \(q_{j+1}\) takes exactly \(h_j^2-h_j+1\) clocks. From an
intermediate \(a_l\), the next mark takes at most \(h_j^2\le l^2\)
clocks. Outside the displayed ray, a mark is reached in at most one
clock. Thus this map has a uniform \(O((1+\log n)^2)\) band-access
and positive-return clock, stronger than the scalar exponent used
above, but the displayed ray escapes.

Its marked gaps grow by at least a factor of two, so every finite
injective prefix of length \(N\) has at most \(2+\log_2(N+1)\)
marked states. This also satisfies the earlier source-uniform
\(O(N/\log N)\) occupation bound.

With source weights \(n^{-4}\), the full lognormal reference and all
the fixed-depth \(L^p\) conclusions C4--C17 still hold for this map,
by exactly the scalar proofs above. Nevertheless, one source at \(q_0\)
keeps an atom \(a=q_0^{-4}\) at each \(q_j\). For any finite \(r>0\),
C4 and C18 imply

\[
\mathcal E_j\ge
\frac{a^2\ell(q_j)^r}{\sum_m\beta(m)\ell(m)^r}
\gg_r h_0^{\,r2^j}.
\tag{C26}
\]

Thus even the quadratic energy grows faster than any polynomial in the
return index. No interpolation argument based only on those scalar
regularity properties can supply C19. A successful improvement must use
additional arithmetic control of the actual Collatz fibers, the
valuation cocycle, or a different cycle-sensitive drift.

## 9. Precise handoff

This pass proves a common finite reference with strong rank moments,
full fixed-depth \(L^p\) transport with original atoms unchanged, an
actual return-stable family with explicit parameter loss, and a
rigorous source-tail estimate. In particular, treating the entrance
residual merely as an uncontrolled tiny measure is no longer necessary
for **finiteness at a fixed return depth**.

The first unsupported step is a sufficiently slow growth estimate for
the actual complete-fiber energy \(\mathcal E_k\), or another estimate
that spends a positive finite budget along every surviving source.
The bound C15 is not at that scale. The countermodel explains why the
new regularity alone cannot supply it.

No universal convergence assertion, growth estimate C19/C20, or
cycle-exclusion premise is installed as an axiom. The common-reference
theorem does not use the source-qualified predecessor-density claim.
