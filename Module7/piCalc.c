#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"

#define xAndYSize 1000000

float randomFloat()
{
      float r = (float)rand() / (float)RAND_MAX;
      return r;
}

main(int argc, char** argv) 
{
	int ierr, size, node;
	MPI_Status status;

	float x[xAndYSize];
	float y[xAndYSize];

	ierr = MPI_Init(&argc, &argv);

	/* find out MY process ID, and how many processes were started */
	
	ierr = MPI_Comm_rank(MPI_COMM_WORLD, &node);
	ierr = MPI_Comm_size(MPI_COMM_WORLD, &size);

	// create an array to hold the pi calculations from the slave nodes
	float piCalculations[size - 2];

	float averagePiSum;
	float averagePi;

	// seed random generator
	srand(843);

	// the size of my x and y arrays
	//int xAndYSize = 1000000;

	/*float f = randomFloat();
	float f2 = randomFloat();
	float f3 = randomFloat();
	printf("Random float 1 = %f\nRandom float 2 = %f\nRandom float3 = %f", f, f2, f3);
	*/
	
	// master node
	if ( node == 0 )
	{
		printf("I'm a master node!\n");
		int i;
		
		for (i = 1; i < size; i++) {
			int j;
			for (j = 0; j < xAndYSize; j++) {				
				x[j] = randomFloat();
				y[j] = randomFloat();
			}
			
			// Send x array
			MPI_Send(x, xAndYSize, MPI_FLOAT, i, 123, MPI_COMM_WORLD);
			// Send y array
			MPI_Send(y, xAndYSize, MPI_FLOAT, i, 987, MPI_COMM_WORLD);
		}

		// loop through and receive all of the calculations from the slave nodes
		for (i = 1; i < size; i++) {
			MPI_Recv(&piCalculations[i-1], 1, MPI_FLOAT, i, i, MPI_COMM_WORLD, &status);
		}

		int piCalculationsArrayElementSize = sizeof(piCalculations)/sizeof(piCalculations[0]) + 1;

		// printf("The size of the array is = %d", piCalculationsArrayElementSize);	

		for (i = 0; i < piCalculationsArrayElementSize; i++) {
			// printf("At index %d, the calculation of pi is = %f\n", i, piCalculations[i]);
			averagePiSum += piCalculations[i];			
		}
	
		averagePi = averagePiSum / piCalculationsArrayElementSize;
		printf("The average pi calculation of all nodes is = %f\n", averagePi);

		
	}
	// slave node
	else
	{
		MPI_Recv(&x, xAndYSize, MPI_FLOAT, 0, 123, MPI_COMM_WORLD, &status);
		MPI_Recv(&y, xAndYSize, MPI_FLOAT, 0, 987, MPI_COMM_WORLD, &status);
		
		// declare array to hold sums, needs to be at xAndYSize
		int pi[xAndYSize];
		int i;
		int piCount = 0;
		for (i = 0; i < xAndYSize; i++) {
			float sum = (x[i] * x[i]) + (y[i] * y[i]); 
			if (sum <= 1) {
				piCount = piCount + 1;
			}
		}
//		printf("Count of pi in node %d is %d\n", node, piCount);	
		
		float piCalc = 0;

		piCalc = (4.0 * piCount) / xAndYSize;
	
		// printf("Calculation of pi in node: %d, and piCalc: %f\n", node, piCalc);

		MPI_Send(&piCalc, 1, MPI_FLOAT, 0, node, MPI_COMM_WORLD);
	}

	ierr = MPI_Finalize();
}
