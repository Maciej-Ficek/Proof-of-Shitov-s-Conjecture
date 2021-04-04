def power_of_GL(n):
    result = 1;
    for i in range(0,n):
        result*=(2**n - 2**i);
    return result;

def number_of_idempotents(n):
    result = 0;
    for r in range(0,n+1):
        result += int(power_of_GL(n)/(power_of_GL(r)*power_of_GL(n-r)));
    return result;

def number_of_nilpotents(n):
    result = 0;
    for j in range(1,n):
        result += 2**(j*(n-j));
    result *= n;
    return result;

decision = bool;
n = int(input());
number_of_all = 2**(n**2);
print(f"idempotents: {number_of_idempotents(n)}");
print(f"nilpotents: {number_of_nilpotents(n)}");
print(f"multiplicity: {number_of_idempotents(n)*number_of_nilpotents(n)}");
print(f"all: {number_of_all}");

decision = number_of_idempotents(n) * number_of_nilpotents(n) < number_of_all;
print(decision);
if decision == True:
    print(f"Shitov's Conjecture is true for {n}");
if decision == False:
    print(f"I don't claim that Shitov's Conjecture is true for {n}");
