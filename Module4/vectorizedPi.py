
# Monte Carlo Calculation of Pi
from random import random, seed
from math import sqrt
import numpy as np
import timeit

def main():
  np.random.seed(843)
  inside=0
  nArray=[10,100,1000,10000,100000,1000000]
  f = open("vectorizedPi.txt", "w")
  f.write("Monte Carlo Calculation of PI")
  pi = []
  for n in nArray:
    x = np.random.uniform(size=n)
    y = np.random.uniform(size=n)
    sums = np.sum(x*x + y*y <= 1)
    pi.append(4 * sums / n)
  f.write("\n")        
  for element in pi:
    f.write(str(element) + "\n")
  f.close()
  print("Successfully completed.")

if __name__ == "__main__":
  print(main.__doc__)
  print(timeit.timeit(main, number=1))

