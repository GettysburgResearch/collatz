# Fixed-height forward power saving: exact partial results and the remaining contraction

> **Status: THEOREM-DEVELOPMENT / PARTIAL.** The fixed-height power-saving theorem is not proved here. This note proves two unconditional forward sparsity theorems, sharpens the inverse/forward bridge to the single floor `H=1`, proves an exact shell-contraction criterion that would close Collatz with the imported `0.901` predecessor exponent, and identifies why the two presently available averaging mechanisms do not supply that criterion.

## 1. Target and the weakest form sufficient for Collatz

For odd `N`, let

\[
\operatorname{Syr}(N)=\frac{3N+1}{2^{\nu_2(3N+1)}}.
\]

For fixed `H>=1` and `C>0`, put

\[
B_H(X;C)=\#\left\{N\le X:\ N\text{ odd and }
\operatorname{Syr}^m(N)>H\text{ for every }0\le m\le C\log N\right\}.
\]

Also put

\[
E_H(X)=\#\left\{N\le X:\ N\text{ odd and }
\operatorname{Syr}^m(N)>H\text{ for every }m\ge0\right\}.
\]

Clearly `E_H(X)<=B_H(X;C)` for every `C`. The eternal set is therefore the weaker target.

### Proposition 1 — the endpoint-one exponent race

Assume that for every fixed positive `b` with `3 ∤ b`,

\[
\pi_b(X)\ge c_bX^\gamma
\]

eventually. If, for one `beta<gamma`,

\[
E_1(X)=O(X^\beta),
\]

then every positive Collatz orbit reaches one. The same conclusion follows from
`B_1(X;C)=O(X^beta)` for any fixed `C>0`.

#### Proof

Suppose an orbit does not reach one. Choose an odd point `a` on that orbit and put
`b=Syr(a)`. Then `b` lies on the same nonconvergent orbit and `3 ∤ b`, since
`3a+1 ≡ 1 (mod 3)` and division by a power of two preserves a nonzero residue modulo
three.

By the inverse hypothesis, at least `c_bX^gamma` positive integers `n<=X` reach `b`.
Write each such integer uniquely as `n=2^r m` with `m` odd. The odd core `m` also
reaches `b`, hence never reaches one. A fixed odd core accounts for at most
`1+floor(log_2 X)` integers not exceeding `X`. Therefore

\[
E_1(X)\ge \frac{c_bX^\gamma}{1+\log_2X}.
\]

This contradicts `E_1(X)=O(X^beta)` when `beta<gamma`. The timed version follows from
`E_1(X)<=B_1(X;C)`. `□`

The imported predecessor theorem supplies `gamma=0.901`. Thus the single estimate

\[
\boxed{E_1(X)=O(X^{9/10})}
\]

would already suffice. Uniformity in every fixed `H` is desirable, but is not logically
necessary for this bridge.

## 2. Why the present first-passage estimate does not iterate to an endpoint power

The imported natural-density theorem separates two errors at a moving passage scale `x`:

\[
P(\text{scheduled no hit})\ll x^{-1/32000},
\]

and

\[
\|\text{flat passage law}-\text{logarithmic passage law}\|_1
\ll (\log x)^{-d},\qquad d<5/143.
\]

After the top-block splice, the fixed-floor inequality contains four terms. Two decay as
powers of the moving scale, one is a passage discrepancy of order `(log X)^(-d)`, and the
trace to the fixed floor contributes `(log H)^(-d)`. With `H` fixed, the published estimate
therefore has the form

\[
B_H(X;C_{\rm Syr})\le C_{d,H}X.
\]

The power-small scheduled failure cannot be substituted for the endpoint term: a source
may successfully pass every moving scale and still land in the exceptional set above `H`.
That distinction is semantic, not a loss from a loose final inequality.

There are two additional quantitative ceilings inside the same proof architecture.

1. The phase comparison is performed on a tube of length
   \[
   W\asymp \sqrt{\log x\,\log\log x}.
   \]
   A discrepancy estimate polynomial in `W` is only polylogarithmic in `x`. Improving the
   irrationality exponent while retaining this tube geometry cannot by itself create
   `x^(-delta)` endpoint decay.
2. The geometric trace uses scales whose logarithms grow by the fixed factor
   `alpha=1001/1000`. The number of passage levels between a fixed floor and `X` is
   `Theta(log log X)`. Even a hypothetical constant loss `theta<1` at every such level
   would produce only
   \[
   \theta^{\Theta(\log\log X)}=(\log X)^{-c},
   \]
   not an `X`-power.

A fixed-height power therefore needs a contraction repeated on `Theta(log X)` comparable
scales, or a one-shot estimate already polynomial in the counting endpoint.

## 3. Quantitative ceiling in the maximal-horizon pullback iteration

Inselmann's maximal-horizon argument uses `*-dense` sets: a set has exponent `D>0` when
its complement up to `X` is `O(X^(1-D))`. The displayed pullback lemmas propagate this
exponent through one bit-length block by a factor that can be made close to

