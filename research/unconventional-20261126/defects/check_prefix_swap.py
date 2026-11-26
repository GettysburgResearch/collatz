"""Exact finite core for the protected arbitrary-prefix transposition theorem."""
import json


def block_path(source):
    path = []
    for _ in range(3):
        shifted = source + 1
        ascent = (shifted & -shifted).bit_length() - 1
        numerator = 3**ascent * (shifted >> ascent) - 1
        excess = (numerator & -numerator).bit_length() - 1
        source = numerator >> excess
        path.append([ascent, excess, source])
    return path


def main():
    rows = []
    for m in range(1, 4):
        eligible = 0
        largest = None
        for upper in range(m, 29):
            for c in range(1, 38):
                for d in range(1, 39-c):
                    numerator = ((2**c-1)*2**m*3**upper
                                 - (2**d-1)*2**upper*3**m
                                 + (2**d-2**c)*2**(m+upper))
                    if numerator == 0:
                        continue
                    magnitude = abs(numerator)
                    valuation = 0
                    while magnitude % 3 == 0:
                        magnitude //= 3
                        valuation += 1
                    for p in range(1, 27):
                        total = p+m+upper
                        if 2**(total+c+d) >= 12*3**total:
                            continue
                        eligible += 1
                        margin = valuation-total
                        if margin >= 0:
                            raise ValueError((m, upper, c, d, p, margin))
                        largest = margin if largest is None else max(largest, margin)
        rows.append([m, eligible, largest])
    if rows != [[1,153963,-2],[2,160218,-3],[3,166119,-4]]:
        raise ValueError(rows)
    x, other = 19806321,19806293
    paths = [block_path(x),block_path(other)]
    expected = [[[1,1,14854741],[1,7,174079],[11,1,7528747]],
                [[1,7,232105],[1,1,174079],[11,1,7528747]]]
    if paths != expected or x%3 or 3*(paths[0][-1][-1]+1)<x+1 or 3*(174079+1)>=x+1:
        raise ValueError(paths)
    print(json.dumps({"columns":["shorter_ascent","gain_eligible","largest_ternary_margin"],
                      "rows":rows,"distinct_integral_mergers":0,
                      "sources":[x,other],"actual_paths":paths},indent=2))


if __name__ == "__main__":
    main()
