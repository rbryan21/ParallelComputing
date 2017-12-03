# ring
#  A program that will allow a processor to communicate its rank
#  around a ring, the sum of all ranks should be accumulated and printed
#  out by each processor.

from mpi4py import MPI

def main():
	"ring"

	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	# Find out neighbors
	left = rank - 1
	right = rank + 1
	if left < 0:
		left = size - 1
	if right == size:
		right=0

	# Send the process rank stored as val to the process on the right
	# receive a process rank from the process on left and store as tmp
	val = rank
	sum = 0
	while True:
		reqout = comm.issend(val, dest=right, tag=66)
		tmp = comm.recv(source=left,tag=66)
		reqout.wait()
		val = tmp
		sum += val
		if val == rank:
			break

	print("Proc ",rank," Sum = ",sum)

if __name__ == "__main__":
	#print(main.__doc__)
	main()
