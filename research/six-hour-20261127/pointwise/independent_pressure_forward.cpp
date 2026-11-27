#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <algorithm>

using Wide = unsigned __int128;
constexpr int stages=8;
constexpr int M=19683;
std::array<int,stages+2> mod{1};
std::array<std::array<int,11>,stages+1> inv{};
std::array<Wide,M> totals{};
std::uint64_t full=0, retained=0;
std::string dec(Wide v) {
    if(v==0) return "0";
    std::string s;
    while(v>0){s.push_back('0'+v%10);v/=10;}
    std::reverse(s.begin(),s.end());return s;
}
void forward(int depth, int state, int A, int startClass) {
    if(depth==stages){
        ++full;
        if(A>=13){++retained;totals[state]+=Wide(startClass)<<(80-A);}
        return;
    }
    int nmod=mod[depth+2];
    int z=3*state+1;
    for(int e=1;e<=10;++e)
        forward(depth+1, (std::int64_t(z)*inv[depth+1][e])%nmod, A+e, startClass);
}
int main(){
    for(int i=1;i<=9;++i)mod[i]=3*mod[i-1];
    for(int r=1;r<=8;++r){
        int v=1, nmod=mod[r+1];
        for(int e=1;e<=10;++e){v=(v%2?v+nmod:v)/2;inv[r][e]=v;}
    }
    forward(0,1,0,1);forward(0,2,0,2);
    int arg=1, nmin=0;
    for(int i=1;i<M;++i)if(i%3){
        if(totals[i]*(arg%3)<totals[arg]*(i%3))arg=i;
    }
    for(int i=1;i<M;++i)if(i%3 && totals[i]*(arg%3)==totals[arg]*(i%3))++nmin;
    std::cout<<"{\"word_and_initial_unit_fibres\":"<<full<<",\"retained_fibres\":"<<retained
             <<",\"argminimum\":"<<arg<<",\"multiplicity\":"<<nmin
             <<",\"raw_numerator\":\""<<dec(totals[arg])<<"\",\"raw_denominator\":\""
             <<dec(Wide(arg%3)<<80)<<"\"}\n";
}
