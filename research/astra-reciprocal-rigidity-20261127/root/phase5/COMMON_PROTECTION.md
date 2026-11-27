# A common ternary protection set exceeding one third

**Written uniform counting theorem.** For each \(K\ge1\) there is a computable set \(F_K\subseteq\mathbb Z/3^K\mathbb Z\) such that
\[
 \frac{|F_K|}{3^K}\ \ge\ \frac{284051}{829440}>\frac13,\qquad
 \frac{|\{r\in F_K:r=0\bmod3\}|}{3^K}
       \ \ge\ \frac{1041139}{4147200}>\frac14 .
\]
Both denominators are the size of the *whole* ternary space. Suppose \(n>0\), \(n\bmod3^K\in F_K\), and \(2n\ge K(1+3^K)\). For every \(j,\delta\ge0\) and every positive integer \(Y\) satisfying
\[
                       2^j(Y+1)=3^j2^\delta(n+1),
\]
every positive \(m<n\) visiting \(Y\) at any ordinary shortcut clock spends more than \(j+K\) odd departures. The same \(F_K\) works for every scale and ramp length. With \(n=2^H v-1,\ v>0\), take any native postpeak word \(w\) from \(3^Hv-1\), with \(f\) odd and \(q\) even departures. If \(w\) is maximal in weight among equally long words with its signed offset and \(H\ge6q+3K+3\), then every positive smaller visitor to its endpoint spends more than \(H+f+K\) odds.

Weaver's Paper 178/v1 already develops the stopped squared-gain argument and signed origins on a pure ramp and obtains a stronger protection proportion above \(0.510269713938\) there. PR201's earlier simultaneous event covers shifted sites over deep \(3\)-divisibility cylinders. The preceding checkpoint gave the exact arbitrary-scale selector, its pointwise cutoff and a simultaneous \(259/960\) bound of the kind studied here. The present calculation improves the common coarse-modulus proportions across *all* additional binary scales using the odd signed origins through seven even inverses, first-odd parity, and two strict first-crossing corrections. It does not improve Weaver's pure-ramp proportion. [Weaver 178/v1 §§2,7](https://rstation.ai/problems/collatz/papers/178/v1) · [Prior simultaneous result and PR201 provenance](../../descent/postpeak/SCALED_DENSITY.md) · [Kernel-checked selector and sharp cutoff](../../descent/postpeak/SELECTOR.md) · [Signed-origin finite closure](SignedOrigins.lean)

## From a smaller ordinary source to a stopped cylinder

Use \(T(2x)=x,\ T(2x+1)=3x+2\). By the cited selector, at the stated height any counterexample supplies a signed origin
\[
                  z=2^{\ell+\delta}(n+1)-M
\]
and a reverse word \(w\) with \(1\le b\le K\) odd inverses in \(d\) letters. The extraction cuts immediately before the last \(j\) odd departures of the lower path. Thus \(M\) is odd, \(1\le M\le2^\ell\), and the reflected native map \(S(2x)=x,\ S(2x+1)=3x+1\) takes \(M\) to 1 with exactly \(\ell\) even departures. For \(j=0\) use the empty suffix \(\ell=0,M=1\). The stopped word is the first reverse prefix with
\[
                       D=2^{a+d}/3^b<1,\qquad a=\ell+\delta .
\]
It preserves an actual positive smaller source on the same path. A fixed word selects at most one ternary cylinder modulo \(3^b\), with full-space mass \(3^{-b}\). Overlaps among words or parameters can only reduce the measure of their union. The selector is finite at precision \(K\), since \(a+d<K\log_2 3\).

For a fixed \(a\), give a reverse even letter probability \(1/4\) and a reverse odd letter \(3/4\). The full family of formal words stopped at their first strict crossing is prefix-free. For one word \(p(w)=3^b4^{-d}\) and
\[
                        3^{-b}=4^{-a}p(w)D^2\le4^{-a}p(w).
\]
Words forbidden by native integrality may be retained in this majorant. If \(z=0\bmod3\), inverse evens preserve zero and no inverse odd is possible. If \(z=1\bmod3\), an odd number of inverse evens precedes the first odd. The total probability of this event is \((3/4)\sum_{r\ge0}4^{-(2r+1)}=1/5\). If \(z=2\bmod3\), the number is even, with total probability \(4/5\). Every crossing has a first odd.

