function trim(a) {
  while (a.length > 1 && a[a.length - 1] === 0n) a.pop();
  return a;
}

function add(a, b) {
  const c = Array(Math.max(a.length, b.length)).fill(0n);
  for (let i = 0; i < a.length; ++i) c[i] += a[i];
  for (let i = 0; i < b.length; ++i) c[i] += b[i];
  return trim(c);
}

function sub(a, b) {
  const c = Array(Math.max(a.length, b.length)).fill(0n);
  for (let i = 0; i < a.length; ++i) c[i] += a[i];
  for (let i = 0; i < b.length; ++i) c[i] -= b[i];
  return trim(c);
}

function shiftScale(a, s, k) {
  return Array(s).fill(0n).concat(a.map(x => x * k));
}

function mul(a, b) {
  const c = Array(a.length + b.length - 1).fill(0n);
  for (let i = 0; i < a.length; ++i)
    for (let j = 0; j < b.length; ++j) c[i + j] += a[i] * b[j];
  return trim(c);
}

function exactDiv(a, b) {
  a = a.slice();
  b = trim(b.slice());
  const q = Array(Math.max(1, a.length - b.length + 1)).fill(0n);
  if (b[b.length - 1] !== 1n && b[b.length - 1] !== -1n) throw Error('nonmonic');
  while (a.length >= b.length && !(a.length === 1 && a[0] === 0n)) {
    const d = a.length - b.length;
    const c = a[a.length - 1] / b[b.length - 1];
    q[d] += c;
    for (let i = 0; i < b.length; ++i) a[i + d] -= c * b[i];
    trim(a);
  }
  if (a.some(x => x !== 0n)) throw Error('remainder: ' + a);
  return trim(q);
}

function remainder(a, b) {
  a = trim(a.slice());
  b = trim(b.slice());
  while (a.length >= b.length && !(a.length === 1 && a[0] === 0n)) {
    const d = a.length - b.length;
    const c = a[a.length - 1] / b[b.length - 1];
    for (let i = 0; i < b.length; ++i) a[i + d] -= c * b[i];
    trim(a);
  }
  return a;
}

const cycloCache = new Map([[1, [-1n, 1n]]]);
function cyclotomic(n) {
  if (cycloCache.has(n)) return cycloCache.get(n);
  let p = [-1n, ...Array(n - 1).fill(0n), 1n];
  for (let d = 1; d < n; ++d) if (n % d === 0) p = exactDiv(p, cyclotomic(d));
  cycloCache.set(n, p);
  return p;
}

function qbinRows(n) {
  let row = [[1n]];
  for (let m = 1; m <= n; ++m) {
    const next = Array(m + 1);
    next[0] = [1n]; next[m] = [1n];
    for (let k = 1; k < m; ++k)
      next[k] = add(row[k], shiftScale(row[k - 1], m - k, 1n));
    row = next;
  }
  return row;
}

function poch(n) {
  let p = [1n];
  for (let k = 1; k <= n; ++k) p = mul(p, [1n, ...Array(k - 1).fill(0n), -1n]);
  return p;
}

function Q(u) {
  const row = qbinRows(2 * u + 1);
  let p = [0n];
  for (let j = 0; j <= u; ++j) {
    const sign = (j & 1) ? -1n : 1n;
    p = add(p, shiftScale(row[u - j], 5 * j * (j + 1) / 2, BigInt(2 * j + 1) * sign));
  }
  return exactDiv(p, poch(u));
}

const maxU = Number(process.argv[2] || 10);
const maxCyclo = Number(process.argv[3] || 200);
let prev = [1n];
for (let u = 1; u <= maxU; ++u) {
  const q = Q(u);
  const d = sub(q, prev);
  let valuation = d.findIndex(x => x !== 0n);
  if (valuation < 0) valuation = Infinity;
  const r = d.slice(valuation);
  const neg = r.map((x, i) => [i + valuation, x]).filter(([,x]) => x < 0n);
  const head = r.slice(0, 20).map(String).join(',');
  const tail = r.slice(-20).map(String).join(',');
  const factors = [];
  for (let L = 1; L <= maxCyclo; ++L)
    if (remainder(q, cyclotomic(L)).every(x => x === 0n)) factors.push(L);
  const forbidden = factors.filter(L => L > 2 * u + 1);
  console.log(`u=${u} degQ=${q.length-1} valDiff=${valuation} degR=${r.length-1} neg=${neg.length} cyclo<=${maxCyclo}=${factors.join(':') || '-'} forbidden=${forbidden.join(':') || '-'} headR=${head} tailR=${tail}`);
  prev = q;
}


