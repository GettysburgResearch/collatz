# Forward-five closure and positive occupation criteria

**Status: PROPOSED, with independent agent reconstruction at the frozen
claims below. This packet does not prove Collatz.** Its principal completed
result is an exact conditional reduction to forward multiplication by five
in the actual basin of 1. The required physical closure remains **OPEN**.
The reviews are mathematical reconstructions and executable cross-checks,
not external acceptance or proof-assistant verification.

All integer dynamics use the ordinary positive shortcut map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

The work starts at main commit
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. Relevant concurrent work is
pinned in [SOURCES.md](SOURCES.md); no unmerged result is silently treated
as an integrated theorem. Four manuscripts contain the proofs and their
first unsupported steps. The [report index](../../reports/2026-11-20-global-closure/README.md)
contains the certificates, independent reviews, exact comparisons, and
checkout validation boundary.

## 1. A single one-way basin law would suffice

Let \(C=\{n>0:T^k(n)=1\text{ for some }k\ge0\}\). Claims GCM-001 and
GCM-002 in [merger.md](merger.md) prove the equivalence

\[
\boxed{\text{Collatz}\quad\Longleftrightarrow\quad
\bigl[x\in C,\ x\text{ odd},\ 3\nmid x\Longrightarrow5x\in C\bigr].}
\]

Equivalently it suffices to prove

\[
t\in C,\qquad v_2(t)=2,\qquad3\nmid t
\quad\Longrightarrow\quad5t+1\in C.
\]

The latter needs only the first valuation layer of PR154's restricted
five-ray domain, and only a forward implication for the one known basin.
No invariance under tripling is assumed. This is a strengthening relative
to the specified repository sources; priority over the literature is not
claimed.

The proof is strong induction on positive integers prime to three. Its
complete certificate gives, for every such \(n>1\), a positive \(q\)
prime to three with

\[
q\le19n/20<n,\qquad q\in C\Longrightarrow n\in C,
\]

**conditional on the five law**. Even inputs use halving; odd multiples
of five use that conditional law. The remaining inputs are covered by
464 infinite residue cells, using 55 explicit words and a complete cover
at modulus 1,866,240. Every cell's affine legality and descent hold for
all of its lifts, not merely the sampled starts.

The independent reconstruction proves coverage by pairwise CRT
incompatibility and the exact density sum, separately from the author's
common-modulus bitmap. Each cell uses at most one conditional division by
five, and at most 19 listed affine instruction groups, including their
specified divisions. These are costs in the conditional
proof graph. Intermediate inputs may exceed the original input; the
membership implications are read backward from the smaller endpoint.
These costs are **not ordinary stopping-time or physical-merger bounds**.

The statement still needed is precisely the displayed forward-five law.
It has not been proved by the certificate or by testing its antecedents.

## 2. A positive occupation estimate would handle escape and cycles

[transport.md](transport.md) uses PR152's exact unsafe-return map \(B\),
its killed pushforward \(H\), and its source-qualified rank \(R\). Let
\(\mathcal V\) be that unsafe domain and set

\[
\psi(u)=1+\log\log(R(u)+6),\qquad
f_0(u)=\frac{\mathbf1_{\mathcal V}(u)}{u(u+1)},\qquad
\mathcal G_N(f)=\sum_{j<N}\sum_{y\in\mathcal V}
\frac{(H^jf)(y)}{\psi(y)}.
\]

GCT-001 proves, from the actual additive return budget,

\[
\liminf_{N\to\infty}\frac{\mathcal G_N(f)}{\log N}
\ge\frac{m_\infty(f)}{\log6},
\]

where \(m_\infty(f)\) is the original source mass never absorbed at 1.
This includes mass entering a nontrivial cycle. Thus the single estimate

\[
\boxed{\mathcal G_N(f_0)=o(\log N)}
\]

would prove full Collatz. **This upper bound is OPEN.** It is a sufficient
quantitative condition, not an equivalence established here. GCT-003
constructs a different, entirely terminating system showing that the
available abstract interfaces and pointwise termination do not themselves
imply this rate.

Two useful estimates are proved rather than postulated:

- GCT-002 bounds every omitted *original* source, including all its later
  mergers, by \(N/((M+1)\psi_*)\), where
  \(\psi_*=1+\log\log7\). Taking source cutoff \(M=N\) reduces the
  closing target to a finite triangular array with an \(O(1)\) tail.
