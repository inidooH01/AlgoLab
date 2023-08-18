import math
import time

def FindGCD1(m : int, n : int) -> int :
    m = abs(m)
    n = abs(n)
    if(m == 0 and n == 0): # gcd(0,0) = 0
        return 0
    
    if ( m == 0 or n == 0): # gcd(0,n) = n 
        return max(m,n)
    
    m_prime =  naivePrimeFactor(m)
    print("Prime factor of m : " , m_prime)
    n_prime = naivePrimeFactor(n)
    print("Prime factor of n : " , n_prime) 
    # list of prime factor is sorted in ascending order

    # check common factor between factor of m and factor of n by intersection of sorted array
    i = j = 0
    commonFactor = []
    while i < len(m_prime) and j < len(n_prime):
        if m_prime[i] == n_prime[j]:
            commonFactor.append(m_prime[i])
            i += 1
            j += 1
        elif m_prime[i] < n_prime[j]:
            i += 1
        else:
            j += 1

    # calculate gcd by multiplying all common factor
    gcd = 1 
    for factor in commonFactor:
        gcd *= factor
    return gcd
  
def naivePrimeFactor(x : int) -> list : # keep dividing until it can't be divided anymore
                                        # เริ่มจาก 2 แปลว่า ทวีคูณของ 2 จะหาร x ไม่ลงแล้ว 
                                        # จะลองหารด้วยทุกค่า 
    factors = []
    divisor = 2
    while x > 1: 
        while x % divisor == 0:
            factors.append(divisor)
            x = x // divisor # make sure that we'll get an int 
        divisor += 1 
    return factors


# main 
m = 450
n = 7743
start_time = time.perf_counter()
result = FindGCD1(m, n)
end_time = time.perf_counter()
print(f"The GCD of {m} and {n} by naive method is {result}")
print(f"Time taken: {(end_time - start_time) * 1000} milliseconds")