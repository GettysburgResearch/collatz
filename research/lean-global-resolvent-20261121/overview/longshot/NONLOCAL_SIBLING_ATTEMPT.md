# Nonlocal sibling transport: checkpoint 14 attempt

**Outcome: no positive closing estimate was obtained.** This note records
the direct continuation of the latest nonlocal stopping-tree and modular
routing attacks. It is an unsuccessful attempt appendix, not a new theorem,
a new equivalent formulation of Collatz, or a formalization receipt.

## The actual quantity retained

Write

\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}},\qquad B(n)=64n+21.
\]

The target is the canonical harmonic function from the pinned construction,
with all of that construction's analytic qualifications retained. The desired
estimate is still

\[
G(n)\ge\eta n
\quad\Longrightarrow\quad
\sum_{j\ge1}64^{-j}\frac{G(B^jn)}{G(n)}
\ge \frac{c_\eta}{\log(2+n)}
\]

for sufficiently large retained ordinary integers. Along a hypothetical
escaping orbit the left side is summable. A proof of this estimate would
therefore exclude escape. The construction kills periodic vertices and does
not settle nontrivial positive cycles.

I used the actual finite Bellman stopping antichain, not an independent
geometric sample. For a word from root \(n\) to source \(z\), write
\(\omega=3^r2^{-A}=(n/z)\Lambda\). If an arbitrary unequal-depth legal
replacement from \(B^jn\) ends at \(z'\), the exact coefficient is

\[
64^{-j}\frac{\omega'}{\omega}
=\left(1+\frac{1-64^{-j}}{3n}\right)
\frac z{z'}\frac{\Lambda'}\Lambda.
\]

Thus an actual nonlocal repair must control the reciprocal replacement
height under the original stopping mass, with image families prefix-free
and all collisions accounted for. This formula is an input from PR175,
not a new result here.

## Attempts pursued

### 1. Branching repair and a drift estimate under the stopping law

The intended argument was to replace a long anchored prefix by many
unequal-depth legal paths, using their aggregate critical mass to offset
the height distortion of individual repairs. The latest PR175 result
changes what the relevant probabilistic law looks like: near-optimal
stopping mass at a late point of an escaping orbit concentrates on its
one long inverse prefix to any sufficiently late fixed anchor. A drift
calculation under independent geometric letters, or under an unconditioned
modular routing family, is consequently not a calculation under the law
that must be transported.

The equal-depth repair identity from the previous own checkpoint remains
\(Z_y/V^{[r]}(n)=\mathbb E_\mu 2^{-\Delta}\), where \(\mu\) is the actual
Bellman payoff law. Jensen gives a useful lower bound only after an upper
bound for \(\mathbb E_\mu\Delta\). I did not establish that bound, nor an
unequal-depth reciprocal-height substitute. Branching alone does not
justify changing \(\mu\).

### 2. Spend all of the new modular-routing multiplicity

PR180 already converts the source-qualified Paper 37 v4 count into

\[
P^bf(x)\ge\frac{2c}{3\sqrt b}\langle f\rangle_k,
\qquad b=O_\varepsilon((k+1)^{1+\varepsilon}),
\]

for every nonnegative observable of \(k\) ternary digits and every
ordinary root. That is the appropriate aggregate mass, rather than the
weight of one selected word.

I tried to use it to transport the part of the stopping payoff concentrated
on the anchored prefix. Appending an arbitrary depth-\(r\) original policy
requires precision \(r+1\) in the supplied construction. Its actual
replacement source is

\[
z'=z+\frac{y-n}{\omega}.
\]

The coefficient retains the cost \(3^{-r-1}\). The whole-observable
minorization does not preserve an exceptional spike: under the existing
qualified density/floor inputs, the finite obstacles have bounded Haar
mean, even when their specified ordinary values are at least \(\eta n\).
No lower bound for the needed fraction of high-valued classes follows.

In particular, summing over nearby siblings is not a substitute for
controlling that fraction. Their explicit ternary displacement satisfies

\[
v_3(B^jn-n)=1+v_3(j)\qquad(n\text{ a ternary unit},\ j\ge1).
\]

Indeed \(B^jn-n=(64^j-1)(3n+1)/3\) and
\(v_3(64^j-1)=2+v_3(j)\). Returning to the same class modulo
\(3^{r+1}\) first requires \(j=3^r\); its prescribed sibling weight is
then \(64^{-3^r}\). This calculation only rejects the proposed direct
return-to-the-spike certificate. It does not upper-bound actual sibling
mass or refute OPEN-S.

### 3. Real renewal, regeneration, and a pointwise sublinear trace

A second possible escape exclusion would be a direct \(G(n)=o(n)\) bound
at the specified ordinary roots. I tried decomposing the full affine law
through the selected bounded-real-offset prefix families used in PR180's
clock-sensitive density construction. The hoped-for improvement was to
show that the exceptional remainder contributes \(o(n)\) rather than
the existing linear pointwise allowance.

The already-published PR180 renewal argument is directly relevant. It
retains the exact real/ternary tail trace and the same ordinary source
word. For an actual escaping prefix \(p\to q_k\), the likelihood under
real-tail conditioning tends to

\[
\frac{pQ(p)}{C\Lambda_\infty(p)}>0.
\]

Thus the real-tail tilt does not erase the exceptional anchored prefix.
The current joint clock mixing estimate preserves the final clock, but
does not supply uniform conditional control at an arbitrarily prescribed
ordinary residue together with the required real endpoint window.

I also considered applying affine Poisson-boundary theory directly to the
paired roots. The previous PR180 work already identifies the relevant
boundary and proves singularity under the sibling action. An ambient
bounded Radon–Nikodym derivative across that action is unavailable. None
of these facts gives the required pointwise arithmetic comparison on the
moving ordinary roots. I did not prove a usable regeneration remainder
bound.

## Result and scope

No estimate of order \(1/\log n\), no sublinear canonical trace, and no
escape exclusion was proved. No actual stopping law was replaced by an
iid law. No full ordinary predecessor count was inferred from a bound on
occupation along one actual path. No new Lean declaration was added:
formalizing the elementary identities above would not close the missing
arithmetic estimate.

The unsuccessful calculations should not be counted as a new positive
advance. They are retained only to prevent a later continuation from
silently substituting an averaged routing law for the anchored stopping
mass or reimporting a boundary theorem that the previous checkpoint has
already tested.

## Additional pass: rederiving the existing contact regeneration

The proposed next step was to subtract a small amount of high-spike flow
once its ordinary height exceeded all active obstacle anchors. Minimality
does supply a precise recurrence statement, but it shows why that proposed
height cutoff is not justified. Independent cross-review identified this
as a consequence already present in the repository: checkpoint 8's
`overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md`, Section 5, proves the
stronger recurrence of every absolute contact set \(\{V\le1+t\}\),
as well as \(V/G\to1\) and \(\liminf V=\liminf G=1\) along the actual
inverse chain. Since \(G\ge\gamma\), absolute contacts with
\(t=\varepsilon\gamma\) lie in the relative contact set below.
The following short survival-subtraction proof is recorded as a
rederivation, not a new result or advance.

Work on retained positive odd units. Here \(V\) is the least excessive
majorant of the unit obstacle, \(PV\le V\), and the canonical harmonic
part satisfies \(PG=G\) and \(0<\gamma\le G\le V<\infty\). The
leastness on this domain follows directly from the finite Bellman
recursion; no extension of a modified function to periodic states is
needed. Define the actual Markov kernel

\[
K_G(q,z)=\mathbf1_{U(z)=q}\frac3{2^{v_2(3z+1)}}\frac{G(z)}{G(q)}.
\]

For \(0<\varepsilon<1\), put

\[
C_\varepsilon=\{q:V(q)-1\le\varepsilon G(q)\}.
\]

**Existing supporting consequence.** From every retained ordinary root, the
\(K_G\)-inverse chain visits \(C_\varepsilon\) infinitely often almost
surely. These visits occur at arbitrarily large ordinary heights, and at
every such visit

\[
G(q)\le V(q)\le\frac1{1-\varepsilon}.
\]

**Proof.** Let \(a(q)\) be the probability that the chain never visits
\(C_\varepsilon\), including time zero, and set \(h(q)=G(q)a(q)\).
On the complement of \(C_\varepsilon\), the Markov property gives
\(Ph=h\). On \(C_\varepsilon\), \(h=0\) and \(Ph\ge0\).
Consequently \(Ph\ge h\) everywhere. Also \(0\le h\le G\le V\),
and

\[
W=V-\varepsilon h\ge1:
\]

on the contact set nothing is subtracted, and outside it
\(\varepsilon h\le\varepsilon G<V-1\). The parent sums are finite,
so subtraction in them is legitimate and

\[
PW=PV-\varepsilon Ph\le V-\varepsilon h=W.
\]

Leastness of \(V\) now forces \(W=V\), hence \(a=0\). Applying the
Markov property after every deterministic time shows that there is a later
visit with probability one; a countable intersection gives infinitely
many visits. Every inverse path in the retained domain is simple: a
repeated vertex would be periodic. It therefore eventually leaves every
finite set of ordinary integers. The visits have arbitrarily large
heights. Finally,
\(V\le1+\varepsilon G\le1+\varepsilon V\) on
\(C_\varepsilon\), which proves the stated bound. \(\square\)

There is an exact stopping-mass interpretation. Fix an ordinary height
\(H\), and stop at the first visit to
\(C_\varepsilon\cap\{z>H\}\). The lemma makes this stopping time
finite almost surely. Its legal words form a countable prefix-free
family. If \(\omega_w\) is its critical word weight, then

\[
\sum_w\omega_w
=G(q)\,\mathbb E_q^{K_G}\frac1{G(X_\tau)},
\qquad
(1-\varepsilon)G(q)
\le\sum_w\omega_w\le\frac{G(q)}\gamma.
\]

The identity follows by multiplying each finite-word probability
\(\omega_wG(X_\tau)/G(q)\) by \(G(q)/G(X_\tau)\) and summing.
The lower floor \(\gamma\) is used for the upper bound. Finite
subfamilies approximate this finite mass arbitrarily well. Thus actual
near-contact stopping mass comparable to \(G(q)\) remains available
beyond every prescribed ordinary height.

This is a rederivation of existing canonical contact recurrence, not a new
global closing estimate. It gives no bound on the first hitting time,
on the height of the first visit, or on the comparison between stopping
laws at \(q\) and \(B(q)\). In particular, it supplies no rate uniform
in moving roots. A local subtraction cannot discard all large ordinary
vertices as inactive: the unit obstacle keeps regenerating there under
the actual inverse law. OPEN-F, OPEN-S, and escape exclusion remain open.

## Exact source pins

- PR175, `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`,
  `research/lean-global-closure-20261121/closing/UNEQUAL_DEPTH_SIBLING_ATTEMPT.md`:
  unequal-depth endpoint distortion and anchored stopping-mass
  concentration.
- PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2`,
  `research/retained-source-attacks-20261122/SIBLING_MASS.md`:
  source-qualified multiplicity consumer, finite-antichain transplant,
  bounded finite-obstacle means, and failed pointwise application.
- Same PR180 head,
  `research/lean-forward-band-20261121/JOINT_CLOCK_MIXING.md`:
  the complete-clock mixed-norm estimate and selected density construction.
- Same PR180 head,
  `research/lean-forward-band-20261121/MINIMAL_ENVELOPE_ATOM_REMOVAL.md`:
  least excessive majorant, harmonicization, positive floor, and prior
  canonical inverse-ray atom removal. These are the inputs to the
  near-contact lemma above.
- Same PR180 head,
  `research/deep-machinery-20261122/RENEWAL_TRANSPORT.md`:
  Goldie and Brofferio theorem interfaces, unchanged-source likelihood,
  and singular sibling translates. Classical theorem imports retain that
  note's source and hypothesis qualifications.
- PR176, `fdcb137214f4be8ac30dbb025d6eeb6568e22e2a`,
  `research/lean-global-resolvent-20261121/overview/returns/STOPPING_TREE_TRANSPORT_ATTEMPT.md`:
  the actual optimal-stopping payoff law and exact repair-cost identity.
- Same PR176 head,
  `research/lean-global-resolvent-20261121/overview/parallel/OBSTACLE_ENTRANCE_RENEWAL.md`,
  Section 5: the prior, stronger absolute-contact recurrence and
  normalization; Section 6 records the missing uniform estimate and
  absence of a nonzero finite-cylinder contact certificate.
