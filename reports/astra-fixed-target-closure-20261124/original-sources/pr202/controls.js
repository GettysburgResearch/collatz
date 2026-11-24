"use strict";
function check(a,m){if(!a)throw Error(m)}
function mod(x,m){return (x%m+m)%m}
function inv(a,m){let [u,v,s,t]=[mod(a,m),m,1n,0n];while(v){let d=u/v;[u,v]=[v,u-d*v];[s,t]=[t,s-d*t]}check(u===1n,"nonunit");return mod(s,m)}
function T(n){return n%2n===0n?n/2n:(3n*n+1n)/2n}
function walk(n,h){for(let i=0;i<h;i++)n=T(n);return n}
function gap(n){check(n>0n&&n%2n===1n,"not positive odd");let v=3n*n+1n,e=0;while(v%2n===0n){v/=2n;e++}return [v,e]}
function pow(a,e){return a**BigInt(e)}
function bitlen(n){return n.toString(2).length}
function main(){
  const syncs=[[2,4,12,8,2],[3,6,36,17,3],[4,9,98,17,4],[5,9,98,17,4],[6,12,386,71,6],[7,14,3988,179,6],[8,16,34448,1151,7]];
  let synchronization_checks=0,word_checks=0,block_member_checks=0,injectivity_checks=0,height_identity_checks=0,phase_bank_steps=0,phase_bank_intervals=0,unit_conversion_checks=0;
  for(const [M,h,rr,zz,p] of syncs){
    const r=BigInt(rr),z=BigInt(zz),E=pow(2n,h),D=pow(3n,p);
    check(z%3n!==0n&&r<E&&z+1n<=pow(3n,h),"profile bounds");
    for(const t of [0n,1n,2n,19n,1n<<128n])for(let i=0;i<M;i++){
      check(walk(r+E*t+BigInt(i),h)===z+D*t,"literal synchronization");
      synchronization_checks++;
    }
    for(let b=2;b<=7;b++){
      const A=pow(2n,2*b),B=pow(3n,b),binary=2n*A,seen=new Map();
      const words=[];
      for(let variant=0;variant<Math.min(12,b*(b-1)+1);variant++){
        let w=Array(b).fill(2);
        if(variant){let a=Math.floor((variant-1)/(b-1)),c=(variant-1)%(b-1);if(c>=a)c++;w[a]=1;w[c]=3}
        words.push(w);
      }
      for(const w of words){
        let C=0n,S=0;
        for(let j=0;j<b;j++){C+=pow(3n,b-1-j)*pow(2n,S);S+=w[j]}
        check(S===2*b,"total clock");
        const residue=mod((A-C)*inv(B,binary),binary);
        const start=residue+binary*mod((z-residue)*inv(binary,D),D);
        for(let l=1;l<=6;l++){
          const y=start+binary*D*(pow(2n,96)+BigInt(l));
          check(y>z&&y%2n===1n&&y%3n!==0n,"positive lift and unit");
          let q=y;
          for(const e of w){let [n,actual]=gap(q);check(e===actual&&n%3n!==0n,"actual inverse route");q=n}
          word_checks++;
          check(A*q===B*y+C&&C>0n,"full carry");
          check(C*pow(2n,b)<=A*(pow(3n,b)-pow(2n,b)),"carry bound");
          const t=(y-z)/D,x=r+E*t;
          check(D*(x-r)===E*(y-z),"lift identity");
          check(B*D*(x-r)===E*(A*q-C-B*z),"height error identity");
          height_identity_checks++;
          for(let i=0;i<M;i++){check(walk(x+BigInt(i),h+2*b)===q,"common actual clock");block_member_checks++}
          if(seen.has(x.toString()))check(seen.get(x.toString())===q,"single target per start");
          seen.set(x.toString(),q);injectivity_checks++;
        }
      }
    }
  }
  for(let q0=1n;q0<1000n;q0++)if(q0%3n!==0n){
    const e=q0%3n===1n?2:1;let z=(pow(2n,e)*q0-1n)/3n;
    if(z%3n===0n)z=4n*z+1n;
    check(z>0n&&z%2n===1n&&z%3n!==0n,"unit conversion");
    check(walk(z,e)===q0||walk(z,e+2)===q0,"unit conversion actual path");unit_conversion_checks++;
  }
  for(let fixture=0;fixture<48;fixture++){
    const q=pow(2n,256)+BigInt(6*fixture+1);
    // 2^256 == 1 mod 3, so q == 2 mod 3.
    const Y=pow(2n,12000+fixture%4),A=Y*BigInt(12+fixture%5)/10n,B=A+Y/20n;
    let y=q,ok=false;
    for(let s=1;s<=500;s++){
      let e=2;while(e<=19&&mod(pow(2n,e)*y,27n)!==4n)e++;
      check(e<=19,"order 18 mod 27");
      const prev=y;y=(pow(2n,e)*prev-1n)/3n;
      check(y%9n===1n&&y%2n===1n&&y>=prev,"phase bank unit");
      let [next,actual]=gap(y);check(next===prev&&actual===e,"literal phase step");
      if(s>=2)check(e%6===2,"phase increment");
      phase_bank_steps++;
      // Find the least admissible padding exponent giving w >= A.
      const k=Math.max(2,bitlen(3n*A+1n)-bitlen(y)-1);
      let f=2+6*Math.max(0,Math.floor((k-2)/6));
      while(pow(2n,f)*y<3n*A+1n)f+=6;
      const w=(pow(2n,f)*y-1n)/3n;
      check(w>=A&&w%2n===1n&&w%3n!==0n,"padded unit");
      if(w<=B){let [v,g]=gap(w);check(v===y&&g===f,"literal final padding");for(let i=0;i<s;i++)v=gap(v)[0];check(v===q,"fixed ancestor");ok=true;phase_bank_intervals++;break}
    }
    check(ok,"finite phase interval fixture not found");
  }
  return {scope:"finite exact controls only; no asymptotic proof or Lean replay",synchronization_checks,word_checks,block_member_checks,injectivity_checks,height_identity_checks,unit_conversion_checks,phase_bank_steps,phase_bank_intervals};
}
const result=main();
if(typeof console!=="undefined") console.log(JSON.stringify(result,null,2));
