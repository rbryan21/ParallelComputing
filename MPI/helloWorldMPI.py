# Hello World, Version 0
from mpi4py import MPI

def main():
	"Hello World, Version 0"
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	print("Hello World from process ", rank)

if __name__ == "__main__":
	print(main.__doc__)
	main()
