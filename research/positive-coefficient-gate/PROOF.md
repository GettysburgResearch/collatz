# Least-counterexample coefficient gate

**Claim IDs:** `D-6701`, `T-6701`--`T-6707`, `L-6705`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-01`  
**Reviewing agents:** none yet  
**Created:** 2026-07-29  
**Last updated:** 2026-07-29  
**Issue:** #75  
**Dependencies:** Barina's verified range, Ansari's recursive-sufficiency extension, Angeltveit's Theorem 4.1 for the auxiliary ballot constraint, the classical Denjoy--Koksma inequality, and exact arithmetic certificate `X-6701`  
**Scope:** necessary conditions for a least positive Collatz counterexample; no full proof of Collatz

---

## 1. Statement

Let

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For a starting integer \(n\), let \(v_i(n)\in\{0,1\}\) be the parity of \(T^i(n)\), and put

\[
q_k(n)=\sum_{i=0}^{k-1}v_i(n),\qquad
C_k(n)=\frac{3^{q_k(n)}}{2^k}.
\]

Define the coefficient stopping time

\[
\tau(n)=\min\{k\ge1:C_k(n)<1\},
\]

with \(\tau(n)=\infty\) if there is no such \(k\).

### T-6707: sharpened coefficient-stopping dichotomy

If the Collatz conjecture is false and \(n\) is its least positive counterexample, then

\[
\boxed{\tau(n)=\infty\quad\text{or}\quad \tau(n)\ge217\,976\,794\,617.}
\]

### T-6702: auxiliary all-prefix ballot barrier

For the same least counterexample and every \(k\ge1\),

\[
\boxed{485q_k(n)>306k.}
\]

The ballot barrier is not needed for the numerical value in T-6707, but it materially narrows the remaining uniform-supercritical survivor tree.

---

## 2. Verified floor

Set

\[
N_*=4\cdot3^{44}+2
 =3\,939\,083\,608\,734\,444\,931\,526.
\]

### T-6701

Every positive integer at most \(N_*\) satisfies the Collatz conjecture.

### Source audit

Barina's 2025 computation verifies all positive starts below \(2^{71}\). Ansari's Proposition 3.2 proves the following reusable implication:

> if all starts through \(A=2\cdot3^r+1\) converge, then every start in \((A,2A]\) also converges.

The phrase "largest known" occurs in the printed statement, but maximality is not used in the proof; the proof uses only convergence through \(A\) and the absence of the recursively sufficient set from \((A,2A]\). Ansari's own Remark 3.1 applies the proposition in exactly this nonmaximal way.

Since

\[
2\cdot3^{44}+1<2^{71}<4\cdot3^{44}+2,
\]

Barina verifies the range through \(A=2\cdot3^{44}+1\), and Ansari extends it through \(2A=N_*\).

This packet does not rerun Barina's distributed computation. It treats the peer-reviewed computational theorem and Ansari's peer-reviewed extension as imported dependencies.

---

## 3. Minimality constraints

Assume Collatz is false, and let \(n\) be the least positive starting value that does not reach \(1\).

### Lemma 3.1: no descent

For every \(k\ge0\),

\[
T^k(n)\ge n.
\]

#### Proof

If \(T^k(n)=m<n\) for some \(k\), minimality says that \(m\) reaches \(1\). The orbit from \(n\) then reaches \(m\) and subsequently \(1\), contrary to the choice of \(n\). ∎

Consequently,

\[
n>N_*.
\]

### T-6702: the `485/306` ballot barrier

Angeltveit's Theorem 4.1 states that if a length-\(k\) shortcut prefix contains \(q_k\) odd steps, satisfies

\[
485q_k\le306k,
\]

and all its iterates are at least \(99\,781\), then its endpoint is below its starting value.

For a least counterexample, every iterate is at least \(n>N_*>99\,781\), while Lemma 3.1 forbids an endpoint below \(n\). Therefore

\[
485q_k>306k
\]

for every \(k\ge1\). Equivalently, the defect walk

\[
D_k=485q_k-306k
\]

stays strictly positive, with increment \(+179\) on an odd step and \(-306\) on an even step.

---

## 4. Finite first crossing gives a microscopic Diophantine window

Let

\[
\alpha=\frac{\log2}{\log3}.
\]

Assume \(\tau(n)=j<\infty\), and abbreviate \(q=q_j(n)\) and \(C=3^q/2^j\). Then \(C<1\), while Lemma 3.1 gives \(T^j(n)\ge n\). Thus this prefix is paradoxical in the terminology of Rozier--Terracol.

Let \(m_0,\ldots,m_{q-1}\) be the odd values encountered before the endpoint. Stepwise multiplication gives the exact identity

\[
\frac{T^j(n)}n
 =C\prod_{r=0}^{q-1}\left(1+\frac1{3m_r}\right).
\]

Every \(m_r\ge n\), so

\[
1\le \frac{T^j(n)}n
 \le C\left(1+\frac1{3n}\right)^q.
\]

Put

\[
\lambda=j\log2-q\log3>0.
\]

Taking logarithms and using \(\log(1+x)<x\) gives

\[
\lambda
 \le q\log\left(1+\frac1{3n}\right)
 <\frac q{3n}
 <\frac{\alpha j}{3n}.
\]

Since

\[
\alpha-\frac qj=\frac{\lambda}{j\log3},
\]

we obtain T-6703:

\[
0<\alpha-\frac qj
 <\frac{\log2}{3n(\log3)^2}
 <\epsilon_*,
\]

where

\[
\epsilon_*
 :=\frac{\log2}{3N_*(\log3)^2}
 <4.86\times10^{-23}.
\]

Hence every finite first crossing supplies a rational \(q/j\) in the open interval

\[
I_*=(\alpha-\epsilon_*,\alpha).
\]

---

## 5. First Farey gate

The exact checker verifies the continued-fraction prefix

\[
\alpha=[0;1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,\ldots].
\]

The consecutive convergents at indices \(22\) and \(23\) are

\[
L=\frac{a}{b}
 =\frac{6\,586\,818\,670}{10\,439\,860\,591},
\]

and

\[
U=\frac{c}{d}
 =\frac{65\,470\,613\,321}{103\,768\,467\,013}.
\]

They satisfy

\[
bc-ad=1,
\]

and the exact interval certificate proves

\[
L<\alpha-\epsilon_*<\alpha<U.
\]

### Farey denominator lemma

If reduced fractions \(a/b<c/d\) satisfy \(bc-ad=1\), then every reduced \(p/s\in(a/b,c/d)\) has

\[
s\ge b+d.
\]

Equality occurs only for the mediant \((a+c)/(b+d)\).

#### Proof

Both integers \(pb-as\) and \(cs-pd\) are positive. Moreover,

\[
s=d(pb-as)+b(cs-pd),
\]

because \(bc-ad=1\). Hence \(s\ge b+d\). Equality forces both positive integers to equal \(1\), which uniquely gives the mediant. ∎

The mediant is

\[
M=\frac{a+c}{b+d}
 =\frac{72\,057\,431\,991}{114\,208\,327\,604}.
\]

The checker proves

\[
\alpha-\epsilon_*<M<\alpha.
\]

Therefore T-6704 holds:

\[
j\ge114\,208\,327\,604,
\]

and equality can occur only at the pair

\[
(j,q)=(114\,208\,327\,604,72\,057\,431\,991).
\]

---

## 6. The first-crossing mechanical extremizer

We now exclude this unique equality candidate.

Let \(v=(v_0,\ldots,v_{j-1})\) be its parity word and define prefix counts

\[
S_m=\sum_{i=0}^{m-1}v_i,
\qquad S_0=0.
\]

Because \(j\) is the first coefficient crossing,

\[
\frac{3^{S_m}}{2^m}\ge1
\qquad(1\le m<j),
\]

so irrationality of \(\alpha\) gives

\[
S_m\ge\lceil m\alpha\rceil
\qquad(1\le m<j).
\]

A crossing from coefficient at least \(1\) to coefficient below \(1\) can only occur on an even step: an odd step multiplies the coefficient by \(3/2\), whereas an even step multiplies it by \(1/2\). Thus

\[
v_{j-1}=0,\qquad S_{j-1}=S_j=q.
\]

For the candidate \(M=q/j\), the exact certificate also proves

\[
q-1<(j-1)\alpha<q,
\]

hence \(\lceil(j-1)\alpha\rceil=q\).

Define the word \(w=(w_0,\ldots,w_{j-1})\) by

\[
w_{m-1}=\lceil m\alpha\rceil-\lceil(m-1)\alpha\rceil
\quad(1\le m<j),
\]

and \(w_{j-1}=0\). Its prefix counts are exactly \(\lceil m\alpha\rceil\) for \(m<j\), and its total weight is \(q\).

### L-6705: extremal remainder

Among all length-\(j\), weight-\(q\) words satisfying the first-crossing prefix constraints, \(w\) maximizes the affine remainder.

#### Adjacent-swap proof

For a parity word \(u\), write

\[
T_u(x)=\frac{3^{|u|_1}x+A_u}{2^{|u|}}
\]

and call \(E(u)=A_u/2^{|u|}\) its additive remainder. Compare two words with a common prefix and suffix, differing only by `10` versus `01` in the middle. If the remainder after the common prefix is \(E_0\), then after the two differing steps the remainders are

\[
E_{10}=\frac34E_0+\frac14,
\qquad
E_{01}=\frac34E_0+\frac12.
\]

Applying the identical suffix preserves the strict order. Therefore replacing `10` by `01`, i.e. moving a `1` one place to the right, strictly increases the final remainder.

The prefix sums of \(w\) are no larger than those of any admissible \(v\), and the total weights agree. By the standard dominance characterization for binary words, \(v\) can be transformed into \(w\) through rightward adjacent moves `10 -> 01`. Hence

\[
E(v)\le E(w).
\]

This reconstructs the Rozier--Terracol remainder-order lemma in the orientation needed here. ∎

---

## 7. Rotation formula for the maximal remainder

For any length-\(j\) word with prefix counts \(S_m\) and total weight \(q\), direct expansion of the affine recurrence gives

\[
E(v)=C\sum_{m=1}^j
 v_{m-1}\frac{2^{m-1}}{3^{S_m}},
\qquad C=\frac{3^q}{2^j}.
\]

For the mechanical word \(w\), let \(\{x\}\) denote fractional part and define the circle function

\[
g(x)=\begin{cases}
3^{x-1},&0<x\le\alpha,\\
0,&x=0\text{ or }\alpha<x<1.
\end{cases}
\]

For \(1\le m<j\),

\[
w_{m-1}=1
\quad\Longleftrightarrow\quad
0<\{m\alpha\}\le\alpha.
\]

Whenever this increment is \(1\),

\[
\frac{2^{m-1}}{3^{\lceil m\alpha\rceil}}
 =\frac12\,3^{\{m\alpha\}-1}.
\]

The final bit is zero, so

\[
E(w)=\frac C2\sum_{m=1}^{j-1}g(\{m\alpha\}).
\]

The integral and total variation of \(g\) on the circle are

\[
\int_0^1g(x)\,dx=\frac1{3\log3},
\qquad
\operatorname{Var}(g)=\frac43.
\]

Indeed, the continuous rise on \((0,\alpha]\) contributes \(1/3\), the downward jump at \(\alpha\) contributes \(2/3\), and the circular jump at \(0\) contributes \(1/3\).

---

## 8. Denjoy--Koksma exclusion of the first candidate

The classical Denjoy--Koksma inequality says that for an irrational rotation by \(\alpha\), a bounded-variation circle function \(f\), any convergent denominator \(Q\), and any starting point \(x\),

\[
\left|\sum_{r=0}^{Q-1}f(x+r\alpha)
 -Q\int_0^1f\right|
 \le\operatorname{Var}(f).
\]

The candidate length is

\[
j=b+d,
\]

where \(b\) and \(d\) are consecutive convergent denominators. Since \(g\ge0\), add the omitted nonnegative term at \(m=j\), split the resulting sum into blocks of lengths \(d\) and \(b\), and apply Denjoy--Koksma to each block:

\[
\sum_{m=1}^{j-1}g(\{m\alpha\})
\le
\sum_{m=1}^{j}g(\{m\alpha\})
\le
\frac{j}{3\log3}+\frac83.
\]

Because \(C<1\),

\[
E(v)\le E(w)
 <\frac{j}{6\log3}+\frac43.
\]

On the other hand, the non-descent condition \(T^j(n)\ge n\) and

\[
T^j(n)=Cn+E(v)
\]

require

\[
E(v)\ge n(1-C)>N_*(1-C).
\]

Experiment `X-6701` proves exactly, without floating-point assumptions, that for the candidate \((j,q)\),

\[
\frac{j}{6\log3}+\frac43
 <N_*\left(1-\frac{3^q}{2^j}\right).
\]

The checker uses rational enclosures for \(\log2\) and \(\log3\), writes

\[
\lambda=j\log2-q\log3,
\qquad C=e^{-\lambda},
\]

and applies the rigorous inequality

\[
1-e^{-\lambda}\ge\lambda-\frac{\lambda^2}{2}
\qquad(\lambda\ge0).
\]

Its certified numerical enclosures are

```text
upper remainder bound < 17,326,149,966.768241
N_* times coefficient drop > 21,707,856,845.723104
certified margin > 4,381,706,878.954863
```

This contradiction proves T-6706: the unique first Farey candidate cannot be the first coefficient crossing of a least counterexample.

---

## 9. The second denominator gate

Define the left mediant adjacent to \(M\),

\[
F=\frac{2a+c}{2b+d}
 =\frac{78\,644\,250\,661}{124\,648\,188\,195},
\]

and the right mediant adjacent to \(M\),

\[
R=\frac{a+2c}{b+2d}
 =\frac{137\,528\,045\,312}{217\,976\,794\,617}.
\]

The exact certificate proves

\[
F<\alpha-\epsilon_*<M<\alpha<U.
\]

Both pairs \((F,M)\) and \((M,U)\) have determinant \(1\).

Let \(q/j\in I_*\), and first reduce it.

- If its reduced value lies in \((M,U)\), the Farey lemma gives reduced denominator at least
  \[
  (b+d)+d=b+2d=217\,976\,794\,617.
  \]
- If it lies in \((F,M)\), its reduced denominator is at least
  \[
  (2b+d)+(b+d)=3b+2d=238\,856\,515\,799.
  \]
- If its reduced value equals \(M\), its original denominator is a positive multiple of \(b+d\). The first multiple has just been excluded, so the next is at least
  \[
  2(b+d)=228\,416\,655\,208.
  \]

The minimum of these three lower bounds is \(b+2d\). Therefore

\[
\tau(n)=j\ge217\,976\,794\,617,
\]

unless \(\tau(n)=\infty\). This proves T-6707, subject to independent review of the stated dependencies and reconstruction of the argument.

---

## 10. Why the target is weaker than Collatz

T-6707 does not assume or prove that every orbit has finite coefficient stopping time. It leaves two exhaustive possibilities for a least counterexample:

1. **uniform-supercritical:** \(C_k\ge1\) for every finite \(k\);
2. **delayed crossing:** \(C_k\) first drops below \(1\) only after at least \(217\,976\,794\,617\) steps.

Excluding both possibilities would prove Collatz. Excluding either one alone is strictly weaker.

The first lane is especially compatible with the repository's ordinary-extraction theorem. For each depth \(k\), form the finite union of residue cylinders whose parity prefixes satisfy:

- \(C_m\ge1\) for all \(m\le k\);
- no descent below the starting value;
- \(485q_m>306m\) for all \(m\le k\);
- any sound path-merging, preimage, and odd-even-even exclusions.

A genuine least counterexample would be one fixed ordinary integer in every depth. The existing extraction theorem says this requires bounded, eventually stable least representatives. Thus a direct positive target is:

> prove that the least ordinary representative among these constrained survivor cylinders tends to infinity.

That target is a cylinder-growth theorem, not another symbolic completion or finite-prefix existence statement.

---

## 11. Dependency audit

### Imported

1. **Barina 2025:** exhaustive convergence through \(2^{71}\).
2. **Ansari 2025:** recursively sufficient extension from \(2\cdot3^r+1\) through twice that value.
3. **Angeltveit 2026, Theorem 4.1:** only for the auxiliary `485/306` ballot barrier.
4. **Denjoy--Koksma:** discrepancy bound at convergent denominators.

### Reconstructed in this file

1. least-counterexample no-descent;
2. product inequality and Diophantine window;
3. Farey denominator lemma;
4. adjacent-swap remainder order;
5. mechanical extremizer;
6. exact rotation-sum expression;
7. two-block reduction to Denjoy--Koksma;
8. second Farey gate.

### Mechanically certified by `X-6701`

1. rational logarithm enclosures;
2. continued-fraction prefix through the next partial quotient;
3. all window-order inequalities;
4. the candidate value of \(\lambda\);
5. the positive candidate-exclusion margin;
6. the three second-gate denominators.

---

## 12. Gap audit

1. **No full resolution.** The uniform-supercritical and delayed-crossing lanes remain open.
2. **Published computation dependency.** This packet does not independently rerun the \(2^{71}\) verification.
3. **Recursive-sufficiency dependency.** The relevant Ansari argument was audited algebraically, but still needs an independent repository reviewer.
4. **Classical theorem dependency.** Denjoy--Koksma is quoted rather than reproved from first principles.
5. **Checker scope.** `X-6701` certifies finite rational inequalities. It does not certify the combinatorial extremizer or Denjoy--Koksma theorem.
6. **No extrapolation.** Excluding the first Farey candidate says nothing by itself about all later candidates.
7. **No symbolic-to-integer confusion.** The argument starts with an assumed ordinary least counterexample; it never promotes a free parity word or a 2-adic completion to an ordinary orbit.
8. **No external priority claim.** Repository search found no overlap, but the external novelty of this precise synthesis has not been established.

---

## 13. Adversarial review checklist

A reviewer should attempt all of the following independently.

1. Re-derive the extension from \(2^{71}\) to \(N_*\) directly from Ansari's recursively sufficient set.
2. Check the strictness and orientation of every inequality in the first-crossing window.
3. Recompute the continued fraction of \(\log2/\log3\) with an independent interval package.
4. Verify that rightward moves `10 -> 01` increase, rather than decrease, the remainder.
5. Verify \(\lceil(j-1)\alpha\rceil=q\) for the mediant candidate.
6. Re-derive the rotation function \(g\), especially the exceptional equality \(\{\alpha\}=\alpha\) at \(m=1\).
7. Check that the circular variation is \(4/3\), including both jumps.
8. Check the two Denjoy--Koksma starting points and the addition of the nonnegative \(m=j\) term.
9. Run `X-6701` under a second Python implementation or Arb/Sage interval arithmetic.
10. Try to produce any admissible word whose remainder exceeds the claimed mechanical extremizer.

---

## 14. Suggested next attacks

### A. Supercritical ordinary-root divergence

Port Angeltveit's descent, path-merging, mod-9 preimage, and odd-even-even sieves into the nested parity-cylinder representation. Track the least ordinary root of the survivor union by depth. The theorem target is divergence of that least root, not merely exponential thinning of the number of cylinders.

### B. Ostrowski remainder bounds for every left approximant

For a later candidate denominator, decompose its length into continued-fraction denominators and apply Denjoy--Koksma blockwise. Combine the resulting upper bound with the exact coefficient gap. The current verification floor excludes the first mediant but not yet the next convergent; additional ballot/path-merging information must lower the admissible remainder.

### C. Ballot-constrained mechanical improvement

The extremizer in L-6705 uses only \(C_m\ge1\). The stronger barrier \(485S_m>306m\) may force earlier odd steps and therefore strictly reduce the maximum remainder. Quantify that forced left-shift cost over continued-fraction blocks.

### D. Prefix endpoint constraints

A least counterexample requires \(T^m(n)\ge n\) at every intermediate time, not only at \(j\). Impose these affine inequalities on the mechanical envelope. Any systematic loss in the remainder budget could propagate the exclusion far beyond the first candidate.