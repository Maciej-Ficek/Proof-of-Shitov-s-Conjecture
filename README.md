# Proof-of-Shitov-s-Conjecture
In that program I proved the Shitov's Conjecture about matrix decomposition for some natural numbers. On my PC program works for n smaller than 46 and gives positive answer for n greater than 4 (for smaller the result is already known so it is not a problem).

Shitov's Conjecture says that for all n greater than 7, the matrix ring of square matrices of size nxn with elements in two element field, is nil-clean of degree 4.
It has been proven by Ster that it is nil-clean of degree at most 4.

For given n, my program calculates number of idempotent matrices, nilpotent matrices with degree of nilpotency at most 3, and multiplies them to show that it is smaller than number of all matrices. That means that even if every sum P + Q where P - idempotent and Q - nilpotent is different, then it is impossible for our ring to be nil-clean of degree 3, because there are more matrices than allowed decompositions.

Shitov's paper: https://www.researchgate.net/publication/332630367_The_ring_mathrmM_8k4mathbbZ_2_is_nil-clean_of_index_four
How to compute number of idempotent matrices: https://mathoverflow.net/questions/121717/number-of-idempotent-n-times-n-matrices-over-mathbbz-m-mathbbz
How to compute number of nilpotent matrices: https://math.stackexchange.com/questions/4089063/how-many-matrices-over-two-element-field-are-nilpotent-of-degree-smaller-equal-3
It is obvious that number of all matrices os 2**(n**2).

Program is written in Python 3.
