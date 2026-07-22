#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using i128 = __int128_t;
static std::array<i128,80> p2{};
static std::array<i128,50> p3{};

struct Type {
    std::string name;
    std::array<int,9> base;
    int first_R;
    int last_R;
    std::vector<std::array<int,9>> words;
    uint64_t expected_candidates;
    uint64_t expected_height;
};

static std::array<int,9> rotate(const std::array<int,9>& word, int shift) {
    std::array<int,9> out{};
    for (int i=0;i<9;++i) out[i]=word[(i+shift)%9];
    return out;
}
static std::vector<std::array<int,9>> rotations(const std::array<int,9>& word) {
    std::vector<std::array<int,9>> out;
    for (int s=0;s<9;++s) out.push_back(rotate(word,s));
    std::sort(out.begin(),out.end());
    out.erase(std::unique(out.begin(),out.end()),out.end());
    return out;
}
static std::vector<std::array<int,9>> one(int value) {
    std::vector<std::array<int,9>> out;
    for (int p=0;p<9;++p) { std::array<int,9>w{}; w.fill(1); w[p]=value; out.push_back(w); }
    return out;
}
static std::vector<std::array<int,9>> equal_pair() {
    std::vector<std::array<int,9>> out;
    for (int p=0;p<9;++p) for (int q=p+1;q<9;++q) { std::array<int,9>w{};w.fill(1);w[p]=w[q]=3;out.push_back(w); }
    return out;
}
static std::vector<std::array<int,9>> ordered_pair() {
    std::vector<std::array<int,9>> out;
    for (int p=0;p<9;++p) for (int q=0;q<9;++q) if(p!=q) { std::array<int,9>w{};w.fill(1);w[p]=3;w[q]=4;out.push_back(w); }
    return out;
}
static std::vector<std::array<int,9>> triples() {
    std::set<std::array<int,9>> out;
    for (const auto& w : {std::array<int,9>{1,1,1,1,3,3,1,1,3},std::array<int,9>{1,1,1,3,1,3,1,1,3},std::array<int,9>{1,1,3,1,1,3,1,1,3}})
        for (const auto& r : rotations(w)) out.insert(r);
    return {out.begin(),out.end()};
}

static i128 centered_by_blocks(const std::array<int,9>& word,const std::array<int,9>& gaps) {
    i128 E=0;
    int A=0;
    for (int i=0;i<9;++i) {
        int gap=i<8?gaps[i]:0;
        i128 block_E=p3[gap]*(4-p2[word[i]]);
        E=p3[1+gap]*E+p2[A]*block_E;
        A+=word[i]+2*gap;
    }
    return E;
}

struct Counts { uint64_t candidates=0,height=0,hits=0; };
static void gaps(int index,int remaining,int maximum,std::array<int,9>& gap,const Type& type,i128 D,Counts& count) {
    if(index==8) {
        gap[8]=remaining;
        if(remaining<maximum) return;
        for(const auto& word:type.words) {
            ++count.candidates;
            i128 E=centered_by_blocks(word,gap);
            i128 rem=E%D; if(rem<0) rem+=D;
            if(rem==0) ++count.hits;
            if(E>=2*D) ++count.height;
        }
        return;
    }
    for(int x=0;x<=remaining;++x) { gap[index]=x; gaps(index+1,remaining-x,std::max(maximum,x),gap,type,D,count); }
}

int main() {
    p2[0]=p3[0]=1;
    for(int i=1;i<80;++i)p2[i]=2*p2[i-1];
    for(int i=1;i<50;++i)p3[i]=3*p3[i-1];
    std::array<int,9> all{}; all.fill(1);
    std::vector<Type> types{
        {"1^9",all,13,19,{all},593995,3954},
        {"1^8,3",{1,1,1,1,1,1,1,1,3},8,19,one(3),5716692,16938},
        {"1^8,4",{1,1,1,1,1,1,1,1,4},6,19,one(4),5730246,3734},
        {"1^8,5",{1,1,1,1,1,1,1,1,5},4,19,one(5),5733198,1712},
        {"1^8,6",{1,1,1,1,1,1,1,1,6},1,19,one(6),5733621,1049},
        {"1^7,3,3",{1,1,1,1,1,1,1,3,3},4,19,equal_pair(),22932792,4945},
        {"1^7,3,4",{1,1,1,1,1,1,1,3,4},1,19,ordered_pair(),45868968,4431},
        {"1^7,3,5",{1,1,1,1,1,1,1,3,5},0,19,rotations({1,1,1,1,5,1,1,1,3}),5733630,138},
        {"1^6,3,3,3",{1,1,1,1,1,1,3,3,3},0,10,triples(),160041,87}
    };
    uint64_t total_candidates=0,total_height=0,total_hits=0;
    for(const auto& type:types) {
        Counts count;
        int B=0; for(int x:type.base) B+=x;
        for(int R=type.first_R;R<type.last_R;++R) {
            i128 D=p2[B+2*R]-p3[9+R];
            std::array<int,9> gap{};
            gaps(0,R,0,gap,type,D,count);
        }
        if(count.candidates!=type.expected_candidates||count.height!=type.expected_height||count.hits!=0) {
            std::cerr<<"mismatch in "<<type.name<<"\n";
            return 2;
        }
        total_candidates+=count.candidates;total_height+=count.height;total_hits+=count.hits;
    }
    if(total_candidates!=98203183ULL||total_height!=36988ULL||total_hits!=0) return 3;
    std::cout<<"independent X-9607 verification passed\n";
}
