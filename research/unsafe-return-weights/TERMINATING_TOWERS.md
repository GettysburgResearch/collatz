# The full unit disk already occurs on certified terminating paths

**Status: PROPOSED.** Use the enlarged unsafe return J, the killed mass operator K_H, and the radial norm l¹(phi(R)) from the [weight classification](README.md). Let B be the ordinary basin of 1. Its supported subspace is forward invariant. Every finite floor H>=1 and every nondecreasing phi satisfying that classification have the following property:

> Every complex number of modulus at most one is an approximate eigenvalue of K_H restricted to U intersected with B. The approximate vectors can have pairwise disjoint finite supports consisting wholly of explicitly terminating trajectories.

In particular a unit spectral radius does not indicate a surviving ordinary point. For every finite-valued nondecreasing phi>=1 with phi(t²)/phi(t) tending to one as t tends to infinity, the spectrum and approximate point spectrum both equal the closed unit disk, on the full space and on the certified basin restriction. This includes the double-log weight in the [first result](README.md).

## Finite parity prescriptions with a chosen terminal basin

Suppose w is a finite parity word of length t with q>=1 odd steps and affine constant C, so its endpoint is (3^q x+C)/2^t. The last odd step makes C a unit modulo three. Fix any positive target v coprime to 3, a ternary precision h>=0 and a source residue r modulo 3^h. There are arbitrarily large positive sources with the specified word and ternary residue whose next k shortcut steps are all halvings to v.

Indeed choose k in the single exponent class determined by

    2^{k+t} v = C+3^q r   modulo 3^{q+h}.

Both sides are units. The order of 2 modulo 3^j is 2*3^{j-1}: it is two at j=1, and v3(4^{3^i}-1)=1+i follows by induction from the factorization of the cube minus one. Thus k exists and can be taken arbitrarily large. The positive integer x=(2^{k+t}v-C)/3^q has the required ternary residue. Modulo 2^t it lies on the unique parity cylinder of w (the affine formula on that cylinder and uniqueness of the solution of 3^q x=-C modulo 2^t suffice). The endpoint is 2^k v as asserted. This gives a finite ordinary completion of each chosen word, without a common integer realizing unbounded prescriptions. The construction also covers an all-even prescription separately by x=2^{t+k}v if the prescribed ternary class is a unit, but that case is not needed here.

## Towers with a last unsafe state

For b>=0 take b copies of the signed-cycle word 11110111000 followed by the first nine bits 111101110 of the next copy. Its length is t=11b+9, odd count q=7(b+1), and C=17*3^q-68*2^t by evaluation at the signed source -17. Apply the construction with r=0, h=7 and v=1. In the notation of the [phase table](README.md), the last endpoint is Z_b=2^k. Through that endpoint all the X, Y and Z values obey the same affine formulas and ternary rows. In particular X_i and Y_i are unsafe, Z_i is safe for i<b, and Z_b is safe because its maximal even module reaches 1. The final 1110 module is maximal since the next state Z_b is even.

Choose k sufficiently large. Every prescribed module stays above H, and the final halving run reaches the killing floor. Hence the following are N=2b+2 consecutive unsafe sources with no surviving successor from the last one:

    X_0, Y_0, X_1, Y_1, ..., X_b, Y_b.

They are distinct because their positive trajectory reaches the absorbing core and visits each before its first core entry, with all of them greater than 2. Every rank from the second source onward exceeds R(X_0) for large k: each value is asymptotic to a fixed multiple of X_0 of size at least one, its rank is asymptotic to the square of that value divided by nine, and R(X_0)<=X_0²/3^7. Given any finite set of earlier tower vertices, a larger k places all these vertices above it. Thus both arbitrary depth and disjoint supports hold inside the ordinary basin of 1.

## Approximate eigenvectors

Write e_j for the unit point mass at the jth tower source, j=0,...,N-1, and w_j for its norm. We have K_H e_j=e_{j+1} for j<N-1 and K_H e_{N-1}=0. Also w_j>=w_0 for all j by monotonicity. For 0<|lambda|<=1 put

    v_N = sum_{j=0}^{N-1} lambda^{N-1-j} e_j.

Then (K_H-lambda I)v_N=-lambda^N e_0. If |lambda|<1, normalization gives residual at most |lambda|^N because ||v_N||>=w_{N-1}>=w_0. At |lambda|=1 the normalized residual is at most 1/N. At lambda=0 the last point mass is itself a zero eigenvector. These finite vectors can be supported on progressively disjoint towers. The same residual bounds apply in the full space.

For completeness, if phi(t²)/phi(t) tends to one then phi(t^8)/phi(t) tends to one by three successive squarings. Given epsilon>0, the polynomial height bound (1) of the first note therefore gives phi(R(Ju))<=(1+epsilon)phi(R(u)) at every sufficiently large surviving source rank. At smaller source ranks there are finitely many sources. Let C_epsilon bound their weights and the weights of their surviving immediate successors, enlarged to at least one. On a path of m returns with large source rank throughout, the endpoint/source ratio is at most (1+epsilon)^m. If the path encounters a small source, apply the large-rank estimate after its *last* small source, starting from the bounded immediate successor. Since the initial weight is at least one, the ratio is at most C_epsilon(1+epsilon)^m. Summing source columns yields spectral radius at most one on either space. Together with the approximate eigenvectors this identifies both spectra as claimed.

The obstruction is to uniform operator estimates and already occurs among terminating inputs. The mass and clock distribution of a particular full-support initialization remain separate questions. The [replay](check_towers.py) checks literal positive-source arithmetic on one tower and modular certificates at larger depths.
