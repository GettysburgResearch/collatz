#!/usr/bin/env bash
set -euo pipefail

# Check only this packet and its three necessary local proof imports.
# No toolchain installation, cache download, or network access is performed.
: "${MATHLIB_DIR:?Set MATHLIB_DIR to the existing pinned Mathlib checkout}"
literature_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
literature_mathlib="$(cd -- "$MATHLIB_DIR" && pwd)"
literature_pin=d13f23b723b8a846827a245b89c10fc7d3f11612
if [[ "$(git -C "$literature_mathlib" rev-parse HEAD)" != "$literature_pin" ]]; then
  printf 'Expected Mathlib revision %s\n' "$literature_pin" >&2
  exit 1
fi
if ! git -C "$literature_mathlib" diff --quiet HEAD --; then
  printf 'Mathlib has tracked changes; use a clean pinned checkout.\n' >&2
  exit 1
fi
if [[ "$(lean --version)" != *"version 4.34.1,"* ]]; then
  printf 'Expected Lean 4.34.1.\n' >&2
  exit 1
fi

cd -- "$literature_root"
sha256sum --check imports.sha256
mkdir -p .build
literature_mathlib_path="$(cd -- "$literature_mathlib" && lake env printenv LEAN_PATH)"
printf '%s\n' "$literature_mathlib_path" > .build/mathlib-path
literature_vendor="$literature_root/../../band-return-20261121/lean/vendor"
literature_previous="$literature_root/../../reframe-20261121/lean"
literature_overlay=""
if [[ -n "${LITERATURE_IMPORT_OVERLAY:-}" ]]; then
  literature_overlay="$(cd -- "$LITERATURE_IMPORT_OVERLAY" && pwd):"
fi
export LEAN_PATH="$literature_root/.build:$literature_root:$literature_previous:$literature_vendor:$literature_overlay$literature_mathlib_path"

for literature_module in ShellCover ForwardSection; do
  printf 'Checking imported %s\n' "$literature_module"
  (
    cd -- "$literature_vendor"
    lean -j1 -DwarningAsError=true -o "$literature_root/.build/$literature_module.olean" \
      "$literature_module.lean"
  )
done
printf 'Checking imported MarkedDyadicTransport\n'
(
  cd -- "$literature_previous"
  lean -j1 -DwarningAsError=true -o "$literature_root/.build/MarkedDyadicTransport.olean" \
    MarkedDyadicTransport.lean
)

for literature_module in SourceCollision PhysicalTailBarrier LiteratureAudit; do
  printf 'Checking new %s\n' "$literature_module"
  lean -j1 -DwarningAsError=true -o ".build/$literature_module.olean" "$literature_module.lean"
done
printf 'Literature Lean build completed.\n'
