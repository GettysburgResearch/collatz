# Independent adversarial reconstruction of the ADEL 9309–9312 chains

**Agent:** `gpt56-review-9309-01`  
**Reviewer identity/model:** OpenAI `GPT-5.6 Pro`  
**Role:** independent adversarial reviewer; reconstruction, not extension  
**Issue:** #15  
**Umbrella issue:** #4  
**Source PR:** #16  
**Review branch:** `agent/gpt56-review-9309-01/15-audit-adel-chain`  
**Frozen target commit:** `e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6`  
**Review date:** 2026-07-22  
**Claimed chains:**

```text
ADEL/L-9309 -> ADEL/T-9307 -> ADEL/T-9308
ADEL/L-9310 -> ADEL/T-9311 -> ADEL/T-9312
```

`T-9312` also uses `T-9308`; the two chains meet there. `L-9309` is not a logical dependency of `L-9310` beyond sharing the reciprocal-phase convention.

## Executive verdict

| Claim | Review verdict | Repository status proposed | First invalid inference / counterexample |
|---|---|---|---|
| `ADEL/L-9309` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `ADEL/T-9307` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none; dependency metadata should be completed |
| `ADEL/T-9308` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `ADEL/L-9310` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `ADEL/T-9311` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |
| `ADEL/T-9312` | **PASSED** | `INDEPENDENTLY_VERIFIED` | none |

I independently reconstructed every load-bearing inference in the six claims and the precise portions of `L-9301`, `L-9303`, `L-9305`, `L-9307`, and `T-9305` used by them. The submitted proofs agree with the reconstructions. No theorem statement needed narrowing, no new claim ID is required, and no downstream invalidation is triggered.

Two repository-maintenance corrections are required but do not alter a theorem:

1. `T-9307` uses the triadic product identity and survivor/CRT transfer clauses, so its dependency metadata should include `L-9305`, `T-9305`, and `T-9306` in addition to `L-9309` and `L-9303`.
2. The packet summary diagrams incorrectly draw `L-9309 -> L-9310`. The correct graph consists of two parallel inputs meeting at `T-9312`:

```text
L-9309 -> T-9307 -> T-9308 --+
                                  +-> T-9312
L-9310 -> T-9311 --------------+
```

## Frozen scope and method

I froze the source at the full commit SHA above before inspecting proofs. I first extracted only each statement, quantifiers, definitions, and declared dependencies. I then:

1. derived each claim independently on scratch paper;
2. audited endpoints, signs, valuations, digit order, moduli, indexing, interval translations, and uniformity parameters;
3. reconstructed the exact dependency interfaces used by the chain rather than trusting their names;
4. implemented a standard-library checker that imports no author code;
5. searched beyond the author experiment ranges, including negative and translated inputs;
6. only after the derivation compared every submitted proof inference with the independent derivation;
7. audited direct downstream claims for consequences of a possible failure.

The checker is corroboration only. The verdicts rest on the derivations below.

---

## `ADEL/L-9309` — lift-digit cylinder bijection

### Hypotheses and quantifiers

For every integer `K >= 1`, every integer `h`, and every `0 <= ell < K`, let `q_ell(h)` be the least nonnegative residue modulo `81^(ell+1)` satisfying

```text
q_ell(h) = -17 h 64^(ell-K)  (mod 81^(ell+1)),
```

where the negative power is the modular inverse. For `0 <= ell < K-1`, define

```text
d_ell(h) = floor(q_(ell+1)(h) / 81^(ell+1)) in {0,...,80}.
```

The claim asserts the exact recurrence, its normalized form, a full bijection modulo `81^K`, a prefix bijection modulo `81^L` for every `1 <= L <= K`, the interval-cylinder consequences, and an exact perturbation congruence for every integer increment.

### Independent derivation

Let `B_ell = 81^(ell+1)`. Reducing the defining congruence for `q_(ell+1)` modulo `B_ell` gives

```text
q_(ell+1) = 64 q_ell  (mod B_ell).
```

Because `q_(ell+1)` lies in `[0,81 B_ell)`, it has the unique decomposition

```text
q_(ell+1) = (64 q_ell mod B_ell) + d_ell B_ell,
0 <= d_ell < 81.
```

This proves the lift recurrence and also verifies that `d_ell` is the new most-significant base-81 lift digit, not a least-significant digit.

Writing `y_ell=q_ell/B_ell`, the fractional part of `64 y_ell` is exactly `(64q_ell mod B_ell)/B_ell`, hence

```text
y_(ell+1) = ({64 y_ell}+d_ell)/81.
```

