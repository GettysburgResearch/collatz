# Active stack cylinders and ordinary stabilization

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Branch:** `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
**Status:** fourth isolated `94xx` packet; theorem-level claims `PROPOSED`

## From stationary ghosts to active steering

The demand-tree packet classified fixed-context same-stage matching.  Active
steering changes the target height and transports an unused high quotient.
The exact one-stage algebra is nevertheless rigid.

For height `m`, define

```text
M_m=64^(9m+1),
A_m=81^(9m+1),
c_m=(M_m+17)/81.
```

For a transition to height `n`, one residue `r_(m,n) mod M_n` is admissible.
Writing

```text
x=r_(m,n)+M_n*y
```

gives the exact next context

```text
x'=A_m*y+k_(m,n).
```

Because `A_m` is odd, the unused quotient is carried through a `2`-adic
isometry. Future conditions select its low digits one block at a time.

## One cylinder per finite directive

For a finite schedule

```text
m_0,m_1,...,m_K,
```

`T-9409` proves that all valid initial contexts form exactly one residue class

```text
R_K mod Q_K,
Q_K=product_(i=1)^K 64^(9m_i+1).
```

The cylinder is computed backward by one modular inversion per stage.  No
search or branching is required.

Consequences:

1. any two initial contexts realizing the schedule agree in the first
   `log_2 Q_K` binary digits;
2. every context in the cylinder realizes the schedule integrally;
3. extending the schedule selects one new block of the initial context;
4. an infinite directive selects one unique point of `Z_2`.

## Ordinary versus adic closure

Let `R_K` be the least representative in `[0,Q_K)`.  The nested `2`-adic point
is an ordinary nonnegative integer **iff** the integer sequence `R_K`
eventually stabilizes.

This is the exact remaining boundary:

```text
compatible finite towers
  -> one Z_2 initial context automatically;
ordinary infinite tower
  <-> eventual zero tail in the new cylinder blocks.
```

Put

```text
a_K=(R_(K+1)-R_K)/Q_K.
```

Then the ordinary question is whether `a_K=0` eventually.  Proving infinitely
many nonzero `a_K` for every admissible directive would close this stack route;
constructing an eventually zero tail would produce one ordinary context to
lift and test.

## Precision budget

For strictly increasing heights,

```text
log_2 Q_K
 >=54*K*m_0+27*K*(K+1)+6K.
```

For increments in `{17,18}`,

```text
54*K*m_0+459*K*(K+1)+6K
 <=log_2 Q_K
 <=54*K*m_0+486*K*(K+1)+6K.
```

Thus a `K`-stage balanced tower fixes quadratically many initial bits.  This is
a padding-free constraint: it counts the exact initial cylinder modulus, not
the factor complexity of emitted zero runs.

## Frozen replay

`X-9404` checks:

- all 1,360 one-through-four-stage schedules over heights `{0,1,2,3}`;
- 5,440 cylinder members;
- 435,696 lower-bit perturbations, all rejected;
- 5,440 quotient-isometry pairs;
- a 24-stage Fibonacci `17/18` prefix.

At that 24-stage checkpoint:

```text
last height = 418,
fixed initial bits = 282,888,
least representative bit length = 282,888.
```

This is bounded evidence only; it does not prove that later block digits never
vanish.

Canonical SHA-256:

```text
73a878073e3e8e39e6e950ad0e4585c522cd7fe1794639dc5b015a3b5115be3f
```

## Strategic connections

- **Issue #4:** replaces “any finite schedule is CRT-constructible” by an exact
  one-cylinder theorem and a stabilization criterion.
- **PR #3:** supplies a reusable ordinary-marker fuel accounting rule for
  counter-stack grammars.
- **PR #16:** the cylinder block sequence is a natural arithmetic object to
  compare with low-energy carry prefixes.
- **M1:** exhibits the same finite-versus-adic boundary in active stack
  coordinates, without claiming equivalence to all survivor codes.

## Next target

Derive a recurrence or invariant for the new block digits `a_K`.  The most
promising candidates are:

```text
- first nonmatching demand-lift depth;
- real sign/height of the terminal context when a_K=0;
- 3-adic valuation of the quotient carry;
- Fourier energy of the selected block digit;
- repetition or automaticity of the block sequence under a Sturmian directive.
```
