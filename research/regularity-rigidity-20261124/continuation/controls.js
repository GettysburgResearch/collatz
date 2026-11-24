"use strict";
function exactControls(){
 const assert=(c,s)=>{if(!c)throw Error(s)};
 const T=x=>x%2n===0n?x/2n:(3n*x+1n)/2n;
 const mod=(x,m)=>((x%m)+m)%m;
 const pow=(x,n,m)=>{let a=1n;for(let i=0;i<n;i++)a=a*x%m;return a};
 let front=[{r:1n,a:2n,b:8n,p:1,k:1}],roots=[],H=18;
 for(let h=1;h<=H;h++){
  const next=[];
  for(const z of front){
   if(z.p===z.k&&z.b===5n*z.a){
    let x=z.r,w="";for(let t=0;t<h;t++){w+=String(x%2n);x=T(x)}
    roots.push({w,r:z.r,p:z.p,h});
   } else if(h<H) for(const v of [0n,1n]){
    const a=z.a+3n**BigInt(z.p)*v,b=z.b+5n*3n**BigInt(z.k)*v;
    next.push({r:z.r+(v<<BigInt(h)),a:T(a),b:T(b),p:z.p+Number(a%2n),k:z.k+Number(b%2n)});
   }
  }
  front=next;
 }
 function update(s,D,i){
  const j=Number(mod(BigInt(i)+D,2n)),t=s+j-i,sm=Math.max(0,-s),tm=Math.max(0,-t),tp=Math.max(0,t);
  let z=3n**BigInt(tm+j-sm)*D+3n**BigInt(tm)*BigInt(j)-5n*3n**BigInt(tp)*BigInt(i);
  assert(z%2n===0n,"state division");return[t,z/2n];
 }
 function parse(w){
  const a=w+"1",cuts=[];let i=0;
  while(i<w.length){
   assert(a[i]==="1","mark starts odd");const begin=i;let s=0,D=0n;
   do{assert(i<w.length,"missing return");[s,D]=update(s,D,Number(a[i++]));}while(s!==0||D!==0n);
   while(i<w.length&&a[i]==="0")i++;
   cuts.push(w.slice(begin,i));
  }
  return cuts;
 }
 function profile(w){
  let C=0n,p=0,h=0;
  for(const b of w){if(b==="1"){C=3n*C+(1n<<BigInt(h));p++}h++}
  return{C,p,h};
 }
 function apply(w,x,m){
  const z=profile(w);return mod((3n**BigInt(z.p)*x+z.C)*pow((m+1n)/2n,z.h,m),m);
 }
 function offset(w,k){
  let m=3n**BigInt(k),v=0n,s=0,j=0,iv=(m+1n)/2n;
  for(let t=w.length-1;t>=0&&j<k;t--){
   s++;
   if(w[t]==="1"){v=mod(v+3n**BigInt(j)*pow(iv,s,m),m);j++;}
  }
  assert(j===k,"enough odd bits");return v;
 }
 let padded=[],physical=0,parseCases=0,offsetCases=0,compositionCases=0;
 for(const z of roots){
  for(let b=0;b<=4;b++){
   const w=z.w+"0".repeat(b);
   const p=parse(w);assert(p.length===1&&p[0]===w,"single parse");
   const q=profile(w);
   let x=z.r, y=5n*x;
   // All original cylinders are verified at the first root, not arbitrary padding.
   for(let i=0;i<z.h;i++){x=T(x);y=T(y);}
   assert(y===5n*x,"literal paired root");
   assert(q.p===z.p,"padding count");physical++;padded.push(w);
  }
 }
 for(let i=0;i<Math.min(1200,padded.length);i++){
  const u=padded[i],v=padded[(i*137+17)%padded.length],w=padded[(i*83+9)%padded.length],total=u+v+w,pp=parse(total);
  assert(pp.length===3&&pp[0]===u&&pp[1]===v&&pp[2]===w,"unique concatenation parse");parseCases++;
  const z=profile(total);
  for(let k=1;k<=Math.min(z.p,12);k++){
   const m=3n**BigInt(k),a=apply(total,7n,m),b=offset(total,k);
   assert(a===b,"reversed suffix offset");offsetCases++;
   assert(a===apply(w,apply(v,apply(u,7n,m),m),m),"composition");compositionCases++;
  }
 }
 let automata=0,pairCases=0,maxDistance=0,blockCases=0;
 function testAutomaton(B,S,index){
  let z=index,step=Array.from({length:S},()=>Array(B).fill(0));
  for(let i=0;i<S;i++)for(let b=0;b<B;b++){step[i][b]=z%S;z=Math.floor(z/S)}
  const H=S*S,counts=Array.from({length:S},(_,i)=>Array.from({length:S},(_,j)=>i===j?1n:0n));
  for(let t=0;t<H;t++){
   const nc=Array.from({length:S},()=>Array(S).fill(0n));
   for(let i=0;i<S;i++)for(let j=0;j<S;j++)for(let b=0;b<B;b++)nc[i][step[j][b]]+=counts[i][j];
   for(let i=0;i<S;i++)counts[i]=nc[i];
  }
  for(let a=0;a<S;a++)for(let b=a+1;b<S;b++){
   const seen=new Set([a*S+b]),queue=[[a,b,0]];let d=-1;
   for(let i=0;i<queue.length;i++){
    const [u,v,l]=queue[i];if(u===v){d=l;break}
    for(let x=0;x<B;x++)for(let y=0;y<B;y++){
     const uu=step[u][x],vv=step[v][y],id=uu*S+vv;
     if(!seen.has(id)){seen.add(id);queue.push([uu,vv,l+1])}
    }
   }
   if(d>=0){
    assert(d<S*S,"product graph shortest path");maxDistance=Math.max(maxDistance,d);
    let overlap=0n;for(let j=0;j<S;j++)overlap+=counts[a][j]<counts[b][j]?counts[a][j]:counts[b][j];
    assert(overlap>=BigInt(B)**BigInt(H-d),"common tail mass");pairCases++;
   }
  }
  if(index%17===0)for(let a=0;a<S;a++){
   const k=5,n=B**k,out=Array.from({length:S},(_,i)=>i%2);
   let direct=0;
   for(let v=0;v<n;v++){
    let q=a,t=v,ds=[];for(let j=0;j<k;j++){ds.push(t%B);t=Math.floor(t/B)}
    for(let j=k-1;j>=0;j--)q=step[q][ds[j]];
    direct+=out[q];
   }
   let v=out.slice();for(let j=0;j<k;j++)v=step.map(row=>row.reduce((s,x)=>s+v[x],0));
   assert(v[a]===direct,"prefix block average");blockCases++;
  }
  automata++;
 }
 for(let S=1;S<=3;S++)for(let i=0;i<S**(2*S);i++)testAutomaton(2,S,i);
 for(let i=0;i<2**6;i++)testAutomaton(3,2,i);
 return {maxFirstReturnClock:H,firstReturnCylinders:roots.length,paddedWordChecks:physical,uniqueConcatenationParses:parseCases,reverseOffsetChecks:offsetCases,compositionChecks:compositionCases,automata,productGraphPairChecks:pairCases,maxShortestPairPath:maxDistance,alignedBlockChecks:blockCases};
}
console.log(JSON.stringify(exactControls(),null,2));
