#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>

using u64=std::uint64_t;
using u128=__uint128_t;
using i128=__int128_t;

struct Type{std::string name;std::vector<int>highs;int first,last;u64 expected;};
struct Pattern{std::uint32_t code;std::vector<int>v;};
struct Gaps{int sum;std::vector<int>r;};
struct Key{std::uint32_t code;std::uint8_t sum;u64 residue;bool operator==(Key const&o)const{return code==o.code&&sum==o.sum&&residue==o.residue;}};
struct Hash{std::size_t operator()(Key const&k)const noexcept{u64 x=k.residue^(u64(k.code)*0x9e3779b97f4a7c15ULL)^(u64(k.sum)<<56);x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;x^=x>>31;return(std::size_t)x;}};

u64 mul(u64 a,u64 b,u64 m){return(u128)a*b%m;}
i128 eg(i128 a,i128 b,i128&x,i128&y){if(!b){x=1;y=0;return a;}i128 x1,y1,g=eg(b,a%b,x1,y1);x=y1;y=x1-y1*(a/b);return g;}
u64 inv(u64 a,u64 m){i128 x,y;if(eg(a,m,x,y)!=1)std::abort();x%=m;if(x<0)x+=m;return(u64)x;}
u64 smod(i128 x,u64 m){x%=m;if(x<0)x+=m;return(u64)x;}

void patrec(int p,int len,const std::vector<int>&uniq,const std::vector<int>&tot,std::vector<int>&rem,std::vector<int>&v,std::vector<Pattern>&out){
    if(p==len){std::uint32_t c=0;for(std::size_t i=0;i<uniq.size();++i)c|=std::uint32_t(tot[i]-rem[i])<<(3*i);out.push_back({c,v});return;}
    v[p]=1;patrec(p+1,len,uniq,tot,rem,v,out);
    for(std::size_t i=0;i<uniq.size();++i)if(rem[i]){--rem[i];v[p]=uniq[i];patrec(p+1,len,uniq,tot,rem,v,out);++rem[i];}
}
std::pair<std::uint32_t,std::vector<Pattern>> patterns(const std::vector<int>&highs,int len){
    if(highs.empty())return{0,std::vector<Pattern>{{0,std::vector<int>(len,1)}}};
    auto uniq=highs;std::sort(uniq.begin(),uniq.end());uniq.erase(std::unique(uniq.begin(),uniq.end()),uniq.end());
    std::vector<int>tot;std::uint32_t tc=0;for(std::size_t i=0;i<uniq.size();++i){int c=std::count(highs.begin(),highs.end(),uniq[i]);tot.push_back(c);tc|=std::uint32_t(c)<<(3*i);}auto rem=tot;std::vector<int>v(len,1);std::vector<Pattern>out;patrec(0,len,uniq,tot,rem,v,out);return{tc,out};
}
void gaprec(int p,int len,int bound,int rem,std::vector<int>&r,std::vector<Gaps>&out){if(p==len){int s=std::accumulate(r.begin(),r.end(),0);out.push_back({s,r});return;}for(int x=0;x<=bound&&x<=rem;++x){r[p]=x;gaprec(p+1,len,bound,rem-x,r,out);}}
std::vector<Gaps> gaps(int len,int bound,int maxsum,bool zero){std::vector<int>r(len);std::vector<Gaps>out;gaprec(0,len,bound,maxsum,r,out);if(zero)for(auto&o:out)o.r.push_back(0);return out;}

struct Sum{int k,A;u64 E;};
Sum sum(const Pattern&p,const Gaps&g,u64 D,const std::vector<u64>&p2,const std::vector<u64>&p3){int k=0,A=0;u64 E=0;for(std::size_t i=0;i<p.v.size();++i){int bk=1+g.r[i],bA=p.v[i]+2*g.r[i];u64 bE=smod(i128(p3[g.r[i]])*(4-(i128(1)<<p.v[i])),D);E=(mul(p3[bk],E,D)+mul(p2[A],bE,D))%D;k+=bk;A+=bA;}return{k,A,E};}

int main(){
    std::vector<Type>ts={{"1^10",{},15,22,5130175},{"1^9,3",{3},10,21,36647600},{"1^9,4",{4},7,21,36768470},{"1^9,5",{5},5,21,36779440},{"1^9,6",{6},3,21,36781290},{"1^9,7",{7},0,21,36781410},{"1^8,3,3",{3,3},5,21,165507480},{"1^8,3,4",{3,4},3,21,331031610},{"1^8,3,5",{3,5},0,21,331032690},{"1^8,4,4",{4,4},0,21,165516345},{"1^7,3,3,3",{3,3,3},0,21,441376920}};
    u64 grand=0,digest=14695981039346656037ULL;auto absorb=[&](std::string const&s){for(unsigned char c:s){digest^=c;digest*=1099511628211ULL;}};
    for(auto const&t:ts){
        auto[tc,lp]=patterns(t.highs,4);auto[tc2,rp]=patterns(t.highs,6);if(tc!=tc2)return 9;
        int B=10-static_cast<int>(t.highs.size())+std::accumulate(t.highs.begin(),t.highs.end(),0);u64 typetot=0;
        for(int R=t.first;R<t.last;++R){
            u64 p3e=1;for(int i=0;i<10+R;++i)p3e*=3;u64 D=(u64(1)<<(B+2*R))-p3e;u64 i2b=inv(2,D),i3b=inv(3,D);
            std::vector<u64>p2(80),p3(50),i2(80),i3(50);p2[0]=p3[0]=i2[0]=i3[0]=1%D;for(int i=1;i<80;++i){p2[i]=mul(p2[i-1],2,D);i2[i]=mul(i2[i-1],i2b,D);}for(int i=1;i<50;++i){p3[i]=mul(p3[i-1],3,D);i3[i]=mul(i3[i-1],i3b,D);}
            u64 row=0;
            for(int term=(R+9)/10;term<=R;++term){
                int m=R-term;auto lg=gaps(4,term,m,false);auto rg=gaps(5,term,m,true);std::unordered_set<Key,Hash>L;L.reserve(lg.size()*lp.size()*2);std::map<std::pair<std::uint32_t,int>,u64>lc,rc;
                for(auto const&g:lg)for(auto const&p:lp){auto z=sum(p,g,D,p2,p3);L.insert({p.code,(std::uint8_t)g.sum,mul(z.E,i2[z.A],D)});++lc[{p.code,g.sum}];}
                for(auto const&g:rg)for(auto const&p:rp){auto z=sum(p,g,D,p2,p3);u64 nr=mul(z.E,i3[z.k],D);int ls=m-g.sum;std::uint32_t comp=tc-p.code;if(ls>=0&&L.count({comp,(std::uint8_t)ls,nr?D-nr:0})){std::cerr<<"hit\n";return 2;}++rc[{p.code,g.sum}];}
                for(auto const&x:lc){auto it=rc.find({tc-x.first.first,m-x.first.second});if(it!=rc.end())row+=x.second*it->second;}
            }
            typetot+=row;absorb(t.name+"|"+std::to_string(R)+"|"+std::to_string(row)+"\n");
        }
        if(typetot!=t.expected){std::cerr<<"count mismatch "<<t.name<<"\n";return 3;}grand+=typetot;
    }
    if(grand!=1623353430ULL||digest!=0x8b0ed2d5d2377bdaULL){std::cerr<<"global mismatch\n";return 4;}
    std::cout<<"independent X-9608 verification passed\n";
}