Given a tuple `(q_0,d_0,...,d_(K-2))`, the recurrence constructs a unique `q_(K-1)` in `[0,81^K)`. At the terminal level,

```text
q_(K-1) = -17 h 64^(-1) (mod 81^K).
```

Both `17` and `64` are units modulo `81^K`, so

```text
h = -64 * 17^(-1) q_(K-1) (mod 81^K).
```

Backward reduction of the recurrence recovers every earlier `q_ell`; therefore the constructed `h` returns the original tuple. This proves bijectivity, including surjectivity rather than merely cardinality agreement.

The identical argument stopped at level `L-1` gives

```text
h = -17^(-1) 64^(K-L+1) q_(L-1) (mod 81^L),
```

so every exact length-`L` prefix is one class modulo `81^L`. A consecutive block of length `81^L` contains exactly one representative of every such class; a shorter interval contains at most one. Subtracting the two defining congruences gives the perturbation law.

### Boundary and convention audit

- `K=1`: the digit list is empty and `h mod 81 -> q_0` is multiplication by a unit, hence a bijection.
- `L=1`: a prefix is just `q_0`, selecting one class modulo `81`.
- `L=K`: terminal inversion uses `64^(-1)` at level `K-1`, so the exponent in the submitted formula is correct.
- Least-nonnegative residues are essential to identify `d_ell` by a floor; no signed representative is used here.
- Multiplication by `81` makes `q_0=0`, consistent with the valuation convention.
- Exact prefix equality is sparse; it does not imply a consecutive frequency block.

### Submitted-proof comparison

| Submitted inference | Independent check | Result |
|---|---|---|
| Reduce the next-level congruence modulo `81^(ell+1)` | Gives `q_(ell+1) = 64q_ell` at the lower modulus | match |
| Decompose the lifted least residue with one digit `d` | Unique because the next modulus is exactly 81 times larger | match |
| Divide by `81^(ell+2)` | Fractional part is the lower residue divided by `81^(ell+1)` | match |
| Reconstruct `q_(K-1)` from the tuple | Recurrence stays in the required residue ranges | match |
| Terminal inversion | Unit is `-64*17^(-1)` modulo `81^K` | match |
| Prefix inversion | Unit exponent is `64^(K-L+1)` | match |
| Complete/short interval statements | Standard residue-class count, including translated intervals | match |
| Perturbation | Direct subtraction of congruences | match |

The author proof leaves the backward check from terminal `h` to the earlier tuple implicit, but the recurrence makes it immediate; this is not a gap.

### Independent checker and counterexample search

- exhaustive bijection/recurrence enumeration for `K=1,2,3`;
- `538,083` complete tuples checked;
- `3,000` large signed random checks with up to 100 decimal digits;
- perturbations with up to 80 decimal digits;
- no collision, missing tuple, recurrence error, prefix-dependence error, or perturbation failure.

**Verdict: PASSED.**

---

## `ADEL/T-9307` — low-energy prefix entropy

### Hypotheses and quantifiers

For all integers `K >= L >= 1` and all integers `h`, use the first `L` reciprocal phases

```text
y_ell(h)=q_ell(h)/81^(ell+1),  0 <= ell < L,
E_(K,L)(h)=sum ||y_ell(h)||^2.
```

Let

```text
beta = 17 sqrt(2)/27 < 1,
eta = -log_81(beta) > 0.
```

The theorem asserts a count in every translated complete block of length `81^L`, a count in every arbitrary translated interval of length `H>=81` with `L=floor(log_81 H)<=K`, and a Fourier-product bound outside that exceptional set.

### Independent derivation

For any real shift `phi`, the 81-point grid `(j+phi)/81` has at most 41 points in the open half-circle `||x||<1/4`; therefore at least 40 points have `||x||>=1/4`. For every `s>0`,

```text
(1/81) sum_j exp(-s ||(j+phi)/81||^2)
 <= 41/81 + (40/81) exp(-s/16).
```

Choose `s=16 log 4`. The right side is

```text
kappa=(41+10)/81=17/27.
```

By `L-9309`, on any complete block modulo `81^L`, `(q_0,d_0,...,d_(L-2))` is exactly uniform. Conditional on previous digits, the next phase is a shifted 81-grid because

```text
y_(ell+1)=({64y_ell}+d_ell)/81.
```

Iterating conditional expectations yields

```text
E[exp(-s E_(K,L))] <= kappa^L.
```

On `E_(K,L)<=L/64`, the exponential is at least `exp(-sL/64)`. Hence

```text
P(E_(K,L)<=L/64)
 <= exp(sL/64) kappa^L
 = (sqrt(2)*17/27)^L
 = beta^L.
```

Multiplication by `81^L` proves the complete-block count.

