# Ternary residues at record clocks on one ordinary orbit

Write $a_k$ for the $k$-th odd iterate of a positive odd integer coprime to three, and $s_k$ for its elapsed shortcut clock. Suppose that this particular orbit never repeats. For $u>v>0$, record an index $k>0$ whenever $uk-vs_k$ strictly exceeds its value at every earlier index, including zero. Every recorded terminal satisfies

$$
 v(s_k-s_i)<u(k-i)\qquad(0\le i<k).
$$

The following lower temporal densities hold simultaneously on the supplied orbit. The last column counts terminal classes modulo $3^8=6561$ compatible with eight successive backwards suffix inequalities. There are 4374 ternary unit classes.

| Slope $u/v$ | Lower density of record times | Compatible unit classes at depth eight |
|---|---:|---:|
| $8/5$ | $1/41$ | 104 |
| $18/11$ | $23/287$ | 143 |
| $2$ | $17/41$ | 403 |

The three class counts are exact kernel reductions. The second row forces at least 8.01% of all odd times into a specified 3.27% of the depth-eight unit classes. The third forces at least 41.46% of all odd times into 9.21% of the classes. The same record times satisfy the constraints at every available depth. [Lean proof, executable residue lists and counts](EscapeFrontier.lean)

## Finite count and passage to one orbit

Each odd gap costs at least one shortcut step. A new record can therefore raise the running maximum by at most $u-v$. If $R_N$ is the number of records through $N$, then

$$
 uN\le v s_N+(u-v)R_N .
$$

For a segment of length $j$ starting at $x$ and ending at $q$, with all odd inputs at least $M$, multiply the exact gap identities to obtain

$$
 M^j2^{s}q\le (3M+1)^j x.
$$

When $q\ge x$, taking $M=2048$ yields $41s\le65j$ by the integer comparison $6145^{41}<2048^{41}2^{65}$. A nonrepeating orbit eventually exceeds every fixed floor. Start the inequality after the last visit below 2048, then wait until every endpoint exceeds that starting value. Thus $41s_N\le65N+O_a(1)$. Substitution into the finite record count gives the table. The Lean statements include explicit existential constants before passing to lower density. [Finite inequalities](EscapeFrontier.lean)

## Ternary concentration in every real phase interval

The following limiting conclusions are written deductions. Let $p=23/287$, $u=18$ and $v=11$. For integers $T\ge0$ and $b\ge1$, let $E_{T,b}$ be the union of the terminal residue cylinders of depth $b$ from positive gap words satisfying $v s_j\le uj+(u-v)T$ at **every** backwards depth $1\le j\le b$. One word determines one terminal residue modulo $3^b$ by its affine identity. The depth cylinders project into the preceding depth cylinders by dropping the earliest chronological gap. Put $E_T=\bigcap_b E_{T,b}$ and $E=\bigcup_{T\ge0} E_T$.

For $L=\lfloor(ub+(u-v)T)/v\rfloor$, the number of positive words of length $b$ and total at most $L$ is $\binom{L}{b}$, by recording the increasing partial sums. Applying the binomial theorem at $11/7$ gives

$$
 \binom Lb\le (18/7)^{7T/11}\Lambda^b,
 \qquad \Lambda=\left(\frac{18^{18}}{11^{11}7^7}\right)^{1/11}<3.
$$

It follows that $E$ has ternary Haar measure zero. Along any nonrepeating orbit, let $\nu$ be any weak subsequential limit of the empirical measures of $(a_k,\{\log_2 a_k\})$ on the ternary units times the circle. For every open arc $I$,

$$
                 \nu(E\times I)\ \ge\ p\,|I|.
$$

Indeed the log phase turns by $\log_2 3+\log_2(1+1/(3a_k))\pmod1$. The error tends to zero on this orbit. For each fixed window length $T$, sufficiently late windows therefore approximate the corresponding irrational rotation uniformly in all $T$ positions. Given $\epsilon>0$, choose a closed interior arc $J\subset I$ and then a finite $T$ so that every sufficiently late window of $T$ consecutive odd times has at least $(|I|-\epsilon)T$ phases in $J$. This follows from uniform distribution of irrational rotations, applied first to a smaller interior arc. For every record time $k$, each of those earlier times $h=k-t$, $0\le t<T$, satisfies every incoming suffix budget with allowance $(u-v)T$, since each of the removed gaps cost at least one. This shift inequality is proved in Lean. Each earlier index is counted at most $T$ times. At every fixed depth $b$, the resulting lower frequency in the closed set $E_{T,b}\times J$ is at least $p(|I|-\epsilon)$. Pass to the weak limit and then take the decreasing intersection over $b$. Finally let $\epsilon$ decrease to zero. In particular, every empirical ternary marginal of this orbit has singular mass at least $p$. [Shift inequality](EscapeFrontier.lean)

PR208 bounds the spatial density of sources without crossings. PR209 supplies finite phase grids on individual orbits. The estimate above concerns joint real-phase and ternary occupation on the same hypothetical escaping orbit. A contradiction would follow from an incompatible upper occupation estimate for that orbit. The whole-population estimates leave this upper bound open. [PR208 clock analysis](https://github.com/GettysburgResearch/collatz/blob/72635b2a3af2f5b6cbf4eeff7ce1c89b6e6a5f7f/research/openai-machinery-20261125/clock/README.md) · [PR209 proof packet](https://github.com/GettysburgResearch/collatz/blob/2d0230aa52d85732dbc85b5df20e30108dc1396f/research/astra-ultra-closure-20261125/README.md)
