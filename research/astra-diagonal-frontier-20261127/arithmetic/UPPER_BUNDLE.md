# A homogeneous ceiling orbit above every ordinary cycle of width below eight

Let a primitive positive ordinary Collatz cycle have odd phases \(x_i\), least and greatest odd states \(s,X\), native edge valuations \(a_i=v_2(3x_i+1)\), odd period \(p\) and clock \(A=\sum a_i\). For an odd positive integer \(N\), let \(\mathcal G_N=\{2^j m:j\in\mathbb Z,\ 1\le m\le N,\ m\text{ odd}\}\). Let \(H_N(v)\) be the least point of this grid at least \(3v\). This nondecreasing map commutes with doubling. All its periodic odd-part components have the same lift rotation \(\rho_N\), measured in dyadic octaves per step.

Then, unconditionally and allowing every native valuation,
\[
 \boxed{\qquad (X+1)/2\le N\le4s\quad\Longrightarrow\quad\rho_N=A/p.\qquad} \tag{1}
\]
Only odd cutoffs occur, so the upper endpoint is actually \(4s-1\). Along growing cycles of fixed odd width \(X/s\le R<8\), the number of consecutive odd cutoffs in (1) is at least \((8-R)s/4-O(1)\). If \(X\le4s-1\), all those cutoffs from \(X\) through \(4s-1\) also have every ordinary phase eligible. This includes widths strictly above three, where the elementary comparison by the original phases can have strict edges even though its two rotations agree.

## The full ordinary orbit in a finite interval above each phase

Define the finite nonempty set
\[
                     J_x=\mathcal G_N\cap(x,x+1].
\]
The upper endpoint is eligible since \(x+1\) is even and its odd part is at most \((X+1)/2\). A noninteger grid point with reduced dyadic denominator at least four and value above \(x\) has odd numerator at least \(4x+1>N\). Therefore every element of \(J_x\) is either \(x+1/2\) or \(x+1\). The first is present exactly when \(2x+1\le N\).

For \(2^a y=3x+1\) and \(V\in J_x\), the exact bounds are
\[
       2^a y=3x+1<3V\le3x+3\le2^a(y+1).
\]
The right endpoint is eligible. Taking the homogeneous ceiling gives
\[
                           H_N(J_x)\ \subseteq\ 2^a J_y.                  \tag{2}
\]
Start at any member of \(J_{x_0}\). After \(kp\) steps its image lies in \(2^{kA}J_{x_0}\). The bounded normalized interval proves (1), either by dividing the lifted logarithmic displacement by \(kp\) or by extracting a periodic point of the finite normalized return. No separate estimate on individual factors of a word determinant is involved. The required integer grid and its ordinary full denominator one hold at every phase of the same orbit.

The points can also be followed exactly. Write \(w_i=x_i+1-d_i/2\), with \(d_i\in\{0,1\}\). The normalized transition on these two choices is
\[
  d_{i+1}=\mathbf1_{2x_{i+1}+1\le N}\,
                 \mathbf1_{\{a_i\ge2\}\,\cup\,\{d_i=1\}}.                 \tag{3}
\]
Indeed the smaller candidate output is \(2^{a-1}(2y+1)=3x+1+2^{a-1}\). If \(a=1\), the larger input has exact output \(3x+3\), while the smaller input rounds to this smaller candidate if it is present. If \(a\ge2\), both raw images are at most the smaller candidate. Equation (2) leaves only these two possible normalized outputs. Some edge has \(a\ge2\) since all exponent-one edges strictly increase a positive input. Such a step resets (3) independently of the preceding choice. More directly, set \(d_x=\mathbf1_{2x+1\le N}\). If \(a=1\) and \(2y+1\le N\), the strict increase \(x<y\) gives \(2x+1\le N\) as well. Hence this choice satisfies (3) on every individual admissible ordinary edge. Write \(\operatorname{succ}_N(v)\) for the strict successor of a real number in the grid. The unique cyclic bundle sequence is exactly \(w_x=\operatorname{succ}_N(x)\), and the pointwise formula is
\[
 H_N(\operatorname{succ}_N(x))=2^a\operatorname{succ}_N(y)
                              =\operatorname{succ}_N(3x+1).
\]
When \(N\ge X\), every ordinary phase is itself a grid vertex, so the orbit consists of its immediate right neighbors. The entire map may have additional periodic components.

