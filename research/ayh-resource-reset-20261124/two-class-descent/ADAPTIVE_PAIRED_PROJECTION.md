# Polynomial-density projection inside exact common-source futures

Let $T(2z)=z$, $T(2z+1)=3z+2$. Start a fixed number $m\ge1$ of positive integer arms $a_i n+b_i$ on one common consecutive block of $H=2^h$ integers $n$. The $a_i$ are positive **odd** integers, and the $b_i$ can be signed. Keep the block label. Write $p_i$ for the number of odd inputs in the first $h$ steps, $Y_i=T^h(a_i n+b_i)$, and retain the ordered record $K=((p_i,Y_i))_{1\le i\le m}$. Thus a record and the block determine every physical future and its accumulated odd counts, simultaneously on every labeled arm.

Fix $0<\alpha<1$, $L\ge1$ and $B\ge1$. Define
$$
  \lambda_i=a_i3^{p_i},\qquad \lambda=\max_i\lambda_i,
  \qquad F=H/\lambda,\qquad
  J=(h+1)^m (1+L)^m B .
$$
In each record keep the good sources defined in the proof below. Discard their entire record fiber if its good size is less than $F/J$. Then discard all remaining fibers with $F<F_0$ if a common modulus range $F_0$ is required. On the unconditioned original block, the combined discarded probability is at most
$$
             C_{m,\alpha}L^{-\alpha}+C_m/B+\Pr(F<F_0).             \tag{1}
$$
Omit the last term if no further cutoff is imposed. Every retained good fiber $S$ has
$$
          |S|\ge F/J,\qquad \operatorname{diam} S\le LF.            \tag{2}
$$
Thus two-sided rank trimming at any integer $k_F\le F/J$ also costs at most $2C_m/B$ in original probability. This extra optional operation applies to eligible origins, keeping every good fiber member as a possible sibling.

For any integer modulus $q\ge1$ and any retrospectively chosen set of residues $E_S$, let $\epsilon$ be a common upper bound for $|E_S|/q$. Different records, block labels and known prefixes can use entirely different tests. Uniformly on every retained good fiber,
$$
 \Pr(n\bmod q\in E_S\mid n\in S)
 \le \min\{1,\ \epsilon J(L+q/F)\}.                               \tag{3}
$$
In particular the polynomial penalty is at most $(L+1)J$ when $q\le F$. This also holds if a prescribed arm's first $k$ parities are tested with $q=2^k$, since its first $k$ symbols form a bijective function of the common source residue. Formula (3) allows every union or mixture of retained good fibers, with their **actual** weights; no division by the probability of this union appears. For an unrestricted selected union of original record marks of probability $w>0$, add the original discard (1) divided by $w$. For example take $L=(h+1)^{(A+1)/\alpha}$, $B=(h+1)^{A+1}$ to achieve absolute discard $O((h+1)^{-A-1})$ plus the slope cutoff. For fixed $m,A,\alpha$ and $q\le F_0$, the conditional penalty in (3) is then a fixed polynomial in $h$. For $w\ge h^{-d}$ one can take $A>d$ and make the relative discarded fraction vanish at any requested inverse-polynomial rate by increasing $A$. Within such marks, retrospective tests of sufficiently high **inverse-polynomial** sparsity have inverse-polynomial exposure, to any prescribed fixed order.

## Exact affine projection and original-source count

Decompose each endpoint as
$$
        Y_i=\lambda_i n/H+c_i+e_i,\qquad c_i=3^{p_i}b_i/H.
