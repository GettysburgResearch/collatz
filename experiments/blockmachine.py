"""Symbolic block calculus for the -5 phase system.

Words are LSD-first octal digit strings containing at most one PUMPED
BLOCK v^{k+off} with a single symbolic parameter k (thought of as
arbitrarily large).  One macro step (= one state rule + carry
normalization = exactly 3 shortcut Collatz steps) is executed exactly on
this representation.

Carry transducer facts (proved by finite check in carry_facts()):
  * carries lie in 0..8 always;
  * for each octal digit r there is a unique stable carry c*(r) with
    (9r + c*)//8 = c*, and the carry map c -> (9r + c)//8 reaches c*
    after at most 2 digits of a constant-r block;
  * under stable carry, digit r maps to out(r) = (9r + c*(r)) % 8.
      r    : 0 1 2 3 4 5 6 7
      c*(r): 0 1 2 3 5 6 7 8
      out  : 0 2 4 6 1 3 5 7    (out(r) = 2r mod 8 ... no: it's 9r+c* mod 8)

The engine derives until:
  * EXIT: low digit has no state rule in the current phase; or
  * LOOP: a configuration shape recurs (same phase, same concrete digits,
    same block digit) with block offset shifted by delta -- a symbolic
    self-similar loop.  delta > 0 would be an expanding schema
    (a Collatz counterexample by induction); delta = 0 is a periodic
    schedule (excluded by the S7 obstruction for positive values);
    delta < 0 is a consuming loop (finite lifetime ~ k/|delta| periods).

Every symbolic derivation is cross-checked against exact integer
computation at several concrete values of k.
"""

from core import T_iter, value_word, CycleSystem, CYC_M5

S5 = CycleSystem(CYC_M5, names=['A', 'B', 'C'])
PH = {0: 'A', 1: 'B', 2: 'C'}


