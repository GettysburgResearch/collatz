"use strict";
function controls(){
  const assert=(p,s)=>{if(!p)throw Error(s)},mod=(x,m)=>((x%m)+m)%m,T=x=>x%2n===0n?x/2n:(3n*x+1n)/2n,gcd=(a,b)=>b?gcd(b,a%b):a;
  const step=(z,b)=>({a:T(z.a+3n**BigInt(z.p)*BigInt(b)),p:z.p+Number((z.a+3n**BigInt(z.p)*BigInt(b))%2n)});
  let syncCases=0,liftCases=0,phaseCases=0,weightedCases=0,actualPaths=0,maxClock=0;
  for(let M=1;M<=8;M++)for(let d=0;d<=4;d++)for(let R=0;R<2**d;R++){
    let h=d,r=BigInt(R),zs=[];
    for(let i=0;i<M;i++){let a=r+BigInt(i),p=0;for(let k=0;k<h;k++){p+=Number(a%2n);a=T(a)}zs.push({a,p});}
    function advance(i,parity){let b=Number(mod(BigInt(parity)-zs[i].a,2n));r+=BigInt(b)<<BigInt(h);zs=zs.map(z=>step(z,b));h++;}
    function offset(i,j){let s=zs[j].p-zs[i].p,D=3n**BigInt(Math.max(-s,0))*zs[j].a-3n**BigInt(Math.max(s,0))*zs[i].a;return {s,D};}
    for(let j=1;j<M;j++){
      let i=0, k=j,lim=0;
      while(true){assert(lim++<20000,"sync did not terminate");let {s,D}=offset(i,k);if(s===0&&D===0n)break;
        if(s!==0){if(D===0n)advance(i,1);else if(D%2n===0n)advance(i,0);else advance(i,s>0?1:0);continue;}
        if(D<0n){[i,k]=[k,i];D=-D;}
        if(D%2n===0n){advance(i,0);continue;}
        advance(i,0);
        while(offset(i,k).D%2n===0n)advance(i,0);
        advance(i,1);
      }
    }
    advance(0,1);
    assert(zs.every(z=>z.a===zs[0].a&&z.p===zs[0].p),"profile equality");assert(zs[0].a%3n!==0n,"unit endpoint");
    assert(mod(r,1n<<BigInt(d))===BigInt(R),"residue");
    for(let t of [0n,1n,2n,7n])for(let i=0;i<M;i++){
      let a=r+(t<<BigInt(h))+BigInt(i),p=0;for(let l=0;l<h;l++){p+=Number(a%2n);a=T(a);}
      assert(a===zs[0].a+3n**BigInt(zs[0].p)*t&&p===zs[0].p,"lift");liftCases++;
    }
    syncCases++;maxClock=Math.max(maxClock,h);
  }
  for(let p=1;p<=4;p++){
    let L=2*3**(p-1),P=3**p,period=2*3**p,N=3*P,log=Array(P).fill(-1),pw=1;for(let j=0;j<L;j++){log[pw]=j;pw=2*pw%P;}
    let table=Array(L);for(let r=1;r<P;r++)if(r%3){let j=log[(3+Number((()=>{for(let v=1;v<P;v++)if(v*r%P===1)return v;throw Error("inverse");})()))%P];table[j]=r;}
    for(let q of [5n,7n,11n,13n,17n,25n,31n,41n,85n]){
      for(let j=0;j<L;j++){
        let r=table[j],e=2;while(mod((q<<BigInt(e))-BigInt(3*r+1),BigInt(N))!==0n)e++;
        assert(e<=period+1,"bounded exponent");let qq=((q<<BigInt(e))-1n)/3n;
        assert(qq>q&&qq%2n===1n&&qq%3n!==0n,"inverse unit");
        assert(log[Number(qq%BigInt(P))]===mod(log[Number(q%BigInt(P))]+e-j,L),"phase");
        let x=qq;for(let v=0;v<e;v++)x=T(x);assert(x===q,"inverse path");actualPaths++;phaseCases++;
      }
    }
    for(let m=2;m<=12;m++)for(let we=0;we<=4;we++)for(let wo=0;wo<=4;wo++)if(gcd(gcd(m,we),wo)===1){
      let u=wo-we,g=gcd(m,we),d0=gcd(m,we*L);
      for(let delta=0;delta<d0;delta++)for(let target=0;target<d0;target++){
        let t=1;while(mod(t*u-(target-delta),g)!==0)t++;assert(t<=g,"steering length");
        let found=false;for(let j=0;j<L;j++)if(mod(delta+t*u+we*j,d0)===target){found=true;break;}
        assert(found,"phase steering");weightedCases++;
      }
    }
  }
  return {syncCases,liftCases,phaseCases,weightedCases,actualPaths,maxClock};
}
console.log(JSON.stringify(controls(),null,2));
