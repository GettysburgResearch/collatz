# Exhausting the expansion budget does not force a paying exit

**Status: the generic nonpayment theorem and an actual eight-block witness
are kernel-checked; the all-length ordinary existence construction below
is a written proof. They refute the proposed first-exit height-payment
rule. They are not Collatz counterexamples.**

The positive charged theorem permits k expanding blocks followed by the
contracting P1 return when its parameter r is at least k. The attempted
closing step was to deduce adequate repayment from the fact that the
expanding block cannot repeat forever at one fixed ordinary source.
This implication is false, even if the first exit is itself a P1 return.

## Statement

For every integer k>=8 there is an entire arithmetic progression of positive
ordinary sources with the following itinerary:

1. Apply the actual 22-step expanding return exactly k times.
2. Leave its source cylinder; the new base is 2 modulo 8.
3. Apply P1 with r=0, a genuine three-step paired contraction.

The final base u is **larger than the initial base m**. The paired relation
is restored at clock 22k+3, and each arm has exactly 14k+1 odd inputs.
The initial expansion charge has exactly 22k factors of two, so its entire
binary budget was consumed before this nonpaying exit.

This is the first exit of the specified rule that repeatedly applies this
22-step block while its guard holds. The statement does not exclude other
orientation-changing opportunities inside a block or a later successful
return.

## Complete ordinary construction

Set

\[
D=2^{22},\qquad P=3^{14},\qquad B=6867833,\qquad
F(x)=\frac{Px+B}{D}.
\]

The proved expanding cylinder is

\[
x=2469887+Dt,\qquad F(x)=2816534+Pt,\qquad t\ge0.
\]

For k>=1 define the positive integer

\[
C_k=B\sum_{i=0}^{k-1}P^{k-1-i}D^i.
\]

Then formal affine composition gives

\[
F^k(x)=\frac{P^kx+C_k}{D^k}.
\]

Because P and D are coprime, there is a unique residue
\(R_k\in\{0,\ldots,D^k-1\}\) such that

\[
P^kR_k+C_k\equiv0\pmod{D^k}.
\]

Put \(Q_k=(P^kR_k+C_k)/D^k\). For every natural t,

\[
m=R_k+D^kt,\qquad q=Q_k+P^kt
\]

satisfy the final affine equation. Here every intermediate step is legal,
as follows; final integrality is not being substituted for an unproved
ordinary guard.

### Final integrality forces every cylinder guard

For k>=1,

\[
P^km+C_k\equiv P^{k-1}(Pm+B)\pmod D.
\]

Since P is invertible modulo D, the final integral equation forces
\(D\mid Pm+B\). The unique source residue modulo D is 2469887, since
\(P\cdot2469887+B=D\cdot2816534\). Hence
\(m=2469887+Dt_0\) with \(t_0\ge0\).

The first step is therefore the actual proved expanding return. Its
endpoint is an integer and is larger than m. Cancel its factor D in the
remaining affine equation and repeat the argument. Induction gives all k
ordinary guards, all intermediate positivity, and the literal paired
trajectories. In particular \(R_k\ge2469887\); no zero or negative source
is introduced.

### Select an exact r=0 exit

P is odd, so there is a unique \(t_k\in\{0,\ldots,7\}\) such that

\[
Q_k+P^kt_k\equiv2\pmod8.
\]

For every natural s choose \(t=t_k+8s\). Then

\[
m=M_k+8D^ks,\quad M_k=R_k+D^kt_k,\qquad
q=Q_k+P^kt_k+8P^ks\equiv2\pmod8.
\]

The even q is outside the odd expanding source cylinder, so exactly k
consecutive expansions have occurred. Define

\[
v=\frac{3q-2}{4},\qquad u=\frac{3q+2}{8}.
\]

Both are positive integers, and v is odd. The two P1 guards hold with r=0:
\(3q=4v+2\) and \(2u=v+1\). Thus the next three actual shortcut steps send
\((q,3q-1)\) to \((u,3u-1)\). As s varies, the final base is
\(u=U_k+3P^ks\), where \(U_k=(3(Q_k+P^kt_k)+2)/8\).

### Net increase for every k>=8

Combining the two affine equations gives

\[
8D^k(u-m)
=(3P^k-8D^k)m+3C_k+2D^k.
\]

The exact base inequality is

\[
3P^8>8D^8,\qquad\text{equivalently }3^{113}>2^{179}.
\]

Since P>D, it follows that \(3P^k>8D^k\) for all k>=8. Every term in the
displayed difference is positive or nonnegative, with a positive constant
term. Hence u>m for every source in every displayed progression.

### The initial charge is exactly exhausted

The already proved charge identity is

\[
D^kE(q)=P^kE(m),\qquad E(x)=588665x+6867833.
\]

Since q is even, E(q) is odd. Since P is odd and D=2^22,

\[
v_2(E(m))=22k.
\]

The nonpayment does not come from leaving unused binary charge in this
run. The exit changes the arithmetic accounting.

## Exact control at k=8

The construction gives

```text
m = 41810139432818474717192283295425337283325624618168319
q = 119559174457862734611245204856814189553032133689548890
u = 44834690421698525479216951821305321082387050133580834
```

An exact integer replay gives both paired endpoints at clock 179, with
113 odd inputs on each arm and u>m. Lean independently checks all eight
literal cylinder guards and the complete paired profile. The whole progression has source
stride \(2^{179}\) and endpoint stride \(3^{113}\). This finite control
checks the displayed constants; the all-k proof is the construction above.

## Scope of the failed global inference

This refutes a specific way to complete the charged descent argument:
finite expansion escape does not imply ordinary-height payment at the
first following P1 return. It does not refute a certificate-length rank,
the mixed multiset order of PR176, a later return, or an argument exploiting
least-defect hypotheses that these ordinary families do not assume.

## Formalization boundary

[UnpaidExit.lean](../lean/Closure/UnpaidExit.lean) proves:

- `expansion_chain_growth`: every actual chain satisfies
  \(P^km\le D^kq\).
- `expansion_multiplier_gap`: \(8D^k<3P^k\) for every \(k\ge8\).
- `unpaid_exit`: any actual guarded chain with \(k\ge8\) and
  \(8u=3q+2\) has \(m<u\).
- `unpaid_paired_return`: the actual clock \(22k+3\), equal odd counts
  \(14k+1\), and strict increase follow from those same hypotheses.
- `concrete_eight_chain` and `concrete_unpaid_return`: the displayed
  witness has all eight exact cylinder guards and its literal paired
  endpoint at clock 179. The chain declaration has no axiom dependencies.

The all-k existence construction uses ordinary modular arithmetic in the
written proof. It is not a Lean CRT existence theorem in this packet.
No universal convergence or divergence assertion follows from these examples.
