# LIT-KTHM-0041 — Centered rational-power trapping is a finite carry system

**Type:** elementary exact reduction with a literature applicability boundary.  
**Literature neighbors:** Flatto--Lagarias--Pollington; Dubickas (2006, 2008).  
**Maps to:** `ADEL/T-9315`.

## Statement

Let `p>q>=1` be coprime integers and let `xi` be real. Suppose that for every `n>=0` there is an integer `k_n` such that

```text
u_n=xi*(p/q)^n-k_n,
|u_n|<=1/p.                                           (1)
```

Then the integer carries

```text
c_n=p*k_n-q*k_(n+1)                                  (2)
```

satisfy

```text
p*u_n-q*u_(n+1)=-c_n                                 (3)
```

and

```text
c_n in {-1,0,1}.                                     (4)
```

If strict inequalities hold in `(1)`, the sign transition `(sign u_n, sign u_(n+1))` restricts the carry more sharply:

```text
same nonzero sign -> c_n may be 0 or the corresponding boundary carry;
opposite signs    -> c_n has the sign forced by (3);
zero phase        -> the next phase and carry are rigid.               (5)
```

For `(p,q)=(81,64)`, a hypothetical ordinary survivor in `ADEL/T-9315` therefore determines one bi-infinite-looking path in a finite sign/carry graph with phases confined to `[-1/81,1/81]`.

## Proof

Multiply the definition of `u_n` by `p` and the definition of `u_(n+1)` by `q`. Since

```text
p*xi*(p/q)^n=q*xi*(p/q)^(n+1),
```

subtraction gives `(3)` with `(2)`.

The bound `(1)` gives

```text
|p*u_n-q*u_(n+1)|
 <=1+q/p<2.
```

The left side is an integer by `(3)`, proving `(4)`. The sign refinements are immediate interval checks in `(3)`. ∎

## Literature boundary

The Flatto--Lagarias--Pollington range-width theorem gives a one-dimensional real width obstruction. It does not automatically exclude the wrapped two-arc set

```text
[0,1/p] union [1-1/p,1).
```

Dubickas's nearest-integer and two-interval theorems are geometrically closer. Their constants must be specialized to `(81,64)` before any conclusion is imported.

## Native next step

Construct the exact interval graph for all sign/carry blocks, propagate interval images, and compare the surviving symbolic language with the explicit Dubickas/Thue--Morse bounds. A finite empty intersection would close the ordinary section.