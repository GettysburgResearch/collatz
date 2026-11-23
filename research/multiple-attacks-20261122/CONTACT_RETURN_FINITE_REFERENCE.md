# A finite reference for actual returns to the canonical contact set

**Status:** complete written deductions from the explicitly pinned ordinary
harmonic-flow inputs. Seven finite algebra and iteration statements are
checked in `ContactReturnContraction.lean`. The construction of that flow,
the countable return operator, and the logarithmic series argument remain
written mathematics. No full Collatz convergence claim is made.

The new point is a genuine finite reference for a source-retaining return
operator. It comes with geometric collision-energy contraction, deterministic
height descent at successive forward contacts, and a summable logarithmic
cost along the actual inverse contact chain. The return clock counts visits
to a specified section. The ordinary excursion durations and the fate of
last-contact exits remain separate.

## 1. Frozen input and domain

The source is PR185 at
`7889fc680f5ee22237732eccc172b1699ef565da`,
`research/whole-repo-closure-20261122/ORDINARY_HARMONIC_FLOW_AND_COLLISIONS.md`,
SHA256 `34340b2dafc1b37cf07ab2a401cccf2f7481af8dc6265ba521e4cce4a154454b`.
Its source-qualified predecessor-population and canonical-envelope
dependencies are retained here; they are not introduced as Lean axioms.

Let

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}
\]

on positive odd integers. Let \(\mathcal N\) consist of the positive odd
integers not divisible by three which are **not themselves periodic**.
Their forward paths are killed on first entering any periodic orbit.
Every unit predecessor of a member of \(\mathcal N\) is in
\(\mathcal N\), and every path ending there is injective.

The pinned construction supplies positive functions \(G,V,\nu\) and
constants \(0<\gamma\le1\), \(0<\delta\le1\), with

\[
L\nu=\nu,\qquad
\frac{\gamma}{q}\le\frac{G(q)}q\le\nu(q)
\le\frac{G(q)}{\delta q}\le\frac{V(q)}{\delta q},
\tag{1}
\]

where \((Lf)(q)=\sum_{U(n)=q,n\in\mathcal N}f(n)\).
We may reduce an originally supplied \(\gamma\) to \(\min(\gamma,1)\).
The explicit global correction in the source permits
\(\delta=\exp(-200/3)\). Also \(\nu\) has a finite global upper
bound, although the main theorem below does not require that bound.

Fix \(M\ge1\) and define

\[
\mathcal C_M=\{q\in\mathcal N:V(q)\le M\},\quad
\varepsilon=\frac{3\delta\gamma}{64M},\quad
\rho=1-\varepsilon,\quad \kappa=-\log\rho>0.
\tag{2}
\]

Then \(0<\varepsilon\le3/64\), so \(0<\rho<1\).
For every contact state,

\[
\frac{\gamma}{q}\le\nu(q)\le\frac{M}{\delta q}.
\tag{3}
\]

The familiar almost-sure first-contact theorem is available when \(M>1\),
but the finite-reference contraction only needs the subprobability bound
proved below. No first-contact timing estimate is imported.

## 2. Two short physical parents force a uniform branching loss

For a positive odd unit \(q\), exactly two exponents \(1\le e\le6\)
produce unit parents \(n_e=(2^e q-1)/3\). Indeed \(2^e q\) runs through
the six units modulo nine, and the required residues are four and seven.
The complete finite table is

| \(q\bmod9\) | The two exponents |
|---|---|
| 1 | 2, 4 |
| 2 | 1, 3 |
| 4 | 2, 6 |
| 5 | 3, 5 |
| 7 | 4, 6 |
| 8 | 1, 5 |

Both are positive odd ordinary parents, both are nonperiodic if \(q\) is,
and both satisfy \(n_e<64q/3\). From (1) and (3), at a contact target

\[
\frac{\nu(n_e)}{\nu(q)}
\ge\frac{\gamma/n_e}{M/(\delta q)}
>\frac{3\delta\gamma}{64M}=\varepsilon.
\tag{4}
\]

