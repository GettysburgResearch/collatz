# Critical physical occupation and summable safe residence below first power

**Status: PROPOSED.** This proof uses the [odd-stride finite coalescence bound and moving-rank slicing](SUBLEVEL_MERGING.md). Put h=H_2(log_3 2) and beta=h/2. For an ordinary n>1 let L(n) be the number of physical shortcut steps consumed by its first maximal module A. For the set O of distinct values of **any one** positive shortcut trajectory, including a finite transient and a cycle, we obtain the uniform bound

    sum_{n in O, n>1, R(n)<=Y} exp(L(n)/32)
        <= C Y^beta/(log Y)^{3/2}                             (Y>=16).  (1)

In particular the weighted critical Mellin sum with terms exp(L(n)/32) R(n)^{-beta} over O is uniformly finite, with tail O(1/sqrt(log Y)). This counts each ordinary state once. The result also bounds the total actual shortcut time of any enlarged-safe excursion from n by O(R(n)^beta/(log(2+R(n)))^{3/2}), with an absolute constant. Under the safe-entry envelope f(n)<=C_0 R(n)^{-p}, the total Green occupation measured in raw shortcut time is finite already at p=1/2+beta=(1+h)/2<1.

## Distinct points of an ordinary orbit after a common clock

For any finite subset E of O and integer r>=0, |E|<=|T^r(E)|+r. If the orbit never repeats, T^r is injective on O. Otherwise O consists of a preperiod followed by a finite cycle. On the entire finite set O its rth image omits precisely the first min(r,preperiod length) transient values. The excess cardinality of any subset over its image is at most that of the whole set, by summing the excess sizes of fibers. Applied to points of O in an odd-stride finite progression, this adds at most the common clock to the progression's critical image count. No injectivity is assumed for an arbitrary union of basins.

## Weighting long physical modules

Write d=3^e and A_e=ceil(sqrt(Y/d))+1 in the minimizing-index and valuation slices of [the preceding note](SUBLEVEL_MERGING.md). Their source covers have odd stride d, at most A_e consecutive indices, and O(e+1) slices per e. T-A3-901 gives L(n)<=3 log_2(n+5)<=3 log_2(Y+6) for all inputs under consideration. Put L_max=floor(3 log_2(Y+6)).

For each ell>=1, an input with L(n)>=ell begins with one of at most ell+1 parity words of length ell. Indeed its letter sequence through that time is a prefix of (1^a0) repeated. For a=0,...,ell-1 this gives at most ell words, and all larger a give the all-ones prefix. In a d-stride progression the inputs on one such word occupy one residue of the index modulo 2^ell. After the common ell raw steps their images form a subset of a progression with odd stride

    d'=d 3^q,               A'=ceil(A_e/2^ell)

consecutive indices or fewer, where q<=ell is the weight. This holds because raising the initial index by 2^ell raises the output by d3^q; the physical map on a single word is injective. All of those images belong to O. An ell=0 copy of this argument without the word restriction counts the basic occupation.

For d<=sqrt(Y) and ell<=0.5 log_2 A_e, A'>=sqrt(A_e) and log A' is comparable to log Y for large Y. With sigma from the progression estimate (2), the main term for one word is at most

    C (1+log d+ell) d^sigma A_e^h/(log Y)^{3/2}
       * (3^sigma / 2^h)^ell.

The rounding in A' costs only a constant here. The additive orbit-cardinality correction is O(log Y log log Y) per cell: d'A' is at most a fixed power of Y throughout the allowed depth. There are only polynomially many cells in log Y (slices, ell and words). Sum the main terms with the factors (ell+1) exp(ell/32). This converges geometrically in ell because sigma<h/2 and

    exp(1/32) 3^{h/2}/2^h <1.

For example h>0.94 and log(2/sqrt(3))>0.14 suffice. The metric in e is summable too: (1+e)^2 3^{e(sigma−h/2)}. This gives the right side of (1).

For d<=sqrt(Y) but ell>0.5 log_2 A_e, one word has at most sqrt(A_e)+1=O(Y^{1/4}) source points per slice. For d>sqrt(Y), the total number of inputs, without a word restriction, is O((1+log Y)Y^{1/4}+(1+log Y)^2). After summing all remaining depths, words, slices and the earlier additive corrections, these terms cost at most a fixed polynomial in log Y times Y^{1/4} exp(L_max/32). They are absorbed by (1) because 1/4+3/(32 log 2)<0.39<beta. Finally exp(L/32)<=sum_{ell=0}^L exp(ell/32), so the summed threshold bounds imply (1). Partial summation on dyadic rank intervals gives the critical Mellin conclusion.

## Actual safe-entry budgets

Start at a boundary in G={n>1:R(A(n))<=R(n)} and end the excursion on first arrival at U or 1, or earlier at a fixed physical killing floor. Its live module sources are distinct by the oriented equal-rank theorem T-A3-1052, lie on one ordinary raw orbit, and have rank at most Y=R(n). Each contributes its physical length L, bounded by 32 exp(L/32). Applying (1) therefore bounds the *total physical duration* tau(n) before exit. Summing the number of module visits also satisfies the same estimate. Unlike multiplying a boundary count by a maximum module length, this preserves all three halves of the logarithmic saving.

Give actual entries nonnegative masses 0<=f(n)<=C_0 R(n)^{-p} supported in G. At p=1/2+beta the sum of f(n) tau(n) is bounded by an absolute multiple of C_0. Indeed, on a dyadic rank shell the global rank-ball bound O(sqrt(Y)) makes its contribution O(C_0/(log Y)^{3/2}). Summation over shells converges; shells above B contribute O(C_0/sqrt(log B)). Every larger p is included. Since the sum of surviving masses over discrete raw time equals the initial mass times lifetime summed over sources, this is a finite Green bound for actual safe residence.

More explicitly, for p>1/2 and t>=3 the safe mass whose excursion still lasts at raw time t is at most

    C_p C_0 t^{-(p-1/2)/beta} (log t)^{-3(p-1/2)/(2 beta)}.   (2)

The duration bound forces R(n)>=c t^{1/beta}(log t)^{3/(2 beta)} on such sources for large t. Use the global O(sqrt(Y)) rank counting bound to sum the envelope above that rank. At the critical p=(1+h)/2 this is O(C_0/(t(log t)^{3/2})), which is summable. The envelope is required for the incoming safe mass; its renewal after every unsafe leg is a separate question. The result puts no upper bound on the lifetime of the entire unsafe process.

The [finite replay](check_occupation.py) checks the low-cardinality module-prefix covers, actual odd strides after pushing a forced prefix, and the finite-preperiod additive correction against a tight example.
