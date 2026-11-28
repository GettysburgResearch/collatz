# Separate grade costs and a linear obstruction when one arm has bounded grade

**PROPOSED elementary theorem.** Use the positive shortcut map on the two odd inputs $s,3^r s$, $r\ge0$. Suppose their states are distinct at each common native date through $k$. Let $g,h$ count their respective odd departures through $k$ and let $J$ count the dates when both depart from odd states. Then
$$
 2^k \max(1,|d_k|)\le 4^{g+h}3^{g(h+r)-J},\qquad
 d_k=3^g T^k(3^rs)-3^{h+r}T^k(s).                              \tag{1}
$$
Thus if **either one** of the two grades is bounded and $r$ is fixed, the native clock is at most linear in the other. The determinant remains an integer at every step.

At date $t$ put $V=\max(1,|d_t|)$, and let $a,b\in\{0,1\}$ indicate the two odd departures, with cumulative grades before them $g_t,h_t$. From the [signed one-step equation](SPARSE_DISCREPANCY_BLOCKS.md) we have
$$
       2V_{t+1}\le (3+3^{h_t+r})^a(3+3^{g_t})^b V_t .          \tag{2}
$$
For $a=b=0$ the positive determinant magnitude halves exactly. Indeed the endpoint determinant cannot vanish at any unmatched date after time zero, using ternary units, and the initial date has both starts odd. For $a=1,b=0$ the signed numerator is $3d_t-3^{h_t+r}$, with analogous $3d_t+3^{g_t}$ for the other single departure. For $a=b=1$ it is $9d_t+3^{g_t+1}-3^{h_t+r+1}$, and the product on the right also contains a nonnegative term $3^{g_t+h_t+r}$. Every active case also bounds the alternative $2$ in $2\max(1,|d_{t+1}|)$.

Use $3+3^z\le4\,3^z$. On multiplying through $k$ the exponent of three is
$$
 \sum_{t<k}\!\left[a_t(h_t+r)+b_tg_t\right]=g(h+r)-J.
$$
This follows by expanding $(g_t+a_t)(h_t+b_t)-g_th_t$. Since $V_0=1$, this proves (1). The elementary quadratic bound can be recovered by bounding the grades jointly, while (1) retains their different costs.

## Two supplied unequal-clock visits

Suppose fixed positive forward-incomparable targets $u,v$ are reached from $s,3^rs$ at native clocks $i,j$ and full respective odd grades $g_*,h_*$. Through $k=\min(i,j)$ the paths cannot coincide, and $\log_2(s/\max(u,v))\le k$. If $h_*\le H$, then
$$
 g_* \ge
   \frac{\log_2(s/\max(u,v))-2H}{2+(H+r)\log_2 3}.               \tag{3}
$$
If $g_*\le H$ the corresponding bound is
$$
 h_* \ge
   \frac{\log_2(s/\max(u,v))-(2+r\log_2 3)H}{2+H\log_2 3}.
$$
Indeed in (1) one can discard $\max(1,|d_k|)$ and $J$, then use each grade through $k$ bounded by its full marked-path grade. These inequalities apply to the physical pair with its supplied targets, even if the two targets eventually meet elsewhere. Formula (3) constrains fixed-grade upper-arm constructions in the native joint visitor problem. It does not claim that an arbitrary catalogued upper-arm witness reaches a prescribed target on its lower arm.

For an unrestricted pair of growing grades the subquadratic theorem is a different estimate. Neither the elementary product bound nor an improvement in its constant supplies an upper bound on the lower grade of a proposed counterexample.