\[
\rho=\log_2\sqrt3=0.792481250360\ldots.
\]

The trajectory-size exponent is propagated as `lambda -> q lambda` for an arbitrary fixed
`q` with `rho<q<1`. In the proof parameters one may make the density-exponent factor
`r_D` satisfy

\[
\rho<r_D<q.
\]

After `n` blocks, the tracked density exponent is at most a constant times `r_D^n`, while
the endpoint size is of order `X^(q^n)`. Reaching a fixed height requires

\[
q^n\asymp \frac1{\log X},
\qquad n=\Theta(\log\log X).
\]

Consequently

\[
r_D^n\asymp (\log X)^{-a},
\qquad a=\frac{\log r_D}{\log q}>1,
\]

and the exponent appearing in `X^{-D_n}` obeys

\[
D_n\log X=O((\log X)^{1-a})\longrightarrow0.
\]

Thus the exponents explicitly transported by that induction do not retain a fixed power at
constant height. This is a limitation of the tracked proof parameters, not a theorem that the
actual survivor set lacks a power saving.

## 4. A rigorous forward power saving for the all-supercritical lane

Use the one-division shortcut map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For a length-`L` parity word `w=(v_0,...,v_(L-1))`, put

\[
q_j(w)=\sum_{i<j}v_i,
\qquad
\alpha_0=\frac{\log2}{\log3},
\]

and let `W_L` be the words satisfying

\[
q_j(w)\ge \alpha_0j\qquad(1\le j\le L).
\]

These are exactly the coefficient-supercritical words through depth `L`.
Define

\[
\eta=h_2(\alpha_0)
=-\alpha_0\log_2\alpha_0-(1-\alpha_0)\log_2(1-\alpha_0)
=0.949955527188\ldots.
\]

### Theorem 2 — Lane-A source sparsity

The number of positive integers `n<=X` whose coefficient prefixes are all supercritical is

\[
O(X^\eta\log X).
\]

The same bound holds for sources that remain coefficient-supercritical through
`ceil(log_2 X)` steps.

#### Proof

Every binary word of length `L` is realized by exactly one residue class modulo `2^L`.
The prefix condition implies the terminal weight condition

\[
q_L(w)\ge\lceil\alpha_0L\rceil.
\]

Since `alpha_0>1/2` and binary entropy decreases on `[1/2,1]`,

\[
|W_L|
\le\sum_{q=\lceil\alpha_0L\rceil}^L\binom Lq
\le(L+1)2^{\eta L}.
\]

Take `L=ceil(log_2X)`. Since `2^L>=X`, each residue class modulo `2^L` contains at most
one integer in `[1,X]`. Hence the number of such sources is at most

\[
(L+1)2^{\eta L}=O(X^\eta\log X).
\]

An all-time coefficient-supercritical source is contained in every finite-depth set. `□`

### Proposition 3 — the symbolic exponent is sharp

\[
\lim_{L\to\infty}\frac1L\log_2|W_L|=\eta.
\]

#### Proof

The preceding estimate gives the upper bound. For the lower bound, choose an integer
`q_L>alpha_0L` with `q_L/L->alpha_0`. For a binary word of weight `q_L`, give a `1`
the increment `1-alpha_0` and a `0` the increment `-alpha_0`. The total increment is
positive. Rotate the cyclic word to start immediately after the last minimum of its partial
sums. Every new partial sum is then positive. Equality between two distinct partial sums is
impossible because `alpha_0` is irrational. Thus every weight-`q_L` word has a cyclic
rotation in `W_L`. At most `L` words rotate to one selected word, so

\[
|W_L|\ge \frac1L\binom L{q_L}.
\]

Stirling's formula gives the lower entropy `h_2(alpha_0)=eta`. `□`

Therefore a proof using only the cardinality of the supercritical parity language cannot
improve the exponent below `0.949955...`. In particular this unconditional Lane-A bound
does not cross the imported inverse exponent `0.901`.

## 5. A second unconditional power saving: global orbit minima

Call `n` a forward record minimum when

\[
T^j(n)\ge n\qquad(j\ge0).
\]

Every nonconvergent forward orbit has such an element: take the least integer on that orbit.

### Theorem 4 — record-minimum sparsity

The number of forward record minima not exceeding `X` is

\[
O(X^\eta\log X),
\]

with the same `eta=0.949955527188...`.

#### Proof

Work in a dyadic block `M<=n<2M`, and put `L=floor(log_2M)`. Along the first `L`
steps of a record-minimum orbit every current value `x` is at least `n`, hence at least `M`.
At an odd step,

\[
\frac{3x+1}{2}\le \frac{3+1/M}{2}x,
\]

while an even step multiplies by `1/2`. If the first `L` parity bits contain `q` odd steps,
then

\[
T^L(n)\le n\frac{(3+1/M)^q}{2^L}.
\]

Since `T^L(n)>=n`,

