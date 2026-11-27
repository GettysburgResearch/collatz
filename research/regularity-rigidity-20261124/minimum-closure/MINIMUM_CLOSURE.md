# Minimum bad multiple: exact strip bound and the limit of bounded inverse screening

24 November 2026. **PROPOSED written research. Collatz remains OPEN.** This pass tests the direct least-bad-multiple approach rather than extrapolating a stationary inverse count. It gives a strengthened actual-orbit bound and an unbounded family of nonordinary rational controls that survives a depth-192 minimum-source screen. The complete denominator separates these controls from ordinary integers. The growing branch and arbitrary nonmechanical bounded-cycle branch remain unclosed.

Use T(x)=x/2 for even x and (3x+1)/2 for odd x, and U(x)=(3x+1)/2^v2(3x+1) on odd x. An odd gap e is a positive valuation in the latter formula; the inverse I_e(y)=(2^e y-1)/3 is legal if the resulting odd state is integral in the domain under discussion.

## 1. Retain the actual least bad multiple

Input M: PR192 at 26f070c38ad9edd21ed7dac6efaab6554550c2a3, research/astra-minimum-source-20261124/minimal/MinimumFailure.lean, proves that if a counterexample exists, there is a least odd tripling disagreement q, q converges, n=3q does not, every smaller positive multiple of three converges, and all positive starts through q converge.

Input E: PR205 at 32d722c5d5597846da5dad842c8ea15742abc176, research/astra-fixed-target-closure-20261124/ordinary/README.md and HEIGHT_STRIP.md, gives the following ordinary excursion. Set s=(n-1)/2. The chain begins at n or at the recentered bad state s, and its completed interior odd runs have exactly one even step, with odd-run entries between s and 2n. It must either cross 2n or repeat. In the repetition case q=1 mod 12, s itself is the cycle minimum, and all cycle odd-run entries are at most 2n. The original trajectory of n reaches the crossing or the cycle (the recentered path has the explicitly proved merger). This is a source-qualified input, not recompiled in this session. The first/last and recentering overheads are O(log n).

