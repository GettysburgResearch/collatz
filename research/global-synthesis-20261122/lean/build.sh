#!/usr/bin/env bash
set -euo pipefail

# Rebuild only this new packet and its one necessary frozen repository import.
# Existing pinned compiler and Mathlib artifacts are required; no downloads.
: "${MATHLIB_DIR:?Set MATHLIB_DIR to the pinned Mathlib checkout}"
synthesis_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
synthesis_mathlib="$(cd -- "$MATHLIB_DIR" && pwd)"
synthesis_pin=d13f23b723b8a846827a245b89c10fc7d3f11612
if [[ "$(git -C "$synthesis_mathlib" rev-parse HEAD)" != "$synthesis_pin" ]]; then
  printf 'Expected Mathlib revision %s\n' "$synthesis_pin" >&2
  exit 1
fi
if ! git -C "$synthesis_mathlib" diff --quiet HEAD --; then
  printf 'Use a tracked-clean pinned Mathlib checkout.\n' >&2
  exit 1
fi
if [[ "$(lean --version)" != *"version 4.34.1,"* ]]; then
  printf 'Expected Lean 4.34.1.\n' >&2
  exit 1
fi

cd -- "$synthesis_root"
sha256sum --check imports.sha256
mkdir -p .build
synthesis_mathlib_path="$(cd -- "$synthesis_mathlib" && lake env printenv LEAN_PATH)"
printf '%s\n' "$synthesis_mathlib_path" > .build/mathlib-path
synthesis_vendor="$synthesis_root/../../band-return-20261121/lean/vendor"
synthesis_overlay=""
if [[ -n "${SYNTHESIS_IMPORT_OVERLAY:-}" ]]; then
  synthesis_overlay="$(cd -- "$SYNTHESIS_IMPORT_OVERLAY" && pwd):"
fi
export LEAN_PATH="$synthesis_root/.build:$synthesis_root:$synthesis_vendor:$synthesis_overlay$synthesis_mathlib_path"

printf 'Checking imported ShellCover\n'
(
  cd -- "$synthesis_vendor"
  lean -j1 -DwarningAsError=true -o "$synthesis_root/.build/ShellCover.olean" ShellCover.lean
)
for synthesis_module in IndependentBlockBudget IndependentPQCertificate OrdinaryBasinMoments QuantitativeInverseSelector AuditQuantitativeInverseSelector GlobalSynthesisAudit; do
  printf 'Checking new %s\n' "$synthesis_module"
  lean -j1 -DwarningAsError=true -o ".build/$synthesis_module.olean" "$synthesis_module.lean"
done
printf 'Global synthesis Lean build completed.\n'
