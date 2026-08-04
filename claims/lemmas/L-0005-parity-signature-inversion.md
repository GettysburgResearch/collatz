# L-0005 — Parity signatures and exact inverse reconstruction

Claim ID: `L-0005`  
Title: Parity-signature inversion for finite shortcut-Collatz words  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001`, `L-0001`  
Scope: finite parity words, ordinary nonnegative integers, and finite inverse reconstruction  
Related counterexample candidates: none

## Statement

Let

\[
w=t_0t_1\cdots t_{L-1}\in\{0,1\}^L
\]

be a chronological parity word, let

\[
a=a(w)=\sum_{j=0}^{L-1}t_j,
\]

and let

\[
B(w)=
\sum_{\substack{0\le j<L\\t_j=1}}
2^j3^{\sum_{i=j+1}^{L-1}t_i}.
\tag{1}
\]

Then the following hold.

### 1. Uniform bound

\[
\boxed{0\le B(w)<2^L3^a.}
\tag{2}
\]

### 2. Unique parity residue

There is exactly one residue

\[
r(w)\pmod{2^L}
\]

whose first \(L\) shortcut-Collatz parities are \(w\). It is characterized by

\[
\boxed{3^a r(w)+B(w)\equiv0\pmod{2^L}.}
\tag{3}
\]

### 3. Inverse-signature criterion

Assume \(a\ge1\), and define the **inverse signature**

\[
\boxed{
\sigma(w)
\equiv 2^{-L}B(w)\pmod{3^a}.
}
\tag{4}
\]

Here \(2^{-L}\) denotes the inverse of \(2^L\) modulo \(3^a\).
For an integer \(y\), put

\[
n_w(y)=\frac{2^Ly-B(w)}{3^a}.
\tag{5}
\]

Then \(n_w(y)\) is an integer exactly when

\[
y\equiv\sigma(w)\pmod{3^a}.
\tag{6}
\]

Whenever (6) holds and \(n_w(y)\ge0\), the integer \(n_w(y)\) follows the parity word \(w\) and

\[
\boxed{T^L(n_w(y))=y.}
\tag{7}
\]

### 4. Consecutive odd tail

If

\[
y=2^ku-1,
\qquad k\ge1,
\qquad u\ge1,
\tag{8}
\]

then the next \(k\) parities of \(y\) are all odd and

\[
\boxed{
T^j(y)=3^j2^{k-j}u-1
\qquad(0\le j\le k).
}
\tag{9}
\]

In particular,

\[
T^k(y)=3^ku-1.
\tag{10}
\]

## Motivation

A collision fiber can be constructed backwards from a common output. The
signature (4) is exactly the finite congruence that says which parity words can
share that output. Part 4 then supplies a common tail whose odd-step density can
be chosen independently of the branching created by the inverse words.

This separates two previously entangled design problems:

- **branching:** find many words with one inverse signature;
- **drift:** append a common tail with enough odd steps to make the full block
  supercritical.

## Proof

### The bound on \(B(w)\)

Proceed by induction on word length. The empty word has \(B=0\). Suppose \(w\)
has length \(L\), weight \(a\), and satisfies (2).

Appending a zero gives

\[
B(w0)=B(w)<2^L3^a<2^{L+1}3^a.
\]

Appending a one multiplies every previous contribution by three and adds the
new contribution \(2^L\):

\[
B(w1)=3B(w)+2^L.
\]

Therefore

\[
B(w1)
<3\cdot2^L3^a+2^L
=2^L(3^{a+1}+1)
<2^{L+1}3^{a+1}.
\]

This proves (2).

### Existence and uniqueness of the parity residue

We prove uniqueness inductively. A word of length zero has one residue modulo
one. Suppose a length-\(L\) word \(w\) is realized by one residue \(r\) modulo
\(2^L\). Its two lifts modulo \(2^{L+1}\) are

\[
r,
\qquad r+2^L.
\]

They have the same first \(L\) parities. By `L-0001`, their values after these
\(L\) steps differ by

\[
\frac{3^a2^L}{2^L}=3^a,
\]

which is odd. Thus exactly one lift has next parity zero, and exactly one has
next parity one. Induction gives one residue for every finite word.

For the realizing residue, `L-0001` gives

\[
2^LT^L(r(w))=3^ar(w)+B(w).
\]

Reducing modulo \(2^L\) proves (3). Since \(3^a\) is odd, it is invertible
modulo \(2^L\), so (3) also uniquely characterizes the residue.

### Inverse reconstruction

Equation (5) is integral exactly when

\[
2^Ly\equiv B(w)\pmod{3^a},
\]

which is equivalent to (6).

Assume now that it is integral and nonnegative. From

\[
3^an_w(y)+B(w)=2^Ly
\]

we obtain

\[
3^an_w(y)+B(w)\equiv0\pmod{2^L}.
\]

By the uniqueness characterization (3), \(n_w(y)\equiv r(w)\pmod{2^L}\), so
it follows the parity word \(w\). Applying `L-0001` to that word gives (7).

### The odd tail

For (8), the case \(j=0\) is immediate. If (9) holds at some \(j<k\), then

\[
3^j2^{k-j}u-1
\]

is odd. One shortcut step gives

\[
\frac{3(3^j2^{k-j}u-1)+1}{2}
=3^{j+1}2^{k-j-1}u-1.
\]

This proves (9) and (10) by induction. ∎

## Dependency audit

- `L-0001` supplies the affine action of a realized parity word.
- The converse direction is justified by the independently proved uniqueness of
  the parity residue; it is not inferred from the affine identity alone.
- Every object in the lemma is finite and ordinary. No adic limit is used.

## Gap audit

- Part 3 requires nonnegativity before claiming an ordinary Collatz trajectory.
- Equal signatures only produce a finite collision family. They do not imply an
  infinite admissible induced-map orbit.
- The signature modulus is exactly \(3^a\); stronger congruence modulo higher
  powers is treated by `L-0006`.

## Adversarial tests

`X-0003` reconstructs the signature classes for every \(1\le m\le8\), directly
traces every selected inverse word, and checks the common odd tails and lifted
identities.

## Remaining uncertainty

The author believes the finite lemma is complete. It awaits independent
reconstruction.

## Suggested next attack

Use equal-signature classes as collision codes, and optimize their internal
digit geometry rather than searching only for record cardinality.
