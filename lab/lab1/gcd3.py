# Euclidean algo O(log(max(m,n)))
# ลดลงทีละครึ่ง เท่ากับประมาณ log2(n) ครั้ง
# if m > n, then GCD(m, n) = GCD(m %n, n) = GCD(m, m %n)
# if m = n, then GCD(m, n) = m = n
# if m< n, thenGCD(m, n) = GCD(m, n %m) = GCD(n %m, n)

import math
import time

def FindGCD3(m : int, n : int) -> int : # recursive until cant be divided anymore
    m = abs(m)
    n = abs(n)
    if(m == 0 and n == 0):
        return 0
    if ( m == 0 or n == 0):
        return max(m,n)
    if m > n: 
        return FindGCD3(m % n, n)
    elif m < n:
        return FindGCD3(m , n % m )
    else:
        return m 
    
    
m = -6
n = -9
start_time = time.perf_counter()
result = FindGCD3(m, n)
end_time = time.perf_counter()

print(f"The GCD of {m} and {n} by Euclidean algo is {result}")
print(f"Time taken: {(end_time - start_time) *1000} milliseconds")