## The two residue counts

For \(n=0\bmod3\), \(z=2^{\ell+\delta}-M\bmod3\). Define \(s(0)=0,\ s(1)=1/5,\ s(2)=4/5\). The cost for fixed \(\ell,M\) over all \(\delta\) is bounded by
\[
  4^{-\ell}\left[\frac{16}{15}s(2^\ell-M\bmod3)
               +\frac4{15}s(-2^\ell-M\bmod3)\right],
\]
where the coefficients sum \(4^{-\delta}\) over even and odd scales. For \(n\in\{0,1\}\bmod3\), the two possible \(z\)'s form \(\{1,2\},\{0,1\},\{0,2\}\) according to \(M\bmod3=0,1,2\), independently of \(\delta\). Their combined first-odd event has probability \(\gamma(0)=1,\gamma(1)=1/5,\gamma(2)=4/5\). The joint cost is thus \((4/3)4^{-\ell}\gamma(M\bmod3)\). These are whole-space cylinder bounds. An extra factor \(1/3\) for a chosen source class would count the same restriction twice.

The exact odd signed origins and their two resulting costs are as follows.

| \(\ell\) | Odd \(M\) | Cost inside the zero class | Cost inside the union of zero and one |
|---:|---:|---:|---:|
| 0 | 1 | \(4/75\) | \(4/15\) |
| 1 | none | \(0\) | \(0\) |
| 2 | 3 | \(2/75\) | \(1/12\) |
| 3 | none | \(0\) | \(0\) |
| 4 | 11 | \(1/300\) | \(1/240\) |
| 5 | 15 | \(17/19200\) | \(1/768\) |
| 6 | 29, 43 | \(1/4800+1/76800\) | \(1/3840+1/15360\) |
| 7 | 39, 59 | \(17/307200+1/76800\) | \(1/12288+1/15360\) |

For \(\ell\ge8\) use all \(2^{\ell-1}\) odd magnitudes up to \(2^\ell\). In either column the total tail is at most \((4/3)\sum_{\ell\ge8}2^{\ell-1}4^{-\ell}=1/192\). Subtracting the rows and tail from \(1/3\) in the zero class and \(2/3\) in the joint class leaves \(74839/307200\) and \(6257/20480\), respectively.

## Two strict first crossings

At \(\ell=0,\delta=1,M=1\), the reverse word \(EOOOO\) has \(a=1,d=5,b=4,D=64/81\). The previous coefficient is \(32/27>1\), and all still earlier coefficients are at least one. The word satisfies the allowed first-odd parity in both counts. Its formal subtree budget is \(4^{-1}(1/4)(3/4)^4=81/4096\), but its actual stopped cylinder costs at most \(1/81\). Subtract \(2465/331776\) from the cost in each column.

At \(\ell=\delta=0,M=1\), the reverse word \(EOO\) has \(D=8/9\) after \(4/3>1\), with all preceding coefficients at least one. It is allowed in the joint count, on the residue \(n=1\bmod3\). Its probability budget \(9/64\) exceeds its exact cylinder cap \(1/9\) by \(17/576\). This is a different scale row, so the two budget corrections add in the joint count without any claim that their actual ternary cylinders are disjoint.

These subtractions apply also when \(K<4\) or \(K<2\). Start with the *full* formal first-crossing tree, with no grade cap, for each specified \(a\) and first-odd event. The probability of all other stopped words is at most the event probability minus the weight of the displayed stopped word. If its grade exceeds \(K\), it contributes no actual cylinder to the precision-\(K\) union; the stated positive exact upper bound for that cylinder remains valid. Adding the two corrections to the previous protections gives the fractions in the theorem.

The maximal-word consumer uses the sharp cone to exclude cheaper grades and transport any paid peak collision with at most \(K\) extra odds to an actual earlier pure visit at an allowed binary scale. The common ternary protection then excludes this visit. The argument leaves visitors at higher cost and later ordinary descent open.
