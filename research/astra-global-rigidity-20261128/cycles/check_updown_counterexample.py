"""Replay a self-contained exact counterexample to Vasilyev's Question 7.1."""

from pathlib import Path
import re


STEPS = 298
START = 4
UP_MASK = int('39babef0fd2abcd777de1a6adf8addcdd39b6babb5b67b2ddefe072dadcdd5f7d0eefdd7b', 16)


LARGE_MASK = int(
    '3d3197c6eb56fd6b5fffc05e34d3adb3e375baf956bfc335bb36bd6cd75ceddc5d6b6b5d6d6de5766defc5fa'
    '85bd36e6dfbf8f59e2e29ff69dfa7e0d25ad6d6dd5bfab17c9eb3af5cadafba8f6b35b5deaadb5dead2f55b9'
    'b735f4bd5bdd1796dbae75ab7f7ee195c5ad6daf3ab5f79756cb6b5db8fb1d79e9735d6fb3b3dbe6e0adaddb'
    'e8d6eab76f5778f0dadb7e5c73af2df4ad7bb3d8b5e7ebff03d5cbf2dff056d49b75e9cdbb4d6dd9b7ceedb4'
    '95e6b6b77f62c7e3ece3cbe3dc6d75b575b6adaf3cd7c5fb99e996db7b6df7a2e38b6f75b1bdc5e5b5b6d5bb'
    'ab3adaeb57576babb375ad7a73ad756d75ef9937fde0ba675add9aeb5d5bcd7a6badfa356fc5ced6b9d9b5fe'
    'cfd05f6ade1eb3abab756bcbf47a6d75cdbeb93b3d9cefe9a8e6eadb9b6e9bd5bd6ad96dadb6aeb9db763ab6'
    'df8bffb035f3b6c95bff97b03e8f65adbb6b39b6bdf95a9fb5b0f4fe995b5bbed94d6f9ce755cdefe872dcf8'
    'dadbb3dbdf4f3b0cab7d93767e8ee7ef455bbf7b4fbad335daa6e85aeff7a666b26de6ad6df78b59eb39f2b7'
    '6756d6de5f5d8d9bd7b3ad4ded9e8f2dbcf539dd3b56f7d25af4dcf35d6b75b6b5e9cefe1b67aadb96b6e7ca'
    'db56eeb9b7d59d3f1ab56df175cdb7d635eabd5773d65bb2dd765bcb6daedfce7356b761ceb5b77b3ff520fd'
    '59dceee89b6bb5aead75ae76add5b6b6b5fc3b37d3db9b1afbbe931dd36bbbbda9b57a66fd8e96bbf977a5be'
    'f761ae7770726dd3d36d6e6dcdbb2de5bd3ab6f99e575aeb9aeb757fb06b766db66f6de8b5b76b74b7acef47'
    'fd4cbb7cdffae063c56eaf373d2f4eb5bae6b6fbf45bd8ab6b5d9d6baedcab6e7b55ade72dd5b5b7b6db79cd'
    '665b79f7dfd8258b6fc97f9e4eb7e2b5fe0ff6e92c6b6aeadbad6be56f6e9c6ead6fe4ceceb9d5bb36d6e756'
    'daee6e5ead6bd5d7b555d5e6f8aeedf99d653cdad6de76f87b2d75b9abae7fd256adf4b6b6b5dffa74f1db2b'
    'b3732b739f65ceba6fe1d9bacf72b6bbacb6de5afafea0eb5fcc6f6dbcfec235f6e8b6f9d55b5f16dad79b6c'
    'dd6b9d73b57aadaeb5adadaeede4d75d3e5da6dadb6cfa759badddbdd42eb5b6bcb5b73ec75756f66cf72bab'
    '5f1b757a79cd79b77ff0e71facffdd7b'
    , 16)

def require(test, reason):
    if not test:
        raise ValueError(reason)


def replay(start, steps, choices):
    require(choices >> steps == 0, 'branch word exceeds stated length')
    x = start
    vertices = []
    for index in range(steps):
        vertices.append(x)
        m = 3 if (choices >> index) & 1 else 1
        x = (m*x + 1)//2
    require(x == start, 'cycle does not close')
    require(len(set(vertices)) == steps, 'a vertex repeats before closure')
    return vertices


def check():
    vertices = replay(START, STEPS, UP_MASK)
    require((min(vertices), max(vertices), UP_MASK.bit_count()) == (4, 998, 187), 'wrong statistics')
    require(2**298 > 3**188, 'ratio fails exact comparison')
    source = Path(__file__).with_name('UpDownCounterexample.lean').read_text()
    block = re.search(r'def witness : List Nat := \[([^]]+)\]', source).group(1)
    require([int(k) for k in re.findall(r'\d+', block)] == vertices, 'Lean witness disagrees with word')
    larger = replay(4, 6471, LARGE_MASK)
    require((max(larger), LARGE_MASK.bit_count()) == (15996, 4081), 'larger cycle mismatch')
    require(2**6471 > 6 * 3**4081, 'larger ratio fails')
    print('6471 distinct states verify a ratio larger than six')
    print('298 distinct positive states; 187 up edges; 4 -> 4; maximum 998; 2^298 > 3^188')


if __name__ == '__main__':
    check()
