module

public import ShellCover

@[expose] public section

/-!
# A complete ordinary normal-form reduction for the blocked mixed-base rule

The five digit maps and the matrix interpretation are from Example 4.3 of
Yolcu--Aaronson--Heule, arXiv:2105.14697v3.  We give an independent proof of
the ten-rule subsystem's termination, retaining its actual ordinary orbit.
No theorem below supplies the missing f1-to-0t rule or asserts Collatz.
-/

namespace CollatzShell.MixedBaseNormalForm

inductive Digit where
  | f | t | z | o | u
  deriving DecidableEq, Repr

open Digit

def num : Digit → Nat → Nat
  | f, x => 2*x
  | t, x => 2*x+1
  | z, x => 3*x
  | o, x => 3*x+1
  | u, x => 3*x+2

def eval : List Digit → Nat → Nat
  | [], x => x
  | d::w, x => eval w (num d x)

def value (w : List Digit) : Nat := eval w 1

def matrix : Digit → Nat × Nat → Nat × Nat
  | f, (x,y) => (x+y,x)
  | t, (x,y) => (x+3*y+1,3*x+4*y+1)
  | z, (x,y) => (7*x+2*y+2,2*x+5*y+1)
  | o, (x,y) => (2*x+y+1,x+y)
  | u, (x,y) => (2*x+2*y,2*x+4*y+2)

def interpret : List Digit → Nat × Nat → Nat × Nat
  | [], p => p
  | d::w, p => matrix d (interpret w p)

def rank (w : List Digit) : Nat :=
  let p := interpret w (1,1)
  p.1+5*p.2

def Below (p q : Nat × Nat) : Prop := p.1 < q.1 ∧ p.2 ≤ q.2

theorem eval_append (w v : List Digit) (x : Nat) :
    eval (w++v) x = eval v (eval w x) := by
  induction w generalizing x with
  | nil => rfl
  | cons d w ih => simpa [eval] using ih (num d x)

theorem interpret_append (w v : List Digit) (p : Nat × Nat) :
    interpret (w++v) p = interpret w (interpret v p) := by
  induction w with
  | nil => rfl
  | cons d w ih => simp [interpret,ih]

theorem eval_pos (w : List Digit) {x : Nat} (hx : 0<x) : 0<eval w x := by
  induction w generalizing x with
  | nil => exact hx
  | cons d w ih =>
    apply ih
    cases d <;> simp only [num] <;> omega

theorem value_pos (w : List Digit) : 0<value w := eval_pos w (by decide)

theorem eval_lt (w : List Digit) {x y : Nat} (h : x<y) : eval w x<eval w y := by
  induction w generalizing x y with
  | nil => exact h
  | cons d w ih =>
    apply ih
    cases d <;> simp only [num] <;> omega

theorem matrix_below (d : Digit) {p q : Nat × Nat} (h : Below p q) :
    Below (matrix d p) (matrix d q) := by
  rcases p with ⟨x,y⟩
  rcases q with ⟨a,b⟩
  rcases h with ⟨h1,h2⟩
  cases d <;> simp only [matrix,Below] <;> omega

theorem interpret_below (w : List Digit) {p q : Nat × Nat} (h : Below p q) :
    Below (interpret w p) (interpret w q) := by
  induction w with
  | nil => exact h
  | cons d w ih => exact matrix_below d ih

theorem rank_context {a b : List Digit}
    (h : ∀ p, Below (interpret b p) (interpret a p))
    (pre post : List Digit) : rank (pre++b++post)<rank (pre++a++post) := by
  have cmp := interpret_below pre (h (interpret post (1,1)))
  dsimp only [rank]
  simp only [interpret_append]
  rcases cmp with ⟨c1,c2⟩
  omega

/-- The five internal exchanges retained when f1 -> 0t is omitted. -/
inductive Exchange : List Digit → List Digit → Prop where
  | fz : Exchange [f,z] [z,f]
  | fu : Exchange [f,u] [o,f]
  | tz : Exchange [t,z] [o,t]
  | to1 : Exchange [t,o] [u,f]
  | tu : Exchange [t,u] [u,t]

theorem exchange_below {a b : List Digit} (h : Exchange a b) (p : Nat × Nat) :
    Below (interpret b p) (interpret a p) := by
  rcases p with ⟨x,y⟩
  cases h <;> simp [interpret,matrix,Below] <;> omega

theorem exchange_value {a b : List Digit} (h : Exchange a b) (x : Nat) :
    eval a x = eval b x := by
  cases h <;> simp [eval,num] <;> omega

