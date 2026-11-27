# A point-spectrum disk on every ordinary component

**Proposed theorem O14.** Every complex scalar of modulus strictly less than
```
sqrt(207384761192/93324220975) > 1.49070337
```
is a genuine eigenvalue of infinite multiplicity for the classical Bergman Collatz transfer on every ordinary component, with Béhani's quotient convention on the basin of 1. Together with O9 this leaves less than 0.000009 in radius between the proven point disk and the upper edge of the full spectrum. This proposition does not identify all eigenvalues.

## The finite lower certificate

Take the period 3^10 integer table v from O9, now setting its nonunit entries to zero. On the units the remaining entries lie between m=71736705115 and M=99999999999. A check over every unit residue and all three possible odd lifts gives
```
2v(2a)+(2/3)1_(a=2 mod3)v((2a−1)/3) ≥ alpha v(a),
alpha=207384761192/93324220975.
```
The least ratio occurs at the coarse residue 3995. A nonunit has a zero right-hand side, so the inequality holds there also. The replay script verifies the input digest and all 3^(10+1) actual lifted residues independently of how v was found.

## Actual Bergman edge weights and eigenvectors

For an ordinary edge from parent a to child j in the inverse graph let w(a,j) be the square root of (j+1)/(a+1), its Bergman Hilbert weight. For the even child the squared weight is 2−1/(a+1). For the odd child it is exactly 2/3. Accordingly at a unit a in a cycle-free inverse subtree
```
sum_{unit children j} w(a,j)^2 v(j) ≥ alpha v(a)−M/(a+1).
```
Fix lambda with |lambda|²<alpha and fix beta strictly between these squares and alpha. Choose N large enough that M/(a+1)≤(alpha−beta)m for a≥N. In any ordinary component O12 constructs infinitely many disjoint forks with two unit children and entire inverse subtrees; discard those that meet the finite set of positive integers less than N. Infinitely many remain.

Start at either unit child of a retained fork with x(root)=1. Keep only descendants reached through unit children and define recursively, with D_a=sum_j w(a,j)^2 v(j) over those children,
```
x(j) = lambda x(a) w(a,j) v(j)/D_a.
```
The denominator is at least beta v(a)>0. Then sum_j w(a,j)x(j)=lambda x(a). The weighted squared norm on one level contracts at each step since
```
sum_j |x(j)|²/v(j) = |lambda|² |x(a)|²/D_a
                    ≤ (|lambda|²/beta)|x(a)|²/v(a).
```
The bounds m≤v≤M on retained vertices imply square summability for the original normalized Hilbert coordinates. Define x to be zero off the retained unit tree. Other descendants of a discarded nonunit child cannot enter this support, and every vertex of the support except its root has its parent in the support. Thus all equations hold inside the full component except possibly at the parent of the root. Combine the two eigenflows from the two children of this fork, taking nonzero coefficients that cancel their sole common parent output. This gives a nonzero square-summable eigenvector on the full component. Distinct forks have disjoint supports, hence give infinitely many linearly independent eigenvectors. The construction includes lambda=0.

Source: V. Béhani, <https://arxiv.org/pdf/2303.03203>, Question 4.1, where the previously displayed open point disk has radius sqrt(2). The full spectral disk and the disjoint-fork construction are proved in O12.
