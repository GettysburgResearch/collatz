'use strict';
const fs = require('fs');
const basisPath = require('path').join(__dirname, 'qpoly-basis.js');
const basis = fs.readFileSync(basisPath, 'utf8').split('const maxU =')[0];

const scan = String.raw`
function modNorm(x, p) { x %= p; return x < 0n ? x + p : x; }
function modTrim(a) {
  while (a.length > 1 && a[a.length - 1] === 0n) a.pop();
  return a;
}
function divModIfExact(a, b, p) {
  a = modTrim(a.map(x => modNorm(x, p)));
  b = modTrim(b.map(x => modNorm(x, p)));
  if (b[b.length - 1] !== 1n) throw Error('modular divisor not monic');
  const q = Array(Math.max(1, a.length - b.length + 1)).fill(0n);
  while (a.length >= b.length && !(a.length === 1 && a[0] === 0n)) {
    const d = a.length - b.length;
    const c = a[a.length - 1];
    q[d] = c;
    for (let i = 0; i < b.length; i++) a[i + d] = modNorm(a[i + d] - c * b[i], p);
    modTrim(a);
  }
  return a.some(x => x !== 0n) ? null : modTrim(q);
}
function multiplicityMod(poly, factor, prime) {
  const p = BigInt(prime);
  let f = poly.map(x => modNorm(x, p));
  let m = 0;
  for (;;) {
    const q = divModIfExact(f, factor, p);
    if (q === null) return m;
    f = q; m++;
  }
}
function primeDivisors(n) {
  const out = [];
  for (let p = 2; p * p <= n; p++) if (n % p === 0) {
    out.push(p); while (n % p === 0) n /= p;
  }
  if (n > 1) out.push(n);
  return out;
}
function phi(n) {
  let ans = n;
  for (const p of primeDivisors(n)) ans = ans / p * (p - 1);
  return ans;
}

const maxU2 = Number(process.argv[2] || 12);
const maxL2 = Number(process.argv[3] || 300);
let candidates = 0, certified = 0;
const survivors = [];
for (let u = 1; u <= maxU2; u++) {
  const P = Q(u), s = 2 * u + 1;
  for (let L = s + 1; L <= maxL2; L++) {
    if (phi(L) > P.length - 1) continue;
    candidates++;
    let witness = null;
    for (const p of primeDivisors(L)) {
      let pk = 1, z = L;
      while (z % p === 0) { pk *= p; z /= p; }
      const m = L / pk;
      const got = multiplicityMod(P, cyclotomic(m), p);
      const need = phi(pk);
      if (got < need) { witness = {p, m, got, need}; break; }
    }
    if (witness) certified++;
    else survivors.push({u, L});
  }
}
console.log('prime-power peeling candidates', candidates);
console.log('certified exclusions', certified);
console.log('unresolved by peeling', survivors.length, JSON.stringify(survivors.slice(0, 80)));
let residueCertified = 0;
const residueWitnesses = [];
for (const z of survivors) {
  const primes = primeDivisors(z.L);
  if (primes.length !== 1) continue;
  const p = primes[0], d = z.L / p, P = Q(z.u);
  const folded = Array(z.L).fill(0n);
  P.forEach((x, n) => folded[n % z.L] += x);
  let witness = null;
  for (let r = 0; r < d && witness === null; r++) {
    const vals = Array.from({length:p}, (_, j) => folded[r + j * d]);
    if (vals.some(x => x !== vals[0])) witness = {r, vals:vals.map(String)};
  }
  if (witness) { residueCertified++; residueWitnesses.push({u:z.u,L:z.L,...witness}); }
}
console.log('prime-power residue certificates', residueCertified, JSON.stringify(residueWitnesses));
if (certified + residueCertified !== candidates) throw Error('certificate gap remains');
`;

Function('process', basis + '\n' + scan)(process);

