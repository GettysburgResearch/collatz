# Published checkpoint

The scientific commit is `b579defec53bb791ddbe2b6e07382cbb079ba8fc`, with tree `33594eec89da3eaeb19ae4f6347efe29edaea8ee`. It was pushed without force to `research/astra-universal-descent-20261124`, advancing [PR193](https://github.com/GettysburgResearch/collatz/pull/193) from `a1379492dbaae85e0d16662b41ccc7176ab3c66e`. A fresh GitHub PR read returned the exact new head.

The remote tree matched the tested local tree byte for byte. A newly created complete checkout of the actual published commit then ran:

```sh
python -X utf8 -B tools/validate.py --receipt /outside/checkout/receipt.json
```

All five default repository-integrity commands passed. The checkout had **446 tracked files**, remained clean, and retained the same commit and tree before and after. [Full receipt](PUBLISHED_CHECKOUT.json).

The scientific replay is separate: nineteen new public Lean declarations passed under official Lean 4.34.1 with warnings as errors and standard-only axiom inventories; three exact finite controls passed normally and with optimization. [Verification](VERIFICATION.md) · [Proof/control receipt](LEAN_AND_CONTROLS.json).

This follow-up adds publication records and links them from the verification report. It leaves all scientific sources and their recorded hashes unchanged. The actual final follow-up head is read back and its integrity result recorded in the PR description, avoiding a self-referential in-tree receipt.

No full Collatz proof is claimed. The analytic theorems retain their written/source-qualified scope.
