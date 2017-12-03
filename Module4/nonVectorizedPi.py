# Monte Carlo Calculation of Pi
from random import random, seed
from math import sqrt
import timeit 

def main():
  seed(843)
  inside=0
  nArray=[10,100,1000,10000,100000,1000000]
  f = open("nonVectorizedPi.txt", "w")
  f.write("Monte Carlo Calculation of PI")
  f.write("\n")
  for n in nArray:
    inside = 0
    for i in range(0, n):
      x=random()
      y=random()
      if sqrt(x*x+y*y)<=1:
        inside+=1
    pi=4*inside / n        
    f.write(str(pi))
    f.write("\n")        
  f.close()
  print("Successfully completed.")

if __name__ == "__main__":
  print(main.__doc__)
  print(timeit.timeit(main, number=1))

