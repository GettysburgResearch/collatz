// Reproduce the finite top-trit Bellman certificates at precisions 2 through 12.
// Compile with c++ -O2 -std=c++17. No external libraries or stored tables.
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <vector>

using Integer = std::int64_t;
constexpr Integer scale = 1000000000;
constexpr double critical_theta = 0.609089767970671;  // Used only for diagnostics.

void require(bool test, const char* description) {
    if (!test) throw std::runtime_error(description);
}

// Traverse all units by inverse doubling. One complete prior turn of the cycle
// supplies every possible stopping position, including the initial position
// after a positive period. Continuing farther only increases the gap.
template <typename Number>
void minimum_clock(int modulus, const std::vector<Number>& stopping_values,
                   Number one_step, Number infinity, std::vector<Number>& result) {
    const int period = 2 * (modulus / 3);
    Number running = infinity;
    for (int pass = 0; pass < 2; ++pass) {
        int doubled = 1;
        for (int index = 0; index < period; ++index) {
            const int source = (doubled + (doubled % 2) * modulus) / 2;
            const int child = (doubled - 1) / 3;
            if (doubled % 3 == 1 && child % 3 != 0)
                running = std::min(running, stopping_values[child]);
            running += one_step;
            if (pass == 1) result[source] = running;
            doubled = source;
        }
        require(doubled == 1, "inverse doubling failed to traverse one period");
    }
}

std::vector<Integer> propose_bias(int modulus) {
    const int parent_count = modulus / 3;
    std::vector<double> bias(modulus), next(modulus), means(parent_count);
    double residual = 1.0;
    for (int iteration = 0; iteration < 400 && residual > 1e-10; ++iteration) {
        for (int u = 0; u < parent_count; ++u)
            means[u] = (bias[u] + bias[u + parent_count] + bias[u + 2 * parent_count]) / 3;
        minimum_clock(modulus, means, 1.0, 1e12, next);
        residual = 0;
        const double cost = next[1];
        for (int s = 1; s < modulus; ++s) if (s % 3 != 0) {
            const double normalized = next[s] - cost;
            residual = std::max(residual, std::abs(normalized - bias[s]));
            bias[s] = normalized;
        }
    }
    // The rational replay below validates the proposal independently of residual.
    std::vector<Integer> rounded(modulus);
    for (int s = 0; s < modulus; ++s) {
        require(std::isfinite(bias[s]) && std::abs(bias[s]) < 1000, "unsafe bias proposal");
        rounded[s] = std::llround(scale * bias[s]);
    }
    return rounded;
}

std::vector<double> refined_law(const std::vector<double>& parent) {
    const int parent_count = static_cast<int>(parent.size());
    const int modulus = 3 * parent_count, period = 2 * parent_count;
    const double q = 1 - critical_theta;
    std::vector<double> law(modulus);
    double mass = 0;
    for (int pass = 0; pass < 2; ++pass) {
        int doubled = 1;
        for (int index = 0; index < period; ++index) {
            const int s = (doubled + (doubled % 2) * modulus) / 2;
            const double forcing = doubled % 3 == 1 ? parent[(doubled - 1) / 3] : 0;
            mass = critical_theta * forcing + q * mass;
            if (pass == 1) law[s] = mass;
            doubled = s;
        }
        if (pass == 0) mass /= 1 - std::pow(q, period);
    }
    return law;
}

void check_precision(int precision, const std::vector<double>& parent,
                     const std::vector<double>& law) {
    const int modulus = static_cast<int>(law.size()), parent_count = modulus / 3;
    const auto bias = propose_bias(modulus);
    std::vector<Integer> sums(parent_count), bellman(modulus);
    for (int u = 0; u < parent_count; ++u)
        sums[u] = bias[u] + bias[u + parent_count] + bias[u + 2 * parent_count];
    // All three lifts now have an integer potential on denominator 3*scale.
    // Candidate magnitudes are < 1000*scale, and the maximum cycle length
    // in this check is 354294. The signed 64-bit arithmetic stays in range.
    minimum_clock(modulus, sums, 3 * scale, Integer(1) << 60, bellman);
    Integer lower = Integer(1) << 60, upper = -lower, max_oscillation = 0;
    double squared_mean = 0, drift = 0, digit_divergence = 0;
    for (int u = 1; u < parent_count; ++u) if (u % 3 != 0) {
        const Integer triple[] = {bias[u], bias[u + parent_count], bias[u + 2 * parent_count]};
        const auto endpoints = std::minmax_element(triple, triple + 3);
        const Integer oscillation = *endpoints.second - *endpoints.first;
        max_oscillation = std::max(max_oscillation, oscillation);
        squared_mean += parent[u] * std::pow(double(oscillation) / scale, 2);
        for (int lift = 0; lift < 3; ++lift) {
            const int s = u + lift * parent_count;
            const Integer residual = bellman[s] - 3 * bias[s];
            lower = std::min(lower, residual);
            upper = std::max(upper, residual);
            drift += (parent[u] / 3 - law[s]) * bias[s] / scale;
            digit_divergence += law[s] * std::log(3 * law[s] / parent[u]);
        }
    }
    require(upper - lower <= 30, "Bellman bracket wider than 1e-8");
    require(max_oscillation <= 3 * scale, "a proposed top-trit span exceeds three");
    require(lower > 3 * scale && upper < 12 * scale, "cost outside elementary range");
    std::cout << precision << " exact cost interval [" << lower << ',' << upper
              << "]/" << 3 * scale << ", exact max top span " << max_oscillation
              << '/' << scale << ", approximate critical RMS " << std::sqrt(squared_mean)
              << ", drift " << drift << ", digit KL " << digit_divergence << '\n';
}

int main() {
    std::cout << std::setprecision(8);
    const double q = 1 - critical_theta;
    std::vector<double> parent{0, q / (1 + q), 1 / (1 + q)};
    for (int precision = 2; precision <= 12; ++precision) {
        auto law = refined_law(parent);
        check_precision(precision, parent, law);
        parent.swap(law);
    }
}
