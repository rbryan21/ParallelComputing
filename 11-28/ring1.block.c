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
 * NOTE: This file has been altered by Asim YarKhan of the Joint Institute 
 * for Computational Science (jics@cs.utk.edu) for an MPI workshop.
 ************************************************************************/
/************************************************************************
 * Write a program that will allow a processor to communicate its rank
 * around a ring, the sum of all ranks should be accumulated and printed
 * out by each processor.
 ************************************************************************/

#include	<stdio.h>
#include	<mpi.h>

void main(int argc, char *argv[])
{
  int myrank, size, left, right;
  int val, sum, tmp;
  MPI_Status recv_status, send_status;
  MPI_Request send_request;
  float fval;
  
   /*----------------*/
  /* Initialize MPI */
 /*----------------*/

  MPI_Init(&argc, &argv);

   /*--------------------------------------------------------------------*/
  /* Find out my rank and size using global communicator MPI_COMM_WORLD */
 /*--------------------------------------------------------------------*/

  MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
     
   /*--------------------*/
  /* Find out neighbors */
 /*--------------------*/

  if ((left=(myrank-1)) < 0) left = size-1;
  if ((right=(myrank+1)) == size) right = 0;
  
    /*---------------------------------------------------------------------*/
   /* Send the process rank stored as val to the process on my right and  */
  /* receive a process rank from the process on my left and store as tmp */
 /*---------------------------------------------------------------------*/

  val = myrank;
  fval = (float)myrank;
  sum = 0;
  do {
    //MPI_Issend(&val,1,MPI_INT,right,99,MPI_COMM_WORLD,&send_request);
    MPI_Send(&val,1,MPI_INT,right,99,MPI_COMM_WORLD);
    MPI_Recv(&tmp,1,MPI_INT,left,99,MPI_COMM_WORLD,&recv_status);
    //MPI_Wait(&send_request,&send_status);
    val = tmp;
    sum += val;
  } while (val != myrank);

   /*--------------------------*/
  /* Print the output message */
 /*--------------------------*/

  printf("Proc %d sum = %d \n", myrank, sum);

   /*-----------------------*/
  /* Exit and finalize MPI */
 /*-----------------------*/

  MPI_Finalize();

}
