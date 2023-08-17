# 15,25 
# 15 -> 5 -> 1 
# gcd(0,n) = n 
# gcd(0,0) = 0
import time

def FindGCD1(m : int, n : int) -> int :
    if(m == 0 and n == 0):
        return 0
    if ( m == 0 or n == 0):
        return max(m,n)
    m_prime =  naivePrimeFactor(m)
    print(m_prime)
    n_prime = naivePrimeFactor(n)
    print(n_prime)
    commonFactor = set(m_prime).intersection(set(n_prime))
    print(commonFactor)
    gcd = 1 
    for factor in commonFactor:
        gcd *= factor
    return gcd

def naivePrimeFactor(x : int) -> list :
    factors = []
    divisor = 2
    while x > 1: 
        while x % divisor == 0:
            factors.append(divisor)
            x = x // divisor # make sure that we'll get an int 
        divisor += 1 
    return factors

m = 2153599
n = 391675650
start_time = time.perf_counter()
result = FindGCD1(m, n)
end_time = time.perf_counter()
print(f"The GCD of {m} and {n} by naive method is {result}")
print(f"Time taken: {(end_time - start_time) * 1000} milliseconds")