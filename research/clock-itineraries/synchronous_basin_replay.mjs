// Exact finite gate-1 counts for the synchronized-triple test.
const stages = process.argv.slice(2).map(Number);
if (stages.length === 0) stages.push(1, 2);
if (stages.some((x, i) => !Number.isSafeInteger(x) || x <= 0 ||
    x > 64 || (i > 0 && x <= stages[i - 1]))) {
  throw new Error("Supply increasing positive integer stages through 64");
}
const limits = stages.map(x => Math.floor(268435456 * x / 9));
const safe = Number.MAX_SAFE_INTEGER;
const evenOrOdd = n => n % 2 === 0 ? n / 2 : (3*n + 1) / 2;
const endpoints = [];
const slopes = [];
for (let i = 0; i < 128; i++) {
  let n = i, slope = 1;
  for (let k = 0; k < 7; k++) {
    if (n % 2 === 1) slope *= 3;
    n = evenOrOdd(n);
  }
  endpoints.push(n);
  slopes.push(slope);
}
function run28(n) {
  for (let i = 0; i < 4; i++) {
    const r = n % 128;
    n = endpoints[r] + slopes[r] * Math.floor(n / 128);
  }
  return n;
}
// T(n)+1 <= (3/2)(n+1) at positive inputs bounds every skipped endpoint.
// Each integer summand in a seven-step affine lift is nonnegative.
if (((9n * BigInt(limits.at(-1)) + 1n) * 3n**28n) >= BigInt(safe) * 2n**28n) {
  throw new Error("The configured prefix range exceeds safe integer arithmetic");
}
const deadline = 2048;
const memo = new Uint16Array(1 << 21);
memo[1] = 1;
function firstHit(n) {
  const path = [];
  let t = 0;
  while (t <= deadline) {
    if (n < memo.length && memo[n]) {
      let time = memo[n] - 1;
      for (let j = path.length - 1; j >= 0; j--) {
        time++;
        if (path[j] < memo.length && time <= deadline) memo[path[j]] = time + 1;
      }
      return time <= deadline ? time : null;
    }
    if (t === deadline) break;
    path.push(n);
    if (n % 2 && n > (safe - 1) / 3) {
      let big = BigInt(n);
      while (big > BigInt(Math.floor((safe - 1)/3)) && t < deadline) {
        big = big % 2n === 0n ? big / 2n : (3n*big+1n)/2n;
        t++;
        if (big > BigInt(Math.floor((safe - 1)/3))) path.push(Infinity);
      }
      if (big > BigInt(safe)) break;
      n = Number(big);
    } else {
      n = evenOrOdd(n);
      t++;
    }
  }
  return null;
}
// Directly replay the affine acceleration on a full low interval and at the far boundary.
for (const seed of [1, Math.max(1, limits.at(-1)-4096)]) {
  for (let x = seed; x < seed + 4096; x++) {
    for (const m of [1, 3, 9]) {
      let n = m*x;
      for (let h = 0; h < 28; h++) n = evenOrOdd(n);
      if (n !== run28(m*x)) throw new Error("Prefix replay mismatch");
    }
  }
}
let stage = 0, synchronized = 0, misses = 0, longest = -1, witness = 0, target = 0;
for (let x = 1; x <= limits.at(-1); x++) {
  const b = run28(x);
  if (b === run28(3*x) && b === run28(9*x)) {
    synchronized++;
    const time = firstHit(b);
    if (time === null) {
      misses++;
    } else if (time > longest) {
      longest = time;
      witness = x;
      target = b;
    }
  }
  if (x === limits[stage]) {
    const passes = BigInt(misses)**25n < BigInt(stages[stage])**21n;
    console.log(JSON.stringify({stage: stages[stage], limit: x, synchronized, deadline,
      misses, passes, longest, witness, target}));
    stage++;
  }
}
