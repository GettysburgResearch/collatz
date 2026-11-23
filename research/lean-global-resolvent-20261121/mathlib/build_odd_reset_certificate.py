"""Build an explicit, reviewable Mathlib port and its composed certificate theorem.

The core project imports an upstream induction shim which collides
with Mathlib declarations.  This generator copies three frozen proof sections
verbatim, changing only the outer reset namespace.  A small ordinary-map
interface replaces the incompatible import, and its equality with the map of
OddCertificateMeasure is proved.  Lean independently checks the resulting file.
"""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
CORE = HERE.parent / "lean" / "Collatz"
FROZEN = {
    "TerminalFive.lean": "369a2189d9a65b3cbe7be8dae1010b34bd53cb0107c7de3f256a0933fbdeddb4",
    "UnboundedReset.lean": "66ec761aaffff2509e6cc2d48ce384a6ea05ca56c221c283c069807c7318dd6a",
    "OddReset.lean": "46556cdabf11a88928cafcb1eab2bf328e8f477ce23767e93337c07eb359fa75",
}


def read_frozen(name):
    data = (CORE / name).read_bytes()
    actual = sha256(data).hexdigest()
    if actual != FROZEN[name]:
        raise ValueError(f"frozen source mismatch: {name}: {actual}")
    return data.decode("utf-8")


terminal = read_frozen("TerminalFive.lean")
first = read_frozen("UnboundedReset.lean")
broad = read_frozen("OddReset.lean")

ordinary_interface = terminal.split("def orbit", 1)[1].split("theorem shortcut_pos", 1)[0]
ordinary_interface = "def orbit" + ordinary_interface
odd_run_proofs = first.split("theorem shortcut_two_mul_pred", 1)[1].split(
    "theorem middle_preserves_offset", 1)[0]
odd_run_proofs = "theorem shortcut_two_mul_pred" + odd_run_proofs
broad_proofs = broad.split("namespace CollatzOddReset", 1)[1].rsplit(
    "end CollatzOddReset", 1)[0]

header = '''import OddCertificateMeasure

/-!
Generated explicit Mathlib port, with kernel-checked end-to-end composition.

The source bodies below are extracted verbatim by build_odd_reset_certificate.py
from the following frozen core modules; the reset's outer namespace is renamed.
TerminalFive.lean: 369a2189d9a65b3cbe7be8dae1010b34bd53cb0107c7de3f256a0933fbdeddb4
UnboundedReset.lean: 66ec761aaffff2509e6cc2d48ce384a6ea05ca56c221c283c069807c7318dd6a
OddReset.lean: 46556cdabf11a88928cafcb1eab2bf328e8f477ce23767e93337c07eb359fa75

The separate core import is incompatible with Mathlib's induction declarations.
No theorem is postulated to cross that boundary: all copied proofs are rechecked.
The small interface below uses the odd-certificate module's exact shortcut map,
and orbit_eq proves equality of the two finite-iteration conventions.
The final theorem applies to EVERY complete supplied source certificate.
-/

set_option autoImplicit false
set_option maxHeartbeats 4000000
set_option linter.unusedSimpArgs false

namespace CollatzResetPortBase

def shortcut (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3*n+1) / 2

def Hits (n : Nat) : Nat → Prop
  | 0 => n = 1
  | k+1 => Hits (shortcut n) k

def Basin (n : Nat) : Prop := ∃ k, Hits n k

theorem basin_step (n : Nat) : Basin (shortcut n) ↔ Basin n := by
  constructor
  · rintro ⟨k,h⟩
    exact ⟨k+1,h⟩
  · rintro ⟨k,h⟩
    cases k with
    | zero => change n = 1 at h; subst n; exact ⟨1,rfl⟩
    | succ k => exact ⟨k,h⟩

'''

bridge = '''
theorem shortcut_eq (n : Nat) : shortcut n = CollatzOddCertificate.step n := rfl

theorem orbit_eq (n k : Nat) : orbit n k = CollatzOddCertificate.orbit k n := by
  induction k generalizing n with
  | zero => rfl
  | succ k ih =>
    rw [← orbit_step, ih]
    rfl

theorem basin_iff_certificate (n : Nat) :
    Basin n ↔ Nonempty (CollatzOddCertificate.HitCertificate n) := by
  constructor
  · rintro ⟨k,hk⟩
    refine ⟨⟨k, ?_⟩⟩
    rw [← orbit_eq]
    exact (hits_iff_orbit n k).mp hk
  · rintro ⟨⟨k,hk⟩⟩
    refine ⟨k, (hits_iff_orbit n k).mpr ?_⟩
    rwa [orbit_eq]

end CollatzResetPortBase

open CollatzResetPortBase

namespace CollatzOddResetPort
'''

composition = '''

/-- Every supplied parent certificate has a strictly smaller complete child
certificate.  The statement preserves its arbitrary common suffix. -/
theorem complete_certificate_descent {l P w m : Nat} (h : Guard l P w m)
    (c : CollatzOddCertificate.HitCertificate (P/2)) :
    ∃ c' : CollatzOddCertificate.HitCertificate m,
      CollatzOddCertificate.Below (CollatzOddCertificate.measure c')
        (CollatzOddCertificate.measure c) := by
  have hp := parent_even_nonterminal h
  apply CollatzOddCertificate.splice_one_halving
    (b := l+12) hp.2.1 hp.1 ?_ ?_ ?_ c
  · have he := source_path h
    rw [orbit_eq] at he
    have hd : (P/2)/2 = P/4 := by omega
    rwa [hd]
  · intro he
    have ho := (source_positive_odd h).2
    omega
  · intro j hj ho
    have hodd : orbit m j % 2 = 1 := by rwa [orbit_eq]
    have hb := source_odd_prefix_below h j (by omega) hodd
    rwa [orbit_eq] at hb

/-- The same complete-certificate descent preserves a failed target comparison.
No closure or normalized-unit coverage is assumed. -/
theorem complete_failed_reset {l P w m : Nat} (h : Guard l P w m)
    (c : CollatzOddCertificate.HitCertificate (P/2))
    (hbad : ¬ Nonempty (CollatzOddCertificate.HitCertificate (P-1))) :
    ∃ c' : CollatzOddCertificate.HitCertificate m,
      CollatzOddCertificate.Below (CollatzOddCertificate.measure c')
        (CollatzOddCertificate.measure c) ∧
      ¬ Nonempty (CollatzOddCertificate.HitCertificate (2*m-1)) := by
  obtain ⟨c',hc'⟩ := complete_certificate_descent h c
  refine ⟨c',hc',?_⟩
  intro hc
  apply hbad
  apply (basin_iff_certificate (P-1)).mp
  exact (target_basin_transfer h).mp ((basin_iff_certificate (2*m-1)).mpr hc)

#print axioms complete_certificate_descent
#print axioms complete_failed_reset

end CollatzOddResetPort
'''

output = header + ordinary_interface + odd_run_proofs + bridge + broad_proofs + composition
destination = HERE / "OddResetCertificate.lean"
destination.write_text(output, encoding="utf-8")
print(f"{sha256(output.encode()).hexdigest()}  {destination.name}")
