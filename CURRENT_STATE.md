# Current integrated state

Last updated: 2026-07-21  
Integrator status: provisional synthesis by `gpt56-pro-01`  
Active issue: `#2`  
Active draft PR: `#3`

## Project maturity

The active branch now contains eleven mathematical research sessions. No claim has received the repository's independent review, so complete-looking finite theorems remain `PROPOSED`.

There is currently **no positive-integer Collatz counterexample**, no regular sanctuary, and no closed counter-stack grammar in the repository.

## Fixed map and exact finite blocks

The shortcut map is

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\[1mm]
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

For a chronological parity word \(w\) of length \(L\) and weight \(a\),

\[
T^L(n)=\frac{3^an+B(w)}{2^L}
\]

on one residue class modulo \(2^L\).

The branch has developed mutually compatible descriptions in terms of:

1. finite collision fibers;
2. induced mixed-radix maps;
3. negative-template return systems;
4. moving negative phases;
5. finite interval and marked-particle lifts;
6. counter-controlled negative-cycle towers.

## Established resources before the latest session

The repository already contains proposed exact results giving:

- sparse and consecutive supercritical collision charts;
- inverse-signature collision codes and exact composition laws;
- exponentially unbounded supercritical branch count;
- arbitrary finite 3-adic precision;
- complete alphabet projection modulo \(2^b\) for every \(b\);
- mixed-radix carry pumping and finite-horizon stacks;
- negative-shadow rational-base returns;
- graph-directed growth and pressure criteria;
- a phase-survival martingale and Doob transform;
- a finite interval lift of every ordinary Collatz orbit;
- a critical particle completion whose distinguished spine is ordinary Collatz;
- a proof that finite-phase regular marked grammars collapse to the regular-sanctuary class already handled by PR #12.

These results remove branch count, finite precision, local expansion, finite-state closure checking, and ordinary-marker semantics as conceptual mysteries. They do not produce one infinite ordinary trajectory.

# Latest session: exact Hensel counter-stack architecture

The literature-informed boundary from PR #13 and PR #12 was enforced strictly: the new work uses an unbounded padding scale and an unbounded ordinary high tail. It is not another finite-state sanctuary in disguise.

## 1. Exact tower replacement

Fix one cycle-padded mismatch type from `T-0015`. Write

\[
k_t=k_0+\ell t,
\qquad
g_t=g_0+at,
\]

and choose the least odd residue \(\mu_t\) satisfying

\[
3^{g_t}\mu_t\equiv-1\pmod{2^{r+1}}.
\]

Define

\[
A_t=2^{k_t}\mu_t,
\qquad
K_t=k_t+r+1,
\]

\[
B_t=3^b\frac{3^{g_t}\mu_t+1}{2^{r+1}},
\qquad
G_t=g_t+b.
\]

`L-0016` proves the exact ordinary-tail identity

\[
\boxed{
A_t+2^{K_t}h
\longmapsto
B_t+3^{G_t}h
}
\]

for every ordinary integer \(h\ge0\). The same finite high tail is preserved while one binary block is replaced by one ternary block.

For the four phase-34 self-return types of the negative eleven-cycle, the finite recovery cores \(\mu_t\) have periods

\[
16,\ 8,\ 4,\ 2.
\]

## 2. Universal canonical connectors

Let a source instance have block data \((A,K,B,G)\) and a target instance have binary anchor \(\bar A\) and depth \(\bar K\). `L-0017` proves that there is one unique canonical tile

\[
\boxed{
B+3^G\eta
=
\bar A+2^{\bar K}\theta
}
\]

with

\[
0\le\eta<2^{\bar K},
\qquad
0\le\theta<3^G.
\]

For every \(z\ge0\),

\[
\eta+2^{\bar K}z
\longmapsto
\theta+3^Gz.
\]

Hence every finite phase-aligned tower schedule has infinitely many ordinary finite realizations. Failure to find a finite connector is never the obstruction.

## 3. What finite or periodic memory cannot do

`L-0018` proves, for odd \(a\),

\[
\operatorname{ord}_{2^K}(3^a)=2^{K-2}.
\]

