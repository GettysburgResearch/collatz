import GoodNeighbors

namespace CanonicalFloor
open GlobalFloor

private theorem even_step (n : ℕ) : shortcut (2*n)=n := by simp [shortcut]

private theorem odd_step (n : ℕ) : shortcut (2*n+1)=3*n+2 := by
  simp [shortcut]
  omega

/-- Two successive exponent-two native edges give a four-clock merger of
the phase's triple with the one-clock image of a good neighboring value. -/
theorem two_edge_bridge {x y w : ℕ} (first : 4*y=3*x+1) (second : 4*w=3*y+1) :
    shortcut^[4] (3*x)=shortcut (2*w-1) := by
  have a : shortcut (3*x)=6*y-1 := by
    rw [show 3*x=2*(2*y-1)+1 by omega,odd_step]
    omega
  have b : shortcut (6*y-1)=2*(2*(3*w-1)) := by
    rw [show 6*y-1=2*(3*y-1)+1 by omega,odd_step]
    omega
  have c : shortcut (2*w-1)=3*w-1 := by
    rw [show 2*w-1=2*(w-1)+1 by omega,odd_step]
    omega
  change shortcut (shortcut (shortcut (shortcut (3*x))))=shortcut (2*w-1)
  rw [a,b,even_step,even_step,c]

private theorem good_iterate (t n : ℕ) : Good n ↔ Good (shortcut^[t] n) := by
  induction t generalizing n with
  | zero => rfl
  | succ t ih => exact (good_step n).trans (ih (shortcut n))

theorem good_triple {x y w : ℕ} (first : 4*y=3*x+1) (second : 4*w=3*y+1)
    (neighbor : Good (2*w-1)) : Good (3*x) := by
  apply (good_iterate 4 (3*x)).mpr
  rw [two_edge_bridge first second]
  exact (good_step _).mp neighbor

/-- A one edge followed by two exponent-two edges starts a canonical
reverse discrepancy, given the actual bad and good neighboring marks. -/
theorem canonical_witness {v x y w : ℕ} (incoming : 2*x=3*v+1)
    (first : 4*y=3*x+1) (second : 4*w=3*y+1)
    (bad : ¬Good x) (neighbor : Good (2*w-1)) :
    x%48=17 ∧ ¬Good x ∧ Good (3*x) := by
  refine ⟨?_,bad,good_triple first second neighbor⟩
  omega

/-- With the supplied one-two-two block and bounded-cycle height input,
leastness of a canonical discrepancy gives a global ordinary good interval. -/
theorem canonical_floor {v x y w q s z : ℕ} (incoming : 2*x=3*v+1)
    (first : 4*y=3*x+1) (second : 4*w=3*y+1)
    (bad : ¬Good x) (neighbor : Good (2*w-1)) (bound : x<8*q)
    (scale : 2*s+1=3*q) (floor : ∀ n>0, ¬Good n → s≤n)
    (least : ∀ n>0, n%48=17 → ¬Good n → Good (3*n) → z≤n) :
    3*z≤16*s+7 ∧ ∀ n>0, 16*n+7<3*z → Good n := by
  obtain ⟨residue,_,triple⟩ := canonical_witness incoming first second bad neighbor
  have scaled := least x (by omega) residue bad triple
  constructor
  · omega
  · intro n pos small
    by_contra hn
    have := floor n pos hn
    omega

private theorem pair (d : ℕ) : shortcut^[2] (1+4*d)=1+3*d := by
  change shortcut (shortcut (1+4*d))=1+3*d
  rw [show 1+4*d=2*(2*d)+1 by ring,odd_step,show 3*(2*d)+2=2*(1+3*d) by ring,even_step]

/-- A supplied divisibility by a power of four gives the actual endpoint
after that many pairs, allowing any final parity. -/
theorem power_descent (r d : ℕ) : shortcut^[2*r] (1+4^r*d)=1+3^r*d := by
  induction r generalizing d with
  | zero => simp
  | succ r ih =>
    have clock : 2*(r+1)=2*r+2 := by omega
    rw [clock,Function.iterate_add_apply, show 1+4^(r+1)*d=1+4*(4^r*d) by rw [pow_succ]; ring,
      pair,show 1+3*(4^r*d)=1+4^r*(3*d) by ring,ih,pow_succ]
    ring

