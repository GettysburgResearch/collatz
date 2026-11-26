import WallBank

namespace WallBank
open WallRefinement WallPeriodic

/-! Exact finite high-bit cover for new 1011 runs. Each literal leaf contains the left and right block counts. -/

private def row0 : Certificate :=
  (.branch (.branch (.branch (.pair 73 41) (.pair 37 21)) (.branch (.pair 19 11) (.pair 55 31))) (.branch (.branch (.pair 46 26) (.pair 10 6)) (.branch (.pair 64 36) (.pair 28 16))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row0_valid : valid 81 row0 4 0=true := by decide

private def row1 : Certificate :=
  (.branch (.branch (.branch (.branch (.branch (.branch (.pair 71 40) (.branch (.pair 26 16) (.pair 61 36))) (.pair 62 36)) (.branch (.branch (.branch (.pair 25 16) (.branch (.pair 61 35) (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.pair 77 43) (.pair 47 27)) (.branch (.branch (.pair 7 5) (.pair 58 33)) (.branch (.branch (.pair 7 5) (.pair 77 43)) (.branch (.pair 17 11) (.branch (.pair 19 13) (.pair 7 5)))))) (.pair 35 19)) (.branch (.branch (.branch (.pair 1 2) (.branch (.pair 35 19) (.branch (.pair 34 20) (.pair 16 13)))) (.branch (.pair 35 19) (.branch (.branch (.pair 58 32) (.branch (.branch (.pair 1 2) (.pair 47 27)) (.pair 58 33))) (.branch (.branch (.branch (.branch (.pair 4 3) (.pair 58 33)) (.branch (.pair 7 5) (.pair 22 14))) (.pair 58 32)) (.pair 1 2))))) (.branch (.pair 64 37) (.pair 35 19)))) (.pair 2 2)) (.pair 20 13)) (.branch (.branch (.pair 20 13) (.branch (.pair 44 25) (.pair 34 20))) (.branch (.branch (.branch (.branch (.branch (.branch (.pair 34 20) (.branch (.pair 16 10) (.branch (.branch (.branch (.pair 44 26) (.branch (.pair 70 40) (.branch (.pair 13 8) (.pair 0 0)))) (.pair 55 33)) (.branch (.pair 44 26) (.branch (.pair 13 8) (.pair 2 2)))))) (.branch (.pair 16 10) (.branch (.pair 7 6) (.pair 34 20)))) (.pair 62 35)) (.pair 25 16)) (.pair 20 13)) (.pair 35 19)))))) (.pair 35 20)) (.pair 26 16))) (.branch (.branch (.pair 0 0) (.branch (.pair 53 30) (.branch (.pair 43 26) (.pair 8 6)))) (.branch (.pair 8 6) (.pair 80 46)))) (.branch (.branch (.branch (.branch (.branch (.branch (.pair 52 30) (.branch (.pair 79 45) (.branch (.branch (.pair 26 14) (.branch (.pair 11 8) (.branch (.pair 16 11) (.branch (.branch (.branch (.pair 7 5) (.branch (.branch (.branch (.pair 2 2) (.pair 0 0)) (.branch (.branch (.pair 17 10) (.pair 2 2)) (.pair 34 20))) (.pair 25 15))) (.branch (.branch (.pair 7 5) (.pair 80 46)) (.pair 25 15))) (.pair 53 30))))) (.branch (.pair 11 8) (.pair 80 45))))) (.pair 16 11)) (.pair 26 15)) (.pair 17 11)) (.branch (.pair 53 31) (.branch (.branch (.pair 52 31) (.pair 17 11)) (.pair 62 35)))) (.branch (.branch (.pair 0 1) (.pair 71 41)) (.branch (.branch (.pair 44 25) (.branch (.pair 34 21) (.pair 0 1))) (.pair 35 21))))) (.branch (.branch (.branch (.branch (.branch (.pair 56 32) (.pair 73 42)) (.pair 20 12)) (.pair 0 0)) (.branch (.branch (.pair 2 2) (.pair 74 42)) (.branch (.pair 0 0) (.pair 38 22)))) (.branch (.pair 0 0) (.branch (.branch (.pair 29 17) (.branch (.branch (.branch (.pair 14 9) (.pair 47 27)) (.pair 10 7)) (.pair 65 37))) (.branch (.branch (.branch (.pair 12 6) (.branch (.pair 29 17) (.pair 38 22))) (.branch (.branch (.branch (.branch (.branch (.pair 51 28) (.pair 64 37)) (.pair 10 7)) (.pair 39 22)) (.pair 50 29)) (.pair 29 17))) (.pair 65 37))))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row1_valid : valid 81 row1 4 1=true := by decide

private def row2 : Certificate :=
  (.pair 0 0)

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row2_valid : valid 81 row2 4 2=true := by decide

private def row3 : Certificate :=
  (.branch (.branch (.branch (.branch (.branch (.pair 6 4) (.pair 24 14)) (.branch (.pair 15 9) (.pair 33 19))) (.branch (.pair 6 4) (.pair 15 9))) (.branch (.branch (.pair 10 6) (.pair 19 11)) (.branch (.pair 0 0) (.branch (.pair 37 21) (.pair 19 11))))) (.branch (.branch (.pair 1 1) (.branch (.branch (.branch (.branch (.branch (.branch (.pair 16 8) (.branch (.pair 33 19) (.pair 42 24))) (.branch (.branch (.branch (.branch (.branch (.pair 68 39) (.pair 55 30)) (.pair 14 9)) (.pair 43 24)) (.pair 54 31)) (.pair 33 19))) (.pair 69 39)) (.branch (.branch (.branch (.pair 14 9) (.branch (.pair 18 11) (.pair 51 29))) (.pair 69 39)) (.pair 33 19))) (.branch (.branch (.pair 51 29) (.branch (.branch (.pair 69 39) (.branch (.pair 15 9) (.pair 24 14))) (.branch (.branch (.pair 69 39) (.pair 36 21)) (.pair 15 9)))) (.branch (.pair 15 9) (.branch (.pair 68 39) (.pair 51 29))))) (.branch (.branch (.branch (.branch (.pair 60 34) (.pair 77 44)) (.pair 24 14)) (.branch (.pair 60 34) (.branch (.branch (.branch (.pair 33 19) (.pair 24 14)) (.pair 7 3)) (.branch (.pair 24 14) (.branch (.pair 78 44) (.pair 45 26)))))) (.branch (.branch (.pair 6 4) (.pair 78 44)) (.branch (.branch (.branch (.pair 6 4) (.branch (.pair 60 34) (.pair 27 16))) (.pair 78 44)) (.pair 42 24)))))) (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.pair 54 31) (.branch (.branch (.pair 2 2) (.pair 68 39)) (.branch (.pair 44 25) (.pair 22 13)))) (.pair 30 18)) (.branch (.branch (.pair 2 2) (.branch (.branch (.branch (.branch (.branch (.pair 60 34) (.pair 54 31)) (.pair 21 13)) (.pair 66 38)) (.branch (.pair 21 13) (.branch (.pair 17 10) (.pair 70 39)))) (.pair 27 16))) (.branch (.pair 30 18) (.branch (.branch (.pair 2 2) (.pair 52 29)) (.branch (.pair 12 8) (.pair 66 38)))))) (.branch (.branch (.branch (.branch (.pair 63 36) (.branch (.pair 6 4) (.pair 8 5))) (.pair 18 11)) (.branch (.branch (.pair 18 11) (.branch (.branch (.pair 29 17) (.pair 30 17)) (.pair 38 22))) (.pair 32 19))) (.branch (.pair 66 38) (.branch (.branch (.pair 58 33) (.branch (.pair 30 18) (.pair 4 3))) (.branch (.branch (.pair 35 20) (.pair 32 19)) (.pair 6 4)))))) (.pair 1 1)) (.branch (.branch (.pair 1 1) (.branch (.branch (.branch (.branch (.pair 9 6) (.branch (.pair 29 17) (.pair 79 44))) (.pair 23 14)) (.branch (.pair 9 6) (.branch (.branch (.branch (.branch (.pair 0 0) (.branch (.pair 20 12) (.pair 21 12))) (.pair 23 14)) (.pair 17 10)) (.pair 54 31)))) (.branch (.branch (.pair 81 46) (.pair 0 0)) (.pair 57 33)))) (.branch (.branch (.branch (.branch (.branch (.pair 72 41) (.pair 0 0)) (.pair 27 16)) (.pair 3 3)) (.pair 1 1)) (.branch (.pair 0 0) (.branch (.pair 39 23) (.branch (.pair 1 1) (.pair 63 36))))))) (.branch (.branch (.branch (.pair 25 14) (.pair 61 34)) (.branch (.pair 7 4) (.pair 43 24))) (.pair 1 1)))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row3_valid : valid 81 row3 4 3=true := by decide

