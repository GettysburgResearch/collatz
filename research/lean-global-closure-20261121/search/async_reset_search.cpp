#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
using I=long long;
struct Rule {int h,k,p,delta,peak; I C,D,r,res,mod;};
int H=23, E=22; I pow3[50];
std::vector<int> qt(50); std::vector<I> dt(50);
std::map<std::pair<I,I>,Rule> rules;
I inv2mod(I x,I m) {I a=(m+1)/2,r=1;while(x--)r=(__int128(r)*a)%m;return r;}
void walk(int h,I r,I X,I Y,int p,I C,int q,I D,int last,int peak) {
  if(h && last==h-1) {
    for(int k=1;k<=h;k++) if(qt[k]==p+1 && dt[k]==6*C+pow3[p+1]-(I(1)<<k)) {
      int delta=h-k+1;
      if(delta>E || peak>E) continue;
      I mod=pow3[p],res=(__int128(C)*inv2mod(k-1,mod))%mod;
      if(res%3==0) {std::cerr<<"nonunit guard\n";std::exit(2);}
      Rule rule{h,k,p,delta,peak,C,dt[k],r,res,mod};
      auto key=std::make_pair(mod,res);
      auto it=rules.find(key);
      if(it==rules.end() || std::make_pair(h,delta)<std::make_pair(it->second.h,it->second.delta)) rules[key]=rule;
    }
  }
  if(h==H)return;
  for(int b=0;b<2;b++) {
    if(h==0 && b==0)continue;
    I xx=X+pow3[p]*b,yy=Y+2*pow3[q]*b;
    int ep=xx&1,eq=yy&1;
    I nx=ep?(3*xx+1)/2:xx/2,ny=eq?(3*yy+1)/2:yy/2;
    I nc=ep?3*C+(I(1)<<h):C,nd=eq?3*D+(I(1)<<h):D;
    qt[h+1]=q+eq; dt[h+1]=nd;
    int npeak=peak,nlast=last;
    if(ep) {if(last>=0)npeak=std::max(peak,h-last);nlast=h;}
    walk(h+1,r+(I(1)<<h)*b,nx,ny,p+ep,nc,q+eq,nd,nlast,npeak);
  }
}
int main(int argc,char**argv) {
 H=argc>1?std::atoi(argv[1]):23; E=argc>2?std::atoi(argv[2]):22;
 if(H>35 || H<1){std::cerr<<"Supported depth is 1..35\n";return 2;}
 pow3[0]=1;for(int i=1;i<39;i++)pow3[i]=3*pow3[i-1];
 walk(0,0,0,-1,0,0,0,0,-1,0);
 std::vector<Rule> keep;
 for(auto const&[key,a]:rules) {
   bool covered=false;
   for(auto const& b:keep)if(a.res%b.mod==b.res){covered=true;break;}
   if(!covered)keep.push_back(a);
 }
 long double density=0;for(auto&a:keep)density+=1.L/a.mod;
 std::cerr<<"H "<<H<<" E "<<E<<" rules "<<rules.size()<<" disjoint "<<keep.size()<<" unit coverage "<<double(1.5L*density)<<"\n";
 std::cout<<"h,k,p,delta,peak,C,D,r,res,mod\n";
 for(auto&a:keep)std::cout<<a.h<<","<<a.k<<","<<a.p<<","<<a.delta<<","<<a.peak<<","<<a.C<<","<<a.D<<","<<a.r<<","<<a.res<<","<<a.mod<<"\n";
}
