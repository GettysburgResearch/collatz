# All-depth positive inverse pressure and first-hit source certificates

**PROPOSED; self-audited, not independently reviewed or formally verified.**
This extends the fixed-depth positive-source argument in PR #142, DSP-005.
Its new scope is the entire inverse history, all depths at once, with genuine
positive-cycle repetitions retained. It is not a full Collatz proof.

For a positive odd integer t, an odd inverse history is a finite positive odd
trajectory x=n_0,...,n_q=t under U(n)=(3n+1)/2^a(n). Write

    A=sum_(j<q) a(n_j),  J=3^q/2^A.

The depth-zero history x=t has J=1. At each fixed q distinct legal histories
have distinct sources, since forward dynamics is deterministic. A source can
occur at several depths only when the target is periodic. Define

    Z_(q,s)(t)=sum_(legal depth-q histories) J^s,
    G_s(t)=sum_(q>=0) Z_(q,s)(t),       s>1.             (1)

All sums are of nonnegative terms; rearrangements below use monotone
convergence. No stochastic law is assumed for an actual forward orbit.

## P1. A first-hit bound across every depth

If x eventually reaches t, take its unique first-hit history, with derivative
J_0(x,t). Its exact affine identity is

    t=J_0(x,t) x+beta, beta>=0,

where beta>0 unless x=t and the first-hit clock is zero. Consequently

    0<J_0(x,t)<=t/x.                                  (2)

This elementary inequality is what lets us combine different depths without
multiplying a source-count bound by the number of depths. First hits are
indexed by distinct positive odd integers, not by arbitrary symbolic words.
In decreasing order their weights obey J_(j)<=t/(2j-1); equivalently they form
a weak-l^1 family. For every s>1,

    H_s(t):=sum_(x first hits t) J_0(x,t)^s
         <= t^s sum_(x positive odd) x^(-s)
         = t^s(1-2^(-s)) zeta(s).                     (3)

This neither assumes nor proves that every x hits the chosen target.

## P2. Exact handling of all returns, including unknown positive cycles

If t is not periodic, each source hits it at most once and G_s(t)=H_s(t).
If t lies on a positive cycle of minimal odd period p, let B be the total
valuation around that cycle and lambda=3^p/2^B. Positivity of the affine
constant gives lambda<1. More explicitly, multiplying the real step ratios
around the cycle gives

    lambda=product_(n on the cycle) [3n/(3n+1)]
          <=3t/(3t+1)<1.                             (4)

Every history reaching t is its source's first hit followed by k complete
cycles, k>=0. Its derivative is exactly J_0 lambda^k. Thus

    G_s(t)=H_s(t)/(1-lambda^s)                        (5)

in the periodic case. In either case we have the unconditional bound

    G_s(t) <= t^s(1-2^(-s))zeta(s)
                /[1-(3t/(3t+1))^s] < infinity.       (6)

This quantifies over **every fixed positive odd t**, not just targets already
known to converge, and covers hypothetical nontrivial cycles as well as the
known fixed point 1. In particular Z_(q,s)(t)->0 as q->infinity.

For s=2 an entirely rational bound is available. For j>=1,
1/(2j+1)^2 < 1/[4j(j+1)], so sum_(odd x) x^-2 < 5/4. Hence

    G_2(t) < 5 t^2 (3t+1)^2 / [4(6t+1)].             (7)

For the known odd cycle t=1, lambda=3/4 and its exact repetition factor is
16/7. The simple bound is G_2(1)<20/7, not H_2(1)<20/7 with loops forgotten.
If 3 divides t, U never lands on t, so G_s(t)=1 exactly.

**Adversarial control.** The same positivity/first-hit argument works for the
odd map (p n+1)/2^v2(p n+1) with any odd p>=3, replacing 3 by p. For p=5 the
actual positive cycle 13 -> 33 -> 83 -> 13 has total valuation 7 and derivative
125/128, and satisfies the same summability conclusion. Therefore P2 cannot
by itself establish that 1 is the only positive Collatz cycle, nor can it
exclude a divergent 3x+1 orbit. At the negative fixed point -1, the repeated
3x+1 branch has J=(3/2)^q and the pressure instead diverges. Positivity is
essential, but is not the only missing global ingredient.

## P3. Finite-source certificates for an infinite-depth quantity

Fix an odd source cutoff X. Suppose every odd x<=X has been classified as to
whether it first hits t, with the derivative of each positive hit supplied.
Let M_s(t;X) be the exact sum of those first-hit weights to the power s.
For s=2 the unenumerated source tail obeys

    0 <= H_2(t)-M_2(t;X) < t^2/[2(X+1)].              (8)

