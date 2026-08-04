# D-9402 — Expanding digit-chart coding

Claim ID: D-9402  
Title: General `M -> N` survivor code for an expanding digit chart  
Status: — (definition; frozen for this packet)  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: finite digit charts with an even source radix and odd expanding target radix  
Related counterexample candidates: issue #4 collision-fiber ladder; no `K-####` candidate

## Chart data

Fix integers

```text
M = 2^L,       L >= 1,
N > M,         N odd,
D subset {0,1,...,M-1},   D nonempty.
```

The associated partial digit chart is

```text
H_D(MB+d) = NB+d,      d in D.
```

Equivalently, if `A_j = MB+d_j` and `A_(j+1)=NB+d_j`, then

```text
M*A_(j+1) = N*A_j - (N-M)*d_j.
```

## Code map

For a one-sided digit code

```text
d = (d_n)_(n>=0) in D^N,
```

define

```text
Phi_(M,N)(d)
  = ((N-M)/N) * sum_(n>=0) d_n * (M/N)^n
  = sum_(n>=0) (N-M)*d_n*M^n / N^(n+1)
  in Z_2.
```

The series converges in `Z_2` because `N` is odd and

```text
v_2(M^n) = L*n -> infinity.
```

The binary `64 -> 81` code of D-9401 is the specialization

```text
M=64, N=81, D={0,1}.
```

Write `sigma d` for the left shift and

```text
A_j(d) = Phi_(M,N)(sigma^j d).
```

An **ordinary chart code** is a code for which `A_0(d)` is an ordinary integer.
An ordinary chart code is called **aperiodic** when its digit sequence is not
eventually periodic.

## Factor complexity

For `ell>=1`, define

```text
p_d(ell) = | { d[a:a+ell] : a>=0 } |.
```

The criticality parameters are

```text
beta_(M,N)  = log_M(N),
delta_(M,N) = beta_(M,N)-1 = log_M(N/M),
kappa_(M,N) = 1/delta_(M,N) = log_(N/M)(M).
```

As the chart multiplier `N/M` approaches `1` from above, `kappa_(M,N)`
diverges.  T-9405 turns this numerical criticality into a required lower bound
on ordinary-code factor complexity.

## Real embedding convention

For an eventually periodic code the same series is one rational number in
both `Q_2` and `Q`.  In the real embedding its value is a convex combination
of the digits because

```text
((N-M)/N) * sum_(n>=0) (M/N)^n = 1.
```

Hence it lies in the interval

```text
[min D, max D].
```

No real value is assigned here to an arbitrary nonperiodic `2`-adic code.