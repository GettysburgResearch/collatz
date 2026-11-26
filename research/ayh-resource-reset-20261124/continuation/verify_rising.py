"""Exact integer replay of long, rising first returns to the eight-excess section."""

def exponent(n):
    return (n & -n).bit_length() - 1


def critical(n):
    d = n.bit_length() - 1
    e = exponent(3*n + 1)
    return n % 2 == 1 and (d+1)*(n-2**d) <= 70*2**d and d+1 <= 5*e <= d+8


def step(n):
    return (3*n+1)//2 if n % 2 else n//2


def rising(q, a):
    # The theorem takes a/q close to log_2(3). The checks below are all exact.
    k, d = q-1, 2*(q-1)
    e = (d+5)//5
    D = d-e-k+a
    f = (D+5)//5
    modulus = 2**(f+1)
    c = ((2**f+2)*pow(3, -(k+1), modulus)) % modulus
    c += ((1+2**e-2**k*c)*pow(2**k*modulus, -1, 3) % 3)*modulus
    low = (3*2**(d-e-k)*(q+3) + q-1)//q
    stride = 3*modulus
    c += ((low-c+stride-1)//stride)*stride
    u = 2**k*c - 1
    n, rem = divmod(2**e*u-1, 3)
    v = 3**k*c - 1
    if rem or n.bit_length()-1 != d or v.bit_length()-1 != D:
        raise AssertionError("octaves or integrality")
    if not critical(n) or not critical(v) or v**25 <= n**27:
        raise AssertionError("critical endpoints or power growth")
    x = n
    for t in range(1, e+k+1):
        x = step(x)
        if t == e and x != u:
            raise AssertionError("missing odd endpoint")
        if t < e+k and critical(x):
            raise AssertionError("earlier critical return")
    if x != v:
        raise AssertionError("wrong physical endpoint")
    return q, d, e, k, D, f, e+k


if __name__ == "__main__":
    print("Q d e k D f clocks")
    for q, a in ((53, 84), (306,485), (665,1054)):
        print(*rising(q, a))
