// Exact controls, no floating-point arithmetic. Run with Node.js.
const require=(p,msg)=>{if(!p)throw Error(msg)};
const T=n=>n%2n?(3n*n+1n)/2n:n/2n;
const bitlen=n=>n.toString(2).length;
const cache=new Map([["1",[1n,1n]]]);
function scalar(n) {
  let path=[],q=n;
  while(!cache.has(q.toString())) {
    let v=3n*q+1n,g=0n;
    while(v%2n===0n){v/=2n;g++;}
    path.push([q,g]); q=v;
    require(path.length<10000,"finite control orbit cap");
  }
  let [num,den]=cache.get(q.toString());
  for(let i=path.length-1;i>=0;i--){
    const [a,g]=path[i];num=g*den+num;den*=3n;
    cache.set(a.toString(),[num,den]);
  }
  return cache.get(n.toString());
}
function phase(q) {
  const [num,den]=scalar(q);
  const k=(2n*num-den-1n)/(2n*den);
  require(k>=0n,"nonnegative carry");
  return [num-k*den,den,k];
}
let prefixes=0,edges=0,budgets=0,reconstructions=0,largeBudget=0;
for(let t=2;t<=12;t++){
 const X=(2n**BigInt(t+1))-1n;
 for(let n=1n;n<=X;n+=2n){
   let q=n,last=0,m=0,states=[],gaps=[],lastOdd=-1;
   for(let i=0;i<t;i++){
     if(q%2n===1n){states.push(q);lastOdd=i;}
     q=T(q);
   }
   const A=BigInt(lastOdd);m=states.length-1;
   if(m===0){prefixes++;continue;}
   let B=0n,K=0n;
   let ks=[],bs=[],gs=[];
   for(let i=0;i<m;i++){
     const [pn,pd,k]=phase(states[i]);
     const [rn,rd,l]=phase(states[i+1]);
     const bnum=3n*pn*rd-rn*pd;
     require(bnum%(pd*rd)===0n,"integer digit");
     const b=bnum/(pd*rd);
     require(b>=1n&&b<=3n,"canonical digit");
     let v=3n*states[i]+1n,g=0n;
     while(v%2n===0n){v/=2n;g++;}
     require(v===states[i+1],"literal accelerated step");
     require(g+l===b+3n*k,"carry edge");
     require(l<=3n*k+b-1n,"birth budget");
     B+=b;K+=k;ks.push(k);bs.push(b);gs.push(g);edges++;
   }
   const km=phase(states[m])[2],k0=ks[0],M=BigInt(m),tt=BigInt(t);
   require(A+km===B+2n*K+k0,"complete telescope");
   require(15n*km+5n*A<=5n*tt+8n*M+20n,"integer height allowance");
   require(15n*(2n*K+B)<=15n*tt+8n*M+20n,"native carry budget");
   budgets++;
   if(16n*M>=3n*tt){
      require(80n*(2n*K+B)<=73n*tt+80n*M+107n,"large m budget");
      largeBudget++;
   }
   const recovered=B+2n*K+k0-A;
   require(recovered===km,"last carry recovered");
   for(let i=0;i<m;i++) {
      require(bs[i]+3n*ks[i]-(i+1===m?recovered:ks[i+1])===gs[i],"word recovery");
      reconstructions++;
   }
   prefixes++;
 }
}
// x=49/144, D=95/46, Lambda=12/7.
require((144n-49n)*46n===(144n-98n)*95n,"D identity");
require(7n*(46n*144n+95n*49n)<=12n*46n*144n,"lambda2 bound");
require(49n*(46n*144n**2n+95n*(49n*144n+49n**2n))<=144n*46n*144n**2n,"lambda3 bound");
require(3n**5n<2n**8n,"alpha < 8/5");
require(12n**365n<2n**284n*7n**365n,"weighted exponent < .71");
require((16n**16n)**25n<2n**284n*(3n**3n*13n**13n)**25n,"entropy exponent < .71");
// Discrete variation certificate on every short vector of nonnegative masses.
let variations=0;
for(let a=0;a<4;a++)for(let b=0;b<4;b++)for(let c=0;c<4;c++)for(let d=0;d<4;d++){
  const v=[0,a,b,c,d,0];
  let variation=0;
  for(let i=1;i<v.length;i++)variation+=Math.abs(v[i]-v[i-1]);
  require(variation>=2*Math.max(...v),"variation peak");
  variations++;
}
console.log(JSON.stringify({prefixes,edges,budgets,largeBudget,reconstructions,variations,exact_constant_certificates:6,scalar_cache_entries:cache.size},null,2));
