import Init

set_option maxRecDepth 10000
set_option exponentiation.threshold 1024

namespace CollatzResearch.UpDownCounterexample

/-- Vasilyev's unrestricted upward and downward maps on positive inputs. -/
def up (x : Nat) : Nat := (3 * x + 1) / 2
def down (x : Nat) : Nat := (x + 1) / 2

def edges (vertices : List Nat) : List (Nat × Nat) :=
  vertices.zip (vertices.drop 1 ++ vertices.take 1)

def upCount (vertices : List Nat) : Nat :=
  ((edges vertices).filter fun e => e.2 == up e.1).length

/-- The wraparound edge is included. Finite distinctness makes the branch
choices consistent with one subset of the positive integers. -/
def SimpleCycle (vertices : List Nat) : Prop :=
  vertices ≠ [] ∧ vertices.Nodup ∧ vertices.all (fun x => 0 < x) = true ∧
  (edges vertices).all (fun e => e.2 == up e.1 || e.2 == down e.1) = true

instance (vertices : List Nat) : Decidable (SimpleCycle vertices) := by
  unfold SimpleCycle
  infer_instance

def witness : List Nat := [
  4, 6, 9, 5, 8, 12, 18, 27, 14, 21, 11, 17, 26, 39, 20, 30, 45,
  68, 102, 153, 230, 115, 173, 260, 390, 195, 293, 440, 660, 330, 165, 83, 42, 63,
  32, 48, 72, 108, 162, 243, 122, 183, 275, 413, 620, 930, 465, 698, 349, 524, 262,
  393, 590, 885, 443, 665, 998, 499, 250, 375, 563, 845, 423, 635, 953, 477, 716, 358,
  537, 806, 403, 605, 908, 454, 681, 341, 171, 257, 386, 579, 290, 145, 73, 37, 19,
  10, 15, 23, 35, 53, 80, 120, 180, 90, 135, 203, 305, 458, 229, 344, 516, 774,
  387, 581, 872, 436, 654, 327, 164, 246, 369, 185, 278, 417, 626, 939, 470, 235, 353,
  530, 265, 398, 597, 299, 449, 674, 337, 506, 253, 380, 570, 285, 428, 642, 963, 482,
  723, 362, 543, 272, 408, 612, 918, 459, 689, 345, 518, 777, 389, 584, 876, 438, 657,
  986, 493, 247, 371, 557, 836, 418, 209, 314, 157, 236, 354, 531, 266, 399, 599, 300,
  150, 225, 338, 507, 254, 381, 572, 858, 429, 644, 966, 483, 725, 363, 545, 273, 137,
  69, 104, 156, 234, 351, 527, 791, 396, 594, 891, 446, 669, 335, 503, 252, 378, 567,
  284, 142, 213, 107, 161, 242, 121, 61, 31, 16, 24, 36, 54, 81, 41, 62, 93,
  140, 210, 315, 158, 237, 356, 534, 267, 401, 602, 903, 452, 678, 339, 509, 764, 382,
  191, 287, 431, 647, 971, 486, 729, 365, 548, 274, 411, 206, 309, 155, 78, 117, 59,
  89, 134, 201, 302, 453, 680, 340, 170, 85, 43, 65, 98, 147, 221, 111, 167, 251,
  377, 566, 849, 425, 638, 319, 479, 240, 360, 540, 810, 405, 608, 912, 456, 228, 342,
  513, 770, 385, 193, 97, 49, 25, 13, 7]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 5000000 in
theorem witness_simple : SimpleCycle witness := by decide

theorem witness_length : witness.length = 298 := by decide

set_option maxRecDepth 10000 in
set_option maxHeartbeats 5000000 in
theorem witness_upCount : upCount witness = 187 := by decide

theorem ratio_exceeds_three : 3 ^ (187 + 1) < (2 ^ 298 : Nat) := by decide

theorem exists_above_three :
    ∃ v : List Nat, SimpleCycle v ∧ 3 ^ (upCount v + 1) < 2 ^ v.length := by
  refine ⟨witness, witness_simple, ?_⟩
  rw [witness_length, witness_upCount]
  exact ratio_exceeds_three

end CollatzResearch.UpDownCounterexample
