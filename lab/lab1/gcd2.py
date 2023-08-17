import time 
primeFactorMemo = {}

def FindGCD2(m : int, n : int) -> int :
    if(m == 0 and n == 0):
        return 0
    if ( m == 0 or n == 0):
        return max(m,n)
    m_prime =  erasPrimeFactor(m)
    print(m_prime)
    n_prime = erasPrimeFactor(n)
    print(n_prime)
    commonFactor = set(m_prime).intersection(set(n_prime))
    print(commonFactor)
    gcd = 1 
    for factor in commonFactor:
        gcd *= factor
    return gcd

def erasPrimeFactor(x : int) -> list :
    primeList = [] # all prime numbers from 2 to x
    notPrime = [False] * (x+1)
    for i in range(2, x+1):
        if notPrime[i] == True: # if num is already marked as not prime, continue
            continue
        for j in range(i*2, x+1, i): # multiple of i will be set to True starting from next multiple of i; i*2
            notPrime[j] = True
        primeList.append(i) # append the prime number to the list
    primeFactors= []
    for prime in primeList:
        while x % prime == 0:
            primeFactors.append(prime)
            x //= prime
        if x == 1:
            break
    primeFactorMemo[x] = primeFactors

    return primeFactors
    
m = 21535
n = 39165
start_time = time.perf_counter()
result = FindGCD2(m, n)
end_time = time.perf_counter()
print(f"The GCD of {m} and {n} by sieve of eras is {result}")

print(f"Time taken: {(end_time - start_time) * 1000} milliseconds")