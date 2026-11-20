# Fractional moments fail; logarithmic moments survive actual unsafe transport

**Status: PROPOSED, with self-contained deductions from the explicitly identified moving-rank interfaces below.** This is an actual-operator result, not a Markov approximation. It establishes an invariant input domain after every finite number of unsafe returns. It establishes neither contraction nor Collatz.

## 1. Exact map and the source interfaces

Use the shortcut map `T(n)=n/2` for even n and `(3n+1)/2` for odd n, absorbed at 1. For a>=0 define

\[
 d_a=3^a-2^{a+1},\quad c_a=3^a-2^a,\quad z_a(n)=d_an+c_a,
 \qquad R_a(n)=z_a(n)^2/3^{v_3(z_a(n))}.
\]

Set R_a=0 when z_a=0, and R(n)=min_a R_a(n). At n>1 the active mode is a=0 for even n and a=v_2(n+1) for odd n. Let k=floor(v_2(z_a(n))/(a+1)) and let A consume exactly k physical copies of the word `1^a0`. Its exact endpoint is

\[
 z_a(A(n))=(3^a)^k z_a(n)/2^{(a+1)k}.
\]

The source `research/astra-three-routes/pass4/MOVING_GHOST_RANK.md`, claims T-A3-901/902, supplies the following interfaces: this A is total; k>=1; its physical replay is exact; the infinite rank minimum is attained among a=0,1,2,h, where h=v_3(2n+1) and h is needed only if h>=3; and

\[
 R(1)=0,\qquad n-1\le R(n)\le n^2\quad(n\ge2).
 \tag{1}
\]

These are the same map and rank as `research/astra-three-routes/pass5/RANK_MOMENTS.md`, not the unrelated section rank or an ordinary-height stochastic model. The component review boundaries remain those recorded in `research/integrated/renewal-transport/README.md`.

Put

\[
 G=\{n>1:4R(A(n))\le R(n)\},\qquad U=\{n>1\}\setminus G.
\]

Starting from u in U, apply A once, then apply A while the current state lies in G. Stop at the first U state or 1. Call the result B(u). Safe excursions are finite because each surviving safe step divides a positive integer rank by at least four. Let H push nonnegative mass along B, killing mass at 1:

\[
 (Hf)(y)=\sum_{u\in U:B(u)=y}f(u),\qquad y\in U.
\]

All projections, norms, and domains below refer to this exact deterministic return.

## 2. Every positive power moment fails, including the square root

**Theorem AT1.** For every p>0 there exists a nonnegative full-support summable f on U with

\[
 \sum_U R(u)^pf(u)<\infty,\qquad
 \sum_U R(y)^p(Hf)(y)=\infty.
 \tag{2}
\]

This remains true after any fixed ordinary floor is imposed on the displayed unsafe transitions.

**Proof.** The exact ordinary family in `RANK_MOMENTS.md`, R-A3-1003(a), is

\[
 e_j=4+16j,\quad x_j=3^{e_j},\quad y_j=(9x_j+7)/16,
 \quad B(x_j)=y_j,
 \quad R(x_j)=x_j,\quad R(y_j)=9(x_j-1)^2/256.
 \tag{3}
\]

Both endpoints lie in U; there is no intervening safe excursion. The physical word is `(10)^2` and its minimum is y_j. For x_j>=81,

\[
 R(y_j)\ge (25/729)x_j^2.
\]

Put f_s(x_j)=R(y_j)^{-p} and f_s=0 elsewhere. Then

\[
 \sum R^pf_s
 =\sum_j\left(\frac{x_j}{R(y_j)}\right)^p
 \le (729/25)^p\frac{3^{-4p}}{1-3^{-16p}}<\infty.
\]

The unweighted mass is finite as well. The y_j are distinct, and every output contributes exactly one to the p-moment, so that output moment is infinite. Add the positive background `1_U(n) R(n)^(-p-1)`. It has finite input p-moment because the same source packet proves `sum_(n>=2) 1/R(n)<=55/6`; positivity preserves the infinite output moment. Removing finitely many j makes every physical path exceed any prescribed floor. This proves (2). The case p=1/2 directly defeats the proposed replacement of the actual rank-moment domain by its square-root counterpart. No probabilistic parity model is involved. QED.

