"use strict";
function runControls(){
 const assert=(x,msg)=>{if(!x)throw Error(msg)},T=x=>x%2n===0n?x/2n:(3n*x+1n)/2n, mod=(a,m)=>((a%m)+m)%m;
 const pow3=Array.from({length:33},(_,i)=>3n**BigInt(i)), H=15, E=24, Bden=2n;
 let front=[{r:1n,a:2n,b:8n,p:1,k:1}],roots=[];
 for(let h=1;h<=H;h++){
  const next=[];
  for(const z of front){
   if(z.p===z.k&&z.b===5n*z.a){
    let x=z.r,w="";for(let i=0;i<h;i++){w+=String(x%2n);x=T(x)}
    roots.push(w);
   } else if(h<H){
    for(const bit of [0n,1n]){
     const a=z.a+pow3[z.p]*bit,b=z.b+5n*pow3[z.k]*bit;
     next.push({r:z.r+(bit<<BigInt(h)),a:T(a),b:T(b),p:z.p+Number(a%2n),k:z.k+Number(b%2n)});
    }
   }
  }
  front=next;
 }
 function profile(w){
  let C=0n,p=0,h=0;
  for(const b of w){if(b==="1"){C=3n*C+(1n<<BigInt(h));p++}h++}
  return {w,e:h,p,C};
 }
 function invMod(a,m){let b=m,x=1n,y=0n;while(b!==0n){const t=a/b;[a,b]=[b,a-t*b];[x,y]=[y,x-t*y]}assert(a===1n,"inverse gcd");return mod(x,m)}
 const padded=[];
 for(const w of roots)for(let b=0;b<=3;b++)padded.push(profile(w+"0".repeat(b)));
 const buckets=new Map(),words=new Set();let sequences=0,retained=0,carryChecks=0,actualChecks=0,reverseChecks=0;
 function parse(w){
  let i=0,blocks=0;
  while(i<w.length){
   assert(w[i]==="1","first mark");
   let s=0,D=0n;
   do {
    assert(i<w.length,"no root");
    const a=Number(w[i++]),b=Number(mod(BigInt(a)+D,2n)),t=s+b-a,tm=Math.max(-t,0),tp=Math.max(t,0),sm=Math.max(-s,0);
    const z=pow3[tm+b-sm]*D+pow3[tm]*BigInt(b)-5n*pow3[tp]*BigInt(a);
    assert(z%2n===0n,"state exact");
    s=t;D=z/2n;
   }while(s!==0||D!==0n);
   while(i<w.length&&w[i]==="0")i++;
   blocks++;
  }
  return blocks;
 }
 function recover(C,p,e){
  let w=Array(e).fill("0"),last=-1;
  for(let j=0;j<p;j++){
   assert(C>0n,"remaining carry");
   let z=C,v=0;while(z%2n===0n){z/=2n;v++;}
   assert(v>last&&v<e,"clock recovery");
   w[v]="1";last=v;C-=pow3[p-1-j]*(1n<<BigInt(v));
  }
  assert(C===0n,"carry exhausted");return w.join("");
 }
 function add(z,j){
  sequences++;
  assert(!words.has(z.w),"unique parse");words.add(z.w);
  assert(parse(z.w)===j,"number of blocks");
  assert(recover(z.C,z.p,z.e)===z.w,"carry injection");carryChecks++;
  let C=0n,odd=0;
  for(let i=z.e-1;i>=0;i--)if(z.w[i]==="1"){C+=pow3[odd]*(1n<<BigInt(i));odd++;}
  assert(C===z.C&&odd===z.p,"reverse offset");reverseChecks++;
  if(Bden*z.C>(1n<<BigInt(z.e)))return;
  retained++;
  const key=`${z.e},${z.p}`;
  if(!buckets.has(key))buckets.set(key,{e:z.e,p:z.p,classes:new Map(),words:0});
  const group=buckets.get(key);group.words++;
  const m=pow3[z.p+1],D=1n<<BigInt(z.e),inv=invMod(D,m);
  for(const a of [1n,2n]){
   const q=mod((z.C+pow3[z.p]*a)*inv,m),id=String(q);
   assert(q%3n!==0n,"unit target");
   const old=group.classes.get(id)||{n:0,fixture:z};
   old.n++;group.classes.set(id,old);
   if(retained<=1500||retained%193===0){
    let Q=q+2n*m;if(Q%2n===0n)Q+=m;
    const num=D*Q-z.C;
    assert(num%pow3[z.p]===0n,"integral inverse");
    const x=num/pow3[z.p];assert(x>0n&&x%2n===1n&&x%3n!==0n,"positive odd unit");
    let u=x,v=5n*x,pu=0,pv=0;
    for(let i=0;i<z.e;i++){assert(String(u%2n)===z.w[i],"word realization");pu+=Number(u%2n);pv+=Number(v%2n);u=T(u);v=T(v);}
    assert(u===Q&&v===5n*Q&&pu===z.p&&pv===z.p,"actual paired endpoint");
    actualChecks++;
   }
  }
 }
 for(const w of padded){
  if(w.e<=E)add(w,1);
  for(const v of padded){
   if(w.e+v.e>E)continue;
   const z=profile(w.w+v.w);
   assert(z.C===pow3[v.p]*w.C+(v.C<<BigInt(w.e))&&z.p===w.p+v.p,"carry composition");
   add(z,2);
  }
 }
 let cells=0,weightedChecks=0,largestCount=0,badMassChecks=0;
 for(const g of buckets.values()){
  let sum=0;
  for(const [r,z] of g.classes){
   sum+=z.n;cells++;largestCount=Math.max(largestCount,z.n);
   // N <= floor(B 2^e / 3^p)+1.
   assert(BigInt(z.n)<=((1n<<BigInt(g.e))/(2n*pow3[g.p]))+1n,"upper carry fiber");
   weightedChecks++;
  }
  assert(sum===2*g.words,"two residues per word");
  const all=2n*pow3[g.p];
  for(const m of [1n,2n,4n,8n,16n,64n]){
   let bad=0n;
   for(const z of g.classes.values())if(BigInt(z.n)<m)bad+=BigInt(z.n);
   assert(bad<=all*m,"bad incidence bound");badMassChecks++;
  }
 }
 return {H,E,firstReturnCylinders:roots.length,paddedWords:padded.length,uniqueSequences:sequences,carryRecoveryChecks:carryChecks,reverseOffsetChecks:reverseChecks,boundedOffsetWords:retained,clockCountBuckets:buckets.size,occupiedFineCells:cells,exactFiberChecks:weightedChecks,actualInversePathChecks:actualChecks,badIncidenceChecks:badMassChecks,maxObservedFiber:largestCount};
}
console.log(JSON.stringify(runControls(),null,2));
