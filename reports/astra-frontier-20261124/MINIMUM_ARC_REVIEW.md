# Independent review of the first crossing from a cycle minimum

**VERIFIED, written with the identified numerical certificate.** For a positive ordinary shortcut source $x\ge2^{71}$, assume a first coefficient crossing exists and its endpoint is at least $x$. That one contiguous word has at least **72,057,431,991 odd inputs** and **114,208,327,604 shortcut steps**. Both hypotheses hold at the minimum of a finite positive cycle. The application to every nontrivial positive cycle uses Barina's published verification for starts below $2^{71}$ as an external computational input.

| Frozen item | Git blob | SHA-256 |
|---|---|---|
| `MINIMUM_ARC.md` | `4a8aa3b7ea3162dd6b64501f7b0231df475bd413` | `431ba55291001e00bdfd134cabff346afdf2dfb1e7479a3160fe327970514329` |
| `MinimumCrossing.lean` | `95736a3ba6c3ffcb13f86cb10b0666668b26c01d` | `36a5de08da5ff9153008b4ac9ab4d17a08cb18de02c7b72d89b9fcd27cbab6be` |
| `check_farey_gate.py` | `839ee5d890526274c88028f01a5054050d1e5aaa` | `6e9f87d499a94ec223d70bd239b78325bd4944f93883a97dd84b1361fb1c0430` |
| `minimum-lean.log` | `7f0353e991380d5a671fd01d156920be8f856d40` | `1a1d18df161ad5d96b715ce5e96e6d08e6ace1be7b572756e4768d1c700217f1` |
| `farey-gate.log` | `effe16e848cdff321a19b678474e6572427e61a4` | `c44b946de4dc90117780142df39f7c130efe9b50ee1f558448cd20b882d6ffff` |

**Written reduction.** The actual affine equation, endpoint non-descent and proper-prefix carry bound give $0<(2^A-3^p)x\le C_w\le p3^p/3$, hence $p>0$. Applying $\log z<z-1$ to $z=2^A/3^p$ and dividing by $p\log 2$ gives the strict interval in the source. A full lap at a positive cycle has some odd input and a positive carry, so the full coefficient strictly contracts. Starting at the minimum therefore gives a first crossing within a lap and a nondescending endpoint. The same pointwise argument and the earlier local finite census also establish the smaller 47,468-odd bound on an arc starting precisely at that minimum.

**Independent numerical certificate.** I reran the published Python check, then evaluated the 90 odd terms of each logarithm independently by backward Horner summation in exact rational arithmetic. With $z=(v-1)/(v+1)$, I used the looser positive remainder bound $2z^{181}/(1-z^2)$, valid by summing a geometric series. Denote the resulting bounds for $\log j$ by $\ell_j,u_j$. For the source's integers $a,b,c,d$, the exact integer

$$
\left\lfloor 10^{15}(b\ell_3-a u_2)\right\rfloor=4612
$$

certifies the strict lower endpoint, and

$$
\left\lfloor 10^{15}\left(c\ell_2-d u_3-\frac{d}{3\cdot2^{71}}\right)\right\rfloor=9193
$$

certifies the strict upper endpoint. I obtained $bc-ad=1$. Thus the two integer gaps $bA-ap$ and $cp-dA$ are at least one. Multiplying them by $(c,d)$ and $(a,b)$ respectively and adding reconstructs $(A,p)$. This yields the displayed numerator and denominator sums for fractions of any reduction status.

**Formal coverage.** I inspected the four declarations and the final axiom receipt. The imported `CyclePacking.lean` has blob `1623eca9961e595179875f3d1da39f8ef0031669`. The new declarations prove the affine inequality, its integer floor version, the strict real-log inequality on the actual nondescending trajectory, and the two Farey coordinate bounds. The receipt reports only `propext`, `Classical.choice` and `Quot.sound`. I independently replayed the rational certificate. The all-starts baseline at $2^{71}$ remains an external computation, and a universal upper bound on these first-crossing sizes remains open.
