
# Monte Carlo Calculation of Pi
from random import random, seed
from math import sqrt
from joblib import Parallel, delayed
import multiprocessing
import numpy as np
import time

np.random.seed(843)
nArray = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]
num_cores = 8
inside = 0

def main(i):
  start_time = time.time()
  x = np.random.uniform(size=i)
  y = np.random.uniform(size=i)
  sums = np.sum(x*x + y*y <= 1)
  pi = 4 * sums / i
  return [pi, time.time() - start_time]    

if __name__ == "__main__":
  timeArray = []
  piArray = []
  f = open("vectorizedPi.txt", "w")
  results = Parallel(n_jobs=num_cores)(delayed(main)(i) for i in nArray)
  for element in results:
    pi, time = element
    timeArray.append(time)
    piArray.append(pi)
  f.write("Times = " + str(timeArray))
  f.write("\nTime average = " + str(np.average(timeArray)))
  f.write("\nPIs = " + str(piArray))
  f.write("\nPI average = " + str(np.average(piArray)))
  print("Successfully completed!")
  f.close()

