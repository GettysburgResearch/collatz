# O-8256 — Exact 512-bit transported closure of the synchronized high sublanguage

**Claim ID:** `O-8256`
**Status:** `PROPOSED`
**Evidence:** exact finite certificate `X-8256`
**Authoring agent:** `gpt56-sol-03`
**Reviewing agents:** none
**Created:** 2026-07-26
**Last updated:** 2026-07-26
**Issue:** #52
**Dependencies:** `L-8251`, `L-8252`, `L-8253`; PR #51 `O-8001` and
`L-8004` for the physical chart; `X-8256` for the exact finite certificate
**Scope:** centered synchronized states with `0<=X_0<2^512` and consecutive
intrinsic labels `s>=44`
**Related counterexample candidates:** none

## Statement

Retain the exact constants

\[
D_9=68\,332\,056\,247,\quad
\omega=37\,933\,813\,917,\quad
a=215\,072\,362,\quad
b=38\,148\,886\,279
\]

and put

\[
W=\omega+D_9X.
\]

For every integer \(s\ge44\), define

\[
h_s=3s+36,\qquad
R_s=2^{h_s},\qquad
M_s=9^{s+9},\qquad
T_s=9^sa-8^sb,
\]

\[
\xi_s=[-T_sM_s^{-1}]_{R_s}.
\]

The partial synchronized branch is

\[
F_s(X)=\frac{M_sX+T_s}{R_s}
\quad\text{when}\quad
X\equiv\xi_s\pmod {R_s}.
\]

There do not exist integers

\[
X_0,X_1,X_2,X_3,X_4
\]

and labels

\[
s_0,s_1,s_2,s_3\ge44
\]

such that

\[
0\le X_0<2^{512},
\qquad
X_{i+1}=F_{s_i}(X_i)
\quad(0\le i<4),
\]

with every label intrinsic:

\[
s_i=\frac{\nu_2(9^9X_i+a)}3.
\]

The bound is sharp in branch depth. There are nonempty length-three
cylinders, and their eighteen branch words are

```text
(44,44,44) (44,44,45) (44,44,46) (44,44,47)
(44,45,44) (44,45,45) (44,45,46)
(44,46,44) (44,47,44)
(45,44,44) (45,44,45) (45,44,46)
(45,45,44) (45,45,45) (45,46,44)
(46,44,44) (46,44,45)
(47,44,44)
```

Every one exits before a fourth label. Thus the maximum number of consecutive
defined synchronized branches with intrinsic labels at least `44`, among
initial centered states below `2^512`, is exactly three.

This is only a bounded synchronized-sublanguage result. It is not a full
Collatz exclusion.

## Definitions

At one branch-prefix node, a transported state

\[
(\theta,K,C,P;Q)
\]

represents exactly

\[
X_0=\theta+Kq,\qquad
X_d=C+Pq,\qquad
0\le q\le Q.
\]

The root is

\[
(\theta,K,C,P;Q)=(0,1,0,1;2^{512}-1).
\]

Because every branch multiplier is odd, `P` remains odd. For a prospective
child label \(s\), define

\[
\rho=[(\xi_s-C)P^{-1}]_{R_s}.
\]

The child is nonempty if and only if \(\rho\le Q\).

An **exit terminal** is a branch word followed by the separate symbol
`EXIT`. It represents the members of that branch cylinder that satisfy no
further high branch. This terminal symbol matters: an internal branch node
can have both continuing subcylinders and members that exit at that prefix.

## Proof and exact computation

### 1. Source constants and branch semantics

`X-8256` rederives

\[
D_9=16^9-9^9,
\qquad
\omega=[-(9^9)^{-1}]_{D_9},
\]

\[
a=\frac{9^9\omega+1}{D_9},
\qquad
b=\frac{16^9\omega+1}{D_9},
\]

and checks

\[
b-a=\omega,
\qquad
2^{36}a-9^9b=1.
\]

For every retained node, both implementations verify

\[
\nu_2(9^9X+a)=3s
\]

and

\[
R_sX'=M_sX+T_s.
\]

They also substitute \(W=\omega+D_9X\) into the `L-8251` source formula

\[
W'=
\frac{9^s(1+9^9W)-2^{3s}}{2^{3s+36}}
\]

and directly replay the physical PR #51 chart:

```text
B: z=1+16q -> 1+9q       (nine times),
A: z=8q    -> 9q         (s times).
```

All 1,935 retained edges pass the intrinsic, centered, raw-source, and
physical checks.

### 2. Exact transported child

Substitute

\[
q=\rho+R_sq'
\]

into the parent state. Then

\[
\theta'=\theta+K\rho,\qquad K'=KR_s,
\]

and

\[
\begin{aligned}
X_{d+1}
&=\frac{M_s(C+P\rho)+T_s}{R_s}+M_sPq'\\
&=C'+P'q'.
\end{aligned}
\]

Hence

\[
C'=\frac{M_s(C+P\rho)+T_s}{R_s},
\qquad
P'=M_sP.
\]

The initial-height cap gives exactly

\[
0\le q'\le
Q'=\left\lfloor\frac{Q-\rho}{R_s}\right\rfloor.
\]

Thus every retained child is exact, and every branch-cylinder intersection
with the parent is retained.

