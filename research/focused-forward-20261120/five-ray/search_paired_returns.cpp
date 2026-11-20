// Exact exploratory enumeration of physical equal-clock five-ray returns.
// No Collatz convergence or all-time merger assertion is inferred.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <tuple>

using U = std::uint64_t;
std::array<U, 32> pow3;
int limit;
std::map<std::pair<int,U>, std::tuple<int,U,U>> minimal_images;
std::array<U, 32> hits{};
std::array<U, 32> growing{};

bool covered(int q, U residue) {
    for(int j=1;j<=q;++j)
        if(minimal_images.count({j,residue%pow3[j]})) return true;
    return false;
}

void walk(int h,U r,U x,U y,int p,int q) {
    if(h && p==q && y==5*x+1) {
        ++hits[h];
        if(pow3[p]>(U(1)<<h)) {
            if(!growing[h]) std::cerr<<"growing example "<<h<<' '<<r<<' '<<x<<' '<<p<<'\n';
            ++growing[h];
        }
        U residue=x%pow3[p];
        if(!covered(p,residue)) {
            minimal_images[{p,residue}]={h,r,x};
            std::cout << "new " << h << ' ' << r << ' ' << x << ' ' << p
                      << ' ' << residue << ' ' << ((U(1)<<h)>pow3[p]) << '\n';
        }
    }
    if(h==limit) return;
    for(int bit=0;bit<2;++bit) {
        U a=x+pow3[p]*bit,b=y+5*pow3[q]*bit;
        int ap=a&1,bp=b&1;
        walk(h+1,r+(U(bit)<<h),ap?(3*a+1)/2:a/2,
             bp?(3*b+1)/2:b/2,p+ap,q+bp);
    }
}

int main(int argc,char**argv) {
    limit=argc>1?std::atoi(argv[1]):22;
    if(limit<1 || limit>26) return 2;
    pow3[0]=1;
    for(int j=1;j<32;++j)pow3[j]=3*pow3[j-1];
    walk(0,0,0,1,0,0);
    std::cerr << "h return_classes growing_classes\n";
    for(int h=1;h<=limit;++h)std::cerr<<h<<' '<<hits[h]<<' '<<growing[h]<<'\n';
    std::cerr<<"recorded ternary cones "<<minimal_images.size()<<'\n';
}
