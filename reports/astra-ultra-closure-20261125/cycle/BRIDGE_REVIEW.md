# Independent review of paired returns and the tower threshold

**VERIFIED for the finite arithmetic, actual transport, rank-one equivalence and conditional tower contradiction. Universal termination remains OPEN.** The scope is the ordinary shortcut map. An odd count includes each odd departure and excludes the final endpoint.

## Independent reconstruction

1. For a common good reference, the first $h$ steps above $a$ multiply a displacement $2^h u$ by $3^{\mathrm{odds}(h,a)}/2^h$. The two lift displacements are in the ratio $4^d:3^d$. Repeating the two physical clocks above 1 consumes that ratio with $d$ extra odd inputs. The proof separately uses the hitting clock of $3a$ and the additional factor of three in its displacement. Both arms therefore end at the asserted actual shared states. For the negative anchor, the first three shortcuts from $3(8u-1)$ reach $9u-1$ with one odd departure, and the intervening $d$ odd steps are literal.
2. A hit before a shared upper prefix would keep every subsequent state in $\{1,2\}$. The shared endpoint above 2 prevents that and justifies copying the suffix of *every supplied* hitting certificate, including certificates with extra laps after the first hit. The negative anchor has common upper endpoint $9\cdot3^dt-1\ge8$. The positive canonical anchor at 17 has explicit nonzero lift there. The general prefix equalities alone do not assert early-hit protection for an arbitrary parameter choice.
3. If an odd $z$ has an upper hit with one odd departure, that departure is the first. Thus $9z+1=2^H$, and $6\mid H$ follows from the order of 2 modulo 9. Each $Z_m=(2^{6(m+1)}-1)/9$ realizes exactly one upper odd departure. Its lower path reaches $4^{3m+2}+1$ in two clocks and then $3^{3m+2}+1$ after $2(3m+2)$ more. The latter has the same next state as $3^{3m+1}$. This proves both directions of the unrestricted **odd** rank-one equivalence. Existence of a bad lower endpoint is not established.
4. If $Z_m$ is bad and $(w,r)$ is a first bad tower, the pure power $3^{3m+1}$ is bad. For $w>1$ that conflicts with goodness at smaller base 1. For $w=1$ it forces $r\le3m+1$. Hence $9Z_m+1\ge2^{2r+4}$; equality is allowed. The two neighbor classes concern the successor index $m+1$, with $m$ in the stated residues. They leave the other classes untreated.
5. The height cost $2^d(y+1)\le3^d(x+1)$ composes by multiplication. If a chain actually carries badness to a rank-one endpoint and its total charge is $D$, the strict inequality $9\cdot3^D(z+1)<2^D2^{2r+4}$ contradicts the floor. The cost relation alone transports no basin certificate. PR197 supplies a canonical defect of height at most $2^{40}3^r$ when $w=1$. The sufficient range $r\ge1600$, $3D\le2r$ gives the strict inequality after cubing. Its exact check at 1600 has left and right bit lengths 12810 and 12813. It gives no route to rank one or bound on the charge of a route.
6. The core transfer consumes two odd departures from a particular good upper certificate and changes the upper multiple from $3x$ to $9Y$. At the later paired clocks its actual upper endpoint is $9Q-1$, while the lower endpoint is $Q$. Its conclusion cannot be fed directly into a theorem requiring a certificate on $3Y$ or $9Q$. No iteration of the reduced count was used in the verdict.

I independently replayed the paired Lean module with Lean 4.34.1, explicit implicit-variable checking and warnings treated as errors. It exited 0 and printed 23 axiom reports using only the standard axioms. Independent integer calculations reproduced the two rank-one representative rows $(1925,7,4)$ and $(200,5,2)$ and the threshold comparison. The PR197 declaration and the fresh branch query in its proof were inspected at full commit b27a6fe31a487adf5615e173329ad009b975a3cd. This review does not assert a new compilation of that external module.

## Reviewed Git blobs

| Source within the research packet | Git blob SHA |
| --- | --- |
| bridge/PairedReturn.lean | bd41ffbe1f1a492f6766fd6073d5c51f127c75fd |
| bridge/README.md | 21a17733d5bc5d3e4792a639ae06d3a08330c159 |
| bridge/check_bridge.py | bd464955d5f78812c1ed2a8e5e149cb73e1a07fe |
| core/ExponentTransport.lean | febf92151ae1a37a33db238e40072833eb747fc5 |
| core/README.md | 87a480f41ec09f3e45f2e3ac91df887aa842a1be |
