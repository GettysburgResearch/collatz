# Independent review of ordinary essential spectrum and smoothing boundaries

**Verdict: VERIFIED at the narrow claim level described below.** I reconstructed
the arguments rather than relying on the author's replay. The main new
essential-spectrum theorem does not assume Collatz, a hypothetical escaping
orbit, a harmonic trace, or a packing theorem. The later coboundary and
regularity claims retain their explicitly stated local-packing dependency.
This review does not verify a proof of Collatz or upgrade any neighboring
unreviewed theorem.

## 1. Exact review boundary

The reviewed staging files are in
`/workspace/scratch/46eba7b29f50/agent-pressure-next/`.

| File | Bytes | SHA256 |
| --- | ---: | --- |
| `ORDINARY_ESSENTIAL_SPECTRUM.md` | 17469 | `436fb7a9e6230271e1b2564e64554ca2b1bbda12f1cc5ee8eccff0562f68432c` |
| `SMOOTHING_BOUNDARY.md` | 9809 | `8a5b38d517f56610e17ac02d44294c810894239d7272e98688eb672e7bbdeb3a` |
| `check_ordinary_spectrum.py` | 13797 | `395beaf29efeb7f66b88e346d04451e04b089cad63ee8b434c6ac9806feba0d4` |
| `ordinary-spectrum-report.json` | 3563 | `a29f5c1ed8aa948af4ec1a32e762cdbce0997ae376c1ed940289dfc3a9734afc` |

I also inspected the following exact repository sources for normalization
and comparison:

- PR143, `41a408e5e617fb4e65142485f6f3ff3e6ef6c408`,
  `research/pressure-decay-20261031/PROOF.md`, PF-002.
- PR144, `df756794e1d8de5cabff148ef433df505e3b68b4`,
  `research/pressure-diagonal-20261031/PROOF.md`, D1–D6.