private def row4 : Certificate :=
  (.pair 0 0)

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row4_valid : valid 81 row4 4 4=true := by decide

private def row5 : Certificate :=
  (.branch (.pair 0 0) (.branch (.branch (.pair 6 4) (.pair 24 14)) (.branch (.pair 15 9) (.pair 33 19))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row5_valid : valid 81 row5 4 5=true := by decide

private def row6 : Certificate :=
  (.branch (.branch (.pair 27 16) (.pair 9 6)) (.pair 0 0))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row6_valid : valid 81 row6 4 6=true := by decide

private def row7 : Certificate :=
  (.branch (.branch (.branch (.branch (.pair 22 13) (.pair 4 3)) (.branch (.pair 13 8) (.pair 31 18))) (.branch (.pair 13 8) (.pair 4 3))) (.branch (.branch (.branch (.pair 8 5) (.pair 26 15)) (.branch (.pair 35 20) (.pair 17 10))) (.branch (.pair 8 5) (.pair 17 10))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row7_valid : valid 81 row7 4 7=true := by decide

private def row8 : Certificate :=
  (.branch (.branch (.branch (.branch (.branch (.branch (.pair 36 21) (.branch (.pair 21 13) (.branch (.branch (.branch (.pair 11 7) (.pair 64 36)) (.pair 15 10)) (.branch (.pair 60 35) (.branch (.pair 15 10) (.branch (.pair 48 28) (.pair 54 31))))))) (.branch (.branch (.pair 0 1) (.branch (.pair 60 35) (.pair 6 5))) (.pair 24 15))) (.branch (.branch (.branch (.branch (.pair 16 10) (.pair 38 22)) (.branch (.pair 62 36) (.branch (.branch (.pair 36 21) (.pair 47 28)) (.pair 16 10)))) (.pair 48 28)) (.pair 24 15))) (.branch (.branch (.branch (.pair 26 16) (.branch (.pair 12 8) (.branch (.pair 32 19) (.branch (.pair 23 14) (.pair 24 14))))) (.branch (.pair 12 8) (.branch (.branch (.pair 2 2) (.pair 20 12)) (.pair 57 33)))) (.branch (.pair 60 35) (.branch (.branch (.branch (.pair 26 16) (.pair 29 17)) (.pair 24 15)) (.branch (.pair 52 30) (.branch (.pair 44 26) (.pair 24 15))))))) (.branch (.branch (.branch (.pair 42 25) (.branch (.branch (.pair 6 5) (.branch (.pair 8 6) (.pair 11 7))) (.pair 66 38))) (.branch (.branch (.pair 14 9) (.branch (.pair 39 23) (.branch (.branch (.pair 8 6) (.branch (.branch (.pair 6 4) (.pair 5 4)) (.pair 33 20))) (.pair 2 2)))) (.branch (.branch (.branch (.pair 64 36) (.pair 14 9)) (.branch (.pair 5 4) (.pair 6 4))) (.pair 8 6)))) (.branch (.branch (.branch (.branch (.branch (.pair 42 25) (.pair 16 10)) (.pair 70 40)) (.pair 6 5)) (.pair 78 45)) (.branch (.pair 6 5) (.branch (.pair 30 18) (.branch (.branch (.pair 20 12) (.pair 18 11)) (.pair 75 43))))))) (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.pair 41 24) (.branch (.pair 32 19) (.pair 33 19))) (.pair 21 13)) (.pair 35 21)) (.branch (.branch (.pair 66 38) (.branch (.pair 9 6) (.pair 11 7))) (.pair 21 13))) (.branch (.pair 69 40) (.branch (.branch (.branch (.pair 33 20) (.pair 7 5)) (.pair 61 35)) (.branch (.branch (.pair 35 21) (.pair 38 22)) (.pair 9 6))))) (.branch (.branch (.branch (.pair 57 33) (.branch (.branch (.pair 2 2) (.pair 5 4)) (.branch (.pair 47 27) (.pair 25 15)))) (.pair 33 20)) (.branch (.branch (.pair 33 20) (.branch (.branch (.pair 15 10) (.pair 69 40)) (.pair 0 0))) (.branch (.pair 0 0) (.branch (.branch (.branch (.pair 69 40) (.branch (.branch (.pair 57 33) (.pair 2 2)) (.pair 24 15))) (.branch (.pair 24 15) (.branch (.pair 20 12) (.pair 73 41)))) (.pair 30 18)))))) (.branch (.branch (.branch (.branch (.branch (.pair 79 45) (.branch (.pair 25 15) (.pair 51 30))) (.pair 15 10)) (.branch (.branch (.pair 12 8) (.branch (.branch (.branch (.branch (.pair 39 23) (.pair 45 26)) (.pair 6 5)) (.pair 51 30)) (.branch (.branch (.pair 2 2) (.pair 55 31)) (.pair 6 5)))) (.pair 27 16))) (.pair 0 1)) (.branch (.branch (.pair 0 1) (.branch (.branch (.branch (.pair 73 41) (.pair 23 14)) (.pair 3 3)) (.pair 17 11))) (.branch (.branch (.branch (.pair 15 10) (.branch (.pair 20 12) (.pair 17 11))) (.pair 0 1)) (.pair 51 30))))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row8_valid : valid 81 row8 4 8=true := by decide

