import time 
from collections import Counter

primeListMemo = []

def FindGCD2(m: int, n: int) -> int:
    if m == 0 and n == 0:
        return 0
    if m == 0 or n == 0:
        return max(m, n)
    
    m_prime = erasPrimeFactor(m)
    print("m_prime : " ,m_prime)
    n_prime = erasPrimeFactor(n)
    print("n_prime : ",n_prime)
    # list of prime factor is sorted in ascending order

    # ลองใช้ Class Counter เป็น dict subclass ที่นับของซ้ำให้ 
    counter_m = Counter(m_prime)
    counter_n = Counter(n_prime)
    common_elements = (counter_m & counter_n) 
    # def __and__ ใน class Counter (เรียกใช้ด้วย &) จะ return ค่าที่ซ้ำกัน เช่น Counter('abbb') & Counter('bcc') => Counter({'b': 1})
    # คือ เอาตัวที่มีร่วมกันที่มีจำนวนน้อยสุด
    commonFactor = list(common_elements.elements())

    # calculate gcd by multiplying all common factor
    gcd = 1 
    for factor in commonFactor:
        gcd *= factor
    return gcd

def erasPrimeFactor(x: int) -> list:
    global primeListMemo  # global ทำให้เวลาเรียกฟังค์ชันซ้ำค่าไม่หายเพราะไม่ใช่ local variable
    if primeListMemo == [] or x > primeListMemo[-1]: # if primeListMemo is empty or next input is larger than prev
        primeList = []  # all prime numbers from 2 to x
        notPrime = [False] * (x + 1)
        for i in range(2, x + 1):
            if notPrime[i]:  # if num is already marked as not prime, continue
                continue
            for j in range(i*2, x + 1, i):  # multiple of i will be set to True starting from next multiple of i; i*2
                notPrime[j] = True
            primeList.append(i)  # append the prime number to the list
            if i not in primeListMemo: # if i is not in primeListMemo before, append it
                primeListMemo.append(i)
    
    index = len(primeListMemo) # ทำให้บรรทัด 53 ทำงานได้กรณี input > primeListMemo ตัวสุดท้าย
    for i, prime in enumerate(primeListMemo): # check that input is smaller than primeListMemo
        if prime > x:
            index = i 
            break

    primeList = primeListMemo[:index] 
    # ถ้า input มีค่ามากกว่า primeListMemo ตัวสุดท้าย(newInput > prevInput นั่นคือ จำนวนเฉพาะต้องมีมากกว่าเดิมที่อยู่ใน primeListMemo) ให้เอา primeListMemo ทั้งหมด
    # แต่ถ้า input ค่าน้อยกว่า จะเอาเฉพาะ prime number ที่น้อยกว่า x มาใช้ (จัดจากของเก่า)
    print("primeList : ",primeList)

    # เอา prime number ทั้งหมด มาหาร x ถ้าหารลงตัวแปลว่าเป็น prime factor ของ x
    primeFactors = []
    for prime in primeList:
        while x % prime == 0:
            primeFactors.append(prime)
            x = x // prime
    print("primeListMemo : " ,primeListMemo)
    return primeFactors 

# main 
m = 30
n = 33
start_time = time.perf_counter()
result = FindGCD2(m, n)
end_time = time.perf_counter()
print(f"The GCD of {m} and {n} by sieve of eras is {result}")

print(f"Time taken: {(end_time - start_time) * 1000} milliseconds")