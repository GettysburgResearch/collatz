# A primitive modular tour with cyclotomic balance and near-exact winding

Fix a modulus Q≥1 and a jet order k≥0. There are arbitrarily long
cyclic lists of distinct positive ordinary integers n_1,...,n_L, all
prime to 3, with K odd members, satisfying the following properties.
Write c=log₂3, δ=L−cK, and set n_(L+1)=n_1.

* gcd(L,K)=1, 0<δ≪1/L, and T(n_i)≡n_(i+1) modulo Q for every i.
  The cyclic list of parities consequently has least period L.
* The set S of these vertices satisfies exactly the cyclotomic
  divisibility of [the finite jet countermodel](CYCLOTOMIC_MOMENTS.md),
  through order k at all Q-th roots.
* Every n_i is comparable to L/δ, with constants depending on the
  fixed tests. The ordinary winding residual obeys

      |δ log 2 − Σ_(n∈S odd) log(1+1/(3n))| ≪ δ²/L² ≪ L^(−4).

* T does not permute S. In particular some successor equality fails
  as an equality of ordinary integers. The winding bound gives
  approximation; it does not assert exact winding.

The construction can also accommodate tests on a fixed number h of
actual chronological steps: enlarge the working modulus to a multiple
of 2^h Q. Functions of the fixed parity window and residues of those
iterates are then determined by the starting residue. On such a class
each iterate is affine, so polynomials of joint degree ≤k in the
window states are quasipolynomials of degree ≤k. Their one-step flow
equalities telescope through any prescribed finite window by using a
sufficiently large fixed working modulus. Equivalently, if the first
h iterates are requested modulo Q, successive edge errors divisible
by 2^h Q lose at most one binary factor per step, so the same tour
has the prescribed modular consistency throughout that horizon.

## Balanced lists of affine functions with controlled counts

The proof uses the mixed moment pair vectors d(u,v) in the linked
construction. The balance of a finite positive integer combination
of these vectors persists identically in the parameter N on replacing
each term by its affine source v+uN. Its list of sources may be made
distinct using that note's digit-sum partition, with *any* base B
at least the maximum multiplicity and B≥2. Each chosen class has
B^k members, so this operation multiplies the list length and its
odd count by the same B^k.

One may prescribe a rational proportion ρ of odd sources for any
1/2<ρ<1. Append the coordinate 1_(v odd)−ρ to d(u,v).
In the separating-functional proof, this constant coordinate cannot
affect any positive leading degree in u or v. After the same
elimination the sign inequalities have the form

    a_s−a_r+t(1_(r odd)−ρ) ≥ 0.

Summing on the all-odd −1 loop and the ordinary 1→2→1 loop gives
t(1−ρ)≥0 and t(1−2ρ)≥0, forcing t=0. The old cone argument applies
and all data are rational. Any finite designated list of pairs may
be included with positive weight: add their vectors and compensate
its negative from the positive cone before clearing denominators.
In particular, require a representative for every edge of the
strongly connected finite residue graph used in the linked proof.

Take such a first list of distinct affine sources with density 3/5,
with length and odd count v_1=(l_1,k_1), and put g=gcd(l_1,k_1).
We need a second list above the critical odd proportion 1/c with
shape v_2=(l_2,k_2) congruent to (2,1) modulo g. For this, first
produce a *signed* solution to the unaugmented mixed moment system
of shape (2,1). The formal pairs (0,1) and (0,2) give this balance
by the ordinary trivial cycle. For v=1 and v=2 use separately the
integer identity

    d(0,v) = Σ_(j=1)^(k+1) (−1)^(j+1) binom(k+1,j) d(j u_0,v)

with u_0 a positive multiple of twice the working modulus. The
identity is finite-difference interpolation in u, and its integer
coefficients sum to one. Both formal zero velocities are thereby
removed without changing the signed shape.

