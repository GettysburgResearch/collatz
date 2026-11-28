#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <vector>

// Integer prefix-deficit recurrence on all units. The optional `limit` is small
// enough that the largest exact child index and q-scaled gap fit in int64_t.
using I = std::int64_t;

std::vector<I> direct(const std::vector<I>& previous, I p, I q) {
  const I old = static_cast<I>(previous.size()), modulus = 3 * old;
  const I largest = *std::max_element(previous.begin(), previous.end());
  std::vector<I> next(modulus, 0);
  for (I x = 1; x < modulus; ++x) {
    if (x % 3 == 0) continue;
    I val = 4 * q + largest;
    I z = x;
    for (I e = 1; e * q - p <= val; ++e) {
      z = 2 * z % modulus;
      if (z % 3 != 1) continue;
      I y = (z - 1) / 3;
      if (y % 3 == 0) continue;
      val = std::min(val, std::max<I>(0, e * q - p + previous[y]));
    }
    next[x] = val;
  }
  return next;
}

std::vector<I> cycle(const std::vector<I>& previous, I p, I q) {
  const I old = static_cast<I>(previous.size()), modulus = 3 * old, period = 2 * old;
  constexpr I inf = I{1} << 40;
  std::vector<I> by_log(period), next(modulus, 0);
  I x = 1;
  for (I d = 0; d < period; ++d) {
    I y = (x - 1) / 3;
    by_log[d] = (x % 3 == 1 && y % 3 != 0) ? previous[y] : inf;
    x = 2 * x % modulus;
  }
  if (x != 1) throw std::runtime_error("log period");
  I best = inf;
  std::vector<I> values(period);
  for (I d = 2 * period - 1; d >= 0; --d) {
    best = std::min(by_log[(d + 1) % period], best) + q;
    if (d < period) values[d] = std::max<I>(0, best - p);
  }
  x = 1;
  for (I d = 0; d < period; ++d) {
    next[x] = values[d];
    x = 2 * x % modulus;
  }
  return next;
}

int main(int argc, char** argv) {
  int limit = argc > 1 ? std::stoi(argv[1]) : 12;
  if (limit < 1 || limit > 14) throw std::invalid_argument("depth out of range");
  for (auto [p,q] : std::array<std::array<I,2>,3>{{{18,11},{5,3},{7,4}}}) {
    std::vector<I> v(3);
    std::array<std::array<I,2>,3> counts{};
    for (int n = 1; n <= limit; ++n) {
      std::vector<I> next = cycle(v, p, q);
      if (n <= 7 && next != direct(v,p,q)) throw std::runtime_error("independent recurrence mismatch");
      for (I x = 1; x < static_cast<I>(next.size()); ++x) {
        if (x % 3 && next[x] < v[x % v.size()]) throw std::runtime_error("non-nested survival");
      }
      v = std::move(next);
      if (n != limit) continue;
      for (I x = 1; x < static_cast<I>(v.size()); ++x) {
        if (x % 3 == 0) continue;
        for (int c=0;c<3;++c) if (v[x] <= c*q) ++counts[c][x%3-1];
      }
    }
    std::cout << "slope " << p << '/' << q << " depth " << limit << " per-trit denominator " << v.size()/3;
    for (int c=0;c<3;++c) std::cout << " credit " << c << ": " << counts[c][0] << ',' << counts[c][1];
    std::cout << '\n';
  }
}
