'use strict';

function trim(a){while(a.length>1&&a[a.length-1]===0n)a.pop();return a;}
function add(a,b){const c=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<a.length;i++)c[i]+=a[i];for(let i=0;i<b.length;i++)c[i]+=b[i];return trim(c);}
function shiftScale(a,s,k){return Array(s).fill(0n).concat(a.map(x=>x*k));}
function mul(a,b){const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return trim(c);}
function qbinRows(n){let r=[[1n]];for(let m=1;m<=n;m++){const z=Array(m+1);z[0]=z[m]=[1n];for(let k=1;k<m;k++)z[k]=add(r[k],shiftScale(r[k-1],m-k,1n));r=z;}return r;}
function numerator(u){const row=qbinRows(2*u+1);let p=[0n];for(let j=0;j<=u;j++)p=add(p,shiftScale(row[u-j],5*j*(j+1)/2,BigInt((2*j+1)*(j&1?-1:1))));return p;}

// Laurent monomial q^e reduced modulo q^d+1.
function monomialResidue(e,d){const L=2*d;let z=((e%L)+L)%L;return [z%d,z<d?1n:-1n];}
function addTerm(r,e,c,d){const [i,s]=monomialResidue(e,d);r[i]+=s*c;}
function negarem(p,d){const r=Array(d).fill(0n);for(let i=0;i<p.length;i++)addTerm(r,i,p[i],d);return r;}
function shiftRem(r,e,d,scale=1n){const z=Array(d).fill(0n);for(let i=0;i<d;i++)addTerm(z,i+e,r[i]*scale,d);return z;}
function mulRem(a,b,d){const z=Array(d).fill(0n);for(let i=0;i<d;i++)for(let j=0;j<d;j++)addTerm(z,i+j,a[i]*b[j],d);return z;}
function same(a,b){return a.length===b.length&&a.every((x,i)=>x===b[i]);}
function assert(x,msg){if(!x)throw Error(msg);}

const maxR=Number(process.argv[2]||5);
for(let r=1;r<=maxR;r++){
  const d=2**r, h=d/2;

  // u=d-1: P = d q^C H modulo q^d+1.
  const p1=negarem(numerator(d-1),d), H=Array(d).fill(0n);
  for(let j=0;j<h;j++)addTerm(H,2*j*j+(d+2)*j,1n,d);
  const C1=-d*(d-1)/2;
  const rhs1=shiftRem(H,C1,d,BigInt(d));
  assert(same(p1,rhs1),`u=d-1 reduction failed at d=${d}`);
  assert(H.some(x=>x!==0n),`H vanished at d=${d}`);
  if(d>=4){
    let n0=0, nh=0;
    for(let j=0;j<h;j++){
      const g=(j*(j+1)+h*j)/2;
      if(((g%h)+h)%h===0)n0++;
      if(((g%h)+h)%h===h/2)nh++;
    }
    assert(n0===2&&nh===0,`half-Gauss witness failed at d=${d}: ${n0},${nh}`);
  }

  // u=d-2, d>=4: (1-q)(1-q^2)P = q^C U modulo q^d+1.
  if(d>=4){
    const p2=negarem(numerator(d-2),d);
    const factor=negarem(mul([1n,-1n],[1n,0n,-1n]),d);
    const lhs=mulRem(factor,p2,d), U=Array(d).fill(0n);
    for(let j=0;j<d;j++){
      const w=BigInt(2*j+1), B=2*j*j+(d+3)*j;
      for(const e of [B,B-j,B-j-1,B-2*j-1])addTerm(U,e,w,d);
    }
    const C2=-(d-2)*(d+3)/2;
    const rhs2=shiftRem(U,C2,d);
    assert(same(lhs,rhs2),`u=d-2 reduction failed at d=${d}`);
    assert(U[1]!==0n && (U[1]===2n*BigInt(d)||U[1]===-2n*BigInt(d)),
      `residue-1 witness failed at d=${d}: ${U[1]}`);

    const sol=[];
    for(let j=0;j<d;j++)if(((2*j*j+3*j-1)%d+d)%d===0)sol.push(j);
    assert(sol.length===1,`Hensel uniqueness failed at d=${d}`);
    const j0=sol[0],j1=d-1-j0;
    const E0=2*j0*j0+(d+3)*j0;
    const E3=2*j1*j1+(d+1)*j1-1;
    assert((E3-E0)%(2*d)===0,`paired exponent failed at d=${d}`);
  }
  console.log(`PASS d=${d} boundary u=${d-2},${d-1}`);
}


