# A polynomial plus a bounded periodic correction at each fixed inverse grade

Fix \(d\ge1\) and a positive odd target \(y\) prime to three. Let \(a_{d,m}(y)\) count odd positive sources prime to three that reach \(y\) in \(m\) shortcut steps, with exactly \(d\) odd departures and no restriction on previous visits. Set \(B_d=2\cdot3^d\). There is a polynomial \(P_{d,y}\) of degree \(d-1\), with leading coefficient \(1/(3^d(d-1)!)\), and a bounded \(B_d\)-periodic function \(\rho_{d,y}\) such that
\[
 a_{d,m}(y)=P_{d,y}(m)+\rho_{d,y}(m)\qquad(m\ge1). \tag{1}
\]
In particular every polynomial coefficient of positive degree is independent of the physical clock class. The periodic function may depend on the target and grade. An exact integer consequence, with \(\Delta_h f(m)=f(m+h)-f(m)\), is
\[
 \Delta_1^{d-1}\Delta_{B_d} a_{d,m}(y)=0\qquad(m\ge1). \tag{2}
\]
This statement concerns fixed grade. The allowable period grows exponentially with the grade.

## Finite Fourier proof

Let \(U_k=(\mathbb Z/3^k\mathbb Z)^\times,\ k\ge1\), and let \(U_0\) be trivial. Use normalized counting measure and identify functions and multiplicative characters on \(U_k\) with their lifts to higher levels. The conductor level \(c(\chi)\) is the smallest \(k\) through which a character factors. Thus only the trivial character has level zero. The unit 2 generates every \(U_k\), since \(v_3(4^{3^j}-1)=j+1\) and odd powers of 2 are \(2\bmod3\).

For \(|z|<1\), define the unnormalized transfer
\[
 (L_z f)(y)=\sum_{\substack{e\ge1\\2^e y\bmod9\in\{4,7\}}}
           z^e f((2^e y-1)/3).
\]
For \(k\ge1\), a level-\(k\) input gives a level-\((k+1)\) output. The initial constant is treated on \(U_1\); \(U_0\) only labels the trivial character. For a fixed ordinary target, \(F_d(z,y)=L_z^d1(y)=\sum_m a_{d,m}(y)z^m\), by the positive odd-gap dictionary. Each contributing word has a unique ordinary source at that clock and grade. Write \(\widehat f(\chi)=\mathbb E_x[f(x)\overline{\chi(x)}]\). For every character of the output level,
\[
 \widehat{L_z f}(\chi)=
 \frac{z\chi(2)}{3(1-z\chi(2))}
 \mathbb E_x[f(x)\overline{\chi(1+3x)}]. \tag{3}
\]
Indeed, for a fixed \(e\), the accepted residues \(y\) are exactly \(2^{-e}(1+3x)\), one for each input unit \(x\). They occupy one third of the output units. Substitution in the finite sum and the geometric series give (3).

Expand \(f\) in the input characters \(\psi\). For \(\chi\ne1\), the expression \(\chi(1+3x)\) depends only on \(x\bmod3^{c(\chi)-1}\), with a constant value when \(c(\chi)=1\). Finite character orthogonality therefore kills every term with \(c(\psi)\ge c(\chi)\). For \(\chi=1\) only \(\psi=1\) survives. Hence in a contributing sequence of \(d\) character transitions starting at \(1\), trivial characters may repeat at the beginning, and the subsequent nontrivial character levels strictly increase. All characters can be regarded on \(U_{d+1}\). Their values on its generator 2 are distinct whenever the characters are distinct.

Iteration of (3) expresses every \(F_d(z,y)\) as a finite sum of scalar multiples of products of \(d\) factors \(z\omega/(1-z\omega)\), \(\omega^{B_d}=1\). Only \(\omega=1\) can repeat in the same product. Thus the only possible poles are roots of unity, every nontrivial pole is simple, and the denominator divides
\[
 (1-z)^{d-1}(1-z^{B_d}).
\]
The sole order-\(d\) contribution at \(z=1\) comes from the all-trivial character path, with coefficient \(3^{-d}\) times \((z/(1-z))^d\). All products remain bounded at infinity. Partial fractions now give (1) for every \(m\ge1\), with a constant polynomial quotient affecting at most \(m=0\). They also give (2). The argument proves the pole multiplicities on finite unit groups directly.

