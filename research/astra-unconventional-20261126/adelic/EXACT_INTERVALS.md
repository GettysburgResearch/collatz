# Consecutive ordinary inputs at supplied exact clocks

**PROPOSED, source-qualified written theorem.** The primary [integral lattice theorem](MOMENT_LATTICE.md) has an elementary proof within this round. This strengthening also uses the analytic fixed-total estimate (76) of a separate research paper and the synchronized-prefix tail estimate (4) from an earlier branch. Given a positive odd ternary-unit endpoint \(y\) and \(d\ge1\), take
\[
                   k\ge A\log^2(2d+2),\qquad H\ge2k-c\sqrt k.        \tag{1}
\]
For absolute \(A,c>0\), **every** exact fiber \(S_{y,k,H}\) in (1) contains \(d+1\) consecutive positive odd numbers. Its degree-\(d\) binomial evaluation matrix thus has one actual unit determinant since its half-odd coordinates are consecutive. The stronger terminal-specific condition
\[
              k\ge A'\log^2(2d+2),\qquad
              H\ge C_k(y)+B'\log^2(2d+2)                             \tag{2}
\]
suffices as well. Here \(C_k(y)\) is the least unit-ended inverse cost. Neither assertion requires changing the terminal when \(k,H,d\) are specified. In (1), one may choose \(k,H=O(\log^2(2d+2))\), giving maximum witness height \(y\exp(O(\log^2(2d+2)))\).

## Two precise inputs

For the shortcut map \(T(x)=x/2\) at even input and \((3x+1)/2\) at odd input, let \(P_h(x)\) count odd inputs before clock \(h\). The pinned synchronized-interval result gives probability of failure \(O(\log(2M)/\sqrt h)\) for the first group of \(M\) consecutive inputs to have identical ordinary endpoints *and* counts at clock \(h\), under a uniform binary starting residue. The estimate there is stated by the first successful time for two groups of affine profiles. Equality within the first group persists at every later time. We use only this first-group consequence. [Whole interval synchronization, Theorem and (4), commit f431078244e868dc699fad011044f0d5e7f76437](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md)

A second input gives the following central-clock inversion consequence. For all sufficiently large \(n\), \(|s-2n|\le\sqrt n\), \(1\le K\le\delta_*(n-1)\), every positive odd ternary unit \(z'\), and every unit residue \(w_*\bmod3^K\), some true inverse path from \(z'\) has exactly \(n\) gaps, total exactly \(s\) and source \(w\equiv w_*\bmod3^K\). To check the central-total extension, let \(R=z'-3^n2^{-s}w_*\bmod3^{n+K}\), a ternary unit. For the fixed cylinder \(u_0\bmod3^{h_0}\) of (76), choose \(1\le v\le2\cdot3^{h_0}\) with \(2^vR\equiv1+3u_0\bmod3^{h_0+1}\). At length \(n-1\), total \(s-v\) and extra depth \(K\), estimate (76) supplies a word of normalized offset \((2^vR-1)/3\) at depth \(n-1+K\). The bound \(|s-v-2(n-1)|\le2\sqrt{n-1}\) holds uniformly for large \(n\), as \(v\) is bounded. Prepending \(v\) changes the normalized offset to \(R\) and restores total \(s\). The identity \(z'=3^n2^{-s}w+\beta\) now makes the source integral in the requested class. Reducing the full congruence through the successive reverse cuts gives integrality of every intermediate state. A positive integer reverse quotient \((2^e z-1)/3\) is positive odd, since its numerator is odd and at least one. This is the same spreading argument as Theorem 8's proof, with central \(s\) retained. [lyapunov_weaver and fourier_wren, paper 48 v2, Lemma 7 (76) and Theorem 8, equations (81)–(84)](https://rstation.ai/problems/collatz/papers/48)

## The synchronized cylinder and the grade equations

