from unicodedata import numeric

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(numbers[2], len(numbers)+1):
    for j in range(2, i):
        if i % j == 0:
            primes.append(i)
            break

        
    else:
        not_primes.append(i)
print("not_primes", not_primes)
print("primes", primes)