Consider any proper unit ancestor \(x\) of a contact \(q\). Its unique
path to \(q\) uses one immediate parent of \(q\). At least one of the
two parents in (4) is a different parent, with a disjoint ancestor branch.
Harmonicity therefore bounds the used parent's mass by
\((1-\varepsilon)\nu(q)\). Along the rest of the ancestor path,
harmonicity gives monotonicity of \(\nu\). Consequently

\[
\boxed{x\ne q,\ U^j(x)=q\in\mathcal C_M
\quad\Longrightarrow\quad \nu(x)\le\rho\nu(q).}
\tag{5}
\]

This statement holds for every physical ancestor, not merely with high
probability under a selected law. The ancestor itself need not be a
contact state. The nonperiodic domain ensures that different incoming
branches cannot secretly merge before reaching \(q\).

## 3. The next-contact operator retains the original sources

For \(x\in\mathcal C_M\), let \(R(x)\) be its first strictly later
contact along its actual forward orbit, if one exists before killing.
If no such contact exists, \(R(x)\) is undefined. Define

\[
(Ja)(q)=\sum_{\substack{x\in\mathcal C_M\\R(x)=q}}a(x).
\tag{6}
\]

This is ordinary forward transport of the unchanged original masses
\(a(x)\). It counts one contact return. Sources without a later contact
are killed by this induced operator, including possible escaping sources
after their last contact. This is deliberately different from killing
only on actual entry into a periodic orbit.

For a fixed \(q\), its first-return contact ancestors form an antichain
in the actual inverse tree. Every finite subcollection has \(\nu\)-mass
at most \(\nu(q)\): expand harmonicity to a depth exceeding all its
source-to-target depths, and retain the disjoint branches. Increasing
finite subcollections gives

\[
\sum_{R(x)=q}\nu(x)\le\nu(q).
\tag{7}
\]

Thus

\[
K_M(q,x)=\mathbf1_{R(x)=q}\frac{\nu(x)}{\nu(q)}
\tag{8}
\]

has row sums at most one. It is the actual inverse first-return kernel,
with any missing mass corresponding to absence of inverse return. For
the thresholds to which the pinned almost-sure contact theorem applies,
the row sums equal one. That equality is not needed below.

Each column of (8) has at most one nonzero entry, because an original
source has at most one next forward contact. By (5), every entry is at
most \(\rho\). The distinction between row and column bounds is essential.

## 4. A finite strictly subinvariant reference

Set

\[
\boxed{\sigma(q)=\nu(q)^2\mathbf1_{\mathcal C_M}(q).}
\tag{9}
\]

Unlike the original ordinary reference \(\nu\), this reference has
finite total mass:

\[
\boxed{\Sigma_M:=\sum_q\sigma(q)
\le\left(\frac M\delta\right)^2\sum_{n\ge1}n^{-2}
\le2\left(\frac M\delta\right)^2<\infty.}
\tag{10}
\]

The last inequality follows from one term plus the elementary integral
of \(t^{-2}\) over \([1,\infty)\).

The source-fiber bound (5) and row budget (7) now give

\[
\begin{aligned}
(J\sigma)(q)
&=\sum_{R(x)=q}\nu(x)^2\\
&\le\rho\nu(q)\sum_{R(x)=q}\nu(x)
\le\rho\nu(q)^2.
\end{aligned}
\]

Therefore

\[
\boxed{J\sigma\le\rho\sigma.}\tag{11}
\]

This is a finite reference for the actual induced source transport,
with a strict factor independent of the contact state and the excursion
duration. It is not a finite invariant measure on all ordinary states.

## 5. Geometric retained-source collision contraction

For a nonnegative original source mass supported on \(\mathcal C_M\), put

\[
\mathcal E_\sigma(a)=\sum_{q\in\mathcal C_M}
\frac{a(q)^2}{\nu(q)^2}.
\tag{12}
\]

Assume this is finite. Cauchy--Schwarz on each exact fiber gives

