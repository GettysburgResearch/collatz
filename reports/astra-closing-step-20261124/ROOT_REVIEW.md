# Coordinator review of the direct closing round

**VERIFIED within the stated boundaries; universal implication OPEN.**

The reviewed science is the descent note, CanonicalSource.lean and
check.py. Exact hashes are recorded in the independent reviews and fresh
replay. This continuation was prompted by the user's request to attack
the ordinary closing implication directly, rather than treat further
counts or approximations as its proof.

I reconstructed the normalization. If (4u+1)/9=3^h w, then the all-odd
identity sends B=8*2^h*w-1 to 27*3^h*w-1=12u+2 in h+3 steps.
Two further actual steps reach 9u+2. Thus B has the child's basin label.

For a raw bad-to-good extra edge with r=2^a*3^q*w, the canonical
source is B+1=(2/3)^q*(8r). It cannot exceed the raw source. Applying
the complete finite descent path to the least bad N gives a first
bad-to-good edge because all ordinary edges preserve membership in C.
Its raw source is bounded by JN in the pinned table, with
J=20970919/122875. This proves N<=B<=JN. In particular the useful
closing condition is z<B/J in the same ordinary component; replacing
the component requirement by a numerical comparison would be invalid.

I read the exact PR193 table replay and its accompanying reduction at
67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e. The replay checks all 291
progressions, their complete period and 3,483 letters, including domains
at every affine intermediate form. Its maximum extra-edge source ratio
is J, attained at the specified 122875 row. The independent reviewers
also replay this dependency. The new CanonicalSource module does not
reformalize the whole table or the least-counterexample extraction.

For the dyadic translate argument, the ordinary common-prefix endpoint
has the exact additive term 9*3^q_a*v. The certified fixed reference
makes q_a=a/2+O_d(1). The nondegenerate three-term Evertse application
uses gcd bounded by 4d+1, so its constant may depend on d. Its resulting
valuation bound is sufficient for the stated fixed-reference asymptotic,
not for changing references without a new uniform estimate.

The power-of-two family has a strict explicit comparison at j=10 and a
monotone ratio proving it for all larger j; ten smaller physical traces
cover the initial cases. The one-odd family instead grows throughout
the parent stopping clock. Its adjacent-Mersenne reselection uses
ordinary paths and least failure in the exponent, and the parity
exclusion of even d is exact. The replacement canonical size can be
larger than JN. No induction measure for repeating that reselection
was proved, so it is not a total certificate-producing procedure.

The [arithmetic review](arithmetic/REVIEW_DESCENT.md) and
[renewal review](renewal/REVIEW_DESCENT.md) independently reconstruct
the final descent files and replay the pinned finite-table dependency.
The original three-stream packet remains
byte-for-byte unchanged; its fourteen named Lean declarations were
freshly checked at science commit 174f5ce593473f49962ab253548693183314391e.
The present packet adds four named finite identities with a separate
clean-commit replay. Neither replay establishes the remaining universal
component contraction.
