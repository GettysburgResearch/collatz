# L-0105 — Odd-multiplier thinning for power-of-two image ports

Claim ID: `L-0105`  
Title: Every power-of-two image-port constraint thins the parameter lattice by the full modulus  
Status: `PROPOSED`  
Authoring agent: `grok45-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: `D-0101`  
Scope: accelerated blocks with destination constraints modulo powers of two  
Related counterexample candidates: none (obstruction)

## Statement

Let \(w\) be a chronological parity word of length \(L\) and odd-weight \(a\ge0\),
with

\[
T^L(2^L q+r)=3^a q+s
\]

for all integers \(q\) in the native domain. Fix \(L'\ge1\) and a residue
\(r'\pmod{2^{L'}}\). Then the set of parameters \(q\) for which the image lies
in the port \(2^{L'}\mathbb Z+r'\) is either empty or a single residue class
modulo \(2^{L'}\). In particular it is never a cofinite subset of the native
parameter line, and never the full native parameter line.

Equivalently: there is no accelerated Collatz block whose image arithmetic
progression is contained, for all native \(q\), in a single residue class
modulo \(2^{L'}\) with \(L'\ge1\).

### Nested-walk form (corrected)

Suppose an ordinary integer \(n_0\) realizes a finite walk of block transitions
in which the \(i\)-th successful transition imposes an image-port constraint of
modulus \(2^{L_i'}\) with \(L_i'\ge1\), and these constraints are expressed as
compatible congruences

\[
n_0\equiv a_N\pmod{2^{m_N}}
\]

with \(m_N=\sum_{i\le N}L_i'\to\infty\) along an infinite walk. Then there is
**at most one** 2-adic integer satisfying all the congruences. That 2-adic
integer lies in \(\mathbb Z_{>0}\) if and only if the nested classes have
nonempty intersection inside the positive integers.

In the special case of a fixed residue tower

\[
n_0\in\bigcap_{N\ge1}\bigl(2^{m_N}\mathbb Z+a\bigr)
\]

with the same \(a\) and \(m_N\to\infty\), the integer intersection is \(\{a\}\)
or empty. Thus no ordinary integer other than (possibly) \(a\) itself can
sustain infinitely many such tower constraints.

Clarification relative to the first draft of this lemma: an ordinary integer
**does** have residues modulo every \(2^k\). The obstruction is not “integers
have only finitely many bits”; it is that an infinite nested family of
**proper** constraints determines at most one 2-adic point, which need not be
a positive ordinary integer (and in the expanding periodic cases is the
negative rational fixed point — see `L-0107`).

## Definitions

Native domain: \(n=2^Lq+r\) with \(r=r(w)\). Image port: the condition
\(T^L(n)\equiv r'\pmod{2^{L'}}\).

## Motivation

General precision-drain for the pure power-of-two port calculus in `D-0102`.
Explains `L-0104` and feeds `L-0106`–`L-0107`.

## Proof

The image-port condition is

\[
3^a q+s\equiv r'\pmod{2^{L'}}
\iff
3^a q\equiv r'-s\pmod{2^{L'}}.
\]

The multiplier \(3^a\) is odd, hence a unit in \(\mathbb Z/2^{L'}\mathbb Z\).
Therefore the congruence has either no solution or exactly one solution class
modulo \(2^{L'}\).

For the nested-walk form: each successful constraint appends a compatible
congruence modulo a higher power of two (after transporting parameters by
odd units / CRT). The inverse limit of a compatible sequence of residues
modulo \(2^{m_N}\) with \(m_N\to\infty\) is a single 2-adic integer. For a
constant-residue tower, if \(n\in\mathbb Z\) satisfies \(n\equiv a\pmod{2^{m_N}}\)
for all \(N\), then \(2^{m_N}\mid(n-a)\) for all \(N\), hence \(n=a\).

## Dependency audit

- Affine block formula: `D-0101`.
- Units modulo \(2^{L'}\): elementary number theory.

## Gap audit

- Does not forbid destination ports of odd modulus.
- Does not by itself identify the unique 2-adic point; `L-0107` does so for
  expanding periodic schedules.
- First-draft wording that “ordinary integers cannot satisfy unbounded nested
  congruences” was incorrect and is replaced by the inverse-limit statement
  above.

## Adversarial tests

- Special case `L-0104`: \(L'=7\), multiplier \(243\equiv115\pmod{128}\) unit.
- `X-0110`: tax tables and \(\bigcap_N(2^{7N}\mathbb Z+47)=\{47\}\).

## Remaining uncertainty

Low for the single-transition and constant-tower statements.

## Suggested next attack

See `L-0106` (budget) and `L-0107` (periodic expanding realizations).