For an arbitrary interval of length `H`, put `B=81^L`. Then `B<=H<81B`. It has at most 80 complete `B`-blocks and one remainder. Enlarge the remainder to one translated `B`-block; overlap cannot invalidate an upper bound. Thus the count is at most

```text
81 B beta^L = 81 B^(1-eta) <= 81 H^(1-eta),
```

where `0<eta<1` because `1/81<beta<1`.

The triadic coefficient is the complete product of the `K` cosine masks. Since every omitted factor has modulus at most one and

```text
|cos(pi x)| <= exp(-2||x||^2),
```

outside the exceptional set,

```text
F_K^(3)(h) <= exp(-2 E_(K,L)(h)) < exp(-L/32).
```

Finally `L>=log(H)/log(81)-1`, giving the stated power bound with factor `exp(1/32)`. The magnitude comparison in `T-9305` transfers it to the survivor product, and `T-9305`/`T-9306` transfer it to the CRT formulations with their explicit errors.

### Boundary and convention audit

- The threshold uses `<=L/64`; the complement has strict `>L/64`, which is stronger than needed for the displayed nonexceptional `<=` bound.
- The open arc convention permits 41 near points and guarantees 40 far points for every shift, including endpoint alignments.
- The digit order is conditional from low lift level to high lift level; no probabilistic independence is assumed outside a complete residue block.
- Uniformity is exact for every translated complete block, not merely a block starting at zero.
- An incomplete interval is handled by at most 81 complete-block estimates, with no alignment assumption.
- `L=floor(log_81 H)` and `L<=K` are both necessary and are present.
- The triadic phase sign is immaterial for magnitudes, but the reconstructed product uses the repository’s negative `-17` residue and positive additive character consistently.

### Submitted-proof comparison

| Submitted step | Independent check | Result |
|---|---|---|
| 41/40 shifted-grid split | Sharp enough for all shifts and endpoint placements | match |
| `s=16 log4`, `kappa=17/27` | Arithmetic exact | match |
| Conditional lift-digit iteration | Follows from full tuple uniformity, not an independence heuristic | match |
| Lower-tail exponential Markov step | Inequality direction is correct | match |
| `exp(s/64)=sqrt(2)` | Exact | match |
| Complete block count | Multiply probability by `81^L` | match |
| Arbitrary interval partition | At most 80 full blocks plus one enlarged remainder | match |
| `beta^L=B^(-eta)` | Exact by definition of `eta` | match |
| Fourier mask and discarded tail factors | Product factors have modulus at most one | match |
| Convert `L` to `H` | Costs exactly the absolute factor `e^(1/32)` | match |

### Dependency metadata correction

The mathematical proof passes, but the header/ledger under-declare the Fourier and transfer dependencies. The count theorem uses only `L-9309` and the local exponential-moment argument. The Fourier clause additionally uses `L-9305` (triadic product) and `L-9303` (cosine-energy inequality). The final survivor/CRT transfer sentence uses `T-9305` and `T-9306`. This is a metadata repair, not a theorem repair.

### Independent checker and counterexample search

- complete translated blocks for `L=1,2,3`, including large negative and positive starting points;
- largest complete block: `81^3=531,441` frequencies;
- arbitrary translated intervals through length `600,000`;
- direct nonexceptional Fourier checks on 491 large signed samples;
- no count or Fourier-bound failure.

**Verdict: PASSED.**

---

## `ADEL/T-9308` — uniform harmonic tail

### Hypotheses and quantifiers

For every integer depth `K>=1` and every integer cutoff `81<=M<=2^K`, define the normalized triadic and survivor magnitudes as in the statement. With

```text
gamma=1/(32 log81),
delta=min(eta,gamma)>0,
```

the theorem claims a `K`-independent constant `C_tail` bounding the weighted tail, then a survivor transfer error and a low/high reduction for every growing cutoff sequence.

### Independent derivation

On a shell `X<=h<2X`, set `L=floor(log_81 X)`. `T-9307` gives at most `81X^(1-eta)` exceptional frequencies. Their harmonic contribution is at most `81X^(-eta)`. Every other coefficient is at most

```text
exp(-L/32) <= exp(1/32) X^(-gamma),
```

so its total shell contribution is at most `exp(1/32)X^(-gamma)` up to a harmless endpoint constant. Thus

```text
shell <= C_eta X^(-eta)+C_gamma X^(-gamma).
```

The prefix condition is uniform: if `X<=2^K`, then

```text
floor(log_81 X) <= floor(log_81 2^K) < K,
```

so `L<=K` even on the last partial shell. Summing shells `X=2^rM` gives a convergent geometric series. One explicit valid choice derived independently is