## 3. A polynomial bound for the same acceleration

The needed source-height estimate is

\[
 A(n)+5\le(n+5)^3.\tag{4}
\]

For completeness, the source argument can be reconstructed as follows. Modes a=0 and a=1 shrink ordinary size. For a>=2, put beta=c_a/d_a, so 1<beta<=5 and rho=3^a/2^(a+1)>1. The affine identity gives

\[
 A(n)+5\le\rho^k(n+5).
\]

Writing L=(a+1)k, the exact divisibility of z_a gives

\[
 L\le\log_2 z_a(n)<a\log_2 3+\log_2(n+1)
 <\frac83\log_2(n+1),
\]

because a<=log_2(n+1) and 3^3<2^5. Also rho^k<=(3/2)^L and log_2(3/2)<3/5 because 3^5<2^8. Consequently

\[
 A(n)+5\le(n+5)^{13/5}\le(n+5)^3.
\]

This argument permits arbitrarily large modes and repetition counts.

## 4. An invariant logarithmic domain

For n>1 define

\[
 \ell(n)=\log(R(n)+6),\qquad
 \|f\|_\ell=\sum_{n>1}\ell(n)|f(n)|.
\]

The logarithm is natural. Absorbed mass is omitted, so no convention for ell(1) is needed.

**Theorem AT2.** For every nonnegative f on U,

\[
 \|Hf\|_\ell\le6\|f\|_\ell.
 \tag{5}
\]

In particular, finite logarithmic rank moment is preserved by each actual unsafe return, and

\[
 \|H^jf\|_\ell\le6^j\|f\|_\ell\qquad(j\ge0).
 \tag{6}
\]

**Proof.** From (1) and (4), the purely integer bound

\[
 R(A(n))+6\le(A(n)+5)^2
 \le(n+5)^6\le(R(n)+6)^6
 \tag{7}
\]

holds. Hence ell(A(n))<=6ell(n). Every subsequent safe step only decreases R, so ell(B(n))<=ell(A(n)) whenever B(n)>1. Pushforward accounting then gives (5), with no assumption about the distribution at re-entry. Iteration gives (6). QED.

The same proof gives, for every q>0,

\[
 \|Hf\|_{\ell^q}\le6^q\|f\|_{\ell^q}.
 \tag{8}
\]

Thus positive powers of a logarithmic weight remain available even though every positive power of R fails.

### Exact gauge criterion

For any positive weight w on U, deterministic pushforward gives

\[
 \|H\|_{\ell^1(w)\to\ell^1(w)}
 =\sup_{u\in U:B(u)>1}\frac{w(Bu)}{w(u)}.
 \tag{8a}
\]

The upper bound follows by summing each source once; point masses give the reverse inequality. If w is bounded below by a positive constant and this supremum is infinite, choose distinct u_j whose ratios exceed 2^(2j), and put f(u_j)=2^(-j)/w(u_j). The input has finite weighted moment and finite mass, while its output weighted moment is infinite. A sufficiently small positive full-support background can be added without changing this conclusion.

In particular, every nondecreasing gauge omega on [7,infinity) satisfying

\[
 \omega(s^6)\le C_\omega\omega(s)\qquad(s\ge7)
\]

gives an invariant domain with `w(n)=omega(R(n)+6)`. Equation (7) proves the bound without an unknown trajectory hypothesis. This includes every positive logarithmic power and the log-log gauge below. It does not include a positive ordinary power of rank, and Theorem AT1 proves the actual failure of those powers rather than merely observing that this sufficient gauge test fails.

## 5. Safe occupation is controlled in the surviving domain

Let K_GG be the A-pushforward restricted to source and endpoint G. A source n initially in G can contribute to at most

\[
 s(n)\le1+\lfloor\log_4R(n)\rfloor
\]

successive G occupations. Therefore every nonnegative g supported on G with finite ell-moment satisfies

