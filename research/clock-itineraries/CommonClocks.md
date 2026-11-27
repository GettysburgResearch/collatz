# Common clocks for prescribed Collatz targets

**PROPOSED, kernel-checked for the ordinary positive integers. Collatz remains open.** Write \(T(2n)=n\) and \(T(2n+1)=3n+2\). An odd unit is a positive odd integer coprime to three.

## One clock works for every target

Fix an odd positive \(w\) and a starting rank \(s\). There is an offset \(0\le d\le2^{1379}\) with the following property. Set \(A=s+d\). Prescribe any binary and ternary precisions \(H,K\) and parameter floor \(B\). There is a threshold \(N\) such that for **each** \(S\ge N\) and **each** odd unit \(b\) one can choose \(u>B\) and
\[
 w'=w+2^{1381+H+1}3^K u
\]
so that all 513 values \(3^{A+r}w'\), \(0\le r\le512\), have the same value \(y<3^A w'\) at clock 1,381, and all equal **the prescribed integer \(b\)** at clock \(1381+H+1+S\). The first \(H+1\) parity bits from \(y\) agree with those of the original merger on the tower of \(w\).

The rank interval is chosen once. Even the final clock can be chosen before the targets. Distinct targets at that clock require distinct ordinary bases. The constructed base can vary with the target and the clock. The theorem about the original base \(w\) itself still gives a common lower endpoint after 1,381 steps. Its subsequent convergence is open. [Exact quantifiers in Lean](TowerCopies.lean) · [Original merger certificate](TowerFrontierMergers.lean)

### Why all targets fit the same clock

On either certified binary class the common endpoint is affine in the free parameter, with slope a power of three. Preserving extra binary digits fixes a further forward parity prefix. At its end the free lift supplies an entire progression \(z+3^{G+1}v\). For any odd unit \(b\), two more odd gaps with lengths \(a,f\) and total \(S\) will work precisely when their ordinary source \(x\) satisfies
\[
       9x=2^S b-2^a-3,\qquad f=S-a .
\]
Choose \(a\) by solving \(2^a\equiv 2^S b-3-9z\bmod 3^{G+3}\). Its right hand side is a unit. The powers of two cover all units modulo this power of three, with \(1\le a\le P=2\cdot3^{G+2}\). If \(S>P\) and \(2^Sb>2^P+3+9z+9\cdot3^{G+1}B\), the source has the form \(z+3^{G+1}v\) with \(v>B\). These conditions allow a single threshold for all positive odd-unit \(b\). The full integer identity gives both positive odd intermediate edges and the exact shortcut clocks. This uses the ordinary two-gap router from PR #201. The bounded modular construction, the physical path, and its composition with the tower certificates are checked in the Std-only development. [Two-gap and exact-clock proofs](FiberRouting.lean) · [Earlier router](https://github.com/GettysburgResearch/collatz/blob/02fb390a76fb2ffb00fee612649ca23a82d99d31/research/killed-green-head-closure-20261124/verified/ExactClockRouter.lean)

### What the entire inverse fiber preserves

Let \(e_1,\ldots,e_k\) be any word of positive odd-return gaps with total \(L\). Moving a positive odd endpoint from \(q\) to \(q+2\cdot3^k t\) translates its exact sources by \(2\cdot2^L t\) in both directions. Nonexistent words remain absent. For a whole row of fixed \(k,L\) this is a single translation, and the quantity \(2^Lq-3^kx\) is unchanged.

One can preserve every incoming word of depth at most \(K\), at **all total clocks simultaneously**, the given finite forward parity prefix, and then route the resulting ordinary base to any prescribed odd unit at any sufficiently late common clock. Words of different total clocks or depths use the translation stated for their own row. In particular, the real location of the center and the later trajectory at the original gate still contain information. Counts and offsets alone do not determine that gate's convergence. The proof also gives dyadic terminal landings for targets of either parity coprime to three. [Whole-fiber translation](FiberTransport.lean) · [Common-clock theorem](FiberRouting.lean)

## An explicit remaining finite-count question

For the selected \(w,A,H,K,B\), choose one clock \(T_0\) from the fixed-clock theorem. For stage \(k\), use the earlier integer window size \(X_k\) and Pascal quota \(Q(k,\lfloor k/2\rfloor)\). Inspect the parameters \(B<u\le2^{T_0}X_k\). A parameter passes if one of its 513 ranks visits a chosen gate \(g\) by an observation time \(O\). The gate and observation time may vary by stage.

**Every positive input converges if and only if, at arbitrarily large stages, fewer than the quota of parameters fail.** To see the reverse implication, fix an eligible target \(q\). Its inverse tree supplies \(Q\) distinct odd-unit witnesses \(b\le X_k\) that reach \(q\). Route each \(b\) at the same clock \(T_0\). Distinct targets give distinct parameters. The elementary bound \(n\le2^{T_0}T^{T_0}(n)\) puts every one inside the inspected range. A passing parameter supplies an actual trajectory visiting both \(q\) and \(g\). Applying the same argument to \(q=1\) proves that \(g\) reaches 1. Conversely a finite set of convergent sources has a common observation deadline.

A uniform count at unbounded stages remains unproved. In particular, 513 paths merging before \(T_0\) cannot certify convergence on their own. The theorem routes arbitrary ordinary targets through such mergers at \(T_0\). [Full equivalence in Lean](TowerCapture.lean) · [Exact quota and height](WindowCapture.md)
