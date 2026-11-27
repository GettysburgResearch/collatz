# The saved 19 clocks do not pay for arbitrary ternary classes

**PROPOSED written theorem.** For every positive ordinary endpoint $X$ and integer clock budget $H\ge0$, the number of positive sources $Y$ with $T^hY=X$ at some $0\le h\le H$ is at most
$$
                        C(25/16)^H
$$
with an absolute constant $C$. Thus the clock $19N$ from the earlier PR192 chain reaches at most an exponentially vanishing fraction of **all** residue classes modulo $3^{8N+3}$, uniformly in $X$ and without any restriction on the visitor's odd count. For the specified rational target class there is also an individual necessary bound on that count.

The late PR192 checkpoint enters *any one prescribed ternary class* from a fixed positive ternary-unit endpoint with subexponential clock allowance. Its earlier chain saves $19N$ clocks and $8N$ odd steps, while its terminal condition has precision $L=8N+3$. The theorem above shows that its saved clock cannot fund a replacement that reaches **every** ternary class at that precision, even on a single arm. It leaves open the specific nested terminal class that the paired argument requests. [PR192 checkpoint, inverse-entry theorem and §5](https://github.com/GettysburgResearch/collatz/blob/1cb3e8496a6bd6092d3d0dc1dd043c3bcd662aca/research/astra-unconventional-20261126/descent/README.md) · [paired return and its different necessary count](https://github.com/GettysburgResearch/collatz/blob/1cb3e8496a6bd6092d3d0dc1dd043c3bcd662aca/research/astra-unconventional-20261126/descent/PAIRED.md) · [original chain and fixed rational terminal](https://github.com/GettysburgResearch/collatz/blob/1cb3e8496a6bd6092d3d0dc1dd043c3bcd662aca/research/astra-literature-closure-20261125/carry/README.md)

## A uniform count of all inverse words

Reverse a physical path, grouping each inverse odd with its preceding doublings. From the current $x$, the stage of length $e\ge1$ yields $(2^e x-1)/3$. If there will be another odd stage afterwards, this new input must be a ternary unit: once a multiple of three has been reached in reverse, no amount of doubling permits another odd inverse. For a unit $x$, the powers of two run through all units modulo nine with period six. The two nonfinal possibilities satisfy $2^e x=4$ or $7\bmod9$. Their exponents occupy two of the three positive residue classes of one parity modulo six.

Give a clock of length $h$ the weight $t^h$, where $t=16/25$. The total weights of **nonfinal** odd stages from any positive input are bounded by
$$
      F=\frac{t+t^3}{1-t^6}=\frac{220250000}{227363409}<1 .
$$
Indeed the two earliest distinct positive exponents of the same parity are at least one and three. At the **last** odd inverse the child may be divisible by three, so just the forced parity gives the bound $G=t/(1-t^2)$. Both bounds hold for nonunit initial inputs as well, since then neither kind of odd stage exists. Final pure doublings of arbitrary length multiply the total weight by $1/(1-t)$. Induction bounds the weight of all paths with exactly $p\ge1$ odd departures by $F^{p-1}G/(1-t)$, even though each next stage depends on its current state. Include the all-even paths and sum the geometric series:
$$
  \sum_{\text{all reverse words into }X}t^{h}
      \le C=\frac{1+G/(1-F)}{1-t}
      =\frac{6339445225}{64020681}.
$$
Every word of clock at most $H$ contributes at least $t^H$. This proves the uniform bound, including repeated visits to an endpoint or multiple words from one source. Since $25^{19}<3^8 16^{19}$ by direct integer comparison, at clock $19N+O(1)$ even the total number of words divided by $3^{8N+3}$ decays exponentially. The conclusion holds for all target residues taken together.

## Height limits the number of odd inverses

In this section fix $X$ independently of $L$ and take $H_L\le19L/8+O(1)$, with a fixed constant in the clock allowance.

Take an upper-half residue with standard representative at least $3^L/2$, so $Y\ge3^L/2$. Write $p$ for the number of odd departures on the physical trajectory. At every shortcut, $2T(n)\ge3^{n\bmod2}n$. Multiplying gives
$$
       3^pY\le2^h X\le2^{H_L}X,\qquad
       p\le H_L/\log_2 3-L+\log_3(2X).
$$
The inequality is strict at the first comparison if $p>0$. Since $2^{19}<3^{12}$, the resulting upper bound on $p$ is at most $L/2+O_X(1)$. This bound comes from the height of the actual required representative and applies without any independent restriction on the odd count.

## The parity of every reverse gap is forced

Reverse a path from $X$. Write each of its $p$ odd inverse stages as $e_i-1$ doublings followed by the odd inverse, with $e_i\ge1$. At the current positive integer $x$, the new state is $(2^{e_i}x-1)/3$. If $3\mid x$ there is no legal odd inverse even after more doublings. Otherwise exactly one parity of $e_i$ can work: its least positive representative is $b_i=2$ if $x=1\bmod3$ and $b_i=1$ if $x=2\bmod3$. Write $e_i=b_i+2k_i$. From fixed $X$ the successive $k_i\ge0$ determine the stages uniquely, by recomputing $b_i$ at the current state. This count may include words that stop being legal. It allows a final odd inverse landing on a multiple of three. After the last odd inverse allow a padding of $d\ge0$ further doublings, corresponding to even inputs at the beginning of the forward path. For $p=0$ only this padding remains.

The clock inequality $d+\sum_i e_i\le H_L$ implies $\sum_i k_i\le\lfloor(H_L-p)/2\rfloor$. For fixed $p$ the number of possible gap vectors is therefore at most
$$
    {\lfloor(H_L+p)/2\rfloor\choose p}
           \le 2^{(H_L+p)/2}.
$$
There are at most $H_L+1$ choices each for $p$ and $d$, including the all-even word. Every physical source representing an upper-half residue occurs among these choices. Substituting $p\le L/2+O_X(1)$ and $H_L\le19L/8+O(1)$ proves the count. As $2^{23}<3^{16}$, the count is $o(3^L)$. Distinct words may give the same source or the same residue; this only strengthens the upper bound.

## The designated class

The earlier terminal condition for the ordinary lower entry is $517727Y\equiv203816\pmod{3^L}$. For any positive such $Y$, the integer $517727Y-203816$ is positive, so $Y\ge(3^L+203816)/517727$. Thus the *individual* height constraint $p\le H_L/\log_2 3-L+O_X(1)$ also holds for this specified class, with its fixed denominator absorbed in the constant. The counting argument provides no lower bound on its distance from the representable residues. A return to this one class, transporting the required second label and fitting the saved clocks, remains open.

## The specified target over ordinary endpoints

Now fix the PR192 target itself and vary the positive ordinary endpoint $X$. Write $D=517727$, $C_0=203816$. For each forward parity word of length $h$ and with $p$ odd departures there is an integer $b$ determined by the word such that $2^hX=3^pY+b$. To reach this $X$ from a positive $Y$ obeying $DY=C_0\bmod3^L$, the word requires
$$
                D2^hX=3^p C_0+D b\pmod{3^{L+p}}.
$$
Since $3\nmid D2^h$, this specifies exactly one *possible* class of endpoints modulo $3^{L+p}$. Counting that entire class is an upper bound, including when some representatives have no legal positive word. Sum over the $\binom hp$ possible bit strings. At $L=8N+3$ the upper natural density of ordinary endpoints that allow any such portal by clock $19N$ is at most
$$
       3^{-8N-3}\sum_{h=0}^{19N}(4/3)^h .
$$
The sum of these bounds over $N\ge1$ is strictly less than
$$
   \delta=\frac4{27}\frac{R}{1-R}
      =\frac{1099511627776}{198469428607161}<0.00554,
       \qquad R=\frac{4^{19}}{3^{27}} .
$$

There is a simultaneous ordinary statement over a growing range of depths. For $1\le X\le B$, each congruence above contains at most $B/3^{L+p}+1$ endpoints. Set $J(B)=\lfloor(\log_2 B-3\log_2\log_2 B)/19\rfloor$ for sufficiently large $B$. The sum of the rounding errors over all depths $1\le N\le J(B)$ and all their words is $O(\sum_{N\le J(B)}2^{19N})=O(B/(\log B)^3)$. Thus at least $(1-\delta-o(1))B$ ordinary endpoints have **no** visitor from this one designated rational class at any of the paid depths $1\le N\le J(B)$. For fixed $B$ this tests only its indicated range of $N$. A particular supplied ordinary endpoint could still admit a larger-depth paid entrance.
