# Pi Estimation (Blocking)
from mpi4py import MPI
from random import random, seed
from math import sqrt
import numpy as np
import time

np.random.seed(843)
xAndYSize = 1000000;

def main():
	"Pi Estimation (Blocking)"

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	# Master process
	if rank == 0:
		slaveResults = [];
		slaveTimes = [];
		slavePis = [];
		for i in range(1,size):
			x = np.random.uniform(size=xAndYSize)
			y = np.random.uniform(size=xAndYSize)
			# Blocking send
			comm.send([x, y],dest=i,tag=11)
			# Receive elapsed time and estimated pi from slaves
			slaveResults.append(comm.recv(source=i,tag=33))
		# print("\nSlave Result = " + str(slaveResults))
		for result in slaveResults:
			piResult, timeResult = result
			slavePis.append(piResult)
			slaveTimes.append(timeResult)
		f = open("blockingPi.txt", "w")
		f.write("Times = " + str(slaveTimes))
		f.write("\nAverage time = " + str(np.average(slaveTimes)))
		f.write("\nPIs = " + str (slavePis))
		f.write("\nAverage PI = " + str(np.average(slavePis)))
		f.close()
		print("Successfully completed!")
	else:
		x, y = comm.recv(source=0,tag=11)
		start_time = time.time()
		sums = np.sum(x*x + y*y <= 1)
		pi = 4 * sums / xAndYSize
		comm.send([pi, time.time() - start_time], dest=0, tag=33)
if __name__ == "__main__":
	#print(main.__doc__)
	main()
