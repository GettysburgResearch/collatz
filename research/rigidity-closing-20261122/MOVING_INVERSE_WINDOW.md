# Canonical inverse paths before the original-source clock

## Status and inputs

This note proves a source-preserving comparison between the canonical inverse
law and windows of one actual escaping orbit. The comparison remains valid at
inverse depths proportional to the forward clock. It yields an explicit
conditional closing criterion in terms of the time needed for the canonical
inverse law to lose its largest complete-path atom. No estimate sufficient to
meet that criterion is proved here, and this is not a proof of Collatz.

The analytic input is the **ordinary harmonic flow** constructed in PR185,
`research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`,
at `980d40fc4afeaaf8f2a9256f322acf3e4568e013`, and used in PR180,
`research/central-step-20261122/CRITICAL_BOUNDARY.md`, at
`a9f471543d7fed0a76f348e6d97a9d6d44fa369e`. Its external analytic dependencies
remain source-qualified. On the retained component it supplies

\[
 0<\nu(n)\le A,\qquad \sum_{Un=q}\nu(n)=\nu(q).
 \tag{1}
\]

Here \(U\) is the accelerated odd Collatz map on retained positive unit
states. Suppose that \(q_i=U^i q_0\) escapes. Then

\[
 v_i:=\nu(q_i)\uparrow C\in(0,A],\qquad v_0>0.
 \tag{2}
\]

The inverse Markov kernel used throughout this note is precisely

\[
 K(q,n)=\frac{\nu(n)}{\nu(q)}\mathbf1_{\{Un=q\}}.
 \tag{3}
\]

It should not be silently identified with another normalized \(G\)- or
\(h\)-transform. The note's deductions require only (1), (2), and the actual
forward orbit. Those elementary deductions are separate from the imported
construction of \(\nu\).

## 1. Exact retracing and total variation

For a root index \(i\ge r\), the probability under \(K\) of the complete
inverse path
\((q_i,q_{i-1},\ldots,q_{i-r})\) is exactly

\[
 \prod_{j=0}^{r-1}\frac{v_{i-j-1}}{v_{i-j}}
       =\frac{v_{i-r}}{v_i}.
 \tag{4}
\]

Let \(I\) be uniform on \(\{r,\ldots,N\}\). Define two probability laws on
**labelled complete paths**:

* \(\mathsf P_{N,r}\): sample \(I\), then sample an \(r\)-step inverse
  \(K\)-path from \(q_I\), keeping \(I\) in the output;
* \(\mathsf Q_{N,r}\): sample the same \(I\), then output
  \((I,q_I,q_{I-1},\ldots,q_{I-r})\).

Use \(\|P-Q\|_{\rm TV}=\sup_E|P(E)-Q(E)|\), or half the \(\ell^1\)
distance on a countable space. Each conditional \(\mathsf Q\)-law is a
point mass, so (4) gives the equality

\[
 \boxed{\|\mathsf P_{N,r}-\mathsf Q_{N,r}\|_{\rm TV}
   =\frac1{N-r+1}\sum_{i=r}^N
       \left(1-\frac{v_{i-r}}{v_i}\right).}
 \tag{5}
\]

In particular this is a comparison with the original orbit, without
replacing its source by a stationary, size-biased, or sibling source law.
Projection to valuation words, residues, or endpoints preserves the upper
bounds below, though equality in (5) need not survive a projection.

Since \(v_i\ge v_0>0\), the summand is at most
\((v_i-v_{i-r})/v_0\). Write \(\Delta_j=v_{j+1}-v_j\ge0\). Each
\(\Delta_j\), \(0\le j<N\), occurs in at most \(r\) of the relevant
windows. Therefore

\[
 \sum_{i=r}^N(v_i-v_{i-r})
 \le r\sum_{j=0}^{N-1}\Delta_j
 =r(v_N-v_0)\le r(C-v_0),
\]

and hence

\[
 \boxed{\|\mathsf P_{N,r}-\mathsf Q_{N,r}\|_{\rm TV}
 \le\frac{r(C-v_0)}{v_0(N-r+1)}.}
 \tag{6}
\]

This covers \(r=0\) and \(r=N\). The right side may exceed one; it is an
upper bound, not an asserted probability. In particular it tends to zero
whenever \(r=o(N)\). The finite sum estimate uses the same counting lemma
as `OriginalSourceEntropy.sliding_window_cost_le`.

## 2. The stronger linear-depth comparison

The averaging in (6) is not essential if all windows end sufficiently far
along the original ray. Let \(I\) have **any** probability law supported on
indices satisfying \(I-r\ge L\). Equations (2), (4) give

