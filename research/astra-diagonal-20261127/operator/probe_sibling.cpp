// Exploratory floating-point scan, not a proof certificate.
// The same authentic ternary row is used for both members of every pair.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

int main(int argc, char **argv) {
  const int last = argc > 1 ? std::stoi(argv[1]) : 15;
  std::vector<double> previous(1, 1.0);
  std::uint64_t oldq = 1;
  std::cout << "{\"status\":\"exploratory_float_only\",\"rows\":[\n";
  for (int n = 1; n <= last; ++n) {
    const auto q = oldq * 3, length = 2 * oldq;
    std::vector<std::uint32_t> orbit(length);
    std::vector<double> value(length), row(q, 0.0);
    std::uint64_t y = 1;
    for (std::uint64_t i = 0; i < length; ++i) {
      orbit[i] = static_cast<std::uint32_t>(y);
      value[i] = y % 3 == 2 ? 1.5 * previous[((2 * y - 1) / 3) % oldq] : 0.0;
      y = 2 * y % q;
    }
    // Solve v_i = a_i + v_(i+1)/2 around the finite doubling cycle.
    // Two sweeps suffice beyond 54 bits; repeat small cycles longer.
    double tail = 0.0;
    const int sweeps = static_cast<int>(std::max<std::uint64_t>(2, 110 / length + 1));
    for (int sweep = 0; sweep < sweeps; ++sweep) {
      for (std::uint64_t i = length; i-- > 0;) {
        tail = value[i] + 0.5 * tail;
        row[orbit[i]] = tail;
      }
    }
    double minimum = std::numeric_limits<double>::infinity();
    double raw = 1.0, max_error = 0.0, mean = 0.0;
    std::uint64_t arg = 0, sibling = 0;
    double arg_rho = 0.0, arg_side = 0.0;
    for (std::uint64_t x = 0; x < q; ++x) {
      mean += row[x];
      const double a = x % 3 == 2 ? 1.5 * previous[((2*x - 1)/3)%oldq] : 0.0;
      max_error = std::max(max_error, std::abs(row[x] - a - 0.5*row[2*x%q]));
    }
    for (std::uint64_t x = 1; x < 2*q; x += 2) {
      const double rho = row[x%q];
      if (rho <= 0.0) continue;
      std::uint64_t b = 4*x+1;
      if (b%3 == 0) b = 16*x+5;
      const double side = row[b%q];
      const double score = side*static_cast<double>(x)/(rho*rho);
      raw = std::min(raw, side/rho);
      if (score < minimum) {
        minimum = score; arg = x; sibling = b; arg_rho = rho; arg_side = side;
      }
    }
    std::cout << (n == 1 ? "" : ",\n") << std::setprecision(17)
              << "{\"n\":" << n << ",\"q\":" << q
              << ",\"min_side_times_y_over_rho_squared\":" << minimum
              << ",\"arg_y\":" << arg << ",\"sibling\":" << sibling
              << ",\"rho\":" << arg_rho << ",\"side\":" << arg_side
              << ",\"min_raw_ratio\":" << raw
              << ",\"mean_density\":" << mean/q
              << ",\"max_recurrence_error\":" << max_error << "}" << std::flush;
    previous = std::move(row); oldq = q;
  }
  std::cout << "\n]}\n";
}