def carry_facts():
    stable = {}
    out = {}
    for r in range(8):
        # fixed point of c -> (9r+c)//8 on 0..8
        cs = [c for c in range(9) if (9 * r + c) // 8 == c]
        assert len(cs) == 1
        c = cs[0]
        stable[r] = c
        out[r] = (9 * r + c) % 8
        # convergence within 2 steps from any start, carry stays in 0..8
        for c0 in range(9):
            c1 = (9 * r + c0) // 8
            c2 = (9 * r + c1) // 8
            assert 0 <= c1 <= 8 and c2 == stable[r], (r, c0)
    return stable, out


STABLE, OUT = carry_facts()

# segments: ('d', r) concrete digit | ('b', v, off) block v^{k+off}
MARGIN = 6   # block treated as having length k+off with k large; we
             # require k+off >= MARGIN at all times, tracking worst case.


class Exhausted(Exception):
    pass


def low_digit(segs):
    s = segs[0]
    if s[0] == 'd':
        return s[1], segs[1:]
    _, v, off = s
    rest = [('b', v, off - 1)] + segs[1:]
    return v, rest


def push_carry(segs, c, stats):
    """Propagate nonary carry c from the low end through segs; return
    new segs.  Transient digits split off blocks as concrete digits."""
    out = []
    i = 0
    for s in segs:
        if c is None:
            out.append(s)
            continue
        if s[0] == 'd':
            r = s[1]
            out.append(('d', (9 * r + c) % 8))
            c = (9 * r + c) // 8
        else:
            _, v, off = s
            trans = 0
            while c != STABLE[v]:
                out.append(('d', (9 * v + c) % 8))
                c = (9 * v + c) // 8
                off -= 1
                trans += 1
                assert trans <= 2, "carry transducer transient bound broken"
            stats['min_off'] = min(stats.get('min_off', 10 ** 9), off)
            out.append(('b', OUT[v], off))
            c = STABLE[v]     # carry exits the block still stable
    # high end: append octal digits of c
    while c:
        out.append(('d', c % 8))
        c //= 8
    # strip high-end zero digits (but never a block)
    while out and out[-1][0] == 'd' and out[-1][1] == 0:
        out.pop()
    return out


def macro(X, segs, stats):
    r, rest = low_digit(segs)
    if (X, r) not in S5.rules:
        return None                      # EXIT
    Y, c = S5.rules[(X, r)]
    return Y, push_carry(rest, c, stats)


def concretize(segs, k):
    ds = []
    for s in segs:
        if s[0] == 'd':
            ds.append(s[1])
        else:
            _, v, off = s
            assert k + off >= 0
            ds += [v] * (k + off)
    while ds and ds[-1] == 0:
        ds.pop()
    return ds


def shape_key(X, segs):
    """Shape with block offset abstracted out; also return offset."""
    key = [X]
    off0 = None
    for s in segs:
        if s[0] == 'd':
            key.append(('d', s[1]))
        else:
            key.append(('b', s[1]))
            off0 = s[2]
    return tuple(key), off0


def derive(X, segs, max_macro=400):
    """Run macro steps; return record dict."""
    stats = {}
    hist = {}
    trace = [(X, segs)]
    t = 0
    while t < max_macro:
        key, off = shape_key(X, segs)
        if off is not None:
            if key in hist:
                t0, off0 = hist[key]
                return dict(kind='LOOP', delta=off - off0, period=t - t0,
                            enter=t0, X=X, segs=segs, stats=stats, trace=trace)
            hist[key] = (t, off)
        nxt = macro(X, segs, stats)
        if nxt is None:
            return dict(kind='EXIT', steps=t, X=X, segs=segs, stats=stats,
                        trace=trace)
        X, segs = nxt
        trace.append((X, segs))
        t += 1
        offs = [s[2] for s in segs if s[0] == 'b']
        if offs and offs[0] < -120:
            return dict(kind='DRIFT', steps=t, X=X, segs=segs, stats=stats,
                        trace=trace)
        if not any(s[0] == 'b' for s in segs):
            return dict(kind='CONCRETE', steps=t, X=X, segs=segs,
                        stats=stats, trace=trace)
    return dict(kind='TIMEOUT', steps=t, X=X, segs=segs, stats=stats,
                trace=trace)


def crosscheck(X0, segs0, rec, ks=None):
    """Verify the symbolic derivation against exact integers."""
    upto = rec.get('enter', 0) + rec.get('period', 0) if rec['kind'] == 'LOOP' \
        else rec.get('steps', 0)
    if ks is None:
        moff = min([s[2] for (_, sg) in rec['trace'][:upto + 1]
                    for s in sg if s[0] == 'b'] + [0])
        k0 = max(40, -moff + 12)
        ks = (k0, k0 + 1, k0 + 7)
    for k in ks:
        n = S5.config_value(X0, concretize(segs0, k))
        if n <= 0:
            continue
        m, par = T_iter(n, 3 * upto)
        Xf, segsf = rec['trace'][upto]
        assert m == S5.config_value(Xf, concretize(segsf, k)), \
            (X0, segs0, k, upto)
        assert sum(par) == 2 * upto   # density exactly 2/3 in-system
    return True


def fmt(X, segs):
    parts = []
    for s in segs:
        if s[0] == 'd':
            parts.append(str(s[1]))
        else:
            sign = '+' if s[2] >= 0 else '-'
            parts.append(f"{s[1]}^(k{sign}{abs(s[2])})")
    return PH[X] + ' ' + ' '.join(parts) + ' #'


# ----------------------------------------------------------------------
# seed sweep
# ----------------------------------------------------------------------

def seed_sweep(pref_maxlen=2, suff_maxlen=1, verbose=False):
    from itertools import product
    results = []
    seeds = 0
    for X in range(3):
        for v in range(8):
            for plen in range(pref_maxlen + 1):
                for pref in product(range(8), repeat=plen):
                    for slen in range(suff_maxlen + 1):
                        for suf in product(range(1, 8), repeat=slen):
                            segs = [('d', d) for d in pref] + \
                                   [('b', v, 0)] + [('d', d) for d in suf]
                            rec = derive(X, segs)
                            crosscheck(X, segs, rec)
                            seeds += 1
                            results.append((X, tuple(pref), v, tuple(suf), rec))
    return seeds, results


if __name__ == '__main__':
    # reproduce the user's growth gadget symbolically:  A 6^{k+1} #
    rec = derive(0, [('b', 6, 1)])
    print("A 6^(k+1) # derivation:")
    for i, (X, segs) in enumerate(rec['trace']):
        print(f"   t={i}: {fmt(X, segs)}")
    print(f"   -> {rec['kind']}", rec.get('steps'), '\n')
    crosscheck(0, [('b', 6, 1)], rec)

    seeds, results = seed_sweep()
    kinds = {}
    loops = []
    long_exits = []
    for X, pref, v, suf, rec in results:
        kinds[rec['kind']] = kinds.get(rec['kind'], 0) + 1
        if rec['kind'] == 'LOOP':
            loops.append((X, pref, v, suf, rec))
        elif rec['kind'] == 'EXIT' and rec['steps'] >= 4:
            long_exits.append((X, pref, v, suf, rec))
    print(f"seed sweep: {seeds} seeds -> {kinds}")
    print()
    print("== symbolic LOOPS found ==")
    deltas = {}
    for X, pref, v, suf, rec in loops:
        deltas.setdefault((rec['delta'], rec['period']), []).append(
            (X, pref, v, suf, rec))
    for (delta, period), items in sorted(deltas.items()):
        X, pref, v, suf, rec = items[0]
        seed = [('d', d) for d in pref] + [('b', v, 0)] + [('d', d) for d in suf]
        print(f"  delta={delta:+d} per period={period} macro steps"
              f"  ({len(items)} seeds)   e.g. seed {fmt(X, seed)}")
        Xe, segse = rec['trace'][rec['enter']]
        print(f"      loop entered at t={rec['enter']}: {fmt(Xe, segse)}")
    print()
    print("== longest in-system EXIT derivations ==")
    long_exits.sort(key=lambda it: -it[4]['steps'])
    for X, pref, v, suf, rec in long_exits[:12]:
        seed = [('d', d) for d in pref] + [('b', v, 0)] + [('d', d) for d in suf]
        print(f"  {rec['steps']:3d} macro steps: {fmt(X, seed)}"
              f"   exits at {fmt(rec['X'], rec['segs'])}")
