from collections import Counter
import time

def FindGCD1two(a: int, b: int) -> int: # 2 ตัว
    gcd_ab = calculateGCD(a, b) 
    return gcd_ab

def FindGCD1three(a: int, b: int, c: int) -> int: # 3 ตัว
    gcd_ab = calculateGCD(a, b)
    gcd_abc = calculateGCD(gcd_ab, c)
    return gcd_abc

def FindGCD1four(a: int, b: int, c: int, d: int) -> int: # 4 ตัว
    gcd_ab = calculateGCD(a, b)
    gcd_cd = calculateGCD(c, d)
    gcd_abcd = calculateGCD(gcd_ab, gcd_cd)
    return gcd_abcd

def calculateGCD(m: int, n: int) -> int: # คิด GCD 
    m = abs(m)
    n = abs(n)
    if m == 0 and n == 0:
        return 0
    if m == 0 or n == 0:
        return max(m, n)
    
    m_prime = naivePrimeFactor(m)
    print(m_prime)
    n_prime = naivePrimeFactor(n)
    print(n_prime)
    counter_m = Counter(m_prime)
    counter_n = Counter(n_prime)
    common_elements = (counter_m & counter_n)
    commonFactor = list(common_elements.elements())

    gcd = 1 
    for factor in commonFactor:
        gcd *= factor
    return gcd

def naivePrimeFactor(x: int) -> list:
    factors = []
    divisor = 2
    while x > 1:
            while x % divisor == 0:
                factors.append(divisor)
                x = x // divisor
            divisor += 1
    return factors
    

# main
numbers = [189,252,1197,292005]  
start_time = time.perf_counter()
if len(numbers) == 2:
    result = FindGCD1two(*sorted(numbers,reverse=True))
elif len(numbers) == 3:
    result = FindGCD1three(*sorted(numbers,reverse=True))
elif len(numbers) == 4 :
    result = FindGCD1four(*sorted(numbers,reverse=True))
end_time = time.perf_counter()
print(f"The GCD of {', '.join(map(str, numbers))} by naive method is {result}")
print(f"Time taken: {(end_time - start_time) * 1000} milliseconds")