Indeed 1/x^2 < (1/2)(1/(x-1)-1/(x+1)) for x>1; summing over the odd tail
telescopes. The source cutoff, not a trajectory-depth cutoff, controls this
error. Multiply (8) by the exact factor from (5) when t is known periodic;
use factor one when t is known nonperiodic. For unclassified sources, their
possible contributions must remain in the upper error, not be called absent.

The checker classifies every odd source x<=65535 by a literal finite path to
1, retaining all first visits to targets 1,3,5,7,13,27,41,127. A second
implementation follows raw shortcut steps, reconstructing both clocks and
first-hit records. Target 1 uses factor 16/7. The other listed targets have
verified paths to 1 and are not periodic. This yields, for example, the strict
rationally certified decimal enclosure

    2.685114973562 < G_2(1) < 2.685132412180.          (9)

The complete rational endpoints, rather than just rounded values, are in the
frozen JSON. Equation (9) concerns infinitely many possible positive sources
and every inverse depth, not only the enumerated finite tree. Its rigorous
infinite tail is the proved inequality (8). This does not make the computation
a proof of Collatz: sources beyond the cutoff need not converge for (8) to hold.

## P4. A simple-pole upper bound for the original critical resolvent

The original reference density in PR #142 is rho_q(t)=Z_(q,1)(t), with rho_0=1.
Set eta=64/81. If t is nonperiodic put c_t=1; if periodic put
c_t=1/(1-lambda). Always c_t<=3t+1. For every integer Q>=1,

    sum_(q=0)^Q rho_q(t)
      <= c_t t [1+(1/2)ln(t)+3Q ln(2)] +(9/8) eta^Q. (10)

**Proof.** Split histories of depths q<=Q according as A<=6Q or A>6Q. In the
first part their positive sources obey x<t 2^(6Q) by (2)'s affine argument;
including depth zero causes no problem. Group all visits from each source and
sum their geometric cycle factor when necessary. Their total weight is at
most c_t t/x. The positive odd harmonic sum through a bound Y>=1 is at most
1+(1/2)ln Y, giving the first term.

For the second part discard integrality and endpoint restrictions. If the
independent reference valuations have probability 2^-a, their sum S_q has
E[(3/2)^S_q]=3^q. The unrestricted tail weight at depth q is at most
9^q (2/3)^(6Q). Summing q=1,...,Q bounds it by
(9/8)(64/81)^Q. This is a reference-word calculation, not an independence
assumption on a fixed trajectory.

Let F_t(z)=sum_(q>=0) z^q rho_q(t), 0<=z<1. Summation by parts in (10), using
the harmless same upper bound at Q=0, gives

    F_t(z) <= c_t t[1+(1/2)ln t]
              +3c_t t ln(2) z/(1-z)
              +(9/8)(1-z)/(1-eta z).                 (11)

Thus F_t(z)=O_t((1-z)^-1), improving the O_t((1-z)^-2) consequence of the
fixed-depth bound in #142. This is a **simple-pole upper growth bound**, not a
claim that F_t has an actual pole, a nonzero residue, a finite value at z=1,
a uniform-in-t bound, or bounded individual rho_q(t). The endpoint factor is
worse than the old fixed-depth estimate; the improvement is in depth summation.

## P5. A tilted ternary law realizes the square pressure exactly

Let independent exponents have probability (b-1)b^-a, a>=1. For b=2 this is
the original reference law; for b=4 it is the square tilt. Let nu_(q,b) be the
law modulo 3^q of the iterated affine maps y -> (3y+1)/2^a, equivalently of

    Y_q=sum_(j=1)^q 3^(j-1) 2^(-(a_1+...+a_j)) mod3^q.

Independence makes the reversal of the q labels immaterial. For each word,
its mass is (b-1)^q b^-A. At a positive odd target, a nonempty residue fiber
corresponds to a unique integral positive odd inverse history, with its exact
valuation labels. Integrality at all levels follows by successive reduction;
positivity follows because (2^a t-1)/3>0 whenever it is an integer and t>0.
Therefore

    3^q nu_(q,2)(t) = Z_(q,1)(t),
    3^q nu_(q,4)(t) = Z_(q,2)(t).                    (12)

Combining (6) with (12) proves that the square-tilted point densities are
summable in depth at **every fixed positive odd integer**. They need not be
monotone in depth. Negative fixed points still have exponential lower spikes.
The exact full residue laws through depth 9 are computed in [EXACT_DENSITY.md](EXACT_DENSITY.md).

## What remains unsupported

Neither G_s(t)'s pointwise finiteness nor (11) supplies a bound uniform along a
moving endpoint t=U^j(n). No theorem here converts inverse square pressure into
the forward fixed-source collision upper bound E5 of the parent packet.
Cauchy--Schwarz with an uncontrolled number of predecessors cannot do that.
The p=5 cycle control shows why positivity plus injectivity alone cannot be
the final argument. The unresolved task is a genuinely 3x+1-specific transport
or complexity theorem, not another claim that finite inverse histories exist.
