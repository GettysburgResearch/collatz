# Verification of the fixed-source attempt

## Prepublication checks

The root compiled both new Lean modules with Lean 4.34.1, commit 5045d0056413266e57c625dcd7c365b10e377c52, using a fresh output directory, one worker, and warnings as errors. Both import only Std. All seven named public declarations passed their axiom audits. The 703 exclusion uses propext and Quot.sound; its exact clock-81 equality has no axioms. The steering declarations use at most propext, Classical.choice and Quot.sound.

The exact Python control ran both normally and with optimization enabled. Both executions returned:

    All 81 critical residues steer. Ordinary contact (81, 628, 1106); quotient contact (22, 140, 282).
    Contact triples are (first clock, endpoint, size of complete smaller-source forward union).

These computations check the finite residue table, complete smaller-source forward unions, and exact first contacts. They do not verify an infinite density estimate, existence of a nonconvergent source, or universal original-floor descent.

## Reproducible source replay

The replay program requires a clean complete checkout, hashes the scientific sources, builds fresh Lean objects, parses all named axiom audits including the axiom-free equality, compares normal and optimized Python output, and runs the complete repository validator. Its output directory must be outside the checkout.

The root executed this replay on the real published science commit 29d61ae09fa4b67641725248ee77f87d29c5e1fb, tree ca797fdda0132cde30ec42464d160ccad6a804bb, in a clean complete checkout with 559 tracked files. It started at 09:14:29 UTC and completed at 09:14:56 UTC on 24 November 2026.

All seven named Lean audits passed; the normal and optimized Python outputs were identical; the complete repository validator passed. The source hashes, commit, tree and clean checkout state were unchanged after execution.

The [execution receipt](fresh_replay/receipt.json) has SHA-256 fd4b5a52d7b0f93034819cd96126a39b2e8784523fd370249e3c0cbcd16414e9. The [repository receipt](fresh_replay/repository-validation.json) has SHA-256 43b315f24022443d0f9cab8a2b5a2218dd1cede8fd8fe771702bf36f07181923. The nonempty Lean audit, Python-control and validation output is retained alongside the receipts. Compiler objects are deliberately not committed.

This verification-only successor adds those records and the final upstream recheck without modifying the scientific files. The final successor's clean-checkout validation is reported in the PR after publication.

The mathematical review and exact source pins are adjacent to this record. The controller pressure proof and the source-qualified density argument remain written mathematics.
