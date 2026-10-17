# T-0022 — Hensel prefix preservation is compatible with tail expansion

Claim ID: `T-0022`  
Title: Logarithmic Hensel-budget schedules for supercritical negative-cycle towers  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-01`  
Reviewing agents: none yet  
Created: 2026-07-21  
Dependencies: `L-0017`, `L-0019`  
Scope: one fixed self-return tower type on a supercritical negative cycle  
Related counterexample candidates: none

## Statement

Fix one self-return tower type from `L-0016` on a negative cycle of period \(\ell\) and odd count \(a\). Write

\[
K_t=\ell t+K_*,
\qquad
G_t=at+G_*.
\tag{1}
\]

The negative-cycle multiplier is supercritical:

\[
\frac{3^a}{2^\ell}>1.
\]

Put

\[
\boxed{
\sigma=a\log_2 3-\ell>0.
}
\tag{2}
\]

Let \(r\) be the fixed recovery depth of the tower type. Choose an integer \(C\ge1\) satisfying

\[
\boxed{
\frac{\ell}{2^C}<\sigma.
}
\tag{3}
\]

For all sufficiently large \(t\), define

\[
H(t)=\left\lfloor\log_2 t\right\rfloor-C-r+1,
\tag{4}
\]

\[
\Delta(t)=2^{H(t)+r-1}
=2^{\lfloor\log_2t\rfloor-C},
\tag{5}
\]

and

\[
t^+=t+\Delta(t).
\tag{6}
\]

Then:

### 1. Exact Hensel prefix preservation

Let \(\eta(t,t^+)\) be the canonical connector seed from tower instance \(t\) to tower instance \(t^+\). Let \(\omega_t\) be the normalized prefix of `L-0019`.

For all sufficiently large \(t\),

\[
\boxed{
\eta(t,t^+)
\equiv
-\omega_t
\pmod{2^{H(t)}}.
}
\tag{7}

If the schedule is iterated,

\[
t_{n+1}=t_n+\Delta(t_n),
\tag{8}
\]

and \(\eta_n=\eta(t_n,t_{n+1})\), then

\[
\boxed{
\eta_{n+1}\equiv\eta_n\pmod{2^{H(t_n)}}.
}
\tag{9}

The actual connector seeds therefore possess a nested LSD-first prefix whose certified length tends to infinity.

### 2. Positive free-tail budget

The connector tile from \(t\) to \(t^+\) acts on the free tail as

\[
\eta+2^{K_{t^+}}z
\longmapsto
\theta+3^{G_t}z.
\tag{10}
\]

For all sufficiently large \(t\),

\[
\boxed{
3^{G_t}>2^{K_{t^+}}.
}
\tag{11}
\]

Thus its affine free-tail slope

\[
\boxed{
\lambda_{\rm tail}(t)
=
\frac{3^{G_t}}{2^{K_{t^+}}}
}
\tag{12}
\]

is greater than one. For every such connector there is an explicit finite threshold

\[
Z_t=
\max\left\{
0,
\left\lfloor
\frac{\eta-\theta}{3^{G_t}-2^{K_{t^+}}}
\right\rfloor+1
\right\}
\tag{13}
\]

such that its output high tail exceeds its input high tail whenever \(z\ge Z_t\).

### 3. The schedule is genuinely all-height

For large \(t\),

\[
\frac{t}{2^{C+1}}<\Delta(t)\le\frac{t}{2^C}.
\tag{14}
\]

Consequently the recursive schedule (8) satisfies

\[
t_n\to\infty,
\qquad
H(t_n)\to\infty.
\tag{15}

It is nonlinear and is not covered by the affine-counter obstruction `T-0021`.

### 4. Logarithmic precision ceiling

Conversely, suppose an order-sized Hensel jump

\[
t^+=t+2^{H+r-1}
\tag{16}
\]

has noncontracting free-tail slope:

\[
3^{G_t}\ge2^{K_{t^+}}.
\tag{17}
\]

Then

\[
\boxed{
2^{H+r-1}
\le
\frac{\sigma t+G_*\log_2 3-K_*}{\ell}.
}
\tag{18}
\]

In particular,

\[
\boxed{H\le\log_2t+O(1).}
\tag{19}
\]

The Hensel-stable prefix can grow without bound, but only logarithmically in the linear tower depth \(K_t=\Theta(t)\). No tail-expanding order-sized jump can freeze a positive fraction of the full connector word.

## Proof

Equation (5) gives the exact order-sized jump of `L-0019` at precision \(H(t)\). Therefore

\[
\omega_{t^+}\equiv\omega_t\pmod{2^{H(t)}}.
\tag{20}
\]

For sufficiently large \(t\), both target anchors in the connectors beginning at \(t\) and \(t^+\) are divisible by \(2^{H(t)}\). Part 2 of `L-0019` therefore gives

\[
\eta_n\equiv-\omega_{t_n}\pmod{2^{H(t_n)}}
\]

and

\[
\eta_{n+1}\equiv-\omega_{t_{n+1}}\pmod{2^{H(t_n)}}.
\]

Together with (20), this proves (7)--(9). The function \(H(t)\) is nondecreasing, so the certified prefixes are nested.

For the tail budget, calculate

\[
\begin{aligned}
\log_2\lambda_{\rm tail}(t)
&=G_t\log_2 3-K_{t^+}\\
&=(at+G_*)\log_2 3
  -\ell(t+\Delta(t))-K_*\\
&=\sigma t-\ell\Delta(t)
  +G_*\log_2 3-K_*.
\end{aligned}
\tag{21}
\]

By (5),

\[
\Delta(t)\le\frac{t}{2^C}.
\]

Hence

\[
\log_2\lambda_{\rm tail}(t)
\ge
\left(\sigma-\frac{\ell}{2^C}\right)t
+G_*\log_2 3-K_*.
\tag{22}
\]

The coefficient of \(t\) is positive by (3), so the right side is positive for all sufficiently large \(t\). This proves (11)--(12).

Using the connector formulas

\[
h=\eta+2^{K_{t^+}}z,
\qquad
h'=\theta+3^{G_t}z,
\]

we have

\[
h'-h
=
(3^{G_t}-2^{K_{t^+}})z+\theta-\eta.
\]

The displayed threshold (13) makes this positive.

If \(2^m\le t<2^{m+1}\), then

\[
\Delta(t)=2^{m-C}.
\]

This gives (14). Therefore \(t_n\) increases by a positive fraction of itself, tends to infinity, and forces \(H(t_n)\to\infty\).

Finally, assumption (17) is equivalent to

\[
0\le
\log_2\lambda_{\rm tail}(t)
=
\sigma t
-\ell2^{H+r-1}
+G_*\log_2 3-K_*.
\]

Rearranging gives (18), and taking logarithms yields (19). ∎

## Negative eleven-cycle parameters

For the four self-return tower types at phase \(-34\),

\[
\ell=11,
\qquad
a=7,
\]

and

\[
\sigma=7\log_2 3-11\approx0.0947375.
\]

The smallest integer satisfying (3) is

\[
\boxed{C=7,}
\]

because

\[
11/128<\sigma<11/64.
\]

Thus one concrete viable schedule is

\[
H(t)=\lfloor\log_2t\rfloor-r-6,
\]

\[
\Delta(t)=2^{\lfloor\log_2t\rfloor-7}.
\]

It preserves a growing connector prefix and has positive free-tail slope after a finite type-dependent threshold.

## Interpretation

This theorem identifies a real construction window between two earlier obstructions.

- Fixed-period control fails by `L-0018`.
- Fixed affine counter lanes with bounded tails fail by `T-0021`.
- Exact multiplicative-order jumps can nevertheless preserve a growing prefix while the negative cycle's real expansion pays for the next binary cylinder.

The balance is tight. The tower's per-cycle gain

\[
\sigma=a\log_2 3-\ell
\]

is the number of new binary stack bits available per padding circuit. The Hensel jump consumes \(\ell\Delta\) bits of future cylinder depth. The inequality

\[
\sigma t>\ell\Delta
\]

is the exact stack-fuel budget.

## What remains

The nested prefix in (9) still naturally determines a 2-adic limit. Positive free-tail slope proves that a sufficiently large *already available* tail grows; it does not generate the missing tail from one finite starting word.

The next theorem must make the finite stack rewrite self-reproducing:

\[
\eta_n+2^{K_{n+1}}z_n
\longmapsto
\theta_n+3^{G_n}z_n
=
\eta_{n+1}+2^{K_{n+2}}z_{n+1}
\]

with \(z_{n+1}\) carrying a larger certified copy of the same finite stack schema.

## Dependency audit

- `L-0019` supplies the Hensel prefix identity.
- `L-0017` supplies the exact connector tail map and canonical bounds.
- The growth calculation is elementary.
- No probabilistic or compactness existence statement is used.

## Gap audit

- A nested sequence of connector prefixes is still not one ordinary integer.
- The theorem does not construct compatible finite \(z_n\) for all stages.
- The threshold \(Z_t\) depends on the full connector seed and is not yet closed under one finite schema.
- Positive tail slope is a resource, not a counterexample.

## Adversarial tests

`X-0012` verifies the concrete \(C=7\) schedule for all four phase-34 self-return types across a finite range of large tower heights, checks exact prefix nesting, and compares the integer powers in (11) directly.

## Suggested next attack

Use the canonical ternary cap \(0\le\theta_n<3^{G_n}\) as an emitted stack symbol and search for a finite pushdown relation that parses

\[
\theta_n+3^{G_n}z_n
\]

into the next binary prefix plus a larger tail. Every bounded stack-height truncation should be compiled through `T-0020` and rejected or certified by PR #12.