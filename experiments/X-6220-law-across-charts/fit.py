"""Combined test of the law  m_N ~ (2^q/D)^N  across architectures of very different dimension."""
import math, glob, re
from math import log, log2

print(f"{'chart':>9} {'D':>8} {'dim':>7} {'pred log-rate':>14} {'fitted slope':>13} "
      f"{'ratio':>7} {'N used':>7}")
rows = []
for p in sorted(glob.glob('results/chart_*.txt')):
    txt = open(p).read().splitlines()
    hdr = txt[0]
    k, q = map(int, re.search(r'\((\d+),(\d+)\)', hdr).groups())
    D = float(re.search(r'= ([\d.]+),\s+dim', hdr).group(1))
    rate = 2**q/D
    pts = []
    for l in txt:
        if l.startswith('#'):
            continue
        f = l.split()
        pts.append((int(f[0]), log(int(f[1]))))
    pts = [p_ for p_ in pts if p_[0] >= 2]          # N=1 is a boundary outlier everywhere
    if len(pts) < 4:
        continue
    n = len(pts)
    sx = sum(a for a, _ in pts); sy = sum(b for _, b in pts)
    sxx = sum(a*a for a, _ in pts); sxy = sum(a*b for a, b in pts)
    slope = (n*sxy - sx*sy)/(n*sxx - sx*sx)
    rows.append((k, q, D, log2(D)/q, log(rate), slope, len(pts)))
    print(f"{f'({k},{q})':>9} {D:>8.0f} {log2(D)/q:>7.4f} {log(rate):>14.4f} "
          f"{slope:>13.4f} {slope/log(rate):>7.3f} {len(pts):>7}")

# the six-branch chart from X-6110 (D = 6 of the 31824 words, dim 0.13605)
sb_pred, sb_meas = log(2**19/6), 11.5067
print(f"{'six-branch':>9} {6:>8} {log2(6)/19:>7.4f} {sb_pred:>14.4f} {sb_meas:>13.4f} "
      f"{sb_meas/sb_pred:>7.3f} {'16':>7}")
rows.append((12, 19, 6, log2(6)/19, sb_pred, sb_meas, 16))

print(f"\nmean ratio (measured/predicted log-rate): "
      f"{sum(r[5]/r[4] for r in rows)/len(rows):.4f}")
print(f"range: {min(r[5]/r[4] for r in rows):.3f} to {max(r[5]/r[4] for r in rows):.3f}")
print(f"dimension range covered: {min(r[3] for r in rows):.4f} to {max(r[3] for r in rows):.4f}")
