# Implementation of the Lennard-Jonnes potential

# E (r, sigma, eps) = 4* eps *((sigma/r)**12-(sigma/r)**6)
from numpy.linalg import norm

def potential_LJ(r, sigma, eps):
    E = 4*eps*((sigma/r)**12-(sigma/r)**6)
    return E

def potential_LJ_shift(r,sigma, eps, R_cutoff=2.5):
    E = potential_LJ(r,sigma,eps) - (4/R_cutoff**12-4/R_cutoff**6)
    return E

def force_LJ(r, sigma, eps):
    norm_r = norm(r)
    f = 48*eps/sigma**2 * ((sigma/norm_r)**14-0.5*(sigma/norm_r)**8)*r
    return f

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    r_vector = np.linspace(0.01, 3, 500)
    eps = 1
    sigma = 1

    potentials = [potential_LJ(r, eps, sigma) for r in r_vector]
    potentials_shift = [potential_LJ_shift(r, eps, sigma) for r in r_vector]
    plt.plot(r_vector, potentials)
    plt.plot(r_vector, potentials_shift)
    plt.xlim([0.0,3.0])
    plt.ylim([-1.5,1.5])
    plt.show()