Therefore no fixed counter period can preserve the inverse-power prefix at growing precision.

`T-0021` proves a stronger all-height obstruction. If tower type, high tail, and affine counter rule

\[
t'=ct+d
\]

are chosen from finite libraries, then exact tower-to-tower transitions occur at only finitely many heights. On a progression freezing the periodic cores, a hypothetical infinite family would solve a nondegenerate power-sum equation

\[
C\alpha^n-E\beta^n+D=0
\]

with multiplicatively independent powers of three and two, contradicting PR #13's imported theorem `LIT-KTHM-0008`.

The padding counter cannot be the sole unbounded memory. The ordinary high tail must carry genuine data.

## 4. Hensel prefix lane

Define

\[
\omega_t=
\frac{\mu_t+3^{-g_t}}{2^{r+1}}
\in\mathbb Z_2.
\]

`L-0019` proves that a requested prefix length \(H\) is preserved by the exact nonlinear jump

\[
\Delta_H=2^{H+r-1}:
\]

\[
\omega_{t+\Delta_H}
\equiv
\omega_t
\pmod{2^H}.
\]

The low connector seed is target-independent:

\[
\eta\equiv-\omega_t\pmod{2^H}
\]

once the target anchor is divisible by \(2^H\).

This gives a genuine append-only Hensel lane, but nested prefixes alone still define a completion object rather than an ordinary starting integer.

## 5. Connector truncation normal form

For a target tower with anchor

\[
\bar A=2^{\bar k}\bar\mu,
\qquad
\bar K=\bar k+\bar r+1,
\]

`L-0022` proves

\[
\boxed{
\eta
=
[\!-\omega_t\!]_{\bar k}
+2^{\bar k}d,
\qquad
0\le d<2^{\bar r+1}.
}
\]

Thus an arbitrarily long connector seed is one source-dependent inverse-prefix stream plus at most six target-control bits. The unbounded target forest collapses to one stack word and bounded finite control.

## 6. One-connector precursor versus true residual stack

`T-0022` and `L-0020`--`L-0021` establish a valid **one-connector precursor**. A 128-step dyadic stage preserves a growing prefix and expands the immediate high-tail height.

However the next connector must also be parsed. If consecutive connector tiles are \((\eta_n,\theta_n)\), the true residual satisfies

\[
\boxed{
 z_{n+1}
=
\frac{3^{G_n}z_n+	heta_n-\eta_{n+1}}
{2^{K_{n+2}}}.
}
\]

The relevant slope is therefore

\[
\frac{3^{G_n}}{2^{K_{n+2}}},
\]

not \(3^{G_n}/2^{K_{n+1}}\).

`T-0023` proves that the 128-step lane eventually contracts this true residual. The corrected lane uses

\[
H(t)=\lfloor\log_2t\rfloor-r-7,
\]

\[
\Delta(t)=2^{\lfloor\log_2t\rfloor-8}.
\]

For all sufficiently large heights,

\[
3^{G_n}>2^{K_{n+2}},
\]

so the residual-stack slope is greater than one.

## 7. Exact 256-step stage

`L-0024` writes the corrected schedule as

\[
t_{m,j}=2^m+j2^{m-8},
\qquad0\le j\le256.
\]

One stage consists of exactly 256 equal counter jumps, followed by scale doubling:

\[
t_{m,256}=t_{m+1,0}.
\]

With

\[
H_m=m-r-7,
\]

the exact odometer law is

\[
\boxed{
\nu_2(\omega_{m,j}-\omega_{m,0})
=H_m+\nu_2(j).
}
\]

The control state is therefore finite: an eight-bit binary odometer over one slowly growing immutable low prefix.

## 8. Periodic frontier and quadratic moving bulk

At dyadic stage boundaries, the four normalized connector frontiers converge to the explicit rational 2-adic values

\[
\frac{19}{243},
\quad
\frac{38}{81},
\quad
\frac{76}{243},
\quad
\frac{638}{729}.
\]

Their connector-prefix streams have exact periods

\[
162,\ 54,\ 162,\ 486.
\]

Thus the stable frontier is finite-state periodic.

`L-0023` isolates the remaining moving bulk. Put

