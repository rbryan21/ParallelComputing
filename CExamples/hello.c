#include <stdio.h>
#include "mpi.h"

main(int argc, char** argv) {
	int my_PE_num;
	MPI_Init(&argc, &argv);
	printf("Hello world \n");
	MPI_Finalize();
}
