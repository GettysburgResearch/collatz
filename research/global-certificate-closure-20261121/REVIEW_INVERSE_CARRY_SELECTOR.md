# Independent review of the inverse carry selector obstruction

**Verdict: PASS for IC1–IC3 and their stated scope.** For every \(H\ge4\),
the certified unit \(q_H=(2^{3^H+1}-1)/3\) admits no positive integral
source \(x<q_H\) from the single completed PR170 carry family, for any
\(r\ge0,b\ge2\). This review does not assert that \(5q_H\) is
nonconvergent or that \(q_H\) is a least five failure.

## Frozen inputs

| Input | SHA-256 |
|---|---|
| `INVERSE_CARRY_SELECTOR.md` | `b2cb40ac4cde2c7b16f4d2121bf073fac1f1b659760502a3f8e4f75d0964e7bf` |
| `check_inverse_carry_selector.py` | `6050dfbb71447b1ca01b762e8632c8ce507f85cb7da5388331a30747e04de356` |
| `inverse_carry_selector_expected.json` | `1fe4fc0b55d741538defe7fd23093c0319d93bdd51059e5540b953de06604c6b` |

No author files were modified. The carry interface was also checked against
PR170 `656063d5efa0f5708356ab2563a4348d39bae013`,
`research/global-forcing-20261121/certificates/CARRY_COMPILER.md`, CF2–CF3.

## Exact interface and necessary bounds

The source word has \(r+9\) odd steps, clock \(r+b+18\), and correction
\(1351\,3^{r+5}+2^{r+16}\). Its full inverse formula therefore agrees
with IC1. For an integral source, \(81x+1351\equiv1\pmod3\), so IC2
forces the **exact** valuation

\[
\nu_3(2^{b+2}q-1)=r+5.
\]

This is a necessary condition, not a sufficient integrality test: the
remaining congruence modulo 81 must still be checked. The proof retains it.

For a positive integral \(x<q\), the resulting integer \(D\ge1\)
gives \(2^{r+16}<81q+1351\). The integrality assumption here is
explicit and essential. If \(b\ge r\), the coefficient of \(q\) in
\(3^{r+9}(x-q)\) is positive, because \(2^{18}>3^9\). Substituting
\(q\ge5\) and then \(4^r\ge3^r\ge2^r\) gives the exact lower
bound \(818476\,3^r>0\). Hence every contracting candidate must have
\(b<r\).

The finite decision bounds are also exact, including the endpoint:
strictness gives \(2^{r+16}\le81q+1350\), and therefore
\(r\le\lfloor\log_2(81q+1350)\rfloor-16\). Enumerating the permitted
\(b\)'s and using the exact valuation to determine the unique possible
\(r\) loses no contracting candidate. This does not assert that such a
candidate exists.

## All-H obstruction

Every \(q_H\) is positive odd, with exact one-step first-hit exponent
\(3^H+1\). Successive cubing gives
\(\nu_3(2^{3^H}+1)=H+1\), hence
\(\nu_3(q_H+1)=H\); in particular \(q_H\equiv-1\pmod3\) is a unit.

The binary comparison

\[
81q_H+1351=54\,2^{3^H}+1324<2^{3^H+6}
\]

has the stated strict sign. Its simple numerical base already holds at
\(H=2\) and increases thereafter. Combining it with \(b<r\) gives
\(r\le3^H-11\) and \(0<b+2<3^H\).

The two cases cover every possible \(r\):

* If \(r+5\le H\), the necessary congruence is
  \(2^{b+2}\equiv-1\pmod{3^{r+5}}\). The exact order of 2 is
  \(2\cdot3^{r+4}\), so \(b+2\ge3^{r+4}\). The inequality
  \(3^{r+4}-2>r\) holds at \(r=0\) and its difference increases by
  \(2\cdot3^{r+4}-1>0\) at every increment. It contradicts \(b<r\).
* If \(r+5>H\), the same congruence modulo \(3^H\) says that
  \(b+2\) is a positive odd multiple of \(M=3^{H-1}\). The strict
  upper bound \(b+2<3M\) forces \(b+2=M\). With \(t=2^M\) and
  \(z=t+1\), the polynomial identity in IC11 is exact. Its bracket
  has valuation two: \(-9\) has valuation two, whereas the other
  terms have valuations \(H+1,2H,3H\), all strictly larger. Thus
  \(\nu_3(tq_H-1)=H+1\), forcing \(r=H-4\). But
  \(b=3^{H-1}-2>H-4\), with positive base and increasing difference
  for every \(H\ge4\). This again contradicts \(b<r\).

No source-unit assumption was used to obtain these contradictions. The
result therefore excludes even the larger set of positive integral
contracting inverse sources, as claimed.

## Independent replay and limits

`review_inverse_carry_selector.py` imports no author checker functions.
It independently checks the source correction, the polynomial identity by
coefficient comparison, the height constants and induction bases, and the
rank-one witnesses and exact valuations for \(H=4,\ldots,9\). Its
complete finite decisions retain integral noncontracting candidates as
controls instead of discarding them at the initial height test. It also
constructs three different positive eligible returns, supplies actual
certificates for their endpoints, preserves those certificates on the
source arm, and checks both ordinary transport arms.

The checker reads only colocated files and prints complete deterministic
JSON. Normal and `-OO` outputs agree byte for byte with
`inverse_carry_selector_independent_expected.json`, SHA-256

```text
5f340c8c419534ceb395af4ecd41a431727546253ecea640965764f5f158ec1f
```

The independent checker SHA-256 is

```text
d993d44669eac5ffc5c96151df7b8890aed6fda937aaf9f3febbc0a4785bea10
```

Author-checker executions in normal and `-OO` modes also matched the
frozen expected report exactly. The infinite theorem rests on the
two-case proof above, not those bounded decisions.

The obstruction refutes an all-certified-endpoint selector made from one
completed carry block. It does not refute a selector restricted to actual
least failures, a separate theorem excluding these certified endpoints
from that role, multiple blocks with intermediate expansion, or a
different guarded return. The supplied certificates prove convergence of
\(q_H\), and no conclusion about convergence or nonconvergence of their
fivefold targets is drawn here.