\[
y_m=3^{-7\,2^m},
\qquad
u_m=rac{y_m-1}{2^{m+2}}.
\]

Then \(u_m\) is an odd 2-adic unit and satisfies the exact quadratic recurrence

\[
\boxed{
 u_{m+1}
=u_m+2^{m+1}u_m^2.
}
\]

The full boundary stack therefore has three tracks:

1. a periodic rational frontier;
2. an eight-bit odometer;
3. one quadratic Hensel bulk word.

The recurrence computes the next bulk at every precision already known. It does not by itself generate missing higher bits.

## 9. Exact cycle-margin certificates

`L-0025` proves without decimal approximations that

\[
\boxed{
\frac5{53}
<
7\log_2 3-11
<
\frac4{41}.
}
\]

The proof uses the integer inequalities

\[
3^{53}>2^{84},
\qquad
3^{41}<2^{65}.
\]

These certify simultaneously:

- the one-connector 128-step gain;
- the corrected two-connector 256-step gain;
- the eventual failure of the 128-step residual budget.

## 10. Full-stage information surplus

For one full corrected 256-transition stage, `T-0024` computes the aggregate residual slope exactly. If \(B=2^m\), then

\[
\log_2\Lambda_m
=
\Gamma B+O(1),
\]

with

\[
\Gamma\approx14.2888644
\]

and rigorous lower bound

\[
\Gamma>
\frac{191801}{13568}.
\]

The increase in connector precision from one scale to the next is exactly

\[
\frac{2827}{256}B
\approx11.043B.
\]

After paying this entire cost, the rigorous surplus coefficient is still greater than

\[
\frac{20985}{6784}>3.
\]

Hence one full late stage has exponentially more residual bit-length than the next connector-precision increase consumes.

This removes information supply as the principal scarcity. Large bit-length does not, however, imply the correct low bits.

# Exact computation

`X-0012` independently checks:

- all four tower-core periods;
- binary-to-ternary tail replacement;
- 1,024 canonical connector families and direct two-block replay;
- Hensel prefix preservation and inverse-order obstruction;
- rational frontier periods and fingerprints;
- quadratic bulk recurrence;
- the 128-step precursor and its residual failure;
- the corrected 256-step stage and positive residual slopes;
- the exact stage sums and information-surplus bounds.

The two scripts use exact Python integers, fractions, and the standard library only.

# Central unresolved step

The project still lacks a **finite-boundary regeneration theorem**.

The strongest current state format is

\[
\boxed{
(i,m,j,W,z,n),
}
\]

where:

- \(i\) is one of finitely many tower/mismatch types;
- \(m\) is the unbounded dyadic scale;
- \(j\in\{0,\ldots,255\}\) is the finite odometer state;
- \(W\) is the finite inverse-prefix/quadratic-bulk stack;
- \(z\) is the ordinary residual high tail;
- \(n\) is one explicitly marked ordinary Collatz integer.

The missing theorem must prove one 256-transition stage macro that:

1. routes every exact connector cylinder;
2. updates \(W\) by the quadratic Hensel law and appends new correct bits;
3. keeps the residual recurrence integral and above its growth threshold;
4. transports the marked integer through the deterministic Collatz blocks;
5. returns the same finite syntactic tracks at scale \(m+1\);
6. starts from one finite ordinary state.

The stage has enough growth and information capacity. Exact low-bit routing and ordinary initialization are now the sole load-bearing obstruction.

## Immediate priorities

1. **Stage router.** Convert the 256 exact connector tiles into one proof-producing stack transducer.
2. **Precision spending.** Use part of the stage surplus to compute one longer quadratic-bulk prefix.
3. **Residual congruence.** Prove an invariant ordinary cylinder for the exact \(z\)-recurrence.
4. **Marked replay.** Carry one explicit ordinary marker through every tower block.
5. **Bounded controls.** Compile every finite truncation through `T-0020` and PR #12; only the symbolic all-height proof counts as new progress.
6. **Independent audit.** Reconstruct `L-0016`--`L-0025`, `T-0021`--`T-0024`, `O-0009`, and `X-0012`, paying special attention to the 128-versus-256 correction.