- GCT-004 transfers PR153's translated-interval theorem to an all-return
  Green bound for smaller height charges, with periodic states explicitly
  removed. In particular,
  \[
  \sum_{j\ge0}\sum_{\substack{y\ge H_0\\y\text{ not periodic for }B}}
  \frac{(H^jf)(y)}{y}
  \le300H_0^{-1/30}\|f\|_1.
  \]
  It yields a bounded exact Poisson corrector for this smaller observable.
  It does not supply the missing reciprocal-\(\psi\) bound or an algorithm
  deciding the periodic set.

The finite calculation encloses the whole-source quantity, not just its
finite-source contribution:

\[
0.140870202043\le\mathcal G_{64}(f_0)\le0.145559765977.
\]

It uses exact outward rational logarithm enclosures, sources through
8192, and the analytic tail for every larger original source. A single
finite horizon establishes no asymptotic rate.

## 3. Actual long blocks defeat the proposed local resource shortcut

[arithmetic.md](arithmetic.md) proves that arbitrarily long **actual**
Collatz odd-map segments can satisfy the proposed binary-complexity,
prime-dispersion, and translated-interval constraints simultaneously.
For each \(N\), it constructs a positive source with \(N\) consecutive
valuation-one odd edges, hence strict growth at every displayed edge.

One regime has initial bitlength exactly \(17(N+1)\). A second regime
makes all displayed states pairwise coprime and excludes every prime at
most \(2N+1\). In both regimes every displayed state's binary one-run
count exceeds one tenth of its bitlength. The bounds on a common set of
\(s\) primes permit selecting that set after seeing the entire block.
The proofs retain the exact additive term in every ordinary edge.

The quantifiers are \(\forall N\,\exists n_0\); no one infinite escaping
source is constructed. These blocks show that the stated constraints
alone do not give a uniform finite bound on such growth segments.

For odd \(n\), the countdown \(b(n)=v_2(n+1)-1\) has the exact accounting
identity GA-001. GA-005 supplies a fixed-valuation-three edge that
recharges this countdown by an arbitrarily large amount while binary
one-run count stays constant, popcount decreases by one, and logarithmic
height changes by a bounded amount. Consequently no fixed potential

\[
\lambda b(n)+\mu r(n)+\nu s_2(n)+\kappa\log_2n,
\qquad\lambda>0,
\]

decreases on every odd edge. This excludes the specified additive family;
nonlinear and multistep approaches remain possible. The global missing
step is an accumulated recharge bound for one fixed ordinary source.

## 4. The direct attempts to close the five law

[closing-attempts.md](closing-attempts.md) records the attempted final
inferences and their exact failure points.

For \(x_a=(4^a-1)/3\), one odd step reaches 1. Nevertheless, for \(a\ge2\),

\[
T^{2a+2}(5x_a)=\frac{5\cdot9^{a-1}-1}{4}.
\]

This exceeds \(5x_a\) for every \(a\ge4\), and the ratio is unbounded.
Thus the simplest synchronized descent fails even for these antecedents.
The ordinary inverse-lift calculation also introduces unbounded affine
multiplier indices. A specified uniform two-arm certificate is excluded
by exact stopping grades. None of these results disproves the five law
or excludes every adaptive argument.

GCL-003 reconstructs a constant-error stopping-burden equivalence already
present in **PR150, STOPPING_BURDEN.md, SB5**. It is credited as an
independent reconstruction, not as new progress. The multiplicative
semigroup theorem of Applegate and Lagarias likewise does not convert
products of unrelated orbit ratios into a pointwise basin closure.

## What is completed, and what remains

| Route | Completed deduction | First unsupported step |
|---|---|---|
| Directed basin closure | Complete all-lift conditional induction from one forward-five law | Prove that physical law for every odd antecedent in the actual basin |
| Positive occupation | Cycle-inclusive lower bound; complete source tails; smaller-charge Green theorem | Prove the actual reciprocal-\(\psi\) upper bound \(o(\log N)\) |
| Arithmetic resource accounting | Exact countdown identity, arbitrary finite legal blocks, recharge obstruction | Bound accumulated recharge along one fixed source |
| Uniform inverse pressure | Reconstruction of the already-published constant-error equivalence | Establish the required uniform stopping burden |

Every route retains its global obligation. Passing the executable bundle
supports the specified finite and symbolic checks; it does not establish
any missing obligation.
