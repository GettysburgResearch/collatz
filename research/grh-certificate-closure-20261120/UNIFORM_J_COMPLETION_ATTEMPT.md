# Uniform high-exponent rigidity: legal reductions and the remaining bridge

**OPEN overall; scoped elementary deductions below, and one explicitly imported S-unit consequence. No full Collatz proof.**

Source: PR146 at `e238c63a5d57f96bb063b7472498d1977df51951`,
`research/upper-bit-mergers/STABILIZED_CORE_DESCENT.md` and
`ONE_CELL_SIXTY_FOUR.md`. The earlier attempt is PR159 at
`0e7d2841b1591073c6399f91f3b6944ebcdbdbd5`,
`research/allhands-global-closure-20261120/UNIFORM_J_ATTEMPT.md`.

## 1. The two hypotheses must remain distinct

The bare uniform-J problem asks for constancy of a label F on positive
ordinary integers from

- F(2n)=F(3n)=F(n) for all n;
- F(3w+1)=F(w) for every positive odd ternary unit w;
- F(3^j w+1)=F(w) for every positive odd w and j>=J, for one finite J.

The actual finite-exception source additionally supplies the laws at each
fixed j=6,...,10 once w is sufficiently large. This latter property is what
makes its old finite affine descent valid outside a finite initial range,
and hence proves that F has finite image. A global cutoff j>=J, by itself,
does not state that fixed small exponents become legal at large w. No
counterexample to the full bare hypothesis is being asserted; the point is
that this deduction cannot simply be imported with changed quantifiers.

I attempted both the bare problem and repair of the actual finite residual
core. Neither was closed.

## 2. A legal commutator consequence

For j>=J and odd w, set Q=3^(j+1). The high laws and free tripling imply

    F(Qw+1)=F(w)=F(Qw+3).

After dividing by two,

    F((Qw+1)/2)=F((Qw+3)/2).                         (U1)

Thus adjacent equality holds on the complete positive progression
`n=(Q+1)/2 mod Q`. Equivalently, the map n -> 3n-1 preserves F on the
progression `2n=1 mod3^J`, as follows by conjugating multiplication by three
through x -> 3^J x+1 on its legal odd domain.

This does not lower J. The inverse n -> (n+1)/3 reduces the valuation of
2n-1 by one, and can leave the progression on which the high law is legal.
Conjugating multiplication by two is worse: after the first inverse high
move its odd input becomes even, so the next high move is unavailable.
Both losses are integer-domain failures, not omitted simplifications of an
affine identity.

## 3. Eventual periodicity would close the label problem, but finite image does not supply it

**Elementary statement.** If F has the first two laws above and is eventually
periodic, then F is constant. No high law or GRH is needed.

First an eventual period m is a global period. For any n, multiply n and
n+m by a sufficiently large power of two, use the eventual period, and use
F(2^a n)=F(n). If m is divisible by p in {2,3}, then m/p is also a global
period, since

    F(n+m/p)=F(pn+m)=F(pn)=F(n).

Remove all factors 2 and 3, leaving a period q coprime to six. For every
residue a mod q choose an odd ternary unit w with 3w=a mod q. The Chinese
remainder theorem permits this because (q,6)=1. Then

    F(3w+1)=F(w)=F(3w),

so F(a+1)=F(a) on every residue class. Hence F is constant.

The missing claim would be eventual periodicity or an appropriate finite
digit-kernel theorem for the ACTUAL stabilized label. Finite image,
computability, and finite carry descriptions of the elementary arithmetic
maps do not by themselves give that theorem. In particular, the indicator
that n has no prime divisor other than 2 or 3 is computable, finite-valued,
and invariant under multiplication by both 2 and 3. It is not eventually
periodic: an eventual period would become a global period by doubling; its
progression through 1 contains an integer divisible by a prime not dividing
6 times that period. It is only a counterexample to that isolated inference: it does
not satisfy the ordinary odd-unit law (5 maps to 16), and is not a
countermodel to the full rigidity problem.

The finite-state result for bounded odd-rank certificates in PR146 does not
supply finite-state recognition of their unbounded union. No automaticity
assumption has been added to the claimed conclusions.

## 4. An exact obstruction to a one-step inverse repair

A proposed inverse repair starts with a fixed positive odd ternary unit n,
chooses

    x=(2^a n-1)/3=3^(h-1) v,

and wants h>=J and the odd ternary core v<n. This requires the exact equation

    2^a n-3^h v=1.                                  (U2)

Congruence solvability alone does not provide the strict core inequality.
There are elementary fixed-source counterexamples to a uniform one-step
recipe:

- For n=5, a smaller odd ternary core can only be v=1. Equation
  `5*2^a-3^h=1` has the unique solution a=1,h=2. Indeed a>=3 would force
  `3^h=7 mod8`, impossible; the two remaining exponents are checked directly.
  Therefore a repair demanding h>=3 fails already at the convergent source 5.
- For n=7, v can only be 1 or 5. At v=1 the same mod-eight argument leaves
  only a=2,h=3. At v=5, reducing (U2) modulo seven gives h=4 mod6, hence h
  even. If a>=3, reduction modulo eight then gives 0=6, impossible. The
  cases a=1,2 also fail directly. Thus a repair demanding h>=4 fails at 7.

These examples do not refute multistep repairs: 5 and 7 have other ordinary
paths. They rule out exactly the claimed one-step high-valuation descent,
regardless of GRH.