```text
C_tail = 81/(1-2^(-eta))
       + exp(1/32)/(1-2^(-gamma)),
```

which is approximately `4675.514482303709`. The submitted proof uses another harmless absolute constant.

`T-9305` gives

```text
|F_K^(2)(h)-F_K^(3)(h)| <= pi h/64^K.
```

After division by `h`, summing over at most `2^K` frequencies costs `pi*2^K/64^K=pi*2^(-5K)`. Splitting at `M_K` leaves no gap or overlap: the low part is `1<=h<M_K` and the tail is `M_K<=h<=2^K`. If the low-window maximum is `epsilon_K`, its contribution is at most `epsilon_K(1+log M_K)`; `epsilon_K log M_K->0` implies this tends to zero.

### Boundary and uniformity audit

- `M=81`: all hypotheses are valid; only the constant is crude.
- `M=2^K`: the one-point tail is included.
- The last dyadic shell may extend beyond `2^K`; applying the interval theorem to the full shell is safe and the actual sum uses only its intersection with the target range.
- `log_81(2^K)<K` for every positive `K`, so the ambient-depth condition is uniform.
- The survivor transfer uses a full-range error, which safely dominates the shorter tail error.
- `M_K->infinity` makes `log M_K->infinity`; hence `epsilon_K log M_K->0` also forces `epsilon_K->0`.

### Submitted-proof comparison

| Submitted step | Independent check | Result |
|---|---|---|
| Exceptional count on `[X,2X)` | Apply `T-9307` directly with interval length `X` | match |
| Exceptional harmonic mass | Coefficients `<=1`, weights `<=1/X` | match |
| Nonexceptional power loss | Correct floor-log conversion | match |
| Prefix depth on largest shell | `log_81(2^K)<K` | match |
| Geometric shell sum | Converges because `delta>0` | match |
| Survivor/mirror transfer | Exactly `pi*2^(-5K)` on the full range | match |
| Low/high reduction | Same cutoff, no missing frequency | match |

### Independent checker and counterexample search

- full frequency ranges for every `4<=K<=18`, reaching `h=262,144`;
- 44 tail checks at endpoint and interior cutoffs using the explicit constant above;
- exact cutoff-partition diagnostics at 15 depths;
- no failure.

**Verdict: PASSED.**

---

## `ADEL/L-9310` — completion-height rigidity

### Hypotheses and quantifiers

For every pair of coprime integers `2<=M<N`, every nonzero integer `c` with `gcd(c,M)=1`, every integer `K>=1`, and every nonzero integer `h` satisfying the primitive condition `M` does not divide `h`, define for every `0<=ell<K` the representative

```text
s_ell in (-N^(ell+1)/2, N^(ell+1)/2]
```

of `-ch M^(ell-K)` modulo `N^(ell+1)`. Put `x_ell=s_ell/N^(ell+1)` and, for `0<=ell<K-1`,

```text
a_ell=(M s_ell-s_(ell+1))/N^(ell+1)=M x_ell-N x_(ell+1).
```

The claim covers carry integrality and energy, every zero-carry run, the nonzero completion numerator, the exact modulus, the run-length bound, right-to-left chaining, and the `64->81` specialization.

### Independent derivation

Reducing the level `ell+1` congruence modulo `N^(ell+1)` gives

```text
s_(ell+1)=M s_ell (mod N^(ell+1)),
```

so every `a_ell` is an integer. Therefore

```text
W <= sum a_ell^2.
```

Also `(u-v)^2<=2u^2+2v^2`, hence

```text
sum a_ell^2
 <= 2M^2 sum_(ell=0)^(K-2) x_ell^2
  + 2N^2 sum_(ell=1)^(K-1) x_ell^2
 <= 2(M^2+N^2) E_K(h).
```

If `a_ell=...=a_(ell+r-1)=0`, exact equality—not merely congruence—gives

```text
s_(ell+r)=M^r s_ell.
```

At level `ell+r`, multiply the defining congruence by `M^(K-ell-r)`. The resulting ordinary integer

```text
Z=M^(K-ell)s_ell+ch
```

is divisible by exactly the claimed modulus `N^(ell+r+1)`. If `Z=0`, then `M` divides `ch`; because `c` is a unit modulo `M`, `M` divides `h`, contradicting primitiveness. Thus `Z` is nonzero.

The signed representative gives `|s_ell|<=N^(ell+1)/2`, so divisibility and height imply

```text
N^(ell+r+1) <= |Z|
 <= (1/2)M^(K-ell)N^(ell+1)+|ch|.
```

After division and the harmless weakening `|ch|/N^(ell+1)<=|ch|`, with `t=K-ell-r>=1`,

