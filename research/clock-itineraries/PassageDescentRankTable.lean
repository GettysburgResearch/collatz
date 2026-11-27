module

public import TowerFrontierAffine
import all TowerFrontierAffine

public section

namespace Collatz.Itinerary.PassageDescent

open TowerFrontier
set_option autoImplicit false
set_option maxHeartbeats 100000000
set_option maxRecDepth 10000

private def test (h i : Nat) : Bool :=
  let b := 48*i+17
  let l := stride h b 0
  let u := stride (h+2) (3*b) 0
  let D := Nat.gcd (9*3^u.2) 243
  decide ((u.2≤10 ∧ l.1+1=4*u.1 ∧ 12*3^l.2=36*3^u.2 ∧
    81*(3*2^(h+2))≤128*(36*3^u.2) ∧ u.1%D=512%D) →
    h=7 ∧ u.2=3 ∧ 81*b+271=512*u.1)

private def tree (f : Nat → Bool) : Nat → Nat → Bool
  | 0,a => f a
  | n+1,a => tree f n a && tree f n (a+2^n)

private theorem tree_sound (f : Nat → Bool) (n a i : Nat) (ok : tree f n a=true)
    (lo : a≤i) (hi : i<a+2^n) : f i=true := by
  induction n generalizing a with
  | zero =>
    have eq : a=i := by simpa using (show a=i by simp at hi; omega)
    simpa [tree,eq] using ok
  | succ n ih =>
    obtain ⟨l,r⟩ := Bool.and_eq_true_iff.mp ok
    by_cases c : i<a+2^n
    · exact ih a l lo c
    · apply ih (a+2^n) r (by omega)
      rw [Nat.pow_succ] at hi
      omega

private theorem join (f : Nat → Bool) (n a : Nat) (x : tree f n a=true)
    (y : tree f n (a+2^n)=true) : tree f (n+1) a=true := by simp [tree,x,y]

/- Each kernel reduction covers at most 512 canonical residues. The joins
   prove exactly the complete interval at each clock with bounded memory. -/
private theorem block_0_0 : tree (test 0) 0 0=true := by decide +kernel
private theorem block_1_0 : tree (test 1) 0 0=true := by decide +kernel
private theorem block_2_0 : tree (test 2) 0 0=true := by decide +kernel
private theorem block_3_0 : tree (test 3) 1 0=true := by decide +kernel
private theorem block_4_0 : tree (test 4) 2 0=true := by decide +kernel
private theorem block_5_0 : tree (test 5) 3 0=true := by decide +kernel
private theorem block_6_0 : tree (test 6) 4 0=true := by decide +kernel
private theorem block_7_0 : tree (test 7) 5 0=true := by decide +kernel
private theorem block_8_0 : tree (test 8) 6 0=true := by decide +kernel
private theorem block_9_0 : tree (test 9) 7 0=true := by decide +kernel
private theorem block_10_0 : tree (test 10) 8 0=true := by decide +kernel
private theorem block_11_0 : tree (test 11) 9 0=true := by decide +kernel
private theorem block_12_0 : tree (test 12) 9 0=true := by decide +kernel
private theorem block_12_512 : tree (test 12) 9 512=true := by decide +kernel
private theorem level_12 : tree (test 12) 10 0=true :=
  (@join (test 12) 9 0 block_12_0 block_12_512)
private theorem block_13_0 : tree (test 13) 9 0=true := by decide +kernel
private theorem block_13_512 : tree (test 13) 9 512=true := by decide +kernel
private theorem block_13_1024 : tree (test 13) 9 1024=true := by decide +kernel
private theorem block_13_1536 : tree (test 13) 9 1536=true := by decide +kernel
private theorem level_13 : tree (test 13) 11 0=true :=
  (@join (test 13) 10 0 (@join (test 13) 9 0 block_13_0 block_13_512) (@join (test 13) 9 1024 block_13_1024 block_13_1536))
private theorem block_14_0 : tree (test 14) 9 0=true := by decide +kernel
private theorem block_14_512 : tree (test 14) 9 512=true := by decide +kernel
private theorem block_14_1024 : tree (test 14) 9 1024=true := by decide +kernel
private theorem block_14_1536 : tree (test 14) 9 1536=true := by decide +kernel
private theorem block_14_2048 : tree (test 14) 9 2048=true := by decide +kernel
private theorem block_14_2560 : tree (test 14) 9 2560=true := by decide +kernel
private theorem block_14_3072 : tree (test 14) 9 3072=true := by decide +kernel
private theorem block_14_3584 : tree (test 14) 9 3584=true := by decide +kernel
private theorem level_14 : tree (test 14) 12 0=true :=
  (@join (test 14) 11 0 (@join (test 14) 10 0 (@join (test 14) 9 0 block_14_0 block_14_512) (@join (test 14) 9 1024 block_14_1024 block_14_1536)) (@join (test 14) 10 2048 (@join (test 14) 9 2048 block_14_2048 block_14_2560) (@join (test 14) 9 3072 block_14_3072 block_14_3584)))
