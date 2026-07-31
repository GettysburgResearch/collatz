# Full-denominator factor synchronization pass

**Agent:** `gpt56-positive-tangent-01` (`GPT-5.6 Pro`)  
**Date:** 2026-08-01  
**Issue:** #75  
**Branch:** `agent/gpt56-positive-tangent-01/75-coefficient-envelope`  
**Draft PR:** #83

## Status boundary

All new theorem-level claims remain **PROPOSED** pending independent
reconstruction.

**FC* is not proved. SC* is not proved. Collatz is not proved.**

## 1. Synchronization performed

The pass re-read PR #81 at exact head

```text
086ac39d93d7c1aad9d05732f5fc11c9ce349530
```

and the current PR #83 branch. It retained the collaborator corrections and
new constraints:

```text
A_w=Dr+2^j d=Ds+3^q d;
0<=d<A_w/2^j<q/3;
complete-prime-power path compiler;
polynomial family sparsity;
square-root displaced support;
two-thirds integrated displacement;
logarithmic early departure;
logarithmic self-shadowing;
cycle absorption into FC*.
```

The source/endpoint labels are not interchanged anywhere in the new packet.

## 2. Exact local-factor theorem

For

```text
D=product M_nu
```

with complete prime-power factors, define

```text
delta_nu=[A_w*3^(-q)]_(M_nu).
```

Every factor larger than the real displacement window must return the same
ordinary integer:

```text
M_nu>A_w/2^j
    ->
delta_nu=d.
```

Thus two such factors with unequal residues exclude the word.

The exact gcd profile is

```text
gcd(D,A_w)=gcd(D,d).
```

This includes the cycle level `d=0` rather than discarding it.

## 3. Quotient jets

For a unitary block `U|D`, `C=D/U`, the first local residue gives `d`. Dividing
out `U` gives a second residue:

```text
sigma_U=
  [((A_w-3^q delta_U)/U)*C^(-1)]_U.
```

For a genuine candidate this is the endpoint modulo `U`. Above the exact
ordinary endpoint bound it is the endpoint itself.

A cofinal denominator therefore has one of two forms.

### Balanced

```text
D=U*V,
U,V > ordinary endpoint bound.
```

Both blocks must return exactly the same `d` and exactly the same endpoint
jet.

### Dominant

```text
D=W*c,
W > endpoint_bound^2,
c <= endpoint_bound.
```

The giant prime power determines `d,r,s`; the small cofactor must complete the
divisibility.

These are lossless exact alternatives, not heuristic classifications.

## 4. Resultant-root normal form

When `gcd(j,q)=1`, choose `a,b` with `aq+bj=1` and put

```text
z=2^a*3^b mod D.
```

Then

```text
z^q=2,
z^j=3,
abs(Res(X^q-2,X^j-3))=D.
```

For odd positions `d_i`, put

```text
gamma_i=j(i-1)-q*d_i.
```

The full displacement condition is one lacunary value:

```text
3d == sum_i z^(-gamma_i) mod D.
```

Relative to the upper mechanical word, displaced positions contribute the
multipliers `2^(-h_i)`. This packages every prime-power congruence into one
universal resultant-root object.

No valid product-formula estimate was found that turns the growing-support
lacunary form into the requested least-residue lower bound.

## 5. Roughness contribution

If `R` odd positions are displaced from the upper-mechanical word, every such
position lowers `A/3^q` by more than `1/12`. Therefore

```text
A_v/2^j
 < A_mech/2^j-(3^q/2^j)*R/12.
```

Every non-descending displacement lies below the right side.

PR #81 supplies `R=Omega(sqrt(j))` for every unbounded acyclic exceptional
family, so the permissible interval loses a square-root-width portion.
This is a real improvement, but the remaining interval is not forced empty.

## 6. Exact countertest to the one-factor strategy

`X-6912` exhausts every first-crossing word through length `27`.

```text
valid lengths:                    17
first-crossing words:        502,523
nontrivial canonical failures:      0
```

Every word below length `27` has one complete prime-power factor that rejects
its short displacement interval.

At

```text
j=27,
q=17,
D=5*71*14303,
```

exactly three descending words evade every individual prime-power witness.
A proper block of two factors rejects each one.

The generator uses modular inversion. The independent verifier reconstructs
canonical source/end pairs by one-bit lifting and imports no generator module.

```text
semantic digest:
c815dd97651f4559f8bb45c6709a45df783ce5f7f825b2454323d937aea20d85
```

This finite result is not extrapolated. Its rigorous role is to refute the
proposed one-factor all-length proof method.

## 7. What was attempted and rejected

### Single large prime-power residue

Refuted exactly at `j=27`.

### Independent local order checks

Insufficient. An order cover reconstructs the path but does not prove the
omitted factors or common ordinary `d`.

### Zero family entropy

Insufficient. A polynomially sparse sequence can still hit one deterministic
CRT residue at every length.

### Square-root support

Insufficient. It shrinks the real interval but does not force two factor
residues to differ.

### Degree/height product formula

Insufficient in its current form. The number of lacunary terms grows at least
as a square root and the naive resultant-height bound is much larger than the
complete denominator.

## 8. Smallest exact obstruction left

FC* is now exactly the nonexistence of two objects.

```text
Object B:
  a balanced pair of large unitary blocks
  with identical d and identical quotient endpoint jet;

Object G:
  a giant prime-power block producing small d,r,s,
  with one small cofactor completing the divisibility.
```

All first-crossing, wrap, roughness, early-departure, self-shadowing, and
physical replay constraints remain attached to these objects.

Equivalently, when the exponents are primitive, the missing theorem is a
uniform least-residue lower bound for the resultant-root Laurent sum.

## 9. New files

```text
research/positive-coefficient-tangent/claims/
  L-6912-complete-factor-synchronization.md
  L-6913-resultant-root-normal-form.md
  T-6914-rough-support-displacement-window.md
  R-6915-cross-factor-obstruction.md

experiments/X-6912-factor-synchronization/
  README.md
  run.py
  verify.py
  results/canonical.json
```

The packet also updates `README.md` and `LATEST.md`.

## 10. Recommended next theorem

Do not return to independent prime factors or candidate counts.

Attack one of:

```text
B-jet incompatibility:
  prove two complementary large factor blocks cannot return the same
  short d and quotient s for a square-root-rough first-crossing path;

G-jet incompatibility:
  prove the giant prime-power quotient jet cannot also satisfy its
  small completing cofactor;

resultant lower bound:
  prove the rough Laurent path polynomial cannot have least residue
  below A_w/2^j, including zero.
```

Any of these, together with the existing complete compiler, would close FC*.