/-- The universal proposed partner erases the ternary one of the blocked
f1 pattern.  Its ordinary value and the very same global matrix rank both
strictly decrease, in every finite mixed context.  Component equality is a
separate, unproved condition; it is not a rewrite rule of the subsystem. -/
theorem blocked_erasure_decreases (pre post : List Digit) :
    value (pre++[f]++post)<value (pre++[f,o]++post) ∧
    rank (pre++[f]++post)<rank (pre++[f,o]++post) := by
  constructor
  · simp only [value,eval_append,eval,num]
    exact eval_lt post (by omega)
  · apply rank_context (a:=[f,o]) (b:=[f])
    intro p
    rcases p with ⟨x,y⟩
    simp [interpret,matrix,Below]
    omega

/-- A reduction on canonical words; the leading value one and final identity
are implicit.  Every rule is one of the ten retained YAH rules. -/
inductive Reduces : List Digit → List Digit → Prop where
  | exchange (pre post : List Digit) {a b : List Digit} (h : Exchange a b) :
      Reduces (pre++a++post) (pre++b++post)
  | leading_z (w : List Digit) : Reduces (z::w) (t::w)
  | leading_o (w : List Digit) : Reduces (o::w) (f::f::w)
  | leading_u (w : List Digit) : Reduces (u::w) (f::t::w)
  | final_f (w : List Digit) : Reduces (w++[f]) w
  | final_t (w : List Digit) : Reduces (w++[t]) (w++[u])

theorem reduces_rank {w v : List Digit} (h : Reduces w v) : rank v<rank w := by
  cases h with
  | exchange pre post h => exact rank_context (exchange_below h) pre post
  | leading_z w => simp [rank,interpret,matrix]; omega
  | leading_o w => simp [rank,interpret,matrix]; omega
  | leading_u w => simp [rank,interpret,matrix]; omega
  | final_f w =>
    have h := interpret_below w (show Below (1,1) (matrix f (1,1)) from by decide)
    dsimp only [rank]
    simp only [interpret_append,interpret]
    rcases h with ⟨h1,h2⟩
    omega
  | final_t w =>
    have h := interpret_below w
      (show Below (matrix u (1,1)) (matrix t (1,1)) from by decide)
    dsimp only [rank]
    simp only [interpret_append,interpret]
    rcases h with ⟨h1,h2⟩
    omega

/-- Every reduction is value preserving or exactly one ordinary shortcut
step.  In particular, no rational or 2-adic source is introduced. -/
theorem reduces_orbit {w v : List Digit} (h : Reduces w v) :
    ∃ k, k≤1 ∧ orbit k (value w)=value v := by
  cases h with
  | exchange pre post h =>
    refine ⟨0,by decide,?_⟩
    simp only [orbit,value,eval_append,exchange_value h]
  | leading_z w => exact ⟨0,by decide,rfl⟩
  | leading_o w => exact ⟨0,by decide,rfl⟩
  | leading_u w => exact ⟨0,by decide,rfl⟩
  | final_f w =>
    refine ⟨1,by decide,?_⟩
    simp [value,eval_append,eval,num,orbit,step]
  | final_t w =>
    refine ⟨1,by decide,?_⟩
    simp only [value,eval_append,eval,num,orbit,step]
    have odd : (2*eval w 1+1)%2 ≠ 0 := by omega
    simp [odd]
    omega

def Normal (w : List Digit) : Prop := ¬∃ v, Reduces w v

inductive Derives : List Digit → List Digit → Prop where
  | refl (w : List Digit) : Derives w w
  | cons {w v u : List Digit} (first : Reduces w v) (rest : Derives v u) :
      Derives w u

theorem derives_orbit {w u : List Digit} (h : Derives w u) :
    ∃ k, orbit k (value w)=value u := by
  induction h with
  | refl w => exact ⟨0,rfl⟩
  | cons first rest ih =>
    obtain ⟨a,_,ha⟩ := reduces_orbit first
    obtain ⟨b,hb⟩ := ih
    exact ⟨a+b,by rw [orbit_add,ha,hb]⟩

/-- Termination for every finite mixed-base word, by the concrete natural
matrix rank.  This is the omitted-rule subsystem, not the full system. -/
theorem normalization_exists (w : List Digit) :
    ∃ u, Derives w u ∧ Normal u := by
  have all : ∀ r w, rank w=r → ∃ u, Derives w u ∧ Normal u := by
    intro r
    induction r using Nat.strong_induction_on with
    | h r ih =>
      intro w eq
      by_cases hn : Normal w
      · exact ⟨w,Derives.refl w,hn⟩
      · obtain ⟨v,hv⟩ := by simpa [Normal] using hn
        obtain ⟨u,chain,normal⟩ := ih (rank v) (by rw [← eq]; exact reduces_rank hv) v rfl
        exact ⟨u,Derives.cons hv chain,normal⟩
  exact all (rank w) w rfl

def Binary (d : Digit) : Prop := d=f ∨ d=t
def Ternary (d : Digit) : Prop := d=z ∨ d=o ∨ d=u

