# Strict ranking on the finite binary expansion

**Universal termination OPEN. Three candidate ranking families are refuted.** Write ordinary positive integers in binary, most significant digit first, without leading zeros. The candidate is a real-valued function on those finite words which strictly decreases at every shortcut step whose source exceeds 2. Every tested inequality below is on an actual positive orbit. The obstructions apply even before imposing properness or a lower bound on the rank.

| Candidate family | Exact positive comparisons | Largest multiplicity | Longest shortcut clock |
|---|---:|---:|---:|
| Arbitrarily weighted counts of all padded binary blocks of widths 1 through 6 | 24 | 1 | 1 |
| Arbitrary weights depending jointly on the block, width up to 6, total word length and its absolute position | 127 | 11,448 | 13 |
| Any linear functional of the ordered product of arbitrary real 2-by-2 digit matrices | 110 | 7,102 | 35 |

For any of these candidates let $F(n)$ be its underlying feature vector. The corresponding finite witness consists of positive ordinary $x_i$, positive clocks $t_i$ and positive integer weights $a_i$ with
$$
 \sum_i a_i F(x_i)=\sum_i a_i F(T^{t_i}x_i).
$$
All sources of the intervening shortcut steps exceed 2. Strict decrease would make the left scalar sum strictly larger. The comparison does not presume any Collatz stopping time beyond the finitely supplied paths.

## Local features, including position and word ends

For width $k$, pad the canonical word by $k-1$ copies of a left marker and $k-1$ copies of a different right marker. Count every consecutive window of width $k$ in this padded word. The 24 single steps in [digit_rank.py](digit_rank.py) cancel all such counts simultaneously for $1\le k\le6$. The largest source is 161.

The 127 longer comparisons all start and end in the 10-bit shell $512\le n<1024$. At each absolute window position, and separately at every width, the initial and final weighted block histograms agree. Thus the rank may assign an arbitrary value to each tuple (length, position, block). This covers different weights at both ends, any polynomial or exponential position multiplier, and arbitrary sums over all six widths. It also permits weights at other lengths to be completely independent. Telescoping cancels all intermediate word evaluations even when the path leaves this shell. The largest intermediate value is 2,888.

## Ordered digit matrices

Assign real matrices $A_0,A_1$ of size two to the digits. For a word $b_1\ldots b_L$ form $P(n)=A_{b_1}\cdots A_{b_L}$. The rank may apply any fixed linear functional to this matrix, including arbitrary left and right boundary vectors. Products read in reverse order are also covered by transposing both matrices and the functional. Even a length-dependent linear functional cannot resolve this witness since all its endpoints have length ten.

The 110 comparisons give an identity of full matrix polynomials in the eight independent entries of $A_0,A_1$. The replay expands all products directly. A length-ten matrix product contributes one monomial per sequence of eleven binary states, recording the initial and final matrix indices and the eight entry multiplicities. Those multiplicities never exceed ten. The weighted coefficient of each monomial in each of the four entries cancels exactly. Specializing the entries to any real values preserves the equality. No commutation between the two matrices is assumed. The largest intermediate integer in these paths is 95,498.

## Search and verification

The original search imposed strict inequalities on finite ordinary samples. A positive dependence in the dual directly rejects a candidate. For the position-sensitive and matrix searches we enumerated first returns to a single fixed word length, starting with every word of that length, stopping a search at 2 or at the supplied search horizon (400 steps for the positional search, 150 for the matrix search). A linear program sought nonnegative return multiplicities of sum one annihilating the features while minimizing their weighted elapsed clocks. Its floating-point support was only a search hint. Exact integer nullspace recovery provided the displayed witnesses.

For matrix discovery we compressed a word to $I,A,B,AB$ using the quadratic identities for two-by-two matrices and polynomial coefficients in their two traces, two determinants and $\operatorname{tr}(AB)$. The independent replay uses generic entry monomials instead. It has no solver dependency and raises an explicit error on any failed check, including under optimized Python.

The two longer witnesses are separate. They do not exclude a sum combining the position and matrix features, a nonlinear terminal function of the matrix, higher-dimensional matrices, or wider contexts. No universal positive rank emerged.