```text
N^r <= (1/2)M^(r+t)+|ch|.
```

If `N^r<=2|ch|`, then `r<=C_h=log_N(2|ch|)`. Otherwise subtraction gives `N^r<M^(r+t)`, hence

```text
r < [log M/log(N/M)] t = kappa_(M,N) t.
```

Thus every run satisfies `r<=kappa t+C_h`.

For terminal indexing, write the zero-run lengths from left to right as `z_0,...,z_W`, allowing length zero. Let `t_i` be the number of phase levels after run `i`. Then

```text
t_W=1,
t_i=t_(i+1)+z_(i+1)+1.
```

Since `z_i<=kappa t_i+C_h`, with `A=1+kappa` and `D=C_h+1`,

```text
t_i<=A t_(i+1)+D.
```

The initial run satisfies `K=z_0+t_0<=A t_0+C_h`. Iterating and simplifying gives

```text
K <= B_h A^(W+1),
B_h=1+(C_h+1)/kappa.
```

The displayed lower bounds for `W` and energy follow by logarithmic inversion. For `M=64,N=81,c=17`, `2(M^2+N^2)=21314` and the stated criticality constant is correct.

### Endpoint, sign, modulus, and primitive audit

- `K=1`: there are no carries, `W=0`, and the positive-part energy lower bound is valid.
- A terminal zero run ends at carry `K-2`; its terminal phase length is `t=1`, not zero.
- Zero-length separator runs are harmless because `C_h>=0`; the right-to-left recurrence remains exact.
- The completion modulus is `N^(ell+r+1)`, not `N^(ell+r)` and not `N^(ell+r+2)`.
- The nonzero argument needs only `M` not dividing `h`, not `gcd(h,M)=1`.
- Negative `c` and `h` are handled by the same divisibility and absolute-height argument.
- If `N` is even, the half-modulus tie is represented positively as required by `(-m/2,m/2]`; the energy and carry inequalities still hold.
- No external Diophantine or S-unit theorem enters.

### Submitted-proof comparison

| Submitted inference | Independent check | Result |
|---|---|---|
| Carry integrality | Correct lower-modulus reduction | match |
| `W<=sum a^2` | Uses integer quantization only | match |
| Quadratic energy bound | Endpoint sums are safely enlarged to all phases | match |
| Zero-run equality | Repeated exact carry-zero equations | match |
| Completion numerator and modulus | Multiplication exponent and modulus both correct | match |
| `Z!=0` | Primitive condition plus `c` an `M`-unit is sufficient | match |
| Height squeeze | Correct; displayed version is a safe weakening after division | match |
| Two-case run bound | Strict inequality on the large branch is correct | match |
| Terminal recurrence | `t_W=1` and `t_i=t_(i+1)+r_(i+1)+1` | match |
| Global affine iteration | The proposed `B_h` is slightly loose but valid | match |
| Special constants | `kappa` and `21314` recompute exactly | match |

### Independent checker and counterexample search

The author’s `X-9302` scanned only the special chart through `K=80` and positive `h<=K^2`. The independent checker instead tested:

- `35,766` carry chains;
- exhaustive small coprime charts with signed `c,h`, including even terminal moduli;
- 900 random general charts;
- numerators up to 70 decimal digits;
- special `64->81` depths `81,127,191,257,383,512`;
- every zero-run modulus, `Z!=0`, height squeeze, large-branch inequality, terminal indexing, carry-energy inequality, and global bound;
- longest zero run observed: 4;
- no failure.

**Verdict: PASSED.**

---

## `ADEL/T-9311` — uniform subexponential cusp decay

### Hypotheses and quantifiers

For every depth `K` and integer frequency `h`, define the survivor and triadic magnitudes. The primitive bound applies whenever `64` does not divide `h`. The arbitrary-frequency bound applies whenever `0<|h|<64^K`, after removing the exact `64`-adic valuation. The uniform theorem applies to every positive sequence `H_K` with `log(2+H_K)=o(K)`.

### Independent derivation

The signed representative `s_ell` from `L-9310` and the least nonnegative residue `q_ell` represent the same class; therefore

```text
|s_ell|/81^(ell+1)=||q_ell/81^(ell+1)||.
```

The triadic coefficient is the exact product of those `K` cosine masks. Applying

```text
|cos(pi x)|<=exp(-2||x||^2)
```

and the `L-9310` energy lower bound yields the primitive `F_K^(3)` estimate exactly. `T-9305` then adds at most `pi|h|/64^K` to obtain the survivor bound.

When `K>=A B(h)`, the positive part is active. Algebra gives

