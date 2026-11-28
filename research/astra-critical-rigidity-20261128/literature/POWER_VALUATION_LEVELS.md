# Uniform counting of the valuations taken by a short sum of powers

Let \(b\ge2\) be an integer, let \(\ell\) be a prime not dividing \(b\), and use \(v_\ell(\ell)=1\). Given \(r\ge1\), \(T\ge0\) and arbitrary \(c_1,\ldots,c_r\in\mathbb Q_\ell\), form the set of **finite, distinct** values
\[
  \mathcal V(c,T)=
  \{v_\ell(c_1 b^{a_1}+\cdots+c_r b^{a_r}):
      0\le a_i\le T,\ a_i\in\mathbb Z,\ \sum_i c_i b^{a_i}\ne0\}.
\]
The coefficients may depend on \(T\). Set \(\delta_1=1\) and
\[
 \frac{1}{\delta_r}=1+\frac{r-1}{\delta_{r-1}}
    =(r-1)!\sum_{i=0}^{r-1}\frac1{i!}\quad(r\ge2).
\]
There is an effectively computable \(C_{b,\ell}>0\) with
\[
       |\mathcal V(c,T)|\le
       \exp(C_{b,\ell}r^2)(T+1)^{1-\delta_r}.                       \tag{1}
\]
This bound is uniform over coefficient heights and common shifts of the valuations. It counts levels; a coefficient may force an individual valuation arbitrarily high.

## Proof

The all-zero coefficient vector gives the empty set. With one nonzero coefficient there is exactly one value since \(b\) is an \(\ell\)-adic unit. Zero coefficients can always be padded or deleted. Let \(F_r(T)\) be the supremum of the cardinality over at most \(r\) coefficients. We may take \(T\) integral.

Scale the coefficients so their minimum finite valuation is zero. This translates the valuation set. Divide each row of powers by \(b^{a_1}\), an \(\ell\)-adic unit, so its first exponent is zero and the other \(r-1\) exponents lie in \([-T,T]\). Choose an integer \(1\le B\le T+1\), and partition each relative exponent interval into consecutive boxes of at most \(B\) integers. There are at most \([4(T+1)/B]^{r-1}\) product boxes. In each product box subtract the lower endpoint of each exponent interval from that coordinate and transfer the common factor to its coefficient. This preserves all coefficient valuations. The rows in that box now have integer entries \(b^{e_i}\) with \(0\le e_i<B\).

Put \(D=\lceil\log_\ell(r!)+rB\log_\ell b\rceil\). The values from zero to \(D\) cost at most \(D+1\) **across all boxes together**. Fix one box and keep the rows whose form has finite valuation greater than \(D\). They span a rational space of dimension less than \(r\). Otherwise \(r\) such rows make an invertible integer matrix \(W\). Every component of \(Wc'\) lies in \(\ell^{D+1}\mathbb Z_\ell\), with \(c'\) the normalized, rescaled coefficient vector. Multiplication by the integer adjugate yields \(\det(W)c'\in\ell^{D+1}\mathbb Z_\ell^r\). Some coefficient of \(c'\) is a unit, so \(\ell^{D+1}\) divides \(\det W\). This contradicts \(0<|\det W|\le r! b^{rB}\).

For a nonempty high box choose a column basis of its row matrix, of rank \(s<r\). Every other column is an exact rational linear combination of these \(s\) original columns, by choosing an invertible \(s\)-row minor. The form therefore agrees throughout this box with a linear combination of \(s\) powers with exponents in \([0,B)\). Its coefficients are allowed in \(\mathbb Q_\ell\), including the rational factors created by this basis change. Their valuations can be normalized afresh. The number of high values here is at most \(F_{r-1}(B-1)\). Thus
\[
 F_r(T)\le D+1+
       \left(\frac{4(T+1)}{B}\right)^{r-1}F_{r-1}(B-1).             \tag{2}
\]

For \(r\ge2\) take \(B=\lceil (T+1)^{\,1-\delta_r}\rceil\). Write \(\beta=1-\delta_r\). The low-value term is at most \(C'_{b,\ell}r\log(2r)(T+1)^\beta\). If the multiplier in the bound for \(F_{r-1}\) is \(K_{r-1}\), the second term is at most \(4^{r-1}K_{r-1}(T+1)^\beta\), since
\[
  r-1-\beta(r-2+\delta_{r-1})=\beta .
\]
Here \(B\ge(T+1)^\beta\), and the power of \(B\) after combining the two factors is nonpositive. Starting from \(K_1=1\), (2) therefore gives \(K_r\le\exp(C_{b,\ell}r^2)\) for a computable constant. This proves (1). In particular \(\delta_r\ge1/r!\).

For two terms the prime \(3\) and base \(2\) permit a sharper elementary bound of order \(\log(T+2)\). After scaling, unequal coefficient valuations give a constant valuation. For equal coefficient valuations, write the expression as a unit times \(c+2^j\) with \(|j|\le T\). Two different \(j,j'\) have \(v_3(2^j-2^{j'})\le1+\log_3(2T)\) for \(T\ge1\), by the order of \(2\) modulo powers of three. Thus at most one exponent can give a value above this threshold. The general bound (1) suffices for the [worst-case landing-clock application](EFFECTIVE_WORST_LANDING.md).
