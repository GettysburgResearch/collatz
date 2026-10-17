# L-0001 — Parity-affine iterate formula

Claim ID: `L-0001`  
Title: Parity-affine formula for a finite shortcut-Collatz word  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0001` / `NOTATION.md`  
Scope: finite shortcut-Collatz trajectories on ordinary integers  
Related counterexample candidates: none

## Statement

Let

\[
w=t_0t_1\cdots t_{L-1}\in\{0,1\}^L
\]

be the chronological parity word followed by an integer \(n\) during its first \(L\) shortcut-Collatz steps. Put

\[
a=\sum_{i=0}^{L-1}t_i
\]

and

\[
B(w)=
\sum_{\substack{0\le j<L\\t_j=1}}
2^j3^{\sum_{i=j+1}^{L-1}t_i}.
\]

Then

\[
\boxed{
T^L(n)=\frac{3^a n+B(w)}{2^L}.
}
\]

In particular,

\[
3^a n+B(w)\equiv0\pmod{2^L}.
\]

## Definitions

All notation is fixed in `NOTATION.md`. Parity bits are chronological, not written in reverse trajectory order.

## Motivation

A finite parity block acts affinely on its residue class. This makes it possible to recognize exact collisions between different parity blocks and to convert those collisions into radix-rewrite maps.

## Proof

For \(0\le k\le L\), let

\[
a_k=\sum_{i=0}^{k-1}t_i
\]

and define

\[
B_k=
\sum_{\substack{0\le j<k\\t_j=1}}
2^j3^{\sum_{i=j+1}^{k-1}t_i}.
\]

We prove by induction on \(k\) that

\[
T^k(n)=\frac{3^{a_k}n+B_k}{2^k}.
\tag{1}
\]

For \(k=0\), this is \(n=n\).

Assume (1) holds at step \(k\).

If \(t_k=0\), the current value is even, so

\[
T^{k+1}(n)=\frac{T^k(n)}2
=\frac{3^{a_k}n+B_k}{2^{k+1}}.
\]

Here \(a_{k+1}=a_k\) and \(B_{k+1}=B_k\), giving (1) at \(k+1\).

If \(t_k=1\), the current value is odd, so

\[
T^{k+1}(n)
=\frac{3T^k(n)+1}{2}
=\frac{3(3^{a_k}n+B_k)+2^k}{2^{k+1}}.
\]

Here \(a_{k+1}=a_k+1\), while every earlier contribution to \(B_k\) acquires one additional factor of \(3\), and the new odd step contributes \(2^k\). Thus

\[
B_{k+1}=3B_k+2^k,
\]

which is exactly the displayed sum defining \(B_{k+1}\). This proves (1) by induction. Taking \(k=L\) gives the result.

Because \(T^L(n)\) is an integer, the divisibility statement follows immediately. ∎

## Dependency audit

The proof uses only the two branches in the definition of the shortcut map.

## Gap audit

- The theorem assumes that \(w\) is the parity word actually followed by \(n\); it does not claim that every arbitrary word is followed by every integer.
- Bit order is explicitly chronological.
- The statement is finite and does not invoke a limiting parity sequence.
- The formula applies equally to other 2-adic inputs when defined, but this claim is intentionally restricted to ordinary integers.

## Adversarial tests

`experiments/X-0001-collision-enumeration/run.py` evaluates the formula exactly for every residue used in the recorded collision bundles and checks the lifted identities on several values of the free quotient parameter.

Useful hand checks:

- `0`: \(T(n)=n/2\), so \(a=0,B=0\).
- `1`: \(T(n)=(3n+1)/2\), so \(a=1,B=1\).
- `10`: \(T^2(n)=(3n+2)/4\), so \(a=1,B=2\).

## Remaining uncertainty

The author believes the proof is complete. Status remains `PROPOSED` until independent reconstruction under the repository protocol.

## Suggested next attack

Use this formula to classify when several consecutive residues have identical affine images, as done in `T-0001`.
