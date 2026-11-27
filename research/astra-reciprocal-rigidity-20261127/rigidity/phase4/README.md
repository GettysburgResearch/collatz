# Source height and periodic pieces

[SMALL_ANCHOR_WORDS.md](SMALL_ANCHOR_WORDS.md) proves a sharp ordinary source-height alternative. Fix a maximum of \(K\) consecutive pieces and a fractional margin \(0<\delta<1\). If a positive source below \(2^{(1-\delta)L}\) realizes a sufficiently long length-\(L\) word whose pieces have rational periodic anchors of height at most \(\epsilon(K,\delta)L\), the source trajectory must hit one piece's exact anchor at that piece's start. The displayed \(\epsilon\) is explicit and the length onset is ineffective. For a bounded number of odd runs this gives \(x\ge 2^{L-o(L)}\), since the pure odd and even anchors are negative one and zero.

The proof invokes the classical rational three-place Subspace Theorem. The paper compares the result with the effective odd-clock periodic-dictionary bound of Weaver and the three-place methods in PR193 and PR210. The source decomposition is a genuine assumption; the result allows arbitrary trajectories whose decompositions require more pieces or greater rational anchor heights.

[ChronologicalAnchor.lean](ChronologicalAnchor.lean) imports the checked ordinary word definitions from the descent packet. It proves the normalized finite word transport and converts the projected prefix identity into an exact physical return, with all specified branch parities. The Subspace Theorem and the asymptotic projection argument are covered by the written proof. Both Lean declarations passed strict Lean 4.34.1 checking with the standard axioms.

[anchor_controls.py](anchor_controls.py) reconstructs the least positive realizer from every shortcut parity word through length eight, checks the ordinary updates, and verifies all partitions into at most three pieces. It also enumerates every one-run word through the selected lengths ending at 256. [ANCHOR_CONTROLS.json](ANCHOR_CONTROLS.json) records the replay. The checks exercise finite arithmetic and do not estimate the ineffective onset. From this directory run

```sh
python anchor_controls.py --check
python -O anchor_controls.py --check
```

The module needs the pinned mathlib cache and previously built PostWords module. For an isolated rebuild, compile \(\texttt{RampShadow.lean}\), \(\texttt{PostWords.lean}\), then \(\texttt{ChronologicalAnchor.lean}\) into the same temporary Lean import path, with \(\texttt{-DwarningAsError=true}\). The phase-two replay script demonstrates the environment setup. [Source of PostWords](../../descent/postpeak/PostWords.lean) · [Source of RampShadow](../../descent/RampShadow.lean) · [Replay setup](../phase2/verify_phase2.py)
