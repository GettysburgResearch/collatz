# T-9701 verification: truncated kernel dimension = number of truncated weak components.
# Exact arithmetic, standard library only, deterministic. Runs in ~0.1s.
from fractions import Fraction

def T(n):  # shortcut Collatz map on N_0
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2

def U(n):  # 3n-1 shortcut control map on positive integers
    return n // 2 if n % 2 == 0 else (3 * n - 1) // 2

def truncated_edges(f, verts):
    vs = set(verts)
    return [(m, f(m)) for m in verts if f(m) in vs]

def component_count_and_find(verts, edges):
    parent = {v: v for v in verts}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return len({find(v) for v in verts}), find

def kernel_dim_gf2(verts, edges):
    # rows of truncated (F - I) over GF(2): row for edge (m,T(m)) has 1s at m and T(m);
    # the self-loop at 0 gives the zero row.
    idx = {v: i for i, v in enumerate(sorted(verts))}
    n = len(verts)
    pivots = {}
    rank = 0
    for a, b in edges:
        row = 0 if a == b else (1 << idx[a]) | (1 << idx[b])
        while row:
            c = row.bit_length() - 1
            if c in pivots:
                row ^= pivots[c]
            else:
                pivots[c] = row
                rank += 1
                break
    return n - rank

def kernel_dim_Q(verts, edges):
    # sparse exact RREF over Q; row for edge (m,T(m)): +1 at column T(m), -1 at column m.
    idx = {v: i for i, v in enumerate(sorted(verts))}
    n = len(verts)
    pivots = {}
    rank = 0
    for a, b in edges:
        if a == b:
            continue
        row = {idx[b]: Fraction(1), idx[a]: Fraction(-1)}
        while row:
            c = max(row)
            if c in pivots:
                coef = row.pop(c)
                for cc, vv in pivots[c].items():
                    if cc == c:
                        continue
                    nv = row.get(cc, Fraction(0)) - coef * vv
                    if nv:
                        row[cc] = nv
                    else:
                        row.pop(cc, None)
            else:
                coef = row[c]
                pivots[c] = {cc: vv / coef for cc, vv in row.items()}
                rank += 1
                break
    return n - rank

def check(name, f, verts):
    edges = truncated_edges(f, verts)
    c, find = component_count_and_find(verts, edges)
    k2 = kernel_dim_gf2(verts, edges)
    kQ = kernel_dim_Q(verts, edges)
    assert k2 == c, (name, "GF(2) kernel dim", k2, "components", c)
    assert kQ == c, (name, "Q kernel dim", kQ, "components", c)
    print(f"{name}: |V|={len(verts)} edges={len(edges)} components={c} "
          f"ker_GF2={k2} ker_Q={kQ}  OK")
    return find

N = 2000

# --- Collatz shortcut T on {0..N} ---
find_T = check("T (3n+1) on {0..N}", T, range(0, N + 1))
# 0-component bookkeeping: T(0)=0 and no m in 1..N maps to 0.
assert T(0) == 0 and all(T(m) != 0 for m in range(1, N + 1))
# {0} separate; 1 and 2 share a component distinct from 0's.
assert find_T(0) != find_T(1) and find_T(1) == find_T(2)
print("T control facts: T^{-1}(0)={0} on range; comp(0)!=comp(1)=comp(2)  OK")

# --- 3n-1 control U on {1..N} ---
find_U = check("U (3n-1) on {1..N}", U, range(1, N + 1))
assert U(1) == 1
c5 = {5, 7, 10}
c17 = {17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34}
for x in c5:
    assert U(x) in c5
for x in c17:
    assert U(x) in c17
r1, r5, r17 = find_U(1), find_U(5), find_U(17)
assert len({r1, r5, r17}) == 3
assert all(find_U(x) == r5 for x in c5) and all(find_U(x) == r17 for x in c17)
print("U control facts: cycles {1},{5,7,10},{17,...,34} verified; 3 distinct components  OK")

print("ALL CHECKS PASSED")