On the complete interior chain, every accelerated gap is 1 or 2. The largest odd input in a completed run is at most (4 y'-1)/3, where y' is the next run entry. Consequently all odd states in the completed bounded segment lie in

    [s,(8n-1)/3]=[s,(16s+7)/3].

The final crossing run is charged separately, with length at most log2(2n+1)+1 physical steps. The same bound on odd states applies throughout the cycle branch, with cyclically extended pasts.

## 2. A sharper exact ordinary strip count

**Theorem S (conditional only on M and E).** For sufficiently large q in the least-bad-multiple alternative of Section 1, the original trajectory crosses 6q or reaches the specified nontrivial cycle within O(q^(479/1000)) shortcut clocks. The odd period p in the cycle branch is O(q^(479/1000)). For large p its reduced physical-period/odd-period ratio is an upper convergent of log2 3 with error O(p^(-1000/479)). This improves the source exponent 49/100; it does not contradict the known effective irrationality bound.

Proof. Take s>=2^30. For a segment of at most N=4096 odd steps with gaps 1 or 2 and all odd states in the displayed strip, set

    R=16003/3000, Q=100001/100000,
    A_j=e_1+...+e_j, r=x_0/s.

The actual normalized height at step j equals r 3^j/2^A_j times the product of the j odd corrections (1+1/(3 x_i)). This product is between 1 and Q: for t=1/(3s), (1+t)^N <=1/(1-Nt) <=Q, using the geometric majorant of the binomial sum. The height cap is at most R. Both numerical inequalities are checked by integer cross multiplication.

For D=128 cover r in [1,R] by bins [i/D,(i+1)/D], D<=i<=floor(DR). A necessary condition on A_j is

    i*3^j*3000 <= D*16003*2^A_j,
    (i+1)*3^j*100001 >= D*100000*2^A_j.

These conditions deliberately allow a different r inside the bin at different steps; hence the resulting count is an upper bound. For fixed i, start with one empty word at A_0=0, then add 1 or 2 at each step, retaining only the two inequalities. Sum the final counts over all 555 bins. Denote this overcount by C. The exact recurrence in controls.py yields C of bitlength 3106 and verifies

    C^1000 < 3^(479*4096).

The exponent search at step j may safely be limited to |A_j-floor(log2(3^j))|<=4: from 1<=r,x_j/s<=R and 1<=product<=Q we get 1/(RQ)<=3^j/2^A_j<=R, with RQ<8. The program uses integer bitlength and integer comparisons only. No approximate logarithm is used to establish the certificate.

For any k, split a length-k past into complete N-blocks and a remaining block. Each complete block, regardless of its actual start height, has at most C possible words; the residual has at most 2^N. Thus there are at most 2^N C^floor(k/N) <= 2^N 3^(479k/1000) words. The exact affine formula for k odd steps puts the final value of each word into a single residue modulo 3^k, because 2^A is a unit there. Set k=ceil(log_3(M+1)), where M is an integer upper bound on the strip. There is at most one positive integer <=M in each residue class. Apart from the first k states of a nonrepeating bounded path, every odd state has such a past. In a cycle use cyclically extended pasts of length k even when k exceeds the period. Hence the number of distinct ordinary odd states is O(M^(479/1000)), with an absolute, nonoptimized constant. Each costs at most two shortcut clocks within the completed segment, and the O(log n) boundary allowance is negligible. Apply E to attach the same bound to the original n.

For a cycle of p odd inputs and h shortcut clocks the exact product gives

    0 < h/p-log2(3) = (1/p) sum_i log2(1+1/(3x_i)) <= 1/(3 s log 2).

Since p=O(q^(479/1000)) and s=(3q-1)/2, the claimed error follows. It is eventually less than 1/(2p^2) as p grows; after reduction the standard continued fraction criterion applies. The exponent 1000/479 is about 2.0877, not a known forbidden approximation exponent for this logarithm. QED.

This argument counts physical odd states, not only odd-run entries. It uses the complete actual strip, then the unique ternary residue of a past word. A stronger upper count at bounded height cannot by itself prohibit a trajectory from leaving that height range.

## 3. A depth-192 comparison theorem on mechanical inverse words

We now examine a possible universal repair of the remaining bounded-cycle branch: look at every short inverse path from each cycle state to a smaller positive multiple of three. The theorem below gives a rigorous obstruction to that strategy with a fixed depth 192.

In this section also allow positive odd rationals of denominator coprime to six, with parities and ternary residues interpreted in Z_2 and Z_3. Legal inverse states must have the same domain and be positive. This is an explicitly relaxed domain, not a counterexample in ordinary positive integers.

A mechanical exponent word of slope a/p in (1,2) has entries floor((i+1)a/p+t)-floor(ia/p+t), where t is an intercept; ceiling words are included by taking the appropriate one-sided phase. Use the open interval

    J=(84/53,485/306), containing log2(3).

The endpoints have determinant one and denominators summing to 359. Hence no reduced rational with denominator <=193 lies strictly between them (Farey neighbor lemma). It follows that the length-193 mechanical factor language is constant throughout J: the circular order of the breakpoints -j r mod 1, 0<=j<=193, can change only at such a rational slope. On each interval between breakpoints the floor-word is constant in the intercept. At a breakpoint its word is the right-sided one. This also covers the ceiling words by the opposite one-sided interval. The representative slope 569/359 is the mediant, so enumerating its 359 intercept residues gives the full language. The exact count is 194 words. Every subword of these factors satisfies 2^(sum e)/3^(length)<=3, by the exact finite check.

**Theorem I192.** Suppose an odd positive ordinary or rational reference path starts at y, consists of legal inverse gaps e_i in {1,2}, and has its first K+1 gaps in this language, K=192. All reference states are ternary units. Suppose furthermore that its reference values, through the first K steps, are at least s>0. Every legal alternative inverse word from the same y of length at most K whose last state is a multiple of three has last state at least 2s+1.

Proof. At equal inverse depth i, write x_i for the reference, z_i for an alternative, d_i=alternative total division minus reference total division. Until the first negative d_i, put z_i=2^d_i x_i+c_i. Direct affine subtraction gives

    d'=d+f-e,
    3c'=2^d' + 2^f c -1.

Here c_i is integral: the formula expresses it with denominator a power of three, and both paths lie in Z_3. When d_i>=0 it is nonnegative by induction. When d_i>0 it is positive and odd, while when d_i=0 it is even. On the reference word,

    c_i/2^d_i = sum_(j=1)^i [(1-2^(-d_j))/3] prod_(l=j+1)^i (2^e_l/3) <= i.

The subword product bound is essential; it makes the search for a zero-grade crossing finite regardless of alternative exponent sizes.

A first negative d can only follow d=0 with reference e=2 and alternative f=1, since e<=2 and f>=1. The reference previous residue is then 1 modulo 3 and the alternative previous residue 2, forcing c=1 mod 3. This is the active crossing. If d=0 and the alternative terminates at a multiple of three, reference previous-to-next-inverse residue r is 1 for next gap 2, 2 for next gap 1, and c=-r mod 3. This is the terminal crossing. In either case c is a positive even integer <=i, since c=0 would make the two current states identical units. Include the next gap in the word to test both conditions.

The finite search in controls.py overapproximates every possible nonnegative-grade past reaching such a candidate (d,c)=(0,c). In reverse at a step with reference gap e, it tries all f in [1,d+e], determines d_prev=d+e-f>=0, and tests

    c_prev=(3c-2^d+1)/2^f

for nonnegative integrality, parity, and the necessary inverse congruence on the alternative previous value. It also retains the necessary prefix bound c_prev<=2^d_prev times prefix length. The search stops successfully at (0,0), since an identical initial path is then possible; ignoring other consistency conditions can only enlarge the search. Its recursion decreases the word length. The program found no possible active or terminal crossing in 638,863 tests across 18,912 prefixes with the next gap. Therefore d never becomes negative, and a terminal multiple of three cannot have d=0. Thus at its endpoint d>=1 and c>=1; z=2^d x+c>=2s+1. QED.

This argument is different from assuming every inverse competitor has strictly larger division total: equal-grade nonzero offsets can occur. Only the two congruences that could defeat the minimum-multiple comparison are forbidden. It is a finite certificate at depth 192, not a claim of all-depth rigidity.

## 4. Unbounded rational controls with the complete denominator retained

**Theorem R.** There are positive nonordinary rational cycles with arbitrarily large minimum s, all odd gaps in {1,2}, all odd states in [s,2s), s=1 mod 9, and q=(2s+1)/3=1 mod 12 (residues in the appropriate local rings). The rational multiple n=2s+1=3q merges with the cycle. No odd inverse path of length at most 192 from any of its odd phases can reach a positive 3-divisible state strictly smaller than n. Every phase has full reduced denominator 2^A-3^p, where A,p are its physical and odd periods.

Proof. Let A/p be a reduced upper convergent of alpha=log2(3), sufficiently close to alpha to be in J and (3/2,2); let p tend to infinity. The inverse mechanical word

    e_i=ceil(i A/p)-ceil((i-1)A/p), i=1,...,p

has total A and gaps in {1,2}. Compose its inverse affine maps to obtain (2^A x-C)/3^p, with C_0=0 and C_{i+1}=2^e_(i+1) C_i+3^i. Its fixed point is s=C/(2^A-3^p)>0. At each rotated word the analogous positive carry gives a fixed point; the formulas identify them as consecutive inverse phases. The denominator D=2^A-3^p is odd and prime to three; every carry is odd and prime to three. Hence all rational phases are positive odd units, and the literal inverse equations also give exact legal forward gaps. The primitive odd period is p, because a shorter period would make the gap word a repetition, contrary to gcd(A,p)=1.

The final carry is the sum, over suffix lengths j=0,...,p-1, of 3^(p-1-j) times 2^(suffix division total). For the displayed upper word, these totals are floor(j A/p), minimal among all rotations. For any fixed j the totals of two rotations differ by at most one (balanced word). Thus this phase is a minimum, and every phase carry is strictly less than twice its carry (the j=0 term is the same positive term in all rotations). Also

    C/3^p >= p/6,
    s >= p/[6(2^(A-p alpha)-1)].

Indeed each suffix multiplier 2^floor(j A/p)/3^j>=1/2 since A/p>alpha. Upper convergents give A-p alpha>0 tending to zero, proving arbitrarily large s. The first two inverse gaps at this minimum are both 2, so (16s-7)/9 is ternary-integral and s=1 mod 9. The next forward gap at the minimum must be 1 when s>1, because a gap 2 strictly decreases any value greater than 1. Hence s=3 mod 4 and q=1 mod 12. Every maximal odd run of the shortcut path is followed by exactly one even step (since the gaps are 1 or 2); in fact consecutive gap-1 entries are excluded by the mechanical length-two sum >=3. The odd-run entries are therefore well inside the strip of E.

Write s+1=2^m a_0 with a_0 odd in Z_2. Its maximal odd run ends at R_0-1, R_0=3^m a_0=3 mod4, then halves once. The source n=2s+1 has one additional initial odd step, its odd run ending at 3R_0-1. Two further halvings give (3R_0-1)/4, the same point reached by s after its own singleton exit and one odd shortcut. Thus n genuinely merges with s. Since every inverse factor of the cycle belongs to the depth-193 language, I192 gives the required lower bound on all tested 3-divisible ancestors. Notice that n itself is a 3-divisible predecessor; its clock need not equal the clocks of other candidates.

Finally, full denominator rigidity is elementary. The words

    e_i(t)=floor((i A+t)/p)-floor(((i-1) A+t)/p), t=0,...,p-1,

are all cyclic rotations because gcd(A,p)=1. Put S_j(t)=floor((j A+t)/p). The carry is C_t=sum_(j=1)^p 3^(j-1) 2^(A-S_j(t)). For t<p-1, incrementing t by one changes exactly one internal S_j by one (the index j A+t=-1 mod p). Therefore the difference of these two carries is a signed pure product of powers of 2 and 3. The inverse recurrence 3 C_next=2^e C_current-D shows gcd(D,C_t) is identical over rotations. It divides that smooth difference, and D is prime to six. Hence gcd(D,C_t)=1 for every t. For A>=3, D>1, since 3^p+1 is nonzero modulo 8. This proves that the entire denominator remains, not merely a proper factor. No external mechanical-cycle theorem is required for this algebra. It is consistent with the classical mechanical-word cycle exclusions and the repository's earlier full-denominator and rotation arguments; no priority claim. QED.

## 5. Why the attempted complete proof stops

The natural ordinary proof would combine M and E with (i) exclusion of the growing branch by a smaller positive multiple of three in the same fixed component, and (ii) exclusion of all ordinary cycles in the bounded branch. The exact finite inverse theorem above shows that treating short predecessor searches as a universal way to exclude the bounded branch is not justified: even arbitrarily large, tightly confined, locally admissible rational cycles can pass the depth-192 arithmetic screen. They are separated here by full denominator divisibility, not by that screen. The controls do NOT claim that rational q converges or that all smaller rational multiples converge, and they do not satisfy the ordinary hypothesis M. They diagnose a relaxation of the arithmetic tests, not a counterexample to M or Collatz.

The mechanical denominator theorem eliminates one complete subclass but does not force the actual bounded branch to be mechanical. The improved strip count still leaves arbitrary large periods and genuinely nonmechanical words. The growing alternative remains entirely open. A proposed final Lean theorem must keep these two obligations as explicit premises, not replace them with inverse-law typicality. The candidate module MinimumClosure.lean formalizes only the finite algebra and the logical consumer of a genuine universal descent premise; no full Lean proof or compilation is claimed.
