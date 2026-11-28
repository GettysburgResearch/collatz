# Negative translations cost only linear time; a positive nonperiodic test

At nonzero signed slope gap orient the physical arms as $B=3^jA-a$ with $j>0$. At $j=0$ use the original ordering. Consider an actual positive odd source $s$ and $3s$, unmerged through native date $k$, with combined odd grade $G$. An adjacent return word, starting from $A-B=1$, has the same signed line and clock bounds. The rounding and ternary-digit conclusions below concern its positive ordinary integer realizations.

**Proposed sign exclusion.** The total number of dates through which the input line has $a<0$ or $j=0$ is at most $2G+1$. The count includes arbitrary sign changes, orientations and common-even waits. Thus the entire contribution of negative rational diagonal centers is linear, regardless of the size and prime factors of their denominators.

Indeed use
$$
                    V=\max(1,\ |a|/3^j,\ -a).
$$
At $j=0$ this equals $|a|$ and thus is invariant under interchanging arms. At positive $a$ it equals the archimedean potential $\max(1,|a|/3^j)$, which grows by at most a factor two per active date (at least one odd letter) by the [occupation theorem](ARCHIMEDEAN_CLOCK_OCCUPATION.md). The oriented updates U,D,E,O preserve positive $a$ until a possible arm exchange at zero level. If $a<0$ stays negative, then $V=|a|$, an E halves it, and any active step satisfies $2|a'|\le4|a|$: an up step gives $3|a|+1$, and the down and common-odd formulas subtract a nonnegative offset from $|a|$ or $3|a|$. A sign change from negative to positive obeys $V'\le2V$ by the archimedean bound. These cases also cover the optional exchange at zero because the starting value of $V$ there is independent of orientation. On any common-even step at $a<0$ or at $j=0$, the nonzero even integer $a$ is halved, hence so is $V$ exactly. The starting potential after the mandatory first ordinary step, and at the adjacent base, equals one. Its total logarithmic decrease in base two is bounded by its total increase, at most $G$. Thus at most $G$ of the specified dates are common even; all other specified dates consume at least one of the $G$ odd letters. The extra one allows the initial date of the ordinary source pair.

Combining the sign exclusion with (1) of the occupation theorem, on any hypothetical sequence $k/(G\log(2+G))\to\infty$, for every fixed $C>0$ a proportion tending to one of **all** native dates satisfies the one-sided ordinary integer relation
$$
              0<A-\frac B{3^j}<G^{-C},\qquad A=\left\lceil B/3^j\right\rceil.
$$
In particular the higher-place portion of the $j$ low ternary digits of $B$ begins with at least $\lfloor C\log_3 G\rfloor$ twos. Indeed $0<a<3^j/G^C$ and $B\bmod 3^j=3^j-a$. At all but another $O(G\log(2+G))$ dates the scalar phase [identified by the common native word](SIMPLE_LINE_CYCLES_AND_SHADOWS.md) is a genuine **positive** rational $a/(3^j-1)$ of this small real size. A factor of at most $3/2$ in its size is absorbed by starting with a slightly larger $C$.

## Clearing a power of three from a positive rational denominator

For $n\ge1$, $m\ge1$, $3\nmid m$, let $\tau(n,m)$ be the first native date at which the shortcut orbit of $m/3^n$ becomes an integer. At each odd step a denominator factor three is removed, and at each even step the same denominator remains reduced. For $h>0$ the normalized numerator and current denominator exponent update by
$$
 (h,d)\longmapsto
 \begin{cases}
 (h,d/2), &d\ {\rm even},\\
 (h-1,(d+3^{h-1})/2),&d\ {\rm odd}.
 \end{cases}                                                          \tag{1}
$$
For $h>1$ the odd-case numerator remains prime to three; at $h=1$ no further coprimality is needed. A nonzero positive numerator has only finitely many consecutive even halvings. Therefore $\tau$ is finite for every such input and occurs on exactly the $n$th odd step. Define
$$
               J(n)=\max_{\substack{1\le m\le3^n\\3\nmid m}}\tau(n,m).
