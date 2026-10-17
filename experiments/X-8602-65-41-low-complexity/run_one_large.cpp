#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using u64 = uint64_t;
using u128 = unsigned __int128;
using i128 = __int128;

static string s128(u128 x){ if(!x) return "0"; string s; while(x){s.push_back(char('0'+x%10));x/=10;} reverse(s.begin(),s.end()); return s; }
static u128 pow128(u128 a,int e){u128 r=1;while(e--)r*=a;return r;}
static u64 mulmod(u64 a,u64 b,u64 m){return (u64)((u128)a*b%m);}
static u64 invmod(u64 a,u64 m){
    i128 t=0,nt=1,r=m,nr=a%m;
    while(nr){i128 q=r/nr; i128 tt=t-q*nt;t=nt;nt=tt; i128 rr=r-q*nr;r=nr;nr=rr;}
    if(r!=1) throw runtime_error("nonunit");
    t%=i128(m); if(t<0)t+=m; return (u64)t;
}
struct Rec{u64 residue;u64 code;};

struct Search{
    int m,K,h,l,total_twos,special_exp;
    u64 D;
    array<array<vector<Rec>, 42>,2> left;
    array<u64,66> pow2{};
    u64 pow3l;
    uint64_t right_leaves=0,matches=0;

    void gen_left(int n,int pos,int q2,int z,int kprefix,u64 c,u64 code){
        if(z>1||q2>total_twos) return;
        if(pos==n){
            int q2r=total_twos-q2;
            int zr=1-z;
            if(q2r<0||q2r>l||zr<0||zr>1||q2r+zr>l) return;
            u64 neg = c? D-mulmod(pow3l,c,D):0;
            u64 target=mulmod(neg,invmod(pow2[kprefix],D),D);
            left[z][q2].push_back({target,code});
            return;
        }
        gen_left(n,pos+1,q2,z,kprefix+1,(mulmod(3,c,D)+pow2[kprefix])%D,code);
        gen_left(n,pos+1,q2+1,z,kprefix+2,(mulmod(3,c,D)+pow2[kprefix])%D,code|(u64(1)<<(2*pos)));
        if(z==0) gen_left(n,pos+1,q2,1,kprefix+special_exp,(mulmod(3,c,D)+pow2[kprefix])%D,code|(u64(2)<<(2*pos)));
    }
    vector<int> decode(u64 code,int n){vector<int>w(n);for(int i=0;i<n;i++){int d=(code>>(2*i))&3;w[i]=(d==2?special_exp:1+d);}return w;}
    void verify_hit(u64 lu,u64 rv){
        auto a=decode(lu,h);auto b=decode(rv,l);a.insert(a.end(),b.begin(),b.end());
        u128 C=0,p=1;int kk=0,large=0,qq=0;
        for(int x:a){C=3*C+p;p<<=x;kk+=x;large+=x>=3;qq+=x==2;}
        u128 DD=(u128(1)<<K)-pow128(3,m);
        if(C%DD) throw runtime_error("false modular match");
        u128 x=C/DD;
        cout<<"DIVISIBLE x="<<s128(x)<<" word=";for(int t:a)cout<<t;cout<<"\n";
        cout<<"counts K="<<kk<<" twos="<<qq<<" large="<<large<<"\n";
        u128 y=x; bool ok=x>0&&(x&1);
        for(int t:a){u128 n=3*y+1;int v=0;while((n&1)==0){++v;n>>=1;}if(v!=t){ok=false;break;}y=n;}
        cout<<"verify="<<ok<<" return="<<(y==x)<<" y="<<s128(y)<<"\n";
        if(ok&&y==x&&x>1) exit(0);
    }
    void gen_right(int n,int pos,int q2,int z,int kprefix,u64 c,u64 code){
        if(z>1||q2>total_twos) return;
        if(pos==n){
            ++right_leaves;
            int zl=1-z, ql=total_twos-q2;
            if(zl<0||zl>1||ql<0||ql>h) return;
            auto &v=left[zl][ql];
            auto it=lower_bound(v.begin(),v.end(),c,[](const Rec&r,u64 x){return r.residue<x;});
            for(;it!=v.end()&&it->residue==c;++it){++matches;verify_hit(it->code,code);}return;
        }
        gen_right(n,pos+1,q2,z,kprefix+1,(mulmod(3,c,D)+pow2[kprefix])%D,code);
        gen_right(n,pos+1,q2+1,z,kprefix+2,(mulmod(3,c,D)+pow2[kprefix])%D,code|(u64(1)<<(2*pos)));
        if(z==0)gen_right(n,pos+1,q2,1,kprefix+special_exp,(mulmod(3,c,D)+pow2[kprefix])%D,code|(u64(2)<<(2*pos)));
    }
    void run_one(int e){
        special_exp=e; m=41;K=65;h=20;l=21;total_twos=24-(e-1);
        for(auto &zz:left)for(auto &v:zz)v.clear(); right_leaves=matches=0;
        u128 DD=(u128(1)<<K)-pow128(3,m);D=(u64)DD;
        pow2[0]=1%D;for(int i=1;i<=65;i++)pow2[i]=(pow2[i-1]*2)%D;
        pow3l=1;for(int i=0;i<l;i++)pow3l=mulmod(pow3l,3,D);
        cout<<"special_exp="<<e<<" twos="<<total_twos<<" D="<<D<<"\n";
        gen_left(h,0,0,0,0,0,0);
        uint64_t left_count=0;for(int z=0;z<=1;z++)for(int q=0;q<=h;q++){auto&v=left[z][q];left_count+=v.size();sort(v.begin(),v.end(),[](auto&a,auto&b){return a.residue<b.residue;});}
        gen_right(l,0,0,0,0,0,0);
        cout<<"left_records="<<left_count<<" right_leaves="<<right_leaves<<" modular_matches="<<matches<<" no_nontrivial_hit\n";
    }
    void run(){ cout<<"m=41 K=65 exactly_one_exponent_ge_3\n"; for(int e=3;e<=25;e++)run_one(e); }
};
int main(){Search s;s.run();}
