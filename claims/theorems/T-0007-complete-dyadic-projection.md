# T-0007 — Supercritical collision fibers with complete dyadic projection

Claim ID: `T-0007`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Created: 2026-07-21  
Dependencies: `L-0005`, `L-0009`, `L-0010`, `T-0002`, `T-0005`

## Statement

For every integer \(b\ge1\), there exists a finite supercritical shortcut-Collatz collision fiber whose induced offset alphabet \(D_b\) has exactly \(2^b\) elements and satisfies

\[
\boxed{D_b\bmod2^b=\mathbb Z/2^b\mathbb Z.}
\]

Moreover the fiber may be chosen mildly supercritical, with expansion ratio in

\[
1<\frac NM\le\frac32.
\]

## Construction

For each \(x\in\{0,1\}^b\), form a length-\(2b\), weight-\(b\) word \(u_x\) whose first \(b\) symbols are \(x\), filling the final \(b\) positions with exactly \(b-|x|\) ones.

Apply `L-0009` with precision

\[
p=b+1
\]

and any unit target signature \(C\pmod{3^{b+1}}\). This appends to every \(u_x\) a length

\[
S=2\cdot3^b
\]

weight-one suffix selected individually, producing a collision code

\[
\mathcal C_b=\{w_x:x\in\{0,1\}^b\}
\]

of common length

\[
L_b=2b+2\cdot3^b
\]

and common weight

\[
a_b=b+1.
\]

Finally choose, by the CRT odd-tail construction of `T-0005`, a common output root and append the shortest all-odd tail of length \(k_b\) making

\[
3^{a_b+k_b}>2^{L_b+k_b}.
\]

The resulting finite collision fiber is supercritical, and minimality of \(k_b\) gives expansion ratio at most \(3/2\).

## Proof of complete dyadic projection

Let \(y\) be the common inverse root before the all-odd tail. For each corrected word \(w_x\), the corresponding starting residue is

\[
n_x=\frac{2^{L_b}y-B(w_x)}{3^{a_b}}.
\]

Since \(L_b\ge b\), reduction modulo \(2^b\) gives

\[
n_x\equiv-3^{-a_b}B(w_x)\pmod{2^b}.
\]

The correction suffix begins after position \(2b\), so its contribution to \(B(w_x)\) is divisible by \(2^{2b}\). The concatenation identity therefore yields

\[
B(w_x)\equiv3B(u_x)\pmod{2^b}.
\]

Hence

\[
n_x\equiv-3^{-b}B(u_x)\pmod{2^b}.
\]

Multiplication by the odd unit \(-3^{-b}\) permutes \(\mathbb Z/2^b\mathbb Z\). By `L-0010`, the values \(B(u_x)\pmod{2^b}\) run through every dyadic residue exactly once. Thus the starting residues \(n_x\) do as well.

Translate the finite fiber by its minimum starting residue to obtain the offset alphabet \(D_b\). Translation also permutes the residue classes modulo \(2^b\), so

\[
D_b\bmod2^b=\mathbb Z/2^b\mathbb Z.
\]

The finite common all-odd tail does not change the branch offsets, only the common output and drift. Therefore the final supercritical chart has the claimed complete projection. ∎

## Strategic consequence

This gives closure-relevant geometry that genuinely grows with scale. For every dyadic correction of size less than \(2^b\), some digit difference in the alphabet realizes that correction modulo \(2^b\).

## Gap audit

- Complete modular projection does not itself imply a vertical macro-tile grammar.
- The construction is extremely long: the one-hot correction suffix has length \(2\cdot3^b\).
- No infinite ordinary-integer orbit is claimed.
- A future step must convert modular correction freedom into uniform positive cofactor relays or finite-boundary regeneration.
