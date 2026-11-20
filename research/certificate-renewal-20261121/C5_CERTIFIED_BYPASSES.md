# Two strictly smaller certified bypasses in the fourth-gap-five family

**PROPOSED elementary theorem, with a complete proof and an independent exact-affine checker.** This is a new pair of height descents for the same reverse implication used in PR146. It covers two infinite arithmetic progressions; it does not establish complete coverage or Collatz.

Use the positive shortcut map

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\]

its odd acceleration \(U(n)=(3n+1)/2^{v_2(3n+1)}\), and its actual basin \(C\) of 1. For a positive index \(k\), write

\[
X(k)=128k+1,\qquad Y(k)=64k+1,
\qquad \mathcal C(k):\ X(k)\in C\Longrightarrow Y(k)\in C.
\]

The theorem below uses only direct ordinary arithmetic. The equivalence of universal eligible \(\mathcal C(k)\) with Collatz, and the globally least-failure interpretation, are separate source dependencies.

## Frozen comparison sources

- PR146, `e238c63a5d57f96bb063b7472498d1977df51951`, `research/upper-bit-mergers/DEEP_REVERSE_BASIN.md`: the full-equivalent implication on `k>0`, `4 ∤ k`.
- PR163, `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`, `research/deep-reverse-closure-20261120/REVERSE_CERTIFICATE_KERNEL.md`, K1--K3: the fourth-gap-five residual and the rank-five Mersenne progression.
- The same PR163/SHA, `research/deep-reverse-closure-20261120/MERSENNE_WITNESS_DEPTH.md`, W1--W2: arbitrarily large predecessor depth is required on some actual exponents. The bypasses here do not overturn that theorem: they occupy particular exponent classes and use fifteen odd inputs.
- PR146 latest inspected head `fd991063721e9c157d318e40bb20131762f7d750`, `research/upper-bit-mergers/LEAST_FAILURE_SIEVE.md`: already proves that every arithmetic progression in the rank-five Mersenne exponents has a subprogression excluded under the globally least-failure hypothesis. The two explicit subprogressions below are therefore not the first result of that general kind. The additional content here is an actual paired equivalence `C(k) <=> C(k′)` on whole index classes, with a strictly smaller eligible antecedent and arbitrary-witness conversion; its proof does not invoke the initial-interval constant 176106.
- PR164, `6fa6b429870a9cd53cde0fc77ad64a3c3956199f`, `research/witness-closure-512-2026-11-20/continuation-negative.md`: earlier paired ordinary descents on different parameter classes. The present classes have `k=14 (mod32)`, not the earlier `k=-1 (mod2048)` domain.

## CB1. Two exact parameter contractions

For every integer \(t\ge0\), either row of the following table defines positive eligible indices \(k,k'\), with \(k'<k\):

