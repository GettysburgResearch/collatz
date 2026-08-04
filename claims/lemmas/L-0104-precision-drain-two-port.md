# L-0104 — Precision drain on the expanding pair `1111010` / `1101110`

Claim ID: `L-0104`  
Title: Exact 2-adic precision drain for a mildly supercritical two-port block pair  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`  
Scope: the explicit words \(w_1=1111010\), \(w_2=1101110\) and their concatenations  
Related counterexample candidates: none (obstruction / cautionary exact example)

## Statement

Let

\[
w_1=1111010,\qquad w_2=1101110.
\]

Each has length \(L=7\), odd-weight \(a=5\), and forward slope

\[
\mu=\frac{3^5}{2^7}=\frac{243}{128}>1.
\]

Their native residues and outputs under \(T^7\) are

\[
r(w_1)=47,\quad T^7(47)=91=r(w_2),
\qquad
r(w_2)=91,\quad T^7(91)=175.
\]

On the arithmetic progression \(n=128q+47\),

\[
T^7(n)=243q+91.
\]

This image lies in the native port of \(w_2\) (i.e. \(\equiv 91\pmod{128}\)) if and
only if

\[
115q\equiv0\pmod{128}.
\]

Since \(\gcd(115,128)=1\), this holds if and only if \(128\mid q\). Thus every
successful \(w_1\to w_2\) transition forces a jump of modulus from \(2^7\) to
\(2^{14}\):

\[
n=2^{14}u+47.
\]

An analogous congruence for the return transition \(w_2\to w_1\) on the image
progression again forces a further factor \(2^7\) in the modulus. Therefore any
ordinary positive integer can realize at most finitely many alternations of
\((w_1,w_2)\); the required 2-adic precision grows by \(7\) bits per successful
leg.

In particular, the expanding symbolic 2-cycle detected by `X-0106` is **not**
an integer Schottky certificate.

## Definitions

Ports and affine block maps as in `D-0101` / `D-0102`.

## Motivation

This is the ping-pong packet’s concrete avatar of the finite-versus-adic
closure gap: local expansion and modular handshakes are abundant; infinite
ordinary-integer walks are not, because each handshake drains precision.

## Proof

The residues, outputs, and affine formulae are verified by direct computation
(`X-0106`, and the adversarial tests below). The congruence

\[
243q+91\equiv91\pmod{128}
\iff
243q\equiv0\pmod{128}
\iff
115q\equiv0\pmod{128}
\]

is elementary. Invertibility of \(115\) modulo \(128\) follows from oddness.
Hence \(q\equiv0\pmod{128}\).

Now restrict to \(q=128u\), so \(n=2^{14}u+47\) and

\[
T^7(n)=243\cdot128u+91=2^{14}\cdot\frac{243}{128}\cdot 128u+91=243\cdot2^{7}u+91.
\]

Apply \(w_2\): the condition that the image lie in a chosen return port of
modulus \(2^7\) is again a linear congruence \(A u\equiv b\pmod{128}\) with
\(A\) odd, hence either impossible or a full-index sublattice \(u\in128\mathbb Z+u_0\).
In the `X-0106` concatenation orientation, explicit search shows the maximal
number of exact concatenated periods on seeds \(2^{14}q+47\) with
\(q<50000\) is \(2\) (`O-0101`). Combined with the forced index-\(128\) thinning
at each successful leg, no infinite ordinary alternation exists.

(The “at most finite” claim for any single integer also follows without search:
an infinite successful alternation would require \(n\) to satisfy congruence
conditions modulo \(2^{7N}\) for all \(N\), hence \(n\) would be determined as a
2-adic limit point; an ordinary integer has only finite 2-valuation of
\(n-r\) relative to any fixed residue tower depth.)

## Dependency audit

- Affine formula: `D-0101`.
- Explicit arithmetic: self-contained.
- Empirical period bound: `X-0106` / `O-0101` (used only as illustration; the
  finiteness argument via unbounded modulus demand does not need the search).

## Gap audit

- The lemma is for one explicit pair, not for all expanding two-port pairs.
- A general precision-drain theorem for all odd-slope transitions is stated as
  `C-0102` (conjectural / to be proved).
- Does not rule out aperiodic automata with compensating precision-creating
  mechanisms (if any exist).

## Adversarial tests

```text
python3 experiments/X-0106-schottky-automaton/run.py
# exposes symbolic cycle words=['1111010','1101110'] prod=59049/16384

# Direct checks:
residue(1111010)=47, T^7(47)=91
residue(1101110)=91
max concat periods for n=2^14 q+47, q<50000: 2
```

## Remaining uncertainty

Low for this pair. Generality is the open part.

## Suggested next attack

Prove `C-0102`: any transition between pure power-of-two ports whose
multiplier is odd forces finite-index thinning, and an infinite walk therefore
demands unbounded modulus unless a precision-regeneration gadget exists.