\[
 \boxed{\|\mathsf P-\mathsf Q\|_{\rm TV}
 \le 1-\frac{v_L}{C}.}
 \tag{7}
\]

For example, sample \(I\) uniformly on \(\{N,\ldots,2N\}\) and take
\(r\le N-L\). If \(L=L_N\to\infty\), the error in (7) tends to zero.
This allows \(r\) to be proportional to \(N\), or even
\(r=N-L_N\) with \(L_N=o(N)\).

At the single moving root \(q_N\), the complete inverse path of length
\(N-L_N\) retraces the same orbit with exact probability

\[
 \frac{v_{L_N}}{v_N}\longrightarrow1.
 \tag{8}
\]

No convergence rate for \(C-v_L\) is asserted. In particular this does
not provide an algorithmic inverse mixing time.

There is also a uniform-shift average that permits arbitrarily large
inverse depths. Sample \(J\) uniformly from \(\{0,\ldots,M\}\) and set
\(I=r+J\). Then, for every \(r\ge0\), the full-path distance is

\[
 \varepsilon_{M,r}
 =\frac1{M+1}\sum_{j=0}^M\left(1-\frac{v_j}{v_{r+j}}\right)
 \le\eta_M:=1-\frac1{(M+1)C}\sum_{j=0}^M v_j
 \longrightarrow0.
 \tag{8a}
\]

The convergence of \(\eta_M\) is Cesàro convergence of \(v_j\to C\);
the bound is uniform over **all** \(r\). The companion note
`SAME_SOURCE_INVERSE_ENTROPY.md` proves the exact endpoint version and
its entropy consequence, retaining the same original source. In that
version endpoint TV equals \(\varepsilon_{M,r}\), and
\(\sup_r\varepsilon_{M,r}=\eta_M\). For a general residue or word
projection only an upper bound is asserted.

At depth exactly \(N\), the original point \(q_0\) instead has path
probability \(v_0/v_N\to v_0/C>0\). Thus substantial branching cannot
begin arbitrarily far before the original-source clock. No upper bound
on the time when it does begin follows from this argument.

## 3. A finite ordinary-state stationarity consequence

Put \(\pi_N=(N+1)^{-1}\sum_{i=0}^N\delta_{q_i}\). Compare
\(K_*\pi_N\) with

\[
 \rho_N=\frac1{N+1}\left(K(q_0,\cdot)+
                   \sum_{i=1}^N\delta_{q_{i-1}}\right).
\]

The first rows agree, and (4) with \(r=1\) bounds the remaining rows.
Moreover \(\rho_N-\pi_N=(K(q_0,\cdot)-\delta_{q_N})/(N+1)\), whose
TV norm is at most \(1/(N+1)\). Consequently

\[
 \|K_*\pi_N-\pi_N\|_{\rm TV}
 \le\frac{1+(C-v_0)/v_0}{N+1}
 =\frac{C}{v_0(N+1)}.
 \tag{9}
\]

These are probabilities on ordinary integer states. Escape makes them
non-tight there. Passing to a compact ternary space does not automatically
make \(K\) Feller or make a weak limit \(K\)-stationary. Equation (9)
does not justify that additional limiting step.

## 4. What the coupling does to conditional word entropy

Map each inverse valuation to an alphabet of \(E\ge2\) symbols, for
example by capping the valuation. The \(r\)-letter word alphabet has at
most \(E^r\) elements. Let \(\varepsilon\) denote the average probability
that the complete inverse path fails to retrace its actual window.
Adjoin the binary indicator of that event. Conditional on the root label,
the success word is determined. The chain rule and concavity of binary
entropy therefore give

\[
 H(\text{capped inverse word}\mid I)
 \le h_b(\varepsilon)+\varepsilon r\log E.
 \tag{10}
\]

This proof remains valid if an incorrect complete path nevertheless has
the same capped word. It does not require an equality between path error
and capped-word error. From (7), the normalized **conditional** entropy
tends to zero at the permitted linear depths.

The unconditional mixture over roots can still have entropy from the
choice of \(I\). Nor does (10) identify an entropy rate of a ternary weak
limit. Those are different assertions with different orders of limits.

## 5. An explicit closing target: the largest-path-atom clock

For fixed \(0<\varepsilon<1\), define

\[
 M_r(q)=\sup_{\omega:\,|\omega|=r}\mathbb P_q^K(\omega),\qquad
 \tau_\varepsilon(q)=\inf\{r\ge0:M_r(q)\le1-\varepsilon\},
 \tag{11}
\]

