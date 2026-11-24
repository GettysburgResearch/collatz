"""Exact all-translation finite certificates for ordinary synchronous merging.

If a window starts at r + 2**k * h, the pair (p, T**k(n)) computed
at the base window starting at r changes to (p, T**k(n) + 3**p*h).
Thus equal signatures at r remain equal at every such translation.
"""
from collections import Counter, deque


def signature(n, k):
    p = 0
    for _ in range(k):
        if n % 2:
            p += 1
            n = (3 * n + 1) // 2
        else:
            n //= 2
    return p, n


def all_translations(k):
    width = 2**k
    counts = Counter()
    window = deque()
    maximum = 0
    for n in range(1, 2 * width):
        key = signature(n, k)
        window.append(key)
        counts[key] += 1
        if len(window) > width:
            old = window.popleft()
            counts[old] -= 1
            if counts[old] == 0:
                del counts[old]
        if len(window) == width:
            maximum = max(maximum, len(counts))
    return width, maximum, width - maximum


if __name__ == "__main__":
    for k in (8, 12, 16):
        print(k, *all_translations(k))
