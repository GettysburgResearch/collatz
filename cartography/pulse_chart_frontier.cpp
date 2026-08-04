#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using u128 = __uint128_t;

struct BestRow {
  bool set = false;
  u128 value = 0;
  std::uint64_t word = 0;
  int exponent = 0;
};

static int max_depth = 31;
static std::vector<BestRow> best;

static std::string to_decimal(u128 x) {
  if (x == 0) return "0";
  std::string out;
  while (x != 0) {
    out.push_back(static_cast<char>('0' + x % 10));
    x /= 10;
  }
  std::reverse(out.begin(), out.end());
  return out;
}

static std::string word_bits(std::uint64_t w, int depth) {
  std::string s;
  s.reserve(depth);
  for (int j = depth - 1; j >= 0; --j) {
    s.push_back(((w >> j) & 1U) ? '1' : '0');
  }
  return s;
}

static std::uint64_t inverse_odd(std::uint64_t a, std::uint64_t modulus) {
  for (std::uint64_t x = 1; x < modulus; x += 2) {
    if ((a * x) % modulus == 1) return x;
  }
  throw std::runtime_error("odd inverse not found");
}

// Invariant at depth d:
//   every initial integer in this cylinder is x_0 = R + 2^E q;
//   after d chart steps, x_d = a + 9^d q.
static void visit(int depth, u128 R, int E, u128 a, u128 pow9,
                  std::uint64_t word) {
  if (depth > 0) {
    const u128 least_positive = (R == 0) ? (u128{1} << E) : R;
    BestRow &row = best.at(depth);
    if (!row.set || least_positive < row.value) {
      row = {true, least_positive, word, E};
    }
  }
  if (depth == max_depth) return;

  for (int epsilon = 0; epsilon <= 1; ++epsilon) {
    const int digit_bits = 3 + epsilon;
    const std::uint64_t modulus = std::uint64_t{1} << digit_bits;
    const std::uint64_t coefficient =
        static_cast<std::uint64_t>((pow9 * 9) % modulus);
    const std::uint64_t rhs =
        static_cast<std::uint64_t>((9 * a + epsilon) % modulus);
    const std::uint64_t q0 =
        ((modulus - rhs) % modulus * inverse_odd(coefficient, modulus)) %
        modulus;

    const u128 R_next = R + (u128{q0} << E);
    const u128 a_next = (9 * (a + pow9 * q0) + epsilon) >> digit_bits;
    visit(depth + 1, R_next, E + digit_bits, a_next, pow9 * 9,
          (word << 1) | static_cast<std::uint64_t>(epsilon));
  }
}

static int chart_step(u128 x, u128 &next) {
  if (x % 8 == 0) {
    next = 9 * x / 8;
    return 0;
  }
  if (x % 16 == 7) {
    next = (9 * x + 1) / 16;
    return 1;
  }
  return -1;
}

int main(int argc, char **argv) {
  if (argc > 1) max_depth = std::stoi(argv[1]);
  if (max_depth < 1 || max_depth > 31) {
    std::cerr << "max_depth must lie in [1,31]\n";
    return 2;
  }

  best.assign(max_depth + 1, BestRow{});
  visit(0, 0, 0, 0, 1, 0);

  const BestRow &last = best.at(max_depth);
  u128 x = last.value;
  int exact_survival = 0;
  u128 next = 0;
  while (chart_step(x, next) >= 0) {
    ++exact_survival;
    x = next;
  }

  const u128 physical_n = 42 * last.value - 5;
  const u128 words_checked = (u128{1} << (max_depth + 1)) - 2;

  std::cout << "{\n";
  std::cout << "  \"schema\": \"collatz.cartography.pulse-chart-frontier.v1\",\n";
  std::cout << "  \"max_depth\": " << max_depth << ",\n";
  std::cout << "  \"finite_words_checked\": \"" << to_decimal(words_checked)
            << "\",\n";
  std::cout << "  \"rows\": [\n";
  for (int d = 1; d <= max_depth; ++d) {
    const BestRow &row = best.at(d);
    std::cout << "    {\"depth\": " << d << ", \"least_x\": \""
              << to_decimal(row.value) << "\", \"modulus_bits\": "
              << row.exponent << ", \"word_bits\": \""
              << word_bits(row.word, d) << "\"}";
    std::cout << (d == max_depth ? "\n" : ",\n");
  }
  std::cout << "  ],\n";
  std::cout << "  \"depth_max_least_x\": \"" << to_decimal(last.value)
            << "\",\n";
  std::cout << "  \"depth_max_physical_n\": \"" << to_decimal(physical_n)
            << "\",\n";
  std::cout << "  \"least_x_exact_survival_depth\": " << exact_survival
            << ",\n";
  std::cout << "  \"first_illegal_x\": \"" << to_decimal(x) << "\"\n";
  std::cout << "}\n";
  return 0;
}