\[
\frac qL\ge p_M:=\frac{\log2}{\log(3+1/M)}.
\]

A residue class modulo `2^L` occurs at most twice in the interval `[M,2M)`. Therefore the
number of record minima in this block is at most

\[
2(L+1)2^{Lh_2(p_M)}.
\]

Now `p_M=alpha_0+O(1/M)` and hence
`L(h_2(p_M)-h_2(alpha_0))=O((log M)/M)`. The block count is consequently
`O(M^eta log M)`, uniformly for large `M`. Summing the dyadic blocks gives
`O(X^eta log X)`. `□`

This theorem power-sparsifies possible counterexample minima. It does not bound the inverse
basin of one minimum, which is exactly the population used by the predecessor theorem.

## 6. The exact local inequality that would finish the exponent race

The missing step can be stated without asymptotic ambiguity.

Put

\[
e_{H,j}=2^{-j}E_H(2^j).
\]

### Lemma 5 — fixed-ratio contraction

Let `R>1`, `0<theta<1`, and `sigma>0`. Suppose normalized bad masses on the scales
`X_j=R^j` satisfy

\[
e_{j+1}\le\theta e_j+A R^{-\sigma j}
\]

for all sufficiently large `j`. Set

\[
\kappa=-\frac{\log\theta}{\log R}.
\]

Then, for every `delta<min(kappa,sigma)`,

\[
e_j=O(R^{-\delta j}),
\qquad
E_H(X_j)=O(X_j^{1-\delta}).
\]

If `kappa` and `sigma` are unequal, the endpoint `delta=min(kappa,sigma)` is also valid;
when they are equal there is only an additional factor `j`.

#### Proof

Iterating the recurrence gives

\[
e_j\le\theta^{j-j_0}e_{j_0}
+A\sum_{i=j_0}^{j-1}\theta^{j-1-i}R^{-\sigma i}.
\]

Writing `theta=R^(-kappa)`, the sum is geometric after factoring
`R^(-kappa j)`. It is `O(R^{-min(kappa,sigma)j})` when the exponents differ and
`O(jR^{-kappa j})` in the equal case. `□`

### Corollary 6 — an exact `0.900` closure certificate

For each fixed `H`, it would suffice to prove that, eventually,

\[
\boxed{
e_{H,j+1}\le\frac{93}{100}e_{H,j}+A_H2^{-j/10}.}
\tag{C}
\]

Indeed,

\[
2\cdot93^{10}<100^{10},
\]

so `(93/100)2^(1/10)<1` and

\[
-\log_2(93/100)>1/10.
\]

Lemma 5 yields

\[
E_H(X)=O_H(X^{9/10})
\]

first on dyadic endpoints and then for every real endpoint by monotonicity. At `H=1`,
Proposition 1 and the imported `0.901` inverse bound would prove Collatz.

The quantitative request is therefore concrete:

```text
On each doubling of the counting endpoint, prove at least a 7% contraction
of normalized eternal bad mass, modulo an O_H(2^(-j/10)) error.
```

A timed analogue of `(C)` would be stronger. A residue-only or one-passage mixing estimate
is not enough: it must contract the particular survivor population after preserving the
remaining time budget or the eternal-tail property.

## 7. Candidate certificate architecture

The most direct proof-producing program is a killed, height-aware transfer operator on one
dyadic shell.

A state must retain at least:

1. the exact transported residue needed to replay the physical Syracuse branches;
2. the current logarithmic height band relative to the lower shell;
3. whether the orbit has entered `[1,H]`;
4. enough accumulated valuation information to transport ordinary counting, not only
   harmonic mass;
5. an unbounded or rigorously truncated carry with a certified tail bound.

The desired finite certificate is a positive test function `V` and a decomposition of one
shell transition into

\[
\mathcal K_HV\le\frac{93}{100}V+\mathcal R_H,
\]

where the total ordinary mass of `R_H` on the `j`-th shell is `O_H(2^{-j/10})`.
The certificate must be checked on the exact ordinary transition law. A spectral radius from
a fixed-depth residue graph, without an ordinary-height/carry tail theorem, would reproduce
the known finite-horizon artifact rather than prove `(C)`.

## 8. Status boundary and handoff

What is proved here:

- the endpoint-one form of the inverse/forward bridge;
- the exponent `eta=0.949955527188...` Lane-A upper bound;
- sharpness of that symbolic entropy exponent;
- the same power upper bound for global forward orbit minima;
- the fixed-ratio contraction lemma and the exact rational certificate target `(C)`;
- the stated method ceilings for the currently tracked transport exponents.

What remains open:

- inequality `(C)` or any other fixed-height upper exponent below `0.901`;
- a proof-producing height-aware transfer operator with an ordinary concretization theorem;
- control of inverse basins of the sparse record minima;
- the full Collatz conjecture.

The next useful computation is not a broad Collatz census. It is a shell-local operator search
whose output is either an exact positive supersolution for `(C)` or a dual obstruction showing
which state variable is missing.
