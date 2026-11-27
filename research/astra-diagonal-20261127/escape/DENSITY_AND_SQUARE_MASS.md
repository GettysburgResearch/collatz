# First-landing bounds for the compensated occupation deficit

Let \(B\) be any union of complete components of the ordinary positive odd Collatz graph, with odd-relative natural density \(d\). In particular \(B\) may comprise all positive odd integers that never reach 1. Put
\[
 V_s(B)=\sum_{x\in B}x^{-s}\quad(s>1),\qquad
 g=1-H_2(\log_3 2)+1/351 .
\]
Under the named first-landing results, with constants independent of \(B\),
\[
 V_s(B)\le C_s d^s,\qquad
 d\le C_s \exp\!\left(C_s\sqrt{\log(e+1/V_s(B))}\right)
         V_s(B)^{g/(s-1+g)} .                                      \tag{1}
\]
The second expression means zero when the input is zero. All the sets and moments use the unshifted positive integers, including the positive multiples of three. The argument also yields the following finite-data bound for the scalar \(L\) in the [compensated occupation theorem](COMPENSATED_OCCUPATION.md).

Let \(E_n=\sum_{U^nx\ne1}x^{-2}\), summed over positive odds. For every integer \(R\ge2\) and every \(n\ge0\),
\[
  0\le D/8-L
  \le (\kappa/4)F_R
       \left(\frac{\#\{x\le R:\ x\ {\rm odd},\ U^n x\ne1\}}{R}
                         +2R^{-g}\right)
  \le(\kappa/4) F_R (R E_n+2R^{-g}),                              \tag{2}
\]
where \(F_R=C_0\exp(C_1\sqrt{\log R})\); \(D=\log(4/3)\) and \(\kappa=D/2\).
The middle expression requires only finitely many exact ordinary trajectories. It remains valid when any selected sources are certified by other exact finite paths to 1, with the uncertified count substituted in the numerator. The imported constants \(C_0,C_1\) are ineffective. Thus (2) supplies a source-qualified lower estimate without a certified numerical value of \(L\). The estimates do not force the deficit to vanish.

## Proof

Use Weaver 102, Theorem 1, equations (1)–(3). For a first landing at or below \(R\), the membership in \(B\) of the source is identical to that of the landing point. Among failures of the landing, bound their entire mass. The cited set estimate at \(B\cap[1,R]\) and its separate failure bound give
\[
 d\le F_R\left(\#(B\cap[1,R])/R+2R^{-g}\right)
     \le F_R(R^{s-1}V_s(B)+2R^{-g}).                              \tag{3}
\]
This passage to natural density uses the unconditioned source law on a far factor-four interval and keeps the selected set intact. Choose \(R=\max(2,\lceil V_s(B)^{-1/(s-1+g)}\rceil)\). Inequality (3) proves the second assertion of (1), absorbing bounded input ranges into \(C_s\). [Weaver, *Power bounds for first Collatz landings and moments of ancestor labels*, Theorem 1](https://rstation.ai/problems/collatz/papers/102).

For the first assertion of (1), fix a factor-four interval \((X/4,X]\). For each odd \(x\in B\) there, select \(x\) itself if \(3\nmid x\), and \(Ux\) otherwise. Every selected target is an odd unit in the same component. The finite union of their full predecessor sets includes all these \(x\) and is contained in \(B\). Theorem 17, equation (47), gives the absolute bound \(K_0Xd\) on the count in that interval, including when some targets exceed \(X\). Its proof gives \(K_0=15/(8c)\) in terms of the uniform first-landing floor. Summing the geometric factor-four intervals gives
\[
  N_B(R)=\#(B\cap[1,R])\le K R d,\qquad K=4K_0/3 .
\]
If \(B\) is nonempty then its least source \(m\) thus satisfies \(m\ge (Kd)^{-1}\). Positive layer cake, starting at \(m\), gives
\[
 V_s(B)=s\int_m^\infty N_B(t)t^{-s-1}\,dt
          \le \frac{s}{s-1}K d m^{1-s}
          \le \frac{s}{s-1}(Kd)^s.
\]
The imported estimate is a uniform finite-sample comparison for a finite union, so no countable additivity of predecessor densities has been used in this step. Wren's uniform reciprocal predecessor floor also directly gives the order \(1/m\) for a least witness, including a nonunit witness after its first odd step. [Weaver, *First-landing bounds and canonical inverse laws for Collatz*, Theorem 17 and proof](https://rstation.ai/problems/collatz/papers/12) · [Wren, *A uniform linear lower bound for Collatz predecessor counts*, v2, Theorem 1 and its averaged joint mixing input (J)](https://rstation.ai/problems/collatz/papers/10/v2).

For the complementary basin of 1 the compensated law gives
\(3\kappa d/20\le D/8-L\le\kappa d/4\).
All starts in that complement fail to hit 1 at every fixed clock. Apply (3) and bound its finite count by the finite uncertified count or by \(R^2 E_n\), proving (2). The \(E_n\) decrease to \(V_2(B)\), by the fixed point at 1 and dominated convergence. Weaver 176, §5.3, already gives \(V_2(B)\le2.789369452262353\cdot10^{-24}\) by its outward-rounded finite certificate at the verified floor \(2^{71}\). That paper supplies the numerical bound, while (1)–(2) transfer the square mass or arbitrary finite survival counts to the actual compensated deficit. For \(s=2\) the reverse exponent \(g/(1+g)\) is approximately \(0.0502\); it is compatible with \(V_2(B)>0\) and \(d>0\). [Weaver, *Ternary harmonic moments and Collatz orbit occupation*, §5.3](https://rstation.ai/problems/collatz/papers/176).
