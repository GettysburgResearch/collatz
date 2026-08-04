#include <bits/stdc++.h>
using namespace std;
using u128=unsigned __int128; using u64=uint64_t;

static string s128(u128 x){if(!x)return"0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
static u128 powu(u128 a,int e){u128 r=1;while(e--){r*=a;}return r;}
static u128 egcd_inv(u128 a,u128 mod){
    __int128 t=0,newt=1,r=(__int128)mod,newr=(__int128)(a%mod);
    while(newr){__int128 q=r/newr; auto tt=t-q*newt;t=newt;newt=tt;auto rr=r-q*newr;r=newr;newr=rr;}
    if(r!=1) throw runtime_error("nonunit"); if(t<0)t+=mod; return (u128)t;
}
struct Rec{u64 residue; uint32_t mask;};

u128 summaryC(uint32_t mask,int n){
    // bit 1 -> exponent 2, bit 0 -> exponent 1
    u128 C=0,p2=1;
    for(int i=0;i<n;i++){
        C=3*C+p2;
        int a=1+((mask>>i)&1u); p2 <<= a;
    }
    return C;
}
int pop(uint32_t x){return __builtin_popcount(x);}

int main(int argc,char**argv){
 int m=argc>1?stoi(argv[1]):41; int K=argc>2?stoi(argv[2]):65; int h=m/2,l=m-h; int q=K-m;
 if(h>31||l>31){cerr<<"halves >31 unsupported\n";return 2;}
 u128 P3=powu(3,m), P2=((u128)1<<K), D=P2-P3;
 cout<<"m="<<m<<" K="<<K<<" q2="<<q<<" D="<<s128(D)<<" h="<<h<<" l="<<l<<"\n";
 vector<vector<Rec>> left(h+1);
 u128 p3l=powu(3,l);
 for(uint32_t mask=0;mask<(1u<<h);mask++){
   int qu=pop(mask); if(qu>q||q-qu>l)continue;
   u128 Cu=summaryC(mask,h)%D;
   int Ku=h+qu;
   u128 inv=egcd_inv(((u128)1<<Ku)%D,D);
   u128 targetFactor=(D-((p3l*Cu)%D))%D;
   u64 target=(u64)((targetFactor*inv)%D);
   left[qu].push_back({target,mask});
 }
 for(auto &v:left) sort(v.begin(),v.end(),[](auto&a,auto&b){return a.residue<b.residue;});
 uint64_t checked=0, matches=0;
 for(uint32_t mask=0;mask<(1u<<l);mask++){
   int qv=pop(mask),qu=q-qv; if(qu<0||qu>h)continue;
   u64 Cv=(u64)(summaryC(mask,l)%D);
   auto &vec=left[qu];
   auto it=lower_bound(vec.begin(),vec.end(),Cv,[](const Rec&r,u64 x){return r.residue<x;});
   for(;it!=vec.end()&&it->residue==Cv;++it){
      matches++;
      uint32_t mu=it->mask,mv=mask;
      vector<int>a; for(int i=0;i<h;i++)a.push_back(1+((mu>>i)&1));for(int i=0;i<l;i++)a.push_back(1+((mv>>i)&1));
      u128 C=0,p=1;for(int x:a){C=3*C+p;p<<=x;}
      if(C%D==0){
        u128 x=C/D;
        cout<<"DIVISIBLE x="<<s128(x)<<" word=";for(int z:a)cout<<z;cout<<"\n";
        u128 y=x; bool ok=(x>0 && (x&1));
        for(int z:a){u128 n=3*y+1;int vv=0;while((n&1)==0){vv++;n>>=1;}if(vv!=z){ok=false;break;}y=n;}
        cout<<"verify="<<ok<<" return="<<(y==x)<<" y="<<s128(y)<<"\n";
        if(ok&&y==x&&x>1)return 0;
      }
   }
   checked++;
 }
 cout<<"checked_right="<<checked<<" modular_matches="<<matches<<" no_nontrivial_hit\n";
}
