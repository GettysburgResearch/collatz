# Exact maximal multiplicities at prescribed ordinary parity densities

**Proposed corollary O16, conditional on the proof of O15.** For the ordinary shortcut map let \(N_{k,q}(a)\) count positive sources \(j\) with \(T^k j=a\) and exactly \(q\) odd inputs among the \(k\) steps. Let \(M_{k,q}\) be its supremum over all positive endpoints. The identical supremum is attained at arbitrarily large endpoints of each ordinary positive merge component. For any sequence \(0\le q\le k\) with \(k\to\infty\) and \(q/k\to\theta\),
$$
\lim k^{-1}\log M_{k,q}=
\begin{cases}
 H(\theta)-\theta\log 3,&0\le\theta\le 1/3,\\
 (1-\theta)\log(3/2),&1/3\le\theta\le1,
\end{cases}
\qquad
H(\theta)=-\theta\log\theta-(1-\theta)\log(1-\theta).
$$
Use natural logarithms and \(0\log0=0\). In particular the maximum total number of depth-\(k\) positive shortcut predecessors has exponential rate \(4/3\). These maxima allow the target to change with the horizon or parity count.

## Ordinary realization

For a prescribed chronological shortcut word with \(q\) odd letters the set of legal endpoints is a single residue class modulo \(3^q\), with its affine inverse prescribed by the word. At sufficiently large ordinary endpoints in the class all intermediate integers are positive. This follows directly by splitting off the last letter as in O9. The same endpoint may support many words, which give distinct sources by forward determinism. Hence \(M_{k,q}\) is the maximum number of word congruences containing a residue, realized at all sufficiently large integers of any maximizing residue. For \(q\ge1\) such a residue is a unit, because after the final odd shortcut the endpoint is a unit and any remaining even shortcuts preserve this property. For \(q=0\) every endpoint has exactly one predecessor.

Every positive ordinary component contains a unit u, and its even inverse descendants \(2^j u\) traverse every unit modulo \(3^q\) at arbitrarily large heights since 2 is a primitive root. This already proves the component assertion. Odd endpoints are also available in any desired unit residue \(a\bmod3^q\): choose arbitrarily large \(j\) with \(2^j u=3a+1\bmod3^{q+1}\), then \((2^j u-1)/3\) is a positive odd endpoint in the same component and the required residue.

## A uniform upper bound

First count words beginning with an odd input. They consist of \(q\) positive-length blocks, each one odd shortcut followed by zero or more even shortcuts. If their lengths are \(e_1,\ldots,e_q\), their total \(s=\sum e_i\) is the shortcut time. For a target \(a\), the legal vectors read in reverse chronological order are exactly the legal depth-\(q\) words of O15 for the maps \(I_e(x)=(2^e x-1)/3\). This statement is for the shortcut parity word; when the terminal target is odd these are also the exact odd-to-odd valuations. A general word has \(k-s\) leading even inputs, whose inverse steps impose no additional ternary restriction. For a fixed \(s\) the induced weight of each word is \(3^q p^q(1-p)^{s-q}\). Thus, writing \(B_p\) for the O15 operator, whenever \(q\ge1\)
$$
 M_{k,q}\le (k-q+1)\ \|B_p^q\|\,(3p)^{-q}(1-p)^{q-k}.
$$
For any fixed \(p\in(0,1)\), O15 gives \(\|B_p^q\|\le C_\epsilon(\max(1,3p)+\epsilon)^q\). If \(0<\theta\le1/3\), choose \(p=\theta\); for \(1/3\le\theta\le1\), choose \(p=1/3\). Divide the logarithm by \(k\) and let \(\epsilon\downarrow0\) to obtain the displayed upper exponents. For \(\theta=0\), the elementary bound \(M_{k,q}\le {k\choose q}\) suffices.

## Matching lower bounds

Each length-\(k\) parity word with \(q\) odd inputs hits precisely one target residue modulo \(3^q\). The maximum is therefore at least \({k\choose q}/3^q\), giving the first exponent by the binomial entropy estimate. There is always at least one allowed word, including at the endpoints \(\theta=0,1\).

For \(1/3<\theta<1\), set \(m=\lfloor(k-q)/2\rfloor\), so \(1\le m\le q\) eventually. Choose a core of \(m\) odd blocks whose total shortcut time is \(s=m+k-q=3m\) or \(3m+1\). Among the \({s-1\choose m-1}\) positive compositions at least \({s-1\choose m-1}/3^m\) share one target residue \(b\bmod3^m\). Give each word the same outer prefix of \(q-m\) induced letters \(e=1\) in the contraction coding convention. The map \(G_1(x)=(3x+1)/2\) takes any fixed \(m\)-cylinder into a single \((m+1)\)-cylinder, and iteration preserves the common target for all these extended words. They have exactly \(q\) odd letters in \(k\) shortcut steps. Ordinary realization above supplies positive sources in every component.

Since \(s/m\to3\), the logarithm of this multiplicity is at least \(m(3H(1/3)-\log3-o(1))=m(2\log(3/2)-o(1))\). Now \(m/k\to(1-\theta)/2\), proving the second exponent. At \(\theta=1/3\) the ordinary binomial average already gives the meeting value. Maximizing the function of \(\theta\) gives \(\log(4/3)\) at \(\theta=1/4\). The upper passage from prescribed \(q\) to total count costs at most \(k+1\); any subsequence of maximizing \(q/k\) has a convergent further subsequence, so the all-density theorem applies. No part of this argument bounds the time to convergence of a prescribed ordinary source.
