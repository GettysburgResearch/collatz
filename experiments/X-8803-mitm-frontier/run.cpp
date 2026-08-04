#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>

struct Node {
    std::uint64_t residue;
    std::uint64_t endpoint;
};

static std::uint64_t pow_u64(std::uint64_t base, unsigned exp) {
    std::uint64_t out = 1;
    while (exp--) out *= base;
    return out;
}

// Inverse of odd a modulo 2^bits using Newton lifting.
static std::uint64_t inverse_mod_power_of_two(std::uint64_t a, unsigned bits) {
    std::uint64_t x = 1;
    // Each Newton step doubles the number of correct low bits.
    for (unsigned i = 0; i < 6; ++i) x *= (2 - a * x);
    if (bits == 64) return x;
    return x & ((std::uint64_t{1} << bits) - 1);
}

static std::vector<Node> frontier(unsigned depth) {
    std::vector<Node> nodes;
    nodes.push_back({0, 0});
    std::uint64_t pow4 = 1;
    std::uint64_t pow5 = 1;
    for (unsigned level = 0; level < depth; ++level) {
        std::vector<Node> next;
        next.resize(nodes.size() * 2);
        for (std::size_t i = 0; i < nodes.size(); ++i) {
            const auto r = nodes[i].residue;
            const auto y = nodes[i].endpoint;
            const std::uint64_t ym = y & 3u;
            const std::uint64_t t0 = (0u - ym) & 3u;
            const std::uint64_t t1 = (3u - ym) & 3u;
            const std::uint64_t z0 = y + pow5 * t0;
            const std::uint64_t z1 = y + pow5 * t1;
            next[2*i] = {r + pow4 * t0, (5*z0 + 3)/4};
            next[2*i+1] = {r + pow4 * t1, (5*z1 + 3)/4};
        }
        nodes.swap(next);
        pow4 *= 4;
        pow5 *= 5;
    }
    return nodes;
}

static std::pair<unsigned,std::string> simulate(std::uint64_t x, unsigned cap) {
    std::string digits;
    for (unsigned k = 0; k < cap; ++k) {
        const auto r = x & 3u;
        if (r != 0 && r != 3) return {k, digits};
        const auto b = (0u - r) & 3u;
        digits.push_back(static_cast<char>('0' + b));
        x = (5*x + 3)/4;
    }
    return {cap, digits};
}

int main(int argc, char** argv) {
    unsigned depth = 50;
    if (argc > 1) depth = static_cast<unsigned>(std::stoul(argv[1]));
    if (depth != 50) {
        std::cerr << "X-8803 is frozen at target depth 50\n";
        return 2;
    }
    const unsigned h = depth/2;
    const unsigned m = depth-h;
    const unsigned bits = 2*m;
    const std::uint64_t modulus = std::uint64_t{1} << bits;
    const std::uint64_t mask = modulus - 1;
    const std::uint64_t H = std::uint64_t{1} << (2*h);

    auto left = frontier(h);
    auto right_nodes = frontier(m);
    std::vector<std::uint64_t> target;
    target.reserve(right_nodes.size());

    const std::uint64_t five_h = pow_u64(5, h);
    const std::uint64_t inv = inverse_mod_power_of_two(five_h, bits);
    if (((five_h * inv) & mask) != 1) {
        std::cerr << "modular inverse self-check failed\n";
        return 3;
    }
    for (const auto& node : right_nodes) target.push_back((node.residue * inv) & mask);
    right_nodes.clear();
    right_nodes.shrink_to_fit();
    std::sort(target.begin(), target.end());
    if (std::adjacent_find(target.begin(), target.end()) != target.end()) {
        std::cerr << "transformed right frontier is not injective\n";
        return 4;
    }

    std::uint64_t best_t = std::numeric_limits<std::uint64_t>::max();
    std::uint64_t best_r = std::numeric_limits<std::uint64_t>::max();

    for (const auto& node : left) {
        const std::uint64_t c = (node.endpoint * inv) & mask;
        auto it = std::lower_bound(target.begin(), target.end(), c);
        std::uint64_t t;
        if (it == target.end()) t = target.front() + modulus - c;
        else t = *it - c;

        if (t == 0 && node.residue == 0) {
            // Exclude the all-zero root and move to the next transformed class.
            auto jt = std::upper_bound(target.begin(), target.end(), c);
            if (jt == target.end()) t = target.front() + modulus - c;
            else t = *jt - c;
        }

        if (t < best_t || (t == best_t && node.residue < best_r)) {
            best_t = t;
            best_r = node.residue;
        }
    }

    if (best_t > (std::numeric_limits<std::uint64_t>::max() - best_r) / H) {
        std::cerr << "minimum root exceeds uint64 verification range\n";
        return 5;
    }
    const std::uint64_t root = best_t * H + best_r;
    auto [survival, word] = simulate(root, depth+1);
    if (survival != depth) {
        std::cerr << "minimum-root replay failed: got depth " << survival << "\n";
        return 6;
    }
    std::uint64_t exit_state = root;
    for (unsigned i=0;i<depth;++i) exit_state=(5*exit_state+3)/4;
    const auto exit_digit = ((0u - (exit_state & 3u)) & 3u);

    // Directly audit the left frontier's least positive representative.
    std::uint64_t left_min = std::numeric_limits<std::uint64_t>::max();
    for (const auto& node : left) if (node.residue > 0) left_min = std::min(left_min,node.residue);

    std::cout << "{\n"
              << "  \"experiment_id\": \"X-8803\",\n"
              << "  \"classification\": \"EXACT_FINITE_COMPUTATION\",\n"
              << "  \"target_depth\": " << depth << ",\n"
              << "  \"split_depths\": [" << h << ", " << m << "],\n"
              << "  \"left_frontier_size\": " << left.size() << ",\n"
              << "  \"right_frontier_size\": " << target.size() << ",\n"
              << "  \"left_depth_least_positive_root\": " << left_min << ",\n"
              << "  \"least_positive_root\": " << root << ",\n"
              << "  \"least_positive_A_seed\": " << (root-1) << ",\n"
              << "  \"composition_quotient\": " << best_t << ",\n"
              << "  \"composition_residue\": " << best_r << ",\n"
              << "  \"verified_survival_depth\": " << survival << ",\n"
              << "  \"bottom_digit_prefix\": \"" << word << "\",\n"
              << "  \"first_forbidden_digit\": " << exit_digit << ",\n"
              << "  \"first_forbidden_state\": " << exit_state << ",\n"
              << "  \"claim_boundary\": \"This proves termination through depth 50 below the displayed root; it does not prove global termination.\"\n"
              << "}\n";
    return 0;
}
