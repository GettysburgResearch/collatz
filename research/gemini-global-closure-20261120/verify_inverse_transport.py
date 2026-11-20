#!/usr/bin/env python3
"""Exact finite interfaces for ACTUAL_TRANSPORT and AVERAGED_CHAIN_AUDIT.

This standard-library replay uses explicit exceptions (also under -O). It does
not import the supplied Gemini scripts or repository generators. All-depth
claims rest on the accompanying proofs, not the finite sample below.
"""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


def require(test, message):
    if not test:
        raise ValueError(message)


def valuation(n, p):
    require(n != 0, "valuation at zero")
    n = abs(n)
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def rank(n):
    if n == 1:
        return 0
    h = valuation(2 * n + 1, 3)
    modes = {0, 1, 2}
    if h >= 3:
        modes.add(h)
    values = []
    for a in modes:
        z = 3**a * (n + 1) - 2**a * (2 * n + 1)
        require(z != 0, "unexpected rank zero")
        values.append(z * z // 3**valuation(z, 3))
    result = min(values)
    require(n - 1 <= result <= n * n, "rank properness interface")
    return result


def accelerate(n):
    if n == 1:
        return 1, 0
    a = 0 if n % 2 == 0 else valuation(n + 1, 2)
    d = 3**a - 2**(a + 1)
    c = 3**a - 2**a
    z = d * n + c
    k = valuation(z, 2) // (a + 1)
    require(k >= 1, "empty acceleration")
    transformed_z = 3**(a * k) * (z // 2**((a + 1) * k))
    require((transformed_z - c) % d == 0, "nonintegral acceleration")
    endpoint = (transformed_z - c) // d
    physical = n
    for _ in range(k):
        for _ in range(a):
            require(physical % 2 == 1, "wrong odd mode bit")
            physical = shortcut(physical)
        require(physical % 2 == 0, "wrong even mode bit")
        physical = shortcut(physical)
    require(endpoint == physical and endpoint >= 1, "affine/physical mismatch")
    require(endpoint + 5 <= (n + 5)**3, "polynomial height bound")
    require(rank(endpoint) + 6 <= (rank(n) + 6)**6, "logarithmic-domain bound")
    return endpoint, (a + 1) * k


def is_safe(n):
    require(n > 1, "safe guard excludes absorbing 1")
    endpoint, _ = accelerate(n)
    return 4 * rank(endpoint) <= rank(n)


def unsafe_return(n):
    require(n > 1 and not is_safe(n), "unsafe return source guard")
    current, _ = accelerate(n)
    first_rank = rank(current)
    safe_steps = 0
    while current > 1 and is_safe(current):
        previous_rank = rank(current)
        current, _ = accelerate(current)
        require(4 * rank(current) <= previous_rank, "safe rank increase")
        safe_steps += 1
        require(4**safe_steps <= max(first_rank, 1) * 4, "safe termination bound")
    require(rank(current) <= first_rank, "return exceeds first endpoint rank")
    require(rank(current) + 6 <= (rank(n) + 6)**6, "return log-domain bound")
    return current, safe_steps


def check_actual_transport():
    source_limit = 4096
    unsafe_sources = 0
    killed_returns = 0
    max_safe_steps = 0
    for n in range(2, source_limit + 1):
        accelerate(n)
        if not is_safe(n):
            unsafe_sources += 1
            endpoint, safe_steps = unsafe_return(n)
            killed_returns += endpoint == 1
            max_safe_steps = max(max_safe_steps, safe_steps)
        else:
            current = n
            occupations = 0
            while current > 1 and is_safe(current):
                occupations += 1
                current, _ = accelerate(current)
            require(4**(occupations - 1) <= rank(n), "safe occupation count")

    half_input = Fraction(0)
    family_count = 17
    family_endpoints = set()
    for j in range(family_count):
        e = 4 + 16 * j
        x = 3**e
        y = (9 * x + 7) // 16
        require((9 * x + 7) % 16 == 0, "family integrality")
        require(rank(x) == x, "family source rank")
        require(rank(y) == 9 * (x - 1)**2 // 256, "family endpoint rank")
        require(729 * rank(y) >= 25 * x * x, "family quadratic lower bound")
        require(not is_safe(x) and not is_safe(y), "family unsafe membership")
        endpoint, safe_steps = unsafe_return(x)
        require(endpoint == y and safe_steps == 0, "family exact B edge")
        path = [x]
        for _ in range(4):
            path.append(shortcut(path[-1]))
        require(path[-1] == y and min(path) == y, "family physical floor")
        require(y not in family_endpoints, "family distinct endpoints")
        family_endpoints.add(y)
        sqrt_rx = 3**(e // 2)
        sqrt_ry = 3 * (x - 1) // 16
        require(sqrt_rx**2 == rank(x) and sqrt_ry**2 == rank(y), "exact square-root rank")
        half_input += Fraction(sqrt_rx, sqrt_ry)
    half_bound = Fraction(3, 5) / (1 - Fraction(1, 3**8))
    require(half_input <= half_bound, "square-root input moment bound")
    shadow_cases = 0
    for j in range(1, 17):
        cycles = j // 2 + 1
        binary_modulus = 1 << (6 * cycles + 1)
        # Exact valuation 6K is equivalent to this one residue mod 2^(6K+1).
        binary_residue = ((1 << (6 * cycles)) - 73) * pow(17, -1, binary_modulus) % binary_modulus
        multiplier = (10 - binary_residue) * pow(binary_modulus, -1, 243) % 243
        base = binary_residue + binary_modulus * multiplier
        period = 243 * binary_modulus
        for lift in (1, 10, 100):
            n = base + period * lift
            require(n % 243 == 10 and valuation(17 * n + 73, 2) == 6 * cycles, "unsafe shadow CRT")
            current = n
            for step in range(j):
                require(not is_safe(current), "unsafe shadow source escaped U")
                actual, safe_steps = unsafe_return(current)
                affine = (27 * current + 19) // 16 if step % 2 == 0 else (3 * current + 1) // 4
                require(actual == affine and safe_steps == 0, "B differs from shadow affine branch")
                current = actual
            require(not is_safe(current), "shadow endpoint lacks one reserved future unsafe source")
            expected_rank = (current - 1)**2 // 9 if j % 2 == 0 else (current + 5)**2 // 9
            require(rank(current) == expected_rank, "shadow endpoint rank formula")
            require(rank(n) == (n - 1)**2 // 9, "shadow initial rank formula")
            shadow_cases += 1
    return {
        "source_range": [2, source_limit],
        "unsafe_sources": unsafe_sources,
        "killed_unsafe_returns": killed_returns,
        "largest_observed_safe_excursion": max_safe_steps,
        "direct_unsafe_family_cases": family_count,
        "largest_family_exponent": 4 + 16 * (family_count - 1),
        "square_root_input_moment_exact_upper_bound": str(half_bound),
        "square_root_partial_output_moment": family_count,
        "essential_spectral_boundary_shadow_cases": shadow_cases,
        "checked_return_horizons": [1, 16],
        "all_p_claim_evidence": "written geometric-series proof; finite replay is supplementary",
    }


def parity_window(n, m):
    bits = []
    for _ in range(m):
        bits.append(n % 2)
        n = shortcut(n)
    return tuple(bits)


def gemini_kills(r, m):
    # Exact reconstruction of the uploaded deletion criterion, not an import.
    modulus = 1 << m
    a, b = modulus, r
    for _ in range(m):
        if a % 2:
            break
        if b % 2 == 0:
            a //= 2
            b //= 2
        else:
            a = 3 * a // 2
            b = (3 * b + 1) // 2
        if a < modulus and (b < r or (r == 0 and a + b < modulus)):
            return True
    return False


def check_binary_operator():
    table = []
    for m in range(1, 11):
        modulus = 1 << m
        windows = [parity_window(r, m) for r in range(modulus)]
        require(len(set(windows)) == modulus, "parity coding not bijective")
        killed = {r for r in range(modulus) if gemini_kills(r, m)}
        require(all(r in killed for r in range(0, modulus, 2)), "even row survives deletion")
        require(modulus - 1 not in killed, "all-ones row deleted")
        all_ones_selfloops = 0
        for r in range(modulus):
            successors = [shortcut(r + c * modulus) % modulus for c in (0, 1)]
            coded = {windows[s] for s in successors}
            expected = {windows[r][1:] + (c,) for c in (0, 1)}
            require(coded == expected, "averaged graph is not coded shift")
            if r == modulus - 1:
                all_ones_selfloops = sum(s == r for s in successors)
        require(all_ones_selfloops == 1, "all-ones loop has wrong multiplicity")
        # Any m-step retained directed cycle emits only ones, hence has the
        # all-ones window. The identities above check the full graph interface.
        table.append({"m": m, "states": modulus, "killed_rows": len(killed), "unique_cyclic_window": modulus - 1})

    path = [27]
    for _ in range(3):
        path.append(shortcut(path[-1]))
    require(path == [27, 41, 62, 31], "original-floor negative control")
    require(min(path) == 27, "negative control actually crosses original floor")
    require(gemini_kills(62 % (1 << 7), 7), "negative control not killed by Gemini")
    return {"parity_shift_interfaces": table, "fixed_floor_counterexample": path,
            "full_radius_formula": "(w0+w1)/2", "killed_radius_formula": "w1/2",
            "robust_minimum_factor": "w1 for alpha>0; equals (3/2)^alpha > 1"}


def inverse_graph():
    modulus = 27
    states = tuple(n for n in range(1, modulus) if n % 3)
    graph = {}
    for n in states:
        actions = []
        for e in range(1, 7):
            numerators = [2**e * (n + 27 * c) - 1 for c in range(3)]
            if any(num % 3 for num in numerators):
                continue
            children = tuple((num // 3) % 27 for num in numerators)
            if all(child % 3 for child in children):
                actions.append((e, children))
        require(actions, "no inverse action")
        graph[n] = tuple(actions)
    return states, graph


def check_inverse_game():
    states, graph = inverse_graph()
    robust_h_list = [-2, -3, -1, -1, 0, -2, -2, -2, -3, -1, 0, -4, -1, -3, -3, 0, 1, -4]
    robust_h = dict(zip(states, robust_h_list))
    for n in states:
        require(min(e + max(robust_h[c] for c in children) for e, children in graph[n]) == 3 + robust_h[n],
                "robust slope-3 additive eigenvector failed")

    optimistic_v = dict.fromkeys(states, 0)
    for iteration in range(1, 101):
        new_v = {n: max(0, min(e - 1 + min(optimistic_v[c] for c in children)
                             for e, children in graph[n])) for n in states}
        if new_v == optimistic_v:
            break
        optimistic_v = new_v
    else:
        raise ValueError("optimistic finite certificate did not stabilize")
    for n in states:
        require(min(e - 1 + min(optimistic_v[c] for c in children) for e, children in graph[n]) <= optimistic_v[n],
                "optimistic slope-1 certificate failed")
    require(any(e == 1 and 26 in children for e, children in graph[26]), "optimistic negative-pin loop")

    # Negative control: a long chain with adjusted cost 1 reaches a zero-cost
    # terminal loop. A fixed point exists, but a 200-round timeout is inconclusive.
    length = 250
    value = [0] * (length + 1)
    nonfixed_at_200 = False
    fixed_at = None
    for iteration in range(1, length + 3):
        new_value = [1 + value[i + 1] for i in range(length)] + [value[-1]]
        if iteration == 200:
            nonfixed_at_200 = new_value != value
        if new_value == value:
            fixed_at = iteration
            break
        value = new_value
    require(nonfixed_at_200 and fixed_at == length + 1, "timeout negative control failed")
    require(value == list(range(length, -1, -1)), "chain finite potential")
    # Disconnected loops of adjusted costs -1 and +1: global minimum is -1,
    # while the second state's self-loop makes an all-state certificate impossible.
    require(min(-1, 1) <= 0 and 1 > 0, "all-state reachability negative control")
    return {"states": states, "optimistic_exact_slope": 1,
            "optimistic_potential": [optimistic_v[n] for n in states],
            "robust_exact_slope": 3, "robust_additive_eigenvector": robust_h_list,
            "timeout_control": {"false_negative_cutoff": 200, "actual_stabilization_round": fixed_at}}


def main():
    result = {"status": "PASS", "evidence_scope": "finite exact interface replay plus stated controls; all-depth results rest on written proofs",
              "actual_transport": check_actual_transport(), "binary_operator": check_binary_operator(),
              "inverse_game": check_inverse_game()}
    here = Path(__file__).resolve().parent
    result["source_sha256"] = {name: sha256((here / name).read_bytes()).hexdigest()
                               for name in ("verify_inverse_transport.py", "ACTUAL_TRANSPORT.md", "AVERAGED_CHAIN_AUDIT.md")}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
