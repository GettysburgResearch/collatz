'use strict';

// Exact checker for the all-order root-value descent in
// composite_value_descent_theorem.md.  Standard-library only.
const fs = require('fs');
const basis = fs.readFileSync(require('path').join(__dirname,'lib','qpoly-basis.js'), 'utf8')
  .split('const maxU =')[0];

const audit = String.raw`
const qCache = new Map();
function Qc(u) { if (!qCache.has(u)) qCache.set(u, Q(u)); return qCache.get(u); }
function scale(a,k) { return a.map(x => x*k); }
function eq(a,b) { trim(a); trim(b); return a.length===b.length && a.every((x,i)=>x===b[i]); }
function binom(n,k) {
  if (k<0 || k>n) return 0n;
  if (k>n-k) k=n-k;
  let z=1n;
  for (let j=1;j<=k;j++) z=z*BigInt(n-k+j)/BigInt(j);
  return z;
}
function pow2(a) { return 1n << BigInt(a); }

let identities=0;
for (let m=2;m<=10;m++) {
  const ph=cyclotomic(m);
  for (let r=0;r<m;r++) for (let A=0;A<=3;A++) {
    const lhs=remainder(Qc(A*m+r),ph);
    const CA=binom(2*A,A);
    let rhs;
    if (2*r+1>=m) {
      rhs=remainder(scale(Qc(r),pow2(A)*BigInt(2*A+1)*CA),ph);
      if (!eq(lhs,rhs)) throw Error('upper-half descent '+JSON.stringify({m,r,A}));
    } else {
      // Division-free version:
      // 4 Q_(Am+r) = 2^A C_A (A Q_(m+r)+4(1-A)Q_r).
      const bracket=add(scale(Qc(m+r),BigInt(A)),scale(Qc(r),BigInt(4*(1-A))));
      rhs=remainder(scale(bracket,pow2(A)*CA),ph);
      const lhs4=remainder(scale(lhs,4n),ph);
      if (!eq(lhs4,rhs)) throw Error('lower-half descent '+JSON.stringify({m,r,A}));
    }
    identities++;
  }
}
console.log('PASS exact root-value descent in '+identities+' cases (m<=10,A<=3)');

// Independent finite-field reductions of the same identities.
function modNorm2(x,p){x%=p;return x<0n?x+p:x;}
function modEq(a,b,p){
  const n=Math.max(a.length,b.length);
  for(let i=0;i<n;i++) if(modNorm2((a[i]||0n)-(b[i]||0n),p)!==0n) return false;
  return true;
}
let reductions=0;
for (const pp of [3,5,7,11]) for (let m=2;m<=10;m++) if(m%pp!==0) {
  const ph=cyclotomic(m),p=BigInt(pp);
  for(let r=0;r<m;r++) for(let A=0;A<=3;A++) {
    const lhs=remainder(Qc(A*m+r),ph),CA=binom(2*A,A);
    if(2*r+1>=m){
      const rhs=remainder(scale(Qc(r),pow2(A)*BigInt(2*A+1)*CA),ph);
      if(!modEq(lhs,rhs,p))throw Error('finite upper '+JSON.stringify({pp,m,r,A}));
    }else{
      const bracket=add(scale(Qc(m+r),BigInt(A)),scale(Qc(r),BigInt(4*(1-A))));
      const rhs=remainder(scale(bracket,pow2(A)*CA),ph);
      if(!modEq(scale(lhs,4n),rhs,p))throw Error('finite lower '+JSON.stringify({pp,m,r,A}));
    }
    reductions++;
  }
}
console.log('PASS finite-field reductions in '+reductions+' cases');

// Kummer/Lucas audit of the quotient scalar in the upper-half channel.
function carriesDoublePlusOne(A,p){
  let carry=1,x=A,any=false;
  while(x>0 || carry){
    const d=x%p;x=Math.floor(x/p);
    const z=2*d+carry;
    if(z>=p)any=true;
    carry=z>=p?1:0;
  }
  return any;
}
for(const p of [3,5,7,11,13])for(let A=0;A<=1000;A++){
  const scalar=BigInt(2*A+1)*binom(2*A,A);
  const div=scalar%BigInt(p)===0n;
  if(div!==carriesDoublePlusOne(A,p))throw Error('carry scalar '+JSON.stringify({p,A}));
}
console.log('PASS upper-half scalar iff A+A+1 has a base-p carry through A=1000');
`;

Function(basis + '\n' + audit)();


