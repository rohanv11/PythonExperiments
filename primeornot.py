def primeCheck(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

primeCount = 0
for i in range(100, 201):
    sub =  "Prime" if primeCheck(i) else "NonPrime"
    print(f"Number: {i}, Status: {sub}")
    if sub == "Prime":
        primeCount+=1
    
print("Primes numbers count:", primeCount)