## 5. Bounded inverse depth cannot reach arbitrary high ternary levels with bounded core

**SOURCE-QUALIFIED consequence of the S-unit finiteness theorem.** Fix a
positive odd target n, a finite core bound B, and a finite odd-step budget R.
There are only finitely many positive odd starts x=3^h v with v<=B and
3 not dividing v that reach n in at most R accelerated odd steps.
Consequently h is bounded for this fixed triple (n,B,R).

For an exact positive odd path of r>=1 steps, write its cumulative division
exponents as `0=A_0<A_1<...<A_r=A`. The exact identity is

    2^A n = 3^(r+h) v + sum_{i=0}^{r-1} 3^(r-1-i) 2^A_i.

For fixed r and v, divide by 2^A n. This is an equation with r+1 positive
terms equal to one, with fixed rational coefficients and variables

    3^h 2^-A,  2^(A_0-A), ..., 2^(A_(r-1)-A).

They lie in a finite-rank multiplicative group generated coordinatewise by
2 and 3. Positivity excludes every vanishing proper subsum. The
Evertse--Schlickewei--Schmidt theorem therefore gives only finitely many
such tuples. The coordinate `2^(A_0-A)=2^-A` determines A; the first
coordinate then determines h, and the remaining coordinates determine the
other A_i. Thus the actual exponent data are finite, not merely their
projective ratios. Sum over the finitely many r<=R and v<=B. The case r=0
is a single start x=n.

Primary source: J.-H. Evertse, H. P. Schlickewei and W. M. Schmidt,
*Linear equations in variables which lie in a multiplicative group*,
Annals of Mathematics 155 (2002), 807--836,
https://annals.math.princeton.edu/2002/155-3/p04
and https://arxiv.org/abs/math/0409604.
The external theorem is cited, not reproved or formally rebuilt here.
This consequence does not compute an exhaustive ancestor list or an effective
height cutoff for h. A bound on the number of S-unit solutions does not by
itself locate their exponents; no such effective location bound is claimed.

This explains a concrete resource requirement: any inverse repair that
works for arbitrarily large J while keeping the same input and a smaller
core must allow the inverse odd-step budget to grow with J. GRH does not
remove this unconditional obstruction. The statement does not exclude
unbounded inverse words, forward motion before inverse routing, or a
successful different global argument.

## 6. Bounded shifted-level experiment

I adapted the source's affine search to J=7,8,9, with fixed local limits:
500 heap pops per class, slope cap 10000 times the original modulus,
base modulus 162, and subdivision at most to modulus 81*2^8. This was a
pattern search, not an exhaustive universal decision.

| J | Cells with contracting affine slope | Unresolved terminal cells | Found certificates using a high forward law |
|---|---:|---:|---:|
| 7 | 514 | 388 | 26 |
| 8 | 461 | 458 | 6 |
| 9 | 444 | 480 | 0 |

The search accepts an endpoint a*t+b when a<M. This supplies strict
descent only for t>(b-r)/(M-a), not automatically for every t>=0. Its
nonnegative threshold is max(0,floor((b-r)/(M-a))+1). The particular
43-move sample below does descend for every t>=0.

All cells in the three retained bounded searches were processed; each run
finished in about five seconds, below its twenty-second deadline. No timeout
occurred in these runs. The original exploratory timeout bookkeeping is not
used as evidence for completed coverage of a timed-out search. Unresolved means only that the finite search did not find
a certificate at its limits. It is not evidence of an actual separating label.

One J=8 word yields `F(n)=F((n+1)/16)` on `n=10368t+3823`, with a related
class at residue 7279. Replacing 3^8 symbolically by q changes its proposed
endpoint map to

    (6561/(16q)) n
      + 2187*(12320q^2-102789q-703096443)/(65536q^3).

Although its leading slope contracts for large q, the intermediate inverse
high moves are not legal for arbitrary q=3^J: fixed offsets lose the required
ternary divisibility. Thus this word is not a parametric proof of the uniform
J theorem. I did not promote bounded coverage or a shrinking formal slope
into a full proof.

The search script and raw finite reports are in the same working directory.
No shared source checkout or remote branch was modified by this agent.

## 7. Exact retained interface verifier

`check_rigidity_interfaces.py` is self-contained and imports no PR146 code.
It reads the retained `level8-sample-verification.json`, independently checks
all 43 affine operations on their full nonnegative parameter class, and
reconstructs the complete residue arguments for the one-step sources 5 and 7.
Its failures are explicit and remain active under optimized Python. Three
altered samples (intermediate form, endpoint, and zero exponent) are rejected.

Both normal Python and `-OO` executions completed successfully with byte-identical
reports. The 43-step sample has 25 forward moves and 18 reverse moves, including
two high forwards and three high inverse moves. The report separates the
recorded raw-search provenance hash from the sample actually reread and
verified; it does not authenticate the omitted large raw report by assertion.
No S-unit solver, external theorem rebuild, or universal-J test is implemented.

The exact executed commands and output identity are in
`rigidity_execution_receipt.json`. The retained normal output is
`rigidity-interfaces-report.json`.

## Outcome

The finite exceptional core has not been eliminated. No legal exponent-lowering
word, actual finite-kernel theorem, or unbounded but well-founded inverse
repair was obtained. Sections2--5 isolate valid deductions and exact resource
requirements; none asserts that GRH implies Collatz or that the uniform-J
hypothesis has been established for the actual Collatz labels.
