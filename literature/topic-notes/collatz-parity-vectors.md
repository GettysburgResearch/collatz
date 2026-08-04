# Collatz parity vectors and 2-adic coding

## Located classical layer

Terras and Everett establish the finite parity-word/residue-class bijection and affine iterate formula. Bernstein–Lagarias place the standard shortcut map in a global 2-adic conjugacy with the shift.

These sources justify the following as standard infrastructure:

- one length-`L` parity word per residue modulo `2^L`;
- an affine formula with multiplier `3^a/2^L` on each cylinder;
- exact loss of one 2-adic digit per common-parity step;
- compact 2-adic coding of infinite parity itineraries.

## Repository-specific layer

The literature audit did not find exact antecedents for:

- grouping distinct finite cylinders by a common affine endpoint;
- conjugating a sparse common-output fiber to `H_D(MB+d)=NB+d`;
- the collision signature modulo `3^a`;
- universal carry pumping for an arbitrary finite fiber;
- the induced-map real-tail asymptotic paired with the 2-adic code.

These should be presented as native theorems whose *inputs* are classical.

## Useful citation pattern

A native proof should cite `LIT-KTHM-0001` at the first use of a parity cylinder and then proceed self-contained. Repeating “by Terras” for every affine calculation obscures where the genuinely new step begins.

## Active connection

`CLAUDE/T-0021` is an especially clean literature corollary: multiplication by an odd `N` permutes residues modulo `2^j`; Terras then identifies those residues uniformly with parity words. This establishes exact bridge-word uniformity without any probabilistic assumption.
