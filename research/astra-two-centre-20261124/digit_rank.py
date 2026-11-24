"""Replay exact ordinary obstructions to three finite-binary-word ranks.

Each row in the two weighted witnesses contains an ordinary source, a positive
shortcut clock and a positive integer multiplicity. No optimizer is needed.
"""

from collections import Counter
from functools import lru_cache


PLAIN_SOURCES = (
    11, 13, 17, 22, 26, 29, 31, 41, 44, 47, 50, 52, 54, 58, 62,
    71, 78, 91, 103, 107, 121, 137, 155, 161,
)

POSITION_PATHS = (
    (513, 1, 2522), (519, 1, 69), (521, 1, 1909), (523, 1, 1834),
    (526, 3, 585), (531, 1, 6629), (537, 1, 3919), (539, 1, 10279),
    (543, 1, 3668), (545, 1, 5628), (551, 1, 11448), (559, 1, 6629),
    (563, 1, 2996), (567, 1, 8801), (569, 1, 8858), (571, 1, 510),
    (579, 1, 1765), (583, 1, 7283), (585, 1, 5680), (591, 1, 7910),
    (595, 1, 8317), (599, 1, 3350), (601, 1, 2979), (603, 1, 441),
    (606, 3, 1245), (607, 1, 8914), (615, 1, 4397), (619, 1, 3177),
    (623, 1, 11267), (627, 1, 5275), (635, 1, 7352), (639, 1, 6846),
    (641, 1, 5876), (647, 1, 441), (654, 3, 761), (655, 1, 9680),
    (659, 1, 4287), (665, 1, 4363), (667, 1, 7875), (671, 1, 2665),
    (673, 1, 3378), (679, 1, 5157), (681, 1, 2522), (683, 3, 5872),
    (685, 2, 2522), (690, 2, 69), (694, 2, 4328), (699, 3, 10432),
    (700, 5, 4012), (706, 2, 3586), (714, 2, 441), (718, 2, 8884),
    (721, 2, 3437), (726, 2, 8538), (728, 13, 441), (733, 2, 4287),
    (734, 2, 4251), (737, 2, 1903), (742, 2, 3278), (745, 2, 439),
    (747, 3, 5680), (754, 2, 9891), (762, 2, 6846), (765, 2, 2522),
    (770, 2, 8394), (777, 2, 654), (782, 2, 1324), (785, 2, 4356),
    (786, 2, 7910), (797, 2, 6629), (801, 2, 2910), (805, 2, 1009),
    (809, 2, 9660), (811, 3, 2522), (813, 2, 1765), (818, 2, 2632),
    (822, 2, 2996), (825, 2, 1574), (826, 2, 506), (830, 2, 9368),
    (834, 2, 5275), (835, 3, 1354), (842, 2, 1324), (845, 2, 7352),
    (849, 2, 1601), (850, 2, 3921), (854, 2, 5807), (855, 5, 6330),
    (862, 2, 510), (866, 2, 1765), (873, 2, 8676), (877, 2, 4287),
    (886, 2, 7910), (888, 7, 1324), (893, 2, 1406), (894, 2, 5587),
    (897, 2, 3281), (902, 2, 3048), (905, 2, 2206), (910, 2, 7149),
    (914, 2, 2522), (921, 2, 69), (925, 2, 3437), (926, 2, 891),
    (929, 2, 3080), (933, 2, 2039), (934, 2, 9325), (940, 4, 3043),
    (941, 2, 3586), (956, 4, 4873), (957, 2, 9325), (962, 2, 5645),
    (963, 4, 231), (974, 2, 441), (978, 2, 8538), (982, 2, 1142),
    (988, 4, 1009), (990, 2, 3278), (997, 2, 1765), (998, 2, 2598),
    (1001, 2, 1756), (1004, 4, 582), (1006, 2, 8202), (1010, 2, 1689),
    (1014, 2, 1689), (1017, 2, 1689), (1021, 2, 5990),
)

