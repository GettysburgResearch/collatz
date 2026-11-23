# Independent semantic review: marked prefix erasure and the new family

Reviewer: `literature_operator`, 21 November 2026.

**Verdict:** the inspected arithmetic statements and their written proof are
correctly scoped. The packet proves smaller marked common-future partners,
including a quarter-source partner for every member of the displayed
native-horizon obstruction family. It does not prove a universal partner
cover or unconditional convergence of that whole family.

This is an independent mathematical/source review, not a compilation or
finite numerical replay. The reviewer did not edit any inspected source.
Previously proved `ShellCover` and `ForwardSection` interfaces are used with
their stated meanings; their older proofs are not re-reviewed here.

## Exact inspected snapshots

All paths below are relative to the symbolic agent's packet directory.

| File | SHA-256 |
| --- | --- |
| HalfSourceMerge.lean | a97887077575d43a9ab27739c27a693d352334ea20dce87c2ecbe72b6f7b0fd5 |
| LongDiamondErasure.lean | 3cc8307078cccf47996298b1ea491722784b0dc50700f676d7f0a5b7260c3726 |
| MarkedErasure.lean | cf10a107ff5829d08f0ffc3c7b7a67ccd27e8af8a88501ef80474c408ee6493a |
| NewBandFamily.lean | 60409cdc2bd9738affe2cddb389df24c1b4540165085ea14de15ff8b6d693369 |
| NEW_BAND_FAMILY_PROOF.md | 1eba9659f84306517db361ff8db977f43276f3e976978ffc91b09357d84b0200 |

## 1. Source erasure and exact clocks

The map is consistently the shortcut map: halving for even inputs and
`(3n+1)/2` for odd inputs. For `u>0`, the identity
`T^b(2^b*u-1)=3^b*u-1` supplies the two initial arms. Under the explicit
synchronous diamond hypothesis, their endpoints meet at clocks
`k-r+h` and `k+h`, respectively. The exact source relation is

\[
 n+1=2^r(x+1),\qquad
 n=2^k u-1,\quad x=2^{k-r}u-1.
\]

The guards `0<r<k` ensure `x>0` and `x<n`; natural subtraction is not
silently used outside its valid range. The half, quarter, and eighth
specializations correctly give `2x+1=n`, `4x+3=n`, and `8x+7=n`.

The short diamond is exact for `v=3 mod 4`: both `v-1` and `3v-1`
reach `(3v-1)/4` in two shortcut clocks. The eight-clock identities were
checked algebraically through all displayed affine steps. Their parity
words `00011100` and `01000001` both end at `27a+20`.

For `v=147 mod 256`, the phases `v=3 mod 4`, `3v=185 mod 256`, and
`9v=3 mod 4` justify the short--long--short composition at one common
clock eight. Thus the quarter and eighth source-erasure clocks in
`LongDiamondErasure.lean` are correct.

## 2. The stronger marked-to-marked conclusion

Let `x>0`, `e=floor(log_2 x)`, and `n=2^r(x+1)-1`. The bounds
`2^e<=x<2^(e+1)` give exactly

\[
 \lfloor\log_2n\rfloor=e+r,\qquad
 n-2^{e+r}=2^r(x-2^e)+(2^r-1).
\]

Hence the marked inequality for `n` implies, after discarding the
nonnegative extra offset and cancelling `2^r`,

\[
 (e+1)(x-2^e)\le70\,2^e.
\]

Oddness of `x` supplies the other markedness condition. This proves the
claimed preservation for every nonnegative `r`, including `r=0`, and
does not need the earlier square-root height guard for arbitrary partners.
Combining it with an actual endpoint diamond gives an actual smaller
**marked** source sharing a future with the supplied source. It does not
claim that the smaller source occurs on the larger source's forward orbit.

## 3. The new explicit family

For `j>=0`, the parameters

\[
 k=64j+31,\quad s=2j+8,\quad d=k+s=66j+39,
 \qquad n=2^d+2^k-1
\]

have the required properties:

- `k>=2s`, `s>=8`, and `k,d` are odd.
- `u=2^s+1` is `1 mod 256`, and
  `3^(k-2)u=3^(64j+29)u=147 mod 256`.
- `floor(log_2 n)=d`; the source is odd and positive.
- `d+1=66j+40<=70(j+1)<=70*2^j<=70*2^s`, proving the exact
  constant-70 marked inequality after multiplying by `2^k`.

The resulting partner is

\[
 x=2^{k-2}(2^s+1)-1=(n-3)/4,
 \qquad T^{k+6}x=T^{k+8}n.
\]

It is positive, smaller, and marked by the preservation theorem. The
meeting clock on the original arm satisfies `k+8<=d`.

The native-horizon non-descent argument is also valid. The first `k`
clocks form an increasing odd run. Every further shortcut step is at
least halving. Writing `k=2s+b` gives

\[
 3^k/2^{k+s}=(9/8)^s(3/2)^b\ge1,
\]

so `3^k*u-1>=2^s(2^k*u-1)`. Even the maximum possible halving over
the next `s` clocks cannot lower the original source. This proves
`T^t(n)>=n` for every `t<=d`, independently of the diamond.

## 4. Scope and remaining obligation

Every member of the explicit family is excluded from being a least
positive counterexample, or a least marked counterexample: its positive
smaller marked partner would converge under that induction hypothesis,
and the actual common future transfers convergence.

The packet correctly states that this does not independently prove
convergence of every family member. The partner is not asserted to lie
in the same parameterized family, so induction only on `j` is unavailable.
The generic erasure theorem retains its endpoint-diamond premise, and no
universal successful diamond selector is asserted.

The coalescence is a component-descent certificate, not a forward-return
descent. Indeed the proved original non-descent prefix rules out visiting
the smaller partner during that prefix.

One minor wording qualification: at `j=0`, `k+8=d` exactly. Descriptions
should say the merger occurs **by the end of** or **within** the native
horizon, rather than strictly before its end. The displayed inequalities
and Lean statements already use the correct non-strict bound.

This review verifies the arithmetic and logical scope. It does not
independently certify novelty priority or the closing paragraph's
Bernstein--Lagarias/Dubickas literature attributions.
