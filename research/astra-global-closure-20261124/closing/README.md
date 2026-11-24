# Positive predecessors, cycle rank, and adelic continuation

This continuation of PR #195 constructs additional ordinary smaller partners,
proves a pointwise conditional bound on the **full** denominator of a rational
cycle, and applies an adelic algebraization theorem to the generating series
of one hypothetical escaping orbit. The positive finite merger results have
end-to-end Lean proofs. The infinite analytic and Diophantine conclusions
remain written proofs with separately checked finite cores.

**Collatz remains OPEN.** No result below supplies a successful merger for
every positive integer, excludes every nontrivial integer cycle, or rules
out every injective orbit. The last section identifies the exact outstanding
inferences.

The preceding packet at commit
\(a24ef018147a1e16bf314d14085e2d0d6c620d32\) remains unchanged. This continuation
uses the later heads of PRs #192–194 and #196–198, with a frozen
[frontier snapshot](../../../reports/astra-global-closure-20261124/closing/frontier-snapshot.json).
The comparison is a review of selected load-bearing claims, not a fresh
audit of every proof in all those branches.

## 1. Ordinary predecessors on every positive ternary height

Use the shortcut convention
\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]
Let \(H\ge1\), \(v>0\), and \(d\ge1\), and suppose
\[
3^d\mid 2+4^H v,\qquad 2^{2H+d}\le3^{H+d}.
\]
Set
\[
n=1+3^H v,\qquad
u=\frac{2+4^H v}{3^d},\qquad m=2^d u-1.
\]
Then
\[
\boxed{0<m<n,\qquad m\text{ odd},\qquad T^{d+2H}(m)=n.}
\]

The first \(d\) iterates follow the all-odd word, ending at \(1+4^H v\).
The identity \(T^2(1+4x)=1+3x\) then gives \(H\) ordinary two-step segments
ending at \(n\). The precise descent margin is
\[
3^d(n-m)=2(3^d-2^d)
       +v\bigl(3^{H+d}-2^{2H+d}\bigr)>0.
\]
The Lean theorem \(\texttt{HeightPartner.height_partner}\) proves positivity,
oddness, strict descent and the literal iterate equality under finite integer
conditions. It does not assume convergence of the smaller integer.

Choose the least uniform exponent
\[
d_H=\left\lceil H\frac{\log(4/3)}{\log(3/2)}\right\rceil.
\]
The congruence forces \(v\equiv1\pmod3\), so \(H\) is exactly
\(v_3(n-1)\); it cannot be adjusted freely for a prescribed input.
For \(H\ge3\) and \(v\equiv2\pmod4\), these sources lie in the odd marked
section \(n\equiv55\pmod{108}\) of the repository's reverse-closure problem.
The relative natural density of these disjoint congruence classes is
\[
\delta=\sum_{H\ge3}\frac{27}{3^{H+d_H}}
       =0.050964047368156957\ldots .
\]
This is the scope of this predecessor construction, including its overlap
with older certificates. It is **not** a claim of that much newly established
Collatz convergence. The tail of the density sum is controlled by the
corresponding ternary-divisibility class, rather than by an unjustified
exchange of infinite unions and densities.

For instance, \(H=d=3\) gives \(n\equiv1891\pmod{2916}\), and
\[
T^9(1327)=1891.
\]
At every exact height \(H\ge3\) there are also infinitely many sources in
this family with \(n=(2^e+1)/3\), so that the other marked arm
\(3n-1=2^e\) has an explicit convergence witness. A congruence for \(2^e\)
modulo \(3^{H+1+d_H}\) supplies them. The source varies when the exponent is
chosen; this does not select a successful partner for every fixed source.

A universal smaller *predecessor of the source itself* would be too strong:
55 has no positive predecessor smaller than 55, although its own orbit
converges. The finite computation plus the closed 1–2 cycle proves this
all-clock statement in Lean. A universal merger with a **later** iterate is
a different possible route.

