# Euclidean algo O(log(max(m,n)))
# ลดลงทีละครึ่ง เท่ากับประมาณ log2(n) ครั้ง
# if m > n, then GCD(m, n) = GCD(m %n, n) = GCD(m, m %n)
# if m = n, then GCD(m, n) = m = n
# if m< n, thenGCD(m, n) = GCD(m, n %m) = GCD(n %m, n)

import math
import time

def FindGCD3(*numbers):
    def FindGCD2(a, b):
        a = abs(a)
        b = abs(b)
        if a == 0 and b == 0:
            return 0
        if a == 0 or b == 0:
            return max(a, b)
        while b:
            a, b = b, a % b
        return a
    
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return abs(numbers[0])
    else:
        gcd_result = numbers[0]
        for num in numbers[1:]:
            gcd_result = FindGCD2(gcd_result, num)
        return gcd_result

    
numbers = [189,252,1197,292005]
start_time = time.perf_counter()
result = FindGCD3(*numbers)
end_time = time.perf_counter()

print(f"The GCD of  {', '.join(map(str, numbers))} by Euclidean algo is {result}")
print(f"Time taken: {(end_time - start_time) *1000} milliseconds")