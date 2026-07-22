# L-8804 — Exact meet-in-the-middle cylinder composition

Claim ID: L-8804  
Title: Survivor cylinders compose by one modular translation  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8806  
Scope: every finite depth of the base-`5/4` bottom map  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Put

```text
tau(x)=ceil(5x/4)=(5x+3)//4.
```

For `n>=0`, let `D_n` be the set of nonnegative integers whose first `n`
bottom digits are all in `{0,1}`; equivalently,

```text
x in D_n
iff
tau^j(x) mod 4 is in {0,3} for 0<=j<n.
```

Let

```text
S_n = D_n intersect [0,4^n)
```

be the canonical survivor residues, and for `r in S_n` put

```text
y_n(r)=tau^n(r).
```

Then the following hold.

### 1. Exact cylinder-affine identity

For every `h>=0`, `r in S_h`, and integer `t>=0`,

```text
tau^h(r+4^h*t)=y_h(r)+5^h*t.                       (1)
```

In particular, every point in the residue cylinder `r mod 4^h` follows the
same first `h` bottom digits.

### 2. Exact composition law

For all `h,m>=0`, every `x in [0,4^(h+m))` has a unique decomposition

```text
x=r+4^h*t,
0<=r<4^h,
0<=t<4^m.
```

It belongs to `S_(h+m)` exactly when

```text
r in S_h
and
(y_h(r)+5^h*t) mod 4^m is in S_m.                  (2)
```

Since `5^h` is a unit modulo `4^m`, for each pair `(r,s) in S_h x S_m`
there is a unique admissible quotient

```text
t congruent 5^(-h)*(s-y_h(r)) mod 4^m.             (3)
```

The pair-to-residue map

```text
(r,s) |-> r+4^h*t
```

is a bijection from `S_h x S_m` onto `S_(h+m)`.

### 3. Exact least-positive-root formula

Put

```text
Q=4^m,
H=4^h,
u=5^(-h) mod Q,
T_m={u*s mod Q : s in S_m}.
```

For `r in S_h`, define

```text
c_r=u*y_h(r) mod Q
```

and let `d(r)` be the least nonnegative cyclic difference from `c_r` to an
element of `T_m`. If `r=0` and this difference is zero, use the least positive
cyclic difference instead, thereby excluding the zero root. Then

```text
min(S_(h+m) \ {0})
  = min_(r in S_h) [r+H*d(r)].                       (4)
```

After sorting `T_m`, every `d(r)` is obtained by one cyclic successor query.
Thus the exact depth-`h+m` minimum can be certified using frontiers of sizes
`2^h` and `2^m`, rather than explicitly materializing all `2^(h+m)` final
residues.

## Motivation

T-8806 reduced the physical chart question to an exact forbidden-digit orbit.
The direct depth-`n` frontier has `2^n` residues and becomes expensive before it
produces a useful sharp lower bound. Equations (1)--(4) expose the missing
semigroup structure: the high quotient propagates through an `h`-step cylinder
by multiplication with `5^h`, while the low residue contributes one translated
endpoint.

The result is not heuristic pruning. It is an exact factorization of the full
finite survivor set.

## Proof

### Cylinder-affine identity

We prove the stronger induction statement that, for `0<=k<=h`,

```text
tau^k(r+4^h*t)=tau^k(r)+5^k*4^(h-k)*t.             (5)
```

It is trivial at `k=0`. Suppose it holds at `k<h`. The difference between the
two current states is divisible by `4`, so the states have the same residue
modulo `4` and hence the same bottom digit. Applying the same affine branch of
`tau` divides the difference by `4` and multiplies it by `5`. This gives (5) at
`k+1`. Setting `k=h` proves (1).

### Composition law

Let `x=r+4^h*t` be its unique mixed-radix decomposition. The first `h` steps
are legal iff `r in S_h`; this is the cylinder assertion in (1). Conditional on
that event, equation (1) gives the state after `h` steps as

```text
y_h(r)+5^h*t.
```

The next `m` steps are legal iff this state lies in `D_m`, which depends only on
its residue modulo `4^m`. This proves (2).

Multiplication by the odd number `5^h` is a bijection modulo `4^m`. Therefore,
for every fixed `r` and every target survivor residue `s in S_m`, equation (2)
has the unique solution (3). Different `s` give different `t`, and different
`r` give different low residues modulo `4^h`. Hence the pair map is bijective.

### Minimum formula

For fixed `r`, equations (2)--(3) say that the valid quotients modulo `Q` are
exactly the cyclic translate

```text
T_m-c_r.
```

The least representative is therefore the first sorted element of `T_m` at or
after `c_r`, wrapping once at `Q`. Since `0<=r<H`, ordering numbers
`r+H*t` first minimizes `t` and then `r`. Excluding only the pair that produces
`x=0` gives (4). **QED**

## Dependency audit

- T-8806 supplies the bottom map and the interpretation of legal digits.
- The proof uses only exact integer arithmetic and modular invertibility of
  `5^h` modulo a power of `4`.
- No probabilistic model, asymptotic assumption, or finite output is used in the
  lemma.

## Gap audit

- Equation (4) computes a finite-depth minimum; it does not by itself prove that
  these minima tend to infinity.
- The zero residue belongs to every `S_n` and must be excluded explicitly when
  asking for a positive root.
- A wrapped successor in `T_m` represents a valid quotient modulo `4^m`; the
  representative must lie in `[0,4^m)`.
- The formula remains exact for unequal split depths.
- Time and memory claims assume exact generation of both input frontiers; they
  are algorithmic consequences, not mathematical dependencies.

## Adversarial tests

X-8803 compares the meet-in-the-middle minimum against direct frontier minima at
every depth through `20`. It then applies a `25+25` split at depth `50` and
physically replays the resulting least root through its first forbidden digit.

## Remaining uncertainty

The global question is whether the nondecreasing least-positive-root sequence
is unbounded. L-8804 makes substantially deeper exact terms accessible but does
not establish their asymptotic behavior.

## Suggested next attack

1. Derive certified lower bounds on the cyclic successor distance `d(r)` from
   arithmetic structure in `T_m`.
2. Search for a composition inequality forcing the least root to increase under
   repeated doubling of depth.
3. Replace sorted materialization by a proof-carrying recursive successor oracle
   suitable for depths beyond the current memory frontier.
