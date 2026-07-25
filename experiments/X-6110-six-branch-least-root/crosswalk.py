# Independent verification of the six-branch rational-base chart <-> Collatz crosswalk.
P = 3**12; Q = 2**19
A = [229376, 258048, 290304, 326592, 367416, 413343]

print("P =", P, " Q =", Q, " P-Q =", P-Q)
print("digit structure a_i = 7*3^(2i)*2^(15-3i)?")
for i,a in enumerate(A):
    print(f"  i={i} a={a}  7*3^{2*i}*2^{15-3*i} = {7*3**(2*i)*2**(15-3*i)}  match={a==7*3**(2*i)*2**(15-3*i)}  v2={(a & -a).bit_length()-1}")

def T(n):  # shortcut Collatz
    return (3*n+1)//2 if n % 2 else n//2

# For each digit, find the least positive x with d_0 = a, then test the physical claim n=6x-5.
invP = pow(P, -1, Q)
print("\n--- per-branch physical replay test (n = 6x-5) ---")
for i,a in enumerate(A):
    x = (-a * invP) % Q
    if x == 0: x = Q
    d = (Q*((P*x + Q - 1)//Q) - P*x)
    assert d == a, (d,a)
    xn = (P*x + a)//Q
    n  = 6*x - 5
    nn = 6*xn - 5
    # run 19 shortcut steps from n, count odd steps
    m = n; odd = 0; parity=[]
    for _ in range(19):
        parity.append(m % 2); odd += m % 2; m = T(m)
    print(f"  i={i} a={a} x={x} -> x'={xn}")
    print(f"      n={n}  T^19(n)={m}  expected 6x'-5={nn}  MATCH={m==nn}  odd_steps={odd}  n_odd={n%2}")
    print(f"      parity word={''.join(map(str,parity))}")
