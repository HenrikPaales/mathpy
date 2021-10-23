import math
import time

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False
    return n>1

def closestMultiple(n, x):
    if x > n:
        return x
    z = (int)(x / 2)
    n = n + z
    n = n - (n % x)
    return n
piFound = 0
p1 = 3/4
cyc1 = 10000000
start_time = time.time()
for n in range(4, cyc1):
    if isPrime(n):
        p2 = closestMultiple(n, 4)
        p1 = p1 * n/p2
        piFound += 1

calc_pi = p1*4

print("{:.0e}".format(cyc1), " cycles in %s seconds" % round((time.time() - start_time), 2))
print("Real pi: ", math.pi)
print("Calc pi: ", calc_pi)
print("Inaccuracy: ", "{:.1e}".format(((math.pi - calc_pi)/math.pi)*100), "%")

print("primes found: ", piFound)