Add sufficiently many multiples of g times a positive balanced
combination covering all negative pairs, which exists by the cone
argument. Add sufficiently many further multiples of g times a
positive balanced combination of density 2/3. This yields a
positive combination with density strictly above 1/c and shape
(2,1) modulo g. The digit-sum removal with B≡1 (mod g) preserves
that congruence and the density. Hence no prime divides every entry
of both completed vectors v_1,v_2. The vectors have opposite signs
of their drift δ_i=l_i−ck_i and nonzero determinant.

## Coprime positive total shapes

Let α=δ_1/(−δ_2)>0. This number is irrational: a rational value
would give a nonzero rational relation between 1 and c, or would
make v_1 and v_2 proportional. Let C_i=(q_i,p_i) be the adjacent
convergent columns for α, taking infinitely many i with
q_i α−p_i>0. For each such i choose an integer u≥2 in a bounded
range depending only on the prototypes. Put

    (M_1,M_2)=u C_i−C_(i−1),       (L,K)=M_1 v_1+M_2 v_2.

The consecutive columns are unimodular, hence gcd(M_1,M_2)=1.
Their errors have opposite signs, giving M_1 α−M_2>0 and
M_1 α−M_2≪1/q_i. The two counts are positive and comparable to
q_i for large i. It remains to specify u. For a prime p dividing
the absolute determinant of the two v's, the corresponding matrix
has rank one over F_p. Its kernel is a line. If C_i is on this
line, then C_(i−1) is not, and no u gives a bad pair. Otherwise
there is at most one forbidden value of u modulo p. Choose u
avoiding all such values by the Chinese remainder theorem, and lift
to the stated bounded range starting at 2. Outside the determinant
primes the matrix is invertible. No prime now divides both L and
K, and the positive drift is O(1/L).

## Winding and a single tour

Use M_i copies of each fixed prototype, each with its own integer
parameter. Start all parameters in the form R+w, with w chosen
nonnegative of size O(L). Arrange that even after independently
increasing any of the parameters by one, no same-slope lines from
different copies coincide. This is possible greedily: a new shift
has O(1) forbidden differences per previous copy, because each
prototype is fixed and only corrections 0 and 1 are allowed. Within
one copy its original lines of the same slope are already distinct.
For R/L sufficiently large the different positive slopes separate
all the other lines, since there are only finitely many slopes and
the additional offsets are O(L).

With no unit corrections yet, consider the real decreasing function

    F(R)=Σ_(odd lines) log(1+1/(3(v+u(R+w)))).

Uniformly for R≫L this is comparable to L/R; here K is comparable
to L and all prototype constants are fixed. For fixed large enough
L the equation F(R_*)=δ log 2 therefore has a solution R_* comparable
to L/δ, by taking two fixed bounding multiples of L/δ. Positivity
and the derivative bound O(R_*^(-2)) per odd line hold throughout
[R_*−1,R_*+1]. Start at the common floor of R_* and raise individual
copy parameters by one in succession. Each change decreases F by
O(R_*^(-2)) since each copy has bounded size. The two extreme choices
bracket the desired value; stop at one of the adjacent choices at
the crossing. The error is O(R_*^(-2)) as claimed. Each copy still
balances its full jets exactly because a single common parameter is
used throughout that copy.

Treat each distinct ordinary source as a directed edge from its
residue to the residue of its actual successor. Degree-zero balances
give an Eulerian graph, and the first prototype supplies every edge
of the strongly connected working graph. An Euler tour gives the
claimed cyclic ordering. If actual successors permuted the sources,
then each equality would force equality of their leading coefficients
in R: these belong to fixed finite sets, while offsets are O(L) and
R/L tends to infinity. Following a permutation cycle would force a
positive slope to equal itself times 3^w/2^l with l>0, impossible.

The sizes and allowable constants depend on the fixed modulus and
jet order. No prescribed growth rate of the order or modulus with
L, exact product identity, or ordinary cycle follows from this result.