Taking just \((x+1)/2\) as the ray representative gives a smaller independent endpoint. Write \(u=(x+1)/2\). Every integer in \([3u,2^a(y+1)/2)\) has form \(2^{a-1}y+j\) with \(1\le j<2^{a-1}\), hence has odd part at least \(2y+1\). Any noninteger dyadic grid point there needs odd numerator greater than or equal to \(6u\). Thus the plus shift alone gives the exact clock at all odd cutoffs \((X+1)/2\le N<2s+1\), at arbitrary valuations. The earlier shifted-clock packet established this interval on the binary branch, together with a different minus-shift interval. The two-point construction extends the upper end of the common interval by another \(2s+O(1)\). Its lower endpoint is sharp for eligibility of every \(x+1\): the maximum \(X\) has outgoing valuation at least two, so \(X\equiv1\pmod4\) and its endpoint has odd part \((X+1)/2\). [Earlier binary shifts](SHIFTED_CLOCKS.md)

## The first quarter point at the ordinary minimum

Assume \(s>1\) and \(X\le4s+1\). Put \(N_-=4s-1\), \(N_+=4s+1=n\), and \(\theta=A/p\). In particular \(N_-\) meets (1). At the single insertion from \(N_-\) to \(N_+\), the old bundle component is destroyed. Either the rotation drops strictly to its next attained Farey neighbor, or the rotation stays \(\theta\) and the number of periodic components decreases by exactly one. In the latter case \(n\) is transient.

Here are the endpoint and transience arguments. The native predecessor \(m\) of the minimum satisfies \(3m+1=2^a s\) with \(a\ge2\). Formula (3) gives \(w_s=s+1/2\) in the old grid. If \(a=2\), then \(m=(4s-1)/3<3s/2\). Its own incoming exponent is at least two, as an exponent-one predecessor would be \((2m-1)/3<s\). Also \(2m+1\le4s-1\), so \(w_m=m+1/2\). In this case, or when \(a\ge3\) and either choice of \(w_m\) is possible, one has
\[
                  4s<3\,2^{2-a} w_m\le4s+1.
\]
For \(w_m=m+1/2\) the additive excess is \(2/2^a\), and for \(w_m=m+1\) it is \(8/2^a\). The old raw image ceiling equals \(4w_s=4s+2\). The insertion of \(n\) lowers it to \(4s+1\), since the old successor and the new point are consecutive here. This exhibits the actual changed edge on the periodic bundle.

The point \(n/4=s+1/4\) has new image exactly \(3s+1\). Its raw triple is \(3s+3/4\), and no eligible strict intermediate point has reduced denominator below eight; dyadic points with larger denominator require an odd numerator exceeding \(N_+\). The raw triple itself has odd numerator \(12s+3>N_+\). The target is eligible since its native odd part is at most \(X\le N_+\). From then on, every true raw output is eligible, so \(H_{N_+}(x)\le3x+1\) throughout the cycle. By monotonicity,
\[
             H_{N_+}^{kp}(n/4)\le 2^{kA}s<2^{kA}n/4\qquad(k\ge1).
\]
Any periodic component of rotation \(A/p\) has a period dividing \(p\), by the order-preserving translation of its ordered lifts and reduction of that translation. Hence \(n\) cannot belong to such a component.

Only one old odd-part vertex changes its outgoing edge at this insertion. In the normalization near \(n\), a changed input must have triple in \((n-1,n]\). An integer or half-integer in the divided input interval is unique when one exists, and any input of denominator at least four there has odd numerator greater than \(n-2\). Equivalently the possible source is \(n/3\) if \(n\equiv0\pmod3\), or \((2n-1)/6\) if \(n\equiv2\pmod3\). The exhibited old edge gives the unique one. Every other old component survives. Every new periodic component which uses the changed edge must contain \(n\), so in the equal-clock case none can replace the destroyed one. If the old component was unique, this forces a strict drop. At a strict drop the adjacent-cut Farey-neighbor identity is the elementary one-insertion theorem of the earlier packet. [One-insertion identity and actual comparison counts](HOMOGENEOUS_MEETINGS.md)

For \(X\le N\le4s-1\) the earlier exact winding identity also says that every homogeneous periodic component avoids every true phase \(x\) with \(3x\le N\). The construction above does not ensure uniqueness of the full homogeneous component at \(4s-1\), and it gives no independent upper bound on the length of a homogeneous rotation plateau. There is no contradiction for the remaining ordinary cycles.

[Exact finite ordinary edges and critical-cut controls](check_upper_bundle.py) · [Recorded controls](upper_bundle_controls.json)

A separate [component-lifetime theorem](PLATEAU_COMPONENTS.md) gives an exact birth/death formula and the asymptotic factor-two bound for each unchanged component. It also counts the same-rotation replacements that a hypothetical ordinary cycle itself supplies. This distinction prevents treating the lifetime of one component as the lifetime of the full rotation plateau.
