# Whole-repository synthesis after checkpoint 9

Date: 2026-11-22. Status: active research; **full convergence is OPEN**.

**Latest incorporated head:** PR183 advanced during this pass to
`68345f60a4f757acb42a69a4ac95910f8ce26163`. The
[late-head integration](LATEST_HEAD_INTEGRATION.md) credits the concurrent
overlap and develops three further combinations: the sharper full-word
cutoff, a joint source-grade/target induction, and an `L²` extension of
the ordinary contact-source residue. The conservative estimates below
remain valid; their stronger current versions are linked there.

The refreshed repository offers three substantially different ways to close
the problem: control the original source mass analytically, find a universal
paid merger arithmetically, or constrain the complete descriptions of cycles.
These routes now share more exact interfaces, but none supplies the missing
universal assertion. The new checkpoint advances each interface and records
two precise reasons that a tempting shorter completion does not follow.

Use the shortcut map \(T(n)=n/2\) for even \(n\),
\(T(n)=(3n+1)/2\) for odd \(n\). The odd map is
\(U(q)=(3q+1)/2^{v_2(3q+1)}\). A unit means a positive odd integer not
divisible by three. Every source and endpoint below is an ordinary integer.

## 1. What the repository-wide refresh changed

The metadata query covered all 145 pull requests returned by GitHub: 122 open
and 23 closed. Detailed reading focused on new global results in PR175,
PR178, PR180, PR182, PR183, and PR185, together with the supplied-source
induction of PR177 and the forced band/coupling work of PR173/184. Existing
main-branch maps, the results catalog, and scoped errata remain the guide to
older packets. This is a broad source synthesis, not a claim that all 145
PRs or every historical theorem were independently verified.

The genuinely useful changes in the newest sources are:

- PR175 gives global superlevel and moment bounds for the canonical inverse
  potential. A large value is constrained globally, but a sparse forward
  escape is not excluded by those bounds.
- PR178 isolates a critical *first moment of actual orbit minima*. Under
  its uniform predecessor-density input, one escaping component forces that
  moment to diverge. Its required upper bound has not been proved.
- PR182 shows that an exact ordinary invariant Boolean label is rigid against
  every fixed real Fourier frequency. A suitable ordinary Besicovitch
  approximation would finish the label route; no such approximation follows
  merely from residue balance or low word complexity.
- PR183's four newer modules are now compiled, with 69 theorem audits reported
  at the pinned head. Its mixed-base normalizer still ends at an explicit
  blocked erasure state unless the open physical cover is supplied.
- PR185 supplies a positive harmonic function for the *ordinary inverse
  counting operator*, with exact original-source collision energy and an
  effective classifier for fixed linear one-parameter block schemas.

The source ledger gives exact commits and paths for these statements. The
new literature guide is useful for hypotheses, but its earlier description
of PR183's replay status has been overtaken by that PR's current head. Its
suggested improved band clock has also already been addressed in our
checkpoint 6. Neither is counted as new unfinished work here.

## 2. An effective classification with independent exponents

Fix binary blocks \(V_1,\ldots,V_r\). The earlier PR185 classifier treats
exponents depending linearly on one common parameter. The present argument
allows each exponent \(e_i\ge0\) to vary independently in

\[
V_1^{e_1}\cdots V_r^{e_r}.
\]

For a block with affine map \((3^s x+C)/2^L\), its defect is
\(\Delta(x)=(2^L-3^s)x-C\). Every actual run of \(e\) repetitions
has the exact reserve \(2^{Le}\mid\Delta(x)\). A nonzero defect pays
for the full repeated clock; a zero defect identifies a replayable template
cycle. Concatenating the nonfixed pieces gives the formally checked inequality

\[
2^A\le[K(x+1)]^{2^r-1}.
\tag{1}
\]

For a closed path, rotate its actual exponent tuple so every suffix multiplier
is at most one. At that boundary,

\[
x\le\frac{B}{1-3^S/2^A},
\quad B=2\sum_i\left|\frac{C_i}{2^{L_i}-3^{s_i}}\right|.
\tag{2}
\]

Matveev's published two-logarithm bound makes (2) polynomial in \(A\).
The exponential left side of (1) then gives a complete finite cutoff:
if \(K(1+B/c)\le2^b\), the total clock outside template cycles satisfies

