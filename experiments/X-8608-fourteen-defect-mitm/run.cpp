#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <stdexcept>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using boost::multiprecision::uint128_t;
using boost::multiprecision::uint256_t;
using u64=uint64_t; using u128=unsigned __int128;

template<class R> struct Entry { R residue; u64 code; bool operator<(Entry const&o)const{return residue<o.residue || (residue==o.residue&&code<o.code);} };
cpp_int ipow(cpp_int a,int e){cpp_int r=1;while(e-- >0)r*=a;return r;}
cpp_int comb(int n,int k){if(k<0||k>n)return 0;if(k>n-k)k=n-k;cpp_int r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}

u64 mul64(u64 a,u64 b,u64 m){return (u128)a*b%m;}
uint128_t mul128(uint128_t a,uint128_t b,uint128_t m){return uint128_t(uint256_t(a)*uint256_t(b)%uint256_t(m));}
template<class R> R addmod(R a,R b,R m){return (a+b)%m;}
u64 addmod(u64 a,u64 b,u64 m){return (u64)(((u128)a+b)%m);}
template<class R> R submod(R a,R b,R m){return a>=b?a-b:m-(b-a);}

template<class R,class Mul> struct Engine {
  R D; Mul mul; std::vector<R> p2,p3,p4;
  Engine(R d,Mul mm,int maxe):D(d),mul(mm),p2(maxe+2),p3(maxe+2),p4(maxe+2){p2[0]=p3[0]=p4[0]=R(1)%D;for(int i=1;i<(int)p2.size();i++){p2[i]=addmod(p2[i-1],p2[i-1],D);p3[i]=addmod(addmod(p3[i-1],p3[i-1],D),p3[i-1],D);p4[i]=addmod(addmod(p4[i-1],p4[i-1],D),addmod(p4[i-1],p4[i-1],D),D);}}
  R append_block(R C,int K,int a,int g)const{
    R diff=submod(p4[g],p3[g],D);
    R x=mul(p3[g+1],C,D);
    R y=mul(p3[g],p2[K],D);
    R z=mul(p2[K+a],diff,D);
    return addmod(addmod(x,y,D),z,D);
  }
};

u64 encode_add(u64 code,int idx,int a,int g){return code | ((u64)a<<(4*idx)) | ((u64)g<<(28+5*idx));}
void decode(u64 x,std::array<int,7>&a,std::array<int,7>&g){for(int i=0;i<7;i++){a[i]=(x>>(4*i))&15;g[i]=(x>>(28+5*i))&31;}}

uint64_t count_def(int n,int S){if(n==0)return S==0;uint64_t z=0;for(int a=1;a<=S-(n-1);a++)if(a!=2)z+=count_def(n-1,S-a);return z;}

cpp_int exact_C(std::vector<int>const&w){cpp_int C=0;int K=0;for(int a:w){C=3*C+(cpp_int(1)<<K);K+=a;}return C;}
int v2(cpp_int x){int v=0;while((x&1)==0){x>>=1;v++;}return v;}
bool replay(std::array<int,14>const&a,std::array<int,14>const&g,cpp_int D,cpp_int&start){std::vector<int>w;for(int i=0;i<14;i++){w.push_back(a[i]);for(int z=0;z<g[i];z++)w.push_back(2);}cpp_int C=exact_C(w);if(C%D!=0)return false;start=C/D;if(start<=0||(start&1)==0)return false;cpp_int n=start;for(int x:w){cpp_int q=3*n+1;int vv=v2(q);if(vv!=x)return false;n=q>>x;if(n<=0||(n&1)==0)return false;}return n==start;}

