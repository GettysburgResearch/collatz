# Grade minima and the complete nonpositive sector

**Status: PROPOSED, unconditional written proofs.** Map and conventions are in
[README.md](README.md). Let `P` be the positive integers reaching 1 under the
shortcut map. Nothing below assumes `P` is all positive integers.

## FB-001: the invariant of a balanced merger

For `n in P`, let `tau(n)` be the first clock reaching 1 and `q(n)` the number
of odd inputs before that visit. Define `g(n)=2q(n)-tau(n)`. For every `h>=0`,

\[
 g(n)=2s_h(n)-h+g(T^h(n)).                                      \tag{1}
\]

For `h<=tau(n)` this follows by splitting the first-arrival path. Each full
lap of `1 -> 2 -> 1` adds two steps and one odd input, so the identity also
holds after first arrival. In particular `g(1)=0` and `g(2)=-1`.

**Theorem.** For `m,n in P`, the following are equivalent:

* `g(m)=g(n)`;
* for some common clock `h`, both `T^h(m)=T^h(n)` and `s_h(m)=s_h(n)`;
* these two equalities hold for every `h>=max(tau(m),tau(n))`.

The second condition implies the first by (1). For the converse note that
`tau(n) == g(n) mod 2`. After both first arrivals the common-time endpoints
therefore have the same phase on the two-cycle. Equation (1) then forces
the odd counts to agree. The final implication is immediate.

For `x=1+3w` and a depth `h` with `w<2^h`, the PR #146 filter keeps the least
`w` for each pair `(s_h(1+3w), T^h(1+3w))`. Call `x` **permanent** if it is
kept at every such depth. Let `S=P intersect {n:n==1 mod 3}`.

**Corollary.** A member `x` of `S` is permanent if and only if

\[
 x=\min\{m\in S:g(m)=g(x)\}.                                  \tag{2}
\]

If a smaller source ties its pair at any depth, that source reaches 1
because its common future does, and (1) gives the same grade. Conversely,
any smaller member of the grade class ties the pair at every sufficiently
large depth by the theorem. Its index is also eligible whenever `x` is.
Thus a smaller nonconvergent source cannot be a hidden exception to (2): a
common finite endpoint with `x` would itself prove its convergence.

This is a classification by actual first-arrival data, not an algorithm that
decides convergence of unknown smaller sources. Minima for grade classes not
known to occur are not asserted to exist.

## FB-002: a sharp gap above the powers of two

Multiply the exact input/output ratios over the first-arrival path. Even
inputs contribute 2. At odd input `z` the ratio is `2z/(3z+1)`. Rearranging
gives

\[
 n2^{g(n)}=\prod_{\substack{z\text{ odd input}\text{ before first }1}}
                    \frac{4z}{3z+1}.                         \tag{3}
\]

Every factor exceeds 1. An empty product occurs exactly when `n` is a
power of two. Consequently `n>=2^{-g(n)}`, with equality precisely for
powers of two.

If `n` is not a power of two, let `z` be the last odd input before first
arrival. All subsequent inputs before 1 are even, so `3z+1=2^a`.
Reduction modulo 3 forces `a` even. Since `z>1`, `a>=4` and `z>=5`.
The function `4z/(3z+1)` is strictly increasing on positive `z`, whence

\[
 n2^{g(n)}\ge\frac{4\cdot5}{3\cdot5+1}=\frac54.                \tag{4}
\]

Equality requires `z=5` and no other odd input before first arrival, since
every other factor would be strictly larger than 1. Thus equality holds
exactly for `n=5*2^j`, `j>=0`. Conversely every such start first halves to 5
and follows `5 -> 8 -> 4 -> 2 -> 1`, so equality holds and `g(n)=-2-j`.
This proves every equality case without an enumeration.

## FB-003: complete classification when the grade is nonpositive

Let `g<=0`.

If `g=-2m` is even, the universal bound from (3) is `n>=4^m`. The lower
bound is attained by `4^m`, which is `1 mod 3` and has grade `-2m`.

If `g=-(2m+3)` is odd and at most `-3`, the power `2^{-g}` is `2 mod 3`.
No power of two in `S` has this grade. Equation (4) therefore gives

\[
 n\ge\frac54\,2^{2m+3}=10\,4^m.
\]

This lower bound is attained: `10*4^m == 1 mod 3` and is an equality case
of (4), with exactly the required grade.

For the one remaining grade `g=-1`, the start 7 has the path