private def row9 : Certificate :=
  (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.pair 7 5) (.branch (.branch (.branch (.pair 26 16) (.branch (.pair 75 42) (.pair 1 2))) (.branch (.pair 1 2) (.branch (.branch (.pair 59 34) (.pair 4 3)) (.pair 26 16)))) (.pair 32 19))) (.branch (.pair 1 2) (.branch (.branch (.pair 7 5) (.pair 57 32)) (.branch (.pair 17 11) (.pair 71 41))))) (.branch (.pair 35 21) (.branch (.branch (.pair 0 1) (.branch (.pair 1 2) (.pair 4 3))) (.pair 59 34)))) (.branch (.branch (.pair 71 41) (.branch (.pair 0 1) (.branch (.pair 63 36) (.branch (.pair 9 6) (.pair 35 21))))) (.branch (.pair 0 1) (.branch (.branch (.branch (.pair 11 7) (.pair 13 8)) (.pair 68 39)) (.pair 23 14))))) (.branch (.branch (.branch (.branch (.branch (.pair 14 9) (.branch (.branch (.branch (.branch (.pair 47 27) (.pair 41 24)) (.pair 8 6)) (.pair 53 31)) (.branch (.pair 8 6) (.branch (.pair 4 3) (.pair 57 32))))) (.pair 29 17)) (.branch (.branch (.branch (.pair 27 16) (.pair 53 31)) (.pair 81 46)) (.pair 17 11))) (.branch (.pair 17 11) (.branch (.pair 41 24) (.branch (.branch (.pair 31 18) (.pair 9 6)) (.branch (.pair 55 32) (.branch (.pair 9 6) (.branch (.pair 29 17) (.pair 40 24)))))))) (.branch (.branch (.pair 53 31) (.branch (.pair 77 44) (.branch (.pair 17 11) (.branch (.pair 19 12) (.pair 22 13))))) (.branch (.branch (.branch (.pair 5 4) (.branch (.pair 25 15) (.pair 75 42))) (.pair 19 12)) (.branch (.pair 5 4) (.branch (.branch (.pair 13 8) (.branch (.branch (.branch (.pair 17 10) (.pair 16 10)) (.pair 44 26)) (.pair 19 12))) (.pair 50 29))))))) (.branch (.branch (.branch (.branch (.pair 26 16) (.branch (.pair 50 29) (.branch (.branch (.pair 40 23) (.pair 18 11)) (.branch (.pair 64 37) (.branch (.branch (.pair 49 29) (.pair 38 22)) (.pair 18 11)))))) (.branch (.branch (.branch (.branch (.pair 62 36) (.pair 8 6)) (.branch (.branch (.pair 25 16) (.pair 62 36)) (.pair 48 27))) (.pair 26 16)) (.branch (.pair 38 22) (.branch (.branch (.branch (.pair 17 11) (.branch (.pair 66 37) (.pair 13 8))) (.branch (.pair 62 36) (.branch (.branch (.pair 50 29) (.pair 56 32)) (.pair 17 11)))) (.pair 23 14))))) (.branch (.branch (.branch (.branch (.branch (.branch (.pair 26 15) (.pair 25 15)) (.pair 34 20)) (.pair 14 9)) (.pair 28 17)) (.branch (.pair 14 9) (.branch (.pair 59 34) (.branch (.pair 2 2) (.pair 4 3))))) (.branch (.branch (.branch (.pair 54 31) (.branch (.pair 0 1) (.pair 26 16))) (.branch (.branch (.pair 28 17) (.pair 31 18)) (.pair 2 2))) (.pair 62 36)))) (.branch (.branch (.branch (.pair 8 6) (.branch (.pair 32 19) (.branch (.branch (.pair 0 1) (.pair 22 13)) (.pair 77 44)))) (.branch (.branch (.branch (.branch (.pair 18 11) (.pair 44 26)) (.pair 72 41)) (.pair 8 6)) (.pair 80 46))) (.branch (.branch (.branch (.branch (.branch (.pair 66 37) (.pair 16 10)) (.branch (.pair 8 5) (.pair 7 5))) (.pair 10 7)) (.branch (.pair 16 10) (.branch (.pair 41 24) (.branch (.pair 4 3) (.branch (.branch (.pair 35 21) (.branch (.pair 7 5) (.pair 8 5))) (.pair 10 7)))))) (.branch (.branch (.pair 68 39) (.branch (.branch (.pair 10 7) (.pair 13 8)) (.pair 8 6))) (.pair 44 26)))))) (.branch (.branch (.branch (.pair 66 37) (.pair 30 17)) (.branch (.pair 48 27) (.pair 12 7))) (.branch (.branch (.pair 57 32) (.pair 21 12)) (.branch (.pair 39 22) (.pair 3 2)))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row9_valid : valid 81 row9 4 9=true := by decide

private def row10 : Certificate :=
  (.branch (.branch (.pair 31 18) (.pair 13 8)) (.branch (.pair 22 13) (.pair 4 3)))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row10_valid : valid 81 row10 4 10=true := by decide

private def row11 : Certificate :=
  .exempt

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row11_valid : valid 81 row11 4 11=true := by decide

private def row12 : Certificate :=
  (.pair 0 0)

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row12_valid : valid 81 row12 4 12=true := by decide

private def row13 : Certificate :=
  (.branch (.branch (.pair 2 2) (.pair 0 0)) (.branch (.branch (.pair 0 0) (.pair 29 17)) (.branch (.pair 20 12) (.pair 2 2))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row13_valid : valid 81 row13 4 13=true := by decide

private def row14 : Certificate :=
  (.branch (.pair 18 11) (.pair 9 6))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row14_valid : valid 81 row14 4 14=true := by decide

private def row15 : Certificate :=
  (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.branch (.pair 20 12) (.pair 42 24)) (.branch (.pair 66 38) (.branch (.branch (.pair 40 23) (.pair 51 30)) (.pair 20 12)))) (.pair 52 30)) (.pair 28 17)) (.branch (.branch (.branch (.branch (.pair 10 7) (.pair 64 37)) (.branch (.branch (.pair 27 17) (.pair 64 37)) (.pair 50 28))) (.pair 28 17)) (.branch (.branch (.branch (.branch (.branch (.pair 68 38) (.pair 15 9)) (.pair 19 12)) (.branch (.pair 64 37) (.branch (.branch (.pair 58 33) (.pair 52 30)) (.pair 19 12)))) (.pair 25 15)) (.pair 40 23)))) (.branch (.branch (.pair 64 37) (.branch (.branch (.branch (.pair 28 17) (.pair 2 2)) (.pair 56 32)) (.branch (.branch (.pair 30 18) (.pair 33 19)) (.pair 4 3)))) (.branch (.branch (.branch (.branch (.pair 6 4) (.pair 4 3)) (.pair 61 35)) (.pair 16 10)) (.branch (.pair 30 18) (.branch (.branch (.branch (.pair 27 16) (.pair 28 16)) (.pair 36 21)) (.pair 16 10)))))) (.branch (.branch (.branch (.branch (.pair 12 8) (.branch (.branch (.pair 10 6) (.pair 9 6)) (.branch (.pair 68 38) (.pair 18 11)))) (.branch (.pair 18 11) (.branch (.branch (.branch (.pair 12 8) (.branch (.branch (.pair 9 6) (.pair 10 6)) (.pair 37 22))) (.pair 6 4)) (.pair 43 25)))) (.branch (.pair 46 27) (.branch (.branch (.pair 10 7) (.branch (.pair 12 8) (.pair 15 9))) (.pair 0 1)))) (.branch (.branch (.branch (.pair 34 20) (.branch (.branch (.pair 24 14) (.pair 2 2)) (.pair 79 45))) (.pair 10 7)) (.branch (.branch (.pair 10 7) (.branch (.branch (.pair 46 27) (.pair 20 12)) (.pair 74 42))) (.branch (.pair 22 13) (.branch (.branch (.branch (.pair 46 27) (.branch (.pair 1 2) (.branch (.pair 34 20) (.pair 40 23)))) (.branch (.pair 1 2) (.branch (.pair 50 28) (.pair 46 27)))) (.pair 7 5))))))) (.branch (.branch (.branch (.branch (.pair 1 2) (.branch (.pair 25 15) (.branch (.pair 70 40) (.branch (.pair 15 9) (.pair 13 8))))) (.branch (.pair 73 42) (.branch (.pair 1 2) (.branch (.pair 65 37) (.branch (.pair 11 7) (.pair 37 22)))))) (.branch (.branch (.branch (.pair 61 35) (.branch (.pair 1 2) (.branch (.pair 3 3) (.pair 6 4)))) (.pair 37 22)) (.branch (.branch (.pair 3 3) (.branch (.branch (.pair 19 12) (.pair 73 42)) (.branch (.pair 9 6) (.pair 59 33)))) (.branch (.pair 9 6) (.branch (.branch (.branch (.branch (.pair 77 43) (.pair 3 3)) (.pair 28 17)) (.branch (.pair 3 3) (.branch (.branch (.pair 61 35) (.pair 6 4)) (.pair 28 17)))) (.pair 34 20)))))) (.branch (.branch (.branch (.branch (.branch (.pair 16 10) (.branch (.branch (.branch (.pair 6 4) (.pair 59 33)) (.pair 10 7)) (.branch (.pair 55 32) (.branch (.pair 10 7) (.branch (.pair 49 28) (.pair 43 25)))))) (.pair 31 18)) (.branch (.pair 19 12) (.branch (.branch (.pair 1 2) (.pair 55 32)) (.branch (.branch (.pair 55 32) (.pair 18 12)) (.pair 41 23))))) (.branch (.branch (.pair 43 25) (.branch (.branch (.pair 33 19) (.pair 11 7)) (.branch (.branch (.branch (.pair 31 18) (.pair 42 25)) (.pair 11 7)) (.pair 57 33)))) (.pair 19 12))) (.branch (.branch (.branch (.pair 21 13) (.branch (.branch (.pair 77 43) (.pair 27 16)) (.pair 7 5))) (.branch (.pair 7 5) (.branch (.pair 52 30) (.pair 0 1)))) (.branch (.pair 55 32) (.branch (.branch (.branch (.pair 24 14) (.pair 21 13)) (.pair 19 12)) (.pair 79 45))))))) (.branch (.branch (.branch (.pair 14 8) (.pair 50 28)) (.branch (.pair 32 18) (.pair 68 38))) (.branch (.branch (.pair 59 33) (.pair 23 13)) (.branch (.pair 5 3) (.pair 41 23))))) (.branch (.branch (.branch (.branch (.branch (.pair 64 37) (.branch (.branch (.pair 28 17) (.pair 63 37)) (.pair 73 41))) (.branch (.branch (.branch (.branch (.pair 63 36) (.branch (.branch (.branch (.branch (.branch (.branch (.pair 64 36) (.branch (.branch (.branch (.pair 9 7) (.pair 36 21)) (.pair 18 11)) (.branch (.branch (.branch (.branch (.branch (.pair 4 3) (.pair 15 9)) (.pair 46 27)) (.branch (.pair 57 34) (.branch (.pair 46 27) (.branch (.branch (.pair 15 9) (.pair 27 17)) (.pair 72 41))))) (.pair 18 11)) (.pair 36 21)))) (.pair 27 17)) (.pair 22 14)) (.pair 1 1)) (.branch (.pair 22 14) (.branch (.pair 46 26) (.pair 36 21)))) (.branch (.pair 22 14) (.branch (.pair 4 3) (.branch (.branch (.branch (.branch (.branch (.pair 9 6) (.pair 60 34)) (.branch (.branch (.pair 19 12) (.branch (.pair 9 6) (.pair 21 14))) (.branch (.pair 9 6) (.pair 79 44)))) (.branch (.pair 79 44) (.pair 49 28))) (.pair 37 20)) (.branch (.branch (.pair 37 20) (.pair 66 38)) (.branch (.branch (.pair 37 20) (.branch (.pair 0 1) (.branch (.branch (.branch (.branch (.pair 24 15) (.pair 9 6)) (.branch (.pair 60 34) (.pair 6 4))) (.pair 60 33)) (.pair 3 3)))) (.branch (.pair 3 3) (.branch (.branch (.pair 36 21) (.pair 18 14)) (.pair 37 20)))))))))) (.pair 27 17)) (.pair 37 21)) (.pair 28 17))) (.branch (.branch (.branch (.branch (.pair 9 7) (.branch (.branch (.pair 72 41) (.branch (.branch (.pair 19 10) (.branch (.branch (.pair 9 7) (.branch (.pair 46 26) (.branch (.branch (.branch (.pair 0 1) (.pair 73 42)) (.pair 18 11)) (.branch (.pair 0 1) (.branch (.pair 81 47) (.pair 18 11)))))) (.pair 4 4))) (.branch (.pair 73 41) (.pair 4 4)))) (.pair 45 26))) (.pair 19 11)) (.pair 10 7)) (.branch (.branch (.branch (.pair 45 27) (.pair 10 7)) (.pair 55 31)) (.pair 46 27)))) (.branch (.branch (.branch (.pair 1 2) (.pair 73 42)) (.branch (.pair 37 22) (.branch (.branch (.pair 36 22) (.pair 1 2)) (.pair 46 26)))) (.branch (.branch (.pair 19 12) (.branch (.branch (.pair 18 12) (.branch (.branch (.pair 81 46) (.branch (.branch (.pair 28 15) (.branch (.pair 13 9) (.branch (.branch (.pair 55 31) (.branch (.branch (.pair 9 6) (.branch (.pair 27 16) (.branch (.branch (.branch (.pair 19 11) (.pair 4 3)) (.pair 36 21)) (.branch (.pair 4 3) (.branch (.branch (.branch (.pair 25 13) (.pair 12 9)) (.pair 37 22)) (.branch (.pair 25 13) (.pair 36 21))))))) (.branch (.pair 27 16) (.branch (.pair 9 6) (.branch (.branch (.branch (.pair 37 22) (.branch (.branch (.pair 1 1) (.pair 6 4)) (.pair 63 36))) (.pair 48 29)) (.branch (.branch (.pair 6 4) (.branch (.branch (.pair 16 10) (.branch (.pair 48 29) (.pair 27 16))) (.pair 9 7))) (.pair 37 22))))))) (.pair 18 12)))) (.branch (.branch (.pair 37 21) (.pair 27 16)) (.pair 13 9)))) (.pair 54 31))) (.pair 28 16))) (.branch (.pair 55 32) (.branch (.branch (.pair 54 32) (.pair 19 12)) (.pair 64 36)))))) (.branch (.branch (.branch (.branch (.branch (.pair 66 38) (.pair 49 28)) (.pair 13 8)) (.branch (.branch (.branch (.pair 13 8) (.branch (.pair 67 38) (.pair 34 20))) (.branch (.branch (.pair 22 13) (.pair 13 8)) (.pair 67 38))) (.pair 49 28))) (.branch (.branch (.branch (.pair 67 38) (.branch (.pair 12 8) (.branch (.pair 16 10) (.pair 49 28)))) (.pair 31 18)) (.branch (.branch (.branch (.branch (.pair 40 23) (.pair 31 18)) (.pair 14 7)) (.branch (.branch (.branch (.branch (.pair 12 8) (.branch (.pair 53 29) (.pair 66 38))) (.pair 41 23)) (.pair 52 30)) (.pair 31 18))) (.pair 67 38)))) (.branch (.branch (.branch (.branch (.pair 58 33) (.pair 75 43)) (.pair 22 13)) (.branch (.branch (.branch (.branch (.pair 22 13) (.pair 31 18)) (.pair 5 2)) (.branch (.branch (.pair 43 25) (.pair 76 43)) (.pair 22 13))) (.pair 58 33))) (.branch (.branch (.branch (.branch (.branch (.pair 58 33) (.pair 25 15)) (.pair 4 3)) (.pair 76 43)) (.pair 40 23)) (.branch (.pair 4 3) (.pair 76 43)))))))

