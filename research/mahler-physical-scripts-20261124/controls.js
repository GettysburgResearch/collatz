"use strict";
function controls(){
  let counts={telescope:0,substitution:0,regularity:0,ratio:0,physical:0,expanding:0};
  const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a};
  const f=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denom");if(b<0n){a=-a;b=-b}let d=gcd(a,b);return [a/d,b/d]};
  const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]), neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b)), mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]), div=(a,b)=>f(a[0]*b[1],a[1]*b[0]), eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], pow=(a,n)=>n<0?pow(div(f(1),a),-n):f(a[0]**BigInt(n),a[1]**BigInt(n));
  const one=f(1),zero=f(0), words=n=>Array.from({length:2**n},(_,i)=>Array.from({length:n},(_,j)=>(i>>(n-1-j))&1));
  const assert=(b,tag)=>{if(!b)throw Error(tag)};
  function sums(w,x,y){let p=one,z=zero,o=zero;for(let a of w){if(a)o=add(o,p);else z=add(z,p);p=mul(p,a?y:x)}return [p,z,o]}
  const vals=[[f(8,9),f(32,9)],[f(2,3),f(4,27)],[f(4,9),f(4,9)]];
  for(const [x,y] of vals) {
    const tests=[...words(0),...words(1),...words(2),...words(3),...words(4)];
    for(const w of tests){let [p,z,o]=sums(w,x,y);assert(eq(add(mul(sub(one,x),z),mul(sub(one,y),o)),sub(one,p)),"telescope");counts.telescope++}
    for(let b=2;b<=4;b++)for(const u of words(b))for(const v of words(b)){
      if(u.join("")===v.join(""))continue;
      let [xp,,p0]=sums(u,x,y),[yp,,p1]=sums(v,x,y);
      let d=sub(mul(sub(one,xp),p1),mul(sub(one,yp),p0));
      let v2=a=>{if(a===0n)throw Error("zero val");let t=0;while(a%2n===0n){a/=2n;t++}return t};
      let k=u.findIndex((a,i)=>a!==v[i]),t=v2(sums(u.slice(0,k),x,y)[0][0])-v2(sums(u.slice(0,k),x,y)[0][1]);
      assert(d[0]!==0n&&v2(d[0])-v2(d[1])===t,"regularity");counts.regularity++;
      let c0=u.reduce((a,b)=>a+b,0),c1=v.reduce((a,b)=>a+b,0);
      assert(eq(div(yp,xp),pow(div(y,x),c1-c0)),"ratio");counts.ratio++;
      for(const w of tests.slice(0,15)){
        let sw=w.flatMap(a=>a?v:u),[p,z,o]=sums(w,xp,yp),[ps,,os]=sums(sw,x,y);
        assert(eq(ps,p),"weight substitute");
        assert(eq(os,add(mul(p0,z),mul(p1,o))),"one substitute");
        assert(eq(mul(sub(one,xp),os),add(mul(p0,sub(one,p)),mul(d,o))),"finite Mahler");
        counts.substitution++;
      }
    }
  }
  const inv=(g,z)=>div(sub(mul(f(2n**BigInt(g)),z),one),f(3));
  const v2n=a=>{if(!a)throw Error("zero");let k=0;while(a%2n===0n){a/=2n;k++}return k};
  for(let n=0;n<=8;n++)for(const w of words(n))for(const end of [f(1),f(5),f(-7),f(1,5)]){
    const gaps=w.flatMap(a=>a?[1,4]:[2,1]);
    let q=end;for(let j=gaps.length-1;j>=0;j--)q=inv(gaps[j],q);
    let [p,z,o]=sums(w,f(8,9),f(32,9));
    assert(eq(q,add(add(mul(f(-7,9),z),mul(f(-5,9),o)),mul(p,end))),"physical expansion");
    let cur=q;
    for(const g of gaps){let t=add(mul(f(3),cur),one);assert(v2n(t[0])-v2n(t[1])===g,"exact physical gap");cur=div(t,f(2n**BigInt(g)))}
    assert(eq(cur,end),"physical endpoint");counts.physical++;
  }
  for(let b=12;b<=30;b++){assert(9n**BigInt(b)>4n*8n**BigInt(b),"expanding");counts.expanding++}
  return counts;
}
console.log(JSON.stringify(controls(), null, 2));