theorem ternary_of_not_binary {d : Digit} (h : ¬Binary d) : Ternary d := by
  cases d <;> simp_all [Binary,Ternary]

theorem last_binary_split {w : List Digit} (h : ∃ d∈w, Binary d) :
    ∃ pre d post, w=pre++d::post ∧ Binary d ∧ ∀ e∈post, Ternary e := by
  induction w with
  | nil => simp at h
  | cons c w ih =>
    by_cases ht : ∃ d∈w, Binary d
    · obtain ⟨pre,d,post,eq,bd,tr⟩ := ih ht
      exact ⟨c::pre,d,post,by simp [eq],bd,tr⟩
    · have bc : Binary c := by
        obtain ⟨d,hd,bd⟩ := h
        rcases List.mem_cons.mp hd with eq | member
        · simpa [eq] using bd
        · exact False.elim (ht ⟨d,member,bd⟩)
      refine ⟨[],c,w,rfl,bc,?_⟩
      intro e he
      exact ternary_of_not_binary (fun be => ht ⟨e,he,be⟩)

/-- The exceptional grammar has one precise final obstruction: f1 followed
only by ternary digits.  The prefix is an arbitrary ordinary mixed word. -/
theorem normal_form_suffix {w : List Digit} (normal : Normal w) (ne : w≠[]) :
    ∃ pre post, w=pre++[f,o]++post ∧ ∀ d∈post, Ternary d := by
  have anyBinary : ∃ d∈w, Binary d := by
    by_contra none
    cases w with
    | nil => exact ne rfl
    | cons d w =>
      have td : Ternary d := ternary_of_not_binary (by
        intro bd; exact none ⟨d,by simp,bd⟩)
      rcases td with rfl | rfl | rfl
      · exact normal ⟨_,Reduces.leading_z w⟩
      · exact normal ⟨_,Reduces.leading_o w⟩
      · exact normal ⟨_,Reduces.leading_u w⟩
  obtain ⟨pre,d,post,eq,bd,tr⟩ := last_binary_split anyBinary
  subst w
  cases post with
  | nil =>
    rcases bd with rfl | rfl
    · exact False.elim (normal ⟨_,Reduces.final_f pre⟩)
    · exact False.elim (normal ⟨_,Reduces.final_t pre⟩)
  | cons e post =>
    have te : Ternary e := tr e (by simp)
    have tail : ∀ a∈post, Ternary a := fun a ha => tr a (by simp [ha])
    rcases bd with rfl | rfl <;> rcases te with rfl | rfl | rfl
    · exact False.elim (normal ⟨_,by
        simpa [List.append_assoc] using Reduces.exchange pre post Exchange.fz⟩)
    · exact ⟨pre,post,by simp,tail⟩
    · exact False.elim (normal ⟨_,by
        simpa [List.append_assoc] using Reduces.exchange pre post Exchange.fu⟩)
    · exact False.elim (normal ⟨_,by
        simpa [List.append_assoc] using Reduces.exchange pre post Exchange.tz⟩)
    · exact False.elim (normal ⟨_,by
        simpa [List.append_assoc] using Reduces.exchange pre post Exchange.to1⟩)
    · exact False.elim (normal ⟨_,by
        simpa [List.append_assoc] using Reduces.exchange pre post Exchange.tu⟩)

theorem ternary_eval (w : List Digit) (h : ∀ d∈w, Ternary d) (x : Nat) :
    eval w x = 3^w.length*x+eval w 0 := by
  induction w generalizing x with
  | nil => simp [eval]
  | cons d w ih =>
    have td := h d (by simp)
    have tail : ∀ a∈w, Ternary a := fun a ha => h a (by simp [ha])
    have hx := ih tail (num d x)
    have hz := ih tail (num d 0)
    simp only [eval,List.length_cons,pow_succ]
    rcases td with rfl | rfl | rfl <;>
      simp only [num] at hx hz ⊢ <;> nlinarith only [hx,hz]

theorem ternary_eval_lt (w : List Digit) (h : ∀ d∈w, Ternary d) :
    eval w 0<3^w.length := by
  induction w with
  | nil => simp [eval]
  | cons d w ih =>
    have td := h d (by simp)
    have tail : ∀ a∈w, Ternary a := fun a ha => h a (by simp [ha])
    have small := ih tail
    have hz := ternary_eval w tail (num d 0)
    simp only [eval,List.length_cons,pow_succ]
    rcases td with rfl | rfl | rfl <;>
      simp only [num] at hz ⊢ <;> omega

