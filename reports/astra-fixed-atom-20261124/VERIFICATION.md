# Verification of the fixed-source attempt

## Prepublication checks

The root compiled both new Lean modules with Lean 4.34.1, commit 5045d0056413266e57c625dcd7c365b10e377c52, using a fresh output directory, one worker, and warnings as errors. Both import only Std. All seven named public declarations passed their axiom audits. The 703 exclusion uses propext and Quot.sound; its exact clock-81 equality has no axioms. The steering declarations use at most propext, Classical.choice and Quot.sound.

The exact Python control ran both normally and with optimization enabled. Both executions returned:

    All 81 critical residues steer. Ordinary contact (81, 628, 1106); quotient contact (22, 140, 282).
    Contact triples are (first clock, endpoint, size of complete smaller-source forward union).

These computations check the finite residue table, complete smaller-source forward unions, and exact first contacts. They do not verify an infinite density estimate, existence of a nonconvergent source, or universal original-floor descent.

## Reproducible source replay

The replay program requires a clean complete checkout, hashes the scientific sources, builds fresh Lean objects, parses all named axiom audits including the axiom-free equality, compares normal and optimized Python output, and runs the complete repository validator. Its output directory must be outside the checkout. The published clean-checkout receipt will be added in a separate verification commit.

The mathematical review and exact source pins are adjacent to this record. The controller pressure proof and the source-qualified density argument remain written mathematics.
