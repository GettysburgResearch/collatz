# L-0009 — One-hot suffixes correct arbitrary finite signatures

Claim ID: `L-0009`  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Created: 2026-07-21  
Dependencies: `L-0001`, `L-0005`, `L-0006`

## Statement

Fix a finite family \(\mathcal U\) of binary words of one common length \(L\) and one common weight \(a\). Let \(p\ge a+1\), and put

\[
S=2\cdot3^{p-1}.
\]

For every unit \(C\in(\mathbb Z/3^p\mathbb Z)^\times\), there exists, for each \(u\in\mathcal U\), a unique exponent

\[
0\le j(u)<S
\]

such that, if \(e_j\) denotes the length-\(S\), weight-one word whose unique one occurs at position \(j\), then

\[
B(ue_{j(u)})\equiv C\pmod{3^p}.
\]

Consequently

\[
\mathcal C_C=\{ue_{j(u)}:u\in\mathcal U\}
\]

is a length-\(L+S\), weight-\(a+1\) collision code of precision at least \(p\), and the map \(u\mapsto ue_{j(u)}\) is injective.

## Proof

The concatenation identity gives

\[
B(ue_j)=3B(u)+2^L2^j.
\]

Because \(C\) is a unit modulo \(3\), while \(3B(u)\equiv0\pmod3\), the residue

\[
R_u=(C-3B(u))2^{-L}\pmod{3^p}
\]

is a unit modulo \(3^p\). The element \(2\) generates the unit group modulo \(3^p\), whose order is

\[
\varphi(3^p)=2\cdot3^{p-1}=S.
\]

Therefore there is a unique \(j(u)\in\{0,\ldots,S-1\}\) satisfying

\[
2^{j(u)}\equiv R_u\pmod{3^p}.
\]

Substitution yields the required congruence. All corrected words have common length \(L+S\), common weight \(a+1\), and constants equal modulo \(3^p\). Since \(p\ge a+1\), they form an inverse collision code. Injectivity follows because the original prefix \(u\) remains unchanged. ∎

## Significance

This is a finite signature-completion theorem: **any** fixed-length, fixed-weight prefix family can be converted into one exact collision code without discarding any prefix choices. The correction cost is a long but explicit one-hot suffix.

## Limitations

- The suffix length is exponential in the requested precision.
- The lemma constructs a finite collision code, not an infinite orbit.
- Supercriticality requires a later finite drift tail or another construction.
