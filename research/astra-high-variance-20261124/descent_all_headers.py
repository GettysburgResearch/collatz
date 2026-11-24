"""All residual headers followed by arbitrary paid-run lengths."""
from descent_macro import certificate, check, source

# Header, M, d, free signed center, repeating paid carry, paid exit length,
# entrance exponent and signed comparison at the first paid boundary.
PROFILES = (
    ("PPLLL", 2442741, 21, -7, 7, 4, -9, -1),
    ("PLLPP", 103789, 17, -5, 10, 4, -7, -1),
    ("PLLPL", 5367, 12, -7, 20, 3, -9, -10),
)


def check_profile(row):
    name, m, d, center, paid, exit_len, ell, anchor = row
    den = 1 << d
    free = 7*m + center*den
    check((paid*den-5*m) % 23 == 0, "fractional interior bias")
    inner = (paid*den-5*m)//23
    check(3*m+min(free, inner) > 2*den, "positive tail outside unit cycle")
    edges = [("L", free, free)]
    edges.extend(("L"*7+"P"*j, free, free) for j in range(1, exit_len+1))
    edges.extend([("L"*7+"P", free, inner), ("P", inner, inner),
                  ("P"*exit_len, inner, free)])
    print(name, "M", m, "D", den, "biases", free, inner)
    for word, old, new in edges:
        a, p, c = source(word)
        numer = m*c+(new << a)-3**p*old
        check(numer % den == 0, "fractional carry")
        print(word, old, new, certificate(a, p, numer//den)[2])
    a, p, c = source(name)
    b, u = a+d-1, p-ell
    target = m*((c-7*3**p+7*2**a)//2)+(center << b)-anchor*3**u
    print("entrance", b, u, certificate(b, u, target)[2])
    if anchor == -1:
        check(8*m <= 5*(1 << (13-ell)), "large-r floor")
    else:
        check(8*m < 5*(1 << 15), "signed entrance floor")
    for r in range(12):
        short = "L"*r+name[:name.index("P", 1)+1]
        a, p, c = source(short)
        check(4*3**p < 3*(1 << a), "direct slope")
        check(4*(3**p*17+c)+3*(1 << a) <= 3*17*(1 << a), "direct floor")


if __name__ == "__main__":
    for row in PROFILES:
        check_profile(row)