Details, scope and source: [descent packet](descent/README.md),
[HeightPartner.lean](descent/HeightPartner.lean),
[independent reconstruction](../../../reports/astra-global-closure-20261124/closing/descent/INDEPENDENT_REVIEW.md).

## 2. Two residual block continuations after a legal LPP history

For the accelerated odd map, use blocks \(L=(2,1)\) and \(P=(1,4)\).
Their boundary identities are \(8q'=9q+7\) and \(32q'=9q+5\).
PR #192 proves smaller partners for 13 of the 16 five-letter continuations
beginning at the first P after an initial light run. Its three remaining
words are PPLLL, PLLPP and PLLPL.

Suppose the prescribed initial boundary \(q_0\) has an actual preceding
LPP history, starting at \(x\). Write
\[
\xi=\frac{q_0+7}{2},\qquad
m=\frac{128q_0+349}{243}=\frac{3x+101}{64}.
\]
The raw history gives
\[
2^{13}q_0=729x+2207,\qquad \xi\equiv229\pmod{729}.
\]
Thus \(m\) is a positive odd integer, smaller than both \(q_0\) and the
initial light intermediate \((3q_0+1)/4\). Its first eight shortcut steps
have word 11110111 and reach \(9\xi-10\). The three-step identity
\[
T^3(8z-10)=9z-10
\]
then transports this partner through an arbitrary initial run \(L^r\).
For each of the following actual suffixes it joins the source's final
boundary:

| Source prefix after \(q_0\) | Source clocks | Partner clocks |
|---|---:|---:|
| \(L^r\mathrm{PLLPP}\) | \(3r+21\) | \(3r+28\) |
| \(L^r\mathrm{PLLPL}\) | \(3r+19\) | \(3r+26\) |

The preceding LPP history can itself have any prescribed finite L/P history
prepended, by the ordinary dyadic cylinder of the complete word. This is
different from the two additional ternary guards in this packet: those
cover all three residual words but can occur only at entry or after at
most two preceding L/P letters. Those history restrictions are proved and
kept explicit.

The sustained LPP result covers two residual words **at a source with this
specified past**. Together with the inherited 13 cases it gives 15 of 16
at that source when \(r\ge3\). It does not force an arbitrary least
nonconverger to have the LPP past, and PPLLL is unresolved by this
particular construction. A successful merger below a later state is not
automatically below an earlier minimum.

An additional seven-letter past construction reaches a smaller predecessor
in 22 clocks. Independent review found that PR #192 already supplies an
even smaller predecessor on that same cylinder in 23 clocks. It is
retained as an alternative exact certificate, with no coverage claim.

There is a separate direct-predecessor result with unrestricted future.
If an actual history PLPPPLPPLPPP ends at \(q\), and the next two shortcut
steps give the integer \(f=(3q+1)/4\), the raw equations force
\[
f=63938345869+3^{24}j,\qquad j\ge0.
\]
Then
\[
m=62228755903+2^{38}j<f,\qquad
\boxed{T^{38}(m)=f}.
\]
The history itself has no consecutive L's, and its resulting ternary class
differs from both the height-three family above and the LPP class. Its
literal 38-step theorem is proved in Lean from the twelve raw block
equations, deriving the congruence internally. A genuine following L
puts \(f\) in the odd marked section; the proof needs only its first two
shortcut clocks. The comparison with PR #192 is limited to its six
explicit prescriptions begun inside this history, not all possible
earlier merger methods. See [the full certificate](descent/LONG_PAST.md)
and [LongPast.lean](descent/LongPast.lean).

