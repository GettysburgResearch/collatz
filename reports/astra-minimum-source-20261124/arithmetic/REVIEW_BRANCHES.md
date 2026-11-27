# Independent review of two minimum-source branches

**VERIFIED for the two conditional claims below at the pinned bytes.** The first identifies a canonical representative on one surviving branch. The second excludes a complementary exit cylinder. Universal closure remains open.

| Section | Local file | SHA256 |
|---|---|---|
| Descent, “An adaptive exclusion at the least odd tripling disagreement” | `descent/README.md` | `3a7e78db667997b7dda877f3fe27842d61e80c236ea97f36ddd88c0e40e2a7c8` |
| Associated declarations | `descent/CarryDescent.lean` | `c0591080aba6ca6eb2cbba0ec7a9148ec235be4f4f7ac368ec3787749a3177ea` |
| Author replay | `descent/check.py` | `7c097c14fbfdd0438bd042b23c15a702c1bb83497b1e1a1174143c71d353a00e` |
| Renewal, “A test on the other parity class” | `renewal/README.md` | `272f09b88158210f553de9676ada5bb683a19c9af3c0657a2ab23f4fd737ea4d` |
| Associated declarations | `renewal/UpperRepresentative.lean` | `56190e59bdc895b1a7825d762a393a5d5c96d74daf3ae0fd29ec2350f17818df` |
| Author replay | `renewal/check.py` | `b13bb0e97f0794f0387e7fd083c70b6bb5d4f6b552df0ff56a06c95c5fa9daf9` |

## Canonical source on the surviving branch

Suppose the least discordant positive odd $q$ exists and use the established physical consequences $q<N$, $3q\notin C$, where $N$ is the least bad integer. Write $n=3q=3^h w=2^m a-1$ with both valuations exact. At $h\ge3$, $2^hw-1<q=3^{h-1}w$ because $2^3<3^2$ and $2/3<1$. Its $h$ literal odd steps arrive at $n-1$, hence $n-1$ is good. Also $n+1$ and $q$ both step to $(n+1)/2$. Writing $H_j=3^j a-1$, $n$ reaches $H_m$ in $m$ steps and $n-1$ reaches $H_{m-1}$ in $m$ steps, one halving followed by $m-1$ odd inputs. When $3^m a=1\bmod4$, the two-step merger at $Y=3^{m-1}a=3\bmod4$ would identify the good and bad components. When $3^m a=3\bmod4$, it instead identifies $H_m$ with $H_{m+1}$, so $n$ and $2n+1$ have a common future.

For the latter alternative with $m\ge3$, $3^{m-1}a=1\bmod4$ makes $U=(3^{m-1}a-1)/4$ integral and positive. The same numerator is $-1\bmod9$, giving $U=2\bmod9$. Since $4U=H_{m-1}$ is good, $U$ is good. The bad $n$ goes through $H_m=12U+2$, $6U+1$, $9U+2$, so this is an actual failed transfer. Because $2^ma=n+1=1\bmod3$, $3\nmid a$. Hence $(4U+1)/9=3^{m-3}a$ is already the ternary-unit factorization in the earlier canonical definition, and $B(U)=8\cdot2^{m-3}a-1=3q$. This proves $N\le B(U)<3N$ with the strict upper bound coming from $q<N$. There is no assertion that this $U$ is globally minimal among failed canonical sources. The original definition is pinned at PR192 `b72cea3bcd5aa51aba8df6f5e63bc1c473e9523b`, `research/astra-closing-step-20261124/descent/README.md`, SHA256 `0893ef76b3fa7d3fe0292e064626ea77920020277f1b3127b6c4938ec783dbfa`. The canonical identity in this new branch is a written proof. `adaptive_down` formalizes the other parity's physical merger.

## Eight-step complementary exit

Start at $3q=2^a b-1$ with $a\ge2$, $b$ positive odd, $q>1$, and $s=3^{a-2}b=147+256t$. The $a$ odd steps of $3q$ reach $9s-1$. The smaller positive integer $z=2^{a-2}b-1=(3q-3)/4<q$ reaches $s-1$ in $a-2$ odd steps, allowing zero steps at $a=2$. At the bases $9s-1=1322$, $s-1=146$, I get chronological words `01000001` and `01011100`. Both end at 47. Their high-parameter slopes at this clock are $9\cdot3^2$ and $3^4$, respectively, since the initial increments are $9\cdot256t$ and $256t$. Thus the two complete original paths end at $47+81t$, with clocks $a+8$ and $a+6$. In particular the proof uses an actual smaller representative even when the two clocks differ. The branch occurs for every $a\ge2$. Choose $b=147\cdot3^{-(a-2)}\bmod256$ and $2^ab=1\bmod3$, then take any sufficiently large positive Chinese remainder lift. The narrower Lean theorem `complementary_exit` proves equality of any orbit-invariant label at the two prescribed inputs. Positivity and strict comparison at the tripling source follow from the displayed formula for $z$.

## Independent controls and formal scope

The separate [review program](review_branches.py) checked the canonical identities on all 3,469 qualifying shapes with odd $q<500000$, without assigning either basin label. It independently built three positive Chinese remainder lifts at each of $a=2,\ldots,101$, checked their two exact clocks, and checked the base words. Ordinary and optimized Python agreed. The two author scripts were also executed in both modes at their pins. The renewal script returned 59 complementary cases in its own range.

I compiled exact copies of both Lean sources plus `SourceDeletion.lean` with Lean 4.34.1 and warnings as errors. For every public definition or theorem I added a fully qualified `#print axioms` in the review copy. All 38 declarations compiled, comprising 14 in `CarryDescent`, 13 in `UpperRepresentative` and 11 in `SourceDeletion` (the latter at SHA256 `21227f38df7f95b29613ec322a1e48f3fc0e423155fb12867c9dfcf546699af0`). The complete [declaration audit](axioms.txt) contains only subsets of `propext`, `Classical.choice` and `Quot.sound`. This audit verifies the declarations as stated. The written verdict above applies only to the named two sections. Neither branch provides an exit covering all hypothetical minimum sources.
