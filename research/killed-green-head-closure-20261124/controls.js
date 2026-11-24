// Exact finite controls for the canonical head comparison.
// Run: node controls.js. No floating point enters the assertions.
const require=(ok,msg)=>{if(!ok)throw new Error(msg)};
const abs=x=>x<0n?-x:x;
const pow3=s=>3n**BigInt(s);
const T=x=>x%2n===0n?x/2n:(3n*x+1n)/2n;
function step(s,D,b){
  if(s===0&&D===0n)return [0,0n,false,1n];
  if(D%2n===0n)
    return b===0?[s,D/2n,false,1n]:[s,(3n*D+1n-pow3(s))/2n,false,3n];
  if(s>0)
    return b===0?[s+1,(3n*D+1n)/2n,false,1n]:
      [s-1,(D-pow3(s-1))/2n,false,3n];
  return b===0?[1,(3n*D+1n)/2n,false,1n]:
    [1,(1n-3n*D)/2n,true,-1n];
}
let trajectories=0, transitions=0, words=0, offsetChecks=0, killedTransitions=0;
const depth=10, size=1<<depth;
for(let r=0;r<81;r++){
  const seen=new Set();
  for(let a=0;a<size;a++){
    let y=10n*BigInt(size)+BigInt(a), x=81n*y+BigInt(r);
    let u=y,v=x, s=4,D=BigInt(r), swapped=false, pu=0,pv=0,w=0;
    for(let t=0;t<depth;t++){
      const X=swapped?v:u,Y=swapped?u:v;
      require(Y===pow3(s)*X+D,"literal profile");
      require(s===Math.abs(4+pv-pu),"absolute signed level");
      const b=Number(X%2n); w=2*w+b;
      const [sn,Dn,flip,an]=step(s,D,b);
      // |z_next - (an/2)z| <= 1, including the fold at s=0.
      const num=2n*Dn*pow3(s)-an*D*pow3(sn);
      require(abs(num)<=2n*pow3(s)*pow3(sn),"normalized offset multiplier");
      offsetChecks++;
      if(s===0&&D===0n){require(sn===0&&Dn===0n,"absorbing state");killedTransitions++;}
      pu+=Number(u%2n);pv+=Number(v%2n);
      u=T(u);v=T(v);swapped=swapped!==flip;s=sn;D=Dn;transitions++;
      require((swapped?u:v)===pow3(s)*(swapped?v:u)+D,"next profile");
      require(s===Math.abs(4+pv-pu),"next signed level");
    }
    require(!seen.has(w),"unique parity word");seen.add(w);trajectories++;
  }
  require(seen.size===size,"complete parity bijection");
  words+=seen.size;
}
// Exact square-root majorants: sqrt(1/2)<=71/100, sqrt(3/2)<=123/100.
require(2n*71n**2n>=100n**2n,"first majorant");
require(2n*123n**2n>=3n*100n**2n,"second majorant");
require(71n+123n===2n*97n,"strict average contraction");
const receipt={depth,head_residues:81,trajectories,transitions,words,offsetChecks,killedTransitions,rational_contraction_certificate:true};
console.log(JSON.stringify(receipt,null,2));
