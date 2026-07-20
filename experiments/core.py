"""Core exact machinery for the Collatz symbolic-rewrite program.

Everything here is exact integer / rational arithmetic (fractions.Fraction),
no floating point in any verification path.

Conventions
-----------
* Shortcut map  T(n) = n/2 (n even),  (3n+1)/2 (n odd).
  Extended to rationals with ODD denominator: parity(p/q) := p*q^{-1} mod 2
  = parity of p (since q odd).
* Words are digit lists, LEAST significant digit first (LSD-first).
* value_word(digits, base) = sum digits[i]*base^i.
* Phase configuration in a negative-cycle system with cycle element -s:
  "X w"  denotes  n = B*q - s_X  with q = value of octal (base-B) word w,
  where B = 2^p is the modulus of the cycle system.
"""

from fractions import Fraction


# ----------------------------------------------------------------------
# the shortcut map
# ----------------------------------------------------------------------

def is_odd(x):
    if isinstance(x, Fraction):
        assert x.denominator % 2 == 1, "need odd denominator"
        return x.numerator % 2 == 1
    return x % 2 == 1


def T(x):
    if is_odd(x):
        return (3 * x + 1) / 2 if isinstance(x, Fraction) else (3 * x + 1) // 2
    return x / 2 if isinstance(x, Fraction) else x // 2


def T_iter(x, k):
    """Return (T^k(x), parity word as list of 0/1)."""
    par = []
    for _ in range(k):
        p = 1 if is_odd(x) else 0
        par.append(p)
        x = T(x)
    return x, par


def orbit_until_repeat(x, cap=10**6):
    """Follow T until a value repeats; return (transient list, cycle list)."""
    seen = {}
    seq = []
    while x not in seen and len(seq) < cap:
        seen[x] = len(seq)
        seq.append(x)
        x = T(x)
    if x not in seen:
        return seq, None
    i = seen[x]
    return seq[:i], seq[i:]


# ----------------------------------------------------------------------
# words
# ----------------------------------------------------------------------

def value_word(digits, base):
    v = 0
    for i, d in enumerate(digits):
        v += d * base ** i
    return v


def to_word(n, base, length=None):
    assert n >= 0
    ds = []
    while n:
        ds.append(n % base)
        n //= base
    if length is not None:
        ds += [0] * (length - len(ds))
    return ds


# ----------------------------------------------------------------------
# radix replacement:  T^L(2^L x + r) = 3^a x + c
# ----------------------------------------------------------------------

def radix_replace(L, r):
    """Return (a, c) with T^L(2^L x + r) = 3^a x + c for all x >= 0.

    Follows the (A,B) evolution from the proof of the radix-replacement
    lemma; also returns the parity word of the block."""
    A, B = 2 ** L, r
    par = []
    for _ in range(L):
        assert A % 2 == 0
        if B % 2 == 0:
            A, B = A // 2, B // 2
            par.append(0)
        else:
            A, B = 3 * A // 2, (3 * B + 1) // 2
            par.append(1)
        assert 0 <= B < A
    a = 0
    AA = A
    while AA % 3 == 0:
        AA //= 3
        a += 1
    assert AA == 1 and A == 3 ** a
    return a, B, par


# ----------------------------------------------------------------------
# negative-cycle phase systems (amplifier compiler)
# ----------------------------------------------------------------------