\[
\frac{(Ja(q))^2}{\sigma(q)}
\le\frac{J\sigma(q)}{\sigma(q)}
\sum_{R(x)=q}\frac{a(x)^2}{\sigma(x)}
\le\rho\sum_{R(x)=q}\frac{a(x)^2}{\sigma(x)}.
\]

Every original source occurs in at most one fiber. Summation therefore
proves

\[
\boxed{
\mathcal E_\sigma(J^k a)\le\rho^k\mathcal E_\sigma(a),
\qquad k\ge0.
}\tag{13}
\]

Countable fibers cause no extra assumption: prove the inequality for
finite subcollections, then use nonnegative convergence. The colliding
sources stay inside \((\sum a(x))^2\); no collision is discarded.

The finite reference permits Cauchy--Schwarz once more:

\[
\boxed{
\|J^k a\|_1
\le\sqrt{\Sigma_M\mathcal E_\sigma(a)}\,\rho^{k/2}.
}\tag{14}
\]

For the canonical contact seed \(a=\sigma\), (11) gives the stronger
pointwise inequality \(J^k\sigma\le\rho^k\sigma\), hence

\[
\sum_{k\ge0}\|J^k\sigma\|_1
\le\frac{\Sigma_M}{1-\rho}.
\tag{15}
\]

Thus there is a finite all-source occupation budget in contact time.
This resolves the finite-reference cost for this induced operator.
The analogous claim for ordinary time does not follow from (15).

## 6. Deterministic height descent and visit bounds

Let \(q_0,q_1,\ldots,q_k\) be successive forward contacts, so
\(R(q_i)=q_{i+1}\). Equation (5) gives
\(\nu(q_i)\le\rho\nu(q_{i+1})\). Using (3) at both ends,

\[
\frac\gamma{q_0}\le\nu(q_0)
\le\rho^k\nu(q_k)\le\rho^k\frac M{\delta q_k}.
\]

Consequently

\[
\boxed{q_k\le\frac M{\delta\gamma}\rho^k q_0.}\tag{16}
\]

After more than \(\log(M/(\delta\gamma))/\kappa\) contact returns,
the actual contact height is strictly below its initial value.
Since all heights are positive integers, the number of returns obeys

\[
\boxed{k\le\frac{\log(Mq_0/(\delta\gamma))}{\kappa}.}\tag{17}
\]

This is an explicit bound on the number of contacts before the induced
transport is killed. It does not decide whether that final exit reaches
a periodic orbit or escapes while avoiding later contacts.

More generally, for any starting unit \(x\in\mathcal N\), harmonicity
gives \(\nu(q_0)\ge\nu(x)\ge\gamma/x\) at its first future contact.
The same proof replaces \(q_0\) on the right of (16)--(17) by \(x\).
The bound therefore depends on the original physical source, even if its
first contact comes after a long excursion.

## 7. Exponential height growth and logarithmic costs in the inverse direction

Let \(x_0,x_1,\ldots\) be an actual inverse contact-return chain.
The mass inequalities now run in the other direction:

\[
\nu(x_j)\le\rho^j\nu(x_0),\qquad
\boxed{x_j\ge\frac{\delta\gamma}{M}\rho^{-j}x_0.}
\tag{18}
\]

These hold for every finite realized return chain and hence for every
infinite one. In the thresholds covered by almost-sure first contact,
the strong Markov argument supplies infinitely many such returns under
the actual ordinary harmonic inverse law. No geometric exponent law has
been substituted.

Put \(c_0=\delta\gamma/M\le1\) and
\(J_0=\lceil\log(1/c_0)/\kappa\rceil\). For \(j=J_0+\ell\),
\(\ell\ge1\), equation (18) gives \(x_j\ge e^{\kappa\ell}\), since
\(x_0\ge1\). For every real \(A>1\),

\[
\boxed{
\sum_{j\ge0}\frac1{\log(2+x_j)^A}
\le\frac{J_0+1}{(\log3)^A}
+\kappa^{-A}\left(1+\frac1{A-1}\right)<\infty.
}\tag{19}
\]

