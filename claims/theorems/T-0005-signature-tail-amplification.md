# T-0005 — Signature pigeonhole and odd-tail amplification

Claim ID: `T-0005`  
Title: Exponentially large supercritical collision fibers exist  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `L-0001`, `L-0005`, `T-0002`  
Scope: finite shortcut-Collatz collision fibers  
Related counterexample candidates: none

## Statement

Let \(L\ge1\), \(1\le a\le L\), and \(k\ge1\). Assume

\[
2^k-1>3^a
\tag{1}
\]

and

\[
3^{a+k}>2^{L+k}.
\tag{2}
\]

Then there are an integer \(s\ge0\) and a finite set

\[
\mathcal R\subset\{1,2,\ldots,2^{L+k}-1\}
\]

such that

\[
\boxed{
|\mathcal R|
\ge
\left\lceil\frac{\binom La}{3^a}\right\rceil
}
\tag{3}
\]

and, for every \(q\ge0\) and every \(r\in\mathcal R\),

\[
\boxed{
T^{L+k}(2^{L+k}q+r)
=3^{a+k}q+s.
}
\tag{4}
\]

Thus \(\mathcal R\) is a supercritical collision fiber.

### Exponential family with mild expansion

For \(m\ge1\), let \(k_m\) be the least integer satisfying

\[
3^{m+k_m}>2^{3m+k_m}.
\tag{5}
\]

Then there is a supercritical collision fiber of length

\[
L_m=3m+k_m,
\]

odd count \(a_m=m+k_m\), and cardinality at least

\[
\boxed{
\left\lceil\frac{\binom{3m}{m}}{3^m}\right\rceil.
}
\tag{6}
\]

Its expansion factor obeys

\[
\boxed{
1<\frac{3^{a_m}}{2^{L_m}}\le\frac32.
}
\tag{7}
\]

Moreover,

\[
\frac{\binom{3m}{m}}{3^m}
\sim
\frac{\sqrt3}{2\sqrt{\pi m}}
\left(\frac94\right)^m.
\tag{8}
\]

Consequently, supercritical collision-fiber cardinalities are unbounded and in
fact admit an exponential lower bound, even while the expansion factor is kept
uniformly in \((1,3/2]\).

## Interpretation

This theorem resolves the existence part of `Q-0002` on the active branch.
Large collision alphabets are not exceptional computational accidents.

The proof also establishes a structural decoupling:

- a **subcritical inverse code** supplies many branches;
- a **common odd tail** supplies positive drift;
- the Chinese remainder theorem synchronizes them in one finite ordinary
  construction.

The remaining problem is therefore not alphabet cardinality. It is to obtain
an alphabet with the right arithmetic geometry for finite vertical closure.

## Proof

### Step 1: a large equal-signature class

Let \(\mathcal W_{L,a}\) be the set of all length-\(L\) parity words with
exactly \(a\) ones. For each word define the signature

\[
\sigma(w)
\equiv2^{-L}B(w)\pmod{3^a}
\]

as in `L-0005`. There are \(\binom La\) words and at most \(3^a\) signatures.
Hence some class \(\mathcal C\) satisfies

\[
|\mathcal C|
\ge
\left\lceil\frac{\binom La}{3^a}\right\rceil.
\tag{9}
\]

Fix its common signature \(\sigma\).

### Step 2: synchronize a common all-odd tail

Because \(2^k\) and \(3^a\) are coprime, there is a unique integer

\[
0\le y<2^k3^a
\]

satisfying

\[
y\equiv\sigma\pmod{3^a},
\qquad
y\equiv-1\pmod{2^k}.
\tag{10}
\]

The second congruence writes

\[
y=2^ku-1
\]

for some \(1\le u\le3^a\). In particular,

\[
y\ge2^k-1>3^a.
\tag{11}
\]

For every \(w\in\mathcal C\), define

\[
r_w=\frac{2^Ly-B(w)}{3^a}.
\tag{12}
\]

The signature congruence makes \(r_w\) an integer. By `L-0005`,

\[
0\le B(w)<2^L3^a<2^Ly,
\]

so \(r_w>0\). Also

\[
r_w<\frac{2^L(2^k3^a)}{3^a}=2^{L+k}.
\tag{13}
\]

Again by `L-0005`, \(r_w\) follows \(w\) for \(L\) steps and reaches \(y\).
The congruence \(y\equiv-1\pmod{2^k}\) then forces \(k\) consecutive odd steps,
ending at

\[
s=3^ku-1.
\tag{14}
\]

Thus every \(r_w\) has total parity word

\[
w1^k,
\]

of length \(L+k\) and weight \(a+k\), and every one reaches the same \(s\).
Distinct words give distinct residues because finite parity words have unique
residues modulo \(2^{L+k}\).

Adding \(2^{L+k}q\) preserves the total parity word. The affine formula
`L-0001` therefore gives

\[
T^{L+k}(2^{L+k}q+r_w)=3^{a+k}q+s,
\]

which proves (3) and (4). Condition (2) makes the fiber supercritical.

### Step 3: the family \(L=3m\), \(a=m\)

At \(k=2m\),

\[
3^{m+2m}=27^m<32^m=2^{3m+2m}.
\]

Therefore the least supercritical tail satisfies

\[
k_m\ge2m+1.
\]

It follows that

\[
2^{k_m}-1\ge2^{2m+1}-1>3^m,
\]

so condition (1) holds. Applying the first part gives (6).

Minimality of \(k_m\) says that the expansion factor at \(k_m-1\) is at most
one. Increasing the tail by one multiplies that factor by \(3/2\), proving
(7).

Finally, Stirling's formula gives

\[
\binom{3m}{m}
\sim
\frac{\sqrt3}{2\sqrt{\pi m}}
\left(\frac{27}{4}\right)^m.
\]

Dividing by \(3^m\) yields (8). ∎

## Dependency audit

- `L-0005` supplies the inverse-signature criterion, the bound on \(B(w)\),
  and the exact all-odd tail.
- `L-0001` supplies the lifted identity for all \(q\ge0\).
- `T-0002` converts any selected fiber into an induced partial radix map, but
  is not needed for the finite existence proof itself.
- The only existence mechanism is finite pigeonhole plus finite CRT.

## Gap audit

- The theorem proves large finite collision fibers, not one infinite induced
  orbit.
- The selected signature class may be arithmetically unstructured. Cardinality
  alone does not imply a regenerative carry grammar.
- No inverse limit, compactness argument, or infinite parity string is used.
- The expansion factor is controlled, but the lifting modulus and digit geometry
  still require study.

## Adversarial tests

`X-0003` constructs the largest signature classes for \(1\le m\le8\), verifies
every selected inverse trajectory and odd tail, and checks the lifted collision
identities on several values of \(q\).

## Remaining uncertainty

The author believes the theorem is complete. It awaits independent
reconstruction.

## Suggested next attack

Replace the flat pigeonhole objective by a structured-code objective: force
complete residue projections, long difference intervals, or tensorable
precision surplus while retaining the mild-expansion tail.
