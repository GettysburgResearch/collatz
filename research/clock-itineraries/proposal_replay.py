"""Independent ordinary-integer controls for the clock and cycle proposal."""

import json


def check(condition, description):
    if not condition:
        raise ValueError(description)


def odd_step(x):
    value = 3*x+1
    e = (value & -value).bit_length()-1
    return e, value >> e


def check_clock_tests():
    crossings = before_one = simple_segments = 0
    for a in range(1, 8192, 2):
        if a % 3 == 0:
            continue
        q, clock, seen, first = a, 0, set(), None
        for k in range(1, 1500):
            seen.add(q)
            gap, q = odd_step(q)
            clock += gap
            if q > 1:
                check(len(seen) == k, "unexpected repeated odd input above one")
                check(((1 << clock)*q)**6 <= (k+1)*(3**k*a)**6,
                      "sixth-power distortion on distinct inputs")
                simple_segments += 1
            if first is None and 1 << (6*clock) > (k+1)*3**(6*k):
                first = k
                check(a == 1 or q < a, "crossing on a terminating trajectory")
                crossings += 1
                before_one += q > 1
            if q == 1 and first is not None:
                break
        else:
            raise ValueError("finite control did not reach its two stopping conditions")
    return dict(clock_crossings=crossings, crossings_above_one=before_one,
                checked_simple_segments=simple_segments)


def check_cycle_rows(depth=16):
    # Use the proved source bound, then follow the actual source deterministically.
    candidate_counts = [0]*(depth+1)
    witnesses = [0]*(depth+1)
    candidate_counts[0] = sum(1 for x in range(3, 10, 2) if x % 3)
    for x in range(1, 10*(1 << depth), 2):
        if x % 3 == 0:
            continue
        q, clock = x, 0
        for b in range(1, depth+1):
            gap, q = odd_step(q)
            clock += gap
            if x >= 10*(1 << b) or q <= 2 or clock != 2*b:
                continue
            candidate_counts[b] += 1
            if ((1 << clock)*q)**6 > (b+1)*(3**b*x)**6:
                check((1 << b)*(q+1) <= 11*3**b, "finite witness endpoint bound")
                witnesses[b] += 1
    check(not any(witnesses), "positive cycle witness in the controls")
    # Keeping the fixed point in this statistic would trigger it at every positive depth.
    check(all(4**(6*b) > (b+1)*3**(6*b) for b in range(1, depth+1)),
          "control at the excluded endpoint one")
    return dict(exhausted_depths=[0, depth], balanced_candidates=sum(candidate_counts),
                cycle_witnesses=sum(witnesses))


def check_shadows():
    traces = {}
    for x in range(1, 200, 2):
        q, gaps = x, []
        for _ in range(3):
            e, q = odd_step(q)
            gaps.append(e)
            traces.setdefault((q, len(gaps), sum(gaps)), []).append((x, tuple(gaps)))
    families = paths = 0
    for (q, b, clock), members in traces.items():
        if len(members) < 2 or q > 31:
            continue
        for target in (1, 5, 7):
            for K in range(2):
                modulus = 2*3**(b+K)
                # Independently search the final gap, without the Lean digit lift.
                for e in range(1, 2*q+2*3**(b+K)+3):
                    endpoint, rem = divmod((target << e)-1, 3)
                    if rem == 0 and endpoint > q and (endpoint-q) % modulus == 0:
                        break
                else:
                    raise ValueError("missing one-gap endpoint in the claimed bound")
                d = (endpoint-q)//modulus
                shift = (1 << (clock+1))*3**K*d
                check(odd_step(endpoint) == (e, target), "terminal gap")
                for x, gaps in members:
                    y = x+shift
                    for g in gaps:
                        actual, y = odd_step(y)
                        check(actual == g, "translated valuation")
                    check(y == endpoint, "translated endpoint")
                    check((endpoint << clock)-3**b*(x+shift) == (q << clock)-3**b*x,
                          "translated integer carry")
                    paths += 1
                families += 1
    check(families > 0, "no multiple-source shadow families tested")
    return dict(shadow_families=families, translated_paths=paths)


def check_published_gate():
    q = (1 << 63)-1
    for clock in range(554):
        if q == 1:
            check(clock == 553, "first hit of the published gate")
            return clock
        q = (3*q+1)//2 if q % 2 else q//2
    raise ValueError("published gate missed its certified hit")


if __name__ == "__main__":
    print(json.dumps(dict(**check_clock_tests(), **check_cycle_rows(), **check_shadows(),
                          original_gate_first_hit=check_published_gate()), indent=2))