/-- If a bad source lies below the witness at the head of the minimum's
descending run and has the full divisibility of that run, equality follows.
The global floor and the existence of the upper witness are explicit inputs. -/
theorem minimum_squeeze {r b s z : ℕ} (endpoint : s=1+3^r*b)
    (least : ∀ v>0, ¬Good v → s≤v) (zpos : 0<z) (zbad : ¬Good z)
    (ceiling : z≤1+4^r*b) (divisible : 4^r ∣ z-1) :
    z=1+4^r*b ∧ shortcut^[2*r] z=s := by
  obtain ⟨d,hd⟩ := divisible
  have start : z=1+4^r*d := by omega
  have visit : shortcut^[2*r] z=1+3^r*d := by rw [start,power_descent]
  have low : s≤1+3^r*d := by
    apply least _ (by omega)
    intro hit
    exact zbad ((good_iterate (2*r) z).mpr (visit ▸ hit))
  have equal : b=d := by
    rcases lt_trichotomy b d with small|same|large
    · have h := Nat.mul_lt_mul_of_pos_left small (by positivity : 0<4^r)
      omega
    · exact same
    · have h := Nat.mul_lt_mul_of_pos_left large (by positivity : 0<3^r)
      omega
  subst d
  exact ⟨start,visit.trans endpoint.symm⟩

private theorem run_slope (xs : ℕ → ℕ) (minimum : ∀ i, 1≤xs i) (r : ℕ)
    (twos : ∀ i<r, 4*xs i=3*xs (i+1)+1) :
    3^r*(xs r-1)=4^r*(xs 0-1) := by
  induction r with
  | zero => simp
  | succ r ih =>
    have a := twos r (by omega)
    have b : 3*(xs (r+1)-1)=4*(xs r-1) := by
      have := minimum r
      have := minimum (r+1)
      omega
    calc
      3^(r+1)*(xs (r+1)-1) = 3^r*(3*(xs (r+1)-1)) := by rw [pow_succ]; ring
      _ = 4*(3^r*(xs r-1)) := by rw [b]; ring
      _ = 4^(r+1)*(xs 0-1) := by rw [ih (fun i lt => twos i (by omega)),pow_succ]; ring

private theorem no_six {s w : ℕ} (large : 25≤s) (cap : 3*w≤16*s+7)
    (slope : 3^6*(w-1)=4^6*(s-1)) : False := by
  norm_num at slope
  omega

private theorem factor_run {i s x v : ℕ} (sp : 0<s) (xp : 0<x)
    (eq : 3^i*(x-1)=4^i*(s-1)) (en : 2*x=3*v+1) :
    ∃ b : ℕ, s=1+3^i*b ∧ x=1+4^i*b ∧ b%3=1 := by
  have cop : (3^i : ℕ).Coprime (4^i) := Nat.Coprime.pow i i (by decide)
  obtain ⟨b,hb⟩ := cop.dvd_of_dvd_mul_left (show 3^i ∣ 4^i*(s-1) from ⟨x-1,eq.symm⟩)
  have hw : x-1=4^i*b := by
    apply Nat.mul_left_cancel (by positivity : 0<3^i)
    rw [eq,hb]
    ring
  have modpow : (4^i : ℕ)%3=1 := by rw [Nat.pow_mod]; simp
  have modu := Nat.mul_mod (4^i) b 3
  rw [modpow,one_mul,Nat.mod_mod] at modu
  refine ⟨b,by omega,by omega,?_⟩
  omega

/-- Only the first six supplied native backward edges are used. A globally
minimal starting phase with the bounded-branch ceiling forces two to five
successive exponent-two incoming edges, then an exponent-one edge. -/
theorem minimum_run (xs : ℕ → ℕ) (large : 25≤xs 0) (minimum : ∀ i, xs 0≤xs i)
    (bounded : ∀ i, 3*xs i≤16*xs 0+7)
    (edge : ∀ i, 2*xs i=3*xs (i+1)+1 ∨ 4*xs i=3*xs (i+1)+1) :
    ∃ r b : ℕ, 2≤r ∧ r≤5 ∧ 2*xs r=3*xs (r+1)+1 ∧
      (∀ i<r, 4*xs i=3*xs (i+1)+1) ∧
      xs 0=1+3^r*b ∧ xs r=1+4^r*b ∧ b%3=1 := by
  have ex : ∃ r : ℕ, r<6 ∧ 2*xs r=3*xs (r+1)+1 := by
    by_contra! h
    have all (i : ℕ) (lt : i<6) : 4*xs i=3*xs (i+1)+1 :=
      (edge i).resolve_left (h i lt)
    exact no_six large (bounded 6) (run_slope xs (fun i => by have := minimum i; omega) 6 all)
  let r := Nat.find ex
  have rs : r<6 := (Nat.find_spec ex).1
  have entry : 2*xs r=3*xs (r+1)+1 := (Nat.find_spec ex).2
  have twos (i : ℕ) (lt : i<r) : 4*xs i=3*xs (i+1)+1 := by
    apply (edge i).resolve_left
    intro one
    exact Nat.find_min ex lt ⟨by omega,one⟩
  have rl : 2≤r := by
    by_contra! h
    rcases (show r=0 ∨ r=1 by omega) with zero|one
    · rw [zero] at entry
      change 2*xs 0=3*xs 1+1 at entry
      have := minimum 1
      omega
    · have a := twos 0 (by omega)
      rw [one] at entry
      change 2*xs 1=3*xs 2+1 at entry
      change 4*xs 0=3*xs 1+1 at a
      have := minimum 2
      omega
  have eq := run_slope xs (fun i => by have := minimum i; omega) r twos
  obtain ⟨b,lo,hi,unit⟩ := factor_run (by omega) (by have := minimum r; omega) eq entry
  exact ⟨r,b,rl,by omega,entry,twos,lo,hi,unit⟩