`7,11,17,26,13,20,10,5,8,4,2,1`.

Its 11 steps have five odd inputs, so its grade is `-1`. The only smaller
positive `1 mod 3` starts are 1 and 4, of grades 0 and `-2`. Hence 7 is the
minimum for this grade.

Applying (2) proves that the permanent members of `S` with grade at most
zero are exactly `4^m`, `10*4^m` for `m>=0`, and 7. This statement includes
the exclusion of every other convergent nonpositive-grade start from
permanent survival; it does not just provide examples.

## FB-004: the upper-bit obligations of this sector

For a start `x=1+3w`, its eligible pairs are

\[
              x,\quad x+3\,2^h,\qquad 2^h>w.                  \tag{5}
\]

Since every start in the classified sector reaches 1, such a pair merges
exactly when its upper arm reaches 1. Write `H` for convergence of

\[
        3^a+1\ (a\ge1),\qquad 3^a+2\ (a\ge2).                \tag{6}
\]

The pairs based at `x=1` already make `H` necessary. Indeed
`T^2(1+4u)=1+3u`. If `h=2r`, the upper arm `1+3*2^h` reaches
`1+3^{r+1}` after `2r` steps. If `h=2r+1`, it reaches
`1+2*3^{r+1}` after `2r` steps, then `2+3^{r+2}` one step later.
Every exponent specified in (6) occurs.

We prove sufficiency for the rest of the classified sector.

### Powers of four

For `x=4^m`, `m>=1`, eligibility means `h>=2m-1`. At the first value of
`h`, the upper arm is `5*2^{2m-1}` and reaches 1. At `h>=2m`, removing
`2m` initial halvings gives `1+3*2^{h-2m}`, one of the row-1 arms above.

### The second infinite family

For `x=10*4^m`, eligibility means `h>=2m+2`. Remove `2m+1` initial
halvings from the upper arm to obtain

\[
                       5+3\,2^\ell,\qquad \ell=h-2m-1\ge1.
\]

For `ell=1,2,3`, this gives 11, 17, 29, respectively. Their finite
first-arrival paths are included in the checker.

For `ell>=4`, the four-step path from 5 has one odd input and endpoint 1.
The parity-prefix identity gives

\[
 T^4(5+3\,2^\ell)=1+9\,2^{\ell-4}.
\]

Write `ell-4=2r+e`, `e in {0,1}`. A further `2r` steps give
`1+2^e*3^{r+2}`. For `e=0` this is in the first family (6); for `e=1`
one more odd step gives `2+3^{r+3}`, in the second.

### The isolated start 7

Here eligibility means `h>=2`. For `h=2,...,10`, the upper arms are
`19,31,55,103,199,391,775,1543,3079`. Each reaches 1; the exact finite
replays are in `check.py`.

For `h>=11`, the first-arrival path of 7 has five odd inputs, hence

\[
 T^{11}(7+3\,2^h)=1+3^6\,2^{h-11}.
\]

Writing `h-11=2r+e` and repeating the two-step identity gives either
`1+3^{r+6}` or, after one more odd step, `2+3^{r+7}`. These are again
covered by (6). Thus `H` is necessary and sufficient for all pairs in
the entire classified sector. The original powers-of-four reduction is
credited to PR #146; the argument here extends it to the complete
nonpositive-grade sector.

## A clock lag does not remove the lifting obligation

Every two members of `P` merge after their respective first-arrival clocks;
once on the two-cycle, a clock difference of at most one suffices. However,
a high-bit identity at a fixed depth has slope `3^{s_h(x)}` in its higher
binary input. A merger of the base integers without matching odd counts
does not equate these slopes. It therefore does not justify replacing a
prefix in all of its higher lifts. The classification above exposes this
precise distinction.

## Dependencies and remaining work

The proofs use elementary shortcut arithmetic and unique binary parity
prefixes. They do not use a predecessor-density theorem, stationary inverse
policies, a random model, or the qualitative synchronization theorem.
Source pins: main `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`; PR #146
`92820dd336b010215eb8a6eb4878a31b58a67656`; the prior branch-count discussion
in PR #145 is pinned at `dd245a712f985909f541590e3f6c179b7ba011e4`.

The first unsupported step of any proposed resolution through this packet
is still a claim that every required shifted-power upper arm reaches 1,
or a new complete selector handling all remaining ordinary pairs.
Positive-grade minima, unknown nonconvergent lower arms, and representatives
retained at finite depths are not removed by the nonpositive classification.
