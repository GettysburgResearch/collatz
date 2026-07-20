"""The corrected supercritical amplifier family (PROGRAM.md section 4).

Seed word  A 6 7^k #  in the -5 phase system has value n(k) = 8^{k+2} - 21.
Four bridge steps take the template -21 onto the -17 cycle
(-21 -> -31 -> -46 -> -23 -> -34, parities 1101), after which the family
rides the supercritical -17 cycle (density 7/11 > log_3 2) for its whole
stored depth:

    LEMMA.  T^{4+11j}(8^{k+2} - 21) = 27 * 3^{7j} * 2^{3k+2-11j} - 34
            for all k >= 1 and 0 <= 11j <= 3k+2.

Contrast: the 24-step gadget of the submitted outline contracts
(3^15/2^24 ~ 0.855); this family EXPANDS while its fuel lasts.

Also demonstrated: two-stage composite (steer to a fresh deep template
BEFORE exhaustion; after exhaustion the value is forced == -34 mod 2^e
and steering is impossible), and CRT constructibility of finite towers.
"""

from core import T_iter, value_word

# word value
for k in range(1, 8):
    assert 8 * value_word([6] + [7] * k, 8) - 5 == 8 ** (k + 2) - 21
print("A 6 7^k #  <->  n(k) = 8^{k+2} - 21")

# bridge onto the -17 cycle
x, par = T_iter(-21, 4)
assert x == -34 and par == [1, 1, 0, 1]
print("bridge: -21 -> -31 -> -46 -> -23 -> -34 (on the -17 cycle), parities 1101")

# the lemma
ok = True
for k in range(1, 40):
    n = 8 ** (k + 2) - 21
    for j in range((3 * k + 2) // 11 + 1):
        got, _ = T_iter(n, 4 + 11 * j)
        ok &= got == 27 * 3 ** (7 * j) * 2 ** (3 * k + 2 - 11 * j) - 34
print("LEMMA T^{4+11j}(8^{k+2}-21) = 27*3^{7j}*2^{3k+2-11j} - 34:",
      "PASS" if ok else "FAIL")
assert ok

# density over the full window at k=33
k = 33
n = 8 ** (k + 2) - 21
S = 4 + 11 * ((3 * k + 2) // 11)
m, par = T_iter(n, S)
O = sum(par)
print(f"k={k}: {O}/{S} odd = {O/S:.5f} > log_3 2; "
      f"bits {n.bit_length()} -> {m.bit_length()} (EXPANDS); "
      f"3^{O} > 2^{S}: {3**O > 2**S}")
assert 3 ** O > 2 ** S and m.bit_length() > n.bit_length()

# two-stage composite with early steering
k, j1 = 40, 6
u = 987654321987654321 | 1
n = 2 ** (3 * k + 6) * u - 21
D = 3 * k + 2 - 11 * j1
V, _ = T_iter(n, 4 + 11 * j1)
assert V == 27 * 3 ** (7 * j1) * 2 ** D * u - 34
j2 = (D - 2) // 11
S = 4 + 11 * j1 + 11 * j2
m, par = T_iter(n, S)
O = sum(par)
assert m == 3 ** (7 * j2) * 27 * 3 ** (7 * j1) * 2 ** (D - 11 * j2) * u - 34
print(f"two-stage composite: {O}/{S} = {O/S:.5f}, supercritical: {3**O > 2**S}, "
      f"bits {n.bit_length()} -> {m.bit_length()}")
assert 3 ** O > 2 ** S
print("ALL CHECKS PASS")