\[
A<\max\bigl(16,4b(2^r-1),16\kappa^2(2^r-1)^2\bigr).
\tag{3}
\]

Here \(c,\kappa\) are explicit valid constants for
\(1-3^S/2^A\ge cA^{-\kappa}\). All remaining tuples are finite;
template-cycle tuples are recognized by finite transition maps, taking all
initial phases and rejecting the empty tuple. This is an actual effective
classification of every cycle in a supplied bounded block language.

The external logarithm theorem, rotation, and cutoff are written arguments.
The repeated-word reserve and (1) are Lean theorems. A second mathematical
read checked the classifier and supplied the phase/empty-input clarification.

This should not be advertised as a new general periodic-complexity theorem.
Classical effective cycle work already uses logarithm separation. A recent
source-qualified rStation manuscript gives stronger dictionary-complexity
lower bounds, and its elementary section already contains periodic
divisibility and height propagation. The contribution here is the explicit
independent-exponent classifier and its universal formal arithmetic kernel.

### What would turn it into a global cycle argument?

An upper bound on the description complexity of every possible primitive
cycle is still missing. With block lengths bounded, a decomposition into
\(r\le(1/2-\varepsilon)\log_2 A\) pieces for one fixed
\(\varepsilon>0\) would contradict (3) for all sufficiently long cycles.
No such decomposition theorem is available. Describing each step separately
has \(r=A\) and gives no contradiction.

The mandatory band does not supply this compression on its own. Every
odd-starting parity word of length \(A\) appears at a marked integer in
either desired ternary unit class once

\[
3\cdot2^A(d+1)\le70\cdot2^d,\qquad d\ge70.
\tag{4}
\]

This follows from the finite parity-cylinder bijection and CRT in an interval
of length \(3\cdot2^A\) above \(2^d\). Thus arbitrary finite prefixes
occur inside the band through clocks nearly equal to its binary height.
The next useful arithmetic restriction must couple successive returns of
the same source or use closed-path integrality, rather than only the leading
binary digits at one marked entrance.

## 3. A total transition language with exact successful-handoff conditions

The new dispatcher removes the finite-state restriction from the carry
language. Suppose the supplied source has edge
\(3r+1=2^a u\), while the target is exactly \(n=3^{p+1}r+d\).
Evolving the signed offset \(d-3^p\) for \(a\) shortcut steps gives
endpoint \(z\) and odd count \(k\). The actual target then satisfies

\[
T^a(n)=3^{p+k}u+z.
\tag{5}
\]

Each subsequent source edge supplies a fresh binary horizon for the existing
signed lifting theorem. Iterating (5) retains the literal unused source
certificate, the target clock, ternary degree, and signed offset. Negative
offsets stay negative. Every low target is admitted by
\(t=27q+(t-27q)\), because \(t\le16q+1\) makes the offset negative.

After a nonempty prefix \(W\), the maximal paid exponent remains
\(f=\max(e,\max_{a\in W}(a-1))\). The same complete-source rank
strictly decreases. The exact terminal target \(v=3^p u+d\) is captured
when \(v\le2^{f+1}u+1\), or when an actual partner satisfies

\[
0<x\le2^{f+1}u+1,\qquad T^L(x)=T^R(v).
\tag{6}
\]

All these compositions are proved in Lean. The target continuation \(R\)
and partner clock \(L\) are independent. No new source certificate is
silently substituted for the retained suffix.

The total program ends either at degree zero, giving capture, or at the source
endpoint one with an explicit residual \(3^p+d\). A complete argument
still needs successful handoffs for every such constrained residual state.

There is a useful exact failure of the shorter proposal. For
\(e=1,q=17,W=[2,3,4],t=63\), the three source-cut target values are
\(143,485,91\), whereas the maximal paid ceilings are \(53,41,17\).
None captures. An existing PR185 rule repairs the example asynchronously:
\(T^8(63)=T^7(31)=182\). Its all-parameter affine family is credited in
the dispatcher note and replayed exactly. Consequently the next target is
successful merger coverage; merely proving that every carry state has a
transition cannot finish this induction.

## 4. Finite ordinary contact mass and its exact limitation

