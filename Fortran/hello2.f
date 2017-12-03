        PROGRAM hello
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C
C This file has been written as a sample solution to an exercise in a 
C course given at the Edinburgh Parallel Computing Centre. It is made
C freely available with the understanding that every copy of this file
C must include this header and that EPCC takes no responsibility for
C the use of the enclosed teaching material.
C Authors:    Alan Simpson, Joel Malard
C Contact:    epcc-tec@epcc.ed.ac.uk
C
C NOTE:        
C This file has been altered by Asim YarKhan of the Joint Institute for
C Computational Science (jics@cs.utk.edu) for an MPI workshop.
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

      IMPLICIT NONE

      include "mpif.h"

      INTEGER ierror, rank, size, i, tag
      CHARACTER*12 message, inmsg
      INTEGER status(MPI_STATUS_SIZE)

C  *------------------->
C *---> Initialize MPI
C  *------------------->

      CALL MPI_INIT(ierror)

C  *--------------------------------------------------------------->
C *---> Find out my rank in the global communicator MPI_COMM_WORLD
C  *--------------------------------------------------------------->

      CALL MPI_COMM_RANK(MPI_COMM_WORLD, rank, ierror)

C  *------------------------------------------------------------>
C *---> Find out size of the global communicator MPI_COMM_WORLD
C  *------------------------------------------------------------>

      CALL MPI_COMM_SIZE(MPI_COMM_WORLD, size, ierror)

C  *----------------------------------------------------------------->
C *---> If I am the MASTER send the "hello world" message, else
C *---> if I am a WORKER receive and print the "hello world" message
C  *----------------------------------------------------------------->

      tag = 17
      IF (rank .EQ. 0) THEN
        message = 'Hello World!'
        DO i=1,size-1
          CALL MPI_SEND(message, 12, MPI_CHARACTER, i, tag,
     +                  MPI_COMM_WORLD, ierror)
        ENDDO
      ELSE
        CALL MPI_RECV(inmsg, 12, MPI_CHARACTER, 0, tag,
     +                MPI_COMM_WORLD, status, ierror)
        WRITE(*,*) 'Process ',rank, ': ',inmsg
      ENDIF
        
C  *-------------------------->
C *---> Exit and finalize MPI
C  *-------------------------->

      CALL MPI_FINALIZE(ierror)

      STOP
      END