Take \(M=2d+2\). At a fixed \(h=\lceil C\log^2(2M)\rceil\), the first input makes the synchronized event have probability at least \(3/4\). The first arm has uniform parity vector through \(h\), because successive incomplete integer affine forms have odd free slope, so its count \(p\) has the binomial \((h,1/2)\) law. By the variance bound the event \(|2p-h|\le4\sqrt h\) has probability at least \(15/16\). We may choose a binary residue \(0\le r<2^h\) satisfying both events. Enlarge \(C\) so that \(p\ge1\), whence \(r>0\). If \(z=T^h(r)\), then \(3\nmid z\) because the first odd departure makes the state a unit modulo three and both types of shortcut step preserve that property thereafter. Also \(z\le3^h\) by iterating \(T(u)+1\le(3/2)(u+1)\). The exact affine profile therefore gives, for every integer \(t\ge0\) and \(0\le j<M\),
\[
        T^h(r+2^h t+j)=z+3^pt,\qquad P_h(r+2^h t+j)=p.             \tag{3}
\]
This step retains one ordinary cylinder and its actual common endpoint at all lifts; synchronizing a statistic alone would not give (3).

Set \(w_*=z+3^p\) and choose \(K\ge p\) such that \(3^K>w_*\), with \(K=O(h)\). Under (1) put
\[
             n=k-p-1,\qquad \ell=H-h-2n=H-2k+(2p-h)+2 .
\]
Choose an integer \(e\in[\max(2,\ell),\max(2,\ell)+5]\) with \(2^e y\equiv4\text{ or }7\pmod9\). Then \(z'=(2^e y-1)/3\) is a positive odd unit. The remaining total \(s=H-h-e\) satisfies
\[
                    -\sqrt n\le s-2n=\ell-e\le0 .
\]
Indeed, for \(\ell\ge2\) the deficit is at most five, and otherwise \(e-\ell\le 7+c\sqrt k+4\sqrt h\). Take \(c\) small and the constant \(A\) large enough that this is at most \(\sqrt n\), while also \(K\le\delta_*(n-1)\) and the fixed onset for the analytic input holds. Applying that input to \(z'\) supplies a positive odd \(w\equiv w_*\bmod3^K\) at precisely \((n,s)\). Since \(0<w_*<3^K\), we have \(w\ge w_*>z\). Thus \(t=(w-z)/3^p\) is a positive integer.

All \(M\) consecutive starts in (3) now have the same ordinary endpoint \(w\), which is odd, and the same count \(p\). Select the \(d+1\) odd starts. For each of them the \(h\) initial shortcuts comprise exactly \(p\) complete odd gaps because both endpoints are odd. Following the true path through \(z'\) to \(y\) adds \(n+1\) odd gaps and \(s+e\) shortcut steps. The totals are
\[
                        p+n+1=k,\qquad h+s+e=H .
\]
This proves (1). It also proves the whole \(M\)-start statement for the shortcut map, using odd-departure grades when a start is even.

For (2), reserve \(r_0=\lceil A\log^2(2d+2)\rceil\) inverse edges at the end of a length-\(k\) minimizing path. The first \(k-r_0\) edges reach a fixed unit at cost \(s_0\le C_k(y)-r_0\). Supply at that unit the consecutive block from (1), with \(r_0\) gaps and total \(H-s_0\ge2r_0\) after increasing \(B'\) absolutely. Appending the fixed tail proves (2). Consequently for each \(\epsilon>0\) the exact single fibers at all \(H\ge(\tau+\epsilon)k\) and all sufficiently large \(k\) contain \(\lfloor\exp(c_\epsilon\sqrt k)\rfloor\) consecutive odd sources, uniformly in \(y\). Here \(\tau\) is the worst-terminal minimum-clock limit in the elementary note.

Earlier fixed-terminal synchronized-basin results already give many consecutive intervals and quantitative bounds at prescribed grade residues, and a second result addresses first-hit timing. This claim specifies both absolute clocks independently at the supplied endpoint; its analytic inputs retain their source qualification. A chosen block can lie high above that endpoint. [Earlier synchronized long basin blocks, commit 3b10b24d12d4b349cb20f4cbc83086c8a09f807e](https://github.com/GettysburgResearch/collatz/blob/3b10b24d12d4b349cb20f4cbc83086c8a09f807e/research/synchronized-long-basin-blocks-20261124/README.md) · [Earlier prefix-density construction, commit b68cf8f0fd565c4bb2151afc3ce7668f8801770d](https://github.com/GettysburgResearch/collatz/blob/b68cf8f0fd565c4bb2151afc3ce7668f8801770d/research/killed-green-head-closure-20261124/prefix-density/README.md)
