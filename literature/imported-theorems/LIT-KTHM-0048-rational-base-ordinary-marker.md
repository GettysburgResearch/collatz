# LIT-KTHM-0048 — Rational-base finite representations are the canonical ordinary-marker boundary

**Type:** imported exact infrastructure with a self-contained finite-integer proof and a strict native nonapplication boundary.  
**Sources:** Akiyama–Frougny–Sakarovitch (2008); Frougny–Klouda (2012).  
**Maps to:** `ADEL/L-9313`, `ADEL/L-9314`, `PR3/T-0002`, `PR35/T-8806`, issue #40, and every restricted-digit ordinary-stabilization problem.

## 1. Modified division in base `p/q`

Let `p>q>=1` be coprime integers. For a nonnegative integer `n_0`, define uniquely

```text
q*n_i = p*n_(i+1) + a_i,
0 <= a_i < p.                                           (1)
```

The digit `a_i` is the least residue of `q*n_i` modulo `p`.

### Theorem — every nonnegative integer has one finite representation

The sequence `(n_i)` reaches zero, and

```text
n_0 = sum_(i>=0) (a_i/q)*(p/q)^i,                        (2)
```

with only finitely many nonzero digits. The digit word is unique.

### Proof

If `n_i>0`, then from `(1)`

```text
0 <= n_(i+1) <= q*n_i/p < n_i.
```

Thus the nonnegative integer sequence strictly decreases until it reaches zero. Iterating `(1)` and dividing by the appropriate power of `q` gives `(2)`. At every step `a_i` is forced modulo `p`; induction proves uniqueness. QED.

This is the least-significant-digit-first rational-base division algorithm of Akiyama, Frougny, and Sakarovitch.

## 2. The p-adic extension

Frougny and Klouda extend rational-base systems to `r`-adic inputs when `r` divides the rational-base numerator. Their results include:

1. exact algorithms representing the relevant `r`-adic numbers;
2. a characterization of finite representations;
3. an eventual-periodicity theorem for rational `r`-adic inputs under the paper's specified representation convention; and
4. finite transducers between four equivalent rational-base conventions.

The external p-adic theorems are imported as black boxes. The finite-integer theorem above is proved directly because it is the load-bearing project interface.

## 3. Native ordinary-marker interpretation

The repository repeatedly reaches a recurrence of the form

```text
q*x_(i+1) = p*x_i + digit_i                              (3)
```

or its reversed/sign-shifted version, together with a restricted digit alphabet. A finite prefix always determines one compatible residue cylinder. The unique completion is an ordinary nonnegative integer exactly when the corresponding least-significant representation terminates — equivalently, when its newly appended high blocks are eventually zero.

This is the correct conceptual placement of:

```text
ADEL/L-9314:  R_(K+1)=R_K+q_K*64^K;
PR35/T-8806: restricted bottom words in base 5/4;
PR3/T-0002:  restricted digits in an induced N/M radix map.
```

The native recurrences use translated, signed, state-dependent, or severely restricted alphabets. Therefore none is silently identified with the canonical full-digit AFS language. A definition-level conjugacy is required in each application.

## 4. Consequence for counterexample construction

The literature does not turn a compatible infinite digit word into an ordinary integer. It instead sharpens the positive target:

```text
construct one restricted rational-base branch
whose least-significant expansion terminates on the input side
while its forward induced orbit remains in the allowed digits forever.       (4)
```

For a stationary expanding chart, `(4)` is an integer-first invariant problem. For a nonstationary chart, it is a terminating-address plus forward-regeneration problem.

## 5. Nonconsequences

The imported results do **not** prove:

- that a restricted digit subtree contains any positive integer branch;
- that a `2`-adic rational value has a bounded real shadow;
- that eventual periodicity in one completion transfers to another;
- that the centered `64 -> 81` survivor exists or is empty;
- that a collision digit alphabet is the canonical AFS alphabet;
- or any Collatz counterexample.

## 6. Repository use

Every constructive branch should record:

```text
RADIX RECURRENCE:
DIGIT ALPHABET:
FULL OR RESTRICTED LANGUAGE:
ORDINARY INPUT CRITERION:
FORWARD INVARIANCE CRITERION:
STATE NEEDED BEYOND THE DIGIT:
```

This prevents a finite-compatible or p-adic branch from being mistaken for a positive ordinary initialization.