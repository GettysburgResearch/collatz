// Reconstruct a finite nonnegative credit from a supplied fixed strategy.
// This is a verifier for that strategy: no action minimization or search occurs.
// Compile: c++ -O3 -std=c++17 -fopenmp reconstruct_policy.cpp -o reconstruct_policy
// OpenMP is optional: omit -fopenmp for a portable single-thread build.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

int main(int argc, char **argv) {
    try {
        if (argc < 7 || argc > 8)
            throw std::runtime_error("usage: reconstruct_policy D p q limit policy.bits output.u8 [threads]");
        int d = std::stoi(argv[1]), p = std::stoi(argv[2]), q = std::stoi(argv[3]);
        int limit = std::stoi(argv[4]);
        if (d < 2 || d > 19 || q <= 0 || p <= q || limit <= 0)
            throw std::runtime_error("invalid parameters");
#ifdef _OPENMP
        omp_set_num_threads(argc == 8 ? std::stoi(argv[7]) : 4);
#endif
        uint64_t n = 1;
        for (int i = 1; i < d; ++i) n *= 3;
        uint64_t h = n / 3, bit_count = 2 * h;
        std::ifstream in(argv[5], std::ios::binary | std::ios::ate);
        if (!in || in.tellg() != static_cast<std::streamoff>((bit_count + 7) / 8))
            throw std::runtime_error("wrong strategy byte length");
        std::vector<uint8_t> bits((bit_count + 7) / 8);
        in.seekg(0); in.read(reinterpret_cast<char *>(bits.data()), bits.size());
        if (!in) throw std::runtime_error("cannot read strategy");
        if (bit_count % 8 && (bits.back() >> (bit_count % 8)))
            throw std::runtime_error("nonzero padding bits");
        std::vector<uint16_t> v(n, 0), next(n, 0), triple_max(h, 0);
        for (int iteration = 1; iteration <= limit; ++iteration) {
#pragma omp parallel for schedule(static)
            for (uint64_t j = 0; j < h; ++j)
                triple_max[j] = std::max({v[j], v[j+h], v[j+2*h]});
            int changed = 0, overflow = 0, maximum = 0;
#pragma omp parallel for schedule(static) reduction(|:changed) reduction(max:overflow,maximum)
            for (uint64_t j = 0; j < h; ++j) {
                uint64_t i = 3*j, b0 = 2*j, b2 = 2*j+1;
                bool choose_o0 = (bits[b0/8] >> (b0%8)) & 1;
                bool choose_o2 = (bits[b2/8] >> (b2%8)) & 1;
                int x0 = choose_o0 ? 2*q-p+triple_max[(4*j)%h]
                                    : 2*q+v[(4*i+2)%n];
                int x1 = 2*q+v[(4*i+6)%n];
                int x2 = choose_o2 ? q-p+triple_max[(2*j+1)%h]
                                    : 2*q+v[(4*i+10)%n];
                x0 = std::max(x0,0); x2 = std::max(x2,0);
                if (std::max({x0,x1,x2}) > std::numeric_limits<uint16_t>::max())
                    overflow = 1;
                next[i] = static_cast<uint16_t>(x0);
                next[i+1] = static_cast<uint16_t>(x1);
                next[i+2] = static_cast<uint16_t>(x2);
                changed |= (x0 != v[i] || x1 != v[i+1] || x2 != v[i+2]);
                maximum = std::max({maximum,x0,x1,x2});
            }
            if (overflow) throw std::runtime_error("credit overflow; no certificate produced");
            v.swap(next);
            if (iteration % 100 == 0 || !changed)
                std::cout << "fixed-policy iteration " << iteration << ", maximum reduced credit " << maximum << '\n';
            if (!changed) {
                if (maximum > 255) throw std::runtime_error("credit exceeds u8 encoding");
                std::vector<uint8_t> encoded(v.begin(),v.end());
                std::ofstream out(argv[6],std::ios::binary);
                out.write(reinterpret_cast<const char *>(encoded.data()),encoded.size());
                if (!out) throw std::runtime_error("cannot write reconstructed credit");
                std::cout << "PASS: " << encoded.size() << " exact credit bytes\n";
                return 0;
            }
        }
        throw std::runtime_error("no fixed point within the specified horizon");
    } catch (const std::exception &e) {
        std::cerr << "FAIL: " << e.what() << '\n';
        return 1;
    }
}
