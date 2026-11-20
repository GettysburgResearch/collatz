// Optional integer synthesis accelerator.  The standalone verifier is Python.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iterator>
#include <stdexcept>
#include <string>
#include <vector>

struct Edge { int action, child[3]; };
struct Row { std::array<Edge, 6> edges; int count = 0; };

int main(int argc, char** argv) {
    if (argc != 8 && argc != 9) {
        std::cerr << "usage: search_credit DIGITS P Q AMAX LIMIT OUT RESUME [START_ITER]\n";
        return 2;
    }
    int digits = std::stoi(argv[1]), p = std::stoi(argv[2]);
    int q = std::stoi(argv[3]), amax = std::stoi(argv[4]);
    int limit = std::stoi(argv[5]), start = argc == 9 ? std::stoi(argv[8]) : 0;
    if (digits < 2 || digits > 14 || amax < 4 || amax > 12 ||
        p < 1 || p > 1000 || q < 1 || q > 1000 ||
        limit < 1 || limit > 10000 || start < 0 || start >= limit) return 2;
    int modulus = 1;
    for (int i = 0; i < digits; ++i) modulus *= 3;
    int count = modulus / 3 * 2;
    auto index = [](int r) { return r - r / 3 - 1; };
    std::vector<Row> rows(count);
    for (int r = 1; r < modulus; ++r) if (r % 3) {
        auto& row = rows[index(r)];
        for (int a = 1; a <= amax; ++a) {
            long long num = (1LL << a) * r - 1;
            if (num % 3 || (num / 3) % 3 == 0) continue;
            auto& edge = row.edges[row.count++];
            edge.action = a;
            for (int h = 0; h < 3; ++h) {
                long long child = num / 3 + (1LL << a) * (modulus / 3) * h;
                edge.child[h] = index(static_cast<int>(child % modulus));
            }
        }
    }
    std::vector<int> values(count, 0), next(count);
    if (std::string(argv[7]) != "-") {
        std::ifstream in(argv[7]);
        std::string raw((std::istreambuf_iterator<char>(in)), {});
        auto pos = raw.find("\"values\"");
        if (pos == std::string::npos) throw std::runtime_error("missing values");
        pos = raw.find('[', pos);
        if (pos == std::string::npos) throw std::runtime_error("missing vector");
        const char* cursor = raw.c_str() + pos + 1;
        char* end;
        for (int i = 0; i < count; ++i) {
            values[i] = static_cast<int>(std::strtol(cursor, &end, 10));
            if (cursor == end || values[i] < 0) throw std::runtime_error("bad value");
            cursor = end;
            while (*cursor == ',' || *cursor == ' ' || *cursor == '\n') ++cursor;
        }
        if (*cursor != ']') throw std::runtime_error("wrong vector length");
    }
    auto begin = std::chrono::steady_clock::now();
    bool fixed = false;
    int iteration = start;
    for (iteration = start + 1; iteration <= limit; ++iteration) {
        fixed = true;
        for (int i = 0; i < count; ++i) {
            int best = 1000000000;
            const auto& row = rows[i];
            for (int j = 0; j < row.count; ++j) {
                const auto& e = row.edges[j];
                int cost = q * e.action - p;
                if (cost >= best) break;
                int maximum = std::max({values[e.child[0]], values[e.child[1]], values[e.child[2]]});
                best = std::min(best, cost + maximum);
            }
            next[i] = std::max(0, best);
            if (next[i] < values[i]) throw std::runtime_error("iteration is not monotone");
            fixed = fixed && next[i] == values[i];
        }
        values.swap(next);
        if (fixed || iteration % 100 == 0) {
            auto bounds = std::minmax_element(values.begin(), values.end());
            std::cout << "iteration=" << iteration << " min=" << *bounds.first
                      << " max=" << *bounds.second << " fixed=" << fixed << std::endl;
        }
        if (fixed) break;
    }
    if (iteration > limit) iteration = limit;
    auto bounds = std::minmax_element(values.begin(), values.end());
    double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
    std::ofstream out(argv[6]);
    if (!out) throw std::runtime_error("cannot open output file");
    out << "{\"summary\":{\"digits\":" << digits << ",\"p\":" << p
        << ",\"q\":" << q << ",\"amax\":" << amax
        << ",\"iterations\":" << iteration << ",\"min\":" << *bounds.first
        << ",\"max\":" << *bounds.second << ",\"pass\":" << (fixed ? "true" : "false")
        << ",\"seconds\":" << seconds << "},\"values\":[";
    for (int i = 0; i < count; ++i) {
        if (i) out << ',';
        out << values[i];
    }
    out << "]}\n";
    std::cout << "seconds=" << seconds << std::endl;
    return fixed ? 0 : 1;
}
