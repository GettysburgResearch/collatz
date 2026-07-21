# X-0003 — Parity signatures and odd-tail collision fibers

Experiment ID: `X-0003`  
Issue: `#2`  
Agent: `gpt56-pro-01`  
Status: `EMPIRICAL` for finite class maxima and the explicit 339-member count; theorem-level existence is proved separately in `T-0005`.

## Research questions

1. Can the signature-pigeonhole construction of `T-0005` be reproduced exactly?
2. How large are the best equal-signature classes among weight-\(m\) words of length \(3m\) for small \(m\)?
3. Does appending the shortest supercritical all-odd tail produce the exact lifted collision identity claimed by the theorem?
4. Does one resulting large alphabet exhibit useful arithmetic geometry beyond cardinality?
5. Does the collision-code concatenation calculus of `L-0006` agree with direct affine-constant computation?

## Method

For each `1 <= m <= 8`, the script enumerates every set of `m` one-positions in a chronological parity word of length `3m`. It computes

```text
B(w) = sum 2^j 3^(number of later ones)
```

and the inverse signature

```text
sigma(w) = 2^(-3m) B(w) mod 3^m.
```

It selects the largest signature class, with smallest signature as the deterministic tie break.

The tail length `k` is the least integer satisfying

```text
3^(m+k) > 2^(3m+k).
```

The common inverse root is the CRT solution

```text
y = sigma mod 3^m,
y = -1 mod 2^k.
```

For each selected word, the script reconstructs

```text
r(w) = (2^(3m) y - B(w)) / 3^m
```

and directly verifies:

- integrality and the range `0 < r(w) < 2^(3m+k)`;
- the exact first `3m` parities and common root;
- the common all-odd tail;
- the full collision identity;
- the lifted identity on several values of the high quotient.

The implementation uses two passes over the combinations so that it retains only the selected class rather than all words.

It also checks `L-0006` on a four-word tensor example.

## Command

```bash
python3 -m py_compile experiments/X-0003-signature-tail-fibers/run.py
python3 experiments/X-0003-signature-tail-fibers/run.py
```

## Environment

- Python 3.11 or newer recommended
- standard library only
- deterministic; no random seed

## Parameter range

```text
1 <= m <= 8
```

The largest enumeration is

```text
binomial(24,8) = 735471
```

core words.

## Output

The checked-in outputs are

```text
results/summary.txt
results/m8-offsets.txt
```

SHA-256 digests for this revision:

```text
35f0dc7f7dafad50ff266b5ef1f0332a146838474c7b46f083a8599d50281863  run.py
2d38cb4a79264100210de4c4704dffe8890884e6f6a7761ae2784e7c3b4c4154  results/summary.txt
934328989d862bb180e6324fc217fad4cefdc5fe4c2cfdadc255a24ac0ea3e5e  results/m8-offsets.txt
```

## Principal finite result

At `m=8`, the largest equal-signature class has 339 words, signature 2906, and shortest supercritical tail length 20. It produces the exact chart recorded as `O-0005`:

```text
T^44(17592186044416*q + 8952950628352 + d)
  = 22876792454961*q + 11642373114938
```

for a reproducible 339-element offset set `D` of diameter 17207.

The program also verifies that:

- `D` meets all residue classes modulo 16;
- `D-D` contains every integer from `-934` through `934`;
- the original residue fiber contains seven consecutive integers.

## Interpretation

The finite maxima are not the proof of unboundedness. `T-0005` proves an exponential lower bound for all `m` by pigeonhole and CRT. This experiment provides explicit witnesses, exact checks, and geometry that may guide the next construction stage.

The decisive strategic conclusion is that large supercritical alphabets are abundant. Future work should optimize alphabet structure and vertical relay quality rather than continue a record-size census as an end in itself.

## Limitations

- No selected residue is proved to remain admissible forever under its induced map.
- A large alphabet, full projection modulo 16, or a long difference interval does not imply finite-boundary regeneration.
- The experiment stops at `m=8`; no empirical asymptotic claim about the largest signature class is made.
- The 339 offsets are committed and are independently regenerated and checked by the script.
