# timing
#  A program that sends data back and forth between two processors
#  and calculates timings

from mpi4py import MPI
import numpy as np

def main():
	"timing"

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	MAXLEN = 8000000
	NREPS = 1000

	inmsg = np.zeros(MAXLEN,dtype=np.int8)
	outmsg = np.zeros(MAXLEN,dtype=np.int8)

	msglen = 1

	# Synchronize the processes
	comm.Barrier()

	if rank == 0:
		for i in range(1,5):
			time=0.0
			print("\n\nRound trip test for:")
			print("Message length = ",msglen," integer values")
			print("Message size = ",8*msglen," Bytes")
			print("Number of Reps = ",NREPS)

			start = MPI.Wtime()

			for j in range(1,NREPS+1):
				comm.Send(outmsg[0:msglen],dest=1,tag=77)
				comm.Recv(inmsg,source=1,tag=78)

			finish = MPI.Wtime()
			time = finish - start

			print("Round Trip Avg = ",time/NREPS," Sec")
			bw = 2*NREPS*8.0*msglen/time
			print("*** Bandwidth = ",bw," Bytes/Sec")
			print("***           =  ",bw*8.0/1000000.0," Megabit/Sec")
			msglen = msglen * 100
	
	if rank == 1:
		for i in range(1,5):
			for j in range(1,NREPS+1):
				comm.Recv(inmsg,source=0,tag=77)
				comm.Send(outmsg[0:msglen],dest=0,tag=78)
			msglen = msglen*100

if __name__ == "__main__":
	#print(main.__doc__)
	main()
