/************************************************************************
 * This file has been written as a sample solution to an exercise in a
 * course given at the Edinburgh Parallel Computing Centre. It is made
 * freely available with the understanding that every copy of this file
 * must include this header and that EPCC takes no responsibility for
 * the use of the enclosed teaching material.
 * Authors:     Joel Malard, Alan Simpson
 * Contact:     epcc-tec@epcc.ed.ac.uk
 * Contents:    C source code.
 *
 * NOTE:
 * This file has been altered by Asim YarKhan of the Joint Institute for
 * Computational Science (jics@jics.utk.edu) for an MPI workshop.
 ************************************************************************/
/************************************************************************
 * Write an MPI "hello World!" program using the appropriate MPI calls.
 ************************************************************************/

#include        <stdio.h>
#include        <mpi.h>

int main(int argc, char *argv[])
{
  int rank;
  int trials = 100;
  int size = 6;
  double pi_estimates[size];
  MPI_Status status;

  /* Initialize MPI */
  MPI_Init(&argc, &argv);
  
  /* Find out my rank in the global communicator MPI_COMM_WORLD*/
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  /* Insert code to do conditional work if my rank is 0 */
  if(rank == 0){
    
    printf("Hello World (from masternode)\n");
    int i;
    for (i = 1; i < size; i++) {
        MPI_Recv(&pi_estimates[i], 1, MPI_DOUBLE, i, 3, MPI_COMM_WORLD, &status);
        
    }
    /*printf(pi_estimates);   */

  } else {

  /* Insert code to print the output message "Hello World"*/
    int i;
    int count = 0;
    for (i = 0; i < trials; i++) {
        double x = (rand() % 1000) / 1000.0;
        printf("x = %d", x);
        x = x * x;
        if(x > 1){
          count++;
        }
    double pi = 4*count/trials;
    printf("%d\n", pi);
    MPI_Send(&pi, 1, MPI_DOUBLE, 0, 3, MPI_COMM_WORLD);
  }
  
  printf("Hello WORLD!!! (from worker node)\n");

  }
  int pis = 1;
  for(pis = 1; pis < size; pis++) {
    printf("%d", pi_estimates[pis]);
  }

  /* Exit and finalize MPI */
  MPI_Barrier(MPI_COMM_WORLD);
  MPI_Finalize();

  

}/* End Main */