template<class R,class Mul,class Callback>
void gen_half(Engine<R,Mul>const&E,int idx,int remB,int remG,R C,int K,u64 code,Callback cb){
 if(idx==6){int a=remB,g=remG;if(a<1||a==2||g<0)return;R out=E.append_block(C,K,a,g);cb(out,encode_add(code,idx,a,g));return;}
 int remain=6-idx;
 for(int a=1;a<=remB-remain;a++){if(a==2)continue;int rb=remB-a;
   if(count_def(remain,rb)==0)continue;
   for(int g=0;g<=remG;g++){R out=E.append_block(C,K,a,g);gen_half(E,idx+1,rb,remG-g,out,K+a+2*g,encode_add(code,idx,a,g),cb);}
 }
}

template<class R,class Mul>
int process_pair(int Rtot,int B,R D,cpp_int DD,Mul mul,uint64_t&left_states,uint64_t&right_states,uint64_t&queries){
 Engine<R,Mul>E(D,mul,B+2*Rtot+10);int hits=0;
 for(int BL=7;BL<=B-7;BL++){if(!count_def(7,BL)||!count_def(7,B-BL))continue;
  for(int u=0;u<=Rtot;u++){int v=Rtot-u;int KL=BL+2*u,lenR=7+v;R fR=E.p2[KL],fL=E.p3[lenR];
   std::vector<Entry<R>> rv;uint64_t reserve=count_def(7,B-BL)*(uint64_t)comb(v+6,6);rv.reserve(reserve);
   gen_half(E,0,B-BL,v,R(0),0,0,[&](R c,u64 code){rv.push_back({mul(fR,c,D),code});});
   std::sort(rv.begin(),rv.end());right_states+=rv.size();
   gen_half(E,0,BL,u,R(0),0,0,[&](R c,u64 code){left_states++;queries++;R p=mul(fL,c,D);R target=p==0?R(0):D-p;auto it=std::lower_bound(rv.begin(),rv.end(),Entry<R>{target,0});for(;it!=rv.end()&&it->residue==target;++it){std::array<int,7> al{},gl{},ar{},gr{};decode(code,al,gl);decode(it->code,ar,gr);std::array<int,14> aa{},gg{};for(int i=0;i<7;i++){aa[i]=al[i];gg[i]=gl[i];aa[7+i]=ar[i];gg[7+i]=gr[i];}cpp_int st;if(!replay(aa,gg,DD,st))throw std::runtime_error("formal divisor replay failure");hits++;std::cout<<"HIT R="<<Rtot<<" B="<<B<<" start="<<st<<"\n";}});
  }
 }
 return hits;
}

int main(){uint64_t ls=0,rs=0,qs=0;int windows=0,hits=0;cpp_int conceptual=0;std::cout.setf(std::ios::unitbuf);std::cout<<"X-8608 full support-fourteen MITM\n";
 for(int Rtot=0;Rtot<100;Rtot++){bool any=false;int k=14+Rtot;for(int B=14;B<100;B++){int A=B+2*Rtot;cpp_int twoA=cpp_int(1)<<A,three=ipow(3,k);if(twoA*ipow(7,k)>ipow(22,k))break;if(!(three<twoA))continue;cpp_int dc=0;for(int BL=7;BL<=B-7;BL++)dc+=cpp_int(count_def(7,BL))*count_def(7,B-BL);if(dc==0)continue;any=true;windows++;conceptual+=dc*comb(Rtot+13,13);cpp_int DD=twoA-three;int h;if(A<=64){u64 D=(u64)DD;h=process_pair<u64>(Rtot,B,D,DD,mul64,ls,rs,qs);}else{uint128_t D=uint128_t(DD);h=process_pair<uint128_t>(Rtot,B,D,DD,mul128,ls,rs,qs);}hits+=h;std::cout<<"window R="<<Rtot<<" B="<<B<<" defects="<<dc<<" gaps="<<comb(Rtot+13,13)<<" hits="<<h<<"\n";}
 if(!any&&Rtot>26)break;}
 std::cout<<"windows="<<windows<<"\nconceptual_words="<<conceptual<<"\nleft_states="<<ls<<"\nright_states="<<rs<<"\nqueries="<<qs<<"\nhits="<<hits<<"\n";return hits?1:0;}