where the infimum is infinity if the set is empty. These are **complete
path atoms**, not ternary fibre masses or endpoint densities. The
sequence \(M_r(q)\) is nonincreasing because each path atom is partitioned
by its next step.

Choose \(J\) with \(v_J>(1-\varepsilon)C\). For every \(N\ge J\),
the actual reversed path of length \(N-J\) has mass
\(v_J/v_N>1-\varepsilon\), so

\[
 \boxed{\tau_\varepsilon(q_N)>N-J.}
 \tag{12}
\]

This gives a precise test for a proposed inverse regularization theorem:
its onset must occur **before** \(N-J\) if it is to contradict escape.
Fixed-root atomlessness at unspecified depth is insufficient.

For example, consider the following additional, currently unproved premise:
there are \(a>0,b\in\mathbb R\) such that, on every sufficiently late root
of any retained escaping ray,

\[
 \tau_\varepsilon(q)\le a\log(q+2)+b.
 \tag{13}
\]

Combining (12) and (13) forces

\[
 \liminf_{N\to\infty}\frac{\log(q_N+2)}N\ge\frac1a.
 \tag{14}
\]

Thus (13) would exclude every zero-exponential-speed escape. The elementary
Collatz growth estimate \(q_N+1\le(3/2)^N(q_0+1)\) shows that a bound with
\(a<1/\log(3/2)\) would exclude **all** escape. More generally, an onset
\(\tau_\varepsilon(q_N)\le N-L_N\) with \(L_N\to\infty\) is
incompatible with (12), independently of a height estimate.

The premise (13) is the missing mathematical estimate, not an imported
fact. Writing it as a mixing assumption does not prove it. A root-uniform
positive conditional entropy bound at these same clocks would also
contradict (10), but requires its own proof.

## 6. Test against the newest available mixing results

The refreshed PR175 at `08fe1388ad63c758680b3695249aca319515c47d`,
`research/lean-global-closure-20261121/machinery/MOVING_CESARO_FIBRES.md`,
Theorem 2 and equations (23), (28), (30), proves mean bounded-Lipschitz
convergence uniformly in the moving forward clock \(k\), at ternary
precision \(k+r+1\), as the excess depth \(r\) is Cesàro averaged.
This is **past** the original-source clock. Equation (32) retains a
persistent positive original-source submeasure. Section 9 expressly gives
no quantitative rate or vanishing-amplitude conclusion. This theorem is
compatible with (7), (8), and (12); it is not the path-atom bound (13).
Its transform must also be kept distinct from (3) until a comparison is
explicitly applied.

The primary manuscript [First-landing bounds and canonical inverse laws
for Collatz, Paper 12](https://rstation.ai/problems/collatz/papers/12),
especially Sections 8–12, 16, and 18, supplies fixed-root selection and
canonical word-frequency conclusions under its stated inputs. Section 18
does not give a root-uniform waiting time. Its ancestor-label tail controls
labels, which must not be substituted for physical parent height. These
statements do not yield (13). The distinction is also explicit in
[Paper 105](https://rstation.ai/problems/collatz/papers/105), which studies
the additional hypotheses needed to pass from ancestor labels to physical
parent tails. Neither manuscript is used as an unqualified proof of a
uniform onset estimate here.

The symmetric-network route has also been checked against the refreshed
PR176 at `00018ce11fa657b5f3fae072e5567a1d93184c2b`,
`overview/machinery/CRITICAL_NETWORK.md`, and PR178 at
`9d4ae09cd50ccd54036141edc3938d2cabe786fd`,
`boundary/RECURRENCE_AND_AFFINE_BOUNDARY.md` in their research trees.
They already establish recurrence of the symmetrized clock network and
failure of the strong sector bound. A transient Green-function boundary
Harnack theorem cannot be inserted into that recurrent network without
checking a different operator and its hypotheses. For example,
[Gouëzel's Martin-boundary theorems](https://arxiv.org/pdf/1302.5388)
assume specified random walks on hyperbolic groups and Green-function
conditions; exponentially decaying jumps alone do not supply their
conclusion. No such import proves (13) or the sibling coercivity bound.

## Deliverable boundary

The new result is the full-path comparison (5)–(8a), with its ordinary
stationarity consequence (9), conditional entropy implication (10), and
the sharp necessary onset (12). The scalar inequalities underlying (6)
and (7), together with the uniform-shift mean bound (8a), are formalized
in `lean/CanonicalRetracing.lean`. The canonical
harmonic-flow construction, probability-law interpretation, entropy
argument, and asymptotic closing criterion remain explicit mathematical
arguments in this note, not claims of kernel verification. The central
unproved step is still an arithmetic estimate forcing branching or
sibling loss before the original source has been reached.