$$

**Proposed realization.** There is an absolute $C_0$ such that $J(n)\le K(C_0(n+1))$ (round up the budget). In particular $J(n)=o(n^2)$ by the [ordinary subquadratic clock](SPARSE_DISCREPANCY_BLOCKS.md). A family with $J(n)/(n\log(2+n))$ unbounded would refute the uniform logarithmic clock law. This test only uses halving and addition of a descending list of powers of three. The tested rational trajectories cannot be repeated nonintegral periodic orbits.

For the proof, the [universal affine entrance](UNIVERSAL_RATIONAL_MERGERS.md) realizes $B=3^nA-m$ on a positive ordinary source cylinder at cost $O(n+\log(2+m))=O(n+1)$ in both native time and grade. Refine $A$ to the residue of $m/3^n$ modulo $2^{\tau(n,m)}$. Then $B$ performs only even steps, and $A$ performs the exact rational parity word through the first integral landing $N>0$. At every date until landing, if the lower arm has so far taken $g$ odd steps, the new normalized line is $B'=3^{n-g}A'-d$, with $d/3^{n-g}$ the current rational state from (1). This follows either from the update formula or by evaluating the two affine maps at the particular lower input $m/3^n$, where the upper input is zero. At landing the exact line is $A'-B'=N$. Thus the terminal states differ on **every** ordinary lift of this longer word; determinism excludes any earlier same-date merger, including during entry. The new interval contributes only $n$ odd letters in total. If $N=1$ and the entrance begins at translation one, this is itself a closed adjacent word.

Conversely suppose $J(n)=O(n\log(2+n))$. This suffices for every **single interval before the first return to zero slope gap** with positive oriented translation, higher-slope arm entirely even, and original total grade budget $G$ through its ending date. Indeed its input is a line $B=3^j A-a$ with $H=j+\log_2(2+|a|)=O(G+1)$ by the native determinant bound. As long as the upper arm stays even while $j>0$, the lower bit is the actual bit of $a/3^j$, since $A\equiv a\bmod2$. Its real state and its normalized numerator then obey (1). If the initial rational is greater than one, let the first visit to $(0,1]$ or the integral landing end the initial part. Its ending state is at least $1/2$ because the preceding state exceeds one, unless the initial part is empty. While the rational is greater than one, an odd step contributes a factor at most four to $2x'/x$ and an even step a factor one. This costs at most $2j+\log_2^+(a/3^j)+1=O(H+1)$ dates. Any remaining portion is bounded by $J(h)$ for some $1\le h\le j$. Thus the whole interval costs $O((G+1)\log(2+G))$. The converse argument here concerns one such interval; it does not sum the entry height anew at each of many successive intervals.

## Exact periodic copying is limited on this test

Take any nonempty native word $W$ of length $\ell$ and grade $p\ge1$, with nonnegative carry $C$, and put $D=2^\ell-3^p$. Suppose $r$ complete copies occur on the rational trajectory before or through its first integral landing, beginning at a state $b/3^h$ in lowest terms with $h>0$. At the end write the state as $b'/3^{h-rp}$. Iteration of the affine word centered at $C/D$ gives the exact integer identity
$$
        2^{r\ell}\big(D b'-3^{h-rp}C\big)=D b-3^h C .                   \tag{2}
$$
The bracket is nonzero. Otherwise the beginning state would be the rational word center, whose reduced denominator divides $D$ and is prime to three; this contradicts its reduced denominator $3^h>1$. For an initial input $m\le3^n$ every intermediate numerator is at most $3^n$ by (1), since each active update averages the previous numerator with $3^{h-1}$. The native bounds $|D|\le 3^\ell+2^\ell$ and $0\le C\le2^\ell3^p$ then give
$$
                         (r-1)\ell\ll n+\ell
$$
uniformly even when the copied motif and its odd grade vary. In particular no bounded number of powered motifs of total defining length $O(n)$ can produce more than $O(n)$ dates on this landing test. Unstructured or increasingly many motifs remain possible. No superlogarithmic example for $J(n)$ is asserted.
