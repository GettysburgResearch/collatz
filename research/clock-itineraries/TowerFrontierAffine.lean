module

public import TernaryItinerary
import all TernaryItinerary

public section

namespace Collatz.Itinerary.TowerFrontier

set_option autoImplicit false
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000
set_option exponentiation.threshold 2048

/-- The shortcut endpoint and the initial exponent plus the number of odd steps. -/
@[expose] def track : Nat → Nat → Nat → Nat × Nat
  | 0, n, e => (n,e)
  | k+1, n, e =>
    if n%2=0 then track k (n/2) e else track k ((3*n+1)/2) (e+1)

theorem affine (k n e t : Nat) :
    run k (n+2^k*3^e*t) = (track k n e).1 + 3^(track k n e).2*t := by
  induction k generalizing n e with
  | zero => simp [run, track]
  | succ k ih =>
    let u := 2^k*3^e*t
    have scale : 2^(k+1)*3^e*t = 2*u := by
      simp only [u, Nat.pow_succ]
      ac_rfl
    rw [scale, run]
    by_cases even : n%2=0
    · have hs : step (n+2*u) = n/2+u := by
        simp [step, even]
        omega
      rw [hs]
      simpa [track, even, u] using ih (n/2) e
    · have hs : step (n+2*u) = (3*n+1)/2+3*u := by
        simp only [step, Nat.add_mod, Nat.mul_mod_right,
          Nat.add_zero, Nat.mod_mod, even, ↓reduceIte]
        omega
      have hu : 3*u=2^k*3^(e+1)*t := by
        simp only [u, Nat.pow_succ]
        ac_rfl
      rw [hs, hu]
      simpa [track, even] using ih ((3*n+1)/2) (e+1)

private theorem transport (k n e j t : Nat) :
    track k (n+2^k*3^e*t) (e+j) =
      ((track k n e).1 + 3^(track k n e).2*t, (track k n e).2+j) := by
  induction k generalizing n e with
  | zero => simp [track]
  | succ k ih =>
    let u := 2^k*3^e*t
    have scale : 2^(k+1)*3^e*t = 2*u := by simp only [u,Nat.pow_succ]; ac_rfl
    rw [scale, track]
    simp only [Nat.add_mod, Nat.mul_mod_right, Nat.add_zero, Nat.mod_mod]
    by_cases even : n%2=0
    · simp only [even, ↓reduceIte]
      have hs : (n+2*u)/2 = n/2+u := by omega
      rw [hs]
      simpa [track,even,u] using ih (n/2) e
    · simp only [even, ↓reduceIte]
      have hs : (3*(n+2*u)+1)/2=(3*n+1)/2+3*u := by omega
      have hu : 3*u=2^k*3^(e+1)*t := by simp only [u,Nat.pow_succ]; ac_rfl
      rw [hs,hu,show e+j+1=e+1+j by omega]
      simpa [track,even] using ih ((3*n+1)/2) (e+1)

private theorem track_add (i j n e : Nat) :
    track (i+j) n e = track j (track i n e).1 (track i n e).2 := by
  induction i generalizing n e with
  | zero => simp [track]
  | succ i ih => rw [Nat.succ_add,track,track]; split <;> apply ih

private def packed : Nat := 0x8cd03a22985b0c2d86167a83c941dca0f25076283b100a080505074a83a4c03480507401a01310098804c6151180698538601a614aa01290094804a200410021850e601a613f309f9008e80475068a011cc02e804750672833880104008506528329008640086128b0944c02c601640209805900806016505f1001c800e4007505e282f1007c40087334282d9416ca0b6505998051007660145057a82bcc028601430099804cc02660145053a00e100708038505208009cb62200260efa82854142a0a1401aa00d54136200272aba82614130a09860de9804500626011300818040c02260114017a00bd005e60115044a8224800a4005504310015831640054015a00b10058802c30071803940fa20027222b05b140f2a079503b200a182bc8028401320098c01a600d4012a00948008600d609fa81ad40d6a06b50339001140ca400471bd1802cc016600b30059802d40bc4004502da816cc014600a608398029003a600a400e20070400220016079303c940a020015026281310034801a300420069408e801a606718020c0106008400b20058c00e2001605b302d9002880144009a0051407080146050b0284800440024008a004500224002604498014c00a600540071000980f24002501320035001a800d30021801100164002602da00290014800a7079100054034400140042002080024001500a28050c00440014002a0014c004600240021800940146002500418004c002600140012000900020000

/-- Eight-step results for the 256 low bytes. Each field packs the endpoint
    in its low thirteen bits and the odd count in its next four bits. -/
private def lookup (i : Nat) : Nat × Nat :=
  let field := packed >>> (17*i)
  (field%8192,(field/8192)%16)

private theorem lookup_eq : ∀ i : Fin 256, lookup i.val = track 8 i.val 0 := by
  decide +kernel

private def jump (n e : Nat) : Nat × Nat :=
  let z := lookup (n%256)
  (z.1 + 3^z.2*(n/256), z.2+e)

private theorem jump_eq (n e : Nat) : jump n e = track 8 n e := by
  have h := transport 8 (n%256) 0 e (n/256)
  have repr : n%256 + 2^8*3^0*(n/256)=n := by omega
  rw [repr,Nat.zero_add] at h
  have ht := lookup_eq ⟨n%256, Nat.mod_lt _ (by decide)⟩
  simpa [jump,ht] using h.symm

private def blocks : Nat → Nat → Nat → Nat × Nat
  | 0,n,e => (n,e)
  | k+1,n,e => let z := jump n e; blocks k z.1 z.2

private theorem blocks_eq (k n e : Nat) : blocks k n e = track (8*k) n e := by
  induction k generalizing n e with
  | zero => simp [blocks,track]
  | succ k ih =>
    rw [blocks,ih,jump_eq,Nat.mul_succ,Nat.add_comm,track_add]

/-- An executable evaluator for the same shortcut endpoints and odd counts. -/
def stride (h n e : Nat) : Nat × Nat :=
  let z := blocks (h/8) n e
  track (h%8) z.1 z.2

theorem stride_eq (h n e : Nat) : stride h n e = track h n e := by
  unfold stride
  rw [blocks_eq, ← track_add, Nat.div_add_mod]

def segment (check : Nat → Bool) : Nat → Nat → Bool
  | 0, _ => true
  | k+1, r => check r && segment check k (r+1)

theorem segment_sound {check : Nat → Bool} {a k r : Nat} (h : segment check k a = true)
    (lo : a ≤ r) (hi : r < a+k) : check r = true := by
  induction k generalizing a with
  | zero => omega
  | succ k ih =>
    simp only [segment, Bool.and_eq_true] at h
    by_cases eq : a=r
    · simpa [eq] using h.1
    · exact ih h.2 (by omega) (by omega)

theorem segment_join {check : Nat → Bool} {k l a : Nat}
    (x : segment check k a = true) (y : segment check l (a+k) = true) :
    segment check (k+l) a = true := by
  induction k generalizing a with
  | zero => simpa [segment] using y
  | succ k ih =>
    simp only [segment, Bool.and_eq_true] at x
    rw [Nat.succ_add,segment,Bool.and_eq_true]
    exact ⟨x.1, ih x.2 (by simpa [Nat.add_assoc,Nat.add_comm,Nat.add_left_comm] using y)⟩

end Collatz.Itinerary.TowerFrontier
