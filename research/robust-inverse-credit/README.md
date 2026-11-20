# Robust inverse credit: an explicit compiler and a stationary-policy bridge

**Collatz remains open.** This packet contains a new explicit inverse
conversion certificate, a general proof connecting stationary inverse
policies to uniform finite credit, and an account of the ordinary-source
obstacle that those results do not remove.

All clocks use

\[
T(n)=n/2\ (n\text{ even}),\qquad T(n)=(3n+1)/2\ (n\text{ odd}).
\]

## Results and evidence

| Claim | Result | Status and evidence |
|---|---|---|
| Explicit inverse compiler | \(T^k(2^k x+r)=3^t x+c\) for every positive prefix \(x\), with \(k\le\lfloor(13t+65)/6\rfloor\) | **PROPOSED**, complete elementary proof and independently checked finite integer certificate |
| Uniform block to finite credit | A common nonpositive finite-horizon minimum cost produces a finite potential valid for every hidden ternary lift | **PROPOSED**, complete argument, independently reviewed |
| Optimal certificate value | At any fixed cap \(R\ge6\), the infimum of robust finite-credit slopes equals the infimum of stationary means of positive local policies | **SOURCE-QUALIFIED** by UQ(R), the explicitly imported unique-stationarity theorem |
| Strict sub-two credit existence | A cap-six robust certificate of slope \(39/20\) exists at some finite precision | **SOURCE-QUALIFIED** by UQ(6); small policy and rational mean-cost bounds verified here; the robust table's size and additive credit are unknown |
| Universal ordinary descent or merging | No complete selector or exclusion of all counterexamples is obtained | **OPEN** |

## 1. The explicit result

For every integer \(t\ge1\) and \(0<c<3^t\) with \(3\nmid c\), we
construct \(0<r<2^k\) and one parity word containing exactly \(t\) odd
events such that

\[
 T^k(2^k x+r)=3^t x+c\quad(x\ge1),\qquad
 k\le\left\lfloor\frac{13t+65}{6}\right\rfloor.
\]

The certificate chooses inverse actions of exponent at most ten using
twelve ternary digits. An integer credit \(0\le V\le66\) obeys

\[
6e+V((2^e c-1)/3)\le13+V(c),
\]

with arguments understood modulo \(3^{12}\). Each chosen action is
verified for all three possible next digits. Telescoping the credit and
paying the final inverse block proves the universal bound.

This improves the asymptotic slope of PR #141's explicit finite-credit
construction from \(7/3\) to \(13/6\). Its earlier additive constants can
still be better at short depths. It is not a claim to the strongest
existential inverse-prefix result in the literature.

Read [the full proof](PROOF.md), [the table](credit_13_6.json.gz), and
[the standalone verifier](verify_credit.py).

## 2. The conceptual result

A stationary policy gives an average cost, whereas a robust credit table
must work for every ordinary source and every unseen digit. These
quantifiers cannot be interchanged directly.

The bridge first uses compactness and unique stationarity to make the
expected finite-horizon bound uniform. Minimizing over actual legal words
then gives \(F^N0\le0\) for one common horizon. The finite minimum

\[
 V=\min\{0,F0,\ldots,F^{N-1}0\}
\]

satisfies \(FV\le V\). Reading one more ternary digit than this potential
uses gives a selector valid for every remaining lift. Conversely, adding
a small amount of positive random choice to a deterministic certificate
and integrating its inequality bounds the resulting stationary mean.
Together these arguments identify the two infima.

Our independent small policy has stationary mean between 1.937 and
1.938. It therefore supplies a strict margin for slope \(39/20=1.95\)
under the imported uniqueness theorem. The proof establishes that some
finite robust certificate exists and that exhaustive search will
eventually find one. It supplies no practical search horizon. The
delivered explicit robust table is still the \(13/6\) table.

Read [the precise hypotheses and proof](DERANDOMIZATION.md),
[the small policy](small_positive_policy.json), and
[its exact verifier](verify_small_policy.py).

## 3. The remaining gap

An inverse path builds predecessors that are already known to reach its
endpoint. It does not prove that the endpoint reaches one. Its symbolic
counter of remaining ternary factors is prescribed by the compiler; no
such decreasing counter has been constructed for arbitrary forward
Collatz trajectories.

Even a slope of 1.95 permits the inverse height multiplier
\(2^{1.95}/3>1\). The earlier entropy-counting lower bound also prevents
this universal same-prefix compiler architecture from achieving a slope
below the real contraction threshold \(\log_2 3\).

[Merger and height boundary](MERGER_AND_HEIGHT.md) identifies the exact
pointwise merger obligation and proves two elementary obstructions to
the attempted synchronized inverse constructions. Neither obstruction
rules out a different asynchronous merger argument.

## Reproduce

From the repository root, using only Python's standard library:

```sh
python -X utf8 -B research/robust-inverse-credit/verify_credit.py
python -X utf8 -B research/robust-inverse-credit/verify_small_policy.py
python -X utf8 -B reports/2026-11-20-collatz-investigation/verify_credit_independent.py research/robust-inverse-credit/credit_13_6.json.gz
```

The first command checks all 354,294 potential rows and 1,062,882 selected
action lifts, rejects an invalid potential, and replays 6,575 forward
affine cones. The second verifies the separate small-policy mean-cost
certificate. The third is a second author's independent scalar replay;
it intentionally refuses optimized Python because it uses assertions.

Optional synthesis programs are [search_credit.py](search_credit.py)
(NumPy), [search_credit.cpp](search_credit.cpp) (C++17), and
[build_small_policy.py](build_small_policy.py) (NumPy). They propose
tables; the standalone exact verifiers are the verification boundary.
Keep generated files and executables outside the repository when
reproducing them.

[Source pins and scope](PROVENANCE.md) and
[investigation review and receipts](../../reports/2026-11-20-collatz-investigation/README.md)
identify the actual evidence. Repository integrity is a separate check
and does not prove the mathematical claims.
