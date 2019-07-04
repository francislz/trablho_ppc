#!/usr/bin/env python
from mpi4py import MPI
import numpy as np

def mpi_max(value):

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    intervalo = len(vet)//size
    global_max = np.zeros(1, dtype='float64')
    #local_max = np.max(value).astype('float64')
    local_max = np.max(value[intervalo*rank:intervalo*(rank+1)]).astype('float64')
    #print(rank, local_max)
    MPI.COMM_WORLD.Reduce(local_max, global_max, op=MPI.MAX)
    if (rank==0):
        return global_max

vet = [11, 5, 228, 75, 96, 8, 25, 7]

print(mpi_max(vet))