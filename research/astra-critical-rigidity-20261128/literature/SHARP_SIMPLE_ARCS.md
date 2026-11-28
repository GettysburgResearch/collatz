# Sharp denominator cost on simple open trajectories

**Status: PROPOSED.** For every fixed \(K\ge1\), the coefficient \(K-1\) in the [open rational height theorem](OPEN_ARC_HEIGHT.md) is optimal, even when every visited physical state is distinct, the starting magnitude stays bounded, and the arcs are powers of fixed words. The denominator varies. This construction does not produce a divergent ordinary orbit.

## The family

Use a finite Collatz fact with the following quantifiers: for every finite set of offsets there is a grade \(s\) and a threshold so that, at every sufficiently late chosen shortcut clock \(\ell\), a translate of the offsets reaches the ordinary target 1 at exactly clock \(\ell\) with exactly \(s\) odd departures. This is the \(v=r=s_{\rm ternary}=0,y=1\) specialization of [BlockClock.cover at PR212, 505d3fe782922904e86477990cc5d41e9110edda](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/merger/BlockClock.lean). The uppercase definition `Cover` specifies the predicate. The lowercase theorem `Collatz.BlockClock.cover` proves its existence for every finite list and every supplied precision: its proof composes the finite affine-profile coalescer with a two-gap arithmetic router. The theorem has no additional hypothesis. The stronger inverse-potential table and a positive-density conjecture are unnecessary. As an entirely explicit starting example, all fourteen integers from 2987 through 3000 have common endpoint 1 and common grade 14 at shortcut clock 34.

Apply this result to the offsets \(0,1,\ldots,K\), and choose \(\ell\) with \(2^\ell>3^s\). Write \(t,t+1,\ldots,t+K\) for the starts and \(w_i\) for their words, indexed by \(0\le i\le K\). Every word has length \(\ell\) and weight \(s\ge1\); if the common grade were zero, distinct starts could not reach the same point. Put
\[
 M=2^\ell,\quad N=3^s,\quad \delta=M-N,\quad a=N/M<1.
\]
The affine carry for \(w_i\) is \(C_i=M-N(t+i)>0\). The center is \(\alpha_i=C_i/\delta\), so
\[
 \alpha_{i+1}=\alpha_i-h,\qquad h=N/\delta>0.
\]
Thus the words are distinct, and the phase centers of each word are positive physical rational points. Indeed a word determines one residue modulo \(M\), its odd-denominator fixed point realizes those parities, and the affine formula returns it after one lap.

For integer \(r\ge 6\) put \(L=r\ell\), \(Q=M^r-N^r\) and
\[
 x_i=\alpha_i+\frac{h}{1-a^r}.
\]
At the start of \(w_i^r\) the excess over its center is \(hM^r/Q\). This is divisible by \(2^L\) in \(\mathbb Z_2\), hence the physical word agrees with that of \(\alpha_i\) for all \(L\) steps. The terminal point is
\[
 \alpha_i+\frac{a^r h}{1-a^r}=\alpha_i-h+\frac h{1-a^r}=x_{i+1}.
\]
Use the first \(K\) arcs, with a spare \((K+1)\)-st arc available to extend the path. Every starting physical value is positive. The reduced denominator of \(x_0\) is exactly
\[
 q=\delta Q=(M-N)(M^r-N^r).
\]
Its presented numerator is \(C_0Q+NM^r\), which is coprime to \(Q\) because \(\gcd(NM,Q)=1\). Also \(\delta\mid Q\), so the numerator is coprime to \(\delta Q\). In particular \(\gcd(q,6)=1\). All physical points have the same reduced denominator.

The physical horizon is \(D=KL\), while \(x_0\to\alpha_0+h>0\), \(\log_2 q=L+O(1)\), and \(\log_2\max(\operatorname{num}(x_0),q)=L+O(1)\). Thus the ratio in the open height theorem tends to 1. Decreasing the denominator coefficient by any positive constant for this \(K\) makes the ratio strictly less than 1 on this family. This proves sharpness even for a dictionary fixed once \(K\) is specified.

## Why the entire open path is simple

Suppose that two physical states at times \(u<v\le KL\) were equal. Equality persists under future iteration. Choose \(j\in\{0,\ldots,3\ell\}\) so both shifted times \(u+j,v+j\) have at least \(\ell\) prescribed bits before their respective arcs end. For each time the forbidden residues modulo \(L\) are the last \(\ell-1\) residues. For \(r\ge6\) an interval of \(3\ell+1\) candidate shifts meets at most one forbidden run (for \(\ell=1\) there are none); together the two times discard at most \(2(\ell-1)\) shifts. The spare arc supplies all prescribed future bits, even at \(v=KL\).

The next \(\ell\) bits agree at the two shifted times. Those words are the rotations of their respective motifs at the local phase. The corresponding rational phase centers therefore agree: each is the unique affine fixed point of the same length-\(\ell\) word. At any local time \(e\) from the beginning of an arc, with \(b\) odd departures so far, the difference from this phase center is
\[
       \frac{h}{1-a^r}\frac{3^b}{2^e}.
\]
Equality of the physical states forces equality of the two factors \(3^b/2^e\). Unique factorization gives the same local time \(e\) and odd count \(b\). The agreeing rotations were therefore taken at the same index modulo \(\ell\); undoing that rotation gives identical original words. Their distinct centers distinguish all arc indices. The two shifted times now have equal arc index and equal local time, a contradiction.

## Two direct controls

* For any \(K\), if simplicity is dropped, the primitive rational word \(0^m1\) has source \(2^m/(2^{m+1}-3)\). Repeat its whole period \(K\) times, using input reference 0 and output reference \(1/2\) on each arc. This cheaper example attains the same ratio, but its repeated states are essential to that example.
* For two simple powered arcs, take odd \(m\ge3\), \(q=2^m-1\) and \(x_0=2^m/q\). Its physical word is \(0^m1^m\). On the even run the numerators are the powers of two from \(2^m\) down to 1. On the odd run the numerator after \(j\) steps is \(3^j2^{m-j}-q\); before its last step these are odd, positive and strictly increasing. The last numerator is even and exceeds \(2^m\). Every visited state is distinct. The bounded real starting value and its exact denominator give the two-piece sharp rate without a routing theorem.

The simple-path construction requires no assertion about what happens after the spare arc. It neither identifies a nonconvergent ordinary source nor sharpens PR212's bounds for primitive **closed** rational cycles.

## Verification

The [integer checker](check_sharp_simple_arcs.py) constructs the first 14 motifs directly from the stated positive starts. Ordinary Python and optimized Python give identical counts for 68 simple prefixes, 147,398 charged states, and denominators up to 646 bits. It also verifies 3,400 states for the independent two-run family. The [fresh Lean receipt](ROUTER_FRESH_LEAN.json) records a complete rebuild of all eight pinned router modules and the [local consecutive-source specialization](SharpMotifInput.lean), run serially on Lean 4.34.1 with warnings treated as errors. A separate import-only audit checks the statements of both `Collatz.BlockClock.cover` and `Collatz.SharpMotif.consecutive_subcritical_motifs`. Each reports exactly `propext`, `Classical.choice`, and `Quot.sound`. The [replay script](replay_sharp_motif.py) verifies the eight source hashes before compilation. The [earlier receipt](ROUTER_REPLAY.json) preserves the prior kernel audit and an earlier fresh rebuild which reached four modules before `AffineProfiles` exited on signal 9. The optimality and simplicity arguments above are written proofs.
