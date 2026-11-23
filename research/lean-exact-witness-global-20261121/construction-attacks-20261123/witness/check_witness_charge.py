#!/usr/bin/env python3
"""Exact finite controls for WitnessCharge.lean; no convergence extrapolation."""
from __future__ import annotations

from collections import deque
from hashlib import sha256
import json
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def prefix(n: int, length: int) -> tuple[int, int, list[int]]:
    odd = 0
    bits = []
    for _ in range(length):
        bits.append(n % 2)
        odd += n % 2
        n = step(n)
    return n, odd, bits


def witness(n: int) -> dict:
    source = n
    states = [n]
    bits = []
    while n != 1:
        require(len(bits) < 100000, "finite control exceeded its explicit replay cap")
        bits.append(n % 2)
        n = step(n)
        states.append(n)
    L, r = len(bits), sum(bits)
    P, C = affine(bits)
    require(P*source + C == 2**L, "complete witness affine identity")
    return dict(n=source, L=L, r=r, charge=2*r-L, states=states, bits=bits,
                future_states=[source], future_odds=[0])


def affine(bits: list[int]) -> tuple[int, int]:
    P, C = 1, 0
    for i, e in enumerate(bits):
        require(e in (0, 1), "nonbinary parity letter")
        if e:
            P *= 3
            C = 3*C + 2**i
    return P, C


def future(w: dict, k: int) -> tuple[int, int]:
    while len(w['future_states']) <= k:
        last = w['future_states'][-1]
        w['future_states'].append(step(last))
        w['future_odds'].append(w['future_odds'][-1] + last % 2)
    return w['future_states'][k], w['future_odds'][k]


def half_oracle(a: dict, b: dict) -> int | None:
    # After these two complete finite witnesses, both paths are in the
    # closed 1<->2 cycle. Two further clocks cover its entire periodic tail.
    for l in range(max(a['L'], b['L']) + 3):
        x, p = future(a, l+1)
        y, q = future(b, l)
        if x == y and p == q:
            return l
    return None


def power_oracle(a: int, b: int, pa: dict, pb: dict) -> int | None:
    for k in range(max(pa['L'], pb['L']) + 3):
        x, p = future(pa, k)
        y, q = future(pb, k)
        if x == y and p+a == q+b:
            return k
    return None


def exact_edit_distance(a: dict, b: dict) -> dict:
    aa, bb = a['states'], b['states']
    require(len(set(aa)) == len(aa) and len(set(bb)) == len(bb), "first-hit uniqueness")
    ia, ib = {n: i for i, n in enumerate(aa)}, {n: i for i, n in enumerate(bb)}
    na = [ia[step(n)] for n in aa]
    nb = [ib[step(n)] for n in bb]
    start = (0, 0)
    queue = deque([(0, start)])
    distance = {start: 0}
    parent: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}
    goal = None
    edges = 0
    while queue:
        cost, state = queue.popleft()
        if distance[state] != cost:
            continue
        i, j = state
        if aa[i] == bb[j]:
            goal = state
            break
        successors = [((na[i], j), 1, 'L'), ((i, nb[j]), 1, 'R')]
        if aa[i] % 2 == bb[j] % 2:
            successors.append(((na[i], nb[j]), 0, '='))
        for target, weight, letter in successors:
            edges += 1
            candidate = cost + weight
            if candidate < distance.get(target, 10**20):
                distance[target] = candidate
                parent[target] = (state, letter)
                if weight:
                    queue.append((candidate, target))
                else:
                    queue.appendleft((candidate, target))
    require(goal is not None, "known convergent controls must merge")
    letters = []
    current = goal
    while current != start:
        current, letter = parent[current]
        letters.append(letter)
    letters.reverse()
    x, y, counted = a['n'], b['n'], 0
    for letter in letters:
        if letter == '=':
            require(x % 2 == y % 2, "matched-parity guard")
            x, y = step(x), step(y)
        elif letter == 'L':
            x, counted = step(x), counted+1
        else:
            y, counted = step(y), counted+1
    require(x == y and counted == distance[goal], "literal optimal alignment replay")
    require(abs(a['charge']-b['charge']) <= counted, "charge lower potential")
    return dict(minimum_edits=counted, alignment_columns=len(letters),
                full_closed_product=len(aa)*len(bb), explored_states=len(distance),
                explored_edges=edges,
                alignment_sha256=sha256(''.join(letters).encode()).hexdigest(),
                endpoint=x)


