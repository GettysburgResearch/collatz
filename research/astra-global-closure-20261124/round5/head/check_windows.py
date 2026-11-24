"""Check same-prefix representative compression on complete ordinary binary grids."""

from functools import lru_cache
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


@lru_cache(maxsize=None)
def trajectory(start, steps):
    value = start
    odds = 0
    for _ in range(steps):
        odd = value % 2
        odds += odd
        value = (3 * value + 1) // 2 if odd else value // 2
    return odds, value


def profile(start, initial_grade, steps):
    odds, value = trajectory(start, steps)
    return initial_grade + odds, value


def last_indices(keys):
    last = {key: index for index, key in enumerate(keys)}
    return sorted(last.values())


def check_case(horizon, start_clock, prefix, radius, digit, center):
    period = 2**horizon
    # The complete grid is positive even at the lowest point of a tested window.
    base = 2 ** (horizon + start_clock + 2)
    expected_reps = {}
    third_count = 0
    live_count = 0
    checks = 0
    for residue in range(period):
        parent = base + residue
        arms = [profile(parent, 0, start_clock),
                profile(81 * parent + digit, 4, start_clock)]
        grade, value = arms[center]
        window = range(value - radius, value + radius + 1)
        require(window.start > 0, "Window contains a nonpositive source")
        early = [profile(v, grade, prefix) for v in window]
        full = [profile(v, grade, horizon - start_clock) for v in window]
        reps = last_indices(early)
        prefix_residue = residue % (2 ** (start_clock + prefix))
        if prefix_residue in expected_reps:
            require(expected_reps[prefix_residue] == reps,
                    "Representative indices changed on one prefix")
        else:
            expected_reps[prefix_residue] = reps
        require(len(reps) == len(set(early)), "Missing or duplicate prefix class")
        require(set(full) == {full[i] for i in reps},
                "Representatives missed a terminal profile")
        last = {early[i]: i for i in reps}
        for i, key in enumerate(early):
            j = last[key]
            require(i <= j and full[j] == full[i],
                    "Rightmost representative lost a continuation")
            checks += 1
        head = {profile(v, a, horizon - start_clock) for a, v in arms}
        if len(head) == 2:
            live_count += 1
            direct = any(k not in head for k in full)
            compressed = any(full[i] not in head for i in reps)
            require(direct == compressed, "Third-profile tests disagree")
            third_count += direct
    return {
        'horizon': horizon, 'start_clock': start_clock,
        'compression_clocks': prefix, 'radius': radius, 'digit': digit,
        'center': ['parent', 'child'][center], 'source_count': period,
        'live_symbolic_head_count': live_count,
        'three_profile_count': third_count,
        'continuation_checks': checks,
    }


def main():
    cases = [check_case(h, s, m, w, r, center)
             for h, s, m, w in [(7, 0, 3, 5), (9, 0, 4, 8), (9, 2, 3, 6)]
             for r in (0, 40, 73, 80) for center in (0, 1)]
    print(json.dumps({
        'status': 'PASS',
        'scope': 'Original-grid equality of finite symbolic profile tests before and after rightmost-representative compression. No eventual-color or asymptotic count.',
        'cases': cases,
        'total_source_case_evaluations': sum(c['source_count'] for c in cases),
        'total_index_continuation_checks': sum(c['continuation_checks'] for c in cases),
    }, indent=2))


if __name__ == '__main__':
    main()
