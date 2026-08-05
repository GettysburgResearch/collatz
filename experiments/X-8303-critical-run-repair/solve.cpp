#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using u64=std::uint64_t; using i64=std::int64_t; using u128=unsigned __int128;
static constexpr u64 K=3149971404836ULL,A=4992586555009ULL;
static constexpr u64 CBL=K/2, EXP=2*K-A, RLEN=CBL-EXP, RWT=EXP-4*RLEN;
static constexpr u64 MOD=1465129870107858983ULL, Q=MOD/7;
static constexpr u64 OMEGA=9029615616ULL;
static u64 mm(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 pw(u64 a,u64 e,u64 m){u64 r=1%m;while(e){if(e&1)r=mm(r,a,m);a=mm(a,a,m);e>>=1;}return r;}
struct S{u64 p,q,c;};
static S mul(S a,S b,u64 m){return {mm(a.p,b.p,m),mm(a.q,b.q,m),(mm(b.p,a.c,m)+mm(a.q,b.c,m))%m};}
static S mpow(S x,u64 n,u64 m){S r{1%m,1%m,0};while(n){if(n&1)r=mul(r,x,m);x=mul(x,x,m);n>>=1;}return r;}
static S mech(u64 ones,u64 len,bool upper,S z,S o,u64 m){
 if(!ones)return mpow(z,len,m);
 if(ones==len)return mpow(o,len,m);
 u64 a=len/ones,r=len%ones;
 if(upper){S nz=mul(o,mpow(z,a-1,m),m),no=mul(o,mpow(z,a,m),m);return mech(r,ones,false,nz,no,m);}
 S nz=mul(mpow(z,a-1,m),o,m),no=mul(mpow(z,a,m),o,m);return mech(r,ones,true,nz,no,m);
}
static S letter(int d,u64 m){u64 r=4+d,e=16+3*d;return {pw(9,5+d,m),pw(2,e,m),mm(48%m,(pw(9,r,m)+m-pw(8,r,m))%m,m)};}
static u64 pref(u64 n){return (u64)(((u128)n*RWT)/RLEN);}
static int bit(u64 n){return (int)(pref(n+1)-pref(n));}
struct Site{u64 pos;int l,r;};
static std::vector<Site> sites(){std::vector<Site>o;u64 pos=0;i64 prev=-2;while(o.size()<80){int l=bit(pos),r=bit(pos+1);if(l!=r&&(i64)pos>prev+1){o.push_back({pos,l,r});prev=(i64)pos;}++pos;}return o;}
static u64 delta(Site s,u64 m){u64 po=pref(s.pos),E=16*s.pos+3*po,B=5*s.pos+po;u64 v=mm(OMEGA%m,pw(2,E,m),m);v=mm(v,pw(9,CBL-B-11,m),m);if(s.l==0&&s.r==1)v=v?m-v:0;return v;}
struct Item{u64 v;std::uint32_t mask;bool operator<(Item const&o)const{return v<o.v||(v==o.v&&mask<o.mask);}};
struct Pair{i64 s;u128 mask;bool operator<(Pair const&o)const{return s<o.s||(s==o.s&&mask<o.mask);}};
static std::vector<Item> subs(const std::vector<u64>&w,u64 shift=0){size_t N=1ULL<<w.size();std::vector<Item>o(N);o[0]={shift%Q,0};for(size_t m=1;m<N;m++){unsigned b=__builtin_ctzll(m);size_t p=m&(m-1);u64 v=o[p].v+w[b];if(v>=Q)v-=Q;o[m]={v,(std::uint32_t)m};}std::sort(o.begin(),o.end());return o;}
static void emit(std::vector<Pair>&o,Item a,const std::vector<Item>&b,u64 B,int off){
 u64 c=a.v?Q-a.v:0;
 auto range=[&](u64 lo,u64 hi){auto x=std::lower_bound(b.begin(),b.end(),Item{lo,0});auto y=std::lower_bound(b.begin(),b.end(),Item{hi,0});for(;x!=y;++x){u64 r=a.v+x->v;if(r>=Q)r-=Q;i64 s=r<=Q/2?(i64)r:(i64)(r-Q);if((u64)(s<0?-s:s)<=B)o.push_back({s,(u128)a.mask|((u128)x->mask<<off)});}};
 if(c>=B&&c+B<Q)range(c-B,c+B+1);else{u64 lo=(c+Q-B)%Q,hi=(c+B)%Q;range(lo,Q);range(0,hi+1);}
}
static std::vector<Pair> near(const std::vector<Item>&a,const std::vector<Item>&b,u64 B,int off){std::vector<Pair>o;o.reserve(a.size()*3);for(auto x:a)emit(o,x,b,B,off);std::sort(o.begin(),o.end());return o;}
int main(){
 auto ss=sites();S base=mech(RWT,RLEN,false,letter(0,MOD),letter(1,MOD),MOD);if(base.c%7)throw std::runtime_error("base not divisible by seven");std::vector<u64>w(80);for(int i=0;i<80;i++){u64 x=delta(ss[i],MOD);if(x%7)throw std::runtime_error("delta not divisible by seven");w[i]=x/7;}u64 target=(Q-base.c/7)%Q;
 std::array<std::vector<u64>,4>g;for(int z=0;z<4;z++)g[z]=std::vector<u64>(w.begin()+20*z,w.begin()+20*z+20);
 auto a=subs(g[0]),b=subs(g[1]),c=subs(g[2]),d=subs(g[3],target?Q-target:0);u64 B=Q/(1ULL<<20);auto x=near(a,b,B,20),y=near(c,d,B,20);u128 sol=0;bool ok=false;for(auto p:x){Pair key{-p.s,0};auto it=std::lower_bound(y.begin(),y.end(),key);if(it!=y.end()&&it->s==-p.s){sol=p.mask|(it->mask<<40);ok=true;break;}}if(!ok)throw std::runtime_error("no solution");u64 sum=0;std::vector<int>idx;for(int i=0;i<80;i++)if((sol>>i)&1){sum+=w[i];sum%=Q;idx.push_back(i);}if(sum!=target)throw std::runtime_error("bad solution");std::cout<<"selected_indices=";for(size_t i=0;i<idx.size();i++)std::cout<<(i?",":"")<<idx[i];std::cout<<"\nselected_positions=";for(size_t i=0;i<idx.size();i++)std::cout<<(i?",":"")<<ss[idx[i]].pos;std::cout<<"\ncount="<<idx.size()<<"\n";
}
