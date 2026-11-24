// Exact bounded arithmetic controls; not a Lean proof or an external theorem check.
'use strict';
function check(condition, message) { if (!condition) throw new Error(message); }
function bitlen(n) { return BigInt(n.toString(2).length); }
function T(n) { return n%2n === 0n ? n/2n : (3n*n+1n)/2n; }
function run(n,t) { for (let i=0n;i<t;i++) n=T(n); return n; }
function v2(n) { let e=0n; while (n%2n===0n) { n/=2n; e++; } return e; }
function inv(y) {
  check(y>0n && y%3n!==0n,'bad inverse input');
  let e=y%3n===1n?2n:1n;
  let z=((1n<<e)*y-1n)/3n;
  if (z%3n===0n) { z=4n*z+1n; e+=2n; }
  check(z>0n && z%2n===1n && z%3n!==0n,'unit alternative');
  check(e>=1n && e<=4n && 3n*z+1n===(1n<<e)*y,'inverse formula');
  check(run(z,e)===y,'literal shortcut inverse');
  check(3n*z>=y && 3n*z<=16n*y,'inverse heights');
  return [z,e];
}
function strip(u,k) {
  check(u>0n && u%2n===1n && u%3n!==0n,'bad strip input');
  let e=u%3n===1n?2n:1n, n=((1n<<e)*u-1n)/3n;
  let s=k*e-bitlen(n), ct=0;
  while(s<0n) {
    let m=((1n<<(e+2n))*u-1n)/3n;
    check(m===4n*n+1n,'exact recurrence');
    check(bitlen(m)===bitlen(n)+2n,'octave shift');
    let s2=k*(e+2n)-bitlen(m);
    check(s2-s===2n*(k-1n),'surplus increment');
    n=m; e+=2n; s=s2; ct++;
  }
  if(s>=2n*(k-1n)) return [null,ct];
  check(0n<=s && s<2n*(k-1n),'strip bounds');
  check(v2(3n*n+1n)===e,'exact valuation');
  check(run(n,e)===u,'literal strip inverse');
  check(u**k<=4n**k*n**(k-1n),'target upper bound');
  check(3n**k*n**(k-1n)<=4n**k*u**k,'source upper bound');
  check(k*(e+2n)-bitlen(4n*n+1n)>=2n*(k-1n),'unique successor test');
  return [[n,e],ct];
}
function main() {
  let invCount=0, strips=0, recurrences=0, injected=0, rows=0, grid=0;
  for(let y=1n;y<=10000n;y++) if(y%3n!==0n) { inv(y); invCount++; }
  for(let k=2n;k<=12n;k++) {
    const ns=new Set();
    for(let u=1n;u<=3001n;u+=2n) if(u%3n!==0n) {
      const [v,ct]=strip(u,k); recurrences+=ct;
      if(v!==null) {
        const key=v[0].toString(); check(!ns.has(key),'injectivity');
        ns.add(key); strips++; injected++;
      }
    }
  }
  // The translated complete grid lemma at exact rational translations.
  for(const [p,Q] of [[19n,12n],[65n,41n],[84n,53n],[485n,306n]]) {
    const den=7n*Q;
    for(let tr=0n;tr<den;tr++) {
      let found=false;
      for(let s=1n;s<=Q;s++) {
        const num=((tr-7n*s*p)%den+den)%den;
        if(14n<=num && num<=21n) {found=true; break;}
      }
      check(found,'positive-margin rational grid'); grid++;
    }
  }
  // Large ordinary inverse rows, with explicit bounded multiplicity and
  // an exact head-width check Q*(n-2^d) <= 5*2^d (no floating logs).
  const Q=53n;
  for(const k of [2n,3n,5n,10n]) {
    const mult=new Map();
    for(let delta=1n;delta<=120n;delta++) {
      const q=(1n<<256n)+delta;
      if(q%3n===0n) continue;
      let y=q, clock=0n, selected=false;
      for(let s=1n;s<=Q;s++) {
        const [z,e]=inv(y); y=z; clock+=e;
        check(run(y,clock)===q,'row retains original target');
        const [v,ct]=strip(y,k); recurrences+=ct;
        check(v!==null,'large row strip exists');
        const [n,ex]=v;
        const pow2=1n<<(bitlen(n)-1n);
        if(Q*(n-pow2)<=5n*pow2) {
          check(run(n,ex+clock)===q,'selected literal path');
          const id=n.toString(); mult.set(id,(mult.get(id)||0)+1);
          selected=true; rows++; break;
        }
      }
      check(selected,'row has narrow head');
    }
    for(const m of mult.values()) check(BigInt(m)<=4n*Q+1n,'multiplicity');
  }
  return {inverseChecks:invCount, stripChecks:strips, recurrenceChecks:recurrences,
    injectivityChecks:injected, rationalGridChecks:grid, actualLargeRows:rows};
}
const result=main();
if(typeof console!=='undefined') console.log(JSON.stringify(result));
