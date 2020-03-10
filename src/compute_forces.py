# this function computes the forces between two atoms using a given potential
import numpy as np
from src.lj import force_LJ

def compute_forces(Box, Rcutoff):
    N = Box.N # number of atoms
    atoms = Box.atoms
    L = Box.box_size
    DIM = len(L) # number of dimensions, normally 3
    # Rcutoff = Box.cutoff

    f_acc = np.zeros((N,DIM))
    Rij = np.zeros(DIM)
    k = 0

    for i in range(N-1):
        for j in range(i+1,N): #i+1 to N ensures we do not double count
            pos_i = np.array(atoms[i].position)
            pos_j = np.array(atoms[j].position)
            Rij = pos_i-pos_j # distance in box scaled units, coordinates

            # Rij = [coor_i - coor_j for coor_i, coor_j in zip(atoms[i].position, atoms[j].position)] # distance in box scaled units, coordinates

            for l in range(DIM):
                dist = np.abs(Rij[l])
                if dist > L[l]*0.5:
                    Rij[l] = Rij[l]-np.copysign(1, Rij[l]) # unfolds the distance

            Rsqij = np.dot(Rij, Rij)

            if (Rsqij < Rcutoff**2):
                sigma = 1
                eps = 1
                f = force_LJ(Rij, sigma, eps)
                f_acc[i,:] = f_acc[i,:] + f
                f_acc[j,:] = f_acc[j,:] - f
                k = k + 1

    print('Computed %s forces' %k)
    return f_acc

