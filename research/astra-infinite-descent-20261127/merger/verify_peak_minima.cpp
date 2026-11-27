// Verify global first meetings of supplied Mersenne peaks on exact ordinary
// representatives. Compile with C++17, GMP and GMPXX. check_peak_minima.py
// supplies the pinned prices and the row-by-row expected results.
#include <gmpxx.h>
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <tuple>
#include <vector>

struct Word {
    unsigned grade, endpoint, multiplier;
};

using Prices = std::array<int, 81>;
using Result = std::tuple<unsigned, int, unsigned>;  // clock, negative saving, gap
std::array<Word, 65536> words;

void initialize_words() {
    for (unsigned r = 0; r < words.size(); ++r) {
        std::uint64_t x = r;
        unsigned grade = 0, multiplier = 1;
        for (unsigned i = 0; i < 16; ++i) {
            if (x % 2) {
                x = (3 * x + 1) / 2;
                multiplier *= 3;
                ++grade;
            } else {
                x /= 2;
            }
        }
        words[r] = {grade, static_cast<unsigned>(x), multiplier};
    }
}

unsigned step(mpz_class &x) {
    unsigned odd = mpz_odd_p(x.get_mpz_t());
    if (odd) {
        x *= 3;
        ++x;
    }
    x >>= 1;
    return odd;
}

unsigned advance(mpz_class &x, unsigned length) {
    unsigned grade = 0;
    while (length >= 16) {
        const Word &word = words[mpz_get_ui(x.get_mpz_t()) & 65535];
        x >>= 16;
        x *= word.multiplier;
        x += word.endpoint;
        grade += word.grade;
        length -= 16;
    }
    while (length--) grade += step(x);
    return grade;
}

struct Arm {
    mpz_class x;
    int grade, saving;
    unsigned gap;
};

bool arm_order(const Arm &a, const Arm &b) {
    if (a.grade != b.grade) return a.grade < b.grade;
    auto low_a = mpz_get_ui(a.x.get_mpz_t()), low_b = mpz_get_ui(b.x.get_mpz_t());
    if (low_a != low_b) return low_a < low_b;
    if (a.x != b.x) return a.x < b.x;
    if (a.saving != b.saving) return a.saving > b.saving;
    return a.gap < b.gap;
}

unsigned first_in_block(mpz_class upper, int upper_grade, const Arm &arm, unsigned time, unsigned length) {
    mpz_class lower = arm.x;
    int lower_grade = arm.grade;
    for (unsigned i = 1; i <= length; ++i) {
        upper_grade += step(upper);
        lower_grade += step(lower);
        if (upper_grade == lower_grade && upper == lower) return time + i;
    }
    throw std::runtime_error("block and literal first arrival disagree");
}

std::pair<Result, Result> minima(unsigned k, unsigned extra, const Prices &prices) {
    const unsigned q = 18 * k, J = q + 4, H = J + extra;
    const mpz_class modulus = mpz_class(1) << H;
    const mpz_class exponent = (mpz_class(12) << q) - 1;
    if (exponent < 4 * H + 4) throw std::runtime_error("source height guard");
    mpz_class b, three = 3;
    mpz_powm(b.get_mpz_t(), three.get_mpz_t(), exponent.get_mpz_t(), modulus.get_mpz_t());

    mpz_class initial = b - 1;
    const unsigned terminal_grade = advance(initial, H);
    const unsigned max_gap = H - terminal_grade;
    Result any{H + 1, 0, 0}, paid = any;
    const unsigned mod_three = mpz_fdiv_ui(modulus.get_mpz_t(), 3);
    constexpr unsigned width = 256;
    for (unsigned left = 1; left <= max_gap; left += width) {
        const unsigned right = std::min(max_gap, left + width - 1);
        unsigned limit = std::min(H, std::get<0>(paid));
        if (left >= limit) break;
        for (unsigned d = left; d <= right; ++d) {
            const unsigned multiple = (3 - mpz_fdiv_ui(b.get_mpz_t(), 3)) * mod_three % 3;
            mpz_addmul_ui(b.get_mpz_t(), modulus.get_mpz_t(), multiple);
            mpz_divexact_ui(b.get_mpz_t(), b.get_mpz_t(), 3);
        }

        // b = 3^(m-right) mod 2^H. All arms in this block share its upper digits.
        mpz_class upper, power = b;
        mpz_ui_pow_ui(upper.get_mpz_t(), 3, right);
        upper = upper * b - 1;
        int upper_grade = 0;
        std::vector<Arm> arms;
        for (unsigned gap = right; gap >= left; --gap) {
            const int price = prices[((172 - static_cast<int>(gap % 162)) % 162) / 2];
            arms.push_back({power - 1, -static_cast<int>(gap), static_cast<int>(gap) - price, gap});
            power *= 3;
        }

        for (unsigned time = 0; time < limit && !arms.empty();) {
            const unsigned length = std::min(16u, limit - time);
            const mpz_class previous = upper;
            int previous_grade = upper_grade;
            upper_grade += advance(upper, length);
            std::vector<Arm> next;
            for (const Arm &arm : arms) {
                mpz_class x = arm.x;
                int g = arm.grade + static_cast<int>(advance(x, length));
                if (g == upper_grade && x == upper) {
                    const unsigned h = first_in_block(previous, previous_grade, arm, time, length);
                    Result hit{h, -arm.saving, arm.gap};
                    any = std::min(any, hit);
                    if (arm.saving >= 0) paid = std::min(paid, hit);
                    continue;
                }
                // A successful augmented grade must still be reachable at H.
                const int remaining = static_cast<int>(H - time - length);
                if (limit == H && (g > static_cast<int>(terminal_grade) ||
                                   g + remaining < static_cast<int>(terminal_grade))) continue;
                next.push_back({std::move(x), g, arm.saving, arm.gap});
            }
            // At equal endpoint and augmented grade all future arrivals coincide.
            // Ordering preserves the best saving, then the least gap, for a tie.
            std::sort(next.begin(), next.end(), arm_order);
            next.erase(std::unique(next.begin(), next.end(), [](const Arm &a, const Arm &b) {
                return a.grade == b.grade && a.x == b.x;
            }), next.end());
            arms.swap(next);
            time += length;
            limit = std::min(limit, std::get<0>(paid));
        }
    }
    return {any, paid};
}

int main() {
    initialize_words();
    Prices prices;
    for (int &p : prices) if (!(std::cin >> p)) return 2;
    unsigned distinct = 0, max_any = 0, max_paid = 0;
    for (unsigned expected_k = 1; expected_k <= 192; ++expected_k) {
        unsigned k, a, d, p, e;
        int saving, paid_saving;
        if (!(std::cin >> k >> a >> d >> saving >> p >> e >> paid_saving) || k != expected_k) return 2;
        const unsigned J = 18 * k + 4;
        auto [any, paid] = minima(k, p, prices);
        if (any != Result{J + a, -saving, d} || paid != Result{J + p, -paid_saving, e}) {
            std::cerr << "unexpected minimum at k=" << k << "\n";
            return 1;
        }
        distinct += a != p;
        max_any = std::max(max_any, a);
        max_paid = std::max(max_paid, p);
    }
    std::cout << "192 exact minima; distinct paid dates " << distinct
              << "; maximal extras " << max_any << " " << max_paid << "\n";
}
