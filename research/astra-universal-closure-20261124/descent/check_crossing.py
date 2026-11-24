"""Replay physical clocks, meeting points, and finite residue permutations."""


def step(z):
    return (3*z + 1)//2 if z % 2 else z//2


def run(z, count):
    for _ in range(count):
        z = step(z)
    return z


def first_hit(z):
    for clock in range(5000):
        if z == 1:
            return clock
        z = step(z)
    raise ValueError("finite replay exceeded its clock limit")


def require(condition, message):
    if not condition:
        raise ValueError(message)


for t in range(4):
    m = 56 + 72*t
    n = 7*2**m - 1
    q = n//3
    u = (7*3**(m-1) - 1)//4
    y = 6*u + 1
    require(n == 3*q and n % 27 == 0 and u % 8 == 3, "initial residues")
    require(run(n, m+1) == y > 2*n, "first crossing")
    require(run((n-1)//2, m+1) == u, "synchronized lower arm")
    require(run(y, 4) == run(3*u, 3) == run(n, m+5), "ordinary merger")
    require(first_hit(q) == m+11 and u >= 2**(83+108*t), "clock comparison")
    print(f"m={m} H(q)={first_hit(q)} H(u)={first_hit(u)}"
          f" H(n)={first_hit(n)} H(3u)={first_hit(3*u)}")

for k in range(1, 13):
    modulus = 2**k
    # 32*T^3(u) = 9*(7*3^(m-1)) + 11.
    values = {
        ((63*pow(3, 55+72*t, 32*modulus)+11)//32) % modulus
        for t in range(modulus)
    }
    require(len(values) == modulus, "finite permutation")
print("post-return residues cover every class at k=1 through 12")
