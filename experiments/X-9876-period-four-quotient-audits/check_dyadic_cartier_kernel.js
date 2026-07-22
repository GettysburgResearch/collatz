'use strict';

function assert(x,m){if(!x)throw Error(m)}
function C2(n){return n*(n-1)/2}
function toggle(M,e){const z=M.get(e)||0;if(z)M.delete(e);else M.set(e,1)}
function one(){return new Map([[0,1]])}
function add(A,B){const C=new Map(A);for(const e of B.keys())toggle(C,e);return C}
function shift(A,k){const C=new Map();for(const e of A.keys())toggle(C,e+k);return C}
function mul(A,B){const C=new Map();for(const a of A.keys())for(const b of B.keys())toggle(C,a+b);return C}
function eq(A,B){if(A.size!==B.size)return false;for(const e of A.keys())if(!B.has(e))return false;return true}

// Gaussian rows over F2, q-polynomials represented by exponent sets.
function qbinRows(n){let row=[one()];for(let m=1;m<=n;m++){const z=Array(m+1);z[0]=z[m]=one();for(let k=1;k<m;k++)z[k]=add(row[k],shift(row[k-1],m-k));row=z}return row}

function directNumerator(u){
  const row=qbinRows(2*u+1),H=new Map();
  for(let v=1;v<=2*u+1;v+=2){const k=v-u,base=5*C2(k);for(const e of row[v].keys())toggle(H,base+e)}
  return H;
}

function centeredF(u){
  let F=[one(),one()];
  for(let j=1;j<=u;j++){
    const h=new Map([[j,1],[-j,1]]),G=Array(F.length+2);for(let i=0;i<G.length;i++)G[i]=new Map();
    for(let v=0;v<F.length;v++){
      G[v]=add(G[v],F[v]);G[v+1]=add(G[v+1],mul(F[v],h));G[v+2]=add(G[v+2],F[v]);
    }
    F=G;
  }
  return F;
}

function pairedNumerator(u){
  const F=centeredF(u),H=new Map();
  for(let v=1;v<F.length;v+=2){const d=4*(C2(v)-u*v);for(const e of F[v].keys())toggle(H,e+d)}
  return H;
}

function elementaryH(u){
  const es=Array(u+1);for(let i=0;i<=u;i++)es[i]=new Map();es[0]=one();
  for(let j=1;j<=u;j++){
    const h=new Map([[j,1],[-j,1]]);for(let r=j;r>=1;r--)es[r]=add(es[r],mul(es[r-1],h));
  }
  const H=new Map();
  for(let r=0;r<=u;r++){
    const N=u-r,a=2*Math.ceil(r/2),K=new Map();
    for(let t=0;t<=N;t++)if((t&~N)===0)toggle(K,4*(C2(a+2*t)-u*(a+2*t)));
    const Z=mul(es[r],K);for(const e of Z.keys())toggle(H,e);
  }
  return H;
}

for(let u=0;u<=Number(process.argv[2]||8);u++){
  const D=directNumerator(u),P=pairedNumerator(u),E=elementaryH(u),constant=5*C2(u+1);
  assert(eq(D,shift(P,constant)),`centered diagonal identity u=${u}`);
  assert(eq(P,E),`elementary/scalar decomposition u=${u}`);
  console.log(`PASS exact Cartier identities u=${u}`);
}

function ordAtOne(exponents){
  let mn=Math.min(...exponents),mx=Math.max(...exponents),p=0n;
  for(const e of exponents)p^=1n<<BigInt(e-mn);
  let ord=0;
  while(p){
    let parity=0n,z=p;while(z){parity^=z&1n;z>>=1n}if(parity)break;
    let q=0n;for(let d=mx-mn;d>=1;d--)if((p>>BigInt(d))&1n){q^=1n<<BigInt(d-1);p^=(1n<<BigInt(d))|(1n<<BigInt(d-1))}
    assert(p===0n,'synthetic division remainder');p=q;mx--;ord++;
  }
  return ord;
}

const maxM=Number(process.argv[3]||40);
for(let M=0;M<=maxM;M++)for(const a of [0,2,6,10])for(const b of [-7,-1,0,5,12]){
  const S=new Set();for(let t=0;t<=M;t++)if((t&~M)===0){const e=C2(a+2*t)-b*(a+2*t);if(S.has(e))S.delete(e);else S.add(e)}
  assert(S.size>0,`zero kernel M=${M},a=${a},b=${b}`);
  assert(ordAtOne([...S])===M,`kernel order M=${M},a=${a},b=${b}`);
}
console.log(`PASS scalar-kernel theorem on ${(maxM+1)*20} exact states through M=${maxM}`);

function pop(n){let z=0;while(n){z+=n&1;n>>>=1}return z}
function v2(n){let z=0;while(n>0&&!(n&1)){z++;n>>>=1}return z}
function Eset(n){const E=[];for(let e=4;e<=2*(n+1);e*=2)if(n%e>=e/2-1)E.push(e);return E}
for(let n=0;n<=Number(process.argv[4]||100000);n++){
  const E=Eset(n),sum=E.reduce((a,b)=>a+b,0),target=2*n+2*((2**v2(n+1))-1);
  assert(E.length===pop(n),`cluster count n=${n}`);assert(sum===target,`cluster sum n=${n}`);
  if(n){let D=1;while(D<=n+1)D*=2;assert(E.at(-1)===D,`largest cluster n=${n}`)}
  if(!(n&1)){
    const a=n/2,R=[];for(let j=0;(1<<j)<=a;j++)if((a>>j)&1)R.push(4*(1<<j));assert(JSON.stringify(E)===JSON.stringify(R),`even recursion n=${n}`);
  }else{
    const R=[4,...Eset((n-1)/2).map(e=>2*e)];assert(JSON.stringify(E)===JSON.stringify(R),`odd recursion n=${n}`);
  }
}
console.log('PASS binary cluster formulas');



