# L-8403 — Euclidean monoid compiler for mechanical words

Claim ID: `L-8403`  
Title: Lower and upper mechanical words can be evaluated in every monoid by a logarithmic-depth Euclidean recursion  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: none  
Scope: finite rational mechanical words and arbitrary associative monoids

## Mechanical words

For integers

```text
0<=p<=q,
```

define the lower and upper binary mechanical words of length `q` and weight
`p` by

```text
L(p,q)_j
 =floor((j+1)p/q)-floor(jp/q),                        (1)
```

```text
U(p,q)_j
 =ceil((j+1)p/q)-ceil(jp/q),                          (2)
```

for `0<=j<q`.

Let `x_0,x_1` be elements of an arbitrary monoid.  For a binary word `w`, write

```text
Pi(w)=x_(w_0)x_(w_1)...x_(w_(q-1)).                  (3)
```

No commutativity is assumed.

## Statement — Euclidean recursion

Write

```text
q=a p+s,
0<=s<p.
```

For `0<p<q`, put

```text
y_0=x_0^(a-1)x_1,
y_1=x_0^a x_1,                                        (4)
```

```text
z_0=x_1 x_0^(a-1),
z_1=x_1 x_0^a.                                        (5)
```

Then

```text
boxed:
Pi(L(p,q);x_0,x_1)
 =Pi(U(s,p);y_0,y_1),                                 (6)
```

```text
boxed:
Pi(U(p,q);x_0,x_1)
 =Pi(L(s,p);z_0,z_1).                                 (7)
```

The boundary cases are

```text
Pi(L(0,q))=Pi(U(0,q))=x_0^q,
Pi(L(q,q))=Pi(U(q,q))=x_1^q.                          (8)
```

Thus the word product is computed using the Euclidean algorithm for `(p,q)`.
The recursion depth is `O(log q)` and no symbol string of length `q` is
expanded.

## Proof

The ones of the lower word occur at

```text
ceil(tq/p)-1,
1<=t<=p.
```

The number of zeros immediately before the `t`-th one is

```text
ceil(tq/p)-ceil((t-1)q/p)-1
 =a-1+[ceil(ts/p)-ceil((t-1)s/p)].                    (9)
```

The bracket is the corresponding symbol of `U(s,p)`.  Therefore each zero of
`U(s,p)` expands to `0^(a-1)1`, each one expands to `0^a1`, and (6) follows.

The ones of the upper word occur at

```text
floor(tq/p),
0<=t<p.
```

The number of zeros immediately after the `t`-th one is

```text
floor((t+1)q/p)-floor(tq/p)-1
 =a-1+[floor((t+1)s/p)-floor(ts/p)].                  (10)
```

The bracket is the corresponding symbol of `L(s,p)`.  Hence the two images are
`1 0^(a-1)` and `1 0^a`, proving (7).  Equation (8) is immediate. **QED**

## Affine-cycle specialization

For a modulus `M`, attach to valuation symbol `epsilon in {0,1}` the summary

```text
(k,A,P,Q,C)
 =(1,1+epsilon,3,2^(1+epsilon),1) mod M.              (11)
```

Concatenation is

```text
(k,A,P,Q,C)*(k',A',P',Q',C')
 =(k+k', A+A', PP', QQ', P'C+QC') mod M.              (12)
```

Applying (6)--(8) computes the exact affine summary of a balanced valuation word
of length trillions using only logarithmically many monoid levels and fast
monoid powering.

The same recursion can operate in:

- exact residue monoids;
- directed real interval affine monoids;
- product monoids carrying several factor residues simultaneously;
- verifier monoids carrying length, valuation, and local certificate hashes.

## Rotation note

For coprime `p,q`, `U(p,q)` is the one-symbol cyclic rotation of `L(p,q)`.  By
`L-8402`, cycle divisibility is rotation invariant; nevertheless the compiler
keeps lower and upper products distinct because the ambient monoid is
noncommutative.

## Dependency audit

The proof is elementary floor/ceiling arithmetic.  It does not import a
Sturmian-value theorem or assume any cycle exists.

## Gap audit

- A compressed exact summary modulo a proper divisor is not a full cycle
  certificate.
- Formal balance does not imply numerator divisibility.
- The compiler does not decide equality of trillion-bit exponential circuits
  over the ordinary integers.

## Adversarial tests

`X-8401` reconstructs every lower/upper word for all small coprime pairs in a
finite control range and compares the recursion with explicit multiplication.
It then compiles the frozen trillion-step target modulo a 61-bit certified
denominator component and in a 120-digit directed interval monoid.

## Suggested next attack

Augment the compiler with block-replacement nodes from `L-8402`, then search for
small arithmetic circuits whose full ordinary numerator factors through the
complete cycle denominator, not merely through a sampled component.