private theorem block_15_0 : tree (test 15) 9 0=true := by decide +kernel
private theorem block_15_512 : tree (test 15) 9 512=true := by decide +kernel
private theorem block_15_1024 : tree (test 15) 9 1024=true := by decide +kernel
private theorem block_15_1536 : tree (test 15) 9 1536=true := by decide +kernel
private theorem block_15_2048 : tree (test 15) 9 2048=true := by decide +kernel
private theorem block_15_2560 : tree (test 15) 9 2560=true := by decide +kernel
private theorem block_15_3072 : tree (test 15) 9 3072=true := by decide +kernel
private theorem block_15_3584 : tree (test 15) 9 3584=true := by decide +kernel
private theorem block_15_4096 : tree (test 15) 9 4096=true := by decide +kernel
private theorem block_15_4608 : tree (test 15) 9 4608=true := by decide +kernel
private theorem block_15_5120 : tree (test 15) 9 5120=true := by decide +kernel
private theorem block_15_5632 : tree (test 15) 9 5632=true := by decide +kernel
private theorem block_15_6144 : tree (test 15) 9 6144=true := by decide +kernel
private theorem block_15_6656 : tree (test 15) 9 6656=true := by decide +kernel
private theorem block_15_7168 : tree (test 15) 9 7168=true := by decide +kernel
private theorem block_15_7680 : tree (test 15) 9 7680=true := by decide +kernel
private theorem level_15 : tree (test 15) 13 0=true :=
  (@join (test 15) 12 0 (@join (test 15) 11 0 (@join (test 15) 10 0 (@join (test 15) 9 0 block_15_0 block_15_512) (@join (test 15) 9 1024 block_15_1024 block_15_1536)) (@join (test 15) 10 2048 (@join (test 15) 9 2048 block_15_2048 block_15_2560) (@join (test 15) 9 3072 block_15_3072 block_15_3584))) (@join (test 15) 11 4096 (@join (test 15) 10 4096 (@join (test 15) 9 4096 block_15_4096 block_15_4608) (@join (test 15) 9 5120 block_15_5120 block_15_5632)) (@join (test 15) 10 6144 (@join (test 15) 9 6144 block_15_6144 block_15_6656) (@join (test 15) 9 7168 block_15_7168 block_15_7680))))
private theorem block_16_0 : tree (test 16) 9 0=true := by decide +kernel
private theorem block_16_512 : tree (test 16) 9 512=true := by decide +kernel
private theorem block_16_1024 : tree (test 16) 9 1024=true := by decide +kernel
private theorem block_16_1536 : tree (test 16) 9 1536=true := by decide +kernel
private theorem block_16_2048 : tree (test 16) 9 2048=true := by decide +kernel
private theorem block_16_2560 : tree (test 16) 9 2560=true := by decide +kernel
private theorem block_16_3072 : tree (test 16) 9 3072=true := by decide +kernel
private theorem block_16_3584 : tree (test 16) 9 3584=true := by decide +kernel
private theorem block_16_4096 : tree (test 16) 9 4096=true := by decide +kernel
private theorem block_16_4608 : tree (test 16) 9 4608=true := by decide +kernel
private theorem block_16_5120 : tree (test 16) 9 5120=true := by decide +kernel
private theorem block_16_5632 : tree (test 16) 9 5632=true := by decide +kernel
private theorem block_16_6144 : tree (test 16) 9 6144=true := by decide +kernel
private theorem block_16_6656 : tree (test 16) 9 6656=true := by decide +kernel
private theorem block_16_7168 : tree (test 16) 9 7168=true := by decide +kernel
private theorem block_16_7680 : tree (test 16) 9 7680=true := by decide +kernel
private theorem block_16_8192 : tree (test 16) 9 8192=true := by decide +kernel
private theorem block_16_8704 : tree (test 16) 9 8704=true := by decide +kernel
private theorem block_16_9216 : tree (test 16) 9 9216=true := by decide +kernel
private theorem block_16_9728 : tree (test 16) 9 9728=true := by decide +kernel
private theorem block_16_10240 : tree (test 16) 9 10240=true := by decide +kernel
private theorem block_16_10752 : tree (test 16) 9 10752=true := by decide +kernel
private theorem block_16_11264 : tree (test 16) 9 11264=true := by decide +kernel
private theorem block_16_11776 : tree (test 16) 9 11776=true := by decide +kernel
private theorem block_16_12288 : tree (test 16) 9 12288=true := by decide +kernel
private theorem block_16_12800 : tree (test 16) 9 12800=true := by decide +kernel
private theorem block_16_13312 : tree (test 16) 9 13312=true := by decide +kernel
private theorem block_16_13824 : tree (test 16) 9 13824=true := by decide +kernel
private theorem block_16_14336 : tree (test 16) 9 14336=true := by decide +kernel
private theorem block_16_14848 : tree (test 16) 9 14848=true := by decide +kernel
private theorem block_16_15360 : tree (test 16) 9 15360=true := by decide +kernel
private theorem block_16_15872 : tree (test 16) 9 15872=true := by decide +kernel
private theorem level_16 : tree (test 16) 14 0=true :=
  (@join (test 16) 13 0 (@join (test 16) 12 0 (@join (test 16) 11 0 (@join (test 16) 10 0 (@join (test 16) 9 0 block_16_0 block_16_512) (@join (test 16) 9 1024 block_16_1024 block_16_1536)) (@join (test 16) 10 2048 (@join (test 16) 9 2048 block_16_2048 block_16_2560) (@join (test 16) 9 3072 block_16_3072 block_16_3584))) (@join (test 16) 11 4096 (@join (test 16) 10 4096 (@join (test 16) 9 4096 block_16_4096 block_16_4608) (@join (test 16) 9 5120 block_16_5120 block_16_5632)) (@join (test 16) 10 6144 (@join (test 16) 9 6144 block_16_6144 block_16_6656) (@join (test 16) 9 7168 block_16_7168 block_16_7680)))) (@join (test 16) 12 8192 (@join (test 16) 11 8192 (@join (test 16) 10 8192 (@join (test 16) 9 8192 block_16_8192 block_16_8704) (@join (test 16) 9 9216 block_16_9216 block_16_9728)) (@join (test 16) 10 10240 (@join (test 16) 9 10240 block_16_10240 block_16_10752) (@join (test 16) 9 11264 block_16_11264 block_16_11776))) (@join (test 16) 11 12288 (@join (test 16) 10 12288 (@join (test 16) 9 12288 block_16_12288 block_16_12800) (@join (test 16) 9 13312 block_16_13312 block_16_13824)) (@join (test 16) 10 14336 (@join (test 16) 9 14336 block_16_14336 block_16_14848) (@join (test 16) 9 15360 block_16_15360 block_16_15872)))))
