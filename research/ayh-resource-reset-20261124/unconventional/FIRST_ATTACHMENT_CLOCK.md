# A smaller visitor pays a logarithmic clock cost at its first attachment

**Self-contained written theorem.** Use the shortcut map \(T\). Fix positive integers \(j,a\) with \(a\) odd and \(3\nmid a\). The ordinary source \(M=2^ja-1\) has increasing ascent
\[
 Y_u=3^u2^{j-u}a-1,\qquad 0\le u\le j .
\]
The final phase \(Y_j\) is even. Let \(0<x<M\) and write \(x+1=2^n b\) with \(b\) odd. The visitor starts with exactly \(n\) odd shortcuts, including the possibility \(n=0\).

If \(T^h x=Y_u\), even allowing previous contacts with the ascent, then \(h=n+t\) with \(t\ge u+1\). If \(u\ge1\) and the visitor's first contact with the prefix \(Y_0,\ldots,Y_u\) occurs at \(Y_u\) at clock \(h\), put \(B=t-u\). Then
\[
        t\le 6B\,3^{3B}\le 3^{6B},
        \qquad
        h\ge n+u+\max\!\left(1,\left\lceil\frac{\log_3 u}{6}\right\rceil\right).       \tag{1}
\]
The threshold is uniform in the original source, the smaller visitor and the length of either initial ascent. The time \(t\) counts every physical shortcut after the visitor's own ascent. This is a different resource from the surplus odd count in the [fresh inverse-gain estimate](FRESH_ASCENT_BARRIER.md).

## Before and after the visitor's first even input

For \(h\le n\), the visitor has value \(3^h2^{n-h}b-1\). If it equals \(Y_u\), comparing the translated heights gives
\[
       (3/2)^h(x+1)=(3/2)^u(M+1).
\]
Thus \(h>u\). After dividing the equality by \(3^u\), the left side of \(3^h2^{n-h}b=3^u2^{j-u}a\) is still divisible by three and the right side is a ternary unit. This rules out all \(h\le n\). The cofactor condition is relevant already here. With \(a=3\), for instance, the smaller \(2^{j+1}-1\) reaches \(M\) in one odd step.

Now write \(h=n+t\), \(t\ge1\), and let \(p\) be the odd count of these last \(t\) steps. An odd step multiplies the translated height \(v+1\) by exactly \(3/2\). An even step weakly decreases it. Consequently
\[
       (3/2)^u(M+1)=Y_u+1
           \le (3/2)^{n+p}(x+1),
       \qquad n+p>u.                                                    \tag{2}
\]
Track the last \(t\) steps from \(3^n b-1\), an even integer. At intermediate clock \(i\), let \(p_i\) count their odd inputs and write the translated affine identity as
\[
    2^i\bigl(T^{n+i}x+1\bigr)=3^{n+p_i}b+A_i .
\]
Initially \(A_0=0\). An even input adds \(2^i\) to \(A_i\), and an odd input multiplies \(A_i\) by three. The first input is even, so \(A_1=1\) and \(A_t>0\). At the meeting, \(3^u\) divides both \(2^t(Y_u+1)\) and \(3^{n+p}b\) by (2). Hence \(A_t=\ell3^u\) for an integer \(\ell\ge1\).

Let \(0=i_0<\cdots<i_{d-1}<t\) be the even input positions in these \(t\) steps. An addition at position \(i_r\) is multiplied by three once for every later odd input. Thus
\[
       \frac{A_t}{3^t}
       =\sum_{r=0}^{d-1}3^{-d+r}(2/3)^{i_r}
       \le 3^{-d}\sum_{r=0}^{d-1}2^r
       < (2/3)^d < 1.                                                   \tag{3}
\]
Here \(i_r\ge r\). Since \(A_t\ge3^u\), this proves \(t\ge u+1\) for every meeting.

## First attachment bounds the last even position

At \(u\ge1\) the target's unique odd shortcut predecessor is \(Y_{u-1}\). On first contact at \(Y_u\), the visitor therefore arrives by an even step. This includes \(u=j\). In (3) the last even index is now \(i_{d-1}=t-1\).

The left side of (3) is \(\ell3^{-B}\). Thus \(3^{-B}<(2/3)^d\), which gives \(d<3B\) since \((3/2)^3>3\). After removing the terms at \(i_0,\ldots,i_{k-1}\), \(1\le k<d\), the remaining sum is positive. Its denominator divides \(3^{\max(B,i_{k-1}+d)}\). Its value is at most \((2/3)^{i_k}\sum_{r=k}^{d-1}3^{-d+r}<(2/3)^{i_k}\). These two bounds give
\[
       i_k < 3\max(B,i_{k-1}+d)\le 3i_{k-1}+9B.                        \tag{4}
\]
Iterating from \(i_0=0\) gives \(i_{d-1}\le (9/2)B(3^{d-1}-1)\). Since \(t=i_{d-1}+1\), \(d<3B\), and \(6B\le3^{3B}\) for each positive integer \(B\), (1) follows. In fact the same proof gives \(B\ge\lceil(\log_3 t)/6\rceil\).

## Equality at every later phase of the original family

Take \(j\equiv5\bmod6\), \(j\ge5\), and \(M=2^j-1\). Since \(2^6\equiv1\bmod9\), the positive integer \(b=(2^{j+1}-1)/9\) is odd. The source
\[
               x=4b-1=(8M-5)/9<M
\]
has exactly two initial odd inputs. Their endpoint is \(9b-1=2M\), and the next even step reaches \(M\). From there it follows the entire target ascent. At each \(Y_u\), the visitor has taken exactly \(t=u+1\) steps after its own ascent. The every-meeting bound is therefore sharp at arbitrarily large phases. Its first attachment was at \(Y_0\).

In particular this example works for every original exponent \(j=11+162m\), \(m\ge0\). The original parent \(81z+271=128\cdot2^j\) satisfies \(z<2M\), whereas \(x>M/2\). The source \(x\sim8M/9\) does not meet the required rescue budget \(2^{40}x<z\).

The theorem bounds the clock of an actual visitor and leaves existence at the required budget open. The signed checkpoint carry comparisons for earlier Mersenne sources use a related ternary divisibility argument. Here the proof permits every smaller ordinary visitor and uses the positive sum in (3) for its original physical word. [Earlier checkpoint comparison](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/paired-reductions/SIMULTANEOUS_CHECKPOINT_DELAY.md)
