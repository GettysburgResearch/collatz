# First-clock atoms weighted by the full ordinary basin

**PROPOSED, source-qualified written deduction.** Write \(P_X\) for the uniform positive source through \(X\), \(B_y\) for the full physical predecessor set of any positive integer \(y\), and \(d_y\) for its natural density. Put \(L=\log X\), \(b=\sigma\sqrt L\), with the normalization in the [native stopped transfer](../phase2/NATIVE_BINOMIAL_TRANSFER.md). Uniformly in \(y\), including even targets, and in the first physical time \(s\ge0\),
\[
                 bP_X(\tau_y=s)\le C d_y+o(1).                       \tag{1}
\]
The constant and the little-oh are absolute with respect to these two parameters. Thus the prior \(O(1/b)\) uniform atom estimate improves to little-oh on every moving sector \(d_y\to0\). [Earlier uniform bound, PR213](https://github.com/GettysburgResearch/collatz/blob/a743bd04d33945b15a1ec91deaca4a82c0261a07/research/astra-global-rigidity-20261128/mass/NATIVE_ENDPOINT_ATOMS.md)

The same argument keeps a signed clock on an escaping component. Fix one such component \(C\) and reference site \(a\). Put \(D(x)=i-j\) when \(T^i x=T^j a\), for \(x\in C\). Simplicity of the common future makes this independent of the merger. Thus \(D(x)=1+D(Tx)\), and \(D\) takes values in all of \(\mathbb Z\) as allowed by the component. Let \(y\) lie on the reference future. Then uniformly in \(s\in\mathbb Z\) and these \(y\),
\[
   bP_X(x\in C\setminus B_y,\ D(x)=s)
                       \le C_0(d_C-d_y)+o(1).                          \tag{2}
\]
The same estimate holds with the restriction \(x\in C\) alone and weight \(d_C\). These are absolute upper bounds. Their relative content concerns sectors above a fixed positive density.

## Uniform sampling of the marked sets

For odd \(y\), the uniform ordinary comparison
\(\sup_y|P_Z(B_y)-d_y|\ll(1+\log Z)^{-1/9}\) was proved in the [moving-clock theorem](../phase2/MOVING_CLOCKS.md). For even \(y=2^e a\) with \(a\) odd, restrict the physical-hitting indicator to odd starts \(x\). Its comparison with the value at the next odd site can disagree only if it hits \(y\) during that gap. Such \(x\) satisfy \(3x+1=2^k y\) for some \(k\ge1\), hence form a set with \(O(1)\) points per original octave, uniformly in \(y\). The extension from odd starts by stripping initial powers of two differs from the true indicator only at \(2^k y\), again with \(O(1)\) points per octave. Apply precisely the same sparse-exception theorem with uniform constants. For a complete component apply the theorem with no exceptional edges. In particular, if \(y\) is on the future in \(C\),
\[
 P_Z(C\setminus B_y)=d_C-d_y+O((1+\log Z)^{-1/9}),
\]
uniformly in \(y\) (also uniformly in the exact component coloring). Consequently, for every \(\delta>0\), all positive \(y\) with \(d_y\ge\delta\) lie on the futures of finitely many fixed integers. Choose \(Z\) at which the uniform error is smaller than \(\delta/2\). Each such basin then contains a source through \(Z\). The finitely many futures consist of finite sets and finitely many escaping rays. This includes their even intermediate vertices. [PR213 sparse countable labels, (1)–(2)](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/linear/renewal_landing.md)

## A clock at a fixed fraction of the initial log scale

Use the fair walk \(L_j=L-j\log2+B_j\log3\) and the crossing \(\mathcal T=\inf\{j:L_j\le H\}\) from the native transfer, with \(H=L/2\). Given the stopped path, choose an independent ordinary \(m\) uniformly through \(e^{L_{\mathcal T}}\in(e^H/2,e^H]\). For a specified first visit put \(D'=\tau_y\), allowing infinity. For (2) put \(D'=D\) on \(C\setminus B_y\) and \(D'=\infty\) outside. In both cases the following comparison holds in total variation, uniformly in \(y\):
\[
         \|\mathcal L_X(D')-\mathcal L(\mathcal T+D'(m))\|_{\rm TV}
                   \ll_A (1+H)^{-A}.                                  \tag{3}
\]
Indeed \(D'(n)=1+D'(Tn)\), with the convention for infinity, except possibly at \(n=y\). The signed starting-trit proof of (6) in the native transfer applies to all integer clock values: on a good cell of physical length \(s\), send the clock to \(s+D'(z)\), where \(z\) is the true endpoint. Only an early hit at the one exceptional vertex can give a wrong label. Through \(h\) steps there are at most \(2^{h+1}\) possible positive starts seeing this vertex, uniformly including an even vertex. Initial halvings seeing it cost at most \(1+\log_2 Z\) sources below cutoff \(Z\). The first-step defect at its own original vertex costs \(O(1/Z)\). The uniform strip-occupation bound then gives (3) exactly as at a fixed odd target. The case of \(C\) without the predecessor flag has no exceptional site.

At any possible crossing date \(j\), \(j\ge (L-H)/\log2\) and \(L_j\in(H-\log2,H]\) (with the harmless equality cases allowed). There are \(O(1)\) possible binomial grades in this strip, so \(\sup_j\Pr(\mathcal T=j)\ll L^{-1/2}\). For every integer \(s\) and large \(X\), positivity gives
\[
 \Pr(\mathcal T+D'(m)=s)\le
    3e^{-H}\sum_{m\le e^H:\,D'(m)\ne\infty}\Pr(\mathcal T=s-D'(m))
     \ll b^{-1}P_{e^H}(D'\ne\infty).
\]
Here the upper factor three follows from the stopped cutoff and its integer part. Take \(A>1\) in (3) and apply uniform sampling of the marked sets. This proves (1)–(2). On a nonperiodic \(y\), \(P_X(T^t n=y)=P_X(\tau_y=t)\) at any physical clock. No cycle lap is assigned this first-visit identity.
