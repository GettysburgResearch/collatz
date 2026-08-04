# Agent report — delayed-window Padé and native period-nine closure

```text
Agent: gpt56-complexity-01
Issue: #18
Draft PR: #20
Branch: agent/gpt56-complexity-01/18-padic-repetition-rigidity
Date: 2026-07-22
```

## Starting point

Wave 5 supplied a source-dependent Väänänen--Wallisser theorem through period
nine and identified period ten as the first fixed period outside that source
condition. The quantitative source measure was then transcribed and found far
too weak for the proposed one-phase bootstrap. The native simultaneous block
Padé family still appeared to stop at period three because its cancellation
window began at the denominator degree.

## Main change

The denominator degree and the start of the cancellation window were separated.
For degree `D=rn`, order `n`, and independent delay `M>=D+1`, define

```text
beta(k)
 =[(1-r)k^2+(2rM-r-1)k]/2.
```

The resulting Gaussian-binomial denominator has exact phase coefficient

```text
Gamma_(j,N)
 =base_(j,N)
  *prod_(h=0)^(D-1)
    (1-lambda^[h+rM-rN-j]).
```

Every phase therefore vanishes for

```text
M<=N<M+n.
```

The first surviving block is `N=M+n`, its phase-zero contribution is uniquely
minimal at the prime two, and the common rational height can be bounded with the
exact quadratic scale

```text
Q_A
 =[D^2+D+rM^2-rM-2M+2]/2.
```

## New asymptotic law

If `M/n->alpha`, then

```text
mu_r^delay(alpha)
 =log_81(64)*[((alpha+1)^2-r)/(alpha^2+r)].
```

The optimizer is

```text
alpha_r^*
 =(2r-1+sqrt(4r^2+1))/2.
```

The optimized exponent is above one through period nine and below one at period
ten.

## Exact source-independent period-nine theorem

The uniform rational delay

```text
alpha=37/2
```

has endpoint shape `297/281` at period nine. The exact inequalities

```text
64^93>81^88,
88*297-93*281=3
```

prove the approximation exponent is strictly greater than one for every period
`r<=9`. The elementary cross-numerator argument therefore gives irrationality
of every such periodic tail, and the finite-prefix transfer excludes every
eventually periodic directive with minimal eventual period at most nine.

This is `T-9422`. It reproduces the period range of source-dependent `T-9417`
without importing a linear-independence theorem.

## Exact period-ten boundary for this family

For `r=10`,

```text
f_10(alpha)
 =(alpha^2+2alpha-9)/(alpha^2+10)
 <263/250
```

because

```text
13alpha^2-500alpha+4880>0
```

has discriminant `-3760`. Together with `64^20<81^19`, this gives

```text
mu_10^delay(alpha)<4997/5000<1
```

for every delay. Thus window placement alone is completely optimized and cannot
close period ten.

## Verification

`X-9413` checks exact Laurent-polynomial products, zero windows, first-error
phases, and every monomial in the frozen height audit.

```text
Laurent product identities       630
zero-window checks                180
first-error checks                 36
height monomials               49,680
```

Canonical SHA-256:

```text
ddce893eef7edf6b15c5b83dc2598bf7a832479507cf2c92309dba2172c8ec4c
```

## Files

```text
research/padic-repetition/claims/L-9418-delayed-window-block-pade.md
research/padic-repetition/claims/T-9422-native-period-nine-delayed-pade.md
research/padic-repetition/claims/R-9410-delayed-window-period-ten-ceiling.md
experiments/X-9413-delayed-window-pade/README.md
experiments/X-9413-delayed-window-pade/run.py
experiments/X-9413-delayed-window-pade/results/canonical.json
```

## Status and limitations

All theorem-level claims remain `PROPOSED` pending independent reconstruction.
The result closes a fixed-period family, not the growing S-adic frontier. Period
ten, the balanced nonperiodic directive, M1, and Collatz remain open.

## Next attack

The first source-uncovered and native-uncovered fixed period is ten. The delayed
family misses by less than one percent, but `R-9410` proves that no further
window movement can help. The remaining credible routes are:

1. direct Padé cancellation of the combined native moment sequence;
2. a theorem for the homogeneous order-two `q`-difference equation in `L-9415`;
3. phase-sensitive Hermite--Padé or maximal-minor factors;
4. a genuine completion-height numerator coupling the ordinary and `2`-adic
   coordinates.

Any future estimate should expose dependence on both period and order so its
constants can be tested on growing standard words.