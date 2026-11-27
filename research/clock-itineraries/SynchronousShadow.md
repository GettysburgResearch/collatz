# A converging gate can pass every row test in a finite list

For every integer $B\ge0$, there exists a single ordinary odd integer $a>2$ that **reaches one** and satisfies all the following row tests at once:

$$
 m\ge2,\qquad b\ge 5m+7,\qquad b-m\le B
 \quad\Longrightarrow\quad \operatorname{FullRow}(a,b,m).
$$

The theorem supplies an ordinary hitting time $B+e$. It includes arbitrary finite lists of sufficiently large $b$ with $m=\lfloor b/12\rfloor$. The gate depends on the list. This proves that the quantifier order in the proposed convergence criterion matters, even when every test in a finite collection uses the same gate. [Lean theorem `converging_gate_full_through`](SynchronousShadow.lean)

## Construction

Let $u$ be a positive integer. The ordinary start $a=6\cdot2^Bu-1$ takes $B$ consecutive shortcut steps at odd states. After $i\le B$ steps it is at $6\cdot2^{B-i}3^iu-1$, which is odd, above two and congruent to two modulo three. Choose $u$ so that the value at $i=B$ takes a single odd-to-odd gap to one. The ternary lifting argument below ensures this is possible. For a suffix of length $n=b-m\le B$, the suffix clock is exactly $n$. The prefix has $2b-n=b+m$ clocks available. This meets the proved $6m+7$ bound, so every prescribed prefix word has a completion. The same $a$ works for every allowed pair.

## Entire families of paths can be copied into a specified orbit

Fix an ordinary positive odd endpoint $q$, a positive odd target $t$ coprime to three, and nonnegative $b,S,K$. Lean constructs positive integers $e,d$ satisfying

$$
 q'=q+2\cdot3^{b+K}d,\qquad 3q'+1=2^e t,\qquad
 e\le 2q+2\cdot3^{b+K}+2 .
$$

Every ordinary path of $b$ odd steps and $S$ shortcut steps from $x$ to $q$ has a path with the **identical ordered list of gaps** from

$$
 x'=x+2^{S+1}3^K d
$$

to $q'$. The same shift works simultaneously for every such path, with no bound on the family size. Pairwise differences of sources and each path's integer affine carry $2^S q-3^b x$ are therefore preserved. Relative carries change by the common factor $q/q'$. Taking $t=1$ gives ordinary paths known to converge. These paths generally have much larger sources and endpoints. [Lean theorems `one_gap_cylinder` and `simultaneous_shadow`](SynchronousShadow.lean)

For the last gap, an odd unit $t$ has a predecessor $z$ with $3z+1=2^f t$. Increasing $f$ by two replaces $z$ by $4z+1$, so a predecessor greater than $q$ is available. The elementary identity $4^{3^k}=1+3^{k+1}(1+3w)$ follows by induction and cubing. Consequently increasing $f$ by $2\cdot3^k$ changes $z$ by $3^k v$, with $v\equiv1\pmod3$. Zero, one or two such increments match the next ternary digit of $q$. The total extra exponent through $n$ digits is at most $2(3^n-1)$. This argument uses no distribution hypothesis.

## Why a smaller copy eventually disappears

For two realizations of the same gap list with ordered sources $x\le y$ and odd endpoints $q,r$, Lean proves that every difference has the exact form

$$
  y-x=2^{S+1}d,\qquad r-q=2\cdot3^b d,\qquad d\ge0.
$$

The affine carries agree, $2^S$ and $3^b$ are coprime, and the difference of the odd endpoints is even. In particular, once $x\le 2^{S+1}$, there is no smaller positive source following that same list of gaps. The argument leaves open mergers with different lists of gaps, different depths, or different clocks. [Lean theorems `translation_necessary` and `frozen_prefix`](SynchronousShadow.lean)
