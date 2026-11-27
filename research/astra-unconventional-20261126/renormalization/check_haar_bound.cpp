#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
int main() {
    constexpr std::uint64_t bound = 5900000;
    std::vector<unsigned> times(bound+1);
    std::vector<std::uint64_t> path;
    unsigned longest = 0;
    std::uint64_t longest_start = 1;
    std::uint64_t peak = 1;
    for (std::uint64_t start=2; start<=bound; ++start) {
        path.clear();
        std::uint64_t x=start;
        while (x!=1 && (x>=start || !times[x])) {
            if (path.size()>=10000 || x>(std::numeric_limits<std::uint64_t>::max()-1)/3) return 1;
            path.push_back(x);
            x = x%2 ? (3*x+1)/2 : x/2;
            peak=std::max(peak,x);
        }
        unsigned t=times[x];
        for(auto it=path.rbegin();it!=path.rend();++it) {
            ++t;
            if (*it<=bound) times[*it]=t;
        }
        if (times[start]>longest) {longest=times[start];longest_start=start;}
    }
    std::cout<<"limit "<<bound<<" max shortcut time "<<longest<<" attained at "<<longest_start<<" max height "<<peak<<"\n";
}
