# R-6915 — The irreducible full-denominator obstruction is cross-factor synchronization

**Claim ID:** `R-6915`  
**Status:** **PROPOSED METHOD BOUNDARY / EXACT FINITE COUNTERTEST**  
**Authoring agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Created:** 2026-08-01  
**Issue:** #75  
**Dependencies:** `L-6912`, `L-6913`, `T-6914`, `X-6912`; latest PR #81 state  
**Scope:** the attempted proof of FC*

## 1. Attempted local theorem

A natural hoped-for closure was:

> for every nontrivial first-crossing word, one complete prime-power factor
> `M|D` already has `M>A_w/2^j` and
> \[
> [A_w3^{-q}]_M\ge A_w/2^j.
> \]

Such a factor would reject the short common displacement without any CRT
coupling.

This statement is false.

## 2. First exact failure at length 27

`X-6912` exhausts every first-crossing word through length `27`. There are

```text
502,523 first-crossing words;
0 nontrivial canonical failures.
```

For every valid length below `27`, every word is rejected by one complete
prime-power factor.

At

\[
j=27,\qquad q=17,\qquad
D=2^{27}-3^{17}
=5\cdot71\cdot14303,
\]

exactly three descending words evade every individual prime-power witness.

Their local displacement residues are:

```text
111010111011101010101101100
  mod 5,71,14303: 1,2,2
  threshold A/2^27 = 368971243/134217728
  block 5*71 gives residue 286 and rejects.

111011011100111111101010000
  mod 5,71,14303: 0,0,1
  threshold A/2^27 = 264503755/134217728
  block 5*14303 gives residue 42910 and rejects.

111110011111010100011011010
  mod 5,71,14303: 2,0,0
  threshold A/2^27 = 352383011/134217728
  block 5*71 gives residue 142 and rejects.
```

Thus a CRT combination of two factors can be decisive even when every
individual factor returns a residue inside the bad interval.

The experiment is a regression test, not an all-length proof.

## 3. Consequence for proof architecture

The exact countertest rules out any proof that treats the complete
prime-power equations independently and then applies only one-factor size
bounds.

The local equations must be coupled through the common ordinary `d`.
`L-6912` identifies two exhaustive cofinal architectures once the denominator
is larger than the cube of the ordinary endpoint bound.

### Balanced synchronization

Two complementary large unitary blocks must produce exactly the same small
displacement and the same quotient jet.

### Dominant prime power

One giant prime power determines the small source, endpoint, and displacement;
one remaining small cofactor must complete the divisibility.

No theorem currently in PR #81 or PR #83 forces a contradiction in either
architecture.

## 4. Why the existing global constraints do not close the jets

Every surviving acyclic family is already:

```text
polynomially sparse across words;
square-root-supported relative to mechanical;
two-thirds-scale in integrated displacement;
early departing from the mechanical prefix;
early departing from its own tail after the near-return;
complete across every prime-power factor.
```

These facts constrain the exponent path and the number of candidate tuples.
They do not determine the least CRT representative of the lacunary sum in
`L-6913`.

In particular:

- zero family entropy does not imply equidistribution or residue avoidance;
- square-root support does not force two factor residues to differ;
- an order cover reconstructs the word but does not certify omitted factors;
- a product formula based only on degree and height is too coarse for the
  growing-support Laurent sum;
- the cycle level `d=0` is the same synchronization problem at residue zero.

## 5. Smallest exact obstruction remaining

After all current reductions, FC* is equivalent to excluding both of the
following complete objects.

### Object B — balanced two-block jet

\[
D=UV,\qquad U,V>\mathcal B_j,
\]

with

\[
\delta_U=\delta_V=d,\qquad
\sigma_U=\sigma_V=s,
\]

and

\[
0\le d<A_w/2^j,\qquad
0<s<\mathcal B_j,\qquad
r=s-d>0.
\]

### Object G — dominant giant-factor jet

\[
D=Wc,\qquad c\le\mathcal B_j,\qquad W>\mathcal B_j^2,
\]

where the giant factor returns small `d,r,s` and

\[
c\mid\frac{A_w-3^q d}{W}.
\]

Both objects retain every first-crossing, wrap, roughness, and physical replay
condition from PR #81.

A proof that neither object exists would establish FC*, including positive
cycles. The present packet does not supply that final exclusion.

## 6. Resultant restatement

When `gcd(j,q)=1`, both objects are equivalent to a short value of

\[
\frac13\sum_i z^{-\gamma_i}
\]

at the universal resultant root satisfying

\[
z^q=2,\qquad z^j=3
\]

modulo every denominator factor.

The missing theorem can therefore be stated in either of two equivalent ways:

```text
CRT form:
  incompatible balanced/dominant quotient jets;

resultant form:
  a uniform least-residue lower bound for the rough lacunary path polynomial.
```

This is narrower than the original full-denominator request and is the exact
point at which the current argument stops.

## 7. Status verdict

FC* is **not proved**.

The rigorous advance is:

1. exact large-factor synchronization;
2. exact balanced/dominant cofinal dichotomy;
3. exact resultant-root normal form;
4. a square-root shrinkage of the displacement window;
5. a finite refutation of the one-factor proof strategy;
6. isolation of the two smallest complete obstructions still requiring a new
   theorem.
