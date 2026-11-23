# Independent reconstruction: unrestricted source boundary

Reviewer: coordinating researcher, separate from the witness author. Date: 2026-11-23.

**VERIFIED at the stated finite and written scopes.** The exact files reviewed are:

- `HIGH_VARIANCE_WITNESS.md`: SHA256 `ba5042f969cf787e6ec5ff44e521890ccbfc9bea04e6126353745c9f8c385634`.
- `finite_source_boundary.py`: SHA256 `01a370c24a21dc95e05746f0689cfaa4428f90df980278ded9e82a10cf22447e`.
- `lean/Collatz/FiniteSourceBoundary.lean`: SHA256 `9e456d32b4015323542f2741b6662bd9160709c9018734628f15f906afe2f051`.

The review reconstructed FB1–FB9 and inspected the executable independently. A last source state above B exists because the supplied certificate reaches the terminal 1,2 cycle below B. Odd positive shortcut steps increase their source, so the final crossing is even and lands below B. The existing literal-certificate consumer gives a strict original-grade drop at every positive consumed clock; the endpoint is above 2, so its terminal exception is unavailable.

The lower-grade iff is obtained by trimming an arbitrary smaller competitor. At a minimum grade every same-grade capture is already a boundary source, which justifies the numerical maximum tie. The graph checker proves both soundness by decreasing first-hit labels and completeness by inverse closure; its label-zero exception at 1 is necessary and correctly implemented. All other first-hit certificates are forced by valuations and differ only by terminal [2] padding, whose removal lowers the grade. Descending-list lex comparison matches the highest changed multiplicity in the original multiset order. The intrinsic output clock bound counts the distinct retained states before the first hit; it is not assumed of the input.

For the update law, odd B cannot enter the new graph because T(B)>B. An even B attaches exactly when B/2 is already retained: a successful path through B/2 cannot revisit B. Every new boundary source then passes through B and has a strictly larger complete grade. The plateau theorem also follows directly from shrinking the set of capturing certificates, and parity yields the upper jump S'<=2S. No relation between source completion time and target descent time was inserted.

The focused replay compiled the new module with warnings as errors and audited all five public theorems. The separate Python replay checks 383 complete boundary certificates, recovers the two pinned global optima and rejects three damaged graph certificates in both normal and optimized modes. Those computations verify the new algorithm on these finite inputs; they are not all-target coverage.

The finite optimization does not prove entry of T(2B+1)=3B+2 into the certified graph. That is expressly retained as the missing closing step. No substantive correction was needed; one explicit sentence linking lex comparison to the original grade order was added during review.
