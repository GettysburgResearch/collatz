// Finite exact controls. They do not test the imported asymptotic atom floor.
const need=(x,m)=>{if(!x)throw Error(m)};
const T=n=>n%2n===0n?n/2n:(3n*n+1n)/2n;
const pow=(a,b)=>a**BigInt(b);
function run(n,t){let p=0;for(let i=0;i<t;i++){if(n%2n)p++;n=T(n)}return [n,p]}
function* comps(s,k){if(k===0){if(s===0)yield [];return}for(let e=1;e<=s-k+1;e++)for(const w of comps(s-e,k-1))yield [e,...w]}
function inv(q,w){
 let x=q;
 for(const e of w){const v=pow(2n,e)*x-1n;if(v%3n!==0n)return null;x=v/3n;if(x<=0n||x%2n===0n||x%3n===0n)return null}
 return x;
}
const targets=[7n,11n,13n,17n,19n];
let words=0,legal=0,unitCongruences=0,firstHits=0,distinctDepths=0,comparisonChecks=0,antichainPairs=0,antichains=0,prefixLifts=0,gradeChecks=0,clockInequalities=0;
for(const q of targets){
 let visited=q;for(let i=0;i<1000&&visited!==1n;i++)visited=T(visited);
 need(visited===1n,"fixed test target must reach 1");
 const rows=new Map();
 for(let b=1;b<=6;b++)for(let s=Math.max(b,2*b-2);s<=2*b+2;s++)for(const w of comps(s,b)){
  words++;let a=0,C=0n;
  for(let i=0;i<b;i++){a+=w[i];C+=pow(3n,i)*pow(2n,s-a);}
  const x=inv(q,w);if(x===null)continue;
  legal++;need(pow(3n,b)*x===pow(2n,s)*q-C,"full inverse carry");
  need(x>0n&&x%2n===1n&&x%3n!==0n,"unit positivity");
  for(let K=1;K<=3;K++){
    const M=pow(3n,K),mod=pow(3n,b+K);
    for(let r=0n;r<M;r++)if(r%3n!==0n){
     need(((pow(2n,s)*q-C-pow(3n,b)*r)%mod===0n)===(x%M===r),"extra precision equivalence");
     unitCongruences++;
    }
  }
  const [y,p]=run(x,s);need(y===q&&p===b,"literal final clock");
  let z=x;for(let i=0;i<s;i++){need(z!==q,"first hit at declared clock");z=T(z)}
  firstHits++;
  need(!rows.has(x.toString()),"distinct source across depths and words");distinctDepths++;
  rows.set(x.toString(),{x,b,s});
 }
 for(const Y of [8n,16n,32n,64n,128n,256n,512n,1024n]){
  const cand=[...rows.values()].filter(v=>v.x>=Y&&v.x<2n*Y&&v.b%2===0&&pow(2n,v.s)*q>=Y*pow(3n,v.b)&&pow(2n,v.s)*q<=2n*Y*pow(3n,v.b));
  const byX=new Map(cand.map(v=>[v.x.toString(),v]));
  const keep=[];
  for(const v of cand){
    let z=v.x,pc=0,comparable=false;
    for(let t=1;t<v.s;t++){
      if(z%2n)pc++;z=T(z);const u=byX.get(z.toString());
      if(!u)continue;
      need(v.b-u.b===pc&&v.s-u.s===t,"exact comparative clocks");
      need(pow(2n,t)<=2n*pow(3n,pc)&&pow(3n,pc)<=2n*pow(2n,t),"comparison slope bound");
      comparisonChecks++;comparable=true;
    }
    if(!comparable)keep.push(v);
  }
  const kept=new Set(keep.map(v=>v.x.toString()));
  for(const v of keep){let z=v.x;for(let t=1;t<v.s;t++){z=T(z);need(!kept.has(z.toString()),"antichain");antichainPairs++}}
  antichains++;
 }
 // Glue exact inverses to arbitrary binary cylinders where compatible.
 const examples=[...rows.values()].slice(0,500);
 for(let h=0;h<=7;h++)for(let r=0n;r<pow(2n,h);r++){
  const [z,p]=run(r,h);
  for(const v of examples){
   const d=pow(3n,p);
   if(v.x<z||(v.x-z)%d!==0n)continue;
   const n=r+pow(2n,h)*((v.x-z)/d);
   if(n===0n)continue;
   const [land,pc]=run(n,h);
   need(land===v.x&&pc===p&&n%pow(2n,h)===r,"affine lift");
   prefixLifts++;
   const [end,total]=run(n,h+v.s);need(end===q&&total===p+v.b,"complete clock and grade");
   for(let m=2;m<=5;m++){need((h+v.s)%m===(h%m+v.s%m)%m&&total%m===(p%m+v.b%m)%m,"grade residues");gradeChecks++}
  }
 }
}
need(3n**5n<2n**8n,"log2(3)<8/5");
for(let k=20;k<=300;k++)for(let t=k;t<=2*k;t++)if(5*t<=8*k+5){
 need(3*t<=5*k,"critical arcs have at least 3/5 odd inputs");clockInequalities++;
}
console.log(JSON.stringify({words,legal,unitCongruences,firstHits,distinctDepths,comparisonChecks,antichainPairs,antichains,prefixLifts,gradeChecks,clockInequalities},null,2));
