# The marked reflected grade has both answers at every ternary precision

Call a positive odd integer \(c\) marked if some \(D\ge1\) gives \(m=17\cdot2^D-c>0\) whose first accelerated reflected visit to 17 has odd and physical counts \((7\ell,11\ell+D)\). The positive map is \(U(x)=(3x+1)/2^{v_2(3x+1)}\); the reflected accelerated map uses \(3x-1\) instead. This property is the signed part of the two-parameter cheaper-visitor test. There is no positive-root cost or source-cutoff condition in this definition.

For every \(p,t\ge0\) and residue \(u\bmod3^t\), there are arbitrarily large positive odd integers \(c,c'\), both congruent to \(u\bmod3^t\) and both satisfying \(3c\equiv3c'\equiv-1\pmod{2^p}\), such that \(c\) is marked and \(c'\) is unmarked. Both reach 1 within two accelerated odd departures. Thus no rule reading only a fixed finite number of low binary and ternary digits can decide this particular grade, even on these convergent inputs. If a positive-depth ordinary endpoint must be a ternary unit, impose \(3\nmid u\) for \(t\ge1\). Every such odd unit has an actual positive odd predecessor, since one parity of division exponents solves \(2^e c\equiv1\pmod3\).

**Marked family.** Put \(c_1(k)=(4^k-1)/3\), \(k\ge1\). For \(D=2k\), its complement \(m=(25\cdot2^{2k+1}+1)/3\) first goes to 25 with exponent \(2k+1\). The six steps from 25 then go through 37, 55, 41, 61 and 91 to 17 in ten physical clocks. The first arrival therefore has grade \((7,11+D)\), and \(U(c_1(k))=1\).

**Unmarked family.** Put \(c_5(k)=(10\cdot4^k-1)/3=(5\cdot2^e-1)/3\), \(e=2k+1\), \(k\ge0\). Its next positive state is 5, followed by 1. Suppose it is marked and write \(d=D-e\). The positive matching-depth cone gives \(r=c_5(k)/2^D>17(1-1000/1009)\), by the small same-phase product calculation and its seven-step propagation. To apply that result to a first-arrival grade, take the 17 phase and lift the signed word through any \(k'\ge\max(1,\ell)\) laps, with the remaining complete laps after the first signed visit. A nonprincipal competing word has the indicated strict ratio. From \(r=(5-2^{-e})/(3\cdot2^d)\) the lower bound forces \(d\le3\), since \(5/48<17(1-1000/1009)\). The strict positivity of \(m\) implies \(3\cdot17\cdot2^d>5-2^{-e}\), forcing \(d\ge-3\) since \(51/16<5-1/2\).

Factor \(51\cdot2^d-5=2^v B\) with \(B\) a positive odd integer. The first reflected step of \(m=(2^{e+v}B+1)/3\) reaches \(B\) with exact exponent \(e+v\). For \(d<0\) one has \(v=d\) and \(e+v=D\ge1\); otherwise \(v\ge0\). The source \(m\) cannot equal 17: a first arrival at time zero would force \(D=0\).

| \(d\) | \(v\) | \(B\) | First reflected arrival at 17 from \(B\) |
|---:|---:|---:|---|
| −3 | −3 | 11 | Reaches the fixed point 1 |
| −2 | −2 | 31 | 2 odd steps, 4 divisions |
| −1 | −1 | 41 | 3 odd steps, 6 divisions |
| 0 | 1 | 23 | 1 odd step, 2 divisions |
| 1 | 0 | 97 | Reaches the fixed point 1 |
| 2 | 0 | 199 | Enters the 5, 7 cycle |
| 3 | 0 | 403 | Reaches the fixed point 1 |

These seven first-hit or repeat checks are complete. In each finite arrival row, adding the first step from \(m\) gives 3, 4 or 2 odd steps. None is a multiple of seven. The family is unmarked at every exponent, even when competing physical exponents are unrestricted.

**The two residue conditions.** For \(k>j\),
\[
  v_3(c_1(k)-c_1(j))=v_3(4^{k-j}-1)-1=v_3(k-j).
\]
The equality follows by factoring a difference of cubes repeatedly, and by \(4^b-1\equiv3b\pmod9\) for \(3\nmid b\). Thus \(k\mapsto c_1(k)\pmod{3^t}\) permutes the \(3^t\) parameter residues. The identity \(c_5(k)=10c_1(k)+3\) gives the same conclusion for the other family. Choose each parameter independently in the appropriate residue class and sufficiently large to ensure \(2^p\mid4^k\). This proves the assertions for prescribed ternary digits and common binary digits. The two witnesses also have identical first \(p\) physical parities since they agree modulo \(2^p\).

**How many marked integers are there?** Although the marked set and its complement both have full ternary closure, the number of marked positive odd integers \(c\le X\) is
\[
                      O(X^{1-1/512}).
\]
Write \(r_0=153/1009\). The cone gives \(D\le\log_2(X/r_0)\). Put \(J=\lfloor(\log_2 X)/32\rfloor\). For \(\ell>J\), the first-arrival product bound (5) in `SIGNED_GRADE_SPARSITY.md` confines \(c\) to the interval immediately below \(17\cdot2^D\) of length \(O(2^D(J+1)(2048/2187)^J)\). Sum the geometric progression over the permitted \(D\). The resulting count is \(O(\log X+(J+1)X(2048/2187)^J)=O(X^{1-1/512})\), using \((2187/2048)^{16}>2\) with strict room for \(J+1\).

For \(\ell\le J\), each signed exponent word has at most \((7/32)\log_2 X\) positive parts and total at most \(N=(43/32)\log_2 X+O(1)\). Given \(D,\ell\), each such word and endpoint 17 determines at most one candidate \(m\), hence one \(c\). The number of compositions of length \(t\) and total at most \(N\) is \(\binom{\lfloor N\rfloor}{t}\), by choosing the cumulative sums. Since \(\binom{N}{t}\le(eN/t)^t\) and this upper bound increases with \(t\le N\), their number is at most \(19^{(7/32)\log_2 X}\) for sufficiently large \(X\), using \(e\cdot43/7<19\). Polynomial factors in \(\log X\) absorb the choices of indices. Since \(19^7<2^{30}\), this contribution is also within the claimed bound. The count is over ordinary *endpoint values*, whereas the sparsity estimate for \(S_h\) counts positive *ranks*. Weaver previously split short and long signed words to bound the size of a different exceptional set, whose endpoints approach twice a power of three. The estimate here is for the exact 17-grade and permits every ternary class in each of the two displayed terminating families. [Paper 180, Section 5](https://rstation.ai/problems/collatz/papers/180/v1)

The proof of the opposite-membership families uses the stronger written matching-depth cone as an input. The finite signed kernel and the seven arithmetic branches are separated from that comparison in `SignedGradeDigits.lean`. The module also kernel-checks the exact first-arrival exponent word for the marked family, including its physical division sum. Ternary coverage and the ordinary-height estimate above have written proofs. The question still asks for some actual marked visit at a later time of one fixed source, or for a cheaper visitor meeting that source; finite digit indistinguishability of the present predicate does not settle either question.
