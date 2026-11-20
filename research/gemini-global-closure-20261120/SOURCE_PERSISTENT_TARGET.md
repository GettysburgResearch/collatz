# A source-persistent occupation target and the meaning of strong stability

**Status: PROPOSED conditional closing criterion.** The inequalities below are
proved from the existing rank-counting interface and exact deterministic
pushforward. The required occupation estimate is **OPEN**. This does not prove
Collatz or exclude a nontrivial cycle, and it is not a new rank-counting result.

Use precisely the `A,R,G,U,B,H` and

\[
\psi(n)=1+\log\log(R(n)+6)
\]

of `ACTUAL_TRANSPORT.md`. The source rank estimate is `T-A3-1001` in
[`RANK_MOMENTS.md`](https://github.com/GettysburgResearch/collatz/blob/ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a/research/astra-three-routes/pass5/RANK_MOMENTS.md):

\[
N_R(X)=\#\{n\ge2:R(n)\le X\}<9\sqrt X\quad(X\ge1).                 \tag{1}
\]

Its resident source/review qualifications are retained. All logarithms are
natural. Let `f>=0` be a **fixed** finite input with finite psi-moment, and put
`mu_N=N^(-1) sum_(j=0)^(N-1) H^j f`. Let `D` be the set of unsafe starts whose
`B` orbit is never absorbed and is not eventually periodic.

## SP-001 — every nonperiodic initial atom has a quantitative occupation cost

For `N>=1`, define

\[
L_N=\frac1N\sum_{i=1}^N
 \left[1+\log\log\left((i/9)^2+6\right)\right].                    \tag{2}
\]

Then the actual transported mass satisfies the direct inequality

\[
\boxed{\quad \|\mu_N\|_\psi\ \ge\ L_N\sum_{u\in D}f(u).\quad}    \tag{3}
\]

Moreover,

\[
\frac{L_N}{\log\log N}\longrightarrow1.                            \tag{4}
\]

**Proof.** An orbit of a deterministic map which repeats a state is eventually
periodic. Thus, for each `u in D`, its first `N` unsafe states are distinct.
Sort their ranks as `rho_1<=...<=rho_N`. At least `i` ordinary states have rank
at most `rho_i`, so (1) implies `rho_i>(i/9)^2`; all these ranks are at least
one, as required by (1). Monotonicity of psi gives

\[
\frac1N\sum_{j=0}^{N-1}\psi(B^j u)\ge L_N.                         \tag{5}
\]

Exact pushforward accounting and nonnegativity now give

\[
\|\mu_N\|_\psi
 =\sum_u f(u)\frac1N\sum_{\substack{0\le j<N\\B^j u\text{ retained}}}
          \psi(B^j u)
 \ge \sum_{u\in D}f(u)L_N.
\]

Possible mergers between different sources cause no problem: their masses add,
and distinctness was used separately along each single original orbit.

For (4), monotonicity bounds `L_N` above by the last summand in (2). For a
lower bound take `k=ceil(sqrt(N))` and retain the summands with `i>=k`:

\[
L_N\ge\frac{N-k+1}{N}
       \left[1+\log\log\left(N/81+6\right)\right].                \tag{6}
\]

Both this bound and the last summand, divided by `log log N`, tend to one.
This proves (4). □

### The concrete sufficient estimate

If `f(u)>0` for **every** unsafe ordinary state, then

\[
\boxed{\quad \frac1N\sum_{j<N}\|H^j f\|_\psi
                     =o(\log\log N)\quad}                         \tag{7}
\]

would force `D` to be empty. Every positive ordinary orbit would then be
eventually periodic: a nonperiodic Collatz orbit visits `U` infinitely often,
because an eventual safe tail would force indefinite positive-integer rank
descent. Its unsafe subsequence would belong to `D`, a contradiction.

Combining (7) with exclusion of nonabsorbing finite `B` cycles would prove
Collatz. This is weaker than demanding a uniform bound for the Cesaro
psi-moments in `ACTUAL_TRANSPORT.md`, but it is still unproved. The existing
additive horizon budget gives only `O(N)` for the left side of (7), and so
does not approach the needed order. No statement of fresh-parity independence
or a changing family of finite witnesses is used in (3).

## SP-002 — basis absorption and weighted strong stability are different targets

For `j>=0`, deterministic pushforward gives the exact operator norm

\[
\|H^j\|_{\ell^1(\psi)\to\ell^1(\psi)}
 =\sup_{u:B^j u\text{ retained}}\frac{\psi(B^j u)}{\psi(u)}.       \tag{8}
\]

An empty supremum is zero. Therefore strong stability on this weighted Banach
space—`||H^j f||_psi ->0` for **every** `f in ell^1(psi)`—holds **if and only
if** both of the following statements hold:

1. Every unsafe starting state is eventually absorbed.
2. The peak ratio in (8), maximized over **all** `j`, is finite.

For sufficiency, finitely supported inputs vanish after a finite horizon.
Approximate an arbitrary input by such inputs and use the uniform operator
bound on its remaining tail. For necessity, an unabsorbed point mass has norm
bounded below by `inf_U psi>0`, so the first condition is necessary. If the
second condition fails, choose increasing times `j_k` and sources `u_k` with
`psi(B^(j_k)u_k)/psi(u_k)>=4^k`. Each fixed time has finite operator norm by
the proved additive horizon estimate, so these times can indeed be chosen to
increase. The positive input

\[
f=\sum_{k\ge1}\frac{2^{-k}}{\psi(u_k)}\delta_{u_k}
\]

has finite psi-norm, but `||H^(j_k)f||_psi>=2^k`. This contradicts strong
stability and proves necessity without any assumption about distinct sources.

Condition 2 is a substantive **uniform excursion bound**. If its constant is
`M`, it says explicitly that every retained return satisfies

\[
R(B^j u)+6
 \le \exp\!\left(e^{M-1}[\log(R(u)+6)]^M\right).                    \tag{9}
\]

The existing `O(j)` operator-norm estimate does not give (9). Pointwise
termination by itself should not be presented as a proof of this weighted
strong-stability assertion.

On **unweighted** `ell^1`, in contrast, `||H^j||<=1` automatically. There,
strong stability is exactly equivalent to absorption of every ordinary point
mass. The full-support unweighted argument in `ACTUAL_TRANSPORT.md` therefore
uses the appropriate topology for its claimed conclusion.