```text
F_K^(3)(h)
 <= exp(2/C_*) (B(h)/K)^[2/(C_* log A)],
```

so the displayed `b_*` is correct.

For arbitrary nonzero `h`, let `v=v_64(h)`, `h_0=h/64^v`, and `K_0=K-v`. The condition `|h|<64^K` forces `v<K`. The moving-character identity gives the exact, lossless equality

```text
F_K^(2)(h)=F_(K_0)^(2)(h_0).
```

For `|h|<=H_K`, uniformly,

```text
v<=log_64 H_K=o(K),
K_0=(1-o(1))K,
B(h_0)<=1+[1+log_81(34H_K)]/kappa=o(K).
```

Thus `K_0/B(h_0)->infinity` uniformly, forcing the first term to zero. The comparison term also vanishes because

```text
H_K/64^(K-o(K)) -> 0.
```

For `H_K=K^R`, `K_0>=K-O_R(logK)` and `B(h_0)=O_R(logK)`, which yields the stated polynomial-window envelope after absorbing the exponentially small comparison term.

### Sign, digit-order, valuation, and uniformity audit

- The triadic product uses the repository’s negative phase sign; cosine magnitudes are even, so no hidden conjugation affects the theorem.
- The dyadic/triadic phase order is reversed in some finite-word descriptions, but the product contains all levels once, so the magnitude is unchanged; the explicit `ell` indexing in `L-9307` aligns them.
- `v_64` counts powers of 64, not powers of 2. This is exactly the depth-reduction unit in `L-9301`.
- A frequency divisible by a large `64^v` is a shallower copy, not an untreated exceptional case.
- The uniform statement is asymptotic; `log H_K=o(K)` ensures `H_K<64^K` eventually.
- Negative frequencies are covered because all bounds depend on `|h|` and Fourier magnitudes are even.
- Every constant is independent of `K`, `h`, and the chosen subexponential sequence except `C_R,K_R` in the polynomial specialization.

### Submitted-proof comparison

| Submitted step | Independent check | Result |
|---|---|---|
| Identify signed energy with circle-distance energy | Exact representative identity | match |
| Apply cosine-energy inequality | All `K` mask factors included | match |
| Substitute `L-9310` | Constant `C_*=21314` correct | match |
| Survivor/mirror comparison | Error and sign correct for magnitudes | match |
| Activate positive part | Condition `K>=AB(h)` is exact | match |
| Compute `b_*` | `2/(C_* log A)` | match |
| Remove powers of 64 | Exact equality, with `v<K` from the frequency range | match |
| Uniform subexponential estimates | Every bound is uniform in `|h|<=H_K` | match |
| Polynomial window | Exponential error can be absorbed for large `K` | match |

### Independent checker and counterexample search

- 690 signed primitive product checks through depth 320;
- 698 arbitrary-frequency and exact power-of-64 reduction checks;
- subexponential samples reaching beyond the author’s `h<=K^2` range;
- exhaustive polynomial windows at `K=96` and `K=112`;
- observed maxima were approximately `6.56e-18` and `4.45e-19`, respectively;
- no bound or depth-reduction failure.

**Verdict: PASSED.**

---

## `ADEL/T-9312` — all-depth complete weighted EQ

### Hypotheses and quantifiers

For every integer `K>=1`,

```text
E_K=sum_(1<=h<=2^K) F_K(h)/h.
```

The theorem asserts `E_K->0` along all integer depths and gives an explicit three-term upper bound for every sufficiently large `K`.

### Independent derivation

Choose the integer cutoff `M_K=K`. For sufficiently large `K`, `81<=K<=2^K`. By `T-9311` with polynomial exponent `R=1`,

```text
max_(1<=h<K) F_K(h)
 <= C_0 (logK/K)^b_*.
```

Therefore

```text
sum_(1<=h<K) F_K(h)/h
 <= C_0(1+logK)(logK/K)^b_*.
```

For every `b_*>0`, the logarithm of this expression tends to `-infinity`, so it vanishes. `T-9308` supplies

```text
sum_(K<=h<=2^K) F_K(h)/h
 <= C_tail K^(-delta)+pi*2^(-5K).
```

The two ranges are disjoint and exhaustive: the first ends at `K-1`, the second begins at `K`. Adding proves the displayed quantitative bound and all-depth convergence.

### Endpoint and scope audit

- `h=0` never appears.
- There is no cutoff gap and no double counting.
- The use of `K` as both depth and cutoff is valid once `K>=81`.
- Large `64`-power frequencies below the cutoff are already covered by `T-9311`.
- No depth average or exceptional subsequence is introduced.
- The theorem proves a finite-set weighted Fourier criterion only; it does not decide the ordinary-integer survivor intersection or the Collatz conjecture.

