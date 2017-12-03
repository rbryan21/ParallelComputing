# Monte Carlo Calculation of Pi
from random import *
from math import sqrt

def main():
  "Monte Carlo Calculation of Pi"
  inside=0
  n=1000
  for i in range(0, n):
    x=random()
    y=random()
    if sqrt(x*x+y*y)<=1:
      inside+=1
      pi=4*inside/n
      print(pi)

if __name__ == "__main__":
  print(main.__doc__)
  main()

