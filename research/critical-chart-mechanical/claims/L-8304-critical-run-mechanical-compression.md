# L-8304 — Critical paired chart as a mechanical word over runs four and five

Claim ID: `L-8304`  
Status: `PROPOSED`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `T-8302`; the finite mechanical-word recursion of `L-8403`  
Scope: the frozen critical pair and the general Euclidean cone below  
Related counterexample candidates: none

## General substitution theorem

Let integers `b>r>0` and put

```text
s=4b+r,
m=5b+r.
```

Define

```text
phi(0)=0 1^4,
phi(1)=0 1^5.
```

Then the lower mechanical words obey

```text
boxed:
L(s,m)=phi(L(r,b)).                                      (1)
```

### Proof

Since `m=s+b`, the first Euclidean step writes `L(s,m)` as the image of `U(b,s)` under

```text
0 -> 1,
1 -> 01.
```

Since `s=4b+r`, the second step writes `U(b,s)` as the image of `L(r,b)` under

```text
0 -> 1 0^3,
1 -> 1 0^4.
```

Composing the substitutions gives `0 1^4` and `0 1^5`, proving `(1)`. This is an identity of finite words. **QED**

## Critical specialization

For

```text
k=3,149,971,404,836,
A=4,992,586,555,009,
```

the paired chart has

```text
m=k/2=1,574,985,702,418,
s=2k-A=1,307,356,254,663.
```

Put

```text
b=m-s=267,629,447,755,
r=s-4b=236,838,463,643.
```

Then

```text
boxed:
L(1,307,356,254,663,1,574,985,702,418)
 =phi(L(236,838,463,643,267,629,447,755)).               (2)
```

The trillion-chart-block schedule is therefore a `267,629,447,755`-letter mechanical word over two macro-runs.

## Exact macro-run maps

In the shifted physical coordinate `x=(n-1)/2`, put

```text
F_0(x)=9x/16,
F_1(x)=(9x+3)/8,
R_d=F_1^(4+d) o F_0,
d in {0,1}.
```

Then

```text
boxed:
2^(16+3d)R_d(x)
 =9^(5+d)x+48(9^(4+d)-8^(4+d)).                          (3)
```

Thus

```text
R_0: (p,q,c)=(9^5,2^16,118,320),
R_1: (p,q,c)=(9^6,2^19,1,261,488).                       (4)
```

The run word in `(2)` has chart length `5b+r=m`, dyadic exponent `16b+3r=A`, and odd multiplier `9^m=3^k`. Its complete denominator is therefore exactly

```text
boxed:
2^A-3^k,                                                 (5)
```

the same denominator as the critical PR #45 circuit.

Formula `(3)` follows by iterating `F_1`:

```text
F_1^u(y)=[9^u y+3(9^u-8^u)]/8^u,
```

and substituting `y=9x/16`, `u=4+d`.

## Constructive meaning

The critical chart now has a second compressed level with Euclidean block boundaries at every scale. It supplies a small exact replacement alphabet while preserving the complete cycle denominator.

## Gap audit

Compression alone gives no denominator divisibility, ordinary integer, cycle, or infinite chart path. Proper-factor repairs remain insufficient.

## Verification

`X-8303` checks `(1)` on `473` small coprime pairs, independently compares the chart and run summaries, and verifies every critical count exactly.

## Suggested next attack

Use the run hierarchy to solve the ordinary quotient congruence one prime-power digit at a time, rather than adding more unstructured symbol swaps.