class CycleSystem:
    """Phase rewrite system built from a negative cycle of T.

    cycle: list of cycle elements (negative integers), in orbit order,
           starting anywhere:  T(cycle[i]) = cycle[i+1 mod p].
    Offsets s_i = -cycle[i] > 0.
    p = len(cycle), a = number of odd elements, Bmod = 2^p, Nmod = 3^a.
    Identity: T^p(Bmod*q - s_i) = Nmod*q - s_i  for all integers q.
    Phase transition (X -> Y) allowed iff q = Bmod*x + r with
      Nmod*r == s_X - s_Y (mod Bmod), and then emitted carry
      c = (Nmod*r - s_X + s_Y)//Bmod,  0 <= c <= Nmod-1... (c < Nmod).
    Carry normalization:  N_c O_r -> O_{(c+r) % Bmod} N_{ r*Nmod... }
    -- careful: N_c(O_r(x)) = Nmod*(Bmod*x + r) + c
              = Bmod*(Nmod*x + (Nmod*r + c) // Bmod ... no:
    We need the rule representing 9(8x+r)+c = 8(9x + t) + u.
    9*(8x+r)+c = 72x + 9r + c;  = 8*(9x + (9r+c - u)/8 ...) choose
    u = (r + ((c + r) // 8)) ??? -- match the user's boxed rule:
      N_c O_r -> O_{(c+r) mod 8} N_{ r + floor((c+r)/8) }.
    Check: RHS value = 9*... The rule asserts both sides represent
    9(8x+r)+c with digits low = (c+r) mod 8 and new carry
    c' = r + (c+r)//8:  8*(9x + c') + ((c+r) mod 8)
       = 72x + 8r + 8*((c+r)//8) + (c+r) mod 8 = 72x + 8r + c + r
       = 72x + 9r + c.  Correct -- and it generalizes:
      N_c O_r -> O_{(c+r) mod B} N_{ r*(N-B)/B ... }
    General check with N = Nmod, B = Bmod:
      N*(B*x + r) + c = B*(N*x + c') + d  where d = (c + (N-B)*r) mod B?
    Simplest: total low part = N*r + c; d = (N*r + c) % B; c' = (N*r + c)//B.
    That is the plain schoolbook carry; the user's elegant form works
    because for B=8, N=9:  9r + c = 8r + (r + c), (9r+c)%8 = (r+c)%8,
    (9r+c)//8 = r + (c+r)//8.  We implement the schoolbook version.
    Carry range: c <= N-1 initially; after: c' = (N*r + c)//B
      <= (N*(B-1) + N-1)/B = N - 1/B  => c' <= N-1.  Stable.
    """

    def __init__(self, cycle, names=None):
        p = len(cycle)
        for i, v in enumerate(cycle):
            assert T(v) == cycle[(i + 1) % p], "not a T-cycle"
        self.cycle = cycle
        self.p = p
        self.a = sum(1 for v in cycle if is_odd(v))
        self.B = 2 ** p
        self.N = 3 ** self.a
        self.s = [-v for v in cycle]
        assert all(si > 0 for si in self.s), "cycle must be negative"
        self.names = names or [chr(ord('A') + i) for i in range(p)]
        # phase transition table: rules[(X, r)] = (Y, c)
        self.rules = {}
        for X in range(p):
            for Y in range(p):
                # need N*r == s_X - s_Y (mod B); N odd => invertible
                r = (pow(self.N, -1, self.B) * (self.s[X] - self.s[Y])) % self.B
                c = (self.N * r - self.s[X] + self.s[Y]) // self.B
                assert (X, r) not in self.rules
                self.rules[(X, r)] = (Y, c)

    def config_value(self, X, word):
        return self.B * value_word(word, self.B) - self.s[X]

    def normalize_carry(self, word, pos, c):
        """Word has a nonary digit N_c inserted before word[pos:]; push it
        to the high end.  Returns new word (list of base-B digits)."""
        word = list(word)
        i = pos
        while i < len(word):
            r = word[i]
            tot = self.N * r + c
            word[i] = tot % self.B
            c = tot // self.B
            i += 1
        # high end: N_c # -> base-B digits of c
        while c:
            word.append(c % self.B)
            c //= self.B
        while word and word[-1] == 0:
            word.pop()
        return word

    def macro_step(self, X, word):
        """One state rule + normalization = p shortcut steps.
        Returns (Y, new word) or None if the configuration exits the
        subsystem (low digit not in the allowed set)."""
        r = word[0] if word else 0
        if (X, r) not in self.rules:
            return None
        Y, c = self.rules[(X, r)]
        rest = word[1:]
        return Y, self.normalize_carry(rest, 0, c)

    def verify_macro(self, X, word):
        """Check macro_step against p literal shortcut steps."""
        n = self.config_value(X, word)
        out = self.macro_step(X, word)
        m, _ = T_iter(n, self.p)
        if out is None:
            return m  # exited; caller handles
        Y, w2 = out
        assert m == self.config_value(Y, w2), (X, word, out, n, m)
        return out


# the three known negative cycles of the shortcut map
CYC_M1 = [-1]
CYC_M5 = [-5, -7, -10]
CYC_M17 = [-17, -25, -37, -55, -82, -41, -61, -91, -136, -68, -34]


def cycle_check():
    for cyc in (CYC_M1, CYC_M5, CYC_M17):
        p = len(cyc)
        for i, v in enumerate(cyc):
            assert T(v) == cyc[(i + 1) % p]
    return True


LOG32 = None  # do not use floats in verification paths


def supercritical(cycle):
    """3^a > 2^p ?"""
    p = len(cycle)
    a = sum(1 for v in cycle if is_odd(v))
    return 3 ** a > 2 ** p, a, p