### Submitted-proof comparison

| Submitted step | Independent check | Result |
|---|---|---|
| Set `M_K=K` | Meets `T-9308` hypotheses eventually | match |
| Apply `T-9311`, `R=1` | Covers the entire low range | match |
| Bound harmonic sum | `sum_(h<K)1/h<=1+logK` | match |
| Show low term tends to zero | Any positive `b_*` suffices | match |
| Apply `T-9308` to high range | Begins at the same cutoff | match |
| Add estimates | Produces the stated three terms | match |

### Independent checker and counterexample search

- exact cutoff-partition diagnostics for all full-range depths `4<=K<=18`;
- direct computation of every coefficient through `h=2^18`;
- observed `E_18 approximately 0.003050220446570828`;
- finite nonmonotonicity at small depths was allowed by the theorem and did not affect the proof;
- no cutoff or summation failure.

**Verdict: PASSED.**

---

## Cross-cutting adversarial findings

### Zero-carry modulus and terminal indexing

The modulus is exactly `N^(ell+r+1)`. It comes from the level `ell+r` state, whose defining modulus is `N^((ell+r)+1)`. The terminal zero run has `t=1` because the carry chain has `K-1` transitions but `K` phase states. Both conventions agree with the submitted proof and the independent exact checker.

### Primitive numerator and nonzero completion numerator

The argument needs `M` not dividing `h`, not full coprimality. If `Z=0`, then `M` divides `ch`; since `c` is a unit modulo `M`, this forces `M` to divide `h`. No absolute-value inequality silently assumes nonzero.

### Dyadic–triadic signs and digit order

The reconstructed triadic character has positive additive-character sign and phase coefficient `-17`; the dyadic reciprocal identity produces the same unshifted phase plus the positive rational shift. A conjugate character would conjugate complex coefficients but not the magnitudes used here. Reversing a finite Bernoulli word changes factor order only; the product and all six statements are unchanged. The exact `ell`-indexed formulas in `L-9307` were separately checked.

### Complete residue blocks

Uniformity is exact because `L-9309` is a bijection, not because of a heuristic Markov model. It applies to every complete translated residue system. No uniformity is claimed for a short interval; `T-9307` covers an incomplete interval by at most 81 complete-block estimates.

### Powers of 64

The reduction uses `v_64`, not `v_2`, and is an exact moving-character equality. The condition `0<|h|<64^K` guarantees positive residual depth. The uniform subexponential proof handles the loss `v=o(K)` uniformly.

### Uniformity in parameters

- `L-9309`: exact for every `K,L,h` in the stated ranges.
- `T-9307`: constants independent of `K`, translation, and interval location; the only restriction is `L<=K`.
- `T-9308`: one absolute constant works for every `K,M` in the stated range.
- `L-9310`: pointwise in every admissible `M,N,c,K,h`; dependence on `h` is explicitly through `B_h`.
- `T-9311`: convergence is uniform over every entire subexponential window, not merely pointwise for each sequence of frequencies.
- `T-9312`: no exceptional sequence of depths remains.

## Independent checker summary

The committed checker imports no repository module and uses only the Python standard library. Load-bearing modular, divisibility, carry, energy, and interval-count assertions use exact integers, `Fraction`, or high-precision `Decimal`; floating-point cosine products are diagnostic only.

| Test family | Range/results |
|---|---|
| Lift bijection | exhaustive `K<=3`; 538,083 tuples |
| Large signed lift perturbations | 3,000 checks; up to 100 decimal digits |
| Complete entropy blocks | translated blocks through `81^3=531,441` |
| Arbitrary intervals | translated positive/negative intervals through length 600,000 |
| General carry chains | 35,766 chains; signed charts; depth through 512; numerators through 70 digits |
| Primitive/power-64 Fourier checks | 690 primitive and 698 reduced checks; depth through 320 |
| Full Fourier ranges | every frequency through `2^18=262,144` |
| Frozen semantic digest | `f206209eab78290569eb63013dc51a4b0bb3d4473bd5bfafb209772abec828d1` |
| Checker file SHA-256 | `9244a142df53e6656f9d42452f5cb5d445f7f9d6b2093936ff3a4a33f4e1da53` |
| Frozen JSON SHA-256 | `406c1f29e48160d2edc893e9af6469fc2ae50b4ec1d925ce73d7484cf89d83cb` |

The author’s carry experiment stopped at depth 80 and positive `h<=K^2`; the independent scan deliberately crosses both boundaries.

## Downstream dependency audit

No reviewed step failed, so no downstream claim is refuted or narrowed. The following are logical consequences only after their other dependencies are reviewed:

