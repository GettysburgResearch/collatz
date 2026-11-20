# An exact kernel after four certified odd inputs

**PROPOSED.** This note uses the ordinary positive shortcut map
`T(n)=n/2` for even `n`, and `T(n)=(3n+1)/2` for odd `n`.
Write `C` for its basin of 1, and `a ~ b` when the two ordinary
orbits meet. A finite certificate, and not mere membership in an
auxiliary graph, is the input to every transfer below.

The source is PR146 at
`e238c63a5d57f96bb063b7472498d1977df51951`,
`research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`.
It proves that full Collatz convergence is equivalent to

\[
128k+1\in C\implies64k+1\in C
\qquad(k>0,\ 4\nmid k).                                      \tag{D}
\]

The source also identifies the minimum rank-four subproblem with
convergence of all `3^(27j-1)`, `j>=1`. That result and its unbounded
first-descent clocks are not new claims here. The additional object
in this note is an exact classification of what remains after the
first four certified odd inputs, including a complete rank-five
specialization. No general kernel implication is proved.

## K1. Four-input normal form

Put `X=128k+1`, `Y=64k+1`. Three consecutive odd-even pairs give

\[
T^6X=54k+1=:w,
\qquad T^6Y=27k+1=(w+1)/2.                                \tag{1}
\]

Let

\[
c=v_2(162k+4),\qquad z=(162k+4)/2^c.
\]

Then `z` is a positive odd ternary unit, `T^(c+6)X=z`, and

\[
X=\frac{2^{c+6}z-175}{81},\qquad
Y=\frac{2^{c+5}z-47}{81}.                                \tag{2}
\]

The index condition `4 ∤ k` is equivalent to `c=1` or `c>=3`.
Precisely:

* `c=1` gives `z ≡ 83 (mod 162)` and `k=(z-2)/81` is odd.
* For `c>=3`, `z` is odd and `2^(c-2)z ≡ 1 (mod 81)`;
  then `k=2(2^(c-2)z-1)/81 ≡ 2 (mod 4)`.

Conversely every displayed admissible `(c,z)` gives a positive
`k` with `4 ∤ k` and exactly that fourth valuation. For `c=1`,
the smallest admissible `z` is 83. For `c>=3`, the expression
`2^(c-2)z-1` is positive. Thus there is no omitted nonpositive
source. Every one of the first four odd inputs of `X` is greater
than 1. Consequently, if `z` is certified, the first-hit odd rank
of `X` is exactly `4+r(z)`.

**Proof.** The identity `T^2(4v+1)=3v+1` proves (1).
Substituting `54k+1=(2^c z-1)/3` gives (2). If `k` is odd then
`162k+4 ≡ 2 (mod 4)`. If `k ≡ 2 (mod 4)`, its valuation is at
least three; if `4 | k`, its valuation is exactly two. Solving
for `k` gives the congruences and their converses. All the
asserted ordinary paths follow the actual parities, rather than
just their affine formulas.

## K2. The three residual certificate obligations

For these same starts the following are exact ordinary identities.

**The odd-index case `c=1`:**

\[
T^7Y=(z+1)/6.                                             \tag{3}
\]

**The even-valuation case `c=2r+4`, `r>=0`:**

\[
T^{c+6}Y=T(3^r z)=\frac{3^{r+1}z+1}{2}.                  \tag{4}
\]

**The odd-valuation case `c=2r+3`, `r>=0`:**

\[
T^{c+4}Y=2\,3^r z+1.                                    \tag{5}
\]

It follows that (D), and hence full Collatz, is equivalent to the
conjunction of the following implications on certified positive
odd `z`:

\[
\begin{array}{ll}
\mathrm{A}:&z\equiv83\pmod{162},\ z\in C
       \implies(z+1)/6\in C;\\[2mm]
\mathrm{B}:&r\ge0,\ 4^{r+1}z\equiv1\pmod{81},\ z\in C
       \implies3^r z\in C;\\[2mm]
\mathrm{C}:&r\ge0,\ 2\,4^r z\equiv1\pmod{81},\ z\in C
       \implies2\,3^r z+1\in C.
\end{array}                                               \tag{6}
\]

The new statement is an equivalence and exact source-preserving
normal form, not an unconditional proof of A, B, or C. The B
case `r=0` is proved: it simply retains the given certificate of
`z`. In particular every source in (D) whose fourth valuation is
four admits a literal merger and a complete certificate transfer.

**Proof of the paths.** When `c=1`, the endpoint in (1) is
`(z+1)/3`, an even integer. This proves (3). For `c>=3`, it is
odd, and one more step gives

\[
T^7Y=2^{c-2}z+1.                                        \tag{7}
\]

