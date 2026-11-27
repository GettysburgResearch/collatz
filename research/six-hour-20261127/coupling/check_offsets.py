"""Replay the entire set of unbounded ordinary query rows at offsets 6..38."""
import json


# Columns: exponent offset, ternary rank, extra evens, signed numerator,
# native ascent clock at lower attachment, upper prefix length, extra upper
# odds after clearing its denominator, exponent decrease.
ROWS = [
    (6,4,7,1951,1,14,2,1), (8,2,9,1543,1,28,11,6),
    (10,1,7,173,1,28,13,7), (12,4,9,10495,0,26,8,5),
    (14,4,9,7423,1,35,14,8), (16,2,2,23,0,6,1,1),
    (18,1,9,461,2,31,14,7), (20,4,8,4463,0,20,5,3),
    (22,1,7,173,1,28,13,7), (24,1,9,461,2,31,14,7),
    (26,2,9,1543,1,28,11,6), (28,3,3,101,0,8,1,1),
    (30,1,9,461,2,31,14,7), (32,3,6,469,1,12,2,1),
    (34,2,2,23,0,6,1,1), (36,4,6,1007,1,13,2,1),
    (38,3,7,1109,0,18,5,3),
]


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def trace(x, clocks):
    odds = 0
    for _ in range(clocks):
        if x % 2:
            x = (3*x+1)//2
            odds += 1
        else:
            x //= 2
    return x, odds


def main():
    require([row[0] for row in ROWS] == list(range(6,40,2)), "exact offset domain")
    require(pow(2,93,243) == 35 and pow(2,162,243) == 1, "common ternary class")
    output = []
    for a,r,e,b,i,h,g,delta in ROWS:
        f = r+e
        lower = f+i
        require(delta == h-f-g and delta>0 and a+delta<80, "positive earlier exponent")
        w0, wrem = divmod(35*2**(80-a+f)-b,3**r)
        stride, srem = divmod(243*2**(80-a+f),3**r)
        require(wrem == srem == 0 and w0>0 and w0%48 == 17 and stride%48 == 0, "canonical")
        require(81*w0+271 < 35*128*2**80 and 81*stride <=243*128*2**80, "parent height")
        require(stride%2**lower == 0 and 3*stride%2**h == 0, "whole class has prefix")
        for v in (0,1):
            X = 35+243*v
            W = w0+stride*v
            require(trace(W,lower) == (3**i*2**(80-a-i)*X-1,r+i),
                    "lower physical endpoint and grade")
            require(trace(3*W,h) == (3**g*2**(80-a+f-h)*X-1,r-1+g),
                    "upper physical endpoint and grade")
        # Independent actual ordinary run on the smallest exponent covered by the chart.
        m = 173
        n = m-a
        z = (128*2**m-271)//81
        w = (2**(n+f)-b)//3**r
        require(0<w<z and w%48 == 17, "first ordinary canonical source")
        require(trace(w,lower)[0] == trace(2**n-1,i)[0], "actual lower join")
        require(trace(3*w,h+n+f-h)[0] == trace(2**(n-delta)-1,n-delta)[0], "actual upper join")
        output.append({"offset": a,"rank": r,"extra_evens": e,"numerator": b,
                       "lower_clock": lower,"lower_odds": r+i,"ascent_attachment": i,
                       "upper_prefix": h,"upper_prefix_odds": r-1+g,
                       "extra_upper_odds": g,"exponent_decrease": delta})
    small = [0,5,11,12,67,68]
    for t,h in enumerate(small,1):
        require(trace(2**t-1,h)[0] == 1, "small original m=11 case")
    print(json.dumps({"reference_exponent": 173,"all_offset_rows": output,
                      "small_mersenne_first_hits": small},indent=2))


if __name__ == "__main__":
    main()
