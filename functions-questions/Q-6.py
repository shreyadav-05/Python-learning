#Find Prime Numbers up to N
def primes_up_to(n):
    primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return primes

print(primes_up_to(20))