Source comparison:
[PR #192, six-prefix code at the reviewed head](https://github.com/GettysburgResearch/collatz/blob/d2081d1cd2410e6004eaee9f9b13c5553afaf3f4/research/astra-closure-attack-20261124/DESCENT_EXTENSION.md).
Full new proofs and formalization:
[descent packet](descent/README.md).

### Transport below the original floor through arbitrarily many PLL blocks

A final written extension addresses part of the late-hit floor problem
directly. For every actual prefix
\[
L^r(PLL)^sW,\quad r\ge2,\quad s\ge1,\quad
W\in\{PPLP,PLPP,PLPL,PPLLP\},
\]
write \(q_0+7=2^{3r+1}v\), choose \(\ell=1\) when \(s\) is even and
\(\ell=0\) when it is odd, and put \(m=2^{2r+\ell}v-1\).
Then \(m\) is below **both original floors**, and reaches the actual final
boundary of \(W\). The comparison uses a four-state cycle of affine
expressions through the repeated PLL block; the selected initial ramp
places it at a joining state regardless of the number of repetitions.
The PPP exit is also covered for \(s\equiv2,3\pmod4\).

The root and an independent agent checked all fourteen exact affine
identities, positivity, integrality and the original-floor bound.
This extension is a **written proof**, separate from the eight compiled
Lean modules. It leaves the PLLL exit and the other PPP phases open
for this construction. See [the parametric proof](descent/PLL_TRANSPORT.md)
and [exact identity controls](../../../reports/astra-global-closure-20261124/closing/descent/pll-identities.json).

## 3. A pointwise full-denominator bound from dependence of actual centers

Take a primitive positive rational shortcut cycle of period \(A\), odd
count \(p\), and complete reduced denominator \(d\). Rotate it to its
minimum \(m/d\). At each cut \(j\), close the remaining suffix by itself;
write its rational affine fixed point as \(c_j=a_j/b_j\) in lowest terms,
with \(b_j>0\). These centers are auxiliary rational values, and need
not be actual states of the original cycle.

For \(1\le t<A\), if one of the first \(t\) centers is zero or their
nonzero absolute values are multiplicatively dependent, the written
argument proves
\[
\boxed{\log d\ge\frac At\log2-O(t+\log(2A)).}
\]
For bounded rank \(r\), taking \(t=r+1\) gives
\[
d\ge2^{A/(r+1)}A^{-O_r(1)}.
\]
This bounds the full reduced denominator of an individual candidate,
rather than one selected factor or an average over parity words.

The mechanism keeps both endpoints of every actual cut. The two-logarithm
estimate gives almost exponential reduced denominators \(b_j\) for cuts
near the minimum. Congruence identities bound cancellation against both
the numerator and the denominator of every other center. A proposed
multiplicative relation, examined at its largest coefficient, would need
more cancellation than those bounds permit.

Consequently every sufficiently long hypothetical integer cycle
(\(d=1\)) has at least
\[
\left\lfloor\frac{\sqrt A}{2}\right\rfloor
\]
multiplicatively independent centers from these very cuts. The independent
review also obtains distinct primes giving a strictly diagonally dominant
valuation matrix. The centers may have arbitrarily large individual
height; no bounded-height window hypothesis is used.

This is a conditional cycle-exclusion result: bounded rank would exclude
long integer cycles. No reviewed theorem supplies that upper bound for
these actual centers. The rank lower bound alone is compatible with a
candidate integer cycle and is not a contradiction.

The same packet gives a complementary unrestricted-word count:
the average entire canceled gcd is \(\exp(o(A))\), and the fraction with
\(d\le2^{(1-\epsilon)A}\) is at most \(2^{-\epsilon A+o(A)}\).
These averages allow exceptional integer words. The stronger periodic-set
packing already proved in PR #193 is credited separately.

Sources: [pointwise proof](cycles/NEAR_MINIMUM.md),
[counting and literature comparison](cycles/README.md),
[independent review](../../../reports/astra-global-closure-20261124/closing/cycles/CYCLE_REVIEW.md).
The external effective input is
[Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006), following
linear forms in logarithms. Two Lean files check the finite divisor and
valuation arguments; the full asymptotic rank theorem is written.

## 4. Adelic algebraization forces a natural boundary on an escaping series

For one injective positive odd orbit, write
\[
2^{a_n}q_{n+1}=3q_n+1,\qquad
A_n=\sum_{i<n}a_i,\qquad F_q(z)=\sum_{n\ge0}2^{A_n}z^n.
\]
The earlier separated-visit theorem gives \(\sum1/q_n<\infty\). Its
physical telescope makes \(F_q(1/3)\) positive and finite over the reals
and equal to \(-3q_0\) in \(\mathbb Q_2\). Thus \(F_q\) cannot be rational.

Let \(s=\liminf A_n/n\) and \(t=\limsup A_n/n\). Its exact radii are
\[
R_\infty=2^{-t},\qquad R_2=2^s,\qquad R_\ell=1\ (\ell\text{ odd}),
\qquad \prod_vR_v=2^{s-t}\le1.
\]
Apply Bost–Chambert-Loir's Theorem 7.9 to the integral formal graph on
\(\mathbb P^1\), using an archimedean continuation domain and the
nonarchimedean disks. Strictly positive capacitary Arakelov degree would
force rationality and contradict the two-place evaluation. Therefore
every permitted simply connected continuation domain \(D\) has
\[
\rho(D,0)\le2^{-s}.
\]
If \(s=t\), any continuation across any point of the convergence circle
would enlarge its conformal radius. Hence the **whole circle is a natural
boundary**, even for meromorphic continuation. The hypothesis is
equivalent to existence of the exponential growth rate of \(q_n\), and
includes subexponential escape.

This is an actual application of the primary algebraization theorem,
with its graph, tube and strict-degree hypotheses checked. It does not
establish that a genuine orbit cannot have the resulting boundary.
Removing the known dyadic zero or rescaling rationally does not improve
the degree. A four-carry comparison construction has positive integral
states, reciprocal summability, critical radii and smooth boundary values,
while still having a natural boundary. It pinpoints the exact \(+1\)
carry as the extra arithmetic information a closing argument must use.

Sources: [full adelic proof](adelic/README.md),
[independent review](../../../reports/astra-global-closure-20261124/closing/adelic/INDEPENDENT_REVIEW.md),
[Bost–Chambert-Loir, Theorem 7.9](https://arxiv.org/pdf/math/0702593).
The nine finite Lean declarations verify the telescopes and comparison
arithmetic, not the external algebraization theorem.

## 5. Literature interfaces and the next universal obligation

The literature was tested on the objects carried by the source, with
quantifiers kept intact.

| Machinery | What it supplies here | First missing input for closure |
|---|---|---|
| Effective linear forms in \(\log2,\log3\) | Polynomial minimum bound and near-exponential cut-center denominators | An upper restriction on the rank or arithmetic complexity of these same centers |
| Bost–Chambert-Loir algebraization | Conformal-radius bound and a full natural boundary when the mean exists | A consequence of the exact unit carry incompatible with that boundary; oscillating means also remain |
| Fixed-rank S-unit and moving-target gcd methods | Qualified count or height statements under their stated dimension, rank and coefficient conditions | A faithful encoding of an arbitrary individual integer cycle satisfying those conditions |
| Brofferio's rational-affine Poisson-boundary theorem | The exact real/ternary boundary of the independent gap model | Independence or a proved comparison with the actual ordinary source marginal |

The [boundary interface note](BOUNDARY_INTERFACE.md) computes all local
drifts and gives a quantitative limit on a root-by-root iid comparison.
It explicitly does not infer anything about unlabelled limiting gap laws
from that labelled comparison. Its
[independent review](../../../reports/astra-global-closure-20261124/closing/BOUNDARY_REVIEW.md)
checks the primary theorem's moment and independence assumptions.

The remaining constructive target is a successful smaller ordinary
partner for **every** eligible prescribed source, with a genuine later
merger allowed. The cycle target is a pointwise arithmetic contradiction
for the candidates of growing center rank. The escape target is an
opposing estimate on the actual orbit's series or time-limit law.
These are three unresolved universal statements. None is replaced by a
density result, an extensible collection of finite witnesses, or an
application to an independent reference process.

Source hashes, execution scope, overlap findings and repository validation
are kept in the
[continuation review](../../../reports/astra-global-closure-20261124/closing/ROOT_REVIEW.md).