$$
The additive intercept $e_i$ for that scalar word starts at zero and under a parity symbol $u$ evolves as $e'= (3^u e+u)/2$. Thus $e_i\ge0$. For uniformly chosen $n$ on the block, each individual arm has independent fair temporal parity symbols through $h$. This follows from the bijection between binary residues and length-$h$ parity words, and oddness of $a_i$. Different arms can be completely dependent. Subadditivity of the $\alpha$-power and independence of the scalar next symbol from its past imply
$$
 \mathbb E(e')^\alpha\le c_\alpha\,\mathbb E e^\alpha+2^{-1-\alpha},
 \qquad c_\alpha=\frac{1+3^\alpha}{2^{1+\alpha}}<1.
$$
The strict inequality follows from strict concavity at the two arguments $1/2$ and $3/2$, whose arithmetic average is one. Consequently $\sup_h\mathbb E e_i^\alpha\le 2^{-1-\alpha}/(1-c_\alpha)$. Declare a source good if every $e_i\le L$. Markov and a union bound give the first term of (1), uniformly in all slopes, offsets and block positions.

Now **fix the count vector** and let $i_*$ be a deterministic choice attaining its maximal slope $\lambda$. Across the whole block the anchor endpoint has range of length at most $\lambda+L$. Hence at most $1+\lambda+L$ integers can occur. For each fixed anchor integer the remaining endpoints belong to intervals
$$
 Y_i\in \frac{\lambda_i}{\lambda}(Y_{i_*}-c_{i_*})+c_i+[-L,L].
$$
This follows by subtracting $(\lambda_i/\lambda)e_{i_*}$ from $e_i$, since $0\le\lambda_i/\lambda\le1$. The location of each interval is fully determined; at most $1+2L$ integers lie inside. Thus the total number of good records at that count vector is at most
$$
     (1+\lambda+L)(1+2L)^{m-1}\le C_m\lambda(1+L)^m,             \tag{4}
$$
using $\lambda\ge1$. Conversely two good sources in the same record obey $|n-n'|=(H/\lambda)|e_{i_*}-e'_{i_*}|\le LF$. This proves the span. Each discarded undersized record costs at most $F/J$ sources, and there are at most $(h+1)^m$ count vectors. Inserting (4), the factor $\lambda$ cancels **exactly** against $F/H$. The total divided by $H$ is at most $C_m/B$, as claimed. The same count allows at most $2k_F$ rank-fringe origins per record. An interval of diameter $LF$ contains at most $1+LF/q$ integers in each residue class modulo $q$. Dividing the resulting numerator by $|S|\ge F/J$ proves (3). The integer fringe and residue counting steps are checked in [PairedSourceShuffle.lean](PairedSourceShuffle.lean).

## Conditional interior windows and ordinary rows

Suppose the original arms are fixed and there are $d$ native source bits on a full block of $2^d$ consecutive integers. Fix an initial $t$-bit residue class in that block. Parametrize its remaining values as $n=2^t v+u$, so $v$ runs over one full consecutive block of $2^{d-t}$ integers. Conditional on that entire prefix, the ordinary arm states at clock $t$ have exact forms $a_i3^{p_i(t)}v+c_{i,u}$ by the binary affine lifting identity. Apply (1)--(3) with $h=d-t$ in **$v$**, keeping $u$, the prefix states and their old counts. The total effective slopes at the end are $a_i3^{p_i(d)}$. The record therefore retains the known past and all physical futures from clock $d$. Tests on $v\bmod 2^k$ can be read as the next $k$ parity symbols of any specified arm after the prefix. There is no independence requirement between the chosen sparse middle-word test and the exact terminal record. The range is $2^k\le F=2^{d-t}/\max_i a_i3^{p_i(d)}$ for the simpler bound in (3). One can also use the exact $q/F$ expression.

For uniform data on the **original** full block with fixed $a_i$, take $t\le (a-\eta)d$ with fixed $\eta>0$ and $a=1-\tfrac12\log_2 3$. Then $F\ge2^{\eta d/2}$ outside $O_{m,\eta,(a_i)}(e^{-c_\eta d})$: apply Hoeffding to each $p_i(d)$ with a sufficiently small fixed linear allowance and absorb the fixed slopes for large $d$. This slope-cutoff probability is averaged over prefixes; some exceptional prescribed prefixes may have arbitrarily skewed early counts. On *every* given prefix the per-fiber theorem and its explicit conditional cutoff probability are valid. A modulus up to $2^{\eta d/2}$ can therefore be tested, including every fixed power of $d$, with the stated polynomial density loss after averaging the original prefixes.

For head rows $n\in[7X,8X)$, $X=81^{j-1}$, and the 81 choices $81n+r$, tile by aligned $2^d$ blocks with $d=\lfloor c\log_2 X\rfloor$, $0<c<1$, and discard the two partial ends of total relative mass $O(2^d/X)$. All coordinates of the selected head pair exceed every fixed polylogarithmic cutoff before clock $d$ since $T^k z\ge z/2^k$. Identical exact future records hence preserve both entrance values and both absolute clocks, both cumulative odd counts, and any ordered basin-color pair. The retained estimates can be applied within polynomially rare ordered landing-mark populations on each actual row. For control of their contribution to the original target series, use $A>1$ in (1), and make the right side of (3) $O(j^{-1-\xi})$ for a fixed $\xi>0$ by the retrospective test's prescribed sparsity. This proves summability for that tested part of any mark. The proof supplies no reason that all discordance passes a sparse retrospective test.

This extends [the scalar stopped sibling result of paper 124](https://rstation.ai/problems/collatz/papers/124/v1) and the earlier exponential-density paired shuffle [PAIRED_SOURCE_SHUFFLE.md](PAIRED_SOURCE_SHUFFLE.md). Its polynomial scale comes from anchoring both the endpoint census and the inverse span to the same largest physical slope. The result controls original residues in the past of the recorded futures.