\[
 \sum_{j\ge0}\|K_{GG}^jg\|_1
 \le\|g\|_1+\frac{\|g\|_\ell}{\log4}<\infty.
 \tag{9}
\]

This sums the actual occupation of each original source before summing sources; it does not resample the input at any return. The omitted occupation tail after J steps is bounded by

\[
 \sum_{j\ge J}\|K_{GG}^jg\|_1
 \le\sum_{R(n)\ge4^J}
 \left(1+\frac{\ell(n)}{\log4}\right)g(n),
 \tag{10}
\]

which tends to zero by the finite ell-moment. This source-tail dependence is retained explicitly. A numerical decay rate does not follow from the moment's finiteness alone.

For a quantitative alternative, q>1 and finite ell^q-moment give

\[
 \sum_{j\ge J}\|K_{GG}^jg\|_1
 \le C_0^qJ^{1-q}\|g\|_{\ell^q},\qquad
 C_0=\frac1{\log7}+\frac1{\log4},\quad J\ge1,
 \tag{11}
\]

because s(n)<=C_0ell(n) and `(s-J)_+<=s^q J^(1-q)`. Equation (8) re-establishes this input domain after each finite unsafe return, with its actual amplification constant.

## 6. A slower energy has an additive horizon budget

Set

\[
 \psi(n)=1+\log\ell(n)>1\qquad(n>1).
\]

**Corollary AT3.** Each retained unsafe return satisfies

\[
 \psi(Bn)\le\psi(n)+\log6.
 \tag{12}
\]

Consequently, for nonnegative initial mass f with finite psi-moment,

\[
 \|H^jf\|_\psi
 \le\|f\|_\psi+j(\log6)\|f\|_1.
 \tag{13}
\]

The proof uses (5) pointwise before summation and mass loss at the absorbing state. It does not use an average over parity lifts.

For X>=1 this supplies the honest finite-horizon tightness bound

\[
 \sum_{R(n)\ge X}(H^jf)(n)
 \le\frac{\|f\|_\psi+j(\log6)\|f\|_1}
 {1+\log\log(X+6)}.
 \tag{14}
\]

The numerator is not uniform in j. Finiteness at each separate horizon therefore does not imply recurrence or all-time tightness.

## 7. An exact source-persistent closing target

This section separates a useful next hypothesis from the finite-horizon bounds already proved. Fix a finite nonnegative mass f that is positive at every u in U, and define its actual Cesaro occupation distributions

\[
 \mu_N=\frac1N\sum_{j=0}^{N-1}H^jf.
\]

**Theorem AT4 (conditional closure).** If the family `{mu_N:N>=1}` is uniformly tight on the ordinary countable state space U, and B has no nonabsorbing finite cycle, every positive ordinary Collatz orbit reaches 1. A sufficient, stronger tightness hypothesis is

\[
 \sup_{N\ge1}\frac1N\sum_{j<N}\|H^jf\|_\psi<\infty.
 \tag{16}
\]

**Proof.** The mass `m_j=||H^j f||_1` decreases to some m_infinity>=0. Uniform tightness, together with the common finite mass bound, gives a subsequence of mu_N converging in ordinary ell^1 to a measure mu of mass m_infinity. H is an ell^1 contraction and

\[
 H\mu_N-\mu_N=(H^Nf-f)/N\longrightarrow0
\]

in ell^1, so Hmu=mu. Equality of total masses first forces zero mass on killed sources, and then on all their finite predecessors. A finite invariant measure for a deterministic killed map is supported on finite cycles: if mu(x)>0, then each subsequent retained orbit point has mass at least mu(x); an infinite injective orbit is therefore impossible. Positive mass on a finite preperiod into a cycle is also impossible, because summing invariance over the cycle leaves zero mass for external entries, and this argument iterates backwards. Thus the absence of finite cycles forces mu=0 and m_infinity=0. Since f is positive at every u, an individual orbit that never reaches 1 would retain its fixed initial atom f(u)>0 in every H^j f, contradicting that limit. Every nonconvergent T orbit must visit U infinitely often, because an eventual G tail would force indefinite strict positive-rank descent. The conclusion therefore covers all ordinary starts. Finally psi is proper and tends to infinity with n, so Markov's inequality makes (16) imply uniform tightness. QED.