| Rule | \(k\) | \(k'\) | Equivalent expression |
|---|---:|---:|---|
| A | \(1889568t+1686382\) | \(524288t+467911\) | \((16384k-6049)/59049\) |
| B | \(1889568t+1196494\) | \(1048576t+663969\) | \((32768k-9911)/59049\) |

On each row,

\[
\boxed{X(k)\in C\Longleftrightarrow X(k')\in C,\qquad
Y(k)\in C\Longleftrightarrow Y(k')\in C.}
\tag{CB1}
\]

In particular,

\[
\boxed{\mathcal C(k)\Longleftrightarrow\mathcal C(k').}
\tag{CB2}
\]

This is an equivalence of actual ordinary memberships and of the two implications. It does not assume that either membership holds.

### Domain and strict decrease

Both original indices have `k=14 (mod32)`. Thus

\[
v_2(162k+4)=5,
\]

and the original fourth odd division exponent is exactly five. Both child indices are odd, so both indices satisfy `4 ∤ k` and `4 ∤ k'`. Their source fourth division exponent is exactly one.

In rule A, \(k-k'=1365280t+1218471>0\). In rule B, \(k-k'=840992t+532525>0\). Positivity and strict decrease therefore hold throughout each entire progression, including its first member.

Equivalently the domain of rule A is precisely `k>0`, `k=14 (mod32)`, and `59049 | 16384k−6049`; rule B uses `59049 | 32768k−9911`. The displayed progressions are the Chinese-remainder solutions, because the two moduli 32 and 59049 are coprime.

### Four physical prefixes for each row

Put

\[
z=\frac{81k+2}{16},\qquad m=\frac{243k+14}{8}.
\]

These are positive odd integers. The old source and old target have exact words

\[
X(k)\xrightarrow{(2,2,2,5)}z,
\qquad
Y(k)\xrightarrow{(2,2,2,1,2)}m.
\tag{CB3}
\]

For rule A the new source and target have exact words

\[
\begin{split}
X(k')&\xrightarrow{(2,2,2,1,2,1,2,1,2,2,3,1,3,1)}z,\\
Y(k')&\xrightarrow{(2,2,3,1,1,1,1,1,1,1,2,2,2,1,2)}m.
\end{split}
\tag{CB4A}
\]

For rule B they have exact words

\[
\begin{split}
X(k')&\xrightarrow{(2,2,2,1,1,3,2,1,2,2,3,1,3,1)}z,\\
Y(k')&\xrightarrow{(2,2,4,1,1,1,1,1,1,1,2,2,2,1,2)}m.
\end{split}
\tag{CB4B}
\]

Every arrow lists accelerated odd division exponents in forward order. The old source has four odd inputs and total division exponent 11; its new counterpart has fourteen odd inputs and total exponent 25 for rule A or 26 for rule B. The old target has five odd inputs and total exponent 9; its new counterpart has fifteen odd inputs and total exponent 23 or 24. Thus each rule adds exactly ten odd inputs on both legs; the shortcut clocks on both legs increase by 14 in rule A, or 15 in rule B.

### A fully finite algebraic proof of every infinite prefix

Let \(P=m+1=(243k+22)/8\). It is an integer divisible by four on both domains. Write `q=15`, and use the following exact constants:

| Rule | \(S\) | \(C_s\) | \(C_t\) | \(P\bmod3^{15}\) |
|---|---:|---:|---:|---:|
| A | 24 | 219936533 | 94405205 | 8177135 |
| B | 25 | 386197525 | 169147093 | 7645694 |

The child pair is exactly

\[
X(k')=\frac{2^S P-C_s}{3^{15}},\qquad
Y(k')=\frac{2^{S-1}P-(C_s-3^{15})/2}{3^{15}}.
\tag{CB5}
\]

The target word has total exponent \(S-1\) and affine correction \(C_t\). Its correction and the source correction satisfy

\[
C_s=2C_t+3^{15}+2^S.
\tag{CB6}
\]

Consequently, applying its fifteen indicated odd steps gives exactly \(P-1=m\).

For the source word, include its fourteen displayed steps and a formal last odd step. If the fourteen cumulative exponents are \(A_i\), their affine correction at odd count fifteen is

\[
C_s=\sum_{i=0}^{14}3^{14-i}2^{A_i},\qquad A_0=0,
\]

and the displayed prefix has total exponent \(A_{14}=S+1\). Thus after its fourteen steps the source endpoint is

\[
\frac{2^S P-2^{S+1}}{3\,2^{S+1}}
=\frac{P/2-1}{3}=z.
\tag{CB7}
\]

The same calculations for the old source and target give (CB3). This verifies both endpoint formulas; it remains to check that each prescribed division is physical, which is essential.

Here is a direct ordinary verification of that point. Substitute the positive affine table for `k,k'` above. At `t=0`, apply each displayed finite word to its initial positive integer. Every division is exact and every output is positive and odd; these are just the finitely many explicit integer operations in the checker. At any prefix of length `i` and total exponent `A_i`, a starting coefficient `b` of `t` becomes `3^i b/2^A_i`. For the four starts in rule A, their initial coefficients are

\[
X(k):3^{10}2^{12},\quad Y(k):3^{10}2^{11},
\quad X(k'):2^{26},\quad Y(k'):2^{25}.
\]

Their total division exponents are respectively 11, 9, 25, and 23. Every intermediate coefficient is therefore an even positive integer, including at the endpoints. In rule B the two old coefficients are unchanged and the two new coefficients are doubled, while the new totals are respectively 26 and 24; the same conclusion follows.

Every lifted state is an odd positive base state plus an even nonnegative multiple of `t`. Hence the indicated valuation is exact at every step for every `t≥0`. This establishes actual ordinary paths on the entire infinite progressions, not just matching rational endpoint formulas. The two shared endpoints establish (CB1), then (CB2).

## CB2. Transfer of an arbitrary supplied certificate

Suppose a complete odd certificate for \(X(k)\) is supplied. Remove its forced four-step prefix to \(z\), and prepend the fourteen-step child prefix. This constructs a complete ordinary certificate for \(X(k')\). Its odd count increases by ten; its final cumulative division exponent increases by 14 in rule A or 15 in rule B.

If a certificate for \(Y(k')\) is subsequently supplied, remove its fifteen-step prefix to \(m\), and prepend the five-step old target prefix. This constructs a certificate for \(Y(k)\). Its odd count decreases by ten and its final cumulative division exponent decreases by the same 14 or 15. The opposite directions follow by exchanging the two prefixes.

All forced intermediate and endpoint values in the domains exceed 1. Therefore an actual first-hit certificate contains these prefixes before reaching 1, and no artificial terminal padding is needed. Arbitrary certificates with terminal loops cause no problem: the suffix is simply retained. This argument uses the actual supplied certificate and makes no assertion that all smaller ordinary integers converge.

## CB3. Consequence for a globally least reverse failure

Suppose the eligible implication fails somewhere, and let \(X(k_*)\) be the globally least failing upper antecedent, as in PR163. It cannot have either of the two parameter classes in CB1.

Indeed a failure in a covered class gives `X(k′) in C` and `Y(k′) not in C` by the ordinary mergers. This is another eligible failure with \(X(k')<X(k)\), contradicting the same global minimum. The larger odd count of the child certificate is harmless: the well-founded quantity is upper numerical height, not certificate rank.

Thus these are rigorous exclusions of two infinite subsets of the previously remaining fourth-gap-five case. They are not unconditional proofs of every source or every target in those subsets.

## CB4. Explicit applications to the hard rank-five Mersennes

PR163's rank-five fourth-gap-five family is

\[
e=119+162j,\quad P=2^e,\quad
k=\frac{8P-22}{243},\quad
X=\frac{1024P-2573}{243},\quad Y=\frac{X+1}{2},
\]

with original source word `(2,2,2,5,e−1)` and old target word `(2,2,2,1,2)` ending at \(2^e-1\).

The two new rules apply respectively to the complete exponent progressions

\[
\begin{array}{ll}
\text{A:}&e\equiv7656401\pmod{9565938},\\
\text{B:}&e\equiv4822049\pmod{9565938}.
\end{array}
\tag{CB8}
\]

Here `9565938=2·3^14`, the order of 2 modulo \(3^{15}\). Both residues equal 119 modulo 162. Direct modular powers give the two last columns in the table above, and primitivity gives the complete solution classes. The elementary order formula follows from \(v_3(2^{2\cdot3^a}-1)=a+1\).

On either progression, the child source has the explicit complete first-hit word consisting of its fourteen-step prefix followed by the unchanged final exponent \(e-1\). Thus its exact odd rank is fifteen. The child target has the fifteen-step prefix to the same Mersenne. The child upper is strictly smaller than the original rank-five upper. These statements are exact compressed certificates for arbitrarily large ordinary sources; no need to run a trajectory with exponentially many bits is hidden in them.

For example, rule A gives

\[
X'=\frac{2^{24}2^e-219936533}{3^{15}},\qquad
X-X'=\frac{43688960\,2^e+68003456}{3^{15}}>0.
\]

This is an explicit cheaper certified predecessor on a Mersenne subfamily. The newer PR146 sieve already establishes existence of least-failure-excluded subprogressions inside every such exponent progression; the distinct contribution here is the fully displayed paired ordinary equivalence, valid beyond the rank-five specialization and independent of the initial-interval lemma. It does not assert all those Mersennes converge: the least-failure argument still uses the validity of smaller eligible implications. Nor does it provide bounded-depth witnesses for every exponent; PR163's unbounded-depth theorem remains compatible with these subfamilies.

## The unresolved completion

The two parameter progressions are disjoint and have relative density \(2/59049\) within the full class `k=14 (mod32)`. The specific covered exponent progressions have the same relative density inside `e=119 (mod162)`. This measures the exact reach of these two rules; it is not evidence that a null or uncovered set is empty.

The search that found them can be phrased as an exact paired-certificate problem: choose an eligible fifteen-step or longer predecessor of the residual, require its upper companion to reach the same supplied source endpoint, and minimize upper height. The new rules show this architecture can repay height on genuine ordinary inputs after a longer certificate. What is missing is a terminating construction for every parameter, especially parameters close to the rational congruence center used in PR163's W1--W2 obstruction. No all-parameter bound or coverage proof is supplied.

`check_c5_certified_bypasses.py` checks every affine prefix, shared endpoint, parity, positivity, strict contraction, exact exponent progression, and witness conversion on declared finite examples. These executable checks corroborate the algebra above. It does not iterate unbounded exponents, solve the uncovered implications, or prove Collatz.
