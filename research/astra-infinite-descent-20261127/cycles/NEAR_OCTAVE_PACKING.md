# Denominator growth near one odd octave with arbitrary clock gcd

Let a positive rational shortcut cycle have least period $h$, odd count $p\ge2$, least odd state $m$, ratio of largest to smallest odd state $R$, and common reduced denominator $q$. Write $g=\gcd(h,p)$, $b=p/g$, $\gamma=\log_2 3$, $\eta=\max(0,\log_2R-1)$ and $\Lambda=h-p\gamma>0$. Suppose $\eta+\Lambda<1/4$. Define
\[
 B=p(\eta+2\Lambda)+g,\qquad
 t=\left\lfloor\frac{p-2}{1+2B}\right\rfloor .
\]
Then
\[
                  qRm>2^t.                                             \tag{1}
\]
This applies irrespective of the number of edited ranks or of the arrangement of the edits between successive circuits of the reduced mechanical clock.

## Physical height and repeated factors

Root the odd cycle at $m$. Write $E_i=\sum_{j<i}e_j$ for cumulative divisions at odd steps and $f_i=\{ih/p\}$. As in the [coprime calculation](COPRIME_NEAR_OCTAVE.md), the height is
\[
 \log_2(x_i/m)=f_i+d_i+\theta_i,\qquad
 d_i=\lfloor ih/p\rfloor-E_i,\quad |\theta_i|\le\Lambda.
\]
No coprimality enters this identity. The only possible nonzero $d_i$ are $+1$ for $f_i\le\eta+\Lambda$ and $-1$ for $f_i\ge1-\Lambda$. The same rank can now occur more than once, and some visits to rank zero may have $d_i=1$. Each value $j/b$, $0\le j<b$, occurs $g$ times. There are at most $\lfloor b(\eta+\Lambda)\rfloor+1$ eligible low ranks and $\lfloor b\Lambda\rfloor$ eligible high ranks, hence at most $B$ exceptional dates. Also $d_0=d_p=0$ and $d$ is periodic.

Compare the actual division word with $a_i=\lfloor(i+1)h/p\rfloor-\lfloor ih/p\rfloor$. Since $e_i=a_i+d_i-d_{i+1}$, at most $2B$ letters of one cyclic lap differ. A length-$t$ factor of $a$ is determined by the vector of floors $\lfloor f+jh/p\rfloor$ for $1\le j\le t$ and a starting phase $f\in[0,1)$. Each coordinate has at most one interior change, and takes its upper value at a change. Consequently there are at most $t+1$ distinct factors. Each edited letter can spoil at most $t$ cyclic starting dates when $t<p$. The actual word has at most $1+(1+2B)t\le p-1$ distinct length-$t$ factors, including those which cross the seam. Thus some two distinct odd phases have the same next $t$ exponents.

Clearing the common denominator in their affine iterates gives
\[
  3^t q(x_i-x_j)=2^{e_i+\cdots+e_{i+t-1}}q(x_{i+t}-x_{j+t}).
\]
The two starting states differ by primitivity. Their nonzero integer numerator difference is a multiple of the displayed power of two, which is at least $2^t$, whereas its absolute value is strictly below $qRm$. The case $t=0$ follows from the same distinctness and positivity.

## A stretched-exponential floor

For any sequence in this class with $h\to\infty$, $m\ge h^{2-o(1)}$ and $R\le2+h^{-1+o(1)}$,
\[
          \log q \ \ge\ h^{2/5.1163051-o(1)} .                         \tag{2}
\]
The numerical exponent is about $0.39091$. More generally, if $m\ge h^{1+a-o(1)}$, $\eta\le h^{-c+o(1)}$ with $a,c>0$, then
\[
 \liminf_{h\to\infty} \frac{\log\log q}{\log h}
 \ge \min\!\left(1,a,c,\frac{1+a}{5.1163051}\right).                  \tag{3}
\]
An impossible parameter range simply supplies no infinite sequence.

Indeed, summing the odd logarithmic corrections gives $\Lambda\le p/(3m\log 2)$, so $\Lambda\le h^{-a+o(1)}$, $p\asymp h$ and $R=O(1)$. Fix any $\nu>4.1163051$. Wu and Wang's Theorem 1 bounds the absolute value of $u_0+u_1\log 2+u_2\log 3$ below by $H^{-\nu}$ for sufficiently large $H=\max(|u_1|,|u_2|)$. Take $(u_0,u_1,u_2)=(0,h/g,-p/g)$ so that the form is exactly $(\Lambda/g)\log 2$. The reduced heights $H\asymp b$ tend to infinity: a bounded set of reduced count pairs would give a positive constant lower bound for $\Lambda/g$. Hence $\Lambda\gg_\nu g b^{-\nu}\asymp h b^{-1-\nu}$. It follows that $b\ge h^{(1+a)/(1+\nu)-o(1)}$. Applying the same lower bound on $\Lambda/g$ to the minimum estimate gives $m\le p/(3\Lambda\log2)\ll_\nu b^{1+\nu}\ll_\nu h^{1+\nu}$, making $\log(Rm)=O_\nu(\log h)$. Finally, (1) has $t\gg\min(p,(\eta+2\Lambda)^{-1},b)-1$, so subtracting $\log(Rm)$ leaves (3) after $\nu$ decreases to $4.1163051$.

[Wu and Wang, *On the irrationality measure of log 3*, Journal of Number Theory 142 (2014), Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007) · [Lagarias, Lemma 2.2](https://arxiv.org/abs/math/0512006) gives the independently available explicit exponent $13.3$ for a homogeneous two-log form, which yields $2/14.3=20/143$ in (2).

The parity-packing step, including its denominator version, appears in earlier work. The physical clipping above derives a complexity bound for the *actual* odd division word directly from its minimum and amplitude with an arbitrary gcd and arbitrary choices at exceptional ranks. Combining it with power separation at the **reduced** clock gives (2). [Solomon, Proposition 2 and the odd-clock comparisons](https://rstation.ai/problems/collatz/papers/216/v1) · [Mahler, complexity–discrepancy bounds for supplied symbolic families](https://rstation.ai/problems/collatz/papers/214/v1)

The [coprime estimate](COPRIME_NEAR_OCTAVE.md) is much stronger when $g=1$. The [independent-clock construction](INDEPENDENT_CLOCKS.md) exhibits positive primitive rational examples satisfying the physical conditions of (2) and $\log q=o(h)$. These estimates leave the optimal all-gcd growth rate undetermined. Neither physical condition in (2) has been proved for arbitrary ordinary cycles. Equations (1)–(3) are written proofs.

[Exact arithmetic replay](check_near_octave.py) verifies 297 primitive physical examples, including 29 with noncoprime clocks. It checks the actual factor counts, root distinctness and dyadic difference divisibility for each duplicate, with a longest checked repeated window of 305 odd steps. [Archived counts](../../../reports/astra-infinite-descent-20261127/cycles/NEAR_OCTAVE.json)