private theorem block_17_0 : tree (test 17) 9 0=true := by decide +kernel
private theorem block_17_512 : tree (test 17) 9 512=true := by decide +kernel
private theorem block_17_1024 : tree (test 17) 9 1024=true := by decide +kernel
private theorem block_17_1536 : tree (test 17) 9 1536=true := by decide +kernel
private theorem block_17_2048 : tree (test 17) 9 2048=true := by decide +kernel
private theorem block_17_2560 : tree (test 17) 9 2560=true := by decide +kernel
private theorem block_17_3072 : tree (test 17) 9 3072=true := by decide +kernel
private theorem block_17_3584 : tree (test 17) 9 3584=true := by decide +kernel
private theorem block_17_4096 : tree (test 17) 9 4096=true := by decide +kernel
private theorem block_17_4608 : tree (test 17) 9 4608=true := by decide +kernel
private theorem block_17_5120 : tree (test 17) 9 5120=true := by decide +kernel
private theorem block_17_5632 : tree (test 17) 9 5632=true := by decide +kernel
private theorem block_17_6144 : tree (test 17) 9 6144=true := by decide +kernel
private theorem block_17_6656 : tree (test 17) 9 6656=true := by decide +kernel
private theorem block_17_7168 : tree (test 17) 9 7168=true := by decide +kernel
private theorem block_17_7680 : tree (test 17) 9 7680=true := by decide +kernel
private theorem block_17_8192 : tree (test 17) 9 8192=true := by decide +kernel
private theorem block_17_8704 : tree (test 17) 9 8704=true := by decide +kernel
private theorem block_17_9216 : tree (test 17) 9 9216=true := by decide +kernel
private theorem block_17_9728 : tree (test 17) 9 9728=true := by decide +kernel
private theorem block_17_10240 : tree (test 17) 9 10240=true := by decide +kernel
private theorem block_17_10752 : tree (test 17) 9 10752=true := by decide +kernel
private theorem block_17_11264 : tree (test 17) 9 11264=true := by decide +kernel
private theorem block_17_11776 : tree (test 17) 9 11776=true := by decide +kernel
private theorem block_17_12288 : tree (test 17) 9 12288=true := by decide +kernel
private theorem block_17_12800 : tree (test 17) 9 12800=true := by decide +kernel
private theorem block_17_13312 : tree (test 17) 9 13312=true := by decide +kernel
private theorem block_17_13824 : tree (test 17) 9 13824=true := by decide +kernel
private theorem block_17_14336 : tree (test 17) 9 14336=true := by decide +kernel
private theorem block_17_14848 : tree (test 17) 9 14848=true := by decide +kernel
private theorem block_17_15360 : tree (test 17) 9 15360=true := by decide +kernel
private theorem block_17_15872 : tree (test 17) 9 15872=true := by decide +kernel
private theorem block_17_16384 : tree (test 17) 9 16384=true := by decide +kernel
private theorem block_17_16896 : tree (test 17) 9 16896=true := by decide +kernel
private theorem block_17_17408 : tree (test 17) 9 17408=true := by decide +kernel
private theorem block_17_17920 : tree (test 17) 9 17920=true := by decide +kernel
private theorem block_17_18432 : tree (test 17) 9 18432=true := by decide +kernel
private theorem block_17_18944 : tree (test 17) 9 18944=true := by decide +kernel
private theorem block_17_19456 : tree (test 17) 9 19456=true := by decide +kernel
private theorem block_17_19968 : tree (test 17) 9 19968=true := by decide +kernel
private theorem block_17_20480 : tree (test 17) 9 20480=true := by decide +kernel
private theorem block_17_20992 : tree (test 17) 9 20992=true := by decide +kernel
private theorem block_17_21504 : tree (test 17) 9 21504=true := by decide +kernel
private theorem block_17_22016 : tree (test 17) 9 22016=true := by decide +kernel
private theorem block_17_22528 : tree (test 17) 9 22528=true := by decide +kernel
private theorem block_17_23040 : tree (test 17) 9 23040=true := by decide +kernel
private theorem block_17_23552 : tree (test 17) 9 23552=true := by decide +kernel
private theorem block_17_24064 : tree (test 17) 9 24064=true := by decide +kernel
private theorem block_17_24576 : tree (test 17) 9 24576=true := by decide +kernel
private theorem block_17_25088 : tree (test 17) 9 25088=true := by decide +kernel
private theorem block_17_25600 : tree (test 17) 9 25600=true := by decide +kernel
private theorem block_17_26112 : tree (test 17) 9 26112=true := by decide +kernel
private theorem block_17_26624 : tree (test 17) 9 26624=true := by decide +kernel
private theorem block_17_27136 : tree (test 17) 9 27136=true := by decide +kernel
private theorem block_17_27648 : tree (test 17) 9 27648=true := by decide +kernel
private theorem block_17_28160 : tree (test 17) 9 28160=true := by decide +kernel
private theorem block_17_28672 : tree (test 17) 9 28672=true := by decide +kernel
private theorem block_17_29184 : tree (test 17) 9 29184=true := by decide +kernel
private theorem block_17_29696 : tree (test 17) 9 29696=true := by decide +kernel
private theorem block_17_30208 : tree (test 17) 9 30208=true := by decide +kernel
private theorem block_17_30720 : tree (test 17) 9 30720=true := by decide +kernel
private theorem block_17_31232 : tree (test 17) 9 31232=true := by decide +kernel
private theorem block_17_31744 : tree (test 17) 9 31744=true := by decide +kernel
private theorem block_17_32256 : tree (test 17) 9 32256=true := by decide +kernel
private theorem level_17 : tree (test 17) 15 0=true :=
  (@join (test 17) 14 0 (@join (test 17) 13 0 (@join (test 17) 12 0 (@join (test 17) 11 0 (@join (test 17) 10 0 (@join (test 17) 9 0 block_17_0 block_17_512) (@join (test 17) 9 1024 block_17_1024 block_17_1536)) (@join (test 17) 10 2048 (@join (test 17) 9 2048 block_17_2048 block_17_2560) (@join (test 17) 9 3072 block_17_3072 block_17_3584))) (@join (test 17) 11 4096 (@join (test 17) 10 4096 (@join (test 17) 9 4096 block_17_4096 block_17_4608) (@join (test 17) 9 5120 block_17_5120 block_17_5632)) (@join (test 17) 10 6144 (@join (test 17) 9 6144 block_17_6144 block_17_6656) (@join (test 17) 9 7168 block_17_7168 block_17_7680)))) (@join (test 17) 12 8192 (@join (test 17) 11 8192 (@join (test 17) 10 8192 (@join (test 17) 9 8192 block_17_8192 block_17_8704) (@join (test 17) 9 9216 block_17_9216 block_17_9728)) (@join (test 17) 10 10240 (@join (test 17) 9 10240 block_17_10240 block_17_10752) (@join (test 17) 9 11264 block_17_11264 block_17_11776))) (@join (test 17) 11 12288 (@join (test 17) 10 12288 (@join (test 17) 9 12288 block_17_12288 block_17_12800) (@join (test 17) 9 13312 block_17_13312 block_17_13824)) (@join (test 17) 10 14336 (@join (test 17) 9 14336 block_17_14336 block_17_14848) (@join (test 17) 9 15360 block_17_15360 block_17_15872))))) (@join (test 17) 13 16384 (@join (test 17) 12 16384 (@join (test 17) 11 16384 (@join (test 17) 10 16384 (@join (test 17) 9 16384 block_17_16384 block_17_16896) (@join (test 17) 9 17408 block_17_17408 block_17_17920)) (@join (test 17) 10 18432 (@join (test 17) 9 18432 block_17_18432 block_17_18944) (@join (test 17) 9 19456 block_17_19456 block_17_19968))) (@join (test 17) 11 20480 (@join (test 17) 10 20480 (@join (test 17) 9 20480 block_17_20480 block_17_20992) (@join (test 17) 9 21504 block_17_21504 block_17_22016)) (@join (test 17) 10 22528 (@join (test 17) 9 22528 block_17_22528 block_17_23040) (@join (test 17) 9 23552 block_17_23552 block_17_24064)))) (@join (test 17) 12 24576 (@join (test 17) 11 24576 (@join (test 17) 10 24576 (@join (test 17) 9 24576 block_17_24576 block_17_25088) (@join (test 17) 9 25600 block_17_25600 block_17_26112)) (@join (test 17) 10 26624 (@join (test 17) 9 26624 block_17_26624 block_17_27136) (@join (test 17) 9 27648 block_17_27648 block_17_28160))) (@join (test 17) 11 28672 (@join (test 17) 10 28672 (@join (test 17) 9 28672 block_17_28672 block_17_29184) (@join (test 17) 9 29696 block_17_29696 block_17_30208)) (@join (test 17) 10 30720 (@join (test 17) 9 30720 block_17_30720 block_17_31232) (@join (test 17) 9 31744 block_17_31744 block_17_32256))))))
