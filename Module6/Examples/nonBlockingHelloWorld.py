# Hello World, Version 2

from mpi4py import MPI

def main():
	"Hello World, Version 2"

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	# These are non-blocking sends
	if rank == 0:
		msgout = "Hello World!"
		for i in range(1,size):
			reqout = comm.isend(msgout, dest=i, tag=11)
			reqout.wait()
	else:
		reqin = comm.irecv(source=0, tag=11)
		msgin = reqin.wait()
		print("Node ",rank," out of ",size," says ",msgin)

if __name__ == "__main__":
	#print(main.__doc__)
	main()