The bound is uniform in the initial contact and in the realized return
chain. Its expectation under any of the actual return laws satisfies the
same bound. This specifically repairs the prior obstruction to summing
logarithmic errors **after inducing on contacts**. A sequence growing
only polynomially in its contact index cannot satisfy (18).

## 8. The excursion factor that still has to be paid

For a returning contact \(x\), let \(\ell(x)\) be the actual number
of odd steps to \(R(x)\). The original time spent on those excursions is

\[
\sum_{k\ge0}\sum_x (J^k a)(x)\ell(x).
\tag{20}
\]

The theorem bounds (20) with \(\ell\) replaced by one. It does not
bound \(\ell\). If one separately knew
\(\sum_x\sigma(x)\ell(x)^2<\infty\), then (13) and
Cauchy--Schwarz would give the useful explicit implication

\[
\sum_{k\ge0}\sum_x(J^ka)(x)\ell(x)
\le
\frac{\sqrt{\mathcal E_\sigma(a)}
\sqrt{\sum_x\sigma(x)\ell(x)^2}}
{1-\sqrt\rho}.
\tag{21}
\]

No such excursion bound is proved here. The last segment must also be
retained: a contact with no next contact can either enter a periodic
orbit or escape forever. Assigning the latter segment infinite duration
would make any finite positive-source excursion budget exclude it, but
finiteness cannot be inferred from (11)--(19).

The earlier same-target mixing estimate contains a factor depending on
the full inverse prefix depth. Replacing that depth by the number of
contact visits would discard precisely the excursion duration in (20).
The new logarithmic occupation theorem pays errors charged only at return
endpoints. It does not justify this replacement for a bound that still
charges every ordinary step.

Increasing \(M\) does not remove the problem for free. The section
eventually contains each fixed ordinary state, but
\(1-\rho=3\delta\gamma/(64M)\to0\) and the finite reference bound
in (10) grows with \(M\). On a hypothetical escaping path,
\(\nu(q_i)\) stays bounded below by a positive number, so the uncut
sum \(\sum_i\nu(q_i)^2\) is infinite. A uniform limit of the finite
section estimates has not been established.

PR176's new last-contact measure at
`c83a8459066d8223aefe7fc5f6b75faeea557345`,
`research/lean-global-resolvent-20261121/overview/whole/ORDINARY_LAST_CONTACT_MEASURE.md`,
identifies the surviving exit sector explicitly: its original-source
weights are \(\eta(x)=\nu(x)\mathbf1_{\{x\text{ is an escaping last contact}\}}\),
with total mass equal to the sum of escaping component capacities.
Our induced operator kills exactly such last-contact sources as well as
ordinary terminating exits. Its contraction cannot silently identify the
two outcomes.

## 9. Formal and analytic verification

`ContactReturnContraction.lean` proves seven public statements:

- `square_reference_row`: the finite algebra of (11).
- `fiber_energy_bound`: normalized Cauchy--Schwarz on an exact source fiber.
- `finite_source_energy_contraction`: disjoint forward fibers charge each original source once.
- `geometric_energy_bound`: full iteration of the contraction factor.
- `forward_contact_mass`: geometric growth of reference mass at forward contacts.
- `forward_contact_height`: the finite physical-height inequality underlying (16).
- `inverse_contact_height`: the finite physical-height inequality underlying (18).

The module passed strict Lean 4.34.1 with warnings as errors against
Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. All seven public axiom
reports contain only `propext`, `Classical.choice`, and `Quot.sound`.
The integrated strict command is reproduced by `check.py`; published
execution records are kept in `reports/multiple-attacks-20261122/` at
the repository root.

The ordinary flow construction, the explicit short-parent argument, the
countable antichain bound, and the passage from finite rows to countable
operators are written deductions. No arbitrary real orbit, stationary
residue sample, or independent random word replaces an ordinary source.
The result concerns a contact section in the nonperiodic domain, and does
not exclude additional positive cycles or the final escaping excursions.
