// Exact fixed-point enclosure of the original geometric Syracuse law.
// No floating-point operation enters a bound or a pass/fail decision.
// Compile: g++ -std=c++20 -O3 -Wall -Wextra check_depth_difference.cpp -o checker
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using UInt = unsigned __int128;
using Int = __int128;
constexpr unsigned precision = 88;
constexpr unsigned tail = 112;
constexpr UInt scale = UInt(1) << precision;

std::string decimal(UInt n) {
    if (!n) return "0";
    std::string s;
    while (n) { s.push_back(char('0' + n % 10)); n /= 10; }
    std::reverse(s.begin(), s.end());
    return s;
}

std::string signed_decimal(Int n) {
    return n < 0 ? "-" + decimal(UInt(-n)) : decimal(UInt(n));
}

Int floor_div(Int n, std::uint64_t d) {
    Int q = n / Int(d);
    if (n < 0 && n % Int(d)) --q;
    return q;
}

Int ceil_div(Int n, std::uint64_t d) { return -floor_div(-n, d); }

UInt absolute(Int x) { return UInt(x < 0 ? -x : x); }

int main() {
    // The only finite range asserted by this program is depth 1 through 14.
    // The theorem rho_k <= 2^k bounds all 128-bit intermediates below 2^105.
    std::vector<UInt> old(1, scale);
    UInt previous_error = 0;
    std::uint64_t oldq = 1;
    bool positive_at_fourteen = false;
    std::cout << "{\n  \"arithmetic\": \"integer fixed-point interval enclosure\",\n"
              << "  \"scale\": \"" << decimal(scale) << "\",\n"
              << "  \"precision_bits\": " << precision << ",\n"
              << "  \"tail_terms\": " << tail << ",\n  \"rows\": [\n";
    for (unsigned k = 1; k <= 14; ++k) {
        std::uint64_t q = 3 * oldq, order = 2 * oldq;
        std::vector<UInt> next(q, 0);
        std::vector<unsigned char> seen(q, 0);
        // rho_k(r)=rho_k(2r)/2 + (3/2) 1_{r=2(3)} rho_{k-1}((2r-1)/3).
        // Unroll from r=1 for 'tail' terms, wrapping the actual unit group.
        UInt at_one = 0;
        std::uint64_t r = 1;
        for (unsigned i = 0; i < tail; ++i) {
            if (r % 3 == 2) {
                std::uint64_t parent = ((2 * r - 1) / 3) % oldq;
                at_one += (3 * old[parent]) >> (i + 1);
            }
            r = (2 * r) % q;
        }
        // The omitted geometric tail is < one scale unit for every k<=14.
        // Input enclosure costs <=3*previous_error; each rounded term <1.
        UInt error = 3 * previous_error + tail + 2;
        UInt running = at_one;
        r = (q + 1) / 2; // 2^(order-1) modulo q.
        for (std::uint64_t i = order; i > 0; --i) {
            if (seen[r] || r % 3 == 0) return 3;
            seen[r] = 1;
            UInt input = 0;
            if (r % 3 == 2) input = 3 * old[((2 * r - 1) / 3) % oldq];
            running = (running + input) >> 1;
            next[r] = running;
            r = r % 2 ? (r + q) / 2 : r / 2;
        }
        if (r != (q + 1) / 2) return 2;
        Int sum_lo = 0, sum_hi = 0;
        UInt abs_lo = 0, abs_hi = 0;
        for (std::uint64_t y = 1; y < 2 * q; y += 2) {
            Int difference = Int(next[y % q]) - Int(old[y % oldq]);
            Int lo = difference - Int(previous_error), hi = difference + Int(error);
            sum_lo += floor_div(lo, y);
            sum_hi += ceil_div(hi, y);
            UInt small = lo <= 0 && hi >= 0 ? 0 : std::min(absolute(lo), absolute(hi));
            UInt large = std::max(absolute(lo), absolute(hi));
            abs_lo += small / y;
            abs_hi += (large + y - 1) / y;
        }
        if (k == 14) positive_at_fourteen = sum_lo > 0;
        std::cout << "    {\"depth\": " << k << ", \"modulus\": " << q
                  << ", \"uniform_density_error_units\": \"" << decimal(error)
                  << "\", \"signed_lower_numerator\": \"" << signed_decimal(sum_lo)
                  << "\", \"signed_upper_numerator\": \"" << signed_decimal(sum_hi)
                  << "\", \"absolute_lower_numerator\": \"" << decimal(abs_lo)
                  << "\", \"absolute_upper_numerator\": \"" << decimal(abs_hi)
                  << "\"}" << (k < 14 ? ",\n" : "\n");
        old = std::move(next); oldq = q; previous_error = error;
    }
    std::cout << "  ],\n  \"signed_depth_14_positive\": "
              << (positive_at_fourteen ? "true" : "false")
              << ",\n  \"status\": \"" << (positive_at_fourteen ? "PASS" : "FAIL") << "\"\n}\n";
    return positive_at_fourteen ? EXIT_SUCCESS : EXIT_FAILURE;
}
