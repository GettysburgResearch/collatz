# Independent review of the opposite-arm witnesses

I reconstructed the infinite-progression argument and replayed all 214 certificates independently, including ordinary positive trajectories on the first member of every progression. The result excludes 1,000 residue classes of the exponent parameter in this one family from supporting the specified globally least reverse defect, using the written \(2^{40}\) quantitative return premise.

**Ordinary realization.** Put \(D=3^d,\ p=E+d,\ j=97+162t\). For \(w=(2^{j+p}-m)/D\), the first exponent in each class satisfies the exact raw congruence \(2^{j+p}-m\equiv17D\bmod48D\). Incrementing \(t\) by \(3^{d-4}\) adds \(2\cdot3^d\) to \(j\). The power remains zero modulo 16 and the added exponent is \(\varphi(3^{d+1})\), so it retains its full residue modulo \(48D=16\cdot3^{d+1}\). I checked the raw congruence directly at the base and after one period. The base bound \(2^{97}>m\) gives positivity throughout. In the comparison with \(81z=1024\cdot2^j-527\), the slope inequality \(1024D-81\cdot2^p\ge1\) and \(2^j\ge2^{97}>527D\) give the strict bound \(w<z\) including its intercept.

**Parity and contraction.** I kept the denominator \(D\) fixed throughout. The numerator update is \(u/2\) for even \(u\) and \((3u+D)/2\) for odd \(u\). Before a clock \(\ell<j+p\), the difference between the ordinary trajectory times \(D\) and the shadow numerator is an odd multiple of \(2^{j+p-\ell}\), including the factor three on the upper arm. Thus the next parity agrees, all certified prefixes apply to every positive member, and physical positivity follows from the positive shortcut map. At the lower terminal this gives \(T^h w=3^{o-d}2^{j-(o-d)}-1=T^{o-d}M_j\). All rows satisfy \(0\le o-d\le j\). At the upper terminal the value is \(3^{O+1-d}2^{j+p-H}+c\). The zero-center rows have unit ternary coefficient and reach a power of two. For a \(+1\) center, each pair trades a factor four for three while retaining the \(+1\). The raw bound \(81\,2^{40+p}3^{O+1-d+k}<512\,2^{H+2k}\) and \(512\cdot2^j>81\cdot2^{40}+527\) give \(2^{40}n<z\) for the actual endpoint, with its additive one. The base has at least \(2k\) available binary digits, and this remains true throughout the progression.

**Minimality.** The parent \(z\) is the least positive reverse defect in the prescribed residue. The nonbasin hypothesis at \(M_j\) and the actual lower meeting imply that \(w\) is outside the basin. In the contraction case, if \(n\) were outside the basin, the quantitative return would produce a reverse defect \(w'\le2^{40}n<z\), contradicting this leastness. Hence \(n\), and thus \(3w\), is in the basin. Together with \(w\equiv17\bmod48\) and \(0<w<z\), this contradicts the same minimum a second time. This uses leastness among reverse defects, without presuming that every smaller integer converges. The numeric return premise is stated in RANK_TWO_DESCENT.md and independently audited in RANK_TWO_INDEPENDENT_REVIEW.md. The 214-row verifier does not prove that premise.

| Depth | Power rows | Contraction rows | Power classes modulo \(3^{10}\) | Contraction classes modulo \(3^{10}\) |
|---:|---:|---:|---:|---:|
| 10 | 2 | 0 | 162 | 0 |
| 11 | 9 | 4 | 243 | 108 |
| 12 | 9 | 6 | 81 | 54 |
| 13 | 33 | 51 | 99 | 153 |
| 14 | 31 | 69 | 31 | 69 |
| Total | 84 | 130 | 616 | 384 |

I checked each pair of distinct classes for incompatibility modulo the greatest common divisor of their periods. Thus there are exactly \(59,049-1,000=58,049\) classes outside this certificate. The independent program replayed 31,847 physical clocks at the first family members, the largest of whose exponents is \(9,355,111\). The maximum lower and upper shadow prefix lengths were 26 and 40. In the \(t=181\bmod2187\) example, the literal base \(j=29,419\) yields \(T^{21}w=M_j\) and \(T^{24}(3w)=2^{j-3}+1\), with 11 and 10 odd steps respectively. A separate literal 200-clock replay gives \(3^{100}2^{j-203}+1<z/2^{40}\). The row needs only 83 pairs in the general checker; the manuscript's 100-pair witness also works. The supplied checker passed normal and optimized Python executions.

**SHA-256 of the reviewed bytes**

| File | SHA-256 |
|---|---|
| OPPOSITE_ARM_CONTRACTION.md | f16df9358f69082d8077a2f6ca1e54a23a35a203ed15bedbcb6bd26bd9379313 |
| OppositeArmQueries.json | c95c810d5c917f9c36bbb851cc8956120d78e843f50bf519b88c6bf31eb7e0cf |
| check_opposite_arm_queries.py | 3feb38e68b93173449df7a6effe2add61d67a282922a8aaa0c8fb7dfdb16153b |
| check_opposite_arm_independent.py | fb6fdbddcaf154d0ba9af35906bc13934cb58e3df43d74a34337c9788ec12cd6 |
