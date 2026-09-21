#!/usr/bin/env python3
"""Whole-progression replay of EPT-005 examples, independent of run.py."""
import json


def affine(a, b, word):
    for ch in word:
        if a % 2 != 0 or b % 2 != int(ch):
            raise ValueError('nonuniform or wrong parity')
        if ch == '1':
            a, b = 3*a, 3*b+1
        a, b = a//2, b//2
    return a, b


def main():
    cases = [(2916, 1731, 2048, 1215, '1111110100', 4374, 2597),
             (8748, 4647, 4096, 2175, '11111110100', 13122, 6971),
             (8748, 111, 8192, 103, '111011110100', 13122, 167)]
    for a, b, c, d, word, slope, constant in cases:
        if not (0 < c < a and 0 < d < b and a % 12 == 0 and b % 12 == 3):
            raise ValueError('whole original-source order or congruence')
        if affine(a, b, '1') != (slope, constant) or affine(c, d, word) != (slope, constant):
            raise ValueError('whole affine endpoint')
    for n in range(88452, 88456):
        for _ in range(19):
            n = (3*n+1)//2 if n % 2 else n//2
        if n != 41:
            raise ValueError('transplanted interval')
    print(json.dumps({'status': 'PASS', 'whole_original_cylinders': 3,
                      'four_consecutive_ancestors_of_41': 4}, sort_keys=True))


if __name__ == '__main__':
    main()
