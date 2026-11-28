"""Rebuild a heterogeneous affine cylinder and its literal first arrivals."""

from check_finite_patterns import advance, check, first_one, refinement, trace


ARMS = [(0, 0, 0), (1, 0, 1), (0, 1, 2), (1, 1, 5), (2, 2, 17), (3, 1, 11)]
CONTROLS = [(0, 148, 80), (1, 130, 68), (13, 79, 34), (1079, 120, 56)]


def cylinder():
    profiles = [(0, 0)]
    for delay, debt, shift in ARMS:
        endpoint, initial_grade = trace(shift, delay)
        profiles.append((debt + initial_grade, endpoint))

    clock, residue = 0, 0
    for index in range(1, len(profiles)):
        while profiles[index] != profiles[0]:
            extra, selected = refinement(profiles[0], profiles[index])
            residue += 2**clock * selected
            clock += extra
            profiles = [advance(profile, extra, selected) for profile in profiles]
    return clock, residue, profiles[0]


def main():
    clock, residue, (grade, base) = cylinder()
    check((clock, residue, grade, base) == (21, 2076818, 11, 175430), "affine cylinder")
    for lift, first_clock, first_grade in CONTROLS:
        parameter = residue + 2**clock * lift
        for delay, debt, shift in ARMS:
            start = 2**delay * 3**debt * parameter + shift
            observed = trace(start, clock + delay)
            check(observed == (base + 3**grade * lift, grade - debt), "prefix replay")
            final = first_one(start, 10000)
            check(final == (first_clock + delay, first_grade - debt), "first visit to 1")
    negative_cases = 0
    for horizon in range(10):
        for offset in (1, 7, 19):
            parameter = 2 * 6**horizon + offset
            left = {trace(parameter, i)[0] for i in range(horizon + 1)}
            right = {trace(5 * parameter + 1, j)[0] for j in range(horizon + 1)}
            check(left.isdisjoint(right), "unequal prime-to-six slopes beyond guard")
            negative_cases += 1
    print(f"PASS {len(ARMS)} affine arms on {len(CONTROLS)} ordinary cylinder lifts")
    print(f"PASS {len(ARMS) * len(CONTROLS)} independent complete first-arrival traces")
    print(f"PASS {negative_cases} finite incompatible-slope guards")


if __name__ == "__main__":
    main()