Uniform Cesaro tightness plus absence of B cycles is also necessary for Collatz: under convergence, dominated convergence gives `H^j f→0` in ell^1, and the Cesaro distributions form a tight family. The stronger moment bound (16) is not claimed necessary. The logarithmic domain theorem establishes only an O(N) upper bound for the average in (16), not a bound uniform in N; it does not prove this closing hypothesis.

## 8. The actual unsafe operator has essential spectral radius exactly one

The log-log domain admits a sharper operator statement than the logarithmic norm. Work on the Banach space X=ell^1(psi), permitting signed or complex inputs. Put `psi_*=1+log(log 7)>0`; every state in U has psi>=psi_*. The pointwise form of (12) gives

\[
 \|H^j\|_{X\to X}\le1+\frac{j\log6}{\psi_*}.
 \tag{17}
\]

**Theorem AT5.** For every j>=1, the distance of H^j to the compact operators on X is exactly one. Consequently

\[
 \boxed{r(H)=r_{\mathrm{ess}}(H)=1.}
 \tag{18}
\]

The conclusion remains valid if any fixed finite ordinary floor is additionally killed along each physical return.

**Upper bound.** Let P_M retain only the finitely many sources n<=M. The operator H^jP_M has finite rank. For all remaining source columns, (12) gives the ratio bound

\[
 \frac{\psi(B^jn)}{\psi(n)}\le1+\frac{j\log6}{\psi(n)}.
\]

Since psi(n) tends to infinity with n, the limsup of these tail ratios is at most one. Equation (8a) therefore implies `||H^j||_ess<=1`.

**Ordinary witnesses for the lower bound.** The precise arithmetic shadow used here is from `research/astra-three-routes/pass5/UNSAFE_REPAYMENT.md`, sections 1–2. For every K>=1, impose

\[
 n\equiv10\pmod{243},\qquad
 v_2(17n+73)=6K,\qquad n\ge11.
 \tag{19}
\]

These conditions form an infinite ordinary arithmetic progression. The first K copies of `111010`, split into A-modes `1110 | 10`, have their first 2K sources in U. At cycle boundaries s and intermediate states t=(27s+19)/16, their ranks are respectively `(s-1)^2/9` and `(t+5)^2/9`. The two-step cycle is `s↦(81s+73)/64`. These exact formulas and unsafe inequalities are retained, not replaced by a rational infinite realization.

For the fixed j, choose 2K>j. Its endpoint after j returns is still one of the displayed unsafe sources, so B^j=A^j on this prefix, with a fixed affine formula `B^jn=gamma_j n+eta_j`, gamma_j>0. As n tends to infinity through (19), both source and endpoint ranks are quadratic in n. Hence

\[
 \psi(B^jn)/\psi(n)\longrightarrow1,
 \qquad B^jn\longrightarrow\infty.
 \tag{20}
\]

For any compact operator C on X, the images of its unit ball have uniformly small weighted output tails. This follows by identifying X with ordinary ell^1 via multiplication by psi and using a finite epsilon-net for a compact set. Apply H^j-C to the normalized atom `delta_n/psi(n)`. Its H^j image has one output atom escaping every finite set, with weighted mass tending to one by (20); the compact image has arbitrarily small tail there. Thus `||H^j-C||>=1`. In particular, no assertion that the ell^1 unit basis is weakly null is used: that assertion would be false. This proves the essential-norm lower bound.

Equation (17) and the spectral-radius formula give r(H)<=1. Essential norms of all powers equal one, giving r_ess(H)=1 and therefore r(H)=1. Every finite physical state in the fixed word has a positive affine slope in n; sufficiently large members of (19) avoid any prescribed finite floor. The lower bound thus survives the additional killing, while the upper bounds only improve.

This is a statement about the **actual unsafe return operator**, not the fresh-lift matrix whose spectral radius is below one. It rules out a proof based on a strict essential spectral gap in this particular proper input space. It does not rule out source-specific eventual absorption or more discriminating estimates. Even if every positive source converged, unbounded finite transients would remain compatible with (18).

