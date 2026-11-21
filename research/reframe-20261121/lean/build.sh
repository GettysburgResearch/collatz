#!/usr/bin/env bash
set -euo pipefail

# Reuse a clean checkout and its cache at the exact pinned Mathlib revision.
# This script does not install a toolchain, download a cache, or access the network.
: "${MATHLIB_DIR:?Set MATHLIB_DIR to the existing pinned Mathlib checkout}"
reframe_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
reframe_mathlib="$(cd -- "$MATHLIB_DIR" && pwd)"
reframe_pin=d13f23b723b8a846827a245b89c10fc7d3f11612
if [[ "$(git -C "$reframe_mathlib" rev-parse HEAD)" != "$reframe_pin" ]]; then
  printf 'Expected Mathlib revision %s\n' "$reframe_pin" >&2
  exit 1
fi
if ! git -C "$reframe_mathlib" diff --quiet HEAD --; then
  printf 'Mathlib has tracked changes; use a clean pinned checkout.\n' >&2
  exit 1
fi
if [[ "$(lean --version)" != *"version 4.34.1,"* ]]; then
  printf 'Expected Lean 4.34.1.\n' >&2
  exit 1
fi

cd -- "$reframe_root"
sha256sum --check source173.sha256
mkdir -p .build
reframe_mathlib_path="$(cd -- "$reframe_mathlib" && lake env printenv LEAN_PATH)"
printf '%s\n' "$reframe_mathlib_path" > .build/mathlib-path
reframe_vendor="$reframe_root/../../band-return-20261121/lean/vendor"
# Optional fast storage for byte-identical dependency cache files. The receipt
# runner checks every overlay file against the pinned original before and after
# using it. Ordinary builds need no overlay and use Mathlib's own cache directly.
reframe_overlay=""
if [[ -n "${REFRAME_IMPORT_OVERLAY:-}" ]]; then
  reframe_overlay="$(cd -- "$REFRAME_IMPORT_OVERLAY" && pwd):"
fi
export LEAN_PATH="$reframe_root/.build:$reframe_vendor:$reframe_root:$reframe_overlay$reframe_mathlib_path"

for reframe_module in ShellCover ForwardSection; do
  printf 'Checking imported %s\n' "$reframe_module"
  lean -j1 -DwarningAsError=true -o ".build/$reframe_module.olean" \
    "$reframe_vendor/$reframe_module.lean"
done

for reframe_module in DiscretePump MarkedDyadicTransport MergerPopulationPacking ReframeAudit; do
  printf 'Checking new %s\n' "$reframe_module"
  lean -j1 -DwarningAsError=true -o ".build/$reframe_module.olean" "$reframe_module.lean"
done

printf 'Reframe Lean build completed.\n'
