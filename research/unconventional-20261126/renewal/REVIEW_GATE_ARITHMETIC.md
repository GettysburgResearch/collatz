# Independent audit of numerical gate arithmetic

**Verdict — VERIFIED at the stated pin.**
[OP-G3, OP-G4 and the one-height identity](../operator/GATE_ARITHMETIC.md),
SHA-256 0c2c0e70ec194484a806158ce7ae046ed26ba32b7bd99c39c66e01620e19198d.
I checked the exact definitions of the source mass, first-hit gate,
moving component atoms and retention in [OP-G1–G2](../operator/EXIT_GATES.md).
A separate [quantitative proximity consequence](GATE_PROXIMITY.md)
uses the numerical strict odd maximum and the two-logarithm estimate.

* Every positive gate belongs to the stated numerical shell: only
  an odd step can first exit, and conversely an eligible shell
  integer $y=2\bmod3$ has the positive odd direct predecessor
  $(2y-1)/3<X$. Thus there are order $X$ genuinely charged sites;
  an $o(X)$ candidate list misses proportion tending to one among
  those sites. Each odd bit in a native suffix multiplies by
  $3/2$ and adds $1/2$, and each even bit halves. The positive
  normalized carry is at most $(3/2)^j-1$ by iterating the
  pointwise dominant native odd rule. The suffix start below
  cutoff is less than its exit $y\ge X$, so its slope is at least
  $1-X^{-(2-\log_2 3)}$ once $j\le\lfloor\log_2 X\rfloor$.
  All suffixes must be taken in the reversed reading of the same
  native word. Its full terminal congruence uses the integer
  carry in the forward reading. An exit sooner than that full
  clock has $x+1\gg X^{2-\log_2 3}$ by the shifted height bound,
  and each source contributes at most $x^{-s}$. Summing these
  source weights is permitted because each has at most one
  first-hit gate at the given threshold.
* The auxiliary native walk uses the centered variables
  $Z_j=(\log_2 3)q_j-j$ under iid Bernoulli-$\log_3 2$.
  The imposed floor is minus one. In a terminal bin
  $v\le Z_k<v+1$, $v\ge-1$, the reverse sums of the last third
  lie below $v+2$, and the first third stays above $-1$.
  Both one-sided probabilities cost $O(k^{-1/2})$, the last
  with factor $v+3$. Conditional on those disjoint increments,
  the middle block final interval has length one, below its
  lattice spacing $\log_2 3$, and its largest binomial atom is
  $O(k^{-1/2})$. The sum of terminal weights $e^{-av}(v+3)$
  converges since $a>0$. This direct specialization proves
  the claimed $k^{-3/2}$ with no second terminal floor issue.
  The same word's $3^q$ is at least $2^{k-1}>X/4$ up to a
  harmless endpoint equality, so only $O(1)$ shell integers
  are charged per word even though the radii vary with $q$.
  The dyadic-shell critical Mellin claim follows from
  $\sum_j j^{-3/2}<\infty$.
* Let $p$ range over the strict odd numerical record values.
  Each strict native maximum beyond the initial transient is the
  immediate successor of an odd, since an even step decreases.
  Comparing such successors compares their preceding odds in
  exactly the same order; the intervening even divisions create
  no new maximum. Hence the native gates in OP-G4 are exactly
  $(3p+1)/2$. At its own cutoff each is the first exit of the
  ray, and OP-G2 applies along these moving cutoffs. The moving
  atoms of distinct components occupy distinct integer vertices.
  Convergence of vectors in $\ell^1$ therefore implies convergence
  at the named gate of an escaping component as claimed.
* For a suffix of $j$ odd steps ending at numerical record $p$,
  write $u$ for its first odd and $x_h$ for its odd departures.
  The exact product gives $2^S/3^j=(u/p)\prod(1+1/(3x_h))$.
  It is at most $(4/3)^j$ and hence $S\le2j$. For each *fixed*
  $j$ the odd departures tend uniformly to infinity on late
  records of the one escaping ray. Thus $2^S/3^j\le1+o(1)$.
  The possible integer $S$ now belong to a fixed finite set
  avoiding equality, forcing the eventual strict inequality.
  Finite cylinder congruences and diagonal extraction give a
  truly critical infinite backwards code at every ternary limit.
* A finite strict coefficient upcrossing from a dyadic limit
  reproduces a *numerical* upcrossing at nearby positive record
  starts because of the positive carry. Thus unbounded odd
  gaps yield a dyadic phase without a finite coefficient
  upcrossing. With bounded odd gaps, the just-proved $S\le2j$
  gives the uniform native clock bound needed at all centers.
  The forward and backward applications of finite-alphabet
  rigidity now give pure periodicity from every relevant center,
  with the bounded offset put on the appropriate side. Backwards
  purity requires the odd-numerator, odd-denominator rational
  hypothesis in PR210. The argument permits distinct rational
  local limits, as does the conditional gate criterion.
* At adjacent integer cutoffs the only gate requiring further
  transport is $n$ itself. Its old mass and its fresh source
  $n^{-s}$ share the subsequent retention. Every other charged
  old target is already at or above $n+1$. This yields the exact
  one-height difference, including $n=1$ with the given empty
  old gate measure. Summing uses augmented monotonicity and the
  OP-G2 limit, without interchanging any signed infinite sums.

The positivity of a single surviving component atom would force
a subsequence of heavy gates separated from rational diagonal
confinement in the indicated limit sense. No positive surviving
atom is established by this verification.