private theorem block_18_0 : tree (test 18) 9 0=true := by decide +kernel
private theorem block_18_512 : tree (test 18) 9 512=true := by decide +kernel
private theorem block_18_1024 : tree (test 18) 9 1024=true := by decide +kernel
private theorem block_18_1536 : tree (test 18) 9 1536=true := by decide +kernel
private theorem block_18_2048 : tree (test 18) 9 2048=true := by decide +kernel
private theorem block_18_2560 : tree (test 18) 9 2560=true := by decide +kernel
private theorem block_18_3072 : tree (test 18) 9 3072=true := by decide +kernel
private theorem block_18_3584 : tree (test 18) 9 3584=true := by decide +kernel
private theorem block_18_4096 : tree (test 18) 9 4096=true := by decide +kernel
private theorem block_18_4608 : tree (test 18) 9 4608=true := by decide +kernel
private theorem block_18_5120 : tree (test 18) 9 5120=true := by decide +kernel
private theorem block_18_5632 : tree (test 18) 9 5632=true := by decide +kernel
private theorem block_18_6144 : tree (test 18) 9 6144=true := by decide +kernel
private theorem block_18_6656 : tree (test 18) 9 6656=true := by decide +kernel
private theorem block_18_7168 : tree (test 18) 9 7168=true := by decide +kernel
private theorem block_18_7680 : tree (test 18) 9 7680=true := by decide +kernel
private theorem block_18_8192 : tree (test 18) 9 8192=true := by decide +kernel
private theorem block_18_8704 : tree (test 18) 9 8704=true := by decide +kernel
private theorem block_18_9216 : tree (test 18) 9 9216=true := by decide +kernel
private theorem block_18_9728 : tree (test 18) 9 9728=true := by decide +kernel
private theorem block_18_10240 : tree (test 18) 9 10240=true := by decide +kernel
private theorem block_18_10752 : tree (test 18) 9 10752=true := by decide +kernel
private theorem block_18_11264 : tree (test 18) 9 11264=true := by decide +kernel
private theorem block_18_11776 : tree (test 18) 9 11776=true := by decide +kernel
private theorem block_18_12288 : tree (test 18) 9 12288=true := by decide +kernel
private theorem block_18_12800 : tree (test 18) 9 12800=true := by decide +kernel
private theorem block_18_13312 : tree (test 18) 9 13312=true := by decide +kernel
private theorem block_18_13824 : tree (test 18) 9 13824=true := by decide +kernel
private theorem block_18_14336 : tree (test 18) 9 14336=true := by decide +kernel
private theorem block_18_14848 : tree (test 18) 9 14848=true := by decide +kernel
private theorem block_18_15360 : tree (test 18) 9 15360=true := by decide +kernel
private theorem block_18_15872 : tree (test 18) 9 15872=true := by decide +kernel
private theorem block_18_16384 : tree (test 18) 9 16384=true := by decide +kernel
private theorem block_18_16896 : tree (test 18) 9 16896=true := by decide +kernel
private theorem block_18_17408 : tree (test 18) 9 17408=true := by decide +kernel
private theorem block_18_17920 : tree (test 18) 9 17920=true := by decide +kernel
private theorem block_18_18432 : tree (test 18) 9 18432=true := by decide +kernel
private theorem block_18_18944 : tree (test 18) 9 18944=true := by decide +kernel
private theorem block_18_19456 : tree (test 18) 9 19456=true := by decide +kernel
private theorem block_18_19968 : tree (test 18) 9 19968=true := by decide +kernel
private theorem block_18_20480 : tree (test 18) 9 20480=true := by decide +kernel
private theorem block_18_20992 : tree (test 18) 9 20992=true := by decide +kernel
private theorem block_18_21504 : tree (test 18) 9 21504=true := by decide +kernel
private theorem block_18_22016 : tree (test 18) 9 22016=true := by decide +kernel
private theorem block_18_22528 : tree (test 18) 9 22528=true := by decide +kernel
private theorem block_18_23040 : tree (test 18) 9 23040=true := by decide +kernel
private theorem block_18_23552 : tree (test 18) 9 23552=true := by decide +kernel
private theorem block_18_24064 : tree (test 18) 9 24064=true := by decide +kernel
private theorem block_18_24576 : tree (test 18) 9 24576=true := by decide +kernel
private theorem block_18_25088 : tree (test 18) 9 25088=true := by decide +kernel
private theorem block_18_25600 : tree (test 18) 9 25600=true := by decide +kernel
private theorem block_18_26112 : tree (test 18) 9 26112=true := by decide +kernel
private theorem block_18_26624 : tree (test 18) 9 26624=true := by decide +kernel
private theorem block_18_27136 : tree (test 18) 9 27136=true := by decide +kernel
private theorem block_18_27648 : tree (test 18) 9 27648=true := by decide +kernel
private theorem block_18_28160 : tree (test 18) 9 28160=true := by decide +kernel
private theorem block_18_28672 : tree (test 18) 9 28672=true := by decide +kernel
private theorem block_18_29184 : tree (test 18) 9 29184=true := by decide +kernel
private theorem block_18_29696 : tree (test 18) 9 29696=true := by decide +kernel
private theorem block_18_30208 : tree (test 18) 9 30208=true := by decide +kernel
private theorem block_18_30720 : tree (test 18) 9 30720=true := by decide +kernel
private theorem block_18_31232 : tree (test 18) 9 31232=true := by decide +kernel
private theorem block_18_31744 : tree (test 18) 9 31744=true := by decide +kernel
private theorem block_18_32256 : tree (test 18) 9 32256=true := by decide +kernel
private theorem block_18_32768 : tree (test 18) 9 32768=true := by decide +kernel
private theorem block_18_33280 : tree (test 18) 9 33280=true := by decide +kernel
private theorem block_18_33792 : tree (test 18) 9 33792=true := by decide +kernel
private theorem block_18_34304 : tree (test 18) 9 34304=true := by decide +kernel
private theorem block_18_34816 : tree (test 18) 9 34816=true := by decide +kernel
private theorem block_18_35328 : tree (test 18) 9 35328=true := by decide +kernel
private theorem block_18_35840 : tree (test 18) 9 35840=true := by decide +kernel
private theorem block_18_36352 : tree (test 18) 9 36352=true := by decide +kernel
private theorem block_18_36864 : tree (test 18) 9 36864=true := by decide +kernel
private theorem block_18_37376 : tree (test 18) 9 37376=true := by decide +kernel
private theorem block_18_37888 : tree (test 18) 9 37888=true := by decide +kernel
private theorem block_18_38400 : tree (test 18) 9 38400=true := by decide +kernel
private theorem block_18_38912 : tree (test 18) 9 38912=true := by decide +kernel
private theorem block_18_39424 : tree (test 18) 9 39424=true := by decide +kernel
private theorem block_18_39936 : tree (test 18) 9 39936=true := by decide +kernel
private theorem block_18_40448 : tree (test 18) 9 40448=true := by decide +kernel
private theorem block_18_40960 : tree (test 18) 9 40960=true := by decide +kernel
private theorem block_18_41472 : tree (test 18) 9 41472=true := by decide +kernel
private theorem block_18_41984 : tree (test 18) 9 41984=true := by decide +kernel
private theorem block_18_42496 : tree (test 18) 9 42496=true := by decide +kernel
private theorem block_18_43008 : tree (test 18) 9 43008=true := by decide +kernel
private theorem block_18_43520 : tree (test 18) 9 43520=true := by decide +kernel
private theorem block_18_44032 : tree (test 18) 9 44032=true := by decide +kernel
private theorem block_18_44544 : tree (test 18) 9 44544=true := by decide +kernel
private theorem block_18_45056 : tree (test 18) 9 45056=true := by decide +kernel
private theorem block_18_45568 : tree (test 18) 9 45568=true := by decide +kernel
private theorem block_18_46080 : tree (test 18) 9 46080=true := by decide +kernel
private theorem block_18_46592 : tree (test 18) 9 46592=true := by decide +kernel
private theorem block_18_47104 : tree (test 18) 9 47104=true := by decide +kernel
private theorem block_18_47616 : tree (test 18) 9 47616=true := by decide +kernel
private theorem block_18_48128 : tree (test 18) 9 48128=true := by decide +kernel
private theorem block_18_48640 : tree (test 18) 9 48640=true := by decide +kernel
private theorem block_18_49152 : tree (test 18) 9 49152=true := by decide +kernel
private theorem block_18_49664 : tree (test 18) 9 49664=true := by decide +kernel
private theorem block_18_50176 : tree (test 18) 9 50176=true := by decide +kernel
private theorem block_18_50688 : tree (test 18) 9 50688=true := by decide +kernel
private theorem block_18_51200 : tree (test 18) 9 51200=true := by decide +kernel
private theorem block_18_51712 : tree (test 18) 9 51712=true := by decide +kernel
private theorem block_18_52224 : tree (test 18) 9 52224=true := by decide +kernel
private theorem block_18_52736 : tree (test 18) 9 52736=true := by decide +kernel
private theorem block_18_53248 : tree (test 18) 9 53248=true := by decide +kernel
private theorem block_18_53760 : tree (test 18) 9 53760=true := by decide +kernel
private theorem block_18_54272 : tree (test 18) 9 54272=true := by decide +kernel
private theorem block_18_54784 : tree (test 18) 9 54784=true := by decide +kernel
private theorem block_18_55296 : tree (test 18) 9 55296=true := by decide +kernel
private theorem block_18_55808 : tree (test 18) 9 55808=true := by decide +kernel
private theorem block_18_56320 : tree (test 18) 9 56320=true := by decide +kernel
private theorem block_18_56832 : tree (test 18) 9 56832=true := by decide +kernel
private theorem block_18_57344 : tree (test 18) 9 57344=true := by decide +kernel
private theorem block_18_57856 : tree (test 18) 9 57856=true := by decide +kernel
private theorem block_18_58368 : tree (test 18) 9 58368=true := by decide +kernel
private theorem block_18_58880 : tree (test 18) 9 58880=true := by decide +kernel
private theorem block_18_59392 : tree (test 18) 9 59392=true := by decide +kernel
private theorem block_18_59904 : tree (test 18) 9 59904=true := by decide +kernel
private theorem block_18_60416 : tree (test 18) 9 60416=true := by decide +kernel
private theorem block_18_60928 : tree (test 18) 9 60928=true := by decide +kernel
private theorem block_18_61440 : tree (test 18) 9 61440=true := by decide +kernel
private theorem block_18_61952 : tree (test 18) 9 61952=true := by decide +kernel
private theorem block_18_62464 : tree (test 18) 9 62464=true := by decide +kernel
private theorem block_18_62976 : tree (test 18) 9 62976=true := by decide +kernel
private theorem block_18_63488 : tree (test 18) 9 63488=true := by decide +kernel
private theorem block_18_64000 : tree (test 18) 9 64000=true := by decide +kernel
private theorem block_18_64512 : tree (test 18) 9 64512=true := by decide +kernel
private theorem block_18_65024 : tree (test 18) 9 65024=true := by decide +kernel
private theorem level_18 : tree (test 18) 16 0=true :=
  (@join (test 18) 15 0 (@join (test 18) 14 0 (@join (test 18) 13 0 (@join (test 18) 12 0 (@join (test 18) 11 0 (@join (test 18) 10 0 (@join (test 18) 9 0 block_18_0 block_18_512) (@join (test 18) 9 1024 block_18_1024 block_18_1536)) (@join (test 18) 10 2048 (@join (test 18) 9 2048 block_18_2048 block_18_2560) (@join (test 18) 9 3072 block_18_3072 block_18_3584))) (@join (test 18) 11 4096 (@join (test 18) 10 4096 (@join (test 18) 9 4096 block_18_4096 block_18_4608) (@join (test 18) 9 5120 block_18_5120 block_18_5632)) (@join (test 18) 10 6144 (@join (test 18) 9 6144 block_18_6144 block_18_6656) (@join (test 18) 9 7168 block_18_7168 block_18_7680)))) (@join (test 18) 12 8192 (@join (test 18) 11 8192 (@join (test 18) 10 8192 (@join (test 18) 9 8192 block_18_8192 block_18_8704) (@join (test 18) 9 9216 block_18_9216 block_18_9728)) (@join (test 18) 10 10240 (@join (test 18) 9 10240 block_18_10240 block_18_10752) (@join (test 18) 9 11264 block_18_11264 block_18_11776))) (@join (test 18) 11 12288 (@join (test 18) 10 12288 (@join (test 18) 9 12288 block_18_12288 block_18_12800) (@join (test 18) 9 13312 block_18_13312 block_18_13824)) (@join (test 18) 10 14336 (@join (test 18) 9 14336 block_18_14336 block_18_14848) (@join (test 18) 9 15360 block_18_15360 block_18_15872))))) (@join (test 18) 13 16384 (@join (test 18) 12 16384 (@join (test 18) 11 16384 (@join (test 18) 10 16384 (@join (test 18) 9 16384 block_18_16384 block_18_16896) (@join (test 18) 9 17408 block_18_17408 block_18_17920)) (@join (test 18) 10 18432 (@join (test 18) 9 18432 block_18_18432 block_18_18944) (@join (test 18) 9 19456 block_18_19456 block_18_19968))) (@join (test 18) 11 20480 (@join (test 18) 10 20480 (@join (test 18) 9 20480 block_18_20480 block_18_20992) (@join (test 18) 9 21504 block_18_21504 block_18_22016)) (@join (test 18) 10 22528 (@join (test 18) 9 22528 block_18_22528 block_18_23040) (@join (test 18) 9 23552 block_18_23552 block_18_24064)))) (@join (test 18) 12 24576 (@join (test 18) 11 24576 (@join (test 18) 10 24576 (@join (test 18) 9 24576 block_18_24576 block_18_25088) (@join (test 18) 9 25600 block_18_25600 block_18_26112)) (@join (test 18) 10 26624 (@join (test 18) 9 26624 block_18_26624 block_18_27136) (@join (test 18) 9 27648 block_18_27648 block_18_28160))) (@join (test 18) 11 28672 (@join (test 18) 10 28672 (@join (test 18) 9 28672 block_18_28672 block_18_29184) (@join (test 18) 9 29696 block_18_29696 block_18_30208)) (@join (test 18) 10 30720 (@join (test 18) 9 30720 block_18_30720 block_18_31232) (@join (test 18) 9 31744 block_18_31744 block_18_32256)))))) (@join (test 18) 14 32768 (@join (test 18) 13 32768 (@join (test 18) 12 32768 (@join (test 18) 11 32768 (@join (test 18) 10 32768 (@join (test 18) 9 32768 block_18_32768 block_18_33280) (@join (test 18) 9 33792 block_18_33792 block_18_34304)) (@join (test 18) 10 34816 (@join (test 18) 9 34816 block_18_34816 block_18_35328) (@join (test 18) 9 35840 block_18_35840 block_18_36352))) (@join (test 18) 11 36864 (@join (test 18) 10 36864 (@join (test 18) 9 36864 block_18_36864 block_18_37376) (@join (test 18) 9 37888 block_18_37888 block_18_38400)) (@join (test 18) 10 38912 (@join (test 18) 9 38912 block_18_38912 block_18_39424) (@join (test 18) 9 39936 block_18_39936 block_18_40448)))) (@join (test 18) 12 40960 (@join (test 18) 11 40960 (@join (test 18) 10 40960 (@join (test 18) 9 40960 block_18_40960 block_18_41472) (@join (test 18) 9 41984 block_18_41984 block_18_42496)) (@join (test 18) 10 43008 (@join (test 18) 9 43008 block_18_43008 block_18_43520) (@join (test 18) 9 44032 block_18_44032 block_18_44544))) (@join (test 18) 11 45056 (@join (test 18) 10 45056 (@join (test 18) 9 45056 block_18_45056 block_18_45568) (@join (test 18) 9 46080 block_18_46080 block_18_46592)) (@join (test 18) 10 47104 (@join (test 18) 9 47104 block_18_47104 block_18_47616) (@join (test 18) 9 48128 block_18_48128 block_18_48640))))) (@join (test 18) 13 49152 (@join (test 18) 12 49152 (@join (test 18) 11 49152 (@join (test 18) 10 49152 (@join (test 18) 9 49152 block_18_49152 block_18_49664) (@join (test 18) 9 50176 block_18_50176 block_18_50688)) (@join (test 18) 10 51200 (@join (test 18) 9 51200 block_18_51200 block_18_51712) (@join (test 18) 9 52224 block_18_52224 block_18_52736))) (@join (test 18) 11 53248 (@join (test 18) 10 53248 (@join (test 18) 9 53248 block_18_53248 block_18_53760) (@join (test 18) 9 54272 block_18_54272 block_18_54784)) (@join (test 18) 10 55296 (@join (test 18) 9 55296 block_18_55296 block_18_55808) (@join (test 18) 9 56320 block_18_56320 block_18_56832)))) (@join (test 18) 12 57344 (@join (test 18) 11 57344 (@join (test 18) 10 57344 (@join (test 18) 9 57344 block_18_57344 block_18_57856) (@join (test 18) 9 58368 block_18_58368 block_18_58880)) (@join (test 18) 10 59392 (@join (test 18) 9 59392 block_18_59392 block_18_59904) (@join (test 18) 9 60416 block_18_60416 block_18_60928))) (@join (test 18) 11 61440 (@join (test 18) 10 61440 (@join (test 18) 9 61440 block_18_61440 block_18_61952) (@join (test 18) 9 62464 block_18_62464 block_18_62976)) (@join (test 18) 10 63488 (@join (test 18) 9 63488 block_18_63488 block_18_64000) (@join (test 18) 9 64512 block_18_64512 block_18_65024)))))))

