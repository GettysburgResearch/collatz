# L-0012 — Inverse signatures are exactly negative return targets

Claim ID: `L-0012`  
Title: Equivalence between finite inverse-signature codes and negative-template preimage families  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0001`, `L-0005`, `T-0008`  
Scope: fixed-length, fixed-weight parity words and ordinary negative integers  
Related counterexample candidates: none

## Statement

Let \(w\) be a binary parity word of length \(L\) and weight \(a\). Put

\[
M=2^L,\qquad N=3^a,\qquad B=B(w),
\]

and define its inverse signature

\[
\sigma(w)\equiv M^{-1}B\pmod N.
	ag{1}
\]

Then the following are equivalent for positive integers \(u,v\):

1. the negative integer \(-u\) follows the parity word \(w\) and
   \[
   T^L(-u)=-v;
   	ag{2}
   \]
2. the exact Diophantine identity
   \[
   oxed{B+Mv=Nu}
   	ag{3}
   \]
   holds;
3. the target satisfies
   \[
   oxed{v\equiv-\sigma(w)\pmod N}
   	ag{4}
   \]
   and
   \[
   u=rac{B+Mv}{N}.
   	ag{5}
   \]

Consequently, let \(\mathcal C\) be any finite fixed-length, fixed-weight parity code. The following are equivalent:

- all words of \(\mathcal C\) have one common inverse signature \(\sigma\pmod N\);
- for every positive representative
  \[
  v\equiv-\sigma\pmod N,
  	ag{6}
  \]
  the integers
  \[
  u_w=rac{B(w)+Mv}{N}\qquad(w\in\mathcal C)
  	ag{7}
  \]
  are positive integers satisfying
  \[
  oxed{T^L(-u_w)=-v}\qquad(w\in\mathcal C).
  	ag{8}
  \]

Thus a finite inverse collision code is exactly a finite family of negative preimages of one negative target, all at the same depth and with the same odd count.

## Proof

If \(-u\) follows \(w\), `L-0001` gives

\[
T^L(-u)=rac{-Nu+B}{M}.
\]

This equals \(-v\) exactly when

\[
-Nu+B=-Mv,
\]

which is (3). Hence (1) and (2) are equivalent.

Reducing (3) modulo \(N\) gives

\[
B+Mv\equiv0\pmod N.
\]

Because \(M\) is invertible modulo \(N\), this is

\[
v\equiv-M^{-1}B=-\sigma(w)\pmod N,
\]

and solving (3) for \(u\) gives (5). Thus (2) implies (3).

Conversely, assume (4) and define \(u\) by (5). Then \(u\) is a positive integer and

\[
N(-u)+B=-Mv\equiv0\pmod M.
\]

Therefore \(-u\) lies in the unique residue class modulo \(M\) that realizes \(w\); this uniqueness is the parity-vector inverse statement in `L-0005`. Hence \(-u\) follows \(w\), and substitution into the affine formula gives \(T^L(-u)=-v\).

For a code \(\mathcal C\), one common signature makes the same congruence (6) valid for every word. Applying the single-word result gives (7)--(8). Conversely, a common target \(-v\) gives

\[
\sigma(w)\equiv-v\pmod N
\]

for every word, so all signatures agree. ∎

## Exact geometry

For two codewords \(w,w'\), the corresponding negative template difference is

\[
u_w-u_{w'}=rac{B(w)-B(w')}{N}.
	ag{9}
\]

The positive branch residues in `T-0008` are \(r_w=M-u_w\), so

\[
r_w-r_{w'}=-(u_w-u_{w'}).
	ag{10}
\]

Hence the inverse-root offset geometry developed in `L-0007` is exactly the reflected geometry of a negative preimage fiber.

## Motivation

This identifies the hidden common object behind two previously separate-looking programs:

- `L-0005`--`T-0007` construct finite equal-signature parity codes;
- `T-0008`--`T-0009` study negative-template return systems.

They are the same construction. The signature is simply the negative target modulo \(3^a\), and the inverse roots are the magnitudes of its negative preimages.

The collision-code composition algebra can therefore be reinterpreted as an algebra for composing negative return languages. Conversely, negative preimage-tree structure can be used to design parity codes with renewal properties rather than only large cardinality.

## Dependency audit

- `L-0001` supplies the affine action.
- `L-0005` supplies uniqueness of the parity residue and the exact inverse direction.
- `T-0008` supplies the negative-shadow interpretation but is not needed for the algebraic equivalence.

## Gap audit

- A large negative preimage fiber is still finite.
- Choosing a target representative \(v\) changes all template magnitudes by the same affine amount but does not solve infinite renewal closure.
- Equal depth and weight are restrictive; variable-depth renewal systems require `T-0009`.

## Adversarial tests

`X-0006` verifies the identity \(B+Mv=Nu\) and the common target for every branch of `O-0001` through `O-0005`.

## Remaining uncertainty

The finite equivalence appears complete.

## Suggested next attack

Apply collision-code composition directly inside the reverse tree of a small negative target or cycle. Seek code operations that preserve a regular return-language state, not merely a common signature and finite offset geometry.
