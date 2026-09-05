# Spectrum-switch packet: publication handoff

The attached `collatz_pr92_pass5_end_to_end.zip` supplies the separately
prepared [spectrum-switch fifth pass](pass5-spectrum-switch/README.md).
It was prepared against `6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc`.

At import time, PR #92 had advanced to
`a19115bbf99485b1b8ba15521df87f5fcef8946b`, with a different fifth-pass
packet already in [pass5/](pass5/README.md). Its README conflicts with the
attachment's README. Both contributions are preserved: the six attached
writeups are placed under `pass5-spectrum-switch/` instead of `pass5/`.
The attached experiment and report retain their original paths. All eleven
attached files retain their original bytes, including historical path and
local-only publication statements. References in this packet to its own
`research/astra-three-routes/pass5/` writeups should use
`research/astra-three-routes/pass5-spectrum-switch/` after this import.

The generator and separately implemented verifier were replayed against
the attached canonical result in normal and optimized Python modes. Both
passed, including eight resealed-corruption checks in each verifier run.
Archive SHA-256 and Git blob receipts match. This is an import/replay check,
not independent mathematical review; theorem-level claims remain proposed.
