# Hello World, Version 1
from mpi4py import MPI

def main():
	"Hello World, Version 1"

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	# These are blocking sends
	if rank == 0:
		msgout = "Hello World!"
		for i in range(1,size):
			comm.send(msgout,dest=i,tag=11)
	else:
		msgin = comm.recv(source=0,tag=11)
		print("Node ",rank," out of ",size," says ",msgin)

if __name__ == "__main__":
	#print(main.__doc__)
	main()