The analytic attack now combines two previously separate objects: checkpoint
8's first-contact representation of the minimal inverse envelope \(V\),
and PR185's harmonic function \(\nu\) for the ordinary inverse counting
operator. The latter removes derivative weights from terminal source mass.

On each hypothetical escaping component, forward values of \(V\) tend
to infinity. Hence a forward path has only finitely many contacts with
\(C=\{V\le2\}\). Once a spine has passed its last contact, all of
its inverse first-contact sources are ordinary *last-contact vertices* of
that component. Their sets increase along the spine. Their \(\nu\)
mass is exactly the value of \(\nu\) at the moving spine root.

This yields a canonical finite atomic measure \(\eta\) on the last-contact
sources. If \(\mathcal P\) denotes the states whose positive-time future
has no further contact, it has the exact ordinary Green representation

\[
\sum_{j\ge0}L^j\eta=\nu\mathbf1_{\mathcal P},
\qquad \nu\mathbf1_{\mathcal P}-L(\nu\mathbf1_{\mathcal P})=\eta.
\]

Its total mass in a component is the positive limiting harmonic capacity
of that component; summing across components remains finite by the
ordinary antichain budget. The ordinary \(K_\nu\) first-contact laws converge in total
variation to this atomic source measure. The full written proof, hypotheses,
normalizations, and domain are in the companion note.

This is useful source-preserving structure, but qualitative finiteness does
not give the needed rate. If a contact source reaches a large root \(q\)
in fewer than \(L\) odd steps, ordinary growth forces

\[
x+1\ge(q+1)(3/2)^{-L}.
\tag{7}
\]

At the critical clock
\(L(q)=\lfloor(\log q-3\log\log(q+2))/\log(3/2)\rfloor\),
every such source lies in a tail above scale \((\log q)^3\).
Short-capture probability therefore tends to zero along a hypothetical
escape, by finiteness of this one original-source measure. This qualitative
boundary limit alone does not supply a lower bound of order \(1/\log q\).
The complete argument also transfers checkpoint 8's stronger finite-front
upper estimate into this same ordinary law:

\[
\nu(q)p_{L(q)}^\nu(q)
\le\frac{16}{\delta\log(3/2)\log(q+2)^2}.
\]

Since \(\nu\) is bounded below on any escaping spine, the joint inputs
already give \(p_{L(q)}^\nu(q)=O(\log^{-2}q)\) there. A proved lower
bound of order \(1/\log q\) on the relevant cofinal marked roots would
contradict escape. No such lower estimate is supplied.

The important next estimate must control that original-source tail or the
actual moving-root contact law quantitatively. Replacing it by a finite
probability on a compact completion, or dropping a source-height factor
when converting to a vertex measure, does not prove the estimate.

## 5. Where to concentrate the next full-theorem attempt

The strongest immediate arithmetic target is a universal version of (6),
allowing genuine independent clocks and source rewrites. We now have a total
all-state language, the exact maximum source budget, and a common rank; the
missing claim can no longer be hidden in a partial transition table.

The new joint induction further admits any genuinely smaller partner at
the same source grade, even beyond the lower-grade prefix envelope. Its
`MixedCover` is the current unified coverage target. Ordinary descent must
still be below the original queried target; descent below a later larger
intermediate state alone is insufficient.

The strongest analytic targets are quantitative contact capture on the
forced band, or an upper bound for PR178's critical first moment of actual
orbit minima. Both address an original source and its full future. The
first-moment route primarily excludes escape and still needs cycle
identification. A sufficient effective contact bound, combined with the
existing finite-basins criterion and its checked base, is a route to full
convergence. No such bound has been proved here.

Cycle-description compression is a separate ambitious route. The new
independent-exponent classifier settles every supplied bounded-language
case, and makes the missing all-cycle upper bound precise. It does not
constrain an arbitrary escaping trajectory or prove that all possible
cycle words belong to such a bounded language.

The invariant-label/Fourier route is mathematically sharp but still needs
an ordinary approximation theorem. Residue equidistribution, zero entropy,
or stationary marginals do not establish that theorem in the current
sources. It should be pursued only with a concrete new approximation or
ordinary-source rigidity input, rather than another compactness extraction.

The result of this pass is a larger checked arithmetic mechanism and a
canonical ordinary-source analytic limit, with the universal obligations
preserved. None of the new statements claims the full theorem.
