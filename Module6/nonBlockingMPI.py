# Pi Estimation (Non-Blocking)
from mpi4py import MPI
from random import random, seed
from math import sqrt
import numpy as np
import time

np.random.seed(843)
xAndYSize = 10000

def main():
	"Pi Estimation (Blocking)"

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	# Master process
	if rank == 0:
		slaveResults = []
		slaveTimes = []
		slavePis = []
		for i in range(1,size):
			x = np.random.uniform(size=xAndYSize)
			y = np.random.uniform(size=xAndYSize)
			# Non-Blocking send
			print("X type = " + str(type( x ) ))
			reqout = comm.isend([x, y], dest=i,tag=11)
			reqout.wait()
			# Receive elapsed time and estimated pi from slaves
			print("Request out from master " + " = " + str(reqout))
			response = comm.recv(source=i,tag=33)
			print("Request from child node " + str(i) + " received!")
			slaveResults.append(response)
		print("\nSlave Result = " + str(slaveResults))
		for result in slaveResults:
			piResult, timeResult = result
			slavePis.append(piResult)
			slaveTimes.append(timeResult)
		f = open("nonBlockingPi.txt", "w")
		f.write("Times = " + str(slaveTimes))
		f.write("\nAverage time = " + str(np.average(slaveTimes)))
		f.write("\nPIs = " + str (slavePis))
		f.write("\nAverage PI = " + str(np.average(slavePis)))
		f.close()
		print("Successfully completed!")
	else:
		# response = comm.recv(source=0,tag=11)
		reqin = comm.irecv(source=0,tag=11)
		response = reqin.wait()
		# print("Request received in node " + str(rank))
		
		print("Request in at node " + str(rank) + " = " + str(response))
		x, y = response
		start_time = time.time()
		sums = np.sum(x*x + y*y <= 1)
		pi = 4 * sums / xAndYSize
		print("Pi " + str(type(float(pi))))
		reqout = comm.isend([pi, time.time() - start_time], dest=0, tag=33)
		reqout.wait()
if __name__ == "__main__":
	#print(main.__doc__)
	main()
