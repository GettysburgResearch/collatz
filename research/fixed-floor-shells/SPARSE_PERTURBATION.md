# A sparse perturbation preserving predecessor and pressure data

**FS-018. PROPOSED method limit.** Use the ordinary Collatz map, with
Syracuse map on odd states. Assume the source-qualified Lau Theorem 1.3
as in [FS-008](TIMED_BLOCKS.md). The following altered map exhibits a
positive-density escaping component while preserving the exact
first-hit pressure at every odd target outside a set of counting function
$O(1+\log X)$. It also retains the two Lau clock constants and a lower
bound of the same uniform order $t^{-25/11}$ for every eligible target.
The altered rule is essential to the construction.

Put $Y=\{13+6i:0\le i\le32\}$, and order the odd vertices
$v_{j,i}=(16^j(13+6i)-1)/3$ lexicographically for $j\ge4$. These
are integers, with true Syracuse image $13+6i$. They strictly increase,
including at the boundary $205<16\cdot13$. Consecutive vertices $v,v'$
satisfy $v'/v<3/2$ (the largest within-row ratio is at $i=0$).
At each $v$ replace the ordinary odd step by $v\mapsto2v'$. Keep every
other step, including every even step. Assign to the modified Syracuse
edge the positive affine chart $x\mapsto\lambda x+(\lambda-1)/3$
where $\lambda=(3v'+1)/(3v+1)$. Use the usual charts elsewhere.
The forward spine escapes. Its derivative from its initial odd state
$b$ to $v$ is exactly $(3v+1)/(3b+1)$.

Let $F$ consist of all true odd iterates of $Y$, including $Y$. Direct
finite verification gives $|F|=106$, $\max F=3077$ and all seeds reach
1. One reproducible check uses the following code.

```python
seen = {1}
for seed in range(13, 206, 6):
    x = seed
    local = set()
    while x not in seen:
        assert x not in local
        local.add(x)
        z = 3*x + 1
        x = z // (z & -z)
    seen.update(local)
assert (len(seen), max(seen)) == (106, 3077)
```

A true path after encountering a modified vertex has only odd states in
$F$ from its next odd step onward. A perturbed path after that encounter
stays on the spine at all odd times. Consequently for an odd target
outside $F$ and the spine, the entire lists of first-hit paths agree,
including derivatives and times. All ordinary odd-target density laws
and power-sparse exceptional-target bounds of FS-010 to FS-017 therefore
transfer, including the law of the minimum genuine predecessor. Yet a
fixed source already contributes $\gg_b v^s$ to the first-hit pressure
$H_s(v)$ along the spine for every $s>0$.

For any positive integer $t$ prime to 3 choose $16\le a\le27$ such
that $w=(2^a t-1)/3$ is an odd unit modulo 3 and
$a+v_2(t)\not\equiv0\pmod4$. Indeed, integrality fixes the parity of
$a$, $3\nmid w$ holds for two of the three classes modulo 6 of that parity,
and of the two lifts of either good class modulo 12 at most one fails
the condition modulo 4.
The height $w>3077$ excludes $F$ and its exact valuation
$v_2(3w+1)$ excludes the spine. Thus every true first-hit path to $w$
avoids all modifications. From $w$ the ordinary path still hits $t$
in $a+1$ steps and its odd core in one Syracuse step. Since
$w/t\ge(2^a-1)/3$, these cost at most $10.46\log(w/t)$ ordinary and
$3.4881\log(w/t)$ Syracuse steps respectively. Concatenating Lau's
certified paths to $w$ provides at least
$\lfloor c t^{-25/11} N\rfloor$ odd sources below $N$ with both original
clock coefficients, for a universal $c>0$ since $w/t\le2^{27}/3$.
In particular choose any unit spine vertex (e.g. $j=4,i=1$, since
$16^4\cdot19\equiv7\pmod9$). Its entire perturbed predecessor set
escapes and has positive lower natural density.

This example leaves open which consequence of the exact Collatz odd
formula precludes pressure concentration on a single forward path.
In particular a sparse-target upper bound, even supplemented by the
two timed positive-density predecessor guarantees, does not give that
pointwise conclusion for the class of maps above.
