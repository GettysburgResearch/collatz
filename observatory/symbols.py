"""Composable parity blocks and exact odd-valuation cycle controls."""
from __future__ import annotations
from fractions import Fraction
import re

try:
    from .core import Budget, bounded_int, fraction_text
    from .pairs import fields
except ImportError:
    from core import Budget, bounded_int, fraction_text
    from pairs import fields


def summary(word: str) -> tuple[int, int, int]:
    b = q = 0
    for j, bit in enumerate(word):
        if bit == "1":
            b, q = 3 * b + 2 ** j, q + 1
    return len(word), q, b


def compose(w: tuple[int, int, int], v: tuple[int, int, int]) -> tuple[int, int, int]:
    """w then v: B_wv=3^qv B_w + 2^Lw B_v."""
    l, q, b = w
    k, r, c = v
    return l + k, q + r, 3 ** r * b + 2 ** l * c


def repeat(w: tuple[int, int, int], count: int) -> tuple[int, int, int]:
    result = (0, 0, 0)
    while count:
        if count & 1:
            result = compose(result, w)
        count //= 2
        if count:
            w = compose(w, w)
    return result


def blocks_config(request: dict) -> dict:
    fields(request, {"blocks"})
    blocks = request.get("blocks")
    if not isinstance(blocks, list) or not 1 <= len(blocks) <= 32:
        raise ValueError("blocks must contain 1–32 word/repeats objects.")
    out, total = [], 0
    for block in blocks:
        if not isinstance(block, dict) or set(block) != {"word", "repeats"}:
            raise ValueError("Each block has exactly word and repeats.")
        word = block["word"]
        if not isinstance(word, str) or not re.fullmatch(r"[01]{1,128}", word):
            raise ValueError("Each block word has 1–128 bits.")
        count = bounded_int(block["repeats"], "repeats", 1, 4096)
        total += len(word) * count
        out.append({"word": word, "repeats": count})
    if total > 4096:
        raise ValueError("Expanded length is capped at 4096 shortcut steps.")
    return {"kind": "blocks", "blocks": out}


def blocks(config: dict, budget: Budget) -> dict:
    total, parts = (0, 0, 0), []
    for block in config["blocks"]:
        budget.check()
        part = repeat(summary(block["word"]), block["repeats"])
        parts.append({"length": part[0], "ones": part[1], "B": str(part[2])})
        total = compose(total, part)
    length, q, b = total
    modulus, multiplier = 2 ** length, 3 ** q
    d = modulus - multiplier
    candidate = Fraction(b, d)
    residue = (-b * pow(multiplier, -1, modulus)) % modulus
    x, replay, legal, clock = candidate, [], True, 0
    for block in config["blocks"]:
        for _ in range(block["repeats"]):
            for bit in block["word"]:
                if clock % 32 == 0:
                    budget.check()
                legal = legal and x.denominator % 2 == 1 and (x.numerator & 1) == int(bit)
                if clock < 64:
                    replay.append({"i": clock, "n": fraction_text(x), "parity": int(bit)})
                x = (3 * x + 1) / 2 if bit == "1" else x / 2
                clock += 1
    legal = legal and x == candidate
    if candidate.denominator != 1:
        classification = "rational_noninteger"
    elif candidate <= 0:
        classification = "signed_integer" if candidate < 0 else "zero_outside_positive_domain"
    else:
        classification = "trivial_positive" if candidate in (1, 2) else "positive_integer_candidate"
    return {"length": length, "ones": q, "B": str(b), "D": str(d), "multiplier": str(multiplier),
            "modulus": str(modulus), "residue": str(residue), "least_positive": str(residue or modulus),
            "candidate": fraction_text(candidate), "full_denominator_divides": b % abs(d) == 0,
            "classification": classification, "replay_legal": legal, "replayed_steps": clock,
            "replay_preview": replay, "parts": parts,
            "residue_probes": [{"modulus": p, "B_mod": b % p, "D_mod": d % p} for p in (3, 5, 7, 11, 17, 31)],
            "scope": "Compositional exact endpoint arithmetic; every bounded branch replayed. Preview only first 64 states. Probes do not replace whole-denominator divisibility. No intermediate extrema are inferred from an endpoint summary."}


def valuations_config(request: dict) -> dict:
    fields(request, {"valuations", "multiplier", "addend"})
    values = request.get("valuations")
    if not isinstance(values, list) or not 1 <= len(values) <= 128:
        raise ValueError("valuations must be a list of 1–128 positive integers.")
    values = [bounded_int(v, "valuation", 1, 64) for v in values]
    if sum(values) > 4096:
        raise ValueError("Total valuation is capped at 4096.")
    multiplier, addend = request.get("multiplier", 3), request.get("addend", 1)
    if type(multiplier) is not int or type(addend) is not int or (multiplier, addend) not in ((3, 1), (3, -1), (5, 1)):
        raise ValueError("Available isolated systems: 3n+1, 3n-1, 5n+1.")
    return {"kind": "valuations", "valuations": values, "multiplier": multiplier, "addend": addend}


def valuation_cycle(config: dict, budget: Budget) -> dict:
    multiplier, addend = config["multiplier"], config["addend"]
    b, length = 0, 0
    for v in config["valuations"]:
        b = multiplier * b + addend * 2 ** length
        length += v
    d = 2 ** length - multiplier ** len(config["valuations"])
    x = candidate = Fraction(b, d)
    legal, replay = True, []
    for i, v in enumerate(config["valuations"]):
        budget.check()
        high = multiplier * x + addend
        numerator = abs(high.numerator)
        actual = (numerator & -numerator).bit_length() - 1 if numerator else None
        valid = x.denominator % 2 == 1 and x.numerator % 2 == 1 and high.denominator % 2 == 1 and actual == v
        legal = legal and valid
        replay.append({"i": i, "n": fraction_text(x), "valuation": v, "actual_valuation": actual, "legal": valid})
        x = high / 2 ** v
    legal = legal and x == candidate
    positive = candidate > 0 and candidate.denominator == 1 and all(Fraction(r["n"]) > 0 for r in replay)
    return {"system": f"{multiplier}n{addend:+d}", "clock": "odd-to-odd", "B": str(b), "D": str(d),
            "candidate": fraction_text(candidate), "whole_divides": b % abs(d) == 0,
            "replay": replay, "replay_legal": legal, "positive_integer_cycle": positive and legal,
            "scope": "One bounded valuation word in the explicitly named system. A control-system cycle is not a Collatz counterexample. Rational, signed and positive legality are checked separately."}
