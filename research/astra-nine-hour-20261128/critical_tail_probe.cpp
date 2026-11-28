// Exact finite counts at the proposed deterministic critical clock.
// This is an arithmetic probe, not an asymptotic proof or a Collatz verifier.
#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

struct Row {
  std::uint64_t cutoff;
  unsigned clock, deficit;
  std::uint64_t lower_count = 0, reached_one = 0;
  std::uint64_t direct_checksum = 0, block_checksum = 0;
};

std::uint64_t odd_image(std::uint64_t x) {
  if (x > (std::numeric_limits<std::uint64_t>::max() - 1) / 3)
    throw std::overflow_error("ordinary orbit exceeds uint64 range");
  return (3*x+1)/2;
}

unsigned direct_count(std::uint64_t n, unsigned t, bool &hit) {
  unsigned q = 0;
  hit = n == 1;
  for (unsigned i=0; i<t; ++i) {
    if (n == 1) { hit = true; return q + (t-i+1)/2; }
    if (n & 1) { ++q; n = odd_image(n); }
    else n >>= 1;
    hit = hit || n == 1;
  }
  return q;
}

unsigned block_count(std::uint64_t n, unsigned t) {
  unsigned q = 0;
  while (t) {
    if (n == 1) return q + (t+1)/2;
    if (!(n & 1)) {
      const unsigned e = std::min<unsigned>(t, std::countr_zero(n));
      n >>= e; t -= e;
    } else {
      n = odd_image(n); --t; ++q;
    }
  }
  return q;
}

int main(int argc, char **argv) {
  try {
    const bool dual = argc == 2 && std::string(argv[1]) == "--dual";
    if (argc > 2 || (argc == 2 && !dual))
      throw std::invalid_argument("only optional argument is --dual");
    std::vector<Row> rows;
    std::uint64_t x;
    unsigned t, a;
    while (std::cin >> x >> t >> a) {
      if (!x || !t || a*a < t || (a && (a-1)*(a-1) >= t))
        throw std::invalid_argument("invalid cutoff, clock or exact square-root ceiling");
      rows.push_back({x,t,a});
    }
    if (rows.empty()) throw std::invalid_argument("no rows supplied");
    std::cout << "{\"scope\":\"exact bounded ordinary-source parity counts; no asymptotic inference\",\"dual\":"
              << (dual ? "true" : "false") << ",\"rows\":[";
    bool first = true;
    for (auto &r : rows) {
      for (std::uint64_t n=1; n<=r.cutoff; ++n) {
        bool hit = false;
        const unsigned q = direct_count(n,r.clock,hit);
        const bool lower = 2*q <= r.clock && r.clock - 2*q >= r.deficit;
        r.lower_count += lower;
        r.reached_one += hit;
        r.direct_checksum += n * (q+1);
        if (dual) {
          const unsigned qb = block_count(n,r.clock);
          if (qb != q) throw std::runtime_error("independent run-block count disagrees");
          r.block_checksum += n * (qb+1);
        }
      }
      if (!first) std::cout << ',';
      first = false;
      std::cout << "{\"cutoff\":" << r.cutoff << ",\"clock\":" << r.clock
                << ",\"deficit_ceiling\":" << r.deficit << ",\"lower_count\":" << r.lower_count
                << ",\"reached_one_by_clock\":" << r.reached_one
                << ",\"direct_checksum_mod_2_64\":" << r.direct_checksum;
      if (dual) std::cout << ",\"block_checksum_mod_2_64\":" << r.block_checksum;
      std::cout << '}';
      std::cerr << "completed cutoff " << r.cutoff << '\n';
    }
    std::cout << "]}\n";
    return 0;
  } catch (const std::exception &e) {
    std::cerr << e.what() << '\n'; return 1;
  }
}