MATRIX_PATHS = (
    (515, 1, 437), (517, 1, 195), (526, 3, 229), (535, 1, 1306),
    (539, 1, 570), (545, 1, 351), (550, 3, 260), (551, 1, 2328),
    (559, 1, 601), (563, 1, 895), (566, 3, 5217), (571, 1, 203),
    (572, 6, 869), (581, 1, 1145), (584, 27, 351), (587, 1, 634),
    (590, 3, 952), (593, 1, 7102), (595, 1, 744), (599, 1, 601),
    (601, 1, 125), (613, 1, 312), (619, 1, 164), (620, 8, 945),
    (623, 1, 1804), (635, 1, 592), (637, 1, 1220), (638, 3, 3396),
    (641, 1, 173), (643, 1, 238), (646, 3, 437), (647, 1, 1022),
    (653, 1, 1098), (658, 5, 670), (659, 1, 363), (662, 3, 437),
    (668, 5, 6935), (670, 3, 610), (671, 1, 199), (677, 1, 833),
    (686, 2, 437), (689, 2, 195), (695, 5, 1577), (700, 5, 497),
    (701, 2, 229), (715, 3, 720), (718, 2, 497), (719, 6, 524),
    (721, 2, 510), (722, 2, 869), (728, 13, 2989), (730, 2, 351),
    (731, 3, 666), (734, 2, 580), (743, 24, 1423), (745, 2, 601),
    (749, 2, 260), (758, 2, 21), (761, 2, 203), (764, 5, 1821),
    (767, 16, 199), (772, 29, 351), (779, 3, 869), (782, 2, 437),
    (790, 2, 770), (799, 13, 173), (805, 2, 918), (806, 2, 268),
    (809, 2, 372), (811, 3, 333), (815, 10, 1405), (818, 2, 83),
    (823, 5, 1110), (827, 3, 497), (829, 2, 134), (833, 2, 437),
    (845, 2, 363), (851, 3, 164), (857, 2, 238), (860, 5, 601),
    (862, 2, 319), (871, 35, 199), (872, 26, 375), (875, 3, 432),
    (878, 2, 258), (881, 2, 833), (890, 2, 6438), (893, 2, 744),
    (899, 3, 601), (911, 7, 351), (919, 5, 156), (923, 10, 670),
    (926, 2, 1220), (929, 2, 934), (935, 11, 335), (941, 2, 437),
    (946, 2, 497), (950, 2, 87), (953, 2, 884), (958, 2, 164),
    (962, 2, 173), (965, 2, 934), (973, 2, 351), (977, 2, 402),
    (979, 4, 1103), (989, 2, 363), (1000, 23, 335), (1007, 21, 199),
    (1010, 2, 601), (1016, 7, 833),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut(n):
    return (3*n+1)//2 if n%2 else n//2


def compare(rows, features, same_length):
    totals = Counter()
    terms = 0
    max_clock = 0
    max_intermediate = 0
    max_weight = 0
    for source, clock, weight in rows:
        require(source > 2 and clock > 0 and weight > 0, "invalid comparison")
        current = source
        for i in range(clock):
            require(current > 2, "path crosses a non-strict transition")
            current = shortcut(current)
            max_intermediate = max(current, max_intermediate)
            if same_length and i+1 < clock:
                require(current.bit_length() != 10, "unexpected earlier shell return")
        if same_length:
            require(source.bit_length() == current.bit_length() == 10, "shell mismatch")
        for n, sign in ((source, 1), (current, -1)):
            for key, coefficient in features(n).items():
                totals[key] += sign * weight * coefficient
        terms += 1
        max_clock = max(clock, max_clock)
        max_weight = max(weight, max_weight)
    require(terms > 0 and not any(totals.values()), "uncancelled coefficient")
    return terms, max_clock, max_intermediate, max_weight


def padded_blocks(n, position=False):
    binary = format(n, "b")
    counts = Counter()
    for k in range(1, 7):
        padded = "^"*(k-1) + binary + "$"*(k-1)
        for i in range(len(padded)-k+1):
            block = padded[i:i+k]
            key = (len(binary), i, block) if position else block
            counts[key] += 1
    return counts


@lru_cache(None)
def matrix_monomials(n):
    """Expand the complete product of two generic 2-by-2 binary matrices."""
    bits = [int(bit) for bit in format(n, "b")]
    require(len(bits) < 16, "monomial exponent field can overflow")
    # (initial state, current state, exponent vector), starting at identity.
    paths = Counter({(0, 0, 0): 1, (1, 1, 0): 1})
    for bit in bits:
        extended = Counter()
        for (initial, current, monomial), multiplicity in paths.items():
            for target in (0, 1):
                variable = 4*bit + 2*current + target
                # Each of the eight multiplicities occupies its own four bits.
                new_monomial = monomial + (1 << (4*variable))
                extended[initial, target, new_monomial] += multiplicity
        paths = extended
    require(sum(paths.values()) == 2**(len(bits)+1), "incomplete polynomial expansion")
    return paths


def main():
    plain = [(n, 1, 1) for n in PLAIN_SOURCES]
    print("plain", compare(plain, padded_blocks, False))
    print("position", compare(POSITION_PATHS, lambda n: padded_blocks(n, True), True))
    print("matrix", compare(MATRIX_PATHS, matrix_monomials, True))


if __name__ == "__main__":
    main()