def main() -> None:
    cycle_controls = cylinder_controls = half_controls = lifted_controls = 0
    for n in range(1, 129):
        w = witness(n)
        for pad in range(5):
            endpoint, r, _ = prefix(n, w['L']+2*pad)
            require(endpoint == 1 and r == w['r']+pad, "actual terminal padding")
            require(2*r-(w['L']+2*pad) == w['charge'], "padding charge")
            cycle_controls += 1
    for n in range(1, 65):
        for k in range(13):
            end, p, _ = prefix(n, k)
            for t in (0, 1, 3):
                new, q, _ = prefix(n+2**k*t, k)
                require(new == end+3**p*t and q == p, "exact ordinary cylinder lift")
                cylinder_controls += 1

    half_rows = []
    half_sources = [5] + [x for x in range(129, 8194, 128) if x % 512 != 1]
    for x in half_sources:
        y = (x+1)//2
        a, b = witness(x), witness(y)
        predicted = a['charge']+1 == b['charge']
        oracle = half_oracle(a, b)
        require(predicted == (oracle is not None), "all-clock half-germ classification")
        half_controls += 1
        if predicted:
            L = a['L']+2*b['r']
            M = b['L']+2*a['r']
            require(L == M+1, "constructive padding clocks")
            px, py = prefix(x, L), prefix(y, M)
            require(px[0] == py[0] == 1 and px[1] == py[1], "constructive germ")
            A, C = affine(px[2])
            B, D = affine(py[2])
            require(A == B and C == A+2*D, "full symbolic affine identity")
            for t in (0, 1, 3):
                xx, yy = x+2**L*t, y+2**M*t
                require((xx+1)//2 == yy, "unchanged half target")
                require(prefix(xx, L)[0] == prefix(yy, M)[0], "lifted family replay")
                lifted_controls += 1
        if x in (5, 129, 257, 385):
            half_rows.append(dict(x=x, y=y, source_charge=a['charge'],
                                  target_charge=b['charge'], germ=predicted,
                                  target_germ_clock=oracle))

    powers = {m: witness(3**m+1) for m in range(1, 61)}
    power_controls = positive_power_germs = 0
    for a in range(1, 61):
        for b in range(a+1, 61):
            ja, jb = 2*a+powers[a]['charge'], 2*b+powers[b]['charge']
            oracle = power_oracle(a, b, powers[a], powers[b])
            require((ja == jb) == (oracle is not None), "all-clock power-germ classification")
            power_controls += 1
            if ja == jb:
                positive_power_germs += 1
                L = powers[a]['L']+2*(powers[b]['r']+b)
                M = powers[b]['L']+2*(powers[a]['r']+a)
                require(L == M, "power-germ padding clocks")
                require(prefix(powers[a]['n'], L)[1]+a ==
                        prefix(powers[b]['n'], M)[1]+b, "power-germ full coefficients")

    # An actual positive infinite family: every parameter gives an exact
    # merger, and the polynomial coefficients as well as its values agree.
    positive_cells = []
    for t in range(12):
        left, right = prefix(256*t+146, 8), prefix(768*t+436, 8)
        require(left[0] == right[0] == 81*t+47, "power-drop cell")
        require(left[1] == 4 and right[1] == 3, "power-drop derivative counts")
        positive_cells.append(t)
    P, C = affine(prefix(146, 8)[2])
    Q, D = affine(prefix(436, 8)[2])
    require(P == 81 and Q == 27 and C == 206 and D == 260, "symbolic cell coefficients")

    source_family = []
    for k in range(1, 13):
        m, B = 27*k, 54*k+8
        require((4**m-1) % 81 == 0, "retained integral parameter")
        K = (4**m-1)//81
        x, y = 256*K+1, 128*K+1
        require(x % 512 == 257 and 81*x+175 == 2**B, "original four-odd tuple")
        sx, sy = prefix(x, B), prefix(y, 2*m+7)
        require(sx[0] == 1 and sx[1] == 4, "literal four-step source")
        require(sy[0] == 3**m+1 and sy[1] == m+4, "literal target power prefix")
        require(3**(3*(9*k))+1 < 2**(5*(9*k)), "unbounded edit-budget inequality")
        source_family.append(dict(k=k, m=m, source_odd_steps=4,
                                  source_clock=B, forced_target_clock=2*m+7,
                                  every_successful_alignment_has_at_least=9*k+2))

    # The new all-policy finite-seed barrier does not run the proposed
    # larger target. It checks only already-certified seed profiles and
    # the exact height inequality used by the universal theorem.
    seed_budget = max(2*m+powers[m]['charge'] for m in range(1, 28))
    barrier_h = seed_budget+1
    require(3**(3*barrier_h)+1 < 2**(5*barrier_h), "finite-seed barrier height")
    require(all(2*m+powers[m]['charge'] <= barrier_h for m in range(1, 28)),
            "finite-seed charge budget")

    K = (4**27-1)//81
    a, b = witness(256*K+1), witness(128*K+1)
    edit = exact_edit_distance(a, b)
    require(edit['minimum_edits'] >= 11, "new four-step edit lower bound")

    # Explicit rejection controls distinguish charge from parity and
    # a pointwise ordinary merger from an affine family.
    rejected = 0
    bad = [(129, 65), (385, 193)]
    for x, y in bad:
        a0, b0 = witness(x), witness(y)
        require(a0['charge']+1 != b0['charge'], "damaged half-germ must fail")
        rejected += 1
    require((witness(385)['L']-witness(193)['L']) % 2 == 1,
            "phase-only false positive remains visible")
    require(2*27+powers[27]['charge'] not in
            [2*m+powers[m]['charge'] for m in range(1, 27)], "first critical power-drop failure")
    rejected += 1
    require(4 < 11, "source odd-step count cannot pay the required edit budget")
    rejected += 1

    here = Path(__file__).resolve().parent
    sources = {}
    for name in ('WitnessCharge.lean', 'WITNESS_CHARGE_AND_POWER_INDUCTION.md', Path(__file__).name):
        path = here/name
        sources[name] = sha256(path.read_bytes()).hexdigest()
    print(json.dumps(dict(
        scope='Exact finite controls; the unrestricted conclusions use the written proofs and Lean theorems.',
        source_sha256=sources, cycle_controls=cycle_controls,
        cylinder_controls=cylinder_controls, half_classifications=half_controls,
        lifted_family_controls=lifted_controls, half_examples=half_rows,
        power_classifications=power_controls, positive_power_germs=positive_power_germs,
        positive_affine_cell_parameters=len(positive_cells),
        retained_four_step_family=source_family,
        power_signature_rows=[dict(m=m, L=powers[m]['L'], r=powers[m]['r'],
                                   signature=2*m+powers[m]['charge']) for m in range(1, 28)],
        finite_seed_barrier=dict(seed_exponents=list(range(1, 28)),
                                 maximum_signature=seed_budget,
                                 excluded_exponent=3*barrier_h,
                                 target_convergence_used=False),
        first_four_step_exact_edit_control=dict(source=a['n'], target=b['n'],
                                               source_clock=a['L'], target_clock=b['L'],
                                               source_charge=a['charge'], target_charge=b['charge'],
                                               **edit),
        rejected_strengthenings=rejected), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