/-- From the bounded native phase sequence, its neighboring labels, the
global bad floor and canonical leastness, locate the canonical witness above
the minimum and squeeze any fully divisible least canonical source onto it. -/
theorem bounded_canonical_minimum (xs : ℕ → ℕ) (z : ℕ) (large : 25≤xs 0)
    (bounded : ∀ i, 3*xs i≤16*xs 0+7)
    (edge : ∀ i, 2*xs i=3*xs (i+1)+1 ∨ 4*xs i=3*xs (i+1)+1)
    (bad : ∀ i, ¬Good (xs i)) (neighbor : ∀ i, Good (2*xs i-1))
    (floor : ∀ n>0, ¬Good n → xs 0≤n)
    (zp : 0<z) (zb : ¬Good z)
    (least : ∀ n>0, n%48=17 → ¬Good n → Good (3*n) → z≤n) :
    ∃ r b : ℕ, 2≤r ∧ r≤5 ∧ xs 0=1+3^r*b ∧ xs r=1+4^r*b ∧ b%3=1 ∧
      (xs r)%48=17 ∧ Good (3*xs r) ∧ z≤xs r ∧
      243*(z-1)≤1024*(xs 0-1) ∧
      (4^r ∣ z-1 → z=xs r ∧ shortcut^[2*r] z=xs 0) := by
  have pos (i : ℕ) : 0<xs i := by rcases edge i with a|a <;> omega
  have min (i : ℕ) := floor _ (pos i) (bad i)
  obtain ⟨r,b,lo,hi,entry,twos,lower,upper,unit⟩ := minimum_run xs large min bounded edge
  have e1 := twos (r-1) (by omega)
  have e2 := twos (r-2) (by omega)
  rw [show r-1+1=r by omega] at e1
  rw [show r-2+1=r-1 by omega] at e2
  obtain ⟨residue,_,triple⟩ := canonical_witness entry e1 e2 (bad _) (neighbor _)
  have cap := least _ (pos r) residue (bad _) triple
  have price : 243*4^r≤1024*3^r := by
    rcases (show r=2 ∨ r=3 ∨ r=4 ∨ r=5 by omega) with h|h|h|h <;> rw [h] <;> decide
  refine ⟨r,b,lo,hi,lower,upper,unit,residue,triple,cap,?_,?_⟩
  · calc
      243*(z-1) ≤ 243*(4^r*b) := Nat.mul_le_mul_left _ (by omega)
      _ = (243*4^r)*b := by ring
      _ ≤ (1024*3^r)*b := Nat.mul_le_mul_right b price
      _ = 1024*(xs 0-1) := by rw [lower]; simp; ring
  · intro div
    obtain ⟨eq,hit⟩ := minimum_squeeze lower floor zp zb (cap.trans_eq upper) div
    exact ⟨eq.trans upper.symm,hit⟩

/-- A least source in the canonical residue class must lie on the cycle
when the descending run has length two, as detected by the ternary digit. -/
theorem length_two_capture {s z r b x : ℕ}
    (lo : 2≤r) (hi : r≤5) (lower : s=1+3^r*b)
    (ternary : ¬27 ∣ s-1) (canonical : z%48=17)
    (squeeze : 4^r ∣ z-1 → z=x ∧ shortcut^[2*r] z=s) :
    r=2 ∧ z=x ∧ shortcut^[4] z=s := by
  have small : r=2 := by
    by_contra h
    apply ternary
    rcases (show r=3 ∨ r=4 ∨ r=5 by omega) with k|k|k <;>
      rw [k] at lower <;> norm_num at lower <;> omega
  subst r
  exact ⟨rfl,squeeze (by norm_num; omega)⟩

#print axioms bounded_canonical_minimum
#print axioms length_two_capture
#print axioms minimum_run
#print axioms two_edge_bridge
#print axioms good_triple
#print axioms canonical_witness
#print axioms canonical_floor
#print axioms power_descent
#print axioms minimum_squeeze
end CanonicalFloor