- PR149, `92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
  `research/asymptotic-inverse-operator/ASYMPTOTIC_OPERATOR.md`,
  in particular its normalization and Theorems A and B.
- PR150, `ef4022fa5ae43dd943ecca0b7c84d69af624c5c9`,
  `research/pointwise-closure-20261120/LOCAL_DISTORTION.md`, is the
  identified dependency of OE5/SM1. I independently reconstructed that
  local shell-packing and reciprocal-budget argument in the preceding
  review packet; its dependency is retained here.

## 2. OE1: compact comparison and singular values

The domain is all positive ordinary odd integers, including nonunits
modulo three. This agrees with PR143 and PR144. No state is killed.
The predecessor parameterization gives the four column sums
3/5, 12/5, 27/85, and 432/85 exactly. It also gives boundedness of both
operators, since 3/4<=c(n)<1 and B_s=M_{c^{-s}}A_s.

For K_s=B_s-A_s, two distinct target columns have disjoint supports.
Consequently K_s^*K_s is diagonal and its singular values are exactly the
rearranged column norms. For s=1 the squared column summands are
9/[4^a(2^a t-1)^2]. For s=2, expanding the weight difference gives the
displayed equation (4) of the reviewed note. I checked both geometric
asymptotic constants independently:

| Exponent | Target 1 modulo 3 | Target 2 modulo 3 |
| --- | --- | --- |
| s=1 | 3/sqrt(255) | 12/sqrt(255) |
| s=2 | 18/sqrt(4095) | 144/sqrt(4095) |

Each is the coefficient of 1/t. The upper bounds use the largest
possible z=1/(2^a t); in the second residue class the least positive odd
target is 5. Thus k_1(t)<1/t and k_2(t)<3/t hold on the entire stated
domain. The two nonzero target classes have density 1/6 each among
positive integers. Counting column norms above a cutoff then gives the
claimed rearranged constants 5/(2sqrt(255)) and 27/sqrt(4095).

**VERIFIED:** compactness, every Schatten class S_p for p>1, and failure
of trace class. None of the more precise Schatten conclusions is needed
for the subsequent essential-spectrum theorem.

## 3. OE2–OE3: genuine convergent supports and the whole circle

The root divisibility is elementary and correct. If
v_3(x+1)=j>=1, then v_3(x^3+1)=j+1 because
v_3(x^2-x+1)=1. This proves that m_k is an integer. The explicit states
2^{k-j}3^j m_k-1 have exactly k-1 initial odd valuations equal to one,
then their root t_k maps directly to 1. The strict ratio bound
n_k/t_k<(2/3)^{k-1} has the correct direction: for 0<a<b,
(am-1)/(bm-1)<a/b.

The complete predecessor basins C_k are disjoint, since each root goes
straight to 1 and can never reach any other root. Their first-hit depths
are unambiguous. Each sum S_{k,s} is positive and finite by the ordinary
reciprocal-power envelope, and the displayed vectors are orthonormal.

The phase sign is correct. If ell(Un)=ell(n)-1, then
z^{-ell(Un)}=z z^{-ell(n)}, so B_s f=z f on every internal edge.
No source outside C_k maps into C_k. The only residual is at the root,
where the parent is 1 outside the support. Its norm is exactly
t_k^{-s}/sqrt(S_{k,s}), bounded by (n_k/t_k)^s.

Compactness sends this orthonormal sequence to zero under K_s, giving
the asserted approximate eigenvectors for A_s at each |z|=1. The norm
of K_s f is independent of z because its column Gram matrix is diagonal.
The basin of 1 is reducing, and the Fredholm obstruction follows from
the lower bound on the complement of a finite-dimensional kernel.

**VERIFIED:** every unit complex number lies in the essential approximate
point spectrum, including after restriction to the basin of 1. This is
consistent with the trivial exact unit-circle eigenspace on that basin:
the equation at 1 forces zero, then propagates backwards. The note
correctly distinguishes approximate spectrum from exact fixed vectors
and from the specific-vector moment D_q.

## 4. OE4: exact finite certificates and effective search

The residual identity includes every off-support predecessor. In detail,
||A_s g||^2=sum_t z_s(t)|g(t)|^2 uses complete predecessor columns,
whereas the cross term has finite support. Every internal edge contributes
c(x)^s |g(x)|^2 to the real cross term because the z factors cancel.
The root contributes zero to the cross term. This gives the displayed
rational formula (15) for every unit phase simultaneously.

Finite forward-closed inverse-tree exhaustions converge in l2 to the
basin vectors. For the terminating construction, among ceil(M/2)+1
disjoint basins at least one avoids all positive odd numbers <=M.
On that basin the diagonal column bound gives ||K_s f||<=C_s/M.
The advertised choices of k_0 and M leave a strict factor-of-two margin
before finite approximation, so dovetailing the finitely many candidate
exhaustions and testing (15) must terminate.

The priority-queue exhaustion is legitimate despite infinite branching.
Once a parent is present, its children are enumerated in increasing
ordinary value, and only finitely many positive integers lie below any
specified child. The unique forward parent prevents conflicting inserts.
Every enumerated vertex has its literal finite route to the selected root
and then to 1. No unknown convergence decision is used.

**VERIFIED:** arbitrary-accuracy finite supported certificates, with no
claim of a useful uniform complexity bound.

## 5. OE5 and SM1: retained local-packing dependence

On a nonperiodic component the odd path expands to a distinct shortcut
path, so the cited reciprocal sum below 600 yields r>=exp(-200).
Eventually periodic paths have r=0. The edge identity r(n)=c(n)r(Un)
gives the stated bounded diagonal similarity
A_s=M_{r^s}B_sM_{r^{-s}} on the nonperiodic reducing subspace.

The moment identity is also exact: J_q/t_q=r_q/n, hence
J_q^4/t_q^2=r_q^4 t_q^2/n^4. This proves both constants in the comparison
with the source-weighted height moment. It does not bound that moment.

For SM1, if one nonperiodic source exists, its distinct forward values
make the nonperiodic set unbounded. The explicit immediate convergers
make its complement unbounded. Two unbounded complementary subsets of
the ordered odd integers have infinitely many adjacent membership
changes. At each such change the limiting product jumps by at least
exp(-200). The equivalence with adjacent smoothing follows.

**VERIFIED relative to the identified local-packing input.** The adjacent
smoothing hypothesis remains open, and this equivalence would establish
eventual periodicity, leaving nontrivial positive-cycle exclusion separate.

## 6. SM2–SM5: exact failed shortcuts

For the adjacent pair N_k=(4^k-1)/3 and M_k=N_k+2, I checked the
valuations 1,1,4 and the subsequent valuation-two segment directly.
The formula U^q(M_k)=3^{q-1}4^{k-q}+1 is correct for 3<=q<=k-1.
Fixed q and k tending to infinity are kept in the correct order.
The finite products have the stated different limits, so K^2 1 fails
the proposed adjacent-regularity class.

Dominated summation proves the arbitrary positive clock-average formula.
Its exact scope is: a law assigning positive mass to some q>=2 has a
nonzero adjacent jump; a family escaping every finite clock set has jump
tending to one. A law supported on {0,1} has no such jump. The displayed
equations are correct. The final reviewed version explicitly includes
this exception in its corrected SM3 heading and paragraph. I reread the
complete final note after that scope clarification; the original reviewed
SM file had SHA256
`1101fdcf90645f8b783d364ee994fed9d64c4234db1884960b32f2da07f08e88`.
The main operator note, checker, and report stayed at the hashes above.
The Cesaro and Abel formulas have the correct constants and endpoints.

For SM4, the word affine formula and the least positive odd representative
are essential. The final congruence implies each reversed intermediate
step is integral. At a positive odd target, any integral inverse step
(2^a t-1)/3 is itself positive odd, since its numerator is positive.
Thus no extra positive lift is needed. The endpoint progression has
spacing 2*3^q and its source progression spacing 2^{A+1}; regrouping
positive terms gives the exact moment trace.

The independent word law P(a=g)=3/4^g has total mass one and gives
word weight J_w^2/3^q. It is correctly labeled an inverse-word
normalization, not an actual forward valuation distribution.

For SM5, E 2^a=3, so M_j is a nonnegative mean-one martingale.
The half-moment ratio is sqrt(6)/(4-sqrt(2))<1. Tonelli therefore gives
sum_j sqrt(M_j)<infinity almost surely, hence sum_j M_j<infinity almost
surely. Monotone convergence simultaneously gives infinite expectation
of the limiting offset, because its finite-depth expectation is q/3.
These facts are compatible and do prove the claimed failure of uniform
integrability. They do not establish the coupled ternary/real estimate.

**VERIFIED:** these stated calculations and obstructions, with the
clock-law exception just described. The two missing closing estimates
are retained explicitly.

## 7. Code audit and actual replay

I inspected the checker and ran it independently with Python. The replay
passed all four quoted full-column residual thresholds on the two
512-state supports, the 54 explicit root/spine edges, 204 finite
smoothing-pair controls, six column identities, and eight rejected
corruptions/domain errors. The two-state support {3,5} gives the exact
squared A_1 residual 53/170, providing a check that external predecessor
contributions are included.

The producer's inverse edges are independently re-evaluated by the
verifier using literal 3n+1 and repeated division by two. Depth labels
strictly decrease along all nonroot forward edges. The rational residual
enclosures use downward integer quotients with explicit upward error
budgets. There are count terms in the norm and column sums, and count-1
cross terms. The upper and lower quotient directions are correct after
normalization. No floating point controls acceptance, and the active
checks do not rely on Python assert statements.

These are finite arithmetic checks and a mathematical review of the
written proofs. They do not certify an infinite numerical experiment,
the open all-clock moment estimate, global adjacent regularity, or
exclusion of any positive orbit or cycle.

## 8. Attribution and limits

The source comparison is accurate: PR143 already classifies exact fixed
vectors and conditional unit-circle eigenvectors on escaping components;
PR149 uses a different inverse Markov operator on a harmonic weighted
space and proves finite-power essential norm one. The new theorem's
unweighted ordinary derivative operators, disjoint certified-convergent
supports, and explicit finite residual interface are genuinely different
statements. No exhaustive literature priority conclusion was audited.

The useful result is an unconditional obstruction to a particular
spectral/Fredholm closure, with explicit arithmetic witnesses. It is not
evidence for an escaping orbit and does not prove the Collatz conjecture.