- `R-9301` may use the verified exact-cylinder sparsity of `L-9309`.
- `T-9309` and `T-9310` may use the verified high-frequency tail, but their valuation/depth-statistical arguments were not reviewed here.
- `R-9302`, `Q-9302`, and the ordinary-code comparison use `L-9310` alongside separate claims not reviewed here.
- `T-9312` itself is verified; any issue-#4 Erdős–Turán, fair-window, minimal-survivor, or ordinary-room consequence remains `PROPOSED` until that translation is independently reconstructed.
- No status change is justified for `T-9313`, `T-9314`, `X-9303`, or the ordinary-integer intersection question from this review.

## What was reconstructed versus what remains external

### Independently reconstructed here

- all six target statements and every load-bearing inference;
- the reciprocal phase sign/index convention needed from `L-9307`;
- the exact triadic Bernoulli cosine product needed from `L-9305`;
- the cosine-energy inequality needed from `L-9303`;
- the magnitude comparison needed from `T-9305`;
- the exact power-of-64 self-similarity needed from `L-9301`.

### Not independently verified here

- the full complex CRT statement of `T-9304`/`T-9306` beyond the magnitude interface used above;
- all stationarization/topological claims in `D-9301` and `D-9303`, beyond directly reconstructing their finite product identities;
- the depth-statistical theorems `T-9303`, `T-9309`, and `T-9310`;
- the fixed-room/minimum claims `T-9313`, `T-9314`, and computation `X-9303`;
- any translation from weighted EQ to an actual ordinary Collatz trajectory or to the existence/nonexistence of a Collatz counterexample.

No external literature theorem is load-bearing for the six verified claims. Literature references in the packet are explanatory motivation only.

## Replay commands

From the repository root:

```bash
python3 reports/gpt56-review-9309-01/check_adel_chains.py \
  --output /tmp/adel-review-replay.json \
  --check-results reports/gpt56-review-9309-01/independent-results.json

sha256sum \
  reports/gpt56-review-9309-01/check_adel_chains.py \
  reports/gpt56-review-9309-01/independent-results.json
```

Frozen environment:

```text
Python 3.13.5 (GCC 14.2.0)
Linux 4.4.0 x86_64, glibc 2.41
seed 0xADE19309
```

A replay on the frozen environment took about 26 seconds. Runtime is not part of the semantic digest.

## Limitations

- Finite computation cannot establish a universal theorem; it only searched for implementation-level and small/medium counterexamples.
- Floating-point product values are not used as proof. The exact arithmetic checks are the load-bearing diagnostics.
- This review did not independently reconstruct the issue-#4 downstream counting interfaces or any ordinary-integer/Collatz interpretation.
- Status promotions are proposed on a draft review PR and remain subject to repository integration; the reviewer does not merge the PR.

## Repository changes recommended by this review

1. Record `gpt56-review-9309-01` as reviewer for the six target claims and promote them from `PROPOSED` to `INDEPENDENTLY_VERIFIED`.
2. Complete the `T-9307` dependency declaration as described above.
3. Correct the dependency diagrams so the entropy and carry chains are parallel and meet at `T-9312`.
4. Preserve all author proof text and history; no claim statement or proof body needs replacement.
5. Keep downstream issue-#4 consequences at their current status until independently reconstructed.

## Session-report fields

**Starting hypothesis:** one or more of the new all-depth steps might fail at a modulus, terminal-run, character-sign, incomplete-interval, or uniformity boundary.  
**Approaches attempted:** independent derivations, exact convention audit, general-chart algebra, complete residue enumeration, translated interval scans, direct Fourier products, and proof comparison.  
**New results:** all six target claims pass; an explicit admissible `C_tail` was reconstructed; two dependency-document defects were identified.  
**Candidate counterexamples:** none.  
**Failed approaches:** the first checker version double-subtracted the cutoff frequency in its own partition diagnostic; correcting it reproduced the theorem’s disjoint split. A larger initial scan was reduced after exact-profile optimization; no mathematical test was removed from the frozen suite.  
**Potential errors:** no mathematical error found; only dependency metadata/diagram corrections.  
**Files changed:** this report, claim matrix, independent checker, frozen results, and reviewed dependency/status summary.  
**Claims affected:** `L-9309`, `T-9307`, `T-9308`, `L-9310`, `T-9311`, `T-9312`.  
**Recommended next actions:** independently review the issue-#4 downstream EQ/counting translation before promoting those consequences.  
**Organizational improvement ideas:** keep logical dependency graphs separate from recommended review order, and distinguish core dependencies from dependencies used only by corollaries.