### 3. Complete finite label bound

At every canonical node, \(C\ge0\), \(P>0\), and

\[
Y(q)=9^9(C+Pq)+a>0.
\]

Put

\[
Y_{\max}=9^9(C+PQ)+a
\]

and let \(\beta\) be the unique integer such that

\[
2^\beta\le Y_{\max}<2^{\beta+1}.
\]

The implementation obtains \(\beta\) as
`Y_max.bit_length()-1`, using no floating-point logarithm. If \(s\) is an
intrinsic label, then

\[
2^{3s}\mid Y(q),\qquad Y(q)>0,
\]

so

\[
2^{3s}\le Y(q)\le Y_{\max}.
\]

Therefore

\[
\boxed{s\le\left\lfloor\frac{\beta}{3}\right\rfloor.}
\]

This is a complete finite upper bound at every node. It is `180` at the root
and never exceeds `186` on the retained trie.

For every label from `44` through that bound, oddness of `P` gives exactly one
candidate residue \(\rho\). Testing \(\rho\le Q\) is therefore exhaustive.
No larger label is possible by the displayed inequality.

### 4. Frozen exhaustive trie

The exact computation gives

```text
nodes including root:                1,936
retained edges:                      1,935
candidate labels tested:           269,000
dead-end branch nodes:               1,866
exit terminals:                      1,936
survivor terminals:                      0

depth 0 nodes:                           1
depth 1 nodes:                         116
depth 2 nodes:                       1,801
depth 3 nodes:                          18
```

At every node, the represented seed count is split exactly into:

1. the disjoint retained child-cylinder counts; and
2. the terminal exit count at that prefix.

The resulting words ending in `EXIT` are prefix-free over the augmented
alphabet and their exact counts sum to \(2^{512}\). There is no depth cutoff
and no survivor record. Since all depth-three nodes have no child, no
length-four high word occurs.

The complete states and terminal counts are frozen in
`experiments/X-8256-transported-height-closure/results/exit-trie.json`.

### 5. Independent reconstruction

`verify.py` imports no author-side module. In particular, it:

- computes ordinary inverses by extended Euclid;
- computes inverses modulo powers of two by Newton--Hensel lifting;
- derives \(\xi_s\) from the distinct reset-coordinate expression
  \[
  \xi_s\equiv-a9^{-9}+2^{3s}b9^{-(s+9)}
  \pmod {2^{3s+36}};
  \]
- obtains binary heights by shifts;
- reconstructs every node, edge, terminal count, and physical replay;
- and matches both frozen JSON artifacts exactly.

This completes the finite certificate, subject to ordinary independent review
of the code and source interfaces. ∎

## Motivation

`L-8251`--`L-8253` reduce one constructive Collatz lane to an ordinary
changing-dyadic-cylinder map. The transported representation tests a
substantial initial-height range without enumerating \(2^{512}\) seeds.

The negative result shows that this bounded region cannot contain a
four-block all-high synchronized prefix. It does not address larger ordinary
states and does not turn finite closure into an infinite theorem.

## Dependency audit

1. `L-8251` supplies the synchronized raw boundary formula and
   \(W=\omega+D_9X\).
2. `L-8252` supplies \(R_s,M_s,T_s,\xi_s\) and the centered affine branch.
3. `L-8253` supplies the intrinsic label and an independent reset-coordinate
   expression for \(\xi_s\).
4. PR #51 `O-8001/L-8004` supplies the physical `A/B` chart replay.
5. No external theorem, real approximation, random search, or claim from
   `T-8255` is used.

## Gap audit

This result does **not**:

- exclude an initial centered state \(X_0\ge2^{512}\);
- exclude paths with labels below `44`;
- exclude nonsynchronized chart words;
- classify general positive Collatz trajectories;
- prove that no ordinary synchronized all-time path exists;
- refute any candidate outside the exact bounded language;
- or resolve the Collatz conjecture.

The cap applies only to \(X_0\); later \(X_i\) are not artificially capped.

## Adversarial tests

`test_run.py`:

1. regresses all constants and sampled branch rows against frozen `X-8251`;
2. checks the common 132-bit high prefix from `L-8253`;
3. brute-forces the valuation bound on small affine intervals;
4. compares transport against every quotient in three actual 12-bit tail
   windows;
5. freezes all headline counts and the absence of survivors.

Both full implementations verify the physical/source formula for every
retained node, not merely sampled labels.

## Source correction

At frozen PR #53 head
`8b63eb7dda864430ad64c46ae6f8f58d399ef7b8`,
`experiments/X-8252-bezout-reset/README.md` names an author script, independent
verifier, and canonical result, but those three files are absent; only the
README is present. `X-8256` therefore rederives the reset identities directly
and does not cite a nonexistent X-8252 artifact as verification.

## Remaining uncertainty

The finite arithmetic has two matching standard-library implementations and
frozen exact artifacts, but no separate reviewing agent has yet audited this
claim. The upstream `L-8251`--`L-8253` claims also remain `PROPOSED`.

## Suggested next attack

Repeat the exact transported computation at larger initial-height caps and
study whether the maximum prefix depth admits a proved cap-dependent bound.
Finite experiments at larger heights must remain bounded observations unless
such a uniform argument is supplied.
