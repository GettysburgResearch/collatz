"use strict";
function primitiveControls(){
  let counts={periodicRegularity:0,prefixCases:0,transverse:0};
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
  const f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}let d=gcd(a,b);return[a/d,b/d]};
  const one=f(1),zero=f(0), add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),sub=(a,b)=>add(a,[-b[0],b[1]]),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),pow=(a,n)=>n<0?pow(div(one,a),-n):f(a[0]**BigInt(n),a[1]**BigInt(n)),eq=(a,b)=>a[0]===b[0]&&a[1]===b[1];
  const words=n=>Array.from({length:2**n},(_,i)=>Array.from({length:n},(_,j)=>(i>>(n-1-j))&1));
  const sums=(w,x,y)=>{let p=one,P=zero;for(const a of w){if(a)P=add(P,p);p=mul(p,a?y:x)}return[p,P]};
  const v2n=x=>{if(!x)throw Error("zero valuation");let i=0;while(x%2n===0n){x/=2n;i++}return i},v2=x=>v2n(x[0])-v2n(x[1]);
  const assert=(p,t)=>{if(!p)throw Error(t)};
  let ws=[...words(1),...words(2),...words(3),...words(4),...words(5)];
  for(const [x,y] of [[f(8,9),f(32,9)],[f(16,27),f(2,3)],[f(4,3),f(4,3)]]){
    for(const u of ws)for(const w of ws){
      let [xp,P]=sums(u,x,y),[yp,Q]=sums(w,x,y),D=sub(mul(sub(one,xp),Q),mul(sub(one,yp),P));
      let k=0;while(k<u.length*w.length&&u[k%u.length]===w[k%w.length])k++;
      if(k===u.length*w.length)assert(D[0]===0n,"common repetition");
      else{
        assert(D[0]!==0n,"distinct periodic images");
        let pref=Array.from({length:k},(_,i)=>u[i%u.length]);
        assert(v2(D)===v2(sums(pref,x,y)[0]),"first difference valuation");
      }
      counts.periodicRegularity++;
      if(u.length!==w.length&&(u.every((a,i)=>a===w[i])||w.every((a,i)=>a===u[i])))counts.prefixCases++;
    }
  }
  // Exhaust positive 2x2 incidence matrices with an integer Perron root and
  // verify the complete transverse ratio identity at rational physical points.
  let x=f(8,9),y=f(32,9);
  for(let a=1;a<=5;a++)for(let b=1;b<=5;b++)for(let c=1;c<=5;c++)for(let d=1;d<=5;d++){
    let disc=(a-d)**2+4*b*c,s=Math.sqrt(disc);if(!Number.isInteger(s)||(a+d+s)%2)continue;
    let lam=(a+d+s)/2,mu=a+d-lam,p=b,q=lam-a,gg=Number(gcd(BigInt(p),BigInt(q)));p/=gg;q/=gg;
    assert(a*p+b*q===lam*p&&c*p+d*q===lam*q,"PF weight");
    let xp=mul(pow(x,a),pow(y,b)),yp=mul(pow(x,c),pow(y,d));
    let r=div(pow(y,p),pow(x,q));
    assert(eq(div(pow(yp,p),pow(xp,q)),pow(r,mu)),"transverse");
    counts.transverse++;
  }
  return counts;
}
console.log(JSON.stringify(primitiveControls(),null,2));
