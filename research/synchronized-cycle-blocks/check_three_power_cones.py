"""Rational two-variable vertex certificates for the three-power theorem."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


@dataclass(frozen=True)
class Form:
    """Affine form in the normalized gains G,J."""
    constant: F = F(0)
    g: F = F(0)
    j: F = F(0)

    def __add__(self, other):
        if not isinstance(other, Form):
            other = Form(F(other))
        return Form(self.constant+other.constant, self.g+other.g, self.j+other.j)

    __radd__ = __add__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, scalar):
        return Form(self.constant*scalar, self.g*scalar, self.j*scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        return self * (F(1)/scalar)

    def at(self, point):
        g, j = point
        return self.constant+self.g*g+self.j*j


def vertices(constraints):
    result = set()
    for l, r in combinations(constraints, 2):
        determinant = l.g*r.j-r.g*l.j
        if not determinant:
            continue
        g = (l.j*r.constant-r.j*l.constant)/determinant
        j = (r.g*l.constant-l.g*r.constant)/determinant
        if all(line.at((g, j)) >= 0 for line in constraints):
            result.add((g, j))
    return result


def lower(forms, constraints):
    points = vertices(constraints)
    if not points:
        return None
    return min(form.at(point) for form in forms for point in points)


def require(test):
    if not test:
        raise AssertionError("failed rational polytope certificate")


def check(a, b, method, loss=0):
    c = F(485, 306)
    require(3**306 < 2**485)
    gamma = c-1
    g = Form(g=F(1))
    j = Form(j=F(1))
    da = a*gamma/(a-c)
    db = b*gamma/(b-c)
    drop = (g+j)/2
    m = 1-g/da
    n = 1+g-j/db
    p = drop-1/gamma
    domain = [g, j, m, n, p]
    require(lower((g, j), domain) > F(1, 10))

    full = 1+g+j-a*m-b*n-2*p-loss
    transport = [term-2*m-p for term in (g, drop, (1+g)/c)]
    if method == "transport":
        require(lower(transport, domain) > F(1, 10))
        return 1
    if method == "two sums":
        require(lower([j-2*n-2*p, j-g], domain) > F(1, 10))
        return 1
    if method == "full":
        require(lower([full], domain) > (F(1, 10) if loss else 1))
    else:
        margin = lower(transport, domain+[-full])
        require(margin is None or margin > F(1, 10))

    # Remove the largest descending term. Only its partner can
    # coincide in exponential height with a retained ascending term.
    upper_scales = [1+g-i*g/a for i in range(a)]
    upper_scales += [1+g+j-i*j/b for i in range(b)]
    exceptional_rays = 0
    for term in upper_scales:
        difference = 1+drop-term
        restricted = domain+[difference, -difference]
        if not vertices(restricted):
            continue
        exceptional_rays += 1
        require(method == "full or transport")
        require(lower(transport, restricted) > F(1, 10))
    return exceptional_rays


if __name__ == "__main__":
    for a, b, method in ((2, 2, "full or transport"), (2, 3, "full or transport"),
                        (3, 2, "full"), (2, 4, "transport"), (4, 2, "two sums")):
        print(a, b, method, check(a, b, method))
    for a, b, method in ((2, 3, "full or transport"), (3, 2, "full")):
        print(a, b, "one normalized unit of gap error", check(a, b, method, loss=1))
