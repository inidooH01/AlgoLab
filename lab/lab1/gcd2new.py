import time
from collections import Counter
import math

primeListMemo = []
prevInput = None

def FindGCD3two(a: int, b: int) -> int: # 2 ตัว
    gcd_ab = calculateGCD(a, b) 
    return gcd_ab

def FindGCD3three(a: int, b: int, c: int) -> int: # 3 ตัว
    gcd_ab = calculateGCD(a, b)
    gcd_abc = calculateGCD(gcd_ab, c)
    return gcd_abc

def FindGCD3four(a: int, b: int, c: int, d: int) -> int: # 4 ตัว
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
    
    m_prime = erasPrimeFactor(m)
    print(m_prime)
    n_prime = erasPrimeFactor(n)
    print(n_prime)
    counter_m = Counter(m_prime)
    counter_n = Counter(n_prime)
    common_elements = (counter_m & counter_n)
    commonFactor = list(common_elements.elements())

    gcd = 1 
    for factor in commonFactor:
        gcd *= factor
    return gcd

def erasPrimeFactor(x: int) -> list:  # ทำ sieve of eras แล้วหา prime factor
    global primeListMemo
    global prevInput
    
    primeList = []
    Prime = [True] * (x + 1)
    for i in range(2, x+1):
            if Prime[i] == False:
                continue
            for j in range(i * 2, x + 1, i):
                Prime[j] = False
            primeList.append(i)
            if i not in primeListMemo:
                primeListMemo.append(i)
    index = len(primeListMemo)
    for i, prime in enumerate(primeListMemo):
        if prime > x:
            index = i 
            break

    primeList = primeListMemo[:index]

    primeFactors = []
    for prime in primeList:
        while x % prime == 0:
            primeFactors.append(prime)
            x = x // prime
            
    prevInput = x
    return primeFactors 

# main
numbers = [189,252,1197,292005]  
start_time = time.perf_counter()
if len(numbers) == 2:
    result = FindGCD3two(*sorted(numbers,reverse=True))
elif len(numbers) == 3:
    result = FindGCD3three(*sorted(numbers,reverse=True))
elif len(numbers) == 4 :
    result = FindGCD3four(*sorted(numbers,reverse=True))
end_time = time.perf_counter()
print(f"The GCD of {numbers} by sieve of eras is {result}")
print(f"Time taken: {(end_time - start_time) * 1000} milliseconds")