For every integer binary exponent `b>=2`, two further steps replace
`2^b v+1` by `3*2^(b-2)v+1`. In the odd case, `r` such pairs
give (5). In the even case, `r+1` such pairs give
`3^(r+1)z+1` at clock `c+5`; one halving proves (4).
The ordinary merger in (4) proves equivalence of convergence of
its two arms, including the reverse implication. Equation (2)
and the supplied ordinary prefix show `X in C` exactly when
`z in C`, which proves both directions of (6).

## K3. Complete rank-five parameterization

Suppose the upper arm has exactly five odd inputs before its
first arrival at 1. The endpoint `z` in K1 has exactly one, so

\[
z=(2^a-1)/3,\qquad a\ge4\text{ even}.                    \tag{8}
\]

The complete odd-gap word of `X` is `(2,2,2,c,a)` with
`c=1` or `c>=3`, and

\[
X=\frac{2^{a+c+6}-525-2^{c+6}}{243}.                      \tag{9}
\]

For `c=1` the condition is `2^a ≡ 7 (mod 243)`.
For `c>=3` it is

\[
2^{c-2}(2^a-1)\equiv3\pmod{243}.                        \tag{10}
\]

For each fixed allowed `c` there is one even residue of `a`
modulo 162. If it is 2, omit `a=2`, which has rank four;
all subsequent positive representatives have rank five.
Indeed 2 generates the units modulo 243: its order is
`2*3^4=162`, from
`v_3(2^(2*3^j)-1)=j+1`. The right side after rearranging (10)
is a unit, so one residue exists; reduction modulo 3 forces
the residue to be even. The forbidden residue zero cannot
satisfy (10), and cannot satisfy the `c=1` condition either.

For `c>=3`, two steps after (1) give the particularly short
rank-five identity

\[
T^8Y=2^{c-3}(2^a-1)+2.                                  \tag{11}
\]

Thus the entire rank-five question is a two-parameter ordinary
family with an explicit congruence, not an unconstrained search
through stopping words.

### Four exact infinite subfamilies

The following table uses `j>=0` throughout.

| Fourth gap `c` | Last gap `a` | Exact residual convergence question |
|---:|---:|---|
| 1 | `162j+70` | `3^(81j+32) in C` |
| 3 | `162j+22` | `3^(81j+10) in C` |
| 4 | `162j+68` | Always true; `T^8Y=2^(a+1)` |
| 5 | `162j+118` | `2^(162j+119)-1 in C` |

The congruences follow by exact modular powers modulo 243.
For `c=4`, both first-hit ranks are exactly five: the upper
word is prescribed, and the lower uses three odd inputs in
the first six clocks, then two more before the displayed
positive power of two. No previous state is 1.

For `c=5`, (11) is `2(2^(a+1)-1)`, so one halving gives the
Mersenne start. For `c=3`, (11) is `2^a+1`. For `c=1`, (3)
and three further actual steps give `T^10Y=2^(a-4)+1`.

For every even `h>=2`, ordinary cycle shadowing gives

\[
T^h(2^h+1)=3^{h/2}+1,
\qquad
T^{h+1}(2^h+1)=T(3^{h/2-1}).                            \tag{12}
\]

For completeness, the first identity follows by induction from

\[
T^i(2^h+1)=T^i(1)+2^{h-i}3^{\lceil i/2\rceil},
\qquad0\le i\le h.
\]

Before the last clock the difference is even, so the actual
parities agree with the cycle from 1. Substituting `h=a` or
`h=a-4` into (12) proves the two pure-power rows.

## Why the apparent rank reduction does not finish induction

K1 removes four certified odd inputs, but K2 changes the target
problem. A would require an unproved closure under `(z+1)/6`
on its indicated class. B introduces an unbounded multiplier
`3^r`; C introduces both such a multiplier and a new additive
term. None follows just from the shorter certificate for `z`.

In particular the known-rank-zero instance of B is already
load-bearing. Setting `z=1` forces `r+1 ≡ 0 (mod 27)` and
asks for every `3^(27j-1)` to converge. This is exactly the
minimum-rank obstruction identified by PR146. It must be
proved as a base case before any induction claiming to use B.
The two other pure-power progressions and the Mersenne row
in K3 likewise have no complete proof here.

Numeric decrease of `(z+1)/6` is not a certificate for it:
only `z`, not every smaller positive integer, is assumed
certified. A global least-counterexample argument must keep
its original least source, since the critical edge supplied
by the directed reduction can occur at a larger integer.
This is the first unsupported step in the attempted induction.

The identities give a complete transfer when `c=4`, exact
residual problems for every other `c`, and a complete next-rank
classification. They do not prove full Collatz convergence.