/-- Every positive ordinary source has a canonical binary representation. -/
theorem representation_exists (n : Nat) (pos : 0<n) : ∃ w, value w=n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases one : n=1
    · exact ⟨[],by simp [value,eval,one]⟩
    · have halfPos : 0<n/2 := by omega
      have halfLt : n/2<n := by omega
      obtain ⟨w,hw⟩ := ih (n/2) halfLt halfPos
      by_cases even : n%2=0
      · refine ⟨w++[f],?_⟩
        simp only [value,eval_append,eval,num] at hw ⊢
        omega
      · refine ⟨w++[t],?_⟩
        simp only [value,eval_append,eval,num] at hw ⊢
        omega

/-- An all-input ordinary reduction.  The terminal alternative is one; the
other alternative retains its complete blocked word and exact finite clock.
The theorem makes no claim that the latter endpoint is smaller than n. -/
theorem ordinary_normal_form (n : Nat) (pos : 0<n) :
    ∃ w k, Normal w ∧ orbit k n=value w ∧
      (w=[] ∨ ∃ pre post q r,
        w=pre++[f,o]++post ∧ (∀ d∈post, Ternary d) ∧
        0<q ∧ r<3^post.length ∧ value w=3^post.length*(6*q+1)+r) := by
  obtain ⟨initial,hi⟩ := representation_exists n pos
  obtain ⟨w,chain,normal⟩ := normalization_exists initial
  obtain ⟨k,hk⟩ := derives_orbit chain
  refine ⟨w,k,normal,by simpa [hi] using hk,?_⟩
  by_cases empty : w=[]
  · exact Or.inl empty
  · obtain ⟨pre,post,eq,tr⟩ := normal_form_suffix normal empty
    refine Or.inr ⟨pre,post,value pre,eval post 0,eq,tr,value_pos pre,
      ternary_eval_lt post tr,?_⟩
    rw [eq]
    simp only [value,eval_append,eval,num]
    rw [ternary_eval post tr (3*(2*eval pre 1)+1)]
    ring

/-- The exact remaining arithmetic obligation for the proposed universal
partner: at least one blocked erasure of every nonterminal normal form has
an ordinary finite common endpoint with the parent. -/
def BlockedErasureCover : Prop :=
  ∀ w, Normal w → w≠[] →
    ∃ pre post a b, w=pre++[f,o]++post ∧
      orbit a (value w)=orbit b (value (pre++[f]++post))

private theorem basin_of_merger {n m : Nat} {a b : Nat}
    (meeting : orbit a n=orbit b m) (known : Basin m) : Basin n := by
  have first : Hits n (orbit a n) := ⟨a,rfl⟩
  have second : Hits m (orbit b m) := ⟨b,rfl⟩
  have endpoint : Basin (orbit a n) := by
    rw [meeting]
    exact (basin_at_hit second).mp known
  exact (basin_at_hit first).mpr endpoint

/-- A single syntactic cover would close the full ordinary theorem.
Normalization may increase ordinary value, but always decreases this rank;
erasure then decreases it again.  No comparison with a later, larger mark
is smuggled into induction on the original source. -/
theorem universal_of_blocked_erasure (cover : BlockedErasureCover) : Universal := by
  have all : ∀ r w, rank w=r → Basin (value w) := by
    intro r
    induction r using Nat.strong_induction_on with
    | h r ih =>
      intro w eq
      by_cases normal : Normal w
      · by_cases empty : w=[]
        · subst w
          exact ⟨0,rfl⟩
        · obtain ⟨pre,post,a,b,shape,meeting⟩ := cover w normal empty
          have smaller := (blocked_erasure_decreases pre post).2
          have basin := ih (rank (pre++[f]++post)) (by simpa only [← shape,eq] using smaller)
            (pre++[f]++post) rfl
          exact basin_of_merger meeting basin
      · obtain ⟨v,hv⟩ := by simpa [Normal] using normal
        have basin := ih (rank v) (by rw [← eq]; exact reduces_rank hv) v rfl
        obtain ⟨k,_,hk⟩ := reduces_orbit hv
        exact (basin_at_hit (show Hits (value w) (value v) from ⟨k,hk⟩)).mpr basin
  intro n pos
  obtain ⟨w,hw⟩ := representation_exists n pos
  simpa [hw] using all (rank w) w rfl

/-- The obligation is explicitly equivalent to Collatz, rather than a
completed theorem inferred from matrix termination alone. -/
theorem blocked_erasure_iff_universal : BlockedErasureCover ↔ Universal := by
  constructor
  · exact universal_of_blocked_erasure
  · intro all w normal ne
    obtain ⟨pre,post,shape,_⟩ := normal_form_suffix normal ne
    obtain ⟨a,ha⟩ := all (value w) (value_pos w)
    obtain ⟨b,hb⟩ := all (value (pre++[f]++post)) (value_pos _)
    exact ⟨pre,post,a,b,shape,by rw [ha,hb]⟩

end CollatzShell.MixedBaseNormalForm