For clarity, eventual killing of each point mass is equivalent to Collatz, and unweighted ell^1 strong stability then follows by dominated convergence. Strong stability on X for every finite-psi-moment input is a potentially stronger assertion: the O(j) power bound in (17) is not a uniform power bound, so pointwise eventual absorption does not by itself establish weighted strong stability.

### The spectral point one has finite ordinary approximate eigenvectors

The same shadows show that 1 itself belongs to the approximate point spectrum and to the essential spectrum. Fix J>=2 and choose 2K>J in (19). Let x_i=B^i n for 0<=i<=J. For a fixed J the affine slopes are all distinct: at even and odd indices they are respectively powers of `81/64` and those powers times `27/16`. Hence these states are distinct for all sufficiently large n in the progression. Increase n further so that

\[
 1-1/J\le\psi(x_i)/\psi(x_0)\le1+1/J\qquad(0\le i\le J).
\]

Normalize the positive finite occupation vector

\[
 f_J=\frac{\sum_{i=0}^{J-1}\delta_{x_i}}
 {\sum_{i=0}^{J-1}\psi(x_i)},\qquad \|f_J\|_X=1.
\]

Only its two endpoint atoms remain under I-H, so

\[
 \|(I-H)f_J\|_X
 \le\frac{2+1/J}{J-1}\longrightarrow0.
 \tag{21}
\]

Choose the ordinary starts successively large enough that the finite supports of distinct f_J are disjoint. Their pairwise distance is two, so they have no norm-convergent subsequence. If I-H had a left inverse modulo compact operators, say S(I-H)=I+C with S bounded and C compact, (21) would give `(I+C)f_J→0`. Compactness of C would then force a convergent subsequence of f_J, a contradiction. Thus 1 is an essential spectral point as well as an approximate eigenvalue. All vectors come from different **finite ordinary shadows**; no infinite positive shadow is asserted.

## 9. Exact failure boundary and next lemma

The family (3) gives

\[
 \frac{\ell(Bx_j)}{\ell(x_j)}\longrightarrow2,
 \qquad \psi(Bx_j)-\psi(x_j)\longrightarrow\log2.
 \tag{15}
\]

So the logarithmic domain is invariant but the raw ell-energy is not contracting; the log-log energy has actual positive drift on infinitely many ordinary inputs above every floor. Its upward jumps are controlled, not absent.

The new completed interface is **preservation of the moment domain by the actual return map**, followed by reusable control of every safe excursion. The remaining global task is a return correlation or amortized estimate that prevents indefinite unsafe energy growth, or a different globally decreasing quantity. A bound like (14) uniform over all j, combined with a complete exclusion of nonabsorbing finite cycles, would exclude escaping orbits. Neither that uniform bound nor cycle exclusion is obtained here. An averaged finite-state parity contraction cannot be inserted for the missing estimate.

## 10. Frozen context and evidence

- Main checkout: `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
- Main `research/astra-three-routes/pass4/MOVING_GHOST_RANK.md`, T-A3-901/902: exact A, R, and polynomial height interface.
- Main `research/astra-three-routes/pass5/RANK_MOMENTS.md`, R-A3-1003(a): actual unsafe family (3); T-A3-1001: reciprocal rank summability.
- Main `research/astra-three-routes/pass5/UNSAFE_REPAYMENT.md`, T-A3-1101: finite ordinary all-unsafe shadows used in Theorem AT5.
- Main `research/integrated/renewal-transport/README.md`: current component and review boundaries.
- Uploaded Gemini `route_3_all_word_potential_and_lyapunov_pr149/PROOF_AND_IDEAS.md`, Idea 3A: square-root/log replacement proposal audited here.

The accompanying integer replay checks arithmetic interfaces and finite negative controls. The all-p divergence and logarithmic-domain results rely on the proofs above, not extrapolation from its finite sample. No new external theorem, stationary-law uniqueness assumption, floating-point spectral estimate, or unbounded computation is used.