The first target-dependent term can be read off at \(z=1\). With \(p=1-z\),
\[
 3^d ((1-z)/z)^d F_d(z,y)
 =1+c_y(1-z)+O_d((1-z)^2),
\]
where \(c_y=(1/2,3/2,-1/2,-1/2,-3/2,1/2)\) for \(y\bmod9=1,2,4,5,7,8\), respectively. The finite mean-preserving proof is in [SPARSE_TILT.md](SPARSE_TILT.md). For fixed \(d\ge3\) this yields
\[
 a_{d,m}(y)=3^{-d}\left[{m-1\choose d-1}
                 +c_y{m-2\choose d-2}\right]+O_d(1+m^{d-3}).
\]
There are only \(2\cdot3^d\) target classes at fixed \(d\), so this error is uniform in \(y\). The constants here provide no fair-law asymptotic as \(d\) grows proportionally to \(m\).

## Exact first-arrival rows and initial even sources

Both pole statements have a physical first-arrival version, with a uniform clock onset. Let \(F^{\mathrm{first}}_d\) be the generating series for the odd sources counted only at their first visit to \(y\); set \(F_0=1\). To decide which series to use at grade \(d\), follow \(y\)'s forward trajectory for \(2d\) shortcut steps. If it returns, write \(H\) for its least positive return time and \(C\) for the number of odd departures on that lap. If no return is found, or if \(C>d\), then \(F^{\mathrm{first}}_d=F_d\). In the other case,
\[
 F^{\mathrm{first}}_d(z,y)=F_d(z,y)-z^H F_{d-C}(z,y). \tag{4}
\]
A repeated visit forces \(y\) to be periodic. Its positive return times are exactly the multiples of the least period. Removing the last lap gives a bijection from the non-first visits onto the visits at \((d-C,m-H)\), keeping the same source. Each complete positive lap obeys \(2^H=\prod(3+1/x)\le4^C\), where \(x\) runs through the odd departures on the lap. In particular \(1\le C\) and, if \(C\le d\), then \(H\le2d\), proving the finite test. A search ending without a return certifies the grade-\(d\) identity for all \(m\).

To include even sources, precede each odd source by any number of halving steps. Since the target is odd, the added even states cannot give an earlier visit. Unique dyadic factorization gives the series \(F_d/(1-z)\) for all visits and \(F_d^{\rm first}/(1-z)\) for first visits. At a nontrivial root of unity, neither this factor nor the subtraction in (4) increases the pole order. The lower-grade period divides \(B_d\). At \(z=1\), the subtracted series has smaller pole order because \(C\ge1\). Thus the odd first-hit and the all-parity first-hit counts at fixed \(d,y\) are also a polynomial plus a bounded \(B_d\)-periodic correction, for every \(m\ge2d+1\). Their polynomial degrees are \(d-1\) and \(d\), respectively, with leading coefficients \(1/(3^d(d-1)!)\) and \(1/(3^d d!)\). The uniform onset allows the possible polynomial quotient introduced by \(z^H\). Without the first-hit restriction, the all-parity result holds for \(m\ge1\).

## Bounded checks and source relation

[check_sparse.py](check_sparse.py) computes the integer arrays by taking the first gap equal to 1, or removing one doubling from that gap. At each clock it checks the exact Haar count \(2{m-1\choose d-1}\) summed over all \(y\bmod3^{d+1}\). With the default parameters it also checks (2) over every target for \(d=1,\ldots,5\) and 19 starting clocks at each grade, and cross-checks the entries against direct ordinary-integer recursion for \(1\le d\le m\le10\). The full clock range reaches 510. [Exact receipt](../../../reports/astra-infinite-descent-20261127/escape/SPARSE_CHECKS.json).

Wirsching's Elka-function generators and partition convolution already give rationality. The period shifts of individual valuation letters are also explicit in Wren's treatment. The finite character argument above gives the cancellation of repeated nontrivial poles for the specified terminal-unit rows. The first-arrival statement uses the additional least-lap identity (4). A fixed-grade row can include only the sources reaching its target. [Wirsching, §2](https://www.math.uni-bielefeld.de/baake/algdyn/posden.pdf) · [Wren, §§4–5](https://rstation.ai/problems/collatz/papers/10/v3).
