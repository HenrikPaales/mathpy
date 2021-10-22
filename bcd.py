import math
import random
import time

def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

def run_cycle(cyc, scale):
    cycles = 0
    oneprime = 0
    print("Progress: ")
    for i in range(1, cyc):
        cycles += 1
        if cycles % (cyc/100) == 0:
            print(int(cycles/(cyc/100)), "%")
        random_nr1 = random.randint(0, scale)
        random_nr2 = random.randint(0, scale)
        if computeGCD(random_nr1, random_nr2) == 1:
            oneprime += 1
    print("100 %")
    ratio = oneprime/cycles
    return math.sqrt(6/ratio)
            
cyc1 = 10**int(input("Cycles: 1e+"))
scale1 = 10**int(input("Range max 1e+"))
print("--- calculating ---")
start_time = time.time()
calc_pi = run_cycle(cyc1, scale1)
print("{:.0e}".format(cyc1), " cycles in %s seconds" % round((time.time() - start_time), 4))
print("Real pi: ", math.pi)
print("Calc pi: ", calc_pi)
print("Inaccuracy: ", "{:.2e}".format(((math.pi - calc_pi)/math.pi)*100), "%")