private theorem table : ∀ h : Fin 19, tree (test h.val) (h.val-2) 0=true
  | ⟨0,_⟩ => block_0_0
  | ⟨1,_⟩ => block_1_0
  | ⟨2,_⟩ => block_2_0
  | ⟨3,_⟩ => block_3_0
  | ⟨4,_⟩ => block_4_0
  | ⟨5,_⟩ => block_5_0
  | ⟨6,_⟩ => block_6_0
  | ⟨7,_⟩ => block_7_0
  | ⟨8,_⟩ => block_8_0
  | ⟨9,_⟩ => block_9_0
  | ⟨10,_⟩ => block_10_0
  | ⟨11,_⟩ => block_11_0
  | ⟨12,_⟩ => level_12
  | ⟨13,_⟩ => level_13
  | ⟨14,_⟩ => level_14
  | ⟨15,_⟩ => level_15
  | ⟨16,_⟩ => level_16
  | ⟨17,_⟩ => level_17
  | ⟨18,_⟩ => level_18
  | ⟨n+19,p⟩ => by omega

/-- Exhaustion of the bounded synchronous low residues. -/
theorem rank_table {h i : Nat} (hh : h≤18) (hi : i<2^(h-2)) :
    let b := 48*i+17
    let l := track h b 0
    let u := track (h+2) (3*b) 0
    let D := Nat.gcd (9*3^u.2) 243
    (u.2≤10 ∧ l.1+1=4*u.1 ∧ 12*3^l.2=36*3^u.2 ∧
      81*(3*2^(h+2))≤128*(36*3^u.2) ∧ u.1%D=512%D) →
      h=7 ∧ u.2=3 ∧ 81*b+271=512*u.1 := by
  have c := tree_sound (test h) (h-2) 0 i (table ⟨h,by omega⟩) (Nat.zero_le _) (by simpa using hi)
  unfold test at c
  simp only [stride_eq] at c
  exact of_decide_eq_true c

end Collatz.Itinerary.PassageDescent