set_option maxRecDepth 16384 in
set_option maxHeartbeats 8000000 in
private theorem row15_valid : valid 81 row15 4 15=true := by decide

private def tree81 : Certificate := (.branch (.branch (.branch (.branch row0 row8) (.branch row4 row12)) (.branch (.branch row2 row10) (.branch row6 row14))) (.branch (.branch (.branch row1 row9) (.branch row5 row13)) (.branch (.branch row3 row11) (.branch row7 row15))))
private theorem tree81_valid : valid 81 tree81 0 0=true := by
  change (((((valid 81 row0 4 0) && (valid 81 row8 4 8)) && ((valid 81 row4 4 4) && (valid 81 row12 4 12))) && (((valid 81 row2 4 2) && (valid 81 row10 4 10)) && ((valid 81 row6 4 6) && (valid 81 row14 4 14)))) && ((((valid 81 row1 4 1) && (valid 81 row9 4 9)) && ((valid 81 row5 4 5) && (valid 81 row13 4 13))) && (((valid 81 row3 4 3) && (valid 81 row11 4 11)) && ((valid 81 row7 4 7) && (valid 81 row15 4 15)))))=true
  rw [row0_valid,row1_valid,row2_valid,row3_valid,row4_valid,row5_valid,row6_valid,row7_valid,row8_valid,row9_valid,row10_valid,row11_valid,row12_valid,row13_valid,row14_valid,row15_valid]
  rfl

theorem reset_81 (col : Coloring) {n : Nat} (cut : Mixed col n) (j : Nat)
    (reset : index col n j%16≠11) : ¬ Copies col n j 81 :=
  forbids tree81 81 tree81_valid col cut j reset

theorem eventually_no_81 (col : Coloring) {n : Nat} (cut : Mixed col n) :
    ∃ J, ∀ j≥J, ¬ Copies col n j 81 :=
  eventually_from_reset col cut 81 (by decide) (reset_81 col cut)

end WallBank
